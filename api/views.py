from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet
from rest_framework import generics,status
from rest_framework.response import Response
from .serializers import BlogPostSerializer
from .models import BlogPost
# Create your views here.


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset=BlogPost.objects.all()
    serializer_class=BlogPostSerializer

    #override default method on DRF
    # def delete(self,request,*args,**kwargs):
    #     BlogPost.objects.all().delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field='pk' # primary key id field
