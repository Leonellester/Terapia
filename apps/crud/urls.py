from django.conf.urls import url, include
from .views import index, terapia_view, terapia_list, terapia_edit, terapia_delete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^insertar$', terapia_view, name='insertar'),
    url(r'^consultar$', terapia_list, name='consultar'),
    url(r'^editar/(?P<id_terapia>\d+)/$', terapia_edit, name='editar'),
    url(r'^eliminar/(?P<id_terapia>\d+)/$', terapia_delete, name='eliminar'),
]



