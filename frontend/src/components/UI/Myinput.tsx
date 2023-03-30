import React from 'react'

type Props = {
   inp_type: string
}

function Myinput({ inp_type }: Props) {
   return (
      <input type={inp_type} className="auth__form-input" />
   )
}

export default Myinput