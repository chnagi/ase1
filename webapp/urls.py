from django.conf.urls import url,include
from . import views
app_name='webapp'
urlpatterns = [
   # url('', views.index, name='index'),
    url('login', views.login, name='login'),
    url('signup', views.signup, name='signup'),
]
