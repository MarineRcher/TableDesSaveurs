import React from 'react';
import { RecipeCard } from "./Card";
import "../css/ListRecipes.css"
import {Link} from "react-router-dom";
export default function ListRecipes() {
    const recipes = [
        { title: 'Recipe 1', image: 'https://via.placeholder.com/150', description: 'Description 1' },
        { title: 'Recipe 2', image: 'https://via.placeholder.com/150', description: 'Description 2' },
        { title: 'Recipe 3', image: 'https://via.placeholder.com/150', description: 'Description 3' },
        { title: 'Recipe 4', image: 'https://via.placeholder.com/150', description: 'Description 4' },
        { title: 'Recipe 5', image: 'https://via.placeholder.com/150', description: 'Description 5' },
        { title: 'Recipe 6', image: 'https://via.placeholder.com/150', description: 'Description 6' },
        // Ajoutez plus de recettes si nécessaire
    ];
    return (
        <div className="recipe-list">
            {recipes.map((recipe, index) => (
                //<Link to={`/recipe/${recipe.id}`}>
                    <RecipeCard
                    key={index}
                    title={recipe.title}
                    image={recipe.image}
                    description={recipe.description}
                    />
                //</Link>
            ))}
        </div>
    );
};

