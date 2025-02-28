from django.urls import path
from .views import hello_world, daargaanwe, metpathvar, get_all_products

urlpatterns = [
    path("hello/", hello_world),
    path("daargaanwe/", daargaanwe),
    path("print/<str:mijntext>/", metpathvar),
    path("products/", get_all_products),
]