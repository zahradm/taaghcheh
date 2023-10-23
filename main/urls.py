from django.urls import path

from main.views import MeanRateAPI

app_name = 'main'

urlpatterns = [
    path('rate/', MeanRateAPI.as_view(), name='rate')
]