from django.conf.urls import patterns, url
from views import AddProductView

##URL para agregar un Producto
urlpatterns = patterns('tienda.apps.ventas.views',
	url(r'^product/add/$',AddProductView.as_view(),name="add_product"),
)