from django.core.management.base import BaseCommand
import telebot
from telebot import types
from shop.models import Figure

bot = telebot.TeleBot("6879858805:AAE6sbNonC6Kk57Y3woVvqnCanVIDWqgELA") # Вставьте сюда свой токен

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello world!")

@bot.message_handler(commands=['figures'])
def figures(message):
    figures = Figure.objects.all()
    for figure in figures:
        bot.send_message(message.chat.id, f"{figure.shape} {figure.color}")

response = (
    "Commands:\n"
    "/start: type start to get Hello World!\n"
    "/figures: show figures\n"
    "/student: show students name and 2nd name\n"
    "/add <shape> <color>: add another figure"
)

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, response)

@bot.message_handler(commands=['add'])
def handle_add_figure(message):
    parts = message.text.split(maxsplit=2)
    if len(parts) == 3:
        _, shape, color = parts
        figure = Figure.objects.create(shape=shape, color=color)
        bot.send_message(message.chat.id, f"Фигура {shape} цвета {color} добавлена!")
    else:
        bot.send_message(message.chat.id, "Используйте /add <shape> <color>")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting bot...")
        bot.polling()
        print("Bot stopped")
