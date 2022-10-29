from django.urls import path
from checking.views import dashboard, checker, get_last_update

app_name = 'checking'

urlpatterns = [
    path('get_last_update', get_last_update, name='get_last_update'),
    path('checker', checker, name='checker'),
    path('', dashboard, name='dashboard'),
]
