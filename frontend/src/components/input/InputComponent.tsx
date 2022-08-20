import React from 'react'
import type { InputProps, SelectProps, TextareaProps } from './InputTypes'
import { CLASS_NAMES } from '../config'


export function InputComponent({ name, labelText, labelProps, containerProps, errors, ...props }:InputProps) {
  return (
	<div {...containerProps}
		className={containerProps?.className?`${containerProps.className} ${CLASS_NAMES.container}`: CLASS_NAMES.container}
		>
		<label {...labelProps} htmlFor={name}
			className={labelProps?.className?`${labelProps.className} ${CLASS_NAMES.label}`: CLASS_NAMES.label}
			>
				{labelText!==undefined?labelText:labelProps?.children}
		</label>
		<input {...props} id={name} name={name} className={props.className?`${props.className} ${CLASS_NAMES.input}`: CLASS_NAMES.input}/>
		<ul className={CLASS_NAMES.formInputErrors}>
			{errors?.map((error, idx)=><li key={idx}>{error}</li>)}
		</ul>
	</div>
  )
}


export function SelectComponent({ name, labelText, labelProps, containerProps, errors, ...props }:SelectProps) {
  return (
	<div {...containerProps}
		className={containerProps?.className ? `${containerProps.className} ${CLASS_NAMES.container}`: CLASS_NAMES.container}
		>
		<label {...labelProps} htmlFor={name}
			className={labelProps?.className?`${labelProps.className} ${CLASS_NAMES.label}`: CLASS_NAMES.label}
			>
				{labelText!==undefined?labelText:labelProps?.children}
		</label>
		<select {...props} id={name} name={name} className={props.className?`${props.className} ${CLASS_NAMES.select}`: CLASS_NAMES.select}>
			{props.children}
		</select>
		<ul className={CLASS_NAMES.formInputErrors}>
			{errors?.map((error, idx)=><li key={idx}>{error}</li>)}
		</ul>
	</div>
  )
}


export function TextareaComponent({ name, labelText, labelProps, containerProps, errors, ...props }:TextareaProps) {
  return (
	<div {...containerProps}
		className={containerProps?.className?`${containerProps.className} ${CLASS_NAMES.container}`: CLASS_NAMES.container}
		>
		<label {...labelProps} htmlFor={name}
			className={labelProps?.className?`${labelProps.className} ${CLASS_NAMES.label}`: CLASS_NAMES.label}
			>
				{labelText!==undefined?labelText:labelProps?.children}
		</label>
		<textarea {...props} id={name} name={name} className={props.className?`${props.className} ${CLASS_NAMES.textarea}`: CLASS_NAMES.textarea}>
			{props.children}
		</textarea>
		<ul className={CLASS_NAMES.formInputErrors}>
			{errors?.map((error, idx)=><li key={idx}>{error}</li>)}
		</ul>
	</div>
  )
}
