import React from "react";
import "./replyInThread.css";
import {
  FiBold,
  FiZap,
  FiItalic,
  FiLink,
  FiList,
  FiPaperclip,
  FiNavigation,
  FiChevronDown,
  FiAtSign,
} from "react-icons/fi";
import { useState } from "react";

const InputBox = ({sendReply}) => {
  const [value, setValue] = useState("");
  return (
    <>
      <div className="inputBox">
        <input
          type="text"
          className="inputBox__input"
          placeholder="Send message to John"
        />
        <div className="inputBox__tool">
          <div>
            <FiBold className="active" />
            <FiZap />
            <FiItalic />
            <FiLink />
            <FiList />
          </div>

          <div>
            <FiAtSign />
            <FiPaperclip onClick={() => {
              sendReply(value)
              setValue("");
            }} />
            <FiNavigation />
            <FiChevronDown />
          </div>
        </div>
      </div>
      <div className="inputBox__checkbox">
        <input type="checkbox" name="directMessage" onChange={(e) => setValue(e.target.value)} />
        <label htmlFor="directMessage">Also send as direct message</label>
      </div>
    </>
  );
};

export default InputBox;
