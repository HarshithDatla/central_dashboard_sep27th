from rest_framework import permissions

class IsUserAssociatedWithTrust(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is associated with the Trust
        return obj.user == request.user
