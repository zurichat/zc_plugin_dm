import React from "react";
import { useSelector } from "react-redux";
import "../assets/css/dmSingleMessageContainer.css";
import { FaAngleDown } from "react-icons/fa";

function DmSingleMessageContainer({ messages, user2_id }) {
  const membersReducer = useSelector(({ membersReducer }) => membersReducer);
  const actualUser =
    membersReducer && membersReducer.find((member) => member._id === user2_id);
  const user = actualUser ? actualUser : null;

  //Changing the message time to 12hour UTC time
  const messageTime = messages?.created_at;
  const localeTime = new Date(messageTime).toLocaleTimeString(
    {},
    { hour: "2-digit", minute: "2-digit" }
  );

  // const dates = new Set();

  // const renderDate = (chat, dateNum) => {
  //   const timestampDate = new Date(chat.created_at).toDateString();

  //   // Add to Set so it does not render again
  //   dates.add(dateNum);
  //   const todayDate = new Date().toDateString();

  //   let prev_date = new Date();
  //   prev_date.setDate(prev_date.getDate() - 1);

  //   if (timestampDate === todayDate) {
  //     return "Today";
  //   } else if (new Date(prev_date).toDateString() == timestampDate) {
  //     return "Yesterday";
  //   }
  //   return <>{timestampDate}</>;
  // };

  // const dateNum = new Date(messages.created_at).toDateString();
  return (
    <>
      <div className="dm-plugin-thread-messages">
        <div className="dm-plugin-thread-message-group px-3 py-3">
          <div className="dm-plugin-thread-message-image-container">
            <img
              src={user?.image_url}
              alt="Profile Picture"
              width="36"
              height="36"
              className="dm-plugin-thread-message-image"
            />
          </div>
          <div className="dm-plugin-thread-message-body">
            <p className="dm-plugin-thread-message-header">
              <span className="dm-plugin-thread-message-name">
                {user?.user_name}
              </span>
              <span className="dm-plugin-thread-message-time">
                {localeTime}
              </span>
            </p>
            <p className="dm-plugin-thread-message-text">{messages?.message}</p>
          </div>
        </div>
      </div>
    </>
  );
}

export default DmSingleMessageContainer;
