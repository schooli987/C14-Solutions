from flask import Flask, render_template, jsonify

# Create Flask app instance
app = Flask(__name__)

# Route returning plain text
@app.route('/text')
def text_response():
    return "This is a plain text response"

# Route returning inline HTML
@app.route('/html')
def html_response():
    return "<h2 style='color:blue;'>This is an inline HTML response</h2>"

# Route returning JSON
@app.route('/json')
def json_response():
    return jsonify({"message": "Hello", "status": "success"})

# Route returning HTML file
@app.route('/')
def home():
    return render_template('index.html')   # Make sure you have 'templates/index.html'

# Run app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
