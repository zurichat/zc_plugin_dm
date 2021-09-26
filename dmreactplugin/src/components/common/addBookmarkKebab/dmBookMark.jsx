import React, { useState } from 'react';
import { BiPlus } from 'react-icons/bi';
import { AiOutlinePaperClip } from 'react-icons/ai';
import './dmBookmarkStyle.css';

const DmBookMarkHeader = () => {
    const [isOpen, setIsOpen] = useState(false);

    return (
        <>
            <div className='dm-bookmark-head'>
                <div className='add-bookmark d-flex flex-flow align-items-center px-3 py-1'>
                    <button className='btn btn-add-bookmark d-flex align-items'>
                        <BiPlus />
                        <p className='m-0'>Add a bookmark</p>
                    </button>
                </div>
            </div>
            {/* <div className='addBookmark-overlay'>
                <div className='container mx-auto pt-3 pb-3 addBookmark'>
                    <div className='row d-flex pt-2 pb-2 mb-3 bookmark-link'>
                        <div className='col-auto align-self-center link-btn'>
                            <button className='col-auto p-2 btn-outline-disabled'>
                                <AiOutlinePaperClip />
                            </button>
                        </div>
                        <div className='col bookmark_description ps-0'>
                            <h2 className='m-0'></h2>
                            <p></p>
                        </div>
                    </div>
                    <hr />
                    <span className=''>Add recent</span>
                </div>
            </div> */}
        </>
    );
};

export default DmBookMarkHeader;
