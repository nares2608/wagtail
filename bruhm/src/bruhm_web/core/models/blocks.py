# home/blocks.py
from wagtail.blocks import StructBlock, ListBlock, CharBlock, URLBlock
from wagtail.images.blocks import ImageChooserBlock

class CarouselSlideBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    title = CharBlock(required=False, max_length=100)
    subtitle = CharBlock(required=False, max_length=250)
    link = URLBlock(required=False)

    class Meta:
        template = "blocks/carousel_slide.html"
        icon = "image"
        label = "Slide"

class CarouselBlock(StructBlock):
    slides = ListBlock(CarouselSlideBlock(), label="Slides")

    class Meta:
        template = "blocks/carousel.html"
        icon = "carousel"
        label = "Carousel"
