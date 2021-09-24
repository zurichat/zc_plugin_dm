import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";

import Pin from "../assets/img/svg/pin.svg";

const PinnedMessage = ({ amount }) => {
  return (
    <div
      className="d-inline-flex gap-1 px-3 py-1 rounded-3"
      style={{ height: "30px", backgroundColor: "#BCF9E6" }}
    >
      <img src={Pin} alt="pin" className="h-100" />
      <div>{`${amount} Pinned`}</div>
    </div>
  );
};

export default PinnedMessage;
