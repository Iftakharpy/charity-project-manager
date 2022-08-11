import React from 'react'

import { CgSpinner } from 'react-icons/cg'
import { SpinnerProps } from './SpinnerTypes'
import { CLASS_NAMES } from '../config'


export function Spinner({ className, ...props }:SpinnerProps) {
  return (<CgSpinner {...props} className={className ? `${className} ${CLASS_NAMES.spinner}`:CLASS_NAMES.spinner}/>)
}
