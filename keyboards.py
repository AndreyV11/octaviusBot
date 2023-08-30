from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, \
                          InlineKeyboardButton, InlineKeyboardMarkup


# клавиатура, resize_keyboard изменяет размер на оптимальный, one_time_keyboard сворачивает клавиатура после нажатия
kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
btn1 = KeyboardButton('/help')
btn2 = KeyboardButton('/description')
btn3 = KeyboardButton('/photo')
btn4 = KeyboardButton('🐙')
btn5 = KeyboardButton('/links')
kb.add(btn1).insert(btn2).add(btn3).insert(btn4).add(btn5)     # add - добавить в строку, insert - добавить в столбец


# инлайн-клавиатура, находится под сообщением, обновляется без вызова новых команд и сообщений
ikb = InlineKeyboardMarkup(row_width=2)
ibtn1 = InlineKeyboardButton(text="TlgBot",
                            url="https://youtube.com/playlist?list=PLe-iIMbo5JOJm6DRTjhleHojroS-Bbocr&si=aA80DEybDAX5fF9n")
ibtn2 = InlineKeyboardButton(text="Git",
                            url="https://youtube.com/playlist?list=PLDyvV36pndZFHXjXuwA_NywNrVQO0aQqb&si=xbV9Qke3_aDsUSrh")
ibtn3 = InlineKeyboardButton(text="Docker",
                            url="https://youtu.be/O8N1lvkIjig?si=fQZtN8vvEbrlGIpI")
ibtn4 = InlineKeyboardButton(text="Backend",
                            url="https://youtube.com/playlist?list=PLoaXavbYQKPPN9wruJe2pLPuEKjXWvaM1&si=Qq3zF9jndgSt9e8i")
ibtn5 = InlineKeyboardButton(text="Django",
                            url="https://www.youtube.com/playlist?list=PLA0M1Bcd0w8xO_39zZll2u1lz_Q-Mwn1F")
ibtn6 = InlineKeyboardButton(text="Patterns",
                            url="https://refactoringguru.cn/design-patterns/python")
ikb.add(ibtn1, ibtn2, ibtn3, ibtn4, ibtn5, ibtn6)
