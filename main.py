import telebot
token = "6781458985:AAGc5-FOdcf32qob04h0Q2X0Xk5Ocwbks3k"
name = 0
main = 0
one = 0
two = 0
three = 0
four = 0
five = 0
end = 0
bot = telebot.TeleBot(token)


# Первая локация, начало истории*******************************************************************
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуй путник, ты готов начать своё приключение(да или нет)?')
    bot.register_next_step_handler(message, start_story)


@bot.callback_query_handler(func=lambda callback: True)
def func(callback):
    if callback.data == 'btn_1':
        markup = telebot.types.InlineKeyboardMarkup()
        btn_1 = telebot.types.InlineKeyboardButton('Вступить в драку', callback_data='btn_3')
        btn_2 = telebot.types.InlineKeyboardButton('Не рисковать', callback_data='btn_4')
        markup.add(btn_1, btn_2)
        bot.send_message(callback.message.chat.id, 'Идя по лесу вы думаете о своём будущем, предках, истории вашей семьи. Ваши мысли прирывает громкий крик сзади. Оборачиваясь вы видите группу людей из трёх человек. Их внешний вид выглядит '
'довольно таинственно. Подходя к вам они двухсмыслено спрашивают не будет ли у вас пару монет, из под плаща вы можете заметить ручку кинжала. Вы начинаете оценивать их и думать как именно вам поступить.', reply_markup=markup)
    elif callback.data == 'btn_3':
        bot.send_message(callback.message.chat.id, 'Куда')
        bot.send_message(callback.message.chat.id, "Для продолжения введите ваше имя:")
        bot.register_next_step_handler(callback.message, story)
    elif callback.data == 'btn_4':
        bot.send_message(callback.message.chat.id, 'Оценив их вы решаете не влезать в драку и послушать их. Вы лезите в карман за имеющимися у вас деньгами как в этот момент в ваше лицо прилитает удар. Падая на землю вы можете замечаете следующий удар. У вас получается парировать его, но бандит резко бьёт вас ногой. Удар попадает вам прямо в грудь. Последнее что вы успеете заметить это летащий в вашу сторону удар ногой. Вы теряете сознание.')
        bot.send_message(callback.message.chat.id, 'Очнулись вы уже заполночь. Вы вспоминаете что с вами произошло. Вы начинаете осторожно вставать, вы чувствуете боль по всему телу. Вспоминая удар ногой вы поднимаете майку и замечаете разбитый Медальон на вашей шее. Сильно расстроевшись вы идетё домой думая: Правильно ли я поступил? Под расстроеные мысли вы доходите до дома. Зайдя в  дом вы быстро ложитесь в кровать и сами не замечаете как засыпаете.')
        bot.send_message(callback.message.chat.id, "Для продолжения введите ваше имя:")
        bot.register_next_step_handler(callback.message, story)
    elif callback.data == 'btn_2':
        bot.send_message(callback.message.chat.id, 'Непон')
        bot.send_message(callback.message.chat.id, "Для продолжения введите ваше имя:")
        bot.register_next_step_handler(callback.message, story)


