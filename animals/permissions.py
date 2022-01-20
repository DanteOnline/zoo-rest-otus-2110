from rest_framework.permissions import BasePermission


class IsStaffPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff


class IsAbertStaffPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user.username == 'Альберт' and request.user.is_staff


class IsNotAdmindPermission(BasePermission):

    def has_permission(self, request, view):
        return not request.user.is_superuser
