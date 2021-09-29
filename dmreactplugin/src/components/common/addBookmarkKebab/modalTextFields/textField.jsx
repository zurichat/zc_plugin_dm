import React, { useState } from "react";
import styled from "styled-components";

const StyledTextField = styled.input`
  border: 2px solid grey;
  outline: none;

  &:focus {
    border: 2px solid #00b87c !important;
    outline: none;
  }
`;

const TextField = ({ placeholder, label, value, onChange }) => {
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
  );
};

export default TextField;
