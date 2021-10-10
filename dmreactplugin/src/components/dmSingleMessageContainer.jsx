import React, { useState } from "react";
import { useSelector } from "react-redux";
import "../assets/css/dmSingleMessageContainer.css";
import DmSingleMessageReaction from "./DmSingleMessageReaction";

import ReactTooltip from "react-tooltip";

import DmpopupProfile from "./DmPopupProfile";

function DmSingleMessageContainer({
  messages,
  user2_id,
  handleOpenThread,
  setNone,
  setGrid,
}) {
  const membersReducer = useSelector(({ membersReducer }) => membersReducer);

  const actualUser =
    membersReducer && membersReducer.find((member) => member._id === user2_id);
  const user = actualUser ? actualUser : null;

  const [showPopup, setShowPopup] = useState(false);

  console.log("USER", user);
  //Changing the message time to 12hour UTC time
  const messageTime = messages?.created_at;
  const localeTime = new Date(messageTime).toLocaleTimeString(
    {},
    { hour: "2-digit", minute: "2-digit" }
  );
  const fullLocaleTime = new Date(messageTime).toLocaleTimeString(
    {},
    {
      formatMatcher: "basic",
      weekday: "long",
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    }
  );

  const handleViewProfile = () => {
    setNone("block");
    setGrid("grid");
    setShowPopup(false);
  };

  return (
    <>
      <div className="dm-plugin-thread-messages">
        <div className="dm-plugin-thread-message-group px-3 py-3">
          <div className="dm-plugin-thread-message-image-container">
            <img
              src={user?.image_url}
              alt="user image"
              width="36"
              height="36"
              className="dm-plugin-thread-message-image"
              onClick={() => setShowPopup(!showPopup)}
            />
          </div>
          <div className="dm-plugin-thread-message-body">
            <p className="dm-plugin-thread-message-header">
              <span className="dm-plugin-thread-message-name">
                {user?.user_name}
              </span>
              <span
                className="dm-plugin-thread-message-time"
                data-tip={fullLocaleTime}
                data-for="dm-time-tool-tip"
              >
                {localeTime}
              </span>
              <ReactTooltip
                effect="solid"
                className="dm-time-toolTip-custom-class"
                id="dm-time-tool-tip"
              />
            </p>
            <p className="dm-plugin-thread-message-text">{messages?.message}</p>
            <span>
              {messages?.media?.map((media) => (
                <img
                  src={media}
                  alt="Message Media"
                  height="15px"
                  width="15px"
                />
              ))}
            </span>
            <span>
              {messages?.reactions?.map((reaction) => (
                <span>{reaction?.data}</span>
              ))}
            </span>
          </div>
        </div>
        <DmSingleMessageReaction
          handleOpenThread={handleOpenThread}
          user={user}
        />
      </div>

      {showPopup ? (
        <DmpopupProfile handleViewProfile={handleViewProfile} user={user} />
      ) : null}
      {showPopup ? (
        <div onClick={() => setShowPopup(false)} className="dm__overlay"></div>
      ) : null}
    </>
  );
}

export default DmSingleMessageContainer;
