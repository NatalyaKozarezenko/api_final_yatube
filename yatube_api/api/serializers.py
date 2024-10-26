import base64
from django.core.files.base import ContentFile
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Follow, Group, Comment, Post, User


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
        return super().to_internal_value(data)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        validators = []

    def get_user(self):
        return self.context['request'].user

    def validate(self, attrs):
        if Follow.objects.filter(
            user=self.get_user(),
            following=attrs['following']
        ).exists():
            raise serializers.ValidationError('Вы уже подписаны!')

        if self.get_user() == attrs['following']:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!'
            )
        return attrs

    def create(self, validated_data):
        return Follow.objects.create(
            user=self.get_user(),
            following=validated_data['following']
        )
