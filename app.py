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

#PUT request
@app.route('/famous/api/restaurants/<int:rank_rest>', methods=['PUT'])
def update_restaurant(rank_rest):
    restaurant = [restaurant for restaurant in restaurants if restaurant['rank'] == rank_rest]
    if len(restaurant) == 0:
        abort(404)
    if not request.json:
        return jsonify({"Error":"Failed"})
    if 'name' in request.json and type(request.json['name']) != type(restaurant[0]['name']):
        return jsonify({"Error":"Failed"})
    if 'rating' in request.json and type(request.json['rating']) != type(restaurant[0]['rating']):
        return jsonify({"Error":"Failed"})
    if 'location' in request.json and type(request.json['location']) != type(restaurant[0]['location']):
        return jsonify({"Error":"Failed"})
    
    restaurant[0]['name'] = request.json.get('name', restaurant[0]['name'])
    restaurant[0]['location'] = request.json.get('location', restaurant[0]['location'])
    restaurant[0]['rating'] = request.json.get('rating', restaurant[0]['rating'])
    return jsonify({'restaurant': restaurant[0]})

#DELETE request
@app.route('/famous/api/restaurants/<int:rank_rest>', methods=['DELETE'])
def delete_restaurant(rank_rest):
    restaurant= [restaurant for restaurant in restaurants if restaurant['rank'] == rank_rest]
    if len(restaurant) == 0:
        abort(404)
    restaurants.remove(restaurant[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)