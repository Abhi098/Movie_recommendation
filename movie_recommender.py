import pandas as pd  
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

data=pd.read_csv("tmdb_5000_movies.csv")
data2=pd.read_csv("tmdb_5000_credits.csv")

print(data.columns)
print("##########")
print(data2.columns)

data2.columns=["id",'Title','Cast','Crew']

data.merge(data2,on='id')

print(data.shape)

C=data['vote_average'].mean()
print("C",C)
avg=data['vote_count'].mean()
print("AVG",avg)

movies=data.copy().loc[data['vote_count']>=avg]
print(movies.shape)
arr=[]
for v,c in zip(movies['vote_count'],movies['vote_average']):
	value=(v/(v+avg) * c) + (avg/(avg+v) * C)

movies['scores']=value

print(movies.shape)

movies['scores']=movies['scores']+movies['popularity']

movies=movies.sort_values('scores',ascending=False)

print(movies[['title','vote_count','scores']].head(5))

#########################################################


tfidf = TfidfVectorizer(stop_words='english')

data['overview'] = data['overview'].fillna('')

tfidf_matrix = tfidf.fit_transform(data['overview'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

indices = pd.Series(data.index, index=data['title']).drop_duplicates()

idx=indices['The Dark Knight Rises']
similar = list(enumerate(cosine_sim[idx]))

similar = sorted(similar, key=lambda x: x[1], reverse=True)
count=0
print("##########################")
for i in similar:
	if count<10:
		print(data['title'][i[0]])
		count+=1
	else :
		break	


# print("Sim scores",sim_scores)