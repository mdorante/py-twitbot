from dotenv import load_dotenv
import os
import tweepy

# Load environment variables
load_dotenv()


# Authenticate to Twitter
auth = tweepy.OAuthHandler(
    os.environ['CONSUMER_API_KEY'], os.environ['CONSUMER_SECRET_KEY'])
auth.set_access_token(os.environ['ACCESS_TOKEN'],
                      os.environ['ACCESS_TOKEN_SECRET'])

twitter = tweepy.API(auth)

try:
    twitter.verify_credentials()
    print('Authentication OK')
except:
    print('Error during Authentication')