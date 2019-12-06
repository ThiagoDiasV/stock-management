from django.utils.crypto import get_random_string

chars = "abcdefghijklmnopqrstuvxwyz0123456789!@$%^&*(-_=+)"

CONFIG_STRING = f"""
DEBUG=True
SECRET_KEY={get_random_string(50, chars)}
ALLOWED_HOSTS=127.0.0.1, .localhost
#DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
#DEFAULT_FROM_EMAIL=
#EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
#EMAIL_HOST=
#EMAIL_PORT=
#EMAIL_USE_TLS=
#EMAIL_HOST_USER=
#EMAIL_HOST_PASSWORD=
"""

with open(".env", "w") as config_file:
    config_file.write(CONFIG_STRING)
