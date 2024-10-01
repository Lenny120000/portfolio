# Portfolio

Tervetuloa!

# Tuotelista:

Vite + Django

Tarvitset ennen ohjeita nämä paketit: python ja node.js

HUOM! Nämä ohjeet ovat Windows-käyttöjärjestelmälle.

# Backend

Avaa cmd Tuotelista kansiossa, voit tehdä tämän kirjoittamalla "cmd" resurssienhallinnan osoitepalkisssa Tuotelista kansiossa, se varmaan myös tarvitsee ylläpitäjän oikeuksia tehdä seuraavat komennot : 

py -m venv .venv

.venv\Scripts\activate

cd Backend

pip install -r requirements.txt

python manage.py runserver

python manage.py makemigrations tuote

python manage.py migrate tuote


# Frontend

Avaa Frontend kansio ja kirjoita cmd osoitepalkkiin:

npm install

npm run dev


