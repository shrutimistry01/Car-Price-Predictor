

from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('carPricePred_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        year = int(request.form['Year'])
        year=2022-year
        mileage = int(request.form['mileage'])
        engine = int(request.form['engine'])
        max_power = int(request.form['max_power'])
        seats = int(request.form['seats'])
        km_driven=int(request.form['Kms_Driven'])
        km_driven2 = np.log(km_driven)
        owner = request.form['owner']
        if(owner =='Second'):
                owner_second =1
                owner_more=0
        elif(owner =="More"):
            owner_second =0
            owner_more=1
        else:
            owner_second =0
            owner_more=0
        fuel = request.form['Fuel']
        if(fuel=='Petrol'):
                fuel_Type_Petrol=1
                fuel_Type_Diesel=0
                fuel_Type_LPG=0
        elif(fuel=='Diesel'):
                fuel_Type_Petrol=0
                fuel_Type_Diesel=1
                fuel_Type_LPG=0
        elif(fuel=='LPG'):
                fuel_Type_Petrol=0
                fuel_Type_Diesel=0
                fuel_Type_LPG=1
        else:
            fuel_Type_Petrol=0
            fuel_Type_Diesel=0
            fuel_Type_LPG=0
        seller_Type=request.form['Seller_Type_Individual']
        if(seller_Type=='Individual'):
            seller_Type_Individual=1
            seller_Type_trustmark=0    
        elif(seller_Type=='TD'):
            seller_Type_Individual=0	
            seller_Type_trustmark=1
        else:
            seller_Type_Individual=0	
            seller_Type_trustmark=0
        transmission_Mannual=request.form['Transmission_Mannual']
        if(transmission_Mannual=='Mannual'):
            transmission_Mannual=1
        else:
            transmission_Mannual=0
            
        prediction=model.predict([[km_driven2,mileage,engine,max_power,seats,year,fuel_Type_Diesel,fuel_Type_LPG,fuel_Type_Petrol,seller_Type_Individual,seller_Type_trustmark,transmission_Mannual,owner_more,owner_second]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

