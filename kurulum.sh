#!/bin/bash

# Bu bir yorum satırıdır, sistem bunu okumaz ama çırak okur!
echo "Sistem güncelleniyor..."
sudo apt update -y

echo "Nginx kuruluyor..."
sudo apt install nginx -y

echo "Sunucu durumu kontrol ediliyor..."
systemctl status nginx | grep "Active"

echo "İşlem tamamlandı usta!"
