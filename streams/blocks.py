from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class WhyProjectBlock(blocks.StructBlock):
    """Struct block for why section."""


    title = blocks.CharBlock(
        max_length=255,
        required=True,
        help_text="Add your title",
    )
    why_sections = blocks.ListBlock(
        blocks.StructBlock(
            [
                (
                    "title",
                    blocks.CharBlock(
                        required=True,
                        max_length=255,
                    ),
                ),
                (
                    "description",
                    blocks.TextBlock(
                        max_length=750,
                        required=True,
                    ),
                ),
                (
                    "icon",
                    ImageChooserBlock(
                        required=True,
                    ),
                )
            ]
        )
    )

    class Meta:
        icon = "circle-check"
        label = "Why Section block"


class ProjectStageBlock(blocks.StructBlock):
    """Stage struct block."""

    title = blocks.CharBlock(
        required=True,
        help_text="Add your title"
    )

    stages = blocks.ListBlock(
        blocks.StructBlock(
            [
                (
                    "title",
                     blocks.CharBlock(
                        required=True,
                        max_length=255,
                    )
                ),
                (
                    "description",
                    blocks.TextBlock(
                        max_length=750,
                        required=True,
                    ),
                ),
            ]
        )
    )

    class Meta:
        icon = "cogs"
        label = "Project Stage block"

    def get_prep_value(self, value):
        """Serialize the block value."""
        serialized_value = []
        for stage in value.get("stages", []):
            serialized_stage = {
                "title": stage.get("title", ""),
                "description": stage.get("description", ""),
            }
            serialized_value.append(serialized_stage)

        return {
            "title": value.get("title", ""),
            "stages": serialized_value,
        }


class FAQBlock(blocks.StructBlock):
    """FAQ Struct block."""

    title = blocks.CharBlock(
        required=True,
        max_length=250,
        help_text="Add your title",
    )

    faqs = blocks.ListBlock(
        blocks.StructBlock(
            [
                (
                    "question",
                    blocks.CharBlock(
                        required=True,
                        max_length=200,
                    )
                ),
                (
                    "answer",
                    blocks.TextBlock(
                        required=True,
                        max_length=400,
                    )
                )
            ]
        )
    )

    class Meta:
        icon = "help"
        label = "Project FAQ block"


class ServiceBlock(blocks.StructBlock):
    """Service struct block."""
    title = blocks.CharBlock(
        required=True,
        help_text="Service Title",
        max_length=100,
    )
    text = blocks.RichTextBlock(
        required=True,
        features=["bold", "italic"],
    )
    button_page = blocks.PageChooserBlock(required=False)

    def get_button_page_slug(self):
        if self.button_page:
            page_instance = self.button_page.specific
            page_slug = page_instance.slug
            return page_slug

        return None

    class Meta:
        icon = "cog"
        label = "Service"


class ServicesListBlock(blocks.StructBlock):
    """Services List struct block."""

    title = blocks.CharBlock(
        required=True,
        help_text="Services",
        max_length=250,
    )

    services = blocks.ListBlock(ServiceBlock())

    class Meta:
        icon = "cogs"
        label = "Services"
