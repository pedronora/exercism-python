class School:
    def __init__(self):
        self.roster_list = []
        

    def add_student(self, name, grade):
        self.roster_list.append((grade, name))
     

    def roster(self):
        return [name[1] for name in sorted(self.roster_list)]
                

    def grade(self, grade_number):
        names = []
        if self.roster_list:     
            for g, n in sorted(self.roster_list):
                if g == grade_number:
                    names.append(n)
        return names
