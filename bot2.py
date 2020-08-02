import collections

from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater

class DialogBot(object):

    def __init__(self, token, generator):
        self.updater = Updater(token='1166049274:AAFkKOIo49YkF9Q9XuHlnuPnV6fwI245SvY')  # заводим апдейтера
        handler = MessageHandler(Filters.text | Filters.command, self.handle_message)
        self.updater.dispatcher.add_handler(handler)  # ставим обработчик всех текстовых сообщений
        self.handlers = collections.defaultdict(generator)  # заводим мапу "id чата -> генератор"

    def start(self):
        self.updater.start_polling()

    def handle_message(self, bot, update):
        print("Received", update.message)
        chat_id = update.message.chat_id
        if update.message.text == "/start":
            # если передана команда /start, начинаем всё с начала -- для
            # этого удаляем состояние текущего чатика, если оно есть
            self.handlers.pop(chat_id, None)
        if chat_id in self.handlers:
            # если диалог уже начат, то надо использовать .send(), чтобы
            # передать в генератор ответ пользователя
            try:
                answer = self.handlers[chat_id].send(update.message)
            except StopIteration:
                # если при этом генератор закончился -- что делать, начинаем общение с начала
                del self.handlers[chat_id]
                # (повторно вызванный, этот метод будет думать, что пользователь с нами впервые)
                return self.handle_message(bot, update)
        else:
            # диалог только начинается. defaultdict запустит новый генератор для этого
            # чатика, а мы должны будем извлечь первое сообщение с помощью .next()
            # (.send() срабатывает только после первого yield)
            answer = next(self.handlers[chat_id])
        # отправляем полученный ответ пользователю
        print("Answer: %r" % answer)
        bot.sendMessage(chat_id=chat_id, text=answer)

def dialog():
    hi = ["Здаров, я шар, че подсказать", "Хаю хай, я магический шар", "Нихао, раса: Шар, класс: Маг", "Салам попалам, Шар магический",
      "Добрейший денечек, Шар магический, к вашим услугам", "Какой у тебя вопрос, а, да, привет",
      "Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос", "Ну здарова, задавай свой вопрос"]
    names = ["Ну хоть не DiMoN.", "ЛОЛ.", "Кек.", "АХАХАХахахахахахаахахах", ")))))))0)))00))", "Пфффф, сори, я аж прыснул.",
        "Могло быть и хуже.", "Респект родителям, чисто приколдес.", "Так-то норм.", "Ладно, сойдет."]
    answer = yield ra.choice(hi), "Тебя как звать?"
    # убираем ведущие знаки пунктуации, оставляем только 
    # первую компоненту имени, пишем её с заглавной буквы
    name = answer.text.rstrip(".!").split()[0].capitalize()

    if name.lower() in ("коля", "николай", "колян", "kolya", "kolyan", "nikolay", "nikolai", "efremov", "ефремов"):
    	answer = yield "Просто бомба! Имя чисто пацанячье, сразу видно, ровный ты тип!"
    elif name.lower() == "DiMoN":
        answer = yield "Ну ты и конченый, конечно"
    else:
        answer = yield "Серьезно?", name + "?", ra.choice(names)
    answer = yield "Ну, привет", name
    answer = yield "Задавай вопрос, постараюсь не осуждать"

def ask_yes_or_no(question):
    """Спросить вопрос и дождаться ответа, содержащего «да» или «нет».

    Возвращает:
        bool
    """
    answer = yield question
    while not ("да" in answer.text.lower() or "нет" in answer.text.lower()):
        answer = yield "Так да или нет?"
    return "да" in answer.text.lower()


def discuss(name):
    answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
          "Это не главная твоя проблема", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
          "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
          "Определённо да", "Знаки говорят - да", "Сейчас нельзя предсказать", "Перспективы не очень хорошие"
          "Можешь быть уверен в этом", "Сконцентрируйся и спроси опять", "Весьма сомнительно",
          "В любом случае, это лучше, чем играть в хоккей", "Лучше покури кальян", "Всяко лучше, чем сидеть-пердеть",
          "Не знаю, но я слышал, что об этом могут знать в Глазове(если что это город)", "Это похоже на начало мема",
          "Это так же тупо, как верить во все, что говорят по федеральным каналам",
          "Это даже более мерзко, чем Соловьев и Киселев вместе взятые"]
    answer = yield ra.choice(answers)
    likes_article = yield from ask_yes_or_no("Есть еще вопросы? Да или Нет?")
    if likes_article:
        answer = yield "Чудно!"
    else:
        answer = yield "Чао Какао!."
    return answer


    dialog_bot.start()
