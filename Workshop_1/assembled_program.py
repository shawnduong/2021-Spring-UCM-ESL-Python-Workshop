# Howdy! This is a comment. Comments start with a "#" sign. I see that you're
# reading through the source code. I highly commend your motivation! These
# comments will help you through the source code.

# Don't worry about understanding the intricacies of the language. Try to focus
# more on the logic and getting the general flow.

# We first start off by defining our function. A function is a collection of
# code that does something. Here, this function is our assembled program.
def assembled_program():

	# This is just some setup stuff. This allows us to use code that other people
	# have written, called libraries.
	import bs4
	import requests
	import spreadsheet
	import time

	# This just prints some logs so we know what's going on. The program then
	# pauses for 5 seconds so that you can actually read it.
	print("PROGRAM: Preparing to scrape. The output will be contacts.csv.")
	time.sleep(5)

	# Make a new spreadsheet called contacts.csv.
	sheet = spreadsheet.make_new("contacts.csv")

	# Make the headers in the spreadsheet.
	sheet.write("Last Name", "First Name", "Company", "Phone Number")

	# !! Read https://shawnd.xyz/assets/misc/2021-03-30/.
	html = requests.get("https://shawnd.xyz/assets/misc/2021-03-30/").content

	# This "soup" is what allows us to scrape data from the website!
	soup = bs4.BeautifulSoup(html, "html.parser")

	# !! Make a list of all the individual URLs on the webpage.
	urls = soup.find("ul", attrs={"id": "companiesList"}).find_all("a")

	# !! A: While the list of URLs is not empty, continue. Else, stop the program.
	while len(urls) > 0:

		# !! Go to a URL in the list.
		url = urls[0]

		# !! Make a list of all the individual contacts in the URL.
		page = requests.get("https://shawnd.xyz/assets/misc/2021-03-30/" + url["href"]).content
		pageSoup = bs4.BeautifulSoup(page, "html.parser")

		# Sidenote but this is technically a dictionary, not a list! But
		# let's not worry about the differences between those two right now.
		contacts = {}

		# We're gonna store the company name so that we know everyone we're
		# about to get contact information from is a part of the client company
		# in question.
		company = url.text
		print(f"PROGRAM: Scraping {company}...")

		# We're gonna learn for loops next workshop, but this basically reads as
		# "for every entry on the web page, do..."
		for entry in pageSoup.find_all("tr", attrs={"id": "entry"}):

			columns = entry.find_all("td")
			last, first = columns[0].text.split(", ")
			phoneNumber = columns[1].text

			contacts[(last, first)] = (company, phoneNumber)

		# !! B: While the list of people is not empty, continue. Else, go to step C.
		while len(contacts) > 0:

			# !! Go to a person in the list of people.
			person = list(contacts.keys())[0]

			# !! Add their contact information to the spreadsheet.
			# In a real-life scenario, we'd be using a complex dictionary
			# instead of what we have, which is much simpler but less versatile.
			last    = person[0]
			first   = person[1]
			company = contacts[person][0]
			number  = contacts[person][1]

			print(f"PROGRAM: Writing the contact information of {company}: {first} {last}")
			sheet.write(last, first, company, number)

			# !! Remove them from the list of people.
			# Sidenote but this is technically a dictionary, not a list! But
			# let's not worry about the differences between those two right now.
			contacts.pop(person)

			# !! Go back to step B.
			# This is automatically done by the indentation and loop!

		# !! C: Remove the finished URL from the list.
		if url in urls:
			urls.remove(url)

		# !! Go back to step A.
		# This is automatically done by the indentation and loop!

	# And we're done!
	print("PROGRAM: Done!")
	print("PROGRAM: Check out contacts.csv")

	# Congrats on making it to the end!

