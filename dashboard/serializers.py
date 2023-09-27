# dashboard/serializers.py
from rest_framework import serializers
from .models import Trust, School

class TrustSerializer(serializers.ModelSerializer):
      
    class Meta:
        model = Trust
        fields = '__all__'

      

class SchoolSerializer(serializers.ModelSerializer):
    trust_name = serializers.SerializerMethodField()
    class Meta:
        model = School
        fields = '__all__'
    
    def get_trust_name(self, obj):
        return obj.trust.name    
