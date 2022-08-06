import { combineReducers, configureStore } from "@reduxjs/toolkit"
import { setupListeners } from "@reduxjs/toolkit/dist/query";
import { userReducer } from "../features/userFeature/userSlice"

import { persistReducer, persistStore } from 'redux-persist';
import storage from "redux-persist/lib/storage";
import { api } from "./services/api";




const combinedReducers = combineReducers({
    user: userReducer,
    [api.reducerPath]: api.reducer,
})

const persistConfig = {
    key: 'root',
    storage,
}
const persistedReducer = persistReducer(persistConfig, combinedReducers)


export const store = configureStore({
    reducer: persistedReducer,
    middleware: (getDefaultMiddleware) => getDefaultMiddleware({
        serializableCheck: true, // to avoid error from redux-persist
    }).concat(api.middleware)
})

export const persistedStore = persistStore(store)


// optional, but required for refetchOnFocus/refetchOnReconnect behaviors
// see `setupListeners` docs - takes an optional callback as the 2nd arg for customization
setupListeners(store.dispatch)

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch
