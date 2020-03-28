from consumer.models import Product, Review
from consumer.util import remove_metadata, get_data, get_type
from consumer.database import save_product, save_review

def process_event(event):
    if 'data' in event:
        data = get_data(event)
        print(data)
        _type = get_type(data)
        print('Type: {}'.format(_type))
        obj = remove_metadata(data)
        if _type == 'Product':
            product = Product(**obj)
            print(product)
            process_product(product)
        elif _type == 'Review':
            review = Review(**obj)
            print(review)
            process_review(review)

def process_review(review:Review):
    save_review(review)

def process_product(product:Product):
    save_product(product)
