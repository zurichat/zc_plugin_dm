import React, { useState } from "react";
import close from "../../../assets/img/svg/close.svg";
import RemovePinnedMessage from "./removePinnedMessageModal";

const HoverPinnedMessage = ({ name, date, link, imgSrc }) => {
  const [openModal, isOpenModal] = useState(false);

  const unPin = () => {
    isOpenModal(true);
  };
  const resetState = () => {
    isOpenModal(false);
    revert();
  };

  return (
    <div
      className="d-flex flex-column align-items-start position-relative gap-1 m-1 p-3 zindex-fixed"
      style={{ backgroundColor: "#BCF9E6" }}
    >
      <button
        onClick={unPin}
        className="btn d-block position-absolute"
        style={{ height: "15px", top: "10px", right: "10px" }}
      >
        <img
          src={close}
          alt="close"
          className="d-block"
          style={{ height: "15px" }}
        />
      </button>
      <div className="d-flex align-items-center gap-2 justify-content-start">
        <img
          src={imgSrc}
          alt="pp"
          className="d-block"
          style={{ height: "50px", width: "50px" }}
        />
        <div className="writeUp">{name}</div>
      </div>
      <p className="mb-0 text-left" style={{ textAlign: "left" }}>
        {link}
      </p>
      <span className="d-block text-secondary text-left">{date}</span>
      {openModal && <RemovePinnedMessage name={name} reset={resetState} />}
    </div>
  );
};

export default HoverPinnedMessage;
