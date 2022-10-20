from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os
import pytz


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    tz = pytz.timezone('Etc/GMT-7')
    current_time = datetime.now(tz=tz).strftime("%H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    path = os.getcwd()
    files_list = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files_list.append(file)
    return render(request, 'app/workdir.html', {'files': files_list})

