# Movie_recommendation
Movie recommendation system consist two types of filtering (a)demographic filtering  (b)content-based filtering.
Demographic filtering:It is basic filtering which assumes that the best movie with best rating is best for everyone.We need to calculate the movie metric which is defined by the formula provided by IMDB:
weighted rating (WR) = (v ÷ (v+m)) × R + (m ÷ (v+m)) × C
R = average for the movie (mean) = (rating)

v = number of votes for the movie = (votes)

m = minimum votes required to be listed in the Top Rated list (currently 25,000)

C = the mean vote across the whole report

Content filtering: As the name suggest the filter uses the content of the movie i.e the overview ofthe movie to find similar movies.It uses TFID vectorizer and cosine similarity coefficient to find similar movies.
 Term Frequency-Inverse Document Frequency (TF-IDF). Is one of the algorithms at the foundation of information retrieval. Here, the algorithm is explained using a formula:
tf(t)=c(t)/N
idf(t)=log(ND/NDt)

You can understand the formula using this notation: C(t) is the number of times a term t appears in a document, N is the total number of terms in the document, this results in the Term Frequency (TF).  ND is the total number of documents and NDt is the number of documents containing the term t, this provides the Inverse Document Frequency (IDF).  TF-IDF for a term t is a multiplication of Term Frequency and Inverse Document Frequency for the given term t:

TFIDF(t)=tf(t)*idf(t)

To get info on cosine similrity use "https://www.machinelearningplus.com/nlp/cosine-similarity/"
