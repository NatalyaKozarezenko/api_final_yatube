from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import IsAuthorOrRead
from api.serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
)
from posts.models import Follow, Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrRead,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrRead,)

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs['post_id'])

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post()
        )


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    http_method_names = ['get', 'post']

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)
