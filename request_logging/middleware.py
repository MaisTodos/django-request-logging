import json
import logging
import re
import time

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin

# request_logger = logging.getLogger("api_request")


class RequestLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()

    # def extract_log_info(self, request, response):
    #     ends_at = time.time()
    #     run_time = ends_at - request.start_time

    #     url_ = request.path
    #     url_base = re.sub(r"\/\d+", "/{id}", url_)
    #     url_base = re.sub(r"\/apply-coupon/?([^\/]*)?", "/apply-coupon/{id}", url_base)

    #     log_data = {
    #         "message": "django_api_request",
    #         "athena_table": "motor_api_request",
    #         "athena": True,
    #         "remote_address": request.META["REMOTE_ADDR"],
    #         "request_method": request.method,
    #         "request_path_base": url_base,
    #         "request_path": request.path,
    #         "request_querystring": dict(request.GET.items()),
    #         "response_code": response.status_code,
    #         "user": request.user.pk,
    #         "starts_at": request.start_time,
    #         "ends_at": ends_at,
    #         "run_time": run_time,
    #     }

    #     conditions_to_log_response = [
    #         request.method != "GET",
    #         response.get("content-type") == "application/json",
    #         response.content,
    #     ]

    #     if all(conditions_to_log_response):
    #         try:
    #             log_data["response_body"] = json.loads(response.content.decode("utf-8"))
    #         except json.decoder.JSONDecodeError:
    #             request_logger.error(
    #                 {
    #                     "message": "api_response_decode_error",
    #                     "request_method": request.method,
    #                     "request_path": request.get_full_path(),
    #                     "response_code": response.status_code,
    #                     "response_body": str(response.content.decode("utf-8")),
    #                 }
    #             )

    #     return log_data

    def process_response(self, request, response):
        # if str(request.get_full_path()).startswith("/api/"):
        #     log_data = self.extract_log_info(request=request, response=response)
        #     request_logger.info(log_data)
        return response
