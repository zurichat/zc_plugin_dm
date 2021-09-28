import React from "react";
import { useSelector } from "react-redux";
import "../assets/css/dmSingleMessageContainer.css";

function DmSingleMessageContainer({ messages }) {
  const { room_messages } = useSelector(({ roomsReducer }) => roomsReducer);
  return (
    <>
      <div className="dm-plugin-thread-messages">
        <div className="dm-plugin-thread-message-group px-3 py-2">
          <div className="dm-plugin-thread-message-image-container">
            <img
              src="https://picsum.photos/200"
              alt=""
              width="36"
              height="36"
              className="dm-plugin-thread-message-image"
            />
          </div>
          <div className="dm-plugin-thread-message-body">
            <p className="dm-plugin-thread-message-header">
              <span className="dm-plugin-thread-message-name">
                {messages.sender_id}
              </span>
              <span className="dm-plugin-thread-message-time">
                {messages?.created_at.slice(11, -11)}
              </span>
            </p>
            <p className="dm-plugin-thread-message-text">
              {messages?.message}{" "}
            </p>
          </div>
        </div>
      </div>
    </>
  );
}

export default DmSingleMessageContainer;
