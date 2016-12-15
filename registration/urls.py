from django.conf.urls import url

from .views import registration_view

urlpatterns = [

    url(r'useradd/', registration_view, name='registration_view')

]
