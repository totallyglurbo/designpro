from django.urls import path
from . import views
from .views import TheLoginView

urlpatterns = [
    path('', views.index, name='index'),

    path('profile/', views.profile_view, name='profile'),
    path('register/', views.register_user, name='register'),
    path('login/', TheLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout')
]
