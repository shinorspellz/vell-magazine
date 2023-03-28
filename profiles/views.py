from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer

class ProfileList(APIView):
## Get method: fetch's all profile objects, serializes and returns in Response.
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

class ProfileDetail(APIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    def get_object(self, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            return profile
        except Profile.DoesNotExist:
            raise Http404

## Get method fetching profile detail using pk.

    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)