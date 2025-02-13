from django.urls import path
from .views import TemplView




app_name = 'landing'

urlpatterns = [
    path('', TemplView.as_view(), name='landing')
]