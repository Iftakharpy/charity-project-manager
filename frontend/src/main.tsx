import React from 'react'
import ReactDOM from 'react-dom/client'

import { BrowserRouter } from 'react-router-dom'
import { Provider } from 'react-redux'
import { PersistGate } from 'redux-persist/integration/react';

import { RiCloseCircleFill } from 'react-icons/ri'
import { ToastContainer } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'; // default styles
import './customizeToastify.css' // custom styles

import App from './App'
import { store, persistedStore } from './app/store'


ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <Provider store={store}>
      <PersistGate loading={null} persistor={persistedStore}>
        <BrowserRouter>
          <App/>
          <ToastContainer
            autoClose={7000}
            newestOnTop
            draggable={false}
            closeButton={
              ({closeToast})=>(
                <span onClick={closeToast}>
                  <RiCloseCircleFill size={28}/>
                </span>
              )}
            />
        </BrowserRouter>
      </PersistGate>
    </Provider>
  </React.StrictMode>
)
