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
    print(f'original={price}')

    for max_size in range(5, 1, -1):
        amount, remaining_books = 0, Counter(basket)
        bundles = []
        print(f'max_size={max_size}')
        for size in range(max_size, 1, -1):
            while remaining_books:
                bundle = tuple(book for book, _ in remaining_books.most_common(size))
                if bundle:
                    bundles.append(bundle)
                    print(f'bundles={bundles}')
                    remaining_books -= Counter(book for book, _ in remaining_books.most_common(size))
                else:
                    break
                amount += BUNDLE_PRICES[len(bundle)]

        print(f'price={amount}')
        price = min(price, amount)

    return price

print(total([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5]))
