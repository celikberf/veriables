"""
Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

Müşteri adı 
Müşteri soyadı
Müşteri ad + soyad
Müşteri cinsiyet
Müşteri tc kimlik
Müşteri doğum yılı
Müşteri adres bilgisi
Müşteri yaşı

"""

musteriAdi  = "Berfin"
musteriSoyadi = " Çelik"
musteriCinsiyet = True #Kadın
musteriTcKimlik = "231231231321" #herhangi bir işlem yapmayacağız. String olarak tanımlayabılırız.
musteriDogumYili = 1999
musteriAdres = "Ankara"
musteriYas = (2024- musteriDogumYili)
musteriAdiveSoyadi = musteriAdi + musteriSoyadi

print(musteriAdiveSoyadi)

"""
Aşağıdaki siparişlerin toplam bilgisini hesaplayınız. 

Sipariş 1 => 110 TL
Sipariş 2 => 1100.5 TL
Sipariş 3 => 356.95 TL

"""

siparis1 = 110
siparis2 = 1100.5
siparis3 = 356.95

toplamSiparis = siparis1 + siparis2 + siparis3

print("Toplam : " , toplamSiparis)
