fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        document.querySelector('#character').textContent = data.name;
    })
    .catch(error => {
        console.error('Fetch operation failed:', error);
        document.querySelector('#character').textContent = 'Error loading character';
    });
