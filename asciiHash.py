# Mühendislik projesi 1. ödev
# Erkan Ercan 2015213024
# Yazılan dil : Python3

# Her bir açıklama satırı altındaki
# fonksiyon ya da işlemi açıklamak için yazılmıştır.

# Python üzerinde dizi yapısı olmadığı için 203 indisli
# ve indisleri NULL olan bir liste oluşturuluyor.
global lstHashListesi
lstHashListesi = []
for i in range(0, 211):
    lstHashListesi.append(None)


def dosyaAc():
    # Üstteki satırda dosya açma işlemi yapılıyor.
    # lstKelimeler değişkeni diğer fonksiyonlarda kullanılmak için
    # global yapılıyor.
    global lstKelimeler
    # txt dosyası açılıp her satır ayrı ayrı listeye atılıyor.
    lstKelimeler = open("kelimeler.txt").read().splitlines()
    # Tüm kelimeler tek tek kontrol edilerek küçük harfe dönüştürülüyor
    lstKelimeler = [item.lower() for item in lstKelimeler]

# Python üzerinde hali hazırda bir hash() fonksiyonu bulunduğu için hash()
# olarak istenen fonksiyonun ismi hashBul yapıldı.


def hashBul(key, n):
    # ascii toplamları bulunan kelimeler listede yerlerine
    # quadratic probing yöntemi ile yerleştiriliyor
    global quadraticYerlestirmeSayisi
    sayac = 1
    quadraticYerlestirmeSayisi = key % n
    # yerleştirilene kadar dönmesi için bir sonsuz döngü
    while n > 1:

        if lstHashListesi[quadraticYerlestirmeSayisi] is None:
            lstHashListesi[quadraticYerlestirmeSayisi] = key
            break

        else:
            quadraticYerlestirmeSayisi = (
                quadraticYerlestirmeSayisi + pow(sayac, 2)) % n
            sayac = sayac + 1


# alınan kelimeler for döngüsü ile tek tek karakterlerine ayırılıp ascii
# numaraları ile keyler oluşturuluyor.
def karakterListesiOlustur():
    global quadraticCarpimSayisi, key
    for kelime in lstKelimeler:
        key = 0
        # her kelime tek tek harflerine ayrılıyor.
        karakterAyir = list(kelime)
        # kelimenin uzunluğu bulunuyor (quadratic probing yöntemi için.)
        quadraticCarpimSayisi = 1
        for harf in karakterAyir:
            # ascii numaraları bulunup toplanıyor
            key = key + ord(harf) * pow(quadraticCarpimSayisi, 4)
            quadraticCarpimSayisi = quadraticCarpimSayisi + 1
        hashBul(key, len(lstHashListesi))


def girisHarflereAyir(kullaniciGiris):
    # Kullanıcıdan alınan kelime harflerine ayrılarak
    # kullaniciHarfListesi dizisine harf harf atanıyor.
    global kullaniciHashToplam
    global kullaniciHarfListesi
    kullaniciHashToplam = 0
    kullaniciHarfListesi = []
    quadraticCarpimSayisi = 1
    for harf in kullaniciGiris:
        kullaniciHarfListesi.append(harf)
        # Kullanıcı girişinin hash değeri bulunuyor.
        kullaniciHashToplam = kullaniciHashToplam + \
            (ord(harf) * pow(quadraticCarpimSayisi, 4))
        quadraticCarpimSayisi = quadraticCarpimSayisi + 1
    print("Aradığınız kelimenin harflerine ayrılmış hali : "
          + str(kullaniciHarfListesi) +
          "\nAradığınız kelimenin hash değeri : "
          + str(kullaniciHashToplam))


def listedeAra(kullaniciHashToplam):
    bulunanIndex = None
    # Diğer programlama dillerinde de olan try-catch yöntemi ile dizide
    # aranan kelimenin olup olmadığı kontrol ediliyor.
    try:
        # Kelime bulunursa ekrana kaçıncı indiste bulunduğu yazdırılıyor.
        bulunanIndex = lstHashListesi.index(kullaniciHashToplam)
        print("Kelimeniz listenin " + str(bulunanIndex) + ". elemanında.")
    except ValueError:
        print("Aradığınız kelime girilen hali ile listede yok.")
        # Kelime bulunamadığı için harf eksiltilerek ve harf değiştirerek
        # arama işlemine başlanıyor.
        kelimeEksiltAra(kullaniciHarfListesi)
        kelimeDegistirAra(kullaniciHarfListesi)


