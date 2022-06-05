class Video:
    def __init__(self,category,name,description,date,director,age_calification):
        self.category = category
        self.name = name
        self.description = description
        self.date = date
        self.director = director
        self.age_calification = age_calification

    def __str__(self):
        return f'-------------------------\nCategoria: {self.category}' \
        f'\nNombre: {self.name}' \
        f'\nDescripcion: {self.description}' \
        f'\nFecha: {self.date}' \
        f'\nCalificacion: {self.age_calification}' \

class Series(Video):

    def __init__(self, category, name, description, date, director, age_calification,seasons):
        super().__init__(category, name, description, date, director, age_calification)
        self.seasons = seasons

    def __str__(self):
        return super().__str__() + f'\nTemporadas: {self.seasons}'

    def add_season(self):
        self.seasons += 1

class Movie(Video):

    def __init__(self, category, name, description, date, director, age_calification, length):
        super().__init__(category, name, description, date, director, age_calification)
        self.length = length

    def __str__(self):
        return super().__str__() + f'\nDuracion: {self.length}'
