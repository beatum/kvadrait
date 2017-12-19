from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.generics import RetrieveAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from app.models import Note


def index(request):
    """
    Home page
    """
    return render(request, 'base.html')


class UploadTxt(TemplateView):
    """
    Form view
    """
    template_name = 'send.html'


class GetTxt(RetrieveAPIView):
    """
    Retrieve data (Note List) from API
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'view.html'

    def get(self, request, *args, **kwargs):
        queryset = Note.objects.all()
        return Response({'objects': queryset})
