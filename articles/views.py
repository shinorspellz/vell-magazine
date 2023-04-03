from django.http import Http404
from rest_framework import status
#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleSerializer
from drf_api.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly


class ArticleList(APIView):
## Get method: fetch's all article objects, serializes and returns in Response.
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(
            articles,
            many=True,
            context={'request': request}
            )
        return Response(serializer.data)

class ArticleDetail(APIView):
    """
    Retrieve or update an article if you're the owner.(or editor)
    """
    # setting serializer class attribute in this view, the rest framework with automatically render the form based on our serializer fields, as opposed to raw Json.
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAdminOrReadOnly]

    def get_object(self, pk):
        try:
            article = Article.objects.get(pk=pk)
            self.check_object_permissions(self.request, article)
            return article
        except Article.DoesNotExist:
            raise Http404
    
    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(
            article,
            data=request.data,
            context={'request': request}
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleGetDetail(APIView):
    """
    Retrieve or update an article if you're the owner.(or editor)
    """
    # setting serializer class attribute in this view, the rest framework with automatically render the form based on our serializer fields, as opposed to raw Json.
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAdminOrReadOnly]
    
    def get_object(self, pk):
        try:
            article = Article.objects.get(pk=pk)
            self.check_object_permissions(self.request, article)
            return article
        except Article.DoesNotExist:
            raise Http404
    
        
## Get method fetching article detail using pk.
    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(
            article,
            # As the logged in user is part of the request object, we need to pass it as context object when we call our serializers in our views.
            context={'request': request}
            )
        return Response(serializer.data)