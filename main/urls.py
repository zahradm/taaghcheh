from django.urls import path

from main.views import MeanRateAPI, FrequentWordAPI

app_name = 'main'

urlpatterns = [
    path('rate/', MeanRateAPI.as_view(), name='rate'),
    path('frequent-word/', FrequentWordAPI.as_view(), name='frequent-word')
]