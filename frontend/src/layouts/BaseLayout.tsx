import React, { useState } from 'react'
import { NavLink, Outlet } from 'react-router-dom'
import { TiThMenu } from 'react-icons/ti'
import { RiCloseCircleFill } from 'react-icons/ri'

import { NavigationLinksComponent } from './NavigationLinksComponent'
import { FooterComponent } from './FooterComponent'
import { HeaderComponent } from './HeaderComponent'



export function BaseLayout() {
	const [isSidebarOpen, setIsSidebarOpen] = useState(true);
  	return (
		<div id="layout" className='layout'>
			<section className='bottom-section'>
				<article className='main-section'>
					<main id='main-content' className='main-content'>
						{/* Page specific contents goes here */}
						<Outlet/>
					</main>

					<FooterComponent/>
				</article>

				<aside id='sidebar' className={`sidebar ${isSidebarOpen? 'open': 'close'}`}>
					<NavigationLinksComponent/>
				</aside>
			</section>
			
			{/* This section should stay at the bottom for backdrop-filter property to work */}
			<section className='top-section'>
				<HeaderComponent isSidebarOpen={isSidebarOpen} setIsSidebarOpen={setIsSidebarOpen}/>
			</section>
		</div>)}
