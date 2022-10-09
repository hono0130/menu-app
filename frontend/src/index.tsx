import React from 'react'
import ReactDOM from 'react-dom'
import { ChakraProvider } from '@chakra-ui/react'
import { ApolloProvider } from '@apollo/client'
import client from './graphql/config'

import App from './App'
import customTheme from './utils/theme'

const rootElement = document.getElementById('root')
ReactDOM.render(
  <React.StrictMode>
    <ApolloProvider client={client}>
      <ChakraProvider theme={customTheme}>
        <App />
      </ChakraProvider>
    </ApolloProvider>
  </React.StrictMode>,
  rootElement,
)
