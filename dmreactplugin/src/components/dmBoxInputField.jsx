import React, { useState, useRef } from 'react';
// import { useDispatch, useSelector } from 'react-redux';

// import styling
import styled from 'styled-components';
import '../assets/css/dmBoxInput.css';

// import icons
import { IoMdSend } from 'react-icons/io';
import { FaAngleDown } from 'react-icons/fa';
import {
    BsLightning,
    BsLink45Deg,
    BsListUl,
    BsTypeItalic,
} from 'react-icons/bs';
import { FiAtSign, FiBold, FiPaperclip } from 'react-icons/fi';
import { Button } from 'react-bootstrap';

const dmBoxInputField = () => {
    // const { input } = useSelector((state) => state.);

    const [messageInput, setMessageInput] = useState('');

    const sendMessage = (e) => {
        e.preventDefault();

        if (!messageInput) return;
        messageSend(messageInput);
        setMessageInput('');
    };

    //Resizeable contenteditable Input function

    return (
        <div className='dm-inputbox-container'>
            <Container>
                <InputContainer>
                    <form>
                        <textarea
                            rows='2'
                            type='text'
                            value={messageInput}
                            // textInputResize={textInputResize}
                            onChange={(e) => setMessageInput(e.target.value)}
                            placeholder='Send Message to '
                            className='px-2'
                        />
                        <ChatInputEditor>
                            <LeftChatEditor>
                                <Button
                                    variant='light'
                                    className='shortcut-btn btn-inputfield-box'
                                >
                                    <BsLightning />
                                </Button>
                                <Button
                                    variant='light'
                                    className='btn-inputfield-box'
                                >
                                    <FiBold />
                                </Button>
                                <Button
                                    variant='light'
                                    className='btn-inputfield-box'
                                >
                                    <BsTypeItalic />
                                </Button>
                                <Button
                                    variant='light'
                                    className='btn-inputfield-box'
                                >
                                    <BsLink45Deg />
                                </Button>
                                <Button
                                    variant='light'
                                    className='btn-inputfield-box'
                                >
                                    <BsListUl />
                                </Button>
                            </LeftChatEditor>

                            <RightChatEditor>
                                <Button
                                    variant='light'
                                    className='btn-inputfield-box'
                                >
                                    <FiAtSign />
                                </Button>
                                <Button
                                    variant='light'
                                    className='btn-inputfield-box'
                                >
                                    <FiPaperclip />
                                </Button>
                                <Button
                                    type='submit'
                                    onClick={sendMessage}
                                    onKeyDown={sendMessage}
                                    className='send-btn-box btn-inputfield-box'
                                    disabled={messageInput}
                                >
                                    <span className='sendMessage'>
                                        <IoMdSend />
                                    </span>
                                    <span className='dm-schedule-message'>
                                        <FaAngleDown />
                                    </span>
                                </Button>
                            </RightChatEditor>
                        </ChatInputEditor>
                    </form>
                </InputContainer>
            </Container>
        </div>
    );
};

export default dmBoxInputField;

const Container = styled.div`
    background-color: #fff;
    padding-left: 16px;
    padding-right: 16px;
    padding-bottom: 24px;
`;

const InputContainer = styled.div`
    border: 1px solid #ebebeb;
    border-radius: 3px;

    form {
        display: flex;
        flex-direction: column;
        height: min-content;
        align-items: space-evenly;

        padding-left: 5px;
        padding-right: 5px;
        padding-top: 10px;
        padding-bottom: 5px;

        textarea {
            flex: 1;
            border: none;
            font-size: 15px;
            background: transparent;
            resize: none;
            overflow: hidden;
        }

        textarea:focus {
            outline: none;
        }
    }
`;

const ChatInputEditor = styled.div`
    display: flex;
    align-items: center;
    justify-content: space-between;
`;

const LeftChatEditor = styled.div`
    display: flex;
    align-items: center;
`;

const RightChatEditor = styled.div`
    display: flex;
    align-items: center;
`;

const SendButton = styled.div`
    background: #007a5a;
    color: #d9d9d9;
    border-radius: 5px;
    width: 32px;
    height: 32px;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: 0.25s ease;

    :hover {
        transform: scale(0.9);
    }
`;
