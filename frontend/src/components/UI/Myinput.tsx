import React from 'react'

type Props = {
   inp_type: string
}

function Myinput({ inp_type }: Props) {
   return (
      <input type={inp_type} className="myInput" />
   )
}

export default Myinput