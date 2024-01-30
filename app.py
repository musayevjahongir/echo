from flask import Flask,request
import telegram
# Create the application instance
TOKEN ='6804364814:AAFG6WL6EcqnIgL_9qY4euWHUcvGaCKLU08'
bot = telegram.Bot(TOKEN)
# chat_id = '1432402481'
app = Flask(__name__)

@app.route('/',methods=["POST"])
def index():
    data=request.get_json()
    print(data)
    bot.send_message(chat_id=data['message']['chat']['id'],text=data['message']['text'])
    return 'index page'

if __name__=="__main__":
    app.run(debug=True)