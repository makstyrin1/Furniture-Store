from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('', cache_page(60)(views.IndexView.as_view()), name='index'),
    # path('', views.index, name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    # path('about/', views.about, name='about'),
]