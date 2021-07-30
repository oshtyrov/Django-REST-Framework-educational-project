import React from 'react';
import {
    BrowserRouter,
    Switch,
    Route,
    Redirect,
  } from "react-router-dom";
import axios from 'axios'
import './App.css';
import UserList from './components/User.js'
import Footer from './components/Footer.js'
import Navbar from './components/Menu.js'
import {ProjectList, ProjectDetail} from './components/Project.js'
import ToDoList from './components/Todo.js'

const NotFound404 = ({ location }) => {
return (
    <div>
        <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
    )
}


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            navbarItems: [
                {name: 'Users', href: '/'},
                {name: 'Projects', href: '/projects'},
                {name: 'TODOs', href: '/todos'},
            ],
            users: [],
            projects: [],
            project: {},
            todos: []
        }

    }

    render() {
         return (
            <BrowserRouter>
                <header>
                        <Navbar navbarItems={this.state.navbarItems} />
                </header>
                <main>
                    <div>
                        <Switch>
                            <Route exact path='/' component={() => <UserList users={this.state.users} />} />
                            <Route exact path='/projects' component={() => <ProjectList items={this.state.projects} />} />
                            <Route exact path='/todos' component={() => <ToDoList items={this.state.todos} />} />
                            <Route path="/project/:id" children={<ProjectDetail getProject={(id) =>
                            this.getProject(id)} item={this.state.project} />} />
                            <Redirect from='/users' to='/' />
                            <Route component={NotFound404} />
                        </Switch>
                    </div>
                </main>
              <Footer />
            </BrowserRouter>
            )
    }

    getProject(id) {
        axios.get(`http://127.0.0.1:8000/api/projects/${id}`)
        .then(response => {
            this.setState({project: response.data})
        }).catch(error => console.log(error))
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/')
        .then(response => {
            this.setState({users: response.data.results})
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/')
        .then(response => {
            this.setState({projects: response.data.results})
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todos/')
        .then(response => {
            this.setState({todos: response.data.results})
        }).catch(error => console.log(error))

    }
}

export default App;

