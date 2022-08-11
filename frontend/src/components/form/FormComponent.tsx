import React from 'react'

import { CLASS_NAMES } from '../config';
import { FormProps } from './FormTypes';


export function FormComponent(props:FormProps) {
  return (
	<form {...props}
		className={props.className ? `${props.className} ${CLASS_NAMES.form}`: CLASS_NAMES.form}
		>
			{props.children}
	</form>
  )
}
