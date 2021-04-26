# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline.transport import HttpRequest, HttpResponse

from ._configuration import MaintenanceClientConfiguration
from .operations import PublicMaintenanceConfigurationsOperations
from .operations import ApplyUpdatesOperations
from .operations import ConfigurationAssignmentsOperations
from .operations import MaintenanceConfigurationsOperations
from .operations import MaintenanceConfigurationsForResourceGroupOperations
from .operations import ApplyUpdateForResourceGroupOperations
from .operations import ConfigurationAssignmentsWithinSubscriptionOperations
from .operations import Operations
from .operations import UpdatesOperations
from . import models


class MaintenanceClient(object):
    """Maintenance Client.

    :ivar public_maintenance_configurations: PublicMaintenanceConfigurationsOperations operations
    :vartype public_maintenance_configurations: azure.mgmt.maintenance.operations.PublicMaintenanceConfigurationsOperations
    :ivar apply_updates: ApplyUpdatesOperations operations
    :vartype apply_updates: azure.mgmt.maintenance.operations.ApplyUpdatesOperations
    :ivar configuration_assignments: ConfigurationAssignmentsOperations operations
    :vartype configuration_assignments: azure.mgmt.maintenance.operations.ConfigurationAssignmentsOperations
    :ivar maintenance_configurations: MaintenanceConfigurationsOperations operations
    :vartype maintenance_configurations: azure.mgmt.maintenance.operations.MaintenanceConfigurationsOperations
    :ivar maintenance_configurations_for_resource_group: MaintenanceConfigurationsForResourceGroupOperations operations
    :vartype maintenance_configurations_for_resource_group: azure.mgmt.maintenance.operations.MaintenanceConfigurationsForResourceGroupOperations
    :ivar apply_update_for_resource_group: ApplyUpdateForResourceGroupOperations operations
    :vartype apply_update_for_resource_group: azure.mgmt.maintenance.operations.ApplyUpdateForResourceGroupOperations
    :ivar configuration_assignments_within_subscription: ConfigurationAssignmentsWithinSubscriptionOperations operations
    :vartype configuration_assignments_within_subscription: azure.mgmt.maintenance.operations.ConfigurationAssignmentsWithinSubscriptionOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.maintenance.operations.Operations
    :ivar updates: UpdatesOperations operations
    :vartype updates: azure.mgmt.maintenance.operations.UpdatesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = MaintenanceClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.public_maintenance_configurations = PublicMaintenanceConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.apply_updates = ApplyUpdatesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.configuration_assignments = ConfigurationAssignmentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.maintenance_configurations = MaintenanceConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.maintenance_configurations_for_resource_group = MaintenanceConfigurationsForResourceGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.apply_update_for_resource_group = ApplyUpdateForResourceGroupOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.configuration_assignments_within_subscription = ConfigurationAssignmentsWithinSubscriptionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.updates = UpdatesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, http_request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.HttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> MaintenanceClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
