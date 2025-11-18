from flask import Flask, render_template, request, redirect, url_for
import os
from utils.image_utils import predict_image
from utils.video_utils import predict_video
from utils.audio_utils import predict_audio
from utils.text_utils import predict_text

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024 

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Static "none" models, for demo mode
image_model = None
video_model = None
audio_model = None
text_model  = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_image', methods=['POST'])
def analyze_image():
    file = request.files['file']
    if not file or file.filename == '':
        return redirect(url_for('index'))
    filename = file.filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    verdict, explanation, score = predict_image(image_model, filepath)
    return render_template('result.html',
                           modality='image',
                           user_input=filename,
                           verdict=verdict, explanation=explanation, score=score)

@app.route('/analyze_video', methods=['POST'])
def analyze_video():
    file = request.files['file']
    if not file or file.filename == '':
        return redirect(url_for('index'))
    filename = file.filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    verdict, explanation, score = predict_video(video_model, filepath)
    return render_template('result.html',
                           modality='video',
                           user_input=filename,
                           verdict=verdict, explanation=explanation, score=score)

@app.route('/analyze_audio', methods=['POST'])
def analyze_audio():
    file = request.files['file']
    if not file or file.filename == '':
        return redirect(url_for('index'))
    filename = file.filename
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    verdict, explanation, score = predict_audio(audio_model, filepath)
    return render_template('result.html',
                           modality='audio',
                           user_input=filename,
                           verdict=verdict, explanation=explanation, score=score)

@app.route('/analyze_text', methods=['POST'])
def analyze_text():
    text = request.form.get('input_text', '').strip()
    if not text:
        return redirect(url_for('index'))

    verdict, explanation, score = predict_text(text_model, text)
    return render_template('result.html',
                           modality='text',
                           user_input=text,
                           verdict=verdict, explanation=explanation, score=score)

if __name__ == '__main__':
    app.run(debug=True)
