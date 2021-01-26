from flask import Flask,jsonify
from flask import abort
from flask import request

#Creating an app using flask
app = Flask(__name__)

# Data Dictionary
restaurants = [
    {
        'rank': 1,
        'name': 'Chaska Restaurant',
        'location' : 'Delhi',
        'rating' : '4.5/4'
    },
    {
        'rank' : 2,
        'name' : 'Daawat Restauarant',
        'location' : 'Mumbai', 
        'rating' : '4/5'
    },
    {
        'rank' : 3,
        'name' : 'Sukhdev Dhaba',
        'location' : 'Haryana',
        'rating' : '5/5'
    },
    {
      "location": "",
      "name": "WahJiWah",
      "rank": 4,
      "rating": "5/5"
    },
    {
      "location": "",
      "name": "Myriad",
      "rank": 5,
      "rating": "5/5"
    }
]

#creating basic api (Default:Get)
@app.route('/famous/api/restaurants/')
def listdown():
    return jsonify({'Restaurants' : restaurants})

# GET request
@app.route('/famous/api/restaurants/<int:rest_rank>', methods=['GET'])
def get_restaurant(rest_rank):
    restaurant = [restaurant for restaurant in restaurants if restaurant['rank'] == rest_rank]
    if len(restaurant) == 0:
        abort(404)
    return jsonify({'Restaurant' : restaurant[0]})

if __name__ == '__main__':
    app.run(debug=True)