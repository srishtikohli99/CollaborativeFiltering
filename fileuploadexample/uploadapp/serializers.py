from rest_framework import serializers
# from .models import File

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    obj = serializers.IntegerField()

