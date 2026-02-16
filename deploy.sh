#!/bin/bash

# 1. En güncel kodu çek
docker compose pull

# 2. Yeni konteynırı arkada ayağa kaldır (Eskisi hala çalışırken)
# --scale ile aynı servisten 2 tane açıyoruz
docker compose up -d --scale web_sunucum=2 --no-recreate

# 3. Kısa bir bekleme (Yeni konteynırın kendine gelmesi için)
sleep 5

# 4. Eski konteynırı (ID'si eski olanı) nazikçe kapat
docker rm -f $(docker ps -a | grep web_sunucum | head -n 1 | awk '{print $1}')

# 5. Sistemi tekrar tek konteynıra düşür (Artık sadece yeni olan kalsın)
docker compose up -d --scale web_sunucum=1
