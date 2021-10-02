import React, { useEffect } from "react";
import "./replyInThread.css";
import MessageBox from "./MessageBox";
import InputBox from "./InputBox";
import { FiX } from "react-icons/fi";
import axios from "axios";
const DmReplyInThread = ({userId, handleCloseThread }) => {
  const textUrl =
    "https://dm.zuri.chat/api/v1/org/6145eee9285e4a18402074cd/rooms/6146cb29845b436ea04d1029/messages/614e320ff31a74e068e4d443/threads";
  useEffect(() => {
    axios.get(textUrl).then((response) => {
      console.log(response);
    });
  }, []);

  const AddReplyThread = (value) => {
    axios.post(textUrl, {
        "message": value,
        "message_id": "614e320ff31a74e068e4d443",
        "sender_id": {userId},
    }).then((response) => {
      console.log(response);
    });
  };

  return (
    <div className="thread">
      <div className="closeThread">
        <FiX onClick={handleCloseThread} />
      </div>
      <MessageBox isThread />
      <div className="divider">
        <p>3 replies</p>
        <hr />
      </div>
      <MessageBox isThread />
      {/* <MessageBox isThread />
            <MessageBox isThread /> */}

      <InputBox sendReply={AddReplyThread} />
    </div>
  );
};

export default DmReplyInThread;
