import os
import telebot
from scrapper import getAttendance
import requests


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
GIPHY_TOKEN = os.getenv('GIPHY_TOKEN')

GIFURL = "https://api.giphy.com/v1/gifs/random"

app = telebot.TeleBot(TELEGRAM_TOKEN)


def get_gif_id(tag):
  response = requests.get(GIFURL,
                          params={
                            "api_key": GIPHY_TOKEN,
                            "tag": tag,
                            "rating": "r"
                          }).json()
  return response["data"]["id"]


@app.message_handler(commands=['start'])
def greet(message):
  print(message)
  gif_id = get_gif_id("hello")
  app.send_animation(
    message.chat.id,
    animation=f"https://media3.giphy.com/media/{gif_id}/giphy.gif",
    caption="bot service")


@app.message_handler(commands=['atd'])
def send_attendance(message):
  [usr, pwd] = message.text.split(" ")[1:]
  usr="160119735" + usr
  pwd="160119735" + pwd
  result = getAttendance(usr, pwd)
  print("sending...")
  if result["success"]:
    app.send_message(message.chat.id, result["message"])
  else:
    app.send_message(message.chat.id,
                     result["message"],
                     reply_to_message_id=message.message_id)


@app.message_handler(commands=['gif'])
def send_gif(message):
  term = " ".join(message.text.split(" ")[1:])
  try:
    gif_id = get_gif_id(term)
    app.send_animation(
      message.chat.id,
      animation=f"https://media3.giphy.com/media/{gif_id}/giphy.gif",
      reply_to_message_id=message.message_id)
  except:
    app.send_message(message.chat.id,
                     reply_to_message_id=message.message_id,
                     text="not available")


@app.message_handler(commands=['java'])
def send_file(message):
  try:
    app.send_document(message.chat.id,document="https://programmingwithmosh.com/wp-content/uploads/2019/07/Java-Cheat-Sheet.pdf",timeout=120)
  except Exception as err:
    print(err)


try:
  app.polling()
except KeyboardInterrupt:
  print("bot quiting...")