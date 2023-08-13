from telebot import types

markupMenu = types.ReplyKeyboardMarkup(row_width=2)
catalogMenuItem = types.KeyboardButton('🛍️ Каталог')
infoMenuItem = types.KeyboardButton('📢 Инфо')
cartMenuItem = types.KeyboardButton('🛒 Корзина')
markupMenu.add(catalogMenuItem, infoMenuItem, cartMenuItem)

sizeKeyboard = types.ReplyKeyboardMarkup(row_width=2)
sizeS = types.KeyboardButton('S')
sizeM = types.KeyboardButton('M')
sizeL = types.KeyboardButton('L')
sizeXL = types.KeyboardButton('XL')
backMarkupBackItem = types.KeyboardButton('⏪ Назад')
sizeKeyboard.add(sizeS, sizeM, sizeL, sizeXL, backMarkupBackItem)

emptyMarkup = types.ReplyKeyboardRemove()

verifyKeyboard = types.ReplyKeyboardMarkup(row_width=2)
trueItem = types.KeyboardButton('ДА')
falseItem = types.KeyboardButton('НЕТ')
verifyKeyboard.add(trueItem, falseItem)

chooseSizeKeyboard = types.InlineKeyboardMarkup()
chooseSizeButton = types.InlineKeyboardButton('Выбрать размер', callback_data=None)
chooseSizeKeyboard.add(chooseSizeButton)

cartMenu = types.InlineKeyboardMarkup()
buyButton = types.InlineKeyboardButton('Оплатить', url='http://www.sberbank.ru/ru/person')
delButton = types.InlineKeyboardButton('Удалить', callback_data=None)
cartMenu.add(buyButton, delButton)
