
# Öğrenci kayıt sistemi

students = []

def add_student(student_info, number):
    students.append({
        "İsim ve Soyisim": student_info,
        "number": number,
    })

def delete_student(student_info):
    for student in students:
        if student["İsim ve Soyisim"] == student_info:
            students.remove(student)
        else:
            break

def listOfStudent():
    for student in students:
        print(f"{student['number']}: {student['İsim ve Soyisim']} ")

def listByNumer():
    for student in students:
        print(f"{student['number']}")                

# Kullanıcı girişi
while True:
    print("1- Öğrenci Ekle")
    print("2- Öğrenci Sil")
    print("3- Öğrenci Listele")
    print("4- Öğrenci Numaraları")
    print("5- Çoklu Öğrenci Sil"  )
    print("6- Çoklu Öğrenci Ekle")
    print("7- Çıkış")
    secim = input("Seçiminiz: ")

    if secim == "1":
        student_info = input("Öğrencinin isim ve soyismi: ")
        number = input("Öğrencinin numarası: ")
        add_student(student_info, number)
        print("----Kayıt başarılı.----")
    elif secim == "2":
        students_info = input("Silinecek öğrencinin isim ve soyismi: ")
        delete_student(students_info)
        print("----Kayıt başarılı ile silindi.----")
    elif secim == "3":
        listOfStudent()
        print("-------------------------------------------------")
    elif secim == "4":
        listByNumer() 
        
    elif secim == "5":
        count=int(input("Silinecek öğrenci sayısını giriniz:"))
        for i in range(count):
            students_info = input("Silinecek öğrencinin isim ve soyismi: ")
            delete_student(students_info)
        print("----Kayıt başarılı ile silindi.----")
    elif secim == "6":
        count=int(input("Silinecek öğrenci sayısını giriniz:"))
        for i in range(count):
            student_info = input("Öğrencinin isim ve soyismi: ")
            number = input("Öğrencinin numarası: ")
        add_student(student_info, number)
        print("----Kayıt başarılı.----")
    elif secim == "7":
        break
    else:
        print("Geçersiz seçim!")