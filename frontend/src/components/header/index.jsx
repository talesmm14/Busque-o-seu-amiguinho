import React from 'react';

import 'bootstrap/dist/css/bootstrap.min.css';

import { Navbar } from 'react-bootstrap';

import './index.css'


class Header extends React.Component {
  render() {
    return (
      <div className="Header">
        <Navbar bg="light">
          <Navbar.Brand>Busque o seu amiguinho!!!</Navbar.Brand>

            <Navbar.Collapse className="justify-content-end">
            <Navbar.Text>
              <Navbar.Brand href="#">Entrar</Navbar.Brand>
              <Navbar.Brand href="#">Registrar</Navbar.Brand>
            </Navbar.Text>
          </Navbar.Collapse>
        </Navbar>

      </div>
    )
  }
}

export default Header;
