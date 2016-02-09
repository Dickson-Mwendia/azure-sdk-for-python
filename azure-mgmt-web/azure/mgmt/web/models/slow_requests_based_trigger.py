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


class SlowRequestsBasedTrigger(Model):
    """
    SlowRequestsBasedTrigger

    :param str time_taken: TimeTaken
    :param int count: Count
    :param str time_interval: TimeInterval
    """

    _required = []

    _attribute_map = {
        'time_taken': {'key': 'timeTaken', 'type': 'str'},
        'count': {'key': 'count', 'type': 'int'},
        'time_interval': {'key': 'timeInterval', 'type': 'str'},
    }

    def __init__(self, time_taken=None, count=None, time_interval=None):
        self.time_taken = time_taken
        self.count = count
        self.time_interval = time_interval
