import twitter
import json


CONSUMER_KEY = 'CK0GtRYmjIZxbSFtSq87CPuM5'
CONSUMER_SECRET = 'Gs8REPBqigYbHoqmMdBiyRh7FUFGxQbMzOmrqxuCHybTRoA546'
OAUTH_TOKEN = '1220398224768425984-O5yUX2rknRGKmW9DXBlCnVWWR3q2fy'
OAUTH_TOKEN_SECRET = 'JKxewUQOWTYYERFktuZsYkj0PaLfAxHLLYJVrA8koMQ2S'

WORLD_WOE_ID = 1
US_WOE_ID = 23424977
CDMX_WOE_ID = 116545   #trends Cuidad de Mexico
MX_WOE_ID = 23424900

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

# Nothing to see by displaying twitter_api except that it's now a
# defined variable
b
print(twitter_api)
world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)
mx_trends= twitter_api.trends.place(_id=MX_WOE_ID)


#print(json.dumps(world_trends, indent=1))
#print()
#print(json.dumps(us_trends, indent=1))
print(json.dumps(mx_trends, indent=1))
