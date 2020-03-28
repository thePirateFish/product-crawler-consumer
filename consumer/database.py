from google.cloud import firestore
from consumer.models import Product, Review

def save_product(product:Product):
    db = firestore.Client()
    # use sku as document ID for Product
    db.collection(u'products').document(product.sku).set(product.to_dict())

def save_review(review:Review):
    db = firestore.Client()
    # use sha1 has of sku+author+title+date as document ID for review
    db.collection(u'products').document(review.sku).collection(u'reviews').document(review.get_unique_id()).set(review.to_dict())