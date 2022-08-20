import React, { useEffect, useState } from 'react'
import { useAppDispatch, useAppSelector } from '../../app/hooks'
import { toast } from 'react-toastify'
import { useNavigate } from 'react-router-dom'

import { InputComponent } from '../../components/input/InputComponent'
import { ButtonComponent } from '../../components/button/ButtonComponent'
import { FormComponent } from '../../components/form/FormComponent'
import { SpinnerComponent } from '../../components/spinner/SpinnerComponent'

import { useLoginUserMutation } from '../../app/services/api'
import { login } from '../../features/userFeature/userSlice'
import { UserEndpointResponse } from '../../features/userFeature/userTypes'


export function LoginPage() {
	const {isLoggedIn, profile} = useAppSelector((state)=>state.user.value)
	const navigate = useNavigate()
	const dispatch = useAppDispatch()
	
	const [username, setUsername] = useState('ab@cd.com')
	const [password, setPassword] = useState('abcd')
	const [formErrors, setFormErrors] = useState<string[]>([])
	const [usernameErrors, setUsernameErrors] = useState<string[]>([])
	const [passwordErrors, setPasswordErrors] = useState<string[]>([])
	const [loginUser, { isLoading, data, error}] = useLoginUserMutation()
	
	useEffect(()=>{
		if (isLoggedIn) {
			toast.error(`${profile?.email} are already logged in!`)
			navigate('/')
		}
		
		if (data){
			dispatch(login(data?.data))
			toast.success(`Welcome ${data.data.first_name} ${data.data.last_name}!`)
			navigate('/')
		}
		if(error!==undefined){
			const errorResponse = error?.data as UserEndpointResponse
			if (errorResponse?.success===false){
				const errors = errorResponse.errors
				setFormErrors(errors?.common || [])
				setUsernameErrors(errors?.password || [])
				setPasswordErrors(errors?.username || [])

				formErrors ? formErrors.forEach((error)=>toast.error(error)) : undefined
			}
		}
	}, [error, data])
	
	if (isLoading) return <SpinnerComponent />

	return (
			<FormComponent
				errors={formErrors} 
				className='login-form'
				method='POST'
				action='/login/'
				formHeaderText='User Login Form'
				onSubmit={(e)=>{
					const form = e.target as HTMLFormElement
					// const formData = new FormData(form)
					// const formEntries = Object.fromEntries(formData.entries())
			
					loginUser({email: username, password: password})
					e.preventDefault()
				}}>
				<InputComponent
					errors={usernameErrors}
					labelText="Email"
					name='username'
					type="email"
					required
					placeholder={username}
					defaultValue={username}
					autoComplete="username"
					onChange={(e)=>{
						const usernameInput = e.target
						const username = usernameInput.value
						setUsername(username)
						// if(usernameInput.checkValidity()) setUsername(username)
					}}/>
				<InputComponent
					errors={passwordErrors}
					labelText="Password"
					name='password'
					type="password"
					required
					placeholder={password}
					defaultValue={password}
					autoComplete="current-password"
					onChange={(e)=>{
						const passwordInput = e.target
						const password = passwordInput.value
			
						setPassword(password)
						// if(passwordInput.checkValidity()) setPassword(password)
					}}/>
				<ButtonComponent buttonText='Login' type='submit'/>
			</FormComponent>
	)
}
