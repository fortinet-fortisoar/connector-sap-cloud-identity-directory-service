## About the connector
The identity directory provides a System for Cross-domain Identity Management (SCIM) 2.0 REST API for managing resources (users, groups and custom schemas). Consumers of this REST API should be familiar with System for Cross-domain Identity Management Protocol before managing their own resources.
<p>This document provides information about the SAP Cloud Identity Directory Service Connector, which facilitates automated interactions, with a SAP Cloud Identity Directory Service server using FortiSOAR&trade; playbooks. Add the SAP Cloud Identity Directory Service Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with SAP Cloud Identity Directory Service.</p>

### Version information
Connector Version: 1.0.0

Authored By: Fortinet SAP Solutions Team

Certified: No

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>

```bash
yum install sap-cloud-identity-directory-service
```

## Prerequisites to configuring the connector
- You must have the credentials of SAP Cloud Identity Directory Service server to which you will connect and perform automated operations.
    - How to generate API Keys, follow the Instractions [here](https://help.sap.com/docs/identity-authentication/identity-authentication/add-administrators#loiocefb742a36754b18bbe5c3503ac6d87c)
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the SAP Cloud Identity Directory Service server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)

### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>SAP Cloud Identity Directory Service</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead>
<tbody><tr><td>Tenant ID</td><td>ID can be found within the URL of the SAP IAS Service: https://"Tenant ID".accounts.ondemand.com/admin/#
</td>
</tr><tr><td>Client ID</td><td>Value of Secret ID
</td>
</tr><tr><td>Client Secret</td><td>Value of Secret Key
</td>
</tr></tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get User Details</td><td>Retrive all user information if no filter is specified</td><td> <br/></td></tr>
<tr><td>Delete User</td><td>Delete existing User.</td><td> <br/></td></tr>
<tr><td>Add User</td><td>Add a new user to the directory service</td><td> <br/></td></tr>
<tr><td>Update User</td><td>Update User Settings like enable, disable or change any availibe attributes.</td><td> <br/></td></tr>
<tr><td>Get Group Details</td><td>Get Details of existing Group. If no filter is specified, all groups will be returned.</td><td> <br/></td></tr>
<tr><td>Delete Group</td><td>Delete an existing Group</td><td> <br/></td></tr>
<tr><td>Add Group</td><td>Add new Group</td><td> <br/></td></tr>
<tr><td>Update Group</td><td>Update existing Group</td><td> <br/></td></tr>
</tbody></table>

### Operation: Get User Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter</td><td>Example: emails.value eq "user@example.com"
</td></tr></tbody></table>

- More Filter & Query Examples can be found here: https://api.sap.com/api/IdDS_SCIM/path/getUsers

#### Output

- Response Codes
<table border=1><thead><tr><th>Response Code</th><th>Description</th></tr></thead>
<tbody>
    <tr><td>200</td><td>The user resource is retrieved successfully. The maximum number of returned user's groups per request is 1000.</td></tr>
    <tr><td>500</td><td>unexpected error</td></tr>
</tbody></table>

