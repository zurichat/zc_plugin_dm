import React, { useState } from "react";
import "../assets/css/dmProfileHeader.css";
// import Modal from "react-modal";
import Parcel from "single-spa-react/parcel";
import { pluginHeader } from "@zuri/plugin-header";
// import {
//     FaAngleDown,
//     FaRegBellSlash,
//     FaRegClock,
//     FaRegEnvelope,
//     FaTimes,
// } from "react-icons/fa";
// import { FiPhone } from "react-icons/fi";
// import { BsClock, BsX, BsEnvelope } from "react-icons/bs";
// import StarButtonButton from "./starPersonButton";

const dmProfileHeader = ({ actualUser, none, grid, setNone, setGrid }) => {
    const user = actualUser && actualUser;
    //dummy data
    const membersList = [
      { _id: "61698477621db9b4275224fe", email: "Lynn" },
      { _id: "6169847770e1730d5820d665", email: "Gomez"},
      { _id: "61698477bf560718682b2d4d", email: "Clemons"},
      { _id: "61698477267095a06c87cbbb", email: "Nettie"}
    ]
    // const [modalIsOpen, setModalIsOpen] = useState(false);
    const headerConfig = {
        name: `${user?.user_name}`, //Name on header
        icon: `${user?.image_url}`, //Image on header
        // eventTitle: () => {
        //     console.log(user);
        //     setModalIsOpen(true);
        //     //Block of code to be triggered on title click
        // },
        roomInfo: {
          membersList:membersList,
          addmembersevent: values => {
            // values.filter(obj => obj.value === selectedValue)
            // data.filter(obj => obj.value === selectedValue
            console.warn("a plugin added",values)
          },
          removemembersevent:id=>{
            console.warn("a plugin deleted",id)
          }
        }
    };
    // const getLocalTime = () => {
    //     let date = new Date();
    //     let hours = date.getHours();
    //     let minutes = date.getMinutes();
    //     let localTime =
    //         hours > 12
    //             ? hours - 12 + ":" + minutes + "PM"
    //             : hours + ":" + minutes + "AM";

    //     return localTime + " Local Time";
    // };
    // const handleViewProfile = () => {
    //     setNone("block");
    //     setGrid("grid");
    //     setModalIsOpen(false);
    // };
    return (
      <div>
        <Parcel
          config={pluginHeader}
          wrapWith='div'
          wrapStyle={{ width: '100%' }}
          headerConfig={headerConfig}
        />
        {/* <header className='dm-profileHeader d-flex align-items-center'>
          
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
              backgroundColor: 'hsla(0, 0%, 0%, 0.4)',
            },
            content: {
              width: '680px',
              height: 'auto',
              borderRadius: '8px',
              margin: '0 auto',
              padding: '0px',
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
                        {user?.first_name} {user?.last_name}{' '}
                      </div>
                      <StarButtonButton />
                    </p>

                    <p className='profilePop__details__para'>{user?.role}</p>
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
                {' '}
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
                  <BsClock /> {getLocalTime()}{' '}
                </p>
                <p className='d-flex align-items-center'>
                  <FiPhone />{' '}
                  <span className='profilePop__blue'> {user?.phone}</span>{' '}
                </p>
                <p className='d-flex align-items-center'>
                  <BsEnvelope />{' '}
                  <span className='profilePop__blue'> {user?.email}</span>
                </p>
                <h2
                  className='profilePop__blue'
                  style={{ cursor: 'pointer' }}
                  onClick={handleViewProfile}
                >
                  View Profile
                </h2>
              </div>
              <div className='profilePop__body__card2'>
                <h1>Files</h1>
                <p>
                  There aren’t any files to see here. But there could be - drag
                  and drop any file to the message panel to add it to this
                  conversation
                </p>
              </div>
            </div>
          </div>
        </Modal>*/}
      </div>
    )
};

export default dmProfileHeader;
