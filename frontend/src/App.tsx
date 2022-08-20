import React from 'react'
import { Routes, Route } from 'react-router-dom'
import { IconContext } from "react-icons";

import { BaseLayout } from './layouts/BaseLayout'

import { UserProfileComponent } from './features/userFeature/userProfileComponent'
import { LoginPage } from './pages/login/LoginPage';
import { NotFoundPage } from './pages/notFound/NotFoundPage';


import './tailwind.css'
import LogoutPage from './pages/logout/LogoutPage';


export function App() {
  return <IconContext.Provider value={{ className: "react-icons" }}>
    <Routes>
      <Route  path="/" element={<BaseLayout/>}>
        <Route index element={<UserProfileComponent/>}/>
        <Route path='about/' element={"about"}/>
        <Route path='login/' element={<LoginPage/>}/>
        <Route path='logout/' element={<LogoutPage/>}/>
        <Route path='*' element={<NotFoundPage/>}/>
      </Route>
    </Routes>
  </IconContext.Provider>
}


export default App
