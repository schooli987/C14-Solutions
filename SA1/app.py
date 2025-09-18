from flask import Flask

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# Dynamic route with variable <name>
@app.route('/<name>')
def hello(name):
    return f"Hello, {name}! Welcome to Flask."


if __name__ == '__main__':
    app.run(debug=True)
