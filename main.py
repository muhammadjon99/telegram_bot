import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import CallbackQuery
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from knopkalar import asosiyknopka
from knopka import *

# 🔹 Bot tokenini kiritish (BotFather'dan olingan tokenni shu yerga qo'ying)
TOKEN = "7888619093:AAFAnOGdkdYNdKyZZPZgbcOIHs-wTsiP6CI"

# 🔹 Bot va dispatcher yaratish
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# 🔹 Logging yoqish
logging.basicConfig(level=logging.INFO)

# 🔹 Tugmalar yaratish (Menyu)
menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(KeyboardButton("ℹ️ Bot haqida"), KeyboardButton("💰 Pul ishlash"))
menu.add(KeyboardButton("🆘 Yordam"), KeyboardButton("📞 Admin bilan bog‘lanish"))

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(f"Salom, {message.from_user.first_name}! 👋\n\nMen yordamchi botman. Quyidagi menyudan kerakli bo‘limni tanlang:", reply_markup=zakazlar())

@dp.callback_query_handler(lambda call: 'fruits' in call.data)
async def getmeva(callback: CallbackQuery):
    chatid = callback.message.chat.id
    messageid = callback.message.message_id
    await bot.edit_message_text(chat_id=chatid, message_id=messageid, text='Mevalarni tanlang',
                                reply_markup=mevalarbutton())


@dp.callback_query_handler(lambda call: 'odejda' in call.data)
async def getkiyim(callback: CallbackQuery):
    chatid = callback.message.chat.id
    messageid = callback.message.message_id
    await bot.edit_message_text(chat_id=chatid, message_id=messageid, text='Kiyim tanlang',
                                reply_markup=kiyimlarbutton())

@dp.callback_query_handler(lambda call: 'ovqat' in call.data)
async def getovqat(callback: CallbackQuery):
    chatid = callback.message.chat.id
    messageid = callback.message.message_id
    await bot.edit_message_text(chat_id=chatid, message_id=messageid, text='Ovqat tanlang',
                                reply_markup=ovqatlarbutton())

@dp.callback_query_handler(lambda call: 'maxsulot' in call.data)
async def getolma(callback: CallbackQuery):
    chatid = callback.message.chat.id
    maxsulot = callback.data.split('_')[1]
    messageid = callback.message.message_id
    await bot.delete_message(chat_id=chatid, message_id=messageid)
    if maxsulot == 'olma':
        olma = open('olma1.jpg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='qizil olma narxi 4000 som', photo=olma,
                             reply_markup=orqagamevalarbutton())
    elif maxsulot == 'nok':
        nok = open('nok.jpg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Nok narxi 8000 som', photo=nok,
                             reply_markup=orqagamevalarbutton())
    elif maxsulot == 'gilos':
        gilos = open('gilos.jpg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Gilos narxi 7000 som', photo=gilos,
                             reply_markup=orqagamevalarbutton())
    elif maxsulot == 'anor':
        anor = open('anor.jpg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Anor narxi 6000 som', photo=anor,
                             reply_markup=orqagamevalarbutton())
    elif maxsulot == 'uzum':
        uzum = open('uzum.jpeg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Uzum narxi 10000 som', photo=uzum,
                             reply_markup=orqagamevalarbutton())
    elif maxsulot == 'banan':
        banan = open('banan.jpeg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Banan narxi 16000 som', photo=banan,
                             reply_markup=orqagamevalarbutton())
    elif maxsulot == 'shim':
        shim = open('shim.jpg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Shim narxi 70000 som', photo=shim,
                             reply_markup=orqagakiyimlarbutton())
    elif maxsulot == 'shortik':
        shortik = open('shortik.jpg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Shortik narxi 45000 som', photo=shortik,
                             reply_markup=orqagakiyimlarbutton())
    elif maxsulot == 'kepka':
        kepka = open('kepka.jpg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Kepka narxi 40000 som', photo=kepka,
                             reply_markup=orqagakiyimlarbutton())
    elif maxsulot == 'futbolka':
        futbolka = open('futbolka.jpg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Futbolka narxi 50000 som', photo=futbolka,
                             reply_markup=orqagakiyimlarbutton())
    elif maxsulot == 'sumka':
        sumka = open('sumka.jpeg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Sumka narxi 99000 som', photo=sumka,
                             reply_markup=orqagakiyimlarbutton())
    elif maxsulot == 'krasofka':
        krasofka = open('krasofkalar.jpeg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Krasofka narxi 290000 som', photo=krasofka,
                             reply_markup=orqagakiyimlarbutton())

    elif maxsulot == 'gamburger':
        gamburger = open('gamburger.jpg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Gamburger narxi 26000 som', photo=gamburger,
                             reply_markup=orqagaovqatlarbutton())
    elif maxsulot == 'hotdog':
        hotdog = open('hotdog.jpg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Hotdog narxi 15000 som', photo=hotdog,
                             reply_markup=orqagaovqatlarbutton())
    elif maxsulot == 'kfc':
        kfc = open('kfc.jpg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Kfc narxi 45000 som', photo=kfc,
                             reply_markup=orqagaovqatlarbutton())
    elif maxsulot == 'osh':
        osh = open('osh.jpg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Osh narxi 50000 som', photo=osh,
                             reply_markup=orqagaovqatlarbutton())
    elif maxsulot == 'pizza':
        pitsa = open('pizza.jpg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Pizza narxi 95000 som', photo=pitsa,
                             reply_markup=orqagaovqatlarbutton())
    elif maxsulot == 'kabob':
        kabob = open('kabob.jpg', 'rb')
        await bot.send_photo(chat_id=chatid, caption='Kabob narxi 10000 som', photo=kabob,
                             reply_markup=orqagaovqatlarbutton())


