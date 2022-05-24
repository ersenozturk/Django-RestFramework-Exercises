# istediğimiz şartı koşmak için custom permissionlar yazmak lazım
from rest_framework.permissions import BasePermission

# BasePermission içindeki bilgileri override ederek istediğimiz şekli alıcaz
class ISOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)