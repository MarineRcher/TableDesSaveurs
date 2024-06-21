import {Link} from 'react-router-dom';
export default function Home() {
    return (
        <div>
            <h1>TDS : Travailleurs de sauce</h1>
                <ul>
                    <li>
                        <Link to="/listRecipe">Voir les recettes</Link>
                    </li>
                </ul>
        </div>
    );
}