class School:
    def __init__(self):
        self.school_roster = []
        

    def add_student(self, name, grade):
        self.school_roster.append((grade, name))
     

    def roster(self):
        return [name[1] for name in sorted(self.school_roster)]
                

    def grade(self, grade_number):
        names = []
        if self.school_roster:     
            for g, n in sorted(self.school_roster):
                if g == grade_number:
                    names.append(n)
        return names
