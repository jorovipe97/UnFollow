#Importando librerias
from time import sleep
from random import randint
import tweepy
from credenciales import *

# Configurando credenciales del bot
print ("Identificando app")
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
print ("Dando pemriso")
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
print ("Secure == true")
auth.secure = True;
print ("Configurando auth en la api")
api = tweepy.API(auth)
user = api.get_user(USER_SCREEN_NAME)
print ("%s, description: %s" % (user.screen_name, user.description))


def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            sleep(15 * 60)
        except StopIteration:
        	break

# Usuarios q siguen al usuario indicado
print ("Buscando lista de seguidores")
followers = api.followers_ids(user.screen_name)

# Lista de usuarios que sigue al usuario indicado
print ("Buscando lista de cuentas que sigo")
friends = limit_handled( tweepy.Cursor(api.friends).items() )

for friend in friends:
    print ("Buscando...")
    try:
        if friend.id not in followers:
            if 2 < randint(0, 9) < 7:
                print ("Se dejo de seguir a: %s, description: %s " % (friend.screen_name, friend.description))
                api.destroy_friendship(friend)
                sleep(30)
            else:
                print ("%s no me esta siguiendo pero lo seguire un rato mas" % friend.screen_name)
    except tweepy.RateLimitError:
        sleep(15*60)
    except tweepy.error.TweepError:
        continue
    except StopIteration:
        break
