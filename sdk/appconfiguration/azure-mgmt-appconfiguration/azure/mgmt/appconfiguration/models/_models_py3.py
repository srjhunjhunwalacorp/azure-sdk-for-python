# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._app_configuration_management_client_enums import *


class ApiKey(msrest.serialization.Model):
    """An API key used for authenticating with a configuration store endpoint.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The key ID.
    :vartype id: str
    :ivar name: A name for the key describing its usage.
    :vartype name: str
    :ivar value: The value of the key that is used for authentication purposes.
    :vartype value: str
    :ivar connection_string: A connection string that can be used by supporting clients for
     authentication.
    :vartype connection_string: str
    :ivar last_modified: The last time any of the key's properties were modified.
    :vartype last_modified: ~datetime.datetime
    :ivar read_only: Whether this key can only be used for read operations.
    :vartype read_only: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'value': {'readonly': True},
        'connection_string': {'readonly': True},
        'last_modified': {'readonly': True},
        'read_only': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'connection_string': {'key': 'connectionString', 'type': 'str'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'read_only': {'key': 'readOnly', 'type': 'bool'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ApiKey, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.value = None
        self.connection_string = None
        self.last_modified = None
        self.read_only = None


class ApiKeyListResult(msrest.serialization.Model):
    """The result of a request to list API keys.

    :param value: The collection value.
    :type value: list[~app_configuration_management_client.models.ApiKey]
    :param next_link: The URI that can be used to request the next set of paged results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ApiKey]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ApiKey"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ApiKeyListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class CheckNameAvailabilityParameters(msrest.serialization.Model):
    """Parameters used for checking whether a resource name is available.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name to check for availability.
    :type name: str
    :ivar type: Required. The resource type to check for name availability. Default value:
     "Microsoft.AppConfiguration/configurationStores".
    :vartype type: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    type = "Microsoft.AppConfiguration/configurationStores"

    def __init__(
        self,
        *,
        name: str,
        **kwargs
    ):
        super(CheckNameAvailabilityParameters, self).__init__(**kwargs)
        self.name = name


class Resource(msrest.serialization.Model):
    """An Azure resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: Required. The location of the resource. This cannot be changed after the
     resource is created.
    :type location: str
    :param tags: A set of tags. The tags of the resource.
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        **kwargs
    ):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = location
        self.tags = tags


