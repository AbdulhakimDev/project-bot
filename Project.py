import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import telebot
from telebot import types
import redis as r

bot = telebot.TeleBot('1297455433:AAGsj72jzZtXxKm13J-3RRaNWVYVs8Oxkvk'); #bot tokenini kiriting
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
@bot.message_handler(commands=['start'])
def welcome(m):
    cid = m.chat.id
    markup = types.InlineKeyboardMarkup()
    b = types.InlineKeyboardButton("📝Ro'yhatdan o'tish",callback_data='registry')
    c = types.InlineKeyboardButton("ℹYordam",callback_data='help')
    markup.add(b,c)
    nn = types.InlineKeyboardButton("Admin", url='https://t.me/Gunnersaur_UZ')
    oo = types.InlineKeyboardButton("📡Kanal", url='https://telegram.me/EnjoyChemistry_channel')
    markup.add(nn,oo)
    id = m.from_user.id
    redis.sadd('memberspy',id)
    bot.send_chat_action(cid, "typing")
    bot.send_message(cid, "Salom \n\n EnjoyChemistry botga xush kelibsiz \n\n Avval ro'yhatdan o'ting:)", disable_notification=True, reply_markup=markup)
    @bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "registry":
        .... #bu yerda ma'lumotlar saqlab olinmoqda...
        bot.edit_message(call.message.chat.id, "Ismingizni yozib jo'nating");
else:
    bot.send_message(message.from_user.id, "Men sizni tushunmayabman. 👉 /help.");
    name = '';
surname = '';
age = 0;
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Ismingiz nima?");
        bot.register_next_step_handler(message, get_name); # get_name funksiyasi ishlatilmoqda
    else:
        bot.send_message(message.from_user.id, 'Oldin royhatdan oting deb yozing');

def get_name(message):
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Familiyangiz nima?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message('Yoshingiz nechida?');
    bot.register_next_step_handler(message, get_age);
    def get_age(message):
    global age;
    while age == 0:
        try:
             age = int(message.text) #Yoshi to'g'ri kiritilganini tekshiramiz
        except Exception:
             bot.send_message(message.from_user.id, 'Sonlar bilan yozing, iltimos');
      bot.send_message(message.from_user.id, 'Siz'+str(age)+' yoshdasiz, ism va familiyangiz '+name+' '+surname+'?')
      def get_age(message):
    global age;
    while age == 0: 
    try:
             age = int(message.text)
        except Exception:
             bot.send_message(message.from_user.id, 'Sonlar bilan kiriting');
      keyboard = types.InlineKeyboardMarkup(); 
      key_yes = types.InlineKeyboardButton(text='Ha', callback_data='yes'); # «Ha» tugmachasi qo'yildi
      keyboard.add(key_yes); #bu yerda klaviyaturaga tugmacha qo'yilmoqda. O'zgartirsangiz bo'ladi
      key_no= types.InlineKeyboardButton(text='Yo*q', callback_data='no');
      keyboard.add(key_no);
      question = 'Siz '+str(age)+' yoshdasiz, ismingiz va familiyangiz '+name+' '+surname+'?';
      bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
      @bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        .... #bu yerda ma'lumotlar saqlab olinmoqda...
        bot.send_message(call.message.chat.id, 'eslab qoldim : )');
    elif call.data == "no":
         ... #qayta F.I.O so'raladi agar 'no' call.data bosgan bo'lsa
    bot.polling(none_stop=True, interval=0)
