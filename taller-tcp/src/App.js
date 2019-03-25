import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import MuiThemeProvider from "material-ui/styles/MuiThemeProvider";
import AppBar from "material-ui/AppBar";
import RaisedButton from "material-ui/RaisedButton";
import TextField from "material-ui/TextField";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: "",
      password: "",
      authenticated: false
    };
  }
  request(cred) {
    var response = "";
    fetch("http://localhost:5000/", {
      method: "POST",
      body: cred,
      mode: "cors",
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Content-Type": "text/plain"
      }
    })
      .then(function(response) {
        return response.json();
      })
      .then(function(myJson) {
        response = myJson;
        console.log(myJson);
      });
    // console.log(response);
    // if (response.includes("correctamente")) {
    //   console.log(response);
    //   this.setState({ authenticated: true });
    // }
  }

  render() {
    return (
      <div>
        <MuiThemeProvider>
          {!this.state.authenticated ? (
            <div>
              <AppBar title="Login" />
              <TextField
                hintText="Enter your Username"
                floatingLabelText="Username"
                onChange={(event, newValue) =>
                  this.setState({ username: newValue })
                }
              />
              <br />
              <TextField
                type="password"
                hintText="Enter your Password"
                floatingLabelText="Password"
                onChange={(event, newValue) =>
                  this.setState({ password: newValue })
                }
              />
              <br />
              <RaisedButton
                label="Submit"
                primary={true}
                style={style}
                onClick={() =>
                  this.request([
                    this.state.username + ":" + this.state.password
                  ])
                }
              />
            </div>
          ) : (
            <div />
          )}
        </MuiThemeProvider>
      </div>
    );
  }
}
const style = {
  margin: 15
};
export default App;
