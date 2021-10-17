import React from 'react'


const ToDoListItem = ({item, deleteToDo}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.text}</td>
            <td>{item.create}</td>
            <td>{item.project}</td>
            <td>{item.user}</td>
            <td><button onClick={()=>deleteToDo(item.id)} type='button'>Delete</button></td>
        </tr>
    )
}

const ToDoList = ({items, deleteToDo}) => {
    return (
        <table className="table">
            <tr>
                <th>Id</th>
                <th>Text</th>
                <th>Create</th>
                <th>Project</th>
                <th>User</th>
            </tr>
            {items.map((todo) => <ToDoListItem item={todo} deleteToDo={deleteToDo}/>)}
        </table>
    )
}

export default ToDoList