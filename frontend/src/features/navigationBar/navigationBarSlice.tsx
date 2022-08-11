import { createSlice, PayloadAction } from "@reduxjs/toolkit";


interface NavigationState{
	isNavbarOpen: boolean;
	navbarPosition: 'left' | 'right' | 'top' | 'bottom';
}

const initialNavigationState = { isNavbarOpen: true, navbarPosition: 'left' } as NavigationState

export const userSlice = createSlice({
    name: 'navigation',
    initialState: {value: initialNavigationState},
    reducers: {
        openNavbar(state){
            state.value = { ...state.value, isNavbarOpen: true }
        },
        closeNavbar(state){
            state.value = { ...state.value, isNavbarOpen: false }
        }
    }
})


export default userSlice.reducer
export const navigationReducer =  userSlice.reducer
export const { closeNavbar, openNavbar } = userSlice.actions
