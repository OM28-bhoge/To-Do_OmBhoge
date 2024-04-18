import { gql } from '@apollo/client';

// Define GraphQL mutations
export const ADD_TODO = gql`
  mutation AddTodo($title: String!, $description: String!, $time: String!) {
    addTodo(title: $title, description: $description, time: $time) {
      id
      title
      description
      time
      image
    }
  }
`;

export const DELETE_TODO = gql`
  mutation DeleteTodo($id: ID!) {
    deleteTodo(id: $id) {
      id
    }
  }
`;

export const EDIT_TODO = gql`
  mutation EditTodo($id: ID!, $title: String!, $description: String!, $time: String!) {
    editTodo(id: $id, title: $title, description: $description, time: $time) {
      id
      title
      description
      time
      image
    }
  }
`;

// Add more mutations as needed
