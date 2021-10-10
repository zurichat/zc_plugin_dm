import React, { useState } from "react";
import EmojiPicker from "../dmEmojiComp/dmEmojiComp";

function DmInputTextField(ref) {
  const [inputValue, setInputValue] = useState("");
  return (
    <div className="position-relative d-flex align-items-center">
      <input
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        id="TestInput"
        type="text"
        placeholder="Enter Text Here"
        ref={ref}
      />
      <EmojiPicker inputValue={inputValue} setInputValue={setInputValue} />
    </div>
  );
}

const forwardedRef = React.forwardRef(DmInputTextField);

export default forwardedRef;
