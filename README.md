# Yok-Atlas-Sitesi-ne-Erisim-Botu

Bu projede ‘https://yokatlas.yok.gov.tr/’ sitesine erişilip aranan bölümün hangi üniversitede olduğunu, kaç yıllık olduğunu ve devlet veya vakıf üniversitesini olduğunu gösterir.  Bu bilgileri hazırlanan arayüzde listbox’ta gösterip bir de dosyaya kaydettim.  
Yazılan kodun açıklaması ve çalıştıktan sonraki durumlar aşağıda gösterilecek.  
![image](https://user-images.githubusercontent.com/103186397/173691431-c0375514-d127-47d2-9235-b4e3aa8fc3c0.png)
*Öncelikle bu projeyi yapmak için selenium ve tkinter kütüphaneleri indirilmeli ve ayrıca botun çalışması için ‘https://chromedriver.chromium.org/downloads’ bu linkten bilgisayarınızdaki chrome’un güncel sürümüne göre Chromediver indirilmeli ve kodun yazıldığı dosyanın içerisinde bulunmalıdır.

*1. Satırda selenium kütüphanesinin webdriver özelliği import edilir.  
*2. Satırda import edilen kütüphane 13 ve 19. Satırlardaki find_element özelliğini kullanmamızı sağlar.  
*3. Satırda  import edilen kütüphane 17 ve 18. Satırlardaki send_keys özelliğini kullanmamızı sağlar.  
*4. Satırda ise time kütüphanesi import edilerek kod içerisinde time.sleep özelliğini kullanmamızı sağlar. ‘time.sleep(saniye)’ özelliği ile parantez içerisine girilen süre kadar program bekler.  
*6. Satırda ise win adlı bir pencere oluşturuyoruz. 44. Satırdaki mainloop() ile de açılan arayüz penceresinin biz kapatana kadar açık olmasını sağlıyoruz.  
*7. Satırda oluşturulan fonksiyonun özelliği aşarıda belirtilecek. Fonksiyon’a erişilmesi için önce fonksiyonun çağrılması gerekir.  
*33. Satırda oluşturduğumuz arayüz’ün boyutu ayarlanır.  
*34. Satırda l1 adında oluşturduğumuz nesne ile label oluşturduk, parantez içerisine win yazılarak oluşturduğumuz arayüzün içerisine yerleşir, text=‘isim’ ile labelin işlevini tanımlayacak isim verilir, .place ifadesi ile arayüzde yerleştirmek istediğimiz konumu ayarlayabiliriz.  
*35. Satırda e1 nesnesi ile Entry yani kullanıcıdan bilgi alabiliriz. Parantez içine win yazarak oluşturduğumuz pencerede olmasını belirtiyoruz.  
*36. Satırda e1 nesnesinin konumu belirlenir.  
*37.Satırda arayüzde buton oluşturulur,parantez içerisine win yazarak oluşturduğumuz pencerede bulunur, text=‘Ara’ ile butonun adı verilir, command=ara ile 7.satırdaki fonksiyona ulaşılır, eğer butona basılırsa 8-32 satırları çalışılır.  

#### Fonksiyon içerisindeki kodlara geçmeden önce 38-43 satırlarının açıklaması    
*41. Satırda l2 nesnesi ile win penceresine bir listBox eklenir width ve height özelliği ile listBox’ın boyutu ayarlanır.  
*42. Satırda listBox’ın konumu ayarlanır.  
*38. Satırda xx nesnesi ile bir scrollbar (kaydırma çubuğu) oluşturulur.  
*39. Satırda scrollbarın konumu ayarlanır.  
*40. Satırda ‘xscrollcommand’ ile xx nesnesi olan scrollbar listesye göre ayarlanır. (scrollbar kaydırılırsa listBoxdaki bilgiler tam olarak görülebilir.)  
*43. Satırda oluşturulan scrollbar yataya yerleştirilir.  

#### Fonksiyon içerisindeki kodlara geçelim.  
Öncelikle tekrar belirteyim bu kodların çalışması için ARA butonuna basılması gerekir.  
*8. Satırda listBox’ın içerisindeki veriler silinir.(bunun amacı ARA butonu birkaç kez çalıştırılırsa listBox’ın içinin boş olması için)  
*9. Satırda kullanıcıdan aradığı bölüm işleme alınır.  
*10. Satırda Chrome’a erişebilmek için gerekir.  
*11. Satırda erişmek istediğimiz site yani yukarda belirttiğim yökatlasın sitesinin linki bulunur.  
*12. Satırda linke ulaşılır.  
*13. Satırda sitede arama yaptığımız yere erişir. (chrome’da incele ile html kodlarından bulunur)  
*14 ve 16. Satırların görevini yukarıda belirtmiştim.  
*15. Satırda 9. Satırda kullanıcıdan alınan bilgi sitedeki arama motoruna yazılır.  
*17 ve 18. Satırda sitede arama motoruna bölüm yazıldıktan sonra Enter tuşu kullanılmadığı için;  
- 17. Satır: bölüm adı aram motoruna yazılınca alta beliren ilk’i seçilir.  
- 18. Satır: Enter tuşu görevi yapar.  
*19. Satırda  aradığımız bölüm projenin amacı olan veri çekme işini yapar.(value kısmının değeri sitedeki html kodları ile ayarlanır)  
*20. Satırda boş bir liste oluşturdum.  
*21-24 satırları arasındaki kod bloğuında alınan veriler oluşturulan boş listeye eklenir.  
*25. Satır listenin son elemanını siler. (çünkü siteden çektiğim bilgilerden gereksiz olanı silmek için kullandım.)  
*26. Satırda arattığımız bölümün adında bir dosya oluşturulur, encoding=‘utf-8’ ile dosya elemanlarının Türkçe karakterlere uyması içindir.  
*27-28  satırlarında liste içerisindeki elemanlar dosyaya yazılır.  
*29. Satırda verişler yazıldıktan sonra dosya kapatılır.  
*30-32 satırlarında listedeki veriler arayüzdeki listBox’a aktarılır.  
*14 ve 16. Satırların görevini yukarıda belirtmiştim.
*15. Satırda 9. Satırda kullanıcıdan alınan bilgi sitedeki arama motoruna yazılır.
*17 ve 18. Satırda sitede arama motoruna bölüm yazıldıktan sonra Enter tuşu kullanılmadığı için;
- 17. Satır: bölüm adı aram motoruna yazılınca alta beliren ilk’i seçilir.
- 18. Satır: Enter tuşu görevi yapar.
*19. Satırda  aradığımız bölüm projenin amacı olan veri çekme işini yapar.(value kısmının değeri sitedeki html kodları ile ayarlanır)
*20. Satırda boş bir liste oluşturdum.
*21-24 satırları arasındaki kod bloğuında alınan veriler oluşturulan boş listeye eklenir.
*25. Satır listenin son elemanını siler. (çünkü siteden çektiğim bilgilerden gereksiz olanı silmek için kullandım.)
*26. Satırda arattığımız bölümün adında bir dosya oluşturulur, encoding=‘utf-8’ ile dosya elemanlarının Türkçe karakterlere uyması içindir.
*27-28  satırlarında liste içerisindeki elemanlar dosyaya yazılır.
*29. Satırda verişler yazıldıktan sonra dosya kapatılır
*30-32 satırlarında listedeki veriler arayüzdeki listBox’a aktarılır.  

### Kodun çalışma resimleri

![image](https://user-images.githubusercontent.com/103186397/173692032-2adda52c-3dbf-4506-9c11-3677a89f9dac.png)
*Bu oluşturduğumuz arayüz. Göründüğü gibi 1 adet aradığımız bölümü soran label, 1 adet giriş bilgi yeri, 1 adet buton, 1 adet listBox, 1 adet scrollbar mevcut.    
![image](https://user-images.githubusercontent.com/103186397/173692096-20985956-dc8b-4e9f-812e-20f7b7932e61.png)  
*Bu şekilde aradığımız bölümü gireriz.  
*ARA butonuna basılırsa aşağıdaki şekilde olduğu gibi site açılır ve bölüm arama motoruna yazılır.  
![image](https://user-images.githubusercontent.com/103186397/173692161-a6db51f7-3b9b-453f-b1b3-6e52e4c59e6b.png)  
*Amacım ise aşağıda göstereceğim bilgileri çekmek.  
![image](https://user-images.githubusercontent.com/103186397/173692225-3d721928-390b-40a9-bb6a-97665100fa9d.png)  
*Bu bilgiler gösterildikten sonra site kapanır ve veriler çekilmiş olup, arayüzde gösterilir. Ve dosyaya eklenir.  
![image](https://user-images.githubusercontent.com/103186397/173692267-e7e0effa-7c57-43b1-a099-12a40c68f5cf.png)
  
  *Site kapandıktan sonra arayüzde listBox içinde veriler böyle gözükür ve aşağıdaki scrollbar’ın sağ ve sol butonuna basarak listBox’daki görünmeyen yazıları görebiliriz.  
  ![image](https://user-images.githubusercontent.com/103186397/173692324-5c31b47f-d4d8-4cc7-8427-d52d1168863a.png)  
  *Yukarıda görüldüğü gibi aradığın bölüm adında (burada tıp.txt) bir dosya oluşur. Dosya içi de aşağıda belirttiğim gibi.  
  ![image](https://user-images.githubusercontent.com/103186397/173692389-d28b22fa-449c-4aad-9f7c-95ff4a7823d4.png)  







 
