from django.db import models
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from wagtail.admin.panels import FieldPanel
from wagtail.images.models import Image

@register_setting

class SiteSettings(BaseSiteSetting):
    logo = models.ForeignKey(
            "wagtailimages.Image",
            null = True,
            blank = True,
            on_delete = models. SET_NULL,
            related_name = "+",
            help_text = "Upload Logo"
                                
            )
    
    favicon = models.ForeignKey(
            "wagtailimages.Image",
            null = True,
            blank = True,
            on_delete = models. SET_NULL,
            related_name = "+",
            help_text = "Upload FavIcon"
                                
            )
    
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    panels = [
        FieldPanel("logo"),
        FieldPanel("favicon"),
        FieldPanel("contact_email"),
        FieldPanel("contact_phone"),
        FieldPanel("address"),
    ]

    class Meta:
        verbose_name = "Site Settings"