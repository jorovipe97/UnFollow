# -*- coding: utf-8 -*-
#Importando librerias
from time import sleep
import random
import tweepy
from credenciales import *

## Instrucciones de uso
# Cree un archivo llamado credenciales.py y dentro defina y asignele el valor correspondiente a las siguientes variables:
# USER_SCREEN_NAME
# CONSUMER_KEY
# CONSUMER_SECRET
# ACCESS_TOKEN
# ACCESS_TOKEN_SECRET

# Configurando credenciales del bot
print ("Identificando app")
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
print ("Dando pemriso")
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
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
print ("\nBuscando lista de seguidores")
followers = api.followers_ids(user.screen_name)
print ("Lista de seguidores cargada")

for friend in limit_handled( tweepy.Cursor(api.friends).items() ):
    print ("Buscando usuarios que no siguen a @" + USER_SCREEN_NAME)    
    try:
        if friend.id not in followers:
            luckNumber = random.randint(0, 9)
            print ("2 < %s = %s" % (luckNumber, 1 < luckNumber))
            if 2 < luckNumber:                
                api.destroy_friendship(friend.id)
                print ("\nSe dejo de seguir a: %s, description: %s " % (friend.screen_name, friend.description))
            else:
                print ("\n%s no me esta siguiendo pero lo seguire un rato mas" % friend.screen_name)
    except tweepy.RateLimitError:
        print ("\nRate Limit Error, esperar 15 minutos")
        sleep(15*60)
    except tweepy.error.TweepError:
        print ("\nTweepy error, continuar al siguiente")
        continue
    except StopIteration:
        print ("StopIteration exception.... Bot finalizado")
        break
    except UnicodeEncodeError:
        print ("\nError de codificado detectado\n")
        continue
print ("...Bot finalizdo")