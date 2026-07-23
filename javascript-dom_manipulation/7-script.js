fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const list = document.querySelector('#list_movies');
        
        // Filmlərin siyahısı 'results' massivinin içindədir
        data.results.forEach(movie => {
            const listItem = document.createElement('li');
            listItem.textContent = movie.title;
            list.appendChild(listItem);
        });
    })
    .catch(error => {
        console.error('Fetch operation failed:', error);
        const list = document.querySelector('#list_movies');
        const errorItem = document.createElement('li');
        errorItem.textContent = 'Error loading movies';
        list.appendChild(errorItem);
    });
