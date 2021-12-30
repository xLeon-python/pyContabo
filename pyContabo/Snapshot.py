from .util import makeRequest, statusCheck


class Snapshot:

    def __init__(self, json, ):

        self.tenantId = json["tenantId"]
        self.customerId = json["customerId"]
        self.snapshotId = json["snapshotId"]
        self.name = json["name"]
        self.description = json["description"]
        self.instanceId = json["instanceId"]
        self.createdDate = json["createdDate"]
        self.autoDeleteDate = json["autoDeleteDate"]
        self.imageId = json["imageId"]
        self.imageName = json["imageName"]

        self.rawJson = json

    def update(self, name: str, desc: str):
        """updates name and description of a snapshot"""

        status = makeRequest(type="patch",
                             url=f"https://api.contabo.com/v1/compute/instances/{self.instanceId}/snapshots/{self.snapshotId}").status_code

        statusCheck(status)
        if status == 200:
            return True
        return False

    def delete(self):
        """deletes a snapshot"""

        status = makeRequest(type="delete",
                             url=f"https://api.contabo.com/v1/compute/instances/{self.instanceId}/snapshots/{self.snapshotId}").status_code

        statusCheck(status)
        if status == 204:
            return True
        return False

    def rollback(self):
        """rollbacks the instance to a snapshot"""

        status = makeRequest(type="post",
                             url=f"https://api.contabo.com/v1/compute/instances/{self.instanceId}/snapshots/{self.snapshotId}/rollback").status_code

        statusCheck(status)
        if status == 200:
            return True
        return False
