# IntiSign API 1.0
This is the IntiSign API.  You can find more about the IntiSign application at https://www.intisign.nl.  

## Version: 1.0.0

### Terms of service
http://www.intisign.nl/terms/

**Contact information:**  
api-support@intisign.nl  

**License:** [Proprietary](http://intisign.nl)

### /signatures/

#### GET
##### Summary:

Get a list of signatures

##### Description:

This call returns a list of signatures the authenticated user has access to.

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful operation. | [ [SignaturesList](#SignaturesList) ] |
| 403 | No access (invalid username/password or insufficient rights). |  |

### /signatures/{id}/

#### GET
##### Summary:

Get a specific signature

##### Description:

This call returns the data of the signature with the given ID. The signature ID can be retrieved from the path in the URL.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | ID of signature to return | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful operation. | [Signatures](#Signatures) |
| 403 | No access (invalid username/password or insufficient rights). |  |
| 404 | Signature with given ID not found. |  |

### /keys/

#### GET
##### Summary:

Get a list of keys

##### Description:

This call returns a list of signatures the authenticated user has access to.

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful operation. | [ [KeysList](#KeysList) ] |
| 403 | No access (invalid username/password or insufficient rights). |  |

#### POST
##### Summary:

Add a new key

##### Description:

This call adds a new key to the database.

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| key | formData | The new key | Yes | string |
| role | formData | The role of the new key | Yes | string |
| owner | formData | The owner of the new key | Yes | integer |
| platform_used | formData | The platorm where this key is used | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Successful operation. | [ [Keys](#Keys) ] |
| 403 | No access (invalid username/password or insufficient rights). |  |

### Models


#### SignaturesList

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| count | integer |  | No |
| next | integer |  | No |
| previous | integer |  | No |
| results | [ [Signatures](#Signatures) ] |  | No |

#### Signatures

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| digest | string | File digest | No |
| salt | string | File salt | No |
| file_name | string |  | No |
| signature | string | The generated signature | No |
| url | string | API call to the specific signature | No |

#### KeysList

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| count | integer |  | No |
| next | integer |  | No |
| previous | integer |  | No |
| results | [ [Keys](#Keys) ] |  | No |

#### Keys

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| key | string | The key | No |
| owner | integer | The ID of the user this key belongs to | No |
| platform | integer | The ID of the platform this key belongs to | No |
| role | string | The role of this key | No |