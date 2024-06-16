from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
import time


def index(request):
    return HttpResponse("Страница приложения women.")


def cupcake(request, cupcake_id, cupcake_amount):
    return HttpResponse(f"Ваш заказ на {cupcake_amount} {cupcake_id} принят. <p>Ожидайте</p>")


def chocolate(request):
    return HttpResponse("Шоколад это вкусно")


def archive(request, year):
    if int(year) > 2024:
        return redirect('/')
    return HttpResponse(f"{year} был тяжёлым")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Не тот запрос, чепушила</h1>")


def cycle1(request):
    time.sleep(2)
    return redirect(cycle1)
