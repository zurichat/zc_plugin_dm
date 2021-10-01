import React from 'react';
import './replyInThread.css';
import MessageBox from './MessageBox';
import InputBox from './InputBox';
import { FiX } from 'react-icons/fi';

const DmReplyInThread = ({ handleCloseThread }) => {
    return (
        <div className='thread'>
            <div className='closeThread'>
                <FiX onClick={handleCloseThread} />
            </div>
            <MessageBox isThread />
            <div className='divider'>
                <p>3 replies</p>
                <hr />
            </div>
            <MessageBox isThread />
            {/* <MessageBox isThread />
            <MessageBox isThread /> */}

            <InputBox />
        </div>
    );
};

export default DmReplyInThread;
