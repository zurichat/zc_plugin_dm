import React, { useState } from "react";
import EmojiPicker from "../dmEmojiComp/dmEmojiComp";

function DmInputTextField() {
  const [inputValue, setInputValue] = useState("");
  return (
    <div style={{ position: "relative", display: "flex", alignItems: "center", gap: "20px" }}>
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
