import React from "react";
import styled from "styled-components";

import { VscReactions } from "react-icons/vsc";

const ReactionContainer = styled.div`
  margin-left: 60px;
  margin-top: 0;
  font-size: 12px;
  display: flex;

  > .replies-images > img {
    height: 18px;
    width: 18px;
    border-radius: 5px;
    margin-right: 5px;
    cursor: pointer;
  }
  > .replies-details {
    display: flex;
  }
  > .replies-details > p {
    margin-right: 10px;
  }
  .grey {
    color: #616061;
  }
  .blue {
    color: #1264a3;
    :hover {
      cursor: pointer;
      text-decoration: underline;
    }
  }
`;
const Emojis = styled.div`
  margin-left: 60px;
  margin-bottom: 5px;
  display: flex;

  .emoji-container {
    background: #efefef;
    margin-right: 5px;
    border-radius: 30%;
    width: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .current-reactions {
    display: flex;
    align-items: center;
  }
`;
const DmSingleMessageReaction = ({ user, handleOpenThread }) => {
  return (
    <>
      <Emojis>
        <div className="emoji-container">😉1</div>
        <div className="emoji-container">
          <VscReactions className="icon" />
        </div>
      </Emojis>
      <ReactionContainer onClick={handleOpenThread}>
        <div className="replies-images">
          <img src={user?.image_url} alt="" />
        </div>
        <div className="replies-details">
          <p className="blue">4 replies</p>
          <p className="grey">Last reply 1 hour ago</p>
        </div>
      </ReactionContainer>
    </>
  );
};

export default DmSingleMessageReaction;
