from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^switch/(?P<motor>\w+)/(?P<state>\d+)/$', views.switch_on, name='switch_on'),
    url(r'^switch/(?P<motor>\w+)/(?P<state>\d+)/$', views.switch_off, name='switch_off'),
    url(r'^switch/(?P<motor>\w+)/$', views.toggle, name='toggle'),
]

## (?P<state>\d+)    --> here <motor> will be considered as a parameter and
# can be directly passed to the function like views.switch on, \d+ will allow only numbers
# and {1} will allow only 1 occurences of number

## ?P<motor>\w+    --> \w+ will allow One or more word characters, numbers.
# {2} will allow only 2 occurences of the same


