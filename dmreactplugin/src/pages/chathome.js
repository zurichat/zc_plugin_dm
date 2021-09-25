import React from "react";
import EmojiPicker from "../components/common/dmEmojiComp/dmEmojiComp";
import DmInputTextField from "../components/common/dmInputTextField/dmInputTextField";
import DmFullProfile from "../components/DmFullProfile/DmFullProfile";

const ChatHome = () => {
  return (
    <div className="chat-home">
      <DmFullProfile />
      <DmInputTextField/>
    </div>
  );
};

export default ChatHome;
