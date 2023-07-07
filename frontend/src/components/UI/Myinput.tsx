import { on } from 'events'
import React, { ChangeEventHandler, KeyboardEventHandler } from 'react'

type Props = {
   inp_type: string
   value?: string
   onChange?: ChangeEventHandler
   mykeypress?: KeyboardEventHandler
}

function Myinput({ inp_type, value, onChange, mykeypress }: Props) {
   return (
      <input type={inp_type} value={value} onChange={onChange} onKeyPress={mykeypress} className="myInput" />
   )
}

export default Myinput