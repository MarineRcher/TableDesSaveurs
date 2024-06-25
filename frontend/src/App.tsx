import { Routes, Route } from "react-router-dom";
import Root from "./routes/root"
import Home from "./routes/Home";
import AddRecipe from "./routes/AddRecipe";
import ListRecipes from "./routes/ListRecipes";
import User from "./routes/User";
import Recipe from "./routes/ShowRecipe";
export default function App() {
    return (
        <Routes>
            <Route path="/" element={<Home />}/>
            <Route path="listRecipe" element={<ListRecipes />}/>
            <Route path="addRecipe" element={<AddRecipe/>}/>
            <Route path="user" element={<User/>}/>
            <Route path="recipe/:id" element={<Recipe />}/>
        </Routes>
    );
}
