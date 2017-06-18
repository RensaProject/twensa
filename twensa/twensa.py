import nodebox_linguistics_extended as nle
from rensabrain.Brain import *
import tweepy
from config import *

def setup_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return tweepy.API(auth)

def run_timeline_query(api):
    return api.search(q=query, lang=language, count=num_tweets, geocode=query_geocode, since_id=query_since_id)

def get_hashtags(s):
    return list(part[1:].replace(",","") for part in s.split() if part.startswith('#'))

def analyze_tweet(tweet):
    tw = tweet.text.encode('utf-8')
    rid_scores = nle.content.categorise(tw)
    return {
        "user_name":tweet.user.name,
        "user_id": tweet.user.id,
        "text": tw,
        "screen_name": tweet.user.screen_name,
        "favorite_count": tweet.favorite_count,
        "retweet_count": tweet.retweet_count,
        "created_at": str(tweet.created_at),
        "hashtags": get_hashtags(tw),
        "keywords": nle.content.keywords(tw, top=10, nouns=True, singularize=True, filters=[]),
        "rid_primary": str(rid_scores.primary),
        "rid_secondary": str(rid_scores.secondary),
        "rid_emotions": str(rid_scores.emotions)
    }

def main():
    api = setup_api()
    results = run_timeline_query(api)
    assertions = []
    for tweet in results:
        assertions.append(analyze_tweet(tweet))
    tweet_info = make_brain(assertions)
    tweet_info.save_brain("assertions/")
    delete_old_assertions("assertions/")

if __name__ == '__main__':
    main()
