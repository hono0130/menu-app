import React, { FC } from 'react'
import { ApolloClient, InMemoryCache, useQuery, gql } from '@apollo/client'
import NavBar from './component/Header'
import './App.css'
import DishTable from './component/DishTable'
import { allMenuQuery } from './graphql/query'
import client from './graphql/config'

const App: FC = () => {
  const { loading, error, data } = useQuery(allMenuQuery)
  if (loading) return <p>Loading...</p>
  if (error) return <p>Error :</p>
  console.log(data.allMenuQuery)
  return (
    <div className="App">
      <NavBar />
      <h1>不要な料理を選んでください</h1>
      {/* <DishTable rows={}></DishTable> */}
    </div>
  )
}

export default App
