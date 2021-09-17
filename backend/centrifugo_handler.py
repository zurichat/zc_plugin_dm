import requests
from typing import Any, Dict
from requests.exceptions import RequestException

# CENTRIFUGO settings
CENTRIFUGO_HOST = "https://realtime.zuri.chat/api"
CENTRIFUGO_API_TOKEN = "58c2400b-831d-411d-8fe8-31b6e337738b"


class CentrifugoHandler:
    """
    Class to establish communication with Centrifugo server
    """

    def __init__(
        self,
    ) -> None:
        self.address = CENTRIFUGO_HOST
        self.api_key = CENTRIFUGO_API_TOKEN

        self.headers = {
            "Content-type": "application/json",
            "Authorization": "apikey " + self.api_key,
        }

    def _send_command(self, data: Dict[int, Any]) -> Dict[int, Any]:
        """[summary]

        Args:
            data (Dict[int, Any]): [description]

        Raises:
            RequestException: [description]

        Returns:
            Dict[int, Any]: [description]
        """
       
        try:
            response = requests.post(url=self.address, headers=self.headers, json=data)
        except requests.RequestException as error:
            raise RequestException(error)
        stat = {"status_code": response.status_code, "message": response.json()}

        return {"status_code": response.status_code, "message": response.json()}

    def publish(self, room: str, data: Dict[str, str], skip_history=False):
        """Publish a message to a Centrifugo channel

        Args:
            room (str): [description]
            data (Dict[str, str]): [description]
            skip_history (bool, optional): [description]. Defaults to False.

        Returns:
            [type]: [description]
        """
        command = {"method": "publish", "params": {"channel": room, "data": data}}

        return self._send_command(command)


centrifugo_client = CentrifugoHandler()