def kelimeEksiltAra(kullaniciHarfListesi):
    bulunanIndex = None
    lstYeniString = []
    a = 0
    print("\nHarf eksiltilerek arama işlemine başlanıyor...")
    print("************************************************")
    print("\nAranacak kelimenin ilk hali : " + str(kullaniciHarfListesi))
    for i in kullaniciHarfListesi:
        kullaniciHashToplam = 0
        quadraticCarpimSayisi = 1
        lstYeniString = list(kullaniciHarfListesi)
        lstYeniString.pop(a)
        print("\nŞimdiki aranan kelime : " + str(lstYeniString))
        # İçerisinden harfi çıkarılan yeni kelimenin hash değeri hesaplanıyor.
        for i in lstYeniString:
            kullaniciHashToplam = kullaniciHashToplam + \
                (ord(i) * pow(quadraticCarpimSayisi, 4))
            quadraticCarpimSayisi = quadraticCarpimSayisi + 1

        a = a + 1
        # Aranan kelimenin liste içinde kontrolü
        # try-catch yöntemi ile yapılıyor.
        try:
            bulunanIndex = lstHashListesi.index(kullaniciHashToplam)
            print("Aradığınız kelime " + str(lstYeniString) +
                  " haliyle listenin " + str(bulunanIndex) +
                  " index numarasında bulunmaktadır.")
        except ValueError:
            print("Aradığınız kelime " + str(lstYeniString) +
                  " haliyle dizide bulunmamaktadır.")


def kelimeDegistirAra(kullaniciHarfListesi):
    bulunanIndex = None
    lstYeniString = []
    print("\nHarf değiştirilerek arama işlemine başlanıyor...")
    print("************************************************")
    print("\nAranacak kelimenin ilk hali : " + str(kullaniciHarfListesi))
    # For döngüsünü n-1 kez dönecek şekilde ayarlıyorum.
    for item in range(0, len(kullaniciHarfListesi) - 1):
        kullaniciHashToplam = 0
        quadraticCarpimSayisi = 1
        lstYeniString = list(kullaniciHarfListesi)
        # lstYeniString[item],lstYeniString[item + 1]
        # = lstYeniString[item + 1], lstYeniString[item]
        # Aşağıdaki satırda listenin "i" indisinde bulunan eleman ile "i+1"
        # insidinde bulunan eleman yer değiştirliyor.
        lstYeniString[item], lstYeniString[item + 1] = \
            lstYeniString[item + 1], lstYeniString[item]
        for harf in lstYeniString:
            kullaniciHashToplam = kullaniciHashToplam + \
                (ord(harf) * pow(quadraticCarpimSayisi, 4))
            quadraticCarpimSayisi = quadraticCarpimSayisi + 1
        print("\nKelimenin [" + str(item) + "] ve [" + str(item + 1) +
              "] indislerinin yer değiştirmiş hali : " + str(lstYeniString))
        print("Aranan kelimenin hash değeri : " + str(kullaniciHashToplam))
        try:
            bulunanIndex = lstHashListesi.index(kullaniciHashToplam)
            print("Aradığınız kelime " + str(lstYeniString) +
                  " haliyle listenin " + str(bulunanIndex) +
                  " index numarasında bulunmaktadır.")
        except:
            print("Aradığınız kelime " + str(lstYeniString) +
                  " haliyle dizide bulunmamaktadır.")


# Dosya açma ve karakter listesi oluşturup
# hash dizisine atama fonksiyonları çalıştırılıyor.
dosyaAc()
karakterListesiOlustur()
print("Hash listesinin son hali : \n")
for item in range(len(lstHashListesi)):
    print("[" + str(item) + "]=" + str(lstHashListesi[item]), end=", ")
# Arama için kullanıcıdan giriş alınıyor.
print("Lütfen aramak istediğiniz kelimeyi giriniz :")
kullaniciGiris = input()
# Kullanıcının girişi harflerine ayrılıyor.
girisHarflereAyir(kullaniciGiris)
# Listede arama fonksiyonu çalıştırılıyor.
listedeAra(kullaniciHashToplam)
