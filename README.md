# Movie_recommendation
Movie recommendation system consist two types of filtering (a)demographic filtering  (b)content-based filtering.
Demographic filtering:It is basic filtering which assumes that the best movie with best rating is best for everyone.We need to calculate the movie metric which is defined by the formula provided by IMDB:
weighted rating (WR) = (v ÷ (v+m)) × R + (m ÷ (v+m)) × C
R = average for the movie (mean) = (rating)

v = number of votes for the movie = (votes)

m = minimum votes required to be listed in the Top Rated list (currently 25,000)

C = the mean vote across the whole report

Content filtering: As the name suggest the filter uses the content of the movie i.e the overview ofthe movie to find similar movies.It uses TFID vectorizer and cosine similarity coefficient to find similar movies.
