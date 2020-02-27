from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import utils

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

winery_age = utils.get_the_age(1920)
products_text_catalog = 'products.txt' #ЗАМЕЧАНИЕ №10 ПРО КОНФИГ -- ЧТО-ТО НЕ ДОХОДИТ ДО МЕНЯ, ПОДТОЛКНИТЕ ЕЩЕ ;-)

with open(products_text_catalog, "r", encoding="utf8") as products_catalog:
    products = products_catalog.read()
    beverages_catalog = utils.create_beverages_catalog(products)

rendered_page = template.render(
    winery_age=winery_age,
    beverages_catalog=beverages_catalog
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
