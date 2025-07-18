
from aiogram import Router, F
from aiogram.types import Message, WebAppData

router = Router()

@router.message(F.web_app_data)
async def handle_web_app_data(message: Message):
    data = message.web_app_data.data
    try:
        import json
        user_data = json.loads(data)
        name = user_data.get("name")
        email = user_data.get("email")
        phone = user_data.get("phone")
        broker = user_data.get("broker")
        lang = user_data.get("lang", "ar")

        print(f"🟢 New user: {name}, {email}, {phone}, {broker}")

        if lang == "en":
            await message.answer("✅ Registration successful!\nWelcome aboard.")
        else:
            await message.answer("✅ تم تسجيلك بنجاح!\nمرحباً بك.")
    except Exception as e:
        await message.answer("❌ حدث خطأ أثناء معالجة البيانات.")
        print("❌ Error parsing web_app_data:", e)
