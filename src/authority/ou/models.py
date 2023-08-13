"""
This module holds the models used by the application:
* Platform
* Keys
* Signatures
"""

from django.db import models
from django.contrib.auth.models import User

class Platform(models.Model):
    """
    The Platform-model contains the platofrm where the key is used
    """

    platform_name = models.CharField(max_length=100)
    """platform_name: The name of the platform"""

    def __str__(self):
        return self.platform_name

class Keys(models.Model):
    """
    The Keys-model holds the public and private keys.
    """
    key = models.CharField(max_length=512)
    """key: the key"""

    role = models.CharField(max_length=64)
    """role: either public or private"""

    platform_used = models.ForeignKey(Platform, on_delete=models.CASCADE)
    """platform_used: the platform where this key is used"""

    owner = models.ForeignKey(User, on_delete=models.RESTRICT)
    """owner: the user that owns this key"""
    
    def __str__(self):
        return self.key

class Signatures(models.Model):
    """
    The Signatures-model hold the signatures that were generated for
    the uploaded files.
    """

    key_used = models.ForeignKey(Keys, on_delete=models.CASCADE)
    """key_used: reference to the key of the Keys-model"""

    file_name = models.CharField(max_length=100)
    """file_name: file name on the filesystem"""

    digest = models.CharField(max_length=512) 
    """digest: hash value of the file"""

    salt = models.CharField(max_length=128)
    """salt: string used for salting the encryption algorithm"""

    signature = models.CharField(max_length=512)
    """signature: the calculated signature"""

    time_stamp = models.DateTimeField('date signed')
    """time_stamp: the timestamp of signing"""
    
    def __str__(self):
        return self.file_name

