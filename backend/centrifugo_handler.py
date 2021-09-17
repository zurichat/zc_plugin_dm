import requests
from typing import Any, Dict, Optional
from requests.exceptions import RequestException

# CENTRIFUGO settings
CENTRIFUGO_HOST = "https://realtime.zuri.chat/api"
CENTRIFUGO_API_TOKEN = "58c2400b-831d-411d-8fe8-31b6e337738b"


class CentrifugoHandler:
    """A helper class to handle communication with the Centrifugo server."""

    def __init__(
        self,
    ) -> None:
        """Initialize CentrifugoHandler with `address` and `api_key` values."""
        self.address = CENTRIFUGO_HOST
        self.api_key = CENTRIFUGO_API_TOKEN

        self.headers = {
            "Content-type": "application/json",
            "Authorization": "apikey " + self.api_key,
        }

    def _send_command(self, command: Dict[int, Any]) -> Dict[int, Any]:
        """Connects to the Centrifugo server and sends command to execute via Centrifugo Server API.

            Args:
                command (Dict[int, Any]): The command to be sent to Centrifugo

            Raises:
                RequestException: There was an ambiguous exception that occurred while handling the
        request

            Returns:
                Dict[int, Any]: The response from Centrifugo after executing the command sent
        """

        try:
            response = requests.post(
                url=self.address, headers=self.headers, json=command
            )
        except requests.RequestException as error:
            raise RequestException(error)

        return {"status_code": response.status_code, "message": response.json()}

    def publish(
        self, room: str, data: Dict[str, str], skip_history=False
    ) -> Dict[int, Any]:
        """Publish data into a room.

        Args:
            room (str): The name of the room where to publish the data
            data (Dict[str, str]): Custom JSON data to publish into the room
            skip_history (bool, optional): Skip adding publication for this request. Defaults to False.

        Returns:
            Dict[int, Any]: The response from Centrifugo after executing the command sent
        """

        command = {
            "method": "publish",
            "params": {"channel": room, "data": data, "skip_history": skip_history},
        }

        return self._send_command(command)

    def unsubscribe(self, user: str, room: str, client: Optional[str] = None) -> None:
        """Unsubscribe a user from a room

        Args:
            user (str): The id of a user inside the current room
            room (str): The name of the room where to unsubscribe the user
            client (Optional[str], optional): Specific client ID to unsubscribe (user still required to be set). Defaults to None.

        Returns:
            [type]: The response from Centrifugo after executing the command sent
        """

        command = {
            "method": "unsubscribe",
            "params": {"channel": room, "user": user, "client": client},
        }

        return self._send_command(command)


# An instance of CentrifugoHandler
# This will be used when importing the class
centrifugo_client = CentrifugoHandler()
