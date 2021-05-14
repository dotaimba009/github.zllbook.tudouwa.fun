import os

# Mail settings:
MAIL_SERVER = os.environ.get("REDASH_MAIL_SERVER", "localhost")
MAIL_PORT = int(os.environ.get("REDASH_MAIL_PORT", 25))
# MAIL_USE_TLS = parse_boolean(os.environ.get("REDASH_MAIL_USE_TLS", "false"))
# MAIL_USE_SSL = parse_boolean(os.environ.get("REDASH_MAIL_USE_SSL", "false"))
MAIL_USERNAME = os.environ.get("REDASH_MAIL_USERNAME", None)
MAIL_PASSWORD = os.environ.get("REDASH_MAIL_PASSWORD", None)
MAIL_DEFAULT_SENDER = os.environ.get("REDASH_MAIL_DEFAULT_SENDER", None)
MAIL_MAX_EMAILS = os.environ.get("REDASH_MAIL_MAX_EMAILS", None)


# MAIL_ASCII_ATTACHMENTS = parse_boolean(
#     os.environ.get("REDASH_MAIL_ASCII_ATTACHMENTS", "false")
# )


def email_server_is_configured():
    return MAIL_DEFAULT_SENDER is not None


HOST = os.environ.get("REDASH_HOST", "")

SEND_FAILURE_EMAIL_INTERVAL = int(
    os.environ.get("REDASH_SEND_FAILURE_EMAIL_INTERVAL", 60)
)
MAX_FAILURE_REPORTS_PER_QUERY = int(
    os.environ.get("REDASH_MAX_FAILURE_REPORTS_PER_QUERY", 100)
)

ALERTS_DEFAULT_MAIL_SUBJECT_TEMPLATE = os.environ.get(
    "REDASH_ALERTS_DEFAULT_MAIL_SUBJECT_TEMPLATE", "({state}) {alert_name}"
)
