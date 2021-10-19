from django.http import HttpResponse
from django.views.generic import View


class PingView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("pong")
