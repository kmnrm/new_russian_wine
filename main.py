from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import utils
import argparse

parser = argparse.ArgumentParser(
    description='This program adds product catalog to the web-site'
)
parser.add_argument('catalog', help='Product catalog, that is to be added.')
args = parser.parse_args()

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

winery_age = utils.get_the_age(1920)

products_text_catalog = args.catalog

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
