from app.src.config import get_env_vars


def get_twilio_config():
    return {
        "account_sid": get_env_vars("TWILIO_ACCOUNT_SID"),
        "auth_token": get_env_vars("TWILIO_AUTH_TOKEN"),
        "content_sid" : get_env_vars("TWILIO_CONTENT_SID"),
        "phone_number": get_env_vars("TWILIO_PHONE_NUMBER"),
        "whatsapp_number" : get_env_vars("TWILIO_WHATSAPP_NUMBER")
    }
