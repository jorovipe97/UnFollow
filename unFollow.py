#Importando librerias
from time import sleep
from random import randint
import tweepy
from credenciales import *


# Configurando credenciales del bot
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
auth.secure = True;
api = tweepy.API(auth)
user = api.get_user(USER_SCREEN_NAME)

"""
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)
        except StopIteration:
        	break
"""

# Usuarios q siguen al usuario indicado
followers = api.followers_ids(user.id)
# Lista de usuarios que sigue al usuario indicado
friends = api.friends_ids(user.id)

for friend in friends:
	if friend not in followers:
		if randint(0, 9) == 2:
			api.destroy_friendship(friend)
