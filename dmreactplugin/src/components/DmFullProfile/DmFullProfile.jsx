import React, { useState } from 'react';
import './DmFullProfile.css';
import message from './svg/message.svg';
import mute from './svg/mute.svg';
import more from './svg/more.svg';
import more2 from './svg/more2.svg';
import copy from './svg/copy.svg';

const DmfullProfile = () => {
    const [moreOptionsOpen, setMoreOptionsOpen] = useState(false);

    const toggleMoreOptions = () => {
        if (moreOptionsOpen) {
            setMoreOptionsOpen(false);
        } else {
            setMoreOptionsOpen(true);
        }
    };

    return (
        <div className='DmfullProfile'>
            <div
                className='profile-picture'
                style={{
                    backgroundImage: 'url("https://picsum.photos/200")',
                }}
            ></div>
            <div className='fullname'>
                <h1>Mama Gee</h1>
            </div>
            <div className='description'>
                <p>Frontend Design Mentor</p>
            </div>
            <div className='pronouns'>
                <p>She/Her</p>
            </div>
            <div className='emoji-tag'>
                <p>&#x1F43A;</p>
            </div>
            <div className='profile-buttons'>
                <div className='btn'>
                    <img className='btn-icon' src={message} />
                    <p>Message</p>
                </div>
                <div className='btn'>
                    <img className='btn-icon' src={mute} />
                    <p>Mute</p>
                </div>
                <div className='btn'>
                    <img
                        className='btn-icon'
                        onClick={() => toggleMoreOptions()}
                        src={moreOptionsOpen ? more2 : more}
                    />
                    <p>More</p>
                </div>
                {moreOptionsOpen && (
                    <div className='more-options-modal'>
                        <div className='top'>
                            <p>View files</p>
                        </div>
                        <div className='bottom'>
                            <p>Copy Member ID</p>
                            <p>ZURI01964647</p>
                            <img className='copy-icon' src={copy}></img>
                        </div>
                    </div>
                )}
            </div>
            <div className='display-name'>
                <p className='label'>Display Name</p>
                <p className='text'>MamaGee</p>
            </div>
            <div className='local-time'>
                <p className='label'>Local Time</p>
                <p className='text'>3:15PM</p>
            </div>
            <div className='phone-number'>
                <p className='label'>Phone Number</p>
                <p className='text'>0123456789</p>
            </div>
        </div>
    );
};

export default DmfullProfile;
