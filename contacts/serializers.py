from rest_framework import serializers


class ContactsFormSubmissionSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    phone = serializers.CharField()
    industry = serializers.CharField()
    message = serializers.CharField(max_length=1000)
    nda = serializers.BooleanField()
    file = serializers.FileField(required=False)


class CalculatePriceSubmissionSerializer(serializers.Serializer):
    email = serializers.EmailField()
    type = serializers.CharField()
    stage = serializers.CharField()
    consultation = serializers.CharField()
    duration = serializers.CharField()
