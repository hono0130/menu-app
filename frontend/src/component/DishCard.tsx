import React, { useState } from 'react'
import {
  Flex,
  Circle,
  Box,
  Image,
  Badge,
  useColorModeValue,
  Grid,
  GridItem,
  Link,
} from '@chakra-ui/react'

interface Payload {
  imageURL: string
  name: string
  duration: number
  tag: string
  isSideDish: boolean
  link: string
}

const DishCard = ({ imageURL, name, duration, tag, isSideDish, link }: Payload) => {
  const [choose, setChoosen] = useState(false)

  const handleClick = () => {
    setChoosen(!choose)
  }

  return (
    <Flex display={'inline'} p={50} w="full" alignItems="center" justifyContent="center">
      <Box
        bg={useColorModeValue('white', 'gray.800')}
        maxW="sm"
        borderWidth="1px"
        rounded="lg"
        shadow="lg"
        position="relative"
      >
        <Circle size="10px" position="absolute" top={2} right={2} bg="red.200" />
        <Link href={link}>
          <Image src={imageURL} alt={`Picture of ${name}`} roundedTop="lg" />
        </Link>
        <Box p="6" backgroundColor={choose ? 'pink.100' : 'white'} onClick={handleClick}>
          <Box display={'flex'} alignItems="baseline">
            <Badge
              rounded="full"
              px="2"
              fontSize="0.8em"
              colorScheme={isSideDish ? 'green' : 'red'}
            >
              {tag}
            </Badge>
            <Grid
              templateAreas={`
              "name duration"
              "name time"`}
            >
              <GridItem fontSize="xl" fontWeight="bold" as="h2" lineHeight="tight" area={'name'}>
                {name}
              </GridItem>
              <GridItem fontSize="sm" as="h4" lineHeight="tight" area={'duration'}>
                所要時間
              </GridItem>
              <GridItem fontSize="sm" as="h4" lineHeight="tight" area={'time'}>
                {duration}分
              </GridItem>
            </Grid>
          </Box>
        </Box>
      </Box>
    </Flex>
  )
}

export type { Payload }
export default DishCard
