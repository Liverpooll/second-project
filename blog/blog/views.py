from django.shortcuts import get_object_or_404, render

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from blog.models import Post


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


class PostUpdate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'update.html'

    def get(self, request):
        return Response()
