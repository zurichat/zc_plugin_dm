import React, { useState } from "react";
import styled from "styled-components";

import link from "../../../../assets/img/svg/link.svg";

const StyledTextField = styled.input`
  border: none;
  outline: none;
  &:focus {
    outline: none;
  }
`;
const StyledNameTextField = styled.div`
  border: 2px solid gray;
  border-radius: 0.25rem;
  display: flex;
  width: 100%;
  &:focus-within {
    border: 2px solid #00b87c;
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
    <div className="d-flex flex-column gap-1 align-items-start">
      <label htmlFor={label} style={{ fontSize: "20px" }}>
        {label}
      </label>
      <StyledNameTextField className="px-3">
        <img src={link} alt="link" />
        <StyledTextField
          type="text"
          className="d-block w-100 p-3 text-secondary rounded-2"
          required
          placeholder={placeholder}
          value={val}
          onChange={textChange}
          id={label}
        />
      </StyledNameTextField>
    </div>
  );
};

export default NameTextField;
