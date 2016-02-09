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


class VirtualApplication(Model):
    """VirtualApplication

    :param str virtual_path:
    :param str physical_path:
    :param bool preload_enabled:
    :param list virtual_directories:
    """

    _required = []

    _attribute_map = {
        'virtual_path': {'key': 'virtualPath', 'type': 'str'},
        'physical_path': {'key': 'physicalPath', 'type': 'str'},
        'preload_enabled': {'key': 'preloadEnabled', 'type': 'bool'},
        'virtual_directories': {'key': 'virtualDirectories', 'type': '[VirtualDirectory]'},
    }

    def __init__(self, virtual_path=None, physical_path=None, preload_enabled=None, virtual_directories=None):
        self.virtual_path = virtual_path
        self.physical_path = physical_path
        self.preload_enabled = preload_enabled
        self.virtual_directories = virtual_directories