def start_story(message):
    if message.text.lower() == 'да':
        markup = telebot.types.InlineKeyboardMarkup()
        btn_1 = telebot.types.InlineKeyboardButton('Пойти на прогулку в лес', callback_data='btn_1')
        btn_2 = telebot.types.InlineKeyboardButton('Пойти выпить', callback_data='btn_2')
        markup.add(btn_1, btn_2)
        bot.send_message(message.chat.id, 'Вы живёте в мире где каждая травинка пропитана магией, а на земле существует неизмерное количество волшебных существ. Всю жизнь вы жили в обычной деревне со своей семьёй на их фамильной земле. Сами вы как и все члены вашей семьи магией не обладаете. Семейное древо вашей семьи начиналось несколько веков назад, более ранние упоминания были утерены. Единственное что есть у вас это их семейная реликвия пренадлежащая твоему очень давнему предку - Медальон с повязкой на шее. С самого детства вам сказали чтобы ты берег его и никогда в жизни не снимал. Вы всегда помнили это и даже на ночь никогда не снимали Медальон.')
        bot.send_message(message.chat.id, 'Вы просыпаетесь рано утром. Быстро встав вы одеваетесь и спускаетесь на первый этаж. Заходя на кухню вы видите коробку посреди стола, как только вы подходите к ней появляются ваши родные и поздравляют с вашим восемнадцатилетием. Вы открываете коробку и видите там праздничный торт. Ваша семья завёт вас за стол и после чего вы весело  проводите время в кругу семьи. После этого вы выходите на улицу и думаете чем вам заняться.', reply_markup=markup)
    elif message.text.lower() == 'нет':
        bot.send_message(message.chat.id, 'Жаль😪😪')
        bot.send_message(message.chat.id, 'Прощай')
    elif message.text == name:
        bot.send_message(message.chat.id, f'{name}')
        bot.send_message(message.chat.id, '/1 - Лес Эльфов\n'
                                          '/2 - Пустыня Орков\n'
                                          '/3 - Подземелье Нечести\n'
                                          '/4 - Гора Дварфов\n'
                                          '/5 - Пиратская Бухта\n'
                                          '/end - Забытые развалины проклятого Королевства')

def story(message):
    global main
    name = message.text
    bot.send_message(message.chat.id, f'{name}')
    bot.send_message(message.chat.id, '/1 - Лес Эльфов\n'
                                        '/2 - Пустыня Орков\n'
                                        '/3 - Подземелье Нечести\n'
                                        '/4 - Гора Дварфов\n'
                                        '/5 - Пиратская Бухта\n'
                                        '/end - Забытые развалины проклятого Королевства')
    main = 1
# *********************************************************************************************************************************


# Лес Эльфов***********************************************************************************************************************
@bot.message_handler(commands=['1'])
def one(message):
    global one
    if main:
        markup = telebot.types.InlineKeyboardMarkup()
        btn_1 = telebot.types.InlineKeyboardButton('Пойти  направо', callback_data='btn_5')
        btn_2 = telebot.types.InlineKeyboardButton('Пойти налево', callback_data='btn_6')
        markup.add(btn_1, btn_2)
        bot.send_message(message.chat.id, 'a', reply_markup=markup)
        one = 1
    else:
        bot.send_message(message.chat.id, 'Для прохождения этой главы пройдите /start')


# **********************************************************************************************************************************


# Пустыня Орков***********************************************************************************************************************
@bot.message_handler(commands=['2'])
def two(message):
    global two
    if main:
        bot.send_message(message.chat.id, 'b')
        two = 1
    else:
        bot.send_message(message.chat.id, 'Для прохождения этой главы пройдите /start')
# ***************************************************************************************************************************************


# Подземелье нечести************************************************************************************************************************
@bot.message_handler(commands=['3'])
def three(message):
    global three
    if main:
        bot.send_message(message.chat.id, 'c')
        three = 1
    else:
        bot.send_message(message.chat.id, 'Для прохождения этой главы пройдите /start')
# *******************************************************************************************************************************************


# Гора Дварфов******************************************************************************************************************************
@bot.message_handler(commands=['4'])
def four(message):
    global four
    if main:
        bot.send_message(message.chat.id, 'd')
        four = 1
    else:
        bot.send_message(message.chat.id, 'Для прохождения этой главы пройдите /start')
# ************************************************************************************************************************************************


# Пиратская Бухта******************************************************************************************************************************
@bot.message_handler(commands=['5'])
def five(message):
    global five
    if main:
        bot.send_message(message.chat.id, 'e')
        five = 1
    else:
        bot.send_message(message.chat.id, 'Для прохождения этой главы пройдите /start')
# ************************************************************************************************************************************************************************************************************************************************************


# Забытые развалины проклятого Королевства, конец истории# ************************************************************************************************************************************************
@bot.message_handler(commands=['end'])
def end(message):
    if one == 1 and two == 1 and three == 1 and four == 1 and five == 1:
        bot.send_message(message.chat.id, 'end')
    else:
        bot.send_message(message.chat.id, 'Для прохождения этой главы пройдите главы: /1\n /2\n /3\n /4\n /5')
# ************************************************************************************************************************************************************************************************************************************************************


bot.infinity_polling()
