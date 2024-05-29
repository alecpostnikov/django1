from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    return HttpResponse("Страница приложения women.")


def cupcake(request, cupcake_id, cupcake_amount):
    return HttpResponse(f"Ваш заказ на {cupcake_amount} {cupcake_id} принят. <p>Ожидайте</p>")


def chocolate(request):
    return HttpResponse("Шоколад это вкусно")


def archive(request, year):
    if int(year) > 2024:
        raise Http404()
    return HttpResponse(f"{year} был тяжёлым")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Не тот запрос, чепушила</h1>")