@dp.callback_query_handler(lambda call: 'back' in call.data)
async def getback(callback: CallbackQuery):
    chatid = callback.message.chat.id
    messageid = callback.message.message_id
    await bot.edit_message_text(chat_id=chatid, message_id=messageid, text='Bosh menu', reply_markup=zakazlar())





@dp.callback_query_handler(lambda call: 'orqaga' in call.data)
async def getorqaga(callback: CallbackQuery):
    chatid = callback.message.chat.id
    messageid = callback.message.message_id

    orqaga = callback.data.split('_')[1]
    await bot.delete_message(chat_id=chatid, message_id=messageid)
    if orqaga == 'mevalar':
        await bot.send_message(chat_id=chatid, text='Mevalar', reply_markup=mevalarbutton())
    elif orqaga == 'kiyimlar':
        await bot.send_message(chat_id=chatid, text='Kiyimlar', reply_markup=kiyimlarbutton())
    elif orqaga == 'ovqatlar':
        await bot.send_message(chat_id=chatid, text='Ovqatlar', reply_markup=ovqatlarbutton())


# 🔹 /start buyrug‘iga javob
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Salom, {message.from_user.first_name}! 👋\n\nMen yordamchi botman. Quyidagi menyudan kerakli bo‘limni tanlang:", reply_markup=menu)

# 🔹 Tugmalar uchun javob
@dp.message_handler(lambda message: message.text == "ℹ️ Bot haqida")
async def about_bot(message: types.Message):
    await message.reply("Bu bot sizga kerakli ma'lumotlarni taqdim etadi.")

@dp.message_handler(lambda message: message.text == "💰 Pul ishlash")
async def make_money(message: types.Message):
    await message.reply("Siz bot orqali pul ishlash usullarini o‘rganishingiz mumkin!")

@dp.message_handler(lambda message: message.text == "🆘 Yordam")
async def help_user(message: types.Message):
    await message.reply("Agar sizga yordam kerak bo‘lsa, admin bilan bog‘laning.")

@dp.message_handler(lambda message: message.text == "📞 Admin bilan bog‘lanish")
async def contact_admin(message: types.Message):
    await message.reply("Admin bilan bog‘lanish uchun: @ibroximov_693")

@dp.message_handler(commands=['token'])
async def send_welcome(message: types.Message):
    await message.reply(f"Salom, {message.from_user.first_name}! 👋\n\nMen yordamchi botman. Quyidagi menyudan kerakli bo‘limni tanlang:", reply_markup=asosiyknopka())


# 🔹 Botni ishga tushirish
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)