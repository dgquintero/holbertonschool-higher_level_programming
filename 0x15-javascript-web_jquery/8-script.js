$(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, textStatus) => {
    if (textStatus === 'success') {
      const movies = data.results;
      for (let movie in movies) {
        $('#list_movies').append(`<li>${movies[movie].title}</li>`);
      }
    }
  });
});
