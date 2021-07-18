from flask import Flask, render_template, Response
import cv2

#vid = cv2.VideoCapture(0) # 카메라 캡쳐
vid = cv2.VideoCapture('ocp.mp4') # 파일 재생

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

def gen():
    while True:
        _, frame = vid.read()
        rimg = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + rimg + b'\r\n')

@app.route('/Feed')
def Feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/Capture')
def Capture():
    return render_template('capture.html')

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
