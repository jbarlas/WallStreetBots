import { NavLink, Outlet } from "react-router-dom";
import { AiOutlineHome } from "react-icons/ai";
import "./App.css";

function App() {
  return (
    <div className="container">
      <div className="nav">
        <NavLink to="/">
          <AiOutlineHome />
          Home
        </NavLink>
        <NavLink to="/comments">Comments</NavLink>
      </div>
      <Outlet />
    </div>
  );
}

export default App;
