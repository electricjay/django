from django.http import HttpResponsePermanentRedirect


class RedirectInResponseMiddleware(object):
    def process_response(self, request, response):
        if request.get_full_path() == '/nest_redirect':
            return HttpResponsePermanentRedirect('/REDIRECTED')
        return response


class RedirectInRequestMiddleware(object):
    def process_request(self, request):
        if request.get_full_path() == '/nest_redirect':
            return HttpResponsePermanentRedirect('/REDIRECTED')
        return None
