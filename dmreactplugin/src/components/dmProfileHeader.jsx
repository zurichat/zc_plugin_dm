import React, { useState } from "react";
import "../assets/css/dmProfileHeader.css";
import Modal from "react-modal";
import Parcel from "single-spa-react/parcel";
import { pluginHeader } from "@zuri/plugin-header";
import Button from 'react-bootstrap/Button'
import {
    FaAngleDown,
    FaRegBellSlash,
    FaRegClock,
    FaRegEnvelope,
    FaTimes,
} from "react-icons/fa";
import { FiPhone } from "react-icons/fi";
import { BsClock, BsX, BsEnvelope,BsPersonPlusFill } from "react-icons/bs";
import StarButtonButton from "./starPersonButton";
import AddPeopleModal from "./AddPeopleModal"
import AddPeopleToDmModal from "./AddPeopletoDmModal";
import Tabs from "react-bootstrap/Tabs"
import Tab from "react-bootstrap/Tab"
import { useDispatch } from "react-redux";

const dmProfileHeader = ({ actualUser, none, grid, setNone, setGrid,org_id, room_id }) => {
    const user = actualUser && actualUser;
    const [modalIsOpen, setModalIsOpen] = useState(false);
    const [showModal,setShowModal] = useState(false);
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

    const handleShowAddModal = () => {
      setModalIsOpen(false);
      setShowModal(true);
    }
    
    return (
      <>
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
        </header> */}
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
              </button></div> {/*}
              <div className='profilePop__switch'>
                <p className='profilePop__switch__2'>About</p>
                <p className='profilePop__switch__1'>Members</p>
                <p>Integrations</p>
              </div>
            </div>
            */}
          <Tabs defaultActiveKey="about" id="Member-tabs" className="mb-3">
            <Tab eventKey="about" title="About">
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
                {/* <p className='d-flex align-items-center'>
                  <button >Add Members</button>
                </p> */}
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
            </Tab>
            <Tab eventKey="members" title="Members">
              <div className='profilePop__body'>
                <div className='profilePop__body__card1'>
                  <div className="d-grid gap-2">
                    <Button variant="primary" size="lg" onClick={handleShowAddModal}>
                      Add People
                    </Button>
                  </div>
                </div>
                <div className='profilePop__body__card1'>
                  <div className='d-flex align-items-center'>

                  </div>
                </div>
              </div>
            </Tab>
            <Tab eventKey="integrations" title="Integrations" disabled>
            <p>Hello,This is a test</p>
            </Tab>
          </Tabs>
          </div>
        </Modal>
      </div>
      <AddPeopleModal showModal={showModal} room_id={room_id} org_id={org_id}/>
      {/* <AddPeopleToDmModal/> */}
      </>
    )
};

export default dmProfileHeader;
