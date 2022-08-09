import React from 'react'
import { useGetUserProfileQuery, useLoginUserMutation } from '../../app/services/api'


export function UserProfileComponent() {
	const [loginUser, { isLoading, isError, data, error}] = useLoginUserMutation()

	if (data==undefined && error==undefined && !isLoading) loginUser({email:'ab@cd.com', password:'abcd'})

	if (isLoading) return <h1>Loading data</h1>
	if (isError) return <h1>Error while loading data</h1>
	if (data) return (<article>
		<h1>Name: {data.data.first_name} {data.data.last_name}</h1>
	<pre>
		{JSON.stringify(data, null, 4)}
	</pre>
	</article>)
	return <h1>Unknown error</h1>
}
