import React from 'react';
import '../assets/css/dmInitMessagebox.css';

const DmInitMessageBox = () => {
    return (
        <>
            <div class='d-flex align-item-center flex-row py-4 px-3'>
                <div class='link-btn '>
                    <button class='btn-outline-disabled btn-dm-chat'></button>
                </div>
                <div class='px-3 chat-description'>
                    <h4 class='m-0'>
                        This conversation is just between two of you
                    </h4>
                    <p class='m-0'>
                        Here you can send messages and share files with
                        <span class='dm-username-id'>@ davidblack</span>
                    </p>
                </div>
            </div>
        </>
    );
};

export default DmInitMessageBox;
