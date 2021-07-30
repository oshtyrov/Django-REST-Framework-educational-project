import React from 'react'


const ToDoListItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.text}</td>
            <td>{item.create}</td>
            <td>{item.project}</td>
            <td>{item.user}</td>
        </tr>
    )
}

const ToDoList = ({items}) => {
    return (
        <table className="table">
            <tr>
                <th>Id</th>
                <th>Text</th>
                <th>Create</th>
                <th>Project</th>
                <th>User</th>
            </tr>
            {items.map((item) => <ToDoListItem item={item} />)}
        </table>
    )
}

export default ToDoList