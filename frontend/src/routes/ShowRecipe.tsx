import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const Recipe = () => {
    // const { id } = useParams<{ id: string }>();
    // const [recipe, setRecipe] = useState<any>(null);
    //
    // useEffect(() => {
    //     // Remplacez ceci par votre logique pour récupérer la recette depuis la base de données
    //     fetch(`/api/recipes/${id}`)
    //         .then(response => response.json())
    //         .then(data => setRecipe(data))
    //         .catch(error => console.error('Error fetching recipe:', error));
    // }, [id]);
    //
    // if (!recipe) {
    //     return <div>Loading...</div>;
    // }
    //
    // return (
    //     <div>
    //         <h2>{recipe.title}</h2>
    //         <img src={recipe.image} alt={recipe.title} />
    //         <p>{recipe.description}</p>
    //     </div>
    // );
    return (
        <div>
            <h1>Recipe</h1>
        </div>
    )
};

export default Recipe;