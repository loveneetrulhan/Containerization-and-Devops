from flask import Flask

# Create Flask app
app = Flask(__name__)

# Define a route
@app.route('/')
def hello():
    return "Hello from Flask App!"

# Health check route
@app.route('/health')
def health():
    return "OK"

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
