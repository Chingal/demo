from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from demo.apps.inicio.views import ContactView

urlpatterns = patterns('',
    url(r'^$',
    	TemplateView.as_view(
    		template_name = 'inicio/index.html'),
    	name = "index" ),
    url(r'^about/$',
    	TemplateView.as_view(
    		template_name = 'inicio/about.html'),
    	name = "about" ),

    url(r'^contact/$',
    	ContactView.as_view(),
    	name = "contact" ),

    url(r'^$',
    	'django.contrib.auth.views.login',
    	{'template_name': 'inicio/index.html'},
    	name = "login"),

	url(r'^logout/$',
		'django.contrib.auth.views.logout_then_login',
		name= " logout"),
)
