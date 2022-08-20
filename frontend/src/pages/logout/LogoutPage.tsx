import React, { useEffect } from 'react'
import { Navigate } from 'react-router-dom'
import { toast } from 'react-toastify'
import { useAppDispatch, useAppSelector } from '../../app/hooks'
import { useLogoutUserQuery } from '../../app/services/api'
import { SpinnerComponent } from '../../components/spinner/SpinnerComponent'
import { logout } from '../../features/userFeature/userSlice'



export default function LogoutPage() {
	const dispatch = useAppDispatch()
	const { isLoading, isSuccess, isError } = useLogoutUserQuery()
	
	useEffect(()=>{
		if (isSuccess) {
			dispatch(logout())
			toast.success('Successfully logged out!')
		}
		if (isError) toast.error('Error occurred while trying to log out!')
	})
	if (isLoading) return <SpinnerComponent/>
	return <Navigate to='/login/'/>
}
