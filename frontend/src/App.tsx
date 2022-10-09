import React, { FC } from 'react'
import { ApolloClient, InMemoryCache, useQuery, gql } from '@apollo/client'
import NavBar from './component/Header'
import './App.css'
import { DishTable } from './component/DishTable'
import { allMenuQuery } from './graphql/query'
import client from './graphql/config'
import { Payload } from './component/DishCard'
import { DishTableProps } from './component/DishTable'

const App: FC = () => {
  const { loading, error, data } = useQuery(allMenuQuery)
  if (loading) return <p>Loading...</p>
  if (error) return <p>Error :</p>

  const data2rows = (data: Payload[]) => {
    const len = data.length
    const rows = []
    for (let i = 0; i < len / 4; i++) {
      rows.push({
        id: i + 1,
        Lunch: [data[i], data[i + 1]],
        Dinner: [data[i + 2], data[i + 3]],
      })
    }
    return rows
  }

  return (
    <div className="App">
      <NavBar />
      <h1>不要な料理を選んでください</h1>
      <DishTable rows={data2rows(data.allMenu)}></DishTable>
    </div>
  )
}

export default App
