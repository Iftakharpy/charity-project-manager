import React from 'react'

import { CLASS_NAMES } from '../config';
import { ButtonProps } from './ButtonTypes';


export function ButtonComponent({ buttonText, containerProps, ...props}:ButtonProps) {
  return (
	<div {...containerProps}
		className={containerProps?.className ? `${containerProps.className} ${CLASS_NAMES.container}`: CLASS_NAMES.container}
		>
		<button {...props}
			className={props.className?`${props.className} ${CLASS_NAMES.button}`: CLASS_NAMES.button}
			>
				{buttonText!==undefined ? buttonText:props.children}
		</button>
	</div>
  )
}
