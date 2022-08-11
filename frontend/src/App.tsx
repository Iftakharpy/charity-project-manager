import React from 'react'
import { Routes, Route } from 'react-router-dom'
import { IconContext } from "react-icons";

import { BaseLayout } from './layouts/BaseLayout'

import { UserProfileComponent } from './features/userFeature/userProfileComponent'
import { LoginPage } from './pages/login/LoginPage';
import { NotFoundPage } from './pages/NotFound/NotFoundPage';


import './tailwind.css'


export function App() {
  return <IconContext.Provider value={{ className: "react-icons" }}>
    <Routes>
      <Route  path="/" element={<BaseLayout/>}>
        <Route index element={<UserProfileComponent/>}/>
        <Route path='about/' element={"about"}/>
        <Route path='login/' element={<LoginPage/>}/>
        <Route path='*' element={<NotFoundPage/>}/>
      </Route>
    </Routes>
  </IconContext.Provider>
}


export default App
