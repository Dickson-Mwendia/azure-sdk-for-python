# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class ErrorDefinition(msrest.serialization.Model):
    """Error definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: Service specific error code which serves as the substatus for the HTTP error code.
    :vartype code: str
    :ivar message: Description of the error.
    :vartype message: str
    :ivar innererror: Internal error details.
    :vartype innererror: any
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
        'innererror': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'innererror': {'key': 'innererror', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ErrorDefinition, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.innererror = None


class InnerErrorTrace(msrest.serialization.Model):
    """Error details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar trace: detailed error trace.
    :vartype trace: list[str]
    """

    _validation = {
        'trace': {'readonly': True},
    }

    _attribute_map = {
        'trace': {'key': 'trace', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(InnerErrorTrace, self).__init__(**kwargs)
        self.trace = None


class MyWorkbookResource(msrest.serialization.Model):
    """An azure resource object.

    :param identity: Identity used for BYOS.
    :type identity: ~azure.mgmt.applicationinsights.v2021_03_08.models.MyWorkbookManagedIdentity
    :param id: Azure resource Id.
    :type id: str
    :param name: Azure resource name.
    :type name: str
    :param type: Azure resource type.
    :type type: str
    :param location: Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param etag: Resource etag.
    :type etag: dict[str, str]
    """

    _attribute_map = {
        'identity': {'key': 'identity', 'type': 'MyWorkbookManagedIdentity'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'etag': {'key': 'etag', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MyWorkbookResource, self).__init__(**kwargs)
        self.identity = kwargs.get('identity', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)
        self.etag = kwargs.get('etag', None)


class MyWorkbook(MyWorkbookResource):
    """An Application Insights private workbook definition.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param identity: Identity used for BYOS.
    :type identity: ~azure.mgmt.applicationinsights.v2021_03_08.models.MyWorkbookManagedIdentity
    :param id: Azure resource Id.
    :type id: str
    :param name: Azure resource name.
    :type name: str
    :param type: Azure resource type.
    :type type: str
    :param location: Resource location.
    :type location: str
    :param tags: A set of tags. Resource tags.
    :type tags: dict[str, str]
    :param etag: Resource etag.
    :type etag: dict[str, str]
    :param kind: The kind of workbook. Choices are user and shared. Possible values include:
     "user", "shared".
    :type kind: str or ~azure.mgmt.applicationinsights.v2021_03_08.models.Kind
    :ivar system_data: Metadata pertaining to creation and last modification of the resource.
    :vartype system_data: ~azure.mgmt.applicationinsights.v2021_03_08.models.SystemData
    :param display_name: The user-defined name of the private workbook.
    :type display_name: str
    :param serialized_data: Configuration of this particular private workbook. Configuration data
     is a string containing valid JSON.
    :type serialized_data: str
    :param version: This instance's version of the data model. This can change as new features are
     added that can be marked private workbook.
    :type version: str
    :ivar time_modified: Date and time in UTC of the last modification that was made to this
     private workbook definition.
    :vartype time_modified: str
    :param category: Workbook category, as defined by the user at creation time.
    :type category: str
    :param tags_properties_tags: A list of 0 or more tags that are associated with this private
     workbook definition.
    :type tags_properties_tags: list[str]
    :ivar user_id: Unique user id of the specific user that owns this private workbook.
    :vartype user_id: str
    :param source_id: Optional resourceId for a source resource.
    :type source_id: str
    :param storage_uri: BYOS Storage Account URI.
    :type storage_uri: str
    """

    _validation = {
        'system_data': {'readonly': True},
        'time_modified': {'readonly': True},
        'user_id': {'readonly': True},
    }

    _attribute_map = {
        'identity': {'key': 'identity', 'type': 'MyWorkbookManagedIdentity'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'etag': {'key': 'etag', 'type': '{str}'},
        'kind': {'key': 'kind', 'type': 'str'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'serialized_data': {'key': 'properties.serializedData', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'time_modified': {'key': 'properties.timeModified', 'type': 'str'},
        'category': {'key': 'properties.category', 'type': 'str'},
        'tags_properties_tags': {'key': 'properties.tags', 'type': '[str]'},
        'user_id': {'key': 'properties.userId', 'type': 'str'},
        'source_id': {'key': 'properties.sourceId', 'type': 'str'},
        'storage_uri': {'key': 'properties.storageUri', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MyWorkbook, self).__init__(**kwargs)
        self.kind = kwargs.get('kind', None)
        self.system_data = None
        self.display_name = kwargs.get('display_name', None)
        self.serialized_data = kwargs.get('serialized_data', None)
        self.version = kwargs.get('version', None)
        self.time_modified = None
        self.category = kwargs.get('category', None)
        self.tags_properties_tags = kwargs.get('tags_properties_tags', None)
        self.user_id = None
        self.source_id = kwargs.get('source_id', None)
        self.storage_uri = kwargs.get('storage_uri', None)


class MyWorkbookError(msrest.serialization.Model):
    """Error response.

    :param error: The error details.
    :type error: ~azure.mgmt.applicationinsights.v2021_03_08.models.ErrorDefinition
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorDefinition'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MyWorkbookError, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class MyWorkbookManagedIdentity(msrest.serialization.Model):
    """Customer Managed Identity.

    :param user_assigned_identities: Customer Managed Identity.
    :type user_assigned_identities:
     ~azure.mgmt.applicationinsights.v2021_03_08.models.MyWorkbookUserAssignedIdentities
    :param type: The identity type. Possible values include: "UserAssigned", "None".
    :type type: str or
     ~azure.mgmt.applicationinsights.v2021_03_08.models.MyWorkbookManagedIdentityType
    """

    _attribute_map = {
        'user_assigned_identities': {'key': 'userAssignedIdentities', 'type': 'MyWorkbookUserAssignedIdentities'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MyWorkbookManagedIdentity, self).__init__(**kwargs)
        self.user_assigned_identities = kwargs.get('user_assigned_identities', None)
        self.type = kwargs.get('type', None)


class MyWorkbooksListResult(msrest.serialization.Model):
    """Workbook list result.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: An array of private workbooks.
    :vartype value: list[~azure.mgmt.applicationinsights.v2021_03_08.models.MyWorkbook]
    :param next_link:
    :type next_link: str
    """

    _validation = {
        'value': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MyWorkbook]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MyWorkbooksListResult, self).__init__(**kwargs)
        self.value = None
        self.next_link = kwargs.get('next_link', None)


