import React from 'react'
import { NavLink } from 'react-router-dom'
import { RiCloseCircleFill } from 'react-icons/ri'
import { TiThMenu } from 'react-icons/ti'

import { openNavbar, closeNavbar } from '../features/navigationBar/navigationBarSlice'
import { useAppSelector, useAppDispatch } from '../app/hooks'


export function HeaderComponent() {
	const { isNavbarOpen } = useAppSelector((state) => state.navigation.value)
	const dispatch = useAppDispatch()

 	return (<header id='header' className="header">
			<button
				className='btn p-1 h-12 flex justify-center items-center'
				onClick={()=>isNavbarOpen ? dispatch(closeNavbar()) : dispatch(openNavbar())}>
				{isNavbarOpen?<RiCloseCircleFill/>:<TiThMenu/>}
			</button>
			<NavLink className='btn' to='/login/'>Login</NavLink>
		</header>)
	}
