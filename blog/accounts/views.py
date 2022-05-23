from re import template
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

import logging
logging.basicConfig(level=logging.INFO)


class Signup(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'signup.html'

    def get(self, request):
        return Response()


class Login(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'log_in.html'

    def get(self, request):
        return Response()
