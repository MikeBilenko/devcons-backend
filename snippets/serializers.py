from rest_framework.serializers import ModelSerializer
from .models import TeamMember, TrustedPartner

class TeamMemberSerializer(ModelSerializer):
    class Meta:
        model = TeamMember
        fields = "__all__"



class TrustedPartnersSerializer(ModelSerializer):
    class Meta:
        model = TrustedPartner
        fields = "__all__"