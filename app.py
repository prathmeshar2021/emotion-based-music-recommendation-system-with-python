from flask import Flask, render_template, Response, jsonify
import gunicorn
import subprocess  # Import subprocess module to run spotipy.py
from camera import *
# Add a global variable to track freeze state
freeze_state = False

app = Flask(__name__)

headings = ("Name","Album","Artist")
df1 = music_rec()
df1 = df1.head(15)
@app.route('/')
def index():
    print(df1.to_json(orient='records'))
    return render_template('index.html', headings=headings, data=df1)

@app.route('/run_spotipy')
def run_spotipy():
    # Call spotipy.py to regenerate CSV files
    subprocess.run(["python", "spotipy.py"])
    # Redirect back to the home page after running spotipy.py
    return redirect(url_for('index'))

def gen(camera):
    while True:
        global df1, freeze_state
        if not freeze_state:  # Only yield frames if freeze_state is False
            frame, df1 = camera.get_frame()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            time.sleep(0.1)  # Sleep briefly if frozen

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/t')
def gen_table():
    return df1.to_json(orient='records')

@app.route('/toggle_freeze')
def toggle_freeze():
    global freeze_state
    freeze_state = not freeze_state
    return jsonify({'freeze_state': freeze_state})


if __name__ == '__main__':
    app.debug = True
    app.run()
