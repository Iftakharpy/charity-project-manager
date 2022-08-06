import {createApi, fetchBaseQuery} from '@reduxjs/toolkit/query/react'
import {API_ROOT} from '../config'


export const api = createApi({
    reducerPath: 'api',
    baseQuery: fetchBaseQuery({
        baseUrl: API_ROOT,
        credentials: 'include',
        mode: 'cors'
    }),
    endpoints: (builder) => ({
        // User related endpoints
        loginUser: builder.mutation({
            query: ({email, password}) => ({
                url: 'users/login/',
                method: 'POST',
                body: {username: email, password}
            }),
        }),

        logoutUser: builder.query({
            query: ()=>'users/logout/'
        }),
        
        getUserProfile: builder.query({
            query: () => 'users/details/'
        }),
    })
})


export const {
    useLoginUserMutation,
    useLogoutUserQuery,
    useGetUserProfileQuery
} = api
