import React from 'react'


class ProjectkForm extends React.Component {
    constructor(props) {
      super(props)
      this.state = {
        'name': '',
        'users': []
      }
    }
  
    handleChange(event) {    
        this.setState({
                    [event.target.name]: event.target.value
                });
                // console.log([event.target.name])
    }

    handleUserChange(event) {
        console.log(event.target.selectedOptions)
        if (!event.target.selectedOptions) {
            this.setState({
              'users': []
            })
            return;
        }
        let users = []
        for(let i=0; i < event.target.selectedOptions.length; i++) {
            users.push(event.target.selectedOptions.item(i).value)
            // console.log(users)
        }
        this.setState({
            'users': users
        })
    }

    handleSubmit(event) {
      this.props.createProject(this.state.name, this.state.users);
      event.preventDefault();
    }
   
    render() {
      return (
        <form onSubmit={(event)=> this.handleSubmit(event)}>
            <label for="login">name</label>
                <input type="text" className="form-control" name="name" value={this.state.name}
                    onChange={(event)=>this.handleChange(event)} />        
                
                <select multiple name="users" className='form-control' 
                    onChange={(event)=>this.handleUserChange(event)}>
                    {this.props.users.map((user)=><option value={user.id}>{user.username}</option>)}
                </select>       
            <input type="submit" className="btn btn-primary" value="Create" />
        </form>
      );
    }
  }

  export default ProjectkForm

