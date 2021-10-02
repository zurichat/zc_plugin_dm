import React, { useState } from "react";
import { useSelector } from "react-redux";
import MessageWrapper from "../common/dmHoverState/dmHoverstate";
import DmInitMessageBox from "../dmInitMessagebox";
import DmSingleMessageContainer from "../dmSingleMessageContainer";
import DmReplyInThread from "../ReplyInThread/replyInThread";
import { RiArrowDownSLine } from "react-icons/ri";
import centrifugeClient from "../../utils/centrifugoClient";

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

  const membersReducer = useSelector(({ membersReducer }) => membersReducer);

  const actualUser =
    membersReducer && membersReducer.find((member) => member._id === user2_id);

  const user = actualUser ? actualUser : null;

  centrifugeClient("6150e69005c9716b90f33f3a", (ctx) => {
    console.log("This is centrifigo " + ctx);
  });

  return (
    <>
      <div className="dm-chatContainerBox w-100 d-flex align-items-end">
        <main className="dm-chat-main-container">
          {room_messages?.results
            ? room_messages?.results
                ?.sort((first, second) => {
                  const firstDate = new Date(first.created_at);
                  const secondDate = new Date(second.created_at);
                  return secondDate - firstDate;
                })
                .map((messages) => (
                  <div key={messages?.id}>
                    <MessageWrapper
                      handleOpenThread={handleOpenThread}
                      messages={messages}
                    >
                      <DmSingleMessageContainer
                        messages={messages}
                        user2_id={user2_id}
                      />
                    </MessageWrapper>
                  </div>
                ))
            : null}
          <div className="dm-chat-main-container-sticky-date">
            <span></span>
            <RiArrowDownSLine />
          </div>
          <DmInitMessageBox secondUser={user} />
        </main>
        <aside className={`asideContent ${openThread ? "active" : ""}`}>
          <DmReplyInThread userId={user2_id} handleCloseThread={handleCloseThread} />
        </aside>
      </div>
    </>
  );
};

export default DmChatContainerBox;
