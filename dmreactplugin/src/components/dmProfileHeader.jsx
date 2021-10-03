import React, { useState } from "react";
import "../assets/css/dmProfileHeader.css";
import Modal from "react-modal";
import Parcel from "single-spa-react/parcel";
import { pluginHeader } from "@zuri/plugin-header";
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
    const headerConfig = {
        name: `${user?.user_name}`, //Name on header
        icon: `${user?.image_url}`, //Image on header
        eventTitle: () => {
            console.log(user);
            setModalIsOpen(true);
            //Block of code to be triggered on title click
        },
    };
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
            <Parcel
                config={pluginHeader}
                wrapWith='div'
                wrapStyle={{ width: "100%" }}
                headerConfig={headerConfig}
            />
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
                        </div>
                    </div>
                </div>
            </Modal>
        </div>
    );
};

export default dmProfileHeader;
