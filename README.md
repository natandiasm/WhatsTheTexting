![Chat Icon](./app/static/img/chat.png)
# WhatsTheTexting 🎤 > 💬
Converta audio em texto, usando o IBM Watson.
- Converta audios do whatsapp para texto.
- Converta audios do telegram para texto.

## Como Executar
1) Copie esse repositório
```sh
git clone https://github.com/natandiasm/WhatsTheTexting.git
```

2) Entre na pasta

```sh
cd WhatsTheTexting
```

3) Execute o comando 

```sh
pip install -r requirements.txt
```

4) Coloque suas credenciais diretamento no arquivo config.py ou coloque nas variaveis de ambiente (Recomendado). Elas podem ser obtidas atraz do [IBM Watson Speech to Text](https://www.ibm.com/br-pt/cloud/watson-speech-to-text).

5) Dentro da pasta, execute o comando. 
```sh
python3 run.py
```

5) O seu servidor funcionará no http://127.0.0.1:5000/