from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
from rest_framework.viewsets import GenericViewSet,ViewSetMixin
from api.serializers.course import CourseSerializer,CourseDetailSerializer
from api.auth.auth import checklogin

class CourseView(ViewSetMixin,APIView):
    def list(self,request,*args,**kwargs):
        """
        课程列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code':1000,'data':None}

        try:
            queryset = models.Course.objects.all()
            ser = CourseSerializer(instance=queryset,many=True)
            ret['data'] = ser.data
        except Exception as e:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'

        return Response(ret)

    def retrieve(self,request,*args,**kwargs):
        """
        课程详细接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'data': None}
        # token = request.GET.get('token')
        # obj = models.UserToken.objects.filter(token=token).first()
        if checklogin.authenticate(self,request)==False:
            ret['code'] = 1001
            ret['error'] = '获取课程失败'
            ret['token'] = request.GET.get('token')
        else:
            try:
            # 课程ID=2
                pk = kwargs.get('pk')

            # 课程详细对象
                obj = models.CourseDetail.objects.filter(course_id=pk).first()

                ser = CourseDetailSerializer(instance=obj,many=False)

                ret['data'] = ser.data
                ret['token']=request.GET.get('token')
            except Exception as e:
                ret['code'] = 1001
                ret['error'] = '获取课程失败'

        return Response(ret)


