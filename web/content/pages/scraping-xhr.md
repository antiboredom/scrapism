Title: Scraping XHR
sortorder: 666

As I've noted in the previous section, it's frequently the case that websites will load in multiple stages. In the first stage, some basic HTML/CSS and JavaScript source gets loaded. In the second stage, JavaScript will make additional network requests that retrieve and insert the bulk of the site's content. This loading of extra content using JavaScript is referred to as "AJAX" (Asynchronous JavaScript And XML) or "XHR" (XML HTTP Request).

To scrape sites that use this technique you can use real browsers (like we did in the previous section), or you can attempt to detect the network requests being made, and then duplicate those requests directly from the command line or through a script. It can actually be much easier and faster to scrape this way.

## Inspecting Network Requests

To see what network requests your browser is making, first open up your developer tools. In Chrome, from the `View` menu, select `Developer` and then `Developer Tools`. Or, use the keyboard shortcut `command-option-i`.

Then click the `Network` button. You should see a list of all the requests your browser has made for the page you're on. Note that you may need to refresh the page after opening up the `Network` tab to see the requests.

![The network inspector]({static}/images/network-tab.png)

The list should contain the initial HTML page, stylesheets, JavaScript files, images, and possibly much more. Typically this is a bit overwhelming. You can filter the list to only view specific requests by selecting requests types from the top bar.

![Filterting network requests]({static}/images/network-filters.png)

## Parsing HTML Fragments

As an example, let's look at what happens when you start typing a search query into Bing.com. As is common, every keystroke you type is sent to Bing, which then suggests possible queries based on what others have searched for.

![Bing autocomplete]({static}/images/bing_autocomplete.png)

Opening the network inspector and filtering by XHR, you can see the requests being made in real time, listed according to the request URL.

![Network requests]({static}/images/network-requests-list.png)

Click on any request to see more details. For example, you can scroll to the bottom of the `Headers` tab to see the query string for the request.

![Network query string]({static}/images/network-headers.png)

The `Response` tab shows the raw response from the server.

The `Preview` tab provides a useful view, which changes based on the type of file requested. In this case, it is an HTML snippet:

![HTML Preview]({static}/images/network-preview.png)

You can copy the URL of the request by right-clicking on it to use later in a Python script.

![Copy a network URL]({static}/images/network-copy-url.png)

We can easily duplicate the request in Python using `requests` and `BeautifulSoup`. Note that I have edited the URL to replace the hard-coded query with a variable.

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

To expand our search and extract more results, we can iterate through the letters of the alphabet in a nested loop, appending letter pairs to our initial base query.

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
    for letter2 in "abcdefghijklmnopqrstuvwxyz":
        auto_complete(base_query + letter + letter2)
