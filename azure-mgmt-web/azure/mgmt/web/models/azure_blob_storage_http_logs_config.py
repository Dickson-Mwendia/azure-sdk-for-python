# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AzureBlobStorageHttpLogsConfig(Model):
    """
    Http logs to azure blob storage configuration

    :param str sas_url: SAS url to a azure blob container with
     read/write/list/delete permissions
    :param int retention_in_days: Retention in days.
     Remove blobs older than X days.
     0 or lower means no retention.
    :param bool enabled: Enabled
    """

    _required = []

    _attribute_map = {
        'sas_url': {'key': 'sasUrl', 'type': 'str'},
        'retention_in_days': {'key': 'retentionInDays', 'type': 'int'},
        'enabled': {'key': 'enabled', 'type': 'bool'},
    }

    def __init__(self, sas_url=None, retention_in_days=None, enabled=None):
        self.sas_url = sas_url
        self.retention_in_days = retention_in_days
        self.enabled = enabled
