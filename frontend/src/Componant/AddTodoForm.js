import React, { useState } from 'react';
import { useMutation } from '@apollo/client';
import { gql } from 'graphql-tag';

const ADD_TODO = gql`
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

const AddTodoForm = () => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [time, setTime] = useState('');
  const [addTodo] = useMutation(ADD_TODO);

  const handleSubmit = () => {
    addTodo({ variables: { title, description, time } });
  };

  return (
    <div>
      <h2>Add Todo</h2>
      <input type="text" value={title} onChange={e => setTitle(e.target.value)} placeholder="Title" />
      <input type="text" value={description} onChange={e => setDescription(e.target.value)} placeholder="Description" />
      <input type="text" value={time} onChange={e => setTime(e.target.value)} placeholder="Time" />
      <button onClick={handleSubmit}>Add Todo</button>
    </div>
  );
};

export default AddTodoForm;
