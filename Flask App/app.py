import argparse
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
	return 'Hello, World!'
if __name__ == '__main__':
	# Create the parser and add arguments
	parser = argparse.ArgumentParser(description='Run a Flask web server.')
	parser.add_argument('--host', type=str, default='127.0.0.1', help='Host to run the server on')
	parser.add_argument('--port', type=int, default=5000, help='Port to run the server on')
	parser.add_argument('--debug', type=bool, default=False, help='Enable or disable debug mode')
	# Parse the arguments
	args = parser.parse_args()
	# Run the Flask app with parsed arguments
	app.run(host=args.host, port=args.port, debug=args.debug)