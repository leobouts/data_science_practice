# # print("a random recipe with values to test if the jaccard is correct")
# # print("88th recipe:")
# # print(sorted(recipes[88]))
# # print('================')
# # print("Jaccard of second recipe with 88th recipe")
# # print(distance_recipes[1][88])
# # print('================')
# a = list_of_lists_of_most_similar_jaccard_values_for_every_n_ucf[1]
# b = list_of_lists_of_most_similar_recipes_for_every_n_ucf[1]
# # #print(len(a))
# # #print(len(b))
# # print("5 most similar recipes(indexes) of the 2th recipe")
# # print(b[1])
# # print("5 most similar jaccard values of the 2th recipe between these:")
# # print(a[1])
# # print("================")
# # # for i in b[0]:
# # #     print(i)
# # #     print(recipes[i])
# # #     print('%%%%%%%%%%%')
# # print("=================")
# # sum_of_jaccard = sum(a[1])
# # print("sum of 5 most similar jaccard values of the 0th recipe between these:")
# # print(sum_of_jaccard)
# # print("=================")



# test_recipe_number = 2

# print("binary matrix values")
# print("M[r',i]")
# for i in b[1]:
#     print("-----------------")
#     print(recipes[i])
#     print("-----------------")
#     for j in sorted(sorted(recipes[test_recipe_number])):
#         print("M[",i,",",j,"]",vectorized_matrix_m[i][unique_ingredients.tolist().index(j)])
#     print("=================")
#     break

# print("recipe before removing:")
# print(sorted(recipes_before_removing_element[test_recipe_number]))
# print("recipe:")
# print(sorted(recipes[test_recipe_number]))
# print('================')
# #hidden_element = list(set(recipes_before_removing_element[test_recipe_number]) - set(recipes[test_recipe_number]))
# #print(hidden_element)
# #print("algorithm found:")
# print("UCF scores for:")
# print(list_of_lists_of_scores_for_every_n_ucf[1][test_recipe_number])
# #max_value = max(list_of_lists_of_scores_for_every_n_ucf[1][test_recipe_number])
# #max_index = list_of_lists_of_scores_for_every_n_ucf[1][test_recipe_number].index(max_value)
# #print(unique_ingredients[max_index])
# print(unique_ingredients[3])

