from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrAuthenticatedOnly(BasePermission):
    """Only auth user has read access; only author - write access"""
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated
                and (
                    request.method in SAFE_METHODS
                    or obj.author == request.user
                ))
