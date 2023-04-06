from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Role
from .serializers import RoleSerializer
from drf_api.permissions import IsAdminOrReadOnly


class RoleList(APIView):
    ## Get method: fetch's all profile objects, serializes and returns in Response.
    def get(self, request):
        roles = Role.objects.all()
        serializer = RoleSerializer(roles, many=True, context={"request": request})
        return Response(serializer.data)


class RoleDetail(APIView):
    """
    Retrieve or update a profile if you're the owner.
    """

    # setting serializer class attribute in this view, the rest framework with automatically render the form based on our serializer fields, as opposed to raw Json.
    serializer_class = RoleSerializer
    permission_classes = [IsAdminOrReadOnly] 

    def put(self, request, pk):
        role = Role.objects.get(pk=pk)
        serializer = RoleSerializer(
            role, data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RoleUserDetail(APIView):
    """
    Retrieve or update a profile if you're the owner.
    """

    # setting serializer class attribute in this view, the rest framework with automatically render the form based on our serializer fields, as opposed to raw Json.
    serializer_class = RoleSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, pk):
        try:
            role = Role.objects.get(pk=pk)
            self.check_object_permissions(self.request, role)
            return role
        except Role.DoesNotExist:
            raise Http404

    ## Get method fetching profile detail using pk.
    def get(self, request, pk):
        role = self.get_object(pk)
        serializer = RoleSerializer(
            role,
            # As the logged in user is part of the request object, we need to pass it as context object when we call our serializers in our views.
            context={"request": request},
        )
        return Response(serializer.data)