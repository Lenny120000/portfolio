# Portfolio

Tervetuloa!

# Tuotelista:

Vite + Django

HUOM! Nämä ohjeet ovat Windows-käyttöjärjestelmälle.

Tarvitset ennen ohjeita nämä paketit: python ja node.js

Nämä linkit toimivat kun saat backendin ja frontendin käyntiin

Nettisivu: http://localhost:5173/

Django: http://127.0.0.1:8000/



# Backend

Avaa cmd tuotelista kansiossa, voit tehdä tämän kirjoittamalla "cmd" resurssienhallinnan osoitepalkisssa tuotelista kansiossa, se varmaan myös tarvitsee ylläpitäjän oikeuksia tehdä seuraavat komennot : 

py -m venv .venv

.venv\Scripts\activate

cd tuotelista-backend

pip install -r requirements.txt

python manage.py runserver


# Frontend

Avaa tuotelista-frontend kansio ja kirjoita cmd osoitepalkkiin:

npm install

npm run dev
