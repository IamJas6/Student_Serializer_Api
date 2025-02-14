from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    address = serializers.CharField()
    email = serializers.EmailField()
    phone_number = serializers.CharField()

    def create(self, kwargs):
        stu = Student.objects.create(**kwargs)
        return stu