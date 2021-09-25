import React, { useState } from "react";
import profilePic from "../assets/profilepic.png";
import styled from "styled-components";

const Home = styled.div`
  width: 100%;
  height: 100vh;
  background: #c6c6c6;

  .home-top {
    display: flex;
    height: 50px;
    flex-direction: column;
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 99;
  }
  .plugin-name {
    margin-top: auto;
    margin-bottom: auto;
    padding: 12px;
    background: #00b87c;
    color: white;
  }
  & .search-box {
    display: flex;
    flex-direction: row;
    background: white;

    width: 100%;
    justify-content: center;
    padding: 10px;
  }
  & .search-box > .search-input {
    display: block;
    width: 100%;
    margin-left: 10px;
  }
  & .search-box > p {
    margin: auto;
    color: black;
  }
  & > .chats {
    margin-top: 20px;
    position: relative;
    top: 80px;
  }
  &.profile-pic {
  }
  & > .chats > .day-chat {
    background: white;
    margin-bottom: 20px;
    padding: 10px;
  }
  & > .chats > .day-chat > .chat {
    display: flex;
  }
  .search-input {
    outline: none;
    border: none;
  }
  .search-modal {
    background: white;
  }
  .black-text {
    color: black;
    font-weight: 500;
  }
  .message-time {
    position: absolute;
    right: 5px;
    top: 30%;
  }
  .chat {
    width: 100%;
    margin-bottom: 20px;

    position: relative;
  }
  .message-details {
    margin-left: 12px;
  }
`;
const ChatHomeMessages = () => {
  const [search, setSearch] = useState("");

  const handleSearch = (e) => {
    setSearch(e.target.value);
    console.log(search);
  };

  return (
    <Home>
      <div className="home-top">
        <p className="plugin-name">#All Direct Messages</p>
        <div className="search-box">
          <p>To:</p>
          <input
            value={search}
            onChange={handleSearch}
            className="search-input"
            placeholder="@somebody or somebody@example.com"
            type="text"
          />
        </div>
        {search[0] === "@" && (
          <div className="search-modal">
            <p>Lorem Ipsum</p>
            <p>Lorem Ipsum</p>
            <p>Lorem Ipsum</p>
            <p>Lorem Ipsum</p>
            <p>Lorem Ipsum</p>
            <p>Lorem Ipsum</p>
          </div>
        )}
      </div>

      <div className="chats">
        <div className="day-chat">
          <p className="black-text">Yesterday</p>
          <div className="chat">
            <div className="profile-pic">
              {" "}
              <img src={profilePic} alt="Picture" />
            </div>
            <div className="message-details">
              <p className="black-text">John Doe</p>
              <p>John Doe: Meeting starts in 1 hour bro. </p>
            </div>
            <p className="message-time">3:50PM</p>
          </div>
        </div>
        <div className="day-chat">
          <p className="black-text">Yesterday</p>
          <div className="chat">
            <div className="profile-pic">
              {" "}
              <img src={profilePic} alt="Picture" />
            </div>
            <div className="message-details">
              <p className="black-text">John Doe</p>
              <p>John Doe: Meeting starts in 1 hour bro. </p>
            </div>
            <p className="message-time">3:50PM</p>
          </div>
        </div>
        <div className="day-chat">
          <p className="black-text">Wednesday August 26th</p>
          <div className="chat">
            <div className="profile-pic">
              {" "}
              <img src={profilePic} alt="Picture" />
            </div>
            <div className="message-details">
              <p className="black-text">John Doe</p>
              <p>John Doe: Meeting starts in 1 hour bro. </p>
            </div>
            <p className="message-time">3:50PM</p>
          </div>
          <div className="chat">
            <div className="profile-pic">
              {" "}
              <img src={profilePic} alt="Picture" />
            </div>
            <div className="message-details">
              <p className="black-text">John Doe</p>
              <p>John Doe: Meeting starts in 1 hour bro. </p>
            </div>
            <p className="message-time">3:50PM</p>
          </div>
        </div>
      </div>
    </Home>
  );
};

export default ChatHomeMessages;
