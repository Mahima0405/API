from flask import Flask,jsonify
from flask import abort
from flask import request
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)

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
    }
]

#Securing API
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == "mahima":
        return "mahima0405"
    return None

@auth.error_handler
def unauthorized():
    return jsonify({'error': 'Unauthorized access'})

@app.route('/famous/api/restaurants/', methods=["GET"])
@auth.login_required
def get_list():
    return jsonify({'restaurants' : restaurants})

if __name__ == '__main__':
    app.run(debug=True)