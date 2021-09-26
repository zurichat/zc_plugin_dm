import React from "react";
import styled from "styled-components";
const MessageBox = () => {
  const Image = styled.img`
    object-fit: cover;
    margin-right: 10px;
  `;

  return (
    <div className="dm-plugin-thread-message-group">
      <div className="dm-plugin-thread-message-image-container">
        <Image
          src="https://www.pixsy.com/wp-content/uploads/2021/04/ben-sweet-2LowviVHZ-E-unsplash-1.jpeg"
          alt=""
          width="36"
          height="36"
          className="dm-plugin-thread-message-image"
        />
      </div>
      <div className="dm-plugin-thread-message-body">
        <p className="dm-plugin-thread-message-header">
          <span className="dm-plugin-thread-message-username">John Doe</span>
          <span className="dm-plugin-thread-message-date-time">YYMMDD:AM</span>
        </p>
        <p className="dm-plugin-thread-message-text">
          It is a long established fact that a reader will be distracted by the
          readable content of a page when looking at its layout.
        </p>
      </div>
    </div>
  );
};

export default MessageBox;
