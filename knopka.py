from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

def zakazlar():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='Mevalar', callback_data='fruits'),
        InlineKeyboardButton(text='Kiyimlar', callback_data='odejda'),
        InlineKeyboardButton(text='Ovqatlar', callback_data='ovqat'),
    )
    return markup



def mevalarbutton():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='olma', callback_data='maxsulot_olma'),
        InlineKeyboardButton(text='nok', callback_data='maxsulot_nok'),
        InlineKeyboardButton(text='gilos', callback_data='maxsulot_gilos'),
        InlineKeyboardButton(text='anor', callback_data='maxsulot_anor'),
        InlineKeyboardButton(text='uzum', callback_data='maxsulot_uzum'),
        InlineKeyboardButton(text='banan', callback_data='maxsulot_banan')
    )

    markup.add(
        InlineKeyboardButton(text='Orqaga', callback_data='back')
    )

    return markup

def kiyimlarbutton():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='shim', callback_data='maxsulot_shim'),
        InlineKeyboardButton(text='shortik', callback_data='maxsulot_shortik'),
        InlineKeyboardButton(text='kepka', callback_data='maxsulot_kepka'),
        InlineKeyboardButton(text='futbolka', callback_data='maxsulot_futbolka'),
        InlineKeyboardButton(text='sumka', callback_data='maxsulot_sumka'),
        InlineKeyboardButton(text='krasofka', callback_data='maxsulot_krasofka'),
    )
    markup.add(
        InlineKeyboardButton(text='Orqaga', callback_data='back')
    )

    return markup

def ovqatlarbutton():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='gamburger', callback_data='maxsulot_gamburger'),
        InlineKeyboardButton(text='hotdog', callback_data='maxsulot_hotdog'),
        InlineKeyboardButton(text='kfc', callback_data='maxsulot_kfc'),
        InlineKeyboardButton(text='osh', callback_data='maxsulot_osh'),
        InlineKeyboardButton(text='pitsa', callback_data='maxsulot_pizza'),
        InlineKeyboardButton(text='kabob', callback_data='maxsulot_kabob'),
    )
    markup.add(
        InlineKeyboardButton(text='Orqaga', callback_data='back')
    )

    return markup

def orqagamevalarbutton():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='Orqaga', callback_data='orqaga_mevalar'),
    )
    return markup

def orqagakiyimlarbutton():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='Orqaga', callback_data='orqaga_kiyimlar'),
    )
    return markup

def orqagaovqatlarbutton():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text='Orqaga', callback_data='orqaga_ovqatlar'),
    )
    return markup