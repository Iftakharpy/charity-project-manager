from rest_framework import permissions


class IsAdminEditOrAuthenticatedReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or admins to edit it.
    But other authenticated users can read it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to authenticated requests,
        # So we'll always allow GET, HEAD or OPTIONS requests to authenticated requests.
        if (request.method in permissions.SAFE_METHODS) and request.user.is_authenticated:
            return True

        if request.user.is_authenticated:
            # Write permissions are only allowed to the owner of the snippet or admins.
            return request.user.is_superuser and request.user.is_active
        return False
