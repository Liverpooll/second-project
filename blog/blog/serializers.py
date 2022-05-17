from rest_framework import serializers
from blog.models import Post


import logging
logging.basicConfig(level=logging.INFO)


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=20)
    content = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        logging.info(validated_data)
        return Post.objects.create(**validated_data)
