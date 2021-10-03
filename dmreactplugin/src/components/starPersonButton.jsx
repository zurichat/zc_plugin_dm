import React, { useState, useRef, useEffect } from "react";
import { useLocation } from "react-router";
import style from "styled-components";
import instance from "../utils/apiServices";

const StyledStarInterior = style.div`
clip-path: polygon(
    50% 0%,
    61% 35%,
    98% 35%,
    68% 57%,
    79% 91%,
    50% 70%,
    21% 91%,
    32% 57%,
    2% 35%,
    39% 35%
);
-webkit-clip-path: polygon(
    50% 0%,
    61% 35%,
    98% 35%,
    68% 57%,
    79% 91%,
    50% 70%,
    21% 91%,
    32% 57%,
    2% 35%,
    39% 35%
);
height: 100%;
width: 100%;
background-color: white;
height: 100%;
`;
const StyledStar = style.div`
-webkit-clip-path: polygon(
    50% 0%,
    61% 35%,
    98% 35%,
    68% 57%,
    79% 91%,
    50% 70%,
    21% 91%,
    32% 57%,
    2% 35%,
    39% 35%
);

clip-path: polygon(
    50% 0%,
    61% 35%,
    98% 35%,
    68% 57%,
    79% 91%,
    50% 70%,
    21% 91%,
    32% 57%,
    2% 35%,
    39% 35%
);
padding: 4px;
height: 20px;
width: 20px;
background-color: black;
`;

const StyledButton = style.button`
padding: 10px;
border: none;
background-color: transparent;
`;

export default function StarButtonButton() {
    const location = useLocation();
    let [org_id, room_id, loggedInUser_id] = location.pathname
        .split("/")
        .filter((string) => string.length > 11);
    const [isStared, setStared] = useState(false);
    const [isDisabled, setDisabled] = useState(false);
    const apiInstance = instance;

    useEffect(() => {
        async function initialData() {
            try {
                setDisabled(true);
                const response = await apiInstance.getStarPersonInfo(
                    org_id,
                    room_id,
                    loggedInUser_id
                );
                if (response.status == 200) {
                    const data = JSON.parse(response.data);

                    if (data) {
                        if (data.status) {
                            setStared(data.status);
                        }
                    }
                }
                setDisabled(false);
            } catch (e) {
                setDisabled(false);
            }
        }
        initialData();
    }, []);

    const starMessage = async () => {
        try {
            setDisabled(true);

            const response = await apiInstance.starPerson(
                org_id,
                room_id,
                loggedInUser_id
            );
            if (response.status === 200) {
                setStared(!isStared);
            }
            setDisabled(false);
        } catch (e) {
            setDisabled(false);
        }
    };

    return (
        <StyledButton
            title={`${isStared ? "remove from starred" : "star person"}`}
            onClick={isDisabled ? () => {} : starMessage}
        >
            <StyledStar
                style={{ backgroundColor: `${isStared ? "#00b87c" : ""}` }}
            >
                <StyledStarInterior
                    style={{ backgroundColor: `${isStared ? "#00b87c" : ""}` }}
                ></StyledStarInterior>
            </StyledStar>
        </StyledButton>
    );
}
