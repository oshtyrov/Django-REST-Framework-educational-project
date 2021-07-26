import React from 'react';
import axios from 'axios';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'
import Footer from './components/Footer.js'
import Menu from './components/Menu.js'



class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'users': []
       }
   }

    componentDidMount() {
       axios.get('http://127.0.0.1:8000/api/users')
           .then(response => {
               this.setState({users: response.data.results})
           }).catch(error => console.log(error))
    }

    render() {
        return (
           <div>
             <header>
             <Menu />
             </header>
             <main>
             <div className="container">
               <UserList users={this.state.users} />
             </div>
             </main>
             <Footer />
           </div>
           )
   }
}

export default App;

