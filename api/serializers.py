from .models import User, Doc
from rest_framework import serializers


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        filed = ['account', 'password']


class DocSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = '__all__'
