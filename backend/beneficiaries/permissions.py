from rest_framework import permissions


class IsSuperUserOrStaffEditAndAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in permissions.SAFE_METHODS:
            return True
        
        if request.user.is_authenticated and ((request.user.is_staff or request.user.is_superuser) and request.user.is_active):
            return True
        
        return False