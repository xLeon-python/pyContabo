from .errors import NotFound
from .types.Audit import SnapshotsAudit
from .util import makeRequest, statusCheck


class SnapshotsAudits:

    def __init__(self):
        pass

    def get(self, page=None, pageSize=None, orderByField=None, orderBy=None, instanceId=None, snapshotId=None,
            requestId=None, changedBy=None):
        """gets audits history through the paging system"""

        url = f"https://api.contabo.com/v1/compute/snapshots/audits?{f'page={page}&' if page is not None else ''}{f'size={pageSize}&' if pageSize is not None else ''}{f'orderBy={orderByField}:{orderBy}&' if orderByField is not None else ''}{f'instanceId={instanceId}&' if instanceId is not None else ''}{f'snapshotId={snapshotId}&' if snapshotId is not None else ''}{f'requestId={requestId}&' if requestId is not None else ''}{f'instanceId={instanceId}&' if instanceId is not None else ''}{f'changedBy={changedBy}&' if changedBy is not None else ''}"
        url = url[:-1]
        resp = makeRequest(type="get",
                           url=url)

        statusCheck(resp.status_code)
        if resp.status_code == 200:
            data = resp.json()["data"]
            if len(data) == 0:
                raise NotFound("InstanceActionsAudits")

            audits = []
            for i in resp.json()["data"]:
                audits.append(SnapshotsAudit(i))  # TODO: Create InstanceAuditActions using JSON
            return audits
        else:
            return False
