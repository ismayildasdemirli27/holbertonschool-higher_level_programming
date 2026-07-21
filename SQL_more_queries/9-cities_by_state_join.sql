-- example
SELECT cities.id, cities.name, states.name FROM cities
INNER JOIN
states
ON cities.state_id = states.id
GROUP BY cities.id;