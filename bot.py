from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
    )
from telegram.ext import (
    Updater, 
    MessageHandler, 
    CommandHandler, 
    CallbackQueryHandler, 
    Filters, 
    CallbackContext
    )
import os
from db import DB

smartphoneDB = DB("data.json")
TOKEN = os.environ["TOKEN"]
def start(update: Update, context: CallbackContext):

    shop = InlineKeyboardButton(text = "🛍 Shop", callback_data="shopping")
    card = InlineKeyboardButton(text = "📦 Cart", callback_data="card")
    contact = InlineKeyboardButton(text = "📞 Contact", callback_data="contact")
    about = InlineKeyboardButton(text = "📝 About", callback_data="about_bot")

    reply_markup = InlineKeyboardMarkup([
        [shop, card],
        [contact, about]
    ])
    update.message.reply_text("Welcome to Bot!", reply_markup=reply_markup)

def main_menu(update: Update, context: CallbackContext):

    query = update.callback_query
    shop = InlineKeyboardButton(text = "🛍 Shop", callback_data="shopping")
    card = InlineKeyboardButton(text = "📦 Cart", callback_data="card")
    contact = InlineKeyboardButton(text = "📞 Contact", callback_data="contact")
    about = InlineKeyboardButton(text = "📝 About", callback_data="about_bot")

    reply_markup = InlineKeyboardMarkup([
        [shop, card],
        [contact, about]
    ])
    query.edit_message_text("Main menu.", reply_markup=reply_markup)

def shopping(update: Update, context: CallbackContext):
    query = update.callback_query

    tables = smartphoneDB.get_tables()

    buttons = []

    for brand in tables:
        button = InlineKeyboardButton(text=brand, callback_data=f"brand_{brand}")
        buttons.append([button])
    back = InlineKeyboardButton(text="back", callback_data="main_menu")
    buttons.append([back])
    reply_markup = InlineKeyboardMarkup(buttons)

    query.edit_message_text("Yoqtirgan brandni tanlang!", reply_markup=reply_markup)
    
def get_phone(update: Update,context: CallbackContext):
    query = update.callback_query
    data = query.data

    brand = data.split("_")[-1]
    query.answer(brand)

updater = Updater(TOKEN)

dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CallbackQueryHandler(shopping, pattern="shopping"))
dp.add_handler(CallbackQueryHandler(main_menu, pattern="main_menu"))
dp.add_handler(CallbackQueryHandler(get_phone, pattern = "brand"))


updater.start_polling()
updater.idle()