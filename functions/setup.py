from dotenv import load_dotenv
import os
import tweepy
import logging

# Load environment variables
load_dotenv()

# Initialize logger
logging.basicConfig(level=logging.INFO, filename='/app/log/bot.log', filemode='a', format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger()


def twitter_auth():
    '''Authenticate to the Twitter API.
    
    Returns:
        twitter (obj): Your Twitter API authentication object.
    '''

    consumer_api_key = os.environ['CONSUMER_API_KEY']
    consumer_secret_key = os.environ['CONSUMER_SECRET_KEY']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_api_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    twitter = tweepy.API(auth, wait_on_rate_limit=True,
                         wait_on_rate_limit_notify=True)

    try:
        twitter.verify_credentials()
        logger.info('Authentication OK')
    except Exception as e:
        logger.error('Error during Authentication', exc_info=True)
        raise e

    return twitter
