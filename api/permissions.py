from rest_framework import permissions


class IsOwnByReadOnly(permissions):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return str(request.user) == obj.account
