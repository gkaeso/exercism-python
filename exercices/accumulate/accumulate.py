def accumulate(collection, operation):
    return [operation(elt) for elt in collection]
