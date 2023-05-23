class Movie:
    def __init__(self, title, genre, director, year):
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        return self._title

    def get_genre(self):
        return self._genre
    
    def get_director(self):
        return self._director

    def get_year(self):
        return self._year

class StreamingService:
    def __init__(self, name):
        self._name = name
        self._catalog = {}

    def get_name(self):
        return self._name
    
    def get_catalog(self):
        return self._catalog
    
    def add_movie(self, movie_object):
        self._catalog[movie_object.get_title()] = movie_object

    def delete_movie(self, movie_title):
        self._catalog.pop(movie_title)


class StreamingGuide:
    def __init__(self):
        self._streaming_services = []

    def add_streaming_service(self, streaming_service_object):
        self._streaming_services.append(streaming_service_object.get_name())

    def delete_streaming_service(self, streaming_service_object):
        ind = self._streaming_services.index(streaming_service_object)
        del(self._streaming_services[ind])

    def where_to_watch_movie(self, movie_title):
        movie_name = movie_title
        movie_year = movie_title.get_year()
        watchlist = [movie_name + ' (' + movie_year + ')']
    #     # for service in self._services: 
    #     #     if movie in service.get_catalog():
    #     #         watchlist.append(service.get_name())
        return watchlist

guide_1 = StreamingGuide
movie_1 = Movie('bugs', 'kids', 'ben', '2008')
movie_2 = Movie('ants', 'kids', 'steve', '2010')
netflix = StreamingService('netflix')
netflix.add_movie(movie_1)
netflix.add_movie(movie_2)
netflix.delete_movie('bugs')
hulu = StreamingService('hulu')

DemoStreamingGuide = StreamingGuide()
DemoStreamingGuide.add_streaming_service(netflix)
DemoStreamingGuide.add_streaming_service(hulu)
# DemoStreamingGuide.delete_streaming_service('netflix')
print(DemoStreamingGuide._streaming_services)
print(netflix.get_catalog())
print(guide_1.where_to_watch_movie('ants'))