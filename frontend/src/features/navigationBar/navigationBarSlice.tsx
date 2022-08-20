import { createSlice, PayloadAction } from "@reduxjs/toolkit";


interface NavigationState{
	isNavbarOpen: boolean;
	navbarPosition: 'left' | 'right' | 'top' | 'bottom';
    closeNavbarOnFooterClick: boolean;
    closeNavbarOnHeaderClick: boolean;
    closeNavbarOnMainContentClick: boolean;
}

const initialNavigationState = {
    isNavbarOpen: true,
    navbarPosition: 'left',
    closeNavbarOnFooterClick: false,
    closeNavbarOnHeaderClick: true,
    closeNavbarOnMainContentClick: false
} as NavigationState


export const userSlice = createSlice({
    name: 'navigation',
    initialState: {value: initialNavigationState},
    reducers: {
        openNavbar(state){
            state.value = { ...state.value, isNavbarOpen: true }
        },
        closeNavbar(state){
            state.value = { ...state.value, isNavbarOpen: false }
        },
        setCloseNavbarOnFooterClick(state, action:PayloadAction<boolean>){
            state.value = { ...state.value, closeNavbarOnFooterClick: action.payload}
        },
        setCloseNavbarOnHeaderClick(state, action:PayloadAction<boolean>){
            state.value = { ...state.value, closeNavbarOnHeaderClick: action.payload}
        },
        setCloseNavbarOnMainContentClick(state, action:PayloadAction<boolean>){
            state.value = { ...state.value, closeNavbarOnMainContentClick: action.payload}
        },
    }
})


export default userSlice.reducer
export const navigationReducer =  userSlice.reducer
export const { closeNavbar, openNavbar, setCloseNavbarOnHeaderClick, setCloseNavbarOnMainContentClick } = userSlice.actions
