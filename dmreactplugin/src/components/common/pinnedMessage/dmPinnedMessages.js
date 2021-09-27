import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

import Pin from "../../../assets/img/svg/pin.svg";
import HoverPinnedMessage from "./hoverViewPinned";

const PinnedMessage = () => {
  const [open, setOpen] = useState(false);
  let check = [1, 2, 3];
  let dropDownMessages = check.map((_, i) => (
    <div key={i}>
      <HoverPinnedMessage
        imgSrc={"https://picsum.photos/200"}
        time={"Today at 3:15AM"}
        messageBody={"isboe sbch aohec owdhos doncow "}
      />
    </div>
  ));
  const onHoverMouseOut = () => {
    setOpen(false);
  };
  return (
    <button
      className="d-inline-flex btn gap-1 px-1 py-1 align-items-center rounded-3 position-relative"
      style={{ height: "30px", backgroundColor: "#BCF9E6", fontSize: "13px" }}
      onClick={() => {
        setOpen(!open);
      }}
      onMouseLeave={onHoverMouseOut}
    >
      <img src={Pin} alt="pin" className="p-1 h-100" />
      <div>{`${check.length} Pinned`}</div>

      {open ? (
        <div
          className="position-absolute bg-white shadow-sm p-3"
          style={{ width: "400px", top: "100%", zIndex: "10" }}
          aria-hidden
          onClick={(e) => {
            e.stopPropagation();
          }}
        >
          {dropDownMessages}
        </div>
      ) : null}
    </button>
  );
};

export default PinnedMessage;
