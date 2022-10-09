import gql from 'graphql-tag'

const allMenuQuery = gql`
  query {
    allMenu(num: 4) {
      name
      link
      imageURL
      duration
      isSide
    }
  }
`

export { allMenuQuery }
