import requests
import time
import os

# Postavke
BASE_URL = 'https://placehold.co'
OUTPUT_DIR = './placeholders'
START_WIDTH = 400
HEIGHT = 400
INCREMENT = 50
NUM_IMAGES = 11  # 1 početna + 10 sljedećih

# Kreiraj mapu ako ne postoji
os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_placeholder(index):
    # Izračun nove širine: 400, 450, 500...
    current_width = START_WIDTH + (index * INCREMENT)
    
    # Konstrukcija URL-a za webp format (npr. https://placehold.co/450x400.webp)
    url = f'{BASE_URL}/{current_width}x{HEIGHT}.webp'
    filename = f'placeholder_{current_width}x{HEIGHT}.webp'
    filepath = os.path.join(OUTPUT_DIR, filename)

    try:
        print(f'Dohvaćam sliku: {url}')
        response = requests.get(url)
        response.raise_for_status()

        # Spremanje datoteke
        with open(filepath, 'wb') as photo:
            photo.write(response.content)
            print(f'Datoteka "{filename}" je uspješno kreirana!')

    except Exception as ex:
        print(f'Dogodila se greška za {filename}: {ex}')

# Glavna petlja
if __name__ == '__main__':
    print(f"Počinjem preuzimanje {NUM_IMAGES} slika u '{OUTPUT_DIR}'...")
    
    for i in range(NUM_IMAGES):
        get_placeholder(i)
        # Kratka pauza da budemo pristojni prema serveru (kao u vašem primjeru)
        time.sleep(1)
        
    print("Završeno!")