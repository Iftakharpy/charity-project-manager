import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
import { API_ROOT } from '../config'
import { User, LoginCredentials, UserEndpointResponse } from '../../features/userFeature/userTypes'

export const api = createApi({
    reducerPath: 'api',
    keepUnusedDataFor: 1,
    refetchOnReconnect: true,
    refetchOnMountOrArgChange:true,
    baseQuery: fetchBaseQuery({
        baseUrl: API_ROOT,
        credentials: 'include',
        mode: 'cors'
    }),
    endpoints: (builder) => ({
        // User related endpoints
        loginUser: builder.mutation<User, LoginCredentials>({
            query: ({email, password}) => ({
                url: 'users/login/',
                method: 'POST',
                body: {username: email, password}
            }),
        }),

        logoutUser: builder.query<unknown, void>({
            query: ()=>'users/logout/'
        }),

        getUserProfile: builder.query<UserEndpointResponse, void>({
            query: () => 'users/details/'
        }),
    })
})


export const {
    useLoginUserMutation,
    useLogoutUserQuery,
    useGetUserProfileQuery
} = api
