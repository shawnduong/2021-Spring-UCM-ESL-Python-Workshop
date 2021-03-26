ANSWERS = (
	"Read https://shawnd.xyz/assets/misc/2021-03-30/company_directory.html.",
	"Make a list of all the individual URLs on the webpage.",
	"A: While the list of URLs is not empty, continue. Else, stop the program.",
	"Go to a URL in the list.",
	"Make a list of all the individual contacts in the URL.",
	"B: While the list of people is not empty, continue. Else, go to step C.",
	"Go to a person in the list of people.",
	"Add their contact information to the spreadsheet.",
	"Remove them from the list of people.",
	"Go back to step B.",
	"C: Remove the finished URL from the list.",
	"Go back to step A.",
)

def answer_checker(f="logic.txt"):

	submission = [l.lstrip().rstrip() for l in open(f, "r").readlines() if len(l) > 4]

	for i in range(len(submission)):
		if submission[i].lower() != ANSWERS[i].lower():
			return f"Your algorithm started going wrong at: {submission[i]}"

	return True

