import React from 'react'

import { CLASS_NAMES } from '../config';
import { FormProps } from './FormTypes';


export function FormComponent({ formHeaderText, formHeaderProps, ...props}:FormProps) {
  	return (
		<form {...props}
			className={props.className ? `${props.className} ${CLASS_NAMES.form}`: CLASS_NAMES.form}
			>
				{
					formHeaderProps||formHeaderText ?
						<header {...formHeaderProps} className={props.className?`${props.className} ${CLASS_NAMES.formHeader}`: CLASS_NAMES.formHeader}>
						{ formHeaderText===undefined ? formHeaderProps?.children:<h2>{formHeaderText}</h2> }
						</header> : undefined
				}
				{props.children}
		</form>
	)
}
