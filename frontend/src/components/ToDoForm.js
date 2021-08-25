import React from 'react'


class ToDoForm extends React.Component {
    constructor(props) {
      super(props)
      this.state = {
        projectName: '',
        userName: '',
        text: ''
      }

    this.handleTextChange = this.handleTextChange.bind(this);
    this.handleUserChange = this.handleUserChange.bind(this);
    this.handleProjectChange = this.handleProjectChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    }
  
    handleTextChange(event) {    
        this.setState({text: event.target.value,
                });
                console.log(event.target.value)
    }

    handleUserChange(event) {    
        this.setState({userName: event.target.value,
                });
                console.log(event.target.value)
    }

    handleProjectChange(event) {    
        this.setState({projectName: event.target.value,
                });
                console.log(event.target.value)
    }


    handleSubmit(event) {
        console.log(this.state.text)
      this.props.createToDo(this.state.userName, this.state.projectName, this.state.text);
      event.preventDefault();
    }
   
    render() {
      return (
        <form onSubmit={(event)=> this.handleSubmit(event)}>
                <label>project</label>
                <select name="project" className='form-control' 
                    onChange={(event)=>this.handleProjectChange(event)}>
                    {this.props.projects.map((project)=><option value={project.name}>{project.name}</option>)}
                </select>
                <label>user</label>
                <select name="user" className='form-control' 
                    onChange={(event)=>this.handleUserChange(event)}>
                    {this.props.users.map((user)=><option value={user.username}>{user.username}</option>)}
                </select>
                <label>text</label>
                <input type="text" className="form-control" value={this.state.text}
                    onChange={(event)=>this.handleTextChange(event)} />        
                       
            <input type="submit" className="btn btn-primary" value="Create" />
        </form>
      );
    }
  }

  export default ToDoForm

