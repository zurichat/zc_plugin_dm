import React, { useState } from 'react';
import './profileSidebar.css';
import message from './svg/message.svg';
import mute from './svg/mute.svg';
import more from './svg/more.svg';
import more2 from './svg/more2.svg';
import copy from './svg/copy.svg';
import { AiOutlineClose } from 'react-icons/ai';

const ProfileSidebar = ({ none, grid, setNone, setGrid, actualUser }) => {
  const [moreOptionsOpen, setMoreOptionsOpen] = useState(false);

  const toggleMoreOptions = () => {
    if (moreOptionsOpen) {
      setMoreOptionsOpen(false);
    } else {
      setMoreOptionsOpen(true);
    }
  };

  const handleCloseProfile = () => {
    setGrid('');
    setNone('none');
  };

  const user = actualUser && actualUser;
  const getLocalTime = () => {
    let date = new Date();
    let hours = date.getHours();
    let minutes = date.getMinutes();
    let localTime =
      hours > 12
        ? hours - 12 + ':' + minutes + 'PM'
        : hours + ':' + minutes + 'AM';

    return localTime;
  };

  return user ? (
    <div className="dm-plugin-full-profile">
      <nav className="dm-plugin-full-profile-navbar">
        <li style={{ marginLeft: '12px' }}>Profile</li>
        <li>
          <AiOutlineClose
            className="fa-times-dm-plugin"
            style={{
              verticalAlign: 'middle',
              cursor: 'pointer',
              marginRight: '12px',
            }}
            onClick={handleCloseProfile}
          />
        </li>
      </nav>
      <div className="dm-plugin-full-profile-section"></div>
      <div className="dm-plugin-full-profile-sidebar">
        <div className="dm-plugin-full-profile-full-profile">
          <div
            className="dm-plugin-full-profile-full-profile-image"
            style={{
              backgroundImage: `url('${user?.image_url}')`,
            }}
          >
            {/* <img src={picture} alt='profile picture' /> */}
          </div>
          <div className="dm-plugin-full-profile-full-profile-details">
            <h2 className="name">{user?.user_name}</h2>
            <h4 className="position">{user?.role}</h4>
            <h4 className="pronouns">{user?.pronouns}</h4>
            <p
              style={{
                textAlign: 'center',
                fontSize: '18px',
                marginBottom: '18px',
              }}
            >
              {user?.status.tag}
            </p>
            <div className="profile-buttons">
              <div className="btn">
                <img className="btn-icon" src={message} />
                <p>Message</p>
              </div>
              <div className="btn">
                <img className="btn-icon" src={mute} />
                <p>Mute</p>
              </div>
              <div className="btn">
                <img
                  className="btn-icon"
                  onClick={() => toggleMoreOptions()}
                  src={moreOptionsOpen ? more2 : more}
                />
                <p>More</p>
              </div>
              {moreOptionsOpen && (
                <div className="more-options-modal">
                  <div className="top">
                    <p>View files</p>
                  </div>
                  <div className="bottom">
                    <p>Copy Member ID</p>
                    <p>{user?._id}</p>
                    <img
                      className="copy-icon"
                      src={copy}
                      onClick={navigator.clipboard.writeText(user?._id)}
                    ></img>
                  </div>
                </div>
              )}
            </div>
            <p className="other-info">Display Name</p>
            <p className="other-info-answer">{user?.user_name}</p>
            <p className="other-info">Local Time</p>
            <p className="other-info-answer">{getLocalTime()}</p>
            <p className="other-info">Phone Number</p>
            <p className="other-info-answer">{user?.phone}</p>
          </div>
        </div>
      </div>
    </div>
  ) : null;
};

export default ProfileSidebar;
