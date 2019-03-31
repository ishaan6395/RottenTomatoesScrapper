from bs4 import BeautifulSoup
import requests

def scrape(link=''):
		page = requests.get(link)

		soup = BeautifulSoup(page.content, 'html.parser') 


	
		#Declare all varialbles
		name = ''
		percent = ''
		audience_score = ''
		reviews_counted = ''
		user_ratings = ''
		description = ''
		mpaa = ''
		genres = ''
		directed_by  = ''
		written_by = ''
		release_date = ''
		on_disc = ''
		box_office = ''
		runtime = ''
		studio = '',
		cast = []


		#Find name
		try:
			name_link = soup.findAll('div',{"class":"mop-ratings-wrap score_panel"})[0]
			name = name_link.findAll('h1')[0].get_text().strip()
		except:
			name = ''

		#Find Percentage
		try:
			percent_link = soup.findAll('span',{"class":"mop-ratings-wrap__percentage"})[0]
			percent = percent_link.get_text().strip()
		except:
			percent = ''

		#audience Score
		try:
			audience_score_link = soup.findAll('div',{"class":"mop-ratings-wrap__half"})[1]
			audience_score = audience_score_link.findAll('span',{"class":"mop-ratings-wrap__percentage"})[0].get_text().strip().split('\n')[0]
		except:
			audience_score = ''

		#Reviews Counted
		try:
			reviews_counted_link = soup.findAll('div',{"class":"mop-ratings-wrap__review-totals"})[0]
			reviews_counted = reviews_counted_link.findAll('small',{"class":"mop-ratings-wrap__text--small"})[0].get_text().strip()
		except:
			reviews_counted = ''

		#user Ratings
		try:
			user_ratings_link = soup.findAll('div',{"class":"mop-ratings-wrap__review-totals"})[1]
			user_ratings = user_ratings_link.findAll('small',{"class":"mop-ratings-wrap__text--small"})[0].get_text().strip()
		except:
			user_ratings = ''


		# Description
		try:
			description_box_link = soup.findAll('section',{"class":"panel panel-rt panel-box movie_info media"})[0]
			description_link = description_box_link.findAll('div',{"class":"movie_synopsis clamp clamp-6"})[0]
			description = description_link.get_text().strip()
		except:
			description = ''

		#MPAA
		try:
			mpaa_box_link = soup.findAll('section',{"class":"panel panel-rt panel-box movie_info media"})[0]
			mpaa_link = mpaa_box_link.findAll('div',{"class":"meta-value"})[0]
			mpaa = mpaa_link.get_text().strip()
		except:
			mpaa = ''


		#genre
		try:
			genre_box_link = soup.findAll('section',{"class":"panel panel-rt panel-box movie_info media"})[0]
			genre_link = genre_box_link.findAll('div',{"class":"meta-value"})[1]
			ls = genre_link.get_text().strip().split('\n')
			genres = ''
			for x in ls:
				if x.strip().replace(' ','') is not '':
					genres+=x.strip()
		except:
			genres = ''


		#directed by
		try:
			directed_by_box_link = soup.findAll('section',{"class":"panel panel-rt panel-box movie_info media"})[0]
			directed_by_link = directed_by_box_link.findAll('div',{"class":"meta-value"})[2]
			directed_by = directed_by_link.get_text().strip()
		except:
			directed_by = ''



		#written by
		try:
			written_by_box_link = soup.findAll('section',{"class":"panel panel-rt panel-box movie_info media"})[0]
			written_by_link = written_by_box_link.findAll('div',{"class":"meta-value"})[3]
			written_by_list = written_by_link.get_text().strip().split('\n')
			written_by = ''
			for item in written_by_list:
				if item.replace(' ','') is not '':
					written_by+=item.strip()
		except:
			written_by = ''



		# release date
		try:
			release_date_box_link = soup.findAll('section',{"class":"panel panel-rt panel-box movie_info media"})[0]
			release_date_link = release_date_box_link.findAll('div',{"class":"meta-value"})[4]
			release_date = release_date_link.get_text().strip().split('\n')[0]
		except:
			release_date = ''

		#on disc
		try:
			on_disc_box_link = soup.findAll('section',{"class":"panel panel-rt panel-box movie_info media"})[0]
			on_disc_link = on_disc_box_link.findAll('div',{"class":"meta-value"})[5]
			on_disc = on_disc_link.get_text().strip()
		except:
			on_disc = ''


		# check if box office is present or not
		box_office_box = soup.findAll('section',{"class":"panel panel-rt panel-box movie_info media"})[0]
		lists = box_office_box.findAll('li',{"class":"meta-row clearfix"})[6]
		if 'Box Office' in lists.get_text():
			try:
				box_office_box =  on_disc_box_link.findAll('div',{"class":"meta-value"})[6]
				box_office = box_office_box.get_text().strip()

			except:
				print('here')
				box_office = ''

			#runtime
			try:
				runtime_link =  on_disc_box_link.findAll('div',{"class":"meta-value"})[7]
				runtime = runtime_link.get_text().strip()
			except:
				runtime = ''

			#studio
			try:
				studio_link = on_disc_box_link.findAll('div',{"class":"meta-value"})[8]
				studio = studio_link.get_text().strip()
			except:
				studio = ''
		else:
			
			box_office = ''
			

			#runtime
			try:
				runtime_link =  on_disc_box_link.findAll('div',{"class":"meta-value"})[6]
				runtime = runtime_link.get_text().strip()
			except:
				runtime = ''

			#studio
			try:
				studio_link = on_disc_box_link.findAll('div',{"class":"meta-value"})[7]
				studio = studio_link.get_text().strip()
			except:
				studio = ''
		

		#Movie cast 
		try:
			cast_box_link = soup.findAll('section',{"id":"movie-cast"})[0]
			cast_list_div = cast_box_link.findAll('div',{"class":"castSection"})[0]
			cast_list = cast_list_div.findAll('div',{"class":"media-body"})
			for div in cast_list:
				span = div.findAll('span')[0].get_text().strip()
				cast.append(span)
		except:
			cast = []

		dict = {
			"name":name,
			"percent": percent,
			"audience_score": audience_score,
			"reviews_counted": reviews_counted,
			"user_ratings":user_ratings,
			"description": description,
			"mpaa":mpaa,
			"genres":genres,
			"directed_by":directed_by,
			"written_by":written_by,
			"release_date":release_date,
			"on_disc":on_disc,
			"box_office":box_office,
			"runtime":runtime,
			"studio":studio,
			"cast":cast


		}

		return dict
	