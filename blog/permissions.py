from rest_framework import permissions

class IsAuthorOrReadonly(permissions.BasePermission):

    """
       this class return True, for edit permission for the author of his own post else it returns false
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS: #GET, OPTIONS, and HEAD–then it is a read-only request and permission is granted
           return True
        
        return obj.author == request.user

