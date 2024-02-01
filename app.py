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
    chat_id=data['message']['chat']['id']
    bot.send_message(chat_id=chat_id, text='Hello World!!!')
    return 'index page'