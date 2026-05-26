import React from "react";
import ReactDOM from "react-dom/client";

import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Dashboard from "./pages/Dashboard";

import "./index.css";

ReactDOM.createRoot(
  document.getElementById("root")
).render(

  <BrowserRouter>

    <Routes>

      <Route
        path="/"
        element={<Dashboard />}
      />

    </Routes>

  </BrowserRouter>
);