import ApolloClient from 'apollo-boost'
import gql from 'graphql-tag'

const client = new ApolloClient({
  uri: 'hoge.com',
  request: (operation) => {
    operation.setContext({})
  },
})

export default client
