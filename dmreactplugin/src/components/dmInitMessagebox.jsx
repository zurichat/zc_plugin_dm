import React from "react";
import "../assets/css/dmInitMessagebox.css";

const DmInitMessageBox = () => {
  return (
    <>
      <div className="d-flex align-item-center flex-row py-4 px-3">
        <div className="link-btn ">
          <button className="btn-outline-disabled btn-dm-chat"></button>
        </div>
        <div className="px-3 chat-description">
          <h4 className="m-0">This conversation is just between two of you</h4>
          <p className="m-0">
            Here you can send messages and share files with
            <span className="dm-username-id">@ davidblack</span>
          </p>
        </div>
      </div>
    </>
  );
};

export default DmInitMessageBox;
