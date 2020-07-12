from setup import twitter

basic_hashtags = [
    '#100DaysOfCode',
    '#Python',
    '#PythonProgramming',
    '#CodeNewbie'
]


def tweet_formatter(tweet_string):
    ''' Add basic hashtags to tweets

    Args:
        tweet_string (str): The tweet you want to add hashtags to
    
    Returns:
        tweet (str): The tweet with hashtags added on a new line.
    '''

    tweet = tweet_string + f'\n {" ".join(basic_hashtags)}'
    return tweet


def post_tweet(tweet):
    '''Post your formatted tweet.

    Args:
        tweet (str): The tweet you want to post.

    Returns:
        none
    '''
    
    twitter.update_status(tweet_formatter(tweet))
    print(f'Tweeted: {tweet_formatter(tweet)}')
