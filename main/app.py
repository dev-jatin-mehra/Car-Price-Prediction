from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open('./model/Model.pkl', 'rb'))
data_car = pd.read_csv("Cleaned_Car.csv")

@app.route('/')
def index():
    Companies = sorted(data_car['company'].unique())
    Car_Model = sorted(data_car['name'].unique())
    Year = sorted(data_car['year'].unique(),reverse=True)
    FuelType = data_car['fuel_type'].unique()

    # Companies.insert(0, 'Select Company')

    return render_template('index.html',Companies = Companies , Car_Model = Car_Model , Year = Year , FuelType = FuelType)
@app.route('/predict',methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('Fuel_Type')
    kms_driven = int(request.form.get('kilo_driven'))

    prediction = model.predict(pd.DataFrame([[car_model,company,year,kms_driven,fuel_type]],columns=['name','company',
    'year','kms_driven','fuel_type']))
    print(prediction[0])
    return str(prediction[0])


if __name__=="__main__":
    app.run(debug=True)