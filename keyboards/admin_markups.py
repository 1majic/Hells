from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.callback_data import CallbackData

from db import init

from cfg.init import db as cfg_init

db = init.db


def main_keyboard():
    edit_panel_btn = KeyboardButton("Редактировать панель")
    blacklist_btn = KeyboardButton("Черный список")
    check_stats_btn = KeyboardButton("Посмотреть статистику")
    coupons_btn = KeyboardButton("Купоны")

    MainMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    MainMenu.row(edit_panel_btn, check_stats_btn).row(blacklist_btn, coupons_btn)
    return MainMenu


def lCabinet(user_id):
    markup = InlineKeyboardMarkup(row_width=2)

    purchase_history_btn = InlineKeyboardButton(text="История заказов", callback_data=f"purchase_history_{user_id}")
    personal_discount_btn = InlineKeyboardButton(text="Личная скидка", callback_data=f"personal_discount_{user_id}")
    referral_system_btn = InlineKeyboardButton(text="Реферальная система", callback_data=f"referral_system_{user_id}")
    top_up_history_btn = InlineKeyboardButton(text="История начислений", callback_data=f"top_up_history_{user_id}")

    markup.row(purchase_history_btn).row(personal_discount_btn).row(referral_system_btn).row(top_up_history_btn)

    return markup


def referral_system_keyboard(user_id):
    markup = InlineKeyboardMarkup()

    referral_list_button = InlineKeyboardButton(text="Список рефералов", callback_data=f"referral_list_{user_id}")

    markup.row(referral_list_button)

    return markup


def edit_buy_course(item):
    markup = InlineKeyboardMarkup()

    markup.row(
        InlineKeyboardButton(text="Изменить название", callback_data=f"edit_item_name_{item}")
    ).row(
        InlineKeyboardButton(text="Изменить описание", callback_data=f"edit_description_{item}")
    ).row(
        InlineKeyboardButton(text="Изменить фото", callback_data=f"edit_photo_{item}")
    ).row(
        InlineKeyboardButton(text="Изменить цену", callback_data=f"edit_price_{item}")
    ).row(
        InlineKeyboardButton(text="Изменить chat id", callback_data=f"chat_id_{item}")
    )

    return markup


def admin_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)

    markup.insert(
        InlineKeyboardButton(text='Редактировать надпись', callback_data='edit_admin_btn_text')
    ).insert(
        InlineKeyboardButton(text='Редактировать ссылку', callback_data='edit_admin_btn_link')
    )

    return markup


def reviews_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)

    markup.insert(
        InlineKeyboardButton(text='Редактировать надпись', callback_data='edit_reviews_btn_text')
    ).insert(
        InlineKeyboardButton(text='Редактировать ссылку', callback_data='edit_reviews_btn_link')
    )

    return markup


def massMessage_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)

    markup.insert(
        InlineKeyboardButton(text=cfg_init.get_chat_text(), callback_data=cfg_init.get_chat_link())
    ).insert(
        InlineKeyboardButton(text=cfg_init.get_admin_text(), callback_data=cfg_init.get_admin_link())
    )


def chat_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)

    markup.insert(
        InlineKeyboardButton(text='Редактировать надпись', callback_data='edit_chat_btn_text')
    ).insert(
        InlineKeyboardButton(text='Редактировать ссылку', callback_data='edit_chat_btn_link')
    )
    return markup


def group_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)

    markup.insert(
        InlineKeyboardButton(text='Редактировать надпись', callback_data='edit_group_btn_text')
    ).insert(
        InlineKeyboardButton(text='Редактировать ссылку', callback_data='edit_group_btn_link')
    )
    return markup


def edit_panel_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)

    buy_course_btn = InlineKeyboardButton(text="Купить курсы", callback_data='edit_buy_course')
    free_course_btn = InlineKeyboardButton(text="Бесплатные курсы", callback_data='edit_free_course')
    help_btn = InlineKeyboardButton(text="Помощь", callback_data='edit_help')
    chat_btn = InlineKeyboardButton(text="Чатик и общая группа", callback_data='edit_chat')

    markup.row(buy_course_btn).row(free_course_btn, help_btn).row(chat_btn)

    return markup


def edit_buy_course_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)

    add_course = InlineKeyboardButton(text='Добавить курс', callback_data='add_course')
    del_course = InlineKeyboardButton(text='Удалить курс', callback_data='del_course')

    markup.row(add_course, del_course)

    return markup


def edit_free_course_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)

    add_free_course = InlineKeyboardButton(text='Добавить бесплатный курс', callback_data='add_free_course')
    del_free_course = InlineKeyboardButton(text='Удалить бесплатный курс', callback_data='del_free_course')

    markup.row(add_free_course, del_free_course)

    return markup


def edit_help_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)

    edit_admin_btn = InlineKeyboardButton(text='Редактировать кнопку "Админа"', callback_data='edit_admin_btn')
    edit_reviews_btn = InlineKeyboardButton(text='Редактировать кнопку "Отзывы"', callback_data='edit_reviews_btn')

    markup.row(edit_admin_btn, edit_reviews_btn)

    return markup


def edit_chat_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)

    edit_chat_btn = InlineKeyboardButton(text='Редактировать кнопку чата', callback_data='edit_chat_btn')
    edit_group_btn = InlineKeyboardButton(text='Редактировать кнопку группы', callback_data='edit_group_btn')

    markup.row(edit_chat_btn, edit_group_btn)

    return markup
