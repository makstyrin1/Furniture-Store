from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    # path('login/', views.login, name='login'),
    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    # path('registration/', views.registration, name='registration'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    # path('profile/', views.profile, name='profile'),
    path('user_cart/', views.UserCartView.as_view(), name='user_cart'),
    # path('user_cart/', views.user_cart, name='user_cart'),
    path('logout/', views.logout, name='logout'),
]