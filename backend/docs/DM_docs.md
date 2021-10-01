# API DOCUMENTATION FOR THE ZURI CHAT DIRECT MESSAGING PLUGIN

## Brief
Contains all the available endpoints for the Zuri Chat DM plugin as compiled By Team Orpheus HNGi8.

These are REST APIs written in Python using the Django RESTFramework.

Each endpoint is triggered using HTTP verbs and accepts or returns a JSON formatted payload

## Base URL
```
https://dm.zuri.chat/
```


## ENDPOINTS
---
## Ping

**Method: GET**

``Description: Makes a simple call to the server to determine a valid connection``

URL:
```
https://dm.zuri.chat/api/v1/ping
```


Response Examples:

*Success*
```
{
    "status": 200,
    "server": true
}
```
*Server Error*
```
{
    "status": 500,
    "server": False
}
```

---
## Room Endpoints
---  

## Create Room

**Method: POST**

``Description: Creates a new room between users``

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/room
```

Request Body:

```
{
    "org_id": "614e8de3f068e4d7fc31a74e",
    "room_user_ids": [
        "614e8de3f31a74e068e40qbr",
        "614e8de3f31d74e0w8e4d7fc"
    ],
    "bookmarks": [
        "string"
    ],
    "pinned": [
        "string"
    ]
}
```

Response Example:

*If room already exists between users the Id is returned*
```
{
    "status": 200,
    "room_id": "614e74e0c8de3f31a68e4d7f"
}
```

*If no room exists between the users a new room is created and the Id returned*
```
{
    "status": 201,
    "room_id": "614e74e08de3f31a68e4d7fc"
}
```
*Request Error*
```
{
    "status": 400,
    "message": Bad Request
}
```


## User Rooms

**Method: GET**

``Description: Retrieves all rooms linked to a user``

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/users/{user_id}/rooms
```
Response Examples:

*Success; returns the rooms available to the user*
```
{
    "status": 200,
    "_id": "61547acc51ca7587f0874785",
    "bookmarks": [
        "string"
    ],
    "created_at": "2021-09-29T14:40:06.514062Z",
    "org_id": "614679ee13c00bcb7a5607b1",
    "pinned": [
        "string"
    ],
    "room_user_ids": [
        "6146fa4a04d10e99845b436e",
        "61467e13c00bcc181a5607b1"
    ]
}
```

*If no room exists for that user*
```
{
    "status": 204,
    "message": "No rooms available"
}
```

*Request Error; if a wrong method was used*
```
{
    "status": 400,
    "message": Bad Request
}
```

## Room Info

**Method: GET**

``Description: Retrieves all the information about a room``

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/rooms/{room_id}/info
```

Response Examples:

*Success; returns the information about a room*
```
{
    "room_id": "614e160068e4d2e26f31a74e",
    "org_id": "614679e3c00bcb7e1a5607b1",
    "room_user_ids": [
        "61467e5fc00bcc41a5607b13",
        "61467e13c00bcc181a5607b1"
    ],
    "created_at": "",
    "description": "This room contains the coversation between 61467e5fc00bcc41a5607b13  and 61467e13c00bcc181a5607b1 only",
    "Number of users": "2"
}
```

*Error response; if such room does not exist*
```
{
    "status": 404,
    "message": "No such Room"
}
```

*Request Error*
```
{
    "status": 400,
    "message": Bad Request
}
```
---
## Direct Messaging Endpoints
---
## Send Message

**Method: POST**

``Description: Sends messages to users in a room``

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/rooms/{room_id}/messages
```
Request Body:

*Required Fields: **sender_id**, **room_id**, **message***
```
{
  "sender_id": "61467e5fc00bcc41a5607b13",
  "room_id": "61467e13c00bcc181a5607b1",
  "message": "This is a test Example",
  "media": [],
  "read": false,
  "pinned": false,
  "saved_by": [
    "string"
  ],
  "threads": [
    {
      "message_id": "string",
      "sender_id": "string",
      "message": "string",
      "media": [],
      "created_at": "2021-09-30T11:23:55.065Z"
    }
  ],
  "reactions": [
    {
      "message_id": "string",
      "sender_id": "string",
      "data": "string",
      "category": "string",
      "aliases": [
        "string"
      ],
      "count": 0,
      "created_at": "2021-09-30T11:23:55.065Z"
    }
  ],
  "created_at": "2021-09-30T11:23:55.065Z"
}
```

Response Examples:

