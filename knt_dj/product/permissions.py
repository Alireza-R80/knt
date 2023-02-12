import jwt
from rest_framework.permissions import BasePermission

from account.models import BaseUser


class GetOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            token = request.COOKIES.get('jwt')
            if not token:
                return False
            try:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                return False
            user = BaseUser.objects.get(id=payload['id'])
            if user.role == 'DES':
                return True
            else:
                return False
        else:
            return bool(request.user.is_staff)
