from django.db import models
from modelcluster.fields import (
    ParentalKey,
    ParentalManyToManyField
)
from wagtail.models import Page, Orderable
from wagtail.fields import StreamField
from django import forms
from wagtail.fields import RichTextField
from wagtail.admin.panels import (
    FieldPanel,
    PageChooserPanel,
    InlinePanel,
    MultiFieldPanel,
)
from streams import blocks
from snippets.models import (
    TeamMember,
    TrustedPartner,
)
from wagtail.api import APIField

from rest_framework.permissions import AllowAny
from snippets.serializers import (
    TeamMemberSerializer,
    TrustedPartnersSerializer,
)
from wagtail.images.api.fields import ImageRenditionField


class Stat(Orderable):
    """Stat orderable."""
    page = ParentalKey(
        "home.HomePage",
        related_name="stat_items",
    )
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    subtitle = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    description = RichTextField(features=[
        "link",
    ], blank=False)

    panels = [
        FieldPanel("title"),
        FieldPanel("subtitle"),
        FieldPanel("description"),
    ]

    api_fields = [
        APIField("title"),
        APIField("subtitle"),
        APIField("description"),
    ]


class HomePage(Page):
    """Home Page representation."""
    permissions_classes = [AllowAny, ]
    max_count = 1
    subtitle = models.CharField(
        max_length=150,
        verbose_name="Intro title",
        null=True,
        blank=False,
    )
    services = StreamField(
        [
            ("services", blocks.ServicesListBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("subtitle"),

            InlinePanel(
                "stat_items",
                max_num=3,
                min_num=0,
                label="Stat",
            ),
        ], heading="Intro data"),
        FieldPanel("services"),
    ]

    api_fields = [
        APIField("subtitle"),
        APIField("services"),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


class AboutImages(Orderable):
    """About page Images."""
    page = ParentalKey(
        "home.AboutPage",
        related_name="about_images"
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )

    panels = [
        FieldPanel("image"),
    ]

    api_fields = [
        APIField("image"),
        APIField(
            "image_serialized",
            serializer=ImageRenditionField(
                "fill-383x259",
                source="image"
            )
        ),
    ]


class WhyUsOrderable(Orderable):
    """WHy us orderable."""

    page = ParentalKey(
        "home.AboutPage",
        related_name="about_why_us"
    )

    icon = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )

    description = models.TextField(
        max_length=400,
        null=False,
        blank=False,
    )

    panels = [
        FieldPanel("icon"),
        FieldPanel("title"),
        FieldPanel("description"),
    ]

    api_fields = [
        APIField("title"),
        APIField("description"),
        APIField("icon"),
        APIField(
            "icon_serialized",
            serializer=ImageRenditionField(
                "fill-48x48",
                source="icon",
            )
        ),
    ]


class AboutPage(Page):
    max_count = 1

    """Fields for page."""
    custom_title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    custom_title_selected = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    description = RichTextField(
        features=[],
        blank=False,
    )

    company_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=False,
    )
    company_description = RichTextField(
        features=[],
        null=True,
        blank=False,
    )

    team_members = ParentalManyToManyField(
        TeamMember,
        blank=True,
    )
    trusted_partners = ParentalManyToManyField(
        TrustedPartner,
        blank=True,
    )
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("custom_title"),
            FieldPanel("custom_title_selected"),
            FieldPanel("description"),
            InlinePanel(
                "about_images",
                max_num=2,
                min_num=0,
                label="About Image"
            ),
        ], heading="About Intro Data"),
        MultiFieldPanel([
            FieldPanel("company_image"),
            FieldPanel("company_description"),
        ], heading="Company Data "),

        MultiFieldPanel([
            FieldPanel(
                "team_members",
                widget=forms.CheckboxSelectMultiple,
            )
        ], heading="Team Members"),
        MultiFieldPanel([
            FieldPanel(
                "trusted_partners",
                widget=forms.CheckboxSelectMultiple,
            )
        ], heading="Trusted Partners"),
        MultiFieldPanel(
            [
                InlinePanel(
                    "about_why_us",
                    max_num=6,
                    min_num=0,
                    label="About Why US",
                ),
            ],
            heading="Why US",
        )
    ]

    api_fields = [
        APIField("custom_title"),
        APIField("custom_title_selected"),
        APIField("description"),
        APIField("about_images"),
        APIField("about_why_us"),
        APIField("company_image"),
        APIField(
            "company_image_serialized",
            serializer=ImageRenditionField(
                "fill-541x371",
                source="company_image"
            )
        ),
        APIField("company_description"),
        APIField(
            "team_members",
            serializer=TeamMemberSerializer(
                many=True
            )
        ),
        APIField(
            "trusted_partners",
            serializer=TrustedPartnersSerializer(
                many=True
            )
        ),
    ]

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"
