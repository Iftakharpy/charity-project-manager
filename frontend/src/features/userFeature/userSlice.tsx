import { createSlice, PayloadAction } from "@reduxjs/toolkit";


interface User{
    isLoggedIn: boolean;
    profile: null | {
        id: number;
        first_name: string;
        last_name: string;
        email: string;
        phone_number: string;
        profile_picture: string;
        groups: string[];
        user_permissions: string[];
        is_active: boolean;
        is_staff: boolean;
        is_superuser: boolean;
        last_login: string;
        date_joined: string;
    };
}
const initialUserState = {isLoggedIn:false, profile: null} as User


export const userSlice = createSlice({
    name: 'user',
    initialState: {value: initialUserState},
    reducers: {
        login(state, action:PayloadAction<Partial<User>>){
            state.value = {...state.value, ...action.payload}
        },
        
        logout(state){
            state.value = initialUserState
        }
    }
})

export default userSlice.reducer
export const userReducer =  userSlice.reducer
export const {login, logout} = userSlice.actions
