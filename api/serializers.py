from rest_framework import serializers

from posts.models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'text', 'author', 'image', 'pub_date')
        read_only_fields = ('author',)
        model = Post

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.username
        return representation


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author',)
        model = Comment

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.username
        return representation
