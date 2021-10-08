import React, { useEffect, useState, useRef } from 'react'
import { useDispatch, useSelector } from 'react-redux'
// import { subscribetoChannel } from '@zuri/control';
import { handleCreateRoomMessages } from '../Redux/Actions/dmActions'

// import styling
import styled from 'styled-components'
import '../assets/css/dmBoxInput.css'

// import icons
import { IoMdSend } from 'react-icons/io'
import { FaAngleDown } from 'react-icons/fa'
import {
  BsLightning,
  BsLink45Deg,
  BsListUl,
  BsTypeItalic,
} from 'react-icons/bs'
import { FiAtSign, FiBold, FiPaperclip } from 'react-icons/fi'
import { Button } from 'react-bootstrap'
// import ApiServices from '../utils/apiServices';

const dmBoxInputField = ({ org_id, room_id, loggedInUser_id }) => {
  // controls inputfield text style e.g italic, bold, border
  const [textStyle, setTextStyle] = useState({ border: '1px solid #e3e3e3' })

  // messageInput value from text-area
  const [messageInput, setMessageInput] = useState()

  const dispatch = useDispatch()

  // save text-area value to messageInput state
  const handleInput = (e) => {
    // do something
    setMessageInput(e.target.innerHTML)
  } 

  // send message to backend
  const sendMessage = (e) => {
    e.preventDefault()
    //console.log("param",org_id,room_id)
    if (!messageInput) return;
        const data={
            "sender_id":loggedInUser_id,
            "message":messageInput
        }
    // ApiServices.postMessageThread(org_id, room_id, "61584d6e87675da1c20179fa", data).then(response=>{
    //   console.log(response);
    dispatch(handleCreateRoomMessages(org_id,room_id, data))

    setMessageInput('')
  }
  // messageSend(messageInput);
  // setMessageInput('');
  // inputRef.current.innerHTML = ''

  //Resizeable contenteditable Input function
  //     useEffect(() => {
  //         refContainer.current.focus();
  //     }, [focus]);

  // change text-area element style
  const changeStyle = (e) => {
    switch (e) {
      // change style to italic
      case 1:
        let style = {
          fontStyle: clikedItalic ? 'normal' : 'italic',
        }
        setTextStyle({ ...style })
        setClicked(!clikedItalic)
        break
      // increase font-weight / change text style to bold
      case 2:
        setTextStyle({
          fontStyle: !clikedItalic ? 'normal' : 'italic',
          fontWeight: clikedBold ? 400 : 900,
        })
        setClicked2(!clikedBold)
        break
    }
  }

  // <input type='file'> -- controls render state for select attach elem
  const [inputKey, setInputKey] = useState('some-key')
  // state for attached file image url
  const [attached, setAttached] = useState(null)
  // ref to control attach input dom
  const attachRef = React.createRef()
  const toggleAttach = (e) => {
    attachRef.current.click()
  }
  // save attach file url to 'attached' state
  const attachFile = (e) => {
    if (e.target.files && e.target.files[0]) {
      setAttached(URL.createObjectURL(e.target.files[0]))
    }
  }
  // on click clear attached file
  const clearAttached = (e) => {
    setInputKey('reset-attached')
    setAttached('')
  }

  // pop-up random link
  const alertRandomLink = (e) => {
    let randString = window.location.href
    alert(`copy ${randString}`)
  }

  // ref for text-area elem
  const inputRef = React.createRef()
  // control button clicked or not
  const [clicked3, changeInputStyle] = useState(false)
  // change message input text style to list
  const listStyle = (e) => {
    let new_format = messageInput
    new_format = messageInput
      .split(!clicked3 ? 'div' : 'li')
      .join(!clicked3 ? 'li' : 'div')
    setMessageInput(new_format)
    inputRef.current.innerHTML = new_format
    // console.log(new_format);
    changeInputStyle(!clicked3)
  }

  // add @ to message Input string
  const mention = (e) => {
    setMessageInput(messageInput + '@')
    inputRef.current.innerHTML += '@'
  }

  return (
    <div className='dm-inputbox-container'>
      <Container>
        <InputContainer>
          {/* preview uploaded file */}
          <img
            key={inputKey || ''}
            style={{
              display: !!attached == false ? 'none' : 'block',
            }}
            src={attached}
            alt='preview attached'
          />
          {/* clear uploaded file */}
          <button
            onClick={clearAttached}
            style={{
              display: !!attached == false ? 'none' : 'block',
            }}
          >
            clear attached
          </button>
          <form>
            {/* hidden attach file */}
            <input
              key={inputKey || ''}
              onChange={attachFile}
              ref={attachRef}
              type='file'
              style={{
                visibility: 'hidden',
                position: 'absolute',
                zIndex: -9999,
              }}
              name=''
              id=''
            />
            {/* <div
              ref={inputRef}
              contentEditable={true}
              style={textStyle}
              rows='2'
              type='text'
              // textInputResize={textInputResize}
              onInput={handleInput}
              className='px-2 p-3'
            >
              <div>Send Message To</div>
            </div> */}
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
                  onClick={e => changeStyle(2)}
                  variant='light'
                  className='btn-inputfield-box'
                >
                  <FiBold />
                </Button>
                <Button
                  onClick={(e) => changeStyle(1)}
                  variant='light'
                  className='btn-inputfield-box'
                >
                  <BsTypeItalic />
                </Button>
                <Button
                  onClick={alertRandomLink}
                  variant='light'
                  className='btn-inputfield-box'
                >
                  <BsLink45Deg />
                </Button>
                <Button
                  onClick={listStyle}
                  variant='light'
                  className='btn-inputfield-box'
                >
                  <BsListUl />
                </Button>
              </LeftChatEditor>

              <RightChatEditor>
                <Button
                  onClick={mention}
                  variant='light'
                  className='btn-inputfield-box'
                >
                  <FiAtSign />
                </Button>
                <Button
                  onClick={toggleAttach}
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
                  //disabled={!messageInput}
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
  )
}

export default dmBoxInputField

const Container = styled.div`
  background-color: #fff;
  padding-left: 16px;
  padding-right: 16px;
  padding-bottom: 24px;
`

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
`

const ChatInputEditor = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
`

const LeftChatEditor = styled.div`
  display: flex;
  align-items: center;
`

const RightChatEditor = styled.div`
  display: flex;
  align-items: center;
`
