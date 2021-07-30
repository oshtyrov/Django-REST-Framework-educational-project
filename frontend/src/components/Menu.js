import React from 'react'
import {
  Link
} from "react-router-dom";

function NavbarItem({name, href}) {
    return (
        <li>
          <Link to={href}>{name}</Link>
        </li>
    )
}


export default function Navbar({navbarItems}) {
    return (
        <nav>
            <a>Menu</a>
            <div>
              <ul>
                <li>
                  {navbarItems.map((item) => <NavbarItem name={item.name} href={item.href} />)}
                </li>
              </ul>
              <form>
                <input placeholder="Search" aria-label="Search" />
                <button type="submit">Search</button>
              </form>
            </div>
        </nav>
    )
}