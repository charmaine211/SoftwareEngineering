## A description of the source code

The course application follows the typical structure of a Django project.
The project is called "authority" and contains a signing application called
"ou", in which you will be mainly working:

1. ecdsa/: This directory contains the unit tests (test_ecdsa_helper) related to a new class
(ECDSAHelper, described in ecdsa_helper.py), which you will use during one of the assignments. 
You can run pytest in this directory to pass the implemented tests. Further, there is
an example script simple_ecdsa.py, which you can use to understand how a file is read and
a signature is created on it. It includes the private and public keys used in the application.

2. models.py: It contains a description of the models in the application, Signatures (a list of
signatures created over a list of files and Keys, where the signing and verification keys are stored):

```
from django.db import models

class Keys(models.Model):
    key = models.CharField(max_length=512)
    role = models.CharField(max_length=64)
    
    def __str__(self):
        return self.key

class Signatures(models.Model):
    key_used = models.ForeignKey(Keys, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100)
    digest = models.CharField(max_length=512)
    salt = models.CharField(max_length=128)
    signature = models.CharField(max_length=512)
    time_stamp = models.DateTimeField('date signed')
    
    def __str__(self):
        return self.file_name
```

3. serializers.py: It contains a description of how a Signature is serialized
into JSON for the REST API:

```
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import  Signatures, Keys                


class SignaturesSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="ou:signatures-detail")
    class Meta:
        model = Signatures
        fields = ['url', 'file_name', 'digest', 'salt', 'signature', 'time_stamp']
```

4. static/ou/style.css: This is the CSS style that is used in the application.
5. templates/ou/: These are the HTML templates that interact with the user and receives
information from the application. Generally, they consist of input forms that process
data using POST. Otherwise, they show a collection of objects from the model.
6. upload/: This is where the uploaded files for signing are stored.
7. urls.py: This is where the urls in the application are configured and how the
interaction with the functions described in the view is performed.
8. views.py: This is a description of the views. The application contains the following
ones:
    - IndexView: It shows a collection of Signature objects in the main page. 
    - VerifyView: It shows an input form to verify a signature on a file.
    - SignView: It shows an input form to create a signature on a file (that is uploaded).

Moreover, views.py contains two methods for verifying a signature and uploading a file
and a method related to the REST API: SignaturesViewSet, that returns a collection
of Signatures and restrict the API to an authenticated user. Use always admin:admin.
