from typing import List, Dict

class Product(object):
    def __init__(self, sku: str, title=None, desc=None, image_urls=None, url=None, tags=None, category=None, specs=None,  price=None, avail=None, options=None, artist_info=None, care_info=None):
        self.sku = sku
        self.title = title
        self.description = desc
        self.image_urls = image_urls
        self.url = url
        self.tags = tags
        self.category = category
        self.specs = specs
        self.artist_info = artist_info
        self.care_info = care_info
        self.price = price
        self.availability = avail
        self.options = options

    def to_dict(self):
        return {'sku': self.sku,
                'title': self.title,
                'description': self.description,
                'image_urls': self.image_urls,
                'url': self.url,
                'tags': self.tags,
                'category': self.category,
                'specs': self.specs,
                'artist_info': self.artist_info,
                'care_info': self.care_info,
                'price': self.price,
                'availability': self.availability,
                'options': self.options }

class Review(object):
    def __init__(self, sku: str, author=None, rating=None, title=None, body=None, date=None, location=None):
        self.sku = sku
        self.author = author
        self.rating = rating
        self.title = title
        self.body = body
        self.date = date
        self.location = location

    def to_dict(self):
        return {'sku': self.sku,
                'author': self.author,
                'rating': self.rating,
                'title': self.title,
                'body': self.body,
                'date': self.date,
                'location': self.location }

    def get_unique_id(self):
        import hashlib
        m = hashlib.sha1()
        m.update(str(self.sku + self.author + self.title + self.date).encode('utf-8'))
        return m.hexdigest()
