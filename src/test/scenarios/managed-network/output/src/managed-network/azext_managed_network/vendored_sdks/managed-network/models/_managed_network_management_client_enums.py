# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum

class ProvisioningState(str, Enum):

    updating = "Updating"
    deleting = "Deleting"
    failed = "Failed"
    succeeded = "Succeeded"

class Type(str, Enum):

    hub_and_spoke_topology = "HubAndSpokeTopology"
    mesh_topology = "MeshTopology"
