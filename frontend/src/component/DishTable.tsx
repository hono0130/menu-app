import React from 'react'
import { Box, Table, TableContainer, Tbody, Td, Th, Thead, Tr } from '@chakra-ui/react'
import DishCard, { Payload } from './DishCard'

interface row {
  id: number
  Lunch: Payload[]
  Dinner: Payload[] // 2つ(for Lunch, for Dinner)
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
      w="100%"
      display="flex"
      justifyContent="center"
      alignItems="center"
    >
      <TableContainer overflowX={'unset'} overflowY={'unset'}>
        <Table variant={'simple'}>
          <Thead position={'sticky'} top={-1} zIndex={'docked'}>
            <Tr bg={'gray.100'}>
              {cols.map((col) => (
                <Th key={col.name} borderWidth="3px" borderColor="gray.300">
                  {col.name}
                </Th>
              ))}
            </Tr>
          </Thead>
          <Tbody alignItems={'center'}>
            {rows.map((row) => (
              <Tr key={row.id}>
                {cols.map((col) => {
                  if (col.id > 0) {
                    const LorD = col.id == 1 ? 'Lunch' : 'Dinner'
                    return (
                      <Td
                        key={`${col.id}-${row.id}`}
                        borderWidth="3px"
                        borderColor="gray.300"
                        bg="white"
                      >
                        <DishCard
                          imageURL={row[LorD][0].imageURL}
                          name={row[LorD][0].name}
                          duration={row[LorD][0].duration}
                          tag={row[LorD][0].tag}
                          link={row[LorD][0].link}
                          isSide={false}
                        ></DishCard>
                        <DishCard
                          imageURL={row[LorD][1].imageURL}
                          name={row[LorD][1].name}
                          duration={row[LorD][1].duration}
                          tag={row[LorD][1].tag}
                          link={row[LorD][0].link}
                          isSide={true}
                        ></DishCard>
                      </Td>
                    )
                  } else {
                    return (
                      <Td
                        key={`${col.id}-${row.id}`}
                        borderWidth="3px"
                        borderColor="gray.300"
                        bg="white"
                      >
                        {row.id}
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
