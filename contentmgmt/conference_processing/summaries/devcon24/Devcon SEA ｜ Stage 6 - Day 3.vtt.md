e e
[Music]
for
e
oh
m
is
and
yeah e
hello hello welcome
everybody day three of devc con we're
going to be we're going to be starting
in 10 minutes get excited get ready
oh e
[Laughter]
ready
okay folks five minutes five minutes
we'll be getting started get excited
all right let's get going welcome to
Devcon day three who's excited for some
applied
cryptography excellent hope you enjoyed
that nice flute music while we got
started um my name is Sam I'll be your
MC today we got some really exciting
talks a lot of good stuff um first off
we got gub sheep is going to be telling
us how to hallucinate a server um I
guess quick
housekeeping um with these talks we'll
try to do five minutes for Q&amp;A at the
end of each you're going to see a QR
code that'll link you to a
mircat um poll to allow you to submit
Q&amp;A and upvote questions as well so take
advantage of that let's learn let's
listen uh let's have fun um and first up
gub sheep
welcome thank you
s awesome thank you Sam for introducing
the morning sessions uh hello Devcon I
am gub sheep and I'm here to talk to you
about hallucinated servers thank you for
joining us on this morning I I know it's
not easy to make the uh first morning
talk of the day so I appreciate
everybody for making it out here um by
way of introduction I'm gub sheep I'm
one of the co-founders of zerox Park uh
in particular I work on a lot of Applied
cryptography projects from research to
production and today I'm going to be
talking to you about frog Zone which is
a game that you might have seen
downstairs if you swung by the Frog
crypto Community Hub so downstairs at
the Frog Community Hub we have two
tables of four machines
each you can log into one of these
machines using your zass by scanning a
QR code and you'll be dropped into this
very simple frog game that I'm going to
describe now so this is a screenshot
from the game
essentially frog zone is a four player
game where you control one of four frogs
on a 32x32 grid so there's a 32x32 grid
there's a map there's some items there's
some monsters um you can attack the
monsters you can pick up the items
you're trying to explore the map you can
only see the 5x5 area around you and in
a time limit of 5 minutes you're trying
to make it up north uh to the ice biome
to find and slay the dragon and this is
a Cooperative game so even though you
don't know where the other players are
all of you are going to have to
collectively come together to figure out
um the right path to get up there and
then use your combined items to uh
finish off the dragon so as you can see
you know my Frog's moving around um I
just uh destroyed some enemy here here I
can see there's a wooden sword I can go
over to the wooden sword and pick it up
um and if I do that uh I should see my
attack stat up there increase so you can
see you know frogs have frogs have lives
they have different stats let's just
watch that happen real quick and as you
can see the rest of the game is shrouded
this fog of War right so I can only see
the 5x5 area around me um and in short
you know it's a pretty simple game right
there's a very very limited set of
mechanics um in terms of you know the
game in numbers the total size of the
game is about a total of 150 bytes
that's the entire state of the game the
front end is built in react and phaser
the source code for the back end is
about 500 or so lines of C+ plus not
including boilerplate that might be
something like half of that um and it
took about a month for a team of of devs
and collaborators from gaus labs and
xerx park and psse to build this
together so um why am i showing you this
why am i showing you this incredibly
simple game that uh you know a a kid
could have probably built as their first
programming project well essentially the
interesting thing about this game is
that the back end of the game is running
entirely inside of fully homomorphic
encryption and to our knowledge this is
the first time a multi-user application
with a backend that is running inside of
FHA has actually been built so that
means that all of the state of this game
is encrypted using FHA and all player
actions and everything happening inside
of the game is happening inside of
FHA thank
you so one question you might ask is why
bother running this inside of FHA right
FHA is super expensive well one thread
that we've been pulling at in the last
year is this idea that technology IES
like fhe can enable us to run what we
think about as hallucinated servers so
let me describe what I mean by that
today if a group of us wanted to come
together and to build some sort of
application that all of us might use
like let's say a social network for
Devcon attendees the way we would do
that today is that we would have someone
rent out an AWS server write some sort
of backend code and then deploy that
backend code to the web server and then
each of us would you know using our
computer using our browser or client or
whatever else talk to this backend
server making API requests to to you
know update and retrieve the state of
the
application now using Technologies like
programmable
cryptography another way we can imagine
doing this sort of thing opens up so we
can imagine in a world with programmable
cryptography that rather than there
existing a specific physical server with
a physical footprint that's running all
of the computations of the application
instead every participant of the
application might store Something Like A
cryptographic Shard of the overall State
and using Technologies like multi-party
computation or fully homomorphic
encryption we could cryptographically
simulate the execution of this virtual
machine using things like ZK proofs or
FHA to advance the state of this
arbitrary computation one step at a time
ensuring its consistency ensuring that
everybody is only you know having access
to the data that they're supposed to be
able to um while doing so in a in a
decentralized multi-party way without
needing to rely on a physical server
anywhere that actually is the source of
Truth for the
system so you know this this sort of
opens up a lot of interesting questions
what if our Digital Services ran as
these distributed hallucinated
computations between just the relevant
parties we could imagine having this
abstraction for a server where instead
of you know servers run by Zuck we have
a server made of math that's perfectly
secure privacy preserving verifiable
interoperable with every other service
built in this way Etc of course right
now we're very early on our journey so
in terms of the game and numbers in
order to run this extraordinarily simple
game 150 bytes of state with four frogs
on a 32x32 grid uh we are using nine
machines to coordinate a variety of
different MPCs together so we have four
MacBooks downstairs and then we also
have five 192 core AWS machines in the
cloud costing us about $200 an hour to
run this game
every binary gate involved in the
execution of any operation takes about
about a one billion times overhead on
top of ordinary computation and for
every bit of plain text state in this
game this bit will blow up to about
be 3,000 bytes of Cipher text I need to
check on that but it's a huge
overhead so the way that I think about
what's going on is it's sort of like you
know we've built almost this particle
accelerator and spent enormous amount of
resources just so that we can suspend in
the middle of The cryptographic Ether
for a brief instant something that looks
like the higs bow Zone and we can we can
sort of hold that stably um and in short
we have built what I believe is the
slowest and worst performing game in the
history of
computing okay so how does it work let's
dig in a little bit to what's going on
under the hood so like I mentioned
there's about nine machines that are
concurrently performing various things
together uh in order to hallucinate the
state of frog zone five of those
machines are c6a 48x large AWS machines
they have 192 cores each 384 gigabytes
of memory and then we've got our four
MacBooks which are our local clients
that are involved in the decryption MPC
so whenever a player wants to make a
move uh you know move their fr up down
left or right or attack a monster or
pick up an item they're going to send
the encryption of that intent of that
request to one of these five servers
that server is then going to share that
encrypted request with all the other
servers and each of them is basically
going to keep a replica of the fully
encrypted state of the game so that move
is then going to be you know uh shared
with between all of these massive
servers and then executed inside of FH
to update the state now in order to
retrieve the latest state of the game
and in particular that 5x5 area around
you each of the client machines is going
to be talking to a dedicated server that
will handle the request of executing a
view function on the overall State and
then returning the result of that view
function in encryption to the players so
we need five servers here because all of
these operations are enormously
expensive we're using these machines to
distribute the load of both executing in
fhe all of the player actions as well as
executing the view functions over the
state to return back to the
players finally because the state is
returned back to the players in
encryption no single player has the
decryption key for the whole game in
fact you know no single party in this
whole system has the blanket ability to
decrypt and read state so the four
clients each contain a decryption key
Shard and they have to coordinate using
a simple multi-party computation in
order to decrypt any individual piece of
state so I'm going to send out requests
that's kind of that big box that that
switch in the middle of the four clients
for those who have seen the machines
downstairs that is helping to coordinate
the the peer-to-peer networking that
needs to happen for these machines to
talk to each other okay so what's going
on with the servers here I've described
the the idea that a hallucinated server
would not need a physical machine that's
actually the source of Truth for the
application State and yet I just showed
you a diagram where there's a fleet of
five machines well it turns out that in
this case the servers aren't
theoretically necessary what they're
doing is they're performing a
deterministic operation that involves no
secret data so they're basically just
these you know cattle which you can
delegate computation to um they're
performing these operations on top of
encrypted data using a deterministic FHA
scheme uh theoretically we could run all
these computations on the local machines
and just have them cross check each
other but for performance reasons based
off of where fhe um is today with the
libraries we're using Phantom Zone we
need to you know sort of add some
additional computation power in addition
to the four client machines that we have
so that's all that those servers are
doing um I want to talk now about some
tricks that we use to get a game working
in such a constrained
environment so building out this game
with the other collaborators has been a
really interesting exercise it kind of
reminds me of what I've read about game
development really really early on you
know with the first uh personal computer
games in the 90s or even earlier than
that arcade machines in a lot of these
settings game developers were working
with very limited constraint sets and
for me also this kind of reminds me of
the early days of building blockchain
based games so about five years ago I
worked on a game called Dark Forest and
this was before l2s um this was before
there was widespread kind of tool chain
support for ZK snarks and you end up
having to do a lot of interesting little
hacks to even get something so simple
working so going back to our constraints
we have about the ability to work with
maybe 200 bytes of plain text State we
have a 1 billionex computation overhead
uh we have an overhead that's somewhere
in the thousands in terms of how big
Cipher texts are which have implications
about how much State you can be
transmitting over the network especially
here at a conference where tons of
people are using bandwidth to find frogs
or you know access their ticket things
like that um and one thing that we
wanted to hold ourselves to was we
wanted to keep each player action
operating under one second so every
action that a player can take should
execute in about one second and that
means that if all four players are
constantly making actions then players
can be rate limited to performing an
action once every about four seconds or
so I can start by even looking at how do
we represent player actions so all of
those different actions that you can see
in the game whether that's uh picking up
an item or moving to a square or
attempting to move onto a square you're
you're not allowed to move to or
attacking a monster all of those are
simply serialized as two encrypted bits
that represent a direction and under the
hood what the FHA circuit is going to do
is it's essentially going to execute all
of these possibilities for what you're
moving on to or what you're attacking
Etc it's going to execute all of that
simultaneously so what that means is the
FHA circuit is going to take in the
approximately 200 bytes of game State as
well as two encrypted bits that
represent your direction and it's going
to check for example for each of the
tiles that you should not be allowed to
move on to we'll do an equality check
between each of those pairs of
coordinates and if any one of those
equality checks turns up true then I'm
going to return your new coordinate as
equal to your current coordinate and not
equal to the the coordinate that would
be computed by incrementing your X or Y
position similarly with an item we're
going to simultaneously check for every
item is the coordinate you're trying to
move to uh you know that that result of
applying the direction on top of your
original coordinate is that coordinate
equal to each coordinate of all of the
items and if any of the items turn up
yes then we're going to prevent you or
we're going to cause you to update your
internal state to reflect the item
upgrade that that item might give and
we're going to mark that item as
consumed and then we're going to refresh
the entire state so uh we basically have
to figure out some strategy for
factoring out the state into these
different pieces and then running these
checks efficiently over all of these
different uh State coordinate
pairs another thing that we have to be
very aware of is the data constraints so
um we don't want when when we're
returning back something from the
hallucinated server to a player for the
decryption phase um we don't want to
have to return a bunch of custom fields
for all of the different kinds of
entities that could live on a tile in
particular because the computation that
is returning what should be on each tile
lives in encryption whoever is making
that return statement cannot know what's
on each of those tiles so we would have
to you one naive way you could imagine
implementing this you could imagine
implementing a big checklist that
contains all of the items and all the
monsters and all of the Just all the
entities and for every single one of the
encrypted bit for each checkbox in the
checklist of whether that particular
entity is at that particular tile and
because that bit is encrypted the server
whoever is running the FHA that could be
a local client would not know anything
about what actually lives there um
that's too expensive given the cipher
text blowup so what we do is we have a
actually um for what is actually being
returned for any given entity so we'll
do some computation in the circuit it
will result in 32 bits depending on what
those bits are after the decryption
phase that will tell you how to
interpret these 32 bits so the first
bite tells you you know various types of
metadata The Entity type the ID knowing
the entity type tells you how to
interpret the the remaining three bytes
um for the second bite if it's a player
or a monster that represents the hit
points if it's an item it represents the
uh additional up if it's a player that
represents score if it's an item or a
monster that represents how many points
you get for picking up the item or
points for defeating the monster and in
this way we can we can make sure that
every tile that's being returned is
simply this uh 32bit thing without
needing to special case for every single
type of
entity moving Monsters uh was a fun one
as well so basically you've got these
four frogs that are moving around in the
universe each of them can see a 5x5
square around them but there's also a
bunch of stuff going on in between each
of the players viewports so monsters are
actually these autonomous agents that
are moving moving around inside of the
global fog of War there's some notion of
global private state state that is being
executed on consistently but which
nobody in the game neither players nor
any of the delegated computation servers
know what's happening so um in order to
do that well this is very expensive
because for every monster we want to try
to move we again have to do that check
of is that monster moving to uh on a
collision course with any of the the
boundary cells so in order to make it
feel like there's a bunch of monsters
and they're moving in a reasonably uh
performant way what we have is we've
just got these different kinds of
monsters one of them one of the kinds of
monsters is immobile so we just never
have to do this another kind of monster
we do have to do all of those Collision
checks and then a final kind of monster
the bat here it's a flying monster so
you don't have to do the Collision
checks which you know speeds up things a
lot on our end and still makes sense in
the context of the
game there is a story about Randomness
here as well so whether it's the initial
conditions of the game or how the
monsters are moving you don't want any
particular particip to know that but you
want that to be able to happen in a way
that is correct and consistent with the
execution of the program so at every
stage and at the beginning of the game
players are going to submit they're
going to randomly generate some
Randomness locally encrypt that and send
that up to the server the server is
keeping an encryption of a global random
State and every time it receives a
request it can mix that in and then it
will use that Randomness to seed various
actions on NPCs or or
whatever okay so that's the current
state of things you can try the game out
downstairs just as a warning it's very
slow and very clunky and very brittle I
would not exactly call it a good
gameplay experience um but you can play
it and you can try to slay the dragon um
so another question to ask is Where Do
We Go From Here Right Now that we've
demonstrated that it is in principle
possible to build an application in this
way what might we want well one thing
that has become really clear is we might
want more performance whether that means
you know adding a fleet of of 10x more
servers or whether that means improving
the underlying FHA protocols or the
libraries that Implement them so with
this actually as a local computation
between the four machines without
requiring these delegated servers to
help us perform these untrusted FHA
operations we could imagine procedurally
generating the map itself so imagine
that rather than a fixed hard-coded map
that is plugged in at the beginning of
the game in encryption all of the
players submit their Randomness and use
an algorithm like pearand noise to
generate a new map every single time
that truly no one not the developers nor
the delegated servers nor the players
would
know another thing that's going on here
is that in the process of building this
we realize that fhe as a technology is
limited in certain ways so I previously
described how in order to make any
operation on the game you would have to
feed the entire previous game state in
plus the mutation that you want to do on
top of it and run a state transition
function over the entire thing in FHA
well that's not really how we think
about programs today we usually think
about programs in terms of memory access
I can access such and such array element
I can update I can read I can write to
this um and that ends up being much
faster because I don't need to carry the
entire state with me on every operation
there's active theoretical work being
done on FHA protocols and MPC protocols
that might fit more naturally with the
the program the memory
model one thing that's been really
annoying especially with a conference
Wi-Fi is the decryption stage that must
occur between all four of the parties
using Technologies like obfuscation and
functional encryption which we uh
discussed earlier this week you would be
able to make it so that the view
functions so long as you're calling the
correct view view function can return to
you the appropriate state that you want
decrypted so without a need for this
kind of group decryption so that makes
the hallucinated server behave at that
point almost identically to a server um
we want verifiability so whatever
machines are executing the computation
the FHA computation right now they can't
learn anything about the computation but
they uh can execute whatever function
they want they'll just they could be
executing some
nonsense and then finally you might want
something like a data availability layer
you know if you want to add in
properties like censorship resistance or
certain forms of consensus perhaps you
want to treat frog Zone as something
like a rollup so that's an interesting
direction as
well um there's a few sort of conceptual
or philosophical questions that arise as
well right like is this an autonomous
world you know somehow the bat that's
flying around an encryption that nobody
knows where it is it has a kind of
autonomy that is a different sort of
autonomy from the kind that we get from
blockchains and smart contracts but it
does feel like a new dimension so what
is you know what is the subjective
experience of being a bat that lives in
frog Zone that lives inside of
encryption you know maybe this is how
we're going to do mind upload technology
in the future I I certainly wouldn't
wouldn't want to upload my brain into
the cloud in plain text but I might do
it if if it's encrypted or OB fiscated
so that's all for this talk I just want
to shout out um a number of contributors
who have made this possible this was a
joint effort uh it was built on top of
Phantom Zone which is developed by gaus
Labs a bunch of folks from psse helped
enormously in running the circuits Han
edu and CC so Han and Maran helped to
build out the front end um and a bunch
of zerox Parkers as well helped with the
deployment of this um so that's all I've
got for this talk you can scan this QR
Code by the way for a froggy surprise
for those of you who have been playing
the Frog crypto zoo pass based ZK based
game uh this will give you access to
something special but thank you all for
coming to this talk and we'll take
questions
now thank you thank you gub sheep we do
have a few minutes for questions I think
it's going to come up on the screen if
not I can read
them um can you elaborate more on The
cryptographic Primitives you used got
into a bit curious if it's Lattis to
achieve the
fhe yeah so one thing that that's
actually been really interesting about
exploring this whole fhe world is that a
lot of our old friends from ZK come up
again so for example one of the
operations that folks might be familiar
with that we have to optimize a lot
during you know ZK programming is fast
fora transforms and various kinds of
polinomial operations these things also
come up in various FHA schemes and we
suspect that maybe they could be
accelerated even with similar methods um
fhe schemes also rely on some
cryptography we don't see as much in ZK
such as lates um and uh we might have
different strategies for approaching
those but this is very much an open kind
of question I don't think that what
we're using right now for uh necessarily
Phantom Zone or frog Zone today is going
to be what we use in perpetuity um but
yeah there's a lot of of these early
exploration directions awesome looks
like some folks are curious what is the
most powerful use case you've imagined
with this with this Tech stack yeah so I
mean one one exercise you can kind of
run is like what if you take the most
ridiculous technology that exists today
and just mash it all together um I like
to think about this idea of a cryptomed
which is what I think as cryptography's
equivalent of AGI so imagine that you
had perfect obfuscation it was running
on a blockchain that had enormous data
availability guarantees and bandwidth um
what you would get is basically like a
truly self Sovereign program that's made
out of math that's can never be taken
down it's always executing properly you
can never open up the program to inspect
its internal State except as it is
allowed to run if you add in things like
Quantum oneshot signatures that program
might have things that can only be
executed once so it really feels like a
physical program and then you might
think what happens if you put an AG what
if you run an AGI inside of that well
now you have this essentially autonomous
being made of pure information that has
first class citizenship with reality in
the same way that you or I do or any you
know living thinking brain so I don't
know the speculation here can get pretty
crazy love it um looks like people are
curious about code repos about Library
usage yeah if you go to github.com zerx
park frog dzone you'll be able to see
the code for this particular game this
is built on Phantom Zone which is under
the gaus labs organization so if you're
curious uh come by the Frog Hub and
we'll get you set
up awesome another round of applause for
gub
[Applause]
sheep awesome really incredible yeah
would highly encourage if you guys do
have more questions or curious to check
it out go check out the Frog Zone lot of
cool stuff happening on there um crypto
frog Mania is in full force this week um
yeah definitely check it out quite a few
rabbit holes you can dig down if you
want to spend the rest of your Devcon
doing that um moving on more great talks
next up we have Andreas co-founder of
file verse oh okay getting ahead of
myself we'll be back in a few minutes
with some more great talks so stay
tuned e
okay
folks another great talk coming up at
the applied cryptography
track um here we got Andreas one of the
co-founders of
filee here to talk about how we
decentralize the internet's
collaboration layer so get excited um
again there will be a QR code if you
guys have questions during the talk feel
free to put pop that in and we'll have a
few minutes at the end to chat through
it so welcome Onre
hey everyone thanks for making it to the
morning sessions I know it's not easy
especially after yesterday's parties so
yeah uh originally this is this was
meant for the real world ethereum track
so I'm going to talk to you today a
little bit about the legend legendary
Pokémons of crypto AKA apps apps apps
not much of infrastructure in here um
and the main goal of the talk is
actually to talk about how do we
actually approach decentralizing one of
the most essential activities on the
internet which is collaboration and I'll
use specifically the Defcon collab app
that we developed for Defcon with a
bunch of uh uh teams right here
including the Defcon team and that I'll
describe in a bit I'm Andreas I'm the
co-founder of favs and d.
new and let's
go so super important oh actually super
important context to uh get started with
there is over half of all internet users
that trust one single close sourced and
centralized App Suite for their daily
knowledge and collaboration Google
workspace and this is catastrophic
because it's what you do every day it's
related to your identity is related to
your uh friends family social graph Etc
so the premise that underlies my my talk
here is that internet Freedom meaning
your uh digital rights right to access
information right to uh coordinate with
others right to not be censored on the
internet cannot be guaranteed behind
World Gardens worse even we cannot even
imagine new forms of coordination and
collaboration that are independent of
the cloud Empires and a third party
guaranteeing this type of collaboration
for us I'm going to speed through
because I have only 10 minutes so I'm
going to go at 1.2 speed here the
problem speaks for itself uh Mass
surveillance constant leaks uh constant
uh uh fumbles by companies companies
going bankrupt linkr leaks
Etc and uh this problem is actually one
that the crypto Community knows very
well and yet um it has a bit of
difficulty moving onto something new uh
we should know better but we could not
necessarily do better until very
recently so you know we had our old
aspirations and we've moved into
something that is a little bit
convoluted uh messy in a bunch of
infrastructure that doesn't give us
enough Direction now um my point uh in
the second section is that uh we should
think of social technical counterposing
to the cloud Empires to the current
situation on the centralized web and one
useful concept uh to use here is by
Ethan Bachman which is personal
computers Unleashed an unimaginable
levels of sovereignty and
interoperability for people and
Community computers meaning public
blockchains will do the same for groups
now examples examples because we want to
see apps here this is the Defcon collab
.io app uh the reason why I wanted to
show you this today is because it was a
community effort it's something that uh
started with the idea that okay what if
we didn't depend on 15 telegram group
chats 35 notion Pages 63 Luma pages and
more for our conferences and actually
preserved our knowledge and ability to
communicate connect and collaborate on
something that is properly decentralized
so here on this app this is powered by a
smart contract that lives on gnosis
chain it's powered by the chatting is
powered by xmt the storage happens on
ipfs it is also uh the content
addressing of all your content here is
put on chain access permissions are also
done on chain you have people actually
contributing incredible uh uh knowledge
through PDFs their own notes uh comments
likes Etc and this combines the
technology that has matured over the
past 10 years including from uh waku
from l2s from uh Zupas for
authentication Etc and one cool part of
this app that I really wanted to
highlight is a realtime collaboration
that you can do and this is accessible
to all Defcon attendees at the moment
which is enabled purely through
peer-to-peer connections to your uh
peers so let me show you with a little
introduction by vitalic
himself
see yeah
yeah
go go like you know like servers like
somewhere in America I'm not sure where
right and the reason why it has to be
this is because people
of
okay so uh this was just a a quick demo
of the live collaboration that you can
do in a peer-to-peer manner now just to
finish since I have just one minute I
want to give you a little list of apps
to give you a little bit of Hope about
the direction of the space at the moment
I just wanted to highlight one of the
latest just St blog post uh just to
describe the actual properties that
developers might have been looking very
actively uh uh for in 2017 during the
Ico era when we were still calling
ethereum the world computer which is
that if you give ethereum
code um uh we can receive a very strong
guarantee that it will run it uh anytime
we call on it and that if you give
ethereum data uh and know with certainty
it will still be available in the future
unaltered and uncorrupted so there are a
lot of Primitives that have matured
since I have 30 seconds uh these are
some of them I'm going to put them Just
online here so that people can see that
take screenshots be available also on
YouTube uh those Primitives have matured
today we combine also see public
blockchains with peer-to-peer networks
in a really scalable and useful way and
this allows us to create new generation
of apps that rival the ux and actually
protect the data of our users at a
global scale we don't need three billion
people anymore depending on one
centralized Cloud Empire we can actually
have properly decentralized apps for
everyone and these are some of the
amazing examples that have emerged in
the past two years only so I highly
encourage you to actually look them up
try them this is a future of ethereum
and and this is actually I believe the
future of the open free web and not one
that will be guaranteed by Third parties
that nobody actually wants to trust
thank you very
much all right thank you Andreas cool
stuff looks like we got some
questions how does one Insurance power
doesn't centralize over time or fail to
be
maintained yeah uh great question so uh
the immediate answer is trying to rely
on as few third parties as possible so
we have a bit of a morbid thought
experiment in our team uh we like to
think okay what happens if our whole
team disappears tomorrow turns uh uh
turns malicious and the answer is that
uh our apps or decentralized apps can
continue running because we actually do
not take care necessarily of uh uh
introducing new infrastructure we
actually leverage networks that already
exist and that do not depend on one two
three four parties actually maintaining
them so here you have communities that
are maintaining these Community
computers if you'd like and building
apps on top of them guarantees that you
know the apps that you're using are
passing the walk away test a team can
walk away you can continue accessing
your data running the software and be
inde dependent and self-
Sovereign Love it yeah um so we like the
tech we like the Vibes how do we how do
we bring the noobs so um a lot of the
AMS that I actually showed in the last
uh uh slide uh are Noob friendly uh so
radical for example is for um your
average uh uh developer coder instead of
using GitHub they can use uh radical
doo.
new is made so that you wouldn't
have even the need to create an account
which is a friction that even Google
Docs have uh has a lot of those apps
also work offline they work in a way
that do not require uh wallet that do
not require you to dox yourself uh at
coinbase give the name of uh your family
where you live uh picture of your cat in
order to get some crypto to then send to
your wallet to then actually sign in a
transaction to actually be able to use a
app so a lot of those app do not require
all this and account abstraction is
something actually that got us past this
important threshold of ux which is
something that we're taking full
advantage of in the apps that I just
showed
you right on and we see question around
how do you how do you do the realtime
Tech is it using crdts
servers tell us more yeah uh so yes uh
we're using crdts amazing piece of
technology that came out or matured by
Martin uh k u kman uh at Inc and switch
that talks about crdts and how uh infra
less and peer-to-peer apps are actually
possible uh also our code is open source
if you want to learn a little bit more
about it go ahead and look at it and
yeah we use web RTC we use indexdb to
keep as much data as possible local and
do the syncing via web RTC and some
other Technologies uh again that you can
look up on GitHub or come talk to me
afterwards for a
discussion right on give it up again for
Andreas thank you very much
yeah pretty insane to see half the
internet is relying on Google sweet glad
to see we're moving away from that um
all right we'll be back in a few minutes
with another great talk stay tuned we'll
see you soon
in
okay welcome
back going strong we got a talk from
Richard one of the co-founders of zkp
top up next
uh talking to us about trust minimalized
P2P marketplaces on ethereum give it up
Richard awesome hey guys I'm Richard uh
today I'll be talking about trust
minimize P2P marketplaces uh on ethereum
uh go over the why how and some thoughts
of looking
ahead so why are we here um if we look
at web 2 today uh data currently exists
in these centralized data silos whether
it's fiat currency in your bank account
uh your social graph concert tickets
domains Etc um these lead to high
switching costs for users for example
you can't bring your followers from
Facebook to Twitter or and these also
are very extractive uh to these users
for example Ticket Master charges like
monopolistic prices because they own
both the secondary and primary uh
exchanges and lastly there's like closed
apis uh which make it very difficult to
interrupt additionally if you look at
web 3 in our permissionless database uh
the problem is that it's really detached
from The Real World uh if you look at
your social graph stable coins like
these defi instruments and even eth uh
all of it runs in a parallel system in
fact most of defi today is self
referential uh and so the solution here
is to bring the real world to ethereum
and the question is how
uh we can break through these kind of
wall Gardens using cryptography and also
maybe tees uh so we can use ZK and MPC
uh these new technologies to allow us to
permissionless export uh data from these
centralized data silos uh techniques
such as ZK email and TLS notary which
also can help us redact any kind of
private sensitive information prior to
exporting uh check out some of the other
talks on ZK Emil or TLS notary today if
you want to learn more
deeply um but yeah now with these tools
we can kind of compose any kind of web
two action with web fre action uh such
as proving a Fiat transfer using ZK
email to swap for some stable coins uh
on chain or proving uh ticket transfer
using TLS notary to swap for stable
coins uh or swap domains for eth ETC or
even put a social graph inside a te to
do some defi stuff
with uh an example of this flow uh that
is in production today is ZK PDP the
project I work on uh the problem uh that
it fixes some of the issues I mentioned
earlier um such as the high fees uh the
construction for this is pretty simple
actually a seller comes in escrow some
funds in a smart contract and provides a
payment ID uh buyer comes in pays a
seller and uses that proof uh to unlock
the esro contract uh kind of replaces
binance or any kind of centralized
exchange with a smart contract and
replaces the manual process of unlocking
the escrow uh with instant unlock upon
satisfying a predicate
this construction extends Beyond Fiat uh
simply replace the offchain payment with
a digital asset transfer and a proof of
payment with a proof of asset transfer
now you can kind of do P2P trading
tickets trading domains trade social
media handles csgo skins uh gift cards
and much
more you can even further extend this
construction if you if you trust tees as
a credit po third party you can kind of
encumber a web 2 account put it inside a
te and act that act as a escrow for the
web 2 asset and both seller and buyer
send requests through the te uh once the
te owns both funds and the web two asset
say tickets uh then they can proceed to
unlock funds to both
parties uh yeah now you kind of can see
the web 2 account is fully programmable
you can do some weird stuff like make
the te run an amm pricing model for exam
for example
yeah in conclusion uh design space is
huge to do trust minimized marketplaces
uh the tech here is ready uh Dev tooling
will continue to only get better and
instead of only bring ethereum to the
real world I think it's time to bring
some of the real world onto
ethereum uh thank you and that's
it thank you Richard do we have any
questions shy crowd today come on
guys graphic of the P2P Marketplace I
don't even know if you have the ability
to go back in
slides sorry is this better yeah yeah if
if you can't go back that's okay I was
going to ask something about it but it
doesn't
matter yeah I don't think we can maybe
you can just just talk to
it
okay any particular use cases you're
most excited about like in terms of
future of peer-to-peer
marketplaces uh I think there's just a
lot of ideas out there like you can put
almost any internet data on chain and
use it uh like use yeah trade trade any
kind of web to asset or even data and
anything that you think has value on it
internet you can kind of bring on chain
to do cool stuff with yeah love to see
it I mean just the like you said Ticket
Master I think a prime example of just
like marketplaces that are absolutely
using monop monopolistic pricing to just
gouge consumers and what is becoming
yeah a very much frictionless process to
do straight straight Peter Pier um I
guess a question have you seen any
regulatory
issues um how are you thinking about
navigating that uh yeah I think
um they're haven't been so far I think
P2P is a legally I guess gray area kind
of thing uh you are allowed to transact
with like your peer for example Facebook
Marketplace is like a huge P2P
Marketplace and we're just basically
enabling uh the coordination of that to
be easier through onchain means uh on
ethereum
totally all right thank you Richard
appreciate it give it up thanks
back next up we got more talks on
hallucinated servers very exciting new
developments in the applied cryptography
in the in the Prague crypto space um and
here here to chat about it is Brian from
ZX Park please give him a warm welcome
Brian thank
you and I'd like to thank the organizers
for putting on this very exciting event
here in Thailand
anyway I'm with zerox Park we a um a
Research Foundation studying
applications of all sorts of modern new
exciting tools and
cryptography
and okay there we go zerox park so we're
a Research Foundation studying
applications of modern developments and
cryptography and today I just want to
take you on a very quick tour of four of
those cryptographic
Primitives that promise to have some
really exciting
applications and tell you where these
tools are as far as is being available
development so first off this is just a
giant uh Tech Tree of all sorts of
different uh cryptographic Primitives
things you can do with
cryptography so it starts out at the
bottom we have plain vanilla
cryptography things like encryption or
digital signatures or public
cryptography which have been around a
long time they're well established we
all know how to do them and we use them
in day-to-day
life and as you go up you get you get
more and more advanced
tools uh the arrows the arrows mean
reductions so for example if you have
fhe then you can use that to get
encryption FHA is kind of strictly
stronger than encryption so as you go up
the tower you get stronger and stronger
cryptographic tools that you can do more
and more things with that unlock
functionalities you didn't have
before so I'm I'm going to for the rest
of this talk I'm going to focus on four
of these
Primitives ZK snarks a snark snark
stands for proof so ZK snark stands for
zero knowledge
proof multi-party
computation fully homomorphic encryption
and then at the very top of the tower
program
obfuscation so I just with the time I
have I just want to give a quick
introduction to these tools and say what
you can do with
them so let's start with ZK
snarks also known as succinct zero
knowledge
proofs so mathematically a zero
proof is a way to prove you have a
solution to a system of equations right
f ofx equals z kind of represents a
system of equations X could
be I don't know of a thousand variables
or a bit string of length a million or
something like that and then f is any
sort of function you could apply to
it and so f ofx equals z is just a
system of many equations and many
variables and if we have some system of
equations then I can prove to you that I
have a
solution to uh to that system of
equations using some sort of Algebra I
can prove it to you without revealing
anything about
X
and the proof can actually be much
shorter than the system of equations so
I could have a million equations and a
million
variables and I somehow I do some sort
of cryptographic
something and I somehow encode my
solution as just maybe a couple of
kilobytes even though the solution
itself was megabytes in size my my
encrypted solution is a couple of
kilobytes
and you take my encrypted solution you
can verify it and be
convinced with with cryptographic
security that I have a real
solution but you can't learn anything
about it you can't learn anything about
the values
X unless I choose to reveal I could
reveal some part of X or all of x if I
wanted to and then you would learn what
I revealed but nothing
else so this is why it's called a zero
knowledge proof I can prove I have a
solution but you don't learn anything
about
it now you might think well systems of
equations those are kind
of well we only see them in algebra
class what good are
those
but X could really you should imagine X
could be any kind of bit string anything
that can be an input to a computer
program and F is any function that you
can you can write and
code so for example if there's some
public key somewhere
I can prove that I'm the owner of that
key I can prove to you know I can prove
to you that I know the private key
corresponding to the public key without
telling you the private
key or for another example if I have
some sort of message that has a digital
signature on it maybe it's an email and
it's been signed by the email server as
part of some some email
protocol then I can redact that message
and reveal only the parts of the message
I want
and yet you still learn you still get
this guarantee that I'm I'm showing you
a legitimately signed
message these um zero knowledge proofs
we know how to do them it's it's they're
kind of widely used in practice there's
a cost
overhead you know compare it to just
redacting a message redacting a message
is very cheap if I want to prove to you
that this is an honestly redacted
message well that's a little bit more
computationally a little bit more
expensive you can do a simple zero
knowledge proof on on a mobile device
you can do a fairly substantial one on a
laptop so this is maybe the easiest the
simplest of the four
Technologies so what I mean
algebraically I said zero knowledge
proofs are about solutions to
equations
conceptually there
you get kind of a different picture
conceptually it's about data Integrity
or about verifiable computation you know
maybe I did some computation for you and
you want to know that I did it right
without having to go through all the
steps yourself a zero knowledge proof
lets you check it more
efficiently or maybe I have some
cryptographically signed
data some a tested data somehow I apply
some transformation to it and I want to
convince you that this this this
transformed data is still legit
so I think of zero knowledge proofs as
being about integrity and
Trust okay let me move on to two uh
related Primitives multi-party
computation and fully homomorphic
encryption and maybe in the interest of
time I'll focus on the first of the two
I'll focus on
MPC the basic idea behind multiparty
computation is Imagine each of us has
some secret some some number some name
some I don't know what and we want to
compute something that's a function of
all our
secrets so maybe we want to I don't know
we want to find out how many of our
secret numbers are bigger than
the same
name but nobody's willing to reveal
their secret we can't we're not just
going to reveal our secret numbers or
share our
names so abstractly you have some
function that takes how many people do
we have in here 30 40 you have some
function that takes 40 inputs and gives
an output and you want to learn the
output to the function without anyone
revealing anything about their
inputs besides of course what you could
learn after what you could learn from
output so this is um this is what
multiparty computation lets you
do multi party computation also it's
been around a while it's been
used at least once in practice it's a
fun story so I'll tell it there was a
Danish beat auction the Dan the the Beet
Market in Denmark is I think the word is
a monopsony you have a single buyer and
a lot of sellers you have a lot of small
time farmers and then there's the one
giant beat conglomerate that buys up
every everybody's beats and turns them
into what do you make out of Beats be
juice I don't know whatever it is they
make so you have the one buyer and they
they they want to run an auction to
figure out what's the what's the price
that they're going to buy the Beats at
but all the farmers are a little bit
afraid of the the the one big buyer
because if if the one big buyer finds
out how you know how strong my financial
position is well that's that's really
dangerous so each farmer has their price
and they're they're not really
comfortable having an the sort of public
auction where you know the the people
running the auction can can learn their
price so they ran maybe 15 years ago in
Denmark they ran this giant multiparty
computation with all the beat farmer
prices as
inputs to set the price of beats in
Denmark that's the sort of thing you can
do with
MPC it's um like ZK like zero knowledge
proofs it's doable in practice it's
definitely a lot more expensive than
doing the computation the naive way
where we all kind of share our inputs or
you know send them to a central server
but it's doable there are software
libraries that will let you do
this so what does multiparty computation
buy
you it's a different kind of thing from
a Zer knowledge proof it's a sort of
collaborative kind of a tool it's
something that lets you collaborate
while still preserving
privacy you don't want to give up all
your secrets you only want to give up a
little bit of your data to
um just enough to be able to do whatever
it is you want to do set the price of
Beats or or you know find out who how
many people have the same name or
whatever it
is and MPC lets you do that
while we're here I want to describe the
image of a hallucinated
server that that this talk is based on
so imagine you you're you're you're a
bunch of people I don't know you're a
billion people and you want to set up a
social
network so one way you could do this is
you could you could find a Zuck
somewhere who could say okay you know
I'm going to open a big company and and
run a big server in in California and
everybody's going to send their data
into my server
and then I'm going to do whatever it is
Facebook does That's So useful to people
I don't know recommend friends to people
or tell people what their friends are
doing or what they're interested in or
is in other words everybody has their
billion inputs to the
server which they kind of like to keep
private and the server takes everyone's
billion inputs and does some sort of
computation on them I don't know what
you know something depending on who you
tell it your friends are and what you
tell what your interests are and
whatever else but you know the server
runs some kind of
computation and then it gives you your
output well this sounds an awful lot
like a multi-party
computation and so if you could do
multiparty computation at this scale
then well then these billion people
don't need a Zuck all they need to do is
the billion of them kind of write the
code okay someone still has to write the
code but you know they they agree on the
program they're going to run the Social
Network program and they all run it as a
multi-party
protocol there is no server there is no
one data broker that holds everyone's
data and does the
computation so if you have NPC these the
this group of people can get together
and and hallucinate a server they can
kind of dream up a server just by using
an NPC protocol that has the same
functionality as a server
so that's why we call this a
hallucinated
server very quickly fully homomorphic
encryption is another tool it's very
different on the surface but it gives
you the same kind of affordances in the
end the idea find fully homomorphic
encryption fhe the idea behind is I
can encrypt some data and give it to
you and then you even though you can't
read it you can operate on it so imagine
I have some X my data is X you have some
function some f you can kind of operate
on operate your F on my encrypted data
and give me back a thing that when I
decrypt it it's F
ofx so here you know I have X you have
the function f and you never learn
anything about what's inside the data
all you do is you blindly apply this F
and you hope when I get the answer back
it means something to me because it
doesn't mean anything to
you but again it's a it's a
collaborative computation sort of tool
the sorts of things you can do with
and the sorts of things you can do with
MPC are broadly very
similar if you've seen our a frog game
as here ARX Park we put together some
game involving
frogs that relies on some sort of
combination of these two things some
multi-party fully homomorphic encryption
fhe is somewhat slower than oops fhe is
somewhat slower than
MPC it's there are implementations out
there it just takes them a very very
long time to do anything at
all so probably you should imagine you
could maybe add two integers in a
fraction of a second but anything more
complicated than that with current
technology is going to be a little slug
and again if you've seen the frog game
you might have you might have
noticed now we're going to move on up
the tree beyond the realm of the
Practical at least the um practical with
current technology and into areas of
active research so at the very top I
promised you indistinguishability
obfuscation or I might call it program
obfuscation and what is
this this simply says I can take any
program I like again you should imagine
f is some you know some source code in
your favorite programming language that
computes some
function and I can obfuscate the
code so it doesn't change the
functionality the obfuscated code still
does the same thing as the original
program but you can't learn anything
about how it works just from reading the
source
code you can feed inputs in you can get
outputs out you can you have the source
code so you can you know see what it's
writing in memory and you debug right
you can see what it's
doing but you don't learn anything about
my original implementation of
f so this seems kind of mysterious what
do you do with this
I'm missing a slide here but the sort of
thing you could do with program aisc is
you could hide data inside of a program
for a simple example I could hide a
private
key to sign a message or decrypt a
cipher text or whatever it
is and so I could write a program that
says well I'm going to read the message
first I'm going to take a message and
I'm going to see if if if if you know if
I would approve it and if my program
approves the message then my program can
sign it issue a digital signature using
my private signing key and I can give
you this program and you can sign any
messages as long as the program approves
them using my private
key but what you can't do because it's
been OB fiscated is you can't learn my
private signing
key because that's the that's
the the whole point of obfuscation you
don't learn anything about F other than
its inputs and it out its outputs so you
feed in a bunch of good messages you get
a bunch of valid signatures you try to
feed in a bad message well there's
nothing you can
do if you had the real the original
source code to F of course you could
just read it and reverse engineer it and
see oh look there's the there's the
variable called private key and well now
now my signature is
useless but if I can obfuscate
that well then I have this program that
more or less acts as an autonomous agent
on my behalf
I can send the program out into the
world and it can do anything for me
whatever I ask it to do and I can trust
that that the data inside can't be
breached you can't learn my private key
you can't learn whatever else I
have in this magical cryptographic
orb so that's the that's the good news
with program aisc the bad news is well
we don't quite know how to do it
yet there are obfuscation protocols out
there that are proven
secure that would run in I don't know
millions or billions of
years there are proposals out there that
are definitely faster that you can
Implement that will run and terminate in
a real amount of
time but we don't really have any reason
to believe they're secure and we well we
kind of suspect they might not be their
protocols from a decade ago and they're
all broken now so this is um an active
area of research there's a lot of new
cryptography that's come out in the past
think that there's a lot of promise for
alisation in the near
future but as of now this is the pipe
dream this is the Holy Grail at the very
top of our cryptographic primitive
pyramid anyway I'll stop there and open
it up to questions
all right thank you
Brian looks like we have a question of
if computation is not a problem what
what would the world look like with ZK
fhe and
MPC what would the world look like if we
could just use these things and
computations not a problem and we can
deploy them in
practice well it seems like it's a lot
easier
to manage data and
computation so when you had the the
internet the internet gives you very
strong communication you can communicate
with anyone anywhere very very quickly
in ways that we couldn't really imagine
until until it happened so you have very
reliable
communication with uh with this
technology zkf MPC all this stuff you'll
be able to build programmable fun
functionality on top of that
communication and it's hard even to
imagine what you could do with
that Beyond you know these vague visions
of you know maybe some we could
hallucinate some sort of server right we
could do things on a peer-to-peer level
do computations peer-to-peer without
having to depend on a centralized server
a centralized service and the apis it
provides
right on and yeah you mentioned the frog
game if you folks haven't yet highly
encourage you to go check out the Frog
Zone on the ground floor to see one of
these implementations in action of
actually using MP fhe to hallucinate a
server and actually allow people to play
a game where these programs are
Computing on this private State um
really incredible I'm curious yeah like
maybe on just the MPC and fhe side what
do you see as the current big challenges
like is it on the research side is it
just engineering and optimization or you
focused on performance so the problem is
performance and I think we need more
research it's not it's the sort of place
it looks like ZK like zero knowledge
proof looks zero knowledge proofs looked
maybe 10 years ago there's a lot of room
for research to improve performance I
wouldn't be surprised at all if you know
a few years of of academic effort got us
a tenfold or a thousandfold Improvement
in performance that makes a lot of
things more
doable
exciting um and another question would
IO be imaginable on
ethereum um and if so yeah what what
implications might that
have what would you do with I aha you
would so how would you you combine IO
ethereum you would I guess you would
take a program and obfuscate it and put
it in a smart contract and so now you
have a smart contract that can act as
your autonomous
agent so potentially like you mentioned
like storing a private key on a smart
contract might enable some use cases
that for developers out there who may
have tried to build some applications
realize oh wait I can't just put this in
the public State because uh people might
take my money um seems like it enables
some interesting use cases there for
sure cool well um yeah Brian and the
zerox park team like I mentioned they'll
be down at the Frog Zone encourage you
to go check it out get in on the the
Frog crypto Mania or or talk to them and
ask questions if you want to learn more
but thank you very much Brian thank you
you
is e
now e
okay welcome back we got our last talk
before lunch another presentation on the
applied cryptography track we got
Richard from zerox Park one of the
people behind the Frog crypto Mania
that's been happening this week um
you're going to want to stick around to
the end I hear there's a nice little
frog surprise so get excited and stay
tuned let's give it up for
Richard hello hello thanks Sam um as as
you said there's going to be a bit of a
surprise for yall I know it's getting
close to lunch towards hungry times so
we'll make sure it's is worth the wait
um yeah I'm Richard I work at zerk Park
and I'm here to talk about zoo pass but
before I get into zoo pass I actually
want to first talk about ethereum um we
are an ethereum conference and one theme
that we've seen popping up over you know
the past I think few years especially
and few months even more specifically is
how do we get to things that people can
use right not just interesting ideas in
theory but um you know as vitalic says
this bog post this is a decade where we
actually have to build things that are
useful um and I think there's been a lot
of really exciting directions in the
staple coins the prediction markets uh
defi in general right I think um that
kind of world has been really exciting
to see things come to fruition uh but
there's this broader world of you know
uh the promise of ethereum Beyond just
you know more ways to use money more
ways to increase Financial access
there's this vision of uh Computing
being a different sort of Paradigm
because of decentralized Technology
because of cryptography so I think
that's where I want to focus on and and
I want to approach specifically this
problem from uh the usefulness lens and
I think one interesting thing about uh
Devcon in AUM conferences is that um
conferences can serve often times as
ground zero for new technology
breakthroughs um their early Glimpse is
what's possible you have a bunch of sort
of really bot in excited people you know
caring a lot about coins or frog hats
right and it's a chance to sort of show
what you can really do um in a short
amount of time and two examples that
people might know of are one is this uh
Cornell Doug Engelbert introduced modern
Computing the personal computer the
mouse the spreadsheets it was all
hard-coded there was no like actual
product but it was a sort of vision for
researchers at Xerox Park and for um
Bell labs and these folks to sort of
actually innovate and build the thing
that we now know as uh probably the most
important industry the past 50 years um
the one on the right is Twitter at South
by Southwest in 2007 just another
example of like how um we've seen early
glimpses of social media and it's
changed our lives for better and For
Worse um so I want to start with this
prompt which is what did going to an
ethereum conference feel like 5 to 10
years ago and uh I actually wasn't part
of the ethereum ecosystem 5 10 years ago
so I'm just kind of guessing but let's
let's play along um and let's target it
from the technology perspective of the
conference so you're at a conference uh
there's a few things you know features
or products that are important right um
there's ticketing you need to be able to
get in there's Communications I want to
meet people I want to sort of expand my
network I want to sort of hear what's
going on and I want to go to talks right
um and you can roughly map this out in a
data way with you have all these sorts
of like objects for example you have
your tickets in this ticketing server
you have communications and messages and
other you have some other stuff going
with talks um it's pretty standard sort
of uh thing you do for any kind of web
application um and and one thing I want
to explore this is you know five 10
years ago what does it feel like in 2023
I chose last year because this year's
you know a little different
um but it's basically the same picture
um you know like the one thing that's
changed is oh now we can you know buy
tickets with ethereum right uh and
that's pretty amazing and Powerful how
that happened but it feels like we could
do be doing a lot better right not
because we're trying to like make the
best conferences because conferences are
where um folks from the community should
sort of see what's going on at the
bleeding edge uh yeah so basically
nothing has changed much and you know
what could it look like in the future
right what could the reality of being
part of the ethereum community look like
in the future um this is a bit more
complicated a diagram but essentially
you know all those pieces of data right
that are being held in servers oh why
aren't they being held by me right and
and not just for you know privacy
reasons but also for the fact that I can
Port them across different applications
um you know applications themselves
could live as smart contracts right be
publicly auditable be composable all
that good stuff um and I I think here's
a here's my take which is like if we
can't do this um if we can't actually
just run the biggest and most important
event on ethereum in a few years like
something's really wrong right and I
think that's sort of a red flag almost
um and and here's one exercise which is
like what would it actually take to run
ethereum conferences on ethereum right
uh you know first off what are the
benefits I think most people here are
familiar I won't sort of spend too much
time but you have all these sorts of
like data ownership composability
permissionless um everything is
verifiable right and this is powerful
because you can have these sort of new
behaviors that emerge um that are only
possible when you have very strong
guarantees now what's holding us back
right um yeah basically all state is
public that really sucks you can't
really have any sort of of um you know
secrecy or privacy that you want sort of
just because you want to build you know
organizers don't want I don't want
somebody else knowing my information
right it's not sort of a ideological
thing it's a very practical thing um
most of the world's data still on web to
it's not very portable yet uh building
and solidity is still really really hard
right um and uh you know computation
expensive and high latency I mean rups
make this better uh the you know
resources in development have made the
third Point better but I think we're
still it's still pretty tough to build
an actual like high load application on
ethereum yeah so I think it's at this
point it's still too high a friction to
go all in but we don't have to go all in
right I think there's this tendency to
like be like oh it has to be fully
decentralized or private or it has to be
nothing but I think there's there's ways
to sort of like 8020 this right um and
the question is like how do we get to
sort of 80% of the
benefits there's a lot of clicks um with
only 20% of the cost of you know using
this Tech right um and one thing that
I'll I'll note uh is that things like
zup pass among other you know really
great applications in the past few years
have made this more possible right and
through uh different types of you know
through certain data formats but also
through encouraging a certain type of
application
um so simply data is not stored directly
in ethereum however it's easily portable
to ethereum because it's cryptographic
right and not only is it portable to
ethereum but it's portable to basically
anything because you just need to be a
person or a computer that speaks math
right it's kind of the universal
language um and just to kind of go
through some vocabulary uh my colleagues
will probably inundate you guys with
these phrases more later on but a pod is
uh essentially you can think of as a
Json that has some proof attached to it
it's a statement about the world um zaps
are these things we're calling which are
applications that operate over pods and
they connect to your zup pass which is a
store for pods um and stores and also
manipulates and these are all stored
locally uh you might hear this thing
called a GPC it's basically it stands
for general purpose circuit essentially
it's a kind of a ZK fpga um where you
can sort of configure a circuit or a
proof through Json rather than having to
like write circom or you know learn uh
functional programming and um you can
make proofs that are really really
efficient like two to three seconds on a
mobile
phone okay so some examples um pods so
your Devcon ticket which I'm sure all of
you uh used maybe struggled with a bit
but um and other sort of uh events zo in
the zul ecosystem which is where zoo
pass got its name from for example Edge
City Zoo connect which was before Dev
connect last year your frogs and other
pods from applications like questions
and answers like mircat is one example
um which will be used at the end of this
talk that QR code to write there um in
terms of zaps we have uh there's just a
lot of stuff on this page but briefly
right there's um things that help with
communication like the telegram there's
things that are just fun games in their
own right like frog crypto
um and actually have their own
extensions right like the necklaces um
these guys and uh you know there's some
apparently there's a game where we can
juice the Frog and put it on chain um
just hearing all kinds of stuff now and
then uh also faucets right so I think
the meong faucet came out and that's
using Devcon gating um so all kinds of
different things are highly you know all
kinds of really complicated logic is
highly flexible because you're just
you're essentially just writing a
typescript app that checks some
cryptography rather than having to write
a whole smart contract um and and given
these sort of like new technologies and
capabilities right you know what does
feeling a Devcon go what does what does
going a Devcon feel like um it feels a
lot like well I have some application
that stores my own data uh it's issued
by you know trusted services like Devcon
but I can now use that across a whole
bunch of different zaps um I can get you
know and not not just tickets right I
can get my frogs and those frogs are
useful for all kinds of like extension
apps the juicing stuff this another one
where you can sort of like put your frog
in a lab um there's like more gated
chats right uh I think this is just very
very fascinating and interesting um of a
way you can sort of engage with an event
uh because you have this technology
where everyone has uh software that can
process pods they can make proofs and
developers can build applications that
interact with
these okay so here's where we get a bit
more experimental and um if we project
this with you know High uncertainty bars
because uh no one can know the future
what does this look like what does this
mean Beyond just okay it's a cool fun
conference experience well I think that
um you know if we sort of just literally
take each of these boxes and do like the
more serious version of it right checkin
is basically how uh you know Customs or
traveling across any sort of like High
um you know high stakes reputation thing
where you're going through and you're
checking that you're you are who you say
you are that's essentially what's going
on uh with ticketing right and it
carries over to the high stakes things
like I want to enter a country or I want
to like do something that's you know
highly restricted uh messages you know
every email has a deim signature and
that can be portable on chain or they
can portable within this sort of
cryptographic environment um voting uh
that's been said a lot before so I won't
go into it you know faucets right what's
the sort of bigger version of a faucet
or you know a bank it's it's it's an
actual bank right and then I think this
direction of apps building on apps is
reminiscent of um two things one is like
in the early Facebook days there would
just be a ton of like Facebook games
right I mean same with Twitter there was
a Twitter API and there's like all these
kinds of like aggregators you know like
or there' be like you know check my face
Instagram followers do some sort of like
you know query over them I mean Tik Tok
there's like the remix Behavior where
someone can sort of like take a Tik Tok
and like build on top of it and you get
sort of like recursive Tik toks like six
down and I think like these kinds of
things are are really fascinating um I
think you see in defi as well right but
it extends far beyond like derivatives
and financial
applications okay so this is all cool um
but how do we actually get here right
cuz uh I think like we can all dream and
sort of Imagine right but I think what's
important is like what what needs to get
done um and we have three main ideas
right now and directions that are I
think pretty concrete uh so the first
one is we just need to get better
technology right um there's been a lot
that's changed so zup pass was first
launched in 2023 it's built in six weeks
uh which is crazy there were like all
kinds of crazy stories that happened
from there but um basically was built
that assuming that hey we have what we
have at March 2023 and so many things
have changed right so pods was not even
a thing until early this year and now we
have um a lot of developments in
recursion which have made so many
different kind of things possible um you
can basically make proofs of proofs of
proofs in sort of arbitrarily long you
know arbitrarily long chains of proofs
in under two seconds on a consumer
laptop
and we have not adapted zath yet to this
new paradigm um and you know that gives
us the ability to also work with data
that's not so nicely like ZK friendly so
like ZK email uh ZK VMS they just take
they take really long and they're just
not very feasible on phones right now
but that's something we can actually
just solve given how much uh things have
progressed over the last
year yeah I think we want to continue
improve performance um we we have uh for
example we've done a lot of open- source
fixes and Feature work with snark JS and
semaphor which um are two of the
libraries we depend on and a lot of it
is because uh both of these libraries
have not really experience the level of
load that uh before something like zass
emerged right like um I'll give you one
example which is there's this memory
leak issue in snark JS that caused
people's screens to freeze up but it
only happened when when they tried to
make really big proofs and it was a
really you know simple bug that we went
we just sort of it was allocating too
many pages but my point is like there's
a lot of loow hanging fruit because a
lot of this stuff has not been tested in
production even though these are sort of
like the you know the classic libraries
you use um and there's all kinds of like
new updates too there's delegated
proving which seems to be uh the
direction of a lot of the future of
client side stuff um essentially where
you're blind it on the client and you
set the server to make it
cinct there's um new apis like web GPU
uh Native proving which has been
exciting um and more of a reason to
actually get a mobile app right so
things like M proo and explorations of
alternative kind of zoth or pod clients
um for example there's one experiment
we've been doing on you know Mac native
with a Mac native app uh and that allows
us to do a lot more like complicated
proofs than you can on just your zoo
pass which is ultimately Bound by the
web browser and your
phone okay yeah we need to get more
valuable data into this ecosystem as
well right we can't you know frogs are
fun uh conferences are fun right but it
can't just sort of stay in our little
bubble we have to really like we have to
actually go out there engage with real
world data right um and you know I think
there's there's passports have been
talked about but there's all kinds of
other data that's highly valuable right
um and I think this is where kicking off
conversations with Builders who are
working on this sort of like import
problem right how do you take data
that's either cryptographic or not and
import it into a format where it can be
used in this way right um TLS notary and
ZK email I think are the great examples
because there's just so many emails and
uh you know websites out there but I
think what we want to focus on is how
can we sort of take these uh you know
new imported data and like find sort of
a use case that makes sense um and then
also let devs build further applications
on top of this right how do we enable
like the Frog crypto of something Beyond
Devcon or an ethereum conference right
that's still an open question that uh I
think will be very interesting to
solve um yeah I think that's where like
Partnerships with universities
governments financial service providers
I think this is still um it's starting
to get to the point where this makes
more sense right um you know there's
there's like there's a lot of cool stuff
you can do at universities right people
want to make apps uh at you know the
stanfords and the sort of berkeleys of
the world and um they want to make
social apps dating apps and these this
is sort of like a great uh way to get
off the ground with a lot of these um
you know new technologies we can sort of
work with portability of social media or
ethereum has been one but also like
farter Blue Sky X um there's all kinds
of directions and this is like not a
complete list by any means
wrong button cool and then last is we
want to empower U this is Devcon we want
to empower developers to build the most
interesting apps and the most powerful
ones so um you know here's an example of
how you can sort of push insert a pod to
somebody zoo pass in basically five
lines of code um we try to make these
things very simple we try to make these
things very at the end of the day we're
we're pragmatic and we we want to ship a
lot of things um so I think this has
been uh a really you know we spent some
time basically in the past few months
rushing together in SDK that you know so
that someone can actually come in and
build a zap without much guidance um we
will have a workshop on
Friday uh where we'll go over and just
literally build it together you can
build frog battling frog you know dating
or like whatever kind of app that that
comes to mind um yeah and and crucially
I think no cryptography experience is
required because a lot of what we're
doing with these libraries is focusing
on how can you just describe the
behavior you want and then we'll take
care of the actual
implementation and um yeah there's some
documentation p.org it's six letters
easy to remember um and we have a
telegram group as well we haven't shared
it too much publicly because we're
worried of spam but I think everyone
should join everyone should um you know
ask our developers with questions and
you know you know help us help you guys
figure out what to build
um yeah some upcoming sessions from my
colleagues and then uh crucially
tomorrow we're going to have a full day
of programming there's going to be some
cool Keynotes in the morning um and then
workshops in the afternoon right so that
workshop with uh building zaps with Pods
at
um and as promised here is a froggy
surprise I'll just let you guys figure
out what's going on and that's all
all right thank you Richard excited to
see what zaps all you folks build out in
the wild um looks like we got a couple
questions when native mobile
app yeah great question um I think we've
probably said uh soon like too many
times um I think we're really excited
for you know uh how fast you can get
with Native proving um rapid snark and
mpro have just been you know really
exciting to see the progress I think
there's a few things um most of most of
it is honestly just you know we're we're
a small team and we uh you know have to
sort of I think we had a lot more people
if we had um a very strong sort of like
you know uh mobile direction that would
be something we we certainly do I I will
say like you know 2025 is a great time
to like we we have already explored a
native Mac client um so I would be very
surprised if there's no native app next
year but don't don't quote me on
that um looks like a question around
breaking down parts of the app um parts
of z pass like built on Primitives like
snark js on
semaphor um versus what is driven
directly by zup pass yeah that's a good
question so um I'll separate snark JS
and semaphor so I'll talk about semaphor
first um semaphor is uh at least the
latest version V4 is essentially a key
pair uh which is super useful for us and
essentially a
semaphor uh identity is a zup pass
identity they're they're Ono one um and
it's what you use for signing pods it's
what you use for uh also like you know
if pods are soulbound to you right or
like Watermark to you they put your we
put your semaphor public key in that pod
to signify that um snark JS is used for
uh proving it's um mostly for if you
remember
gpcs uh it is I think still the fastest
web-based library that we've found and
to be reliable enough um although we're
very open to sort of change it it's
crazy because it was built mainly for
educational purposes but now it's being
used for like huge use cases um yeah
yeah and a lot of the rest of zup pass
functions similar to a traditional web
app um I think the the pods being stored
locally rather than being stored in a
server is a really big
difference and looks like curiosity
around you know zup pass building this
data wallet is there any plans for
association with an etherium wallet I'm
guessing and or ZK email like like
functionality or Authentication yeah
we're really excited about um we've been
really excited about I think all of the
sort of zkx you know movements right um
TLS notary had put in this as well and I
think like we finally have the
technology to actually do this it's it's
pretty crazy but um uh with with these
things we're we're terming pod to right
we essentially anything that has a
verification function um which is any
cryptography really can be put in a zoo
pass so I think this is something we're
we're going to um yeah it's going to
happen and now we finally have the
resources to do it love
it um got some more questions sounds
like people should show up at the
workshop tomorrow uh but curious
integrating pods with traditional web 2
stuff what that might look like so one
interesting thing that um happens for
frog crypto is that we created this new
data form format called a pwt it's a pod
web token um JWT is Json web token so
pod is essentially a superet of Json it
can also be serialized to other formats
right but uh anyway as in the side just
to point out like that um it's very easy
it's almost like asking is Json um you
know compatible it's it's mostly a
theorization format um with some opinion
this around like how do you verify the
data and but um yeah these are all like
very easily Poss because they're
cryptographic sources of identity at
least jbts I think um oath and I'm not
familiar with oidc but there are ways to
Port import those over to cryptographic
data types for example with
notaries one last question I see hi can
you go back to the Frog QR code page
again please and thanks
I mean I I don't think I can unable to
do it unable to do that it was there it
was gone those frogs are slippery yes um
all right thank you very much Richard
yeah encourage you guys to go check out
the workshops tomorrow to learn more
let's give it up for
Richard I think that is is for lunch
we're going to take a 1-h hour break
we'll be back here at 1: p.m with with
more programming so enjoy lunch see you
guys soon
ch e
y
h
what
I
now
for e
that's
to
all right hello everyone good afternoon
I get everyone seated please so next we
are going to kick off this afternoon
with a very interesting panel on Multi
party FHA for melti party privacy and
our panelists are hopefully I can
pronounce their names correctly Edward
gup sheep
je Jaya and Veronica let's welcome our
panelists onto the stage
all right let's go ahead and get started
welcome everybody hope folks are not too
sleepy from lunch thanks for making it
out here for the multi-party fhe for
multiplayer privacy
panel to introduce things I'm gub sheep
and I will be our host of the panel for
today and and I'm delighted to introduce
our three panelists as well three
incredible cryptography Engineers who
have been working on various topics in
programmable cryptography over the past
several years we have with us today joh
maaya who is the uh founder of gaus labs
and the creator of the Fantom Zone fully
homomorphic encryption Library we have
edu a researcher and engineer at psse
who was one of the first contributors
and developers on the zkm project that's
the original Z K evm project and we also
have with us Veronica an open source
developer who has worked on everything
from consumer facing crypto products at
coinbase to Frontier cryptography
prototyping alongside organizations like
the EF and zerox park so the title of
this panel is nominally about
but as with many things in this fast
moving world of programmable
cryptography and as you might have heard
if you came to one of the other
programmable phography panels earlier in
this week this term is largely a
placeholder name for a set of Concepts
that we don't fully know yet how to
describe or how to use or how to even
think about yet necessarily in the in
the clearest ways but I want to start
off by introducing this term itself
because it's sort of been one of the
best anchors we've had emerge uh in the
past year for describing um some of the
things that have emerged from the recent
world of research and development around
these Concepts so maybe for starters
I'll direct the first question to Jay
here can you tell us about mpf so this
isn't a term that as I understand this
is not a term that actually is
conventionally used in the academic
world of FHA and what do we mean when we
say multi-party FHA you know does that
what distinguishes that from fully
homomorphic encryption how do we sort of
think about that prefix in this
context H well the way I would think
about MIP f is it's a way of doing
multiparty computation using fully
homographic
encryption and the advantage of this
approach than taking the traditional
ways of doing multiparty computation
is in this case the computation is
offloaded to the server if you take a
traditional approach to multiparty
computation let just say SEC Shar in
scheme or Y
gobling you would have to pay a
bandwidth cost
it is not the computer that is bot like
in that case but you have to you know
upload things and send to the other
party
um the difference between multi-party F
and the normal way people think of f uh
which is fomor of encryption is that in
in the single single party F where it's
a single player game a single person
holds a secret key and then encrypts
everything sends to the server server
has some function that it usually wants
to keep a private let's just say neural
network and the server would evaluate
that neural network and send the output
to the client back and the client can
decrypt it but in contrast to this in
multi-party FG the secret key which was
just held by a single client in single
party FG is now split among multiple of
them so that individually no one can
decp the artw only when all of them come
together uh they can DEC the output and
that's the difference between single
party F and multi party F cool so
multi-party FHA somehow
exists in the intersection of the best
of what we want out of multi-party
computation as well as fully homomorphic
encryption yes because it's sort of like
trades of bandwidth cost that the client
needs to pay in traditional MPC with
compute so you have higher compute but
we know how to solve higher compute
instead of solving a higher bandwidth
requirement
problem cool so maybe one thing that I
also want to dig into a bit is this idea
of so we have this contrast with MPC
which is that we can take the bandwidth
costs down um in terms of the contrast
with FHA as I understand it a lot of
what's going on with trying to introduce
this term uh or when we think about
related things like obfuscation is to
also catalyze a mental model shift and
how we think about what FHA is good for
so I think FHA is actually a pretty new
topic for um all the panelists by new I
mean on the on the time scale of kind of
one to two years but a lot of us have
heard about FHA as this technology that
has been you know this wild DARPA
project for a very long time how did you
guys think about FHA before you started
embarking on the most recent research
journey and how has that mental model
shifted now in the context of
mpf uh yeah I think like when I first
heard of FH it's like about 10 years ago
in college and then uh yeah and then
like uh people say like okay I the first
time I heard about it I think it's magic
because for most people when you think
about uh encryption uh you you think
about hashing you think about okay you
put your input are it's like you come
out with like a a string and it's kind
of garbage and now you kind of like have
a piece of uh string garbage and then
you add to another piece of string and
garbage for some reason it preserves
like the addition you can somehow
decrypt it and then get the result so
for me it's kind of like really magical
uh but around that time people were
telling me like you know it's like a
million times to a billion times slower
and then you know I just feel like it
probably wouldn't be relevant for me as
a software engineer I just moved on
never thought about this until like you
know we uh started experimenting on
stuff this summer like build on top of J
Library phom Zone and then I saw okay
this is something actually possible and
then you can use it for multi-party
computation so yeah it's like a really
magical experience for
me yeah I think I also learned about FH
first around eight or 10 years ago just
like Veronica and it also felt quite
magical but I found the technical side
of things more
interesting uh because if you think
about having encrypted data and being
able to do arbitrary operations on top
of that while preserving the data sounds
really awesome but but then on terms of
applications of traditional FH I think I
got less excited about that because it's
a lot of about offloading computation
from like a weak device but in my
opinion like these devices are no longer
weak like we get more power every year
on our phones so my first question is
why cannot just run the same competition
on my phone or maybe not today but in
one year maybe I like I think people are
trying to run llms on phones right now
so to me there was a paradigm shift with
the introduction of multi party which is
it's not something that you can uh it's
not just of loading computation that you
could already do it on your phone and
then you do something to accelerate now
it's Computing on private data from
multiple people which is something that
you could not do before so that was
pretty awesome yeah so to summarize it
kind of sounds like there's been two
major updates in the thinking in the
last couple years the first is more than
just being this crazy theoretical
technology someone can actually sit down
and write an FHA Library write FHA
circuits on top of that um it's no
longer this Pine the sky thing and the
second thing here sounds like our
understanding of what FHA is even good
for or useful for has shifted you know
with the introduction of this
intersection with MPC and the idea that
it's not about delegating computation
but actually about multiple people
coming together to to produce some joint
output so maybe you know I'm curious if
someone could give an example of both
maybe just to contrast what the world
looked like when I remember sometimes I
would see a popular science article
about FHA 10 years ago and there'd be a
certain flavor of application which I
agree with you Ed just was not so
exciting to me but now the things that
we're starting to see people prototype
and build very early on on these systems
is qualitatively different so I'm not
sure if any of you have some examples
here or can speak to that differ
one really good example is like out
there at the Frog Zone um where you have
uh you have a global state in which each
party has their own private state that
no one knows um so you have a global
state that sort of like composes of
private States coming from multiple
people which is kind of interesting
which we did not like which we cannot
have with
normal well I wouldn't say normal but
like things that we now consider normal
like zero knowledge proofs uh um and so
on and so forth um suppose do you guys
have any other interesting new case yeah
it's not a particular use case but I
think a lot of people have observed that
smart contracts in ethereum work with
public data and then I think many people
learned about ZK and thought can we use
ZK to have private smart contracts and
the answer is most of the times no
because we need private shared state so
there are many applications where we
want computation on private State like I
don't know uh Unis
swap um maybe there are particular
solutions that can be built off ZK but
they need to be tailor made for the
particular use case but multiparty FH
gives you a general framework to build
these kinds of applications with shared
State yes so for me um mpf AG it's like
changed the for under users like I think
change like my entire view about how I
think about data so like with my mpf
like my default is like going to be I
want to share my data more uh so just to
give an example so uh I normally when I
meet like strangers I feel like very
awkward and very anxious I don't know
what to talk about I just don't know
like what to say to those people uh I
know some of you may not think so but
like a lot of us do uh so like uh so one
thing like in the past few days like you
know just going to those After parties
I'm just keep on thinking like you know
what if I can just like upload all my
data my interests the books I read like
all my thoughts my experiences like on
server somewhere and then like you know
like everywhere else also upload their
information and when I meet a stranger
like I meet brand and then it just pops
up say like okay you guys both
interested in this or like you guys are
have different opinions on this so I'm
like okay maybe I can talk about this so
I don't need to think about what to talk
anymore uh I think like in traditionally
like before like uh mpf AG like if I
want to do this I mean I have to write
the code of course but I still have to
convince people to upload all those
information uh to my service like how do
I trust people to do that like I
probably need to start a company and
like trying to uh build a brand
and uh like maybe make myself like a
Facebook or Google and then people start
to upload their data uh and then like
you know like when I have those data I
might not want to have all those data
because it's kind of like scary like
what if I leak people's data uh and then
I have to hire a bunch of Engineers to
like secure the data and then you know I
needed to have money so maybe how do I
how do I make money like out of this I
might have to show people ads so you
know like a lot of things can go wrong
like from there uh but with uh
multiparty F I didn't need I don't need
to do like any of those things I can
simply like write my code okay and then
like we can do this kind of uh matching
or like a suggesting recommendation
thing like peer to peer uh without going
through all of those things I think it's
just going to like open a lot of like
different use cases yeah so it sounds
like one of the underlying themes here
with what you all are excited about with
mpf is idea of multiple people coming
together to jointly compute something
and without needing to rely on on some
other strategies and you know there's
this first strategy of we can have
someone build a company build a business
model build a trusted brand around
collecting everybody's data and doing
those joint computations and there's
some problems with that and then edu you
mentioned something interesting as well
which was like well you know we have
ethereum we have Smart contracts we have
ZK maybe a thought could be can we can
we combine these tools together to uh
get what we want and as you
mentioned this doesn't turn out to be
enough and what I want to do actually is
a lot of the folks in this room might be
a little bit more familiar with ZK than
FHA and I know for all of us we kind of
came into this space as well through the
ZK world as well
um what is the right way to look at
comparing zcan FHA what what can they do
what can each of them do that the other
cannot and
why is it the case that actually in the
blockchain world we've talked so much
more and seen so much more progress in
ZK over the last five years than in
these other programmable encryption
Technologies I think one of the main
interest from the blockchain industry in
Z has been focused on scaling not on
privacy and there's a lot of economic
incentives to solve the scaling problem
because you can have
l2s uh that are pinned on ethereum and
Within These l2s it's easy to extract uh
to get to monetize them because you get
fees but on the other hand
um yeah well that's the answer I have
why the blockchain space have focused
mostly in ZK and I think even in the ZK
world we have seen more uh scaling
development than just privacy
applications on ZK that's my impression
so probably um mpf gives you a different
angle and we still need to explore and
convince people why this is
nice I would say the programming model
for multi party F still kind of un
explode um we were trying to build this
frog zone game with Brian Z spark people
and uh we we came AC a lot of issues
while doing that as well you know we set
up five Serv was just for the game by
the way uh oh we we just set up five
serves for the game by the way so the
programming model for multi party f is
still bu on explode it's not as clear as
ZK at the
moment the difference is that um I can
point a few differences for
example uh it's not all in multiparty F
I suppose the memory access model
becomes problematic because the moment
you of leak which part of the memory
you're reading um it's sort of like
violates the law of you know privacy
like you cannot do that so you have to
pay you know linear amount of time to
actually retrieve anything from the
memory so that becomes a problem um what
becomes better is that now you have um
instead of just thinking in like single
player term in ZK where you have just
one person generating Witnesses on their
devices and then just posting the proof
somewhere what needs to be done in
multiparty FG world is like you have to
consider multiple people and they have a
shared State and a private state within
that shared State um and that is sort of
a switch which took me some time to
grasp over I would also quickly answer
the second
question I I somewhat agree with um edu
that um there was there's a huge
economic incentive to build um use Z for
scaling but I also think that
uh uh blockchain world people are not
that comfortable with uh so so usually
the people that are using multi- party F
or like threshold fig in certain
scenarios at the moment from blockchain
they have some they have something
called God servers these are the servers
that hold these secret shards that we
usually put put on the
clients uh blockchain people are not
that much comfortable with it um
and that is the tangible part of FG that
is like what is possible at the moment
and uh what we need to do now is sort of
like figure out a way around that
problem which is more like not tangible
at the moment like people are not able
to see a way around it which inevitably
leads to something called program
officiation which we can talk about
later as well so I think that it's not
just about like there's a huge economic
incentive it's also because um getting
around this problem of God ex servers
holding the secret shards is uh is is a
is a challenge it's more like a
theoretical question at the moment than
you know within the reals of like us
right out of college being able to do
all these things um so there's also a
switch over there so maybe actually one
thing I'll prompt here as well is it
sounds like the reasons that you guys
are mentioning are related to on the one
hand there's the economic incentive for
blockchains that drive ZK forwards or at
least ZK for scalability forwards not
clear yet how far it drives ZK for
privacy and then on the other hand you
you know there is ultimately this
technological problem of can we make uh
the idea of secret shards that need to
be held by a bunch of people more you
know palpable to different communities
that could adopt this technology but
what that also kind of signals to me is
there's a little bit of like almost like
a social or a cultural aspect to that
what I'm curious about also is from a
technological perspective or a
theoretical perspective is there an
inherent reason why ZK needed to happen
it actually the case that you know we
think it's more of a social economic
incentive that sort of thing that's
pulling this forward in other words
could FHA is there actually just a lot
of lwh hanging fruit that's waiting to
be discovered or is FHA inherently
harder
somehow I would say that with
Z I think you need to solve a single
piece but with FH to be usable you need
to solve FH
but verifiability and figure out a way
to spread among many users so there are
more
pieces and maybe it's harder to solve
all these pieces together and while we
don't solve these pieces we can have
some examples or demos but maybe not
quite get there to this final solution
that we
envision I I would say that uh
uh in in the in the
more uh Web Two World F has received
more attention than ZK um than our world
where we sort of like
inhabit
um I I I I I'm I'm not in a position to
say whether ZK is harder than FG or fig
is harder than ZK or so and so forth but
I would say that
um it's more like a social thing as well
um the cultural thing of us carting
about this tool to make sure that we're
delivering libraries and building tools
so that people can use it easily which
is not often the case in the traditional
world like not the traditional like web
to World whatever that
is did you have anything I saw that you
were picking up your mic a bit ago oh
yeah uh so I think like I'm not too sure
about the theoretical which is harder uh
but from like app ation developers point
of view I feel like ZK there's like less
it's more like a non-interactive it's
like okay you have like a approver
approve a piece of something and then
you can give it to the verifier and then
for uh mpf AG there's just a lot of like
those kind of participants and
interaction happening and uh as of now
like when we decrypt the like you know
like the decrypt the output they still
like like aliveness so that's like a lot
harder to build like application around
uh so yeah but one thing is quite
interesting is like uh when I build uh
like ZK applications normally uh I would
like you know make the data hiding the
data by default I would actually like
just by default hide data but with M uh
mpf AG like I think like as an
application developer you kind of want
the user to share as much much as
possible so that's like another
difference yeah U one more thing would
be that I I sort of uh so there's only
one way of doing F at the moment if you
know about it like there's just like
luses and ring Ling with erors that
you're familiar with and you can only
use that for FG there's somewhat hints
that probably theoretically f is much
harder than ZK just a conjecture no no
sort of like commitment to that um but I
also think that it's more like a
cultural issue where not we not s
probably we are not coming with new
ideas and probably if we sort of like
enforce us a lot of people are paying
attention to this thing and find useful
then probably we can come up with new
ideas like the way we did for Z like for
a long time we just had God 16 um and
then you know UPC come plonk U and so
and so forth
uh there's a lot of really great
insights there I guess one thing that
actually I had I had not considered was
the role of interactivity here so
interactivity played a huge role in
actually making ZK snark practical as
well you know the idea that the way a ZK
snark or a general purpose zkp used to
work was you would have these two
parties and they would perform some
interactive protocol between themselves
we actually did have general
purpose zero knowledge proofs that were
interactive before ZK snarks came onto
the scene it seems like the really
important thing that actually made this
practical for developers is you have
this one-hot nature where I can generate
a proof I can publish it publicly or I
can send it to you and you can verify it
and we can get on with our application
so so you know it makes sense actually
that the nature of interactivity here
just makes it so much harder to reason
about you now need to do this
coordination problem amongst all the
different parties um I think that's a
super good Insight um I'm curious to
double click into J some of the
directions you were just gesturing at
from the theoretical
perspective what can we carry over from
what we know from I guess the first
Branch or generation of programmable
cryptography that we have really advaned
what carries over from ZK into fhu or
are we in a totally different world how
do we how do we think about development
in this
space uh is anything even relevant or is
this like we need to go off and have
some completely different kind of
cryptographer think about some
completely different kind of systems uh
I would say that the programming model
somewhat can be transported over um I
when first starting with f I was having
enough information about bir ZK did help
me sort of understand a lot of things
but The Primitives are entirely
different um you're working with lates
uh which are much simpler than electric
curves so that's a that's a good point
um there less
ways I do not know but like I think
there less way to shoot yourself in the
leg with
lisis because you know now we have
standardized parameters and so on and so
forth there are more ways to shoot
yourself in the leg with the altic
curves
um at least on the base primitive
level
uh ltis is sort of like uh give you
they're much more they give you more API
probably because of which they give you
when I say API sort of like you know I
think of hardness assumption as API
giving me things to manipulate um I
think uh plates give you more structure
in terms of like the API which gives you
f eventually um and and
um uh what else one thing about elter
curves is that the the size of any cyhex
that you encrypt using you know the
normal cryptography that we know is like
very small ltis has blow up everything
like the data that you sent over the
communication is is is way bigger than
the way you would do it you know maybe
if it's by some commitment or something
like
that H what else did I miss
anything yeah one thing I'm curious
about also is is you know in when we
sort of bottom out at the Z in terms of
the ZK performance Story We bottom out
in things like uh ffts or you know fast
forier transforms or msms multiscalar
multiplications what do we bottom out at
least in the current generation of FHA
schemes are any of those similar does
any of our acceleration work Hardware
work think ways of thinking about parall
parallelization do any of those carry
over yeah they do um because um all we
are working with is polinomial um and
have thef polinomial and zqf polinomial
and you have to multiply these
polinomial which requires something
called fast for your transforms if you
were to do them efficiently and I
suppose that really applies like the all
the work that is happening at least on
the GPU side for ZK sort of ports over
to I would I would rather go ahead and
conjecture that it's directly ports over
to the FG world because all of them are
working over friendly primes like
Goldilocks or all of them are probably
not working with f50s but like probably
mercen prime or logs and so on and so
forth so I think that is completely
relevant to the fu world as well cool so
that's a bit on the theoretical side
we're now one of the big jumps in the
last really half year is we've started
to move from if you want to engage with
this kind of Technology you purely have
to engage with it at the theoretical or
at most cryptography Library level one
of the big transitions it seems is that
developers can now at least begin to
engage with this maybe developers who
have a high awareness of cryptography
and some math background but nonetheless
at least you don't yourself have to be a
cryptographer to start building on top
of and using these things so edu and
Veronica the both of you have been
amongst the first developers I'm
guessing in the world to really engage
with mpf or fhe broadly and really take
it seriously and think how do we build
stuff with this um where are we at right
now can you describe what the journey
has been or what the experience has been
what does the tool stack look like the
both of you were also among the early
developers in the applied ZK world as
well how does that contrast where where
are we in comparison is this like 2017
is this 2022 does that question even
make sense tell us a little bit about
the development experience
today uh yeah I I feel like it's it's
similar to 2017 it's like uh in 2017
like I remember we have this njs and the
circum which is like super awesome uh
and uh now uh I think like we have this
Phantom Zone built by J uh so I was able
to experiment with it and build stuff uh
during this summer so like we built this
like a chickens game which is like a
previous version of this frog game uh so
we have this like 4x4 20 by 20 grade
with like four chickens move around and
then chickens can lay X which is like
one and zero uh so I think like from
that uh experience
we uh like how we build a game is like
we can write the code like maybe at that
time we writing C+ plus and then we have
like a compiler compile it down to like
binary circuits like binary Gates that's
like what Phantom Zone is using uh and
then once we have that uh we can use a
Phantom Zone Library uh to to do that I
think like um if you start writing the
circuits like At first it's like uh yeah
so so I remember like why I when I talk
this IDE and like how to like how to
think about this like uh you know egg in
a Grade like zero and one and then I
realized okay like every time like you
encrypt a zero and one you sample like
different Randomness so like when you
encrypt like zero and one every time
it's like the uh Seer text is actually
like different so that is like a shift
and we also realize okay you cannot just
access like a cell in the braid because
a CO coordinate is like encrypted so
like in so like in traditional
programming if you want to lay a EG say
sell like a two stay you just access two
stay flip a bit but here you have to go
through like the entire grade uh so yeah
it's it's it's pretty interesting but I
think like on the high level it's
actually the experience is pretty
similar to like the ZK development
experience like we just experiment like
build a lot of demo code build a lot of
use cases and then we realize okay here
is the things we need like researchers
to do more to help us like optimize and
here are the things we need to build
like Library framework as like ZX Park
built like this pod and GPC Library so
you can help developers to build a more
useful application so I think like in
general like the experience feels pretty
similar yeah
yeah I would add that as far as I know
there's been FH libraries for single
party for a few years but probably they
there's not been a lot of developers
interested in building applications on
top maybe it's because of the
performance maybe it's because just of
loading computation was less exciting
and on the other hand in the ZK space
we've had so many developers wanting to
build applications and deploy them on
chain and build proof of Concepts and I
think this has helped a lot on the
maturity of the tooling and making it
more usable so in that sense for FH
tooling I think we're are not there yet
and then we have all this FH previous
tooling that was single party but now we
want to use it on the multi-party
setting so we can reuse the ideas of
having circuits but maybe we need a
layer on top to Define who is the owner
of the data that is coming into the
circuit and I think there's been some um
exploration on this from the MPC side so
hopefully we can take all these ideas
and build better tooling that is more
usable and that makes the process of
taking the library and building an
faster yeah I want to touch on a couple
of things that the both of you raised um
the first is this idea Veronica you
mentioned that
if I have some sort of you know you guys
try to build a chicken game over the
summer right which is basically there's
a grid the chickens can move around the
if you're a chicken you can lay an egg
at a square then you can keep moving
around and you can only see what's
around your chicken and you said this
thing that was the
uh being able to actually flip a bit at
a certain coordinate is not as simple as
accessing what's the value at 2 comma 3
in this two-dimensional array and flip
the bit you know somehow you need to
scan over every single coordinate and do
a maybe flip in encryption over every
single coordinate so that you're
preserving the location that your
chicken is actually is um interacting at
so um one of the things that this makes
me think about is this idea of thinking
of FHA more in terms of programs rather
than functions where a program is
something that might keep some
persistent state where as a function is
something that you run once it has some
inputs and it has some outputs a program
might have some memory you execute some
you know imagine like a smart contract
call and then the memory changes and
then you execute another call and then
the memory changes and you can read from
it so um when we talk about something
like the uh this model of
programming without thinking about
things in terms of the the program and
memory model I guess we're just limited
to edu like you were saying these single
player application single party FHA
applications where you're basically just
running an extremely slow calculator
right like I can I can perform delegated
computations but a billion times more
slow than I would be able to on my own
machine is that kind of an accurate
summary
yes so we've gone then from I I was able
to observe some of your guys'
experiments over the summer um can you
talk a bit about not just the
development process but the mental model
shift and going from the first
application were these kinds of uh
calculators where we can add numbers
together running a one-hot function or J
I know you built a simple game Bomberman
and then after that we moved on to this
chicken game and now we've got the Frog
demo going on in in the downstairs
basement what was the process of
figuring out the programming model here
like for all of you how what did you go
into feeling uncertain about and then
what clarified as you started writing
circuits I would say that one of the
challenges that if you imagine this
server that is running FHA functions and
has a private State and and then clients
keep uh sending request to run stuff on
this private State there is the question
of how much does the server see for
instance you can have a state and four
methods and the server knows which
method you are calling to update the
state but you could also put these
methods encrypted so the there's only a
single endpoint and there's like a
switch in the circuit that picks the
method and then runs the computation and
there's also like if you try to balance
both you will find trade-offs between
performance and privacy so trying to
reason about that is pretty
hard um for me it was
um so in FG turns out that you have to
perform something called bootstrapping a
lot like this is a bootstrap this is a
single operation that is the bottom like
requires a lot of polom multiplications
and and your entire function is like
many of the these bootstrapping
operations I observed myself to search
over from like I just started
appreciating paralyzation a lot more
after F than before because what you can
do is like you can take a program but
you can write a program in a way so that
it's very paralyzable and you can assume
you have a server in the cloud that has
you know thousands of codes and you just
put it over there and executes in parall
and the latency is like really
low so that what that is one thing that
I like like to mention is like in F you
just start to appreciate the power of
polarization a lot more than
otherwise yeah uh yeah as I said like
you know access like me memory like is
hard uh another thing is hard is like uh
how do you think about how to represent
States like that like actually um you
know matters a a lot like in terms of
the performance of the algorithm so like
think about what how how you like Bond
those States together and then uh so
like yeah so basically that's like one
part of the thing we have to think about
uh another thing is like I I think it's
just how do you uh think about your API
and like because the thing is like uh
you can do like a bunch of computation
and at the end like if you want to
actually see the result you have to have
like every party to decrypt it and then
so you can get the result uh so that is
the one thing to really think about and
also like um you think about who get the
result because a person who decrypted
last like who get all the other people's
decryption shares would to see the
result so that is also another thing to
think about when you uh desire your
program so we're getting back to this
interactivity topic that we touched on
earlier in this panel it seems like this
is a real thorn in our ability to build
more scalable mpf applications I mean as
far as I'm aware all the demos that each
of you has tried to run are involving at
most three or four parties um how do we
scale past that how do we get to a world
where the Twitter backend can be run as
one huge multi-party computation or mpf
or just general cryptographic
computation is that something mpf can
bring us
or uh well with with mpfg or any any MPC
protocol you stuck with this this issue
of someone holding the secrets um and
that is hard to get around unless you
have something new um which sort of fled
to the investigation of program autic
and IND distinguished Le ofation in the
first
place well um and can we get there yes
we can get there we have like a few
things to present and and I think if you
were there for Bar's talk he sort of
introduced bounty we implemented a
program tication SCH and sort of we want
people to break it because it's based on
newer assumptions so I think there's a
path there there's a path for building a
tutor back in based on the hallucinated
server model um that you've been
mentioning um yeah can one of you
describe maybe what program alisation
gives us here what problem does it solve
that we're running into with
mpf maybe you can think of it as
non-interactive
mpf so you have the program you have the
private State and anyone can uh call
this program and get the outputs without
interaction from the other
parties so in short we don't have to do
this multi-party decryption every single
time I want to retrieve some result from
my encrypted program think of it as the
the offs circuit now has the ideal
secret GI F which was first split among
these different parties embedded inside
it and now you feed your inputs you feed
your cyhex which is output of the FG
evaluation to this off security program
which holds the ideal secrety and it
decrypts it for you it's just like a
decryption Oracle and if you want to be
more strict I would say that it's a
conditional decryption Oracle because it
just first needs to verify whether the F
was evaluated correctly or not but
that's a different
question so yeah maybe my final line of
questioning here with my final line of
questioning here I want to look a bit
towards the future so
we've heard this topic obfuscation come
up a couple of times at
Devcon and we've also heard a lot of
really strong claims about obfuscation
obfuscation removes the need for ZK
obfuscation generalizes
mpf how much of the work on these
Technologies you know mpf the schemes we
we're using in particular the
programming models around them um is
actually going to be relevant in a world
where we think obfuscation is actually
the final boss of cryptography should we
still be developing these particular mpf
schemes like what what role do these
still play or is this something where
this is a bridge technology but what we
really think is going to happen is at
some point obfuscation is going to take
over once it becomes practical enough
and completely you know remove the need
for any of of these
tools uh I would say that to answer that
like answering that question would take
a while honestly um but there's one way
for taking officiation that requires
publicly verifiable proofs of f
valuation and F so you require certain
proof generation they're not Z knowledge
exactly but you require FG over there
you require some sort of MPC protocol as
well but once you've build officiation
then it encompasses all these things
um
yeah I would say a different view point
of view which is that for performance
reasons we may want to stick with the
fastest solution so we may have hybrid
Solutions in the same sense that you can
build a signature scheme with ZK but we
still use like traditional signature
schemes so maybe I all the part that you
can do with f you will do it with FH and
only the part that needs IO you will
need you will be using
IO uh there's also a question of whether
you can build program autic for generic
circuits or can you only build program
officiation for limit lied class of
circuits uh and we do not know a full
answer to that yet
um all right um a final question I have
is uh what would all of you be most
excited to see built next on top of mpf
or any of these technologies that are
creating this model enabling this model
of this trusted third party built inside
cryptography hallucinated server maybe
folks here have heard a couple of
different terms what what should we
build
next uh I I I wouldn't want like
researchers and also like uh uh you know
cryptographers like someone like Jay to
build like improve the library and uh
actually try to make up fation a reality
if that happens I think there's like so
much things uh we can actually build on
uh for app developers I think this is
the time you can actually try like and
TF AG uh I would like to uh people to
build more things like for uh multi-
parties like for people to connect to
coordinate and to kind of negotiate
things so that's type of the things I
want to see yeah I think someone should
finally build the I trust um we have
been trying this for like now almost
four years now and I think someone
should finally build the I trust with
multiparty f ofation if it's practical
in near future and for those who don't
know igen trust is basically proofs
about social graphs if we have a
decentralized social graph then we would
like to be able to perform some
operations on it yeah I totally agree
with these uh two points I would like to
add one which is less exciting but it
would be nice to lower the resources
requirements of mpf so that it can run
on Lower End Hardware so more people can
use
it awesome thanks vulk so now we're
going to go to audience
questions I believe that in a moment
you'll be able to see oh cool okay here
we go so we've got this QR code on the
screen you can scan and make a ZK proof
with your zass ticket uh to post a
question to this feed and we're going to
start picking some of these questions to
pose to our panelists here so maybe uh
I'll I'll go a proximately in order here
what would be a good framework to start
with for someone interested in building
on top of mpf what is even the
landscape Phantom Zone that would be a
library that already implements mpf
protocols and then you would need a
compiler on top of that unless you want
to be writing Boolean circuits by hand
which is a fun option if you want to
learn how it works but not very
practical and we there are some
solutions for the compiler thing but
they are not very very robust and some
someone in PSC will probably working on
this are there other tool Stacks besides
Phantom Zone that exist uh there exists
lgo that is like a more lower level
Library again gives you multiparty f for
different schemes not just the schemes
that Phantom Zone implements you can
work with that uh there is something
something called open F that also
implements multiparty f
um again very low level not as not as
high level as phandom Zone but like if
you really want to you know go into this
Wilderness and sort of explore Effigy
then I would recommend these to
libraries for
sh awesome so the next question here is
tees uh have you considered the
combination of tees and FHA to solve
privacy issues you mentioned and about
how much the server knows maybe to add
on to this it sounds like what what mpf
almost resembles is like a mathematical
te that also happens to be 1 billion
times slower so I'm curious for each of
your takes on basically you know why is
it worth exploring this Avenue why is it
worth incurring such a high performance
cost overhead is it because we believe
that that cost is going to go down
enormously or is it because we believe
that there's some fundamental reason why
the direction of things like fhe and
obfuscation versus the direction of
things like tees lead us to different
capabilities I would say I find it
harder to reason about the because I
believe all thees can be broken and then
it's a matter of how hard it is to break
them so you try to put a cost on
breaking them but this estimation I
don't know how good you can make it
because if someone finds a new flaw that
reduces the cost and you build a
solution with that assumption
then uh you have a bad solution so FH
gives you an alternative where yeah it's
the performance is worse but you
have better guarantees on the
security um I would say that what I what
I really want is like a box that comp
that is like this mathematical te and
this I can sort of like explore this box
and confirm the guarantees that it
provides and I don't think we can do
that with te at the
moment um the only feasible way of doing
that at the moment is by relying on
mathematical guarantees which comes from
cryptography and one form that is like f
morphy
encryption yeah I I think what I think
about it maybe mpf AG can also make you
to be able to do things like peerto peer
fashion so you can have like a A
cryptographic Shard of the of a program
and then to run it that way rather than
put everything inside a central box uh
so that might be useful in some use
cases
yeah one thing maybe I'll contrast this
with and I would love to get some takes
on this is well with a lot of the FHA
prototypes that we've seen built in the
recent months the architecture for these
things looks like you have multiple
clients and you also have a server that
computation is delegated to that's
responsible per for actually performing
The FHA over encrypted data you know
there's some Spectrum here between
everybody is running the FHA locally on
their local machines two there's a
delegated computation two actually we're
going to delegate the trust model to the
te as well how do you think about
navigating that Spectrum like what is an
appropriate place to land on and of
course we might even take it further on
the Spectrum in the other direction
which says well maybe we don't even
accept fhe because at the end of the day
some set of parties needs to hold a
bunch of decryption key shares so
theoretically some K ofn people could
collude to to decrypt the entire State
we need program off fisc instead where
do you think about landing on the
Spectrum and where do you essentially
draw the line for what technology is
actually useful for an
application yeah I think there should be
a world all those things exist and
depend depending on the special like
your use case and then you choose one
versus the other you might think about
like what of your uh security guarantee
you want to achieve like and then also
like the performance and like how is the
uh when you have users like how is the
user flow going to look like uh so
I yeah I think like depending on the
stakes of your problem you may use the
in certain parts you may also try to
have hybrids like maybe you have a model
where you have a collusion assumption
but then you run this under te so now
you need to break through security
properties which is that they Collide
and also sorry they collude and also
they break the te so I guess on the
Practical side of things if you want to
build a product some people may find
using these is
acceptable but I think we as a I don't
know as a researcher as researchers we
should try to push more and try to work
towards having practical mfh and
practical NPC in
general the problem with relying on just
tees or even like this God server model
of the multiple servers in the cloud
probably you know T so was in the cloud
holding the secet shards is that the
moment you try to build a big
application or the moment there's enough
incentives people will break it like the
moment there's a way to break it people
will break it um which sort of like forc
me to push on this other Direction Where
We should really aim for program ofation
to become practical for any of these
things to scale in terms of going global
um it would be really hard to even scale
multiparty F if you're not able to get
on this problem um
one other thing that I want to ask about
and this is inspired by one of the
questions on the screen which is about
ecdsa the signature scheme ethereum uses
is where do these Technologies intersect
with blockchain I mean after all we are
at Devcon the annual or you know
semiannual ethereum developer conference
um and it also sounds like the way that
we've been talking about mpf obfuscation
hallucinated servers and all these
Concepts is very similar to the idea of
the world computer spiritually that it
ium is gesturing towards so are there
any specific technical interfaces that
any of you think about as this is the
border between FHA and blockchain in the
near future right now it might not be
performant enough but where where are we
going to see these things finally dock
or converge or how should we think about
docking
them uh like at
the okay if we if we just imagine that
we have program OBS secution practical
future then there's there's a huge
chance that we can make we can
completely change the smart contract
framework of eum itself this might be a
big claim but like you know uh just just
take it for granted at the moment that
we have program officiation
but uh we can completely replace that
with IO um or program ofation we cannot
do that at the moment with multipart FG
because us as the community are not
comfortable with these God servers
holding the secret shots
um which is why I also think that we
cannot Dock at the moment uh we would
make future progresses to be able to be
compatible with what blockchain people
are comfortable with I mean this kind of
gets me back to some of the discussion
we had about interactivity right so ZK
snarks became a very good fit for
blockchains once they became
non-interactive when we had general
purpose interactive zkps the liveness
assumptions needed to interoperate with
smart contracts were just too high is
that a fundamental barrier to to fhe and
blockchains or is that something where
we can actually do some sort of hacks in
the near term to find some useful
convergence I can imagine some solutions
where a a like a small party um
coordinates outside of the blockchain
and they they compute something with
multiparty FH and send it to the
blockchain for instance I don't know
like f
multi something like that I guess that
would be but when you want to go to the
global state with no coordination I
think the only solution is going to be
ofation awesome all right that is all
the time that we have let's give a big
round of applause to our panelists and
thank you to everybody for joining us
this
afternoon all right thank you to our
amazing panelist
for for
w
all right hi everyone welcome back um if
you enjoy the previous panel a lot the
good news is we have another talk from
Jemma J on scalable multi-party FHA with
Phantom Zone let's welcome JJ onto the
stage hello um welcome back um
so today I I would be talking about
Phantom Zone uh but before I sort of
like dive deep into Phantom Zone and
talk about the rest of the things I
would uh sort of walk you through the
motivation behind Phantom
Zone
so if you guys are familiar with
globally mutually trusted third
party I would want to introduce this you
to this idea of globally mutually
trusted third
party what is this m globally mutually
trusted third party well it provides you
three
guarantees the first thing that it says
is that whatever information you send to
this third party it will always keep
that private it would not leak it to
anyone the second guarantee that it
provides is
that all the information that it has
collected over time from different
people you know we have been sing this
globally mutually interest a third party
all our information lets for a year all
the information has collected for all
these years it would always keep that
private and would not allow anyone to
poke inside its Sate inside its
memory and the third guarantee that it
provides which makes this particular
party very magical is that it you can it
can compute any arbitary function we
want it to
compute as long as we provided enough
authorization to be able to compute that
function and it would only output the
necessary
outputs usually I sort of like refer to
this this mutually Tred third party as a
mutually shared computer and if you guys
are familiar with something called the
god protocol this is the god
protocol this is a picture from xabo
back in
um so first observation to make is that
if you really want want these three
guarantees uh to be if you really want
this party to be globally mutually
trusted we want this party be party to
be able to prove these three guarantees
to any individual without requiring any
additional interaction which is why we
require cryptography we cannot just make
it on certain legal agreements or
something like that we require
cryptography for building this the
building this um globally mutually
trusted shared
computer and we started to build Phantom
Zone to eventually build the god
protocol but to stick within the Realms
of practicality we could only build an
Abridged version of
it so for the rest of the talk I will be
talking about a what is fundom zone why
it is an a bridged version of this God
protocol and the second important thing
that we're talking about is how can we
push the Frontiers to eventually build
the got
protocol okay so Phantom Zone The
Abridged version the key idea in Phantom
Zone is something called multi-party
fullyy
encryption and for you to describe for
me to describe you multiart folio Murphy
encryption I'll have to eventually
describe you what is single party folio
Murphy
encryption in single body fol of
encryption you have a single client you
know this guy over here they hold a
secret they keep the secret private to
them they can encrypt their information
which is a here with the secret and
produce an FG Cipher text and then they
can send this F Cipher text to any
server and the server can evaluate an
any arbitrary function on their private
input which is a and produce an output
Cipher text and then the and the client
can receive the output CER and decrypt
it so this is single party
FG coming to multiparty FG while the key
IDE in multi party f is that you split
the secret which is held private by a
single client in single party F among
many clients so you have s0 S1 S2 as
secret shots split among these three
people over
here the first step in multiparty eff is
something called Collective p uh public
generation so all these three parties
come together and they generate the
collective public
key and then all these three parties
using the collective public key encryp
their private inputs and produce F
Cipher text and then they then they send
their FG Cipher Tex to the server server
executes a Mary function on the F CeX
and produce an F produce an F
output the key thing to notice here is
that all these parties would have to
produce a decryption share to De
eventually decrypt the output cext here
so they produce the decryption share
using the secret shards and then they
send it to each other and then only
they're able to uh decrypt the art with
Cipher text because in this case the
secret was split among all these parties
so why is Phantom Zone an Abridged
version well because Phantom
Zone assuming that in the future we able
to add publicly viable Effigy to a
Phantom Zone can only guarantee the
three guarantees that I talk about in
the god protocol to only the holders of
the secret shots it cannot guarantee
these three guarantees to everyone
around the
globe which is why Phantom Zone is just
an a bric version of
it okay so you might wonder how do we
build towards the god protocol like how
do we even do
well what I would like to say at the
moment is you know I would have loved to
say that you know after a lot of
research and a lot of like five years of
research we' have figured out the
solution to get build the god protocol
but no like there are no at lightening
thoughts
here and there's one obvious answer to
building to eventually building the god
protocol which is program
officiation what's program
officiation well to Simply describe a
officiation let's just assume that you
have function f right what you can do
with program offs cation is you take
this function f and perform some
Transformations on this function f and
produce an offic
circuit you can give this off circuit to
someone else and program off Association
guarantees that the only thing that you
can learn from that offs skit circuit is
the input to Output map and nothing
else now you might be wondering why is
this useful because if the function is
Trivial then you can e easily learn it
from the input to Output
map program observation becomes easy
become becomes very interesting when you
sort of like obate a program that is a
cryptographic function for example let's
just say that I take take
uh I take a function I take a function
that is that decrypts any Cipher text
that is encrypted to my public key right
so I take a function and this function
has my secret key and it decrypts any
Cipher Tex that was encrypted to me
using my public
key and I perform certain
Transformations using program
officiation to this function and produce
an officed
circuit I give this obate circuit to
someone else what they can do is that
they can decrypt any side aex that was
encrypted to me using this obus circuit
but they can never ever learn what the
secret is inside that circuit they can
never learn my secret
key
um and this is these are the class of
functions where program ofation becomes
useful and I'll tie it to to building
the god protocol later in the
slides uh okay so now assume that we can
only build program officiation for some
limited class of functions you know not
for General class of functions but like
limited class of
functions I'll tell you one way of
building the pro U building the god
protocol using program
appication step
one modify the F scheme that we using
before to become publicly verifiable
what do I mean by that
well a publicly verifiable FG schemes
does those things it evaluates the F
function which you know a normal F
scheme does in addition to evaluating
the function it also produces a proof of
correct evaluation so that anyone can
verify this proof with the output CeX
and be assured that the server that sort
of executed this F function exe executed
correctly and which I usually referred
to as proof Pi of correct
evaluation step two replace the collect
key generation operation that we did in
the multiparty F with a trusted setup in
The Trusted setup you have AR number of
people here they perform some MPC
protocol to produce FG keys there two
types of FH Keys which are very
important public key in the
bootstrapping key bootstrapping key is
usually used for some sort of like f
operations that you can completely
blackbox the key thing here is that no
one knows the ideal secret key because
we're generating a we're doing a trusted
setup in NPC to generate these two keys
the third step is modify the trust setup
to also output an officiated conditional
decryption Oracle okay that's a mouthful
I sort of like go into it one deep one
level deeper what is an offs skated
conditional decryptor this particular
conditional decryptor is an offse secut
program of the following functionality
what it does is that takes an output
Cipher text and a proof of correct
evaluation of FG
circuit it verifies whether the proof is
valid and Crypts the output cyhex if and
only if the proof is
valid and this sort of like tells you
why did we assume in the first place
that program autic may be feasible only
for like limited class of functions
because to build a got protocol like to
to build the got protocol using the F
route we only need program offic to be
practical for this officiated
conditional
decryptor so we modify the trer setup to
also output this offc conditional
decryptor and that's it and another
thing to notice that this conditional
decryptor also has the secret key the
ideal secret key that no one knows
embedded inside
it okay so the end to endend flow is you
do NPC to generate three things public
key bootstrapping key and the um and the
offc conditional decryptor which I now
realize is somewhat of mouthful uh I
should have chosen some other term
anyways the second flow is now anyone
can encrypt their private inputs using
the public key that is the output of the
NPC protocol so you have multiple Cipher
Texs here and then they can send it to
the F server F server evaluates the F
function outputs the encrypted output in
addition it produces a proof because the
F server is evaluating a publicly
verifiable F
scheme um and then we Pro we we plugged
in the proof as well as the output to
the to the offc conditional decryptor
and the conditional decryptor would only
out for the uh would only decrypt the
encrypted output if and only if the
proof is wallid so this is one way of
building the god protocol using publicly
verifiable F and program ofation for off
seced conditional
decryptor so there's one way which I've
just shown you but we need new ideas to
push the Frontiers and to finally build
the pro uh to to finally build program
officiation or indistinguishability
officiation if you're familiar with that
here I've showed you just one way but if
you're able to come up with new ideas
then probably we can make program
officiation more practical for General
circuits not just for like limited class
of functions that we used before and
probably we can directly build the god
protocol from program
officiation okay so while I was
exploring this field of program
officiation and
IO one key observation that I made um
this uh one key observation that I made
was that it's really hard to get
efficient program ofation from standard
assumptions and we would inevitably
require exotic assumptions and I'll tell
you what are standard assumption what
are exotic assumptions well a standard
assumption is assumption that has been
there for a while for example dlog
discreet log
problem there's also there also exists
additional incentive for people to break
these stand uh standard assumtion
and exotic assumptions are somewhat
newer assumptions like they have been
only there for like 5 years or not even
five years like 2 to 3
years
um what we can do as a community to you
know realizing that we might inevitably
need newer assumptions to build
practical program officiation
is we can start examining these newer
assumptions start breaking them start
testing them or we can build
applications using this assumption so
that we can incentivize people to break
them and tell us whether they're broken
or not and then eventually in like few
years we would have can assumptions that
are newer assumptions but they have
become then standard using which we can
build practical program
ofation okay
uh and taking a first step towards this
we launching a py program for program to
break one of the candidate assumptions
which is called program officiation VI
local mixing the way I think about this
particular assumption is that you
they're taking take taking more
computational complexity approach than
taking like the traditional approach of
using algebraic structures to build
program offs
cation the goal of the bounty is that we
provided you an offs skated circuit with
roughly like 240,000
Gates which was officiated from an
original circuit with roughly thousand
Gates and you have to find the original
circuit you can learn more about the
Bounty at off estopia toio if you know
what off estopia is off hostopia means
that we living in a world where
officiation is practical uh and the
Bounty amount is 10K and this bounty is
launched in collaboration with um eum
foundation and z
spk um okay so before I break um and I
think that I have a bunch of time okay
before I break I would want to make one
conjecture
and the conjecture goes as follows I
think the god protocol is the
convergence of
cryptography probably building the god
protocol would require certain sort of
like f that is just one route but like
publicly viable F and other things like
MPC for setup and so on and so forth but
once we've built the god
protocol I think it compasses everything
it gives us everything that we have we
have been like wanting for for a while
it gives us witness encryption it gives
us Z knowledge proves by signatures it
gives us NPC multiparty computation it
gives us Fe fun functional encryption
all all of these things that we've been
demanding for a
while and this is also one of the major
reasons that we should start
investigating much more seriously how to
get practical program appication and
finally build the god
protocol and that's it thank
you all right thank you for the talk we
do have some questions rolling in
uh yeah uh let's go through some of the
questions uh let's start with the first
one can we Implement threshold ecdsa
with Phantom
Zone at the moment yes because you can
express every like practical like
theoretically yes but it would be very
impractical to implement ecds with
Phantom Zone at the moment because ecds
is like you doing eptic of operations
which is a lot of operations um as far
as I understand threshold ecds is
possible
it takes 2 days to generate one single
signature all right so next question can
you tell us a little bit more about the
definition of obfuscation as a virtual
blackbox that's the first question over
here isn't your definition ofation as a
virtual blackbox
impossible I I am not posing officiation
as a virtual blackbox um I I did not
mean to say bation is a virtual blackbox
um by the way the impossibility resolve
for virtual blackbox is only for like
certain very restricted class of
programs it's not for like General class
of programs eventually you can aim for
virtual blackbox with certain caveats um
but again saying that my my definition
of officiation is not virtual blackbox
um all right and what can be done today
Zone at the moment as I said Phantom
Zone is an Abridged version of this God
protocol it does not even have a
publicly scheme so it does not give you
all the three guarantees the only
guarantee that it gives you is that it
will execute the function that you ask
it to execute while input while private
information can be coming from multiple
people you'll keep the information
private but you'll have to trust it for
it so you have to trust this particular
server to always keep the information
private and not send it to anyone else
perfect and we do have one last question
oh cool more questions rolling in can
obus skating programs undermine open
source transparency and make it harder
to verify the absence of malicious
code uh I see make it harder to verify
absence of malicious code well that is
assuming that the entire program is
officiated um when I say officiation we
require obse cation for certain parts of
the program which can interact with a
public program and a private program
which is obs cated I understand that
observation can be used for many
malicious purposes as well like for
example you know like there there's
several reasons why people might be
interested in officiation but we can as
a community make sure that there's an
interaction between the public
interfaces and the private interfaces
which are
officiated all right and why do you call
the publicly verifiable FH circuit
obfuscated doesn't the require solidity
verifier or something which is public
uh no uh I think once I give you obsc
circuit there are certain guarantees
that you can learn from the offic
circuit itself that it does not reveal
anything as long as you done the OBS
cation correctly all right and do you
have evidence that the conditional
decryption functionality is imposs uh is
possible using IO yes uh there is there
theoretical results and we're trying to
make it practical as
well all right uh can you give one
example each on how IO can replace ZK
fhe okay so for ZK what you can do is
like you can embed a secret key inside
this off SEC circuit the god
protocol and uh a zero knowledge proof
is just a signature from this God
protocol whatever the signature whatever
secret exists inside this particular
server or this SC protocol or this FG
circuit off SEC
circuit a signature by that thing
becomes the Zer knowledge proofs so you
do not require zero knowledge on the
client side uh anymore for MPC again
it's a globally mutually trusted third
party all of us encrypt our private
inputs with the public key corresponding
to the secret key that lives inside this
off gate circuit and we send a private
inputs to this it decrypts that performs
some function and produces the output so
that's one way of replacing MPC and the
same applies for FG cool uh we can stay
here for maybe another 10 seconds if
there are any new questions rolling in
all right cool um let's give another
round of applause
to J all right
hi everyone welcome back my have
everyone to get seated
please thank you next we have a talk on
melti party homomorphic encryption from
ring learning with errors from Jean
Philip um a little housekeeping rule
there's going to be a QR code on the
right side of the screen please scan the
QR code uh if you have any Live question
questions so Jean Philip can address
them at the end of his talk now let's
give a round of applause to Jean Philip
onto the
stage so hello
everyone yes so before we had a high
level introduction to multi party F and
and in this talk I will go more into the
details how you in practice instance
this kind of construction so this talk
will be like bit more formal and
Technical with the previous one but it
should give you a good Insight on how
it's done in
practice so what is
MPC essentially MPC
is um a function you want to achieve and
you want to compute a public function or
private over a set of inputs that can be
some private or private
and get an
output um
wait just just yes but my slides are not
working your slide not blocking it's no
the slide I made you you are missing the
equations and a lot of it on it it's
wrong slide yes
it's not possible to give a talk
without
yes I
get
all
right uh so sorry guys we're going to
take maybe a 2 minute is time to figure
out some technical difficulties so bear
with us uh we'll be back very shortly
do you know who I
can seual r
do you already send this light but it's
not
online this is online but not connect
right
know screen is connect
to already
connect ufi is already connected with
have the B and monitor
already yeah
yeah yeah there was an issue with the
slides M fixed now okay sorry there was
an with the slide but it's fixed uh yeah
back to the slides now everything
appears uh yes
so you want two things you want output
functionality so you ensure that you you
get Y and also input privacy so you do
not learn more than what you could learn
from the inputs and the
outputs and we consider a set of n
parties and up to n minus one
adversaries with are public and Statics
which means they follow the prot calls
and try to learn AAS as
and in fact uh you can instantiate MPC
with f by adding an access structure on
top of FH this is man meaning that your
restrict who is able to decrypt uh what
and this is done with um a key
generation protocol like Jay introduced
to you where you secret share the key
among the participants
you generate some public evaluation key
and public Keys then you have an
evaluation phase and finally you
interact again to the
Crypt so I will uh introduce now the
ring learning ferror problem which is
the base construction on which all these
schemes are are based and so you have we
work in a polinomial ring of DK n minus
one modu q and we need free distribution
we need a uniform distribution of this
ring a small error distribution and a
tary distribution and that's it and
essentially the ring learning f uh
problem is distribution is defined as um
a small secret polinomial time a public
uniform polinomial plus a
error and you have two hard problem on
this lce watch which is a search problem
essentially you need to either find e or
s or distinguishing problem which task
you to distinguish a ring a valid ring
learning for sample from a uniform
distribution and from this you can bu
build homop
encryption and this works because all
operation are aine operation of the
secret Keys meaning that if you apply an
operation on a CER text then it outputs
a saer text on which the secret the same
operation I appli on the secret key
and it essentially preserve the
structure of the saer text so before and
after the evation all you need to do
is have a secret key and multiply back
the two component of the saer text to
recover your
message and because all of these are a
kind of secret
key sorry yeah there is one more thing
to introduce which is G Gadget so sorry
yeah um to encrypt the CER text you
simply sample a ring infer sample and
you add the message on top of it but
sometime you also want to multiply with
a message and for this you need another
uh Cipher text which is called Gadget
regular in the same as before except you
decompose your message with a base and
what this allows you to do is to do
multiplication where the noise is
independent of the
message
and since all operation are fins of the
secret key then the setup
phase which generates the public
encryption Keys is also a f of the
secret keys so all the elements in blue
they are linear operation of the secret
Keys as well as a decryption and re
encryption which is simply changing the
secret keys so these are all linear
equations and yeah is one issue with s
square but we will deal with it after
and this is great because now
you can instantiate your
protocols as public agreable
transcripts so since everything is a
fine function of a secret key then
everything is additive so each party can
sample its own secret key locally and
then you do some protocol with public
transcript which
output a sum of all the transcript which
correspond to a new transcript that is
encrypted under the collective SEC key
which is unknown by anyone but it each
one knows a part of the secret
key so this is great because with that
you can Sun a onetime
setup and it has a low round complexity
compared to traditional NPC you have two
round for the setup uh one of the two
rounds is because of
this really key which has an S Square
which is not linear in
s then valuation f is completely non-
interactive this is why you have a
overall low cost of communication ation
and you again need to interact for the
decryption and what this allows is a
completely deleg delegated delegated
public share aggregation and overall it
has a sublinear complexity multi party
competition so these kind of schemes are
implemented in the laal library and it
enables N Out of N and T out of n
pressure schemes so this is the library
that provides all the stateof the art F
schemes and it's also wiely used for
example for the adash privacy and
security Workshop where Reser is was
used by the two um first place
competitors but simply implementing
these protocols is not enough because
you run into a lot of issues when you
try to De them in practice so Latigo has
the construction and deployment of the
Bas protocol but when you run them in
practice then you run into some security
issue and Cent issue for example you
need to make sure you have a reusable
setup and that everything can be
parallelizable but the share for the key
which can be quite large in practice can
be uh supported by a Cleon so you need
to share the shares you need to support
a predefined h circuit evaluation and
also you need to ensure that if a client
drops for example during the setup or
during the OR at the decryption you have
some uh robustness but also but it's
still
secure uh even if you have these kinds
of unexpected events and for
this um alium was developed by Christan
mus and this solve of these issues so
alium is bit on top of Latigo and it
provides a framework to be able to do
FHA based
MPC and deploy practical
Solutions so we have seen that we have a
two round
setup uh basically you need one round to
generate a public key and then one round
to encrypt and generate the elevation
Keys um but it would be great if we
could have a one round setup because we
would this would enable much more many
applications so essentially why do we
have a two round setup is because when
we generate one of the public key key
this key enables CER text compactness so
when you multiply to CER Tex together
with not grow in size it depends on the
key which itself depends on a previous
protocol so it would be great if we
could reduce this to a single round and
the ideal framework would be that we
have a set of predetermined parties and
each of these parties will send a single
public aggregable transcript to a server
and then a server can choose any subset
of these parties Aggregates this the
part Associated to these parties to
generate the corresponding Evolution
keys and SA text he can run an Abit
circuit and then it only requires the
collaboration of this subset of party
decryption so back to the issue that
prevents a two round protoc a one round
protocol this is this interaction public
key which is an encryption of a square
of the secret key it's both important
for seex multiplication but also for
expanding some over caner Tex which are
used for the few boot strappings which
is the scheme that is for example used
as the back end in Phantom
Zone so if we look more at the structure
of this key then we see that it's a
gadget ler text of encryption of a
secret key time the sum of all the
secret
keys so it would be great if we could
have a one round protocol that is able
produce um this kind of key dependant
message for both LW and GW CER text and
well how can we a
that it's possible with some home
operation basically
we
generate three uh yeah from two R CER
text and one GW CER text you can
hopefully generate this kind of key
dependent message text and here both all
the message the FMA secret KU the error
the the secret Etc they are all um Ain
so we are all additive which means each
party can generate locally interactively
and at the end you can aggregate
everything and get uh this encryption of
message time
secret and this is great because now you
have a solution to have this one R
protocol and so we are back to our
diagram and now we solved the
the this was a previous instance where
we have one run for the
public key generation one R for the
encryption and the r resion key
generation and this solves and changes
it to one R for key setup and one R for
the encryption this is already
great um but allocating one R just for
encryption is fine if you want to have
Dynamic and flexib on the secet inputs
but if the input circuit is fixed for
example if you have a starting State
like for a game like frog zone or bank
account maybe you want to have
everything into one round and this is
easily solvable basically um the party
that wants to encrypt a message encrypts
it under its secret and the all other
party they have to generate encryption
zero under their own secret and you can
aggregate everything and this is
equivalent to encrypting under the
secret the public key of the ideal
secret key the only issue is that it
requires a on communication per sepher
text per party meaning that for each SE
Tex that a party wants to generate all
the other parties also need to generate
a corresponding encryption of
zero and yeah at the end you could have
a full one round non interactive setup
with encryption if if you
want um so these uh Protocols are not in
the base library but they are in the my
Fork of Library Latigo it's a fork of of
Latigo that has over 30,000 change it
has functional protocols Etc like these
non- interactive
protocols and there are also uh the back
end of Phantom Zone which is a r based
MPC Focus Library which can evaluate
arbitrary functions over a set of
private or public inputs and it has a
high level abstraction which is focused
for res use developers and uh yeah if
you did not know it it's the back end of
The Game forom Zone but is U
downstairs and um
well I the
questions yeah I have to disconect for
the so we do have some live questions uh
you can H here so here we have one on
screen is this a best method than ZK
proves
um I would say it doesn't solve a same
problem it tries to ensure privacy Z
proof do not provide
privacy so FH and ZK proof are
complementary you would use uh ZK proof
to for
example right now the server you have to
trust him that he will evaluate the
correct ciruit and so what you get is a
Sur of text which looks like fom noise
uh how can you be sure that it's not a
malicious Seer text which when you
decrypt it will leak some information so
you use the proof uh to have a proof of
the server did evaluate the circuit it
was asked to
evaluate all right uh we do have some
extra time for QA so let's wait for a
few seconds to see if there are any
other questions popping up oh we have
another one what are the main
differences between this library and the
pre-existing ones like concrete uh
concrete primar focus on
TF and vend stack is buil on this
scheme um these Library they are more
generic they are I would say more low
level also they are not in the same
language so I would say first uh if you
want to use the rest then uh use
concrete um but this Lao for example Pro
provides support for bgvs which are
scheme that enables vectorize arithmetic
over complex number of finite fields and
if it is more like single gate
arithmetic awesome and and can you give
some concrete use cases where one round
protocol
unlocks yes
so basically what it solve is um
liveness um now you can just send your
share and forget and go offline you
don't have to wait on the other parties
um to have some interaction to generate
the setup and the safer
text all right uh can you share any ins
SI or number on the performance versus
other libraries or
protocols uh so okay so multi party F
what is essentially solved is the setup
the evolation phase is the same as
single party F and the setup remains in
most of the case um negligible to the
evolution of the circuit so there isn't
like um concrete difference in
practice all right are there examples to
use your fortical with the features you
mentioned in this
presentation yes uh Fork has a fold up
with examples and there is an example
that show how to do a full one round
protocol for all the use key that will
be used in
practice uh what resources would you
recommend to learn about multi-party
homomorphic
encryption um I would recomend to join
the Discord of a.org they have a lot of
it's a great community and there are
channels to learn and to discover to ask
questions and um there's always someone
online and they will point you uh toward
the correct references if you have a
specific
questions all right I guess the next
question is also kind of uh related to
the previous one are there any posts or
Publications where we can learn about
these protocols so yeah unfortunately
right now no it's only in the library
but we will um submit something for V f.
conference which will happen in March uh
the thing is that these are very simple
and small protocols even if solve the
problem that was not solved before um
for question of time we do not have the
resource to produce something but it
will be there in a few months uh one
last question what are the challenges in
this space we should look
into
um right now the I see two challenges
that people fac in practice uh we have a
lot of people that complain that the
setup is heavy like few hundred
megabytes to a few gigabytes depending
what you want to
do and depending the circuit you want to
run the overhead can be quite large so a
lot of people say that if has a million
to billion time of override but it's not
really true it depends really on the
circuit you want to run some f circuits
are as fast as PL Tech circuit but they
are very
shallow um so it's use case basis uh
personally it I look forward to have GPU
or Hardware acceleration for f it would
make things a lot more practical but
I've also we had collaboration with um
people in the medical sector and they
said they did not care if we would take
three weeks for the competition to
finish because it took them two years to
get the data so it was nothing for
them all right so that's all the
questions thank you guys so much for
coming and let's give another round of
applause to for leave thank
you so our next talk will begin at 3
I'll see you guys
then for
sh
all right hello hello welcome back um
please have a seat for our next panel um
very excited for this one the next panel
will be on building consumer apps with
DK MPC and F and our panelists are we
have aush
from CK email we have aish from too
Andrew from cursive Richard from DK P2P
and Ying Chom indepentent researcher so
let's give another round of applause to
our amazing panelists on the stage
all right thanks so much Teresa um for
introducing us and welcome to the panel
on consumer apps um built with CK MPC
and FHA I'm also super excited about
this panel here um how I'm thinking of
these projects is we have two of them
that actually built Primitives so ZK
email and teso they're building sort of
libraries and tools and then we have two
of them who buildt on top of um so we
have ZK PDP that built on ZK email and
then cursive which uses t as well as mpf
so this is a really good representation
across the stack and we'll have I have
lots of questions for you guys um so I
want to first start with an intro can we
get um ZK email ZK P2P too and cursive
in that order yeah sweet um yeah I'm
aush I work a bunch on ZK email the idea
is you make proofs of emails in your
inbox or emails you've sent and these
can get proved on chain um we've thought
a lot about what are both the
interesting apps you can build and what
is the best kind of Dev tooling to do
that um and on the side I also like
thinking about mpcf and things like that
so happy to also jump in
there cool uh I'm Richard I work on ZK
P2P uh we build P2P marketplaces that
connect web 2 assets and uh like digital
Goods with web 3 uh like smart contracts
uh in particular we have like a P2P like
onoff ramp uh so basically you can uh
send money from VMO and use that to
trade directly for usdc on chain and
that's powered by ZK email um as the
source of proving that you've sent that
VMO payment and among other things we've
also launched a couple I guess different
marketplaces for trading tickets and
trading domains on the secondary
Marketplace uh hello my name is Ash I'm
fromo we build uh tooling and networks
to build and deploy MPC based
applications um in particular coars
which is what uh cursive are using and
you heard a lot about this week it was
the first week that it's live so we're
very excited and my role there I care a
lot about privacy um so I think about
how using these tools and the real world
actually affects the lives of the people
using them cool uh my name is Andrew I
work at cursive and cursive is exploring
different ways for cryptography to
enable new forms of human connection so
specific C uh certain things that we're
exploring are like multiparty FHA uh
looking at karks uh with t and also like
new MPC Primitives that we're like super
excited about as well very cool um I
want to start us off with a high level
question
because you guys are building in a
paradigm that is very new um and a
different from most consumer apps that
we're used to and I'm wondering um what
are some application design patterns
that um are unlocked by these
cryptographic Primitives and I want to
address this sort of like in in like
ascending order so in my mind like ZK is
the like most basic PR
followed by MPC Co narts followed by mpf
so let's go in that order like what are
some design patterns um that are
unlocked for you and give us examples um
from some of your favorite
apps let's start with ZK Emil yeah yeah
I guess we've seen two main ways people
design applications that I think are
different than everything we've seen
before one is around proof of received
emails so that's kind of the stuff that
Richard nzp can contribute to but it's
very interesting now that it's very easy
to make these proofs um people are kind
of starting to compose them so one
example is you can prove your part of a
slack workspace by using any slack
confirmation or invitation email and
then also prove you for instance took a
flight on United and you ended up at
Thailand and now you can automatically
build a system where everybody in your
slack workspace automa atically gets
reimbursed for their flight to Thailand
and it's kind of interesting because
you're not just using one proof you're
combining all sorts of different proofs
and just because it's very easy to build
each sort of proof you can build these
new applications that take multiple
facets of your identity into account and
so that's one that I've been really
excited by by seeing um we've also seen
um on the side of using emails to send
transactions people kind of hot swapping
almost emails and ethereum accounts in
their application so for instance multi6
signers can just be an email instead of
an ethereum address and it's kind of
interesting seeing okay once that's
really easy to do then people start
being able to expand their apps to all
sorts of new kinds of users so um I
think those are the two and I think
we've seen over the last few years the
design evolved more into uh this being
almost TurnKey for developers instead of
like ZK PDP which had to slog through
like months of The Primitives of getting
it up to speed but we learned a ton from
that yeah I'm curious what your takes
are though
yeah I think for us at ZK PDP we're
particularly focused and excited about
the idea of bringing web2 data and using
that like all across um blockchains
especially I think if you think about
like web 2 um all the data currently
exists in these like centralized data
silos like it's you you basically can't
export them to use anywhere else think
of like your Facebook follow or your
Facebook friends you can't just take
that and use it um on Twitter for
example right and some of these like ZK
Primitives allow you and I guess also
like MPC with like TLS notary um allow
you to kind of permissionless export uh
these web to like data from these like
silos and use that anywhere uh you want
and we're particularly excited about
like putting these on chain uh because
of this like Global like incredibly
neutral settlement layer that you can do
like really cool stuff and composable
stuff
with who go who goes with coars you are
using them I can go general purpose
NPC well you buil them I think I mean
with coars and MPC for coars I think one
of the nicest examples is actually what
you are doing and this is essentially
doing private proof delegation so with
zero knowledge proofs if you want to
generate a proof where um like the
witness gets particularly big and you're
doing it client size and maybe it's your
phone is not uh powerful enough or you
don't have enough time to do it on your
phone you might want to Outsource it and
so you see all these proof markets
popping up that offer services that you
know can generate your proofs for you
but if you have any notion of privacy at
all or if you care about the witness
data and not leaking this in the clear
to everybody then you might want to do
this in a privacy preserving way and I
think this is where coars enter the
story so doing yeah private Pro like
proof delegation but maintaining privacy
in an mpca I think is the one real sort
of awesome use case that uh coar offer
that wouldn't be possible otherwise so
like in yours now you don't do proof
generation on the phone you Outsource it
to the network and then I think for
general purpose MPC um I think the thing
for me this is the most exciting part
because there you start to now be able
to collaborate on private data across
multiple users so I think ZK is great in
the sense that it gives you like this um
sort of control over your data but in a
way it restricts you because it's like
okay I have control over my data but now
it's stuck and uh I can't share it with
you and sometimes I want this sort of
flexibility I don't want this all or
nothing and so if I have this
flexibility to say okay I can share it
with you and you and you or I can share
something about it with you and you and
you and we can compute over it together
um then this is great so for me this is
like the real kind of new thing that's
opened up by using APC in a in a ZK
World let yeah so I personally feel like
ZK by itself is quite lame for the use
cases that we're thinking about which is
social applications like I feel like
social is inherently like multiplayer
you want to get like a bunch of people
involved and the coolest applications
there involve multiple people's private
information and for that MPC is a
perfect fit so I would say for coars the
thing that's more exciting um to me
personally is the the idea that you can
actually generate proofs about a group's
data so it's like the other side of the
coin and I think in general like NPC FHA
all of these things uh cool applications
or design patterns or like uh one thing
that we're trying to explore is asking
questions to your social graph asking
private questions specifically so one
setup here is that like Richard could
like have his like private data uploaded
in some like encrypted form or whatnot
and I can just like ask certain queries
or I can ask questions like hey like who
here wants to join the hackathon with me
like do anyone in my social graph meet
these criteria and wants to like be part
of this group um and these queries would
only be decrypted if they're actually uh
satisfying that criteria so I think like
the MPC FHA angle feels a little more
exciting for
that absolutely I wanted to also so this
interesting theme sort of came up about
making connections so from Web Two to
web
um from one note to another in your
graph and it's also kind of making
connections between The Primitives like
karks is a good example mpf is a good
example so one question that's always at
the top of my mind is security and how
security assumptions
compose both across Primitives so what
are so you are introducing new
cryptographic assumptions how do these
compose um and also across applications
and in that case it's more about threat
modeling so for example if you're
relying on say the Vanos email format um
and they Chang it let's say um or yeah
you're um relying on like uh some dkim
servers some registry like how do the
threat models um compose um so I'm still
curious as designer
how you reason about that first of all
and also how you communicate it to your
users how you educate your users about
it all right I'll go first um so I think
because ZK PDP uh is building like a
financial application if you will uh
we're dealing with like movement of I
guess stable coins on chain so there is
real value t to it uh we do like treat
security pretty seriously uh both on the
cryptographic side and on the
application side um I think on the I I
guess overall we see like security as
kind of like how comfortable are we like
securing like this dollar amount over
this amount of hours uh for example uh
and I guess like different Primitives uh
that we use uh I think fall under
different parts of that Spectrum
uh for example like email may not be I
guess the most I guess um
like yeah like gated and secured uh for
example whereas like behind like gated
like private API with 2fa uh and
everything um uh yeah the data might be
more secure so I think we do account for
all that in like how much we allow like
the max transaction limit uh to be in
some of these protocols and I think yeah
I think we're constantly monitoring and
seeing as these Technologies mature uh
we feel more Comfort uh confident on it
securing higher dollar
amounts yeah I can also address trust
assumptions on the ZK email side I guess
we think about this in two ways one is
around when things update so you say
your email template updates or the Deon
registry updates it's one very easy to
change that so we have a very simple
Builder where you put in the new format
or the new pars thing and it
automatically handles everything for you
and so one thing is okay when a template
changes the developer ability to react
should be extremely fast and then number
two is we kind of want to make sure the
system is robust to any weird kinds of
like bugs or malicious DM key updates
and so one way we think about this for
instance with email based account
recovery where it really matters like
the entire security of your account
hinges on you know it really shouldn't
hinge on will this recovery modu get
hacked and so one thing we think about
is like very intentional time locks and
kill switches so for instance uh like
many of these accounts will have uh once
all the emails say hey I should recover
this account to this new address a onewe
time lock starts that's non-negotiable
on chain and so even if either the email
server got hacked or the dkim key got
somehow maliciously rotated or even like
uh you know the users Guardians acted
against their own will then at least the
account owner has a week to prepare that
and so I think non-negotiable timel has
also been quite compelling and the final
thing is giving users the ability to
exit so for instance for the dkim keys
if a user doesn't trust hey these
oracles theyve set for the dkim keys are
are going to always act correctly we've
made it so that users can say look I
have to approve all deck key rotations
that are applied to my account and so
now we kind of show you know in the
maybe in the ux hey uh confirm your
guardian emails and the relevant keys
and the user just uh kind of does say
some pass key authorization and that'll
automatically check okay I'm going to do
the DNS check did the DM Keys match okay
I'm going to rotate them on chain for
this user specifically so allowing users
to have control over their own Keys
within an intuitive manner I think is
also quite important so yeah these are
the three ways easy updates um uh having
it so that there's non-negotiable time
lockss and giving users control over
their own keys or parts or oracles that
they don't have to trust
it yeah sure uh for MPC and fhe security
is generally a lot more difficult like
there's been so much money being put
into ZK Audits and all these rollups and
everything that like people know how to
audit ciruits very well um and for MPC
fhe this is maybe becoming more of like
a nin thing so we'll see how that
progresses I think there are certain
things you can do to make MPC FHA more
secure one way to look at it is there's
this notion of Direct Security versus
delegated Security in MPC so delegated
security is when you take your private
data and you split it up and you give it
to all the NPC parties and they run this
computation versus Direct Security is
you are actually running this
computation yourself and you are one of
the parties when you actually want to
run compute over your own data and
that's like a simple way to say oh it's
your own data you should be a part of
the computation and I think that
simplifies part of the equation or some
of the threat assumptions but I think
for for MPC FP as a whole like we're
still trying to work this
out maybe I can add something on like I
think you talked very nicely about the
comp posibility but maybe I can try to
say how this translates to users and I
think to end users in particular like
now we start to hear that like oh people
do start to care about privacy and like
okay yeah we do have stuff to hide so
people do start to feel something about
privacy but I think they really don't
understand like the Nuance or even the
language around it so like explaining to
end users like consumers that we're
talking about now is
just hard and like uh but even like for
us now we start to kind of onboard
developers to use MPC Tooling in the
network and it's like even to developers
it's really hard to explain and I think
a lot of developers even have like a lot
of confusion around the security
assumptions and like it's actually a
little bit worrying and I so like we and
as you said like there's no auditing and
like there little sort of support to for
security in MPC and FH and this SL
slightly more advanced Primitives so at
least we talk a lot I mean like all of
us talk a lot um to each other about
like okay are we right in thinking this
and like with you I was talking about
private proof delegation and I was
saying like Okay just Outsource
everything and you were like okay no
we're happy to Outsource some stuff
maybe but like if there's like a
whistleblower or something that's you
know particularly sensitive or you know
then know like everything needs to be
done client side so I think having
conversations amongst each other to like
raise the general bar of Education like
e either amongst consumers and the
developers and like the researchers and
everyone um yeah generally just raising
the level of Education I think is good
and that's what we do and try to yeah
inform each
other I love that I think a lot of since
we're building at a very early stage a
lot of it is about talking to each other
and communicating well communicating
like in an intuitive way to users um so
to that end I I want to sort of find out
like some practical insights that you've
gained from your experiences deploying
these apps in the wild so by practical I
mean like insights that you could not
have gained from like just writing a
white paper um just implementing it on
in a hackathon for example um ux
features like I use to um make making it
clear to the users that they can control
the set of Tak key St um so like ux
prompts how these CU behaviors in users
I'm interested in that and um I'm also
interested in sort of how we compensate
for the ux hit so a lot of these apps um
they involve heavy computations right uh
for example making a ZK proof for
example having to be on online for a
long time um for the MPC or FH well not
for FH but yeah um so having to wait for
a long time be online for a long time
like these are ux hits that we have to
take how how have you been dealing with
those so that's on the ux site and then
I'm also interested like on the infra
site like actually what what are the
infra requirements like what
difficulties have you run into um
yeah let's go let's do the U stuff first
like so like what interesting user
behaviors have you observed um what sort
of ux prompts ux patterns have you found
useful and um how do you compensate for
like the ux hit the performance hit in
these
apps okay um
so for ZK PTP we have two flows of
interacting with these like
cryptographic Primitives that we use uh
one the first one is obviously using ZK
email um I think the main thing about
using ZK email is trying to get that
email in your inbox um to yeah to start
the proof generation process and that's
been a difficult thing to resolve you
could basically the manual way is you
have to open like the raw email uh copy
it and then paste it into the UI and
then click up on to run the proof
generation process uh so we basically
built uh like a o we like got a Gmail
API oath flow uh that will basically um
yeah oath into your inbox uh and read
the email and but uh keeping it
completely local in client side uh to
kick off the proof generation process um
so that has helped helped with ux a
little bit but it's obviously like a
workaround kind of thing um in trying to
smooth out ux things and also uh yeah
after getting extracting that email the
next step is obviously generating that
proof VMO email circuits are like
massive they're like they probably will
take like eight minutes to do client
side um but like 20 seconds to do on the
server um so we pass it all through the
server and so far like I guess all of
our users are fine with that uh I think
um yeah I think it it's yeah they're
okay with that leaking that level of
privacy um uh yeah do they know that
they're sending the pl Tex email yeah
yeah yeah we uh yeah we disclose
everything um to to the user uh that we
are doing that um yeah and then I guess
the second flow I was going to talk
about is we also use like TLS notter uh
which uh I guess for that flow you
basically need to have the US users like
like credentials in order to generate
that like NPC proof so in order to get
that you basically need to install or
create a browser extension uh to scrape
those like that request and response uh
in order to pass it to the NPC proof um
and of course all of this is done local
in client side um but yeah I think the
reason for that is that's kind of
non-negotiable like us like storing
cookies on a server uh running cookies
through a server and their credentials
is like a complete noo whereas email is
a little bit more okay uh in terms of
privacy um but yeah that that's also a
kind of ux hurdle we had to deal with
like trying to get users to install a
browser extension and going through that
flow yeah maybe one thing Z email
learned a lot from zkp Top is that yeah
it's always important to have the clear
user flow so actually after you guys
added the Google o flow and realized
people are actually using this we added
it to all of the exting KS too it's like
you can because we noticed hey like as
long as there is a way for users to do
the easy path and as long as we that
means we have to offer a way for the
self-hosted or fully private path and so
it's kind of as long as that path exists
it's kind of fine to have an option for
easy users who don't care to just use
the kind of simple sign in with Google
select the email move on path um as long
as it's possible for the people who
really care about privacy to get that
privacy they want either they manually
upload the email they select do it
client side they're willing to take the
ux hit in exchange for privacy or we and
this is one of the advantages of having
a totally open- Source organization is
that all of our repos are open like you
can go if you don't trust DK pb's front
end get the or you don't trust zk's
frontend go go to the GitHub repo clone
it locally run it and if you really
really care about privacy there's always
ways to to get around the ease of use uh
turn keys that we've put into the UI but
for me it's kind of like we've learned
okay as long as there is the easiest
possible path and a way for for someone
who cares about privacy to do the
private path we feel like that's been
like a good enough mix of things even if
people in general don't necessarily
always do the private path um so that's
one ux pattern we've noticed has been
really nice
um yeah yeah um bunch of thoughts here I
guess first one is about privacy and
like I I feel like one of the main
appeals of building consumer apps with
programmable cryptography is is the
Privacy you get right is the choice in
the consent that you have and that is
like one of the major reasons why these
Technologies are so powerful but I feel
like if you go down the street and you
just like talk to people I think what
I've noticed is people just don't even
understand privacy from your peers
versus privacy from the server like the
simple concept of like hey they look at
your venmo history and if you look at it
you can have like venmo or whatever
payments app you use like you can have
transactions only visible to your
friends only visible to yourself like
people think when you set your
transactions to be only visible to
yourself like that is privacy right that
is like just privacy in general that's
what that means but it's like a
completely different concept when all
this cryptography offers privacy from
the server which is really what we're
aiming for right like we don't trust
server to get hacked or to be malicious
or all this stuff um and I feel like
this this is really like a critical
question we need to solve in like
communication and design of how do you
actually convey this to users um so
here's here's one idea I can propose
which is like from from Rachel uh at
cursive and also Tomo from the EF like
they're both wonderful designers and
they have this idea uh which they can
talk more about of like hey we should
have some sort of like standard UI kit
for like communicating to users like
when you see this interface it means
it's actually private from the server
like this looks totally different it
feels totally different uh it is
different um and that's actually
connected to the technology right
because right now there really is no
difference and people don't understand
that so I feel like having something
like that where when the user actually
uses the app that would maybe change
their perception things a little bit you
mean like a incognito mode or something
yeah yeah something like that like
incognito mode like it feels different
because it's like dark yeah right it's
like or the I think of like the TLs like
green lock icon like at the very least
having some visual component where it's
like oh it's not like a standard or
something but it's basically this Norm
you assume that if we have this green
lock icon then you your connection is
like more secure in some ways and we're
just going to all like uphold each other
to This Promise because at the end of
the day like this is all up to like
people building apps to just agree on
and to like call out the people who
don't follow this and to all work
together to
communicate I think that's a super nice
point and like if you look at
cryptographic papers or whatever when
they like draw the protocols and The
Primitives like they do have a sort of
like it's hashed box like it's there's
lines in the box when things are secret
shared or it's a clear box when it's in
plain text or it's black whatever so it
does exist and I think this is nice but
one other point that I was I wanted to
mention was a bit on still on the design
side and also from Rachel I guess or
from cursive is like that you really
play with the ideas that you know like
the concepts that these programmable
crypto Primitives give and you sort of
yeah you play with them in your own
minds and sort of somehow translate this
I don't know about design or how you do
it but like you somehow translate this
to the user so like downstairs in the
museum there's these art pieces where
there's the QR code that you can scan
and input an emotion and like it
explains like Hey we're going to send a
hash of this and like prove that you
know the pre-image and like this is so
cool like even just showing people the
language and showing people like just
mentioning it just saying okay this is
what's going on here I think makes
people aware and like it's like okay
cool I'm doing
some crypto yeah and I so I was just
getting lunch with Gordon who's like the
artist behind that piece like basically
like uh we were talking about ZK
cryptography for for a while for a few
hours and like he made this wonderful R
piece explaining how you can keep your
emotions private blah blah blah um but I
feel like what what came out of that
conversation is that the most important
thing for all of us who are building
apps in programmable cryptography is
communication like we cannot just be
technologists like if we want to
actually build apps that people use like
we need to communicate and we need to
talk to people and like explain hey this
is what privacy means this is why you
should want it this is what
decentralization means or whatever like
communication is arguably like more than
half the job you can't just build the
technology build The Primitives and just
like throw it out there and hope
something Good's going to happen but
it's not even just regular communication
it's like you make it look cool and fun
and entertaining and like if I'm using
an app I gen okay unless it's like a
super serious thing that I want actual
privacy like real real privacy for fine
but if I'm just like using it up I'm
probably doing it for some sort of
entertainment or like some fun or to
like engage with my friends or whatever
like and then having it like look cool
and feel cool and feel like a shiny cool
up then it's great and I think this is
something that you do well like uh it
feels cool I want to be part of it so
yeah I
think yeah like that's what's cool about
cursive is like they make it like joyful
social um and like uh they sort of it's
sort of turning that um privacy as like
isolation and darkness kind of metaphor
on its head so um that was really cool I
I think yeah um all these ux insights
there's no way to get them without
deploying in the wild without being in
production um I guess I'm also
interested in sort of on the back end
like um the on the infrastructure side
um so I I guess I have two sort of
questions about infrastructure first of
all um is it expensive to run these apps
so it's a leading question cuz I know it
is I want to know how expensive and then
like basically what improvements do you
see in store what improvements are you
excited about
my second question is sort of a spicier
one and it's about um decentralization
so for
example for example worldcoin um there's
secret sharing
their Iris codes using
teso um to three servers so to me three
is a small number um how do we yeah I
I'm wondering like another example is
TLS notary
so they rely on a set of trusted
notaries to be the other party in the
it's it's kind of an infrastructure
question but it's also kind of a
decentralization question like um
underlying these Primitives like what
implementations and what infrastructure
are we actually using um and yeah what
are your thoughts on how how this will
develop should I start we laughed when
you brought this up and I wanted to
explain why we laughed and I don't know
if I should say it like in front of a
room because we haven't discussed this
at all with the teams but like so like
this week was the first time we deployed
let's say co- snarks in like prod like
property so like this week is it's like
fresh out of the oven and it's like
messy it's been a bit messy it's all our
fault they didn't do anything not like
so like um so so the situation is this
like we have established a network so T
is running a bunch of nodes cursive are
running a bunch of nodes and psse are
running a bunch of nodes and they all do
computation they do a multi comp party
computation between them and produce a
coastar and so some of the things you
might learn when you go into prod that
you wouldn't learn in a hackathon like
as you said about like auditing and
security like being immature for MPC and
F and the more advanced things yeah like
infrastructure and support there is
super uh not in place yet so like
yesterday we had um a bit of an incident
where two of the nodes of one of the
parties died and they had one node left
and so this there our
party but like okay there was some sleep
involved because they stayed up all
night to finish the thing to actually
get it done for Decon so it's a it's a
good reason but uh yeah like one like
just the noes died and they just needed
to be rebooted and um that's it but
there was no like alarm or notifications
or like anything set up you know this
kind of like support that just keeps
things online or like small stupid
things that are like the absolute like
complete like essential things in any
sort of advanced Tech not even Advanced
but like used Tech like the the most
basic things are not there and we focus
on just getting things working but like
yeah this sort of support to keep it
going it's just not there but um um and
in terms of cost I also don't know if I
should talk about this without knowing
exactly but like I think for us setting
this up I think is it for each party I
think it's about $7 per day for like
seriously beefy machines so yeah not too
bad yeah I don't I don't have much on
numbers that I know of uh concretely but
I think in terms of like what you said
like this is not something that we would
have learned this quickly if we didn't
deploy it right like this uh we were
using Co snarks for like the leaderboard
for like handing out merch downstairs
like if you tap like 40 people you
generate a proof of it and like you can
get a shirt um the shirt that I'm
wearing which is super sick um but like
we learned of this incident like
literally 30 seconds in because people's
leaderboards like weren't updating and
they couldn't get their shirts and like
they were were so mad they were like oh
where's my shirt I want my shirt like my
leaderboard isn't updating so I feel
like having that feedback loop
instantaneously is like super useful and
we like we learned this lesson and like
we fixed it overnight and like now we
learn something new maybe I can add one
good point and then I'll be quiet but uh
like the good point is that we had many
more we generated many many more coars
than we expected so like the load was
much much higher than we expected and
the reason it went down was like yeah
like it was not because of let's say so
much load um but like we are handling
much more throughput than we expected we
could in like pretty good times so
that's the good outcome that we wouldn't
have also expected without going into
prod and like a lot of it is because of
the response of people at the conference
actually like people are super curious
and cool to try it out so that's
something we wouldn't
learn yeah that's a good problem like
higher than expected through pit and
that's a good like alert system angry
users demanding
shirts those are like the joys of
deploying in the wild and having real
users um so I do think I'm supposed to
open to questions from the audience but
I don't see any questions do you you
don't I think questions after that time
oh okay so we have 9 minutes left and
then we'll open into questions great
because I'm really not done here um yeah
I think the second part of my question
was like what do you see in the future
like future improvements that you're
looking forward to I in particular um
want to ask about mobile interfaces and
whether yeah that's a priority for you
guys what challenges do you see like
sort of what blockers do you have right
now um and what challenges do you see in
future or what needs to happen to make
um like a joyful mobile experience for
the users
uh maybe one thing we've thought about
on the infrastructure side and on the
mobile side is um because proofs cost a
couple cents on a server and will cost a
couple more cents if you do Co snarks um
there is quite a pressure to push things
to the client side because then it's
free the user handles the computation
for you and so one interesting thing is
that if ZK proofs get really big and if
people are doing you know not just
hundreds of proofs a day but thousands
or hundreds of thousands of proofs a day
then there's a really big pressure
economically to create client side
proving I think that's quite cool
because client side proving is kind of
the Holy Grail of where ZK privacy comes
in you don't actually leave privacy to
anybody else and so I think that's it's
actually potentially a good thing that
it that uh we can incentivize This
research um and so far there's only like
you know maybe two or three
organizations I can think of that are
really invested in okay really we should
get client side proving today because
you kind of like you value in crypto
often cruise to the points of
centralization and by saying we're going
to do client side proving you're
removing that point of centralization of
We Run The prover we make the money um
and so it's not currently economically
advantageous for infrastructure
providers to do client side proving but
when applications are like we don't we
don't want to pay you know hundreds of
dollars a month or or thousands of
dollars a month to you then all of a
sudden applications are now incentivized
to use somebody who is providing that
client side proving and so um yeah
that's one thing that I'm excited about
in the future infrastructure wise and
also for mobile proving we've seen some
teams like mpro like ligron like teams
in psse like Noir really be like how can
we get this client side proving done um
and yeah we're we're excited to see more
of that there's there's a lot of tech
that has been underutilized like web GPU
simd acceleration things you can get on
mobile devices that you need for these
email proof because people most of the
time are just going to scan a QR code
sign into their email on mobile and make
a proof and you want to make that flow
as fast as
possible yeah I think for us uh we Echo
a lot of the same things uh you said
about client side proving for our ZK
stack um I guess for us we also since we
also use TLS notary and the MPC side um
we're I guess we're especially also
really interested in building like a
mobile base flow uh to enable like yeah
enable some of our
marketplaces and the bottleneck there um
is I guess the it's also memory where
like yeah like like mobile has just much
lower memory um than on I guess browser
uh but yeah also like bandwidth and
internet connection matters a lot in NPC
um and when you're on your phone um
you're typically like out um so uh you
may not have access to like high-speed
internet for example to like finish
generating these NPC proofs and as a
result like the connection drops and
which is a terrible user experience uh
for some people but I think there are
quite a lot of like improvements like
like coming soon on the NPC front on the
TLs notary front which uh yeah cuts the
bandwidth requirement by like I don't
know like like a huge like Factor um and
yeah we're pretty excited to adopt that
and yeah support mobile um as a Next
Step yeah I think like mobile is super
interesting to us just because it has
such a wide toolkit for social apps like
things like Bluetooth NFC like web
Bluetooth web NFC like they just suck I
don't know they just don't work um or
like not supported by a lot of browsers
I think apple has a lot of security
restrictions on on some things there um
and it just sort of widens the toolkit
of things that you can build uh in the
social context um so I think like mobile
to me is super important and it also is
just like a much more buttery experience
than a than a web app but then you have
the question of like how do you get
people to download a mobile app I don't
know yeah there's there's these things
called app clips now
you don't need to download a mobile app
tell me about app
Clips yeah it's um yeah so there's
basically these app clips and instant
apps on the Android store where uh like
Google or um Google and Apple offer ways
for you to like try out the app without
actually downloading going through the
App Store so you basically scan a QR
code it load some like temporary like uh
like a binary on your phone and you get
to interact with some limited features
of the application without needing to go
through the App
Store maybe like one point that kind of
touches on another question you wanted
is um like something that I'm excited
about is something that I think both of
you mentioned a little bit is about the
different models of NPC so like the one
where the user is actually part of the
computation or when uh yeah it's a
different like you delegate fully
everything to the network um and so like
in some cases it can be that you know as
long as one party is honest that you
know the whole thing can remain secure
and so if I'm involved in this protocol
and I know for sure that I'm honest then
I can say that this is a good like that
this protocol is secure and there's no
collusion happening we're like quite I
think not there yet at all for that but
like I would love to see this happening
this would be super cool oh absolutely
that's like um one of the interesting
thing about CO narks as well is because
of the security guarantee from the snark
site you can relax requirements on the
NPC site and so yeah all all these sort
interesting like paradigms emerge um
when you're like confronted with these
use cases um where and they they can
like these use cases become interesting
in applications like maybe in Academia
they were not interesting theoretically
but yeah like in practice you realize
okay like this is like an opportunity um
to like get some performance gains yeah
so that's a really cool point I guess
with my remaining 2 and 1 half
minutes um I want to I want to find out
what you're excited about so yeah what
what applications have you seen that are
like wow far out there or what
applications can you imagine um what
applications um would be like holy grail
for you um and this can involve like uh
this can be extensions of what you're
working on now or it can even involve
like um far out Primitives that you're
looking at like witness encryption or
something um yeah I'd like to hear um
what's in store for the next few months
years I personally really want to see
more digital signatures and more ZK po
of those signatures I mean emails is
just one example but if you can get for
instance the designed website standards
to be more adopted you can get any
website frontend now approved onchain
and you can already do this with some
things like Forbes in Italy um but it
would be great if more websites did this
I'm also excited about um pufs like
physical unclonable functions being the
route for new open source tees I think
uh like uh open source tees is kind of a
holy grail and gives us the ability to
to do a lot of this private computation
without having to rely in uh you know
Intel getting hacked every two years um
um what else I'm excited about witness
encryption I think more research around
new kinds of privacy modes and maybe
I'll even that Andrew talk more about
that and um yeah I'm also excited about
more far out things like making certain
versions of IO a little bit faster or
making um having NPC F be faster things
like we've seen like Apple's W they just
release like a ML and fhe kind of
application and I think seeing more of
that um more Enterprises get into these
privacy protocols make them faster um
yeah so for me I guess um yeah like
making things faster like harder better
faster stronger is always the goal but I
think I would love to see more like what
you are doing actually and I think um
there's not so much incentive to
actually play with these tools and I
think the gain from playing with these
tools and like onboarding users and
educating them is huge but somehow
people don't do it enough and so like
there are s like yours like Tonk they're
building these you know like uh Salon
basically where EAS Speak Easy yeah
exactly where you can meet your friends
like and have this private environment
where you can yeah like come in if you
can prove some stuff and like yeah this
sort of transitive trust idea like all
this kind of cool stuff um like this for
me would be great I'd love to see this
actually happening more and more yeah
I'm super excited about new applications
of MPC so specifically this concept
called digital phermones and the idea
here is that like real phermones are
these chemical biochemical signals that
you send around to find people you're
compatible with and what if we could
build the same thing with MPC but
related to Digital Data digital
information so you have these signals
that you send around and because
everything is private everything is safe
just like your normal phermones are you
just get to see like where your
compatibility is you get to see who you
match with who you might be in a group
with who you might be able to do stuff
with um and it just happens naturally
and so one way we can actually implement
this is through a new scheme uh we came
up with called Trinity and Trinity is
called Trinity because it's a
combination of three schemes
specifically kzg witness encryption uh
garbled circuits and plunk uh so the
rough setup here is that you have your
own private data and you just upload a
kcg commitment of this into the cloud or
wherever and like people can just start
asking you questions people can start
making private queries based on this
data right and essentially like you only
need to respond to these queries if you
actually meet those criteria like these
these commitments are like fairmon from
your data they're like hiding
commitments to your data um and you can
just like naturally have other people
around you ask questions and say hey
like am I compatible with this person
like uh am I able to do something with
this person uh and you can just discover
that and it's only possible because MPC
uh enables this privacy and
safety yeah I I think I'm really excited
about like
more practical applications that like
use these schemes that are like um being
like more and more robust and secure
over I guess the next year I think a lot
of protocols I think ZK email went
through a audit um and a lot of these
other like protocols such as tlsn will
be I guess in the next year or two and I
think uh as these protocols become
faster and easier to use I think we'll
see more and more practical applications
like ours um and yeah like stuff that
you can do with web two data uh come
online and yeah I think I'm just really
excited to see like combination using
schemes these these different schemes in
combination with each other in
production yeah very cool um so I think
now we're supposed to open to audience
questions I still don't see
them oh there they
are so we'll start with the most
uploaded which is um yeah what's the
path forward for mobile do we need a new
browser who will fund
it I guess like we already addressed um
sort of Outsourcing heavy computations
from mobile whereas this question is I'm
I'm interpreting it more of like um sort
of the current standards of mobile like
you mentioned there's aets now but
there's lots of um sort of restrictions
on mobile apps that make it hard to say
directly interface into like TLS notary
let's say um so like how do we deal with
these standards that are um incompatible
with The Primitives we need do we yeah
how do we deal with them do we like
start from scratch with a new browser
what what do you guys think
for mobile specifically like I feel like
we just need more people building mobile
apps and just experimenting like that's
basically it like there's how many apps
exist today on the App Store that are
like uh mobile apps with programmable
cryptography running clients side like I
I don't I don't know we we don't have
one um so I feel like we just need to
learn the lessons there pretty
much yeah I agree with that I think we
need yeah more Dev tooling more
developers uh building these kind of
program well crypto um mobile apps um I
think in particular like there's a lot
of pain we experienced trying to do this
um in like yeah the main requirements
being able to extract like the
credentials um through like a web view
like privately and keep it local and
apple just doesn't give you or react
native or any of the mobile Frameworks
just don't they don't give you that
tooling right now so you have to be
pretty hacky um uh when you're
developing I think on the mobile browser
side one thing we really want is uh
there's this kind of vectorization
called simd and you can only access
if we could access the full 256bit
registers you could do ZK proofs a lot
faster um similarly web GPU exists on
most laptops but doesn't isn't doesn't
have very good support on mobile so I
think in the short term if browsers can
ship those that would be super awesome
and then uh but I do think the large
browsers will have that eventually in
Mobile within the next like year or two
and that'll help accelerate a lot of
these client side
proofs cool um okay what are you going
to have privacy by default the hard path
not just privacy by complicated UI and
default no privacy and limited
security I don't I don't know how to
parse this do you guys get the question
um I guess it's kind of responding to
something I used that about yeah like
it's okay to present an easy path as
long as we make available the fully
private like hard path of like
completely self-hosted approving
um question mark maybe one thing I can
clarify on that is I I think it is
possible to have decent UI for things
that are private like for instance
dragging and dropping the email
on on like a computer is not that bad
like it's still an option UI and it's
definitely harder than sounding with
Google but it's it's not like you have
to download something and get clone and
run locally like you can still give
option to do that in the UI and we try
to do that where we can and so I I do
think yeah it's a fair point that for
people to self host is maybe not the
best way to offer privacy but I do think
you can have buttons in the UI that hey
this will take a little bit longer this
might require an extra action but it'll
private how far are we from ZK based
trans positive trust graphs of 10K plus
users in
doubts good
question I'm looking at you I would say
uh and I probably shouldn't say but I
would probably say it's closer than we
think I mean it's a hard problem and
especially if you want to do this fully
privately like suppose you want to do
like a full trust graph in in MPC you
need to do like essentially a full
search because almost everything is
connected so it's super inefficient and
it's yeah not not so good now but I
would imagine that like I mean the speed
at which things are improving now I
would say not too far away yeah I think
technically it's possible for me it's
like a like how to design this like
protocol Wise It's like how do you do
this the right way where this is like
fair for people there's a lot of like
tricky I don't know moral uh product
questions that are uh to be answered
here mhm
yeah I was also thinking just now that
um fhe is one example where like you
cannot offload and don't want to offload
to client side you fully want the server
to absorb the cost so yeah like I guess
um and the tradeoffs you know oh sorry
for gesturing this is just my my opinion
um like the tradeoff is um just
individual users doing less work
um and that could maybe allow you to
scale to 10K class users but yeah like
you said there's a it's a big design
space um all right how do you solve the
issue of querying large databases
efficiently in MPC all queries are
linear in the database size
no maybe one quick thing is like apple w
like their new F system solves this by
one like bucketing so you say look we're
going to make Square of end buckets and
we're going to send it to the right
bucket then you leak a little bit of
information which is which bucket did
the query go to so they send square root
of end queries and then it's like well
you know which which query is the right
query you don't know and the user throws
away all but one of the queries so I
thought that was a kind of clever way to
you know leak a little bit of privacy
but then undo that leakage uh and have
it be a bit more
efficient oh okay so it's like linear
over square root and buckets and you can
keep kind of recursive doing the square
root of n uh I see
yeah how about I know world does have
this um they do a database search per
new Iris code so yeah we do actually
search over the full database for this
and like it is quite optimized and it's
quite efficient but like it's yeah
heavily specialized optimized protocol
so far um but I mean there is work
definitely on um
like like lookup tables and you know
like there are ways I mean there people
are looking into this and coming up with
like clever tricks like this um but yeah
so far it's
uh people are looking into it but it is
still an issue we need more P research
PR is really cool private information
retrieval isn't P also like linear work
on the server site though yeah yeah yeah
right now I think they you just like
encrypt the whole database yeah but not
for the user yeah um cool so I think we
are over time now um and I really love
this panel thank you so much to the
panelists thank you thank you you
guys I actually had to sit in the
audience because I wanted to enjoy this
full panel so thank you guys so much um
our next talk was Will rum adds four
thank you
all right hi everyone welcome back next
we have a talk on little things we've
learned about FH let's welcome CC on the
stage uh also there will be a QR code on
the right side of the slide so feel free
to scan the QR code if you have any live
questions for our speaker so now let's
give a round of applause to CC on the
stage
hello uh thank you Teresa uh um hi
welcome here um so I'm cilian from PSC
um we're talking about F FH today so
here's my selected uh resume to fit my
narrative uh first like uh in August and
July this year I'm very honored to work
with ZX Park our lab and PSC Fox on the
uh FH project called
fanzone and before that uh in the past
three years I've been um working on ZK
ebm projects uh with kimy there and okay
with bunch of many people and more
before that like I was working on um
different various C applications uh in
PSC so uh I think in summary like what
have what I haveen what I have seen is
like a rise of the uh
computational Primitives on
cryptography so what does that means
like we discovered a bunch of
computation
Legos uh this Legos starts with Gates
like this you can uh add numbers
together or you can multiply numbers
together
um and we call these Gates uh arithmetic
Gates and if you're are going uh coming
for programming world uh you probably
seen this end Gates or gates exort gates
and not Gates and you can fit bits
inside it and do operation with it said
uh these are called bullan Gates um so
these are kind of abstract uh models uh
once you get this you get the whole uh
computation you need you can uh serve
user with um different kind of
application logic uh how does that go um
so first you have Gates and then if you
combine these Gates together you get
circuits and then if you build uh
language and compilers on top of them
and you feed uh developers some coffees
and teas and they'll build amazing
applications and to happy
users um so I think that's what happened
in the ZK past uh in the ZK we kind of
have some uh arithmetic guge uh that
allows you to um perform computations on
secret values and now uh FHA we are
getting new sets of Legos and they
unlocked new sets of capabilities and
this is what we'll dive into uh
today so before that let's do some recap
on ZK calculation so when we talk about
computations like uh we we usually start
with calculations and then we build more
abstractions and then uh we can do
computations on actual application
logic so here is a circuit uh that looks
like a stu board they have some
prefilled values seven and three you can
fill in some initial value five and then
you multiply together you get 35 you
plus three you get 38 you can witness
some private value too and then you get
the result 40 and then you can uh send
the input and output to the verifier and
without sending all the computation
trays in the middle and in this way uh
you get privacy for your uh private
value uh you also get the computation uh
compression for uh people call this the
sness and if we accept some more
abstractions um so we wrap of Developers
are very good at uh turning your
application needs into the computation
of bits and
bites so uh we can do some high level
logic like this uh for example you have
ID one two three that is uh reside in
the ID registry um so uh this
computation result tell us this is a
valid
ID uh as a this do you can can insert
some uh secret value in the this secret
field of ID this ID have some certain
attributes and then uh the whole things
combined together that shows uh you know
a secret uh so you are the owner this
dog is the owner of
id123 and then furthermore this id123
has a ag field says 19 uh so that this
dog is 19 years old but the dog want to
tell people it's 19 years old the dog
want to tell uh it's uh greater than 18
years old with just one additional
computation step so uh that works well
for if your user is just one dog but now
like uh if you you you want to build
applications that interact with multiple
users uh like this uh dog and cat and
they want to decide what to for dinner
either Cy or py but like their opinions
are very sensitive so secret that need
some cryptography that can pretend uh
protect you from State actor
attackers
so um they kind of that's that's imagine
we we don't uh have any cryptography and
we Host this computation and The Trusted
third party like the the the horse below
and then and the dog sends uh their vote
one uh and the uh preference for PTI
zero and the cat sends uh the their vote
one and uh the vote for partti then we
perform some computations uh we want to
add the Vols together and to get the uh
final preference for the for for the
dinner but then like you see like this
requires the interaction of the Dog
secret and the cat's secret and then
it's not achievable by the uh the the ZK
gate so uh that's where FHA comes to
help so FH stands for uh it's a short
for three words but uh I'm not going to
torture you with that nerdy details um
uh I going to uh redefine FH as just one
word and it's a computation over encrypt
data uh as people say like the ticker is
f and
so um what does mean like computation
over uh encryp encrypted data so you
basically get this two new Legos and
then you can have encrypted data from
player one encrypted data from player
two and then you add them together you
get a computation result and so when I
heard like the encrypted computation
over encrypted data first time I didn't
realize how powerful it is or like the
significant it is but it uh if you see
here it kinds of builds a boundaries
between two players and then you let
their secret to interact with each other
and you get a computation
result um so now like with FH you can do
uh the dinner voting properly so the dog
send the encrypted uh preference cat
send their encrypted preference and then
you use the uh new FH gate and to add
add them together to get a encrypted
computation result and then you have to
decry it to get the actual
result so I think balic has a saying
like all the technology we have is kind
of a simulating it trusted third party
and I think we uh like from this example
we're kind of seeing this phenomena like
this uh horiz on the button is kind of
like a trans party and when we're using
uh FH and without it like the the applic
the application logic looks similar but
like it's kind of wrapping on another
layer of
security and uh
for the user from the perspective of
user they all they see is the same they
input some value on their browser and
then they got some values from their
browser but like the uh there are
difference behind the scene and there
are different security and Trust
assumption behind the
scene so uh why are we not already using
FH now uh we kind of already like uh so
in the basement you have frog Zone from
uh ZX Park uh I highly recommend you to
play
it um but there are three main problems
of FH right
now uh first is uh the computation is
costly uh let's say you want to send one
bit of PL text uh from this do to the
server you have to encrypt it and in
this encrypted message is a data itself
so it has some size and how big is this
data
um so this data takes uh six bytes it's
kind of
um it's amortized and it's kind of uh
grows linearly it means if you have 100
bits you multiply uh 16 bytes by
uh but the terrible part is the
computation part you need a server of
I highly uh recommend you to play the
Frog games on the basement to feel that
like $10 per hour like
feeling
so the second problem is the
verifiability
um so uh you're getting this uh
computation result but is this
computation result coming from the
correct computation step or the
incorrect computation step uh to be
honest like you cannot really tell like
it needs extra work you either wrap
another DK proof on top of it you either
do some like message check or something
to to either guarantee kind of integr
um it's it's a problem people are
actively solving but it's still a
problem so the problem number three is
the decryption problem so after all the
computations we're getting the uh
encrypted computation output but how do
you decrypt this how do you remove that
elephant from the fridge um so you need
someone to decrypt the the message but
uh you can you know give the decretion
key to a centralized uh party but this
is this is like you're are not doing FH
at all um but the concern is like uh if
you like if someone have has the ability
to decrep the output can they also
decrit other users input and this uh you
know this makes the whole like FH
security
theater um so uh the other way to solve
this is you use some threshold
decryption scheme um so every uh
encrypted output you need all the party
to derive a decrypted uh decretion key
share and together uh they have to
collect all the decretion key together
to actually see the output so if the dog
did not give um it's uh decryption key
to their input the other people will not
able to decrypt the dog's
input but uh the problem here is the cat
uh if the cat ghosted then nobody nobody
can actually decrep this output and then
this this secret will be secret
forever so uh let's give a quick recap
uh the message is simple um in ZK we
kind of have uh computations on top of
your own
secret and for FH um we can engage with
other Secrets uh so you can build uh
applications for multiple uh multiple
peop and that opens a lot of doors to
many new
applications so I expect like you will
heard like the world FHA in the like
near years there will be more talks more
uh in the next step
like uh this is a kind of trending topic
and lastly uh I want to direct you to
play the Frog crypto and a basement uh
to feel like how early days of uh FH
feel like uh also if you're coming for a
developer background here are some
reports you should check uh the first
two are from G lab uh there it's a
library for uh multi party FH uh uh uh
pay attention to the branch because like
the latest call is living on some branch
and if you want to uh you deploy your
frog Zone yourself uh check the last
link you can deploy frog Zone and you
know it's early days things break so
expect some hi up on the Cod and yeah
that's all I have for you thank you so
much all right thank thank you CCE we
actually have a lot of time for QA so
feel free to submit questions uh let's
go from the first one on the screen what
are the best use cases you've seen for
FH so far uh that's a very good question
so uh for me personally like definitely
not for others like I'm more from like
economic background and I'm very
interested in like uh auctions and
volage things these are very you know
like old FFG applications they are they
are very ancient but I feel like uh if
we can do proper voting and proper
actions uh that would be cool but uh but
people like I think what makes people
exciting in the future is if you can
build uh some uh private State uh you
you can build a uh let's say P2P Network
you have a private State and then you
have some State transition function you
can continuously update State and then
you have some uh you can build a like
some kind of private blockchain and
private uh application to many but like
I uh I cannot say anything concrete at
this moment because I don't
know um and we have another one which
optimizations do you see possible to
solve performance issue oh
uh so um so this is uh what I heard from
uh our our uh colleagues uh P he said
like the last um so the latest
performance update was already in like
uh for that performance um improve
Improvement so we might be looking for
some like a new generation of uh
bootstrapping technique uh to to improve
their
performance uh when should you use ZK FH
or
MPC um so I so my my you know
over over simp
simplistic understanding of this is if
you're application involve just one
party then use DK if you have two
parties uh use M uh NPC if you're more
than three parties uh try FH all right
cool uh yeah let's wait a few more
seconds because we do have more time for
QA uh what do you think of tees as the
solutions for shared State shared
private priv State computation as a
performance solution over
FH good question I don't know yet I
haven't dive into this topic and so I
haven't developed opinions on
this all right
perfect okay um all right let's give it
another 10 15 seconds to see if any
more maybe a question for you like who
here have heard FH
before Oh okay almost everyone
okay who here have heard
indistinguishable AAS
before okay
oh nice
all right cool uh thank you CeCe for
your amazing
talk our next talk will be in 10 minutes
so see you guys
that
is for
all right hi everyone let's get ready
for our next talk on non-native
arithmetic via CRT codes by Liam Egan um
there will be a QR code on the right
side of the screen so please scan the QR
code if you have any questions for Liam
now let's welcome Liam on the stage
hi um I'm I'm Liam yep thanks for coming
to my talk um in writing the talk I
found
that I think it probably makes sense to
mostly go over sort of what non-native
arithmetic is and sort of build up to
the question because this is sort of an
idea I've been casually thinking about
for a while and I don't have like um you
know definitive answer to yet so yeah
um do I push the button or how does
that is this
working the the clicker oh wait it is
working
okay okay so
um for people who don't know uh what
what is like uh the context for all of
this so um non-native arithmetic is
something that comes up in snarks which
are succinct non-interactive arguments
of knowledge may have heard of like zero
knowledge proofs um and this is the same
kind of thing um so in a snark uh some
party the prover wants to convince the
verifier that they know some Witness
um and they want to do this by
generating a proof without interacting
with the verifier so non- interactively
and the proof should be small and uh if
it's zero knowledge it keeps the witness
secret um yeah and sorry for the
formatting I did the slides in Beamer
and had to import them to Google Slides
so might be a little weird but um yeah
so the way that we usually write this is
there's some C which is like a circuit
um that has some public in put X and
some private input W and the protocol
allows the prover to convince the
verifier that they know W by sending a
proof um so for example right you could
have some like chain State X which is
public some transaction W that is
private and you want to prove that you
know W for a given chain State and so
not all transactions will be valid um
and so that's what C
checks um
yeah so the the cor of important
takeaway for this from this for our for
our topic today is
uh that c is defined typically over a
field so field is like a place where we
can do arithmetic addition
multiplication Etc and uh that field
will be defined modulos some prime
P
um the field is s sort of like a free
parameter depending on the proof system
you can pick the field freely uh and
sometimes it's not so if you're using
like a stark you can sort of in
principle use any Fields just some
caveats but for like an elliptic curve
based proof system it's usually fixed as
part of the the curve which again
depending on the particulars is
something you probably can't
control um so the question that
motivates non-native arithmetic is what
what happens if we want to prove a
statement about some arithmetic that
lies in a different field than the one
that we're defining our relation
over so right suppose you want to verify
a signature that is defined over some
other curve externally to your proof
system right you want to
verify um a Bitcoin transaction or
something inside of
b254 and uh in that case both of your
Fields will be fixed and you can't you
know change them and they're different
so you have to simulate one field inside
of the
other and
uh yes so we need to emulate or simulate
the non-native field inside of the field
that our relation is defined
over um so just like as a simple example
of of why this doesn't work right uh
suppose we wanted to check that like 4 *
I think all the arithmetic there is
right and uh 4 * 5 is 6 mod s but then
if if our proof system is defined mod 5
then you know directly carrying out the
computation will yield the wrong result
so they're fundamentally different
spaces for doing arithmetic and so you
need to simulate the one inside of the
other um so what can we do uh the
situation is not hopeless uh like in
principle right this is this is a
solvable problem CU you can simulate or
you can encode any NP relation into an
arithmetic circuit over any
field um you know you can encode it into
binary digits and check that the digits
are binary and en code the bitwise
operations and so this is just sort of
like an existence proof but this is you
know very slow and we would prefer to do
things more efficiently than this and
intuitively you'd kind of expect it to
be possible to do something something
better because fields
are similar right they wrap around but
for small values they behave kind of
like the integers you're just adding
numbers and if you don't exceed the
modulus then maybe we can exploit that
somehow that's what we're going to try
do um
so the first observation is to check
modular arithmetic we just have to check
integer arithmetic because if you want
to check something mod R this is the
same thing as just checking some integer
relation for a
quotient
uh and in some cases this is actually
sort of Enough by itself so depending on
the relative sizes of the fields the it
might be possible to do this like if you
check that a b c and Q are all small you
can just check this relation as written
here directly in the larger field and
and the reason this works is because it
will never wrap around the larger field
um so if all the sizes of everything are
small or provably small then uh if it's
equal to zero mod P it has to be it has
to hold mod R um you can convince
yourself of this I think it's not uh
that strange right because if something
has magnitude less than p and it holds
mod P that means it's zero mod P and
since it has magnitude less than P the
only thing that's Z mod P with magnitude
less than p is zero so
um and so this this works sort of like
up to square root of the size of the
field basically
um and that that's coming from the fact
that we're checking a multiplication if
you were checking a degree 3 thing then
you'd want like cube root or something
that um but what if our you know
Fields not small or our modulus is not
small right maybe it's even bigger than
the prime that we're working over um
then then you can't like expect your
encodings of the small values in the
larger fields to behave well and in fact
it might not be possible at all if your
you know elements are larger than the
field that you're carrying out your or
you're encoding your relation into you
can't even commit to a big value in a
single field
element so this this technique I think
originally or at least I I first heard
about it from um Aztec but uh there's
this you know ancient um theorem the
Chinese remainder theorem that allows us
to work around this problem um and so
what that says is if you want to work in
a big
modulus it's sufficient to work in two
smaller moduli that divide the larger on
or that multiply to give the larger one
if they're
co-prime um and uh it's it's sort of
like you both sides of that are are
rings right so you can take a value and
instead of working mod AB you work mod a
and you work mod b and uh these two
rings are
isomorphic and
so people call it a residue number
system and you can represent a large
number mod AB by representing it by by
encoding all of its residues mod
different small primes that divide
AB um and I here I've written it with
two but you can sort of recursively
apply this this uh equivalence to
include arbitrary numbers of co-prime
divisors
um and
so remember we were working mod P and we
had some R and our R might be too big
but now we can pick whatever modulus we
want right we can pick a bunch of small
primes so it's always large enough to
recover the
uh value that we're operating
over um and so long as everything kind
of remains small that Q is supposed to
be a product but uh so long as
everything remains small um this works
and uh like before how we didn't want to
wrap around P here we would don't want
to wrap around M but here m is a free
parameter it's not fixed by the proof
system okay so now like a slight
digression to explain the
idea um read Solomon codes are an error
correcting code scheme that is
ubiquitous in in snarks uh if you've
heard of starks or fry this is you know
essential to how they
work um um and the basic idea is we have
some message that we treat as a vector
of Dimension K and we encode it as a
polinomial as the coefficients of a
polinomial uh and then that polinomial
we evaluate at more points so remember a
polinomial of degree K or k minus one is
determined by K points and by evaluating
it at more points you're adding
redundant
information and so like in the original
conception of read Solomon codes this
was to deal with the fact that some of
the information might be corrupted um so
you only need like even if some of the
data is is uh maliciously altered you
can still recover the original
message um certainly given all of the
points you can
recover
uh
so given a polinomial and we evalua it
at some set of end points this is
equivalent uh to reducing the polinomial
mod this kind of uh un like um degree
one ideal x minus
RI um and
so this Insight allows us to generalize
read Solomon codes to other like you
know domains um ideal domains and for
example algebraic geometry codes which
replace um polinomial and uh evaluations
with functions of some curve and
divisors uh can be cast in this language
as well and
um this is
also how we're going to introduce uh CRT
codes here CRT is still Chinese
remainder
theorem so the idea of a CRT code is
rather than encoding our message as a
polinomial we encode it as an
integer and then rather than evaluating
the polinomial at multiple points we
take the integer mod a bunch of small
primes and so you can think of these mod
small primes as analogous to evaluating
a polinomial at a
point um it's not exactly the same right
because the the ring you get from
reducing mod different primes is not the
same but the ring you get from
evaluating at a point is always the same
that it's not really important for our
purposes um yeah so if you have enough
primes so that the product of all the
Primes exceeds like the bound of your
your original sort of space of integers
that you're encoding into then even if
some of the primes are wrong in the same
way that with a read Solomon code you
can correct errors with a CRT code you
can also correct
errors um and this encoding
is the same as a residue number system
so you're taking an integer you're
reducing a mod a bunch of small primes
you're keeping the residues and you can
just work with
those um and for for those who are
familiar there's a lot of similarities
here with with how um you know Starks
work and uh other kinds of algebraic
proof type
stuff okay so this slide I just
screenshotted because it was horrible
mangled by the formatting
so the sketch of the protocol is suppose
we want to verify some non-native
arithmetics we have some system of
polinomial equations the F in in
different X's which are
integers and uh the fs have degree D and
all the integers are bounded
so in the original version of this right
we'd be checking um arithmetic mod some
other Prime and you can encode that as
an integer relation and so the primes
are fixed in advance and you have some M
which is larger than the kind of Maximum
value achievable by F uh as written it's
it's a little wrong because you'd
probably want to account for the
additions but you know something like
that and then you encode your integers
mod all the small primes as we
described and uh also provide quotients
for the evaluations of these functions I
guess that's written that those should
all be zero so maybe there's a slight
confusion there
but yeah so you prove your encoding of
all of the integers is um sort of within
its appropriate range and then you
choose a random subset of the primes to
test the relations over and uh for
Simplicity assuming the primes are all
like roughly the same size then you can
calculate the success probability of a
dishonest Prov pretty
straightforwardly um you know it's just
the probability of having like
some code word right some set of
residues that does not correspond to a
small integer uh or that's that's like
wrong in some position and then uh yeah
anyway
um yeah so it's similar to how Starks
work um
H
okay yeah okay so this is the
interesting stuff
um as described in the the previous
protocol um we're testing each encoding
of X is close to a small integer
directly you're just taking your set of
residues and like checking that it is
close to a small integer or an integer
within the right
bound um this used to be how like fry
based proofs did things but it turns out
that there's a much more efficient
batched proximity test so proximity test
here is you're testing the closeness of
the set of residues to its space of
correct messages and what people do now
with Starks is is uh take a random
linear
combination of encoded columns or
encoded integers and test that the
random linear combination is close to a
code word um so instead of testing each
one independently you can just take a
random linear combination and test that
one
thing so the question is can we do the
same thing here with CRT codes
so uh I think so uh but it's very it's
very different right because in the read
Solomon setting you have polinomial and
you're working over a field and you're
taking your random linear combination
over the field here we have a set of
integers and we're taking a random
linear combination of these integers but
there's no obvious base field in the
same way that there would be for
polinomial to take a random linear
combination over so instead we would
pick a random integer linear combination
to take of the the integers and this has
a lot of interesting issues so for
example
this is not sensitive to encodings of
small rational numbers if you encoded
like 1/2 then there's like a one and two
chance that a random linear combination
will cause the one half to go away uh
and you might think well we could pick
primes to multiply by but that doesn't
really work
um so it is in some sense fundamentally
different but I think that it's it's
possible to do this the question is just
like how
good is it and if if those things can be
worked around so for example for working
mod R this is kind of fine cuz small
rationals are also valid sort of to
reduce mod R for large R but there's
lots of details to be worked
out
so yeah just just some overview of the
things I haven't talked about in this uh
this talk so I mentioned a little bit
that CRT codes the the notion of is a
little bit subtle especially if the
primes are not all like the same size
they can't uh sometimes always be I mean
right like every Prime is of a different
size
so um you have to account for that it's
not like a fundamental problem it's just
a little more
complicated um as well I mentioned this
decoding to uh rationals rather than
integers which in some applications is
fine it might not always be fine so have
to work that out as well
then um another thing I haven't talked
about but that could actually be you
know worth considering in practice is
all of this generalizes from integers to
number fields and in number Fields you
have a sort of different situation where
the first point you actually can have
primes that are like of the same size
right if you have some prime over
rationals or the integers that splits
over a number field then that might
yields like a more convenient thing to
work over and in some cases this this
sort of
works
um and then you have to ask like how do
you define the size of things and and so
on but just more technicalities I think
and then one other interesting uh thing
worth considering is so we we moved to
the integers and we were no longer able
to take random linear combinations over
an extension of the base field but what
happens if we work over Starks with pols
and instead of taking a random linear
combination over the base field we took
a random linear combination of columns
by random
pols not over an extension
field in in this way it's sort of
analogous to taking an integer linear
combination of integers and it has a lot
of the same problems but uh it would
allow us to avoid ever working with
extension fields
potentially so I think that would be an
interesting direction to explore if this
work ends up making sense um and that is
all I have thank
you all right thank you so much Liam uh
we do have a question here could you
repeat how you calculate which primes
are small enough to use for creating a
CRT
encoding um so I guess there's two ways
to or I'm not sure what the question is
referring to but for encoding into like
a residue number system the primes can
be any primes um that you you usually
choose them to be small because working
mod small primes is much more
efficient um it this question could also
be talking about the the example that I
gave where you can simulate arithmetic
mod a square root sized number in a
larger field and that is just coming
from the fact that the the relation that
you're calculating over can't exceed the
field you're operating in so you're you
fix some field that you're actually
working over and then if your field that
you're simulating is small enough then
uh everything kind of just works out as
long as everything remains smaller than
the characteristic of the larger
field all right perfect uh we do have a
little bit time for questions so let's
give it another 10 seconds to see if we
have any question uh what is the size of
the coefficients in the RLC such as that
security is still
sure I think
uh I mean you can sort of work out that
it they need to at least be drawn from a
space of size 2 to the 128 but I don't
know how much loss you get from from the
uh protocol itself so I would say at
least two to the
space all right perfect thank you so
much for the amazing talk Liam uh so we
will resume at 5 for our next talk
for I
all right welcome back everyone I am
personally very excited for our next
talk um we have Jen Groth the inventor
of Gro 16 to give us a talk on the
verifiability vision let's give a warm
Round of Applause to Jens on the stage
thank
you hi
everyone uh yeah so I'm going to talk
about uh the verifiability vision uh so
so the idea is that we want to verify uh
the full Digital World um and I think
it's something that resonates uh with
with many of you right this is also what
we hope for in in the blockchain world
that we can uh create sort like very
trustworthy uh data that people can rely
on so the very this slide here s like
the very short summary of what is the
verifiability uh Vision U so uh
Alexander KZ and a androma in
carrying data so the idea is that you
have uh data and data comes with a proof
of correctness and whenever you compute
a new piece of data
you sort like take verified data check
their proofs of correctness and then you
know that you're relying on on
verifiable data you can now compute your
new piece of data and you can create a
proof that this corre computation is
correct right and that proof would both
show that you computed correctly but it
also show that well all the previous
data the inputs you had were also
provably correct right so you have this
recursive composition of proofs that
means that the whole graph of data that
you're computing is
verifiable okay so what are examples of
things that we would want to Claim about
data right so so imagine you're you're
reading your online news site right you
may see an image and it would be nice to
know that this is actually a correct
image not some some fake uh
information um
and nowadays there are some cameras that
sign the data sign so like what are the
GPS coordinates what is the time and so
forth right so as an witness to this
being a correct image you may imagine
using the raw data from this camera and
and the GPS coordinates and the
signature and so forth right and then
the proof might demonstrate that you
know this 100 kilobyte image that you're
looking at is actually derived from a
much bigger set of raw data with these
kind of uh meta information associated
with it
other examples if you are building
online uh voting systems you may encrypt
votes for privacy right but then you
know these system can get messed up if
somebody submits an invalid vote so
there you may have proofs that the
encrypted vote is valid
um and and here it's actually important
to have confidentiality right that you
don't want to leak anybody's vote you
just want to make sure that they're
actually casting a valid
vote um so like the poster child uh
example that we use for zero knowledge
proofs is that identification purpose
right where customer wants to prove
they're over 18 years old and people are
now s like actually going out and
getting data from say passport ships or
something like that so you have some raw
material to work with to give these kind
of proofs and in the blockchain world
there's a lots of applications right so
for instance you may want to prove
something about a smart contract
execution
okay so let me sort like generalize that
a little right so cryptographers they
then think about this as a class of
statements okay and talk about proof
system for these class of statements and
there we have typically a setup that we
expect to be publicly available to all
parties
um sometimes there's some trust
assumption in that so that may for inst
a ceremony in which you could create
that um but if that is once that is done
then it's there and available to
everybody and then you specify a pro
algorithm a verify algorithm the pro
algorithm would take the pro key the
statement you want to prove and
potentially a witness if there's such a
thing to this statement being true and
produce a proof and the verifier
conversely would take the verification
key the statement and the proof right
and then either accept or
reject and this was invented back in in
the 80s where um the definition was that
should be complete so if if it's a true
statement then the Prov has a witnessed
should be possible to create a proof and
conversely if it's a false statement
then it should be infeasible to create a
proof and then the twist in the story
back then was that well it turns out the
proofs can actually convey that well
this is a true statement without
conveying any other information right
which is very surprising so the Z
knowledge property in is that you know
well the proof reveals nothing about the
witness it just gives you one bit of
information namely that the statement is
true so it's this kind of proofs that we
would want to give for the data that we
want to
verify what I want to talk about today
are what I see as as challenges for
proof carrying date to really take off
um and so like four aspects of that I
want to talk about the vitility and ease
of use of these proofs the cost that
comes with with them uh to create them
um composability right because the idea
of proof carrying data is that you you
actually compose proofs you would have
like inputs and they have some proofs
and you would want then to compute new
data and give proofs for those and so
you have to have some composability of
of the proofs and then I'll talk a bit
about the trust us how do we link these
proof to to real world
data okay and so so this is like a bit
of a a history of like you know how did
people go about as s like EAS of views
for for developers in the olden days and
this is an old picture of me I uh did my
PhD work working on voting systems where
you needed to create proofs of of valid
votes and back in the day the way you
construct a a proof system is that you
hire a cryptographer and then they
construct a special purpose proof system
um um and then in the recent years
there's been a lot of uh exploration of
building tools that make it easier to
construct proof uh so something we could
dub as s like the ASC approach is um
that you have a program you want to
prove that in you know inputs to that
program yield a certain output well
let's compile the program into a proof
system that can handle
that and more recently uh there's a lot
of teams now working on ZK VMS where
this is sort of like giving you a more
traditional experience of proving
something so the idea is that you take a
program you compile it down to something
that the VM can execute and then the VM
takes this executable file the program P
some inputs and produce an output and
together with that approve that the
computation was
correct so let's dig a little more into
the so like what does that look
like um so um so ZK VM takes as input a
program um at Nexus we're using risk
five as the target programming language
but of there also many many teams
building ckvm so you could also find
this for for wasm or special purposes
language like Kyu and and so
forth then the program can take an
input uh an input X they may also take
an A Witness W and will produce an
output Y and then approve Pi that this
output is
correct and there will be a matching
verify algorithm that then looks at the
program and and the inputs X and the
output Y and the proof and decides
whether it accepts this proof as being
correct and the whole goal for for all
these teams that are building ckvm is to
give a very easy developer experience
right so so the way it will look like
for a developers something like this you
can just use a command line and you can
prove or verify these
computations so I think we're getting
somewhere with like the the ease of use
from a developer
perspective um the next thing the next
barrier I think is is the cost so let's
sort like dig into what where we are
and I think the whole Community has
settled that that the type of proof that
you want is a snark okay and what is a
snark well it's in one of these proof
systems where we want the proof to be
succinct okay so the succinctness
property is that the proof is really
small okay and we're talking about in
the best cases something like a couple
of hundred bytes okay and the
interesting thing is that it can be a
couple of 100 bytes regardless of how
complex the statement is right so
imagine you have program it does like
lots and lots of operations but you
still just get a very small proof and
something that's very easy to uh to
verify
uh we want the proof to be
non-interactive um and to give a little
bit of context because that's not
present on the slide here so in the
olden days when people were thinking
about Ser knowledge proof they were
thinking about proofs where you had an
interaction where the verifier was
interrogating the the prover um but the
nice thing if it can be non-interactive
where the proof just produces the proof
and then it's
done um is that now you can take these
proofs and you can copy them and you can
distribute them right so if you see a
proof uh for for some claim then you can
just make a copy and you can send it to
somebody else and they will be convinced
as
well and then we want to it to be an
argument of knowledge which is sort like
a technical way of saying that um the
only way you can construct a proof is if
you were also able to construct a
witness so in other words you're ensure
that it is a true statement
okay so when we have sucin proofs right
then we have these very small proofs and
the verification time is really small as
well it's independent of the program
execution time it's also independent the
verifi does not take this auxiliary
witness as input right and that's super
cool right because it means verification
can be much cheaper than doing the
computation itself
and I think this is like a a key message
here right that verification is cheap
okay and that's what sort like makes the
verifiability vision possible Right In
some sense all these data that come
around with proofs right the proofs are
for free right so it's so like from a
user perspective okay I can get a piece
of data and blindly trust it or I can
add exactly the same cost almost get the
data and the prove that it's correct
right which one do I prefer well if it's
for free I would want it to be
verifiable okay so where are we today uh
proof size is really small it can be as
low as a couple of hundred bytes the
verification time is really low as well
it can be as small as just essentially
reading the
statement what is the bottleneck
nowadays is the proving time time and
and that's horrendous right so the
overhead of like you know the cost to
prove something versus you just compute
it directly are it's like many orders of
magnitude there's a lot of work going on
to improve that right uh and if you saw
like look across time right like back in
the 80s when when Z proves were invented
people didn't even think about like the
efficiency of the pro it could have
infinite time to prove some thing and
people have been become more and more
careful and I think now we s like you
know the way you measure it is you would
talk about like you know how many cycles
does it take to prove a cycle uh so
trying to compare apples to to to Apples
um and in the future I mean there's a
lot of companies working on Hardware
acceleration so forth right at some
point we may sort like go to using
physics terminology to to measure
something like you know many how much
energy do you spend per per GR cycle for
instance so we are at sort of like an
interesting phase right now where we
have these proofs that while they're
efficient to verify and they're
efficient to copy and transmit they're
really expensive to create right and the
question is who's willing to pay for
that okay and and it's very nice I I
think zero knowledge proofs have been
fortunate to to meet the blockchain
space because there are actually a lot
of applications where we're willing to
pay for that in the blockchain space
right because and that could be because
it unlocks a unique
capability it could also just be because
there's so much replication going on
when you're verifying computation right
so think about thousands of valid dat
noes that have to redo the exact same
computation to verify that it's okay on
a blockchain right well instead of doing
that why don't we just send aof wrong
that's very easy to verify that hey this
is a correct next
block and also uh the cost of storage is
something that can be prohibitive on on
a blockchain right so instead of storing
a lot of data and and so forth now maybe
we can just have a proof that says oh
there is some data that would result in
this end
state so one of those examples right ZK
rollups right where it used to be that
you do onchain execution so you have
this kind of like low throughput
expensive operation whenever you're
processing
transactions and now we're talking about
well why don't we do all of that
offchain right and we just
create compute what is the the Delta
what is the change that would happen to
the smart contract from all of these
transactions and then create a proof
that that's the case and then we just
give the the change and the proof to the
smart contract and can update the
balance okay um so the next thing I want
to talk about is composability so how do
these things glue
together and here here it's really the
succinctness property why we like snarks
right because they ensure that these
recursive proofs of proofs of proofs and
proofs that you have when you do proof
carrying data and you're Computing new
data based on verifiable inputs that
they stay small right because all of
these proofs are small and whenever
regardless of how many inputs and so
forth you have when you're Computing new
piece of data you can still compute a
small succinct proof for that being a
correct operation
so the nice thing about snarks is that
they they compose well right they're
succinct so there's no size explosion in
proofs they're non- interactive so you
can sort of like give them as inputs and
be used in further
computation and the soundness of them is
well cryptographically speaking uh close
to 100% so also there's no degradation
it's not like you are getting sort of 9%
and then you have like another 10% loss
in the next step and so forth right
you're staying close to 100%
soundness And this is unlike other types
of of evidence you could give right so
for instance if you want to do direct
recomputation to verify something well
then you would have to send all the data
along right so there would be no
succinctness
anymore right if you wanted to do some
interactive techniques so like
interactive proves or spot checking or
something like that well there's some
interaction you can't do recursion you
can't give that as input to the next
step and for Economic Security uh
techniques which I think is a really
cool idea right but it becomes difficult
to manage this kind of Economic Security
and track that over a long path of of
statements
one thing that's interesting about um
about this proof cost then when we use
it in proof carrying data is that we can
amortize the cost of our many
verifications right so if you have a
proof that you've created at some step
and then you're building on that and
you're building on that and building on
that somehow you're acre value of
verification value in all these
subsequent steps right are relying on
that proof
and I think this is sort of like a
really sort like nice thing right but it
also points to so like maybe there's a
threshold effect that the more data we
put into a proof carrying data system
right the more we can amortize the cost
of of creating a proof over many
steps okay so so the last part I want to
talk about um our uh um trust Anor and
Trust
management and in blockchain we have the
Oracle problem right how can we get data
into a blockchain and the same thing
happens with these proof carrying data
right sometimes there are data that
comes some from from outside and we just
have to trust them okay and how do we
incorporate
those and that's what we refer to as as
trust anchor right so there's a question
of of how do we incorporate that data so
maybe it's a camera that signs a raw
image it's etherum that finalizes block
and you have some sort like threshold
signature multi signature on it or
something like that
right and this is an adoption barrier so
so there are not many places in the
world today where we get these trust
anus for free people have to go around
hunt for it but the exciting thing
people are going around and hunting for
it and trying to strip you know data
from from passports and using that for
identification protocols and so
forth it does lead to point to a problem
as well though right which is proof
management what happens if a trust
anchor fails okay now you create a lot
of data on top of that you have proofs
right and maybe you've lost sort like
what was the origin of that so what if
it turns out that well somebody who
signed something they actually malicious
and and they signed some fake input so I
think there are lots of these kind of
management issues that we still have to
resolve with s knowledge proofs and
proof carrying data and I think that's
sort like going to be something people
are not thinking too much about now but
I think in in the years to come that's
going to be an issue that is uh
increasing in
importance okay so I want to to wrap up
I'm s like
talked about some of the barriers I see
and sort like where we we're going and
I'm hopeful that we're we're going to
get there so so what is what is the end
result what does success look
like um I think in the blockchain space
uh we're talking about the proof
Singularity uh so think about taking all
the computation and take it that off
chain and doing it where it's cheap
outside the chain and really using sort
like the L1 chain as a verification
settlement L right because that's what
the blockchain is good at it's good at
verifying
stuff and more broadly I hope we will s
like be able to go so like beyond the
blockchain space or maybe we can hope
for the blockchain space becoming so
like all encompassing is something
that's very widespread in use and there
are what I'm um the vision I'm hoping
for is sort like a digital world where
we have this web of verifiable data
right and since verification is cheap
right hopefully people would want most
of their data to come with proofs of of
correctness right and we would have a
much more trustworthy World um and with
that uh thank you for for your
attention all right thank you Jen uh
we're actually running a short short on
time but we can take some questions uh
type theorist have thought a lot about
composition of proofs how can type
theory help with composability of
cryptographic
proofs okay yeah
um huh um I'm not entirely sure okay so
but but I
think I I guess in
I suppose it's
been from a somewhat different angle
that type theorists have been thinking
about this I guess in terms of
uh so one thing that you're using type
theory for is so like static analysis
like so will it program execute
correctly will it process the data
correctly um and that is an
orthogonal thing to what we are trying
to do with with these kind of proofs
which is more like has it executed
correctly so so in some sense I think
that is sort like a complementary thing
and I think one should do both right so
you should use sort like formula
verification and type Theory to make
sure that whatever you're doing is
correct and maybe for proof carrying
data there's also a question of like how
how does one
computation Carry On from the next one
and does that make
sense and then you would want the proofs
to make sure that well once you know
that that is like the correct structure
of of data and computation then that
that has actually been executed
correctly uh what are the advantages of
elliptic curve based proofs versus small
field
proofs yeah so I think elliptic curve
proofs are um I think in some some ways
easier to reason about you can have some
very nice homomorphic commitment schemes
like Peterson
commitments um the the disadvantage is
that you're working with larger fields
and that can be a costlier operation um
so if I had to conjecture I think the
world is moving toward using small
Fields rather than elliptic curves just
for performance reasons and then
potentially also for postquantum
security all right and a lot of people
want to see this answered should we be
prioritizing postquantum proof
systems uh yeah um so I think it's not
as urgent for proof system as it is for
say encryption schemes because the proof
systems if there's a knows proof their
suing they don't actually carry the data
around right so it's more a question of
like how long time do you want the
verification to hold then nobody could
break the soundness but for anything you
verify here today right then since as
far as we know no quantum computers
exist that should be good enough um I do
think that the world is probably moving
to post towards postquantum security
anyway just because of like they seem to
be pretty efficient techniques anyway
for creating
proofs uh what proving system does Nexus
use yeah so we have uh several approved
systems so we have um a
ckvm uh we uh implement reimplemented
the Nova family of folding schemes from
the ground up so that's Nova and
Supernova and hypernova we have in the
ckvm um but we also have an
implementation of of jol in in the
ckvm all right given the time constraint
I think we can only take one more uh was
an application of this verifiable layer
you would be excited for that isn't
currently
possible yeah um
so so I'm very concerned about deep
fakes uh and in general s like the the
news that you get and the fake
information you get
misinformation uh which is very
deliberate misinformation that we're
facing so I would love to have um a
system by which you had much stronger
guarantees whenever you were reading an
article or piece of of news that you
know that there sort like a path back to
the original sources that provided that
information um I've so like tried myself
talking to journals being misquoted not
maliciously it's even worse if it's
malicious so if there's some sort like
way of saying you know in an article
guaranteeing well that the original
person who they talk to agree that this
a correct interpretation so forth I
think we could all already eliminate a
lot of misinformation and I think this
Zer proofs can be part of that
uh I also think that there are other
components uh involved in in getting to
that solution all right so unfortunately
our time is up but thank you so much for
the amazing talk Jens
SC
all right welcome back everyone can I
just get everyone seated
please so our next talk is on
decentralizing consensus and we have
another Legend that's going to be on
stage he is the co-founder of ethereum
and the founder of consensus so let's
give it for Joe luin on the
stage hey everyone thanks for
coming there we
go so this
talk uh will have a different tone given
the the recent political shift in the
United States uh than if it was written
a month ago um though I've lived in the
US for years um I'm a proud Canadian I
would describe myself as politically
Centrist and neutral uh if there was a
progressive rigorous open
decentralization party uh I would be an
nft caring member for years in the US
companies in our industry have been
living in fear feeling unable to engage
in certain activities that should be
natural for a web3 company like issuing
utility tokens for instance we're
operating in a climate characterized by
regular atory
uncertainty gas uh by regulatory
uncertainty by gaslighting and carpet
bombing of our industry with inquiries
that felt like
inquisitions Wells notices and lawsuits
from the SEC the industry asked for rul
making and engaged in good faith but a
strategy of Regulation by enforcement
action replac the approach any lawful or
constructive regul would take because
the goal was to slow kill or coopt our
our industry in the US this was the case
for three reasons the progressive wing
of the democratic party believes a large
strong central government should have
granular control over the
population two Central large financial
institutions preferred to keep winning a
rigged game rather than compete on the
Level Playing Field of decentralized
finance and three the US controls as
much of the world as possible via
intermediaries especially financial
intermediaries and ethereum represents
the most powerful Unstoppable dis
intermediation technology on the
planet there's been concern about a
second American Revolution there's
indeed going to be another Revolution it
will be a bloodless and probably
bipartisan Revolution that sheds the
regulatory Cru and reformats America
according to the principles under which
she was founded liberty and justice for
all distrust for overreaching
centralized Authority and a healthy
reverence for self-determination and
decentralization paraphrasing William
Gibson the world of decentralization is
already here it is just unevenly
distributed while it is finally looking
like America is getting on track
decentralization has already been
blossoming in many places where it is
needed or where opportunity presents
decentralized protocols flourish in
places like Argentina where industrious
people need ways to Route around the
damage rought by centralized government
or in Asia or in the Middle East where
the population is hungry for opportunity
and agile in how it
responds we have an opening now to
reformat the world bottom up the whole
world the massive shift that America's
about to drive including an Embrace of
our technology will become an imperative
for the world's countries to follow
something like the American experiment
or the American project that began with
the American Revolution and was soon
followed by the French Revolution in the
various parts of the
world this Age of Enlightenment led to
the development of the western liberal
Democratic philosophy in Many Nations
this philosophy is characterized by many
ideals that have been corrupted over the
past few decades rationality reason and
progress individual liberty and rights
empiricism and scientific method Limited
in Democratic governance pluralism
intolerance and genuinely free markets
our globalist decentralization project
the Natural Evolution of the American
project will bring new kinds of
sovereignty to the people and
communities of the planet and it will
grow viral crossing different kinds of
borders because once you see
decentralization at work you can't unsee
our Tech ecosystem and sociopolitical
movement must always be about
progression towards rigorous
decentralization in the Deep
foundational infrastructure of the
world with rigorous decentralization we
get all of the characteristics of w
Western liberal Democratic philosophy
and more specifically we get open source
transparency and credible neutrality we
get permissionless participation and
Innovation we we get a world computer
with a verifiable computation stack and
software supply chain web 3 will be the
world computer on which all the World
Systems will eventually be
rearchitecturing
news alerts disclosures of political
business
and social events and unfettered
journalism shout out to multiple
concurrent proposers distributed
globally with robust real-time
information dissemination and journalism
we get an informed public and an
informed public is an Engaged public
with an informed and engaged public we
get healthy local Regional and Global
participation in governance broad
participation in open governance at all
levels makes makes it hard for
exploiters to capture and control the
important systems of the world with good
governance globally we get a healthy
rapidly evolving
Society waves of decentralization are
cyclical see the ancient Greeks and then
the Romans and the recent American
elections but the secular
decentralization trend has been underway
for centuries as monarchies have seated
power to nation states which have seated
power to joint stock corporations First
National then multinational and
technology has increasingly empowered
communities and individuals the trend is
to make sovereignty more and more
granular a simple definition of the
network State a network state is an
online digital first Collective of
independent actors can be humans groups
or AIS who are aligned with respect to
exploring and addressing one more issues
Network Stakes can be realized as Dows
social graphs online discussion forums
or combination of tools Network States
benefit from New web3 Primitives like
decentralized ID constructs verifiable
credentials attestations governance
tools Etc Network states have the
ability to create their own magic
internet tokens for different purposes
utility loyalty governance money Equity
memes Etc people who are aligned with
the mission of the network dat might be
inclined to do work in exchange for
compensation in the form of some of
these tokens others might also find the
tokens of value for different reasons
Network states that choose to work
together May swap tokens to establish
greater alignment a network State can
bootstrap itself following various
strategies Bitcoin ethereum and salana
can be considered a certain class of
network State layer 2 networks can also
be considered a class of network state
to protect decentralization we need
rigorous incessant ritualized vigilance
Thomas Jefferson wrote The Tree Of
Liberty must be refreshed from the from
time to time with the blood of patriots
and tyrants we too will have to tend to
the long-term health of the tree of
decentralized Liberty not with blood but
with attention paid and shrill
commentary on on crypto Twitter and
other discourse platforms and with
attention and gas paid to systems that
are constantly monitoring the threats to
decentralization
sovereignty refers to the supreme
authority or ultimate power that a state
institution or individual holds over a
specific territory or group of people
sovereignty has several Dimensions
domestic sovereignty the state's control
over its population and territory
International legal sovereignty
International recognition of all states
Independence and Authority
and no interference into the internal
affairs of a sovereign sovereignty can
be limited by constitutions
International agreements or inter or
internal divisions of power one can
imagine a web 3 plus
AI uh one can imagine as web 3 plus AI
enables new modes of living in
overlapping networked states that we
have the opportunity to to Define new
kinds of sovereignty and just as nation
states Define their forms of sovereignty
we've started to Define new forms online
and onchain one for individuals online
self- sovereignty in various forms VI
IDs and other identity constructs
combined with reputational Primitives
like attestations verifiable credentials
webs of trust and rating systems in
which the Raiders have skin in the game
when they vouch for something two for
communities online sovereignty embodied
in Dows social graphs and other
mechanisms these are network states that
will take very different forms they will
operate as sovereigns in online domains
setting rules for their participants
that are of by and for their
people Sovereign individuals are already
becoming members or neens of network
States some of those Network States will
eventually have arrangements with one or
more nation states some of those Network
States uh sorry um enabling temporary or
permanent rights to be resident there
the state of Wyoming for instance allows
Dows to register as limited liability
companies this is a small step but we
can think of it as cracking the door
open uh and that will lead to
establishing relationships between
Network States and more traditional
polies many nation states are facing cat
catastrophic demographic challenges they
need more people to take care of the
Boomers and keep the economies from
collapsing some nation states provide
passports to citizens of other nations
in exchange for investments in the
country and some nation states actively
recruit for talented immigrants Canada
has targeted recruiting
residents in
which legislators and Regulators
consider themselves in the service of
the citizenry as they do in Switzerland
and compete for companies and people to
choose residents
there the internet begat web 1 which
which begat web 2 which begat web 3 the
red decentralized web the internet
started out decentralized it was a bunch
of protocols running on nodes
distributed around the us then the world
on wires provided by telecom companies
the internet was Loosely governed by the
ietf a decentralized organization web 1
also started out decentralized it was a
bunch of open protocols and
specifications running on top of the
internet protocols web 2 picked up steam
in the late '90s and early a as it
became clear that there were billions of
dollars to be made as some sectors of
the economy were moving online and brand
new sectors were being
invented web two companies had exciting
New Primitives at their disposal in the
form of protocols and open
specifications and some new ones were
created but the dominant mode of
operation of web 2 companies was closed
Source systems and if you were fortunate
enough to grow your product into a
platform the standard strategy was to
invite
companies and users onto your platform
so that they can get a leg up in
offering their products but when the
platform felt it necessary to grow
revenues further it became opportun to
rug pull those projects to capture their
revenues the web two platform strategy
became became to build as Broad and deep
a moat as possible to stifle competition
Moes not
Bridges web 2 represents
de centralization of the web eventually
web 2 on steroids became big Tech big
Tech itself built Big te built itself
into a weapon of mass manipulation
available to any actor who would pay and
big Tech learned how to use Ai and
behavioral psychology to addict its
users to its product one result is that
discourse on the planet is now
hopelessly polarized and dysfunctional
big Tech has fed as a negative
externality of its business processes
the shredding of the social fabric of
much of the
world and now big Tech on even stronger
steroids is poised to convert its
control of AI Talent Plus vast amounts
of data and computation into building
the most powerful tool in history for
the centralized control of
humanity fortunately the pendulum is
swinging back hard now towards
and web 3 the red centralization of the
worldwide
web consensus was formed to continue the
vision and mission of the ethereum
project and just like ethereum we're
dedicated to Progressive prudent
decentralization of everything we do
prudent because it must be done with
care to ensure that we always Focus
first on the safety of and benefits to
our users and also that we never destroy
value in evolving a project towards
rigorous decentralization we
decentralize to build better more
valuable systems metamask for instance
is progressively decentralizing itself
the metamask snaps plug-in architecture
allows users to add functionality to
their metamask individual Snaps are
features created by third-party
developers that metamask users can
install directly into their metamask and
the metamask team has been leaning into
account abstraction for a while when the
account abstraction dust settles uh
somewhat at least we expect to expand
metamask scope and capabilities with
components embedded in applications and
enable you to add superpowers to your
metamask or to any project via Dan
Finley's delegation toolkit and
framework continuing the pattern of
progressing the vision and mission of
the ethereum project consensus software
announced yesterday yesterday that we're
externalizing our Linea ZK evm rollup
technology and network into its own
ecosystem Linea is accelerating on the
Progressive path to rigorous
decentralization and token-based
Community governance linea's Evolution
will be maximally ethereum aligned Den
the decentralized infrastructure Network
blockchains are complicated databases in
infura enables developers products to
read from and write to various
blockchains with these but in a web 3
world of potentially millions of block
chains infura can't integrate them all
on its own so infura has been
progressively decentralizing itself into
din the decentralized infrastructure
Network a robust multi-chain RPC
provider din is already operational with
connectivity to various networks and is
already handling a 100 million requests
daily and din is about to evolve into an
igen layer
AVS INF fur will become a premier
specialized provider on the in network
and fears openly sharing its
optimizations distribution to customers
and revenue opportunities with other
providers in order to evolve the
ecosystem Bridges not Moes can't be evil
din Linea and metam mass snaps enable
permissionless Innovation and onboarding
to our infrastructure we will not be The
Gatekeepers as our systems become more
rigorously decentralized it will not be
possible for us to deplatform projects
Bridges not modes can't be
evil there are many other projects that
are on our product development pipeline
that runs from ideation through
development through product Market fit
and into Pro protocolization
externalization and tokenization we
expect many of these to have powerful
synergies in both functionality and
benefit to the
user standing up a Proto Network
State the initial consensus company
consensus mesh began as a tiny
multinational startup because we had to
look globally to find people who had a
clue about what we were
doing becoming a large multinational
corporation is not cool becoming a
Global Network state is cool in order to
operate most effectively in web 3 we
build Bridges not silos so we're working
towards making consensus software Inc
more permeable or porous for example
we've had policies for a while that
enable our members to spend more time
spend some of their work time on
projects outside of consensus like Dows
consensus is embarking on a new phase in
its
Evolution consensus software Inc several
several of its products projects and
other projects in the extended consensus
ecosystem and Beyond will soon set up
shop on what we're calling the consensus
Network State Network states are about
alignment transparency broad governance
and Collective benefit we will
progressively iterate in those
directions the capital city or da of the
consensus Network state will be resident
on Linea mainnet the first island
composed of Linea digital real estate
while consensus will operate throughout
web 3 we will consider Linea main net
our home network on which we build cores
of our critical infrastructure we will
continuously look to build synergies
among our products via explicit onchain
agreements and we will look to create
synergies among our products and your
products via explicit onchain
agreements our friends at soble soo.
are
in the early stages of building an
onchain agreements framework that we
will use to form agreements between
projects that specify in explicit and
measurable terms what should be done by
each party and what compensation yes
token compensation is Due based on
levels of performance performance can be
measured in usage of our products and
protocols or in providing liquidity or
in bringing your project onto Linea or
attaining levels of performance in your
project in terms of users transaction
volume tvl Etc we will be employing a
new yet ancient meta work to earn if a
person or project adds value to the
Linea ecosystem Andor the consensus
Network State they will be compensated
in tokens based on
onchain explicit agreements
many of you out there are already
self-sovereign on chain but we're all in
the early stages of discovering what
self- sovereignty means we will be
living more of Our Lives on chain as our
finances identities Communications art
and entertainment are increasingly
mediated by open networks and
decentralized
protocols the new relationships and
communities that form will will be the
basis of new overlapping Network States
in which we will all participate today
we're launching soles.
XYZ a project
inviting everyone to declare their
personal sovereignty as another small
step towards the decentralized future
you can go to soles.
XYZ
to you can go to sal.
XYZ to attest the
kinds of sovereignty that matter most to
you and write your support for the
emerging world of network States and our
Liberation through them permanently on
Linea we have bigger plans coming soon
this is the beginning of a partnership
with the community to build a network we
all want to be part
of when we hear www in the decentralized
future we should think about a
win-win-win world computer Humanity has
flourished via communication and
coordination capabilities that give us
Mass massive advantages over other
species coordination requires trust
Satoshi invented decentralized trust
possibly the most profound invention in
human history decentralized trust
platforms are now broadly available to
builders and users based on blockchain
and smart contract based credible
commitments web three Primitives plus AI
automation are about to enable Humanity
to distrust each other much less and
collaboratively build towards a post
scarcity abundance mindset that will
enable us to evolve a massively positive
some
world so what does leadership look like
in the decentralized future self-
sovereigns in the decentralized future
will be the CEOs of themselves and they
will collaborate with other CEOs using
credible commitments on ethereum they
will have clouds of AI allies amplifying
their capabilities and they will create
complex delegations of onchain powers
with those AIS and with other collabor
CEOs so what will
leadership in a web three world look
like well that's up to
you thank
you all right
uh all right thank you guys so much and
Joe we do have some questions uh let's
go from the first one uh what can we do
in 2025 in terms of tooling to boost the
creation of network
States um well there are lots of
Primitives out there um and uh we're
exploring them so um Network States
right now are more like Proto Network
states where where The Primitives are
available but uh um a a few systems are
using them uh as I said you could you
can call ethereum a network State you
can call uh the avara set of projects at
Network States so uh it's happening and
we just uh we need to keep kicking the
tires on our tools and and start living
in them uh how can we make the ecosystem
safer to allow real adoption in a
decentralized world um say it again uh
the very first question ecosystem safer
um we have to keep building and security
auditing uh it's uh it's tough
building uh web three on on live
monetary rails with with the entire
world watching um so it's uh it is a
complicated Prospect uh but uh we need
to get better and better in terms of
security uh here's another one uh we can
actually take the second one if you
prefer
um how can we more urgently shift the
ecosystem towards reputational Works
where influence is in determined by
contributions to project according to
its values uh so uh consensus has built
a a reputation system uh an attestation
system we're working on identity systems
or or aggregating identity systems so um
we're trying to figure out um exactly
that so whether it's reputation for
metam Mass snaps or reputation for for
your activities in a project or a
network State uh it's uh it's pretty
much the same system so it'll get a lot
exercise what makes a network a
state um well a network State uh is a
group of actors that are aligned uh to a
specific purpose um it has capabilities
could be anonymous people it could be
identified people it could be um um
could have the ability to create tokens
for different purposes uh has the
ability to set its values to set its
goals and and to achieve its
goals uh and we have one on the
ecosystem fund would there be identity
and reputation systems to align not just
financially but personally and
professionally um so uh the forthcoming
Linea ecosystem fund or consensus
ecosystem consensus Network State
ecosystem fund um will will have
um um forms of decentralized ID uh forms
of reputation systems um but it should
also be possible to to be to operate as
an Anon uh you may unlock fewer
opportunities you might get compensated
um less because there might be more risk
in in working with you uh but I do
believe that as reputation systems uh
grow richer uh we should get much more
comfortable um doing risky things with
anons because you'll be able to to
calculate your risk uh we have enough
time for one more question how's Network
State different from
Dows um a dow is uh very much like a
network state in its uh in its
superficial definition um uh if you ask
bology re bason who who's been uh
promoting the idea of network States um
there's uh a an element of formation uh
which is initially onchain uh but then
uh he likes the idea that uh it will
reestablish itself itself or establish
itself um in physical context perhaps in
archipelagos all around the world and so
um in his definition a network State
could be composed of a DA and other
constructs it could be social GR it
could be discourse platforms but there
will also be uh some sort of uh physical
um touch Point all right so our time is
actually up uh let's give a round of
applause to Joe everyone thank you
hello can I get everyone seated please
so our next speaker Walden will give us
a talk on how heart hat 3 will ensure
precise simulation for l2s using EDR
let's give a round of applause to Walden
welcome everyone and thank you for
staying uh until the end of the day I am
Wan a developer at the nomic foundation
and today I'll be talking about how
heart hat 3 will ensure precise
simulation for l2s using
EDR there's a lot to unpack there but
first I wanted to comment on the nomic
foundation maybe not everyone's familiar
with it but you're probably familiar
with our work we are a nonprofit
dedicated to ethereum developers you
guys um and our most well-known product
is likely hard hat and the hard hat vs
code extension that's
us so an overview of what I'll be
discussing today is I'll start off with
a quick introduction to what EDR is um
then I'll go into variability between
l2s I'll look at some problems that
currently exist when Developers are
developing for l2s using L1 tooling then
I'll do a technical Deep dive into how
EDR actually simulates l2s accurately
this will also be interesting for any of
you L2 developers out there um as I'll
talk about the extensibility points that
EDR will expose in the future and
finally I'll touch upon a demo that
shows how l2s work in hard hat 3 this
will be interesting for all of you hard
hat users as it will show how the
technical complexity of all of this
variability is boiled down to a simple
and straightforward user
experience so what is EDR EDR or
ethereum development runtime in full is
an reusable evm development runtime
library for tooling it is a set of
building blocks for blockchain
simulation and in particular it allows
you to observe evm and solidity
execution so as such we are targeting
smart contract development the
simulation testing and debugging thereof
and we're not targeting to be an
execution layer node if you're curious
to learn more about EDR earlier this
year we had an EDR launch announcement
when we integrated into Hard Hat 2 um
and there's more information about other
features performance improvements that
brought to hard hat and future road map
for EDR as
well so what variability exists between
l2s and L1
for the sake of this presentation and
also for the implementation of EDR we're
assuming l2s that are evm equivalent
this means that they have to comply with
the evm specification or the ethereum
white paper if you
will when we can depend on rollups any
of the L2
transactions uh can have their own
custom types this means that when we're
dealing with custom uh L2 transactions
that there is logic that's different
which is executed with in the evm um the
way that we're dealing with rewards the
way we're dealing with fees can be
different and even the output that's
return can be different for example halt
reasons when an exceptional halt occurs
when we go into a transaction and we
look at the bite code the op codes might
also be different it could be that an L2
doesn't support all of the op codes of
L1 or vice versa but it can even be that
the same op code is has a different type
of behavior in the L2 for example the
block n number op code how would we
simulate this on an L2 do we give a
prediction of the L1 block that we
expect to be included in or do we return
an L2 block
number um within the evm another thing
that's different are pre- compiles the
set that's available in different l2s
differs as well as them being different
from
L1 another thing that is different are
hard Forks every L2 will have a
different set of breaking changes uh for
which they'll have their own heart forks
and something that we need to track as
well is so-called hard Fork activations
those are the block numbers or time
stamps at which a particular heart Fork
becomes activated um and these will for
example be needed when you do an E call
at a particular block number if we're
forking a blockchain and we want to run
a historic block we need to know what
hard Fork uh should be activated at this
point um when we then roll up everything
into L2 block uh we also need to at the
protocol level take into consideration
fee calculation and we need to
incorporate custom transaction
receipts when we are deploying our own
chain uh for specific l2s we need to
consider their own preep contracts these
are Incorporated in the Genesis State
and mean that you can access these
contracts that are predefined address
these differ per L2 and then finally if
we go up one more layer you have have
rpcs uh the RPC which uh might have
additional field for methods it could be
that a method returns Fields but with a
different behavior and it can even be
that one of those methods has entirely
different logic altogether all of these
types of variability need to be
incorporated and keeping track of them
is a is a is a huge pain so a big shout
out to evm diff and the L2 documentation
that was very instrumental when we were
implementing the op stack for EDR
so we have an idea now of what
variability exists but what problems
might occur here are some examples um so
when we start off at the execution layer
um when we're dealing with unknown
transaction types from an L1 perspective
uh we're not sure how to actually
execute them it could be that they they
throw an error or or um it could be that
they do execute but because the op codes
have different Behavior the result is
different and as such the L2 execution
will be incorrect within your L1 tooling
when we're then trying to mine a full
block we also run into issues the rlp
encoding for these unknown transactions
is unknown which would result in a
incorrect uh TR rout um and it could be
that the header has different header
fields which would also result in an
incorrect block
hash um then when we look at the gas
calculation these end up being incorrect
as well let's have a look at the way
that L2 transaction costs are structured
so on the left side you'll see something
that's very familiar we have our
execution gas cost consisting of a gas
price multiplied by gas used this is the
same as on L1 except that L2 gas prices
will be lower um but we have something
new which is the L1 data fee this is the
the cost we have to pay for the rollup
or the part that our transaction is
within that rollup uh this is the L1 gas
price multiplied by the L1 gas used
multiplied by the number of bytes of
transaction data usually this is
compressed to reduce the amount of
memory usage but we somehow need to
convey this cost to the user l2s do this
differently it could be that they try
and uh convert this factor of gas price
multiplied by gas used to an L2 gas
usage or it could be that they somehow
try to change this to the L2 gas price
each L2 will have their own strategy for
doing
this then when we're looking at
debugging uh for example using debug
Trace Transaction what we're trying to
do is we replay some block on the Chain
until we reach the transaction that we
want to debug uh and it could be that up
until that point we find some unknown
transaction um and we could treat them
as an EIP 155 transaction or a legacy
transaction um and try to execute based
on a best effort uh but this might
result in errors so instead we could
choose to skip it um but this might have
a negative side effect that if that
transaction affected the state that our
contract is also accessing that we are
getting a different result than we would
on a test or main
net all of these examples that I gave
have something in common we're trying to
build L2 smart contracts using L1 tools
and hoping that it just
works it could be that the tests are
passing but there are still subtle
execution differences that give us a
false sense of security and this leaves
room for security vulnerability once we
deploy so how does EDR circumvent this
and accurately simulate
choose so here we have an overview of
the different building blocks that I
mentioned uh outlined in Black in Orange
we have entry points uh from and into
hard hat and in purple we have RM which
is the evm uh dependency that we
use everything outlined in green is
parts that we previously had supported
for L1 ethereum but now we need to
convert to be able to be multi-chain and
also support different l2s
um I've numbered it in two sections as
they both have different requirements
and we'll delve into those uh
respectively
now so the part outlined in one uh was
all rust code so we need to look at
expansibility from a rust perspective
for this we had several requirements we
wanted compound time polymorphism this
would allow users of our crates or
packages if you will uh to be able to
use these interfaces or uh traits during
compile time to to generalize their
types and functions we also wanted to
generate type errors at compile time
this would force L2 developers to
resolve any issues with their typing as
opposed to the error bubbling up to
hardhead users at runtime finally we
also wanted to ensure that their type
definitions were reusable from a base
chain to a uh L2 chain for example if we
have an EIP 2930 transaction this is
used in op stack as well so being able
to reuse those types lightens the burden
for L2
developers the solution we used are the
rust traits and generics traits are a
form of interface that can be used both
at runtime and at compile time to
constrain uh generics and generics are
just a way to generalize function
definitions and type definitions across
a type um for each of these traits or
interfaces we Associated uh types with
them uh that we consider to be a chain
specification think of a transaction
type a block type Etc and there are some
constants which are used within the
protocol we distribute individual change
using rust grates for
reusability so if we look at the
overview again here um and we start at
the top right we have a remote Network
clients which does RPC calls to a
provider like INF or Alchemy here we
introduced an RPC spect rate that would
define the RPC transaction or an RPC
receipt Etc then when we go to
revm um here we introduced something
called evm wiring uh we proposed changes
to RM and with the graceful help of
dragan raita the maintainer we were able
to incorporate these large changes into
rvm which means that now within rvm you
can also run and extend uh different
chain types um here you would Define a
runable transaction a block Within which
it's executed the hard Fork H reasons
Etc then we go up one level to something
we call the executor the executor is a
wrapper around the evm which receives a
signed transaction passes it in and
while it's executing we We Gather
additional data which we use for runtime
observability so things like traces for
stack Trace Etc that we expose to the
end user here we introduce a type run
runtime spec
and then when we're incorporating all of
these transactions into a block within
our block Builder we need to consider uh
parameterizations for the protocol level
such as the Bas Fe calculation this has
specific constants that need to be
incorporated which differ between L1 and
L2 and here we introduced a eth header
constants interface to define
those then all of this logic is tied
together within the node or provider um
and here we introduced a provider spec
with things such as a pulled transaction
for example for blob transactions we
also keep track of additional blob data
Etc and these are stored within the mol
then finally we reach the RPC interface
that's exposed to uh hard hat here what
we do is we use uh a tool called napi
which can be used for generating
typescript bindings from rust code and
this allows us to basically from heart
hat which just typescript call our rust
functions um and here we introduced a
sync and API spec uh sync basically
means we're trying to call um our rust
code from a uh threaded environment and
this ensures that the access to that
data is correct and we also do a
conversion from compile types to um
runtime polymorphic types which we'll
have a look at
next um all in all this com encompasses
six different traits or interfaces and
these are all the things that an L2
developer would have to implement in
order for all of the building blocks
that we have within EDR to be supported
for their chain and in addition for
their chain to be usable within hard hat
future so when we look at the part that
was outlined on the left we're dealing
with typescript so the requirements for
extensibility are slightly different
we're dealing with runtime
polymorphism we're trying to minimize
memory usage and load times um the goal
here is that we shouldn't have to load
all the possible L2 chains only the ones
that the user of hard hat in that
particular configuration wants to use
and we want to avoid centralization of
chain types we don't want a repository
where you have to add your specific
chain type to an enum instead we want
you to just be able to plug and play
your own chain types
independently for this we created an
napi wrapper around Dynamic trade
objects Dynamic trade objects are
basically virtual objects where you can
access a specific instance of an object
through an interface um and to
distinguish chain types we use a string
identifier um and then finally for
distribution we're using npm
packages here we have an overview of
what that looks like um on the
typescript side uh we have a uh if we go
from right to left we have a provider
interface that receives a generic Json
RPC request
um and returns a generic Json RPC
response we have two different
implementations one for L1 one for
optimism these would basically parse the
input make it a typed request for their
respective backends uh handle it and
then again convert the response to a
generic string which is returned to the
user in order to be able to construct
these we're just using a factory pattern
so if we move one column to the left we
have a Prov divider Factory um which
would receive a generic configuration
again using strings and we have two
implementations that would parse those
configurations and make them typed and
construct a respective provider
depending on L1 or optimism if we then
move one column further to the left we
have something called the context this
is maintained from the start until the
shutdown of your application and
contains a registry of Provider
factories which is a mapping of the
string identifier to the instance of the
provider Factory if we look at a usage
example you start your application and
would register any of the requested uh
providers based on a
configuration and you store them in the
registry then when a hard hat user would
actually re request to create a provider
let's say optimism we do a look up in
the registry find the optimism provider
Factory pass on the config and ask it to
create an instance of the optimism
provider which is returned to to the
user this is um the way that we have
designed extensibility um for the
hardhead beta will be releasing with the
op stack and L1 support in the future
we'll also be uh releasing uh all of
these apis and it would allow you guys
to extend it uh for your own
L2 um now let's have a look at what this
actually looks like in hard hat 3 that
got a little bit complicated on a
technical level but from a user side
it's actually quite straight forward to
use so here we see an example of a heart
at 3 user config at line seven we have
two networks defined EDR L1 sapoia and
EDR opoa they both have the EDR type for
the backend simulation um the first one
has a chain type for L1 whereas the
second one has a chain type for optimism
this is communicating to EDR which
typing system to use use um and when we
switch to an hard hat script we see on
line three we're requesting the hardhead
network manager to connect to the
previously configured Ops ofoia and we
specified that for its types it needs to
use optimism this is informing the
typescript type system uh that the
estimate L1 gas function needs to be
available which would only exist for
optimism and not for L1 and we make a
call to it through the public client and
then we send an L2 transaction to
transfer one way and we wait for the
transaction receipt to be included in a
block so when we execute this we're
estimating L1 gas get 1,600 and then we
see that our transaction that was sent
is included in a
block if we then go back and we switch
the network we are connecting to to EDR
L1 spolia and used L1 typing we see that
we're getting a type error for estimate
L1 gas as this is not available for L1
networks and the vhm uh object knows
this um so this is a sneak peek at some
of the features that will be available
with multichain and the kind of simple
user experience that you get as a heart
hat user um if you want to learn more um
we've had several other talks already at
Devcon uh we had a talk um about the
Future Vision of namic foundation and
the products that we're developing uh we
also had a talk which was a preview for
hard hat 3 um and tomorrow we'll have a
talk by the slang team slang is a
compiler as an API um for developer
tools and this is basically useful for
writing your own linters doing
formatters Etc so if you're curious
about that go have a look at them
tomorrow thank
you all right so we do have some extra
time for QA uh feel free to scan the QR
code if you have more questions for wden
uh in the meantime let's take this one
um ARB has pre-employ contracts that do
not exist as evm code on chain instead
is go code embedded into G any efforts
to handle
this um so the way that we could
theoretically handle that is instead of
having it as go code we could include
this in the Genesis state that is uh
deployed when you're using uh an
arbitrum L2 chain
all right so let's wait for a few more
seconds we have another one here
when when hard hat at three um I think
we don't have a announcement uh date yet
so stay tuned we have an internal Alpha
going at the moment um but the beta will
be sometime at the start of next year
but there's no definitive date yet how
does EDR compare to foundaries anvil
um the hard hat simul or the simulation
component of it and the RPC that's
exposed is comparable like identical in
that sense to Anvil the performance is
also very comparable uh we have a
slightly different uh way of maintaining
our state um and as a result of that if
you're very often switching between
different states uh so going and doing e
calls and jumping back and forth between
a previous state making some
modifications and jumping back in those
use cases we're often faster um but from
a use case perspective they're the same
um we the only difference that we might
have is we haven't released our crates
yet which I think Foundry or Anvil has
um but in the future we'll be releasing
a first version of EDR as well as crates
on all right perfect uh let's remain on
the stage for a little while to see if
have more questions
all right if you have any questions you
can also meet me afterwards and our CTO
is also here who can answer any
questions about hard hat 3 all right
that would be great thank you guys so
much and let's give a round of applause
to wam thank
voice over about tomorrow
uh just to give everyone a heads up
tomorrow uh we can reconvene here at 4
you guys so much for coming
great
h e
n
