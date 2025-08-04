from django.urls import path

from deals.views import show_deals

app_name='deals'

urlpatterns = [
    path('deals/',show_deals)
]