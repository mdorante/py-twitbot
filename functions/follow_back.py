import setup
from setup import twitter_auth, logger
import tweepy
import logging
import time


def follow_followers(auth):
    '''Follows all unfollowed followers.

    Args:
        auth (str): Your Twitter API authentication object

    Returns:
        none
    '''

    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(auth.followers).items():
        if not follower.following:
            logger.info(f'Following {follower.screen_name}')
            follower.follow()


def main():
    '''Indefinitely follows back users who follow you.
    Takes a 5 minute break after each iteration.'''

    twitter = twitter_auth()
    while True:
        follow_followers(twitter)
        logger.info('Follow back - Waiting five minutes...')
        time.sleep(300)


if __name__ == '__main__':
    main()
