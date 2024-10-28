from flask import Flask, render_template, request, redirect, url_for, session
import cv2  # Ensure cv2 is installed in your environment
import numpy as np  # Ensure numpy is installed in your environment

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# A route for the index page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'user_one' and password == 'pass_one':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return render_template('index.html', error="Invalid credentials")
    return render_template('index.html')

# A route for the dashboard page
@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    return render_template('dashboard.html', identities=get_available_identities(), error=None)

# Simulate the work.py script function
def get_identity():
    return {
        "name": "Krishna",
        "age": 19,
        "gender": "M",
        "location": "hyd"
    }

# Example function to get available identities
def get_available_identities():
    return [
        {"name": "Krishna", "age": 19, "gender": "M", "location": "hyd"},
        {"name": "John", "age": 25, "gender": "M", "location": "ny"},
        {"name": "Emily", "age": 22, "gender": "F", "location": "sf"},
        {"name": "Alice", "age": 30, "gender": "F", "location": "la"},
        {"name": "Bob", "age": 27, "gender": "M", "location": "lv"},
    ]

# A function to process image and return the matching identity
@app.route('/capture', methods=['POST'])
def capture():
    # Here, you'd normally capture and process the image from the webcam
    current_identity = get_identity()
    
    identities = get_available_identities()
    # Simulating the matching and sorting mechanism
    sorted_identities = sorted(
        identities, 
        key=lambda x: x['name'] == current_identity['name'], 
        reverse=True
    )
    
    return render_template('dashboard.html', identities=sorted_identities)

if __name__ == '__main__':
    app.run(debug=True)
