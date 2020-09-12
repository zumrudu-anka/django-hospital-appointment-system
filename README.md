# Hospital_Appointment_System

Öncelikle projeyi yerel çalışma alanınıza kopyalayın:

`git clone https://github.com/zumrudu-anka/django-hospital-appointment-system.git`

Bu repoyu kopyaladığınıza göre yerel çalışma alanınızda Python ve Django yüklü olduğunu varsayıyorum.

Komut penceresini açın ve projenin bulunduğu çalışma dizinine komut penceresinden ulaşın.

Django framework sanal ortamınızda kurulu ise öncelikle sanal ortamınızı aktifleştirmeyi unutmayın.

Projenin bulunduğu çalışma dizininde iken(manage.py dosyasının bulunduğu) konsola öncelikle

`python manage.py migrate` komutunu yazın. Böylece kullanıcı tablolarını oluşturmuş olacaksınız.

Daha sonra `python manage.py makemigrations` komutunu ve ardından tekrar `python manage.py migrate`

komutunu yazın. Böylece projemizde oluşturduğumuz modelleri de veritabanı tablosuna eklemiş olacaksınız.

Herşeyi yönetebilmek için `python manage.py createsuperuser` komutu ile süper kullanıcı oluşturma zamanı.

Komutu yazdıktan sonra kullanıcı adı, e-mail ve şifre bilgilerini sırayla girmeniz gerekiyor.

E-mail alanını boş bırakabilirsiniz, bu bilgileriniz kendi yerel veritabanınızda kullanıcı tablolarında tutulur ve

bu bilgiler ışığında sisteme giriş yapabilir, sistemi yönetebilirsiniz.

Veritabanına Türkiye'deki bütün şehirleri eklemek için konsol ekranına:

`python manage.py addcities` komutunu yazıp onayladıktan sonra bekleyin.

İşlem tamamlanınca kendi oluşturduğumuz komut aracılığı ile Türkiye'deki şehirlerin bilgisinin bulunduğu json dosyasından sisteme şehirleri eklemiş oluyoruz.

Tüm şehirlerin tüm ilçelerini de eklemek için komut satırına:

`python manage.py addcounties` komutunu yazıp onaylayın ve yine işlemin bitmesini bekleyin.

Bu işlem de tamamlandıktan sonra artık serverı başlatıp, kullanıcı oluşturabilir, giriş yapabilir,

şifre değiştirebilir, randevu alabilir, geçmiş randevularınızı listeleyebilirsiniz. Ama bunlardan önce sisteme

Django admin panelinden giriş yapıp randevu almanız için gerekli olan hastane, poliklinik ve doktorları veritabanına

eklemelisiniz. Hastalar zaten sistemi kullanmak için üyelik alan kullanıcılar olduğundan her yeni üyelik ile veritabanında

yeni bir hasta da oluşmaktadır.

`python manage.py runserver` komutu ile serverı başlattıktan sonra web tarayıcınızın adres çubuğuna 127.0.0.1:8000/admin

(port numarasını server başlatırken özel olarak belirlemezseniz default olarak bu şekilde setlenecektir) adresini girin ve

karşınıza çıkan sayfada az önce oluşturduğunuz süper kullanıcı bilgileriniz ile kullanıcı girişi yapın.

Birkaç hastane, poliklinik ve doktor ekledikten sonra sistemden çıkış yapın.

Adres çubuğuna 127.0.0.1:8000 yazın ve hastane randevu sistemini kullanıcı gözünden kullanmaya başlayın.

Not: Bazı linkler ölüdür, bazı içerikler tamamlanmamış haldedir.
