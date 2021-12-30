from .util import makeRequest, statusCheck
from .errors import NotFound
from .Snapshots import Snapshots

import json


class Instance:

    def __init__(self, json, contabo):

        self.tenantId = json["tenantId"]
        self.customerId = json["customerId"]
        self.name = json["name"]
        self.instanceId = json["instanceId"]
        self.region = json["region"]
        self.ipv4 = json["ipConfig"]["v4"]["ip"]
        self.ipv6 = json["ipConfig"]["v6"]["ip"]
        self.macAddress = json["macAddress"]
        self.ramMb = json["ramMb"]
        self.cpuCores = json["cpuCores"]
        self.osType = json["osType"]
        self.diskMb = json["diskMb"]
        self.createdDate = json["createdDate"]
        self.cancelDate = json["cancelDate"]
        self.status = json["status"]
        self.vHostId = json["vHostId"]
        self.addOns = json["addOns"]
        self.productType = json["productType"]

        self.rawJson = json
        self.contabo = contabo
        self.Snapshots = Snapshots(contabo, self.instanceId)

    def start(self):

        status = makeRequest(type="post",
                           url=f"https://api.contabo.com/v1/compute/instances/{str(self.instanceId)}/actions/start",
                           access_token=self.contabo.access_token).status_code

        statusCheck(status)
        if status == 201:
            return True
        return False

    def stop(self):

        status = makeRequest(type="post",
                           url=f"https://api.contabo.com/v1/compute/instances/{str(self.instanceId)}/actions/stop",
                           access_token=self.contabo.access_token).status_code

        statusCheck(status)
        if status == 201:
            return True
        return False

    def restart(self):

        status = makeRequest(type="post",
                           url=f"https://api.contabo.com/v1/compute/instances/{str(self.instanceId)}/actions/start",
                           access_token=self.contabo.access_token).status_code

        statusCheck(status)
        if status == 201:
            return True
        return False
