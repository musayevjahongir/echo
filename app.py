from flask import Flask, request
import telegram
# Create the application instance
app = Flask(__name__)

TOKEN ='6800652506:AAFckawp2yqAzZdI9EgCui2qZqu_KUqnwPE'
bot = telegram.Bot(TOKEN)

# route for index page
@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    print(data)
    if 'text' in data['message']:
        chat_id=data['message']['chat']['id']
        text=data["message"]['text']
        bot.send_message(chat_id=chat_id, text=text)

    if 'photo' in data['message']:
        chat_id=data['message']['chat']['id']
        photo=data["message"]['photo'][0]['file_id']
        bot.send_photo(chat_id, photo)

    if 'video' in data['message']:
        chat_id=data['message']['chat']['id']
        video=data["message"]['video']['file_id']
        bot.send_video(chat_id, video)
    if 'document' in data['message']:
        chat_id=data['message']['chat']['id']
        document=data["message"]['document']['file_id']
        bot.send_document(chat_id, document)
    if 'voice' in data['message']:
        chat_id=data['message']['chat']['id']
        voice=data["message"]['voice']['file_id']
        bot.send_voice(chat_id, voice)
    if 'video_note' in data['message']:
        chat_id=data['message']['chat']['id']
        video_note=data["message"]['video_note']['file_id']
        bot.send_video_note(chat_id, video_note)
    return 'hello world'