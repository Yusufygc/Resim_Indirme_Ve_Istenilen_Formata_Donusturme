import os
import requests
from urllib.parse import urlparse

# txt dosyasının yolunu belirleyin
txt_file_path = '' # txt dosyasının yolunu buraya yazın

# Resimleri kaydedeceğiniz ana klasörün yolunu belirleyin
main_folder = 'indirilen_resimler'

# Ana klasörü oluşturun (eğer yoksa)
if not os.path.exists(main_folder):
    os.makedirs(main_folder)

# txt dosyasını açın ve her satırı okuyun
with open(txt_file_path, 'r') as file:
    urls = file.readlines()

for url in urls:
    url = url.strip()
    if url:
        try:
            # Resim dosyasını indirin
            response = requests.get(url)
            response.raise_for_status()
            
            # Resmin uzantısını belirleyin
            parsed_url = urlparse(url)
            file_name = os.path.basename(parsed_url.path)
            file_extension = file_name.split('.')[-1]
            
            # Uzantıya göre klasör oluşturun (eğer yoksa)
            folder_path = os.path.join(main_folder, file_extension)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            # Resmi klasöre kaydedin
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'wb') as img_file:
                img_file.write(response.content)
            
            print(f'{file_name} başarıyla indirildi ve {folder_path} klasörüne kaydedildi.')
        
        except requests.exceptions.RequestException as e:
            print(f'{url} adresinden resim indirilemedi. Hata: {e}')
