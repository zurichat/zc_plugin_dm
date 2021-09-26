import React, { useState } from 'react';
import '../assets/css/dmProfileHeader.css';
import Modal from 'react-modal';
import {
    FaAngleDown,
    FaRegBellSlash,
    FaRegClock,
    FaRegEnvelope,
    FaTimes,
} from 'react-icons/fa';
import { FiPhone } from 'react-icons/fi';
import { BsClock, BsX, BsEnvelope } from 'react-icons/bs';

const dmProfileHeader = () => {
    const [modalIsOpen, setModalIsOpen] = useState(false);
    return (
        <div>
            <header className='dm-profileHeader'>
                {/* Img to be placed here */}
                <div
                    className='dm-profile-header-name-img'
                    onClick={() => setModalIsOpen(true)}
                >
                    <img
                        className='profileHeader__img'
                        src='https://picsum.photos/200'
                        alt='Profile Pic'
                    />
                    <p className='profileHeader__name'>Sandra Bernard</p>

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
                                    src='https://picsum.photos/200'
                                    alt='profile pic'
                                    className='profilePop__img'
                                />
                                <div className='profilePop__details'>
                                    <p className='profilePop__details__header'>
                                        Mama Gee 🦊 ⭐️{' '}
                                    </p>
                                    <p className='profilePop__details__para'>
                                        Frontend Design Mentor{' '}
                                    </p>
                                    <p className='profilePop__details__para'>
                                        She/Her{' '}
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
                            <p>
                                <BsClock /> 3:15AM Local Time
                            </p>
                            <p>
                                <FiPhone />{' '}
                                <span className='profilePop__blue'>
                                    {' '}
                                    +23701877832
                                </span>{' '}
                            </p>
                            <p>
                                <BsEnvelope />{' '}
                                <span className='profilePop__blue'>
                                    {' '}
                                    mamagee@gmail.com
                                </span>
                            </p>
                            <h2 className='profilePop__blue '>View Profile</h2>
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
