
How it was Done:


Decode A Web Page Solutions
The How To Decode A Website exercise was a challenging one, involving many complex pieces of code and two new Python modules. When appropaching problems like this one, it helps to develop a plan for the program before executing it.

Our plan should be as follows:

1.Use the requests library to load the HTML of the page into Python
2.Set up BeautifulSoup to process the HTML
3.Find out which HTML tags contain all the titles
4.Use BeautifulSoup to extract all the titles from the HTML
5.Format them nicely



Let us break this down piece by piece and line by line.

Line 1:

  import requests
First, install the requests library according to the official documentation and your operating system, then import the library into the program.

Next,

  from bs4 import BeautifulSoup
Install BeautifulSoup according to the installation documentation. Importing the library is not like the usual way of import foo. Reading the import / useage documentation is the right approach.

Next:

  base_url = 'http://www.nytimes.com'
  r = requests.get(base_url)
These lines make the request to the New York Times homepage. Making a request is simple, according to the documentation you supply a URL and make a GET request.

  soup = BeautifulSoup(r.text)
Reading further through the documentation, we discover that r, contains all the information from the request sent to the New York Times homepage. What we actually want is to look at the HTML of the page and analyze it, so we find that r.text returns all the HTML from the returned request.

After this, BeautifulSoup is the tool we use to recode the HTML. In the same documentation that describes how to import BeautifulSoup, it describes how to import the HTML to analyze it in Python using the line of code in line 6.



Our working assumptions for the moment is that all of the story titles are embedded inside some kind of HTML tag with a class called story-heading. Confirm with another title or two to make sure this assumption is correct, which it is.

Now that we know we are looking for all elements on the page with the class story-heading, so we need to find the documentation for how to do that, with special instructors for how to do this for a class. We end up with:

  soup.find_all(class_="story-heading")
This returns a list of all tags with story-heading as a class. What we need to do is loop through all of them with a for loop and see what format the output is in.

  for story_heading in soup.find_all(class_="story-heading"):
    print(story_heading)
  <h2 class="story-heading">...


