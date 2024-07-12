import json
from django.db import models
from wagtail.admin.panels import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    FieldRowPanel,
)
from wagtail.contrib.forms.models import (
    AbstractEmailForm,
    AbstractFormField,
    AbstractFormSubmission,
    FORM_FIELD_CHOICES,
)
from modelcluster.fields import ParentalKey
from django.shortcuts import render


class FormField(AbstractFormField):
    page = ParentalKey(
        "ContactsPage",
        related_name="form_fields",
        on_delete=models.CASCADE,
    )


class CustomContactsFormSubmission(AbstractFormSubmission):
    class Meta:
        pass


class ContactsPage(AbstractEmailForm):

    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel(
            "form_fields",
            label="Form fields",
        ),
    ]

    def serve(self, request, *args, **kwargs):
        if self.get_submission_class().objects.all().exists():
            return render(request, self.template, self.get_context(request))

        return super().serve(request, *args, **kwargs)

    def get_submission_class(self):
        return CustomContactsFormSubmission

    def process_form_submission(self, form):
        return self.get_submission_class().objects.create(
            form_data=json.dumps(form.cleaned_data),
            page=self
        )


class CalculateFormField(AbstractFormField):
    page = ParentalKey(
        "CalculateFormPage",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class CalculateCustomFormSubmission(AbstractFormSubmission):
    class Meta:
        pass


class CalculateFormPage(AbstractEmailForm):
    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel(
            "form_fields",
            label="Form fields",
        ),
    ]

    def serve(self, request, *args, **kwargs):
        if self.get_submission_class().objects.filter(page=self).exists():
            return render(
                request,
                self.template,
                self.get_context(request),
            )

        return super().serve(request, *args, **kwargs)

    def get_submission_class(self):
        return CalculateCustomFormSubmission

    def process_form_submission(self, form):
        return self.get_submission_class().objects.create(
            form_data=json.dumps(form.cleaned_data),
            page=self
        )
