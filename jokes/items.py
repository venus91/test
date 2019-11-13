import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags

def remove_whitespace(value):
    return value.strip()

class JokeItem(scrapy.Item):
    joke_text= scrapy.Field(
        input_processor= MapCompose(remove_tags, remove_whitespace),
        output_processor= TakeFirst()
    )