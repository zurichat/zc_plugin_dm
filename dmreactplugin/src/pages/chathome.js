import React from "react";
import DmFullProfile from "../components/DmFullProfile/DmFullProfile";
import ChatHomeMessages from "./ChatHomeMessages";

const ChatHome = () => {
  return (
    <div className="chat-home">
      <ChatHomeMessages />

      {/* <DmFullProfile /> */}
    </div>
  );
};

export default ChatHome;
