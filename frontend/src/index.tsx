import React from 'react';
import * as ReactDOM from 'react-dom/client';
import {BrowserRouter, createBrowserRouter, RouterProvider} from "react-router-dom";
import App from './App';
import './App.css';
import reportWebVitals from "./reportWebVitals";

// const router = createBrowserRouter([
//     {
//         path: "/",
//         element: <App />,
//     },
// ]);

const rootElement = document.getElementById('root');

if (rootElement) {
    ReactDOM.createRoot(rootElement).render(
        <React.StrictMode>
            <BrowserRouter>
                <App />
            </BrowserRouter>
        </React.StrictMode>
    );
}

reportWebVitals();