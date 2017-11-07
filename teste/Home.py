from flask import Flask, json
from flask.json import JSONEncoder, jsonify
from flask_restful import Api, Resource

from model.Person import Person

app = Flask(__name__)
api = Api(app)


@api.resource('/')
class HomeController(Resource):
                    
    def get(self):
        person = Person('Delano', 'Junior', 10000.85)
        data = jsonify(name=person.name, surname=person.surname, salary=person.salary)
        return data
    

class Main:
    
    app.run(port=1010, debug=True)
    
