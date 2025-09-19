from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from core.models.blocks import CarouselBlock

class HomePage(Page):
    body = StreamField([
        ('carousel', CarouselBlock()),
        # other blocks here
    ], null=True, blank=True)

    # Wrap the StreamField in FieldPanel
    content_panels = Page.content_panels + [
        FieldPanel('body'),  # <-- Correct!
    ]
