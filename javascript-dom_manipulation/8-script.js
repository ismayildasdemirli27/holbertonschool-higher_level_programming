document.addEventListener('DOMContentLoaded', function() {
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Məlumatı təhlükəsiz şəkildə textContent ilə əlavə edirik
            document.querySelector('#hello').textContent = data.hello;
        })
        .catch(error => {
            console.error('Fetch operation failed:', error);
            document.querySelector('#hello').textContent = 'Error';
        });
});
