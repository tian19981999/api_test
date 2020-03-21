class MiddlewareMixin:
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        response = response or self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response

class middleservice(MiddlewareMixin):
    def process_response(self,request,response):
        # 允许跨域
        response['Access-Control-Allow-Origin']='*'
        # 允许携带的请求头，用逗号隔开
        response['Access-Control-Allow-Headers']='Content-Type'
        # 允许请求的方法
        response['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE'

        return response