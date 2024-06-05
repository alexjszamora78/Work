import json
import requests
from bs4 import BeautifulSoup

resp = requests.get('https://www.bazar-virtual.ca/')
soup = BeautifulSoup(resp.text, 'html.parser')
v = soup.find("td",{"id":"footer_td_2"})
productos = v.find_all('span')
titulos = [producto.text for producto in productos]
p = soup.find_all('div', {'class': 'footer_price'})
precios = [precio.text for precio in p]
datos = dict(zip(titulos, precios))
with open('productos.json', 'w') as f:
    json.dump(datos, f)


#contenido de productos.json
#{"Jab\u00f3n de Tocador Antibacterial Fresh, 110g.": "Precio: 1.00 USD", "Adocreto Monocapa Gris (200x100x80 mm)": "Precio: 0.13 USD", "Frazada de Piso (Entrega a domicilio)": "Precio: 1.50 USD", "Dent Elixir y Dentrifico Menta, 120ml": "Precio: 1.36 USD", "FOUR SEASONS - Energy. Desodorante roll on,  90 ml ": "Precio: 0.99 USD"}