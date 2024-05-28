from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Страница приложения women.")


def cupcake(request, cupcake_id, cupcake_amount):
    return HttpResponse(f"Ваш заказ на {cupcake_amount} {cupcake_id} принят. <p>Ожидайте</p>")


def chocolate(request):
    return HttpResponse("Шоколад это вкусно")


def archive(request, year):
    return HttpResponse(f"{year} был тяжёлым")
