import json
import requests
from datetime import datetime

response = requests.get("http://data.foli.fi/siri/sm/pretty")
pysakit = json.loads(response.text)
while 1:
    numero = input("Anna pysäkin numero: ")
    if numero == 'x':
        break
    try:
        pysakki = pysakit[numero]
    except:
        print("Pysäkkiä ei ole")
        continue
    print(pysakki['stop_name'])
    response2 = requests.get(f"http://data.foli.fi/siri/sm/{numero}/pretty")
    stops = json.loads(response2.text)
    bussit = stops['result']

    i = 0
    for bussi in bussit:
        aimed = bussi['aimedarrivaltime']
        expected = bussi['expectedarrivaltime']
        saapumisaika = datetime.fromtimestamp(expected)
        virhe = expected - aimed
        ero = ""
        if virhe:
            ero = f"({virhe//60:+d})"
        print(saapumisaika.strftime("%H:%M"), ero.rjust(5), bussi['lineref'].rjust(3), "-", bussi['destinationdisplay'])
        i = i + 1
        if i >= 10:
            break
