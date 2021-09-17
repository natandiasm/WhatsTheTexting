import os
import config
import json

from flask import Blueprint, request, flash, redirect, render_template
from werkzeug.utils import secure_filename
from models import ConvertAudio

upload_blueprint = Blueprint(
    'appapp',
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path=''
)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS


@upload_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('Não é um arquivo')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('Arquivo não selecionado')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # Verifica se o arquivo é seguro
            filename = secure_filename(file.filename)
            # Faz o upload do aquivo na pasta
            file.save(os.path.join(config.UPLOAD_FOLDER, filename))
            # Recupera o caminho do arquivo
            file_path = os.path.join(config.UPLOAD_FOLDER, filename)
            # Cria uma instancia do Model de conversão
            convert_audio = ConvertAudio()
            response = json.loads(convert_audio.convert_audio(file_path))
            text = response['response'][0]
            return render_template('transcription.html', text=text)
    return render_template('index.html')