```

This results in many duplicates. To sort the output of our script and filter out duplicates, you can pipe the script through the `sort -u` command, like so:

```bash
python3 bing_autocomplete.py | sort -u
```

The sorted, unique results:

<pre style="font-size: 0.85em;height:300px;overflow-y:scroll">
how can i a youtube channel
how can i abbreviate hours
how can i abbreviate transfer
how can i abort
how can i abort pregnancy
how can i absorb b12
how can i absorb iron
how can i absorb magnesium
how can i abuse suboxone
how can i accept google pay
how can i access census records
how can i access chrome
how can i access mls
how can i access my 1098 t
how can i access my 2018 w2
how can i access my iphone backup
how can i access quora in china
how can i acquire - the cross in my pocket
how can i acquire a domain name
how can i acquire bitcoin
how can i acquire death certificate
how can i acquire my driving record
how can i activate my tracfone
how can i activate windows 7
how can i add a hyperlink
how can i add a new browser
how can i add a printer
how can i add another language
how can i add korean input
how can i add money to paypal
how can i add the paramount network
how can i add youtube on roku
how can i adjust audio
how can i adjust color
how can i adjust contrast
how can i adjust monitor
how can i adjust p
how can i adjust screen
how can i adjust sound
how can i adjust time
how can i adjust webcam
how can i aerate my lawn
how can i aerate my lawn cheaply
how can i aerate my lawn without a machine
how can i aerate my pond
how can i afford
how can i afford a million dollar home
how can i afford braces
how can i afford homes
how can i afford house
how can i afford ivf
how can i afford rent
how can i afford scad
how can i age copper
how can i age faster
how can i age galvanized metal
how can i age metal
how can i age new wood to look weathered
how can i age slowly
how can i age steaks at home
how can i airdrop photos
how can i airdrop to my mac
how can i airdrop to my pc
how can i airdrop to windows
how can i airplay
how can i airplay on mac
how can i airplay to my tv
how can i airprint
how can i akc register my dog
how can i alert you
how can i alexa
how can i all
how can i allow flash
how can i allow java
how can i allow pop ups in edge
how can i allow pop-ups
how can i alphabetize
how can i alphabetize in word
how can i am
how can i amend 2017 taxes
how can i amend my fafsa
how can i amend my return
how can i amend my taxes
how can i amend my taxes online
how can i amend my trust
how can i amend my will
how can i analyse article
how can i android kindle fire 7
how can i animate myself
how can i annotate
how can i annotate a video
how can i annoy neighbors
how can i annoy you
how can i annul marriage
how can i antique brass
how can i appeal my financial aid
how can i apply for food stamps online
how can i apply for medi-cal
how can i apply for medicaid
how can i apply for medical
how can i apply for section 8
how can i apply for unemployment
how can i apply to target
how can i apply walmart
how can i arch text in word
how can i archive a website
how can i archive emails
how can i archive gmail
how can i archive my books
how can i archive my documents
how can i archive outlook emails
how can i articulate better
how can i ascend
how can i ask for consent
how can i ask for money
how can i ask for money from rich people
how can i ask for you
how can i ask god to help me
how can i ask joe biden a question
how can i ask my mom
how can i ask questions
how can i ask to help
how can i assist
how can i assist you synonyms
how can i assure
how can i atop
how can i attend
how can i attract ants
how can i attract bees to my garden
how can i attract birds
how can i attract cardinals
how can i attract cardinals to my yard
how can i attract cats
how can i attract hummingbirds
how can i attract hummingbirds to my feeder
how can i attract men
how can i audio
how can i audio record
how can i audition for disney channel
how can i audition for netflix
how can i auto fill forms
how can i automate excel
how can i automate tasks
how can i automatically call you
how can i automatically log on
how can i automatically log on to windows 10
how can i avoid 5g
how can i avoid ads
how can i avoid bpa
how can i avoid bumping an older thread
how can i avoid constipation
how can i avoid hiv
how can i avoid probate
how can i avoid scams and hoaxes
how can i avoid uti
how can i awake cortana
how can i back up
how can i backup data
how can i backup files
how can i backup laptop
how can i backup my
how can i backup my iphone to my computer
how can i balance my hormones
how can i ban a book
how can i ban bing
how can i bcc in outlook
how can i bcc myself on all emails
how can i be a superhero
how can i be a youtuber
how can i be faithful to god
how can i be famous
how can i be happier
how can i be happy
how can i be pretty
how can i be rich
how can i be safe
how can i be sure
how can i be sure rascals
how can i become a contact tracer
how can i become a priest
how can i become a singer
how can i become a witch
how can i become a wolf
how can i become an actor
how can i become famous
how can i become royalty
how can i become stronger
how can i bet on esports
how can i bet on football
how can i bet on sports
how can i bet online
how can i better my career
how can i better my life
how can i better myself
how can i bid on construction jobs
how can i bid on ebay
how can i bid on public jobs
how can i bid on storage units
how can i bill collect on ups
how can i bill medicare secondary
how can i binge watch yellowstone
how can i bite off my pinkie
how can i block a website
how can i block apps
how can i block email
how can i block emails from someone
how can i block google ads
how can i block robocalls
how can i block someone
how can i block youtube
how can i board
how can i boat
how can i book
how can i boost
how can i boost my internet speed
how can i boost my vitamin d
how can i boost my wifi range
how can i boost my wifi signal
how can i br
how can i breathe
how can i bring back a deleted excel file
how can i bring my blood pressure up fast
how can i bring my dog to school
how can i broadcast
how can i broadcast my computer to my tv
how can i browse the internet on my tv
how can i build my credit
how can i bulk up
how can i buy a home
how can i buy a horse
how can i buy cbd
how can i buy gold
how can i buy property
how can i buy robux
how can i buy stocks online
how can i by
how can i bypass apple activation lock
how can i bypass bitlocker
how can i bypass facebook
how can i bypass firewall
how can i bypass google
how can i bypass google verification
how can i bypass login
how can i bypass the facebook code generator
how can i calculate age
how can i call amazon prime
how can i call aol
how can i call cash app
how can i call for free
how can i call jojo
how can i call venmo
how can i calm down my anxiety
how can i cash my stimulus check
how can i cast to my roku tv
how can i cc someone in gmail
how can i celebrate beltane
how can i celebrate lent
how can i celebrate passover
how can i center an image
how can i center my title
how can i center screen
how can i center the page
how can i certify a letter
how can i cg
how can i change dns
how can i change my address
how can i change my id
how can i change password
how can i change the world
how can i chat with amazon
how can i check email
how can i check my address
how can i check my credit score
how can i check my unemployment status
how can i check on my stimulus check
how can i check on my stimulus payment
how can i circle something in adobe
how can i circulate blood in my feet
how can i circumcise myself
how can i cite a movie
how can i cite a pdf
how can i cite a source
how can i cite a video
how can i cite a youtube video mla
how can i cite book
how can i cite in apa
how can i ck my internet speed
how can i ck my samsung tv if it is an hgtv
how can i ck on my stimulus check
how can i claim eic
how can i claim unemployment
how can i clean guitar strings
how can i clean jewelry
how can i clean my ears
how can i clean my glasses
how can i clean my scalp
how can i clean pillows
how can i clear cache
how can i clear my cloud
how can i combine to photos into one
how can i comment on youtube
how can i comment on youtube livestream
how can i communicate with a deceased person
how can i compare
how can i compare drug prices at pharmacies
how can i completely remove avast
how can i completely reset my laptop
how can i cone
how can i contact amazon
how can i contact amazon customer service
how can i contact donald trump
how can i contact facebook
how can i contact facebook admin
how can i contact instacart
how can i contact postmates
how can i contact shein
how can i contact the irs
how can i contact ups
how can i contact upwork
how can i contact usps
how can i contact wish
how can i control
how can i craft
how can i craft this again minecraft
how can i create a bitmoji
how can i create a countdown
how can i create a new folder
how can i create a new password
how can i create a pie chart
how can i create a website
how can i create a zoom meeting
how can i create amazon account
how can i create an online store
how can i create another email
how can i create my own blog
how can i create my own resume
how can i crop pictures
how can i cry
how can i cry choir
how can i cry lyrics
how can i cry moira smiley
how can i cry sheet music
how can i ctrl f on a pdf
how can i cure fatigue
how can i cure ibs
how can i cure my autism
how can i curve my text in word
how can i customize bing wallpaper
how can i cut a video clip
how can i cut and paste a pdf
how can i cut my own hair
how can i dance
how can i darken
how can i darken grout
how can i darken oak
how can i darken paint
how can i darken pdf
how can i date you
how can i day trade
how can i dcelete msn news
how can i ddos someone
how can i ddos someone on xbox
how can i debug computer
how can i default google
how can i delay menopause
how can i delete a book
how can i delete a website
how can i delete apps
how can i delete chromium
how can i delete gmail address
how can i delete multiple emails
how can i delete my email
how can i delete my games
how can i delete screenshots
how can i denounce
how can i deny a zelle payment
how can i deposit check online
how can i design my living room
how can i design my own popsocket
how can i destroy a hard drive
how can i detox
how can i dictate
how can i dictate a book
how can i dictate documents
how can i dictate email
how can i dictate text
how can i dictate typing
how can i dictate word
how can i disable my touchpad
how can i discontinue facebook
how can i disinfect my dog
how can i disinfect my n95 mask
how can i dispose of old gas
how can i dispose of old paint
how can i dispose of tv
how can i dm in instagram
how can i dm on instagram on a computer
how can i dm on instagram online
how can i dm on instagram pc
how can i dm on my computer
how can i dm on twitter
how can i dm people on chrome
how can i dm someone on instagram on laptop
how can i donate a piano
how can i donate blood
how can i download a youtube video
how can i download apps
how can i download fortine
how can i download fortnite
how can i download google apps
how can i download google classroom
how can i download google play fire tablet
how can i download revit
how can i download roblox
how can i download stuff
how can i download youtube videos
how can i dox someone
how can i drain my ear
how can i draw a girl
how can i draw a star
how can i draw in word
how can i drink
how can i drop 30 pounds fast
how can i drop a class
how can i dry my iphone out
how can i dry my nails quickly
how can i dual screen
how can i dunk
how can i duplicate a cd
how can i duplicate a file
how can i duplicate a slide
how can i duplicate my money
how can i duplicate my screen
how can i dust under my bed
how can i dvr streaming media
how can i dvr without cable
how can i dye eggs
how can i dye linen
how can i dye my
how can i dye my carpet
how can i dye my hair
how can i dye my hair without bleaching it
how can i dye my hair without hair dye
how can i dye polyester
how can i earn 5%
how can i earn amazon coins
how can i earn money
how can i earn money fast as a kid
how can i earn more bing rewards
how can i ease the pain lisa fischer
how can i eat
how can i eat clean
how can i edit a mov file
how can i edit a pdf doc
how can i edit a video on my iphone
how can i edit audio file on my computer
how can i edit jpg
how can i edit my linkedin url
how can i edit my zoom recording
how can i edit pdfs
how can i edit user
how can i efax
how can i efax for free
how can i efax from windows 10
how can i effect change
how can i effectively communicate
how can i efile 1099 misc
how can i efile 2018
how can i efile for free
how can i egg
how can i eject cd
how can i eject disc
how can i eject disk d
how can i eject dvd
how can i eject my cd tray
how can i eject my usb
how can i eject usb safely
how can i ejeculate more
how can i electronically sign
how can i electronically sign a pdf document
how can i elementary
how can i eliminate
how can i eliminate bing
how can i eliminate debt
how can i eliminate mortgage insurance
how can i elope
how can i email amazon
how can i email amazon.com
how can i email fox news
how can i email nancy pelosi
how can i email runescape
how can i email snapchat
how can i email the nfl
how can i emancipate myself
how can i embed gif in email
how can i embed into google docs
how can i embed into powerpoint
how can i embed videos into powerpoint
how can i embrace change
how can i embrace diversity
how can i embrace vulnerability
how can i embroidery
how can i enable it
how can i enable javascript
how can i enable javascript in microsoft edge
how can i enable sli
how can i enable vt
how can i encrypt
how can i enlarge
how can i enlarge emails
how can i enlarge font
how can i enlarge page
how can i enlarge text
how can i enlarge type
how can i enlarge words
how can i enroll
how can i enter bios
how can i enter google
how can i enter password
how can i enter safe mode
how can i entertain myself
how can i entertain teenagers
how can i equalize sinus pressure
how can i equalize sounds on my dell laptop
how can i equalize volume on playlist
how can i erase all emails at once
how can i erase bing
how can i erase files
how can i erase games
how can i erase junk
how can i erase my
how can i erase pen
how can i erase photos
how can i escape
how can i escape google
how can i escape hell
how can i escape poverty
how can i escape school
how can i estimate my closing costs
how can i estimate my iq
how can i estimate my taxes
how can i etch marble
how can i euthanize my cat
how can i euthanize my cat at home
how can i euthanize my dog
how can i euthanize my dog at home
how can i euthanize my pet at home
how can i evaluate
how can i evangelize
how can i ever
how can i ever forgive
how can i ever repay
how can i ever retire
how can i ever survive
how can i evolve eevee
how can i excel
how can i exchange
how can i exchange currency
how can i exchange foreign coins
how can i exchange iraqi dinar
how can i exercise at home
how can i exercise more
how can i exercise my back
how can i exercise my body
how can i exercise my brain
how can i exercise my dog
how can i exercise my rights
how can i exercise with copd
how can i exfoliate my face
how can i exfoliate my face without a scrub
how can i exfoliate my feet
how can i exfoliate my legs
how can i exfoliate my lips
how can i exfoliate my scalp
how can i exfoliate my skin
how can i exfoliate my skin naturally
how can i exit
how can i exit edge
how can i exit microsoft
how can i exit safe mode
how can i exit skype
how can i exit this page
how can i exit this site
how can i expand
how can i expedite a passport
how can i explain
how can i explain myself lauryn hill
how can i explain shot
how can i explore
how can i export my
how can i express my feelings
how can i express myself
how can i extend cobra
how can i extend my desk
how can i extend my house
how can i extend my i-94
how can i extend my life
how can i extend my visa
how can i extend my wifi signal
how can i extract you
how can i f help my anxiety
how can i face time here
how can i facebook
how can i facetime
how can i facetime jojo
how can i facetime on my kindle fire
how can i fact check
how can i fact check an article
how can i factor
how can i fade a picture
how can i fade a tattoo
how can i fade age spots
how can i fade away
how can i fade bruises
how can i fall
how can i fall asleep
how can i fall lyrics
how can i famous
how can i fax from home
how can i fax from pc
how can i fax online
how can i fax without machine
how can i fear
how can i fear hymn
how can i fear song
how can i feel full
how can i feel full without eating
how can i feel god
how can i feel good
how can i feel love
how can i feel numb
how can i feel safe
how can i feminize myself
how can i file 2018 taxes
how can i file for unemployment
how can i find my 2018 taxes
how can i find my birth mom
how can i find my ghin number
how can i find my password
how can i find my phone
how can i find my phone google
how can i find my wifi password
how can i find out about my stimulus check
how can i find out my blood type
how can i find someone
how can i firm up poop
how can i fix corrupted files
how can i fix my anxiety
how can i fix my ed
how can i fix my lawn
how can i fix my unemployment claim
how can i fix myself
how can i flip $20
how can i flip $5000
how can i flip 1000 dollars
how can i flip 10k
how can i flip 20k
how can i flip an image horizontally
how can i flip screen
how can i flip text
how can i flirt my crush
how can i float
how can i fly
how can i follow someone on facebook
how can i forget
how can i forget mkto
how can i forget someone i love
how can i forget you girl lyrics
how can i forgive
how can i forgive myself for my past
how can i forgive ya
how can i format
how can i forward
how can i forward email
how can i forward gmail automatically
how can i free some disk space
how can i free up space on my laptop
how can i free up storage space on my kindle
how can i freeze angel food cake
how can i freeze fresh cilantro
how can i freeze my credit
how can i freeze potatoes
how can i freeze white raw mushrooms
how can i ft on my computer
how can i ft on my laptop
how can i ftp into my pc
how can i full screen
how can i fund an hsa
how can i fund an ira
how can i fund my llc
how can i fund robinhood
how can i fundraise for myself
how can i furnish an apartment
how can i further my education
how can i gain 4 lbs overnight
how can i gain muscle
how can i gain muscle mass quickly
how can i gain wait
how can i gain wealth
how can i gain weight
how can i gain weight easily
how can i gain weight fast
how can i gain weight fast for men
how can i gamble online
how can i game
how can i game on my laptop
how can i game share on ps4
how can i game share on xbox
how can i gameshare on 2 ps4 systems
how can i gameshare xbox
how can i get a grant
how can i get a stimulus check
how can i get an antibody test
how can i get fha loan
how can i get free money
how can i get free robux
how can i get free v bucks
how can i get google chrome
how can i get google play on amazon fire
how can i get hbo max
how can i get messenger
how can i get my stimulus
how can i get peacock tv
how can i get powers
how can i get rid of carpenter bees
how can i get roblox
how can i get ssi benefits
how can i get tested for coronavirus
how can i get zoom
how can i gift a kindle book to someone else
how can i gift kindle unlimited
how can i gift stocks to kids
how can i girls
how can i give away my cat
how can i give back
how can i give blood
how can i give my
how can i give my friends fortnite skins
how can i give my timeshare away or donate it
how can i give plasma
how can i give roblox
how can i glo up
how can i glo up yahoo
how can i glorify god
how can i glorify god today
how can i glow
how can i glow my skin
how can i glue metal together
how can i glue plexiglass
how can i go into bios
how can i go on
how can i go on lyrics
how can i go online
how can i go to china
how can i go to cuba
how can i go to sleep
how can i go to sleep early
how can i gps a cell phone
how can i gps a phone
how can i gps my car
how can i gps my kids phone
how can i gps someone
how can i gps someone's phone
how can i gps track my phone
how can i grow 6 inches
how can i grow a pineapple
how can i grow as a christian
how can i grow taller
how can i grow taller at 13
how can i grow tea
how can i grow vegetables in the house
how can i grow wings
how can i guarantee a baby girl
how can i guard my heart
how can i guard my wealth
how can i guard my wealth from a greedy
how can i guess a ring size
how can i guess tax refund
how can i guess the masked singer
how can i guitar make sound
how can i gw
how can i hack a instagram account
how can i hack a website
how can i hack someone phone
how can i hand wash clothes
how can i handle my grief
how can i handle my temper
how can i handle stress
how can i hang a shelf
how can i hang a tapestry
how can i hang curtains without rods
how can i hang on brick
how can i hard reset apps
how can i harden my nails
how can i harden my poop
how can i harden my stool
how can i harden paper
how can i harden play dough
how can i harden sand
how can i harden steel
how can i have a lucid dream tonight
how can i have fun
how can i have google as my search engine
how can i have internet without a phone line
how can i have joy
how can i have psa grade my cards
how can i have self-discipline
how can i have the less amount of taxes taken
how can i hedge my portfolio
how can i help a vet
how can i help bees
how can i help black lives
how can i help blm
how can i help covid-19
how can i help cuba
how can i help during pandemic
how can i help flint
how can i help homeless
how can i help humanity
how can i help people
how can i help quote
how can i help the black community
how can i help the community
how can i help the earth
how can i help the protesters
how can i help with coronavirus
how can i help you in spanish
how can i help you say goodbye
how can i hem pants without sewing
how can i hibernate
how can i hide an order on amazon
how can i hide apps
how can i hide cords
how can i hide my air conditioner
how can i hide my birthday on facebook
how can i hide my ip
how can i hide my outdoor trash can
how can i hide my profile picture on facebook
how can i hide photos
how can i hide toolbar
how can i hide you
how can i highlight
how can i highlight every other row in excel
how can i highlight in excel
how can i highlight in word
how can i highlight pdf
how can i highlight text
how can i highlight text in microsoft edge
how can i hire the property brothers
how can i hiv
how can i hold a sloth
how can i hold mail
how can i hold myself accountable
how can i hold you
how can i home page
how can i homeschool and work full time
how can i homeschool my child
how can i homeschool my child for free
how can i homeschool my child in texas
how can i homeschool my kid
how can i homestead my home in texas
how can i honey
how can i honor god
how can i hook up my
how can i hook up my kindle to my tv
how can i hook up my laptop to tv
how can i hook up my tablet to my tv
how can i host a zoom meeting
how can i how are you today
how can i how can i live
how can i how can i lyrics
how can i how can i set up
how can i how can my
how can i how can you make
how can i hug you
how can i humidify my home
how can i hurt china
how can i hurt god
how can i hurt my testicles
how can i hurt you
how can i hurt your feelings
how can i hurt youtube
how can i hydrate better
how can i hydrate my dog
how can i hydrate my face
how can i hydrate my hair
how can i hydrate raisins
how can i hyper a links
how can i hypnotize myself
how can i hypnotize people
how can i i write a letter on my laptop
how can i identify
how can i identify a flower
how can i identify a pill by the way it looks
how can i identify birds
how can i identify fonts
how can i identify ivory
how can i identify my plant
how can i identify pills
how can i identify plants
how can i identify trees
how can i ignore a windows update
how can i ignore my mom
how can i ignore my neighbor totally
how can i ignore people
how can i ignore you
how can i ignore you baby i adore you
how can i ignore you tik tok song
how can i ignore you trust me i adore you
how can i illegally
how can i illuminate my keyboard
how can i illuminati
how can i illustrate my book
how can i illustrate my own children's book
how can i illustrate what the word iffy means
how can i immigrate to canada
how can i improve circulation
how can i improve my art
how can i improve my diet
how can i improve my eyesight
how can i improve my immune system
how can i improve my kidney
how can i improve my reflexes
how can i improve my vocal
how can i incorporate myself
how can i increase credit score
how can i increase my bandwidth
how can i increase my ferritin level
how can i increase my hdl level
how can i increase my hemoglobin level
how can i increase my internet speed
how can i increase my pulse rate
how can i increase my sperm
how can i increase sperm volume
how can i induce vomiting
how can i injure my shoulder on purpose
how can i inquire about stimulus check
how can i inspect element
how can i install fortnite
how can i install google play
how can i install office
how can i install play store
how can i introduce myself
how can i invest $100
how can i invest in bitcoin
how can i invest in spacex
how can i invest in stocks
how can i ionize water
how can i iphone
how can i iron faux fur when sewing
how can i island hop in hawaii
how can i isolate cells in excel
how can i issue a 1099
how can i issue a partial refund on ebay
how can i issue corporate shares
how can i ist
how can i italicize a post in facebook
how can i italicize text in a post
how can i itemize on my taxes
how can i jailbreak a firestick
how can i jailbreak amazon firestick
how can i jailbreak ios 12.1.4
how can i jailbreak iphone x
how can i jailbreak my ipad
how can i jailbreak my roku
how can i jam a cell phone signal
how can i jam wifi cameras
how can i jam wireless cameras
how can i jazz up a yellow cake mix
how can i jazz up banana bread
how can i jazz up brown rice
how can i jazz up canned green beans
how can i jazz up cauliflower rice
how can i jessica reedy lyrics
how can i join a militia
how can i join aaa
how can i join antifa
how can i join hermitcraft
how can i join hermitcraft server
how can i join people's game in roblox
how can i join protests
how can i join q
how can i join whatsapp
how can i jpeg a picture
how can i judge if i am depressed
how can i juice grapes
how can i jump
how can i jump higher
how can i junk a car
how can i just be happy
how can i just be normal
how can i just die
how can i just disappear
how can i just fall asleep
how can i just let you walk away
how can i just purchase word
how can i just sure
how can i kcopy the nusic on a cd
how can i keep bananas fresh
how can i keep cats away
how can i keep cilantro fresh
how can i keep fresh basil
how can i keep from getting the coronavirus
how can i keep from singing
how can i keep from singing chords
how can i keep from singing lyrics
how can i keep from singing youtube
how can i keep my lymphatic system healthy
how can i keep myself awake
how can i keep potatoes fresh
how can i kick
how can i kidnap my friend
how can i kill a groundhog
how can i kill a tree stump
how can i kill bamboo growing in my yard
how can i kill english ivy
how can i kill flies
how can i kill me
how can i kill moss on my roof
how can i kill moss with acetic acid
how can i kill mushrooms in my lawn
how can i kill poison ivy
how can i kill sedum
how can i kill termites in my home
how can i kill water bugs
how can i kms
how can i know if i'm pregnant
how can i know my blood type
how can i know my bmi
how can i know my property line
how can i know robert jeffress
how can i know what graphic card i have
how can i know what windows i have
how can i know when
how can i know who unfriended me on facebook
how can i kyc on paytm
how can i label photos
how can i lactate
how can i lactate more for breastfeeding
how can i lactate without being pregnant
how can i laminate my own paper
how can i laminate paper
how can i laminate something
how can i lance a
how can i land my back handspring
how can i last
how can i laugh
how can i laugh tomorrow
how can i launch
how can i launch itunes
how can i lead my peers
how can i learn about stocks
how can i learn asl
how can i learn english
how can i learn hypnosis
how can i learn klingon
how can i learn korean
how can i learn spanish
how can i learn spanish fast
how can i learn swahili
how can i learn telekinesis
how can i learn to code
how can i learn to whistle
how can i learn yardi
how can i left
how can i lessen cold symptoms
how can i lessen fibroid pain
how can i lessen my carbon footprint
how can i lessen my period
how can i let go
how can i let go of anger
how can i let go of fear
how can i let my light shine
how can i let my light shine for jesus
how can i let my partner help ptsd
how can i let things go
how can i level my floor
how can i level my grass
how can i level my lawn
how can i level my yard
how can i level up quickest
how can i leverage my money
how can i levitate
how can i license my dog
how can i lift deapite tendonidis
how can i lift heavier
how can i lift my cheeks
how can i lift my forehead
how can i lift my spirits
how can i lift sagging jowls
how can i lighten my hair at home
how can i like myself
how can i line
how can i link devices
how can i link my device
how can i link my facebook
how can i link my facebook to instagram
how can i link resume
how can i liquidate my 401k
how can i liquify honey crystals
how can i liquify stevia powder for baking
how can i listen to ham radio
how can i listen to scotus tomorrow
how can i listen to supreme court
how can i litter train my ferret
how can i live stream a wedding
how can i live stream cnn
how can i live without you
how can i log in to my hotmail account
how can i log into my cash app
how can i log into my gmail personal account
how can i log into my icloud
how can i log into youtube without google
how can i log off facebook
how can i log out of facebook messenger
how can i login back with instagram
how can i login to my router
how can i lose 10 pounds
how can i lose belly fat
how can i lose weight
how can i lose weight fast
how can i lose weight fast naturally
how can i love myself
how can i lower my a1c
how can i lower my blood pressure
how can i lower my blood sugar
how can i lower my cholesterol
how can i lower my mortgage
how can i lower my ping
how can i lower my potassium
how can i lower my triglycerides level
how can i lubricate my knee joints
how can i lucid dream
how can i lucid dream easily
how can i lunch
how can i lyrics
how can i lyrics john lennon
how can i lyrics laura marling
how can i lyrics marion
how can i magnetize a magnet
how can i magnetize a screwdriver
how can i magnetize something
how can i magnify
how can i magnify a page
how can i magnify a screen page
how can i magnify my computer screen
how can i magnify print
how can i make a difference today
how can i make a email
how can i make a new gmail account
how can i make a song
how can i make a website
how can i make buttermilk
how can i make distilled water
how can i make google my default browser
how can i make hummus
how can i make money
how can i make money fast
how can i make money online
how can i make my hair grow fast
how can i make myself fall asleep
how can i make myself happy
how can i make pins
how can i mark all gmail emails as read
how can i match font
how can i match foundation online
how can i match my floor tile
how can i match paint
how can i match paint color
how can i match values in excel
how can i match wall paint
how can i match woods
how can i maximize 401k
how can i maximize a window
how can i maximize my page
how can i maximize my refund
how can i maximize my savings
how can i maximize my tsp
how can i maximize screen
how can i maximize you
how can i meet addison rae
how can i meet dua lipa
how can i meet emma watson
how can i meet jojo siwa
how can i meet new people
how can i melt
how can i melt belly fat
how can i melt brass
how can i melt glass
how can i melt gold
how can i melt plastic
how can i melt rock
how can i melt silver
how can i mend a broken nail
how can i mentally feel better
how can i mentor someone
how can i merge cells
how can i merge excel workbooks
how can i merge files
how can i merge multiple pdfs
how can i merge pdf
how can i merge songs
how can i merge two pdf files together
how can i message
how can i message facebook
how can i message government
how can i message microsoft
how can i message people
how can i message trump
how can i message twitter
how can i message youtube
how can i mine
how can i minimize
how can i minimize app
how can i minimize screen
how can i minimize screen size
how can i mirror
how can i mirror my iphone to my tv
how can i mirror my laptop to my tv
how can i mm
how can i mod minecraft
how can i mod steam games
how can i mod xbox 360
how can i model for nike
how can i modify a jpeg
how can i modify a pdf document
how can i modify my car
how can i modify my will
how can i modify pdf
how can i move books off my kindle
how can i move my laptop screen
how can i move on
how can i move on with life
how can i move to canada legally
how can i move to israel
how can i move to japan
how can i move to switzerland
how can i move to the usa
how can i multiply ranges
how can i multitask
how can i music
how can i mute audio
how can i mute cortana
how can i mute iphone
how can i mute you
how can i mute zoom
how can i my computer screen with color again
how can i my logo for my label
how can i my outlook email
how can i my stimulus check
how can i my twitter account suspended
how can i mz
how can i n
how can i nail salon
how can i name a folder
how can i name a photo
how can i name a star
how can i name my ipad
how can i name pc
how can i name photos
how can i name you
how can i nap during the day
how can i narrate a powerpoint
how can i naturally color my hair
how can i need your help
how can i negotiate a debt
how can i negotiate a medical bill
how can i negotiate salary
how can i negotiate with the irs
how can i netflix
how can i network
how can i network two laptops
how can i neutralize acid
how can i never talk again
how can i nickname my wells fargo account
how can i nine year-old get money
how can i not die
how can i not eat
how can i not hear
how can i not lag
how can i not love you song
how can i not sin
how can i not sing
how can i notarize a document
how can i now
how can i numb a toothache
how can i numb my dogs paw
how can i numb my skin
how can i numb my toe
how can i number a pdf
how can i number my pages
how can i number my rows
how can i nut more
how can i obtain a medical marijuana card
how can i obtain a ss card for my child
how can i obtain an ein number on a business
how can i obtain dmt
how can i obtain lsd
how can i obtain my ged
how can i obtain my high school transcript
how can i obtain my military medical records
how can i obtain wifi
how can i ocr a .pdf
how can i off function
how can i off my computer
how can i off my location
how can i off myself
how can i off windows update
how can i offer ceu
how can i offer help
how can i offset my taxes
how can i on cortana
how can i on my bluetooth
how can i on my camera
how can i on my microphone
how can i on my mood
how can i on wifi
how can i online my printer
how can i only use one airpod
how can i open a .rpt file
how can i open a daycare
how can i open a powerpoint
how can i open a savings account
how can i open a zip file
how can i open an .xps document
how can i open an iphone
how can i open facebook
how can i open google
how can i open icloud account
how can i opt out of facebook
how can i order checks for my account
how can i order checks online
how can i order disinfectant spray
how can i order from walmart
how can i order john oliver stamps
how can i order postage stamps online
how can i order starbucks online
how can i organize email
how can i organize files
how can i organize gmail
how can i organize my chest freezer
how can i organize my google docs
how can i organize my room
how can i organize myself
how can i out pizza the hut
how can i outline a photo
how can i outline text in publisher
how can i outline words in word
how can i outlook
how can i outlook email
how can i outsmart my mom
how can i outsource my call center
how can i overcome
how can i overcome guilt
how can i overcome laziness
how can i overcome ocd
how can i overcome sin
how can i overdose
how can i overnight a package
how can i overnight mail
how can i owe money
how can i owe taxes
how can i own a bear
how can i own a cafe
how can i own a fox
how can i own a gun
how can i own a monkey
how can i own apartments
how can i oxidize copper
how can i oxidize sterling silver
how can i oxygenate my blood
how can i pack cookies to ship
how can i package my product
how can i page number in excel
how can i paint over silicone caulking
how can i pan fry a steak
how can i pass a drug test
how can i pass a urine test for meth
how can i patent a game
how can i pay at the dmv
how can i pay for my college
how can i pay my car tax online
how can i pay my excise tax
how can i pay my rent online
how can i pay my state tax
how can i pay my taxes
how can i pay off my cc debt
how can i pcs to another unit
how can i pdf a doc
how can i pdf a document
how can i pdf a jpeg file
how can i pdf an email
how can i pdf an excel workbook
how can i pdf documents
how can i perform better
how can i perform weddings
how can i permanently delete
how can i permanently stop having periods
how can i permission
how can i permit you
how can i personalize
how can i pet a wombat
how can i phone amazon
how can i phone pay pal
how can i phone ups
how can i photograph better
how can i photoshop
how can i photoshop a photo
how can i photoshop pictures
how can i phrase
how can i physically help in the bahamas
how can i pick a lock
how can i pick up
how can i pick up girls
how can i pick up weight
how can i pictures
how can i pin
how can i pin a note
how can i pin a site
how can i pin a tab
how can i pin favorites
how can i pin my gmail to my taskbar
how can i pin pinterest
how can i pin tiles
how can i pirate
how can i pixelate a photo
how can i pixelate a photo on a mac
how can i pixelate a picture
how can i place an order
how can i play d&d online
how can i play fortnite for free
how can i play games online
how can i play just dance
how can i play minecraft
how can i play roblox
how can i play roblox online
how can i play ttt
how can i please god
how can i podcast
how can i polish brass
how can i polish marble
how can i polish metal
how can i poop
how can i post photos to instagram from my pc
how can i post to instagram from laptop
how can i powder coat rims
how can i power
how can i power my raspberry pi
how can i power off ipad
how can i power off my computer
how can i powerpoint presentation mode
how can i preserve potatoes
how can i prevent bullying
how can i prevent copyright
how can i print an email
how can i print checks
how can i print from my kindle
how can i print stamps online
how can i print texts
how can i print unemployment application
how can i print using wifi
how can i promote change
how can i publish 1 book
how can i publish a book
how can i publish a poem
how can i publish a song
how can i publish articles
how can i publish my game
how can i publish online
how can i publish paper
how can i pull my w2
how can i purchase netflix
how can i purchase stock online
how can i put ads on youtube
how can i put cds on my laptop
how can i put facebook on desktop
how can i put money on cash app
how can i put music on my iphone
how can i put netflix on my tv
how can i put the date in taskbar
how can i qualify for
how can i qualify for eic
how can i qualify for hud
how can i qualify for pua
how can i qualify for unemployment
how can i qualify for unemployment benefits
how can i qualify for usaa
how can i qualify for usaa car insurance
how can i qualify grants
how can i qualify loans
how can i quench my thirst
how can i quickly die
how can i quiet
how can i quit
how can i quit beer
how can i quit cable
how can i quit soda
how can i quit sugar
how can i quit work
how can i quote in essay
how can i radio
how can i raise money
how can i raise my blood pressure
how can i raise my credit score
how can i raise my platelets count
how can i raise my wbc count
how can i rap
how can i rate instacart
how can i rdp to my home computer
how can i read faster
how can i reboot a mac
how can i reboot computer
how can i reboot iphone
how can i reboot laptop
how can i reboot my ipad
how can i reboot my pc
how can i reboot my roku
how can i reboot my router
how can i receive money paypal
how can i receive tv channels
how can i record a video
how can i record my screen
how can i record shows on firestick
how can i record video on pc
how can i recover deleted emails
how can i recover my fb account
how can i reduce cholesterol quickly
how can i reduce gas problem
how can i reduce heartburn
how can i reduce inflammation
how can i reduce my tax bill
how can i reduce ping
how can i reduce plastic
how can i refill
how can i refinance
how can i refinance my car
how can i refinance my home
how can i refinish my hardwood floors
how can i refresh
how can i refund nintendo eshop
how can i refuse
how can i register a business name
how can i register my car
how can i register my car online
how can i register to vote
how can i reheat pizza
how can i reheat quiche
how can i reheat rice
how can i rehydrate
how can i reject a venmo payment
how can i reject unwanted email
how can i rejoin paparazzi
how can i rejuvenate a battery
how can i rejuvenate my lilac bushes
how can i rejuvenate my liver
how can i rekey a lock
how can i rekindle my marriage
how can i release gas
how can i relieve cramps
how can i relieve gas
how can i relieve gerd
how can i relieve hives
how can i relieve itching
how can i relieve nausea
how can i relieve stress
how can i remember my dreams
how can i remove acrylic nails
how can i remove facebook account
how can i remove gel nail polish
how can i remove gel nails
how can i remove password login
how can i remove roblox
how can i remove saved passwords
how can i remove window tint film
how can i rename a link
how can i renew my driver license
how can i renew my driver's license
how can i renew my food stamps online
how can i renew my license
how can i renew my license in ohio
how can i renew my nyc drivers license
how can i renew my passport
how can i rent with bad credit
how can i repair ceiling tiles
how can i replace a missing w2
how can i replace cable tv
how can i replace my social security card
how can i replay alexa notifications
how can i report fraud
how can i report my wages ssi
how can i report scammers
how can i request
how can i request a foia
how can i request an absentee ballot
how can i request an mvr
how can i request fmla
how can i request my criminal record
how can i request my w-2
how can i request w2
how can i reset my computer
how can i reset my kindle
how can i reset my password
how can i reset my roku
how can i restore my kindle fire
how can i retrieve deleted emails
how can i retrieve my apple id
how can i retrieve my archived emails
how can i retrieve my email password
how can i retrieve my emails
how can i retrieve my voicemails
how can i return a kindle book
how can i return amazon purchases
how can i reuse
how can i reverse heart disease
how can i reverse kidney damage
how can i reverse type 2 diabetes
how can i revert
how can i revert back
how can i revert back to onenote 2016
how can i review
how can i review etsy
how can i review my unemployment application
how can i reward my staff
how can i reward myself
how can i rewatch nfl games
how can i rewind on tinder
how can i rewind time
how can i rewire my brain
how can i rewrite this
how can i ring
how can i rip cd's
how can i rip dvds
how can i ripen apples
how can i ripen bananas
how can i ripen bananas fast
how can i ripen green bananas
how can i ripen kiwi
how can i roast
how can i rose
how can i rotate
how can i rotate desktop
how can i rotate my video
how can i rotate pdf
how can i rotate photo
how can i rotate view
how can i run c++
how can i run cd
how can i run diagnostic
how can i run dual monitors
how can i run dvd
how can i run flash
how can i run it
how can i run python code
how can i run someone's credit
how can i salt unsalted nuts
how can i save a password
how can i save email addresses
how can i save instagram pics
how can i save money fast
how can i save skype conversations
how can i save xml file
how can i say congratulations
how can i say goodbye
how can i say this podcast
how can i scan a document and email it
how can i scan something from my printer
how can i schedule a drivers test online
how can i schedule a fedex pickup
how can i schedule an email in outlook
how can i screenshot
how can i screenshot on hp laptop
how can i screenshot on kindle fire
how can i see hamilton
how can i see imessage usage
how can i sell avon
how can i sell my gold
how can i sell my url
how can i sell paparazzi
how can i sell stuff
how can i sell tupperware
how can i send someone robux
how can i share a kindle book
how can i share kindle books
how can i share my amazon cart
how can i share my amazon prime
how can i ship a bicycle
how can i short bitcoin
how can i shorten my life
how can i shorten my menstrual cycle
how can i show support for police
how can i shrink my blue jeans
how can i shrink my sweater
how can i sign a document on word
how can i sign a pdf electronically
how can i sign a pdf on my ipad
how can i sign a word document
how can i sign up for disability
how can i sign up for disney plus
how can i sign up for stimulus check
how can i simplify my life
how can i size
how can i size ring
how can i sketch something
how can i skip 8th grade
how can i skip a grade
how can i skip recaptcha
how can i skip school
how can i skype
how can i skype call
how can i skype for free
how can i sleep
how can i sleep better
how can i sleep better at night
how can i sleep cooler
how can i sleep early
how can i sleep fast
how can i sleep sleep
how can i sleep with sciatica
how can i slim
how can i slim my face
how can i slow aging
how can i slow down
how can i smell again
how can i smell my breath
how can i smile more
how can i smile today
how can i smoke
how can i smoke cbd oil
how can i smoke thc concentrate
how can i smoke wax
how can i smooth my hair
how can i smooth rough concrete
how can i snap
how can i snap windows
how can i snapshot
how can i sneeze
how can i sneeze fast
how can i snip
how can i snip a image
how can i snore less
how can i soften an avocado
how can i soften bread
how can i soften brown sugar gone hard
how can i soften brown sugar quickly
how can i soften clay
how can i soften dates
how can i soften denim
how can i soften hard brown sugar
how can i soften hard sugar
how can i soften my toenails
how can i song
how can i soothe my dogs itchy skin
how can i speak to an irs agent
how can i speak to someone at irs
how can i speed up my amazon tablet
how can i speed up my computer
how can i speed up my internet
how can i speed up my kindle fire
how can i speed up my old ipad
how can i spend my ppp funds
how can i spy on whatsapp
how can i square in word
how can i stop a toothache
how can i stop one drive
how can i stop overeating
how can i stop snoring
how can i stop stressing
how can i stop unwanted emails
how can i stream espn
how can i stream fs1
how can i stream gsn
how can i stream hamilton
how can i stream metv
how can i stream msnbc
how can i stream yellowstone
how can i strengthen my heart
how can i stretch elastic
how can i study chinese
how can i subscribe to disney plus
how can i subscribe to roblox
how can i substitute bread flour
how can i sue amazon
how can i support black lives
how can i support police
how can i support tucker carlson
how can i suppress my appetite
how can i survive the coronavirus
how can i sweat less
how can i sweeten my chili
how can i switch back to classic facebook
how can i switch banks
how can i switch between desktops
how can i switch between windows
how can i switch careers
how can i switch on
how can i switch side
how can i switch to google chrome
how can i switch user
how can i sync devices
how can i sync edge
how can i sync email
how can i sync gmail
how can i sync ipod
how can i sync my phone to my tablet
how can i sync windows
how can i sync you
how can i tag a page on facebook
how can i tag files
how can i tag friends in facebook
how can i tag in fb
how can i tag my chickens
how can i tag people in my photos
how can i tag photos
how can i tag someone on facebook
how can i take a screenshot
how can i take a screenshot on my amazon fire
how can i take a shot screen on my computer
how can i take my dogs temp
how can i take my dogs temperature
how can i take pictures
how can i take the bar exam
how can i talk to an angel
how can i talk to epic games
how can i talk to jojo siwa
how can i talk to piper rockelle
how can i tell her lyrics lobo
how can i tell if eggs are bad
how can i tell my blood type
how can i tell the difference
how can i tell what iphone i have
how can i tell which ipad i have
how can i tell which kindle fire i have
how can i tell you chords
how can i temporarily disable avast
how can i temporarily disable avg
how can i temporarily disable facebook
how can i temporarily disable mcafee
how can i temporarily disable norton
how can i temporarily disable webroot
how can i temporarily leave facebook
how can i tenderize beef
how can i tenderize meat
how can i tenderize sirloin
how can i tenderize steak
how can i test a microphone
how can i test my gpu
how can i test my iq
how can i test my ram
how can i test my soil
how can i test my usb camera
how can i test my video cam
how can i test my webcam
how can i text
how can i text a youtube video
how can i text cnn
how can i text from my mac
how can i text on a laptop
how can i text on my tablet
how can i text santa
how can i text someone through a computer
how can i thank
how can i thicken my eyebrows
how can i thicken my hair
how can i thicken my homemade hand sanitizer
how can i thicken my split pea soup
how can i thicken soup
how can i thin my blood naturally
how can i thrive
how can i tickle myself
how can i tighten
how can i tighten jowls
how can i tighten leather
how can i tighten skin
how can i time travel
how can i time travel in real life
how can i tint epoxy
how can i tint my windows
how can i tint plexiglass
how can i tip on postmates
how can i tkprof a query
how can i toast walnuts
how can i toggle
how can i tone up my arms and back
how can i touch jesus
how can i touch laptop
how can i touch screen
how can i touch you
how can i tour chernobyl
how can i track my mail
how can i track my phone
how can i track my receipts
how can i track my samsung
how can i track my stimulus payment
how can i track stimulus check
how can i transfer schools
how can i trust god
how can i turn into a mermaid
how can i turn into a werewolf
how can i turn off dropbox notifications
how can i turn off icloud storage
how can i turn off my location
how can i turn off my location services
how can i turn off my messenger
how can i turn the sound
how can i tweak my graphics card
how can i tweet
how can i tweet cnn
how can i tweet fox news
how can i tweet to twitter
how can i tweet trump
how can i twist my own hair
how can i twitter donald trump
how can i ty
how can i type
how can i type 1/2
how can i type arrow
how can i type in a pdf
how can i type on a pdf document
how can i type on pc
how can i type on the form
how can i typing
how can i unblock
how can i unblock access
how can i unblock chrome
how can i unblock content
how can i unblock email
how can i unblock games
how can i unblock url
how can i unclog a drain
how can i unclog a needle
how can i unclog a toilet
how can i unclog my ears
how can i unclog my nose
how can i unclog my pores
how can i unclog my toilet without a plumber
how can i unclog my tub
how can i undelete
how can i underline
how can i understand
how can i understand god
how can i understand hegel
how can i understand lds
how can i understand the bible
how can i unflag an email
how can i unfreeze excel
how can i unfreeze my ipad
how can i unfreeze my pc
how can i unfreeze outlook
how can i unfriend facebook
how can i unfriend on fb
how can i unfriend someone
how can i uninstall a program
how can i uninstall google chrome
how can i unlock my
how can i unlock my ipad
how can i unlock my iphone 4s
how can i unlock my iphone7
how can i unlock my laptop
how can i unzip a file without winzip
how can i unzip photo files
how can i update an app
how can i update chrome
how can i update microsoft excel
how can i update my games
how can i update my ipad to 12.0
how can i update my kindle
how can i update my silk browser
how can i update roblox
how can i update safari
how can i upgrade my firestick
how can i upload fonts
how can i use avocado seed
how can i use duck eggs
how can i use excel for free
how can i use my brain
how can i use my eidl funds
how can i use my hsa
how can i use my ppp loan
how can i use my redbox points
how can i use my stimulus debit card
how can i use paypal on amazon
how can i use ppp funds
how can i use sba loan
how can i use telehealth
how can i use the eidl loan
how can i use the f keys
how can i utilize my free time
how can i utilize my intuition
how can i validate a ssn
how can i validate a tin
how can i validate myself
how can i value my car
how can i value my house
how can i value my land
how can i value my trade
how can i vapor meth
how can i ve
how can i venmo myself
how can i vent a dryer with no outside access
how can i vent a toilet
how can i vent my anger
how can i vent my garage
how can i vent my microwave
how can i vent my ventless fireplace
how can i vent my wall oven
how can i verify
how can i verify a business
how can i verify a business license
how can i verify an ein number
how can i verify dea
how can i verify ein
how can i verify ged
how can i verify if my phone is unlocked
how can i verify my information in epic games
how can i verify my medicare
how can i verify my ssn
how can i vet a charity
how can i video call
how can i video chat
how can i video chat for free
how can i video chat on my kindle
how can i video chat on zoom
how can i video myself on my computer
how can i video myself sleeping
how can i videos
how can i view a docx file
how can i view a vcf file
how can i view foreclosed homes
how can i view recently deleted files
how can i view wingdings
how can i visit america
how can i visit armenia
how can i visit canada
how can i visit china
how can i visit cuba
how can i visit google
how can i visualize pi
how can i vlookup conditions in excel
how can i vlookup in a pivot table
how can i volunteer coronavirus
how can i volunteer for coronavirus testing
how can i vomit
how can i vote
how can i vote by mail in illinois
how can i vote by mail in mn
how can i vote on political polls
how can i vote online
how can i vote online in pa
how can i vote online today
how can i vote today
how can i vpn into my home computer
how can i vpn into my office network
how can i wake cortana
how can i wake my computer
how can i wake up
how can i wake up at work
how can i wake up earlier
how can i wake up early
how can i wake up easier
how can i wake up feeling refreshed
how can i walk again
how can i walk faster
how can i wash my car without water
how can i watch belgravia
how can i watch harry potter
how can i watch hbo max
how can i watch killing eve
how can i watch local channels
how can i watch scoob
how can i watch teen wolf
how can i watch the chosen
how can i watch the last dance
how can i watch the spacex launch
how can i watch uncle tom
how can i watch videos
how can i watch yellowstone
how can i watch yellowstone online
how can i watch yellowstone series
how can i way
how can i weakness overcome
how can i weather wood
how can i webcam
how can i website
how can i weigh gold
how can i weigh letters
how can i weigh myself
how can i weld cast iron
how can i weld hard plastic
how can i weld plastic together
how can i welding aluminum
how can i whatsapp
how can i whiten crowns
how can i whiten my bras
how can i whiten my dogs teeth
how can i whiten my eyes
how can i whiten my teeth in two days
how can i whiten my toenails
how can i whiten teeth
how can i whiten veneers
how can i win full custody of my child
how can i win pch
how can i win robux
how can i win some money
how can i win song
how can i win the lottery
how can i wire money
how can i withdraw 401k
how can i withdraw pf
how can i withdraw tsp
how can i work abroad
how can i work faster
how can i work from home
how can i work hard
how can i work harder
how can i work out
how can i work smart
how can i world
how can i wrap
how can i wright
how can i write an essay
how can i write notes
how can i write on a google slide
how can i write on a pdf
how can i write to president trump
how can i writing
how can i yelp a business
how can i you help me
how can i you use the apps i have installed
how can i you're taking all
how can i youtube
how can i youtube on a hisense smart tv
how can i zan fiskum
how can i zero out my quickbooks receivables
how can i zest a lemon without a zester
how can i zip a directory
how can i zip a pdf
how can i zip a video
how can i zip file
how can i zip folder
how can i zip my photos
how can i zip pdf files
how can i zip pictures
how can i zoom
how can i zoom in access
how can i zoom in chrome
how can i zoom in on edge
how can i zoom in on screen
how can i zoom my icons
how can i zoom out my video on zoom
how can i zoom outlook
</pre>

## Parsing JSON

Frequently network requests will return JSON data rather than HTML snippets. JSON, which stands for JavaScript Object Notation, is a plain-text file format for defining data structures with key and value pairs, with a syntax modelled on JavaScript's for defining objects.

A JSON file might look something like this, with an object containing a single key, `people`, whose value is an array of objects.

```json
{
  "people": [
    {
      "firstName": "Karl",
      "lastName": "Marx"
    },
    {
      "firstName": "Franz",
      "lastName": "Kafka"
    }
  ]
}
```

You may have noticed that JSON is structured quite similar to Python's `dictionary` type. In fact, it is easy to transform JSON into Python dictionaries, and vice versa.

As an example, let's look at FoxNews.com. Scrolling through the home page I see a small dashboard to the side with COVID statistics. By looking at the network requests, I can see that the data for this element is coming in through a request to something called `covid.json`.

![Covid request on FoxNews.com]({static}/images/covid1.png)

Clicking on that request, and then on the `Preview` panel, opens an interface that allows you to explore the JSON file. Click on different object keys to expand the data.

![Covid request on FoxNews.com]({static}/images/covid2.png)

The full file looks like this: an array of 2 objects.

```json
[
  {
    "ConfirmedToday":"18157379",
    "RecoveredChange":"0",
    "RecoveredToday":"4448281",
    "FullUpdate":"8/3/2020 4:09:14 PM",
    "Region":"World",
    "ConfirmedYesterday":"17859763",
    "DeathsYesterday":"685179",
    "RecoveredYesterday":"4448281",
    "DeathsChange":"5522",
    "UpdatedDate":"8/3/2020 12:00:00 AM",
    "ConfirmedChange":"297616",
    "DeathsToday":"690701"
  },
  {
    "ConfirmedToday":"4696573",
    "RecoveredChange":"0",
    "RecoveredToday":"622133",
    "FullUpdate":"8/3/2020 4:09:14 PM",
    "Region":"US",
    "ConfirmedYesterday":"4635279",
    "DeathsYesterday":"154598",
    "RecoveredYesterday":"622133",
    "DeathsChange":"567",
    "UpdatedDate":"8/3/2020 12:00:00 AM",
    "ConfirmedChange":"61294",
    "DeathsToday":"155165"
  }
]
```

To bring this in to Python, right click on the request, select `copy link address`, and then use the `requests` library to fetch the url. Calling the `json()` method on the response object will convert the file into a Python dictionary:

```python
import requests

