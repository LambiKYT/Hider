import telebot
import os

print("""
██╗░░██╗██╗██████╗░███████╗██████╗░
██║░░██║██║██╔══██╗██╔════╝██╔══██╗
███████║██║██║░░██║█████╗░░██████╔╝
██╔══██║██║██║░░██║██╔══╝░░██╔══██╗
██║░░██║██║██████╔╝███████╗██║░░██║
╚═╝░░╚═╝╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝""")

token = input("Введи токен своего телеграм бота: ")

bot = telebot.TeleBot(token)

@bot.message_handler(commands= ['start'])
def start(message):
    start_message = """👋 Привет! Данный бот создан с целью скрытия читов дистанционно на твоем пк!
    ✅ Если ты видишь это сообщение, то значит, что программа работает!
    📋 Ознакомиться со списком команд ты можешь по команде /help или /commands!"""
    bot.send_message(message.chat.id, start_message)

@bot.message_handler(commands= ['help', 'commands'])
def help(message):
    help_message = """📋 Список команд:
    /help - открыть этот список команд
    /cw - проверка работы бота
    /cmd - отправить команду в командную строку (Сначала пишем /cmd и отправляем, после чего пиши команду)
    /stop [programm] - закрыть программу (Пример: /stop taskmgr.exe)
    /close - прекращает работу программы и бота
    /hideall - запрещает запуск программ и не дает включить просмотр скрытых файлов (Everything, ShellBag, AnyDesk, Process Hacker, Диспетер задач)"""
    bot.send_message(message.chat.id, help_message)

@bot.message_handler(commands= ['cw'])
def cw(message):
    bot.send_message(message.chat.id, "✅ Бот работает отлично!")

@bot.message_handler(commands= ['cmd'])
def cmd(message):
    try:
        cmd = bot.send_message(message.chat.id, "🖊️ Введи команду: ")
        bot.register_next_step_handler(cmd, cmd2)
    except:
        bot.send_message(message.chat.id, "❌ Произошла ошибка!")

def cmd2(message):
    try:
        cmd = message.text
        os.system(f'{cmd}')
        bot.send_message(message.chat.id, "✅ Команда была успешно выполнена!")
    except:
        bot.send_message(message.chat.id, "❌ Произошла ошибка!")

@bot.message_handler(commands= ['stop'])
def stop(message):
    try:
        program = (message.text.split()[1])
        os.system(f'taskkill /f /im {program}')
        bot.send_message(message.chat.id, '✅Программа была успешно закрыта!')
    except:
        bot.send_message(message.chat.id, "❌ Произошла ошибка! Возможно программа не запущена или ее не существует.")
@bot.message_handler(commands= ['hideall'])
def hideall(message):
    msg = bot.send_message(message.chat.id, "✅ Скрытие активировано!")
    while True:
            os.system('taskkill /f /im everything.exe')
            os.system('taskkill /f /im shellbag_analyzer_cleaner.exe')
            os.system('taskkill /f /im processhacker.exe')
            os.system('taskkill /f /im taskmgr.exe')
            os.system('taskkill /f /im anydesk.exe')
            os.system(r'reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced\ /v Hidden /d 0 /f')
            bot.register_next_step_handler(msg, stophideall)
def stophideall(message):
    msg = message.text
    bot.send_message(message.chat.id, "✅ Остановлено!")

@bot.message_handler(commands= ['close'])
def stopall(message):
    bot.send_message(message.chat.id, '✅ Остановка прошла успешно!')
    os.system('taskkill /f /im hider.exe')
    os.system('taskkill /f /im python.exe')

bot.polling(none_stop= True)