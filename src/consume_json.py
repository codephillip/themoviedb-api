import simplejson as json
import urllib2

from movie.models import Category, Movie


def connect_to_server():
    for page in range(1, 30):
        if(page <= 24):
            continue
        print('PAGE' + str(page))
        base_url = "http://api.themoviedb.org/3/discover/movie?primary_release_year=2016&sort_by=popularity.desc&api_key=ae6766bd4f9bebf18e24c1bc0c2c282a&"
        actual_url = base_url + 'page=' + str(page)
        # actual_url = 'http://localhost/downloads/movie1.json'
        print('actual: ' + actual_url)
        result = json.load(urllib2.urlopen(actual_url))

        print(result.get('results'))
        result2 = result.get('results')
        print(result2)
        for x in result2:
            print(x.get('original_title'))
            print(x.get('poster_path'))
            print(x.get('overview'))
            try:
                save_to_db(x.get('original_title'), 'http://image.tmdb.org/t/p/w300' + x.get('poster_path'),
                           x.get('overview'), x.get('vote_average'), x.get('release_date'))
            except Exception:
                print(str(Exception))
                save_to_db(x.get('original_title'), x.get('poster_path'),
                          x.get('overview'), x.get('vote_average'), x.get('release_date'))


def save_to_db(title, image, overview, vote_average, release_date):
    cate_object = Category.objects.get(name='2016')
    movie = Movie(name=title, image=image, category=cate_object, description=overview, vote_average=vote_average,
                  release_date=release_date)
    movie.save()


def main():
    connect_to_server()


if __name__ == '__main__':
    main()
