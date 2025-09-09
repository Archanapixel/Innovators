from flask import Flask, request
from main import generatorAI
import pickle

# Run your AI generator function (if needed)
generatorAI()

# Load the trained model
ai = pickle.load(open('ai.pkl', 'rb'))

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def homepage():
    return "Server Running"

@app.route("/predict")
def predict():
    ir = request.args.get('ir')   # Get input parameter
    ir = int(ir)
    data = [[ir]]
    result = ai.predict(data)
    return str(result[0])   # Convert NumPy/prediction result to string

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
