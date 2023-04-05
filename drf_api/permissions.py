from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(request.user.role.role)
        if (
            request.method in permissions.SAFE_METHODS
            and request.user.role.role == "SUPERADMIN"
        ):
            return True
        return request.user.role == "SUPERADMIN"
