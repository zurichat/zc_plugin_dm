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
import StarButtonButton from "./starPersonButton";

const dmProfileHeader = ({ actualUser, none, grid, setNone, setGrid }) => {
    const user = actualUser && actualUser;
    const [modalIsOpen, setModalIsOpen] = useState(false);

    const getLocalTime = () => {
        let date = new Date();
        let hours = date.getHours();
        let minutes = date.getMinutes();
        let localTime =
            hours > 12
                ? hours - 12 + ":" + minutes + "PM"
                : hours + ":" + minutes + "AM";

        return localTime + " Local Time";
    };
    const handleViewProfile = () => {
        setNone("block");
        setGrid("grid");
        setModalIsOpen(false);
    };
    return (
        <div>
            <header className='dm-profileHeader d-flex align-items-center'>
                {/* Img to be placed here */}
                <div
                    className='dm-profile-header-name-img d-flex align-items-center'
                    onClick={() => setModalIsOpen(true)}
                >
                    <img
                        className='profileHeader__img'
                        src={user?.image_url}
                        alt='Profile Pic'
                    />
                    <p className='profileHeader__name'>{user?.user_name}</p>

                    <FaAngleDown className='profileHeader__icon' />
                </div>
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
                        height: "auto",
                        borderRadius: "8px",
                        margin: "0 auto",
                        padding: "0px",
                    },
                }}
            >
                <div className='profilePop'>
                    <div className='profilePop__head'>
                        <div className='profilePop__top'>
                            <div className='profilePop__header'>
                                <img
                                    src={user?.image_url}
                                    alt={user?.first_name}
                                    className='profilePop__img'
                                />
                                <div className='profilePop__details'>
                                    <p className='profilePop__details__header'>
                                        <div>
                                            {user?.first_name} {user?.last_name}{" "}
                                        </div>
                                        <StarButtonButton />
                                    </p>
                                    <p className='profilePop__details__para'>
                                        {user?.role}
                                    </p>
                                    <p className='profilePop__details__para'>
                                        {user?.pronouns}
                                    </p>
                                </div>
                            </div>
                            <BsX
                                className='profilePop__icon'
                                onClick={() => setModalIsOpen(false)}
                            />
                        </div>
                        <button className='profilePop__mute'>
                            {" "}
                            <FaRegBellSlash /> Mute
                        </button>
                        <div className='profilePop__switch'>
                            <p className='profilePop__switch__1'>About</p>
                            <p>Integrations</p>
                        </div>
                    </div>
                    <div className='profilePop__body'>
                        <div className='profilePop__body__card1'>
                            <p className='d-flex align-items-center'>
                                <BsClock /> {getLocalTime()}{" "}
                            </p>
                            <p className='d-flex align-items-center'>
                                <FiPhone />{" "}
                                <span className='profilePop__blue'>
                                    {" "}
                                    {user?.phone}
                                </span>{" "}
                            </p>
                            <p className='d-flex align-items-center'>
                                <BsEnvelope />{" "}
                                <span className='profilePop__blue'>
                                    {" "}
                                    {user?.email}
                                </span>
                            </p>
                            <h2
                                className='profilePop__blue'
                                style={{ cursor: "pointer" }}
                                onClick={handleViewProfile}
                            >
                                View Profile
                            </h2>
                        </div>
                        <div className='profilePop__body__card2'>
                            <h1>Files</h1>
                            <p>
                                There aren’t any files to see here. But there
                                could be - drag and drop any file to the message
                                panel to add it to this conversation
                            </p>
                        </div>
                    </div>
                </div>
            </Modal>
        </div>
    );
};

export default dmProfileHeader;
