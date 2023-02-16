from django.urls import path

from .views import *

urlpatterns = [
    path('', AjaxHandler.as_view()),
    path('test', Number.as_view(), name='number'),
]