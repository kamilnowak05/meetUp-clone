from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrAdminOrReadOnly(BasePermission):
    message = "You have to be an admin or owner of this object"

    def has_object_permission(self, request, view, obj):
        if request.method in ["GET"]:
            return True
        try:
            if request.user:
                return obj.user == request.user or request.user.admin
        except Exception:
            return self.message


class IsOwnerOrReadOnly(BasePermission):
    message = "You have to be owner of this object"

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        return obj.owner == request.user


class IsOwnerGroupOrReadOnly(BasePermission):
    message = "You have to be owner of this object"

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        return obj.owner_group.owner == request.user


class IsOwnerOrAdmin(BasePermission):
    message = "You have to be owner of this object"

    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        return obj.user == request.user

    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user and request.user.admin)
