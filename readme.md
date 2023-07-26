# Smartphone shop bot

This is a bot for a smartphone shop. Using telegram bot API, it can be used to order a smartphone. It is written in python and uses the python-telegram-bot library.

## Menu map

### Main menu

- 🛍 Shop
- 📦 Cart
- 📞 Contact
- 📝 About

### Contact menu

- 📞 Phone number
- 📌 Address
- 📍 Location
- 📧 Email

### About menu

- 📝 About us
- 📝 About the bot

### Cart menu

- 📦 Cart
- 📝 Order
- 📝 Clear cart

### Shop menu

- Apple
- Samsung
- Xiaomi
- Huawei
- Oppo
- Vivo

### Under each brand

- 🌄 Photo
- 📱 Model
- 💵 Price
- 📦 Add to cart

## Structure of the bot

- The bot will have the following handlers:
  - start
  - about
  - contact
  - products
  - products_by_brand
  - cart
  - cancel

- The bot will have the following functions:

## List of tasks

- Start handler: The bot will send a welcome message and a main menu when the user starts the bot.

- Main menu.
The main menu will have 4 buttons: View Products, View Cart, Contact Us, About Us.
