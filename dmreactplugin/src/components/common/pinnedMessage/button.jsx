import React from "react";
import style from "styled-components";

const ModalButton = ({ close, children }) => {
  const Button = style.button`
    border: ${close ? "1px solid grey" : "none"};
    width: 100px;
    padding:10px;
    background-color: ${close ? "transparent" : "green"};
    margin-right:${close ? "10px" : "0"};
    color: ${close ? "black" : "white"}
    `;

  return (
    <Button
      onClick={() => {
        console.log("onClickListener");
      }}
    >
      {children}
    </Button>
  );
};

export default ModalButton;
