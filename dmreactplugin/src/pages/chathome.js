import React from "react";
import EmojiPicker from "../components/common/dmEmojiComp/dmEmojiComp";
import DmInputTextField from "../components/common/dmInputTextField/dmInputTextField";
import DmFullProfile from "../components/DmFullProfile/DmFullProfile";
import ThreeDotKebab from "../components/common/threeDotKebabMenu/threeDotKebab";

const ChatHome = () => {
  return (
    <div className="chat-home">
      <DmFullProfile />
      <DmInputTextField/>
      {/* This is the Popup menu for the threeDotKebab from the hover state */}
      <ThreeDotKebab />
    </div>
  );
};

export default ChatHome;