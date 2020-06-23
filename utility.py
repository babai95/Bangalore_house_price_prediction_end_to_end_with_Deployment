import json
import pickle
import numpy as np

area_types = None
locations = None
columns = None
model = None
def get_location_names():
    """ It should read the columns.json file and returns the locations"""
    return locations

def get_area_types():
    return area_types

def load_saved_artifacts():
    global locations
    global columns
    global model
    global area_types

    with open("columns.json", "r") as f:
        columns = json.load(f)["data_columns"]
        area_types = columns[4:8]
        locations = columns[8:-1]

    with open("banglore_home_prices_model.pickle", "rb") as f:
        model = pickle.load(f)

def predict_price(area_type, location, bhk ,total_sqft, bath, balcony):
    tokens = area_type.split(" ")
    if(len(tokens) == 2):
        area_type = tokens[0] + "  " + tokens[1]
    else:
        area_type = tokens[0] + " " + tokens[1] + "  " + tokens[2]
    area_type_ind = columns.index(area_type.lower())
    if location not in locations:
        location = 'other_loc'
    location_ind = columns.index(location.lower())

    data = np.zeros(len(columns))
    data[0] = bhk
    data[1] = total_sqft
    data[2] = bath
    data[3] = balcony
    data[area_type_ind] = 1
    data[location_ind] = 1
    return np.round(model.predict([data])[0],2)

if __name__ == '__main__':

    load_saved_artifacts()
    print(get_location_names())
    print(get_area_types())
    print(predict_price('built-up area','ambedkar nagar',2,4000,2,3))
    print(predict_price('built-up area', 'ambedkar nagar', 2, 2000, 2, 3))
    print(predict_price('built-up area', 'ambedkar nagar', 2, 2000, 3, 3))
    print(predict_price('built-up area', 'durgapur', 2, 2000, 2, 3))