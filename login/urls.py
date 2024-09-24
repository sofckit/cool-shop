from django.urls import path
from . import views
from .views import logout_view



urlpatterns = [
    path('login/', views.login_view),
    path('register/', views.register_view),
    path('logout/', logout_view, name='logout'),
]