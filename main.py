import scrapper
from bs4 import BeautifulSoup
import requests

website = 'https://www.rottentomatoes.com'
list_of_data = []
def getMovies(movie_link):
	
	main_page = requests.get(website+movie_link)
	main_soup = BeautifulSoup(main_page.content, 'html.parser') 
	main_container = main_soup.findAll('div',{"id":"main_container"})[0]
	section = main_container.findAll('section')[0]
	table = section.findAll('table',{"class":"table"})[0]
	tr = table.findAll('tr')
	tr_len = len(tr)
	for index in range(1, tr_len):

		tr = table.findAll('tr')[index]
		a = tr.findAll('a')[0].get('href')
		link = website+a
		
	
		try:
			list_of_data.append(scrapper.scrape(link))
		except:
			print('error in parsing')
	print(list_of_data)

if __name__ == '__main__':
	list_of_links = ['/top/bestofrt/','/top/bestofrt/top_100_action__adventure_movies/',
	'/top/bestofrt/top_100_animation_movies/','/top/bestofrt/top_100_art_house__international_movies/',
	'/top/bestofrt/top_100_classics_movies/','/top/bestofrt/top_100_comedy_movies/',
	'/top/bestofrt/top_100_documentary_movies/','/top/bestofrt/top_100_drama_movies/',
	'/top/bestofrt/top_100_horror_movies/','/top/bestofrt/top_100_kids__family_movies/','/top/bestofrt/top_100_musical__performing_arts_movies/',
	'/top/bestofrt/top_100_mystery__suspense_movies/','/top/bestofrt/top_100_romance_movies/',
	'/top/bestofrt/top_100_science_fiction__fantasy_movies/','/top/bestofrt/top_100_special_interest_movies/',
	'/top/bestofrt/top_100_sports__fitness_movies/','/top/bestofrt/top_100_television_movies/','/top/bestofrt/top_100_western_movies/']

	for link in list_of_links:
		getMovies(link)