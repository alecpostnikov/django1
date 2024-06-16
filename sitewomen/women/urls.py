from django.urls import path, include, register_converter, re_path
from . import converters, views


register_converter(converters.FourDigitConverter, "four_digit")

urlpatterns = [
    path('', views.index),
    path("cupcake/", include('women.cupcake_urls')),
    re_path(r'.+choco.', views.chocolate),
    re_path(r"^archive/(?P<year>[0-9]{4})/", views.archive),
    path("converter/<four_digit:year>/", views.archive),
    path("cycle/", views.cycle1),
]