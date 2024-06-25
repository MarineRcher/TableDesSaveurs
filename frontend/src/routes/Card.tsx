import React from 'react';
import {Link} from 'react-router-dom';

type RecipeCardProps = {
    title: string;
    image: string;
    description: string;
};

type MenuCardProps = {
    title: string;
    url: string;
    image: string;
};

const RecipeCard: React.FC<RecipeCardProps> = ({title, image, description}) => {
    return (
        <div className="recipe-card">
            <img src={image} alt={title} />
            <h3>{title}</h3>
            <p>{description}</p>
        </div>
    );
};

export {RecipeCard};

const MenuCard: React.FC<MenuCardProps> = ({ title, url, image}) => {
    return (
        <Link to={url}>
            <div className="menu-card">
                <img src={image} alt={title} />
                <h3>{title}</h3>
            </div>
        </Link>
    )
}

export {MenuCard};