- Example Response:
```json
{
  "Resources": [
    {
      "id": "4609edbc-679e-428b-a06d-11e1f57443aa",
      "externalId": "user1",
      "meta": {
        "created": "2020-10-26T16:03:49Z",
        "lastModified": "2020-10-26T16:03:49Z",
        "location": "https://agsecgqdp.accounts400.ondemand.com/scim/Users/4609edbc-679e-428b-a06d-11e1f57443aa",
        "version": "0e7c79a2-bfc7-4080-8a75-bc2e4f00af26",
        "resourceType": "User"
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User",
        "urn:ietf:params:scim:schemas:extension:sap:2.0:User"
      ],
      "userName": "user1",
      "name": {
        "formatted": "Mr John Doe I",
        "familyName": "user1",
        "givenName": "John",
        "middleName": "Doe",
        "honorificPrefix": "Mr.",
        "honorificSuffix": "I"
      },
      "displayName": "John Doe",
      "nickName": "Johnie",
      "profileUrl": "https://www.sap.com",
      "title": "King",
      "userType": "Employee",
      "timezone": "Europe/Sofia",
      "active": true,
      "emails": [
        {
          "value": "john.doe@sap.com",
          "display": "John Doe",
          "primary": true,
          "type": "work"
        }
      ],
      "addresses": [
        {
          "streetAddress": "string",
          "locality": "string",
          "region": "string",
          "postalCode": "string",
          "country": "string",
          "type": "string",
          "primary": true
        }
      ],
      "phoneNumbers": [
        {
          "value": "555-123-456",
          "primary": false,
          "type": "work"
        },
        {
          "value": "555-123-333",
          "primary": true,
          "type": "mobile"
        }
      ],
      "urn:ietf:params:scim:schemas:extension:sap:2.0:User": {
        "userId": "P000000",
        "userUuid": "4609edbc-679e-428b-a06d-11e1f57443aa",
        "loginTime": "2020-10-26T10:54:59Z",
        "sourceSystem": 15,
        "sourceSystemId": "sourceSystem1",
        "status": "active",
        "industry": "Chemicals",
        "addresses": [
          {
            "streetAddress": "string",
            "streetAddress2": "string",
            "locality": "string",
            "region": "string",
            "postalCode": "string",
            "country": "string",
            "type": "string",
            "primary": true
          }
        ],
        "passwordDetails": {
          "loginTime": "2020-10-26T10:54:59Z",
          "failedLoginAttempts": 0,
          "setTime": "2020-10-22T07:49:38Z",
          "status": "enabled",
          "policy": "https://accounts.sap.com/policy/passwords/sap/enterprise/1.0"
        },
        "corporateGroups": [
          {
            "value": "string"
          }
        ]
      },
      "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
        "division": "X",
        "manager": {
          "value": "d478473e-af5f-45dc-977c-8447313216dc",
          "$ref": "https://tenant.accounts.ondemand.com/scim/Users/d478473e-af5f-45dc-977c-8447313216dc",
          "displayName": "James"
        },
        "costCenter": "4130",
        "organization": "Manufacturing company",
        "department": "Marketing",
        "employeeNumber": "751988"
      }
    }
  ],
  "totalResults": 12014,
  "itemsPerPage": 1,
  "startIndex": 1,
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ]
}
```

### Operation: Delete User
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>User UUID</td><td>The UUID of the User which should get deleted
</td></tr></tbody></table>

#### Output
- Response Codes
<table border=1><thead><tr><th>Response Code</th><th>Description</th></tr></thead>
<tbody>
    <tr><td>204</td><td>The user is deleted successfully.</td></tr>
    <tr><td>400</td><td>The provided identifier is not valid.</td></tr>
    <tr><td>404</td><td>The user with the provided ID does not exist.</td></tr>
    <tr><td>500</td><td>unexpected error</td></tr>
</tbody></table>


### Operation: Add User
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>User details</td><td>When creating a user, schemas, userName and emails attributes are required.
</td></tr></tbody></table>

- More details can be found here: https://api.sap.com/api/IdDS_SCIM/path/createUser

