from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = "8943672380:AAGyuzgm2cCRKvKmXRkYgD-3kHoQOh5L1aM"
usuarios_esperando_codigo = set()

CODIGO_CORRECTO = "1234"
keyboard = [
    ["📺 Activar TV", "🔐 Login"],
    ["👤 Cuenta", "📊 Stats"],
    ["❓ Ayuda"]
]

markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        f"✨ Bienvenido {user.first_name}",
        reply_markup=markup
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📺 Activar TV":
        usuarios_esperando_codigo.add(update.effective_user.id)
        await update.message.reply_text("🔑 Envia el código de activación")

    elif text == "🔐 Login":
        await update.message.reply_text("Login correcto")

    elif text == "👤 Cuenta":
        await update.message.reply_text("Información de cuenta")

    elif text == "📊 Stats":
        await update.message.reply_text("Tus estadísticas")

    elif text == "❓ Ayuda":
        await update.message.reply_text("Centro de ayuda")
    elif update.effective_user.id in usuarios_esperando_codigo:

        if text == CODIGO_CORRECTO:
                await update.message.reply_text("✅ TV activada correctamente")
        else:
                await update.message.reply_text("❌ Código incorrecto")

    usuarios_esperando_codigo.remove(update.effective_user.id)

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.add_handler(
    MessageHandler(filters.TEXT, buttons)
)

print("BOT ONLINE")

app.run_polling()
