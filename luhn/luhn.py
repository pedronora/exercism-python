class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')


    def valid(self):
        if all(map(str.isdigit, self.card_num)) and len(self.card_num) > 1:
            numbers = list(filter(str.isdigit, self.card_num))

            sum_all = 0
            for n, i in enumerate(numbers[::-1]):
                if (int(i) == 9) or (n % 2 == 0):
                    sum_all += int(i)
                else:
                    sum_all += (int(i)*2) % 9

            if sum_all % 10 == 0:
                return True
        return False
