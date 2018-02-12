import glob
import telebot
import commands_executor
from telebot import types
import props_bot

bot = telebot.TeleBot(props_bot.token)


def log_files(path):
    return glob.glob(path + "/*.log")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    print(message.text)
    if message.text == 'logs':
        onlyfiles = log_files(props_bot.logs_path)
        print(onlyfiles)
        logs = log_files(props_bot.logs_path)
        keyboard = types.InlineKeyboardMarkup()
        for log in logs:
            callback_button = types.InlineKeyboardButton(text=log, callback_data="show|" + log)
            keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Choose a log file:", reply_markup=keyboard)
    elif message.text == 'system':
        keyboard = types.InlineKeyboardMarkup()
        memory_but = types.InlineKeyboardButton(text='Ram free', callback_data='ram')
        cpu_but = types.InlineKeyboardButton(text='Cpu application usage', callback_data='cpu')
        keyboard.add(memory_but)
        keyboard.add(cpu_but)
        bot.send_message(message.chat.id, "Choose a log file:", reply_markup=keyboard)
    elif message.text == 'info':
        data = commands_executor.system_info()
        bot.send_message(chat_id=message.chat.id, text=data)
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        keyboard.row("logs", "system", "info")
        bot.send_message(message.chat.id, "Main menu", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data.startswith('show'):
            log_file_name = call.data[5:]
            data = commands_executor.ge_last_rows(log_file_name)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=data)
        elif call.data == 'cpu':
            data = commands_executor.cpu_application()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=data)
        elif call.data == 'ram':
            data = commands_executor.memory_stat()
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=data)
    elif call.inline_message_id:
        if call.data == "test":
            bot.edit_message_text(inline_message_id=call.inline_message_id, text="Splash")


def star_bot():
    bot.polling(none_stop=True)


if __name__ == '__main__':
    try:
        star_bot()
    except Exception as e:
        print(e)
        star_bot()
