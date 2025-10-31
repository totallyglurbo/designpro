from django.urls import path
from . import views
from .views import TheLoginView, TheRegisterView

urlpatterns = [
    path('', views.index, name='index'),

    path('profile/', views.profile_view, name='profile'),
    path('register/', TheRegisterView.as_view(), name='register'),
    path('login/', TheLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout')
]