- Example custom User input:
```json
{
  "externalId": "34F578JK",
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:User",
    "urn:ietf:params:scim:schemas:extension:sap:2.0:User",
    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
  ],
  "userName": "John",
  "password": "Abcd1234",
  "name": {
    "familyName": "Smith",
    "givenName": "Johny",
    "formatted": "Mr. John Smith I",
    "middleName": "Gilbert",
    "honorificPrefix": "Mr.",
    "honorificSuffix": "II"
  },
  "displayName": "Mr. John",
  "nickName": "Johny10",
  "profileUrl": "https://www.google.com/john.smith",
  "title": "Software Developer",
  "userType": "Employee",
  "preferredLanguage": "English",
  "locale": "EN",
  "timezone": "Europe/Sofia",
  "active": true,
  "emails": [
    {
      "type": "work",
      "value": "john.smith@sap-test.de",
      "display": "john.smith",
      "primary": true
    }
  ],
  "phoneNumbers": [
    {
      "type": "work",
      "value": "555-555-5555",
      "display": "John's phone",
      "primary": true
    }
  ],
  "photos": [
    {
      "type": "photo",
      "value": "https://www.facebook.com/john.smith",
      "display": "J.Smith",
      "primary": true
    }
  ],
  "addresses": [
    {
      "formatted": "8 Europa Str.",
      "primary": true,
      "country": "BG",
      "locality": "Sofia",
      "postalCode": "1000",
      "region": "SA",
      "streetAddress": "Europa Str.",
      "type": "work"
    }
  ],
  "entitlements": [
    {
      "type": "work",
      "value": "random",
      "primary": true
    }
  ],
  "roles": [
    {
      "type": "Read Users",
      "value": "random",
      "primary": true
    }
  ],
  "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
    "division": "IDS",
    "costCenter": "4130",
    "organization": "IDStore",
    "department": "Administration",
    "employeeNumber": "701984",
    "manager": {
      "displayName": "Manager",
      "value": "30ac69fe-5155-4d7f-8830-e9af6bf3e573",
      "$ref": "http://localhost:8080/idds/scim/v2/Users/<manager>"
    }
  },
  "urn:ietf:params:scim:schemas:extension:sap:2.0:User": {
    "loginTime": "2023-07-31T09:32:41.889Z",
    "sourceSystem": 0,
    "sourceSystemId": "000T41F12",
    "applicationId": "74P13R08",
    "emailTemplateSetId": "emailTemplateSetId",
    "sendMail": true,
    "targetUrl": "https://google.com",
    "mailVerified": true,
    "userUuid": "30ac69fe-5155-4d7f-8830-e9af6bf3e401",
    "userId": "P000008",
    "sapUserName": "Random",
    "status": "active",
    "totpEnabled": true,
    "webAuthEnabled": true,
    "industry": "Banking",
    "mfaEnabled": true,
    "contactPreferences": {
      "email": true,
      "telephone": true
    },
    "socialIdentities": [
      {
        "socialId": "777K815BM",
        "socialProvider": "LINKEDIN",
        "dateOfLinking": "2023-07-31T09:32:41.889Z"
      }
    ],
    "passwordDetails": {
      "loginTime": "2023-07-31T09:32:41.889Z",
      "failedLoginAttempts": 0,
      "setTime": "2023-07-31T09:32:41.889Z",
      "status": "enabled",
      "passwordLockedTime": "2023-07-31T09:32:41.889Z",
      "policy": "policy"
    },
    "emails": [
      {
        "type": "work",
        "value": "john.smith@sap-test.de",
        "display": "john.smith",
        "primary": true,
        "verified": true,
        "verifiedTime": "2023-07-31T09:32:41.889Z"
      }
    ],
    "corporateGroups": [
      {
        "value": "admin"
      }
    ],
    "phoneNumbers": [
      {
        "type": "work",
        "value": "555-555-5555",
        "display": "John's phone",
        "primary": true
      }
    ],
    "validFrom": "2023-07-31T09:32:41.889Z",
    "validTo": "2023-07-31T09:32:41.889Z"
  }
}
```

#### Output

- Response Codes
<table border=1><thead><tr><th>Response Code</th><th>Description</th></tr></thead>
<tbody>
    <tr><td>201</td><td>The user is created successfully.</td></tr>
    <tr><td>400</td><td>Wrong format or structure of the provided request body.</td></tr>
    <tr><td>409</td><td>The created user does not fulfill the uniqueness criteria for userName or emails.</td></tr>
    <tr><td>500</td><td>unexpected error</td></tr>
</tbody></table>

- Example Response:
```json
{
  "id": "string",
  "externalId": "string",
  "meta": {
    "created": "2023-07-31T09:32:41.910Z",
    "lastModified": "2023-07-31T09:32:41.910Z",
    "location": "string",
    "resourceType": "User",
    "version": "string"
  },
  "schemas": [
    "string"
  ],
  "userName": "string",
  "password": "string",
  "name": {
    "familyName": "string",
    "givenName": "string",
    "formatted": "string",
    "middleName": "string",
    "honorificPrefix": "string",
    "honorificSuffix": "string"
  },
  "displayName": "string",
  "nickName": "string",
  "profileUrl": "string",
  "title": "string",
  "userType": "string",
  "preferredLanguage": "string",
  "locale": "string",
  "timezone": "string",
  "active": true,
  "emails": [
    {
      "type": "work",
      "value": "string",
      "display": "string",
      "primary": true
    }
  ],
  "phoneNumbers": [
    {
      "type": "work",
      "value": "string",
      "display": "string",
      "primary": true
    }
  ],
  "ims": [
    {
      "type": "aim",
      "value": "string",
      "display": "string",
      "primary": true
    }
  ],
  "photos": [
    {
      "type": "photo",
      "value": "string",
      "display": "string",
      "primary": true
    }
  ],
  "addresses": [
    {
      "formatted": "string",
      "primary": true,
      "country": "string",
      "locality": "string",
      "postalCode": "string",
      "region": "string",
      "streetAddress": "string",
      "type": "work"
    }
  ],
  "entitlements": [
    {
      "type": "string",
      "value": "string",
      "primary": true
    }
  ],
  "roles": [
    {
      "type": "string",
      "value": "string",
      "primary": true
    }
  ],
  "x509Certificates": [
    {
      "type": "string",
      "value": "string",
      "primary": true
    }
  ],
  "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
    "division": "string",
    "costCenter": "string",
    "organization": "string",
    "department": "string",
    "employeeNumber": "string",
    "manager": {
      "displayName": "string",
      "value": "string",
      "$ref": "string"
    }
  },
  "urn:ietf:params:scim:schemas:extension:sap:2.0:User": {
    "loginTime": "2023-07-31T09:32:41.911Z",
    "sourceSystem": 0,
    "sourceSystemId": "string",
    "applicationId": "string",
    "emailTemplateSetId": "string",
    "sendMail": true,
    "targetUrl": "string",
    "mailVerified": true,
    "userUuid": "string",
    "userId": "string",
    "sapUserName": "string",
    "status": "string",
    "totpEnabled": true,
    "webAuthEnabled": true,
    "industry": "string",
    "mfaEnabled": true,
    "contactPreferences": {
      "email": "string",
      "telephone": "string"
    },
    "socialIdentities": {
      "socialId": "string",
      "socialProvider": "string",
      "dateOfLinking": "2023-07-31T09:32:41.911Z"
    },
    "passwordDetails": {
      "loginTime": "2023-07-31T09:32:41.911Z",
      "failedLoginAttempts": 0,
      "setTime": "2023-07-31T09:32:41.911Z",
      "status": "string",
      "passwordLockedTime": "2023-07-31T09:32:41.911Z",
      "policy": "string"
    },
    "emails": [
      {
        "type": "string",
        "value": "string",
        "display": "string",
        "primary": true,
        "verified": true,
        "verifiedTime": "2023-07-31T09:32:41.911Z"
      }
    ],
    "corporateGroups": [
      {
        "value": "string"
      }
    ],
    "phoneNumbers": [
      {
        "type": "work",
        "value": "string",
        "display": "string",
        "primary": true
      }
    ],
    "validFrom": "2023-07-31T09:32:41.911Z",
    "validTo": "2023-07-31T09:32:41.911Z"
  }
}
```

