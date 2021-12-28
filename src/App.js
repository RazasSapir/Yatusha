import logo from './images/logoYatusha.jfif';
import './style/App.css';
import React from 'react';
import HomePage from './components/HomePage';
import Form from './components/Form'
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

class App extends React.Component{

  // constructor(props){
  //   super(props);
  //    this.state={
  //      first_name: "",
  //      last_name: "",
  //      list:[]
  //    }
  // }

  // updateName(key, value){
  //   //update react state
  //   this.setState({
  //     [key]: value
  //   });
  //   console.log("owo"); // for testing
  // }

  // addItem(){
  //   // create item with unic id
  //     const newItem={
  //     id: 1+Math.random(),
  //     value: this.state.newItem.slice()
  //   };

  //   //copy the current list
  //   const list = [...this.state.list];

  //   //add new item
  //   list.push(newItem);

  //   //update state
  //   this.setState({
  //     list,
  //     first_name: "",
  //     last_name: ""
  //   });

  //   console.log(list); //for testing
  // }

  render(){
    return (
      <div className="App">
        {/* <Form /> */}
        <HomePage />
      </div>
    );
  }
  
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
