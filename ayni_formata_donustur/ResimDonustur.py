import os
from PIL import Image

# Resimlerin bulunduğu dizin
input_folder = '' # Resimlerin bulunduğu dizin

# Dönüştürülen resimlerin kaydedileceği dizin
output_folder = os.path.join(input_folder, 'donusturulmus_resimler')
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Resimleri dönüştürme ve kaydetme
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.lower().endswith(('jpg', 'jpeg', 'png', 'jfif')):
            img_path = os.path.join(root, file)
            try:
                img = Image.open(img_path)
                
                # Dosya adını ve uzantısını kontrol ederek dönüştür
                base_name, ext = os.path.splitext(file)
                if ext.lower() != '.jpg':
                    new_file_path = os.path.join(output_folder, f"{base_name}.jpg")
                    img.convert('RGB').save(new_file_path, 'JPEG')
                    print(f'{file} -> {base_name}.jpg olarak kaydedildi.')
                else:
                    new_file_path = os.path.join(output_folder, file)
                    img.save(new_file_path)
                    print(f'{file} zaten jpg formatında, kopyalandı.')
            except Exception as e:
                print(f'{file} dönüştürülürken hata oluştu: {e}')

print('Tüm resimler başarıyla dönüştürüldü.')
