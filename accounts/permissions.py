from rest_framework import permissions

from config import constants


class IsOperator(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == constants.UserType.OPERATOR
