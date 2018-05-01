SELECT * FROM friends;


SELECT users.first_name,users.last_name,user2.first_name AS friend_first_name,user2.last_name AS friend_last_name
FROM users
LEFT JOIN friends ON users.id = friends.user_id
LEFT JOIN users AS user2 ON user2.id = friends.friend_id




