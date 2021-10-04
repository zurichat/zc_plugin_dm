import React from 'react';
import SearchUsers from './SearchUsers';
import { useSelector } from 'react-redux';
import './AllDms.css'

const AllDms = ({org_id, loggedInUser_id})=>{
    const membersReducer = useSelector(({ membersReducer }) => membersReducer);

    const orgUsers = membersReducer;

    // const orgUsers = [
    //     {
    //         _id: "6145f987285e4a18402074eb",
    //         user_name: "seunpaul",
    //         first_name: "Seun",
    //         last_name: "Oluwafemi",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a44202074eb",
    //         user_name: "casper",
    //         first_name: "Tobi",
    //         last_name: "Amasa",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a18472074eb",
    //         user_name: "andy",
    //         first_name: "Anu",
    //         last_name: "Adewale",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a18402174ec",
    //         user_name: "fado",
    //         first_name: "Fuad",
    //         last_name: "Agboola",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a18402084ed",
    //         user_name: "richycool",
    //         first_name: "Richard",
    //         last_name: "Olufarati",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285b4a18402074eb",
    //         user_name: "damiDev",
    //         first_name: "Dami",
    //         last_name: "Smith",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a18404474eb",
    //         user_name: "Haywhy._Online",
    //         first_name: "Ayo",
    //         last_name: "Amoo",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f457285e4a18402074eb",
    //         user_name: "wallyStrinGs",
    //         first_name: "Wale",
    //         last_name: "Ademilola",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987285e4a18542074eb",
    //         user_name: "LaCasera",
    //         first_name: "David",
    //         last_name: "Adeoye",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     },
    //     {
    //         _id: "6145f987272e4a18402074eb",
    //         user_name: "INEC",
    //         first_name: "Damilare",
    //         last_name: "Atanda",
    //         email: "seunpaul148@gmail.com",
    //         image_url: "https://res.cloudinary.com/ds5l1k3bl/image/upload/v1629593472/user_scepnk.jpg"
    //     }
    // ]

    return(
        <div className='alldms'>
            <header className='alldms-header d-flex align-items-center'>
                <div className='alldms-header-text d-flex align-items-center'>
                    <p>#</p>
                    <p>All direct messages</p>
                </div>
            </header>
            <SearchUsers orgUsers = {orgUsers} org_id={org_id} loggedInUser_id={loggedInUser_id}/>
        </div>
    )
};

export default AllDms;