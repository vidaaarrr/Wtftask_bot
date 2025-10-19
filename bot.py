import os
import json
import telebot
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)
TASKS_FILE = "tasks.json"

if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "w") as f:
        json.dump({"tasks": []}, f)

def load_tasks():
    with open(TASKS_FILE, "r") as f:
        return json.load(f)["tasks"]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump({"tasks": tasks}, f, indent=2)

@bot.message_handler(func=lambda m: not m.text.startswith("/"))
def add_task(message):
    tasks = load_tasks()
    tasks.append({"text": message.text, "done": False})
    save_tasks(tasks)
    bot.reply_to(message, f"✅ تسک اضافه شد ({len(tasks)}): {message.text}")

@bot.message_handler(commands=["list"])
def list_tasks(message):
    tasks = load_tasks()
    active_tasks = [t for t in tasks if not t["done"]]
    if not active_tasks:
        bot.reply_to(message, "✨ هیچ تسک فعالی نداری!")
        return
    reply = "🧾 لیست تسک‌ها:

"
    for idx, task in enumerate(active_tasks, start=1):
        reply += f"{idx}. {task['text']}
"
    bot.reply_to(message, reply)

@bot.message_handler(commands=["done"])
def done_task(message):
    tasks = load_tasks()
    try:
        index = int(message.text.split()[1]) - 1
    except (IndexError, ValueError):
        bot.reply_to(message, "❗ فرمت اشتباه — از دستور /done [شماره] استفاده کن.")
        return
    active = [t for t in tasks if not t["done"]]
    if index < 0 or index >= len(active):
        bot.reply_to(message, "❗ شماره تسک معتبر نیست.")
        return
    target = active[index]
    for t in tasks:
        if t == target:
            t["done"] = True
            break
    save_tasks(tasks)
    bot.reply_to(message, f"✅ تسک '{target['text']}' انجام شد.")

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "👋 سلام هستی! هرچی بنویسی میشه تسک جدیدت. دستورها:
/list برای دیدن تسک‌ها
/done [شماره] برای تیک خوردن.")

print("🤖 Bot started successfully...")
bot.infinity_polling()
