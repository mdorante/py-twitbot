import setup
from setup import twitter_auth, logger
import tweepy
import logging
import time


def like_mention(auth, tweet):
    '''Like the tweet that you are mentioned in.

    Args:
        auth  (str): Your Twitter API authentication object.
        tweet (str): The tweet that you are mentioned in.
    '''

    if not tweet.favorited:
        logger.info(
            f'Liking mention: {tweet.text} by {tweet.user.screen_name}')
        tweet.favorite()


def follow_mentioner(auth, tweet):
    '''Follows the user that mentioned you.

    Args:
        auth  (str): Your Twitter API authentication object.
        tweet (str): The tweet that you are mentioned in.
    '''

    if not tweet.user.following:
        logger.info(f'Following: {tweet.user.screen_name}')
        tweet.user.follow()


def check_mentions(auth, last_id):
    '''Retrieves all your mentions starting from the last processed mention.

    Args:
        auth    (str): Your Twitter API authentication object.
        last_id (int): The tweet ID of the last processed tweet you were mentioned in.

    Returns:
        new_last_id (int): The updated ID of the last processed tweet you were mentioned in.
    '''

    logger.info('Retrieving mentions')
    new_last_id = last_id
    for tweet in tweepy.Cursor(auth.mentions_timeline, since_id=new_last_id).items():
        new_last_id = max(tweet.id, new_last_id)
        if tweet.in_reply_to_status_id is not None:  # Evaluates to True if tweet is a reply
            like_mention(auth, tweet)
            follow_mentioner(auth, tweet)
    return new_last_id


def main():
    '''Indefinitely like tweets that mention you and follows the users that tweeted them.
    Takes a 5 minute break after each iteration.'''

    twitter = twitter_auth()
    last_id = 1
    while True:
        last_id = check_mentions(twitter, last_id)
        logger.info('Like and follow - Waiting five minutes...')
        time.sleep(300)


if __name__ == '__main__':
    main()
