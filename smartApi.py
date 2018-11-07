from flask import Flask, request, Response
from flask_restful import Resource, Api
import requests


application = app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return 'Welcome to the SMART API'


class LandingUrl(Resource):
    def get(self):
        return {
            'url': {
                'Touro University':'link to url'
                }
            }


#add resources to url
api.add_resource(Home,'/')
api.add_resource(LandingUrl, '/url')


if __name__ == '__main__':
    app.run(debug=True)

