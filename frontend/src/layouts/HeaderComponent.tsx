import React from 'react'
import { NavLink } from 'react-router-dom'
import { RiCloseCircleFill } from 'react-icons/ri'
import { TiThMenu } from 'react-icons/ti'


interface HeaderProps{
	isSidebarOpen: boolean;
	setIsSidebarOpen: (arg:boolean)=>void;
}


export function HeaderComponent(props:HeaderProps) {
	const { isSidebarOpen, setIsSidebarOpen } = props
 	 return (<header id='header' className="header">
			<button className='btn p-1 h-12 flex justify-center items-center' onClick={()=>setIsSidebarOpen(!isSidebarOpen)}>
				{isSidebarOpen?<RiCloseCircleFill/>:<TiThMenu/>}
			</button>
			<NavLink className='btn' to='/login/'>Login</NavLink>
		</header>)
	}
