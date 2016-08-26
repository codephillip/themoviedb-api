import simplejson as json
import urllib2

for page in range(1, 3):
    print('PAGE' + str(page))
    base_url = "http://api.themoviedb.org/3/discover/movie?primary_release_year=2016&sort_by=popularity.desc&api_key=ae6766bd4f9bebf18e24c1bc0c2c282a&"
    print(base_url + 'page=' + str(page))
    result = json.load(urllib2.urlopen(base_url + str(page)))

    print(result['page'])
    print(result.get('page'))
    print(result.get('results'))
    result2 = result.get('results')
    for x in result2:
        print(x.get('original_title'))

print(range(1, 3))

for x in range(1, 3):
    print(x)
