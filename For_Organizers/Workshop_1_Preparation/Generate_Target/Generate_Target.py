#!/usr/bin/env python3

import hashlib
import os
import random
import shutil

OUTPUT_PATH = "./target/"
N_COMPANIES = 10
N_EMPLOYEES = 50

def main():

	print(":: Generating targets...")

	if os.path.exists(OUTPUT_PATH):
		shutil.rmtree(OUTPUT_PATH)

	os.mkdir(OUTPUT_PATH)

	companies = [l.strip("\n") for l in open("fake_companies.txt", "r").readlines()]
	employees = [l.strip("\n") for l in open("fake_employees.txt", "r").readlines()]
	phNumbers = [l.strip("\n") for l in open("fake_phNumbers.txt", "r").readlines()]
	md5hashes = {}

	for i in range(N_COMPANIES):

		company = random.choice(companies)
		companies.remove(company)

		md5hash = hashlib.md5(company.encode()).hexdigest()
		md5hashes[md5hash] = company

		html  = "<!DOCTYPE html>\n"
		html += "<html>\n"
		html += "<head>\n"
		html += f"\t<title>{company} - CONTACTS DIRECTORY</title>\n"
		html += f"\t<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">\n"
		html += "</head>\n"
		html += "<body>\n"
		html += f"\t<h1>{company} - CONTACTS DIRECTORY</h1>\n"
		html += "\t\t<table id=\"directory\">\n"

		html += "\t\t\t<tr>\n"
		html += "\t\t\t\t<th>Employee Name</td>\n"
		html += "\t\t\t\t<td>Phone Number</td>\n"
		html += "\t\t\t</tr>\n"

		for j in range(N_EMPLOYEES):

			employee = random.choice(employees)
			phNumber = random.choice(phNumbers)

			html += "\t\t\t<tr id=\"entry\">\n"
			html += f"\t\t\t\t<td>{employee}</td>\n"
			html += f"\t\t\t\t<td>{phNumber}</td>\n"
			html += "\t\t\t</tr>\n"

		html += "\t</table>\n"
		html += "</body>\n"
		html += "</html>\n"

		print(f":: Writing target to {OUTPUT_PATH}{md5hash}.html")
		open(f"{OUTPUT_PATH}{md5hash}.html", "w+").write(html)

	print(":: Generating index and styles...")

	loot = ""

	for md5hash in md5hashes.keys():
		loot += f"\t\t<li><a href=\"{md5hash}.html\">{md5hashes[md5hash]}</a></li>\n"

	html = ""

	for line in [l.strip("\n") for l in open("./s_index.html", "r").readlines()]:
		if "FILL ME UP SCOTTY" in line:
			html += loot
		else:
			html += line

	open(f"{OUTPUT_PATH}index.html", "w+").write(html)
	open(f"{OUTPUT_PATH}style.css", "w+").write(open("./s_style.css", "r").read())

	print(":: All targets generated.")

if __name__ == "__main__":
	main()
