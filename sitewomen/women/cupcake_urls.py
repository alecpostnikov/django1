from django.urls import path, include
from . import views

urlpatterns = [
    path()
    path("<str:cupcake_id>/<int:cupcake_amount>/", views.cupcake),
]