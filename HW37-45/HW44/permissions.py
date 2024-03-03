from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Разрешение, которое позволяет доступ только для чтения всем
пользователям,
а редактирование - только администраторам.
"""

    def has_permission(self, request, view):
        # Чтение разрешено всем пользователям, поэтому разрешаем GET, HEAD или OPTIONS запросы.
        if request.method in permissions.SAFE_METHODS:
            return True
        
        #Запись разрешена только администраторам.
        return request.user.is_superuser