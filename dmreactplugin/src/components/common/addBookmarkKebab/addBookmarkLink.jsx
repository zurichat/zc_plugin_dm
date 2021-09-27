import React, { useState } from 'react';

import ModalButton from '../pinnedMessage/button';
import Close from '../../../assets/img/svg/close.svg';
import TextField from './textField';
import AddBookmarkModal from './addBookmarkModal';
import NameTextField from './nameLinkTextField';
const AddBookmarkLink = () => {
    const [closed, setClose] = useState(true);
    const [isLink, setIsLink] = useState(false);

    const Button = (
        <>
            <NameTextField label='Name' placeholder='Name' />
            <div className='d-flex justify-content-end'>
                <ModalButton onClick={() => setClose(false)} close>
                    Cancel
                </ModalButton>
                <ModalButton>Add</ModalButton>
            </div>
        </>
    );
    const onTextChange = (value) => {
        const regex1 =
            /((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)/;
        const regex2 =
            /(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})/;
        const isUrl = regex2.test(value);
        setIsLink(isUrl);
    };
    return (
        <AddBookmarkModal close={closed}>
            <div
                className='d-flex flex-column p-4 w-50 gap-3 bg-white rounded-1'
                role='presentation'
                onClick={(e) => {
                    e.stopPropagation();
                }}
            >
                <div
                    className='d-flex justify-content-between text-capitalize align-items-center'
                    style={{
                        fontSize: '30px',
                        fontWeight: '700',
                        height: '20px',
                    }}
                >
                    <div className='writeUp'>Add a Bookmark</div>
                    <img
                        src={Close}
                        alt='close'
                        className='d-block h-75'
                        role='presentation'
                        onClick={() => setClose(false)}
                    />
                </div>
                <div>
                    <TextField
                        placeholder='Link'
                        label='Link'
                        onChange={onTextChange}
                    />
                </div>
                {isLink ? Button : null}
            </div>
        </AddBookmarkModal>
    );
};

export default AddBookmarkLink;
