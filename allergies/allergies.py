# Solution without use BitWise
items = {128: 'cats', 64: 'pollen', 32: 'chocolate',  16: 'tomatoes', 8: 'strawberries', 4: 'shellfish', 2: 'peanuts', 1: 'eggs'}

class Allergies:

    def __init__(self, score):
        if score > 256:
            self.score = score - ((score // 256) * 256)
        else:
            self.score = score

    def allergic_to(self, item):
        if item in Allergies(self.score).lst:
            return True
        return False

    @property
    def lst(self):
        all_allergies = []
    
        index = 0
        if self.score % 2 != 0:
            all_allergies.append(items[1])
            self.score -= 1
            index = 1

        while self.score > 0:
            for k in items:
                if k <= self.score:
                    self.score -= k
                    all_allergies.insert(index, items[k])
        return all_allergies


# Solution using BitWise
items = ['eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats']

class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        if item in Allergies(self.score).lst:
            return True
        return False

    @property
    def lst(self):
        all_allergies = []

        for n in range(len(items)):
            if self.score & 2**n:
                all_allergies.append(items[n])
        return all_allergies
