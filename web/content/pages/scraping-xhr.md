Title: Scraping XHR
sortorder: 666

As I've noted in the previous section, it's frequently the case that websites will load in multiple stages using JavaScript. In the first stage, some basic HTML/CSS and JavaScript source gets loaded. Then, JavaScript will make additional network requests that retrieve and insert the bulk of the site's content. This loading of extra content using JavaScript is typically referred to as "AJAX" (Asynchronous JavaScript And XML) or "XHR" (XML HTTP Request).

To scrape sites that use this technique you can use real browsers (like we did in the previous section), or you can attempt to detect the network requests being made, and then duplicate those requests directly from the command line or through a script. It can actually be much easier and faster to scrape this way.

## Inspecting Network Requests

To see what network requests your browser is making, first open up your developer tools. In Chrome, from the `View` menu, select `Developer` and then `Developer Tools`. Or, use the keyboard shortcut `command-option-i`.

Then click the `Network` button. You should see a list of all the requests your browser has made for the page you're on (you may need to refresh first).

![The network inspector]({static}/images/network1.png)

This list contains the initial HTML page, stylesheets, JavaScript files, images, and more. Typically this is a bit overwhelming. You can filter the list to only view specific requests by selecting requests types from the top bar.

![Filterting network requests]({static}/images/network-filters.png)

## Parsing HTML Fragments

As an example, let's look at what happens when you start typing a search query into Bing.com. As is common, every keystroke is sent to Bing which suggests possible queries based on what others have searched for.

![Bing autocomplete]({static}/images/bing_autocomplete.png)

Opening the network inspector and filtering by XHR, you can see the requests being made in real time, listed according to the request URL.

![Network requests]({static}/images/network-requests-list.png)

Click on any request to see more details. For example, you can scroll to the bottom of the `Headers` tab to see the query string for the request.

![Network query string]({static}/images/network-headers.png)

The `Response` tab shows the raw response from the server.

The `Preview` tab provides a more useful view, which changes based on the type of file requested. In this case, it is an HTML snippet:

![HTML Preview]({static}/images/network-preview.png)

You can copy the URL of the request by right-clicking on it to use later in a Python script.

![Copy a network URL]({static}/images/network-copy-url.png)

In this case, we can easily duplicate the request in Python using `requests` and `BeautifulSoup`.

```python
from bs4 import BeautifulSoup
import requests

query = "How can I"
url = (
    "https://www.bing.com/AS/Suggestions?pt=page.home&mkt=en-us&qry="
    + query
    + "&cp=10&cvid=B8D86CB090A240A196E4867715E40B15"
)
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
items = soup.select("li")
for item in items:
    print(item.text)
```

To expand our search and extract more results, we can iterate through the letters of the alphabet, appending each one to our initial search.

```python
from bs4 import BeautifulSoup
import requests

def auto_complete(query):
  url = (
      "https://www.bing.com/AS/Suggestions?pt=page.home&mkt=en-us&qry="
      + query
      + "&cp=10&cvid=B8D86CB090A240A196E4867715E40B15"
  )
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  items = soup.select("li")
  for item in items:
      print(item.text)

base_query = "How can I "
for letter in "abcdefghijklmnopqrstuvwxyz":
  auto_complete(base_query + letter)
```

The results:

