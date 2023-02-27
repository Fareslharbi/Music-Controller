import React, { Component } from 'react';
import { render } from 'react-dom';

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return <h6>Testing React Code</h6>
    }
}


const appDiv = document.getElementById("app");
render(<App />, appDiv);