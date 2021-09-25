// Import all API endpoints
import APIService from "../../utils/apiServices";

// import all action types
import {
  GET_MEMBERS,
  CREATE_ROOM,
  GET_ROOMS,
  GET_SOCKETS,
  GET_MESSAGES,
  SEND_MESSAGE,
  GET_PINNED_MESSAGE,
  PIN_MESSAGE,
  GET_MESSAGE,
  MESSAGE_REACTION,
  GET_ROOM_MESSAGES,
  UNPIN_MESSAGE,
  GET_BOOKMARKS,
  ADD_TO_BOOKMARK,
} from "./actionTypes";

// Get Organization Members
const handleGetMembers = (org_id) => async (dispatch) => {
  try {
    const res = await APIService.getOrgUsers(org_id);

    dispatch({ type: GET_MEMBERS, payload: res.data.data });
  } catch (error) {
    console.log(error);
  }
};

const createDmRoom = (org_id, user1_id, user2_id) => async (dispatch) => {
  try {
    const res = await APIService.createChatRoom(org_id, {
      data: {
        org_id: org_id,
        room_user_ids: [user1_id, user2_id],
        bookmark: ["string"],
        pinned: ["string"],
      },
    });

    dispatch({ type: CREATE_ROOM, payload: res.data.data });
  } catch (error) {
    console.log(error);
  }
};

const getRoomInfo = (org_id) => async (dispatch) => {
  try {
    const res = await APIService.getRoomInfo(org_id);

    dispatch({
      type: GET_ROOMS,
      payload: res.data.data,
    });
  } catch (error) {
    console.log(error);
  }
};

const handleGetRoomMessages = () => async (dispatch) => {
  try {
    const res = await APIService.getRoomMessages(org_id, room_id);

    dispatch({
      type: GET_ROOM_MESSAGES,
      payload: res.data.data,
    });
  } catch (error) {
    console.log(error);
  }
};

const handlePostRoomMessage = () => async (dispatch) => {
  try {
    const res = await APIService.postRoomMessage(org_id, room_id, sender_id, {
      data: {
        sender_id: sender_id,
        room_id: room_id,
        message: ["string"],
      },
    });

    dispatch({
      type: SEND_MESSAGE,
      payload: res.data.data,
    });
  } catch (error) {
    console.log(error);
  }
};

const handleSingleMessage = () => async (dispatch) => {
  try {
    const res = await APIService.getSingleMessage(room_id, message_id);

    dispatch({
      type: GET_MESSAGE,
      payload: res.data.data,
    });
  } catch (error) {
    console.log(error);
  }
};

const handleGetPinnedMessage = () => async (dispatch) => {
  try {
    const res = await APIService.getPinnedMessages(org_id, room_id);

    dispatch({
      type: GET_PINNED_MESSAGE,
      payload: res.data.data,
    });
  } catch (error) {
    console.log(error);
  }
};

const handlePinMessage = () => async (dispatch) => {
  try {
    const res = await APIService.pinMessage(org_id, message_id, {
      data: { org_id: org_id, pinned: ["string"] },
    });
    dispatch({
      type: PIN_MESSAGE,
      payload: res.data.data,
    });
  } catch (error) {
    console.log(error);
  }
};

const handleGetMessageReaction = () => async (dispatch) => {
  try {
    const res = await APIService.getMessageReactions(
      org_id,
      room_id,
      message_id
    );

    dispatch({
      type: MESSAGE_REACTION,
      payload: res.data.data,
    });
  } catch (error) {
    console.log(error);
  }
};

const handleUnPinMessage = () => async (dispatch) => {
  try {
    const res = await APIService.unPinMessage(org_id, message_id);

    dispatch({
      type: UNPIN_MESSAGE,
      payload: res.data.data,
    });
  } catch (error) {
    console.log(error);
  }
};

const handleGetBookmarks = () => async (dispatch) => {
  try {
    const res = await APIService.getAllBookmarks(org_id, room_id);

    dispatch({
      type: GET_BOOKMARKS,
      payload: res.data.data,
    });
  } catch (error) {
    console.log(error);
  }
};

const addToBookmark = () => async (dispatch) => {
  try {
    const res = APIService.addToBookmark(org_id, room_id, {
      data: {
        link: link(url),
        name: "string",
      },
    });
    dispatch({
      type: ADD_TO_BOOKMARK,
      payload: res.data.data,
    });
  } catch (error) {
    console.log(error);
  }
};

const appActions = {
  handleGetMembers,
  createDmRoom,
  getRoomInfo,
  handleGetRoomMessages,
  handleGetMembers,
  handleGetMessageReaction,
  handleGetPinnedMessage,
  handleGetBookmarks,
  addToBookmark,
  handleUnPinMessage,
  handlePinMessage,
  handleSingleMessage,
  handlePostRoomMessage,
};

export default appActions;
