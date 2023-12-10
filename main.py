from k_model import detect_class, detect_object
from flask import Flask, render_template, request
import os



app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'images'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html',
                               error='Файл не был загружен')
    
    file = request.files.get('file')

    if file.filename == '':
        return render_template('index.html',
                               error='Не выбран файл')

    file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    response = detect_object(f'images/{file.filename}')
    return render_template('index.html', error=response)


if __name__ == '__main__':
    app.run()
