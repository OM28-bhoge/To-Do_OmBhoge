import React from 'react';
import { useQuery } from '@apollo/client';
import { gql } from 'graphql-tag';

const GET_TODOS = gql`
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

const TodoList = () => {
  const { loading, error, data } = useQuery(GET_TODOS);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  return (
    <div>
      <h2>Todo List</h2>
      <ul>
        {data.todos.map(todo => (
          <li key={todo.id}>
            <h3>{todo.title}</h3>
            <p>{todo.description}</p>
            <p>{todo.time}</p>
            {todo.image && <img src={todo.image} alt="Todo Image" />}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TodoList;
