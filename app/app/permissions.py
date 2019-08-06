from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrAdminOrReadOnly(BasePermission):
    message = "you must be an admin or owner of this object"
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET']:
            return True
        try:
            if(request.user):
                return obj.user == request.user or request.user.admin
        except:
            pass

class IsOwnerOrReadOnly(BasePermission):
    message = "you must the owner of this object"
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return obj.user == request.user

# class IsAdminOrReadOnly(BasePermission):
#     message = "you must the admin"
#     def has_object_permission(self, request, view, obj):
#         if request.method == 'GET':
#             return True
#         return request.user.admin

class IsAdminOrReadOnly(BasePermission):
    """
    The request is admin as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.admin
        )