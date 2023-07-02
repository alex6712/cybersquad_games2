import React from 'react'

type Props = {
   children: string,
   inp_type: "submit" | "button" | "reset" | undefined
   disabled?: boolean
   onClick?: any
   style?: any
   params?: any[]
}

function Mybtn({ children, params, style, inp_type, disabled, onClick }: Props) {
   return (
      <button
         type={inp_type}
         style={style}
         disabled={disabled}
         onClick={onClick({ ...params })}
         className="myBtn">
         {children}
      </button>
   )
}

export default Mybtn