### Operation: Update User
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Enable</td><td>Enable User
</td></tr><tr><td>Disable</td><td>Disable User
</td></tr><tr><td>User UUID</td><td>Provide the Unique User ID
</td></tr><tr><td>Custom JSON</td><td>Provide a Custom Input (JSON format) to update the User
</td></tr></tbody></table>

- Example of Custom JSON input:
```json
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [
    {
      "op": "replace",
      "path": "phoneNumbers[type eq \"work\" and value eq \"123\"]",
      "value": [
        {
          "value": "456",
          "display": "John Smith",
          "primary": false,
          "type": "work"
        }
      ]
    }
  ]
}
```
- More Examples can be found here: https://api.sap.com/api/IdDS_SCIM/path/patchUser

#### Output
- Response Codes
<table border=1><thead><tr><th>Response Code</th><th>Description</th></tr></thead>
<tbody>
    <tr><td>204</td><td>The user is updated successfully. If you are passing an email with missing primary value through the replace operation or it is false, it will be set automatically to true.</td></tr>
    <tr><td>400</td><td>The provided identifier is not valid.</td></tr>
    <tr><td>404</td><td>The user with the provided ID does not exist.</td></tr>
    <tr><td>409</td><td>The updated user does not fulfill the uniqueness criteria for certain fields.</td></tr>
    <tr><td>500</td><td>unexpected error</td></tr>
</tbody></table>

### Operation: Get Group Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter</td><td>Provide a Custom Filter. Example: displayName eq "Administrators"
</td></tr></tbody></table>

- More Filter & Query Examples can be found here: https://api.sap.com/api/IdDS_SCIM/path/getGroups

#### Output
- Response Codes
<table border=1><thead><tr><th>Response Code</th><th>Description</th></tr></thead>
<tbody>
    <tr><td>204</td><td>The group resource is retrieved successfully. The maximum number of returned members per request is 20 000.</td></tr>
    <tr><td>500</td><td>unexpected error</td></tr>
</tbody></table>

- Example Response:
```json
{
  "Resources": [
    {
      "id": "<group_id>",
      "meta": {
        "created": "2020-10-14T14:33:39Z",
        "lastModified": "2020-10-14T14:33:39Z",
        "location": "https://tenant.testaccounts.ondemand.com/scim/Groups/<group_id>",
        "version": "<version_id>",
        "resourceType": "Group"
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:Group",
        "urn:sap:cloud:scim:schemas:extension:custom:2.0:Group"
      ],
      "displayName": "Tour Guides1",
      "members": [
        {
          "value": "<member_id>",
          "$ref": "https://tenant.testaccounts.ondemand.com/scim/Users/<member_id>",
          "type": "User"
        }
      ]
    }
  ],
  "totalResults": 1,
  "itemsPerPage": 100,
  "startIndex": 1,
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ]
}
```

