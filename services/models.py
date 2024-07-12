from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import StreamField
from wagtail.fields import RichTextField
from wagtail.admin.panels import (
    FieldPanel,
    PageChooserPanel,
    InlinePanel,
    MultiFieldPanel,
)
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField
from streams import blocks


class ServicePage(Page):
    """Service detail page."""

    custom_title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    description = RichTextField(
        features=[],
        blank=False,
    )
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=False,
    )

    content = StreamField(
        [
            (
                "stages",
                blocks.ProjectStageBlock(),
            ),
            (
                "why",
                blocks.WhyProjectBlock(),
            ),
            (
                "faq",
                blocks.FAQBlock(),
            )
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("image"),
        FieldPanel("description"),
        FieldPanel("content"),
    ]

    api_fields = [
        APIField("custom_title"),
        APIField("description"),
        APIField("content"),
        APIField("image"),
        APIField(
            "image_serialized",
            serializer=ImageRenditionField(
                "max-1000x1000",
                source="image"
            )
        ),
    ]

    def serialize_blocks(self):
        """Serialize StreamField content."""
        serialized_data = []
        for block in self.body:
            serialized_block = block.block.get_prep_value(block.value)
            serialized_data.append(serialized_block)
        return serialized_data



    class Meta:
        verbose_name = "Service Page"
        verbose_name_plural = "Service Pages"


class ServicesImages(Orderable):
    """Serive Listing page Images."""
    page = ParentalKey(
        "services.ServicesListPage",
        related_name="services_images"
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
                "fill-352x238",
                source="image"
            )
        ),
    ]


class ServicesListPage(Page):
    max_count = 1

    """Fields"""
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
    services = StreamField(
        [
            ("services", blocks.ServicesListBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("custom_title_selected"),
        FieldPanel("description"),
        InlinePanel(
            "services_images",
            max_num=2,
            min_num=0,
            label="Service Image",
        ),
        FieldPanel("services"),
    ]

    api_fields = [
        APIField("custom_title"),
        APIField("custom_title_selected"),
        APIField("services_images"),
        APIField("description"),
        APIField("services"),
    ]

    class Meta:
        verbose_name = "Services Page"
        verbose_name_plural = "Services Pages"