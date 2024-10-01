# Portfolio

Tervetuloa!

# Tuotelista ohjeet:

# Frontend

cmd:

npm run dev


# Backend

Avaa cmd Tuotelista kansiossa, voit tehdä tämän kirjoittamalla "cmd" resurssienhallinnan osoitepalkisssa Tuotelista kansiossa, se varmaan myös tarvitsee ylläpitäjän oikeuksia tehdä seuraavat komennot : 

py -m venv .venv

.venv\Scripts\activate

cd backend

pip install -r requirements.txt

python manage.py runserver

python manage.py makemigrations tuote

python manage.py migrate tuote
