class Garden:

    SEEDS = {'G': 'Grass', 'C': 'Clover', 'R': 'Radishes', 'V': 'Violets'}

    def __init__(self, diagram, students=['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']):
        self.diagram = diagram
        self.students = sorted(students)

    def plants(self, student):
        size = (len(self.diagram)) // 2 + 1
        index = self.students.index(student)*2
        cups = f'{self.diagram[index:index+2]}{self.diagram[size+index:size+index+2]}'
        return [self.SEEDS[s] for s in cups]
