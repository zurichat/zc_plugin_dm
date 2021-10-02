import React, { useState } from 'react';
import './threeDotKebab.css';
import { FaUniregistry } from 'react-icons/fa';
import { IoIosArrowForward } from 'react-icons/io';
import { RiParkingLine } from 'react-icons/ri';
import { BiEditAlt } from 'react-icons/bi';
import { HiOutlineExternalLink } from 'react-icons/hi';
import { MdPoll } from 'react-icons/md';
import { FaTrashAlt } from 'react-icons/fa';
import { useDispatch, useSelector } from 'react-redux';
import { handleDeleteRoomMessage } from '../../../Redux/Actions/dmActions';
import DmEditMessage from '../dmEditMessage/dmEditMessage';
// import { IoLogoMedium } from "react-icons/io"

function ThreeDotKebab({ messages }) {
    const [secondPopupOpen, setSecondPopupOpen] = useState(false);
    const [dmdeletepopup, setdmdeletepopup] = useState(false);
    const [dmEditMessage, setDmEditMessage] = useState(false);
    // const [secondPopupOpen,setSecondPopupOpen]=useState(false);

    const dispatch = useDispatch();

    // const messages = useSelector(({roomsReducer}) => roomsReducer);
    // console.log(messages)
    const OnDeleteMessage = () => {
        dispatch(handleDeleteRoomMessage(org_id, room_id, message_id));
    };
    return (
        <>
            <div className='Dm-ThreeDotKebab-Menu-FirstPopup'>
                <div className='DmMenuListBorder'>
                    Turn off notififcations for replies
                </div>
                <div>
                    Mark Unread
                    <FaUniregistry />
                </div>
                <div onClick={() => setSecondPopupOpen(!secondPopupOpen)}>
                    Remind me about this <IoIosArrowForward />
                </div>
                <div>Copy Link</div>
                <div>
                    Pin to this conversation <RiParkingLine />{' '}
                </div>
                <div onClick={() => setDmEditMessage(!dmEditMessage)}>
                    Edit Message <BiEditAlt />
                </div>
                <div onClick={() => setdmdeletepopup(!dmdeletepopup)}>
                    {' '}
                    Delete Message <FaTrashAlt />{' '}
                </div>
                <div className='DmPollMore DmPollMoreSpecial'>
                    {' '}
                    <MdPoll /> Turn question into poll
                </div>
                <div className='DmPollMore'>
                    More message shortcuts <HiOutlineExternalLink />
                </div>
            </div>
            {secondPopupOpen && (
                <div className='Dm-ThreeDotKebab-Menu-SecondPopup'>
                    <div>In 20 minutes</div>
                    <div>In 1 hour</div>
                    <div>In 3 hours</div>
                    <div>Tomorrow</div>
                    <div>Next week</div>
                    <div className='Dm-ThreeDotKebab-Menu-SecondPopupCustom'>
                        Custom... <span>M</span>{' '}
                    </div>
                </div>
            )}
            {dmdeletepopup && (
                <div className='Dm-ThreeDotKebab-DeleteMessage'>
                    <p> Are You Sure You Want to Delete Message?</p>
                    <div className='Dm-Delete-Confirm'>
                        <button onClick={() => setdmdeletepopup(false)}>
                            Cancel
                        </button>{' '}
                        <button onClick={() => OnDeleteMessage()}>
                            Confirm
                        </button>
                    </div>
                </div>
            )}
            {
              dmEditMessage && <div className='Dm-ThreeDotKebab-DeleteMessage'>
                <DmEditMessage/>
              </div>
            }
        </>
    );
}
export default ThreeDotKebab;
