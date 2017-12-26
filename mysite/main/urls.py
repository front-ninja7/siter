
from django.conf.urls import url, include
from main.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^web/', include('web.urls')),
]
