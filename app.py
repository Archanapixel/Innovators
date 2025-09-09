from flask import flask
from main import generatorAI
import pickle

generateAI()
ai=pickle.load(open('ai.pkl','rb'))
app=Flask(__name__)


@app.route("/")
 def homepage():
    return"Server Running"


@app.route("/predict")
def predict():
    ir=request.args.get('ir')
    ir=int(ir)
    data=[[ir]]
    result=ai.predict(data)
    return result
if(__name__)=="__main.py__":

    app.run(host='0.0.0.0',port=3000)
