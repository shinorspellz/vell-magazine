from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Article
        fields = [
            "id",
            "owner",
            "is_owner",
            "created_at",
            "updated_at",
            "mainHeader",
            "subHeader",
            "contentHeader",
            "content",
            "image",
            'theme',
            'template',
        ]
"""
    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                "Image size too large! Must be under 2MB!"
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                "Image height too large! Must be under 4096px!"
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                "Image width too large! Must be under than 4096px!"
            )
        return value
"""