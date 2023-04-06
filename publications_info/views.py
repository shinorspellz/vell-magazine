from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PublicationsInfo
from .serializers import PublicationsInfoSerializer
from drf_api.permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly


class PublicationsInfoList(APIView):
## Get method: fetch's all PublicationsInfo objects, serializes and returns in Response.
    def get(self, request):
        publications_info = PublicationsInfo.objects.all()
        serializer = PublicationsInfoSerializer(
            publications_info,
            many=True,
            context={'request': request}
            )
        return Response(serializer.data)

class PublicationsInfoDetail(APIView):
    """
    Retrieve or update an PublicationsInfo if you're the owner.(or editor)
    """
    # setting serializer class attribute in this view, the rest framework with automatically render the form based on our serializer fields, as opposed to raw Json.
    serializer_class = PublicationsInfoSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAdminOrReadOnly]

    def get_object(self, pk):
        try:
            publications_info = PublicationsInfo.objects.get(pk=pk)
            self.check_object_permissions(self.request, PublicationsInfo)
            return publications_info
        except PublicationsInfo.DoesNotExist:
            raise Http404
    
    def put(self, request, pk):
        publications_info = self.get_object(pk)
        serializer = PublicationsInfoSerializer(
            publications_info,
            data=request.data,
            context={'request': request}
            )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PublicationsInfoGetDetail(APIView):
    """
    Retrieve or update an PublicationsInfo if you're the owner.(or editor)
    """
    # setting serializer class attribute in this view, the rest framework with automatically render the form based on our serializer fields, as opposed to raw Json.
    serializer_class = PublicationsInfoSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAdminOrReadOnly]
    
    def get_object(self, pk):
        try:
            publications_info = PublicationsInfo.objects.get(pk=pk)
            self.check_object_permissions(self.request, PublicationsInfo)
            return publications_info
        except PublicationsInfo.DoesNotExist:
            raise Http404
    
        
## Get method fetching PublicationsInfo detail using pk.
    def get(self, request, pk):
        PublicationsInfo = self.get_object(pk)
        serializer = PublicationsInfoSerializer(
            PublicationsInfo,
            # As the logged in user is part of the request object, we need to pass it as context object when we call our serializers in our views.
            context={'request': request}
            )
        return Response(serializer.data)