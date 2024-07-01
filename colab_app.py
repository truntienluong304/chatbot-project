from colabcode import ColabCode
import subprocess

# Run the Flask server
subprocess.Popen(["python", "app.py"])

# Start ColabCode server to expose the Flask app
ColabCode(port=5000, code=False)
