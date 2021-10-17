import React from 'react';
import {
    BrowserRouter,
    Switch,
    Route,
    Redirect,
    Link,
  } from "react-router-dom";
import axios from 'axios'
import './App.css';
import UserList from './components/User.js'
import Footer from './components/Footer.js'
import Navbar from './components/Menu.js'
import {ProjectList, ProjectDetail} from './components/Project.js'
import ToDoList from './components/Todo.js'
import LoginForm from './components/Auth.js'
import ProjectForm from './components/ProjectForm';
import ToDoForm from './components/ToDoForm';
import Cookies from 'universal-cookie';

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
                {name: 'Authorization', href: '/login'},
                {name: 'Create Project', href: '/projects/create'},
                {name: 'Create ToDo', href: '/todos/create'}
            ],
            users: [],
            projects: [],
            project: {},
            todos: [],
            todo: {},
            token: ''
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token}, ()=>this.load_data())
    }
    
    is_authenticated() {
        return this.state.token !== ''
    }
    
    logout() {
        this.set_token('')
    }
    
    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, ()=>this.load_data())
    }
    
    get_token(login, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {"username": login, "password": password})
        .then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
          'Content-Type': 'application/json'
        }
      if (this.is_authenticated())
        {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    getProject(id) {
        axios.get(`http://127.0.0.1:8000/api/projects/${id}`)
        .then(response => {
            this.setState({project: response.data})
        }).catch(error => console.log(error))
    }

    deleteProject(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/projects/${id}`, {headers})
            .then(response => {
            //   this.setState({projects: this.state.projects.filter((item)=>item.id !== id)})
            this.load_data()
            }).catch(error => console.log(error))
      }

      createProject(name, users) {
        console.log(name, users)
        const headers = this.get_headers()
        axios.post(`http://127.0.0.1:8000/api/projects/`,
            {"name": name, "users": users},    
            {headers},
            )
            .then(response => {
                this.load_data()
            }).catch(error => console.log(error))
      }


    deleteToDo(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/api/todos/${id}`, {headers})
            .then(response => {
            this.load_data()
            }).catch(error => console.log(error))
      }

      createToDo(userId, projectId, text) {
        console.log(userId, projectId, text)
        const headers = this.get_headers()
        axios.post(`http://127.0.0.1:8000/api/todos/`,
            {"user": userId, "project": projectId, "text": text, "is_active": true},    
            {headers},
            )
            .then(response => {
                this.load_data()
            }).catch(error => console.log(error))
      }

    load_data() {
        const headers = this.get_headers()

        axios.get('http://127.0.0.1:8000/api/users/', {headers})
        .then(response => {
            this.setState({users: response.data.results})
        }).catch(error => {
            console.log(error)
            this.setState({users: []})
          })

        axios.get('http://127.0.0.1:8000/api/projects/', {headers})
        .then(response => {
            this.setState({projects: response.data.results})
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todos/', {headers})
        .then(response => {
            this.setState({todos: response.data.results.filter((item)=>item.is_active !== false)})
        }).catch(error => console.log(error))    
    }

    componentDidMount() {
        this.get_token_from_storage()
    }

    render() {
        return (
           <BrowserRouter>
               <header>
                   <Navbar navbarItems={this.state.navbarItems} />
                       {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
               </header>
               <main>
                   <div>
                       <Switch>
                           <Route exact path='/' component={() => <UserList users={this.state.users} />} />
                           <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
                           <Route exact path='/projects/create' component={() => 
                                <ProjectForm
                                users={this.state.users}
                                createProject={(name, users) => this.createProject(name, users)} />} />
                            <Route exact path='/todos/create' component={() => 
                                <ToDoForm
                                projects={this.state.projects}
                                users={this.state.users}
                                createToDo={(userId, projectId, text) => this.createToDo(userId, projectId, text)} />} />
                           <Route exact path='/projects' component={() => <ProjectList 
                                items={this.state.projects} 
                                deleteProject={(id)=>this.deleteProject(id)}/>} />
                           <Route exact path='/todos' component={() => <ToDoList 
                                items={this.state.todos}
                                deleteToDo={(id)=>this.deleteToDo(id)} />} />
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
}

export default App;

