import random as ra
import telebot

bot = telebot.TeleBot('1166049274:AAFkKOIo49YkF9Q9XuHlnuPnV6fwI245SvY')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Кого там опять несет')

@bot.message_handler()
def first(message):
	answer = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
          "Это не главная твоя проблема", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
          "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
          "Определённо да", "Знаки говорят - да", "Сейчас нельзя предсказать", "Перспективы не очень хорошие"
          "Можешь быть уверен в этом", "Сконцентрируйся и спроси опять", "Весьма сомнительно",
          "В любом случае, это лучше, чем играть в хоккей", "Лучше покури кальян", "Всяко лучше, чем сидеть-пердеть",
          "Не знаю, но я слышал, что об этом могут знать в Глазове(если что это город)", "Это похоже на начало мема",
          "Это так же тупо, как верить во все, что говорят по федеральным каналам",
          "Это даже более мерзко, чем Соловьев и Киселев вместе взятые"]

	hi = ["Здаров, я шар, че подсказать", "Хаю хай, я магический шар", "Нихао, раса: Шар, класс: Маг", "Салам попалам, Шар магический",
      "Добрейший денечек, Шар магический, к вашим услугам", "Какой у тебя вопрос, а, да, привет",
      "Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос", "Ну здарова, задавай свой вопрос"]

	names = ["Ну хоть не DiMoN.", "ЛОЛ.", "Кек.", "АХАХАХахахахахахаахахах", ")))))))0)))00))", "Пфффф, сори, я аж прыснул.",
        "Могло быть и хуже.", "Респект родителям, чисто приколдес.", "Так-то норм.", "Ладно, сойдет."]

	bot.send_message(message.chat.id, ra.choice(hi))
	bot.send_message(message.chat.id, "Тебя как звать?")

	name = message.text("")

	if name.lower() in ("коля", "николай", "колян", "kolya", "kolyan", "nikolay", "nikolai", "efremov", "ефремов"):
		bot.send_message(message.chat.id, "Просто бомба! Имя чисто пацанячье, сразу видно, ровный ты тип!")

	elif name == "DiMoN":
		bot.send_message(message.chat.id, "Сори, конечно, но ты конченый.")

	else:
		bot.send_message(message.chat.id, "Серьезно?", name + "?", ra.choice(names))
	bot.send_message(message.chat.id, "Ну, привет", name)
	bot.send_message(message.chat.id, "Задавай вопрос, постараюсь не осуждать")

	ask = message.text()

	bot.send_message(message.chat.id, ra.choice(answer))
	while True:
		bot.send_message(message.chat.id, "Есть еще вопросы? Да или Нет?")
		rep = message.text()
		if rep.lower() in ("да", "yes", "ага", "даа", "da", "йес"):
			bot.send_message(message.chat.id, "Есть еще вопросы? Да или Нет?")
			ask = message.text()
			bot.send_message(message.chat.id, ra.choice(answer))
		else:
			bot.send_message(message.chat.id, "Ну, слава богу, мне за это так-то не платят")
			break

	bot.send_message(message.chat.id, "Аривидрочи!")
bot.polling()