response = request.get("https://feeds-elections.foxnews.com/covid/covid.json")

# convert the response into a python dictionary
data = response.json()

# data is now an array with two elements, the second contains us data
us_deaths_total = data[1]["DeathsToday"]
us_deaths_today = data[1]["DeathsChange"]

print("Total US Deaths: {}".format(us_deaths_total))
print("Total US Deaths Today: {}".format(us_deaths_today))

```

## Complex Requests & Being Yourself

Simply copying the request URL and pasting it into a Python script may not always work, for multiple reasons:

1. The browser might be making a POST request rather than a GET request. In this case data is being passed to the server through the body of the request, rather in the URL's query string, so copying the URL will not pass the proper data to the server.
2. The browser request could be using cookies, either because you are logged in to the website you're trying to scrape, or to pass other data to the server.
3. The server could be attempting to limit requests to browsers, by looking for a user agent string or other indicators, and is identifying your script as a script or a bot.
4. Who knows!

Regardless, there is an easy way to just _make things work_ and perfectly duplicate the behavior of your browser: Right click on a request and select `Copy` and then `Copy as cURL`.

![Copying a network request as cURL]({static}/images/network-copy-as-curl.png)

`cURL` is a command line tool for making HTTP requests. The "copy as cURL" option copies the request URL, it's parameters, cookies, and **all** other data sent to the server as a single (usually very complex-looking) cURL command. To execute the command, just paste it into your terminal and hit enter. As far as the server is concerned, the cURL command should be indistinguishable from what your browser is doing.

### Integrating cURL and Python

You can also translate the cURL command into Python code (as well as many other languages) using a wonderful tool called [curlconverter](https://curl.trillworks.com/).

Simply paste the cURL command you copied from the browser into the form and you'll get back a functioning Python script.

### Scraping Employee Reviews of US Customs and Border Protection

Many websites, including free ones, require you to register an account before you can browse their content. For example, Glassdoor provides a forum for employees to leave reviews about their employers. These reviews, while freely accessible, cannot be read by anonymous visitors. To scrape a website like this, you would need to make a script that acted as a logged in user. Fortunately, this is easy using the `copy as cURL` trick.

As an example, here's how you'd scrape employee reviews of US Customs and Border Protection on Glassdoor:


1\. Log in or create an account with Glassdoor. Then [visit the review page](https://www.glassdoor.com/Reviews/US-Customs-and-Border-Protection-Reviews-E41481.htm) for Customs and Border Protection.

2\. Open up your console with `command-option-i` and click on the `Network` tab.

3\. It's probably empty! Scroll to the bottom of the page and hit the next page button to load in the second page of reviews.

4\. Click on the different network requests that start appearing until you see one that seems to hold the data you're looking for. In this case, I notice that a request with the name `graphql` looks promising.

![graphql request]({static}/images/graphql_request.png)

5\. Based on the syntax (the brackets!) I can see that the data is being loaded in as a JSON file. In the `Preview` tab I can click on different keys in the data to see their contents, and by exploring the tree deeply enough I start to see the content of the actual reviews.

![Expanding JSON requests]({static}/images/graphql_expanded.png)

6\. This next step is to bring this request into Python. Right click on the request and select `copy as cURL`.

7\. Paste into the curl box in the [curlconverter](https://curl.trillworks.com/).

8\. Finally, paste the generated Python code into a new Python file. You should have something that roughly looks like this (I've shortened it for the sake of readability):

```python
import requests

