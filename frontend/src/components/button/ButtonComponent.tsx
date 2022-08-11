import React from 'react'

import { CLASS_NAMES } from '../config';
import { ButtonProps } from './ButtonTypes';


export function ButtonComponent(props:ButtonProps) {
  return (
	<div {...props.containerProps}
		className={props?.containerProps?.className ? `${props.containerProps.className} ${CLASS_NAMES.container}`: CLASS_NAMES.container}
		>
		<button {...props}
			className={props.className?`${props.className} ${CLASS_NAMES.button}`: CLASS_NAMES.button}
			>
				{props.buttonText!==undefined?props.buttonText:props.children}
		</button>
	</div>
  )
}
