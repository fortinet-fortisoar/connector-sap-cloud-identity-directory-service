## About the connector
The identity directory provides a System for Cross-domain Identity Management (SCIM) 2.0 REST API for managing resources (users, groups and custom schemas). Consumers of this REST API should be familiar with System for Cross-domain Identity Management Protocol before managing their own resources.
<p>This document provides information about the SAP Cloud Identity Directory Service Connector, which facilitates automated interactions, with a SAP Cloud Identity Directory Service server using FortiSOAR&trade; playbooks. Add the SAP Cloud Identity Directory Service Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with SAP Cloud Identity Directory Service.</p>

### Version information
Connector Version: 1.0.0
Authored By: Fortinet SAP Solutions Team
Certified: No

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
`yum install sap-cloud-identity-directory-service`

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
<tbody><tr><td>Tenant ID</td><td>
</td>
</tr><tr><td>Client ID</td><td>
</td>
</tr><tr><td>Client Secret</td><td>
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

### operation: Get User Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter</td><td>Example: emails.value eq "user@example.com"
More Details: https://api.sap.com/api/IdDS_SCIM/path/getUsers
</td></tr></tbody></table>

#### Output

 No output schema is available at this time.

### operation: Delete User
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>User UUID</td><td>
</td></tr></tbody></table>

#### Output
No output schema is available at this time.

### operation: Add User
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>User details</td><td>When creating a user, schemas, userName and emails attributes are required.
More details can be found here: https://api.sap.com/api/IdDS_SCIM/resource
</td></tr></tbody></table>

#### Output

No output schema is available at this time.

### operation: Update User
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Enable</td><td>Enable User
</td></tr><tr><td>Disable</td><td>Disable User
</td></tr><tr><td>User UUID</td><td>Provide the Unique User ID
</td></tr><tr><td>Custom JSON</td><td>
</td></tr></tbody></table>

#### Output
No output schema is available at this time.

### operation: Get Group Details
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Filter</td><td>
</td></tr></tbody></table>

#### Output
No output schema is available at this time.

### operation: Delete Group
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Group UUID</td><td>
</td></tr></tbody></table>

#### Output

No output schema is available at this time.

### operation: Add Group
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Name</td><td>
</td></tr><tr><td>Custom JSON</td><td>
</td></tr></tbody></table>

#### Output

No output schema is available at this time.

### operation: Update Group
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
