from flask import Flask
import HTMLParser

# Create the Flask Object
app = Flask(__name__)
parser = HTMLParser.HTMLParser()

# Create the Endpoints
@app.route('/')
def index():
	return parser.convert_to_html(app.root_path, 'index')

# Run the App
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=50)