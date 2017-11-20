 solution

In the previous exercise, I saved birthday information in a slightly different format, so I had to use a slightly different method to extract the months. In my dictionary, the birthdays were saved in the format “MM/DD/YYYY”, or the standard date format we use in the US. My birthdays.json file looked like this:

{
	"Albert Einstein": "03/14/1879",
	"Ada Byron Lovelace": "12/10/1815",
	"Benjamin Franklin": "01/17/1706"
}
To count how many birthdays are in each month, what we need to do is:

Extract the number that represents the month
Convert that number to a string
Print the result
Here is my code to do that:

import json
from collections import Counter

with open("birthdays.json", "r") as f:
	birthdays = json.load(f)

num_to_string = {
	1: "January",
	2: "February",
	3: "March", 
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10: "October",
	11: "November",
	12: "December"
}

months = []
for name, birthday_string in birthdays.items():
	month = int(birthday_string.split("/")[0])
	months.append(num_to_string[month])

print(Counter(months))
And the output you will see is:

Counter({'January': 1, 'March': 1, 'December': 1})
