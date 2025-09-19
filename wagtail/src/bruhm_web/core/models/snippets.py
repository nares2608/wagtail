from django.db import models
from wagtail.models import Page
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField


@register_snippet
class Menus(ClusterableModel):
    name = models.CharField(max_length=100, default="Menu Name")
    link_page = models.ForeignKey(
        Page, null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    link_url = models.URLField("Custom URL", blank=True)
    panels = [
        FieldPanel("name"),
        FieldPanel("link_page"),
        FieldPanel("link_url"),
        InlinePanel("submenus", label="Sub Menus"),
    ]

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"


class SubMenu(models.Model):
    menu = ParentalKey(Menus, related_name="submenus", on_delete=models.CASCADE)
    link_name = models.CharField(max_length=100)
    link_page = models.ForeignKey(
        Page, null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    link_url = models.URLField("Custom URL", blank=True)

    panels = [
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
    heading = models.CharField(max_length=100)
    link_name = models.CharField(max_length=100)
    link_page = models.ForeignKey(
        Page, null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    )
    link_url = models.URLField("Custom URL", blank=True)

    panels = [
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
    


@register_snippet
class Testimonial(models.Model):
    text = RichTextField()
    client_name = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)

    panel = [
        FieldPanel("text"),
        FieldPanel("client_name"),
        FieldPanel("department"),
        FieldPanel("designation"),
    ]


    def __str__(self):
        return f"{self.client_name} → {self.designation}"
    
    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
