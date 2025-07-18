from aiogram import types, Dispatcher
from aiogram.types import Message, WebAppData

# دالة التعامل مع أمر /start
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(
            text="📋 تسجيل",
            web_app=types.WebAppInfo(url="https://ramybot.onrender.com/form_ar.html" if message.from_user.language_code == 'ar' else "https://ramybot.onrender.com/form_en.html")
        )
    )
    await message.answer("اختر اللغة وابدأ التسجيل:", reply_markup=keyboard)

# دالة استقبال بيانات WebApp
async def webapp_data_handler(message: Message):
    try:
        data = message.web_app_data.data  # JSON string
        print("📥 بيانات التسجيل:", data)
        
        # إرسال رسالة للمستخدم حسب اللغة
        lang = message.from_user.language_code
        if lang == "ar":
            await message.answer("✅ تم التسجيل بنجاح، شكرًا لك!")
        else:
            await message.answer("✅ Registration successful, thank you!")

    except Exception as e:
        print("❌ حدث خطأ في استقبال البيانات:", e)
        await message.answer("❌ حدث خطأ أثناء معالجة بيانات التسجيل.")

# تسجيل الهاندلرز
def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start"])
    dp.register_message_handler(webapp_data_handler, content_types=types.ContentType.WEB_APP_DATA)
