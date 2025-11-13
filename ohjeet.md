# Ympäristön valmistelu VS Codessa

1. Avaa VS Codessa uusi tyhjä kansio.
2. Kloonaa tämä repo sinne: ``.
3. Luo virtuaaliympäristö: `python -m venv venv`
4. Aktivoi ympäristö: `.\venv\Scripts\Activate.ps1`

- Nyt voit asentaa mitkä tahansa tarvitsemasi paketit `pip install <package>` niin, että ne asentuvat vain tähän virtuaaliseen ympäristöön. Esimerkiksi `pip install python-dotenv`.
- Aina välillä on hyvä ajaa `pip freeze > requirements.txt`, jotta käsin asennetut paketit päivittyvät riippuvuuksien listalle. Myös sinne voi lisätä suoraan.
- Tässä repossa pitäisi kuitenkin olla suurin osa harjoituksiin tarvittavista paketeista jo listattuna, ks. seuraava vaihe.

5. Ota ympäristö käyttöön myös IDE:ssä: `Ctrl+Shift+P` > `Python: Select Interpreter` > valitse se, missä näkyy (venv).
6. Aja `pip install -r requirements.txt`. Riippuvuuksina olevat paketit pitäisi asentua.
7. Kopioi `.env.example` tiedostoon `.env`. Tähän tiedostoon voit kerätä ympäristömuuttujia Foundryn portaalista.

Huom! `.env` on `.gitignore`:ssa ja syystä: se sisältää salaisuuksia, joita ei missään nimessä pidä laittaa gittiin.

Kun lopetat harjoitukset, aja `deactivate`.