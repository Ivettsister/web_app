from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "title": "SolVio - главная",
        "content": "Сайт репетитора Соловьевой Виолетты",
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "О нас",
        "content": "Вы находитесь на образовательной платформе, созданной Соловьевой Виолеттой",
        "text_on_page": "Текст о том, какая я крутая, умная и красивая:)",
    }

    return render(request, "main/about.html", context)
