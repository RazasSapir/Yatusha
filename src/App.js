import logo from './logoYatusha.jfif';
import './App.css';
import React from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";

//Redirection link definition
class RedirctLink extends React.Component{
  render() {
    const {txt, dest} = this.props;
    return(<li>
    <Link to={dest}><button>{txt}</button></Link>
    </li>
    );
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
    </div>
  );
}

// Routing between the pages

// function MRoutes(){
//   return(
//     <Router>
//         <div>
//           <nav><ul>
//               <RedirctLink txt = 'hello' dest = '/a'/>
//               <RedirctLink txt = 'world' dest = '/b'/>
//               <RedirctLink txt = '!' dest = '/c'/>
//           </ul></nav>

//           {/* A <Routes> looks through its children <Route>s and
//               renders the first one that matches the current URL. */}
//           <Routes>
//             <Route path="/a">
//               <First />
//             </Route>
//             <Route path="/b">
//               <First />
//             </Route>
//             <Route path="/c">
//               <First />
//             </Route>
//           </Routes>
//         </div>
//       </Router>
//   );
// }

export default App;
