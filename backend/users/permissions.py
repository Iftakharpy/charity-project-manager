from rest_framework import permissions


class IsSuperuserAndOwnerEditOrAuthenticatedReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or superusers to edit it.
    But other authenticated users can read it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to authenticated requests,
        # So we'll always allow GET, HEAD or OPTIONS requests to authenticated requests.
        if (request.method in permissions.SAFE_METHODS) and request.user.is_authenticated:
            return True

        if request.user.is_authenticated:
            # Write permissions are only allowed to the owner of the snippet or superusers.
            return obj.owner == request.user or ((request.user.is_superuser or request.user.is_staff) and request.user.is_active)
        return False
