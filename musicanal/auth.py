from flask import Flask, request
import spotipy
import spotipy.util as util


# Вроде как должно работать!
# Чтобы получить новый токен нужно поднять локальный сервер на ngrok
# Это простенькая програмка. После того, как поднимаешь сервер тебе даётся ссылка ввида
# https://a5bf0cab.ngrok.io - её нужно указывать в redirect_uri в настройках спотифая
# Для этого зайти на developer.spotify.com и залогиниться подо мной:
# avscherbakov@icloud.com / asuswl-500wlan
# Не смей палить мои данные и использовать мой аккаунт Спотифая, я узнаю [:
# Ну, удачи!


app = Flask(__name__)
SCOPE = 'user-library-read'
USERNAME = 'mrgoldlion'

SPOTIPY_CLIENT_ID = '2677052c01ac46f69ae9fa2dd8a5ffc2'
SPOTIPY_CLIENT_SECRET = '9e0665f38b944d008d94eb97bcf2f28a'
SPOTIPY_REDIRECT_URI =  'http://ec095cfe.ngrok.io/auth'


def hello(request):
    token = util.prompt_for_user_token(
                                        USERNAME,
                                        scope=SCOPE,
                                        client_id=SPOTIPY_CLIENT_ID,
                                        client_secret=SPOTIPY_CLIENT_SECRET,
                                        redirect_uri=SPOTIPY_REDIRECT_URI)

    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
        for item in results['items']:
            track = item['track']
            print (track(['name'] + ' - ' + track['artists'][0]['name']))
    else:
        print( "Can't get token for", USERNAME)

    return "Success"


@app.route("/webhook/", methods=['GET', 'POST'])
def handle_data():
    return hello(request)


@app.route("/auth/", methods=['GET', 'POST'])
def handle_auth():
    return "Success"

app.run(port=8071, debug=True)
app.config['SERVER_NAME'] = ' http://ec095cfe.ngrok.io'
