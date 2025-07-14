import React from 'react';
import "../assets/style.css";
import "../assets/bootstrap.min.css";

const Header = () => {
    const logout = async (e) => {
        e.preventDefault();
        const res = await fetch("/djangoapp/logout", {
          method: "GET",
          credentials: "include", // CRITICAL for session cookie
        });
      
        const json = await res.json();
        if (json && json.status === true) {
          const username = sessionStorage.getItem("username");
          sessionStorage.removeItem("username");
          alert("Logging out " + username + "...");
          window.location.href = "/";
        } else {
          alert("Logout failed");
        }
      };
      
    
//The default home page items are the login details panel
let home_page_items =  <div></div>

//Gets the username in the current session
let curr_user = sessionStorage.getItem('username')

//If the user is logged in, show the username and logout option on home page
if (curr_user !== null && curr_user !== "") {
    home_page_items = (
        <div className="input_panel">
          <span className='username'>{curr_user}</span>
          <button
            className="nav_item btn btn-link"
            onClick={logout}
            style={{ textDecoration: "underline", color: "black", background: "none", border: "none" }}
          >
            Logout
          </button>
        </div>
      );
      
  }  
    return (
        <div>
          <nav class="navbar navbar-expand-lg navbar-light" style={{backgroundColor:"darkturquoise",height:"1in"}}>
            <div class="container-fluid">
              <h2 style={{paddingRight: "5%"}}>Dealerships</h2>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarText">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" style={{fontSize: "larger"}} aria-current="page" href="/">Home</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" style={{fontSize: "larger"}} href="/about">About Us</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" style={{fontSize: "larger"}} href="/contact">Contact Us</a>
                  </li>
                </ul>
                <span class="navbar-text">
                  <div class="loginlink" id="loginlogout">
                  {home_page_items}
                  </div>
                  </span>
              </div>
            </div>
          </nav>
        </div>
    )
}

export default Header
