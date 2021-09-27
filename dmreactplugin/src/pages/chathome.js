import React from "react";
import ThreeDotKebab from "../components/common/threeDotKebabMenu/threeDotKebab";
import DmFullProfile from "../components/DmFullProfile/DmFullProfile";

const ChatHome = () => {
  return (
    <div className="chat-home">
      <DmFullProfile />
      {/* This is the popup menu for the threeDotKebab hover state component */}
      <ThreeDotKebab />
    </div>
  );
};

export default ChatHome;
