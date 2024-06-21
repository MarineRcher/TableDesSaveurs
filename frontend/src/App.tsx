import { Routes, Route } from "react-router-dom";
import Root from "./routes/root"
import Home from "./routes/Home";
import ListRecipes from "./routes/ListRecipes";
export default function App() {
    return (
        <Routes>
            <Route path="/" element={<Home />}/>
            <Route path="listRecipe" element={<ListRecipes />}/>
        </Routes>
    );
}
