import certifi
from app.src.config.twilio import get_twilio_config
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

def get_twilio_client(verify=False):
    account_sid, auth_token, *_ = get_twilio_config().values()
    
    # Create a custom HTTP client with SSL verification
    http_client = TwilioHttpClient()
    
    # Set SSL certificate verification
    http_client.session.verify = certifi.where() if verify else False
    
    return Client(
        account_sid,
        auth_token,
        http_client=http_client
    )