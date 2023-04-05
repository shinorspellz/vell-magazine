from rest_framework import serializers
from .models import Role


class RoleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    # As the logged in user is part of the request object, we need to pass it as context object when we call our serializers in our views.
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Role
        fields = [
            "id",
            "role",
            "is_owner",
        ]
