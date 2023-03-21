import matematik as m #alias(takma isim veriyoruz)
import random #built-in moduller(hazır olan moduller)
#package dışardan alınmış paket moduller
#from matematik import topla (belli bir yapıyı import etmek)
from day2 import Human
from seleniumEx import webdriver
print(m.topla(10,20))

print(random.randint(0,150))

human1=Human("Tuna")
human1.talk("Merhaba")


#---packages---
