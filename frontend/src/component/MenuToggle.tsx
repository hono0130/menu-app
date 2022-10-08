import React from 'react'
import { Box } from '@chakra-ui/react'

const MenuToggle: FC = ({ toggle, isOpen }) => {
  return (
    <Box display={{ base: 'black', md: 'none' }} onClick={toggle}>
      {isOpen ? <CloseIcon /> : <MenuIcon />}
    </Box>
  )
}
