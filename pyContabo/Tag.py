
class Secret:

    def __init__(self, json, _http):

        self._http = _http

        self.tenantId = json["tenantId"]
        self.customerId = json["customerId"]
        self.tagId = json["tagId"]
        self.name = json["name"]
        self.color = json["color"]

        self.rawJson = json

    def update(self, name: str, color: str):
        """updates the name and the value of the secret"""

        resp = self._http.request(type="patch",
                                  url=f"https://api.contabo.com/v1/tags/{self.tagId}",
                                  data={"name": name, "color": color})

        if resp.status_code == 200:
            return True
        return False

    def delete(self):
        """deletes the secret"""

        resp = self._http.request(type="delete",
                             url=f"https://api.contabo.com/v1/tags/{self.tagId}")

        if resp.status_code == 204:
            return True
        return False