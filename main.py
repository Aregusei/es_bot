import telebot
from telebot import types

bot = telebot.TeleBot('6173857823:AAHTo02qVRb4cLzswgN88gi-MxvbEZlKcqs')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hola!, {message.from_user.first_name}!\nPuedes encontrar respuestas a tus preguntas utilizando los comandos que se encuentran en el menú desplegable a la izquierda del campo de mensaje de entrada.',disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['website'])
def website(message):
    bot.send_message(message.chat.id, '⛓ <a href="https://c-patex.com/es/latin-america">Sitio web</a> de ecosistemas <b>C-Patex</b>\n Para obtener más información, consulte en <a href="https://t.me/cpatexespanol/9362"><b>F.A.Q</b></a>  👈',disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['withdrawal'])
def withdrawal(message):
    bot.send_message(message.chat.id, '💰<b>Todos los retiros</b> se procesan dentro de las 3 horas. Si su retiro se retrasa, comuníquese con soporte (detalles en /contact de contacto)\nPara obtener más información, consulte en <a href="https://t.me/cpatexespanol/9362"><b>F.A.Q</b></a> 👈', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['fees'])
def fees(message):
    bot.send_message(message.chat.id, '💲 Puede encontrar una <b>ista detallada de comisiones</b> <a href="https://c-patex.com/es/fees">aquí</a>.\n Para obtener más información, consulte en <a href="https://t.me/cpatexespanol/9362"><b>F.A.Q</b></a> 👈', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['kyc'])
def kyc(message):
    bot.send_message(message.chat.id, '👤 <b>El límite de tiempo máximo</b>  para las verificaciones es de ~24 horas.  Sin embargo, por lo general, las solicitudes se procesan mucho más rápido.\nPara obtener más información, consulte en <a href="https://t.me/cpatexespanol/9362"><b>F.A.Q</b></a> 👈', disable_web_page_preview=True, parse_mode='HTML')


@bot.message_handler(commands=['deposit'])
def deposit(message):  bot.send_message(message.chat.id, '🪙 Si su depósito <b> no ha sido acreditado</b>, proporciónenos los detalles detallados de la transacción <b> (CANTIDAD, VALOR, HASH) </b>al correo electrónico: 📬 support@c-patex.com\nPara obtener más información, consulte en <a href="https://t.me/cpatexespanol/9362"><b>F.A.Q</b></a> 👈', disable_web_page_preview=True, parse_mode='HTML')


@bot.message_handler(commands=['contact'])
def contact(message):   bot.send_message(message.chat.id, 'Puede contactarnos por correo — 📬 support@c-patex.com\n🌐 Crear un ticket de soporte en e <a href="https://c-patex.com/es/latin-america">sitio web</a>\n📱 O comuníquese con un agente de soporte en <a href="http://t.me/Cpatex01">Telegram</a>', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['two_factor_auth'])
def  two_factor_auth(message):   bot.send_message(message.chat.id, '👤Para deshabilitar <b>2FA</b> proporcione <b> ambos lados de su documento (pasaporte, tarjeta de identificación o licencia de conducir) y 🤳  una selfie de usted sosteniendo el documento y una hoja de papel con el siguiente texto escrito a mano "C-PATEX.COM",  fecha actual y tu firma. </b>\nEnvíenos todas las fotos a support@c-patex.com.\nPara obtener más información, consulte en <a href="https://t.me/cpatexespanol/9362"><b>F.A.Q</b></a> 👈\n', disable_web_page_preview=True, parse_mode='HTML')

@bot.message_handler(commands=['docs'])

def docs(message):   bot.send_message(message.chat.id, '📝Enlace al <a href="https://c-patex.com/files/en/wp.pdf?v=1.2"><b>documento técnico</b></a>\n🔩 Enlace a <a href="https://patex.io/docs/Patex%20Tokenomics.pdf"><b>tokenomics</b></a>', disable_web_page_preview=True, parse_mode='HTML')


@bot.message_handler(commands=['socials'])
def socials(message):   bot.send_message(message.chat.id, '📜 <a href="https://linktr.ee/patex_ecosystem"><b>Linktr.ee</b></a>\n \
— <a href="https://www.facebook.com/patexecosystem"><b>Facebook</b></a>\n \
— <a href="https://www.instagram.com/patex_ecosystem/"><b>Instagram</b></a> \n \
— <a href="https://www.youtube.com/channel/UCLmHyM6kZ5bViyh7my6ZkpA"><b>YouTube</b></a> \n \
— <a href="https://medium.com/@patex_ecosystem"><b>Medium</b></a> \n \
— <a href="https://twitter.com/patex_ecosystem"><b>Twitter</b></a> \n \
       \n \
📝<a href="https://linktr.ee/patex_ecosystem"><b>Patex Chats</b></a>\n \
— <a href="https://t.me/cpatexeng"><b>TG Channel (English)</b></a> \n \
— <a href="https://t.me/cpatexexchange"><b>TG Channel (Español / Portuguese)</b></a> \n \
— <a href="https://t.me/cpatexespanol"><b>TG Chat (Español)</b></a> \n \
— <a href="https://t.me/cpatexportuguese"><b>TG Chat (Portuguese)</b></a> \n \
— <a href="https://t.me/+HmW0DJAYl1YzMjAy"><b>TG Chat (English)</b></a> \n \
— <a href="https://t.me/cpatexcis"><b>TG Chat (CIS)</b></a>', disable_web_page_preview=True, parse_mode='HTML')

bot.polling(none_stop=True, interval=1)