#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    index = 0
    for weight in weights:
        difference_w = limit - weight

        possible_answer = hash_table_retrieve(ht, difference_w)

        if possible_answer is not None:
            if possible_answer < index:
                return(index, possible_answer)
            else:
                return(index, possible_answer)

        hash_table_insert(ht, weight, index)
        index +=1

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

weights = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21

print(get_indices_of_item_weights(weights, length, limit))
