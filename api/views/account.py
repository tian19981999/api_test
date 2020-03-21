from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from api import models
import uuid


class AuthView(APIView):

    def post(self,request,*args,**kwargs):
        """
        用户登录认证
        :param request:
        :param args:
        :param kwargs:
        :return:
        """

        ret = {'code':1000}
        user = request.data.get('user')
        pwd = request.data.get('pwd')

        user = models.UserInfo.objects.filter(user=user,pwd=pwd).first()
        if not user:
            ret['code'] = 1001
            ret['error'] = '用户名或密码错误'
        else:
            uid = str(uuid.uuid4())
            models.UserToken.objects.update_or_create(user=user,defaults={'token':uid})
            ret['token'] = uid
        return Response(ret)