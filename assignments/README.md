# Assignments

This document describes the assignments for the Software Engineering course.
They are classified by domain and some of them are optional. Please, refer
to the installation tutorial for details about the application and its
components.

- [MVC](#mvc)  
- [Unit testing](#unit-testing-with-pytest)
- [REST API](#rest-api)
- [Open Questions](#open-development-ideas)

## MVC

1. Create a new view (and a corresponding template) to show the keys of the
signing authority that are stored in the database. However, you should filter
the list of keys by role and only show the public keys. You can use the CSS
style that is applied to other templates.

2. Currently, a signature is generated taking into account only the contents
of the file. We would like to generate a signature on a file based on a time
stamp related to the signing date. The Signatures model contains a field 
for storing a time stamp that is updated with each signature. However, it is
not included in the signature process. Your task is: concatenate the resulting
time stamp with the file contents before signing. Tip: transform the time
stamp into a string, then to bytes.

3. (* Optional) Extend the verification functionality to include the time
stamp. You will need to obtain the time stamp from the model and concatenate
it with the file contents before verifying the signature.

## Unit testing with pytest

Suppose there will be a big refactoring in the codebase of the application
in the future. A new class, ECDSAHelper, will be used in the application. You
have the task to add new methods and to test them. The Signatures model contains
one fields that are not utilized in the application: hash. In this exercise,
we will be working with the class ECDSAHelper, implemented in
ou/ecdsa/ecdsa_helper.py. 

1. Create a new method hash(file) that receiving an existing file, reads contents
of the file in order to generate a hash on it; e.g. using sha256. You can refer
to simple_ecdsa.py (in the same directory) to see how a file can be read into
bytes. You can use the hashlib sha256 function to generate the hash.
2. Create different tests for this method using pytest (add them in 
test_ecdsa_helper.py) so you can run them via the "pytest" command in this
directory: e.g. ensure that the hash method reacts accordingly when a file does
not exist.
    
## REST API

1. Create a new API for recovering the signing and verifying keys
of the table Keys. You can check the model of the Keys in model.py

2. Can you add new keys using POST via the tool "http" that we installed
(httpie)?

3. (* Optional) Can you add a DELETE method so it is possible to remove keys from
the database?

## Open task

In the last iteration of your project, you are extending the project with
something that you think is important. Make your choice clear and document
briefly what this extension is, why is it important and how it works on a
high level. Then, design, implement, test and document the extension. During
the last meeting with the teacher, you will present it to the teacher.

You can devise this extension. Nevertheless, we provide a few possible
directions. Note that the result does not need to be a full-blown application.
It is much more important that all activities are carried out for at least
one well-defined feature.

- GUI
- Embedding the REST API to provide a microservice
    - Docker with a Linux distribution
    - Define the types of I/O parameters (i.e. interface definition)
- Organizing the signing service into a broader context
    - Different signing entities with different keys
    - Public-key certificate authority with multiple verification entities
    - Web of trust or CA hierarchy
- Connection to a directory service (e.g. LDAP) to enable users to sign
- Signing multiple documents simultaneously (each one separately)
