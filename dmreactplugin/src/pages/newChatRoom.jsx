import React, { useEffect } from "react";
import DmProfileHeader from "../components/dmProfileHeader";
import BookmarkHeader from "../components/common/addBookmarkKebab/dmBookMark";
import DmChatContainerBox from "../components/ChatContainer/dmChatContainerBox";
import InputBoxField from "../components/dmBoxInputField";
import { useDispatch } from "react-redux";
import {
  handleGetRoomInfo,
  handleGetRoomMessages,
} from "../Redux/Actions/dmActions";
import { useSelector } from "react-redux";

// Chat Home Page
const ChatHome = ({ org_id, loggedInUser_id, room_id }) => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(handleGetRoomMessages(org_id, room_id));
    dispatch(handleGetRoomInfo(org_id, room_id));
  }, [dispatch, org_id, loggedInUser_id, room_id]);

  return (
    <div className="dm-newchat-room position-relative w-100 d-flex flex-column">
      <div className="dm-chatroom-header">
        <DmProfileHeader />
        <BookmarkHeader />
      </div>
      <div className="dm-message-in-out-box w-100 position-relative row align-items-end">
        <DmChatContainerBox />
      </div>
      <div className="dm-footer-input-field w-100 position-relative">
        <InputBoxField />
      </div>
    </div>
  );
};
export default ChatHome;

/*


import React, { useEffect } from "react";
import DmProfileHeader from "../components/dmProfileHeader";
import BookmarkHeader from "../components/common/addBookmarkKebab/dmBookMark";
import DmChatContainerBox from "../components/dmChatContainerBox";
import { useDispatch } from "react-redux";
import {
  handleGetRoomInfo,
  handleGetRoomMessages,
} from "../Redux/Actions/dmActions";
import { useSelector } from "react-redux";

// Chat Home Page
const ChatHome = () => {
  const dispatch = useDispatch();
  const roomsReducer = useSelector(({ roomsReducer }) => roomsReducer);

  // const { org_id } = props?.match?.params;

  const room_id =
    roomsReducer?.room_ids?.room_id && roomsReducer?.room_ids?.room_id;

  useEffect(() => {
    dispatch(
      handleGetRoomMessages(
        "614679ee1a5607b13c00bcb7",
        "6150e69005c9716b90f33f3a"
      )
    );
    dispatch(
      handleGetRoomInfo("614679ee1a5607b13c00bcb7", "6150e57405c9716b90f33f34")
    );
  }, []);

  return (
    <div className="dm-newchat-room position-relative w-100 d-flex flex-column">
      <div className="dm-chatroom-header">
        <DmProfileHeader />
        <BookmarkHeader />
      </div>

      <div className="dm-message-in-out-box w-100 position-relative">
        <DmChatContainerBox />
      </div>

      <div className="dm-footer-input-field w-100 position-relative"></div>
    </div>
  );
};


*/
