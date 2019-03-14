from django.urls import path
from . import views
# app_name = 'polls'
urlpatterns = [
    path('createUser/', views.UserHandler.as_view()),
]