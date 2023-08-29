from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    html = """
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>Главная</title>
        </head>
        <body>
            <h1>...Информация главной страницы...</h1>
            <p>Тут можно написать все что будет интересно гостям сайта.</p>
        </body>
        </html>
        """
    logger.info('Visit "main" page')
    return HttpResponse(html)

def about(request):
    html = """
            <!DOCTYPE html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <title>Информация</title>
            </head>
            <body>
                <h3>Информация обо мне:</h3>
                <p>Имя студента: Евгений</p>
                <p>Факультет: Разработчик Python</p>
                <p>Год окончания обучения: 2023</p>
            </body>
            </html>
            """
    logger.info('Visit "about" page')
    return HttpResponse(html)