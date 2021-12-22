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

class App extends React.Component{

  constructor(props){
    super(props);
     this.state={
       first_name: "",
       last_name: "",
       list:[]
     }
  }

  updateName(key, value){
    //update react state
    this.setState({
      [key]: value
    });
    console.log("owo"); // for testing
  }

  addItem(){
    // create item with unic id
      const newItem={
      id: 1+Math.random(),
      value: this.state.newItem.slice()
    };

    //copy the current list
    const list = [...this.state.list];

    //add new item
    list.push(newItem);

    //update state
    this.setState({
      list,
      first_name: "",
      last_name: ""
    });

    console.log(list); //for testing
  }

  render(){
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
  
          <form>
            <label htmlFor="fname">First name:</label>
            <input type="text" id="fname" name="fname"
            onChange={e=> this.updateName("first_name", e.target.value)}/>
            <br/><br/>
            <label htmlFor="lname">Last name:</label>
            <input type="text" id="lname" name="lname"
            onChange={e=> this.updateName("last_name", e.target.value)}/>
            <br/><br/>
            <input type="submit" value="Submit"/>
            <ul>
              {this.state.list.map(item=>{
                return(
                  <li key={item.id}>
                    {item.value}
                  </li>
                )
              })}
            </ul>
          </form>
        </header>
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
