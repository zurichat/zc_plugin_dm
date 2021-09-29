import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

import Pin from "../../../assets/img/svg/pin.svg";
import HoverPinnedMessage from "./hoverViewPinned";

const PinnedMessage = () => {
    const [open, setOpen] = useState(false);
    let check = [
        {
            imgSrc: "https://picsum.photos/200",
            time: "today at 5:35AM",
            messageBody:
                "keep learning we grow every day, be proud of how far you've come",
        },
        {
            imgSrc: "https://picsum.photos/200",
            time: "yesterday at 5:35AM",
            messageBody: "whats up have you added that stuff to the body",
        },
        {
            imgSrc: "https://picsum.photos/200",
            time: "yesterday at 1:05AM",
            messageBody: "please finish up the pinned message objective",
        },
    ];
    const onHoverMouseOut = () => {
        setOpen(false);
    };

    let dropDownMessages = check.map((item, i) => (
        <div key={i}>
            <HoverPinnedMessage
                imgSrc={item.imgSrc}
                time={item.time}
                messageBody={item.messageBody}
                revert={onHoverMouseOut}
            />
        </div>
    ));
    return (
        <button
            className="d-inline-flex btn gap-1 px-1 py-1 align-items-center rounded-3 position-relative"
            style={{
                height: "30px",
                backgroundColor: "#BCF9E6",
                fontSize: "13px",
            }}
            onClick={() => {
                setOpen(!open);
            }}
            onMouseLeave={onHoverMouseOut}
        >
            <img src={Pin} alt="pin" className="p-1 h-100" />
            <div>{`${check.length} Pinned`}</div>

            {open ? (
                <div
                    className="position-absolute bg-white shadow-sm p-3"
                    style={{ width: "400px", top: "100%", zIndex: "10" }}
                    aria-hidden
                    onClick={(e) => {
                        e.stopPropagation();
                    }}
                >
                    {dropDownMessages}
                </div>
            ) : null}
        </button>
    );
};

export default PinnedMessage;
