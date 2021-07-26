import json

links_menu = [
        {'href': 'index', 'name': 'все'},
        {'href': 'products_home', 'name': 'дом'},
        {'href': 'products_office', 'name': 'офис'},
        {'href': 'products_modern', 'name': 'модерн'},
        {'href': 'products_classic', 'name': 'классика'},
    ]

with open('mainapp/templates/mainapp/links_menu.json', 'w') as f:
    f.write(json.dumps(links_menu))

with open('mainapp/templates/mainapp/links_menu.json') as f:
    print(f.read())