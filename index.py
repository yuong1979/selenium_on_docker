from flask import Flask, request
# from yahoo_extract import main
from dotenv import load_dotenv
import os
from test_selenium import test

# Load the environment variables from the .env file
load_dotenv()




app = Flask(__name__)

@app.route('/')
def home():
    print ('main page loaded successfully')
    app.logger.info('main page loaded successfully')
    page = "Main page"

    return page


@app.route('/run_function', methods=['POST'])
def run_function():
    if request.method == 'POST':

        # Access the header
        my_header_value = request.headers.get('my_header')
        # Access the payload
        my_payload_value = request.json.get('my_payload')
        payload = request.json.get('my_payload')

        if payload == os.getenv("PASSWORD"):

            # main()
            app.logger.info("run main ok")
            return 'Function executed!'
        else:
            return 'Invalid payload value'
    else:
        return 'Invalid request method'



@app.route('/testing')
def testing():

    test()

    print ('testing')
    return 'Test'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)


# http://127.0.0.1:3000/testing

