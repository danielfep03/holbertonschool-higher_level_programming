$.get('https://swapi-api.hbtn.io/api/films/?format=json', ({ results }) => {
  results.forEach(({ title }) => {
    $('#list_movies').append(`<li>${title}</li>`);
  });
});
