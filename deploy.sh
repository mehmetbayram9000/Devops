#!/bin/bash
# Tam yola git (Küçük harf 'devops' olduğuna emin ol)
cd /home/ubuntu/devops || exit

# GitHub'dan en son hali çek
git pull origin main

# Eski konteynırları temizle (Yoksa bile hata verme, devam et)
docker compose down || true

# Yeni imajı çek ve 5 tane ayağa kaldır
docker compose pull
docker compose up -d --scale web_sunucum=5
