# Flask app.py corrections
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics
import warnings
import pickle
warnings.filterwarnings('ignore')
from feature import FeatureExtraction

file = open("models/phishing_rf.pkl", "rb")
savedmodel = pickle.load(file)
file.close()

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def index():
   
    url = ""
    safe_probability = -1
    
    if request.method == "POST":
        url = request.form["url"]
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1, 30)
        
       
        prediction_probabilities = savedmodel.predict_proba(x)[0]
        safe_probability = prediction_probabilities[1] 
        
       
        print(f"URL: {url}, Safety Score: {safe_probability}")
        
    
    return render_template('index.html', xx=safe_probability, url=url)

if __name__ == "__main__":
    app.run(debug=True)