class ConfigurationStore(Resource):
    """The configuration store along with all resource properties. The Configuration Store will have all information to begin utilizing it.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: Required. The location of the resource. This cannot be changed after the
     resource is created.
    :type location: str
    :param tags: A set of tags. The tags of the resource.
    :type tags: dict[str, str]
    :param identity: The managed identity information, if configured.
    :type identity: ~app_configuration_management_client.models.ResourceIdentity
    :param sku: Required. The sku of the configuration store.
    :type sku: ~app_configuration_management_client.models.Sku
    :ivar provisioning_state: The provisioning state of the configuration store. Possible values
     include: "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled".
    :vartype provisioning_state: str or
     ~app_configuration_management_client.models.ProvisioningState
    :ivar creation_date: The creation date of configuration store.
    :vartype creation_date: ~datetime.datetime
    :ivar endpoint: The DNS endpoint where the configuration store API will be available.
    :vartype endpoint: str
    :param encryption: The encryption settings of the configuration store.
    :type encryption: ~app_configuration_management_client.models.EncryptionProperties
    :ivar private_endpoint_connections: The list of private endpoint connections that are set up
     for this resource.
    :vartype private_endpoint_connections:
     list[~app_configuration_management_client.models.PrivateEndpointConnectionReference]
    :param public_network_access: Control permission for data plane traffic coming from public
     networks while private endpoint is enabled. Possible values include: "Enabled", "Disabled".
    :type public_network_access: str or
     ~app_configuration_management_client.models.PublicNetworkAccess
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'sku': {'required': True},
        'provisioning_state': {'readonly': True},
        'creation_date': {'readonly': True},
        'endpoint': {'readonly': True},
        'private_endpoint_connections': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'identity': {'key': 'identity', 'type': 'ResourceIdentity'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
        'endpoint': {'key': 'properties.endpoint', 'type': 'str'},
        'encryption': {'key': 'properties.encryption', 'type': 'EncryptionProperties'},
        'private_endpoint_connections': {'key': 'properties.privateEndpointConnections', 'type': '[PrivateEndpointConnectionReference]'},
        'public_network_access': {'key': 'properties.publicNetworkAccess', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        location: str,
        sku: "Sku",
        tags: Optional[Dict[str, str]] = None,
        identity: Optional["ResourceIdentity"] = None,
        encryption: Optional["EncryptionProperties"] = None,
        public_network_access: Optional[Union[str, "PublicNetworkAccess"]] = None,
        **kwargs
    ):
        super(ConfigurationStore, self).__init__(location=location, tags=tags, **kwargs)
        self.identity = identity
        self.sku = sku
        self.provisioning_state = None
        self.creation_date = None
        self.endpoint = None
        self.encryption = encryption
        self.private_endpoint_connections = None
        self.public_network_access = public_network_access


class ConfigurationStoreListResult(msrest.serialization.Model):
    """The result of a request to list configuration stores.

    :param value: The collection value.
    :type value: list[~app_configuration_management_client.models.ConfigurationStore]
    :param next_link: The URI that can be used to request the next set of paged results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ConfigurationStore]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["ConfigurationStore"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(ConfigurationStoreListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ConfigurationStoreUpdateParameters(msrest.serialization.Model):
    """The parameters for updating a configuration store.

    :param identity: The managed identity information for the configuration store.
    :type identity: ~app_configuration_management_client.models.ResourceIdentity
    :param sku: The SKU of the configuration store.
    :type sku: ~app_configuration_management_client.models.Sku
    :param tags: A set of tags. The ARM resource tags.
    :type tags: dict[str, str]
    :param encryption: The encryption settings of the configuration store.
    :type encryption: ~app_configuration_management_client.models.EncryptionProperties
    """

    _attribute_map = {
        'identity': {'key': 'identity', 'type': 'ResourceIdentity'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'encryption': {'key': 'properties.encryption', 'type': 'EncryptionProperties'},
    }

    def __init__(
        self,
        *,
        identity: Optional["ResourceIdentity"] = None,
        sku: Optional["Sku"] = None,
        tags: Optional[Dict[str, str]] = None,
        encryption: Optional["EncryptionProperties"] = None,
        **kwargs
    ):
        super(ConfigurationStoreUpdateParameters, self).__init__(**kwargs)
        self.identity = identity
        self.sku = sku
        self.tags = tags
        self.encryption = encryption


class EncryptionProperties(msrest.serialization.Model):
    """The encryption settings for a configuration store.

    :param key_vault_properties: Key vault properties.
    :type key_vault_properties: ~app_configuration_management_client.models.KeyVaultProperties
    """

    _attribute_map = {
        'key_vault_properties': {'key': 'keyVaultProperties', 'type': 'KeyVaultProperties'},
    }

    def __init__(
        self,
        *,
        key_vault_properties: Optional["KeyVaultProperties"] = None,
        **kwargs
    ):
        super(EncryptionProperties, self).__init__(**kwargs)
        self.key_vault_properties = key_vault_properties


class Error(msrest.serialization.Model):
    """AppConfiguration error object.

    :param code: Error code.
    :type code: str
    :param message: Error message.
    :type message: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        **kwargs
    ):
        super(Error, self).__init__(**kwargs)
        self.code = code
        self.message = message


class KeyValue(msrest.serialization.Model):
    """The result of a request to retrieve a key-value from the specified configuration store.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar key: The primary identifier of a key-value.
     The key is used in unison with the label to uniquely identify a key-value.
    :vartype key: str
    :ivar label: A value used to group key-values.
     The label is used in unison with the key to uniquely identify a key-value.
    :vartype label: str
    :ivar value: The value of the key-value.
    :vartype value: str
    :ivar content_type: The content type of the key-value's value.
     Providing a proper content-type can enable transformations of values when they are retrieved
     by applications.
    :vartype content_type: str
    :ivar e_tag: An ETag indicating the state of a key-value within a configuration store.
    :vartype e_tag: str
    :ivar last_modified: The last time a modifying operation was performed on the given key-value.
    :vartype last_modified: ~datetime.datetime
    :ivar locked: A value indicating whether the key-value is locked.
     A locked key-value may not be modified until it is unlocked.
    :vartype locked: bool
    :ivar tags: A set of tags. A dictionary of tags that can help identify what a key-value may be
     applicable for.
    :vartype tags: dict[str, str]
    """

    _validation = {
        'key': {'readonly': True},
        'label': {'readonly': True},
        'value': {'readonly': True},
        'content_type': {'readonly': True},
        'e_tag': {'readonly': True},
        'last_modified': {'readonly': True},
        'locked': {'readonly': True},
        'tags': {'readonly': True},
    }

    _attribute_map = {
        'key': {'key': 'key', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'content_type': {'key': 'contentType', 'type': 'str'},
        'e_tag': {'key': 'eTag', 'type': 'str'},
        'last_modified': {'key': 'lastModified', 'type': 'iso-8601'},
        'locked': {'key': 'locked', 'type': 'bool'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(KeyValue, self).__init__(**kwargs)
        self.key = None
        self.label = None
        self.value = None
        self.content_type = None
        self.e_tag = None
        self.last_modified = None
        self.locked = None
        self.tags = None


class KeyVaultProperties(msrest.serialization.Model):
    """Settings concerning key vault encryption for a configuration store.

    :param key_identifier: The URI of the key vault key used to encrypt data.
    :type key_identifier: str
    :param identity_client_id: The client id of the identity which will be used to access key
     vault.
    :type identity_client_id: str
    """

    _attribute_map = {
        'key_identifier': {'key': 'keyIdentifier', 'type': 'str'},
        'identity_client_id': {'key': 'identityClientId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        key_identifier: Optional[str] = None,
        identity_client_id: Optional[str] = None,
        **kwargs
    ):
        super(KeyVaultProperties, self).__init__(**kwargs)
        self.key_identifier = key_identifier
        self.identity_client_id = identity_client_id


class ListKeyValueParameters(msrest.serialization.Model):
    """The parameters used to list a configuration store key-value.

    All required parameters must be populated in order to send to Azure.

    :param key: Required. The key to retrieve.
    :type key: str
    :param label: The label of the key.
    :type label: str
    """

    _validation = {
        'key': {'required': True},
    }

    _attribute_map = {
        'key': {'key': 'key', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        key: str,
        label: Optional[str] = None,
        **kwargs
    ):
        super(ListKeyValueParameters, self).__init__(**kwargs)
        self.key = key
        self.label = label


class NameAvailabilityStatus(msrest.serialization.Model):
    """The result of a request to check the availability of a resource name.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name_available: The value indicating whether the resource name is available.
    :vartype name_available: bool
    :ivar message: If any, the error message that provides more detail for the reason that the name
     is not available.
    :vartype message: str
    :ivar reason: If any, the reason that the name is not available.
    :vartype reason: str
    """

    _validation = {
        'name_available': {'readonly': True},
        'message': {'readonly': True},
        'reason': {'readonly': True},
    }

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'message': {'key': 'message', 'type': 'str'},
        'reason': {'key': 'reason', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(NameAvailabilityStatus, self).__init__(**kwargs)
        self.name_available = None
        self.message = None
        self.reason = None


class OperationDefinition(msrest.serialization.Model):
    """The definition of a configuration store operation.

    :param name: Operation name: {provider}/{resource}/{operation}.
    :type name: str
    :param display: The display information for the configuration store operation.
    :type display: ~app_configuration_management_client.models.OperationDefinitionDisplay
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDefinitionDisplay'},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        display: Optional["OperationDefinitionDisplay"] = None,
        **kwargs
    ):
        super(OperationDefinition, self).__init__(**kwargs)
        self.name = name
        self.display = display


class OperationDefinitionDisplay(msrest.serialization.Model):
    """The display information for a configuration store operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provider: The resource provider name: Microsoft App Configuration.".
    :vartype provider: str
    :param resource: The resource on which the operation is performed.
    :type resource: str
    :param operation: The operation that users can perform.
    :type operation: str
    :param description: The description for the operation.
    :type description: str
    """

    _validation = {
        'provider': {'readonly': True},
    }

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        resource: Optional[str] = None,
        operation: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(OperationDefinitionDisplay, self).__init__(**kwargs)
        self.provider = None
        self.resource = resource
        self.operation = operation
        self.description = description


class OperationDefinitionListResult(msrest.serialization.Model):
    """The result of a request to list configuration store operations.

    :param value: The collection value.
    :type value: list[~app_configuration_management_client.models.OperationDefinition]
    :param next_link: The URI that can be used to request the next set of paged results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[OperationDefinition]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["OperationDefinition"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(OperationDefinitionListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class PrivateEndpoint(msrest.serialization.Model):
    """Private endpoint which a connection belongs to.

    :param id: The resource Id for private endpoint.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        **kwargs
    ):
        super(PrivateEndpoint, self).__init__(**kwargs)
        self.id = id


class PrivateEndpointConnection(msrest.serialization.Model):
    """A private endpoint connection.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :ivar provisioning_state: The provisioning status of the private endpoint connection. Possible
     values include: "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled".
    :vartype provisioning_state: str or
     ~app_configuration_management_client.models.ProvisioningState
    :param private_endpoint: The resource of private endpoint.
    :type private_endpoint: ~app_configuration_management_client.models.PrivateEndpoint
    :param private_link_service_connection_state: A collection of information about the state of
     the connection between service consumer and provider.
    :type private_link_service_connection_state:
     ~app_configuration_management_client.models.PrivateLinkServiceConnectionState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'private_endpoint': {'key': 'properties.privateEndpoint', 'type': 'PrivateEndpoint'},
        'private_link_service_connection_state': {'key': 'properties.privateLinkServiceConnectionState', 'type': 'PrivateLinkServiceConnectionState'},
    }

    def __init__(
        self,
        *,
        private_endpoint: Optional["PrivateEndpoint"] = None,
        private_link_service_connection_state: Optional["PrivateLinkServiceConnectionState"] = None,
        **kwargs
    ):
        super(PrivateEndpointConnection, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.provisioning_state = None
        self.private_endpoint = private_endpoint
        self.private_link_service_connection_state = private_link_service_connection_state


class PrivateEndpointConnectionListResult(msrest.serialization.Model):
    """A list of private endpoint connections.

    :param value: The collection value.
    :type value: list[~app_configuration_management_client.models.PrivateEndpointConnection]
    :param next_link: The URI that can be used to request the next set of paged results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PrivateEndpointConnection]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["PrivateEndpointConnection"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(PrivateEndpointConnectionListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class PrivateEndpointConnectionReference(msrest.serialization.Model):
    """A reference to a related private endpoint connection.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :ivar provisioning_state: The provisioning status of the private endpoint connection. Possible
     values include: "Creating", "Updating", "Deleting", "Succeeded", "Failed", "Canceled".
    :vartype provisioning_state: str or
     ~app_configuration_management_client.models.ProvisioningState
    :param private_endpoint: The resource of private endpoint.
    :type private_endpoint: ~app_configuration_management_client.models.PrivateEndpoint
    :param private_link_service_connection_state: A collection of information about the state of
     the connection between service consumer and provider.
    :type private_link_service_connection_state:
     ~app_configuration_management_client.models.PrivateLinkServiceConnectionState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'private_endpoint': {'key': 'properties.privateEndpoint', 'type': 'PrivateEndpoint'},
        'private_link_service_connection_state': {'key': 'properties.privateLinkServiceConnectionState', 'type': 'PrivateLinkServiceConnectionState'},
    }

    def __init__(
        self,
        *,
        private_endpoint: Optional["PrivateEndpoint"] = None,
        private_link_service_connection_state: Optional["PrivateLinkServiceConnectionState"] = None,
        **kwargs
    ):
        super(PrivateEndpointConnectionReference, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.provisioning_state = None
        self.private_endpoint = private_endpoint
        self.private_link_service_connection_state = private_link_service_connection_state


class PrivateLinkResource(msrest.serialization.Model):
    """A resource that supports private link capabilities.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :ivar group_id: The private link resource group id.
    :vartype group_id: str
    :ivar required_members: The private link resource required member names.
    :vartype required_members: list[str]
    :ivar required_zone_names: The list of required DNS zone names of the private link resource.
    :vartype required_zone_names: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'group_id': {'readonly': True},
        'required_members': {'readonly': True},
        'required_zone_names': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'group_id': {'key': 'properties.groupId', 'type': 'str'},
        'required_members': {'key': 'properties.requiredMembers', 'type': '[str]'},
        'required_zone_names': {'key': 'properties.requiredZoneNames', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(PrivateLinkResource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.group_id = None
        self.required_members = None
        self.required_zone_names = None


class PrivateLinkResourceListResult(msrest.serialization.Model):
    """A list of private link resources.

    :param value: The collection value.
    :type value: list[~app_configuration_management_client.models.PrivateLinkResource]
    :param next_link: The URI that can be used to request the next set of paged results.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[PrivateLinkResource]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        value: Optional[List["PrivateLinkResource"]] = None,
        next_link: Optional[str] = None,
        **kwargs
    ):
        super(PrivateLinkResourceListResult, self).__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class PrivateLinkServiceConnectionState(msrest.serialization.Model):
    """The state of a private link service connection.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param status: The private link service connection status. Possible values include: "Pending",
     "Approved", "Rejected", "Disconnected".
    :type status: str or ~app_configuration_management_client.models.ConnectionStatus
    :param description: The private link service connection description.
    :type description: str
    :ivar actions_required: Any action that is required beyond basic workflow (approve/ reject/
     disconnect). Possible values include: "None", "Recreate".
    :vartype actions_required: str or ~app_configuration_management_client.models.ActionsRequired
    """

    _validation = {
        'actions_required': {'readonly': True},
    }

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'actions_required': {'key': 'actionsRequired', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        status: Optional[Union[str, "ConnectionStatus"]] = None,
        description: Optional[str] = None,
        **kwargs
    ):
        super(PrivateLinkServiceConnectionState, self).__init__(**kwargs)
        self.status = status
        self.description = description
        self.actions_required = None


class RegenerateKeyParameters(msrest.serialization.Model):
    """The parameters used to regenerate an API key.

    :param id: The id of the key to regenerate.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        **kwargs
    ):
        super(RegenerateKeyParameters, self).__init__(**kwargs)
        self.id = id


class ResourceIdentity(msrest.serialization.Model):
    """An identity that can be associated with a resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param type: The type of managed identity used. The type 'SystemAssigned, UserAssigned'
     includes both an implicitly created identity and a set of user-assigned identities. The type
     'None' will remove any identities. Possible values include: "None", "SystemAssigned",
     "UserAssigned", "SystemAssigned, UserAssigned".
    :type type: str or ~app_configuration_management_client.models.IdentityType
    :param user_assigned_identities: The list of user-assigned identities associated with the
     resource. The user-assigned identity dictionary keys will be ARM resource ids in the form:
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
    :type user_assigned_identities: dict[str,
     ~app_configuration_management_client.models.UserIdentity]
    :ivar principal_id: The principal id of the identity. This property will only be provided for a
     system-assigned identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant id associated with the resource's identity. This property will only
     be provided for a system-assigned identity.
    :vartype tenant_id: str
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'user_assigned_identities': {'key': 'userAssignedIdentities', 'type': '{UserIdentity}'},
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        type: Optional[Union[str, "IdentityType"]] = None,
        user_assigned_identities: Optional[Dict[str, "UserIdentity"]] = None,
        **kwargs
    ):
        super(ResourceIdentity, self).__init__(**kwargs)
        self.type = type
        self.user_assigned_identities = user_assigned_identities
        self.principal_id = None
        self.tenant_id = None


class Sku(msrest.serialization.Model):
    """Describes a configuration store SKU.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The SKU name of the configuration store.
    :type name: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        name: str,
        **kwargs
    ):
        super(Sku, self).__init__(**kwargs)
        self.name = name


class UserIdentity(msrest.serialization.Model):
    """A resource identity that is managed by the user of the service.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar principal_id: The principal ID of the user-assigned identity.
    :vartype principal_id: str
    :ivar client_id: The client ID of the user-assigned identity.
    :vartype client_id: str
    """

    _validation = {
        'principal_id': {'readonly': True},
        'client_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'client_id': {'key': 'clientId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(UserIdentity, self).__init__(**kwargs)
        self.principal_id = None
        self.client_id = None
