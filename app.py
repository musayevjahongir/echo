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
    return 'hello world'