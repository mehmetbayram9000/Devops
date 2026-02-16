#!/bin/bash
# 1. Tam yola git
cd /home/ubuntu/devops || exit

# 2. Kodları güncelle
git pull origin main

# 3. Eski yapıyı temizle (Hata verse de durma)
sudo docker compose down || true

# 4. Yeni imajları çek ve 5 adet ayağa kaldır
sudo docker compose pull
sudo docker compose up -d --scale web_sunucum=5
