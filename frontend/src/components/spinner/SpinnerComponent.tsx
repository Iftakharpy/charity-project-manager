import React from 'react'
import type { IconBaseProps } from 'react-icons'
import { CgSpinner } from 'react-icons/cg'


export function Spinner(props:IconBaseProps) {
	let spinnerClasses = 'spinner'
	const className = !props.className ? spinnerClasses : `${props.className} ${spinnerClasses}`
  return (<CgSpinner {...props} className={className}/>)
}
