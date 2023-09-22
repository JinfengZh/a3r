''' calculate film strength'''


import operator


def film_strength(MUR, MUC, MUD, user_id, film_id, films, ratings, similarities_for_user, movies_genres, movies_authors):
	nSimUsers = 20 # number of similar users to use
	simsSorted = sorted(similarities_for_user, key = operator.itemgetter(1), reverse = True)
	sims = simsSorted[:nSimUsers]
	film = films[film_id]

	# take an average of each of the the genre's average ratings
	
    
    
	nDirectors = 0
	dDirectors = 0
	if type(film['authors']) is str:
		film['authors'] = [film['authors']]
	for director in film['authors']:
		aspect_value =  movies_authors[director].to_dict()
		movie_ids_with_aspect_value = [k for k,v in aspect_value.items() if v == 1]

		# get the average rating for each film of this director and take an average of those from the user and similar users
		nDirector = 0
		dDirector = 0
		nDirectorSim = 0
		dDirectorSim = 0

		for directorfilm in movie_ids_with_aspect_value:
			if (directorfilm, user_id) in ratings.keys():
				dDirector += ((ratings[(directorfilm, user_id)] - 1) / 2)-1   # adds this to the current user's ratings total for this director
				nDirector += 1         # and the count
			else:
				avg_rat = average_rating(sims, directorfilm, ratings)
				if avg_rat:
					dDirectorSim += MUR * avg_rat  # adds this average to the similar users' ratings total for this Director
					nDirectorSim += 1       # and the count

		if nDirector > 0:              # if we have films of this Director with ratings from the user
			if nDirectorSim > 0:        # and also films of this Director with ratings from similar users
				avDirector = ((dDirector / nDirector) + (dDirectorSim / nDirectorSim)) / (1 + MUR)       # uses both the current user's and similar users' ratings 
			else:
				avDirector = dDirector / nDirector       # uses only the current user's ratings
		else:                       # if we do not have films of this Director with ratings from the user
			if nDirectorSim > 0:        # but we have films of this Director with ratings from similar users
				avDirector = dDirectorSim / nDirectorSim       # uses only the similar users' ratings
			else:
				avDirector = 0

		dDirectors += avDirector
		nDirectors += 1

	if nDirectors > 0:
		avgauthorRating = dDirectors / nDirectors
	else:
		avgpriceRating = 0
	nDirectors = 0
	dDirectors = 0
	if type(film['genres']) is str:
		film['genres'] = [film['genres']]
	for director in film['genres']:
		aspect_value =  movies_genres[director].to_dict()
		movie_ids_with_aspect_value = [k for k,v in aspect_value.items() if v == 1]

		# get the average rating for each film of this director and take an average of those from the user and similar users
		nDirector = 0
		dDirector = 0
		nDirectorSim = 0
		dDirectorSim = 0

		for directorfilm in movie_ids_with_aspect_value:
			if (directorfilm, user_id) in ratings.keys():
				dDirector += ((ratings[(directorfilm, user_id)] - 1) / 2)-1   # adds this to the current user's ratings total for this director
				nDirector += 1         # and the count
			else:
				avg_rat = average_rating(sims, directorfilm, ratings)
				if avg_rat:
					dDirectorSim += MUR * avg_rat  # adds this average to the similar users' ratings total for this Director
					nDirectorSim += 1       # and the count

		if nDirector > 0:              # if we have films of this Director with ratings from the user
			if nDirectorSim > 0:        # and also films of this Director with ratings from similar users
				avDirector = ((dDirector / nDirector) + (dDirectorSim / nDirectorSim)) / (1 + MUR)       # uses both the current user's and similar users' ratings 
			else:
				avDirector = dDirector / nDirector       # uses only the current user's ratings
		else:                       # if we do not have films of this Director with ratings from the user
			if nDirectorSim > 0:        # but we have films of this Director with ratings from similar users
				avDirector = dDirectorSim / nDirectorSim       # uses only the similar users' ratings
			else:
				avDirector = 0

		dDirectors += avDirector
		nDirectors += 1

	if nDirectors > 0:
		avggenreRating = dDirectors / nDirectors
	else:
		avgratingRating = 0

	# compute strength
	item_strength = ((MUC * avgauthorRating) + (MUD * avggenreRating)) / ( MUC + MUD)
	film_strength = (((item_strength + 1)*2)+1)
	return film_strength


def average_rating(sims, film_id, ratings):
	# counts and totals for each type of aspect
	nRatings = 0
	dRatings = 0

	for sim in sims:
		user_id = sim[0]
		similarity = sim[1]

		if (film_id, user_id) in ratings.keys():
			user_rating = ratings[(film_id, user_id)]
			scaled_rating = ((user_rating - 1) / 2)-1
			dRatings += scaled_rating * similarity
			nRatings += 1

	if nRatings == 0:
		return None
	return dRatings / nRatings
