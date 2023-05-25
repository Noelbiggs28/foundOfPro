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
        self._streaming_services.append(streaming_service_object)

    def delete_streaming_service(self, streaming_service_name):
        for elem in self._streaming_services:
            if elem.get_name() == streaming_service_name:
                self._streaming_services.remove(elem)

    def where_to_watch_movie(self, movie_title):
        watch_list = []
        for streaming_obj in self._streaming_services:
            streaming_obj_name = streaming_obj.get_name()
            streaming_service_catalog = streaming_obj.get_catalog()
            if movie_title in streaming_service_catalog:
                movie_string = f"{movie_title} ({streaming_service_catalog[movie_title].get_year()})"
                if movie_string not in watch_list:
                    watch_list.append(movie_string)
                watch_list.append(streaming_obj_name)
        if len(watch_list) == 0:
            return None
        return watch_list


movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

stream_serv_1 = StreamingService('Netflick')
stream_serv_1.add_movie(movie_2)

stream_serv_2 = StreamingService('Hula')
stream_serv_2.add_movie(movie_1)
stream_serv_2.add_movie(movie_4)
stream_serv_2.delete_movie('The Seventh Seal')
stream_serv_2.add_movie(movie_2)

stream_serv_3 = StreamingService('Dizzy+')
stream_serv_3.add_movie(movie_4)
stream_serv_3.add_movie(movie_3)
stream_serv_3.add_movie(movie_1)

stream_guide = StreamingGuide()
stream_guide.add_streaming_service(stream_serv_1)
stream_guide.add_streaming_service(stream_serv_2)
stream_guide.add_streaming_service(stream_serv_3)
stream_guide.delete_streaming_service('Hula')
search_results = stream_guide.where_to_watch_movie('Little Women')
print(search_results)