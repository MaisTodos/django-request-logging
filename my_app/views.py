from django.http import JsonResponse
from django.views.generic import View


class PingView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({"pong": True})

    def post(self, request, *args, **kwargs):
        return JsonResponse({"pong": True})
