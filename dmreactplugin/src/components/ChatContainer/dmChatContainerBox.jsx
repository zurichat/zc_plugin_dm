import React, { useState } from "react";
import { useSelector } from "react-redux";
import MessageWrapper from "../common/dmHoverState/dmHoverstate";
import DmInitMessageBox from "../dmInitMessagebox";
import DmSingleMessageContainer from "../dmSingleMessageContainer";
import DmReplyInThread from "../ReplyInThread/replyInThread";

import "./chatContainerBox.css";

const DmChatContainerBox = ({ user2_id }) => {
  const { room_messages } = useSelector(({ roomsReducer }) => roomsReducer);
  const [openThread, setOpenThread] = useState(false);

  const handleOpenThread = () => {
    setOpenThread(true);
  };

  const handleCloseThread = () => {
    setOpenThread(false);
  };

  return (
    <>
      <div className="dm-chatContainerBox w-100 d-flex align-items-end">
        <main>
          <DmInitMessageBox />

          {room_messages?.results ? (
            room_messages?.results?.map((messages) => (
              <div key={messages?.id}>
                <MessageWrapper handleOpenThread={handleOpenThread}>
                  <DmSingleMessageContainer
                    messages={messages}
                    user2_id={user2_id}
                  />
                </MessageWrapper>
              </div>
            ))
          ) : (
            <h4>There are no messages here, Start a conversation</h4>
          )}
        </main>
        <aside className={`asideContent ${openThread ? "active" : ""}`}>
          <DmReplyInThread handleCloseThread={handleCloseThread} />
        </aside>
      </div>
    </>
  );
};

export default DmChatContainerBox;
