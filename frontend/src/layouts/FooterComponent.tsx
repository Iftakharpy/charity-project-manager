import React from 'react'
import { DateTime } from 'luxon'
import { useAppDispatch, useAppSelector } from '../app/hooks'
import { closeNavbar } from '../features/navigationBar/navigationBarSlice'


export function FooterComponent() {
	const { closeNavbarOnFooterClick } = useAppSelector((state) => state.navigation.value)
	const dispatch = useAppDispatch()
  return (
	<footer id='footer' className='footer' onClick={(e)=>{
		if(closeNavbarOnFooterClick) dispatch(closeNavbar())
	}}>
		Copyright © {DateTime.now().year} Iftakhar Husan.
	</footer>
  )
}
