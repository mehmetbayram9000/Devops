#!/bin/bash

# 1. Klasöre gir ve hata varsa dur
cd /home/ubuntu/devops || exit

# 2. GitHub'dan en son hali çek
git pull origin main

# 3. Eski yapılandırmayı temizle (Hata verse de devam et)
sudo docker compose down || true

# 4. En güncel imajları çek
sudo docker compose pull

# 5. Sistemi 5 konteynırla ayağa kaldır
sudo docker compose up -d --scale web_sunucum=5
