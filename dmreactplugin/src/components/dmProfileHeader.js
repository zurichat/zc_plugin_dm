import React, { useState } from "react";
import "../assets/css/dmProfileHeader.css";
import Modal from "react-modal";
import {
  FaAngleDown,
  FaRegBellSlash,
  FaRegClock,
  FaRegEnvelope,
  FaTimes,
} from "react-icons/fa";
import { FiPhone } from "react-icons/fi";
import { BsClock, BsX, BsEnvelope } from "react-icons/bs";

const dmProfileHeader = ({ actualUser }) => {
  const user = actualUser && actualUser;

  const [modalIsOpen, setModalIsOpen] = useState(false);

  return (
    <div>
      <header className="profileHeader" onClick={() => setModalIsOpen(true)}>
        {/* Img to be placed here */}
        <img
          className="profileHeader__img"
          src={user?.image_url}
          alt="Profile Pic"
        />
        <p className="profileHeader__name">{user?.user_name}</p>

        <FaAngleDown className="profileHeader__icon" />
      </header>
      <Modal
        isOpen={modalIsOpen}
        onRequestClose={() => setModalIsOpen(false)}
        ariaHideApp={false}
        style={{
          overlay: {
            backgroundColor: "hsla(0, 0%, 0%, 0.4)",
          },
          content: {
            width: "680px",
            borderRadius: "8px",
            margin: "0 auto",
            padding: "0px",
          },
        }}
      >
        <div className="profilePop">
          <div className="profilePop__head">
            <div className="profilePop__top">
              <div className="profilePop__header">
                <img
                  src={user?.image_url}
                  alt="profile pic"
                  className="profilePop__img"
                />
                <div className="profilePop__details">
                  <p className="profilePop__details__header">
                    {user?.first_name} {user?.last_name} 🦊 ⭐️{" "}
                  </p>
                  <p className="profilePop__details__para">{user?.role} </p>
                  <p className="profilePop__details__para">{user?.pronouns}</p>
                </div>
              </div>
              <BsX
                className="profilePop__icon"
                onClick={() => setModalIsOpen(false)}
              />
            </div>
            <button className="profilePop__mute">
              {" "}
              <FaRegBellSlash /> Mute
            </button>
            <div className="profilePop__switch">
              <p className="profilePop__switch__1">About</p>
              <p>Integrations</p>
            </div>
          </div>
          <div className="profilePop__body">
            <div className="profilePop__body__card1">
              <p>
                <BsClock /> Joined at: {user?.joined_at.slice(0, -19)}{" "}
                {user?.joined_at.slice(11, -13)}
              </p>
              <p>
                <FiPhone />{" "}
                <span className="profilePop__blue"> {user?.phone}</span>{" "}
              </p>
              <p>
                <BsEnvelope />{" "}
                <span className="profilePop__blue"> {user?.email}</span>
              </p>
              <h2 className="profilePop__blue ">View Profile</h2>
            </div>
            <div className="profilePop__body__card2">
              <h1>Files</h1>
              <p>
                There aren’t any files to see here. But there could be - drag
                and drop any file to the message panel to add it to this
                conversation
              </p>
            </div>
          </div>
        </div>
      </Modal>
    </div>
  );
};

export default dmProfileHeader;
