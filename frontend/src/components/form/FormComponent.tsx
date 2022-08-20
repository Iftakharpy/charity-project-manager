import React from 'react'

import { CLASS_NAMES } from '../config';
import { FormProps } from './FormTypes';


export function FormComponent({ formHeaderText, formHeaderProps, errors, ...props}:FormProps) {
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
			<ul className={CLASS_NAMES.formErrors}>
				{errors?.map((error, idx)=><li key={idx}>{error}</li>)}
			</ul>

			{props.children}
		</form>
	)
}
