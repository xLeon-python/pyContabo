import json
from typing import List, Union

from .Snapshot import Snapshot
from .audits.SnapshotsAudits import SnapshotsAudits


class Snapshots:
    def __init__(self, instanceId: int, _http):

        self._http = _http
        self.instanceId = instanceId
        self.Audits = SnapshotsAudits(_http)

    def get(
        self,
        id: str = None,
        page: int = None,
        pageSize: int = None,
        orderBy: str = None,
        name: str = None,
        x_request_id: str = None,
        x_trace_id: str = None,
    ) -> Union[Snapshot, List[Snapshot]]:
        """fetches any snapshot(s) by id or other parameters

        Examples:
            >>> Snapshots.get()
            [snapshot]
            >>> Snapshots.get(name="mysnapshots")
            [snapshot]
            >>> Snapshots.get(id="100")
            snapshot

        Args:
            x_request_id: Uuid4 to identify individual requests for support cases.
            x_trace_id: Identifier to trace group of requests.
            id: The identifier of the snapshot
            page: Number of page to be fetched.
            pageSize: Number of elements per page.
            orderBy: Specify fields and ordering (ASC for ascending, DESC for descending) in following format `field:ASC|DESC`
            name: The name of the snapshot.

        Returns:
            List of snapshots
        """

        if id:
            resp = self._http.request(
                type="get",
                url=f"https://api.contabo.com/v1/compute/instances/{self.instanceId}/snapshots/{id}",
                x_request_id=x_request_id,
                x_trace_id=x_trace_id,
            )

            if resp.status_code == 404:
                return []

            return Snapshot(resp.json()["data"][0], self._http)

        else:
            url = f"https://api.contabo.com/v1/compute/instances/{self.instanceId}/snapshots?{f'page={page}&' if page is not None else ''}{f'size={pageSize}&' if pageSize is not None else ''}{f'orderBy={orderBy}&' if orderBy is not None else ''}{f'name={name}&' if name is not None else ''}"
            url = url[:-1]
            resp = self._http.request(
                type="get", url=url, x_request_id=x_request_id, x_trace_id=x_trace_id
            )

            data = resp.json()["data"]
            if len(data) == 0:
                return []

            snapshots = []
            for i in resp.json()["data"]:
                snapshots.append(Snapshot(i, self._http))
            return snapshots

    def create(
        self,
        name: str,
        description: str = None,
        x_request_id: str = None,
        x_trace_id: str = None,
    ) -> bool:
        """Creates a new snapshot

        Examples:
            >>> Snapshots.create(name="aName", description="desc.")
            True

        Args:
            x_request_id: Uuid4 to identify individual requests for support cases.
            x_trace_id: Identifier to trace group of requests.
            name: The name of the snapshot.
            description: The description of the snapshot. There is a limit of 255 characters per snapshot.

        Returns:
            Bool respresenting if the snapshot has been succesfully created.
        """

        if description:
            data = json.dumps({"name": name, "description": description})
        else:
            data = json.dumps({"name": name})

        resp = self._http.request(
            type="post",
            url=f"https://api.contabo.com/v1/compute/instances/{self.instanceId}/snapshots",
            data=data,
            x_request_id=x_request_id,
            x_trace_id=x_trace_id,
        )

        if resp.status_code == 201:
            return True
        return False
