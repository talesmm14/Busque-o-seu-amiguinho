import React from 'react';

import Header from './components/header/index';
import Footer from './components/footer/index';

import './index.css';

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <Header />
        <Footer />
      </div>
    );
  }
}

export default App;
