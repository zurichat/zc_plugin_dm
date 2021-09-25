import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

import Pin from "../assets/img/svg/pin.svg";
import HoverPinnedMessage from "./common/pinnedMessage/hoverViewPinned";

const PinnedMessage = ({ amount }) => {
  const [open, setOpen] = useState(false);
  let check = [1, 2, 3];
  let dropDownMessages = check.map((_, i) => (
    <div key={i}>
      <HoverPinnedMessage />
    </div>
  ));

  return (
    <div
      className="d-inline-flex gap-1 px-3 py-1 rounded-3 position-relative"
      style={{ height: "30px", backgroundColor: "#BCF9E6" }}
      role="button"
    >
      <img src={Pin} alt="pin" className="h-100" />
      <div
        aria-hidden
        onClick={() => {
          setOpen(!open);
        }}
      >{`${amount} Pinned`}</div>

      {open ? (
        <div
          className="position-absolute bg-white shadow-sm p-3"
          style={{ width: "400px", top: "100%" }}
        >
          {dropDownMessages}
        </div>
      ) : null}
    </div>
  );
};

export default PinnedMessage;