*Message success response*
```
{
    "status": 201,
    "event": "message_create",
    "message_id": "6155a0ee7f31a92765a1ecab",
    "room_id": "614e160e068e4d2e26f31a74",
    "thread": false,
    "data": {
        "sender_id": "61467e181a500cc6b07b13c1",
        "message": "Test example",
        "created_at": "2021-09-30T11:23:55.065000Z"
}
```

*Error response; if sender not in the room*
```
{
    "status": 400,
    "message": "sender not in room"
}
```

*Error response; if room does not exist*
```
{
    "status": 400,
    "message": "room not found"
}
```

*Request Error*
```
{
    "status": 400,
    "message": Bad Request
}
```

*Error response; if message was not sent*
```
{
    "status": 424,
    "message": "message not saved and not sent"
}
```

*Error response; if centrifugo connection fails*
```
{
    "status": 424,
    "message": "centrifugo server not available"
}
```

## Get Message

**Method: GET**

``Description: Retrieves all messages in a room``

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/rooms/{room_id}/messages
```
Response Examples:

*Success response*
```
{
    "status": 200,
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "created_at": "2021-09-30T11:23:55.065000Z",
            "media": [],
            "message": "Test example",
            "pinned": false,
            "reactions": [
                {
                    "aliases": [
                        "string"
                    ],
                    "category": "string",
                    "count": 0,
                    "created_at": "2021-09-30T11:23:55.065000Z",
                    "data": "string",
                    "message_id": "string",
                    "sender_id": "string"
                }
            ],
            "read": false,
            "room_id": "614e160068e4d2e26f31a74e",
            "saved_by": [
                "string"
            ],
            "sender_id": "61467e181c00bcc1a5607b13",
            "threads": [
                {
                    "created_at": "2021-09-30T11:23:55.065000Z",
                    "media": [],
                    "message": "string",
                    "message_id": "string",
                    "sender_id": "string"
                }
            ],
            "id": "6155a0ee7f31a92765a1ecab"
        }
    ]
}
```

*Response; if message is not in the room*
```
{
    "status": 204,
    "message": "No messages available"
}
```

*Request Error*
```
{
    "status": 400,
    "message": Bad Request
}
```

*Error response; if room does not exist*
```
{
    "status": 404,
    "message": "No such room"
}
```

## Send Thread Messages

**Method: POST**

`Description: Sends messages as threads in room`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/rooms/{room_id}/messages/{message_id}/threads
```
Request Body:

*Required Fields: **sender_id**, **message_id**, **message***
```
{
  "message_id": "6155a0e6be7f31a9275a1eca",
  "sender_id": "61467e181ab13c00bcc15607",
  "message": "Checking out the threads",
  "media": [],
  "created_at": "2021-09-30T15:41:45.685Z"
}
```

Response Examples:

*Thread message success response*
```
{
    "status": 201,
    "event": "thread_message_create",
    "thread_id": "bd830644-2205-11ec-9853-2ff0a732e3ef",
    "room_id": "614e1606f31a74e068e4d2e2",
    "message_id": "6155a0e6be7f31a9275a1eca",
    "thread": true,
    "data": {
        "sender_id": "61467e181ab13c00bcc15607",
        "message": "Checking out the threads",
        "created_at": "2021-09-30T15:41:45.685000Z"
    }
}
```

*Request Error*
```
{
    "status": 400,
    "message": Bad Request
}
```

*Error response; if sender not in the room*
```
{
    "status": 404,
    "message": "sender not in room"
}
```

*Error response; if room does not exist*
```
{
    "status": 404,
    "message": "message or room not found"
}
```

*Error response; if thread message was not sent*
```
{
    "status": 424,
    "message": "message not saved and not sent"
}
```

*Error response; if centrifugo connection fails*
```
{
    "status": 424,
    "message": "centrifugo server not available"
}
```


## Get Thread Messages

**Method: GET**

`Description: Retrieves thread messages in rooms`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/rooms/{room_id}/messages/{message_id}/threads
```

Response Examples:

*Status 200 Response*
```
[
    {
        "_id": "bd830644-2205-11ec-9853-2ff0a732e3ef",
        "created_at": "2021-09-30T15:41:45.685000Z",
        "media": [],
        "message": "message field is required",
        "sender_id": "61467e181a50bcc1607b13c0"
    },
    {
        "_id": "61fe0dc8-2205-11ec-9853-2ff0a732e3ef",
        "created_at": "2021-09-30T15:41:45.685000Z",
        "media": [],
        "message": "Checking out the threads",
        "sender_id": "61467e181a50bcc1607b13c0"
    }
]
```

*Request Error*
```
{
    "status": 400,
    "message": Bad Request
}
```

*Error response*
```
{
    "status": 404,
    "message": "message not found"
}
```

*Error response; if room does not exist*
```
{
    "status": 404,
    "message": "room not found"
}
```

## Update Thread Messages

**Method: PUT**

`Description: Edits a thread message in a room`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/rooms/{room_id}/messages/{message_id}/threads/{message_uuid}
```

