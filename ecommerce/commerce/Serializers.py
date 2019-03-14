from rest_framework import serializers
from .models import *
from django.db import models

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'


class UserSerializerSave(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserSerializerGet(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('contactName', 'email')

class UserSerializer(serializers.Serializer):

    contactName = models.CharField(max_length=50)
    email = models.EmailField()


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    linenos = serializers.BooleanField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.save()
        return instance
