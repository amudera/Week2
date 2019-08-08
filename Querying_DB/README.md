## Querying a SQL Database

In this challenge you are given a SQL database with data inside. You will need to mine it for important information.

Open it up in terminal by typing
```bash
$ sqlite3 sitemetrics.db
```
To see the existing tables and columns, use the .schema command. Map this by hand or on SQL designer so you have a greater understanding of what we're working with.

#### Answer the following questions in this file, with the results and the sql you wrote to get it.
-------------

##### How many people are from California?  
14

##### Who has the most page views? How many do they have, and where are they from?
[(179,
  'Edison Mcintyre',
  'hattie.harriet@far.me',
  'Mauriceville',
  'ME',
  '2014-06-02',
  19937)]

##### Who has the least page views? How many do they have and where are they from?
(477,
  'Hattie Ross',
  'jeffery.travis.jeff@laugh.info',
  'Hubbard',
  'MA',
  '2014-07-19',
  16)]

##### Who are the most recent visitors to the site?(at least 3)

##### Who was the first visitor?
(1, 'Fletcher Haney', 'reed@cupcup.info', 'Scenic Oaks', 'LA', '2014-06-19', 14330)

##### Who has an email address with the domain 'horse.edu'?
(400,
  'Valentine Gonzales',
  'steve.louis.jeremy@horse.edu',
  'Valley View',
  'SD',
  '2014-09-06',
  11065)]

##### How many people are from the city Graford? 
3

##### What are the names of all the cities that start with the letter V, in alphabetical order?
[('Valley View',),
 ('Valley View',),
 ('Van',),
 ('Van',),
 ('Vega',),
 ('Victoria',),
 ('Victoria',)]

##### What are the names and home cities for people searched for the word "drain"?

##### How many times was "trousers" a search term? 
1

##### What were the search terms used by visitors who last visited on August 22 2014?

##### What was the most frequently used search term by people from Idaho?

##### What is the name of user 391, and what are his search terms?

