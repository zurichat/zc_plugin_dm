import React from "react";

const HoverPinnedMessage = ({ messageBody, time, imgSrc }) => {
  return (
    <div
      className="d-flex flex-column align-items-start position-relative gap-1 m-1 p-3 zindex-fixed"
      style={{ backgroundColor: "#BCF9E6" }}
    >
      <div className="d-flex align-items-center gap-2 justify-content-start">
        <img
          src={imgSrc}
          alt="pp"
          className="d-block"
          style={{ height: "50px", width: "50px" }}
        />
        <div className="writeUp">Deyrin Cutting</div>
      </div>
      <p className="mb-0 text-left" style={{ textAlign: "left" }}>
        {messageBody}
      </p>
      <span className="d-block text-secondary text-left">{time}</span>
    </div>
  );
};

export default HoverPinnedMessage;
