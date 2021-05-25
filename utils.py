from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


def main_keyboard():
    return ReplyKeyboardMarkup([['Добавить заведение'],
                               ['Посещённые заведения'],
                               ['Не посещённые заведения']],
                               resize_keyboard=True)


def rate_keyboard():
    return ReplyKeyboardMarkup([['Пропустить', 'Заново', 'Выйти']], resize_keyboard=True)


def rate_end_keyboard():
    return ReplyKeyboardMarkup([['Закончить', 'Заново']], resize_keyboard=True)


def show_rating_keyboard():
    keyboard = [
        [
            InlineKeyboardButton('Подробнее', switch_inline_query_current_chat='Подробнее: '),
            InlineKeyboardButton('Удалить', switch_inline_query_current_chat='Удалить: ')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def rating_keyboard():
    keyboard = [
        [
            InlineKeyboardButton('Оценить', switch_inline_query_current_chat='Оценить: '),
            InlineKeyboardButton('Удалить', switch_inline_query_current_chat='Удалить: ')
        ]
    ]
    return InlineKeyboardMarkup(keyboard)


def rate_again_keyboard(cafe_name):
    keyboard = [
        [
            InlineKeyboardButton('Редактировать', switch_inline_query_current_chat=f'Редактировать: {cafe_name}',
                                 resize_keyboard=True)
        ]
    ]
    return InlineKeyboardMarkup(keyboard)
