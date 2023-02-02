# Boun-Teacher-Ranking-with-AHP
Öğrencilerin ders programı oluşturma esnasında yararlanması için dersi veren öğretmenlerin puanlanma sürecini içeren bir projedir

Bu proje web-scraping veri görselleştirme, cosine similarity metodu ile yorumları puanlandırma ve excel dosyası üzerinden Analytic Hierarchy Process yöntemi ile puanlandırma içermektedir.

Web-Scraping

https://www.bouncim.com/ ve https://kilicbaran.github.io/boun-course-planner/ sitelerinden web-scraping yolu ile Boğaziçi Üniversitesi dersleri hakkındaki öğrenci yorumları ve mevcut dönemde verilen dersler elde edilmiştir

Data Visualisition

Elde edilen veriler hakkında çeşitli görselleştirmeler yapılmıştır.

Cosine Similarity

https://www.bouncim.com/ sitesinde ki öğrenci yorumlarından yola çıkarak dersi veren öğretmenlerin puanlandırmada 3 ana kriter olan öğrenci dostu olması, alanında yetkin olması ve ingilizce yeterliliklerine göre Cosine similarity yöntemiyle belirli örnek cümleler benzerlikleri değerlendirilerek puanlandırılması

Data preprocessing

Web-scraping ile elde edilen 2 ayrı verisetinin çeşitli ön hazırlıklar sonucunda birleştirilmesi ve bu sayede sadece mevcut olan dersler hakkında puanların görüleceği bir final veriseti haline getirilmesi ve excel dosyası olarak elde edilmesi

AHP Ranking
Excel dosyası üzerinde AHP yöntemi uygulanarak derslerin ve dersi veren öğretmenler puanlanmıştır.


