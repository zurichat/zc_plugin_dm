import React, { useState, useRef, useEffect } from "react";
import { BiPlus } from "react-icons/bi";
import "./dmBookmarkStyle.css";
import AddBookmarkDropDown from "./dmBookmarkDropDown";


{
    /* <div className='addBookmark-overlay'>
                <div className='container mx-auto pt-3 pb-3 addBookmark'>
                    <div className='row d-flex pt-2 pb-2 mb-3 bookmark-link'>
                        <div className='col-auto align-self-center link-btn'>
                            <button className='col-auto p-2 btn-outline-disabled'>
                                <AiOutlinePaperClip />
                            </button>
                        </div>
                        <div className='col bookmark_description ps-0'>
                            <h2 className='m-0'></h2>
                            <p></p>
                        </div>
                    </div>
                    <hr />
                    <span className=''>Add recent</span>
                </div>
            </div> */
}

const DmBookMarkHeader = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [bookmarks, setBookmark] = useState([]);
    function getBookMark() {
        fetch("https://dm.zuri.chat/api/v1/org/614679ee1a5607b13c00bcb7/rooms/615110993036822db275f738/bookmarks")
            .then(data => data.json())
            .then(data => {
                console.log(data);
                setBookmark(data);
            });
    }

    useEffect(() => {
        getBookMark();
    }, []);


    const HoverOutStop = useRef(false);
    const onHoverMouseOut = () => {
        if (HoverOutStop.current) {
        } else {
            setIsOpen(false);
        }
    };
    function renderBookmark() {
        var returnHTML = "";
        if (bookmarks.length > 0) {
            returnHTML = bookmarks.map((bookmark) => {
                return (
                    <div className="display-bookmark" key={name}>
                        <h3 className="display-bookmark-link">{bookmark.link}</h3>
                        <h4 className="display-bookmark-name">{bookmark.name} - {bookmark.created_at} </h4>
                    </div>
                )

            })
        } else {
            returnHTML = < p className="pl-3 text-start" > No recent links</p >;
        }

        return returnHTML;
    }

    return (
        <>
        <button
            className="position-relative btn btn-add-bookmark d-flex align-items"
            onClick={() => {
                setIsOpen(!isOpen);
            }}
            onMouseLeave={onHoverMouseOut}
        >
            <BiPlus />
            <p className="m-0">Add a bookmark</p>
            {isOpen ? (
                <div
                    className="position-absolute bg-white shadow-sm p-3 dropDown-zindex d-flex flex-column gap-2"
                    style={{ width: "400px", top: "100%", left: "0" }}
                    aria-hidden
                    onClick={(e) => {
                        e.stopPropagation();
                    }}
                >
                    <AddBookmarkDropDown
                        onOpenModal={(value) => {
                            HoverOutStop.current = value;
                        }}
                    />
                    <div className="border-bottom border-secondary">
                    </div>
                    {renderBookmark()}
                </div>
            ) : null}
        </button>
        </>
    );
};

export default DmBookMarkHeader;
