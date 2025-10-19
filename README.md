# Telegram Task Bot – نسخه شخصی هستی

یک ربات مینیمال برای مدیریت تسک‌ها در تلگرام.
هر پیام → تسک جدید
/list → نمایش همه تسک‌های باز
/done [شماره] → تیک‌زدن تسک

## نصب
```bash
pip install -r requirements.txt
python bot.py
```

## Deploy رایگان در Render
1. فایل‌های پروژه را به GitHub پوش کنید.
2. به https://render.com بروید → New Web Service.
3. ریپو را انتخاب کنید.
4. در محیط سرویس، متغیر محیطی اضافه کنید:
   ```
   BOT_TOKEN=توکن‌ربات‌خودت
   ```
5. Deploy را بزنید و تمام 🎯
