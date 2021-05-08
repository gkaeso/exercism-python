ALLERGIES = {
    'eggs': 1,
    'peanuts': 2,
    'shellfish': 4,
    'strawberries': 8,
    'tomatoes': 16,
    'chocolate': 32,
    'pollen': 64,
    'cats': 128
}


class Allergies:

    def __init__(self, score):
        self._score: int = score
        self._lst: list[str] = []

    def allergic_to(self, item):
        return bool(self._score & ALLERGIES[item])

    @property
    def lst(self):
        if not self._lst:
            self._lst = [allergy for allergy in ALLERGIES.keys() if self.allergic_to(allergy)]
        return self._lst
