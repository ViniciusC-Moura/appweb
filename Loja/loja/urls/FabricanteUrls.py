from django.urls import path
from loja.views.FabricanteView import edit_fabricante_view, list_fabricante_view, details_fabricante_view, delete_fabricante_view, delete_fabricante_postback, create_fabricante_view
urlpatterns = [
    path("", list_fabricante_view, name='fabricante'),
    path("<int:id>", list_fabricante_view, name= 'fabricante'),
    path("edit/<int:id>", edit_fabricante_view, name= 'edit_fabricante'),
    path("details/<int:id>", details_fabricante_view, name= 'details_fabricante'),
    path("delete/<int:id>", delete_fabricante_view, name='delete_fabricante'),
    path("delete", delete_fabricante_postback, name='delete_fabricante_postback'),
    path("create", create_fabricante_view, name= 'create_fabricante'),
]