import { createBrowserRouter, Route, createRoutesFromElements, RouterProvider, } from "react-router-dom"
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './pages/App.tsx'
import Luotuote, {postTuote} from './pages/luotuote.tsx'
import Muokkaatuote from './pages/muokkaatuote.tsx'
import {fetchTuotteet, muokkausLoader } from './pages/tuoteloader.tsx'
import RootLayout from './layouts/RootLayout.tsx'
import Muokkaus, { muokkaaTuote } from './pages/muokkaus.tsx'
import './pages/index.css'
import NotFound from "./pages/NotFound.tsx"
import TuoteError from "./pages/tuoteError.tsx"

const router = createBrowserRouter(
  createRoutesFromElements(

    <Route path="/"  element={ <RootLayout />}>
      <Route loader={fetchTuotteet} index element={ <App />}/>
      <Route 
      action={postTuote}
      path="luotuote" 
      element={ <Luotuote />}
      />

      <Route path="muokkaatuote" element={ <RootLayout />} errorElement={<TuoteError/>}>
        <Route loader={fetchTuotteet} index element={ <Muokkaatuote />}/>
        <Route 
        action={muokkaaTuote}
        loader={muokkausLoader} 
        path=":id" 
        element={ <Muokkaus />} 
        />
      </Route>
      <Route path="*" element={<NotFound/>}/>
    </Route>

  )
)

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
)