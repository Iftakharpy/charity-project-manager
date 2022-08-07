import './tailwind.css'
import React from 'react'
import { Routes, Route, Outlet } from 'react-router-dom'
import { UserProfileComponent } from './features/userFeature/userProfileComponent'


function App(){
  return <div>
    <div>hello</div>
    <Routes>
      <Route path="/" element={<Outlet/>}>
        <Route index element={<UserProfileComponent/>}/>
        <Route path="*" element={"Not Found"}/>
      </Route>
    </Routes>
    {/* <Routes>
      <Route path="/" element={<BaseLayout/>}>
        <Route index element={<HomePage/>}/>
        <Route path="login/" element={<LoginPage/>}/>
        <Route path="logout/" element={<LogoutPage/>}/>
        <Route path="profile/" element={<ProfilePage/>}/>
        <Route path="about/" element={<AboutPage/>}/>
        <Route path="*" element={"Not Found"}/>
      </Route>
    </Routes> */}
  </div>
}

export default App
