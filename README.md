# Target

### Data
ChatGPT kullanarak bir temsilci ve müşteri arasında İngilizce bir transkript oluşturun (tercihen JSON formatında olsun). Görüşme yaklaşık 20 adım olsun ve müşterinin iphone14 almak istemesi üzerine olsun.

### Görev
İngilizce Large Language Model kullanarak Sentiment (Duygu: positive, negative, neutral) ve Intention (Niyet: siz belirleyin örneğin ‘change_package’, ‘upgrade’ etc) tahminini Zero-Shot yapan bir kod yazın. 

### Proje Yapısı
Kod tabanında src (sisteminizin adı), config(model konfigürasyonları tercihen .ini ama .yaml de olabilir), data (ChatGPT ile oluşturduğunuz simülasyon datası), resources (zero-shot model, Hugging face zero-shot modeli facebook/bart kullanabilirsiniz) dizinleri bulunsun. Bu kodu setup.py ile pyhon paketi haline getirin (Wheel ve/veya tar dosyası oluştursun, PyCharm bu işi çok kolaylaştırıyor).

Hedefimiz software development yeteneklerinizi ölçmek.

### Tartışma Soruları

Burada implementasyon beklenmiyor.

- Zero-Shot kullanmanın avantajları ve dezavantajları nelerdir? Bu sistemi nasıl Türkçe hale getirebiliriz? Önerileriniz nelerdir?

* Zero-Shot learning avantajları: 

- Özel eğitim verilerine ihtiyaç duymaz.
- Özel etiketleme gerektirmez.
- Çoklu sınıflandırma yapabilir.
- Hızlı uygulanabilir.
- Uygulanma alanı geniştir.

* Zero-Shot learning dezavantajları:

- Hassas sonuçlar üretemeyebilir.
- Özelleştirmek zordur.
- Çeviri hataları olabilir.

* Türkçe hale getirmek için:

- Türkçe veri seti oluşturulabilir.(Veri toplama ve etiketleme, vs.)
- Özelleştirilmiş bir preprocess aşamasına ihtiyaç duyar.
- Özelleştirilmiş bir eğitim gerekir.
- Open source Türkçe veri setleri için üretilmiş modeller kullanılabilir.

- Speech-To-Text dönüşüm yapan bir API ve transkriptleri yayınlayan bir gRPC sistemi olduğunu varsayalım. Bu sistemi dinleyen ve transkript üzerine duygu ve niyet analizi yapmak için sizin paketinizi kullanan ve sonucu yayınlayan bir diğer gRPC sistemi düşünün. Böyle bir sistemin ne gibi sorunları olabilir? Nelere dikkat etmek gerekir?

* Dikkat Edilmesi Gereken Hususlar:
- Yeterli sayıda veri bulunmalıdır.
- Veri seti dengeli olmalıdır. (Aksan, hızlı konuşma, vs.)
- Performans sürekli ölçülebilmelidir.

* Sorunlar:
- Verilerin korunması ve gizliliği.
- API'ye erişim izin ve yetki kontrolleri gerektirdiğinden hızlı bir şekilde erişim sağlanamayabilir ve maliyetli olabilir.
- Büyüyen veri seti ile birlikte modelin performansı düşebilir ve trafik sorunları ortaya çıkabilir.
- Sürekli dokümantasyon ve destek maliyeti yaratabilir. (Personel, zaman, vs.)
- Sentiment ve Intention tespitleri kişiden kişiye değişen kavramlar olduğundan nesnel olmayabilir.

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

### Time spent for the project
 
Start time: 29.08.2023 19.00

End time: 04.09.2023 21.00

# API Quickstart

### Run the app in containers

* Clone the repo and navigate to the root folder.

* To run the app using Docker, make sure you've got [Docker][docker] installed on your
system. From the project's root directory, run:

    ```bash
    docker compose up -d
    ```

### Or, run the app locally

If you want to run the app locally, without using Docker, then:

* Clone the repo and navigate to the root folder.

