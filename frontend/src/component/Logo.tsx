import React, { FC } from 'react'
import { Box, Text } from '@chakra-ui/react'

interface Props {
  w: string
  color: string[]
}

const Logo: FC<Props> = (props: Props) => {
  return (
    <Box {...props}>
      <Text fontSize="2xl" fontWeight="bold">
        Menu App
      </Text>
    </Box>
  )
}

export default Logo
