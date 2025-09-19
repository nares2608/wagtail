from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.images.models import Image
@register_snippet
class Menus(ClusterableModel):
    name = models.CharField(max_length=255, default="Menu Name")
    menu_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",  
        help_text="Optional icon for the menu",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("menu_image"),
        InlinePanel("submenus", label="Sub Menus"),
    ]

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"


class SubMenu(models.Model):
    menu = ParentalKey(Menus, related_name="submenus", on_delete=models.CASCADE)
    heading = models.CharField(max_length=255, blank=True)
    link_name = models.CharField(max_length=255)
    link_page = models.ForeignKey(
        Page, null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    link_url = models.URLField("Custom URL", blank=True)

    panels = [
        FieldPanel("heading"),
        FieldPanel("link_name"),
        FieldPanel("link_page"),
        FieldPanel("link_url"),
    ]

    def __str__(self):
        return f"{self.link_name}"

    @property
    def url(self):
        if self.link_page:
            return self.link_page.url
        return self.link_url





@register_snippet
class FooterMenu(models.Model):
    heading = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    link_page = models.ForeignKey(
        Page, null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    link_url = models.URLField("Custom URL", blank=True)

    panels = [
        FieldPanel("heading"),
        FieldPanel("link_name"),
        FieldPanel("link_page"),
        FieldPanel("link_url"),
    ]

    def __str__(self):
        return f"{self.heading} → {self.menu_name}"
    
    class Meta:
        verbose_name = "Footer Menu"
        verbose_name_plural = "Footer Menus"

    @property
    def url(self):
        if self.link_page:
            return self.link_page.url
        return self.link_url




