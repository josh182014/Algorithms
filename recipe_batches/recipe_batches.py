#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # try one
    # batches = 0
    # max_batches = None
    # for i in ingredients:
    #     for j in recipe:
    #         if i == j and ingredients[i] - recipe[i] < 0:
    #             max_batches = 0
    #             return max_batches
    #         elif i == j and ingredients[i] - recipe[i] >= 0:
    #             while ingredients[i] - recipe[i] >= 0:
    #                 ingredients[i] = ingredients[i] - recipe[i]
    #                 if max_batches != 0:
    #                     batches += 1
    #         max_batches = batches
    # return max_batches

    # try two
    batches = 0
    max_batches = 0
    batch_array = []
    for i in ingredients:
        for j in recipe:
            if j not in ingredients:
                batch_array.append(0)
            if i == j:
                while ingredients[i] - recipe[i] >= 0:
                    ingredients[i] = ingredients[i] - recipe[i]
                    batches += 1
        batch_array.append(batches)
        batches = 0
    print(batch_array)
    print(max_batches)
    batch_array.sort()
    max_batches = batch_array[0]
    return max_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 50, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
