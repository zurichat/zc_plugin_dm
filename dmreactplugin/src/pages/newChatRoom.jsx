import React, { useEffect } from "react";
import DmProfileHeader from "../components/dmProfileHeader";
import BookmarkHeader from "../components/common/addBookmarkKebab/dmBookMark";
import DmChatContainerBox from "../components/ChatContainer/dmChatContainerBox";
import axios from "axios";
import { useLocation } from "react-router-dom";

// Chat Home Page
const ChatHome = () => {
  const location = useLocation();
  const getRoomDetails = (orgId, roomId) => {
    const baseUrl = `https://dm.zuri.chat/api/v1/${orgId}/${roomId}/messages`;

    axios
      .get(baseUrl)
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => {
        console.error("Error", err);
      });
  };

  useEffect(() => {
    const ids = location.pathname.split("/");
    const org_id = ids[1];
    const room_id = ids[2];

    console.log("These are the room IDs", ids);
    getRoomDetails(org_id, room_id);
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

export default ChatHome;
