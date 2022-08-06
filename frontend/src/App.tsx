import './tailwind.css'
import React from 'react'
import { Routes, Route } from 'react-router-dom'



function App(){
  return <div>
    <Routes>
      <Route path="/" element={<BaseLayout/>}>
        <Route index element={<HomePage/>}/>
        <Route path="login/" element={<LoginPage/>}/>
        <Route path="logout/" element={<LogoutPage/>}/>
        <Route path="profile/" element={<ProfilePage/>}/>
        <Route path="about/" element={<AboutPage/>}/>
        <Route path="*" element={"Not Found"}/>
      </Route>
    </Routes>
  </div>
}

export default App
