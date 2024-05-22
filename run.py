from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class TestAPI(Resource):
    def get(self):
        return jsonify(status='API is working')

class TestDB(Resource):
    def get(self):
        # Here you would typically check database connection
        return jsonify(status='Database is working')

api.add_resource(TestAPI, '/api/test')
api.add_resource(TestDB, '/db/test')

if __name__ == '_main_':
    app.run(debug=True)