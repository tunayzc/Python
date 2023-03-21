class Human:
    #built-in yani consturactor
    def __init__(self,name):
        self.name=name
        print("Bir human instance'ı üretildi")
    def __str__(self):
        return f"STR Fonksiyonundan dönen değer: {self.name}"
    def talk(self,sentence):
        print(f"{self.name} {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

human1= Human("Tuna")
human1.talk("Merhaba")
human1.walk()
print(human1)

human2=Human("Ahmet")
human2.talk("Merhaba")
human2.walk()
print(human2)

human3=Human("Tunahan")
human3.talk("Selam")
human3.walk()
print(human3)