import json

from .Assignment import Assignment
from .audits.TagAssignmentsAudits import TagAssignmentsAudits


class Assignments:

    def __init__(self, _http, tagId):

        self._http = _http
        self.tagId = tagId
        self.Audits = AssignmentsAudits(_http)

    def get(self, resourceType: str = None, resourceId: str = None, page: int = None, pageSize: int = None,
            orderBy: str = None):
        """gets any tag assignment by id or other parameters through the paging system"""

        if resourceType and resourceId:
            resp = self._http.request(type="get",
                               url=f"https://api.contabo.com/v1/tags/{self.tagId}/assignments/{resourceType}/{resourceId}")

            if resp.status_code == 404:
                return []

            return Assignment(resp.json()["data"][0], self._http)

        else:
            url = f"https://api.contabo.com/v1/tags/{self.tagId}/assignments?{f'page={page}&' if page is not None else ''}{f'size={pageSize}&' if pageSize is not None else ''}{f'orderBy={orderBy}&' if orderBy is not None else ''}"
            url = url[:-1] # Remove the "?" at the end of the url
            resp = self._http.request(type="get",
                               url=url)

            data = resp.json()["data"]
            if len(data) == 0:
                return []

            assignment = []
            for i in resp.json()["data"]:
                assignment.append(Assignment(i, self._http))
            return assignment

    def assign(self, resourceType, resourceId):
        """assigns tag to resource"""

        resp = self._http.request(type="post",
                                  url=f"https://api.contabo.com/v1/tags/{self.tagId}/assignments/{resourceType}/{resourceId}")

        if resp.status_code == 201:
            return True
        return False


