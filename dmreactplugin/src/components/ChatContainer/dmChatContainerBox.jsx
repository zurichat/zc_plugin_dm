import React, { useState,useEffect } from "react";
import { useSelector } from "react-redux";
import MessageWrapper from "../common/dmHoverState/dmHoverstate";
import DmInitMessageBox from "../dmInitMessagebox";
import DmSingleMessageContainer from "../dmSingleMessageContainer";
import DmReplyInThread from "../ReplyInThread/replyInThread";
import "./chatContainerBox.css";
import { FaAngleDown } from "react-icons/fa";
import {SubscribeToChannel} from '@zuri/control';
import { useDispatch } from 'react-redux';
import { handleGetRoomMessages } from "../../Redux/Actions/dmActions";


const DmChatContainerBox = ({ user2_id, room_id }) => {
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
  
  
  SubscribeToChannel(`${room_id}`, (ctx) => {
    const websocket = ctx.data
    console.log("Websocket", websocket);
    //console.log("This is centrifigo " + ctx);
  });
  const dates = new Set();
  const renderDate = (chat, dateNum) => {
    const timestampDate = new Date(chat.created_at).toDateString();
    // Add to Set so it does not render again
    dates.add(dateNum);
    const todayDate = new Date().toDateString();
    let prev_date = new Date();
    prev_date.setDate(prev_date.getDate() - 1);
    if (timestampDate === todayDate) {
      return "Today";
    } else if (new Date(prev_date).toDateString() == timestampDate) {
      return "Yesterday";
    }
    return <>{timestampDate}</>;
  };
  return (
    <>
      <div className="dm-chatContainerBox w-100 d-flex align-items-end">
        <main className="dm-chat-main-container">
          {room_messages?.results
            ? room_messages?.results
                ?.sort((first, second) => {
                  const firstDate = new Date(first.created_at);
                  const secondDate = new Date(second.created_at);
                  return Date - secondDate;
                })
                .map((messages) => {
                  // console.log(messages);
                  //const [message, setMessage] = useState(messages)
                  const dateNum = new Date(messages.created_at).toDateString();
                  
                  return (
                    <div key={messages?.id}>
                      <div className="__date_tags">
                        {dates.has(dateNum) ? (
                          ""
                        ) : (
                          <div className="__date_tag">
                            <p> {renderDate(messages, dateNum)}</p>
                            <small>
                              <FaAngleDown />
                            </small>
                          </div>
                        )}
                      </div>
                      <MessageWrapper handleOpenThread={handleOpenThread}>
                        <DmSingleMessageContainer
                          messages={messages}
                          user2_id={user2_id}
                          room_id={room_id}
                        />
                      </MessageWrapper>
                    </div>
                  );
                })
            : null}
          <DmInitMessageBox secondUser={user} />
        </main>
        <aside className={`asideContent ${openThread ? "active" : ""}`}>
          <DmReplyInThread handleCloseThread={handleCloseThread} />
        </aside>
      </div>
    </>
  );
};
export default DmChatContainerBox;