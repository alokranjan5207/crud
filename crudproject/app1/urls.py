from django.urls import path
from app1 import views

urlpatterns = [
    path(route='index/',view=views.index,name='index'),
    # path(route='add/',view=views.add,name='add'),
    # path(route='all/',view=views.all,name='all'),
    path(route='',view=views.home,name='home'),
    path(route='show/',view=views.show,name='show'),
    path(route='send/',view=views.send,name='send')
]