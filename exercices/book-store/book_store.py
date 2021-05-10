from collections import Counter


BOOK_PRICE = 800

BUNDLE_PRICES = {
    1: 1 * BOOK_PRICE,
    2: 2 * BOOK_PRICE * 0.95,
    3: 3 * BOOK_PRICE * 0.90,
    4: 4 * BOOK_PRICE * 0.80,
    5: 5 * BOOK_PRICE * 0.75,
}


def total(basket):
    price: float = len(basket) * BOOK_PRICE

    book_counter = Counter(basket)
    for max_size in range(len(book_counter), 1, -1):
        remaining_book_counter = book_counter - Counter(book for book, _ in book_counter.most_common(max_size))
        remaining_books = list(remaining_book_counter.elements())
        price = min(price, BUNDLE_PRICES[max_size] + total(remaining_books))

    return price

