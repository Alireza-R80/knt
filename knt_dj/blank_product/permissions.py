import jwt
from rest_framework.permissions import BasePermission

from account.models import BaseUser


class DesignerGetOnly(BasePermission):

    def has_permission(self, request, view):
        token = request.COOKIES.get('jwt')
        if not token:
            return False
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return False
        user = BaseUser.objects.get(id=payload['id'])
        if request.method == 'GET' and user.role == 'DES':
            return True
        else:
            return bool(request.user.is_staff)
