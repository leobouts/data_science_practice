from sklearn.feature_extraction.text import CountVectorizer
from sklearn import feature_extraction
from heapq import nlargest
from functools import reduce
from operator import add
import scipy.spatial.distance as dist
import heapq
import random
import numpy
import string
import json
import re

# Computes the UCF score of n similar recipes
def user_based_collaborative_filtering(n,matrix):
	scores = []
	for i,obj in enumerate(recipes):
		jaccard_dot_matrix_sum = 0
		jaccard_sum = 0
		for j,obj in enumerate(recipes[i]):
			for k in range(n):
				m = set_of_n_similar_recipes[i][k]
				#print(vectorized_matrix_m[m][j])
				jaccard_dot_matrix_sum += most_similar_jaccard_values[j][k] * matrix[m][i]
				jaccard_sum += most_similar_jaccard_values[j][k]

			scores.append(jaccard_dot_matrix_sum/jaccard_sum)
	return scores


## Computes Jaccard similarity
def jaccard_similarity(list1, list2):
    set1, set2 = set(list1), set(list2)
    # Jaccard = Intersection(set1,set2) / Union(set1,set2)
    return len(set1 & set2) / len(set1 | set2)

## returns the n most similar recipes for every recipe
def get_n_similar_recipes(n,data):
	similar_recipes = []
	for i,obj in enumerate(data):
		a = numpy.array(distance[i])
		#the Jaccard similarity of an item with itself is always 1.
		#we are going to get the n+1 largest values so we can pop out
		#the one with itself.
		
		#gives the indexes of the n+1 largest values
		most_similar = heapq.nlargest(n+1, range(len(a)), a.take)

		#remove the most similar(itself)
		most_similar.pop(0)
		similar_recipes.append(most_similar)

	return similar_recipes

## returns the Jaccard similarity of the n most similar recipes
## for every recipe

def get_n_similar_jaccard(n,data):
	values = []
	for i,obj in enumerate(data):
		#gives the jaccard of the n+1 largest values
		jaccard = heapq.nlargest(n+1, distance[i])
		#remove the most similar(itself)
		jaccard.pop(0)
		values.append(jaccard)

	return values

## returns a list of 1000 recipes with one random ingredient deleted
def clean_data():
	f = open('train.json')
	data = json.load(f)

	recipe_list = []

	for i in data:
		#split with comma to get the cuisine.
		split1=str(i).split(',')
		#clean the strings with split and regex
		split2 = split1[1].split(':')
		cuisine = re.sub(r'[.\W]','',split2[1])
		#get the recipe id
		recipe_split = split1[0].split(': ')
		recipe_id=recipe_split[1]
		#keep only the pepperoni guys
		if cuisine=='italian':
			#splitting with [ because ingredients have the only list in the string
			split3=str(i).split('[')
			#final cut
			ingredients=split3[1].split(',')
			#removing ' from the strings
			ingredients = [s.translate(str.maketrans('','',string.punctuation)) for s in ingredients]
			recipe_list.append(ingredients)

	#randomize the recipes
	random.shuffle(recipe_list)
	#get the first 1000 randomized items
	set_of_recipes = recipe_list[:1000]

	#remove 1 random ingredient from every recipe
	for i,obj in enumerate(set_of_recipes):
		#remove whitespaces
		set_of_recipes[i] = [x.strip() for x in set_of_recipes[i]]
		#randomise the list and remove the first element
		random.shuffle(set_of_recipes[i])
		set_of_recipes[i].pop(0)

	return set_of_recipes



def create_vectorized_matrix():
	matrix =[]
	for i,obj in enumerate(recipes):
		vector = [0] * len(unique_igredients)
		for j,obj in enumerate(recipes[i]):
			if recipes[i][j] in unique_igredients:
				vector[unique_igredients.tolist().index(recipes[i][j])] = 1
		matrix.append(vector)
	return matrix


def main():
	#will hold the jaccard similarity
	global distance
	global most_similar_jaccard_values
	global set_of_n_similar_recipes
	global recipes
	global unique_igredients

	recipes = clean_data()


	#make the 2d list 1d so we can count occurences easily
	flattened_recipes_set = recipes.copy()
	flattened_recipes_set = reduce(lambda x,y :x+y ,flattened_recipes_set)

	#remove whitespaces
	#flattened_recipes_set = [x.strip() for x in flattened_recipes_set]

	#popular is a dictionary with : (ingredient,times igredient used in all the recipes)
	popular = dict((x,flattened_recipes_set.count(x)) for x in set(flattened_recipes_set))

	#find the unique ingredients list
	numpy_of_flattened = numpy.array(flattened_recipes_set)
	unique_igredients = numpy.unique(numpy_of_flattened)



	#Create Vectorized Matrix
	vectorized_matrix_m = create_vectorized_matrix()


	#list that holds every score for every ingredient.
	#every line i of the array corresponds to the score
	#the ingredients have for the recipe in line i of the recipes array.
	most_popular_score_list = []

	#popular_without_recipes_ingredients is a dict but without the ingredients of the current recipe
	#of the loop.
	for i in recipes:
		popular_without_recipes_ingredients = list(filter(lambda x: x in i, popular)) 
		most_popular_score_list.append(popular_without_recipes_ingredients)
			
	distance = []
	for elem1 in recipes:
		#list with the jaccard of the recipe elem1 with every other
		jaccard_of_recipe = []
		for elem2 in recipes:
			jaccard_of_recipe.append(jaccard_similarity(elem1,elem2))
		distance.append(jaccard_of_recipe)

	#distance array now has in line i the jacard similarity of
	#the recipe of line i in the recipes set with every other recipe


	#set_of_n_similar_recipes has in each line i the n most similar recipes
	#for the recipe in line i of the recipes array according to the jaccard metric

	set_of_n_similar_recipes = get_n_similar_recipes(10,recipes)
	most_similar_jaccard_values = get_n_similar_jaccard(10,recipes)

	#print(set_of_n_similar_recipes)
	#print(vectorized_matrix_m)
	scores = []
	scores = user_based_collaborative_filtering(10,vectorized_matrix_m)
	print(scores)


if __name__== "__main__":
  main()


