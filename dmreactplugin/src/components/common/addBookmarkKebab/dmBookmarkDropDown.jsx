import React, { useState } from "react";
import styled from "styled-components";
import link from "../../../assets/img/svg/link.svg";
import AddBookmarkLink from "./modal/addBookmarkLink";

const StyledDiv = styled.div`
  padding: 10px;
  background-color: white;
  display: grid;
  grid-template-columns: repeat(2, max-content);
  grid-template-rows: repeat(2, min-content);
  align-items: flex-center;
  justify-items: flex-start;
  line-height: 1;
  column-gap: 5px;

  &:hover {
    background-color: #e1fdf4;
  }
`;
const StyledImg = styled.img`
  height: 100%;
  width: auto;
  display: block;
  padding: 5px;
  background-color: white;
  box-sizing: border-box;
`;

const StyledImgCover = styled.div`
  height: 100%;
  grid-row: 1 / -1;
  padding: 5px;
`;

const AddBookmarkDropDown = () => {
  let [open, setOpen] = useState(false);
  let openModal = () => {
    setOpen(true);
  };
  let closeModal = () => {
    setOpen(false);
  };
  return (
    <>
      <StyledDiv onClick={openModal}>
        <StyledImgCover>
          <StyledImg src={link} alt="link" />
        </StyledImgCover>
        <h6 className="mb-0 pb-0">Add a bookmark</h6>
        <div className="mb-0 pb-0">Easily find your teams important links</div>
        <AddBookmarkLink opened={open} onClose={closeModal} />
      </StyledDiv>
    </>
  );
};

export default AddBookmarkDropDown;