* Create a virtual environment. Here I'm using Python's built-in venv in a Unix system.
Run:

    ```bash
    python3.11 -m venv .venv
    ```

* Activate the environment. Run:

    ```bash
    source .venv/bin/activate
    ```

* Install the dependencies. Run:

    ```bash
    pip install -r requirements.txt -r requirements-dev.txt
    ```

* Start the app. Run:

    ```bash
    uvicorn app.main:app --port 5000 --reload
    ```

### Check the APIs

* To play around with the APIs, go to the following link on your browser:

    ```
    http://localhost:5000/docs
    ```

* Press the `authorize` button on the right and add *username* and *password*. The APIs
use OAuth2 (with hashed password and Bearer with JWT) based authentication. In this
case, the username and password is `teb` and `nlp2023` respectively.

* Then select any of the `api_v1` API and click Try It Out and execute the API.

* Also, notice the `curl` section in the above screen shot. You can directly use the
highlighted curl command in your terminal. Make sure you've got `jq` installed in your system.

    ```bash
    curl -X GET "http://localhost:5000/api_v1/sentiment_intention_prediction" \
         -H "accept: application/json" \
         -H "Authorization: Bearer $(curl -X POST "http://localhost:5000/token" \
                            -H "accept: application/x-www-form-urlencoded" \
                            -d "username=teb&password=nlp2023" | jq -r ".access_token")"
    ```

    This should show a response like this:

    ```json
    {
        "sentiments": [
            {
            "message": "Hi! I'm interested in buying the new iPhone 14. Can you tell me more about it?",
            "sentiment": "positive",
            "score": 0.6474151015281677
            },
            {
            "message": "That sounds great! Can you tell me about the available storage options and colors?",
            "sentiment": "positive",
            "score": 0.9964686632156372
            },
            {
            "message": "I'd like the 256GB version in Midnight Green, please.",
            "sentiment": "positive",
            "score": 0.8825816512107849
            },
            {
            "message": "Yes, I'm interested in a protective case and AppleCare+. Can you provide me with the pricing details?",
            "sentiment": "positive",
            "score": 0.918483555316925
            },
            {
            "message": "Yes, please add both the protective case and AppleCare+ to my order.",
            "sentiment": "positive",
            "score": 0.9587196111679077
            },
            {
            "message": "Sure, my shipping address is 123 Main Street, Anytown, USA. I'll pay with my Visa card. The number is 1234 5678 9012 3456.",
            "sentiment": "positive",
            "score": 0.7980246543884277
            },
            {
            "message": "Excellent! Thanks for your assistance. I'm looking forward to my new",
            "sentiment": "positive",
            "score": 0.9918376207351685
            },
            {
            "message": "You too! Goodbye!",
            "sentiment": "negative",
            "score": 0.9381532669067383
            },
            {
            "message": "I just received my iPhone 14, and it's amazing! Thank you for the quick delivery.",
            "sentiment": "positive",
            "score": 0.9659854769706726
            },
            {
            "message": "I'm really impressed with your service. The phone is perfect, and the accessories are top-notch. Thank you!",
            "sentiment": "positive",
            "score": 0.9774714112281799
            },
            {
            "message": "I certainly will! Thanks again for everything. Have a fantastic day!",
            "sentiment": "positive",
            "score": 0.8244415521621704
            },
            {
            "message": "Goodbye.",
            "sentiment": "negative",
            "score": 0.8930509090423584
            }
        ],
        "intentions": [
            {
            "message": "Hi! I'm interested in buying the new iPhone 14. Can you tell me more about it?",
            "intention": "greeting",
            "score": 0.25905296206474304
            },
            {
            "message": "That sounds great! Can you tell me about the available storage options and colors?",
            "intention": "information",
            "score": 0.3638773262500763
            },
            {
            "message": "I'd like the 256GB version in Midnight Green, please.",
            "intention": "inquiry",
            "score": 0.236429363489151
            },
            {
            "message": "Yes, I'm interested in a protective case and AppleCare+. Can you provide me with the pricing details?",
            "intention": "information",
            "score": 0.28849807381629944
            },
            {
            "message": "Yes, please add both the protective case and AppleCare+ to my order.",
            "intention": "confirmation",
            "score": 0.20851221680641174
            },
            {
            "message": "Sure, my shipping address is 123 Main Street, Anytown, USA. I'll pay with my Visa card. The number is 1234 5678 9012 3456.",
            "intention": "confirmation",
            "score": 0.3083619773387909
            },
            {
            "message": "Excellent! Thanks for your assistance. I'm looking forward to my new",
            "intention": "praise",
            "score": 0.4329412579536438
            },
            {
            "message": "You too! Goodbye!",
            "intention": "closing",
            "score": 0.5078788995742798
            },
            {
            "message": "I just received my iPhone 14, and it's amazing! Thank you for the quick delivery.",
            "intention": "acknowledgment",
            "score": 0.27712002396583557
            },
            {
            "message": "I'm really impressed with your service. The phone is perfect, and the accessories are top-notch. Thank you!",
            "intention": "praise",
            "score": 0.3697708249092102
            },
            {
            "message": "I certainly will! Thanks again for everything. Have a fantastic day!",
            "intention": "gratitude",
            "score": 0.3380465507507324
            },
            {
            "message": "Goodbye.",
            "intention": "closing",
            "score": 0.7575727105140686
            }
        ],
        "errors": []
    }
    ```

