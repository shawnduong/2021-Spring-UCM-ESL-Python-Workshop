# Workshop 1: Automate Work Tasks

Let's suppose that you've been tasked with updating the company's contacts list as a spreadsheet. Although you *could* go through webpage after webpage of mindless, boring, zombie-brained data entry for days and days, you would much rather make a computer do it for you.

**Objective:** use logical thinking to create an algorithm that compiles contacts into a spreadsheet. We want the following information:

| Last Name | First Name | Company       | Phone Number    |
|-----------|------------|---------------|-----------------|
| Doe       | John       | Carroll Group | +1-202-555-0143 |
| Doe       | Jane       | Kemmer LLC    | +1-202-555-0727 |
| ...       | ...        | ...           | ...             |

**Disclaimer:** all person names and company names are generated from [fakedetail.com](https://fakedetail.com/) and all phone numbers are generated from [fakenumber.org](https://fakenumber.org/). These are **not** real details.

The website [shawnd.xyz/assets/misc/2021-03-30/](https://shawnd.xyz/assets/misc/2021-03-30/) contains a list of URLs to the contacts pages for individual companies.

## Instructions

1. You will be **split** into groups. This is the instructions document. Read this document as a group.
2. Have one individual in the group start **screensharing**. Have this person open up `logic.txt` with Replit. They may need a Replit account. Replit allows you to program without having to install software on your own system.
3. Start **writing** an algorithm in the `logic.txt` file by using the following steps. These steps are *not* in order. It's your job as a group to figure out the order they go in by thinking logically!
   - Note: the answer checker can be very finnicky. For best results: copy and paste these lines into `logic.txt`.
   - Note: if you get stuck, or if something goes wrong, feel free to use the "Call for Help" feature on Zoom!

```
Make a list of all the individual URLs on the webpage.
A: While the list of URLs is not empty, continue. Else, stop the program.
Go back to step B.
C: Remove the finished URL from the list.
Read https://shawnd.xyz/assets/misc/2021-03-30/.
Remove them from the list of people.
Make a list of all the individual contacts in the URL.
Go to a URL in the list.
Go back to step A.
Go to a person in the list of people.
Add their contact information to the spreadsheet.
B: While the list of people is not empty, continue. Else, go to step C.
```

4. After you're done, **click "Run."** The answer checker will see if your answer is correct, and then it will assemble your program and run it.

5. You can **view** your results in `contacts.csv`.

6. After you're done, **reflect** with your group.

7. If you're feeling courageous, feel free to have a look into `assembled_program.py` if you want to see the code you created. It's important to become comfortable reading code and seeing how *our logic* translates to *source code.*

8. Thanks for attending! You may leave the workshop whenever you'd like. We hope you learned something new and we hope to see you again next week!
