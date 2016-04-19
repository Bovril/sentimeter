from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Tweet


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class TweetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False,
                                  allow_blank=True,
                                  max_length=100)
    tweet = serializers.CharField(style={'base_template':'textarea.html'})

    def create(self, validated_data):
        """
        Create and return a new `Tweet` instance, given the validated data.
        """

    def update(self, instance, validated_data):
        """
        Update and return an existing `Tweet` instance, given the validated data.
        """

        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance


