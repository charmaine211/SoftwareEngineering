#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The ECDSAHelper class is used for
ECDSA signature verification and creation.
Moreover, it imports public and private
keys. This test suite corresponds to the
ECDSAHelper class, different tests has
been implemented. """


# test vectors

from ecdsa_helper import ECDSAHelper


valid_sig_1 = "07f6828970aaad3f2ae4d120041fac416eab9807011f04a7473f84947c3598a4c146be68ad91ea63a9289d27700110ca686e436f44d759507f66b8ffe9034381"
valid_doc_path = "src/authority/ou/ecdsa/file.txt"
invalid_doc_path = "file_non_existent.txt"

__author__ = "Open University"
__copyright__ = "Copyright 2021"
__version__ = "1.0.0"


class TestClass:


    def test_correct_initialization_sign(self):
        """ This test asserts that when a user attempts
        to sign a message without importing first a
        private key, an error is reported. It fails
        otherwise """

        ecdsa_helper = ECDSAHelper()

        msg_bytes = bytes.fromhex("aabbccddeeff00112233445566778899")
        sig, status, err_msg = ecdsa_helper.sign_bytes(msg_bytes)

        assert sig == ""
        assert status == False
        assert err_msg is not None

    def test_correct_initialization_verify(self):
        """ This test asserts that when a user attempts
        to verify a message without importing first a
        public key, an error is reported. It fails
        otherwise """

        ecdsa_helper = ECDSAHelper()

        msg_bytes = bytes.fromhex("aabbccddeeff00112233445566778899")
        status, err_msg = ecdsa_helper.verify_bytes(
            bytes.fromhex(valid_sig_1), msg_bytes)

        assert status == False
        assert err_msg is not None


    def test_hash_unreadable(self):
        """ This test asserts that when a user attempts
        to hash an unreadable file, an error is reported. 
        It fails otherwise """

        ecdsa_helper = ECDSAHelper()
        h_string, err_msg = ecdsa_helper.hash(invalid_doc_path)

        assert h_string == ""
        assert err_msg == "[!] Error hashing file: [Errno 2] No such file or directory: 'file_non_existent.txt'"


    def test_hash_readable(self):
        """ This test asserts that when a user attempts
        to hash a readable file, no error is reported. 
        It fails otherwise """
        
        ecdsa_helper = ECDSAHelper()
        h_string, err_msg = ecdsa_helper.hash(valid_doc_path)

        assert h_string == "cad1380c04163a961a881d51f145435bdbf89bf25030e27bdd4e1bb0d3d958f7" # Hash for file.txt
        assert err_msg == ""
