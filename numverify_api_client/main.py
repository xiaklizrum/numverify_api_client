import json
import http.client


class Client:
    "API Client class"

    def __init__(self, access_key: str):
        self.ACCESS_KEY = access_key
        self.HOST = "apilayer.net"
        self.URL = "/api/validate"
        self.URI_PARAMS = "?access_key={}&number={}&country_code={}&format={}"

    def get_info(
        self, phone_number: str, country_code: str = "", _format: int = 1
    ) -> dict:
        "Get information about phone number"
        uri = self.URI_PARAMS.format(
            self.ACCESS_KEY, phone_number, country_code, _format
        )
        return self._get_content_by_url(self.URL + uri)

    def _get_content_by_url(self, url: str) -> dict:
        "Request and response processing"
        headers = {
            "User-Agent": (
                "Mozilla/5.0"
                "(X11; U; Linux x86_64; en-US; rv:1.9.1b3pre)"
                "Gecko/20090109 Shiretoko/3.1b3pre"
            )
        }
        connection = http.client.HTTPConnection(self.HOST)
        connection.request("GET", url, "", headers)
        response = connection.getresponse()

        if response.status == 200:
            body = json.loads(response.read())
        else:
            raise Exception(
                "Error: {}, Code: {}".format(
                    body["error"]["info"], body["error"]["code"]
                )
            )

        if "success" in body and body["success"] == False:
            raise Exception(
                "Error: {}, Code: {}".format(
                    body["error"]["info"], body["error"]["code"]
                )
            )
        else:
            return body
