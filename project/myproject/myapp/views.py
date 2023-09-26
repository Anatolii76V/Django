import logging
from django.http import HttpResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    html = """
    <html>
    <head>
        <title>Django страница</title>
    </head>
    <body>
        <h1>Добро пожаловать на мой сайт!</h1>
        <p>Это мой первый Django сайт.</p>
    </body>
    </html>
    """

    logger.info('Посетили главную страницу')

    return HttpResponse(html)


def about(request):
    html = """
    <html>
    <head>
        <title>О себе</title>
    </head>
    <body>
        <h1>Обо мне</h1>
        <p>Я - Анатолий !</p>
        <p>Я учусь программировать на python !</p>
    </body>
    </html>
    """

    logger.info('Посетили страницу "О себе"')

    return HttpResponse(html)