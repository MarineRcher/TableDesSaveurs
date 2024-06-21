import logo from "../logo.svg";
import React from "react";
import '../index.css';
import { Link } from "react-router-dom";

export default function Root() {
        return (
            <div className="App">
            <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <p>
                Coucou Edit <code>src/App.tsx</code> and save to reload.
            </p>
            <a
        className="App-link"
        href="./Home.tsx"
        target="_blank"
        rel="noopener noreferrer"
            >
            Go home
        </a>
        </header>
        </div>
    );
}