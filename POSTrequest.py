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

#POST request
@app.route('/famous/api/restaurants/', methods=['POST'])
def add_restaurant():
    if not request.json or not 'name' in request.json:
        abort(400)
    newrestaurant={
        'rank': restaurants[-1]['rank'] + 1,
        'name': request.json['name'],
        'location' : request.json.get('Location', ""),
        'rating': "5/5"
    }

    restaurants.append(newrestaurant)
    return jsonify({'Restaurants' : restaurants}), 201

if __name__ == '__main__':
    app.run(debug=True)