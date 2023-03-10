        #Python'da veri tipleri

#Metin tipi veriler = str, Metinsel veri saklamak için kullanılır
#Numerik (sayısal) tip veriler: 
    #int = integer tam sayı tutmak için 
    #float ondalık sayı tutmak için  
    #complex karmaşık sayılar tutmak için kullanılır
#Sequence(sıralama) tipi veriler : 
    #list = birden fazla öğeyi tutmak(liste haline getirmek) için kullanılır
    #tuple = List'ten farkı, değiştirelemez ve ilk tanımlandığı şeklinde kalır 
    #range = for döngüsünde kullanılır ve bir aralık tanımlar. Örneğin == for i in range(0,11):  print (i), 0'dan 11 e kadar anlamına gelir
#Mapping (adresleme) tipi veriler : dict == Sıralanamaz ama değiştirelebilir ve anahtar ile çağırılabilir. Anahtar:değer şeklinde tanımlanır.
#Set tipi veriler :
    #set == Pythonda set listeleri, list' e benzer ancak fark olarak set içindeki elemanlar sıralanamaz ve indekslenemez. Yani set'e eklenen bir elemanın hangi sırada olduğunu bilemeyiz.
    #frozenset == Set ile aynıdır ancak değiştirilemez. Bu yüzden kısıtlanmış küme de denir.
#boolean tip veriler : bool == True-False değerlerini tutmak için kullanılır. 
#binary tip veriler = bytes,bytearray,memoryview

        #Kodlama.io da kullanılan değişkenler
#Mail adresi ve kullanıcı şifresi : bool
#Ders ilerleme yüzdesi : float
#Kategori,eğitmenler : list
#Kurs isimleri : string

user_mail ="tunahanyzc@gmail.com"
user_pword = 12345
get_mail= input ("Lütfen mail adresinizi giriniz: ")
get_user_pword= int (input ("Lütfen şifrenizi giriniz: "))
if (get_mail == user_mail):
    if (get_user_pword == user_pword):
        print('Giriş başarılı.Hoşgeldiniz.')
    else:
        print('Hatalı veya eksik şifre girdiniz.')
else:
    print('Kullanıcı bulunamadı')

