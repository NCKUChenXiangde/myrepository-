#統計系116陳祥德H24124068
#1
def top_3_movies_highest_ratings_2016(data):
    movies_2016 = data[data['Year'] == 2016]
    top_3_movies = movies_2016.nlargest(3, 'Rating')[['Title', 'Rating']]
    return top_3_movies

top_3_movies_2016 = top_3_movies_highest_ratings_2016(data)
print(top_3_movies_2016)

"""

print(top_3_movies_2016)


                    Title  Rating
2                  Dangal     8.8
28  Koe no katachi         8.2
45             Hacksaw Ridge     8.1

"""


#2
def director_most_movies(data):
    director_count = data['Director'].value_counts()
    most_involved_director = director_count.idxmax()
    return most_involved_director

most_involved_director = director_most_movies(data)
print(most_involved_director)


"""

print(most_involved_director)

Ridley Scott

"""
#3
def actor_highest_total_revenue(data):
    actor_revenue = {}
    for _, row in data.iterrows():
        actors = row['Actors'].split('|')
        revenue = row['Revenue (Millions)']
        if pd.notna(revenue):
            for actor in actors:
                if actor in actor_revenue:
                    actor_revenue[actor] += revenue
                else:
                    actor_revenue[actor] = revenue
    highest_revenue_actor = max(actor_revenue, key=actor_revenue.get)
    return highest_revenue_actor

highest_revenue_actor = actor_highest_total_revenue(data)
print(highest_revenue_actor)

"""
print(highest_revenue_actor)

Robert Downey Jr.

"""
#4
def average_rating_emma_watson(data):
    emma_movies = data[data['Actors'].str.contains('Emma Watson', na=False)]
    avg_rating = emma_movies['Rating'].mean()
    return avg_rating

emma_watson_avg_rating = average_rating_emma_watson(data)
print(emma_watson_avg_rating)

"""

print(emma_watson_avg_rating)

7.8875

"""
#5
def top_4_actors_most_movies(data):
    actor_movie_count = {}
    for _, row in data.iterrows():
        actors = row['Actors'].split('|')
        for actor in actors:
            if actor in actor_movie_count:
                actor_movie_count[actor] += 1
            else:
                actor_movie_count[actor] = 1
    top_4_actors = sorted(actor_movie_count.items(), key=lambda x: x[1], reverse=True)[:4]
    return top_4_actors

top_4_actors = top_4_actors_most_movies(data)
print(top_4_actors)

"""

print(top_4_actors)

[('Robert De Niro', 7), ('Nicolas Cage', 6), ('Tom Hanks', 6), ('Tom Cruise', 5)]

"""

#6
from collections import Counter

def top_7_collaboration_pairs(data):
    collaboration_pairs = Counter()
    for _, row in data.iterrows():
        director = row['Director']
        actors = row['Actors'].split('|')
        for actor in actors:
            collaboration_pairs[(director, actor)] += 1
    top_7_pairs = collaboration_pairs.most_common(7)
    return top_7_pairs

top_7_pairs = top_7_collaboration_pairs(data)
print(top_7_pairs)

"""

print(top_7_pairs)

[(('Ridley Scott', ' Russell Crowe'), 5), (('Michael Bay', ' Josh Duhamel'), 4), (('James Gunn', ' Chris Pratt'), 4), (('Ridley Scott', ' Michael Fassbender'), 3), (('Michael Bay', ' John Turturro'), 3), (('Ridley Scott', ' Guy Pearce'), 3), (('Tim Burton', ' Johnny Depp'), 3)]

"""

#7
def top_3_directors_most_actors(data):
    director_actors = {}
    for _, row in data.iterrows():
        director = row['Director']
        actors = set(row['Actors'].split('|'))
        if director in director_actors:
            director_actors[director].update(actors)
        else:
            director_actors[director] = actors
    top_3_directors = sorted(director_actors.items(), key=lambda x: len(x[1]), reverse=True)[:3]
    return [(director, len(actors)) for director, actors in top_3_directors]

top_3_directors = top_3_directors_most_actors(data)
print(top_3_directors)

"""

print(top_3_directors)

[('Steven Spielberg', 27), ('Ridley Scott', 26), ('Clint Eastwood', 22)]

"""

#8
def top_6_actors_most_genres(data):
    actor_genres = {}
    for _, row in data.iterrows():
        genres = set(row['Genre'].split('|'))
        actors = row['Actors'].split('|')
        for actor in actors:
            if actor in actor_genres:
                actor_genres[actor].update(genres)
            else:
                actor_genres[actor] = genres
    top_6_actors = sorted(actor_genres.items(), key=lambda x: len(x[1]), reverse=True)[:6]
    return [(actor, len(genres)) for actor, genres in top_6_actors]

top_6_actors_genres = top_6_actors_most_genres(data)
print(top_6_actors_genres)

"""

print(top_6_actors_genres)

[(' Robert De Niro', 10), (' Johnny Depp', 9), (' Bruce Willis', 9), (' Tom Hanks', 8), (' Brad Pitt', 8), (' Tom Cruise', 8)]

"""

#9
def top_3_actors_max_gap_years(data):
    actor_years = {}
    for _, row in data.iterrows():
        year = row['Year']
        actors = row['Actors'].split('|')
        for actor in actors:
            if actor in actor_years:
                actor_years[actor].append(year)
            else:
                actor_years[actor] = [year]
    max_gap_actors = []
    for actor, years in actor_years.items():
        if len(years) > 1:
            max_gap = max(years) - min(years)
            max_gap_actors.append((actor, max_gap))
    top_3_actors = sorted(max_gap_actors, key=lambda x: x[1], reverse=True)[:3]
    return top_3_actors

top_3_actors_gap = top_3_actors_max_gap_years(data)
print(top_3_actors_gap)

"""

print(top_3_actors_gap)

[(' Hugh Jackman', 10), (' Scarlett Johansson', 10), ('Brad Pitt', 10)]

"""