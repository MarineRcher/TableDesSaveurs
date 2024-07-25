-- Crée l'utilisateur avec un mot de passe sécurisé
CREATE OR REPLACE USER 'TDSuser'@'localhost' IDENTIFIED BY '524urikX43aWLN';

-- Accorde les privilèges nécessaires à l'utilisateur
GRANT INSERT, DELETE, SELECT ON TDS.* TO 'TDSuser'@'localhost';
FLUSH PRIVILEGES;

-- Drop database if exists and create a new one
drop database if exists TDS;
create database TDS;
use TDS;

-- Drop and create roles table
drop table if exists roles;
create table roles (
    id_roles int(11) primary key auto_increment not null,
    role int(5)
);

-- Drop and create users table
drop table if exists users;
create table users (
    id_user int(11) primary key auto_increment not null,
    login varchar(40) not null,
    name varchar(40),
    email varchar(40),
    password varchar(255),
    create_user datetime default current_timestamp,
    id_roles int(11),
    CONSTRAINT fk_roles_users FOREIGN KEY (id_roles) REFERENCES roles(id_roles)
);

-- Drop and create measurements_quantity table
drop table if exists measurements_quantity;
create table measurements_quantity (
    id_measurement_quantity int(11) primary key auto_increment not null,
    measurement_quantity varchar(25)
);

-- Drop and create measurements table
drop table if exists measurements;
create table measurements (
    id_measurement int(11) primary key auto_increment not null,
    measurement varchar(25) default (`solid`, `liquid`)
);

-- Drop and create categories_ingredients table
drop table if exists categories_ingredients;
create table categories_ingredients (
    id_category_ingredient int(11) primary key auto_increment not null,
    category_ingredients varchar(25)
);

-- Drop and create ingredients table
drop table if exists ingredients;
create table ingredients (
    id_ingredient int(11) primary key auto_increment not null,
    ingredient varchar(25),
    id_category_ingredient int(11),
    id_measurement int(11),
    id_measurement_quantity int(11),
    CONSTRAINT fk_category_ingredient FOREIGN KEY (id_category_ingredient) REFERENCES categories_ingredients(id_category_ingredient),
    CONSTRAINT fk_measurement_ingredient FOREIGN KEY (id_measurement) REFERENCES measurements(id_measurement),
    CONSTRAINT fk_measurement_quantity_ingredient FOREIGN KEY (id_measurement_quantity) REFERENCES measurements_quantity(id_measurement_quantity)
);

-- Drop and create difficulties table
drop table if exists difficulties;
create table difficulties (
    id_difficulty int(11) primary key auto_increment not null,
    difficulty varchar(25)
);

-- Drop and create diet table
drop table if exists diet;
create table diet (
    id_diet int(11) primary key auto_increment not null,
    diet varchar(25)
);

-- Drop and create categories_recipes table
drop table if exists categories_recipes;
create table categories_recipes (
    id_category_recipes int(11) primary key auto_increment not null,
    category_recipes varchar(25)
);

-- Drop and create recipes table
drop table if exists recipes;
create table recipes (
    id_recipe int(11) primary key auto_increment not null,
    name varchar(50),
    created_at datetime default current_timestamp,
    id_user int(11),
    id_category_recipes int(11),
    id_difficulty int(11),
    CONSTRAINT fk_user_recipe FOREIGN KEY (id_user) REFERENCES users(id_user),
    CONSTRAINT fk_category_recipe FOREIGN KEY (id_category_recipes) REFERENCES categories_recipes(id_category_recipes),
    CONSTRAINT fk_difficulty_recipe FOREIGN KEY (id_difficulty) REFERENCES difficulties(id_difficulty)
);

-- Drop and create ingredients_recipes table
drop table if exists ingredients_recipes;
create table ingredients_recipes (
    id_ingredient_recipe int(11) primary key auto_increment not null,
    measure_quantity int(11),
    id_ingredient int(11),
    id_recipe int(11),
    CONSTRAINT fk_ingredient_recipe FOREIGN KEY (id_ingredient) REFERENCES ingredients(id_ingredient),
    CONSTRAINT fk_recipe_ingredient_recipe FOREIGN KEY (id_recipe) REFERENCES recipes(id_recipe)
);

-- Drop and create kitchen_ustensiles table
drop table if exists kitchen_ustensiles;
create table kitchen_ustensiles (
    id_kitchen_ustensile int(11) primary key auto_increment not null,
    kitchen_ustensile varchar(25)
);

-- Drop and create kitchen_ustensiles_recipes table
drop table if exists kitchen_ustensiles_recipes;
create table kitchen_ustensiles_recipes (
    id_kitchen_ustensile_recipe int(11) primary key auto_increment not null,
    id_kitchen_ustensile int(11),
    id_recipe int(11),
    CONSTRAINT fk_kitchen_ustensile_recipe FOREIGN KEY (id_kitchen_ustensile) REFERENCES kitchen_ustensiles(id_kitchen_ustensile),
    CONSTRAINT fk_recipe_kitchen_ustensile_recipe FOREIGN KEY (id_recipe) REFERENCES recipes(id_recipe)
);

-- Drop and create steps_recipes table
drop table if exists steps_recipes;
create table steps_recipes (
    id_step int(11) primary key auto_increment not null,
    step varchar(100),
    number_step int(5),
    id_recipe int(11),
    CONSTRAINT fk_recipe_step FOREIGN KEY (id_recipe) REFERENCES recipes(id_recipe)
);

-- Drop and create rates_recipes table
drop table if exists rates_recipes;
create table rates_recipes (
    id_rate_recipe int(11) primary key auto_increment not null,
    rate int(3),
    comment varchar(255),
    id_recipe int(11),
    id_user int(11),
    CONSTRAINT fk_rate_recipe FOREIGN KEY (id_recipe) REFERENCES recipes(id_recipe),
    CONSTRAINT fk_user_comment FOREIGN KEY (id_user) REFERENCES users(id_user)
);

-- Drop and create favorites_recipes table
drop table if exists favorites_recipes;
create table favorites_recipes (
    id_favorites_recipes int(11) auto_increment primary key not null,
    id_recipe int(11),
    id_user int(11),
    CONSTRAINT fk_favorite_recipe FOREIGN KEY (id_recipe) REFERENCES recipes(id_recipe),
    CONSTRAINT fk_user_favorite_recipe FOREIGN KEY (id_user) REFERENCES users(id_user)
);
