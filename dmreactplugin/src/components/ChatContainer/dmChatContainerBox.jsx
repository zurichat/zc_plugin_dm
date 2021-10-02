import React, { useState } from 'react';
import { useSelector } from 'react-redux';
import MessageWrapper from '../common/dmHoverState/dmHoverstate';
import DmInitMessageBox from '../dmInitMessagebox';
import DmSingleMessageContainer from '../dmSingleMessageContainer';
import DmReplyInThread from '../ReplyInThread/replyInThread';

import './chatContainerBox.css';

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
  console.log('This is the userooooo' + user?.name);
  return (
    <>
      <div className='dm-chatContainerBox w-100 d-flex align-items-end'>
        <main className='dm-chat-main-container'>
          {room_messages?.results
            ? room_messages?.results
                ?.sort((first, second) => {
                  const firstDate = new Date(first.created_at);
                  const secondDate = new Date(second.created_at);
                  return secondDate - firstDate;
                })
                .map((messages) => (
                  <div key={messages?.id}>
                    <MessageWrapper handleOpenThread={handleOpenThread}>
                      <DmSingleMessageContainer
                        messages={messages}
                        user2_id={user2_id}
                      />
                    </MessageWrapper>
                  </div>
                ))
            : null}
          <DmInitMessageBox secondUser={user} />
        </main>
        <aside className={`asideContent ${openThread ? 'active' : ''}`}>
          <DmReplyInThread handleCloseThread={handleCloseThread} />
        </aside>
      </div>
    </>
  );
};

export default DmChatContainerBox;
