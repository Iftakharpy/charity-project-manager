import React from 'react'
import { useAppSelector } from '../../app/hooks'
import { toast } from 'react-toastify'
import { useNavigate } from 'react-router-dom'

import { InputComponent, SelectComponent, TextareaComponent } from '../../components/input/InputComponent'
import { ButtonComponent } from '../../components/button/ButtonComponent'


export function LoginPage() {
	const {isLoggedIn, profile} = useAppSelector((state)=>state.user.value)
	const navigator = useNavigate()
	if (isLoggedIn) {
		toast.error("You are already logged in!")
		navigator('/')
	}
	return (
		<form className='form login-form'>
			<InputComponent labelText="Email" type="email" name='username' value={'ab@cd.com'} />
			<InputComponent labelText="Password" type="password" name='password' value={'abcd'} />
			<ButtonComponent buttonText='Login'
				type='submit'
				onClick={(e)=>{
					e.preventDefault()
					toast.info("Trying to login!"); 
				}}
			/>
		</form>
	)
}
