from django.db import models
from random import randint
from requests import get

# Create your models here.
class Greeting(models.Model):
    farts = []

    # NoOp (comment out when deploying with code below)
    def random_fart(self):
        return {"sound": ""}

   # Uncomment below for actual audio functionality
   #for i in range(0,20):
   #    try:
   #        fart = get("https://sfx-api.herokuapp.com/farts/random").json()
   #        farts.append(fart)
   #    except:
   #        pass
   #
   #def random_fart(self):
   #    fart = Greeting.farts[randint(0,len(Greeting.farts)-1)]
   #    return fart if fart else {"sound": ""}
