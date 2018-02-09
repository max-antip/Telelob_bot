from array import array

from telebot import types
import props_bot
import telebot

bot = telebot.TeleBot(props_bot.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button4 = types.KeyboardButton(text="🎞")
    button5 = types.KeyboardButton(text="🔦")
    keyboard.row("🚗", "🚲", "⏱")
    keyboard.add(button4)
    keyboard.add(button5)
    bot.send_message(message.chat.id, "Я – сообщение из обычного режима", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Logging")
    # Если сообщение из инлайн-режима
    elif call.inline_message_id:
        if call.data == "test":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Бдыщь")


if __name__ == '__main__':
    bot.polling(none_stop=True)
