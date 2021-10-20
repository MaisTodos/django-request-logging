from unittest.mock import patch

import freezegun
from django.test import TestCase


class middlewareTest(TestCase):
    @freezegun.freeze_time("2020-01-01")
    @patch("request_logging.middleware.request_logger")
    def test_ping(self, mock_logger):

        self.client.get("/ping")

        # essa foi a resposta que obtive quando alterei o middleware pra não pegar o
        # request.user.pk na linha 37
        mock_logger.info.assert_called_once_with(
            {
                "message": "django_api_request",
                "remote_address": "127.0.0.1",
                "request_method": "GET",
                "request_path_base": "/ping",
                "request_path": "/ping",
                "request_querystring": {},
                "response_code": 301,
                "user": "null",  # no motor quando não tem usuario logado fica assim
                "starts_at": 1577836800.0,
                "ends_at": 1577836800.0,
                "run_time": 0.0,
                "athena_table": "motor_api_request",
                "athena": True,
            }
        )
