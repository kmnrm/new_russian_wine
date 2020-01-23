from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import utils

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

winery_age = 'Уже {} лет с нами'.format(utils.get_the_age(1920))
beverages_catalog = utils.create_beverages_catalog('products.txt')
categories = [*beverages_catalog]

rendered_page = template.render(
    winery_age=winery_age,
    beverages=beverages_catalog,
    categories=categories
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
