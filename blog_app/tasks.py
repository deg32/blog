from datetime import datetime

from celery import shared_task
from django.core.mail import send_mail


@shared_task(name='comments_log')
def comment_add_log(comment_author):
    """Добавляет в лог-файл запись о новом комментарии"""

    with open('log.txt', 'a') as f:
        f.write(comment_author + ' add comment at ' + datetime.strftime(datetime.today(), "%H:%M %d.%m.%Y") + '\n')


@shared_task
def send_mail_to_subscribers(message):
    """Рассылает письма-оповещения о новом комментарии всем подписанным пользователям"""

    send_mail('New comment', 'New comment text:' + message, 'from@example.com', ['to@example.com'], fail_silently=False)
