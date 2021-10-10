import React, { useState } from "react";
import EmojiPicker from "../dmEmojiComp/dmEmojiComp";

function DmInputTextField() {
  const [inputValue, setInputValue] = useState("");
  return (
    <div className="position-relative d-flex align-items-center">
      <input
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        id="TestInput"
        type="text"
        placeholder="Enter Text Here"
      />
      <EmojiPicker inputValue={inputValue} setInputValue={setInputValue} />
    </div>
  );
}

export default DmInputTextField;
