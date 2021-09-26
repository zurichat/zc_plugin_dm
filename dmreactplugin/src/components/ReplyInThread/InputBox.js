import React from "react";
import "./dmReplyInThread.css";
import {
  FiBold,
  FiZap,
  FiItalic,
  FiLink,
  FiList,
  FiPaperclip,
  FiNavigation,
  FiChevronDown,
} from "react-icons/fi";
import { HiOutlineAtSymbol } from "react-icons/Hi";

const InputBox = () => {
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
            <HiOutlineAtSymbol />
            <FiPaperclip />
            <FiNavigation />
            <FiChevronDown />
          </div>
        </div>
      </div>
      <div className="inputBox__checkbox">
        <input type="checkbox" name="directMessage" />
        <label for="directMessage">Also send as direct message</label>
      </div>
    </>
  );
};

export default InputBox;