Request Body:
```
{
    "sender_id": "61467e13c00bcc181a5607b1",
    "message_id": "6155a0e7f365e1a927a1ecab",
    "message": "thread message edit"
}
```

Response Examples:

*Thread message edit response*
```
{
    "status": 201,
    "event": "thread_message_update",
    "thread_id": "61fe0dc8-2205-11ec-9853-2ff0a732e3ef",
    "room_id": "614e1606f31ae4d2e274e068",
    "message_id": "614e1606f374e061ae4d2e28",
    "thread": True,
    "data": {
        "sender_id": "61467e181a50bcc1607b13c0",
        "message": "thread message edit",
        "created_at": "2021-09-30T15:41:45.685000Z",
    },
    "edited": True,
}
```

*Request Error*
```
{
    "status": 400,
    "message": Bad Request
}
```

*Error response; if Id invalid*
```
{
    "status": 400,
    "message": "Sender_id or message_id invalid"
}
```

*Error response; if room, message or thread does not exist*
```
{
    "status": 404,
    "message": "room, message or thread message not found"
}
```

*Error response; if thread message was not updated*
```
{
    "status": 424,
    "message": "message not updated"
}
```

*Error response; if centrifugo connection fails*
```
{
    "status": 424,
    "message": "centrifugo server not available"
}
```


## Delete Message

**Method: DELETE**

`Description: Deletes messages in rooms`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/rooms/{room_id}/messages/{message_id}/message
```

Response Examples:

*Success*
```
{
    "status": 200,
    "message": OK
}
```

*Request Error*
```
{
    "status": 400,
    "message": Bad Request
}
```

*Error response*
```
{
    "status": 404,
    "message": "message not found"
}
```


## Search Messages

**Method: GET**

`Description: Searches through messages in a room using keyword query params`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/users/{user_id}/messages/search?keyword=required
```

Response Example:

*Success: status 200*
```
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "_id": "61fe0dc8-2205-11ec-9853-2ff0a732e3ef",
            "created_at": "2021-09-30T15:41:45.685000Z",
            "media": [],
            "message": "This field is required.",
            "sender_id": "61467e181a5607b13c00bcc1",
            "room_id": "614e1e068e4d606f31a742e2",
            "message_id": "6155f31a9a0e65a1ecabe727",
            "thread": true
        },
        {
            "_id": "bd830644-2205-11ec-9853-2ff0a732e3ef",
            "created_at": "2021-09-30T15:41:45.685000Z",
            "media": [],
            "message": "message field is required",
            "sender_id": "61467e181a5607b13c00bcc1",
            "room_id": "614e1e068e4d606f31a742e2",
            "message_id": "6155f31a9a0e65a1ecabe727",
            "thread": true
        }
    ]
}
```

*Error Response*
```
{
    "status": 404,
    "message": "user not in any DM room"
}
```


## Mark or Unmark Messages

**Method: PUT**

`Description: Marks a message as read or unread`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/messages/{message_id}/read
```

Response Examples:

*Success; Read*
```
{
    "status": 200,
    "read": true
}
```

*Success; Unread*
```
{
    "status": 200,
    "read": False
}
```

*Request Error*
```
{
    "status": 400,
    "message": Bad Request
}
```

*Server Error*
```
{
    "status": 503,
    "message": "Service unavailable"
}
```

## Pin or Unpin Messages

**Method: PUT**

`Description: Pins and unpins messages in rooms`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/messages/{message_id}/pin
```

Response Examples:

*Success; Pinned*
```
{
    "status": 201
    "message_id": "6155a0e6be7f31a9275a1eca",
    "pinned": [6155a0e6be7f31a9275a1eca],
    "Event": "pin_message"
}
```

*Success; Unpinned*
```
{
    "status": 201
    "message_id": "6155a0e6be7f31a9275a1eca",
    "pinned": [],
    "Event": "unpin_message"
}
```

*Error response*
```
{
    "status": 404,
    "message": "message not found"
}
```

*Server Error*
```
{
    "status": 503,
    "message": "Service unavailable"
}
```


## Schedule Messages

**Method: POST**

