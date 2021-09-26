import React from 'react'
import './dmReplyInThread.css';
import MessageBox from './MessageBox';
import InputBox from './InputBox';

const DmReplyInThread = () => {
    return (
        <div className="thread">
            <MessageBox />
            <div className="divider">
                <p>4 replies</p>
                <hr />
            </div>
            <MessageBox />
            <MessageBox />
            <MessageBox />
            <MessageBox />
            <InputBox />
        </div>
    )
}

export default DmReplyInThread
