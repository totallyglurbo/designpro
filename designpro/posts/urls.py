from django.urls import path
from . import views
from .views import TheLoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', views.register_user, name='register'),
    path('accounts/login/', TheLoginView.as_view(), name='login'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/logout/', views.logout_view, name='logout')
]
