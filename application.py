from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application=Flask(__name__)
app=application


ridge_model=pickle.load(open("models/ridge.pkl","rb"))
standard_scaler=pickle.load(open("models/scaler.pkl","rb"))

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/predictdata",methods=['POST','GET'])
def predict_datapoint():
  if request.method=="POST":
    # get form values
        Temperature = float(request.form.get("Temperature"))
        RH = float(request.form.get("RH"))
        Ws = float(request.form.get("Ws"))
        Rain = float(request.form.get("Rain"))
        FFMC = float(request.form.get("FFMC"))
        DMC = float(request.form.get("DMC"))
        DC = float(request.form.get("DC"))
        ISI = float(request.form.get("ISI"))
        BUI = float(request.form.get("BUI"))

        input_data = np.array([[Temperature, RH, Ws, Rain,
                                FFMC, DMC, DC, ISI, BUI]])

        # scale data
        scaled_data = standard_scaler.transform(input_data)

        # predict
        prediction = ridge_model.predict(scaled_data)[0]

        return render_template(
            "home.html",
            prediction=round(prediction, 2)
        )
  else:
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
