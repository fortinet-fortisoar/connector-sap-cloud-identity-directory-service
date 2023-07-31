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
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>User UUID</td><td>
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
More details can be found here: https://api.sap.com/api/IdDS_SCIM/resource
</td></tr></tbody></table>

#### Output

No output schema is available at this time.

### Operation: Update User
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Enable</td><td>Enable User
</td></tr><tr><td>Disable</td><td>Disable User
</td></tr><tr><td>User UUID</td><td>Provide the Unique User ID
</td></tr><tr><td>Custom JSON</td><td>
</td></tr></tbody></table>

#### Output
No output schema is available at this time.

### Operation: Get Group Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter</td><td>
</td></tr></tbody></table>

#### Output
No output schema is available at this time.

### Operation: Delete Group
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Group UUID</td><td>
</td></tr></tbody></table>

#### Output

No output schema is available at this time.

### Operation: Add Group
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>
</td></tr><tr><td>Custom JSON</td><td>
</td></tr></tbody></table>

#### Output

No output schema is available at this time.

### Operation: Update Group
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Add User</td><td>Add User to group. User UUID required
</td></tr><tr><td>Remove User</td><td>Remove User from group. User UUID required
</td></tr><tr><td>User UUID</td><td>
</td></tr><tr><td>Group UUID</td><td>
</td></tr><tr><td>Custom JSON</td><td>
</td></tr></tbody></table>

#### Output

No output schema is available at this time.

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