cookies = {
  # a bunch of stuff in here!
}

headers = {
  # a bunch of stuff in here!
}

data = 'a very very long and confusing looking line'

response = requests.post('https://www.glassdoor.com/reviews/api/graphql', headers=headers, cookies=cookies, data=data)
```

To convert the response to a Python dictionary, and print out some negative reviews, add the following lines:

```python
json_data = response.json()
reviews = json_data[0]["data"]["employerReviews"]["reviews"]
for r in reviews:
    rating = r["ratingOverall"]
    cons = r["cons"]

    print(cons)

time.sleep(1)
```

Note that you will need to carefully look through the response JSON in the web inspector to figure out exactly what fields to extract.

You can also change the data being sent to the server to fetch different results. In [this example](https://github.com/antiboredom/scrapism/blob/master/examples/glassdoor_reviews.py) I modify the `page` field being sent to the server to get a small archive of negative Border Patrol reviews:

<div style="border: 1px 0px solid #ccc; font-size:0.85em;height:300px;overflow-y:scroll;font-family:monospace;">
<p>"All duties as assigned" Means anything they want you to.</p>
<p>"We only speak the simple language here". (Being English)</p>
<p>- CBP/DHS is consistently ranked as the worst place to work in the Federal Government (according to OPM's annual Federal Employee Viewpoint Survey).  I can tell you through personal experience that this is accurate.</p>
<p>- From first-line supervisors to SES personnel, CBP has some of the most incompetent managers I have ever seen. Not only do many of them lack the technical skills to do the job, but they have no idea how to LEAD people.</p>
<p>- Management constantly provides negative feedback and they refuse to believe that happy employees are productive employees.</p>
<p>- Management does not communicate with its employees enough</p>
<p>- The morale is dead and is not going to improve unless most of management is replaced with people who actually know how to motivate, inspire, and engage their employees.  This will never happen since there is so much nepotism and favoritism within the agency.</p>
<p>- The turnover rate is very high; it's a revolving door and you are just a number.</p>
<p>- Too many meetings behind "closed doors"</p>
<p>-Cynicism</p>
<p>-Feels like DMV with a firearm</p>
<p>-Lack of employee development</p>
<p>-Long Hours</p>
<p>5 day, 50hr minimum work weeks on a shift rotation.</p>
<p>A lot of hours and overtime</p>
<p>A lot of irregular work schedules. You will be working a lot of holidays and weekends and possibly even double shifts.</p>
<p>A shift could go from 8 - 16 hours with little notice.</p>
<p>Abusive environment. You get to be an a hole to everyone who isn't an American citizen. And sometimes you get to be an a hole to Americans as well.</p>
<p>Always changing shift work makes it hard to balance work and life plus the president does not support the mission as much as they should.</p>
<p>Always understaffed, some times very little training.</p>
<p>Apathy - There was no commitment to do the best you can do.  Management was afraid to address union or race issues.</p>
<p>Back Stabbing SOB's,,,lookout for the management.</p>
<p>Bad management, stupid people, poorly maintained facilities, inadequate staffing, micromanagement,</p>
<p>Basically TSA with a gun</p>
<p>Biggest con is most southern border port of entries(where CBP does most hiring) are by far some of the worst places to live in the country.</p>
<p>Budget cuts suck and you will wonder if you have to start looking else where. Sequestration sucks like the leaders.</p>
<p>Bureaucracy was stifling.  It feels like you have to write a memo to get approval to write the real memo.</p>
<p>Bureaucratic and "old-boys" club culture. Very stratified. Commitment to the mission is evident in the "field" but is lip service at the leadership level where competition for position and power is evident. The mission is affected by the lack of collaboration between CBP and other DHS organization's.</p>
<p>Can be mundane.</p>
<p>Can be seen as "inferior" from some of the Law Enforcement Officers (Customs, ICE, etc.)</p>
<p>Changing shifts, Pay is equal to a lover level manager, small overtime budget and staffing.</p>
<p>Constant pay cuts, not enough promotional opportunities</p>
<p>Could be a fairer playing firld</p>
<p>Coworkers and managers lack job knowledge and don't care about doing it right.</p>
<p>Cubicles are a modern form of torture!</p>
<p>Dealing with the government in general can be frustrating.  Everything depends on congressional funding. Multiple systems that do not work together.  Always a time delay and red tape for program and systematic updates.</p>
<p>Difficult to get a transfer, lots of forced overtime, poor management, horrible working conditions.  Mangers micro manage every single aspect of your work day. Very little autonomy</p>
<p>Difficult to get hired.</p>
<p>Employees moved rather than fired. Incompetent management. Everyone is acting in their positions. If you are “on the inside” you will travel often to courses and conferences on the government dime, if not you will sit in your home office and never leave.</p>
<p>Extremely poor upper management, dangerous working conditions, poor leadership, lack of support, poor experience of lower graded agents.</p>
<p>Geographically poor work locations with inability to move.</p>
<p>Getting hired is hard due to the polygraph procedure which is right of out 1984 "Orwell".   How horrible this is depends on the examiner but their play book comes straight from Internal Affairs with orders to tear you down.   Yes I have read it and I personally find it insane.   FWIW since it's transition  DHS has rated bottom of the list or second place at the bottom in the annual Gov employee satisfaction. survey.   First and second level supervisor turnover is very high with many working a couple years then voluntarily busting back to regular officer.    There is little or no positive interactive between management and first line officers and CBP brings new meaning to the term Micromanagement .   You will encounter these conditions at every POE anywhere in the country with very few exceptions.</p>
<p>Government BS, Have to work a normal work week or weekend, either way its M-F 8 to 4. for an average of 8 days off a month, compared to airlines and most other jobs.</p>
<p>Govt shutdowns get to be a pain when your paycheck is delayed.</p>
<p>Hard to balance family life. If you take the job in another state it's really hard to move around if your port is not a desirable port.</p>
<p>Have to stop work until other agencies are contacted.  Homeland Security is subject to political funding and that causes issues.  Other agencies pay one grade higher .</p>
<p>Having to deal with upper management that makes decisions that look good on paper but don't work in reality.</p>
<p>Hiring freezes and the lack of ability to move from one area to another.   Some folks display favoritism.</p>
<p>Hiring process is overkill, Mandatory overtime, Polygraph interview turns into an interrogation, will share your answers with other agencies,Polygraph is setup to incriminate yourself,not a fair hiring process</p>
<p>Homeland Security and CBP are politically driven agencies.  The mission can become clouded by the administration in power.</p>
<p>Hours tend to be long, work is hard and tiring.</p>
<p>However, the over staffed management positions detailed or employed in USBP's administrative/office settings have abused their overpaid positions, and are an ineffective bloated element within USBP.</p>
<p>I don't believe I've ever had a bad experience while working there.</p>
<p>I have never encountered such hostility</p>
<p>If you don't like to work overtime not the place for you. Schedule is different from one location to the next.</p>
<p>If you work at an airport, you will most likely be opening people's luggage all day</p>
<p>Inability for upward movement, unwilling to spend money to get certifications that would benefit the agency and office, and applied pressure from senior management to do things that violate policies, law, and agreements.</p>
<p>Incompetent Supervisors that advanced through the ranks by the agency's growth. Redundant training. Since, nobody really gets fired if someone gets in trouble or messes up they usually end up being a supervisor. Mindless repetitive work. Health and Physical fitness is not a priority. Hiring process is very long.</p>
<p>Inconsistent workflow (slow then busy)</p>
<p>Inept management, low morale as a whole, very difficult to transfer or relocate.</p>
<p>Instead of challenging the system, I chose to quietly give my 2 weeks notice and leave without starting a fuss. Trying to stand up to the ingrained ineptitude at CBP isn't worth anyone's time. The realization I came to was that If you want a REAL law enforcement career try a local police department. They will likely have similarly poor office politics, but you are much likelier to work alongside respectable, hard-working individuals who care about helping their community.</p>
<p>Institutional barriers working for the federal government brings continuous frustration in meeting objectives. Lack of originality in management practice.</p>
<p>Involuntary drafts. Weird shifts. Social cliques.</p>
<p>It doesn't matter if you do a good job or a bad job. You'll be rewarded or punished according to the whims of who ever has the power to do so. The level of nepotism and cronyism is unbelievable so if you are not in, you're out. The incompetence that some people get away with will astound you and promote them because they've got the connections and you don't.</p>
<p>It's a job, how bad can it be.</p>
<p>Job application process took extremely long. Almost a year since the day I submitted the application</p>
<p>Lack of intellectual challenge. A great many CBP Officers just want a government job to collect a paycheck from. Nothing more, nothing less. They don't care about stopping crime or enforcing the law, just give them a paycheck and don't ask them to work too hard. This attitude is reinforced from the top to the bottom.</p>
<p>Law enforcement is not condusive to a strong work/life balance that other professions may provide. Government bureaucracies tend to operate without efficiency which can be frustrating for some.</p>
<p>Limited advancement opportunities for Agriculture Specialists beyond Deputy Chief Level.</p>
<p>Limited employment opportunities for recent graduates</p>
<p>Little actual law enforcement.  Sitting at work day in and day out watching many law breakers go about their day due to little to no enforcement.</p>
<p>long hours and constant travel</p>
<p>long hours and lots of detail assignments away from home</p>
<p>Long hours at various times</p>
<p>Long hours away from family.  Last minute notice of overtime after working a full 8 hour shift.</p>
<p>long hours, alot of prior tranining, long probational period</p>
<p>Long hours, facilities can be rough in older airports/cargo offices, normal headaches that come along with managing union employees.</p>
<p>Long hours, lack of respect for common employee by public and management</p>
<p>Long hours, shift work, varying work locations.</p>
<p>lots of corruption</p>
<p>low hiring standards</p>
<p>low morale</p>
<p>Management at DC level is more concerned with looking like they are doing something rather than accomplishing anything.  Most missions are a joke. Academy has been dumbed down to make it easier to get the job.</p>
<p>management doesn't really care about employees</p>
<p>Management forgets the employees are not robots but human beings.</p>
<p>Management here doesn't care about you. Will easily replace you with contractor if they can. JOIN THE UNION!!! The government managers can be very shady. When I worked at WSPD, my managers promised me one thing then broke it the next. Don't trust your directors, they don't have your back. Literally work until your step grade is up or your GS7/9/11 program finishes. After that, move on to another government job. They promised me a job at the end of my 3.5 year internship (which by itself is kinda odd), but they fired me because of "Lack of Performance" (After I got a JAC Award from the Director that said my performance was outstanding)...Went to a DoD contractor after that.</p>
<p>Management in IT is often clueless.  You need to push a mountain to get things accomplished because of the crazy policies put in place.</p>
<p>Management is scared of it's own shadow.</p>
<p>Management isn't held accountable for anything and seems to be rewarded through promotions for bad behavior. Managers are rated on their leadership skills without any feedback from employees. Developing employees to become top performers is not a priority to managers. It seems that the agency would rather continue to pay contractors than invest in their own employees.</p>
<p>Management may not be perfect.  However, the worst people you will deal with is not management or passengers.  The worst individuals that you will have to deal with are you're fellow employees.  Depending on whether they are on the Fox News side or the CNN side, that's how they will treat the passengers.</p>
<p>Managers are under too much stress and aren't always leaders.</p>
<p>managers not well trained</p>
<p>Mandatory overtime with no regard for your personal life or family life. You get up to 5 weeks vacation but they steal it from you anyway by forcing you to call in sick to get a day off - so after you burn up your sick leave you use up annual leave then take leave without pay. Frequent payroll errors never in your favor: You have to check your hours worked against your earning and leave statements. They mess them up constantly, making you chase your money.</p>
<p>Micro management, irregular hours, constantly changing policy.</p>
<p>Middle of border town with not alot to do, Laws for immigration</p>
<p>Monotonous work sometimes that could get boring.</p>
<p>Morale has been a problem for some years. Constant problems with Congress and budget. Supervisors change every two to three years.</p>
<p>Morale is low due to the constant battle over pay. Lack of prosecution of cases due to current administration. No real brotherhood with co-workers.</p>
<p>morale low</p>
<p>Most supervisors lack training and knowledge are insecure in their positions. Therefore, they project their insecurities on front-line personnel through mistreatment and vindictive disciplinary write-ups. I was once ordered to write a false report for a supervisor to corroborate his write-up of another officer he didn't like. I told him "no" and promptly gave my two weeks notice. I didn't even bother reporting the incident to CBP Internal Affairs because I knew they wouldn't do anything and that the supervisors would simply adopt me as their new "punching bag."</p>
<p>Much of the mission support leadership are career govies that lack the strategic planning skills to really be effective</p>
<p>Mundane at times</p>
<p>Need more of a challenge</p>
<p>Nepotism and cronyism kills morale.</p>
<p>Nepotism, sometimes it may seem who you know vs. Who you are in relation to upward mobility.</p>
<p>New approaches to problems, not welcome.</p>
<p>No advancement opportunities in Field Offices.</p>
<p>No cons all is good.</p>
<p>No cons are described in the duty</p>
<p>No cons that I can think of</p>
<p>No cons that I can’t think of</p>
<p>No cons to be noted.</p>
<p>No downsides at all to working here.</p>
<p>No life balance, over worked, and "good ol boys" club attitude</p>
<p>No life, always working. Stressful</p>
<p>No maternity leave</p>
<p>No mobility. Limited upward potential. Bi-polar management from the top down. Extremely politicized environment with little guidance or continuous focus on any particular mission.</p>
<p>No moral some DEPT may be different</p>
<p>No OT, and bad union. Micro management! !!</p>
<p>No professionalism, bureaucratic, no management support.</p>
<p>No respect, less than a number, low morale. Owned by the government and at their mercy. Dangerous, very hard on the health, will die younger.</p>
<p>None so far and none expected.</p>
<p>None that I can think of right now.</p>
<p>None, I plan to stay with the Agency until I retire.</p>
<p>none, it is a wonderful career</p>
<p>Not enought incentives for improved employee performance. Need better training programs. Need to have training for employees who want to learn different job functions, even if it's not appart of their job description.</p>
<p>Not for the faint of heart. You wear a gun and train for deadly force for a reason. This can be a very hazardous job. Also,  you have to "give up" your life. Overtime is mandatory, and most times you do not know you are doing mandatory overtime until 1 or 2 hours before your shift is over. Many, many days of 16 hours. By the time you get home and manage to fall asleep, the alarm goes off. This can happen once or twice a week, or even up to 4 times per week. No time for family. If you are single, it is great. If not, well it is NOT great.</p>
<p>Not good for a family life.  It is hard to relocate closer to family, that's the reason of some agents leaving the agency or switching to other components within DHS.</p>
<p>Not great if you have a family</p>
<p>Not very creative or exciting.</p>
<p>Note: If CBP/DHS is your first federal job, I suggest you get your career status and/or max out your promotion potential in your position... then start looking for a new job in a better agency (you can only go up).</p>
<p>Odd hours, but easy to change schedules.</p>
<p>Often weird hours and holidays as typical in LE.    Leave can be hard to get when you want / need it as they are often understaffed to accommodate .    You have to set up leave choices  for the year by the fall before (usually).    The big money comes working double shifts with turnarounds, it's great cash but hard on you.</p>
<p>One other "con" I have is how this agency abuses, and outright steals overtime benefits.  Uniformed employees believe they are entitled to 2hrs OT/day even if they are not required to remain at work.  Most of the time, USBP agents are hanging around, complaining of the lack of work there is to do in the office, but stay to collect OT funds.  This is a HUGE ongoing problem, with no resolution on the horizon...ever.</p>
<p>Others are not so good to work with</p>
<p>Overall USBP is a good-ole-boys-club for management level staff.  The agents in the field are some of the greatest around.  They are extremely frustrated with the political mess we are in right now as a nation, unable to complete their mission effectively, but they DO give it their all every single day.  My hats-off to them.</p>
<p>Paperwork for the smallest of tasks.</p>
<p>Pathetic management, liars and chronic harrasers</p>
<p>Pay does not match the responsibilities that are given to techs as higher level tasks are given at low pay.</p>
<p>Pay freezes, limited promotion potential. Unions exercise great control but rarely produce any results. Shifts can be erratic and management has unrealistic expectations at time.</p>
<p>Pay, lack of youth, may not pay for education, slow</p>
<p>Per the current union contract, managers can force you to work up to 3 mandatory overtime shifts of 16 hours in a row. It's unsafe, especially because CBP Officers are armed law enforcement entrusted to make sound decisions. Who can make a sound decision after 15 hours of work?</p>
<p>Political Climate/Politics & Government Shutdowns</p>
<p>Political environment when moving up the ladder.</p>
<p>Polygraph Has 68% fail rate, their interrogation will last over 10 hours. Compared to 90 min with other departments. They are short 20,000 agents according to articles. Have a TS Clarence and could not pass.</p>
<p>Poor management</p>
<p>poor schools</p>
<p>Possibility of being voluntold to go places for tdy.</p>
<p>Problems recruiting due to current process</p>
<p>Professional staff salaries are not that great</p>
<p>Questioning the status quo, not welcome.</p>
<p>Rotating shifts and days off... no Saturday and Sunday</p>
<p>rude and hostile locals</p>
<p>Senior leadership is not consistently on the same page as CBP faces a multitude of security and monetary challenges over the prior few years.  More and more leaders seems to be "seeing the light" recently, but it will take some time before everyone is on the same page strategically speaking.</p>
<p>Senior management has a tendency to not delegate decision-making to the manager who has the greatest competency in their particular area of expertise.  CBP needs to be more flexible in streamlining their procurement process.  CBP unwillingness to allow Industry as a value added partner, has result in failurs such as the SBI net.</p>
<p>Seniority based days off</p>
<p>Seniority decides all management will not enforce any immigration law</p>
<p>Sexual harassment of females is ever-present at CBP. Many supervisors, chiefs, and even higher have a mysoginistic attitude towards females. In fact, many supervisors feel that it's their right to flirt with and attempt to pick up female members of the public while on-duty and in full uniform. It was truly embarassing to be associated with these slobs.</p>
<p>Shift work and sometimes long hours standing up.</p>
<p>Shift work, mandatory overtime, and lack of communication are 3 downfalls of CBP.  If management would discontinue it's separation from the front line things would run smoother.  Management has no clear idea of what day to day operations are like. Often 1-4 hour port tours are given breezing over nonsense that has nothing to do with the reality of the job.</p>
<p>Shiftwork and time away from family</p>
<p>Short term contracts and lack job opportunity to transfer over to the Federal government.</p>
<p>Slow promotion track</p>
<p>Some of the dumbest and most incompetent management I have ever experienced. Been here ten years and it keeps getting worse. Looking for a better opportunity. Good luck.</p>
<p>Some of the policies tie your hands.</p>
<p>Sometimes it can be a little to easy.</p>
<p>sometimes there are mandatory overtime, very fast paced, repetitive</p>
<p>Tax payer dollars fund this department and restrict solid advancement.</p>
<p>Th work can be very mundane.  If you do  not have any strong feelings about customs or immigration it can feels as if you are not accomplishing anything.</p>
<p>The agency uses Scare Tactics and focuses on publicly calling attention to the prosecution of officers that have broken the rules.  There is a weirdly negative undertone to many of the guidelines they want staff to follow.  The agency prioritises the issues and needs of their direct law enforcement staff above all other staff. They are still not treated too well.  They refuse to allow  several of the veterans here to use their GI bill education benefits while employed.  The training for this position is very intense as well,  if you fail any of the eight exams more then once...You lose your job .</p>
<p>The atmosphere is too much like being back in high school, too many clicks.</p>
<p>the hours can be hard on family</p>
<p>The Interview process if you are person of diverse background (Hispanic* or Black) DON'T NOT APPLY.  Not matter how qualified you are the hiring authority, think otherwise. Even if you did score best. Speak another language? Don't even think about putting it down on your resume. Interviewer will qualify this as Un-American. Your diversity seems to be the issue here. They don't even bother in shaking hands with the person of diverse backgrounds, Unfortunately this seems to be a common theme for DHS not hiring Diversity at top management. Mass amount of security breaches take place and rather than hire people, they look as diversity as a problem.</p>
<p>The job can be repetitious at times as you will need seniority to get better assignments (which can take years).  The agency is top heavy with management, and some of these managers know very little about the job.  Favoritism is rampant and many officers are promoted based on who they know, not how much you know.  There is little to no warning on forced overtime and you will likely have to stay for another shift (16 hour day total).  The schedule can also disrupt your family life as some supervisors will not give you time off.</p>
<p>The job had very very long days, Overtime is only compensated at 25% of pay, bad hierarchy, too much is based on seniority and not on past experience or production.</p>
<p>The management level employees I have worked with have always been a disappointment.  Aside from the 10yrs w/the IRS, management with each agency have been extremely overpaid, lazy, and careless.  With USBP the management staff are continually rotated in/out, leaving permanent department employees in a constant state of "re-inventing the wheel" syndrome. In the 6yrs with USBP, I have seen 7 immediate supervisor changes, 5 next level changes, and our Chief of Sector has rotated out 6 times now.  The department I work in, currently has 6 supervisors for 13 employees... yes you read that right 6/13.  Every time a new immediate supervisor comes in, they want to "change things", even though it adversely affects everyone in the department.  It might be a law enforcement thing, but every new supervisor wants to "leave their mark" before moving on (even if it is unnecessary, disruptive or foolish).  Each supervisor is assigned to our department for no more than 2yrs, but you would be amazed at the havoc they can create in those 2 short years!</p>
<p>The mission was not fully supported by the management.   Shift-rotations played havoc on personal life and sleep. Career development was based on seniority and favoritism instead of performance and merit.</p>
<p>The overall senior leadership could benefit from a course in open communication, if such a course exists.  Leaders are not as engaged as is necessary to get the most out of their employees.  Most of the senior leaders are afraid of their own leaders.  Their direction to us is based on that fear - not truly free to think on their own.</p>
<p>The work can get monotonous and boring.</p>
<p>There are no cons for this job.</p>
<p>There are no cons, Do your Job!</p>
<p>There is limited opportunities for training and caps at GS-07. Due to the GS-07 cap it is difficult to move to a higher paying position.  If a person is not careful you can get stuck. Also this position allows for forced overtime and working holidays, it all depends on management.</p>
<p>There is no clear career path and promotion opportunities are very limited.  Leadership do not take the time to recognize employee excellence and provide opportunity for team or individual success.</p>
<p>There is no upward mobility or career growth.</p>
<p>They say it does not exist but it definitely does.</p>
<p>This was the worst job I ever had. The office culture is unprofessional and reminded me of being in high school. I worked with many unqualified people who really didn't work that much during the day. Basically I didn't gain anything at this job, and my manager was totally hostile.</p>
<p>To be recognized for my contribution.</p>
<p>To much favortism. Standards for hiring have gone way down. Professional Behavior is only  in theory.  Many new hires are not there to work but for socializing and Management will do nothing about it</p>
<p>Too many bosses and higher ups.  You have to do everything their special way  Then wait a long time for any outcome.</p>
<p>Too many to mention here</p>
<p>Tough work schedules.  16 hr work days, and 7 to 8 day' straight work' stretches. Government seniority detects opportunities. Hard to transfer out of Laredo, TX.Not great for city people.  The nearest cities are San Antonio 2.5 hrs away; McAllen 2.5hrs away; Corpus Cristi 3 hrs away; Austin is 4 hrs away.</p>
<p>Travel for work and training</p>
<p>Trying to cut our pay and retirement</p>
<p>Understaffed with many employees performing multiple acting roles.</p>
<p>undesirable locales to live in</p>
<p>Uniformed persons treated much better than civilians</p>
<p>unprofessional management</p>
<p>USBP also has a big problem with promoting those who are liked, as opposed to the quantity of those who perform.  It's a buddy system here.  You're either promoted "out" for being unliked, or promoted "in" because their buddy decides it to be so...and it's always a promotion to move along the unliked.  Yes, there are some good leaders, but the ratio of good AND qualified remains a big question mark.</p>
<p>Varying shifts, nepotism, bad locations</p>
<p>VBT (video based test) gave scenarios of jobs and situations that eventually you will be trained for at the academy. Yes it does measure you behavior along with a lot of other things. I feel as if applicants and candidates should only have the Structure Interview and not the VBT that you will be trained for. Is a serious job, a lot of pressure and most applicants would be nervous. Is not comfortable to be video taped while interviewing.</p>
<p>Very archaic in terms of flexibility. This is NOT the agency to join if you are looking for all of the wonderful flexible arrangements you hear about in federal government</p>
<p>Very boring job with little ability to hone various skills</p>
<p>very busy sometimes, but its a rewarding career.</p>
<p>We need to be a proactive organization</p>
<p>When the head of the entire agency releases a memo to all employees stating  "...federal employee survey results indicate that we have the lowest morale among all federal agencies  for the 5th year running.  We will no longer be taking feedback regarding morale."  you know you have problems and that they will never be taken seriously or resolved.  The organization is run like a mafia outfit with tyrannical power pockets, unjust firings, and an atmosphere of suppression and fear that make doing your job done on a day-to-day basis a living hell.  Leadership is as politically dysfunctional as it's technology is advanced (for a government agency).</p>
<p>With much overtime comes no life.</p>
<p>Work and life balance challenging.</p>
<p>Working as an automotive mechanic has its downsides.  Working in the hot and cold weather.  Budget is low for tools.</p>
<p>WOW....worst leadership I have EVER experienced.</p>
<p>You can forget about being recognized for your accomplishments. On-the-spot awards are given only to officers that management likes. In one case, I saw multiple on-the-spot awards given to an officer simply because she was a supervisor's niece.</p>
<p>You might have to work on weekends and holidays.  You might get dirty opening up cargo and inspecting it.  The benefits are good but not as good as a state or county employment agency.</p>
<p>Your hard work won't count as a person or individual. You will just be a number like a robot if you can bear it after years of service, many employees wind up divorced stress or more serious health conditions.  Large male environment not supportive of WOMEN, very difficult for women of any age and much more difficult job to balance if you have a family.  Women have the highest calls for counseling needs to EAP and EEO's. Lots of schmoozing croonism copycat self entitlement attitudes and environment. Lots of demoralized coworkers and mismanagement caused issues. Agency is worst rated within Federal Viewpoint Survey and overall. HQ and DFO management does not have a clue to ask lower level grade employees how to improve agency and work environment and save jobs and monies. Very difficult to get promoted, management spends wastes budget Congress allocated monies on promoting management and creating management positions instead of lower grade employees. NTEU union takes your dues and local union (male) president plays politics with little legal representation when needed much less for women's issues. Union is "not" representative of  women's issues at work. Cons rating is for all of Florida.</p>
<p>Zero leadership. Chief of the Border Patrol bows to the commissioner of CBP. Constant threats of cutting agents pay. You stress every year because Customs and Border Protection finds another way to demoralize agents by taking a percentage of pay. Agency spends billions on stuff it doesn't need like forward operating bases, which the agents have to man on weeks on end. Frivolous spending on ridiculous agent manned camps that agents are forced to work while simultaneously claiming agents there is no money to pay the agents. Start work here, than move to a professional law enforcement agency</p>
</div>

You can use the same technique to scrape virtually any website.
