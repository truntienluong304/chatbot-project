const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const { pipeline } = require('transformers');

const app = express();
const port = 3000;

app.use(bodyParser.json());

// Serve static files from the React app
app.use(express.static(path.join(__dirname, 'new-frontend/build')));

// Load the model from Hugging Face
const qaPipeline = pipeline('question-answering', {
    model: 'trungtienluong/experiments500czephymodelngay11t6l2',
    tokenizer: 'trungtienluong/experiments500czephymodelngay11t6l2'
});

app.post('/api/ask', async (req, res) => {
    const { question } = req.body;

    try {
        const response = await qaPipeline({
            question: question,
            context: 'Your context here if needed' // Thêm context nếu cần
        });
        res.json({ answer: response.answer });
    } catch (error) {
        console.error('Error fetching the answer:', error);
        res.status(500).json({ error: 'Error fetching data from the chatbot' });
    }
});

// The "catchall" handler: for any request that doesn't
// match one above, send back React's index.html file.
app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'new-frontend/build', 'index.html'));
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
