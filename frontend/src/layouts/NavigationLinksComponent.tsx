import React, { FC } from 'react';
import { NavLink } from 'react-router-dom'
import { FaHome, FaInfoCircle, FaUsers, FaUsersCog } from 'react-icons/fa'


interface LinkType{
	path: string;
	text: string;
	icon: FC;
}


const NAV_LINKS = [
	{
		path: '/',
		text: 'Home',
		icon: FaHome
	},
	{
		path: '/users/',
		text: 'Users',
		icon: FaUsers
	},
	{
		path: '/beneficiaries/',
		text: 'Beneficiaries',
		icon: FaUsersCog
	},
	{
		path: '/about/',
		text: 'About',
		icon: FaInfoCircle
	},
] as LinkType[]




export function NavigationLinksComponent() {
  	return (<nav className='sidebar-nav'>
		<ul className='sidebar-nav-items-container'>
			{
				NAV_LINKS.map((link, idx)=>{
				return (<li key={idx} className='sidebar-nav-item-container'>
						<NavLink className='sidebar-nav-link' to={link.path}>
							<link.icon/>
							<span className='nav-link-text'>{link.text}</span>
						</NavLink>
					</li>)
			})}
		</ul>
		</nav>
	)}
