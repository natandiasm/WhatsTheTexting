import json

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import SpeechToTextV1

import config


class ConvertAudio:

    def __init__(self):
        authenticator = IAMAuthenticator(config.IBM_API_KEY)
        self.service = SpeechToTextV1(authenticator=authenticator)
        self.service.set_service_url(config.IBM_URL_SERVICE)

    def __verify_file_extension(self, file):
        if file.endswith('.mp3'):
            return ['audio/mp3', file]
        elif file.endswith('.ogg'):
            return ['audio/ogg', file]

    def __send_audio_to_server(self, file):
        # Abre o arquivo de audio audio
        with open(file[1], 'rb') as audio_file:
            # Envia o audio para o serviço da IBM
            response_server = self.service.recognize(
                audio=audio_file,  # Arquivo de audio
                content_type=file[0],
                # Tipo do arquivo consultar em https://cloud.ibm.com/apidocs/speech-to-text?code=python#addaudio
                model=config.IBM_MODEL_LANGUAGE
                # Modelo de conversão consultar em https://cloud.ibm.com/docs/speech-to-text?topic=speech-to-text-models-list
                ).get_result()
            # Converte a resposta em DIC
            dic = json.loads(
                json.dumps(
                    response_server,
                    indent=2
                )
            )

        return dic['results'][0]['alternatives']

    def convert_audio(self, file_path):
        file_valid = self.__verify_file_extension(file_path)
        response = self.__send_audio_to_server(file=file_valid)
        result = json.dumps({"code": 200, "response": response}, ensure_ascii=False).encode('utf8')
        return result
