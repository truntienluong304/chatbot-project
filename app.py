import os
import torch
from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel, PeftConfig, prepare_model_for_kbit_training

app = Flask(__name__)

# Environment setup
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
MODEL_NAME = "HuggingFaceH4/zephyr-7b-beta"
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16
)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    trust_remote_code=True,
    quantization_config=bnb_config
)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token
model.gradient_checkpointing_enable()
model = prepare_model_for_kbit_training(model)

# Load the fine-tuned model with PEFT
peft_config = PeftConfig.from_pretrained("trungtienluong/experiments500czephymodelngay11t6l1")
model = PeftModel.from_pretrained(model, "trungtienluong/experiments500czephymodelngay11t6l1")

# Move model to appropriate device
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    question = data.get('question', '')
    
    inputs = tokenizer(question, return_tensors='pt').to(device)
    outputs = model.generate(**inputs)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
