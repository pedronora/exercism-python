class Matrix:
    def __init__(self, matrix_string):
        input = matrix_string.split('\n')
        
        # Create rows
        self.rows = []
        for row in input:
            new_row = row.split(' ')
            new_row = [int(n) for n in new_row]
            self.rows.append(new_row)
        
        # Create columns
        self.columns = list(map(list, zip(*self.rows)))


    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]
