class PhoneNumber:
    def __init__(self, number):
        numbers = ''.join((filter(str.isdigit, number)))

        if numbers[0] == '1':
            numbers = numbers[1:]
        
        if len(numbers) != 10:
            raise ValueError('Invalid phone number format')

        if numbers[0] in ['0', '1'] or numbers[3] in ['0', '1']:
            raise ValueError('Invalid phone number format')

        self.number = numbers
        self.area_code = self.number[:3]

    def pretty(self):
        return f'({self.area_code})-{self.number[3:6]}-{self.number[6:]}'
