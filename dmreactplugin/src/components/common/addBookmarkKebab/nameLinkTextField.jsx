import React, { useState } from "react";
import styled from "styled-components";

import link from "../../../assets/img/svg/link.svg";
const StyledTextField = styled.input`
  border: none;
  outline: none;

  &:focus {
    border: none;
    outline: none;
  }
`;
const StyledNameTextField = styled.div`
  border: 2px solid grey;
  border-radius: 0.25rem;

  &:focus {
    border-color: #00b87c;
  }
`;

const NameTextField = ({ placeholder, label, value, onChange }) => {
  let textValue = value;
  const [val, setTextValue] = useState(textValue);
  const textChange = (e) => {
    textValue = e.target.value;
    setTextValue(textValue);
    onChange(e.target.value);
  };
  return (
    <div className="d-flex flex-column gap-1">
      <label htmlFor={label} style={{ fontSize: "20px" }}>
        {label}
      </label>
      <div className="">
        <img src={link} alt="link" className="some" />
        <StyledTextField
          type="text"
          className="d-block w-100 p-3 text-secondary rounded-2"
          required
          placeholder={placeholder}
          value={val}
          onChange={textChange}
          id={label}
        />
      </div>
    </div>
  );
};

export default NameTextField;
