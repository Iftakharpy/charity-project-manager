import React, { useState } from 'react'
import { Outlet } from 'react-router-dom'
import { NavigationLinksComponent } from './NavigationLinksComponent'
import { FooterComponent } from './FooterComponent'
import { HeaderComponent } from './HeaderComponent'

import { closeNavbar } from '../features/navigationBar/navigationBarSlice'
import { useAppSelector, useAppDispatch } from '../app/hooks'


export function BaseLayout() {
	const { isNavbarOpen } = useAppSelector((state)=>state.navigation.value);
	const dispatch = useAppDispatch()

  	return (
		<div id="layout" className='layout'>
			<section className='bottom-section'>
				<div className='main-section'>
						<div className='main-content-wrapper'>
							<main id='main-content' className='main-content' onClick={()=>dispatch(closeNavbar())}>
								{/* Page specific contents goes here */}
								<Outlet/>
							</main>
						</div>


					<FooterComponent/>
				</div>

				<aside id='sidebar' className={`sidebar ${isNavbarOpen? 'open': 'close'}`}>
					<NavigationLinksComponent/>
				</aside>
			</section>
			
			{/* This section should stay at the bottom for backdrop-filter property to work */}
			<section className='top-section'>
				<HeaderComponent/>
			</section>
		</div>)}
