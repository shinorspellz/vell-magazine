from rest_framework import serializers
from publications_info.models import PublicationsInfo


class PublicationsInfoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = PublicationsInfo
        fields = [
            "id",
            "owner",
            'is_owner',
            "status",
            "month",
            "date",
        ]