import React from "react";
import DmFullProfile from "../components/DmFullProfile/DmFullProfile";
import ThreeDotKebab from "../components/common/threeDotKebabMenu/threeDotKebab";

const ChatHome = () => {
  return (
    <div className="chat-home">
      <DmFullProfile />
      <ThreeDotKebab />
    </div>
  );
};

export default ChatHome;
