SELECT city.city_id,city.city,customer.first_name,customer.last_name,customer.email,address.address
FROM city
JOIN address ON city.city_id = address.city_id
JOIN customer ON customer.address_id = address.address_id
WHERE address.city_id = 312
ORDER by address.address_id;

SELECT film.film_id, film.title, film.description, film.release_year, film.rating,film.special_features,category.name
FROM film
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';

SELECT actor.actor_id, CONCAT(actor.first_name,' ',actor.last_name) AS actor_name, film.film_id, film.title, film.description,film.release_year
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5;

SELECT store.store_id,city.city_id,customer.first_name,customer.last_name,customer.email,address.address
FROM address,store,city

LEFT JOIN customer ON customer.store_id = store.store_id




WHERE (city.city_id = 1 OR 42 OR 312 OR 459) AND (store.store_id = 1)




