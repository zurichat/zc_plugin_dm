import React, { useState, useEffect } from "react";

import ModalButton from "../../pinnedMessage/button";
import Close from "../../../../assets/img/svg/close.svg";
import TextField from "../modalTextFields/textField";
import AddBookmarkModal from "./addBookmarkModal";
import NameTextField from "../modalTextFields/nameLinkTextField";

const AddBookmarkLink = ({ opened, onClose, initialLink }) => {
  //initialLink is the initial bookmark if any
  //opened is a boolean for if the modal should open
  //onClose is to reset the parent components opened value to false
  const [closed, setClose] = useState(opened);
  const [isLink, setIsLink] = useState(false);
  useEffect(() => {
    if (opened) {
      setClose(opened);
    }
  }, [opened]);
  let onClosed = () => {
    setClose(false);
    onClose();
  };
  const Button = (
    <>
      <NameTextField label="Name" placeholder="Name" onChange={onNameChange} />
      <div className="d-flex justify-content-end">
        <ModalButton
          onClick={() => {
            setClose(false);
            onClose();
          }}
          close
        >
          Cancel
        </ModalButton>
        <ModalButton>Add</ModalButton>
      </div>
    </>
  );
  const onLinkChange = (value) => {
    //value is the text value as link textfield changes
    const regex1 =
      /((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)/;
    const regex2 =
      /(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})/;
    const isUrl = regex2.test(value);
    setIsLink(isUrl);
  };

  const onNameChange = (value) => {
    //value is the text value as name textfield changes
  };
  return (
    <AddBookmarkModal onClose={onClosed} close={closed}>
      <div
        className="d-flex flex-column p-4 w-50 gap-3 bg-white rounded-1"
        role="presentation"
        onClick={(e) => {
          e.stopPropagation();
        }}
      >
        <div
          className="d-flex justify-content-between text-capitalize align-items-center"
          style={{
            fontSize: "30px",
            fontWeight: "700",
            height: "20px",
          }}
        >
          <div className="writeUp">Add a Bookmark</div>
          <img
            src={Close}
            alt="close"
            className="d-block h-75"
            role="presentation"
            onClick={() => {
              setClose(false);
              onClose();
            }}
          />
        </div>
        <div>
          <TextField
            placeholder="Link"
            value={initialLink}
            label="Link"
            onChange={onLinkChange}
          />
        </div>
        {isLink ? Button : null}
      </div>
    </AddBookmarkModal>
  );
};

export default AddBookmarkLink;
