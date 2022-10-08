import React from 'react'
import internal from 'stream'
import {
  Box,
  ChakraProvider,
  Table,
  TableContainer,
  Tbody,
  Td,
  Th,
  Thead,
  Tr,
} from '@chakra-ui/react'
import DishCard, { Payload } from './DishCard'

interface row {
  id: number
  dishes: Payload[] // 2つ(for Lunch, for Dinner)
}

interface DishTableProps {
  rows: row[]
}

const DishTable = ({ rows }: DishTableProps) => {
  const cols = [
    {
      id: 0,
      name: 'Day',
    },
    {
      id: 1,
      name: 'Lunch',
    },
    {
      id: 2,
      name: 'Dinner',
    },
  ]
  return (
    <Box
      bg={['primary.500', 'primary.500', 'transparent', 'transparent']}
      w="90%"
      borderWidth={'1px'}
    >
      <TableContainer overflowX={'unset'} overflowY={'unset'}>
        <Table variant={'simple'}>
          <Thead position={'sticky'} top={-1} zIndex={'docked'}>
            <Tr bg={'gray.100'}>
              {cols.map((col) => (
                <Th key={col.name} borderWidth="1px" borderColor="gray.200">
                  {col.name}
                </Th>
              ))}
            </Tr>
          </Thead>
          <Tbody>
            {rows.map((row) => (
              <Tr key={row.id}>
                {cols.map((col) => {
                  if (col.id > 0) {
                    return (
                      <Td
                        key={`${col.id}-${row.id}`}
                        borderWidth="1px"
                        borderColor="gray.200"
                        bg="white"
                      >
                        <DishCard
                          imageURL={row.dishes[col.id - 1].imageURL}
                          name={row.dishes[col.id - 1].name}
                          duration={row.dishes[col.id - 1].duration}
                          tag={row.dishes[col.id - 1].tag}
                        ></DishCard>
                      </Td>
                    )
                  } else {
                    return (
                      <Td
                        key={`${col.id}-${row.id}`}
                        borderWidth="1px"
                        borderColor="gray.200"
                        bg="white"
                      >
                        {col.id + 1}
                      </Td>
                    )
                  }
                })}
              </Tr>
            ))}
          </Tbody>
        </Table>
      </TableContainer>
    </Box>
  )
}

export default DishTable
