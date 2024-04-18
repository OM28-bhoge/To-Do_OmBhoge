import React from 'react';
import TodoList from './components/TodoList';
import AddTodoForm from './components/AddTodoForm';
import { ApolloProvider } from '@apollo/client';
import { client } from './graphql/client';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import KeycloakProvider from './auth/KeycloakProvider';
import PrivateRoute from './auth/PrivateRoute';
import PaymentForm from './components/PaymentForm';

const App = () => {
  return (
    <ApolloProvider client={client}>
      <KeycloakProvider>
        <Router>
          <Switch>
            <Route exact path="/" component={TodoList} />
            <PrivateRoute exact path="/add" component={AddTodoForm} />
            <PrivateRoute exact path="/payment" component={PaymentForm} />
          </Switch>
        </Router>
      </KeycloakProvider>
    </ApolloProvider>
  );
};

export default App;
