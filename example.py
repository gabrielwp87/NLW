my_dict = {
    "hello": "world",
    "I am": "here"
}

other_dict = {
    **my_dict,
    "id": "one",
    "here": "my_dict"
}

print(other_dict)

another_dict = {
    **other_dict,
    "id": "two"
}

print(another_dict)
