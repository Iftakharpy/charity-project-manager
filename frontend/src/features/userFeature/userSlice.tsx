import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { User, UserState } from './userTypes'


const initialUserState = { isLoggedIn: false, profile: null } as UserState

export const userSlice = createSlice({
    name: 'user',
    initialState: {value: initialUserState},
    reducers: {
        login(state, action:PayloadAction<Partial<User>>){
            state.value = { ...state.value, ...action.payload}
        },
        
        logout(state){
            state.value = initialUserState
        }
    }
})


export default userSlice.reducer
export const userReducer =  userSlice.reducer
export const {login, logout} = userSlice.actions
