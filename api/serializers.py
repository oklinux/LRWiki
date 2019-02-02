from .models import User, Doc
from rest_framework import serializers
from lib.doc.create import create_doc
from lib.doc.check import is_check_title_already_created


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        filed = ['account', 'password']


class DocSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doc
        fields = '__all__'

    def validate(self, data):
        title = data.get('title')
        if is_check_title_already_created(title):
            raise serializers.ValidationError('title already used')
        return data

    def create(self, validated_data):
        doc = create_doc(**validated_data)
        return doc

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
