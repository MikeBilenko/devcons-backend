from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField


class TrustedPartner(models.Model):
    """Trusted partner snippet."""
    name = models.CharField(
        max_length=100,
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    panels = [
        FieldPanel("name"),
        FieldPanel("image"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Trusted Partner"
        verbose_name_plural = "Trusted Partners"


class TeamMember(models.Model):
    """Team Member snippet."""
    name = models.CharField(max_length=100)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    position = models.CharField(
        max_length=100,
        null=True,
        blank=False,
    )
    description = RichTextField(
        features=[],
        blank=False,
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("position"),
        FieldPanel("image"),
        FieldPanel("description"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"


register_snippet(TeamMember)
register_snippet(TrustedPartner)
