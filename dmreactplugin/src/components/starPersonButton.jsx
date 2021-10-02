import React, { useState } from "react";
import style from "styled-components";

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
    const [isStared, setStared] = useState(false);

    return (
        <StyledButton
            title={`${isStared ? "remove from starred" : "star person"}`}
            onClick={() => {
                setStared(!isStared);
            }}
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
