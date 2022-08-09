import React, { useState } from 'react'
import { Routes, Route } from 'react-router-dom'
import { UserProfileComponent } from './features/userFeature/userProfileComponent'
import { BaseLayout } from './layouts/BaseLayout'
import { IconContext } from "react-icons";


import './tailwind.css'


export function App() {
  return <IconContext.Provider value={{ className: "react-icons" }}>
    <Routes>
      <Route  path="/" element={<BaseLayout/>}>
        <Route index element={<UserProfileComponent/>}/>
        <Route path='about/' element={"about"}/>
        <Route path='login/' element={"login"}/>
        <Route path='*' element={"Not Found"}/>
      </Route>
    </Routes>
  </IconContext.Provider>
}


export default App
