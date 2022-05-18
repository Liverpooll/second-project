from django.shortcuts import get_object_or_404, render, redirect

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from blog.serializers import PostSerializer

from blog.models import Post

import logging
logging.basicConfig(level=logging.INFO)


class PostList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'list.html'

    def get(self, request):
        queryset = Post.objects.all()
        return Response({'post':queryset})


class PostDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'detail.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return Response({'post':post})


class PostCreate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'create.html'

    def get(self, request):
        return Response()
    
    def post(self, request):
        logging.info(request.data)
        serializer = PostSerializer(data = {
            'title':request.POST.get('title'),
            'content':request.POST.get('content'),
        })
        if not serializer.is_valid():
            logging.info('not valid')
            return Response()
        else:
            serializer.save()
            id = serializer.data['id']
            return redirect(f'/blog/detail/{id}')


class PostUpdate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'update.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return Response({'post':post})

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(
            post,
            data = {
                'title':request.POST.get('title'),
                'content':request.POST.get('content'),
            }
        )
        if not serializer.is_valid():
            logging.info('not valid')
            return Response()
        else:
            serializer.save()
            logging.info(serializer)
            id = serializer.data['id']
            return redirect(f'/blog/detail/{id}')


class PostDelete(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect(f'/blog/list')
