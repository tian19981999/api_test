
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from api import models

class checklogin():
    def authenticate(self, request):
        token = request.GET.get('token')
        obj = models.UserToken.objects.filter(token=token).first()
        if not obj:
            return False
        return True