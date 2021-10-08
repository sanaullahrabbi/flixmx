function isInViewport(element, offset = -30) {
    return (window.innerHeight - element.getBoundingClientRect().top >= offset)
}

function CreateSearchedOutputMovie(item, index) {
    if (item['tmdb_thumbnail'])
        searchedOutput +=
        `<li><a href="/details/movie/${item['slug']}"><div><img src="${item['tmdb_thumbnail']}" alt="tmdb_thumbnail"></div> <span>${item['title']} (movie)</span></a></li>`
    else
        searchedOutput +=
        `<li><a href="/details/movie/${item['slug']}"><div><img src="/mediafiles/${item['thumbnail']}" alt=""></div> <span>${item['title']} (movie)</span></a></li>`
}

function CreateSearchedOutputSeries(item, index) {
    if (item['tmdb_thumbnail'])
        searchedOutput +=
        `<li><a href="/details/series/${item['slug']}"><div><img src="${item['tmdb_thumbnail']}" alt=""></div> <span>${item['title']} (tv-series) </span></a></li>`
    else
        searchedOutput +=
        `<li><a href="/details/series/${item['slug']}"><div><img src="/mediafiles/${item['thumbnail']}" alt=""></div> <span>${item['title']} (tv-series) </span></a></li>`
}

function CreateSearchedOutputSoftsGames(item, index) {
    if (item['tmdb_thumbnail'])
        searchedOutput +=
        `<li><a href="/details/${item['category']}/${item['slug']}"><div><img src="${item['tmdb_thumbnail']}" alt=""></div> <span>${item['title']} (${item['category']}) </span></a></li>`
    else
        searchedOutput +=
        `<li><a href="/details/${item['category']}/${item['slug']}"><div><img src="/mediafiles/${item['thumbnail']}" alt=""></div> <span>${item['title']} (${item['category']}) </span></a></li>`
}