# IntiSign

[![pipeline status](https://git.cs.ou.nl/nick/signing-authority/badges/main/pipeline.svg)](https://git.cs.ou.nl/nick/signing-authority/-/commits/main)
[![Latest Release](https://git.cs.ou.nl/nick/signing-authority/-/badges/release.svg)](https://git.cs.ou.nl/nick/signing-authority/-/releases)

Welcome to the IntiSign repository.<br>
Intisign is a full-service system that allows you to publish artistic work in a discrete, yet secure, way to various broadcasting platforms.
Intisign aims to be easy to use and protective to your copyright.

## Documentation

- API documentation is available [here](/docs/api).
- Technical documentation about this application is available
  [here](/src/authority/docs/html/).
- UI design is available [here](https://www.figma.com/proto/JXBHwyDQXFjRDqDEuFbt2l/IntiSign?node-id=1-2&starting-point-node-id=1%3A2&mode=design&t=2FiF72XjV1OTeLLP-1).

## Technical data

- IntiSign is developed in Python framenwork [Django](https://www.djangoproject.com/).
- This program uses several Python [requirements](src/requirements.txt) that can be installed with PIP (`pip install -r src/requirements.txt`).
- Unit tests are available for PyTest. Run them from the root-directory to include all tests. All tests are run through pipelines using the CI-functionality of GitLab.

## Background information

A lot of background information is available in the Wiki that belongs to this project.

## Support

Support is available during business hours at <api-support@intisign.nl>.

## Repository contents

- The [src/authority](src/authority) directory contains the actual source-code.
  - [src/authority/docs](src/authority/docs) contains the API documentation.
  - [src/authority/tests](src/authority/tests) holds various tests.
  - [src/authority/ou](src/authority/ou) holds the code that implements both the IntiSign website and the API.
  - [src/authority/authority](src/authority/authority) contains some Django-related configuration.
- [tutorials](tutorials/) contains some generic tutorials to help you get started (not-IntiSign-related).
- [assignments](assignments/README.md) is the assignment that was the base of this project.

## Copyright

IntiSign was developed in 2022-2023 by

- Developer, Product owner & Scrum master: Lisanne Tor
- Developer & UI designer: Charmaine Noten
- Developer & GIT maintainer: Nick Huijsmans

for the `Software Engineering (IB3112)` course at the [Open University of The Netherlands](https://www.ou.nl).
