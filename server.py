#This function will just do routing of request and response
from flask import Flask, request, jsonify
import utility
app = Flask(__name__)

@app.route('/get_locations')
def get_locations():
    response = jsonify({
        'locations' : utility.get_location_names()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_area_types')
def get_area_types():
    response = jsonify({
        'area_types' : utility.get_area_types()
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
@app.route('/predict_house_price', methods=['POST'])
def predict_house_price():
    area_type = request.form['area_type']
    location = request.form['location']
    bhk = int(request.form['bhk'])
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])

    response = jsonify({
        'estimated_house_price': utility.predict_price(area_type,location,bhk,total_sqft,bath,balcony)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Starting flask server")
    utility.load_saved_artifacts()
    app.run()

