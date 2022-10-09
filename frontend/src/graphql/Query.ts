import gql from 'graphql-tag'

const allMenuQuery = gql`
  query {
    allMenu(num: 3) {
      name
      link
      imageURL
      duration
      isSide
    }
  }
`

export { allMenuQuery }
