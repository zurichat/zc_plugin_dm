import React, { useState } from "react";
import { FaGoogleDrive } from "react-icons/fa";
import { RiComputerLine } from "react-icons/ri";
import "./attachfile.css";
import img from "./Rectangle.jpg";

const AttachFile = () => {
  const [uploadModal, setUploadModal] = useState("block");
  const handleUpload = (event) => {
    console.log(event.target.files);
  };
  return (
    <>
      {/* <button onClick={() => setUploadModal('block')}>attach</button> */}
      <div
        className="dm-plugin-attach-file"
        style={{ display: `${uploadModal}` }}
      >
        <div className="dm-plugin-files">
          <p>Your recent files</p>
          <div className="recent-files">
            <img src={img} alt="" className="image" />
            <div className="image-details">
              <h4>HNG Task 1.jpg</h4>
              <p>7 sept</p>
            </div>
          </div>
          <div className="recent-files">
            <img src={img} alt="" className="image" />
            <div className="image-details">
              <h4>HNG Task 2.jpg</h4>
              <p>2 sept</p>
            </div>
          </div>
          <div className="recent-files">
            <img src={img} alt="" className="image" />
            <div className="image-details">
              <h4>HNG Task 3.jpg</h4>
              <p>1 sept</p>
            </div>
          </div>
          <p className="all-files">View all your files</p>
        </div>
        <div className="dm-plugin-upload-files">
          <p>Add a file from...</p>
          <div className="google-drive">
            <FaGoogleDrive className="google-drive-icon" />
            <span>Google Drive</span>
          </div>
          <label
            htmlFor="upload-btn"
            className="computer"
            onClick={() => setUploadModal("none")}
          >
            <RiComputerLine className="computer-icon" />
            <span>Upload from your computer</span>
          </label>
          <input
            type="file"
            id="upload-btn"
            multiple={true}
            onChange={handleUpload}
          />
        </div>
      </div>
    </>
  );
};

export default AttachFile;
