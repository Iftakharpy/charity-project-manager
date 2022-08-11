import React from 'react'
import NotFound from './NotFound.svg'

export function NotFoundPage() {
  return (
	<div>
    <img className='not-found-img' src={NotFound} alt="An image of error: 404 Not found"/>
  </div>
  )
}
