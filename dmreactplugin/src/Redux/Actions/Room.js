import axios from "axios";
import { Base_Url } from "./Members";

export const CREATE_ROOM = "CREATE_ROOM";
export const GET_ROOMS = "GET_ROOMS";
export const GET_ROOM_MESSAGES = "GET_ROOM_MESSAGES";

// Creating a room
export const createRoom = (roomId) => ({
  type: CREATE_ROOM,
  payload: roomId,
});

export const handleCreateRoom =
  (user1Id, user2Id, org_id) => async (dispatch) => {
    try {
      const roomId = await axios.post(`${Base_Url}/${org_id}/createroom`, {
        data: {
          org_id: org_id,
          room_user_ids: [user1Id, user2Id],
          bookmarks: ["string"],
          pinned: ["string"],
        },
      });
      await dispatch(createRoom(roomId));
    } catch (error) {
      console.log(`Error from createRoom: ${error}`);
    }
  };

//   Get Rooms
//   This is used to retrieve all rooms a user is currently active in.
// if there is no room for the user_id it returns a 204 status.

export const getRooms = (rooms) => ({
  type: GET_ROOMS,
  payload: rooms,
});

export const handleGetRooms = (org_id, user_Id) => async (dispatch) => {
  try {
    const rooms = await axios.get(`${Base_Url}/${org_id}/${user_Id}/rooms`);
    dispatch(getRooms(rooms));
  } catch (error) {
    console.log(`Error from getRooms: ${error}`);
  }
};

/*
// Get room messages
This is used to retrieve messages in a room.
It returns a 204 status code if there is no message in the room.
The messages can be filter by adding date in the query,
it also returns a 204 status if there is no messages.
*/

export const getRoomMessages = (messages) => ({
  type: GET_ROOM_MESSAGES,
  payload: messages,
});

export const handleGetRoomMessages = (org_id, roomId) => async (dispatch) => {
  try {
    const messages = await axios.get(
      `${Base_Url}/${org_id}/${roomId}/messages`
    );
    dispatch(getRoomMessages(messages));
  } catch (error) {
    console.log(`Error from getRoomMessages: ${error}`);
  }
};
