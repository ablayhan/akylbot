# однострочный комментрий
"""
многострочный коментарий
"""

import telebot
import constants
import os

bot = telebot.TeleBot(constants.token)

print(bot.get_me())


def log(message, answer):
    print("\n ------------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст = {3}".format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id), message.text))


    print(answer)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('/start', 'help')
    user_markup.row('фото', 'аудио', '3D модель')
    user_markup.row('видео', 'голос', 'локация')

    bot.send_message(message.from_user.id, 'Привет. Я, бот. Запущен в тестовом режиме, и имею большинсво функций телеграм ботов, подробнее о том, что я могу, можете узнать нажав на кнопку "help"', reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'фото':
        directory = 'C:/Users/ww/Desktop/bot/photo'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
             img = open(directory + '/' + file, 'rb')
             bot.send_chat_action(message.from_user.id, 'upload_photo')
             bot.send_photo(message.from_user.id, img)
             img.close()

    elif message.text == 'аудио':
        audio = open("C:/Users/ww/Desktop/bot/audio/tu.mp3", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()

    elif message.text == '3D модель':
        directory = 'C:/Users/ww/Desktop/bot/documents'
        all_files_in_directory = os.listdir(directory)
        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()
    elif message.text == 'видео':
        video = open("C:/Users/ww/Desktop/bot/video/video.mp4", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_video')
        bot.send_audio(message.from_user.id, video)
        video.close()

    elif message.text == 'голос':
        voice = open("C:/Users/ww/Desktop/bot/voice/voice.ogg", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, voice)
        voice.close()
    elif message.text == 'локация':
        bot.send_chat_action(message.from_user.id, 'find_location')
        bot.send_location(message.from_user.id, 37.086247, 76.38088)

    elif message.text == 'help':
        bot.send_message(message.from_user.id, 'Доступны следующие функции:')
        bot.send_message(message.from_user.id, 'Договор')
        bot.send_message(message.from_user.id, 'Реквизиты')
        bot.send_message(message.from_user.id, 'Ссылку')
        bot.send_message(message.from_user.id, 'Событие')
        bot.send_message(message.from_user.id, 'Прайс')
        bot.send_message(message.from_user.id, 'Интересное')
        bot.send_message(message.from_user.id, 'Что послушать')
        bot.send_message(message.from_user.id, 'Что посмотреть')
        bot.send_message(message.from_user.id, 'Что почитать(отправлю вам название книги, что бы я отправил книгу, напишите мне "отправь книгу"')
        bot.send_message(message.from_user.id, 'Важно знать что это не команды, а обычный текст, ставить "/" не нужно.')

    elif message.text == 'реквизиты':
        bot.send_message(message.from_user.id, 'ТОО xx 010000, г.Астана, xx, xx, xx. Счёт номер: xxx БИН компании: xxx.  БИК xxxx КОд xx ')

    elif message.text == 'Договор':
        directory = 'C:/Users/ww/Desktop/bot/dogovor'
        all_files_in_directory = os.listdir(directory)
        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()

    elif message.text == 'Прайс':
        directory = 'C:/Users/ww/Desktop/bot/price'
        all_files_in_directory = os.listdir(directory)
        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()

    elif message.text == 'Ссылку':
        bot.send_message(message.from_user.id, 'https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%82_%D0%A8%D1%80%D1%91%D0%B4%D0%B8%D0%BD%D0%B3%D0%B5%D1%80%D0%B0')

    elif message.text == 'Событие':
        bot.send_message(message.from_user.id, 'xx.xx.xx г.Астана.xx.xx.xx')
    elif message.text == 'Интересное':
        bot.send_message(message.from_user.id, 'Man kann auch ganz burleske Fälle konstruieren. Eine Katze wird in eine Stahlkammer gesperrt, zusammen mit folgender Höllenmaschine (die man gegen den direkten Zugriff der Katze sichern muß): in einem Geigerschen Zählrohr befindet sich eine winzige Menge radioaktiver Substanz, so wenig, daß im Laufe einer Stunde vielleicht eines von den Atomen zerfällt, ebenso wahrscheinlich aber auch keines; geschieht es, so spricht das Zählrohr an und betätigt über ein Relais ein Hämmerchen, das ein Kölbchen mit Blausäure zertrümmert. Hat man dieses ganze System eine Stunde lang sich selbst überlassen, so wird man sich sagen, daß die Katze noch lebt, wenn inzwischen kein Atom zerfallen ist. Der erste Atomzerfall würde sie vergiftet haben. Die ψ-Funktion des ganzen Systems würde das so zum Ausdruck bringen, daß in ihr die lebende und die tote Katze (s.v.v.) zu gleichen Teilen gemischt oder verschmiert sind.Das Typische an solchen Fällen ist, daß eine ursprünglich auf den Atombereich beschränkte Unbestimmtheit sich in grobsinnliche Unbestimmtheit umsetzt, die sich dann durch direkte Beobachtung entscheiden läßt. Das hindert uns, in so naiver Weise ein „verwaschenes Modell“ als Abbild der Wirklichkeit gelten zu lassen. An sich enthielte es nichts Unklares oder Widerspruchsvolles. Es ist ein Unterschied zwischen einer verwackelten oder unscharf eingestellten Photographie und einer Aufnahme von Wolken und Nebelschwaden.')
    elif message.text == 'Что послушать':
        bot.send_message(message.from_user.id, 'https://www.youtube.com/watch?v=7C9EYka6fIU')
    elif message.text == 'Что посмотреть':
        bot.send_message(message.from_user.id, 'https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BC%D0%BD%D0%B8')
    elif message.text == 'Что почитать':
        bot.send_message(message.from_user.id, 'Жесткий век, Автор: Исай Калашников.')

    elif message.text == 'Отправь книгу':
        directory = 'C:/Users/ww/Desktop/bot/book'
        all_files_in_directory = os.listdir(directory)
        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()
    else:
        bot.send_message(message.from_user.id, 'Я Вас не понял, и вообще я еще не доработан')

bot.polling(none_stop=True, interval=0)

