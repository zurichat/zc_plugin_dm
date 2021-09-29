import React, { useEffect, useState } from 'react'
import {
  BrowserRouter as Router,
  Route,
  Switch,
  useLocation,
} from 'react-router-dom'
export const AppContext = React.createContext()
// Import all Global CSS components
import 'bootstrap/dist/css/bootstrap.min.css'
import '../src/assets/css/global.module.css'

// Import all Router components
import ChatHome from './pages/newChatRoom'
import { useDispatch, useSelector } from 'react-redux'
import { handleGetRooms } from './Redux/Actions/dmActions'

const App = () => {
  const roomsReducer = useSelector(({ roomsReducer }) => roomsReducer)
  const dispatch = useDispatch()
  const [actualRoom, setActualRoom] = useState([])
  let location = useLocation()
  let [org_id, room_id, user_id] = location.pathname.split('/').filter(item => item.length > 11)

  // useEffect(() => {
    //   dispatch(
      //     // pass in the org_id and the user_id from the url
      //     handleGetRooms('614679ee1a5607b13c00bcb7', '6145f987285e4a18402074eb')
      //   )
      // }, [dispatch])
      
      // console.log(roomsReducer)
      const getActualRoom = async () => {
        const res = await fetch(
          `https://dm.zuri.chat/api/v1/sidebar?org=${org_id}&user=${user_id}`
          )
          const data = await res.json()
    const joinedRooms = data.joined_rooms
    const actualRoom = joinedRooms.filter(
      (room) => room.room_url === `/dm/${org_id}/${room_id}/${user_id}`
    )
    setActualRoom(actualRoom)
  }

  useEffect(() => {
    getActualRoom()
  }, [location])

  if (actualRoom.length === 0) {
    return <div>loading...</div>
  }
  return (
    <AppContext.Provider value={{ actualRoom }}>
      <Router basename='/dm'>
        <Switch>
          <Route exact path={`/${org_id}/${room_id}/${user_id}`}>
            <ChatHome />
          </Route>
        </Switch>
      </Router>
    </AppContext.Provider>
  )
}

export default App
