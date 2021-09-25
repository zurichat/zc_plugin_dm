import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";

import avatar from "../../../assets/img/svg/avatar.svg";
import close from "../../../assets/img/svg/close.svg";
const HoverPinnedMessage = () => {
  return (
    <div
      className="d-flex flex-column position-relative gap-1 m-1 p-3 zindex-fixed"
      style={{ backgroundColor: "#BCF9E6" }}
    >
      <img
        src={close}
        alt="close"
        className="d-block position-absolute"
        style={{ height: "15px", top: "10px", right: "10px" }}
      />
      <div className="d-flex align-items-center gap-2 justify-content-start">
        <img
          src={avatar}
          alt="pp"
          className="d-block"
          style={{ height: "50px", width: "50px" }}
        />
        <div className="writeUp">Deyrin Cutting</div>
      </div>
      <p className="mb-0">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem blanditiis
      </p>
      <span className="d-block text-secondary">Today at 3:15AM</span>
    </div>
  );
};

export default HoverPinnedMessage;
