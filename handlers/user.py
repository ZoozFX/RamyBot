from aiogram import Router, F
from aiogram.types import Message, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
import json

router = Router()

@router.message(Command("start"))
async def start_command(message: Message):
    lang_code = message.from_user.language_code or "en"
    if lang_code.startswith("ar"):
        button = KeyboardButton(
            text="📋 تسجيل البيانات",
            web_app=WebAppInfo(url="https://frabjous-manatee-ae3536.netlify.app/form_ar.html")
        )
        markup = ReplyKeyboardMarkup(keyboard=[[button]], resize_keyboard=True)
        await message.answer("مرحبًا بك! اضغط على الزر بالأسفل لتسجيل بياناتك.", reply_markup=markup)
    else:
        button = KeyboardButton(
            text="📋 Register Data",
            web_app=WebAppInfo(url="https://frabjous-manatee-ae3536.netlify.app/form_en.html")
        )
        markup = ReplyKeyboardMarkup(keyboard=[[button]], resize_keyboard=True)
        await message.answer("Welcome! Click the button below to register your info.", reply_markup=markup)

@router.message(F.web_app_data)
async def on_webapp_data(message: Message):
    try:
        data = json.loads(message.web_app_data.data)
        name = data.get("name")
        email = data.get("email")
        phone = data.get("phone")
        broker = data.get("broker")
        lang = data.get("lang", "en")

        # هنا يتم طباعة البيانات ويمكنك حفظها لاحقًا بأي طريقة
        print("✅ بيانات المستخدم:")
        print(f"الاسم: {name}")
        print(f"البريد: {email}")
        print(f"الهاتف: {phone}")
        print(f"الوسيط: {broker}")
        print(f"اللغة: {lang}")

        if lang == "ar":
            await message.answer("✅ تم التسجيل بنجاح")
        else:
            await message.answer("✅ Registration completed successfully")

    except Exception as e:
        print("❌ خطأ في استقبال البيانات:", e)
        await message.answer("حدث خطأ أثناء معالجة البيانات. حاول مرة أخرى.")
