from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('addMsg/', views.addMsg, name='addMsg'),
    path('queryMsg/', views.queryMsg, name='queryMsg'),
    path('checktime/', views.checktime, name='checktime'),
]