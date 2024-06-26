from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('list/', views.cupcake_list),
    path("<str:cupcake_id>/<int:cupcake_amount>/", views.cupcake),
]