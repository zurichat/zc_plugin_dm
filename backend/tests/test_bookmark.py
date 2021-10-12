
from unittest.mock import patch

from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


class BookmarkEndpointTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch("backend.booklinks.DataStorage.read")
    @patch("backend.booklinks.DataStorage.update")
    @patch("backend.booklinks.centrifugo_client.publish")
    def test_save_bookmark_endpoint(self, mock_publish, mock_update, mock_read):
        """Test saving a new bookmark to a room or updating an existing one"""

        payload = {
            "link": "https://google.com",
            "name": "Google"
        }

        mock_read.return_value = {"bookmarks": [{"link":"www.google.com", "name": "Google"}]}
        mock_update.return_value = {"status": 200}
        mock_publish.return_value = {"status_code": 200}

        response = self.client.post(
            reverse("create_bookmark",
                    kwargs={
                        "org_id": "614679ee1a5607b13c00bcb7",
                        "room_id": "6150e4fc05c9716b90f33f33"
                    }
                ),
            data=payload)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)
        self.assertTrue(response.data["event"] == "bookmark_create")

    @patch("backend.booklinks.DataStorage.read")
    def test_save_bookmark_on_server_down(self, mock_read):
        """Test saving a new bookmark to a room when server is down"""

        payload = {
            "link": "https://google.com",
            "name": "Google"
        }

        mock_read.return_value = None

        response = self.client.post(
            reverse("create_bookmark",
                    kwargs={
                        "org_id": "614679ee1a5607b13c00bcb7",
                        "room_id": "6150e4fc05c9716b90f33f33"
                    }
                ),
            data=payload)
        
        self.assertEqual(response.status_code, 503)
        self.assertTrue(response.data == None)
