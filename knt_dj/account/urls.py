from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('user/', UserView.as_view()),
    path('user/promote/', PromoteView.as_view()),
]
