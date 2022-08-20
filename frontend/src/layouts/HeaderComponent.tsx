import React from 'react'
import { Link, NavLink } from 'react-router-dom'
import { RiCloseCircleFill } from 'react-icons/ri'
import { TiThMenu } from 'react-icons/ti'

import { openNavbar, closeNavbar } from '../features/navigationBar/navigationBarSlice'
import { useAppSelector, useAppDispatch } from '../app/hooks'


export function HeaderComponent() {
	const { isLoggedIn } = useAppSelector((state) => state.user.value)
	const { isNavbarOpen, closeNavbarOnHeaderClick } = useAppSelector((state) => state.navigation.value)
	const dispatch = useAppDispatch()

 	return (<header id='header' className="header" onClick={(e)=>{
		const target = e.target as HTMLElement
		if (closeNavbarOnHeaderClick && target.id==='header') dispatch(closeNavbar())
	}}>
			<button
				className='btn p-1 h-12 flex justify-center items-center'
				onClick={()=>isNavbarOpen ? dispatch(closeNavbar()) : dispatch(openNavbar())}>
				{isNavbarOpen?<RiCloseCircleFill/>:<TiThMenu/>}
			</button>
			{
				isLoggedIn ?
					<Link className='btn' to='/logout/'>Logout</Link>
					:
					<NavLink className='btn' to='/login/'>Login</NavLink>
			}
			
		</header>)
	}
