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

    
    user = update.message.from_user
    shop = InlineKeyboardButton(text = "🛍 Shop", callback_data="shopping")
    card = InlineKeyboardButton(text = "📦 Cart", callback_data="card")
    contact = InlineKeyboardButton(text = "📞 Contact", callback_data="contact")
    about = InlineKeyboardButton(text = "📝 About", callback_data="about_bot")

    reply_markup = InlineKeyboardMarkup([
        [shop, card],
        [contact, about]
    ])
    text= f"Hello, {user.first_name}! Welcome to your bot."
    update.message.reply_text(text=text, reply_markup=reply_markup)

def main_menu(update: Update, context: CallbackContext):
    """
    
    """
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

    phones = smartphoneDB.get_phone_list(brand)

    buttons = []
    a=0
    b=a+10
    for i, phone in enumerate(phones[a:b], 1):
        name = phone.get("name")
        color = phone.get("color")
        ram = phone.get("RAM")
        memory = phone.get("memory")
        text = f"{name}, {color}-{ram}/{memory}"
        button = InlineKeyboardButton(text=text, callback_data=f"phone_{brand}_{i}")
        buttons.append([button])
    Main_menu = InlineKeyboardButton(text="Main_menu", callback_data="shopping")
    
    next = InlineKeyboardButton(text='👉',callback_data=f"nextbrand,{data},{a},{b}")
    if a>=10:
        back = InlineKeyboardButton(text='👈',callback_data=f'Backbrand,{data},{a},{b}')
        buttons.append([back])
    buttons.append([next])
    buttons.append([Main_menu])
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text("Yoqtirgan smartphoneinigzni tanlang!", reply_markup=reply_markup)
    # query.answer(brand)


def Next(update:Update,context:CallbackContext):
    query = update.callback_query
    print(query.data)
    data = query.data.split(',')[1]

    brand = data.split("_")[-1]

    phones = smartphoneDB.get_phone_list(brand)

    buttons = []
    a=int(query.data.split(',')[2])
    b=int(query.data.split(',')[3])
    print(a,b)
    a=a+10
    b=b+10
    for i, phone in enumerate(phones[a:b], 1):
        name = phone.get("name")
        color = phone.get("color")
        ram = phone.get("RAM")
        memory = phone.get("memory")

        text = f"{name}, {color}-{ram}/{memory}"
        button = InlineKeyboardButton(text=text, callback_data=f"phone_{brand}_{i}")
        buttons.append([button])
    Main_menu = InlineKeyboardButton(text="Main_menu", callback_data="shopping")

    next = InlineKeyboardButton(text='👉',callback_data=f'nextbrand,{data},{a},{b}')
    if a>=10:
        back = InlineKeyboardButton(text='👈',callback_data=f'Backbrand,{data},{a},{b}')
        buttons.append([back])
    buttons.append([next])
    buttons.append([Main_menu])
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text("Yoqtirgan smartphoneinigzni tanlang!", reply_markup=reply_markup)

def Back(update:Update,context:CallbackContext):
    query = update.callback_query
    print(query.data)
    data = query.data.split(',')[1]

    brand = data.split("_")[-1]

    phones = smartphoneDB.get_phone_list(brand)

    buttons = []
    a=int(query.data.split(',')[2])
    b=int(query.data.split(',')[3])
    a=a-10
    b=b-10
    for i, phone in enumerate(phones[a:b], 1):
        name = phone.get("name")
        color = phone.get("color")
        ram = phone.get("RAM")
        memory = phone.get("memory")

        text = f"{name}, {color}-{ram}/{memory}"
        button = InlineKeyboardButton(text=text, callback_data=f"phone_{brand}_{i}")
        buttons.append([button])
    Main_menu = InlineKeyboardButton(text="Main_menu", callback_data="shopping")
    next = InlineKeyboardButton(text='👉',callback_data=f'nextbrand,{data},{a},{b}')
    if a>=10:
        back = InlineKeyboardButton(text='👈',callback_data=f'Backbrand,{data},{a},{b}')
        buttons.append([back])
    buttons.append([next])
    buttons.append([Main_menu])
    reply_markup = InlineKeyboardMarkup(buttons)
    query.edit_message_text("Yoqtirgan smartphoneinigzni tanlang!", reply_markup=reply_markup)


def send(update:Update, context:CallbackContext):
    query=update.callback_query
    bot=context.bot
    chat_id=query.message.chat.id
    callback_data=query.data
    dic=smartphoneDB.get_phone(callback_data.split('_')[1],callback_data.split('_')[2])
    photo=dic["img_url"]
    text=f"name  {dic['name']}\nCompany  {dic['company']}\nColor {dic['color']}\nRAM  {dic['RAM']}\nMemory {dic['memory']}"
    cancel=InlineKeyboardButton(text='Cancel',callback_data='Cancel')
    keyboard=InlineKeyboardMarkup([[cancel]],resize_keyboard=True)
    query.delete_message()
    bot.sendPhoto(chat_id=chat_id,photo=photo,caption=text,reply_markup=keyboard)
    

def Cancel(update:Update, context:CallbackContext):
    bot=context.bot
    query = update.callback_query
    chat_id=query.message.chat.id
    tables = smartphoneDB.get_tables()

    buttons = []

    for brand in tables:
        button = InlineKeyboardButton(text=brand, callback_data=f"brand_{brand}")
        buttons.append([button])
    back = InlineKeyboardButton(text="back", callback_data="main_menu")
    buttons.append([back])
    reply_markup = InlineKeyboardMarkup(buttons,resize_keyboard=True)
    query.delete_message()
    bot.sendMessage(chat_id=chat_id,text="Yoqtirgan brandni tanlang!", reply_markup=reply_markup)



updater = Updater(TOKEN)

dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CallbackQueryHandler(shopping, pattern="shopping"))
dp.add_handler(CallbackQueryHandler(main_menu, pattern="main_menu"))
dp.add_handler(CallbackQueryHandler(get_phone, pattern = "brand"))
dp.add_handler(CallbackQueryHandler(send,pattern="phone"))
dp.add_handler(CallbackQueryHandler(Cancel,pattern="Cancel"))
dp.add_handler(CallbackQueryHandler(Next,pattern='nextbrand'))
dp.add_handler(CallbackQueryHandler(Back,pattern='Backbrand'))
updater.start_polling()
updater.idle()