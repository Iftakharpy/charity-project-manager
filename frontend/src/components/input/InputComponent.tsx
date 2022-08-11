import React from 'react'
import type { InputProps, SelectProps, TextareaProps } from './InputTypes'
import { CLASS_NAMES } from '../config'


export function InputComponent(props:InputProps) {
  return (
	<div {...props.containerProps}
		className={props?.containerProps?.className?`${props.containerProps.className} ${CLASS_NAMES.container}`: CLASS_NAMES.container}
		>
		<label {...props?.labelProps} htmlFor={props.name}
			className={props?.labelProps?.className?`${props.labelProps.className} ${CLASS_NAMES.label}`: CLASS_NAMES.label}
			>
				{props.labelText!==undefined?props.labelText:props?.labelProps?.children}
		</label>
		<input {...props} id={props.name} className={props.className?`${props.className} ${CLASS_NAMES.input}`: CLASS_NAMES.input}/>
	</div>
  )
}


export function SelectComponent(props:SelectProps) {
  return (
	<div {...props.containerProps}
		className={props?.containerProps?.className ? `${props.containerProps.className} ${CLASS_NAMES.container}`: CLASS_NAMES.container}
		>
		<label {...props.labelProps} htmlFor={props.name}
			className={props?.labelProps?.className?`${props.labelProps.className} ${CLASS_NAMES.label}`: CLASS_NAMES.label}
			>
				{props.labelText!==undefined?props.labelText:props?.labelProps?.children}
		</label>
		<select {...props} id={props.name} className={props.className?`${props.className} ${CLASS_NAMES.select}`: CLASS_NAMES.select}>
			{props.children}
		</select>
	</div>
  )
}


export function TextareaComponent(props:TextareaProps) {
  return (
	<div {...props.containerProps}
		className={props?.containerProps?.className?`${props.containerProps.className} ${CLASS_NAMES.container}`: CLASS_NAMES.container}
		>
		<label {...props.labelProps} htmlFor={props.name}
			className={props?.labelProps?.className?`${props.labelProps.className} ${CLASS_NAMES.label}`: CLASS_NAMES.label}
			>
				{props.labelText!==undefined?props.labelText:props?.labelProps?.children}
		</label>
		<textarea {...props} id={props.name} className={props.className?`${props.className} ${CLASS_NAMES.textarea}`: CLASS_NAMES.textarea}>
			{props.children}
		</textarea>
	</div>
  )
}
