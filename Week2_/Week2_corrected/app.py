from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Api, Resource, reqparse
from flask_httpauth import HTTPBasicAuth

# Done by: Laura Ong 1002464
app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()
#Create and manage users of
users = [
    {
    	'id': 1,
        "name": "Nick",
        "age": 42,
        "occupation": "Lawyer"
    },
    {
    	'id':2,
        "name": "Elvin",
        "age": 32,
        "occupation": "Doctor"
    },
    {
    	'id':3,
        "name": "Chris",
        "age": 22,
        "occupation": "Actor"
    }
]

class User(Resource):
    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200
        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200
      
api.add_resource(User, "/members/<string:name>")



@app.route('/members', methods = ['GET'])
def get_members():
	return jsonify({'users':users})


#Create a new member and add it onto members list
#Accept two mimetypes -- plain text, json
@app.route('/members', methods = ['POST'])
def create_member():
	newid = users[-1]['id'] + 1
	if request.headers['Content-Type'] == 'text/plain':
		user = {
			'id': newid,
			'name': request.data.decode('UTF-8'),
			'age':12,
			'occupation':'Lawyer'
		}
		users.append(user)
		return jsonify({'user': user}), 201
	elif request.headers['Content-Type'] == 'application/json':
		user = {
			'id': newid,
			'name': request.json['name'],
			'age': request.json['age'],
			'occupation': request.json['occupation']
		}
		users.append(user)
		return jsonify({'user': user}), 201
	else:
		#bad request
		abort(400)

@app.route('/members/<string:name>', methods = ['PUT'])
@auth.login_required
def update_member(name):
	myuser = [user for user in users if user['name'] == name]
	if len(user) == 0:
		abort(404)
	if not request.json:
		abort(400)
	if 'name' in request.json and type(request.json['name']) != unicode:
		abort(400)
	if 'occupation' in request.json and type(request.json['occupation']) != unicode:
		abort(400)
	if 'age' in request.json and type(request.json['age']) != unicode:
		abort(400)
	myuser[0]['name'] = request.json.get('name',myuser[0]['name'])
	myuser[0]['age'] = request.json.get('age',myuser[0]['age'])
	myuser[0]['occupation'] = request.json.get('occupation',myuser[0]['occupation'])
	return jsonify({'user':myuser[0]})
@app.route('/members/<string:name>', methods = ['DELETE'])
@auth.login_required
def delete_member(name):
	myuser = [user for user in users if user['name'] == name]
	if len(myuser) == 0:
		abort(404)
	users.remove(myuser[0])
	return jsonify({'deletion':True})

@auth.get_password
def get_password(username):
	if username == 'Valerie':
		return 'Ong'
	return None

# error handlers
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error': 'Not found, the resource you requested does not exist in the server.'}), 404)

@app.errorhandler(400)
def bad_request(error):
	print(error)
	return make_response(jsonify({'Error': 'The server is unable to understand your request.'}), 404)

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'Error': 'Unauthorized access, please achieve the way of the nils.'}), 403)


app.run(debug=True)