def test_email(email):
    domen = ('.com','.ru','.net')   #list of correct domen
    good = False
    if ('@' in email) and email.endswith(domen): #check the email for the presence of '@' and the ending correct domen
        good = True
    return good
def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if test_email(recipient) == False or test_email(sender) == False:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print( f'Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
send_email('Проверка обратной связи', 'university.help@gmail.com', sender='university.help@gmail.com')
send_email('Отправка на печать', 'printer.univ@total.org')