
from django.core.management.base import BaseCommand
import os
import json

from mainapp.models import ProductCategory

from mainapp.models import Product

from authapp.models import ShopUser

JSON_PATH = 'mainapp/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as f:
       return json.load(f)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('productcategory')

        ProductCategory.objects.all().delete()

        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()


        products = load_from_json('products')

        Product.objects.all().delete()

        for product in products:
            category_name = product['category']

            _category = ProductCategory.objects.get(name=category_name)

            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        ShopUser.objects.create_superuser('admin','admin@local','123', age=33)