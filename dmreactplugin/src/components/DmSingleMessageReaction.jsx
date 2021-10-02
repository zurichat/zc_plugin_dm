import React from "react";
import styled from "styled-components";
import profilePic from "./beke.jpg";
import { VscReactions } from "react-icons/vsc";
import { GrEmoji } from "react-icons/gr";

const ReactionContainer = styled.div`
  margin-left: 60px;
  margin-top: 0;
  > img {
    height: 20px;
    border-radius: 5px;
    margin-right: 5px;
  }
  > .replies-details {
    display: flex;
  }
  > .replies-details > p {
    margin-right: 10px;
  }
`;
const Emojis = styled.div`
  .icon {
    font-size: 20px;
  }
  margin-left: 60px;
  display: flex;
`;
const DmSingleMessageReaction = () => {
  return (
    <div>
      <Emojis>
        <div className="single-emoji">
          <GrEmoji className="icon" />
        </div>
        <div>
          <VscReactions className="icon" />
        </div>
      </Emojis>
      <ReactionContainer>
        <img src={profilePic} alt="" />
        <img src={profilePic} alt="" />
        <img src={profilePic} alt="" />
        <img src={profilePic} alt="" />
        <div className="replies-details">
          <p>4 replies</p>
          <p>Last reply 1 hour ago</p>
        </div>
      </ReactionContainer>
    </div>
  );
};

export default DmSingleMessageReaction;
