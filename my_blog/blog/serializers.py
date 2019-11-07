from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    model = Post
    fields = ['title', 'category', 'desc', 'content_html', 'created_time']
