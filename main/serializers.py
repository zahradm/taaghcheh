from rest_framework import serializers


class BookNameInputSerializer(serializers.Serializer):
    book_name = serializers.CharField(max_length=200)
