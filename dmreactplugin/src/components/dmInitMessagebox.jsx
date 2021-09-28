import React from "react";
import { useSelector } from "react-redux";
import "../assets/css/dmInitMessagebox.css";

const DmInitMessageBox = () => {
  const roomsReducer = useSelector(({ roomsReducer }) => roomsReducer);
  const { description } = roomsReducer?.room_info;
  return (
    <>
      <div className="d-flex align-item-center flex-row py-4 px-3">
        <div className="link-btn ">
          <button className="btn-outline-disabled btn-dm-chat"></button>
        </div>
        <div className="px-3 chat-description">
          <p className="m-0">{description}</p>
          <p className="m-0">
            Here you can send messages and share files with each other
          </p>
        </div>
      </div>
    </>
  );
};

export default DmInitMessageBox;
