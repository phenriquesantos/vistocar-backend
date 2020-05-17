from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from models import initialize_database
from os import environ
from resources import initialize_resources
from schema.schema import Schema


application = Flask(__name__)

# load de variáveis de ambiente
print('Loading environment variables from .env file')
load_dotenv('./environments/local.env')

# load das variaveis de ambiente dentro do flask
for item in environ.items():
    application.config[item[0]] = item[1]

# definição de CORS
if not environ.get('CORS_URL', None):
    CORS(application, supports_credentials=True, origins="*")
else:
    print(environ.get('CORS_URL'))
    CORS(application, resources={r"*": {"origins": environ.get('CORS_URL')}})

# start no database
initialize_database(application)

# Starting RESTful endpoints
initialize_resources(application)

@application.before_request
def startup():
    print("Initializing migration DB")
    Schema.migration()

@application.after_request
def add_headers(response):
    response.headers.add('Content-Type', 'application/json')
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Expose-Headers', 'Content-Type,Content-Length,Authorization,X-Pagination')
    return response

# Run application
if __name__ == '__main__':
    print('Initilizing application')
    application.run()
