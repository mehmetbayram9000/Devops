# 1. Temel imajı seç (Mutfak tezgahını hazırla)
FROM python:3.9-slim

# 2. Çalışma dizinini belirle (Mutfakta hangi masada çalışacağız?)
WORKDIR /app

# 3. Uygulama kodunu bilgisayardan konteynırın içine kopyala
COPY app.py .

# 4. Konteynır başladığında çalışacak komutu söyle
CMD ["python", "app.py"]