### Operation: Delete Group
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Group UUID of the Group which should get deleted</td><td>
</td></tr></tbody></table>

#### Output

- Response Codes
<table border=1><thead><tr><th>Response Code</th><th>Description</th></tr></thead>
<tbody>
    <tr><td>204</td><td>The group is deleted successfully.</td></tr>
    <tr><td>400</td><td>The provided identifier is not valid.</td></tr>
    <tr><td>404</td><td>The group with the provided ID does not exist.</td></tr>
    <tr><td>500</td><td>unexpected error</td></tr>
</tbody></table>

### Operation: Add Group
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>
</td></tr><tr><td>Custom JSON</td><td>When creating a group, schemas and displayName attributes are required. If you add members to the group, the value (UUID) attribute of the member is required, while all other attributes of the member are optional.
</td></tr></tbody></table>

- More details can be found here: https://api.sap.com/api/IdDS_SCIM/path/createGroup
- Example Custom JSON input:
```json
{
  "id": "string",
  "meta": {
    "created": "2023-07-31T09:50:48.682Z",
    "lastModified": "2023-07-31T09:50:48.682Z",
    "location": "string",
    "resourceType": "User",
    "version": "string"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ],
  "displayName": "Administrators",
  "members": [
    {
      "value": "string",
      "type": "User",
      "$ref": "<path to access member>"
    }
  ],
  "externalId": "string",
  "urn:sap:cloud:scim:schemas:extension:custom:2.0:Group": {
    "additionalId": "string",
    "name": "string",
    "description": "string"
  }
}
```

#### Output

- Response Codes
<table border=1><thead><tr><th>Response Code</th><th>Description</th></tr></thead>
<tbody>
    <tr><td>201</td><td>The group is created successfully. The maximum number of returned members per request is 20 000.</td></tr>
    <tr><td>400</td><td>Wrong format or structure of the provided request body.</td></tr>
    <tr><td>500</td><td>unexpected error</td></tr>
</tbody></table>

- Example Response:
```json
{
  "id": "string",
  "meta": {
    "created": "2023-07-31T09:50:48.692Z",
    "lastModified": "2023-07-31T09:50:48.692Z",
    "location": "string",
    "resourceType": "User",
    "version": "string"
  },
  "schemas": [
    "urn:ietf:params:scim:schemas:core:2.0:Group"
  ],
  "displayName": "Administrators",
  "members": [
    {
      "value": "string",
      "type": "User",
      "$ref": "<path to access member>"
    }
  ],
  "externalId": "string",
  "urn:sap:cloud:scim:schemas:extension:custom:2.0:Group": {
    "additionalId": "string",
    "name": "string",
    "description": "string"
  }
}
```

### Operation: Update Group
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Add User</td><td>Add User to group. User UUID input required
</td></tr><tr><td>Remove User</td><td>Remove User from group. User UUID input required
</td></tr><tr><td>User UUID</td><td> Indentifier of the Group. Required if User should be added or removed.
</td></tr><tr><td>Group UUID</td><td> Indentifier of the Group
</td></tr><tr><td>Custom JSON</td><td> Custom input to performe custom operations like rename a Group
</td></tr></tbody></table>

- More examples can be found here: https://api.sap.com/api/IdDS_SCIM/path/patchGroup
- Example of Custom JSON:
```json
{
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:PatchOp"
  ],
  "Operations": [
    {
      "op": "add",
      "path": "members",
      "value": [
        {
          "value": "c7fcdd8c-a280-40f6-9b6b-ecffc512dcd2"
        }
      ]
    }
  ]
}
```

#### Output

- Response Codes
<table border=1><thead><tr><th>Response Code</th><th>Description</th></tr></thead>
<tbody>
    <tr><td>204</td><td>The group is updated successfully.</td></tr>
    <tr><td>400</td><td>The provided identifier is not valid.</td></tr>
    <tr><td>404</td><td>The group with the provided ID does not exist.</td></tr>
    <tr><td>500</td><td>unexpected error</td></tr>
</tbody></table>

## Included playbooks
The `Sample - SAP Cloud Identity Directory Service - 1.0.0` playbook collection comes bundled with the SAP Cloud Identity Directory Service connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the SAP Cloud Identity Directory Service connector.

- Get User Details
- Delete User
- Add User
- Update User
- Get Group Details
- Delete Group
- Add Group
- Update Group

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
