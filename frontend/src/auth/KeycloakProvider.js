import React from 'react';
import Keycloak from 'keycloak-js';

const keycloak = Keycloak('/keycloak.json');

const KeycloakProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = React.useState(false);

  React.useEffect(() => {
    keycloak
      .init({ onLoad: 'login-required' })
      .then(authenticated => {
        setIsAuthenticated(authenticated);
      })
      .catch(err => {
        console.error(err);
      });
  }, []);

  if (!isAuthenticated) return <div>Loading...</div>;

  return <>{children}</>;
};

export default KeycloakProvider;
