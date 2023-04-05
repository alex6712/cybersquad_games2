import React from 'react'

type Props = {
   children: string
   inp_href: string
}

function Mylink({ children, inp_href, ...props }: Props) {
   return (
      <a href={inp_href} {...props} className="myLink">{children}</a>
   )
}

export default Mylink