* To test the `GET` APIs with Python, you can use a http client library like
[httpx][httpx]:

    ```python
    import httpx

    with httpx.Client() as client:

        # Collect the API token.
        r = client.post(
            "http://localhost:5000/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data={"username": "teb", "password": "nlp2023"},
        )
        token = r.json()["access_token"]

        # Use the token value to hit the API.
        r = client.get(
            "http://localhost:5000/api_v1/sentiment_intention_prediction",
            headers={"Accept": "application/json", "Authorization": f"Bearer {token}"},
        )
        print(r.json())
    ```

### Folder structure

This shows the folder structure of the default template.

```
fastapi-nano
├── app                           # primary app folder
│   ├── apis                      # this houses all the API packages
│   │   ├── api_v1                # api_v1 package
│   │   │   ├── __init__.py       # empty init file to make the api_v1 folder a package
│   │   │   ├── prediction.py     # main module of api_v1 package
│   │   │   └── utils.py          # utils module of api_v1 package
│   │   └── api_v2                # api_v2 package
│   │       ├── __init__.py       # empty init file to make the api_v2 folder a package
│   ├── core                      # this is where the configs live
│   │   ├── auth.py               # authentication with OAuth2
│   │   ├── config.py             # sample config file
│   │   └── __init__.py           # empty init file to make the config folder a package
│   ├── data                      # data folder 
│   │   ├── conversation.json     # data generated from ChatGBT
│   ├── models                    # Zero-Shot facebook/bart-large-mnli model files lives here
│   │   ├── ...                   # model files
│   ├── static                    # static folder
│   ├── __init__.py               # empty init file to make the app folder a package
│   ├── main.py                   # main file where the fastAPI() class is called
│   ├── routes                    # this is where all the routes live
│   │   └── views.py              # file containing the endpoints of api_v1
│   └── tests                     # test package
│       ├── __init__.py           # empty init file to make the tests folder a package
│       ├── test_api.py           # integration testing the API responses
│       └── test_functions.py     # unit testing the underlying functions
├── dockerfiles                   # directory containing all the dockerfiles
├── .env                          # env file containing app variables
├── Caddyfile                     # simple reverse-proxy with caddy
├── docker-compose.yml            # docker-compose file
├── pyproject.toml                # pep-518 compliant config file
├── requrements-dev.in            # .in file to enlist the top-level dev requirements
├── requirements-dev.txt          # pinned dev dependencies
├── requirements.in               # .in file to enlist the top-level app dependencies
└── requirements.txt              # pinned app dependencies
```

### Further modifications

* You can change the application port in the `.env` file.