"""
This module contains frontendviews and gives an implementation of the API-endpoints.
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Signatures, Keys
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from datetime import datetime
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SignaturesSerializer, KeysSerializer

import ecdsa
from ecdsa import SigningKey, VerifyingKey
from hashlib import sha256

import os.path
from os import path

from django.conf import settings


class IndexView(generic.ListView):
    """
    Index views, shows the latest signatures.
    """
    template_name = 'ou/index.html'
    context_object_name = 'latest_signature_list'

    def get_queryset(self):
        return Signatures.objects.all()


class VerifyView(generic.ListView):
    """
    View to verify signature.
    """
    model = Signatures
    template_name = 'ou/verify.html'


class SignView(generic.ListView):
    """
    View to sign documents.
    """
    model = Signatures
    template_name = 'ou/sign.html'

class KeyView(generic.ListView):
    model = Keys
    template_name = 'ou/keys.html'
    context_object_name = 'my_public_keys'

def Keys_View(request):
   
    public_keys = Keys.objects.filter(role='public')
    return render(request, 'ou/keys2.html', {'public_keys': public_keys})

   
def verify_signature(request):
    """
    Verifies signature of a given filename. Both the filename and the signature
    should be given. The given signature will be matched against the key in the
    database. 

    Args:
        request.POST['file_name']: The filename of the file on the filesystem of the server
        request.POST['signature']: The signature to test against

    Returns:
        Returns a redirect to ou/verify.html with the result of the verification.
    """
    file_name = request.POST['file_name']
    signature = request.POST['signature']

    complete_path = os.path.join(settings.BASE_DIR, "ou/upload/" + file_name)
    if path.exists(complete_path) == False or file_name == "" or signature == "":
        return render(request, 'ou/verify.html', {'uploaded_file_url': "Empty field or error"})

    file = open(complete_path, 'rb')
    file_bytes = file.read()

    # obtain public key from database
    public_key = get_object_or_404(Keys, pk=2)
    vk_import = VerifyingKey.from_string(bytes.fromhex(
        public_key.key), curve=ecdsa.SECP256k1, hashfunc=sha256)

    try:
        verify_result = vk_import.verify(bytes.fromhex(signature), file_bytes)
    except:
        return render(request, 'ou/verify.html', {'uploaded_file_url': "Failed verification"})

    return render(request, 'ou/verify.html', {'uploaded_file_url': str(verify_result)})


def upload_file(request):
    """
    Uploads file, saves file to filesystem, signs file and 
    stores signature in database.

    Args:
        request: Django request-object. request.FILES is used to handle the upload

    Returns:
        Returns a redirect to ou/sign.html with the new uploaded
        file on success (otherwise redirect to ou/sign.html without
        that file).
    """
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        # obtain signature here

        complete_path = os.path.join(
            settings.BASE_DIR, "ou/upload/" + myfile.name)
        if path.exists(complete_path) == False:
            return HttpResponse("File does not exist.")

        file = open(complete_path, "ab+")
        current_time = timezone.now()
        date_string = datetime.strftime(current_time, '%d-%m-%Y %H:%M:%S')
        date_bytes = bytes("\nDate signed: " + date_string, 'utf-8')

        file.write(date_bytes)
        file_bytes = file.read()

        # obtain private key from database

        private_key = get_object_or_404(Keys, pk=1)
        sk_import = SigningKey.from_string(bytes.fromhex(
            private_key.key), curve=ecdsa.SECP256k1, hashfunc=sha256)

        # sign the document

        sig = sk_import.sign(file_bytes).hex()

        # store result in database

        signature = Signatures(key_used=private_key, file_name=myfile.name,
                               digest="test", salt="test", signature=sig, time_stamp=current_time)
        signature.save()

        # return signature to user

        return render(request, 'ou/sign.html', {
            'uploaded_file_url': sig
        })
    return render(request, 'ou/sign.html')


class SignaturesViewSet(viewsets.ModelViewSet):
    """
    API endpoint for signatures.
    """
    queryset = Signatures.objects.all().order_by('id')
    serializer_class = SignaturesSerializer
    permission_classes = [permissions.IsAuthenticated]

class KeysViewSet(viewsets.ModelViewSet):
    """
    API endpoint for keys.
    """
    queryset = Keys.objects.all().order_by('id')
    serializer_class = KeysSerializer
    permission_classes = [permissions.IsAuthenticated]

