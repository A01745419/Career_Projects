# Set this variable to a trending topic, or anything else
# for that matter. The example query below was a
# trending topic when this content was being developed
# and is used throughout the remainder of this chapter.
import twitter
import json
from collections import Counter  #contador sencillo
from prettytable import PrettyTable #libreria para hacer tablas bonitas
from firebase import firebase
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
q = '#ObamaGate'

CONSUMER_KEY = 'CK0GtRYmjIZxbSFtSq87CPuM5'
CONSUMER_SECRET = 'Gs8REPBqigYbHoqmMdBiyRh7FUFGxQbMzOmrqxuCHybTRoA546'
OAUTH_TOKEN = '1220398224768425984-vAxiIM9YPEaNMq2tsfysMa0mPdgB16'
OAUTH_TOKEN_SECRET = 'cbjHHAfsv3UDz6idiyAWQDa3C3gkqF1aa98n21UNC92Bz'

WORLD_WOE_ID = 1
US_WOE_ID = 23424977
MX_WOE_ID = 23424900   #trends Cuidad de Mexico
count = 100

# Import unquote to prevent URL encoding errors in next_results
from urllib.parse import unquote

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)
print(twitter_api)

# See https://dev.twitter.com/rest/reference/get/search/tweets

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']
#print(json.dumps(statuses, indent=1))

# Iterate through 5 more batches of results by following the cursor
for _ in range(5):
    print('Length of statuses', len(statuses))
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError as e: # No more results when next_results doesn't exist
        break

    # Create a dictionary from next_results, which has the following form:
    # ?max_id=847960489447628799&q=%23RIPSelena&count=100&include_entities=1
    kwargs = dict([ kv.split('=') for kv in unquote(next_results[1:]).split("&") ])

    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']
#print(statuses)
# Show one sample search result by slicing the list...
#print(json.dumps(statuses[0], indent=1))

#gets ten texts with their favorite or retweet count
for i in range(10):
    print()
    #print(statuses[i]['text'])
    print('Favorites: ', statuses[i]['favorite_count'])
    print('Retweets: ', statuses[i]['retweet_count'])


firebase = firebase.FirebaseApplication('https://twitter-tec-977f1.firebaseio.com/', None)
result = firebase.post('/twitter-tec-977f1/Tweet/',statuses)

status_texts = [ status['text']
                 for status in statuses ]

screen_names = [ user_mention['screen_name']
                 for status in statuses
                     for user_mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text']
             for status in statuses
                 for hashtag in status['entities']['hashtags'] ]

#create or append a new table with the current
firebase.post('/twitter-tec-977f1/Status_text/',status_texts)
firebase.post('/twitter-tec-977f1/Screen_Names/',screen_names)
firebase.post('/twitter-tec-977f1/Hashtags/',hashtags)



# Compute a collection of all words from all tweets
words = [ w
          for t in status_texts
              for w in t.split() ]

# Explore the first 5 items for each...
firebase.post('/twitter-tec-977f1/Words/',words)

print(json.dumps(status_texts[0:5], indent=1))
print(json.dumps(screen_names[0:5], indent=1))
print(json.dumps(hashtags[0:5], indent=1))
print(json.dumps(words[0:5], indent=1))

for item in [words, screen_names, hashtags]:
    c = Counter(item)
    print(c.most_common()[:10]) # top 10
    print()

for label, data in (('Word', words),
                    ('Screen Name', screen_names),
                    ('Hashtag', hashtags)):
    pt = PrettyTable(field_names=[label, 'Count'])
    c = Counter(data)
    [ pt.add_row(kv) for kv in c.most_common()[:10] ]
    pt.align[label], pt.align['Count'] = 'l', 'r' # Set column alignment
    print(pt) 