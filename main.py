
from flask import Flask
import threading

flask_app = Flask('')
@flask_app.route('/')
def home(): return "I am alive"

def run_flask():
    flask_app.run(host='0.0.0.0', port=8080)

# این خط را درست قبل از app.run_polling() قرار دهید:







from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import json


from flask import Flask
import threading

flask_app = Flask('')
@flask_app.route('/')
def home(): return "I am alive"

def run_flask():
    flask_app.run(host='0.0.0.0', port=8080)

# این خط را درست قبل از app.run_polling() قرار دهید:



import os
TOKEN = os.environ.get("BOT_TOKEN")





with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for i, p in enumerate(products):
        keyboard.append([InlineKeyboardButton(p["name"], callback_data=str(i))])
    await update.message.reply_text(
        "💎 محصولات طلافروشی:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def show_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    p = products[int(query.data)]

    final_price = p["price_base"] + p["labor_fee"] + p["tax"]

    text = (
        f"💍 {p['name']}\n\n"
        f"قیمت پایه: {p['price_base']:,} تومان\n"
        f"اجرت: {p['labor_fee']:,} تومان\n"
        f"مالیات: {p['tax']:,} تومان\n\n"
        f"💰 قیمت نهایی: {final_price:,} تومان"
    )

    await query.message.reply_photo(photo=p["photo"], caption=text)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(show_product))
    print("🤖 Bot is running...")
  threading.Thread(target=run_flask).start()
    
    
    app.run_polling()




