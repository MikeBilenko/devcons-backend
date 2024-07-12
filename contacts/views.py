from rest_framework import generics, status
from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework.response import Response
from .models import (
    ContactsPage,
    CustomContactsFormSubmission,
    CalculateFormPage,
    CalculateCustomFormSubmission,
)
from .serializers import (
    ContactsFormSubmissionSerializer,
    CalculatePriceSubmissionSerializer,
)


class ContactsFormSubmissionAPI(generics.CreateAPIView):
    queryset = ContactsPage.objects.all()
    serializer_class = ContactsFormSubmissionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            try:
                page = ContactsPage.objects.first()
                if not page:
                    raise ContactsPage.DoesNotExist
            except ContactsPage.DoesNotExist:
                return Response(
                    {"error": "Page not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            form_data = {
                "email": serializer.validated_data.get("email"),
                "name": serializer.validated_data.get("name"),
                "phone": serializer.validated_data.get("phone"),
                "industry": serializer.validated_data.get("industry"),
                "message": serializer.validated_data.get("message"),
                "nda": serializer.validated_data.get("nda"),
            }

            if serializer.validated_data.get("file"):
                file = serializer.validated_data.get("file")
                file_url = self.handle_file_upload(file) if file else None
                full_url = request.build_absolute_uri(file_url)
                form_data["file"] = full_url

            CustomContactsFormSubmission.objects.create(
                page=page,
                form_data=form_data
            )

            subject = "MBDev Consulting Contact"
            body = ("Hello, thanks for contacting us, "
                    "we will get back to you soon!")
            from_email = settings.EMAIL_HOST_USER
            to_email = [serializer.validated_data.get("email")]

            email = EmailMessage(subject, body, from_email, to_email)
            email.send()

            email_new = EmailMessage(
                "New Potential customer for Dev Consulting",
                f"New potential client {serializer.validated_data.get('email')}; "
                f"{serializer.validated_data.get('name')}",
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER,]
            )
            email_new.send()

            return Response(
                {"message": "Form submitted successfully"},
                status=status.HTTP_201_CREATED
            )
        except:
            raise ValueError("Error")

    def handle_file_upload(self, uploaded_file):
        from django.core.files.storage import default_storage
        import os

        if not uploaded_file:
            return None

        filename = uploaded_file.name
        directory = "contacts"
        path = os.path.join(directory, filename)

        if not default_storage.exists(directory):
            os.mkdir(f"media/{directory}/")

        with default_storage.open(path, "wb+") as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        return default_storage.url(path)


class CalculateFormPricePageAPIView(generics.CreateAPIView):
    queryset = CalculateFormPage.objects.all()
    serializer_class = CalculatePriceSubmissionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            try:
                page = CalculateFormPage.objects.first()
                if not page:
                    raise CalculateFormPage.DoesNotExist
            except CalculateFormPage.DoesNotExist:
                return Response(
                    {"error": "Page not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            print(serializer.validated_data.get("consultation"))

            form_data = {
                "email": serializer.validated_data.get("email"),
                "type": serializer.validated_data.get("type"),
                "stage": serializer.validated_data.get("stage"),
                "consultation": serializer.validated_data.get("consultation"),
                "duration": serializer.validated_data.get("duration"),
            }

            CalculateCustomFormSubmission.objects.create(
                page=page,
                form_data=form_data
            )

            subject = "MBDev Consulting Calculate Price"
            body = "Hello, thanks for contacting us, we will get back to you soon!"
            from_email = settings.EMAIL_HOST_USER
            to_email = [serializer.validated_data.get("email")]

            email = EmailMessage(subject, body, from_email, to_email)
            email.send()

            email_new = EmailMessage(
                "New Potential customer for Dev Consulting from price calculation.",
                f"New potential client wants to calculate price {serializer.validated_data.get('email')}; ",
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER,]
            )
            email_new.send()

            return Response(
                {"message": "Form submitted successfully"},
                status=status.HTTP_201_CREATED
            )
        except:
            raise ValueError("Error")
