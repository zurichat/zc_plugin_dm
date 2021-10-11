import React, { useState, useEffect } from 'react';
import { useSelector } from 'react-redux';
import MessageWrapper from '../common/dmHoverState/dmHoverstate';
import DmInitMessageBox from '../dmInitMessagebox';
import DmSingleMessageContainer from '../dmSingleMessageContainer';
import DmReplyInThread from '../ReplyInThread/replyInThread';
import './chatContainerBox.css';
import { FaAngleDown } from 'react-icons/fa';
import { SubscribeToChannel } from '@zuri/control';
import { useDispatch } from 'react-redux';
import { handleGetRoomMessages } from '../../Redux/Actions/dmActions';

const DmChatContainerBox = ({
  user2_id,
  none,
  grid,
  setNone,
  room_id,
  setGrid,
}) => {
  const { room_messages } = useSelector(({ roomsReducer }) => roomsReducer);
  const [openThread, setOpenThread] = useState(false);
  const handleOpenThread = () => {
    setOpenThread(true);
  };
  const handleCloseThread = () => {
    setOpenThread(false);
  };
  /* const dispatch = useDispatch()
   useEffect(() => {
    dispatch(handleGetRoomInfo(org_id, room_id))
   }, [messages]) */

  const membersReducer = useSelector(({ membersReducer }) => membersReducer);
  const actualUser =
    membersReducer && membersReducer.find((member) => member._id === user2_id);
  const user = actualUser ? actualUser : null;

  const messages =
    room_messages?.results.length > 0
      ? room_messages.results.sort(
          (a, b) => new Date(b.created_at) - new Date(a.created_at)
        )
      : [];

  const groups = messages.reduce((groups, message) => {
    const date = message.created_at.split('T')[0];
    if (!groups[date]) {
      groups[date] = [];
    }
    groups[date].push(message);

    return groups;
  }, {});

  const groupedMessages = Object.keys(groups).map((date) => {
    return {
      date,
      messages: groups[date],
    };
  });

  console.log(groupedMessages);

  //This function below helps group messages (Today, Yesterday etc)

  const renderDate = (chat) => {
    const timestampDate = new Date(chat).toDateString();

    const todayDate = new Date().toDateString();

    let prev_date = new Date();
    prev_date.setDate(prev_date.getDate() - 1);

    if (timestampDate === todayDate) {
      return 'Today';
    } else if (new Date(prev_date).toDateString() == timestampDate) {
      return 'Yesterday';
    }
    return <>{new Date(chat).toUTCString().slice(0, 11)}</>;
  };

  SubscribeToChannel(`${room_id}`, (ctx) => {
    const websocket = ctx.data;
    console.log('Websocket', websocket);
    //console.log("This is centrifigo " + ctx);
  });
  return (
    <>
      <div className='dm-chatContainerBox w-100 d-flex align-items-end'>
        <main className='dm-chat-main-container'>
          {groupedMessages.length > 0
            ? groupedMessages.map((group, index) => (
                <span key={index}>
                  <p className='__date_tag'>
                    {renderDate(group.date)} <FaAngleDown />
                  </p>
                  {group.messages.map((message, mIndex) => (
                    <p key={mIndex}>
                      <MessageWrapper handleOpenThread={handleOpenThread}>
                        <DmSingleMessageContainer
                          key={mIndex}
                          messages={message}
                          user2_id={user2_id}
                          none={none}
                          setNone={setNone}
                          grid={grid}
                          setGrid={setGrid}
                          room_id={room_id}
                        />
                      </MessageWrapper>
                    </p>
                  ))}
                </span>
              ))
            : ''}
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
