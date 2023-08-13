#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hashlib import sha256
from ecdsa import SigningKey, VerifyingKey
import ecdsa

__author__ = "Open University"
__copyright__ = "Copyright 2021"
__version__ = "1.0.0"


class ECDSAHelper:

    """The ECDSAHelper class is used for
    ECDSA signature verification and creation.
    Moreover, it imports public and private
    keys.
    The class also creates a hash for a file."""

    def __init__(self):
        self._public_key = None
        self._private_key = None

    def import_public_key(self, pk_string):
        """Imports a public key.

        Args:
            pk_string: The public key in a hex string

        Returns:
            Returns the status of the import and an error message.
            When the import is successful, status is true and error message is an empty string
            Otherwise status is false and error message returns a string containing the error description"""

        err_msg = ""
        status = False

        try:
            self._public_key = VerifyingKey.from_string(bytes.fromhex(
                pk_string), curve=ecdsa.SECP256k1, hashfunc=sha256)
        except:
            err_msg = "[!] Error importing public key"
            status = False
            self._public_key = None
        else:
            err_msg = ""
            status = True
        finally:
            return status, err_msg

    def import_private_key(self, pk_string):
        """Imports a private key.

        Args:
            pk_string: The private key in a hexstring

        Returns:
            Returns the status of the import and an error message. 
            When the import is successful, status is true and error message is an empty string
            Otherwise status is false and error message returns a string containing the error description"""

        err_msg = ""
        status = False

        try:
            self._private_key = SigningKey.from_string(bytes.fromhex(
                pk_string), curve=ecdsa.SECP256k1, hashfunc=sha256)
        except:
            err_msg = "[!] Error importing private key"
            status = False
            self._private_key = None
        else:
            err_msg = ""
            status = True
        finally:
            return status, err_msg

    def sign_bytes(self, data):
        """ 
        Creates a signature for data.

        Args:
                data: a file that is converted into bytes e.g. via bytes.fromhex(hex_string)

        Returns: 
            Returns a hex string corresponding to the ECDSA signature"""

        sig = ""
        err_msg = ""
        status = "False"

        if self._private_key is not None:
            try:
                sig = self._private_key.sign(data).hex()
            except:
                err_msg = "[!] Error generating the signature"
                status = False
            else:
                status = True
                err_msg = ""
        else:
            err_msg = "[!] Private key is none"
            status = False

        return sig, status, err_msg

    def verify_bytes(self, sig, data):
        """Verifies if the signature belongs to the data.

        Args:
            data: a file that is converted into bytes e.g. via bytes.fromhex(hex_string)
            sig: bytes created by signing data e.g. via bytes.fromhex(hex_string)

        Returns:
            Returns status and error message.
            When the signature belongs to the data, status is true and error message is an empty string
            Otherwise status is false and error message returns a string containing the error description"""

        err_msg = ""
        status = "False"

        try:
            if self._public_key is not None:
                status = self._public_key.verify(sig, data)
                err_msg = ""
            else:
                err_msg = "[!] Public key is none"
                status = False
        except ecdsa.keys.BadSignatureError:
            err_msg = "[!] Error verifying signature"
            status = False
        else:
            err_msg = ""
        finally:
            return status, err_msg

    def hash(self, filename):
        """ Creates a hash for a file.

        Args:
            filename: The path of a file

        Returns:
            Returns hash and error message
            When the file is hashed, hash contains the hashvalue and the error message is and empty string.
            Otherwise the hash is and empty string and error message contains the error description."""

        err_msg = ""
        h_string = ""

        try:
            file = open(filename, 'rb')
            file_bytes = file.read()
            h = sha256(file_bytes)
            h_string = h.hexdigest()

        except Exception as e:
            err_msg = "[!] Error hashing file: " + str(e)

        finally:
            return h_string, err_msg


# constants
private_key = "c55aa56fa92e1fa54d71006c1194f9401e065d7ae2d3c20edf0310717f58fe57"
public_key = "f517069a424d598dfb62c18b0c445ee19a1849fcdf2c8db4e39aa0a5df278c7041425d4a24171e33ade9652b6a0d64e6f65d19c65b011ed73f04bb9dfffc4f99"

# test vectors

valid_sig_1 = "07f6828970aaad3f2ae4d120041fac416eab9807011f04a7473f84947c3598a4c146be68ad91ea63a9289d27700110ca686e436f44d759507f66b8ffe9034381"
valid_sig_2 = "62bbe4c3bf959cc46c45c3ebff612135ff39dd7f407a3ef15949cf1c07c440882338c3fb6c1eb1850c11655ca69fcd1db0f08127c32be6c4ea1e374880b86c72"
invalid_sig_1 = "62bbe4c3bf95dcc46c45c3ebff612135ff39dd7f407a3ef15949cf1c07c440882338c3fb6c1eb1850c11655ca69fcd1db0f08127c32be6c4ea1e374880b86c72"

if __name__ == "__main__":
    print("ECDSA helper --")

    ecdsa_helper = ECDSAHelper()
    status, err_msg = ecdsa_helper.import_private_key(private_key)

    if status is True:
        status, err_msg = ecdsa_helper.import_public_key(public_key)
        msg_bytes = bytes.fromhex("aabbccddeeff00112233445566778899")
        sig, status, err_msg = ecdsa_helper.sign_bytes(msg_bytes)

        if status is False:
            print(err_msg)
        else:
            print("[*] Signature: ", sig)

        status, err_msg = ecdsa_helper.verify_bytes(
            bytes.fromhex(sig), msg_bytes)
        if status is False:
            print(err_msg)
        else:
            print("[!] Verification: True")

    ecdsa_helper = ECDSAHelper()
    hash, err_msg = ecdsa_helper.hash('file.txt')
    if (err_msg == ""):
        print("[*] Hash file: ", hash)
    else:
        print("[!] Hash failed: ", err_msg)
