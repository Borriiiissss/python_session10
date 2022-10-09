import telebot
#a
x = 0
y = 0
lst = []

bot = telebot.TeleBot('5753604058:AAHLeZ1vZfdB6kJDd7TW64DwrLJybb9fpHo')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('1', '2', '3', ' ', '4', '5', '6',' ', '7', '8', '9', '.', '+', '-', '*', '/', '=')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, включаем калькулятор', reply_markup=keyboard1)
    global lst
    lst = []
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    if message.text.isdigit:
        # bot.send_message(message.chat.id, message.text)
        result = listadding(message.text)
        if result: 
            bot.send_message(message.chat.id, f'результат {result} ')
            if result < 10:
                bot.send_message(message.chat.id, f'ну капец ты пифагор')
            global lst
            lst = []
        if '=' in lst:
            lst = []
        
def listadding (num):
    global lst
    lst.append(num)
    if '=' in lst:
        result = lst_calculate(lst)
        if result != 0.354648:
            return result      
    
def lst_calculate(lst):   
    for i in range(len(lst)):
        print (lst)
        if lst[i] == '+' or lst[i] == '-' or lst[i] == '*' or lst[i] == '/':
            sign = lst [i]
            x = get_num_from_list(lst[0:i])
            y = get_num_from_list(lst[i+1:len(lst)-1])
            match sign:
                case '+':
                    return float(x) + float (y)
                case '-':
                    return float(x) - float (y)
                case '*':
                    return float(x) * float (y)
                case '/':
                    return float(x) / float (y)

def get_num_from_list(lst_part):
    print (lst_part)
    full_num = ''
    full_num = full_num.join(lst_part)
    # for m in lst_part:
    #     full_num = full_num.join(m)
    print (full_num)
    return (full_num)

bot.polling()