import React from 'react'
import { useGetUserProfileQuery } from '../../app/services/api'


export function UserProfileComponent() {
	const { isLoading, isError, data, error} = useGetUserProfileQuery()

	console.log('data', data)
	console.log('error', error)

	if (isLoading) return <h1>Loading data</h1>
	if (isError) return <h1>Error while loading data</h1>
	if (data) return (<article>
		<h1>Name: {data.data.first_name} {data.data.last_name}</h1>
		<h2>Name: {data.data.first_name} {data.data.last_name}</h2>
		<h3>Name: {data.data.first_name} {data.data.last_name}</h3>
		<h4>Name: {data.data.first_name} {data.data.last_name}</h4>
		<h5>Name: {data.data.first_name} {data.data.last_name}</h5>
		<h6>Name: {data.data.first_name} {data.data.last_name}</h6>
	<pre>
		{JSON.stringify(data, null, 4)}
	</pre>
	</article>)
	return <h1>Unknown error</h1>
}
