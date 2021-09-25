import React from "react";
import style from "styled-components";

const ModalButton = ({ close, onClick, children }) => {
  const Button = style.button`
    border: ${close ? "1px solid grey" : "none"};
    width: 100px;
    padding:10px;
    background-color: ${close ? "transparent" : "green"};
    margin-right:${close ? "10px" : "0"};
    color: ${close ? "black" : "white"}
    `;

  return <Button onClick={onClick}>{children}</Button>;
};

export default ModalButton;
