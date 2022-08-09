import React from 'react'
import { DateTime } from 'luxon'

export function FooterComponent() {
  return (
	<footer id='footer' className='footer'>
		Copyright © {DateTime.now().year} Iftakhar Husan.
	</footer>
  )
}
