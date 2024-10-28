from flask import Flask, render_template, request, jsonify
import cv2
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/capture', methods=['POST'])
def capture():
    # Initialize camera and capture image
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    
    # If image is captured, convert to base64 for HTML display
    if ret:
        _, buffer = cv2.imencode('.jpg', frame)
        img_str = base64.b64encode(buffer).decode('utf-8')
        return jsonify({'status': 'success', 'image': img_str})
    else:
        return jsonify({'status': 'failed', 'image': None})

if __name__ == '__main__':
    app.run(debug=True)
