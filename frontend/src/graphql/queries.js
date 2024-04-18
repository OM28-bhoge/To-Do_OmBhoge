import { gql } from '@apollo/client';

// Define GraphQL queries
export const GET_TODOS = gql`
  query {
    todos {
      id
      title
      description
      time
      image
    }
  }
`;

// Add more queries as needed
