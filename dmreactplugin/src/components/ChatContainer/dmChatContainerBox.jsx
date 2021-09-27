import React, { useState } from "react";
import MessageWrapper from "../common/dmHoverState/dmHoverState";
import DmInitMessageBox from "../dmInitMessagebox";
import DmSingleMessageContainer from "../dmSingleMessageContainer";
import DmReplyInThread from "../ReplyInThread/replyInThread";
// import styled from "styled-components";
import "./chatContainerBox.css";

const DmChatContainerBox = () => {
  const [openThread, setOpenThread] = useState(false);

  const handleOpenThread = () => {
    setOpenThread(true);
  };

  const handleCloseThread = () => {
    setOpenThread(false);
  }

  return (
    <>
      <div className="chatContainerBox">
        <main>
          <DmInitMessageBox />
          {}
          <MessageWrapper handleOpenThread={handleOpenThread}>
            <DmSingleMessageContainer />
          </MessageWrapper>
          <MessageWrapper handleOpenThread={handleOpenThread}>
            <DmSingleMessageContainer />
          </MessageWrapper>
        </main>
        <aside className={`asideContent ${openThread ? 'active' : ''}`}>
          <DmReplyInThread handleCloseThread={handleCloseThread} />
        </aside>
      </div>
    </>
  );
};

export default DmChatContainerBox;
