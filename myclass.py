class flower:
    def __init__(self, name, color, season):
        self.name = name.capitalize()
        self.color = color.capitalize()
        self.season = season.capitalize()
        
    def show(self):
        new=self.name + " " +self.color +" " + self.season
        return new
        


