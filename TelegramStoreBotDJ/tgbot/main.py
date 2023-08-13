from store.models import Goods, Order, Users, Status, StatusVariables

import telebot
import tgtoken
from markups import *
from messageTexts import *

token = tgtoken.value
bot = telebot.TeleBot(token)

goods = Goods.objects.all()
StatusVariables.objects.get_or_create(name='Не оплачено')

def showCatalog(message):
    availableItems = 0
    for item in goods:
        if item.is_available:
            availableItems = 1
            chooseSizeButton.callback_data = f'chooseSize{item.id}'

            textForItem = f'Товар: {item.cat}, <b>{item}</b>' + '\n' + f'Цена: <b>{str(int(item.price))}</b> р.'
            photo = open(f'../media/photos/{item.id}.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=photo, caption=textForItem,
                           parse_mode='html', reply_markup=chooseSizeKeyboard)

    if availableItems == 0:
        bot.send_message(message.chat.id, emptyCatalog)

def showCart(message):
    itemInCart = 0
    user_id = message.from_user.id
    user_orders = Users.objects.filter(userId=user_id).values_list('order__orderId', flat=True)
    for orderId in user_orders:
        status = Status.objects.filter(order=orderId).get()
        if str(status) == 'Не оплачено':

            delButton.callback_data = f'delete{orderId}'

            itemInCart = 1
            order = Order.objects.filter(orderId=orderId).get()
            photo = open(f'../media/photos/{order.goodsId}.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=photo, caption=f'{order.cartInfo()}',
                           parse_mode='html', reply_markup=cartMenu)
    if itemInCart == 0:
        bot.send_message(message.chat.id, emptyCart)

def showInfo(message):
    paidItem = 0
    user_id = message.from_user.id
    user_orders = Users.objects.filter(userId=user_id).values_list('order__orderId', flat=True)
    for orderId in user_orders:
        status = Status.objects.filter(order=orderId).get()
        if str(status) != 'Не оплачено' and str(status) != 'Сделка завершена':
            paidItem = 1
            order = Order.objects.filter(orderId=orderId).get()
            photo = open(f'../media/photos/{order.goodsId}.jpg', 'rb')
            bot.send_photo(message.chat.id, photo=photo, caption=f'{order.cartInfo() + curStatus.format(status)}',
                           parse_mode='html', reply_markup=markupMenu)
    if paidItem == 0:
        bot.send_message(message.chat.id, noPaidItems)

@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    for item in goods:
        if f'chooseSize{item.id}' == call.data:
            x = bot.send_message(call.message.chat.id, chooseSizeForItem.format(item), reply_markup=sizeKeyboard)
            bot.register_next_step_handler(x, chooseSize, item)

    if 'delete' in call.data:
        delItemId = str(call.data).split('delete')[-1]
        Order.objects.filter(orderId=delItemId).delete()
        bot.send_message(call.message.chat.id, deletedOrder.format(delItemId))

def chooseSize(message, item):
    if message.text == backMarkupBackItem.text:
        bot.send_message(message.chat.id, backInMainMenu, reply_markup=markupMenu)
    else:
        curSize = message.text
        curThing = item
        curThingId = item.id
        curPrice = item.price
        x = bot.send_message(message.chat.id, chooseSizeForItemVerify.format(curSize, curThing)+addToCartQuestion,
                             parse_mode='html', reply_markup=verifyKeyboard)
        bot.register_next_step_handler(x, verification, curSize, curThingId, curThing, curPrice)

def verification(message, curSize, curThingId, curThing, curPrice):
    if message.text == trueItem.text:
        userId = message.from_user.id
        order = Order.objects.create(goodsName=curThing, goodsId=curThingId, size=curSize, price=curPrice)
        Users.objects.create(userId=userId, order=order)
        Status.objects.create(order=order)
        bot.send_message(message.chat.id, addToCart, reply_markup=markupMenu)
    else:
        bot.send_message(message.chat.id, cancelOrder, reply_markup=markupMenu)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, startMessage, reply_markup=markupMenu)

@bot.message_handler(content_types=['text'])
def menuSetting(message):
    if message.text == catalogMenuItem.text:
        showCatalog(message)
    if message.text == cartMenuItem.text:
        showCart(message)
    if message.text == infoMenuItem.text:
        showInfo(message)

bot.get_updates()

bot.polling(none_stop=True)