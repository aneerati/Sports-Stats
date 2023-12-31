from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


# Response from GET request
class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}


api.add_resource(HelloWorld, "/helloworld")

# delete when out of development
if __name__ == "__main__":
    app.run(debug=True)
