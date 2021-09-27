import React, { useState, useEffect } from "react";

const AddBookmarkModal = ({ close, children, onClose }) => {
  const [show, setShow] = useState(close);
  useEffect(() => {
    if (!close && show) {
      setShow(close);
      onClose();
    } else {
      setShow(close);
    }
  }, [close, show]);

  return (
    <div
      role="presentation"
      onClick={() => {
        onClose();
      }}
      className={`${
        show ? "d-flex" : "d-none"
      } fixed-top h-100 w-100 flex-column justify-content-center align-items-center zindex-modal`}
      style={{ backgroundColor: "rgba(0,0,0,0.4)" }}
    >
      {children}
    </div>
  );
};

export default AddBookmarkModal;
