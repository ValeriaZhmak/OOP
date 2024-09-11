# Базові класи
class Book:
    def info(self):
        print("This is a Book")

class Movie:
    def info(self):
        print("This is a Movie")

class VideoGame:
    def info(self):
        print("This is a Video Game")

class TVSeries:
    def info(self):
        print("This is a TV Series")

# Клас, що успадковує від усіх чотирьох
class Multimedia( Movie, Book,VideoGame, TVSeries):
    pass

media = Multimedia()
print(Multimedia.mro())
media.info()
