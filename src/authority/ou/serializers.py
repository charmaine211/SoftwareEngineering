"""
Here the signatures are defined that are in use by the API.
The API can deal with both signatures and keys, so both are implemented here.
"""

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import  Signatures, Keys                

class SignaturesSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for signatures used by API to define the included fields.
    The serialiazer includes:
    ['url', 'file_name', 'digest', 'salt', 'signature', 'time_stamp']
    """
    url = serializers.HyperlinkedIdentityField(view_name="ou:signatures-detail")
    class Meta:
        model = Signatures
        fields = ['url', 'file_name', 'digest', 'salt', 'signature', 'time_stamp']


class KeysSerializer(serializers.ModelSerializer):
    """
    Serializer for keys used by API to define the included fields.
    The serialiazer includes:
    ['key', 'role', 'platform_used', 'owner']
    """
    class Meta:
        model = Keys
        fields = ['key', 'role', 'platform_used', 'owner']


