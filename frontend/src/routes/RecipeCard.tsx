import React from 'react';

type RecipeCardProps = {
    title: string;
    image: string;
    description: string;
};

const RecipeCard: React.FC<RecipeCardProps> = ({ title, image, description}) => {
    return (
        <div className="recipe-card">
            <img src={image} alt={title} />
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
    );
};
export default RecipeCard;