<pre style="font-size: 0.85em;height:300px;overflow:scroll">
how can i access chrome
how can i access mls
how can i apply for medi-cal
how can i apply for medicaid
how can i apply for medical
how can i apply for unemployment
how can i apply walmart
how can i avoid probate
how can i balance my hormones
how can i be a superhero
how can i be happy
how can i be sure rascals
how can i become a singer
how can i block email
how can i block youtube
how can i buy stocks online
how can i change password
how can i change the world
how can i chat with amazon
how can i check my unemployment status
how can i check on my stimulus check
how can i check on my stimulus payment
how can i contact amazon
how can i contact amazon customer service
how can i contact facebook
how can i contact instacart
how can i contact the irs
how can i delete multiple emails
how can i detox
how can i download apps
how can i download fortnite
how can i download google play fire tablet
how can i download roblox
how can i download stuff
how can i download youtube videos
how can i eat clean
how can i edit pdfs
how can i efax
how can i elementary
how can i email amazon
how can i email amazon.com
how can i email runescape
how can i email snapchat
how can i explain
how can i explain myself lauryn hill
how can i extend my wifi signal
how can i fall lyrics
how can i file for unemployment
how can i find my 2018 taxes
how can i find my birth mom
how can i find my wifi password
how can i find out about my stimulus check
how can i find out my blood type
how can i forget mkto
how can i gain weight
how can i get free money
how can i get free robux
how can i get hbo max
how can i get my stimulus
how can i get rid of carpenter bees
how can i get tested for coronavirus
how can i get zoom
how can i hack a website
how can i help black lives
how can i help blm
how can i help cuba
how can i help during pandemic
how can i help flint
how can i help the black community
how can i help the protesters
how can i immigrate to canada
how can i improve circulation
how can i induce vomiting
how can i install google play
how can i invest in bitcoin
how can i invest in spacex
how can i invest in stocks
how can i ist
how can i join a militia
how can i join antifa
how can i join hermitcraft server
how can i join people's game in roblox
how can i join protests
how can i join q
how can i jump
how can i just let you walk away
how can i keep cats away
how can i keep fresh basil
how can i keep from singing
how can i keep from singing chords
how can i kill flies
how can i kill me
how can i kill sedum
how can i know my blood type
how can i lose 10 pounds
how can i lose belly fat
how can i lose weight fast
how can i love myself
how can i lower my a1c
how can i lower my blood sugar
how can i lower my cholesterol
how can i lower my potassium
how can i make a difference today
how can i make a song
how can i make a website
how can i make buttermilk
how can i make money
how can i make money online
how can i make my hair grow fast
how can i make pins
how can i n
how can i name pc
how can i netflix
how can i network
how can i not die
how can i not lag
how can i notarize a document
how can i now
how can i paint over silicone caulking
how can i play fortnite for free
how can i play minecraft
how can i please god
how can i polish marble
how can i print from my kindle
how can i print texts
how can i print unemployment application
how can i qualify for
how can i qualify for usaa
how can i qualify for usaa car insurance
how can i qualify grants
how can i qualify loans
how can i quiet
how can i quit
how can i quit beer
how can i reduce inflammation
how can i refuse
how can i register my car
how can i register to vote
how can i rename a link
how can i renew my passport
how can i retrieve deleted emails
how can i reuse
how can i say congratulations
how can i screenshot on kindle fire
how can i see hamilton
how can i short bitcoin
how can i sign a pdf electronically
how can i stop a toothache
how can i stop one drive
how can i stop snoring
how can i take a screenshot
how can i take pictures
how can i tell my blood type
how can i tell the difference
how can i tell you chords
how can i test my webcam
how can i track my stimulus payment
how can i track stimulus check
how can i unclog a toilet
how can i uninstall a program
how can i update my ipad
how can i update my ipad to 12.0
how can i update my kindle
how can i use my ppp loan
how can i use my redbox points
how can i use paypal on amazon
how can i verify my medicare
how can i video call
how can i video myself sleeping
how can i videos
how can i view foreclosed homes
how can i view wingdings
how can i vote online today
how can i vote today
how can i watch belgravia
how can i watch harry potter
how can i watch hbo max
how can i watch teen wolf
how can i watch uncle tom
how can i watch videos
how can i watch yellowstone
how can i work from home
how can i yelp a business
how can i you help me
how can i you use the apps i have installed
how can i you're taking all
how can i youtube
how can i youtube on a hisense smart tv
how can i zip file
how can i zoom
how can i zoom in access
how can i zoom in chrome
how can i zoom in on screen
how can i zoom my icons
how can i zoom out my video on zoom
how can i zoom outlook
</pre>

## Complex Requests & Being Yourself

coming soon!
