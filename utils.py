import datetime

def translate_category(category):
    if category == 'Название':
        return 'name'
    if category == 'Сорт':
        return 'sort'
    if category == 'Цена':
        return 'price'
    return 'image'


def make_beverage_card(beverage_description):
    beverage_card = {}
    promo = 'Выгодное предложение'
    if promo in beverage_description:
        beverage_description = beverage_description.replace(promo, '').strip()
        beverage_card['on_promo'] = 'Yes'
    else:
        beverage_card['on_promo'] = 'No'
    beverage_props = beverage_description.split('\n')
    for prop in beverage_props:
        (category, category_value) = prop.split(': ')
        category = translate_category(category)
        beverage_card[category] = category_value
    return beverage_card


def allot_beverages_from_file(products_text_catalog):
    groups_names = []
    beverages_groups = []
    with open(products_text_catalog, "r", encoding="utf8") as products:
        for products_block in products.read().split('\n\n\n'):
            if not '#' in products_block:
                beverages_group = products_block
                beverages_groups.append(beverages_group)
            else:
                group_name = products_block.replace('# ', '')
                group_name = group_name.replace('\ufeff', '')
                groups_names.append(group_name)
    beverages_allotted = dict(zip(groups_names, beverages_groups))
    return beverages_allotted


def create_beverages_catalog(products_text_catalog):
    beverages = allot_beverages_from_file(products_text_catalog)
    beverages_catalog = {}
    for category in beverages.keys():
        beverages_cards = []
        for beverage_description in beverages[category].split('\n\n'):
            beverage_card = make_beverage_card(beverage_description)
            beverages_cards.append(beverage_card)
        beverages_catalog[category] = beverages_cards
    return beverages_catalog


def get_the_age(year):
    the_age = datetime.date.today() - datetime.date(year=year, month=1, day=1)
    the_age = int(the_age.days/365)
    return the_age