#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""helper.py: Creates a key pair for signing
and verifying documents using ECDSA and the 
SECP256k1 elliptic curve and SHA256 as digest."""

__author__      = "Open University"
__copyright__   = "Copyright 2021"
__version__ = "1.0.1"

import os
import sys
import ecdsa

from ecdsa import SigningKey, VerifyingKey
from hashlib import sha256

# constants

private_key = "c55aa56fa92e1fa54d71006c1194f9401e065d7ae2d3c20edf0310717f58fe57"
public_key = "f517069a424d598dfb62c18b0c445ee19a1849fcdf2c8db4e39aa0a5df278c7041425d4a24171e33ade9652b6a0d64e6f65d19c65b011ed73f04bb9dfffc4f99"

valid_sig_1 = "07f6828970aaad3f2ae4d120041fac416eab9807011f04a7473f84947c3598a4c146be68ad91ea63a9289d27700110ca686e436f44d759507f66b8ffe9034381"
valid_sig_2 = "62bbe4c3bf959cc46c45c3ebff612135ff39dd7f407a3ef15949cf1c07c440882338c3fb6c1eb1850c11655ca69fcd1db0f08127c32be6c4ea1e374880b86c72"

if __name__ == "__main__":
    print("ECDSA helper --")

    """
    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) 
    vk = sk.get_verifying_key()

    sk_serial = sk.to_string().hex()
    vk_serial = vk.to_string().hex()

    print("private:" , sk_serial)
    print("public: ", vk_serial)
    """
    sk_import = SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1, hashfunc=sha256)   
    vk_import = VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1, hashfunc=sha256)

    file = open(sys.argv[1], 'rb')
    file_bytes = file.read()

    print("[*] Reading: ", sys.argv[1])

    sig = sk_import.sign(file_bytes).hex()
    
    print("[*] Signature: ", sig)

    print("[*] Verify test: ", vk_import.verify(bytes.fromhex(sig), file_bytes)) # True
 
    print("[*] Verify test (1): ", vk_import.verify(bytes.fromhex(valid_sig_1), file_bytes)) # True

    print("[*] Verify test (2): ", vk_import.verify(bytes.fromhex(valid_sig_2), file_bytes)) # True


    file.close()
