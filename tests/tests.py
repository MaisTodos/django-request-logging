from json.decoder import JSONDecodeError
from unittest.mock import patch

import freezegun
from django.test import TestCase


class middlewareTest(TestCase):
    @freezegun.freeze_time("2020-01-01")
    @patch("request_logging.middleware.request_logger")
    def test_get_ping(self, mock_logger):

        self.client.get("/ping/")

        extra = {
            "message": "django_api_request",
            "remote_address": "127.0.0.1",
            "request_method": "GET",
            "request_path_base": "/ping/",
            "request_path": "/ping/",
            "request_querystring": {},
            "response_code": 200,
            "user": None,
            "starts_at": 1577836800.0,
            "ends_at": 1577836800.0,
            "run_time": 0.0,
            "athena_table": "motor_api_request",
            "athena": True,
        }
        mock_logger.info.assert_called_once_with(
            'django-request-logging',
            extra=extra
        )

    @freezegun.freeze_time("2020-01-01")
    @patch("request_logging.middleware.request_logger")
    def test_post_ping(self, mock_logger):

        self.client.post("/ping/")
        extra = {
            "message": "django_api_request",
            "remote_address": "127.0.0.1",
            "request_method": "POST",
            "request_path_base": "/ping/",
            "request_path": "/ping/",
            "request_querystring": {},
            "response_code": 200,
            "user": None,
            "starts_at": 1577836800.0,
            "ends_at": 1577836800.0,
            "run_time": 0.0,
            "athena_table": "motor_api_request",
            "athena": True,
            "response_body": {"pong": True},
        }
        mock_logger.info.assert_called_once_with(
            'django-request-logging',
            extra=extra
        )

    @freezegun.freeze_time("2020-01-01")
    @patch("request_logging.middleware.json.loads")
    @patch("request_logging.middleware.request_logger")
    def test_post_json_error(self, mock_logger, mock_json):

        mock_json.side_effect = JSONDecodeError("msg", "doc", 0)

        self.client.post("/ping/")

        mock_logger.error.assert_called_once_with(
            {
                "message": "api_response_decode_error",
                "request_method": "POST",
                "request_path": "/ping/",
                "response_code": 200,
                "response_body": '{"pong": true}',
            }
        )
        extra = {
            "message": "django_api_request",
            "remote_address": "127.0.0.1",
            "request_method": "POST",
            "request_path_base": "/ping/",
            "request_path": "/ping/",
            "request_querystring": {},
            "response_code": 200,
            "user": None,
            "starts_at": 1577836800.0,
            "ends_at": 1577836800.0,
            "run_time": 0.0,
            "athena_table": "motor_api_request",
            "athena": True,
        }
        mock_logger.info.assert_called_once_with(
            'django-request-logging',
            extra=extra
        )
