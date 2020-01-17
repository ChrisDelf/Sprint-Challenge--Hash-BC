#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        if ticket.source == "NONE":
            route[0] = ticket.destination
    index = 0
    current_destination = 0
    while True:
        current_destination = route[index]
        next_destintation = hash_table_retrieve(hashtable, current_destination)
        index += 1
        route[index] = next_destintation
        if next_destintation == "NONE":
            break

    return route


# tickets = [
#   { source: "PIT", destination: "ORD" },
#   { source: "XNA", destination: "CID" },
#   { source: "SFO", destination: "BHM" },
#   { source: "FLG", destination: "XNA" },
#   { source: "NONE", destination: "LAX" },
#   { source: "LAX", destination: "SFO" },
#   { source: "CID", destination: "SLC" },
#   { source: "ORD", destination: "NONE" },
#   { source: "SLC", destination: "PIT" },
#   { source: "BHM", destination: "FLG" }
# ]
#
# print(reconstruct_trip(tickets, 9))
