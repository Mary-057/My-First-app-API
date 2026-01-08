from rest_framework import serializers
from .models import guests_registration

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = guests_registration
        fields = '__all__'