class MyWorkbookUserAssignedIdentities(msrest.serialization.Model):
    """Customer Managed Identity.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal ID of resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of resource.
    :vartype tenant_id: str
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MyWorkbookUserAssignedIdentities, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None


class SystemData(msrest.serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :param created_by: The identity that created the resource.
    :type created_by: str
    :param created_by_type: The type of identity that created the resource. Possible values
     include: "User", "Application", "ManagedIdentity", "Key".
    :type created_by_type: str or ~azure.mgmt.applicationinsights.v2021_03_08.models.CreatedByType
    :param created_at: The timestamp of resource creation (UTC).
    :type created_at: ~datetime.datetime
    :param last_modified_by: The identity that last modified the resource.
    :type last_modified_by: str
    :param last_modified_by_type: The type of identity that last modified the resource. Possible
     values include: "User", "Application", "ManagedIdentity", "Key".
    :type last_modified_by_type: str or
     ~azure.mgmt.applicationinsights.v2021_03_08.models.CreatedByType
    :param last_modified_at: The timestamp of resource last modification (UTC).
    :type last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'created_by_type': {'key': 'createdByType', 'type': 'str'},
        'created_at': {'key': 'createdAt', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'lastModifiedBy', 'type': 'str'},
        'last_modified_by_type': {'key': 'lastModifiedByType', 'type': 'str'},
        'last_modified_at': {'key': 'lastModifiedAt', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SystemData, self).__init__(**kwargs)
        self.created_by = kwargs.get('created_by', None)
        self.created_by_type = kwargs.get('created_by_type', None)
        self.created_at = kwargs.get('created_at', None)
        self.last_modified_by = kwargs.get('last_modified_by', None)
        self.last_modified_by_type = kwargs.get('last_modified_by_type', None)
        self.last_modified_at = kwargs.get('last_modified_at', None)
