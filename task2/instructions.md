See the following tabular data model for a personal library application.

id
title
author
read
date_added
1
The Outlier
Malcolm Gladwell
false
02-11-2015
2
Winning Wisdom
David Oyedepo
false
03-04-2013
3
21 Laws of Leadership
John C. Maxwell
true
12-01-2011
4
Getting Things Done
David Allen
false
11-07-2014
..
...
...
...
...

Replicate the model in Django.
Create a file called book_library.sql to hold the table definition syntax. The primary key is id.
Create a view that renders all the data in a table by navigating to /books/list
I should be able to filter the data by name by supplying a ?name=lorem parameter at the end of the URL.
I should be able to limit search results by supplying a &limit=n parameter at the end of the URL.

See the template design below:

Create a view that handles deletion of each of the objects by clicking on the [trash] icon beside the book name in the list template.
Create logic that handles toggling of the read status of each of the books by clicking on the [tick] icon beside the book name in the list template.
