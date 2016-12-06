from celery import task, shared_task
from datetime import datetime
from django.core.mail import send_mail


# логирование добавления нового комментария
@shared_task(name='comments_log')
def comment_add_log(comment_author):

    with open('log.txt', 'a') as f:

        f.write(comment_author + ' add comment at ' + datetime.strftime(datetime.today(), "%H:%M %d.%m.%Y") + '\n')


#рассылка писем при добавлении нового комментария
@shared_task
def send_mail_to_subscribers(message):

    send_mail('New comment', 'New comment text:' + message, 'from@example.com',['to@example.com'], fail_silently = False)



