import requests


URL = 'https://dummyjson.com/recipes'
PHOTO_URL = 'https://robohash.org/python1?set=set5'

try:
    response = requests.get(PHOTO_URL)
    # response = requests.get(URL)
    response.raise_for_status()

    # content je binary -> odnosno file i koristi se za dohvat slika ili drugih datoteka
    print(response.content)
    with open('RoboHash.png', 'wb') as photo:
        photo.write(response.content)


except Exception as ex:
    print(f'Dogodila se greska: {ex}')
