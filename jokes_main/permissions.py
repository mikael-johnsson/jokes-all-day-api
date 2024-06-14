from rest_framework import permissions

class IsProfileOwnerOrReadOnly(permissions.BasePermission):
    """
    Returns true or false based on if the owner of the profile
    is the request user
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Returns true or false based on if the author of the profile
    is the request user
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user