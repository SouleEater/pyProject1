from django.urls import path, include
from users.views import CustomLoginView
from users.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
]