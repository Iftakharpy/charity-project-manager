import React from 'react'
import { useAppSelector } from '../../app/hooks'
import { toast } from 'react-toastify'
import { useNavigate } from 'react-router-dom'


export function LoginPage() {
	const {isLoggedIn, profile} = useAppSelector((state)=>state.user.value)
	const navigator = useNavigate()
	if (isLoggedIn) {
		toast.error("You are already logged in!")
		navigator('/')
	}
	return (
		<form className='form login-form'>
			<div className='form-input-container'>
				<label htmlFor="username" >Email:</label>
				<input name='username' type="email" value='ab@cd.com' />
			</div>
			<div className='form-input-container'>
				<label htmlFor="password">Password:</label>
				<input name='password' type="password" placeholder='abcd' value={'abcd'} />
			</div>
			<div className='form-input-container'>
				<button type='submit' onClick={(e)=>{
					e.preventDefault()
					toast.info("Trying to login!"); 
				}}>Login</button>
			</div>
		</form>
	)
}
