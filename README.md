# Target

## Data
ChatGPT kullanarak bir temsilci ve müşteri arasında İngilizce bir transkript oluşturun (tercihen JSON formatında olsun). Görüşme yaklaşık 20 adım olsun ve müşterinin iphone14 almak istemesi üzerine olsun.

## Görev
İngilizce Large Language Model kullanarak Sentiment (Duygu: positive, negative, neutral) ve Intention (Niyet: siz belirleyin örneğin ‘change_package’, ‘upgrade’ etc) tahminini Zero-Shot yapan bir kod yazın. 

## Proje Yapısı
Kod tabanında src (sisteminizin adı), config(model konfigürasyonları tercihen .ini ama .yaml de olabilir), data (ChatGPT ile oluşturduğunuz simülasyon datası), resources (zero-shot model, Hugging face zero-shot modeli facebook/bart kullanabilirsiniz) dizinleri bulunsun. Bu kodu setup.py ile pyhon paketi haline getirin (Wheel ve/veya tar dosyası oluştursun, PyCharm bu işi çok kolaylaştırıyor).

Hedefimiz software development yeteneklerinizi ölçmek.

## Tartışma Soruları

Burada implementasyon beklenmiyor.

- Zero-Shot kullanmanın avantajları ve dezavantajları nelerdir? Bu sistemi nasıl Türkçe hale getirebiliriz? Önerileriniz nelerdir?

- Speech-To-Text dönüşüm yapan bir API ve transkriptleri yayınlayan bir gRPC sistemi olduğunu varsayalım. Bu sistemi dinleyen ve transkript üzerine duygu ve niyet analizi yapmak için sizin paketinizi kullanan ve sonucu yayınlayan bir diğer gRPC sistemi düşünün. Böyle bir sistemin ne gibi sorunları olabilir? Nelere dikkat etmek gerekir?

# Sources

Hello, I will also share my educational roadmap here to share with you how I approach a topic that I will be familiarising myself with for the first time. 

I usually first browse free resources in my native language to understand the terms and topic. 

https://www.btkakademi.gov.tr/portal/course/dogal-dil-islemeye-giris-11864

Then I search Kaggle and Github for references and guides.

https://www.kaggle.com/code/emirkocak/in-depth-series-sentiment-analysis-w-transformers

https://www.kaggle.com/code/shyambhu/introduction-to-sentiment-analysis

https://www.kaggle.com/code/manchunhui/us-presidential-election-sentiment-analysis

https://www.kaggle.com/code/redwankarimsony/nlp-101-tweet-sentiment-analysis-preprocessing

https://github.com/rajatdiptabiswas/flask-api-hugging-face-fb-bart-large-mnli

I use FastAPI a lot in my own projects and in my professional life. There is a FastAPI architecture that I use for this.

https://github.com/rednafi/fastapi-nano

The prompt I gave to Chatgbt to generate data.

https://chat.openai.com/share/7e220744-2030-4045-bb29-722ec8994ff2

# Attachments

## Time spent for the project
 
Start time: 29.08.2023 19.00

End time: -

## Favourite sources

- 

