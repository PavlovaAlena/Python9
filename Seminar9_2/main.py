import logging
from config import TOKEN
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (Updater, CommandHandler,
                          MessageHandler, Filters, ConversationHandler)

# **************Логирование************
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# **************
CHOICE, INT_ONE, INT_TWO, OPERATIONS_INT = range(4)

# **************


def start(update, _):
    reply_keyboard = [['Считать', 'Выход']]

    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        f'Привет, {update.effective_user.last_name}, - это калькулятор. Выберите пожалуйста команду.\n' 'Команда /cancel, чтобы прекратить разговор.\n\n', reply_markup=markup_key,)
    return CHOICE

# **************


def choice(update, context):
    user = update.message.from_user
    logger.info("Выбор операции: %s: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    if user_choice == 'Считать':
        update.message.reply_text(
            'Введите число. \n Первое число - это: ')
        return INT_ONE
    elif user_choice == 'Выход':
        update.message.reply_text('Спасибо, до свидания!')
        return ConversationHandler.END
    else:
        update.message.reply_text(
            'Ошибка ввода. Введите цифру операции: \n 1 - для операций с числами; \n2 - для выхода \n')

# **************


def INT_ONE(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s",
                user.first_name, update.message.text)
    get_rational = update.message.text
    if get_rational.isdigit():
        get_rational = float(get_rational)
        context.user_data['INT_ONE'] = get_rational
        update.message.reply_text('Введите второе число')
        return INT_TWO

    else:
        update.message.reply_text('Нужно ввести число')

# **************


def INT_TWO(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s",
                user.first_name, update.message.text)
    get_rational = update.message.text
    if get_rational.isdigit():
        get_rational = float(get_rational)
        context.user_data['INT_TWO'] = get_rational
        reply_keyboard = [['+', '-', '*', '/']]
        markup_key = ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True)
        update.message.reply_text(
            'Выберите действие: \n\n+ - для сложения; \n- - для вычетания; \n* - для умножения; \n/ - для деления. \n',
            reply_markup=markup_key,)
        return OPERATIONS_INT

# **************


def operatons_INT(update, context):
    user = update.message.from_user
    logger.info(
        "Пользователь выбрал операцию %s: %s", user.first_name, update.message.text)
    INT_ONE = context.user_data.get('INT_ONE')
    INT_TWO = context.user_data.get('INT_TWO')
    user_choice = update.message.text
    res = True
    if user_choice == '+':
        result = INT_ONE + INT_TWO
    elif user_choice == '-':
        result = INT_ONE - INT_TWO
    elif user_choice == '*':
        result = INT_ONE * INT_TWO
    elif user_choice == '/':
        try:
            result = INT_ONE / INT_TWO
        except:
            result = '#дел'
            update.message.reply_text('Деление на ноль запрещено')
    else:
        res = False
        update.message.reply_text(
            'Ошибка ввода. Выберите действие: \n+ - для сложения; \n- - для вычетания; \n* - для умножения; \n/ - для деления. \n')
    if res == True:
        update.message.reply_text(
            f'Результат: {INT_ONE} {user_choice} {INT_TWO} = {result}')
        return ConversationHandler.END

# **************


def cancel(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    update.message.reply_text('Спасибо, до свидания!',
                              reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


# **************
if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(

        entry_points=[CommandHandler('start', start)],

        states={
            CHOICE: [MessageHandler(Filters.text, choice)],
            INT_ONE: [MessageHandler(Filters.text, INT_ONE)],
            INT_TWO: [MessageHandler(Filters.text, INT_TWO)],
            OPERATIONS_INT: [MessageHandler(Filters.text, operatons_INT)],
        },

        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conversation_handler)
    print('server start')
    updater.start_polling()
    updater.idle()
