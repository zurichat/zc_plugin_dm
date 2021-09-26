import React, { useState } from 'react';
import './Emoji.css';
import 'emoji-mart/css/emoji-mart.css'
import { Picker } from 'emoji-mart';
import { FaRegSmile } from "react-icons/fa";




function EmojiPicker() {
    const [emoji, setEmoji] = useState(false)

    return (
        <div className="dm-emoji">
            <FaRegSmile className=" btn-emoji"
                onClick={() => setEmoji(!emoji)}
                 />
                 {/* emoji picker  */}
               <div className="emojipicker"
                 style={{ display: `${emoji ? "block" : "none"}` }}>
                <Picker title='Pick your emoji '
                />
            </div>
        </div>
    );
}

export default EmojiPicker;