`Description: Schedules messages in rooms`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/rooms/{room_id}/schedule-message
```

Request Body:
```
{
    "sender_id": "614e1606f31a74e068e4d2e2",
    "room_id": "611a744d24e16e068e06f3e2",
    "message": "tomorrow is independence day",
    "timer": "2021-09-30T22:18:57.476Z"
}
```

Response Examples:

*Success*
```
{
    "status": 201,
    "message": "Message Scheduled"
}
```

*Error Response*
```
{
    "status": 400,
    "message": "Bad Request"
}
```


## Message Reactions

**Method: POST**

`Description: Creates new message emoji reactions`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/rooms/{room_id}/messages/{message_id}/reactions
```

Request Body:
```
{
  "message_id": "6155a0e6be7f31a9275a1eca",
  "sender_id": "6155a0e9276be7f31a5a1eca",
  "data": "string",
  "category": "string",
  "aliases": [
    "string"
  ],
  "count": 0,
  "created_at": "2021-09-30T18:59:48.088Z"
}
```

Response Examples:

*Success; 201 created response*
```
{
    "status": "success",
    "event": "add_message_reaction",
    "reaction_id": "f82283bc-2221-11ec-9853-2ff0a732e3ef",
    "room_id": "614e16064f8ed2e231a74e06",
    "message_id": "6155a0e65a1f31a927ecabe7",
    "data": {
        "sender_id": "61467ec00bcc181a5607b131",
        "reaction": "string",
        "created_at": "2021-09-30T18:59:48.088000Z"
    }
}
```

*Error Response*
```
{
    "status": 404,
    "message": "message or room not found"
}
```

*Error Response*
```
{
    "status": 424,
    "message": "data not sent"
}
```


## Get Message Reactions

**Method: GET**

`Description: Retrieves all the reactions to a message`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/rooms/{room_id}/messages/{message_id}/reactions
```

Response Examples:

*Success*
```
{
  "status": 200,
  "event": "get_message_reactions",
  "room_id": "614e1606f31a74e068e4d2e2",
  "message_id": "6155a0e65a1ecabe7f31a927",
  "data": {
    "reactions": [
      {
        "aliases": [
          "string"
        ],
        "category": "string",
        "count": 0,
        "created_at": "2021-09-30T11:23:55.065000Z",
        "data": "string",
        "message_id": "6a1ecabe155a0e657f31a927",
        "sender_id": "6155be7f31aa0e65a1eca927"
      }
    ]
  }
}
```

*Error Response*
```
{
    "status": 404,
    "message": "No such message or room"
}
```

*Error Response*
```
{
    "status": 424,
    "message": "Data not retrieved"
}
```

---
## Bookmarks and Links
---

## Save Bookmarks

**Method: POST**

`Description: Saves links as bookmarks in rooms`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/rooms/{room_id}/new-bookmark
```

Request Body:
```
{
  "link": "https://dm.zuri.chat/docs/v1/",
  "name": "dm plugin docs",
  "created_at": "2021-09-30T19:29:32.378Z"
}
```

Response Examples:

*Success; 200 status response*
```
{
  "link": "https://dm.zuri.chat/docs/v1/",
  "name": "dm plugin docs",
  "created_at": "2021-09-30T19:29:32.378000Z"
}
```

*Error Response*
```
{
    "status": 400,
    "message": "Bad Request"
}
```


## Get Bookmarks

**Method: GET**

`Description: Retrieves all bookmarks in rooms`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/rooms/{room_id}/bookmarks
```

Response Examples:

*Success; 200 status response*
```
{
    "name": "dm plugin docs"
}
```

*Error Response*
```
{
    "status": 400,
    "message": "Bad Request"
}
```

*Error Response*
```
{
    "status": 404,
    "message": "bookmark not found"
}
```


## Delete Bookmarks

**Method: DELETE**

`Description: Deletes bookmarks in rooms`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/rooms/{room_id}/bookmark
```

Response Examples:

*Success*
```
{
    "status": 200
}
```

*Error Response*
```
{
    "status": 400,
    "message": "Bad Request"
}
```

*Error Response*
```
{
    "status": 404,
    "message": "bookmark not found"
}
```

## Get Message Link

**Method: GET**

`Description: Retrieves the link to a message`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/messages/{message_id}/link
```

Response Examples:

*Success; status 200*
```
{
  "room_id": "6144e068e4d2ee1606f31a72",
  "message_id": "6155a1a9270eecabe65a17f3",
  "link": "https://dm.zuri.chat/getmessage/614e1068e606f34d21a74ee2/6155aecaa1f31be70e65a927"
}
```

*Error Response*
```
{
    "status": 404,
    "message": "message not found"
}
```


## Get Links

**Method: GET**

`Description: Retrieves all links in a room`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/rooms/{room_id}/links
```

Response Examples:

