import React from 'react';
import SearchUsers from './SearchUsers';
import { useSelector } from 'react-redux';
import './AllDms.css'

const AllDms = ()=>{
    const membersReducer = useSelector(({ membersReducer }) => membersReducer);

    console.log(membersReducer)
    const orgUsers = membersReducer && membersReducer;
    // const orgUsers = [
    //     {
    //         _id: "6145f987285e4a18402074eb",
    //         user_name: "seunpaul",
    //         first_name: "Seun",
    //         last_name: "Oluwafemi",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a44202074eb",
    //         user_name: "casper",
    //         first_name: "Tobi",
    //         last_name: "Amasa",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a18472074eb",
    //         user_name: "andy",
    //         first_name: "Anu",
    //         last_name: "Adewale",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a18402174ec",
    //         user_name: "fado",
    //         first_name: "Fuad",
    //         last_name: "Agboola",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a18402084ed",
    //         user_name: "richycool",
    //         first_name: "Richard",
    //         last_name: "Olufarati",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285b4a18402074eb",
    //         user_name: "damiDev",
    //         first_name: "Dami",
    //         last_name: "Smith",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a18404474eb",
    //         user_name: "Haywhy._Online",
    //         first_name: "Ayo",
    //         last_name: "Amoo",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f457285e4a18402074eb",
    //         user_name: "wallyStrinGs",
    //         first_name: "Wale",
    //         last_name: "Ademilola",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a18542074eb",
    //         user_name: "LaCasera",
    //         first_name: "David",
    //         last_name: "Adeoye",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987272e4a18402074eb",
    //         user_name: "INEC",
    //         first_name: "Damilare",
    //         last_name: "Atanda",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     }
    // ]

    return(
        <div className='alldms'>
            <header className='alldms-header d-flex align-items-center'>
                <div className='alldms-header-text d-flex align-items-center'>
                    <h5>#</h5>
                    <p>All direct messages</p>
                </div>
            </header>
            <SearchUsers orgUsers = {orgUsers}/>
        </div>
    )
};

export default AllDms;