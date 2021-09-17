import os
from os.path import join

# Raiz do projeto
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# API Key do IBM Watson
IBM_API_KEY = os.environ.get('IBM_API_KEY')

# URL do serviso de conversão de texto
IBM_URL_SERVICE = os.environ.get('IBM_URL_SERVICE')

# Modelo de conversão de texto
IBM_MODEL_LANGUAGE = "pt-BR_NarrowbandModel"

# Pasta para upload
UPLOAD_FOLDER = join(BASE_DIR, r'app/static/uploads')

# Arquivos aceitos
ALLOWED_EXTENSIONS = {'ogg', 'mp3'}