*Success; status 200*
```
{
  "links": ["https://dm.zuri.chat/getmessage/614e1068e606f34d21a74ee2/6155aecaa1f31be70e65a927",
            "https://dm.zuri.chat/docs/v1/"],
  "room_id": "614e1606f31a74e068e4d2e2"
}
```

*Error Response*
```
{
    "status": 404,
    "message": "message not found"
}
```

---
## Message Media
---

## Send Files

**Method: POST**

`Description: Sends media files in rooms (authorization is required)`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/rooms/{room_id}/messagemedia
```

Request Body: *to be entered as a form data*
```
{
    "file": "file.jpg"
}
```

Response Examples:

*Success*
```
{
    "status": 201,
    "media_url": "https://api.zuri.chat/files/message_media/614679ee1abcb75607b13c00/61467e18000bcc7b13c11a56/20210928143839_0.jpg"
}
```

*No content*
```
{
    "status": 204,
    "message": "No file attached, Use send Message api to send only a message"
}
```

*Error Response: Bad Request*
```
{
    "status": 400,
    "message": "sender not in room"
}
```

*Error Response*
```
{
    "status": 404,
    "message": "room not found"
}
```

*Error Response*
```
{
    "status": 424,
    "message": "data not sent"
}
```

---
## Members
---

## Get Organization Members

**Method: GET**

D`escription: Retrieves all members in an organization (requires authorization)`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/members
```

Response Examples:

*Success; status 200*
```
{
    "status": 200,
    "message": "Members retrieved successfully",
    "data": [
        {
            "_id": "61467e18100bcc1a5607b13c",
            "bio": "",
            "deleted": false,
            "deleted_at": "0001-01-01T00:53:28+00:53",
            "display_name": "",
            "email": "tedfelasvetest@gmail.com",
            "files": null,
            "first_name": "",
            "image_url": "https://api.zuri.chat/files/profile_image/614679ee1a5607b13c00bcb7/61467e181a5607b13c00bcc1/20210928143839_0.jpg",
            "joined_at": "2021-09-19T02:02:32.935+02:00",
            "last_name": "",
            "org_id": "61467b13c00bcb79ee1a5607",
            "phone": "",
            "presence": "true",
            "pronouns": "",
            "role": "owner",
            "settings": {
                "messages_and_media": {
                    "additional_options": null,
                    "bringemailsintozuri": "",
                    "convert_emoticons_to_emoji": false,
                    "custom": false,
                    "emoji": "",
                    "emoji_as_text": false,
                    "frequently_used_emoji": false,
                    "inline_media_and_links": null,
                    "messages_one_click_reaction": null,
                    "names": "",
                    "show_jumbomoji": false,
                    "theme": ""
                },
                "notifications": {
                    "channel_hurdle_notification": false,
                    "email_notifications_for_mentions_and_dm": null,
                    "message_preview_in_each_notification": false,
                    "mute_all_sounds": false,
                    "my_keywords": "",
                    "notification_schedule": "",
                    "notify_me_about": "",
                    "thread_replies_notification": false,
                    "use_different_settings_mobile": "",
                    "when_iam_not_active_on_desktop": ""
                },
                "sidebar": {
                    "always_show_in_the_sidebar": null,
                    "list_private_channels_seperately": false,
                    "organize_external_conversations": false,
                    "show_conversations": "",
                    "show_profile_picture_next_to_dm": false,
                    "sidebar_sort": ""
                },
                "themes": {
                    "colors": "",
                    "themes": ""
                }
            },
            "socials": null,
            "status": "",
            "time_zone": "",
            "user_name": "tedfelasvetest"
        },
```

*Error Response*
```
{
    "status": 400,
    "message": "Bad Request"
}
```

*Error Response*
```
{
    "status": 401,
    "message": "Unauthorized Access"
}
```


## Get User Profile Details

**Method: GET**

`Description: Retrieves the user details of a member in an organization (requires authorization)`

URL:
```
https://dm.zuri.chat/api/v1/org/{org_id}/members/{member_id}/profile
```

Response Examples:

*Success; status 200*
```
{
    "bio": "Medic and Tech Intern at HNGi8",
    "display_name": "Mykie88",
    "first_name": "Michael",
    "last_name": "Rowland",
    "user_name": "Mykie88",
    "image_url": "https://api.zuri.chat/files/profile_image/614679ee1a5607b13c00bcb7/61467e181a5607b13c00bcc1/20210928143839_0.jpg",
    "phone": "2348012345678",
    "pronouns": "He/Him/We/Us",
    "status": "exhausted olohun"
}
```

*Error Response*
```
{
    "status": 400,
    "message": "Bad Request"
}
```

*Error Response*
```
{
    "status": 401,
    "message": "Unauthorized Access"
}
```
