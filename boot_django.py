import os

import django
from django.conf import settings

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "request_logging"))


def boot_django():
    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
            }
        },
        INSTALLED_APPS=("request_logging",),
        MIDDLEWARE=["request_logging.middleware.RequestLogMiddleware"],
        REQUEST_LOGGING_CONFIG={
            "paths_regex": [
                (r"\/\d+", "/{id}"),
                (r"\/apply-coupon/?([^\/]*)?", "/apply-coupon/{id}"),
            ],
            "log_data_extra": {"athena_table": "motor_api_request", "athena": True,},
            "log_url_path": "/api/",
        },
        ROOT_URLCONF="urls",
        TIME_ZONE="UTC",
        USE_TZ=True,
    )
    django.setup()
