import React from 'react'
import type { InputProps, SelectProps, TextareaProps } from './InputTypes'
import { CLASS_NAMES } from '../config'


export function InputComponent({ name, labelText, labelProps, containerProps, ...props }:InputProps) {
  return (
	<div {...containerProps}
		className={containerProps?.className?`${containerProps.className} ${CLASS_NAMES.container}`: CLASS_NAMES.container}
		>
		<label {...labelProps} htmlFor={name}
			className={labelProps?.className?`${labelProps.className} ${CLASS_NAMES.label}`: CLASS_NAMES.label}
			>
				{labelText!==undefined?labelText:labelProps?.children}
		</label>
		<input {...props} id={name} className={props.className?`${props.className} ${CLASS_NAMES.input}`: CLASS_NAMES.input}/>
	</div>
  )
}


export function SelectComponent({ name, labelText, labelProps, containerProps, ...props }:SelectProps) {
  return (
	<div {...containerProps}
		className={containerProps?.className ? `${containerProps.className} ${CLASS_NAMES.container}`: CLASS_NAMES.container}
		>
		<label {...labelProps} htmlFor={name}
			className={labelProps?.className?`${labelProps.className} ${CLASS_NAMES.label}`: CLASS_NAMES.label}
			>
				{labelText!==undefined?labelText:labelProps?.children}
		</label>
		<select {...props} id={name} className={props.className?`${props.className} ${CLASS_NAMES.select}`: CLASS_NAMES.select}>
			{props.children}
		</select>
	</div>
  )
}


export function TextareaComponent({ name, labelText, labelProps, containerProps, ...props }:TextareaProps) {
  return (
	<div {...containerProps}
		className={containerProps?.className?`${containerProps.className} ${CLASS_NAMES.container}`: CLASS_NAMES.container}
		>
		<label {...labelProps} htmlFor={name}
			className={labelProps?.className?`${labelProps.className} ${CLASS_NAMES.label}`: CLASS_NAMES.label}
			>
				{labelText!==undefined?labelText:labelProps?.children}
		</label>
		<textarea {...props} id={name} className={props.className?`${props.className} ${CLASS_NAMES.textarea}`: CLASS_NAMES.textarea}>
			{props.children}
		</textarea>
	</div>
  )
}
