import React, { useEffect } from "react";
import DmProfileHeader from "../components/dmProfileHeader";
import BookmarkHeader from "../components/common/addBookmarkKebab/dmBookMark";
import DmChatContainerBox from "../components/ChatContainer/dmChatContainerBox";
import InputBoxField from "../components/dmBoxInputField";
import PinnedMessage from "../components/common/pinnedMessage/dmPinnedMessages";

// Chat Home Page
const ChatHome = () => {
  return (
    <div className="dm-newchat-room position-relative w-100 d-flex flex-column">
      <div className="dm-chatroom-header">
        <DmProfileHeader />
        <div className=" dm-bookmark-head">
          <div className="add-bookmark gap-2 d-flex flex-direction-column flex-flow align-items-center px-3 py-1">
            <PinnedMessage amount={3} />
            <BookmarkHeader />
          </div>
        </div>
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
