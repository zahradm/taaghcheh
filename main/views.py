from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import BookNameInputSerializer
from utils.preprocessing import mean_rating, frequent_word


class MeanRateAPI(APIView):
    serializer_class = BookNameInputSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        mean_rate = mean_rating(data['book_name'])
        return Response({'success': True, 'results': mean_rate})


class FrequentWordAPI(APIView):
    serializer_class = BookNameInputSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        frequent_word_comment = frequent_word(data['book_name'])
        return Response({'success': True, 'results': frequent_word_comment})
