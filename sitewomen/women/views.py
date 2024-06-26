from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
import time
from django.template.loader import render_to_string

cupcake_data = [{'type': 'vanilla', 'description': 'an all time classic only for boomers',
                 'ingredients': 'cupcake stuff, vanilla, our love(E111, E112, E113, E114, E115..., cancirogens )', 'in_stock': True},
                {'type': 'protein chocolate', 'description': '0 sugar',
                 'ingredients': "sugar(98%), flour, eggs, cocoa powder", 'in_stock': True},]


def index(request):
    return HttpResponse("Страница приложения women.")


def cupcake_list(request):
    data = {'menu': cupcake_data}
    return render(request, 'women/cupcake.html', context=data)


def cupcake(request, cupcake_id, cupcake_amount):
    return HttpResponse(f"Ваш заказ на {cupcake_amount} {cupcake_id} принят. <p>Ожидайте</p>")


def chocolate(request):
    return HttpResponse("Шоколад это вкусно")


def danger(request):
    # t = render_to_string("women/danger.html")
    # return HttpResponse(t)
    data = {'given_thing': 'медаль'}
    return render(request, 'women/danger.html', data)


def archive(request, year):
    if int(year) > 2024:
        return redirect('/')
    return HttpResponse(f"{year} был тяжёлым")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Не тот запрос, чепушила</h1>")


def cycle1(request):
    time.sleep(2)
    return redirect(cycle1)
