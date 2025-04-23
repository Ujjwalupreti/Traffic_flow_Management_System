import { useState } from 'react'
import './App.css'
import Header from './Header.jsx';
import Home from './Home.jsx';
import Map from './Map.jsx';
import Dashboard from './Dashboard.jsx';
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Header/>
      <div>
        <Home/>
        <Dashboard/>
        <Map/> 
      </div>
    </>
  ) 
}

export default App
