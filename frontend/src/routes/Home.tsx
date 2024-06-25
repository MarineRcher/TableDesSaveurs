import {Link} from 'react-router-dom';
import "../css/Home.css"
import { MenuCard } from "./Card";
export default function Home() {
    return (
        <div className="container">
            <div className="topbar">
                <h1>TDS : Travailleurs de sauce</h1>
            </div>
            <ul>
                <MenuCard
                    title={"All Recipes"}
                    url={"/listRecipe"}
                    image={"https://via.placeholder.com/150"}
                />
                <MenuCard
                    title={"Add Recipes"}
                    url={"/addRecipe"}
                    image={"https://via.placeholder.com/150"}
                />
                <MenuCard
                    title={"User"}
                    url={"/user"}
                    image={"https://via.placeholder.com/150"}
                />
            </ul>
        </div>
    );
}