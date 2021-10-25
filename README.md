django-request-logging
======================

The `django-request-logging` is a Django App including RequestLogMiddleware.
This middleware can be used for improving request logging.

Installing

---------------

This app can be installed and used in your django project by:

.. code-block:: bash

    pip install https://github.com/MaisTodos/django-request-logging.git

Edit your `settings.py` file to include `'request_logging'` in the `INSTALLED_APPS`
listing.

.. code-block:: python

    INSTALLED_APPS = [
        ...

        'request_logging',
    ]

Configuring

---------------

Edit your project `settings.py`, including the `REQUEST_LOGGING_CONFIG` dict:

.. code-block:: python

    REQUEST_LOGGING_CONFIG = {
        "paths_regex_replace": [],
        "log_data_extra": {},
        "log_url_path": ""
    }

- `paths_regex_replace` (list):
  - Description: A list of regex tuples to apply in the path
  - Example: [(r"\/\d+", "/{id}")]
- `log_data_extra` (dict):
  - Description: Any extra log information you want to be logged by the middleware
  - Example: {"foo": "bar", "project": "FooBar"}
- `log_url_path` (str):
  - Description: Define the path "starts with" pattern to activate the middleware logger
  - Example: "/api/"
- `log_handler` (str):
  - Description: The django log handler to be user by the middleware
  - Example: "default"

Source

---------------

- <https://github.com/MaisTodos/django-request-logging/>

References

---------------

- <https://github.com/realpython/django-receipts>
