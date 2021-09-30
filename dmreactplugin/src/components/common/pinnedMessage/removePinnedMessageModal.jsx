import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

import ModalButton from "./button";
import close from "../../../assets/img/svg/close.svg";
const RemovePinnedMessage = ({ reset, messageBody, time }) => {
    const [show, setShow] = useState(true);
    return (
        <div
            onClick={() => {
                setShow(false);
                reset();
            }}
            role="presentation"
            className={`${
                show ? "d-flex" : "d-none"
            } fixed-top h-100 w-100 flex-column justify-content-center align-items-center zindex-modal`}
            style={{ backgroundColor: "rgba(0,0,0,0.4)" }}
        >
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
                    <div className="writeUp">remove pinned item</div>
                    <img
                        src={close}
                        alt="close"
                        role="presentation"
                        className="d-block h-75"
                        onClick={() => {
                            setShow(false);
                            reset();
                        }}
                    />
                </div>
                <p className="mb-0 text-start">
                    Are you sure you want to remove this pinned item?
                </p>
                <div className="border border-dark p-3 mb-3 text-start">
                    <p className="mb-1">{messageBody}</p>
                    <span className="d-block text-secondary">{time}</span>
                </div>
                <div className="d-flex justify-content-end">
                    <ModalButton
                        onClick={() => {
                            setShow(false);
                            reset();
                        }}
                        close
                    >
                        Cancel
                    </ModalButton>
                    <ModalButton>Remove</ModalButton>
                </div>
            </div>
        </div>
    );
};

export default RemovePinnedMessage;
