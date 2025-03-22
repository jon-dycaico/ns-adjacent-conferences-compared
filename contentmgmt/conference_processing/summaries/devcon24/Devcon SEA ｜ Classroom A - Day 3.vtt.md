[Music]
[Laughter]
oh that's
oh for
is
for for
good for
I
a hello
hello oh where's my
clicker
test can you beat box can you beat box
um welcome to M day uh you guys are
amongst the one that woke up on time
probably more people were trickle in
over time so um two years ago alvarius
who is about to give the opening talk uh
presented the first version of mud in
Colombia um and from that onwards a
bunch of people kind of like thought it
was not that bad of an idea and um
started building things with mud and
over time we improved mud through like a
major version mud 2 and more teams came
in more stuff got built and and today is
going to be really interesting because
even compared to last year it's much
more focused on people showing what
they've shipped so whether it's demos or
like learning or whatever it's less it's
less speculative and more uh applicative
is not really a word I guess but it's it
it's just much more concrete so I'm
pretty excited about that but uh water
fresh we'll have flow come in and and
talk a little bit through first the
H from on um and then after that we'll
jump straight into demos um list of like
rapid fire five minutes demo from a
bunch of people so yeah on that I'll
pass the stage to alvarus thank
you thank
you all right my name is my name is
alvarius and I have the honor of doing
the intro keyot today and I'm gonna talk
about the past the present and the
future of mud um some of you might have
lived through the past of mud with us
and some of you might have just
discovered mud so after this hopefully
all of you should have the same
context past present and future of mud
or with the words of Kent backck U make
it work make it right and then make it
fast it fits surprisingly well to the
phases or chapters that mut went through
um so I thought I'd I structure the talk
like that um so we start with the first
chapter make it work
it started basically three and a half
years ago when Justin and I um got
really inspired by Dark Forest and
decided to build our own fully onchain
game and so this was a very early
version of what we started building
building um back then it was called ZK
dungeon we quickly removed all the ZK
from it because it actually didn't
really matter for the for the game
mechanics um but the game at the name
stuck for a little
bit and then after around six months um
we had this all the game mechanics were
really really polished um all the all
the UI was really polished polished as
well um but we made one big mistake
which was we didn't really do any play
tests until then we really only played
with the two of us we thought it's fun
and maybe with a couple of people from
The Dark Forest office where we were
working from at the time um but yeah we
never did any larger scale play tests
and so when we did our first larger
scale play test um after like 6 months
we realized it's actually not as fun as
we thought and so lesson learned you
should do play tests early and iterate
based on that um we then tried to
iterate from that point on but because
of the custom Network stack that we had
built for this game specifically because
there was no mud at the time um
iterating on this game was actually
really hard and for that let me let me
illustrate just real quick how we had to
do things before mud was a thing um we
had positions in our game so we created
a mapping on our contracts and then geta
functions on the contracts so that the
client can initialize the initial State
when the client loads up and then we
also had um events whenever anything
changed on the contract so here now move
function we have to we have we had to um
like set the set the storage but then
also emit an event and then replicate
the whole state on the client um and
then we had to do that with every type
of state that we wanted to have in our
game position was obviously not the only
type of state so Health
Energy
skills inventory and so on like you you
get the idea lot of boiler plate just to
keep the contract and the client stayed
in
sync and then at some point we also
discovered ECS which which then kind of
like made a big impression of us on us
um it's kind of a pattern that people
use in the you know traditional gaming
industry a lot to manage the complexity
of games and so around this time we
decided to basically trash what we have
so far and instead build a framework for
ourselves to solve our own problems so
that we for the next project can skip
all the boilerplate and jump right into
the the game mechanics and iterate much
more quickly and so that's basically
what became the version one of
mud we basically implemented ECS on
chain and it worked pretty well uh at
least in terms of iterating faster this
is a screenshot of of basically our
second prototype we built and this time
it only took us a couple weeks to build
a functioning prototype um this is what
eventually turned into Sky Drive we did
play tests uh like a lot of them and
then iterated on it and we also built
another game around this time which we
called opcraft and that started almost
as a challenge for ourselves we wanted
to see if we could put Minecraft fully
on chain um and turned out it's possible
and um we built actually the Prototype
of this even in in the in the matter of
a couple days it we we you know cut some
corners but um like position for example
wasn't fully Unchained like the player
position but it was possible because M
basically solved almost all the hard
problems that we had for our first
prototypes were already already solved
so here we could move much faster and
then we did a twoe play test of this and
it was really fun people build a lot of
crazy stuff and there were even even
some emerging drama there was uh one
player who claimed a lot of regions
around the spawn and then claimed the or
declared the autonomous People's
Republic of op and um it was basically a
Communist Regime they they you could
join the Communist Regime by giving up
all your personal belongings and they
even built some onchain and client
extensions to basically be able to join
the the the autonomous peoples Republic
and then tap into the inventory of the
of the Republic and so
on and people built monuments and it was
all very fun but eventually after two
weeks play test nothing worked anymore
and that was because worked anymore and
that was because we in our case one
example was the inventory um we modeled
our state in a way where each individual
ENT each individual item was an entity
and so once people figured out how to
mine with Bots they had like tens of
thousands of dirt blocks in their
inventory and then each of those dirt
blocks was a uni client and also because
of our data model um and so after two
weeks people had to download multiple
gigabytes of data just to boot the
client which brings us to our next
chapter make it right and to have a full
stack framework and this this these
patterns to iterate faster um and it
proved that the developer experience and
the iteration speed was much faster with
it but it had some fundamental
limitations and for that to illustrate
that um I'm going to give you a super
quick ECS crash course in case you're
not familiar um it's very simple ECS
stands for entity component systems and
entities are basically just IDs and then
you associate data with them with
components and it works really well for
something like position you can have a
position component and then each entity
has their position in this component
works well but then for something like
an inventory it's much trickier because
you have to you know you have to
associate everything with entities so
you have basically have two options for
an inventory um option one is what we
used for opcraft which is each item is
its own entity and then you have
something like an owned by component
which basically Associates the owner of
this entity with the enti with the item
and then you model the inventory that
way but then you run into this problem
with you know 10,000 unique dirt blocks
in your
inventory um another option is a little
bit more hacky um you can basically
create this kind of pseudo entity by
something like hashing together the
player and the item um and then that's
your entity and then you associate the
number of of entities or the number of
items the player has um with this pseudo
entity but it's really hacky not nice to
work with you know you have only still
one one column for player and item and
in the worst case it's a hash so you
can't even really see what's the player
and what's the
entity then we um had a realization
which is um ECS is basically just a
subset of relational
databases and um it has one limitation
which is the entity has to be the key
table which made modeling something like
an inventory much
easier and ECS can still be represented
within this new model because it's a
subset so you can now have uh something
like the position table still um just by
using the entity as the only key that
sounds like an easy change but it was
actually much harder than we thought um
we proposed doing this
um early in
changing the world framework to work
better with the STA model but turns out
we were wrong it wasn't just a 20-minute
Adventure it almost took us um an entire
year and was basically a full rewrite of
the entire
thing and migrating from version one to
V2 was pretty painful for the people who
started building with version one we
felt that in our own team and we started
build the first version and then we had
to migrate it to the second version
which drove kusaba our main engineer on
Sky Drive almost crazy um but once we
pushed through it it was worth it um the
gas was way down because we focused way
more on gas
optimization
and the the improved data model on the
improved the improved sync stack meant
that now you could load the client much
much much
faster and so once we pushed through it
it was it was worth it and kusaba was
happy
again then more and more teams started
using mud and also larger larger Studios
like CCP games started building um their
new game e Frontier on mud and so we
realized oh and more more more and more
te teams were already pushing for
production back then and so we realized
okay it's time for an audit um we then
with open Zeppelin to audit the core of
mut but still maintain the flexibility
to add more features as modules because
mud version two was built to be very
modular but what that also means is that
there are no more breaking changes in
the core of mud and that now means that
we can on our end first focus more on
the the Integrations and developer
experience um but also other third
parties can now you know a couple things
um that we built in terms of developer
experience since then um here you see
the world Explorer which basically
allows you to interact inspect the
transactions that are happening in your
in this case local client but also
remote view where you can inspect all of
your tables data um yeah in in the in
the world explor so all of your onchain
state you can just inspect it
here and then we have a second view of
the world Explorer which is a slightly
more complex table um where now we can
even use SQL to uh filter the table
completed or the ones that are not
completed and then the last thing I want
to show you is again World Explorer but
the world Explorer is basically just do
your ey for all the other features that
we had to build below that um here you
can see the world EXP exporer
automatically synchronizes the ABI of
the world and you can interact with the
ABI through the world Explorer and then
when you modify your your contracts your
systems um it's automatically picked up
by the you know contract Staff Runner
and it's going to update the AI on the
world Explorer immediately so you can
again interact with your new
functionality on the world Explorer
immediately and these you know like
these stable interfaces enable um more
and more Integrations to be built and we
wanted to take that commitment one step
further for it a stable interface and so
we're now working on an on an ERC for
the store standard so for the events and
the interface of the store um it's
currently in draft State ERC is 7813 if
you want to follow along or join the
discussion and yeah the hope is that
that will allow more and more uh tools
and Integrations to be built on top of
that and I want to give a shout out to
blog Scout at this point because they
already built bu an integration format
so now you can go on blog Scout explore
the worlds there and um even inspect the
table data directly from block
Scout all right all of that brings us to
the present chapter of making it
fast imagine you want to join a new
shiny autonomous
world all right it doesn't load but just
imagine use your imagination um but then
suddenly you greeted by a fox and the
fox tells you that you don't have any
funds on this
chain and now you have to find a bridge
to bridge the funds to this chain and
then you have to approve that
transaction and then when you want to
make a move in the world you have to
approve that transaction and approve
another one and every time you want to
do anything you have to approve all of
those transactions and we don't want
that for our games at least like while
when you're logged in we don't want to
hit approve every time and so there
there already is the foundation for very
smart very smooth onboarding in the
contracts of mud but we can take it
further with like clients side libraries
and deeper integration with smart
accounts so um what M already allows you
is to create you know a session wallet
and then create a scope delegation um
and then avoid that approval popup and
here's what it looks like in action
hopefully that one
loads so you can see you can you could
connect a wallet here or you can just
create a new wallet if you don't have a
wallet yet in this case one that's um
secured by a pasy and then you get an
allowance on this chain immediately
which is basically some some e that you
can only spend on actions on this chain
and then uh you basically approved the
Del the delegation scoped and temporary
delegation to a session wallet and now
you can make moves in this game um
immediately without having to click the
approv button all the
time and one thing you also is the fly
was moving pretty fast um that's
something I'm not going to talk about
about right now but we have another
session later today that explains um how
the fly can move so fast um okay B quick
bonus chapter what's happening in the
future after making it fast um make it
scale we can already see the first
worlds that are starting to you know
outgrow uh single chains and we can see
much more worlds that are some of them
presenting today that are basically you
know have a clear trajectory of
outgrowing a single chain even the most
powerful single chain so we eventually
have to scale those worlds across
multiple chains and mud was always about
um improving the developer experience um
and so one thing that one thing that
will be a big theme of next year will be
can we use mud to basically abstract
away the multi-chain develop experience
and just make it feel like you're
building on a single chain but have the
ability to scale across multiple
chains all right with that we've
completed the mud time travel and I'm
very excited for what's next we'll see a
bunch of demos and then also later a
bunch of talks um and we have a gaming
Corner over there where later you can
try out some of the Mud Games as well um
and then later I don't know what time
but some something around one or
something we have also some some
announcements to make um so be sure to
catch that and yeah with that thank you
very much and have
fun all right um alvaris cannot leave
yet um we're going to give you guys
about 30 seconds to scan this cure code
code um log into zo pass uh you don't
need a frog for this interaction um but
you should have frogs if you don't have
frogs anyway so you scan this thing and
you can ask questions anyway so you scan
this thing and you can ask questions to
alvarus they will appear on the screen I
will read its worth of question time so
hurry
up everybody's busy making ZK proofs
whoa okay
first question are there any are there
any plans to make mud use less gas
alvarus that's a great question
um so we spent already a lot of lot of
time making M to much more gas efficient
than mud one and now we're at the point
where if you use mud to do the things
you you know like if you would build an
app from scratch and you would set the
storage and you would um emit an event
um you know to sync the state on the
it's not going to be much more gas
efficient actually than than to use mud
um so it might seem like it's using more
gas but that's just because there's so
much stuff that you know comes by
default out of the box that you would
have to implement yourself in solidity
if you if you wanted to get to the same
um functionality so um while we always
you know optimize the stuff it's it's
not as gas inefficient as you as you
might think on first side thank you um
the other the next most upvoted question
is sorry I am a noob thanks for coming
by the way if you're a n uh we
appreciate why is it good to put
movements on chain for
example it's essentially I mean it's
it's almost like a philosophical
question but the more stuff you put on
chain more Downstream Integrations you
enable because it's it's like a you know
you're deploying to this public computer
and this public you know database that
anybody else can also deploy to and the
more stuff is in there the more can be
used for Downstream integration so let's
say you put movements on chain um now
somebody could build an integration that
you know does something if you move to a
certain position that wouldn't be
possible if you don't put movements on
chain thank you alvarus another round of
impl
please all right so we are getting into
our rapid fire demo section where you're
going to see a lot of stuff and no time
for going on your computer and catching
frogs if you blink you lose something
the first person we have here is brief
kendle uh brief kendle is coming here to
show us aw aw RPG an onchain RPG built
with mod that explores multiple games
genres and Mechanics for you now brief
kandle uh thanks for having me
here uh so
we coming up so uh we are aw RPG we
build tools so that uh Web Two game devs
can build complex system that's aw so
actually a game sucks because to make a
world you need complex system but there
are cost to making games onchange Hefty
costs and uh but the benefits not
validated let's let's face it it's not
validated nothing works right now in
this space otherwise we're going to see
a nft 2.0 right now so but so only when
the benefits is larger than the cost on
chain otherwise offchain uh so we are
we'd like to make a proposal which is
mechanism that's collectively people can
build on top of of them so that they can
become merged into complex emerged into
complex system that feels like aw and
actually it is going to be this is how
we going to work uh so we have templates
going to reduce the cost and then we're
going to adapt this kind of RPG that's
uh already there and then our basic unit
is ft and ft for composability yeah
that's how but I don't have time to show
you guys and also it's boring uh so in
the end we're going to make complex
system uh that's reduce cost it deliver
web to ux and then since we know
benefits is possible so you know that's
the extra sugar on top um so basically
we're making an onchain RPG Maker for
web to devs so we're going to show some
demos um and people will get bored
otherwise uh we make seven kind of
mechanisms uh in the short time of a
year so this is Rog like some of you
might play it it's a t base PVP you have
multiple players in the dungeon you can
go down the dungeon and PVP is commit
review so it feels like rock paper
scissor so this is our base defense here
this is my favorite I spent three months
making it you can make ships and all the
maps are lzy updated you can mine stuff
to view ship and then you can laun ship
to and then you can put them into diff
on the map anywhere on the map you can
either do normal travel or you can do
warp travel so then you can you can
attack enemy ships and enemy buildings
everything on the map every entity on
the map is um attackable so
um and then I did I spent three days
doing this isometric transformation it's
the same anching data just cats and then
also the map is isometric so you see the
previous you got we got the Rings now
it's the
donut um then uh another one is shoot
them M shoot them UPS so basically you
command a ship on the map and yeah
flying lazy updating you can update your
upgrade your ships and then you can uh
like speed weaponry and stuff and then
right in the in the SL so oh not t t
base I don't have much time so T base uh
we also make it and this is my personal
project uh I'm not going to show it
because it's and ffw so but yeah I'm
making it so anyone liking it can call
talk to me we can yeah we can yeah and
uh we also have a demo play test demo
like right over there over the computer
over there so yeah you guys go go play
it uh have fun I'm not going to shoot
this so again why RPG mechanism because
we can achieve gun complexity with
composable
mechanisms remember the Starships we see
earlier we put it into RPG world that
becomes a
dragon so ultimately we want to make
focg as easy as fing nft yeah thank you
uh thank you brief candle um another
round of applause Okay so next uh we
have sto cars who let me get out of the
way who is showing us battle for
blockchain an onchain auto battler and
strategy game between forktown and Spoon
City uh on to you sto cars thank you
everyone that's not mine
all
right so when I was a child I used
maniacally play strategy games basically
all day
long right can can it work can we
actually show the demo oh it's should be
in the presentation
should I open with my own slides you
don't have the slides the
presentation yeah we can do it this way
that
way but I'm not connected to the Wi-Fi
here so want be able to show the the
video
can you just open my presentation Google
Slides um anyone knows how to
beatbox I can bring them the mic I can
only do very basic beatboxing
like see you have to do better than that
now because otherwise it's going to be
right we got the presentation I I hope
so at least
all right can we start all right hello
everybody I'm stash um I'm going to show
you the ball blockchain which is the
massive fully onchain war strategy
game uh so when I was a child I used to
manically play strategic games uh
basically all day long so I grew up
enjoying them but I noticed that there's
something missing so digital wart was
exciting but it lacked any connection to
like real
reality outside of it so my decisions in
game didn't really exactly transfer to
any positive things in my life and to
some it might be great but for me
somebody who truly loves games and the
experience that they give um it made
them kind of boring so over the years
I've heard many strategic strategics uh
feel basically the same so our actions
Were Meant to have real consequences yet
it didn't happen so that's why I'm very
happy uh to present you a B for
blockchain today which is a massive
onchain war game built on Mad uh with a
financial Market underneath actually so
we brought of about financial markets uh
to the game category I hope of games
that with a financial Market underneath
so you start as like you can support
your kingdom on its journey to win the
war that's basically your whole goal
here so once you start playing you can
join spoon city of or for town both with
their own history and cultural
heritage so shortly after you will be
put into the uh huge conflict in the
culinaries so in ball blockchain players
are offered a wide variety of tactics
thetics that can lead to Victory so we
can upgrade your kingdom set up personal
village where you passively create War
resources or establish a strike force as
you can see right now in the demo uh and
uh fight bottles in the AO botling
format that you can know for example
from Team fight
tactics so you will encounter um more
than 24 distinct zones and cities so you
have 14 unique Heroes as you can see
today and um the battle field and the
state of the battles distribute our
in-game
currency
so yeah we quite excited to say that
it's going to launch in Alpha very very
soon and well uh that's it if you have
any questions you can ask them me quite
later all right thanks a
lot thank you star um so before I
introduce our next speakers if you're a
speaker or doing a demo or anything can
you please come to the front to register
uh it seems like we're missing some
people but I see them across the room so
it it would be really useful if you
could come here and register register
with the AV crew okay thanks again star
another Round of Applause and
um now we have drum and vany who are
going to present us um biomes biomes is
a fully ENT voxel world where everything
from every single or and item in the
game especially Sakura is running fully
on Redstone mainnet um please welcome
them on stage
okay hello everyone I'm davani from
biomes and we believe that a crazy new
asset class enabled by digital matter
and smart items will unlock
AWS okay let's go so if you haven't
heard about biomes it feels and looks it
feels and looks just like Minecraft with
everything on chain for the first time
ever items players physics actions even
movement is fully onchain uh the slide
hasn't
updated uh wait can you share my screen
the my laptop no no
uh can you take the input from the
laptop share the laptop
one second there's going to be more
beatboxing
guys I can't take it anymore fix the
laptop
any any airplane
uh to all the newcomers we're currently
stuck on a technical problem but things
have been extremely interesting before
you arrived it will continue to be
extremely interesting so please stick
around try the
H oh
no it's it's over
here it shows no
HDMI is is the signal not coming over
here I saw it over
here because it was a ball without it
wa all right let's let's um all right
let's see if we can find more first
there was mud mud is very dirty we're
going to use Cory Cory to dig it upy
Cory to dig it up with all the dirt we
dig up we build
Redstone Redstone
Redstone now what else would you do with
it so now we put some voxels on a
blockchain yay he's going all right that
that's it I I think this is the demo I
guess uh um maybe we might do a screen
share but if not okay here's what you
can do right if aw you can try the demo
on your and then this is a decentralized
demo cuz it will run on all of our
computers and we don't need this big
screen anymore so feel free to do
that it weip guys all right well um
thanks drum and Van as they said their
game is live you can go on biomes aw to
play it um still Round of Applause for
the two speakers please all right next
we have Kel from blog Scout um to show
us the integration of M within block
Scout uh please welcome K on stage thank
you guys
I'm just a demo I'll
from oh my God is it going to be
another okay
another thanks
Christ this is so broken this
nothing
works am I tweet
did they have an option to upload their
slides
beforehand yeah I guess that's probably
why they ask for slides to be uploaded
you get this
problem Oh
God how you
doing you're welcome we want you guys to
free work all of these people are going
to be fut SC customers so you have yeah
they have
to lock Scout sorry for the technical
issue hopefully Kier is going to be able
to yeah more bid
boxing
what everything is dirty talk with d
games
games to
exist another joke what did one mud
puddle say to the other we really need
to stick
together more laughter
please
yes ask GPT or CL
uh 3 minutes please stand by here um
there is water in the back if you want
to uh drink um if you want more
beatboxing please make it be known if
you want more jokes from Peter Pan
please make it be known as well make
sure you draw the difference between
beatboxing or it would be unfortunate if
you get what you're not expecting um
wait is it working let's go back to
Carol
no one two three my name is Kil I'm the
head of research at blog Scout so I hope
you've seen this Explorer before already
on Redstone or any other chains we
support blog Scout is a most widely used
open source blockchain Explorer for
different evm networks we have more than
different Nets rollups test Nets and so
on and so one of the greatest Partners
we have right now is redstone team and
we are proud to support this chain from
the very beginning from the first block
they have ever sequenced through the op
St rollup so just let me Demo our blog
Explorer which is available at explorer.
ron.
XYZ and for Garnet testet explorer.
Garnet chain.com
so first of all for the most cool
feature today that I wanted you to show
show is the features that we
specifically built for Redstone for
supporting M worlds m games we had block
Scout laes unfortunately we haven't
developed any yet but we'll have playing
them and we have exploring them on chain
to observe the contracts to see what's
going on how to interact them how users
are using them so that's and if you go
to the tab you'll see a list of all the
different world contracts and games that
have been indexed and pared via the mod
indexer and uh so yeah this list is
quite huge especially on garet it's
hundreds of different games and so you
can pick any and then once you select
the particular World contract you will
see this mod tab that is basically a
table view that provides you an overview
of all name spaces of all tables that
are available within the particular game
so you can paginate across this list you
can find a particular table
you can search by its name by the name
Space by the table ID and so on so for
each of these tables you can see quickly
the snippet of the table schema you can
see all the fields their names their
types the keys and values and then for
example let's explore what's inside the
character info table in some of the gar
chain
worlds so once we load this table we
have this table view view which is
similar to what you can find in any
database SQL based Explorers so we see a
bunch of different records we can sort
by the character id we can sort by the
second column if there is any in the key
we can also filter by the specific key
values on the index columns so let's
find the user with the ID 150 we can see
its name we can see all the
fields we can also jump into the
particular record to see all the fields
in in the vertical mode then one of the
other features we have here is that you
can also share the link you can copy the
link and share with slack within the
telegram with your community to go to
allow other users to go jump into
directly the specific record to the
specific tap so you can copy the link to
the particular record you can copy the
link on the previous View to the
particular table and so
on so that's what we have on the table
View and then one second feature that we
recently released is related to the
contract
interaction so if you go to the contract
tab on any of the games contract first
of all you'll see redesigned the
contract interaction tabs that allow you
to write and read directly from the
proxy contract but word contracts
doesn't have a lot of useful functions
here but what we built specifically for
M enabled contracts is the separate tab
that allows you to interact with the
specific systems under this world so in
a so first of all we are getting the ABI
from the mod table um SC and so we match
the abis and combine
the um field names for example in the
function calls so if you go ahead and
verify all the system contracts this UI
will be even nicer because all the
function names and the argument names
will be verified and displayed as they
intend to
be so yeah say it again that's pretty
much it let's see if you have any
questions okay thank you Carol thank you
um all right I hope we're going to stay
in a stable era where the HDMI cable
keeps on functioning instead of failing
our next speaker is Nico from Cafe
Cosmos uh Nico is building a cafe Cosmos
which is an anent Cafe management game
built with mod and unity please welcome
him to the stage thank you
is it
working all right I always wanted to
speak in front of a mic
before uh this is Cafe Cosmos uh this is
a cafe management game set in outer
space uh it does a whole bunch of things
it uh it has its own uh demand
simulation engine uh but overall it just
uh looks nice and fluffy and makes you
want to play it um so so anyway we're
honored to be here we love everyone here
so so yeah this is this is Cafe Cosmos
super stoked to be showing you
guys it's a chaotic
era how always wanted to try standup so
I mean I guess this is my chance
[Applause]
eh wait keyboard assistant what is
this all right rewind
all right y'all uh so yeah my dudes this
is Cosmos uh as you can see right here
we're we're building the sickest Cafe uh
here we're about to make a we about to
make a smoothie um so we can do that
right by just putting our smoothie
inside of the blender as usually does uh
we can water plants we can take care of
animals uh we've got different beings
that actually uh beam from different uh
Parts in space to come to your Cafe so
this is a Japanese bear uh so uh one of
the many parts of the space that we have
yet to conquer uh and uh and here you
have different trees now you can
interact with these different items you
can uh collect wood you can collect
fruits you can expand this Cafe uh and
you can actually strategic you can even
uh strategically pick your ovens and all
of this is actually
changing dynamically on time right so if
everyone starts using your oven that
oven's going to go down in its uh in its
power right so you have to strategically
try to figure out what the other players
are going to be doing going to be doing
and and and we do this uh in you know in
in try to do this in the in the most
userfriendly uh interface possible um
overall we just want everything to look
beautiful all the time uh here you see
our new Quest system that we just
introduced so now you can do daily
quests so for example in in this
scenario we're we're doing uh growing
five tomatoes a day so this allows you
to check in on on your Cafe every day uh
do different do different quests uh try
new things out this is our new store
right here so using the ca the cafe
points that you earn in Cafe Cosmos you
can buy different things uh we've got a
ton of new items that we're adding uh
pretty much every month to the game and
uh yeah dudes this is Cafe Cosmos uh
thank you for tuning in and uh I'll be
giving another talk later W all right
thank you Nico uh next up we have ddy
from the Dark Forest Arron Community um
they're presenting their recent effort
porting one of the first ever fully aing
game Dark Forest to Mud God bless you
guys I've seen the code base uh but it's
important for preservation thank you D
please welcome on stage thank
you very
quickly hello I'm ddy from
have our color is
clean try to how
to it count
show
strange speakers how to the
because you don't have if they're going
to come
like don't have internet you know what
I'm saying okay okay I have this
one ddy you need the mic okay okay okay
recently wait you already have the demo
okay the first hello I'm ddy for account
team recently I part dark first mod okay
then uh
closer okay okay
hello okay uh hello I'm du from D
account team recently we part dark for
down mod uh actually I think everyone
knows dark for already so I just want to
highlight that we have active Community
Development ecosystem actually uh build
for about one and a half years introduce
a lot of new features for example new
artifacts uh Union system and uh
circuits okay and the beginning the
summer uh luckily uh the mod is very
developer user friendly so the first is
the variable t r down block time uh
however uh we update it to it to all the
game logic update based on tick instead
of block time then we can game post and
resume and we can uh adjust the game
State update speed that speed during the
game is on uh actually here here has the
so you can feel uh I uh yes I will go to
another slides uh just uh to show we can
plugins uh is admin control plugins we
can CH make the game uh PA UNP and
change the ticker rate uh when we set a
low ticker rate the time become very
high and the second I want to highlight
for our Pro highlight for our project is
that we try to uh make in uh fully
leverage scalability and composability
here's the answer uh we we try divide
the whole game into PL uh Planet players
and and artifacts and the mark question
uh question mark uh is where we can find
and explore the compossibility uh
actually uh we can introduce more
entities protocols later uh uh before
compossibility is based on data however
we want to introduce uh the logic where
can uh make the logic and the data data
have a uh have a strong connection as
you can say where can different
functions can be added to Creation
activate and disappearance of uh
artifact uh and uh even uh can create
his own artifacts uh uh which means uh
players players can join the development
uh yeah that's U uh that's our three
highlight Parts uh that's and thank you
that's all
uh thank you ddy um so ddy was talking
about variable tick rate that reminded
me of Eve online tie dye and well we're
lucky because next up we have Scott AKA
CCP overload who is going to share with
us a demo of e Frontier uh an onent game
created by the developers of you a video
transfer this is a new operation as
the
a
for Kingdom please welcome him on
stage um TN will be demoing for the
kingdom a browser based RPG currently on
testnet hello okay thanks guys uh so
yeah super great presenting our game
right after e Frontier like just
super so okay hi everyone uh thanks a
lot for joining many one they want to
be okay so can you let you know repeat
the video for me thanks a lot okay so
our vision is to craft an expansive and
persistent game world where players can
freely a vast open world where you can
explore and fight monsters for valuable
materials F other players to steal to
steal their items or simply lead a
peaceful Life by chopping away some wood
the true goal of the game is becoming
the best at what you do and contribute
the most to your kingdom imagine you're
the best blacksmith in the whole game
and only you can craft the most powerful
weapon it means your Kingdom's Warriors
have an edge of their opponents or you
can even sell your weapons to other
kingdoms as well for a profit
and so here I'll show you the first 3
minutes of our game VI recording but you
can definitely already play the game
even on your smartphone so the first
thing you do is to choose one of four
available Kingdom and start building
your character so you can see here that
uh that's basically me creating a
character called Defcon for the win I'll
be able to customize the character's
backstory by answering some of the
random questions about the characters
childhood or their personality your
choices here determine your character's
starting stats like choosing that you
stole a trinket from a rich woman when
you're wor 10 will get you a boost in
agility the first the first thing you do
in the game is claim a welcome package
where you'll get all the beginner items
necessary to start basically you know
doing any any we have like some text to
support onboarding but I'll just you
know like skip it to get to the fun fun
parts
so right after that the next thing you
can do you can prevent yourself from
punching some monsters
barehanded so the next thing you can do
is to browse some available quest line
quest as well as story lines you that
you can explore through Kingdom specific
quests uh next up you can move from your
starting point to different parts of the
map like here I'm moving to a grass line
outside of my starting City moving right
now kind of cost 15 seconds to computate
that right now we don't have an like you
know a zoom in map or an INT map like
doas or Rak Fu yet but we'll get there
sometime you can see during that time
that I've also equipped a batttle
skill next you'll be able to engage in
PVE in each tile like right now I'm
fighting a slime enemy as the game is an
out of battle and fully on chain it
means that right now the outcome is
deterministic and the result of the
battle is already decided once you click
on the uh on the button but the Amion
here is like you know kind of like a
good
representation here you can also engage
in PvP with different players in in this
game like for example I can challenge
literally the best player right now and
probably will get decimated in one move
yeah yep that's because soulmate or like
d here dandi I think that he's here
thanks a lot for coming
like you know he is stoked with very
very powerful weapons and
equipments so as you can see here the
map is right now very huge and the main
goal of this demo basically is to defeat
ignes our first raid boss it's a
powerful Dragon that can drop the best
loot right right now once
defeated so bottling monsters bosses and
you know farming resources will enable
you to craft various items to get
stronger in the future these items can
be tokenized and sold to other
players uh that cannot craft them so
that's our demo and like you know
just yeah I'm just going to skip to I
have like five seconds left I can't like
you
know can you change the I mean yeah
somehow I can change it
to to the next slide
like can you manually change like you
know I don't have enough time yet so if
you can like you know go to the like you
know kind of like a last the last
slide
yeah oh so okay like just 5 seconds on
this this is what we've been do doing
for the next build as well we'll add
more Co-op features and basically a card
demo game that we kind of stolen from
Final Fantasy right now and yeah just
can you move on to the last slide please
so yeah thank you guys the game is
playable right now cross device on
mobile and browser so yeah just if you
can scan it and we'll be happy to see
you playing your game thank you
Tran next up we have CK uh who is going
to show us popcraft a puzzle game which
plays with and rewards assets from
moving castles disc cursed machine what
an odd decision and our game buil in mud
please welcome CK to the stage thank you
folks this one this
one
screen okay hello everyone I'm sing you
from Medan team uh today I in this field
so what's the
outcome in this field a lot of people
have do a lot of exploring and to do
something different uh so we choose the
cron and compossibility as our Co start
point and which lead us to create
popcraft uh it's a fully uh compatible
game uh which make um coron and
compossibility uh no longer just that
mean so uh the game play is just like um
pop star uh you can re by iming uh all
atom uh or B in 19 seconds um multiple
adjust item can be uh conncted to uh
elimination uh directly s atoms needed
to uh buy a prop to eliminate
okay
okay uh this is a video but i c i canot
to play
it okay so um what in popcraft uh simply
put popcraft equals to uh pixelon plus
this custom machine plus uh R swap okay
uh so how we build
it uh actually we build two things based
on month um I compatible pxel and
popcraft okay we just use pong as a game
board of popcraft uh which gives game uh
very excellent uh compossibility at a
Cod level okay so we use this custom
machine as as a game atom Factory uh
while we playing uh this custom machine
we think uh how we can use this material
more useful uh we and up came up an idea
of uh we just use this material in
another game
yeah okay uh we use rest drop as a game
Market Place okay um this SW is DX or
Resto and um it make the game problem
exchange uh game problem price
very uh transparent okay so uh profram
now is live on rest minut uh you can
play any
time okay uh also you can play Beyond
popcraft uh you can play
po uh p p game prop in uh popcraft uh
raise the price of game prop uh you can
also play uh this custom machine um
produce machine and producing material
and uh uh sell or R SW uh you can also
just be a treat on rest SW uh buying and
selling uh T material they are on rc20
tokens um okay you can do
uh choose any of the above or all of the
above okay compatibility in
pop okay um we can replace um this
custom machine as any other project
which has has Y2 tokens uh as game prop
and game atem uh also we can replace a
red drop uh with any other DX okay one
more thing I think we need to make
crypto uh vable in for game uh M have do
a SC but um we also need to do
mon thank
you thank you very much CK um next up we
have Xavier um Zer is going to demos
project Mirage a fully Unchained City
Builder which play with different
financialization and tokenization
strategies from the crypto world please
welcome on stage zver thank you
FS did you steal someone's identity
Xavier no
okay uh hey um my name isos Closer
Closer closer okay hey my name is Xavier
um I'm the co-founder of project Mirage
um project Mirage is an island building
game and we are uh using um Redstone
garet test net and uh we are building
fully a mud um so let me Demo the the
game so when you begin it's not like
that uh it will be like an empty island
with a city hall in the middle um you
have to PVE road yeah you have to PVE
Road and like add more buildings you can
see their drop downs
uh we have a road pavement you can drag
can save the the the road and add like
more buildings there are like a virus um
category of buildings they are
residential the first thing you need to
build is like resident um buildings to
add like labors but you also can build
like different um commercial industrial
um Civic landscape um to like fulfill
certain requirement and uh produce
certain uh resources so for example I
can put like a house here and uh put
like a commercial building
nearby you can view the details while by
clicking into the
buildings uh we have some like res
here oh now oh level up unlock some
buildings and put some names like X
Island um by reaching like certain
levels you all see some something like
this this is my own Island so I have
built like various um like uh buildings
um we also have like a uh a
functionality called summon so um I
don't have like resource to to summon
any character right now but um you can
view the character here for example I
have this one um we have some
description uh and uh you can actually
um produce resource um by assigning um
the character so for example this one uh
he can plus 4% U onto the res yeah uh
and also we have a a functionality
called
shares so for example if I visit my
co-workers
Island I can trade shares on her Island
for to become like a shareholder um on
different people's Island uh you gain
profit by um gaining resources when um
the other owners are pretty resources so
you gain certain percentage and also you
can trade Island there's a Leaderboard
on our game tag for example this is uh
one of our um top
players and we can see um his island is
much larger than
mine yeah that's it thank
you thank you Xavier all right um next
up we have small brain but it's unclear
whether small brain is in the room with
us right now
um okay so small brain is unfortunately
not in the room with us uh you can you
can tell your psychiatrist uh small
brain brain is not real um next up with
Genji who's going to T to demo TX
Monster uh TX monster is a 3D onine RPG
featuring monsters large and small
welcome Genji to the stage thank you
wait is Genji actually
here oh we have more
ghosts Genji's
here hi guys how are you
doing you guys F here SL Pokémon go
here okay so this is a chance for us to
play the game similar to Pokémon
go so please I need a clicker like
you okay so we can do without it okay so
you can just skip into the the next
slide I this the game Loop so the next
one the next one one the next one the
next
one okay the text manter is like the
monster capturing so that is the 3DS web
browser and we doing with the unity so
we are coming from the web tools like
Studio games so we want to bring like
the gaming experience inspired into the
weet free and the fully onchain games
blockchain so uh this one we will bring
like the whole news diversities like
monster system so we can try to use and
Discovery with the like a Sandbox and
open world uh please next
slide okay the game look be very like
simple we see in here we build the
characters uh we expore the world we
just like taming the monster and then we
so just following it okay next one okay
we have like a lot of features in
ecosystem but the most important thing
here I want to emphasize is the F
mechanism first thing is like we talk
about the game f is the ownership of the
access but talking about the fully
onchain game the next one
okay that is the gaming nft contributing
because we need to make sure that the
people and the user need to play the
gameing so we have in here the NFD the
the monster achievement based cosmetic
and all of the things the user need to
contribute by the finance or by Gaming
experience by go for the game itself
okay and of course uh blockchain people
earn value not only for the game and
also for like finance things so we also
have the further value so looking for it
and we get the next
one okay this is our emphasize things
the US say in the Futures we have the
user generated content it mean for
example we have like our own project
with access and then the community they
can create their own access uh make this
one and then put into the game but in
extra you can own your sub client and
you just like use accet and then you can
bring the subcontract and put into the
game and then you also have like all
other features in the game and go along
with us but most an important thing is
like if you have the better team and you
can build the client with our asset you
can do that so the UDC is the most
important thing when you play the game
if you anyone in here Play Steam
Community you have like the modding the
people we just like building the content
for the game and in extra so this is
very important and we want to build the
TX monster with the UDC in the Futures
with the matep so we can make make it
happen Okay so after this I want to show
like a little bit of our gam play okay
you see the Monster here we have like
couple of weapon we just like fighting
them get in like a contract and T house
and we just follow up you see okay like
we can put a lot of monster in here and
then in the future I really try to
inspire this game like a Pokémon go or
exra you see you can fly over the way
you can fly fly all over the mapping and
you can see everyone so I hope in the
future we can bring it there so next up
we have Rohan um Rohan and Roshan are
going to are going to present us yomen
uh it's an analytics and automation
platform for onchain Games built with
Mod on their toolkit please welcome them
to the
station oh okay let's Okay little change
in ordering uh
never mind you will have to wait a
little bit longer for Yen next up we
have Genji not Genji we just had Genji
oh my God this list is not the right one
anymore uh next up we have Ritz raspa
please welcome Ritz raspa to the stage
who's presenting ultimate Dominion a
text based RPG happening on the 2
platform testing testing lovely
yeah
awesome uh hello everybody my name is
Ritz Rosa um this is my first time at
Devcon 19 and I'm really excited to show
you what me and my team have worked up
for you guys um we've been working on
this game called ultimate Dominion for
the past six months it's going into this
I've been drawing Knights and Dragons
since I was a kid and I'm glad I'm able
to have the same assets uh as the uh
things I've been drawing and growing up
with um narrative is a really big part
to me in this I mean I feel a lot of
games in the last decade just haven't
been um haven't really been focusing on
that World building haven't had a world
that you that felt like we should fight
for and US narrative that we would want
to push forward a lot of games focus on
um building a game that feels like it's
going to outlive the players but we want
to work on a game that feels like it's
uh it's lived for and has it had AED for
and has had a history long before
they've
arrived um now heading into that game is
it this is what we have my character
name is going to be Mr slays lot this is
a beta and and I'm going to be doing
this live for you guys um that's my
profile picture deal with it uh moving
moving forward I'm going to be rolling
my stats next this is uh the stats
determine what you're good at and what
you're bad at uh if you have high HP
then um if you have high HP then you're
harder to kill a higher strength means
you swing your sword heavier um agility
you're faster and better at running away
from me and intelligence gives you the
gives you access to the strongest uh
Magic in the game uh heading uh let me
actually roll my sets my bad um rolling
into here the this world is going to be
in a 10x10 grid um you're going to be
moving uh you're going to be moving
about it more uh think of it like you're
moving a piece in a CH in a chess board
uh loading loading into it here um
you're going to see uh to the right here
we're going to have several points of
interest and a yellow border this yellow
border is going to be the player uh the
player area the safe area um your
character is depicted as a uh dragon
icon and as you see that I'm as I move
through here the middle uh the the
middle screen is going to be updating
with whatever uh with the players and
the monsters that are currently there um
this uh getting into the getting into
the combat here I'm going to be going up
up against a Cobalt a Cobalt Scout
uh oh um apologies uh so the items in
this game are are the main way that
you're going to be attacking things and
dealing damage these individual items as
I as I them and uh even these low-level
items they don't do a lot they they're
mostly numbers and have small X however
when you when you couple them up with uh
with when you have multiplayer and
multiple people using several attacks
like think of a rogue with a smoke bomb
and then like your wizard casts Fireball
and lights up the lights up the smoke
bomb and does extra damage we want to
incentivize players and Empower them to
have cool uh cool cool interactions like
that that we really can't anticipate
that sort of storybuilding is really the
is really
the it's what we want to push we as
developers want to empower players to
have a narrative to push forward and to
attack with and that's that's the main
dream right now with this beta we're
trying we're focusing on this in this
main Loop uh where where you attack
items where you attack monsters get
their items and sell them um and with
with that comes well that progression
but this is the meat and bones of the
game the all this narrative stuff that
we want to do all this ambition this
this crazy world right that we want to
build is great but we want to have a
good game that goes with it um I mean I
think it's I think it's really important
uh getting into it now I'm going to be
getting to the combat here uh going up
against the
uh there we go apologize for that um
getting getting into the combat shortly
here you're going to see that uh as I
get it as I get into it we're going to
have we're going to have these uh these
actions actionable items here are what I
have to attack with as I was saying it
with when you mix and match with
multiplayer you have a you have a lot of
combination and a lot of things that you
can do um but ultimately this is the
game if you want to support it and you
want to uh see it live through you can
can join the you can join the demo with
the uh code we're going to have uh back
here and uh that's I mean I can't wait
to see you there guys um that my name is
Ritz rospa and this was Ultimate
Dominion thank you thank you
Ritz all right so next up we have Rohan
and Roshan who are presenting yomen um I
already gave the pitch for why I think
yoman is interesting but I'll do it
again in analytics and automation
platform for game built with mud um
they've built a lot of really great data
data tooling over the last year uh and
I'm I'm looking forward to see what they
have to show today thank you
hey hello my name is Rohan I'm from Yen
uh how many people here are game
developers
games okay and and how many play
games great I have something here for
every one of you Gamers and developers
so uh um what I want to show this
morning is um so can we go back my
email not able to show demo okay one
more
yes so we have Dash we built dashboard
so all of the data is on chain all of
our game data everything you play is
onchain we wanted to visualize it and
this is useful for both developers and
Gamers so let me jump into uh one of the
games biomes um so we what we do with Y
is we index all this data we then create
charts and graphs that's helpful for
both the developers and The Gamers so
here we have biomes we have like a
million transactions indexed and we
create these chart for example here what
we show is like most of the actions in
biomes is mining actions you have move
have quite a few things as you scroll
down you get to see activity over the
lifetime it had a uh it surged in the
beginning of the launch it was quiet for
some time and we see a huge Spike now
and yeah that's in biomes pretty cool
these days um we then as you scroll down
you get to see a lot of data again all
of this data is on chain but then we
make it presentable we make it uh
visualize when you visualize it you
quickly get an idea of how all this data
looks it's pretty cool and as you scroll
down you get to see lots of charts
graphs we have all those data indexed on
chain so you just uh it's just you can
create all these chain so you can chess
uh if you are a gamer on biomes if
you're looking at mining for example
it's pretty early days we have about 6
percentage of the neptunium mind at the
moment and uh yeah as you scroll down
you get to see lots of charts this is
interesting testing biomes is a 3D World
we have a 2d representation of of what
is mind and what's not so this the red
represents all the ores and the white is
all the ones that are mind so uh this is
useful for gamers and developers as let
me scroll down to the last chart so this
is all the movement within biomes so all
the everybody that's moved on it's all
plotted on a single uh 2D graph you can
see the high traffic areas at the middle
and then it's quieter at the sides so as
as a developer if you were to visualize
your game you get to see things like hey
there's a hot spot here you can probably
design you can probably build a Bazaar
somewhere far or if you want to build be
a gamer and if you want to see hey where
to position your wonder that you're
building you could be like go on to a
high traffic area or something like that
so all of this data is on chain and this
helps uh helps you quite a bit so that's
that okay uh uh let me switch on to
another game so okay I've got two
minutes so this is another game called
Draw Tech which was uh built by small
brain a while ago uh what I showed you
now was all the data that we've indexed
we've then be we able to query it plot
it into charts and graphs and all of
that I want to show you something else
interesting so what we did was we built
a uh a time travel feature for um for
mud mud indexer so basically what you
see here is the canvas on draw Tech when
it was launched this was a first block
uh this is probably small brain Somebody
went in and tested this they they they
put a tree in there if you click on next
what it'll do is it'll fet very next
block so it this is all um using a mud
indexer it goes to uh what it was at the
point point in time or rather point in
Block so it gets all that and click on
next next you can see how the whole game
developed as you click on next it goes
to every subsequent block it fetches and
then if you go back in time from you can
and then if you go back in time from you
can rewind from where it is you can go
back and all of that so all of this data
is on chain we're making it presentable
pretty accessible and all of that for
ders and Gamers and uh if you uh if you
if a project is not listed here please
reach out you just fill out this form
send in send us your ABI send us all the
information we can get it indexed U this
afternoon we are talking about our cool
new project called cand it's pretty
interesting but I need more time to talk
about it it then so thank you guys
that's all thank you um all right
so someone took the clicker on stage
after they did their demo uh no shame
for doing that but if you could please
return the clicker that would be amazing
um
so last demo before lunch and do not
head out now because I will share a few
things with you before people have out
for lunch but we're bringing back the
biomes team on CH on on chain on stage
uh to have them do their demo because we
were not successful previously so please
warm the stage again for danani and
drill actually I thought it was
R where are
day okay we're
back okay it's working so yeah hey
everyone I'm davani from biomes and I'll
start again so we believe a crazy new
and smart items will unlock autonomous
worlds so if you haven't heard about
biomes biomes feels and looks just like
and this is not on a test net it is live
on vet Stone the L2 ethereum main net
you can try today so if I just you know
I can move around in the world um I can
WD around I can mine I can build I can
craft like all the things you'd expect
from Minecraft um we have working and it
feels just like Minecraft we almost have
parody
ux okay so then what's different
so the main thing that's different
inside of the world is smart items Smart
IT are basically items that have regular
functionality in the game like a chest
where you can store items take stuff out
but but you can augment them with a
smart contract and now that item will
behave based on the smart contract so as
a concrete example we have a Unis swop
like chest which is basically a chest um
with a the Unis swop smart contract
which which makes it so you can only
take stuff take items in and out if you
transfer a token and now you have
basically like a third party shop that
behaves based on this smart contract and
the design space for the smart contracts
is kind of w because it's a regular
smart contract that any player can write
so already since our like Alpha release
a couple weeks ago we've seen a couple
of smart items being created inside of
the world so I'll just go around the
world and show you a couple so the first
one I mentioned was that Unis swap like
smart uh smart item and so this is one
of the main bazaars in the game where
people people are buying and selling
items and as you can see like when I go
up to a chest I can't just take the
items out I sort of have to interact via
this UI which lets me pick how many wood
I want to buy which is the Sakura wood
which is this new like uh rare wood that
rare religion that's forming inside the
community um and you can see it's giv me
like the current Dynamic price for this
wood so now I'm going to go into
spectator just beside this like main
Bazar fee mechanism but they're doing a
similar thing of buying and selling
items uh using a chest now you might ask
well why can't I just mine this chest
and take all the items um and that's
because we have another smart items
which is a force field Tower and when
you have a force field Tower you can
again use a cont track to control
permissions for who can build and mine
inside of your area and as and the main
thing to know is that compared to other
um like decentralized like projects
where they have land sales for nfts that
control permissions um with biomes you
can control the land forever to control
your land you have to use this in-game
item which is the force field Tower and
you have to charge it using batteries
which is another in-game item and so all
of these smart items function via
batteries and as long as the batteries
charge it will work but players can
rebel by by damaging the battery and
making the smart item no longer work so
just two other cool very interesting
smart items players have created um one
of them is this Sakura holy tree so
there's four kinds of wood in biomes but
one of them which is the Sakura wood has
become kind of Meed and everyone sort of
rallying around it and so this player
wants to build this like giant Monument
of the biggest sakura tree but he needs
a lot of Sakura logs and they're hard to
get they take like over a year to grow
and so he's created this chest where you
donated a 100 like Sakura logs which
will he which will he which he'll use to
create this tree and in return He mins
you this like nft and or we call them
passes inside of biomes and this pass G
access to his like um like to use all of
the like go inside of his buildings
other like events he's going to run and
so by donating your wood you sort of
getting access to all of those things
he's going to use in the
future in a similar sense another user
another gaming guild has created their
own like hotel where they sort of have
beds and rent out like for people to
sleep inside and to access that to
become a part of their Guild you have to
get to their chest and you have to again
transfer a couple of items to get their
p and once you have their P you can now
access all their
things um the last thing I'll show is
not a like a a p uh it is a pass but
it's not about just transferring items
but it's actually about parkour because
now we have like real- time movement you
can actually um oh it's the chunk itself
is not loading um but over here we have
basically um a place where players can
play parkour and you get to the top of
the parkour you get to again mint a pass
by interacting with a chest and only
players who get to their top can
interact with it because that's where
the the uh the actual chest is and yeah
so that's pretty much it we think smart
items can birth an asset class enabled
by inde dependent on the virtual world's
physics um we have a talk later uh in
the afternoon so come by to hear more
about it thank
you thank you okay
so um we're about to take a break for
lunch um so because I know that by
default people are not going to come
back I will try to convince you to come
back this afternoon so um this afternoon
is going to be much more focused on
technical presentations from people that
have been building projects using mod
mod developers themselves infrastructure
developers all centered around being
able to build um basic basically onchain
worlds via this technology so starting
right after lunch at 10000 p.m.
sh I
will be giving a talk on um something
new from Lis so if you're interested in
that please come over I promise it will
be fun right after that my colleague
Frolic is going to talk about hey how
with modern mod you know cuz mud becomes
classic like if you're three or four
months behind cuz these guys ship so
much stuff with modern mud how do you
build an application you know like in 20
minutes he's going to walk through
through like hey this is how you use all
the modern tools to to just go through
better um after this drum and vany whom
you just saw on stage about biomes
will'll talk about growing the biomes
GDP using digital matter and smart items
so if you thought this demo was
interesting and you want to know how it
works please come back this afternoon um
after that we'll have ju BL Blanco uh
the developer actually of the most
popular vs code extension for solidity
who is going to talk about how they are
were able to build Cafe Cosmos that you
show you saw on stage using ether Unity
Blazer and mud and how it all works
together um they were able to get like a
pretty good development speed by
combining all of these tools so I think
this will be interesting after that we
have small brain I texted small brain
proba told me I didn't know how to up
but he's for sure showing up this
afternoon to talk about they've been
working and and how you built them um
and then we'll have a bunch of um we'll
have like an hour of break where people
will will hang around the gaming corner
to to try some some games and at 4 pm we
have another uh big batch of talks so
we'll have a talk from the e Frontier
team on how they're building the
frontier technically um right after that
we'll have a talk from Nico from Cafe
Kosmos where he's going to talk simulate
onchain economies so if you're
interested in in building sustainable
onchan economies this should should be
interesting um and then after that we'll
have you Mirage uh the kind of like Town
Builder game you saw on stage talk a
little bit through um the way they
building project Mirage and then two
more talks after that we'll have the Yan
folks that you saw talk through their um
new product called the in command um and
then we'll close with um another gaming
corner for Cafe Cosmos so we have a
pretty big agenda this afternoon uh
please get out of here breathe a little
bit go outside uh get some food and come
back right before 1:00 p.m.
if you want
to catch uh something new from lce thank
catch something new from lce thanks
everybody and thank you for being quiet
um it's a small room so thanks again see
for
e
oh
he for
o
and
I up
it's can already come here it's going to
be
quick from the lunch exciting talk talk
that we have plenty of videos plenties
of ways for this whole thing to fail
like this morning so we shall see see if
we can go make make it through the whole
thing so uh cool doors are being closed
hello folks good afternoon welcome back
from lunch um I'm Justin one of the
co-founder of ltis um some people know
ltis as the company that started mud um
and then later the company that launched
Redstone chain in other words what we've
been doing is building infrastructure
for autonomous worlds um but as you
might have seen from alv various opening
talk this morning we started off by
building our an nonch gain ourselves
about like two years ago uh I was P
personally fascinated by the idea of
building multiplayer games on the world
computer following the footsteps of gub
sheep in Dark Forest we're super
interested in the IDE of ethereum as a
computer that know single party controls
that allows immutable physics and roles
that enable massive Valuable Player
based economy and as an open code based
in API by default for anyone to extend
and while these prop are pretty damn
magical um the computer also had some
significant downsides first it had no
development framework there is no Ruby
on Rails no Unity no Unreal Engine and
so that's why we basically build mod
from the ground up to make it possible
to develop onent games in the first
place without spending two two like two
years like dark first to get like a few
a few few features up we were hoping to
see the next 10 dark first emerged from
this work and the amount of projects
that we're demoing this morning is a
testament to the success of these teases
so second the issue with the the word
computer is it cost a ton of money to
run um I actually dark PR was first
running on robone test net and then they
broke the test net and then they moved
to um noses chain formerly called XI uh
because running on Main it was not
possible and this was before l2s and so
running any decently complex game would
cost you hundreds of dollars every day
even with blobs basically so the second
large infrastructure project we we we we
worked on is building Redstone and the
underlying LDA and op plasma protocol
with the op stacking the guarantee of
the world computer too significantly and
so with these two upgrades we saw the
design space open up like massively many
many games are being worked on as you
have seen in demos this morning this is
a snapshot of of the logos of the people
that presented so far but the computer
still like some pretty significant cap
and we make to the comp fix next so
first the computer is still slow as hell
um actions are being confirmed after two
plus second delays on most l2s and half
a second on the lowest latency on once
like this is about as close as you can
get and even then with all this the
other kinds of overhead from tools
usually reach for 5 seconds to two
seconds the second biggest issue is
creating an account is also like
extremely complicated you thought going
to the game store and buying World of
Warcraft and putting your CD key in was
hard we found something hard and harder
so after you create an account on the
world computer you have to like add
money to it and because otherwise
created solutions that don't bring other
kinds of problem when you start adding
this stuff up
um and so earlier today uh you know
already if you're too online because we
tweeted about it if you don't know about
it I'm I'm proud of you guys for not
spending all of your time on on on
Twitter we announced Quarry which is an
upgrade to the computer that tackled
both of these issues so the biggest
thing from Quarry is we basically
decrease the latency 99% from the no to
Common 2C block time to as low as 7
milliseconds we also and then on board
progressively um and in order to show
you uh cuz we hate the meme of like just
build a bunch of INR we should spend a
lot of time building a bunch of demos so
um the first one is
doom and it's running on Quarry um so
this runs at about like 35 FPS because
of the net code of Doom transactions are
sent to um query confirm in about like 7
to 15 milliseconds come back and reflect
the state update on each client so this
is running in real time there are no
tricks there are no like optimistic
updates or like a lot of client code to
make this work this is basically just
Doom with like a little bit of mud State
synchronization on top um and some
interesting things to point here is
every second each client is sending 35
transactions so inputs and state update
to the chain from which the other
clients receive the information to
synchronize what's shown on the clients
and because of the way Doom was written
which is very poorly I mean we we
forgive them they're the first kind of
like multiplayer first person shooter um
it's before any modern net code
implementation so there's no uh
predictive net code there's no roll back
so any little amount of latency gets
reflected immediately because the whole
game freezes so as we've been optimizing
quar of the last two months Doom became
our Benchmark there was a notorious
problem where every two second there
would be a little blip that we didn't
catch when we were working on Quarry but
that was like pretty significant when
playing Doom so yeah it has been great
to to kind of use that as a as a target
for hey hey if we can run doom on Quarry
then we can run anything we want um the
second demo I have um if it plays yes is
okay uh move the fly is um a game where
you can either move a fly or you can
move a frog frogs eat flies flies don't
eat anything they just get eaten um and
you can start playing move the fly by
pulling out your phone um either doing
face ID if you're on an iPhone or um the
Android web withon protocol and you can
just like get into the game immediately
with a smart account wallet and play
with the same kind of latency as Doom so
this same thing this doesn't have any
optimistic update this basically plays
like a web to iio game you know um and
in order to build this we pulled out the
normal mud template and we added like
two three lines of code to connect it to
query um and one last Dem I want to show
you folks is this which is basically
fight so uh we took the code base from
opcraft uh we added guns and walls um
alvaris who is the worst person at
making names at the company called it m
shoot we all hate it it's such a stupid
 name but it's called M shoot um
and there's a lot of interesting things
in this game so first all the physics is
on chain so jumps movement Etc R casting
as well so you can't just like declare
hey I'm hitting that player there's
actually like a full R cast happening on
it and all of this just runs same thing
without tricks when we built opcraft you
actually had a lot of tricks to make it
feel good this doesn't have any trick as
all we just like removed a ton of code
so these are the three demos we have uh
you'll be able to try them at the gaming
corner at at 3 p.m.
I think later today
now I want to talk a little bit about
like how we made this so um common
across the three projects is the need
for low latency without sacrificing on
boarding so we'll talk about how that
works so this is um a traditional block
building algorithm so transactions come
into the men poool they get ordered
right before the payload gets built by
the concess blocks after about 2 seconds
the way query works is the block
building algorithm does not span 2
seconds it operates on much smaller
micro batches and so you stream the
block as it's being created we're not
creating the blocks every 17
milliseconds that would be really silly
because it would overwhelm different
kind of infrastructure like block
explorers wallets Etc you would also
spend most of your time Computing Merk
Roots which is the very expensive action
when putting together a block so the
blocks get streamed to you as you play
um and you and because we don't actually
need things like the block hash in order
to reflect a state update in the game
you don't actually need to wait for the
full block to be built to to be able to
see what happened and this does not like
introduce any additional kind of like
security assumptions in a rollup the the
way rollups work with centralized this
does not add essentially like any
guarantees at all sorry any assumption
at all to the the whole system um so the
hot path of query which is users sending
a transaction adding into the bending
block and getting a stream update
happens in about 7 milliseconds so we're
able to do this by essentially
rebuilding the whole stack so we rebuilt
the load balancer we built a custom
block Builder on top of the ref model
architecture from The Ref team and we
also rebuild our indexer so everything
is very tightly up an actual block is
being built and then sent back to other
kinds of infrastructure whether they're
a block Explorer or or a um the other
interesting thing is most tooling outs
out there for like stuff like like er
c437 and on boarding actually creates a
lot of latency because it's just another
part of the hot path if you want to send
a 437 user operation and you have to go
through a bundler even if you have fast
block time you end up spending like 1 to
bundler and an pain Master inside query
itself so the 7 millisecond Loop Remains
the Same um even if you use these kind
of onboarding features so it's it's
pretty neat because you can have
something like move the fly where you
basically scan your face it's a bit
dystopian but you scan your face you
become a fly and you can move the fly
around and do all of that stuff by using
like everything you would expect if
you're a developer like I want to have
my users like log in with an email and I
want to be able to like sponsor their
gas and all that you can from a
networking perspective is we have built
um kind of like a a series of edge
regions on bare metal with servers all
around the world where we have copies of
the state that get synchronized with the
central sequencer and copies of wio or
block Builder So currently the thing
that's live is a single wire so per
chain so there's a single place in the
world where things get built um over
already started working on it but it's
not it's not ready yet where the state
of a mud world can be partition into
different geographical location such
that you can have different matches as
an example of Sky strive or of different
regions of biomes where the computer
doing the ordering can be in Asia North
America Etc because even if we have 7
millisecond latency you still have the
pay the cost of light sadly we have not
worked on that yet we'll probably do
that later um so yeah we we hope that
this both benefit existing mod games and
significantly expanded design space of
onine games and worlds it's basically
Plug and Play you just have to add five
lines of code to your system so I had
some biome shell but I will I will skip
it sorry guys um so that's it for me
today to learn more you can scan this QR
code or go to this link l
xquery all right we have three minutes
for questions apparently just stay here
oh man okay
right if you have a question you can
either scan this QR code or um if people
have a question also they can just raise
their hand then I can run and give the
mic yo uh if I'm doing local development
can I run quar like this whole system
locally or do I I have to do it on devet
at all all times yeah currently yes so
you can put envil in automine but
actually funny enough envil automine is
slower
than query so yes we don't have great de
local development environment yet but
we'll probably work on this next because
this is a distribut system it's kind of
a pain to run
yourself all right we have another
question here from somebody in the
audience what about Doom logic is it
being validated on mud great question so
out of the three demos you've seen um
the Doom demo only uses query for event
relaying so or the P2P protocol of Doom
works and we relay it through a single
mud table we actually attempted to
rebuild all of Doom in mud but there
were so many like weird problems
because John karmac is insane that we
kind of like gave up and that's where we
built M Shoot actually so M Sho runs
fully inside mud it's not just using mud
for event kind of like cordination but
for the Doom demo specifically we only
use it for sending events around mostly
As A Benchmark for latency next question
is what is
wsaw wiaw is a Blog Builder the reason
it's called wiaw is because we have um
our internal theme for names is uh blue
color workers so we have Quarry Warsaw
Redstone rolite so it's other Stone
stuff to cut stones with or things
related to Stones next question please
people in the audience really want to
know how your last name is pronounced my
last name is it's kind of funny because
it says is it pronounced glibert or
glibert it's pronounced gibert so you
were right sponsorship yeah so the way
it works is we have a p Master that's
part of query that that like gets
evaluated within the sequencer and so
this uh pay Master exposes rules you can
tap into as a game developer saying like
I don't like users can get their first
or under these certain conditions so you
kind of have like a whole system you can
tap into to have flexible
sponsoring all right I don't see any new
questions on here if you have another
question you can also raise your hand
real quick and I can hand you the
mic all the way back okay somebody else
running bottleneck currently I mean it
would always be the B neck is the size
of it blocks so query doesn't really add
like the the query doesn't really have
currently doesn't get bottleneck by
stuff like CPU on RAM if you use good
enough machines the issue becomes how B
big your blocks are so as an example if
you have transactions that have that
consumes a tiny amount of gas you can
actually put a lot of players if you
have actions that use a ton of gas you
end up being bottlenecked by block size
so it really depends on what you're
doing but I mean I'd say you can
probably have like depending on what do
you probably can probably get like 200
concurrent players per chain probably
like doing actions all at the same time
all the time in a hot Loop that's pretty
cool but for Doom specifically it's not
the case like Doom is just a beast of a
demo and I you can't get to 200
players all right another question that
we have is can we use non- evm networks
underneath
no uh because we have not built that
like this whole thing is deeply
integrated in the way ethereum works all
the way from the clients to sponsorship
to the block building Etc so no cool all
right somebody's asking will we be able
to use pods with Quarry absolutely so
pods uh which stands for provable object
data uh also known as frogs all of your
frogs are pods pods all frogs are not
pods but all pods are actually some pods
are frogs and some frogs are pods it's
not an exact mapping but yes you'll be
able to bring pods on chain and and and
settle them because pods can be verified
in the evm
all right and I don't see any more
questions here we have 30 seconds if
somebody wants to all right so I switch
back from being a speaker to being an MC
so uh next up we have Fric Fric is going
to show us how to build mod applications
with um all the new toolings that we
have so please welcome him on stage
no slides
yeah okay let me get my hello hello I'm
Frolic can you hear me good great I'm uh
one of the core developers of mud um
we're going to attempt to build an non
train on train game in 20 minutes it's
kind of a lot to ask uh we'll see if
it's a actually a game by then but um so
this is meant to demonstrate the uh
stuff we've been working on um didn't
quite have enough time to make this a
full-on template that you can use but uh
yeah we've got a a template project that
we'll we'll clone from and just to save
a bit of time I've already uh cloned it
into my um personal uh GitHub account
and also um cloned it here so let me um
adjust sizing here real
quick how does that
look looks great thank you um okay so
let's start this mud um project um this
mud project um so when you run the dev
script um actually let me qu out this
and run the local one um when you start
the dev script you get uh a frontend
server that's your client you get
contracts you can see it's currently um
evaluating all of our contracts and
deploying them to our local chain we
have our local chain and then the
Explorer which you may have seen uh
already um but we'll take a look at that
in a second um so in our browser we now
have uh a application um and if you've
uh played with mud before at all um you
might recognize this we we have a to-do
list app as kind of our default
application I don't know why you would
put a to-do list app on chain but it's a
good demonstration of of uh the kind of
full stack and and really easy to
understand um so in this uh demo we've
already got um our onboarding flow wired
up so I'll sign in here uh create
account with a pass
key and then right now behind the scenes
it it gave us a gas allowance and then
it's setting up a session account uh the
session account under the hood is
basically a local signer that signs all
of our transactions so we don't have to
confirm every time uh with a wallet pop
up um so we're approving the the session
account and now we're good to go so
we've started started our new project
can tick that box great
job uh and we will uh next open Explorer
um to kind of show you the the local
flow there um this is both um able to
run locally and um uh once we deploy we
we'll show it there as well but um you
can pop this open a new tab when you're
running locally but I've embedded it
here just so we can see it a bit easier
um so we can already see uh our task
table um we've already got the uh the
first task completed U marked this
completed and if I connect uh I can
actually edit start editing code so if I
want to uh change this back to zero I
can you can see it unticked and then if
I uh check this again we can see the the
Explorer update automatically
um and similarly if we want to interact
and call the complete task function um
we can do that here the first task oh
actually it's completed so let's reset
reset
task uh uh and it it um reset it and
then we can complete it just calling
these functions to the Explorer and it
completed it and then as we um check and
uncheck we also get a live view of all
of our transactions floating uh flowing
through our world um here which we can
then inspect um and and see all the uh
mud logs being emitted um including the
user operation so every one of these uh
transactions is a user operation 4337
user operation um so everything is
wrapped automatically for you sent to
wies saww confirmed uh very rapidly um
and yeah makes our our web uh web app
super
responsive um so let's try oh we did the
explore great um let's try to build uh
sorry
I'm not used to these full screen things
so just
second there we
go okay get this running locally again
get the code editor open
great okay so everything in a mud
project starts from your mud config this
is where you define um your tables and
uh your schemas your data model um we
use a very familiar approach uh like you
would with a database uh you have a list
of fields in your schema and then you
define basically a primary primary key
which can be one or more Fields uh so in
here we've already got a task table for
our to-do list app um next for our game
we're going to add a position table so
every player has a position on the map
and they can move around uh so we'll do
here
schema so the first thing we want is a
player um this will be one position per
player and then we'll have an next X and
Y
coordinate uh and then our our
typescript is telling us um everything
in mud is strongly typed um so
typescript is telling us we're missing a
key uh add that next and also we can see
auto complete kind of reminding us what
our fields are in case uh you've
forgotten um and behind the scenes as
I'm I'm typing this and saving uh mud is
actually rebuilding the project
um so if we look at our uh Dev contract
script again um it recognized that there
was a file change in the config uh it
reran the dev
Runner I think it actually already found
our position table up here let me see if
I can find
it oh yeah so um up here when we saved
first time we had the uh existing uh
task table um and then it recognized
that we need to register a new table so
it's uh ident I I don't know how to say
that word um and every time you um make
an update to your mud config it
automatically um figures out what it
needs to deploy whether it's a a table
or a system and and runs it for you and
then we can also see in the Explorer um
if we open that up uh we have our
position table already but there's no
data in here yet so um we'll do that
next um
okay not sure why oh because I restarted
the server so everything redeployed so
just a
second so we got the um Explorer going
with a new project out of the uh
position table um but we haven't been
able to do anything with the position
table yet so let's add a a system so we
can move our player um so we will um let
see see in our contracts add a move
system and I have some code
sorry uh I have some code here
copy
this
oh a sorry hang
on okay so I've I've copied over our our
Tas um system but this is going to be a
move system so so we're going to import
our position table um uh call this move
system and we'll paste in our code uh
sorry function move uh direction
direction and I'm realizing actually I
forgot to Define our our um Direction so
another thing in in mud is um being able
to specify
enums uh so I'm going to do that now uh
Direction uh
north east south
West great and so then we'll import
direction from Cen common and again
behind the scenes mud is already um
generating code for us strongly typed um
solidity code so we don't have to worry
about that uh this is a public function
okay so we have our our move system
hooked up um let's see in the Explorer
if we've got that in here now so we're
going to go inter
app move no
something's oh no demo
Gods uh so restarting one more time just
to see if this um helps
uh we've just redeployed to Anvil again
with a fresh state so take all these see
if the move systems in
here no what's going
on move system okay so I think it's in
here um we'll just uh keep going
um so after our move systems all wired
up um um we need to um render our
players and our um our game map so that
you can move around on the map so I'm
going to open up our app here um I'm
going to import our game map
component it's not going to do anything
yet so we're just we've got a blank um
map for now um but we'll start by
getting our
players uh we have a new State library
in mud called stash um with a bunch of
react hooks um this one particular uh is
called use record so it will give us a
list of Records these are automatically
synced for you uh from the chain so all
the data that we need is already um
available so we're going to use our
stash we're going to tell it we need a
table and for that that we can import
from the mud
config uh
from M
config just to save some time to um
remap this mug.
name spaces app do
app.
tables
okay and then tables.
position is what
we want so we have all of our
players and we're going to pass that
into oh we got to import this
too okay so these aren't doing anything
yet um actually let's see if we can open
up the Explorer and give something of
position oh I think because we don't
have our um move system available I
can't actually set the position very
easy yet easily yet um so we'll just
move on to the um the actual game
controls which will allow for keyboard
movement and tap movement um which
you'll be able to play play with on your
phone in just a second um so for that
I'm going to add uh import the world
contract um if you use VM it's
essentially a uh strongly typed uh world
or um contract object that represents
our World um so we will import um that
using this
hook which again will be available uh
from mud
soon and then on here we want on
move I
think and then I'm just going to check
the world contract because it it needs
to load um some data so it's not
available right away so we're just going
to uh throw if if it's not ready yet
ready and then we're going to get a
transaction back from this we're going
to
await World contract right.
apppp move
okay so we can see our move uh our move
system calls here so we're going to call
move um VM when you're calling a
contract takes in a list of arguments so
that we want um on move uh call back is
a work because this is expecting an enum
um fortunately that's available on our
config as well um actually we'll just
use it directly here so mud config enum
values.
direction.
Direction so again um all the strong
typing is is uh helping me here um it it
autoc completed uh this direction enum
that we added and I passed in um our
Direction string which then mapped it to
the the actual enum value um which we
want for our contracts uh and then we'll
just log move transaction is this so we
should be able to move around
yay we built a
game okay so so today um mud temp um so
another big Improvement aside from
onboarding is actually like getting
getting you on on chain and making it a
real app um so next step we'll uh deploy
so pray to demo Gods going to deploy to
Roo light which is where we have all the
new uh Tech
running can you show what this script
does deploy rot
light
yes uh let's see deploy rotor light it
grabs a bunch of stuff from our umv file
and right now that's that's pretty
basic uh it specifies a chain ID and RPC
URL uh and then um calls out to this m
file which we don't actually need um um
we had some more stuff running here but
um I'll just show you that's one thing
and all it's calling is is mud deploy
with an RPC URL um that's basically it
um internally on my system I also have a
um environment variable set for my
private key um that acts as my deployer
um we are also working on allowing you
to deploy with um user operations in the
same sort of onboarding flow or the same
rails so basically you will need uh you
won't need to um Bridge any funds or or
whatever you can just use the the the
daily gas allowance to to deploy
contracts um so we've got a deployment
here um we can now go look at the real
life world
Explorer uh let's see
explorer.
deev enter and oh
jeez enter in our contract address
explore the
world so we can said to Garn it oh yeah
thank
you yep there we go so we got our um
task list up and running and we also
have the position table and in here we
can should see our move function move
yep great and we can move north oh hang
on oh I I'm not going to connect here
but um we'll show you in the the the
live app Okay so we've got our Roto
light deploy um now we're going to
actually upload a front end here so
we're going to build build for Roto
light this basically just binds the
chain ID into the um client application
uh and then we'll just do a quick quick
drag and drop into uh netlify they have
like this drag and drop um static file
uploader um doesn't require any sign up
uh you can use it a couple of times for
free um I've actually already signed up
and set up a uh Workshop uh domain so
I'll drop it in
here uh let's see
open so I want the dist file going here
here and um in the meantime if you want
to open this up in your phones um
workshop.
mud.
deev it should show you
the same thing you can ex uh test out
this new onboarding flow um create a
pass key sign in uh get some free gas
and then uh start moving around on the
map um you can also check off items if
you want to check
items let's see our
deploy okay published great so we'll go
through that sign in process again since
we're on um a new domain it's asking for
the pass key
again setting up the session wallet or
the session
account and now we're in oh I see a
bunch of people already playing that's
great refresh real quick
great there we
go do you have time for questions is it
it's question time um Can a switch to
question screen so just like before um
scan the C code ask
questions um okay so while while while
better questions are being asked or not
better questions but at least votes are
being casted we'll start from the top
Fric are the tables
relational uh yes and no from the
onchain perspective we're still using um
Native solidity essentially mapping so
you can think about it more as a key
value store but the data is modeled in
such a way that allows us to then index
the data in a relational way so that you
can query the data um we have a query
API that um isn't demonstrated here but
the indexers that are running on our
chains is a hosted indexer that supports
a full SQL API um so you can run
relational queries as you'd expect there
and and get your data thanks to Ryan
from index
Supply um the next question here is what
is stash in Ed records so I I kind of
breeed through that a little too quickly
but um stash is our new uh client store
it if you're if you've used mud before
it's going to going to replace reccs and
Zoo um but it's a high performance um
client store that kind of fuses the
functionality of both so you get um all
the benefits of each under one one um
Library um okay so we we'll we'll skip
the trolling questions what is rotolite
frolic R that's a question for you
rotolite is our um our chain running uh
our devet chain uh running all this new
query infrastructure um available now
but just to caveat that it's likely to
be reset restarted go down as we play
with things and stress test yeah so so
while Redstone of course is a production
environment Garnet is our testet that is
also in a production environment and
Redstone sorry rotol light is a devnet
that is not not in a production
environment so it will break it'll be
restarted but that's where the the
bleeding edge of the stuff we're working
on can be found in um I don't think we
have any more questions left there's
there's more we need to to can we scroll
the questions cu the top question is
bugs and also you guys are not taking
off the questions we've answered so we
need to remove
them oh there is oh my God all right
first okay can you use mud as a library
and build a meta framework over it like
react and
next uh I'm not mud so we build a lot of
in addition to the the solidity side we
build a lot of JavaScript tooling um so
it kind of is already doing this it's
it's sort of a framework over the top of
of JavaScript and we um use internally
we use react a lot so we build a lot of
react tooling on top of it as well um
but you can use it on basically any
framework um and I'm sure you could
build a meta framework over top of it if
you wanted to as well I'd be curious to
know what your use case is so um yeah
does CCP Games Team build kind of a meta
framework on top of mod yeah that's true
like they're they um smart object
framework and yeah will we hear about
that later today we will here indeed
about this later today so please stick
around um so okay here's a new one what
are some of the primary reason for us to
switch to on onchain game development
Frolic I personally love uh building
onchain because I don't like running
backends so it means that I can write
some code put it on the internet and it
will run on the world computer forever
as long as people are willing to pay to
play Within the game so that's my reason
sure there's many more and registering
uh Securities yeah these are the two
reasons I'm joking
um okay I think we're done um thank you
foric thank you so next up we will have
uh druman and vany from biomes um
no no no we're going
now just take more time we don't wait
for minutes all right so next up we have
druman vany um please take your seat
back um so Dr and V are going to talk
about growing the GDP of biomes how they
built it uh what their theories on and
tees on Smart objects are lots of good
stuff coming please welcome uh sir
biomes to the
stage uh all right hello uh I'm drill I
work on biomes biomes you probably
played in the gaming Corner over there
or maybe you saw the demo earlier in the
morning um you can also uh you know just
go and biomes RW and actually play it so
today we're going to talk about growing
the biomes GDP which is the primary
thing we're trying to prove out with
biomes and and two things we want to use
to try and Achieve those goals before we
start we're going to take just like a
minute to think about why we're doing
this uh most people who view ethereum
they view it as an open Financial system
if you view it this way you care about a
particular set of things you care about
stable coins rwas treasuries wallets and
payments but this is kind of the weird
room this is that's why it's in a
classroom and uh it's it's a bit of a
different scene it's not interested in
moving our existing World on chain
rather it's interested in trying to
uncover a totally new and weird future
that's very different from the world
that exists today and if I was going to
sum up the core question that's being
asked in this
room okay half of the room but I will do
it if if Bitcoin was able to birth
digital coins that people treat like
real valuable coins can we basically
that people treat like a real valuable
planet and and I think the short answer
is that I think we can and I think it
actually might end up being much more
simple and obvious than we might have
thought thought before there might be a
line of sight to this um I think what we
should just do is we should take ideas
that already work and we should just
reshape them right we should reshape
them from being built for finance and
and and just and just make them work
with Virtual Worlds right so we we got
to take the idea of scarse digital coins
and and and convert that to digital
matter we got to take temper proof IUS
and turn that into temper proof physics
and we got to take smart contracts and
turn that into smart items and that's
basically what this talk will be about
and we're going to actually make this
concrete with examples of us trying to
do this within biomes and I hope that
makes it much more
legible um and the claim with those with
those three pieces the the claim is that
the digital matter and smart items can
birth a crazy new asset class the
weirdest asset class the world has seen
and that if it gets mind share will
unlock autonomous worlds it'll make them
super obvious super visceral and you
you'll never have to answer the question
of why you put this on
chain so to make things concrete let's
look at biomes uh on the surface biomes
is just Minecraft with everything on
chain you can you you probably tried it
out the items players physics all the
actions you can see it move and mine and
build it's all on chain you know right
now there's like a this like client
optimization thing going on to make this
work sometimes it'll be bugs but you
know I I think you got to pressure T dot
wherever you find him to make Cory go
main net faster and then and then and
then this will not happen um and what's
been happening with biomes ever since we
have sort of been in our Alpha phase the
last month is it's it's coming alive the
world is coming alive there's a lot of
more activity we're sort of seeing it
grow the transactions are up and to the
right you know the players up and to the
right GDP up and to the right everything
bullish there's uh people like Ben who
are spending 5 hours building something
Dei spending 8 hours plus days mining
stuff U you know so people are doing WTF
which is really funny considering this
like barely ever hits 15 current players
right um and and ditto can dto is a
Community member who who made this Grand
claim that biom FS like ethereum but
more playful and so what we're going to
do today is we're going to go down the
rabbit hole why are people so excited if
found on the surface it just looks like
onchain Minecraft why are we even doing
this right the first concept is digital
matter the thing the thing we brought up
in the beginning think of digital matter
as a playful vision of blockchain
created scarcity so while in Bitcoin you
have crops and wood and ore and land in
Bitcoin you have temper proof IUS in
biomes you have temper proof physics and
what this means is if there is a tree I
can't just like Snap My Fingers and mint
more trees arbitrarily the only way for
there to be more trees is if I farm it
according to the physics right so
there's always like wood is actually
valuable and if you do like the weird
thought experiment you might be like if
Bitcoin was an AWS It could only be
worth so much but Bitcoin with true
scarcity and temper proof rules could be
worth a trillion dollars and if you go a
bit crazy why can't the same happen with
with digital wood right you you have
like Ben who's maybe thinks one Sakura
wood will be wor
$31,000 so like this can happen this can
happen just you just need to believe
right um and just like having lots of
scars Bitcoin grants you power in
bitcoin's World controlling lots of the
scarse resources and land let you build
businesses and be effective in the
biomes world the second thing we're
going to is smart items so we looked at
digital matter now we're going to look
at smart items smart items present a
playful vision of smart contracts you
can think of them as items with
functionality in the physics that you
can program with a smart contract
they make it really easy for players to
build real economies for anything in the
world to visualize it think of a smart
contract as a chip and you can insert a
chip into an item like a chest to
program it so if I have my Unis swap
chip and I put it into a chest it turns
into Unis swap chest and at this point
if people mine ores around the world
they can put ores in the chest and get
you know swap it for some tokens
according to the amm prices or they can
give tokens to the chest and and get
ores according to amm set
prices and you can sort of take this
concept and basically apply it to all
the kinds of different objects in the
world you can imagine I have a door and
it turned it into a token gate right I
need the token to actually open it so
what you just did here is you gave the
Homer Simpson treatment to ethereum
where you if if you told Homer Simpson
what is a token gate that's what he
would think it is right and so now
you're like taking all of these smart
contract patter patterns and you're just
making them much more relatable for a
more like normal audience so you can
turn a door into token gate a force
field a cart a
bed and with all of these items you can
build a lot of cool stuff uh and these
are all real examples of things that are
already being built within biomes the
bizaar is the biomes version of Unis
swap it's like this like Shop with a lot
of liquidity where you can trade all
kinds of items for coins the funny thing
is as soon as we made the bazaar there's
like this other group that put up a a a
really crappy shop next to it um you
know relatively and it's like the sushi
swap of biomes right and it's trying to
vamper attack the bazaar and take all
the liquidity you also Temple where you
donate sakur wood to get this membership
nft they use all that wood to build the
largest sakura tree in the world and all
future Sakura meme events that happen
will probably gate access based on
whether you donated the sakura tree and
got the nft is to sleep and recharge
your player and load without worrying
about know getting grieved and in return
you just sort of have to pay rent The
Pyramid Arena and parkour challenge are
going to going to host a bunch of games
and these games will use Smart items to
have betting and prize pools and
everything so in a way you can basically
think of these as like deploying daps
inside of a virtual world
right and third if you have digital
matter and you have Smart items you have
a new asset class um and I think it'll
be the craziest asset class that crypto
has ever seen maybe the world has ever
seen and I think when that asset class
gets mind sure is is when you know um um
with a smart contract imagine I program
it such that when a player gets gold ore
from by the actual gold in the virtual
world and if I put the coin in it burns
the coin and lets me take out a gold or
and every time this happens the chest
takes a small fee and it uses that fee
to incentivize players to charge the
force field and and defense of the chest
to make sure it cannot be broken
in if this coin rises in price let's say
it's even worth like 10 million or
something it becomes extremely extremely
obvious why all the gold or need to be
provably scarse because if I just like
mint more gold or at a thin air I can
just put them in the chest and mint more
coins for myself so it's really obvious
you don't want you know you need the
gold or to be scars and you don't want
the devs to just randomly mint more it's
also really obvious why the physics
needs to be on chain because if I change
the physics such that it becomes super
easy to break the force field I can now
come in and steal all the gold doors
from within the chest and now that coin
that was backed by the gold do is no
longer backed by anything and it's just
going to plummet right so if you have
this AET class take off it's super super
obvious why the actual phys physics and
research of the world are
significant to do one more example we
can kind imagine how uh in the 2021 like
crazy Bow Cycle there was this idea of
nft land right so basically in the sand
forever land ownership of that land and
this was really good for a particular
type of user that you can have hyper
rational financial markets and
speculation on those nfts because if I
buy an a land nft I forever own that
land so I can you know speculate on it
and trade these nfts 8 months down the
line it' be totally okay you can't do
that in biomes right if you want to to
control land and biomes you need to
build defenses you need a military you
need force field the military can now
decide that okay US military are
protecting this land we're going to
tokenize this land and sell it to you
and if you hold this token you're
allowed to come and build within our
premises knowing that everything will be
secure let's say I buy this token I come
back in 4 months and that military is
just dead all the defenses are broken
now this token doesn't mean any anything
even if I hold this token I don't
actually have access to any land right
so now you have this like entire asset
class that is only worth anything as
long as players actually like maintain
their defenses and what you just did
right here is you made a fundamental
like switch you you made a switch from
the system carrying about who owns what
asset into the system only caring about
physics and assets can live on top of
them but the assets are not the first
class citizen um to make a concrete you
went from metaverse land and FS where he
owns something into field and when you
have a new asset class you birth an
economy with new properties this
requires new types of participation and
appeals to a new set of users um which
is really cool which is why even though
this like has voxi and stuff it's it's
not the sandbox right it's it's a very
different system um and this brings us
back to the original claim that we
started off with digital matter and
smart items can birth a crazy new asset
to visualize it one more time you think
let's just expand that statement unlike
bit konus worlds will have scarse
digital matter and temp physics inside
the players will use Smart items which
are tangible physical forms of smart
contracts to grow extremely large wild
we have taken ideas already work and we
have just kind of reapplied them we have
changed these ideas such that instead of
being built for finance they're now
built for these Virtual Worlds scarse
digital coins become scarse matter
temper prooof IUS becomes temper proof
physics
smart contracts become smart items I
think if you take anything away from
this talk I think it would just be this
um and okay now now zooming out only
because I have like a few more minutes
so I can just say some um we're
seeing how ethereum can eventually birth
worlds we don't inhabit physically but
we still treat as tremendously real and
valuable right so imagine biomes has
like uh $1 billion GDP right or or maybe
the autonomous world you build has a 10
million 1010 billion GDP um autonomous
agents start living inside inside then
you'll have a really funny thing so if
they live inside they're obviously going
to they're going to in biomes and I give
it a bunch of neptunium ore it can take
that and build weapons with it and use
those weapons so it's good it's clear
why it has value if I give it coins if I
give it the US dollar it can't like what
it can't buy a burger right what's it
for payment they don't believe in coins
in 2027 biomes is our only communication
challenge channel to ASI agents and when
we want Council we travel into biomes
and journey to their lands and homes and
bring the agents glowstone and in return
they give you you know some
cryptographically encrypted reman
hypothesis solution in a book so this is
how we solve the problems of of the
future right we just we just we just
appeal to the the agents in in biomes
and and they give us all their Solutions
and Skyler is really smart you need to
trust in Skyler right he he he built
this like he he runs this event thing
which means everything he says is
definitely true and and what he said is
that biomes is Unstoppable Minecraft
today but that doesn't mean you can take
it you know for fun you have to take it
very seriously because tomorrow he said
it'll be an Unstoppable lifelike
simulation that's going to have
unalterable digital physics run by AI
who believe there are sentence as we
believe we are which is crazy so take it
seriously stock up on all the Sakura you
can um go to bi.
aw you'll see all this
unfold it'll probably like go through
many cycles over the years but hopefully
something really crazy will come out of
it at some point um and thank
you all right question times um as
before scan the C code log in with Zupas
start asking your question so up vote
other questions if you want them to top
to come to the top of the screen uh
please do that so we don't have to
scroll because it was awkward last time
so we'll start with the first question
can smart items interact with the world
like Place remove blocks and Define in
and take stuff out of a door is an item
that you open or close to like enter
something so smart items are just like
regular items with functionality in the
world and all you do is by inserting a
smart contract into the item you can
hook into that functionality and further
augment it with your own economics right
so I turn a door that just opens and
closes into a door that is now token
gating before deciding if it wants to
open or
close thank you um what are the
considerations when designing or
deploying physic and New Primitives it
seems that playing God is high stakes
yeah I feel like something we've been
noticing is um as people start investing
their time into this stuff and they
start building stuff with the world
especially if they use Smart items so
now they're actually building an economy
in the world you can't anymore just
arbitrarily push physics updates if we
start like randomly one day minting a
lot more sakura trees it kind of screws
up what a lot of people are building um
so it does make it high stakes you need
like you need to really get some sort of
rough consensus within your community so
you don't piss people off we're trying
to build stuff inside um it is higher
Stakes yeah
um okay I I'll take the the digital
physics one so how can we design digital
physics to attract agents to live in our
games coins may be useful for them to
pay for compute and storage second part
is probably a statement not a question
yeah yeah um so okay ultimately I'm
going to say at the end of the day right
right now biomes is very much Minecraft
it's not we're not creating some
superpower AGI thing but okay how do we
Design This like this this world how do
we evolve biomes um to attract agents I
think basically if you get the GDP of
the world to be high enough like if if
if you reach a world where it's
neptunium or people value like people
value it at $100 because they can build
a weapon with it and be powerful in the
world agents might just want to live in
these worlds from a purely rational
region that's that gdps there and all
the activities
there
um oh okay I think there's one down
there which was can you play for free
and earn for free can you play for free
um at some point I'm sure you'll be able
to play for semif free when you have the
pass key on boarding stuff so you won't
need to worry too much about gas what
you can do in the world is yeah I can
come in okay imagine this imagine like
you have different parts of the world
that have different types of resources
that they're abundant abundant in if I
build a train system to move resources
from one part of the world to another
part all these Arbitrage opportunities
if I build this train system I just need
to play the game and like build a train
train right and then I protect the train
system with a force field to make sure
it can't be broken down by others and
they make this train system start
charging tickets to for people to
actually like take it I can start
selling these tickets people can buy
them and now I'm making money from the
the game but it's not play to earn in
the in the sense of I'm earning these
points it's kind of if you build a
business inside and and the world sort
of has a GDP then you can the normal
actions you take inside will be
economically
significant um I'm just going to log in
on my phone to see the questions myself
but for now I saw someone's question
which roughly goes like is it possible
for me to put a door down as a smart
item that Grieves someone by using a ton
of gas like in a wild Loop or something
like
that yeah I think right I think one of
the ch Alles with the smart item stuff
is going to
be what if you insert like a contract
into one of these smart items that is
just a bad actor and then if players
interact with it it's just doing some
crazy stuff this is possible but I think
this is also possible on the evm right
it's kind of the wild west and we're
going to probably let it up to clients
and communities to maybe white label
which type of smart item chips they
audit and verify and know to be
trustworthy and they'll only use those
items so I don't think you need to build
security against this at the protocol
level and and you can sort of deal with
it higher up uh another quick one is Are
biomes contracts going to be
audited well right now biomes is like uh
it's in a heavy Dev like update cycle
thing so there's like the physics that's
changing and getting updated at some
point you probably want it to get
audited especially if the GDP is going
to be high so I could see this happening
down the line another one is how do you
bridge biomes to solve real word
scientific problems
yeah so I
think I'm not totally sure you want to
do that I think like if you want to
solve real world problems with
simulation technology I think you can
just run run simulation technology on a
normal computer and simulate whatever
you want there and use that to like
solve your problems in the world I don't
think this will solve that for you I
think this is more about creating this
like digital simulation that for some
reason people take super seriously and
they just want all the wood
inside okay so maybe any IRL questions
I'm I'm running out of the list um if
someone wants to raise their hand we can
bring them a mic I'll give 10 seconds
for people to make their
mind all right next up with have Juan
Blanco um Juan blano is going to show us
how to use neum Unity Blazer and mud
together to build games quickly and uh
with high quality Juan Works uh with NCO
at cafos uh and yeah he's going to tell
us how they put together like a really
nice stack for building these
games hi hi I'm Juan Blanco
uh a bit about me I've been involved in
the blockchain since uh 20
and also the PS code solid
extension H I have also been 24 years
inet and more NT so mainly I'm pretty
old
um so neum ethereum the vision of
ethereum is just to provide tools and
Frameworks to sony.net developer can
create
applications and integrate with the
ethereum or
even so what can you do with the net
ecosystem and ethereum you can create
desktop applications you can create
Mobile iot gaming uh as we're going to
see here H web wasm as well as we can
see here line of business applications
like sap or uh and of course Cloud
integration and and you and using neon
and you can have common logic that can
work
across so what theum features so this is
the same as any core uh client
integration you have the The Ether node
us RPC smart Contra integration your rlp
EVMS siging aiod coding indexing L to
support Etc we have all the standards
and common protocols uh so you have like
cwe nois safe enss Etc Merles external
Wells if you don't want to create your
uh wallet with neum like metamask wallet
connect assur keyb Etc and tooling neum
playr so you can actually test how you
neum integrates Cod generators and many
templates like a sewe Blazer Unity Etc
so
and what mod brings to the plate uh mod
uh brings uh new data models and
Dynamics schemas something that was we
were really missing for create
applications in gaming and data indexing
something that we can actually rely on
and and mainly the operability and be
able to create new worlds and complex H
applications so in ethereum brings the
new packages so we have neum mode mode
uh so together you know now we can
create these great applications and
games that we can do
before
so how does this work you know so we've
been fooding this H with Cafe Cosmos so
so it has been fully tested there and it
works you know so it's it's pretty
pretty cool so what is Cafe Cafe Cosmos
so Cafe Cosmos is a a is a game for for
uh management
uh you manage resources you you cook H
ER you can do many things in here we can
see the Blazer version which is a
application uh as you can see you got
the tools you can H you can put H fences
there you are cooking Etc but obviously
this is a web H application so it looks
much better as a Unity site and so here
we can see exactly the same view but
actually in unity so yeah it looks much
much better than HTML version um so how
does it work underneath uh here is got a
small diagram we can see in the top H we
got the
Placer version the unity ver which in
itself it connects to the name space in
the net version which system service and
table Services locally and the logic and
all that integrated with obviously the
the H node we have the the mod smart
contracts and obviously custo systems
and lock processing and so on on the
right hand side H or left hand side you
can see the storl processor you know so
you have all the data stored to the
database and in the other side you can
see how we can create a net integration
test and obviously deploy it using do
net so let's see how this work if we
were adding some functionality to to
Cafe Cosmos so Cafe Cosmos H wouldn't it
be great yeah if you can have a crazy OV
there but
sadly uh I only have one simple open you
know but I don't have enough items to
actually create my craft my crazy oven
not not really really FC to having this
crazy oven so what if I could actually
buy it in instead of C in and and
created a catalog yeah so let's start
how will it look like so let's start
with the smart contract tracks so first
of all you know uh we'll create our in
our mode config our our table you know
so here we call a catalog item with a
item id catalog ID and a price you know
because we're going to buy it and then
we will go and cogenerate it if because
we are working working on Windows um
normally with
unity um you will have to use the kbass
or wl2 because it mod works better in an
unit environment so once we H
cogenerated our table we we can start
working with it so how as you can see
here we got the a new catalog system and
then we can access the data
there for the cut item then now we have
cut the price Etc and then it this
integrates where our other Library so we
can get the token balance that we have
so we can do the purchas it and
validated so now we got our system
created what we're going to do um so
ethereum now includes a a new code
generator so this code generator ER is
is part of the forign ethereum you would
have a simple code generator just to
create your normal services so now but
now has these mode extensions mode
extensions for table generations and mod
so once you created this you just go to
BS station right click and there you go
you can code generate it and then you've
got these files so so here here you have
the catalog item record your catalog
table um uh service your catalog system
service your catalog system service mode
extension
so let's have a look at this in detail
so first first of all let's look at the
table record a table record is a exactly
H the same as we have seen before you
know it just Maps you it's just the
representation of your catalog price
Etc now we have the table service the
table service is what allows you to qu
directly the data uh uh from the smart
contract so we can uh H get the records
set the records or even use the the
logs as you can see here we can set it
we can set the records for example that
will be our H crazy oven so we are going
to create a new item and it will have
the item id of one and then the catalog
uh ID of zero and give a price of five
um we can also later on after create it
we can create you know the get the table
record and also get the data directly
from the logs once we have a um overall
we could have a table repository the
table repository is where all that data
can be stored and in this scenarios you
can see in the screen we created an
memory table repository uh but obviously
you can have a postgress etc and that
way we can create all stract all the
data and store it locally or in memory
or in a database
and let's have a look how will this will
look in the in the database
so neum now also includes a ethereum
mode repositories EF package for for
anybody who familiar with not net the EF
is the Entity framework which mainly
provides a common provider for many
databases so you can H actually store
that they have uh store bites um and
once we start the processing this we get
all the data here and as you can see
this is all the data from the from the
world system um very similar to what mod
does and and you can see that everything
is encoded there and um yeah M just can
see the data but obviously because
everything is encoded we want to be able
to cre the data so in eum also includes
a new predicate Builder which will allow
us to qu the data in and
using simple queries like uh equal not
equal on or Etc so this will dynamically
create some queries that it will uh
create the
database um but obviously uh sometimes H
we went to the data in the database so
it's h it also includes a new normalizer
there which mainly will convert all the
data and tables in the
database um the previous versions uh it
also includes a race API just in case
obviously if you're working on webg you
will want to connect to that data H but
in here we just live on your own you
know so because you might want to create
different indexes this and and optimize
the database once you have extracted all
the data and
recreated so we that was the data so
what happens next you know let's look at
the systems obviously want to integrate
with the logic so first of of all we
have a we have our system service our
system service is the normal neum uh
cogenerated H service H so here we can
access the method purchase purchase
catalog item and but also there are
extensions for uh into a system service
for and here we we see the the ass is in
the top we have the the the catalog as
the as the system name and also ways to
do the deployment and in
inet um once we cut all the tables H and
the systems we can add it into our
custom name space we just create some
classes there and and then later on we
connect all this into our player service
who will integrate in your game and in
here we can see we has a simple method
which will do the purchas purchase item
from catalog and wait for receipt is
async and so mainly this will go into
your land name space and you go the
systems go to the catalog and do the
purchase and also afterwards it process
all the changes uh that will'll talk
about it in a second so now we got the
method we can connect it and create a
simple uh Blazer or HTML UI so we can
purchase our crazy oven and then put it
in our Unity obviously I have to build
the the unity
uh UI yet but the beauty of having two
different front ends is like I can test
it in the HTML version because building
something Unity takes a lot um so now we
go local so talking about local state so
we as we can see before we were H we
were talking about what happens after
safe and adual process of the changes so
um sometimes you know we have seen many
demos here like you you might went to
constantly send transactions for every
movement but in other ways you you come
to keep a local state with and and keep
it in memory and batch uh um uh or bulk
save all the data uh just the number of
transactions and then will save your gas
so maintain a local state what we do is
keep it an IM memory table repository
that's the one I was talking before but
in here what we do is when Once the user
starts uh the game we load all the data
in the current state and any actions
that we do we keep it in a separate uh
objects um also any actions that the
user will make we keep it into a
collection of actions that we that we
keep in memory so later on we can batch
those actions so first so and obviously
validate all the actions that we ER we
keep in memory using the logic in in net
so so what what happens if I craft
something or anything on the land so
mainly I craft something then the logic
uh I'm I'm doing I'm doing the
validation
internally and keep all the logic in.net
and later on I just H once I'm finished
and I have done all these actions I use
the Magnificent thing called system
multi-input and then and bat all these
operations into the into the node as a
one single
transaction um er once we all this save
H we want to synchronize the data and
and instead of like having something in
the background running as a processor we
can use the the the logs of the receips
so the L of the receipts will bring all
the changes that has happened on the
database sorry in the in the
blockchain uh and then what chains can
come from the chain so uh we can keep a
logic and donate but not everything so
we have like uh things like XP Point
changes level progress Etc so many the
core logic that where people normally
cheat in your game we can keep it h
we'll keep it obviously in in the
evm so uh apart from this uh obviously
we have deployment and testing so the
way that neion deploys if you wanted to
deploy with neion uh we we neon has also
the the M smart contract so this just
deployed as a use n World Factory ET
then deploy your your your tables and
then configure the the tables very
helpful because uh if you want to run
your integration testing against your
net code you will constantly uh run into
deployment configure you know configure
all the data it see ET and and then uh
and then just just run the testing nean
also includes some little uh tools to to
provide integration help integration for
testing and also extension for like
common uh development noes like hard
Bill and finally but not least you know
one of the coolest thing about uh mod is
got the delegate Authority so uh the
capability to have tempor
uh key private Keys Etc uh so you can
not having a link to your main uh
account we have all the money Etc uh so
this is also supported as well and this
is going to be the basis as well for
account instruction that we're going to
uh going to put in in ethereum uh later
on uh as as us as it's allowed me to
think about a better pattern to solve
how to put a kind of struction there and
wrapping up so we have seen how we have
H we can start with the blaz area a
Unity front end as well all integrated
with the player service um having our
res saers and table services within net
a local state all integrated with your
any ether node and doing the store close
processor to get all the data yeah ready
you all right um so same as before it's
kind of C Co to ask question to ju
because there are no questions yet I
will ask questions so um you kind of
rebuild the whole stack in net so what
did you find what was hard about it what
was surprisingly easy where were you
able to reuse a lot of your work I'm
kind of curious about about your journey
doing
that um
obviously the the the hard part was
encoding and decoding uh because you
have pack so much data so I modifi the
neion Avi to support the the the packing
and the the coding of the
pack data um just mainly using the fix
areas and but mainly I extended there
because actually fited very well you
know
because we have all the pack functions
isol provides you know so it look
actually fit very well as an extension
uh on top of that and eum mod is where
the specifics of the mod are put in
place just to do the extra decoding and
and and encoding so so that was the one
of the hard Parts um the overall um I
really really like this as you may know
because uh you know nine years um as an
example nine years ago when we talking
about uio I don't know if somebody
remembers uio and talk about the music
Etc one of the main things like hey how
we what what do we do with the data you
know how we can have some structur data
H that we can actually put the artist
and and so on the records Etc and we
have all these huge debates you know how
we we're going to we're going to do with
this uh fast forward 9 years later uh uh
now we can do it um because we're
scaling uh before I is like hey let's
put this in ipfs but where's the logic
you know so love it you fantastic you
know so now we can actually you know
just not just gaming you know the gam
the gaming are great because obviously
can provide some fantastic
logic and B application yeah so you've
heard it here first Han thinks mud can
be used for anything not just gaming
it's just the beginning um so we got one
question from the audience which is how
do you prevent it to the stale game of
the state to to the stale game state
that there's hundreds of players in the
world right uh obviously the example
that example is a for a single player
within your confined line so it's
obviously this is no Bas on a
multiplayer enironment uh so H for that
we have to think about it so
it will be you will have to think about
how to delimitate the that part of the
data and so if you don't really want to
constantly SN and then say like hey you
know this por is where you working yeah
and then and then and then that way
allows you to keep that
data without saving all the time
obviously the other solution is like
conly constantly sing Etc but you if you
got millions of users you always
eventually you're going to get some
scalability yeah yeah I mean here it's
because each player has a lock on their
land essentially so that's why they can
work offline okay makes sense uh we have
another question here which is are you
guys going to do this for godo or Unreal
Engine um everything that works in unity
Works in God do uh the so yeah bullish
for goto guys if you use goto you can
just use all of this yeah so this that
was that first slide so mainly every
this works it uh using normal task Etc
in in net so mainly anything that works
there it works in in any the parts of
net and hence the example with a blazer
because here you call wasam Blazer app
you know so that's not running in a web
page it's mainly like fully wasn't there
H so it will working thing is that go do
the latest version for they are yet not
supporting the the latest version of uh
net H but that's mainly go do and net is
us but but yeah and unreal H I found the
other day that there is a new extension
plugin for unreal with unreal sharp uh
if I remember the name because it's like
very very new and so yeah you should be
able to work with unreal as well who is
do you know if the the unreal.
net
integration is from epic games or is it
like a third party thing third party
third party the the epic games was
supporting another one but the
that one is stale but this one it seems
to be working but again it's only
working on desktop and that's because
obviously when you're starting hitting
thinking about aot and mobile Etc the
cas are very more complicated but
obviously desktop Mac and and and
windows and Linux is all right yeah um
be very heavy with with
textures um
obviously uh you will ask the unity
Unity specialist on that the unity
assets are something completely
different so obviously that's nothing to
do with the mod framewor in itself so if
you are something has very heavy the
unity has ways to deploy things like WL
that you can do it dynamically uh so
uh you can load dynamically the data um
in our our game nothing is done
dynamically yet because well our the
cafe Cosmos game probably the assets are
not very big it's going to be it yet
yeah yeah and I think for the person
asking the questions with mud you don't
need to store your assets in mud like
assets are just about viewing the state
only the the key State needs to be
stored in in mod I mean you can do it
but I I don't think it's a
good um okay I think that's it thanks
again right thank you
right um You can give the the
mic uh next up we have small
brain so small brain is about but it
will for sure be entertaining so please
welcome to the stage small
brain thank you I'm actually going to
take the mic on thing
so cool
CER this clicks oh that's fine
um I do have more than two minutes to
talk yes okay yeah
cool oh okay one note I forgot to make
is this is a a classroom so the audio is
very different from the main stage so
sound covered a lot from the back so
please be mindful of of your uh noise
level because it's really easy for
people to hear in the front thanks
hey
everyone Hey Okay cool so for this talk
I I've given a couple of talks I've done
Devcon and if you listen to my one on
Monday you heard some of the crazy weird
you heard about end to-end internet
games and a couple of new technologies
that I think could enable a bunch of
insane new uh uh consumer crypto apps if
I just went through a couple of kind of
hard SL interesting technical challenges
I faced uh building random stuff over
the past like year and
better people can hear me well yeah yeah
I figured I'd go through a couple of
technical challenges I faced building
stuff over the past year um and talk
through some problems and what they were
and and what I did to fix them and so
with
that the talk is
what three things from building stuff by
small brain and so what we're going to
do because this is a classroom is we're
going to play a game and the game is
called are you smarter than small brain
and how it's going to work is I'm going
to propose to you one problem that I ran
into and and just like for some poetry
it it's really fun that these problems
exist because the things I build are
really simple right like it's not like
you're trying to cure cancer and you
have a hard math problem it's like
you're trying to get people to yell at
each other over the internet and you
have a math hard math problem um uh and
there some some of there going be math
problems some of there going to be like
solidity questions and we have very
smart people in this room like Dr J and
Mr indexer and Paco and David and Frolic
and you know our German friend in the
back and so maybe this is going to be
really lame and you guys are going to
get the answers really quickly but
hopefully what's going to happen is
you're going to struggle a little bit
then get the answer and then it'll be
interesting but please participate okay
question number one we're going to start
easy and we're going to go to harder so
question number one is you is what I
want to do is I want to put some money
on ethereum in a smart contract and then
I want to have a password that I give to
somebody and I want anybody with this
password to be able to unlock the funds
it's like a really really simple like
like escrow smart contract I put some
money in a smart contract I have a
password and then I give this password
to somebody and they can unlock the
funds how do you do it and while I give
you a little bit of time to think um
this was useful okay amazing well this
was useful for for an app I built called
yon um which was an app where you can
send people voice memos with a little
bit of payment attached and if they
don't listen to your voice memo in time
face ID no headphones um they won't get
the money and the longer they wait the
less they get um and and and it was used
in this app to do invite links so if we
have this primitive we can actually send
people who don't have wallets yet an
invite link with a yon in it but anyways
getting back to the question yeah does
anyone of you want to jump in you want
to use your mic yeah what do you think
yeah so mine is kind of a Brute Force
but what you do is you hash to SEC a
simp zkp that you know the pre-image of
the hash but it's kind of Brute Force I
don't know if it's the best way to do it
no no I I think that totally works and I
think this is actually a valid solution
the solution makes sense to people in
the room and and adjustin can you
explain why it needs to be a zkp yeah so
okay so do you guys know what a hashes
like you take some some value you can
turn into a hash but you can't go from
the hash and turn it back into the value
so if you put the hash of the password
on the blockchain you commit to the
password but people cannot recover the
password from the hash and now your
problem is can someone show that they
know the thing behind the hash without
revealing to everybody else so if you
were to just put the password in a
transaction and be like look look
blockchain if you hash my password you
can get you you you'll get the hash the
issue is people can front run you and
like see it in the menol and front run
you so what you do instead you make a
zero knowledge proof that that you know
the preimage of the hash yes so that's
exactly right and I think what's
interesting here is this is the solution
I also initially came up with and then I
was sitting in my room like 4 days
before eth Denver like you know trying
to write circom and being very sad and
like I I felt in my heart that there had
to be a better solution and there
actually was Ryan do you have a
different was your solution different it
was that one okay yes uh here I'll run
over to you with the
mic you make a new hash from the uh the
address of the sender with the the
password okay oh no no never mind that's
not going to
work never mind well well I I I think
there's something interesting there all
right are we ready for the answer to be
revealed or anybody have
it okay cool um this is how it works I'm
so excited about this one because all
right so the first thing you do is you
generate a new key pair and we are going
to call so like a private key and a
public key pretty much a new wallet and
we're going to call this key pair an
ephemeral wallet okay because like we're
just going to use it to make this happen
and we're going to throw it away pretty
quickly afterward all right so the big
insight and some of you might be seeing
the whole punchline now is oh oh oh is
that the the private key from this key
pair is going to be the password that we
give to people um and so what you do is
you Escrow in the smart contract the
money you want to put in and the public
key associated with that ephemeral
wallet then what you do is you take the
private key which is the password and
you give the password to somebody else
you give the private key to somebody
else when they want to unlock the
payment what they do is they take their
own address their own actual address and
sign it with the the the private and
public key pair from the ephemeral
wallet and then they can use that
signature to claim the funds on chain
because the smart contract on chain just
does a signature check to see that okay
cool the person with the password said
that this wallet should have the money
so we should give them the money and
this prevents like front run and all of
the problems that the zkp was solving
because you are signing exactly which
address should get the money to yeah so
so the signature is a zkp like a
signature is a zero proof it's not a z
snark so we went too far on the on the
on on on the heaviness of the solution
that's actually a better way to think
about it it's exactly the same solution
but a much smaller proof that shows
exactly what you need to versus like you
know writing something in circom um this
solution is not credited to me actually
it was deep in the doo code because Dao
uses exactly the same thing for invite
links so you know big shout out to DC
and Nan for doing like extremely elegant
piece of cryptography um to do invite
links onchain so this is a little trick
for fully onchain invite link okay cool
little breath um let's move on to
question number two which I end up
looking at it is a little bit of a
mouthful but let me take you through the
question and then you can like throw out
what what you think will be a good
answer to me okay this is the problem
and you need to do this again on a
blockchain and the round and during the
round people are posting vectors to the
chain vectors like like a long sequence
of numbers so a bunch of players are
posting vectors to a blockchain during a
round and then at some time it's the end
of the round at the end of the round an
oracle comes and puts another Vector on
chain and this is the truth vector and
let's say like the players are like me
Justin Ellena Frolic Ryan Etc what we
want at the end is we want the sum of
the distance between the Oracle and
Justin vectors and the Oracle and Len is
vectors and the Oracle how you can
efficiently calculate this all right I
need to give you a second to think while
I give you context that's the pattern so
don't jump in just yet um oh and the
formula we're using for distance between
vectors actually we can use anything
reasonable we can literally just use
ukian distance um but but another valid
formula which is a nice little hint for
this question is cosine distance which
is uh the dotproduct of the two vectors
over the mag magnitude of the two
vectors all right sweet anyways the
context for this is uh this app called
tomorrow.
news which is a prediction
market for tomorrow's New York Times
headline um that's tm.
news that pays
people out how close and meaning they
are to the truth and we use sentence
embeddings to do this so sentence
embeddings are a way to turn a sentence
into a vector and when two vectors are
close to each other when two sentences
are close to each other in meaning the
vectors are close to each other in
distance so we can actually use this to
build a prediction Market Market that's
semantic anyways back to the problem um
how do you do how do you do do this
nicely on chain what were you going to
say oh I mean I don't have a full answer
but but one thing I'm wondering if it's
useful is
to uh consider the truth Vector to be
zero okay so and then we shift
everything by the truth ve I mean okay
so as reshift everything then stuff much
simpler at least conceptually uh so this
is what I thought too but but it
actually doesn't because the truth truth
Vector could end up anywhere and
distance from zero is the vector itself
so it kind of keeps everything exactly
the same in your
example any other
thoughts all right should I ruin
it give us a hint um the the hint is you
have to stare well so do we understand
like the coree problem with this like I
guess a question somebody should ask is
like why don't we just sum the distances
at the end yeah are you assuming that
you don't want to have an O of n exactly
because we're on a block I kind of
expected somebody to say it and then I
would be like no but why we can't just
sum the distances at the end is because
there might be end players and then we
need to do like you know on the order of
end computations it might brick the game
unless there's batching um so you want a
constant time solution we want a
constant time solution to this
problem all right I'll give it to you um
can it be an incremental what does that
mean well every time someone adds a
vector they do an incremental amount of
competition okay so it would it would
still be o of n it's just you don't pay
it in one go at the end exactly great
but you don't have the you always do it
with respect to the previous Vector um I
will give you a hint that you just
increment one big value as you go
on
yes oh amazing thank you oh thanks uh I
wonder if this expression can be
factorized yeah how would you factor it
uh I see there there is the dot product
I'm I'm not sure about if the dot
product can be factorized but I think
that you can keep the ones on the side
sum the F the the factor and then do the
operation on the sum that's it that's
exactly it oh my God I'm so happy the
computer is gone yeah yeah it's coming
back um okay cool that's exactly it
what's your name B BOS great job um
that's literally what you do so here are
all your uh you know these things you
need to sum these are everybody's
guesses like this is somebody's guest
this is somebody's guess this is
somebody's guess if you stare at this
long enough you're like be over
magnitude of B is is the the truth
Vector over the magnitude of the truth
vector and that's like a common factor
in all of these terms so you can pull
that baby out and also all the ones you
can just like you know pull out to the
side of the sum and then this thing
starts looking
like sorry I didn't math script but it
starts looking like you know n which is
all the ones that you pulled out uh
minus the the common factor times like
the sum of other stuff and so all you do
is you keep track of the sum of other
stuff as people are making their votes
and you do a nice little multiplication
at the end and you're you're all very
happy the problem with this really is
that like what we ended up needing to do
is we ended up needing to square
everything or actually raise anything to
a power we wanted to decide because the
distances weren't like crazy enough and
so the market was like kind of boring
and like fundamentally now like this
kind of sucks because you can expand
this out actually can use ukian distance
here and then because there's a squared
and a square root it like you know ends
up being kind of nice you still can't do
it um because high level what you did is
you like added non nonlinearities to a
thing which we were like was really nice
that it happened to be linear um and so
to do this there's two things that we
aligned on one was you could do a zkp
using something like sp1 right to like
succinctly verify the sum on chain later
and comput it offchain um but it turns
out that like the cost of doing that on
their approver network is actually more
than the cost of literally just looping
on chain and doing the sum because the
vectors were of such high dimension and
so we actually did end up doing the
stupidest thing which was looping on
chain great all right um okay third
question um third question is a really
open-ended question and there's not like
a clear uh correct answer to this one um
but what it is is I guess first is like
are are people here familiar with words
three all right like maybe maybe like a
fourth of you so I'll go over just the
part of the game you need to know to to
motivate this question uh words 3 is a
game where you're playing Scrabble on
chain on like an infinite grid and you
have to buy in letters to play and the
price of buying letters changes with
some formula that formula used to be a
VR GDA
um that's how that's how the game one
iteration of the game looked it's a
bunch of people playing and then letters
are in different price curves um the the
letters the pricing curve of letters
used to be a VR GDA with Target rates
per letter set based on the Rarity of
the letter um what that mean what a VR
GDA tries to do like kind of reductively
is sell a certain amount things at a
certain rate so might be trying to sell
one letter per day at a certain price
and if if letters are going faster than
that rate it rises the price Rises
exponentially if letters are going
slower than that rate the price Falls
logistically and so you know you kind of
like push use prices to push the rate at
which your items are sold to the rate
you want the issue with VR gdas was it
broke it had two pretty bad properties
um both related to memory one thing is
like it doesn't sustain a lot of players
playing at once because prices Sky
really fast and they never come back
down and it kind of pushes people out
from playing you know because you're
going way too fast from the target rate
that price is rising exponentially now
there are a bunch of people who want to
play and they can't the second bad thing
is if nobody plays for a really long
time prices stay depressed for a really
long time because you're like so far off
from the target rate that like you're if
if if nobody plays for a week and then
people start playing you're so far off
from the target rate and you should have
sold so much stuff in that time um that
you know the price is always going to
end up being zero and so what we want is
we want some sort of new pricing
function where that allows players to
like enter at any time and also like if
the game is no activity for a long time
doesn't brick it still maintains that
it's into play um and so that the open
question is like what is a better way to
price these
letters
yes reset my formula yeah yeah I think
that's a very just kind of works oh my
god did I knock the water over um you
could reset a kind of inelegant window
yeah so how I think this is what he was
suggesting
okay okay okay so you limit the memory
of the thing to just the past day yeah
yeah and you roll it so there's no
discontinuity you just roll yeah I I I
think that would
work I actually quite like that get an
investment from Paradigm and then they
can think about a new yeah exactly write
a new blog post yeah yeah yeah totally
any other thoughts
this one this one there's lots of valid
answers too well yeah what is
it what if um so basically buying other
letters affect all the other letters so
like you know if there was a lot of A's
they keep growing in price but as soon
as somebody bought a single b a single c
a single D you just see that the part of
the ace among of the all the letters in
the game diminishes and so the price
goes down so then you might not even
need a rolling window you just uh like a
match every letter against the to total
number of all the other letters yeah I I
think that's another good idea and I
think like specifically what's going on
in that idea and I might have
misunderstood you but specifically the
underlying thing that's going on in that
idea that fixes our problem is like you
shifted your notion of time from actual
time to like players buying things like
one tick is not like one second it is
like one buy and so if there's a bunch
of inactivity the game actually doesn't
even feel it it's just like it's started
off when the next player buys something
wait but isn't it circularly defined
because if you say I want to sell four
letters per unit of time if your unit of
time is amount of letters sold well it
wouldn't work with the VR GDA okay I see
I see see okay yeah yeah I I agree it
wouldn't work and in that case like it's
just always going to be on the line yeah
it's just linear right yeah um okay I I
have a minute left so I'll I'll give you
what I ended up doing I don't think this
one's the answer I think it's a answer
what I ended up doing is like drawing
this little curve in Desmos and how this
curve works I'll go point at the screen
at this side this time how this little
curve works is like this is time this is
the price and whatever you buy it just
like jumps a fixed amount of X on this
curve does that make sense and so why
this is really really is like and up
here right like around $300 this line is
straight up and so if like somebody buys
at $300 the price is going to like sky
like crazy and then Fall Down super fast
and then like around here like the price
is kind of never going to get lower than
some amount of T than like what whatever
this is I think like around $10 like
kind of no matter interesting gamep play
in this area um if if the price starts
getting pushed up like crazy because a
ton of people are playing it like Falls
really fast so that people can enter
again and if the game's inactive for a
really long time it still stays
somewhere down here and like can jump up
the curve pretty fast do you bound it so
it doesn't go too far on the right you
to catch up by you still have the
problem of VR GDA which is if the price
has gone too low you have to catch up by
buying a ton uh sorry it it didn't move
forward by a fixed amount it moved
forward by a percentage of how far back
it had been okay it makes sense yeah uh
and it move it moves forward that's
linear and the curve is exponential and
so you you get your difference um yeah
catch right but that's how this works
and that's what ended up being deployed
one really bad thing well I don't think
it's bad but like one criticism of this
curve was that like you can't really get
letters above like $500 or $600 cuz like
you literally you can't buy that fast
and so it kind of puts like an upper
bound on the price of like how high
things can go um again which I thought
was reasonable but but some people did
not react well to
anyways that's the talk I hope you
learned something this is me and the
best way to contact
me all right question time so small
brain asked questions to you now you can
ask questions to small brain you can
have your revenge there's one question
which big brain amazing thank you great
thanks for your contribution um okay so
you can either pose the question by
scanning The Cure code or you can raise
your hand we'll bring you a mic I it
works
yeah I'd say like the other two it's
like really not
important better oh oh the question was
how important is it for players to ask
these formulas to formulas um
specifically the last one uh but so I
think like the first two it's it's
actually like really not important for
players to like you jump in and you buy
and you see the prices going up and you
like they kind of feel the curve um but
I think like if you want if you're like
a words three power player which there
definitely were you know you you go in
and you understand how the curve and the
math behind the curve works and that
one's like and if I think like if you
have a strong understanding of how the
curve works it does give you an
advantage in the game in the last case
yeah that's another thing too is there's
lots of complicated constructions that
are better like you also want your
construction to be like as simple as
possible for this reason and so you know
trade-offs yeah
um we have two questions that have to do
with past projects yeah so one is what
is the next plan for Network State and
then the other one is what's happening
with wor words three in terms of users
currently yeah both are good questions I
think words three in terms of users
currently is I think they're like two
like it's not much uh and like words
three tends tend have like a bunch of
activity the first couple of weeks and
then kind of petered out I think like it
will come back like there's like clear
things to fix um I think like one thing
I'm focusing on the next time it has to
come back like you know there's like I
feel like there's a thousand people in
crypto who are like excited about the
things I make and play them actively it
has to be really clear to me how like a
larger audience past those people like
can get excited and be pulled into it
and I think like until I figured those
problems out there's there's not not
going to be a big push to main net and
people have like spent on it and and
played the thing so you know it's it's
implemented all the way um one question
that has received Co few vote is what's
your next project uh the next project is
a talking duck which you like will grow
up over a month and you can like Pat it
on the head to influence its personality
that's what it is and there's actually a
question related to that which is when
can I buy a talking duck uh right now if
you want to you can find me and like
venmo me 30 bucks what about people that
don't have venmo uh you can dieo me 30
bucks great
um why are you called small brain it's a
good question I mean I think it started
off as uh one it was funny David came on
and one I wanted people to like not take
it too seriously right and also like it
was a little bit of like the first time
I deployed something it was unaudited I
like tend to take security a lot more
seriously now but I was like this was
like my last this was like my audit it
was like all right it was deployed by
like a small brain pfp like you can't
get that mad at me if there's a bug in
the contract address what's my Dio
address um I don't know if the I think
it's like SBG I'll F just literally find
me after and I'll
confirm
um okay so no more questions digitally
anyone has a question in the audience
raise your hand and we'll bring you a
mic nope all right thanks another round
of applause thank you
all right so what's next now um we're
about to take an hourong break uh it's
not really a break it's only a break if
you decide to make it a break if you
don't want to take a break alvaris is
going to organize a doom tournament on
chain um I don't know if they have
prizes but I just claim they have prizes
and they'll have to figure it out if
they don't have prizes so if you want to
stick around and play a doom tournament
uh head towards the gaming Corner we
have about an hour for this we also have
a play test of brief candles latest game
um and we'll come back here at 400 p.m.
sharp for a workshop from the e Frontier
team about how e Frontier is built
technically that's going to be super
great so please be back on time until
then feel free to like stretch your leg
go get a drink and play Doom thanks
again
he
in I
n
all up
l
he he
talk it's going to be about
financialization in games
some some technical stuff going
on wait a minute stay Ceda don't
leave I'm kidding if you have to like go
to the washroom or something you're
totally allowed you can leave
hello all right uh okay now I know
everyone is listening Applause uh let me
test my slides real quick I haven't used
this before okay nice cool um so we're
talk going to talk about
financialization in games you might like
this talk you might hate me I don't know
so we'll see um quick intro I am y77 or
uh my real name is yua also known as y77
on the internet I am the founder of
project Mirage we
are um an island management game um you
might have seen our demo this morning
about it um but basically Mirage players
build out their Islands by um buying and
trading properties um they can also
invest in Island shares to boost endless
productivity and get dividends of
trading fees and Resources by um doing
so so you can think of it as uh a
speculative Sim City or Animal Crossing
on chain um it's currently live on
Redstone garet testnet and uh built with
mut too um so Mirage with the shares
mechanics that makes it a uh like Town
simulation with financial incentives um
when I design Mirage my thesis was that
a fun crypto game should combine two
components uh it should combine a fun
game mechanic and a fun money mechanic
so um basically we want players to enjoy
playing a game with money um and Mirage
is like kind of the first exploration of
um or first exploration of this thesis
and we're just going to share our
lessons and learnings about it
today so the game mechanic part of
Mirage is very simple um it's very
similar to any other city builders that
you've experienced where you produce
things and you earn money and you expand
your City to like a bigger fancier City
so that is simple and very common in
like web2 City Builder and then the
money part of Mirage um I looked into
like mainly three like money strategies
that you can add into the your games
basically uh speculation price Po and
Ponzi and uh Mirage ended up adopting
the first two speculation and price pool
um for Ponzi uh I'm sure you all know
that it's like unsustainable by Design
um and I'm also not trying to build a
scam here specu and price po uh our
lessons and learnings around that and
later going to kind of the general
takeaway uh from us building a
financialized
game so uh for speculation when it comes
to a city Builder there are many ways
that you can add speculation on top of
it um and you can have an in game token
where players can Farm by build out
their Islands there are many ways that
you can approach it um basically uh as a
game design need to think about um what
do you want players to find valuable
within the game and then for Mirage um
we want players to bet on others uh
effort basically um so we want players
to spend and bet on the island
productivity so on the right side we see
a screenshot of um kind of the share
trading screen where uh the more
shareholders you get of that Island the
more like benefit and it unlocks um so
you get better production speed you know
within the same amount of a time you get
to uh produce things more effec and then
uh into a higher tier you also get to
like distribute more things to your
shareholders and and later like trading
fees um so you can think of it um so one
good thing about this design isolate to
enjoy the game so we're able to you know
acquire a shareholders of your Island um
you will unlock a pre but our
speculation you know not good thing or
not so good side of things about it is
that um Island progress or like players
so like at least in the Casual game
context is not a very exciting thing to
be spec speculating on um when it comes
to speculation uh things need to be very
easy and stupid I think the best example
of it will be like mcoins I'm sure um a
lot of you know um so uh a sing Single
like very cute stupid jpeg are able to
um gather a group of supporters you know
who have the same taste and hence a c
like values on that token um so it needs
to be like very simple and emotional
triggering um in a context of the game
you kind of need to think about like
what in my game is very simple to
understand and also emotional triggering
that players will feel excited to bet on
and will feel like they have an edge to
maybe like for like 100x or something
they don't have to actually gain the
money but they you feel that excitement
of you know potential returns even
though it's like emotional returns or or
um Financial returns um so yeah um
that's that's like kind of nerling on
the speculation side and next is price B
so um Mirage is a casual game um we
don't really have a buil-in price B for
the game mechanics but we do use Price p
to run our play test um so on the right
side we see a screenshot of like one
our players uh who's like the winner of
the uh one of places we host that has a
prize pull for the top like wealthiest
Island basically um so usually we ship
uh a release like a new update of Mirage
every three weeks and then we usually
gather enough player data uh after a
week or so like after like players make
a lot progress on their islands and like
trior feature um but have you know make
meaningful decision within two to three
days um you know by making making a
casual game competitive it actually
speed out our play test process and
because it's competitive um players will
try everything they could to break the
game and try to win uh so basically the
competitiveness allow us to find a lot
of vulnerabilities use in our game
design um so I would like recommend even
though maybe your game doesn't really
have a price Po build-in in terms of
mechanics you could still try it um to
test out maybe like a new feature that
you want to
test um
and then yeah that actually wraps up
like two very simple money mechanic that
Mirage has and next next I want to dive
into kind of our general takeaways um of
like building the financial Li game like
this and I'm going to go through them
who is the audience um I find that a
common approach of building a crypto
game or onchain game would be you know
what if we build like XXX inserting like
a web te mechanic or title here um and
then on chain or like with crypto um to
make it fun right that is that has been
the approach of Mirage you know with
like City builder plus uh crypto stuff
and being on chain um which I would say
it's a good idea in theory because you
are using something that like players
are very likely to like are familiar
with um in web 2 and then like by making
it posible or by adding incentives using
crypto to make it more fun um but what
what we learned is that just simply
following this formula does not make a
fun game and does not um you know serve
or does not like make player happy
without identifying and knowing what
Target customer or that what target
audience that you serving um so Mirage
didn't do a really good job at this um
but being a casual game on chain it
didn't really serve the casual gamers
because casual gamers enjoy a casual uh
relaxing experience and being on chain
um creates a lot of hurdle for them to
enjoy that and they actually make things
more complex and they also fail to serve
I would say strategic sophisticated
players uh that play onchain games that
you know are capable of extending the
game because um casual like lore or
setting is not something that's very
exciting to extend about um so we didn't
really do a good job at this um and then
what we also learned is that if you're
building a crypto game within the
current market like today um you're very
likely to get started with crypto play
players you know your initial players
will be the ones that use crypto and
familiar with it and then what we learn
about crypto players that or most of
them that is they only want two things
from a crypto game or there are like
only two reasons that will they will
play a crypto game the first is making
money and the second is feel connected
and then how they feel connected is also
usually achieved by the first one which
is making money with the same same group
of people or lose money with the same
group of people to make it like a
community um so you kind of so realize
that like as a crypto game you kind of
need to figure out so what do building
things on chain and adding crypto to my
game inals and then at the end of the
day like what target audience am I
serving um so that's the first question
second one is uh what is the game goal
um one of the biggest design mistake
that we made at Mirage is that uh it's
lack of a very clear goal of the game it
starts with a very clear goal at the
beginning when we're like start Play
testing um which is uh you know like um
players need to maximize their building
production very like you know simple
logic like that um but after we play
tested a few times we find players turn
after a week um and then our thoughts
around it is that you know player just
feel bored after a week um it's probably
because we just didn't have enough
content within the game so we just go
ahead and then add a bunch of content
besides the city building part so we add
added uh gachas um which pull characters
which you know characters can help
building your city and then we also
added Explorations which you can go to
like different unknown islands with
different terrains with r RAR resources
we also add many things you know uh on
top of the existing mechanics but what
we learned is that that didn't help like
players still turn after a week um only
after we did the price po um play test
did we realize that um you after seeing
like players compete um for a certain
goal we know that um the game is not fun
or or boring to players it's not because
of lack of content it's because of a
lack of a clear goal um so if you're
also facing like a retention problem of
your game I think instead of um serving
more content you should go and grind for
your like core game Loop and make it
more fun and addictive for players um
lastly what is enjoyable um so if you're
building a game in crypto you kind kind
of is fighting a war of attention where
every day there's new shiny narratives
and content that's served to to the
players Like There's No Lack of exciting
things in crypto um and crypto games so
um as a g as game devs we have to ask
ourselves like what is enjoyable you
know so enjoyable maybe to a small group
of players because that's enough um so
enjoyable that we are able to capture
tensions you know compare with all the
other shining things in the space um you
know like we see a lot of play to
airdrop uh play to air drop games in the
space um and and you know we all know
that's like unsustainable and the game
is not really fun um if you check out
it's like very simple with with very
simple mechanics with like very shitty
like Graphics but players still enjoy
like play them because um what's fun is
not play to earn like the content that
they serve itself but the experience
that play to earn serves with where um
players get to hop from one game to
another to farm and that is the exciting
part so that is the fun content that
play to earn games to provide and so
with that you need to think about like
do I provide a fun experience that's as
exciting as that or you know more
exciting for the Target I'm I'm I'm like
trying to serve
um so last note uh I'm not trying to
convince you to build like a play to air
drop because you you get like players
there so please don't take that as a
takeaway
um I'm trying to say that
um oh God I forgot what to say okay uh
I'm trying to say that so um what makes
like a crypto game fun for a lot of
players today um is being able to play
with money very easily with a financial
well um that's like a superpower of
building this space and it's an
experience that you cannot get elsewhere
so I think like if you think long term
that we are going to use crypto or
blockchain as a you know global payment
rail or application rail um I think this
is a very bullish sign that at least we
can do like one thing well of course we
can do like more than that um so yeah I
hope you learn what we learned today um
yeah the more we learn about
financialization the better the closer
we get to build games that um achieve
all we want you know um sustainable open
and fun yep that's
it okay we need some question questions
in here we got to we need to pull them
in okay I know this entire talk was
about how we need to move Beyond
airdrops but air drops for Q&amp;A um you
all get an airdrop if you
Q&amp;A no um okay I think I'll ask some
questions and that I I'm kind of okay
never mind uh what is missing for Mirage
before main net
launch uh good question I think we need
to figure out if f addictive Loop for
attention before mainnet
launch so mainnet soon TM um okay the
second question very good question it's
all about yield because everyone cares
about yield does your game redeposit
funds into defi protocols in order to
and we're kind of still exploring it um
because we don't really want like yield
farming to be the only source of fun we
want it to um players to kind of enjoy
in the grinding process of building up
City and then um again like speculation
only in both like premium uh experience
um so I would say maybe but I would I
wouldn't say it's like a core game Loop
that we want to add so the next question
I think is really funny because that's
what the entire talk was about but is
financialization required for onchain
games um I would say it really depends
on what you are trying to achieve um I
think onch game enables different things
it's like open source it's composable um
it's bable right so um if
deliver financial gain as the source of
fund is the purpose of the game yes you
should add it but if not maybe you
shouldn't right I think it really
depends on like what experience you're
trying to deliver um to the users if you
do want to sort of do like a financial
experience and you're going to have
tokens in your game what steps would you
take to design the tokenomics before you
sort of mainten it it
um I would say like our team is like not
really good at tokenomics so um I would
say like the uh speculation that we add
here is like a founding curve that's not
really a token but so we're like better
at like allowing you to bet on like
people's skills um but yeah so I would
say I don't know can we contribute to
the game as an open source Dev um it's
right now closed Source because we need
faster iterations um to ship um but yeah
if you're interested please come talk to
me afterwards okay so there's definitely
a troll in the audience cuz the one
question was super funny it was uh
should onchain games come with a pro
trading platform um uh I didn't see the
question a pro trading platform yeah uh
I would say prot trading platform is a
fun unchain game game if you're trying
to serve that group of like players yeah
yeah you should build unchain game for
that how long did it take you to build
this is there anything else you want
okay what okay how much money but you
perhaps get 1,000 High spending Wheels
instead uh I think it really depends on
what's the definition of the Casual
gaming that you mentioned because as far
as I understand casual gamers spend a
lot of money on things like if you I
think like if you consider like Sim City
they're they're like the main Revenue
driver um for like games um
so yeah yeah I I think I would need
clarification on this uh but yeah if you
were trying to Target the high Spenders
I think you would need to design the
game a little bit different um but yeah
okay and I think as the last question
how do you think you will compete with
simple games like pumped off
fun how do you think you compete with
other ring games like pump of
fun that is a good question I wouldn't I
would say you're not you shouldn't try
to compete directly with pump.
fun
because it is the extreme of like
dopamin like it's the extreme version of
casino that you can achieve like you
know in the short term within crypto um
so what you should aim for is try to
deliver a different experience and try
to find your target audience because not
everyone enjoys a very PVP speculative
experience um so maybe you should find
people that enjoys different type of
speculation maybe they enjoy a more
casual one or maybe they enjoy your
Aesthetics or maybe enjoy they they
enjoy something else so it's always
about identifying players that want your
game I want your content thank you for
the talk um and the lengthy Q&amp;A it was
it was nice hearing from you
um up next is the last Talk of the day
you do want to stay here because it's
going to be a really cool one it's by
the team behind yman they work on a
bunch of data analytics and automation
tools for fully unchain games and we're
going to hear what they have to say
uh hey hello guys um my name is Rohan
I'm from
yen.
uh our team's been working on uh
quite a few things with autonomous
worlds for quite a while and I'd love to
show them to you so U um the outline of
the talk today we're talking about
exploring autonomous worlds where we
will showcase our awesome dashboards and
I'll tell you how uh we help developers
build great games and also how we give
Gamers an edge uh we then we'll talk
about command our brand new platform for
autonomous worlds we'll talk about how
we automate and mod games and our
intense platform and our very Grand
plans for the future so there are quite
a few slides let me jump straight in so
exploring autonomous worlds uh isn't all
the data on chain CH uh yes it is uh
this is this is what you see on chain uh
so uh it it's on a block Explorer you
see something like this uh a block
explorers are very helpful for erc2 the
transfers and things like where you
transfer money and all of that but here
you get to see the raw input it doesn't
you don't it doesn't make sense what you
have to do is you have to decode the
data to make it actually useful once you
decode it you get things like this you
get to see things like login Player move
you get to see what AC performed what
the input parameters was and this this
opens up interesting possibilities
emerge uh if we were to index it and
store it at scale we can then create
nice tables Gra charts and all of that
and uh this is an example from Eve
online play test uh uh you can see the
data and you can compare it with each
other so on a table you get to see U uh
compare and contrast as much visual
representation makes a lot of
sense um it gets even better if we make
the game make the data game aware so let
me show you an examp uh what you see
here is all the fleet movements within
the primordium universe and the same
data but this time it's aware of the
game so you can see all the fleet
movements so uh as a developer when you
look at it you'll be like hey why are
these people making these incredible
long Journeys uh and uh you see like
clusters of movement you also see these
massive long trips and you can you can
then tailor make your game redesign the
game it's also great for gamers to see
what the hot spots are and think this is
one more example this is u a 2d
representation of a biomes 3D World
uh if you if you look carefully you
might see white spots those are the mind
uh ores and the red ones are to be
minded again these are very helpful for
gamers and developers alike so great we
have useful
dashboards uh one other thing so on on a
blockchain the live State can be queried
so uh the all the block all the all the
work is gone to make the state um pretty
the consensus is on the state but what
about the history of the state what if
you want to see what happened back in
time at at a point in time say say a
month ago or 6 months ago or you want to
see like how many players group together
to fight the battle that they won and
whose Health was how much at that point
in time so if you want to go back to
Something in point in time it's it's
much harder and that's where human's
time travel indexer comes in uh I showed
you this morning quickly but what you
can do is um I have a video here so uh
this is draw so you're able to show
you're able to to move back and forth
and you're able to see what the state of
the blockchain was at that point in time
so all of this comes from our mud
indexer as you click it generates a
whole it pulls all the data data from
all the different tables at that point
in time and gets the data to you um so U
yeah so clicking back and forward on
that demo it it got us thinking hey what
if we clicked forward one second at a
time or like match the block speed and
that's where we got the idea for a live
replay so uh I want to try this um I
want to replay the first ever Sky Strife
match on Redstone this was back in May
May 1st I think and I I want to do the
live replay let me check if it
works uh okay let's move SC
screens okay so yeah it didn't work this
morning but uh as it loads let me tell
you what it's doing so this is loading
the date uh from May and once it loads
it tries to like replay the game so you
can actually see what the game is about
okay it's a blank screen give it a
minute so yeah perfect so it it loads so
what you're looking at is the actual
first ever game on Redstone with Sky
Strife you can see luden Ben from West
and proof of Jake and I think that's
Peter Pan they're battling it out in the
first ever Sky strive game so uh uh this
is all from M indexer working with the
data so yeah it's pretty cool and so
cool so let me go back and so that
that's so I've covered Yen for
exploration of data we we've discussed
the rich dashboards and also the ability
to like uh visualize data go back to
time travel capabilities and all of that
uh I want to move ahead from exploration
to action so this is where we actually
make onchain actions uh we had a few
questions
while we're thinking about human command
the questions were how do we extend an
autonomous world and how do we
incentivize developers to actually EX in
autonomous worlds and how do we give
security guarantees to users we don't
want users to go to random websites or
or download things to actually run mods
and automation so and also we were
thinking about what the mechanis of
interaction between all these various
parties would be so I want to show you
Yan command but Yan command is a few
things uh and let me start by the first
thing and Yan command is an app store
for autonomous worlds so uh this is uh y
command if you go in there now you see
this this is a list of it's a gallery of
apps each app is a mod or an automation
submitted by a developer you could
submit it anybody could submit it and
they're all listed there and uh you
could you we have U mods and automation
for biomes primordium quite a few other
games and then if you were to click on
one pretty much like what you see on an
app store uh you get ratings reviews you
uh there is an exploration explanation
of what the app actually does does and
uh you get to see related apps um and
also you get to view the code is
important you can actually see what the
actual thing does and once you're happy
with the app you click on install and
that that's when uh the our our sandbox
environment for users come in uh when
you click on install we tell you hey
this app is looking for access to this
world contract in this case it's a
biomes World contract is looking to mine
move jump build and these are the
actions it wants to do if you feel yes
it's okay it's safe let me do install it
you install it and this is uh a list of
all the apps running on youran command
and uh you can either stop them start
them you control them you uninstall them
all kinds of things like that there are
various apps there are also apps which
send you telegram alerts each time
something happens on chain and yeah so
there are quite a few things quite a few
apps already in there so an App Store
with a Sandbox environment is already
awesome uh we can do quite a few things
and uh we've already we have quite a few
we had a few people testing it uh this
is uh uh Ben from wasid uh he's his
team's actually tested it and what he
says is command is a game changer and
one of the coolest Platforms in the
space it kills the fud that Bots will
ruin fully on chain games by
democratizing access to Automation and
improving the gameplay experience poish
AF so uh uh essentially the keyword here
is democratized so we are able to like
like create a simple interface users are
able to click on stuff they're able to
like mod automate uh and and and yeah
experience the autonomous World in a
different way uh and everybody do you
want to build a yman all you have to do
is uh head to command do.ai and then you
can get started uh it's it's pretty easy
because all the other apps are also open
source you can just go there click on a
click on the fork button you're able to
like improve the apps submit it back to
the app store for other users they're
able to play and all of that so which is
great and you reach a bunch of users uh
and yeah so what's next for command
we've learned a lot by building all that
you've seen till now and command as well
and now I want to I want to I want to
really invite ideas questions feedback
as we think about what next what's next
for command so uh U Yan command has an
intense platform for autonomous worlds
now um think think about this say say
for example you are in biomes and um
you're building a Wonder it's it's
creative work you're you're putting that
together and you need 125 stone blocks
so um there are two labor intensive you
actually you have to switch off from
your creative mode you'll have to do
something else or the other option is to
go make a physical trip digital physics
apply and things like that you'll have
to make a trip to the Bazar go buy it
and things like that so what do you do
if you don't want to do either of these
things what do you
do um what you really need is uh deliver
in biomes or some kind of a grab if you
were in Thailand that's uh something
like a service that would give it to you
and uh uh we can't really build this on
an autonomous world now because we need
an intense powered Services layer on
chain and once we have this we can
actually launch services like uber
bounties or job book and things like
that so uh uh let me let me tell you how
an intense platform would work first
there is the intent so your intent is
simple it's get 125 stone blocks to me
in 50 minutes you have a clear high
level goal the constraints are defined
there just four constraints I need 125
and the type is stone blocks and the
target is me in this case and I need it
in minutes uh this is verifiable and
auditable so you get to see it on chain
and this is permissionless fulfillment
as anybody can do the job anybody can
get it to me and anything is fine uh and
you can and again only the intent is
specified you don't have to specify
things like delivery routes or how how
you get it you just have to get it to me
in get me this fulfill my intent and uh
the solvers work to satisfy your intent
intent so on cig GOI you might have you
might say feed my Cami one snack every
five FAS which is a continuous type of
an intent in Cafe Cosmos you might say
things like acquire the land and farm on
it which is again composable ioms you
might say something like guard my force
field while I'm away which is a
conditional intent so yes intents do
vary based on the game uh we see two
kinds of intents really based on the
transaction execution externally
fulfilled which are service request and
self- executed which is part of
automation so let me talk about the
externally fulfilled intents so this is
an intent that we were just talking
about now in biomes so as a user you
would broadcast this intent that you
want something service providers would
actually bid in real time so they say
hey I'll do it for $150 there are random
amounts and U um ratings and reviews are
based on the past um past activity um
you could actually manually select one
or even let Yen uh automate this hiring
process based on your pref your
preferences of how you want it to be
assigned and and so this is an example
of an externally fulfilled intent or a
service request the other type is is
also interesting these are self-
executed intents so uh say for example
you have a dark forest or a complex game
and you want to find a path from A to B
now these are like hard paths it's not
trivial you broadcast this intent again
and solvers this time around they
compete to find a path but they don't
don't execute the transaction they work
on a they work on a path they then
submit the solution to you to pay out uh
if they don't want to give you the whole
solution it could be a ZK proof or
something like that the solvers use
offchain compute they could be doing AI
inferences complex calculations whatever
in in this case the actual execution is
by you and uh the transaction is could
be crafted by the solver this is great
for automation cases uh command in this
case has to verify the alignment with
your and with what the solution is from
the user from from the uh solver so
great and this is one interesting
concept request and another worker
another person running human would
actually run the automation script to
perform that perform the T So command
would really power both the Uber driver
and the Uber the person who's requesting
it so all that could be
automated uh to achieve all this we
really need an intense standard with an
intense platform
um and it needs to be effective we will
need a single standardized intent across
all the different autonomous worlds so
it it should be easy it should be one
single standard and we enable solvers to
compete for the best solution it has to
be a Marketplace model we could also
look at things like uh uh cross chain
intent
fulfillment uh we need to we need the
int platform to be intelligent we'll
have ai solvers and also we need to
somehow maintain alignment with these
intents uh to facilitate all all the
seamless collaboration between humans
and AI solvers and lastly we'll need it
to be responsive uh if for example you
were on you were booking a grab uh you
would actually put the request out and
then you can edit it you can change your
destination you can cancel it things
like that so these things are also
important on an intense platform so uh
uh once we have this all working it's
going to be a pretty sophisticated
intense platform so the the Focus right
now is on the on the top quadrant there
the fully on chains are high transaction
volumes and low Financial Risk like if
you if you get if you forget to feed
your Camy or something like that the the
possible loss is is minimal compared to
like something on a def or or a DEX so
uh uh it could start ideal starting
point because it's it's high transaction
it gets tested as alvarius was talking
about this morning we can go into the
different stages of making it work
making it fast making it scale so we can
also increase it from security so start
with something and then move to more
security demanding applications so yes
uh in all these points I'd like to
stress that the intense solvers are the
real heroes they're actually the real
workers that get things done so which
brings me to my final aspect of human
command which is a solver control and
ownership platform so uh as described
before the solvers are the ones that
actually do it do the work and and uh
they create value and they AC value so
uh you pay them for the work that they
do and all of that so they they will
definitely ACR value uh the solvers are
going to be busy in an onchain world uh
it's it's continuous it never stops uh
what do you do at the end of the day
after you play a game do you log out of
an autonomous world uh why not be a
gamer by day and a solver by night I
think what the example is say for
example you the the vision with Tesla
and the Rob taxi is you get a Tesla you
drive it around when you don't need it
anymore you send it away it actually
does uh takes other jobs it does other
stuff and then and then it comes back
when you want it so and not if you have
a player that's fairly advanced in an
autonomous world you could um you could
then send it out to do jobs and and
things like that so which is going to be
which is interesting um this is one of
the last uh pictures here so uh a solver
will have different first of firstly
we'll have developers developers are
individuals that actually build the
logic they put it out there uh we will
need hardware for these solvers they
will be they'll be running AI inferences
or or complex CPU intensive jobs and
then you have IP contributors IP
contributors are interesting because you
don't have to like uh you don't have to
write long pages of of ideas or
something like that we've we've been in
Discord groups where the ideas are very
simple they're like hey why don't you
mine in a staircase pattern or something
like that those ideas also are pretty
important and then uh any system would
have to figure out how to how to
compensate these these users and fin
finally we have external Services uh for
any agentic framework we have access to
realtime data things like that so uh and
finally each solware can be operated as
a do so as they get larger and they ACR
more value uh it can it can be pretty
cool so that's a glimpse of the future
of
command uh so back to the original
questions that I asked at the beginning
uh this is how human command could
evolve to answer these questions so how
do we extend an autonomous world uh an
app store for mods and automation along
with an intense powered Services layer
could be a great start how do we how do
we incentivize developers we spoke about
the solver ownership model with a single
owner or a DA the solvers would get paid
and then we would have IP contributors
and they all get paid really with with
something like a solver ownership model
and how do we offer some security
guarantees to users uh we spoke about
things like sandboxing and intern
alignment at the platform level along
with discovery of with ratings reviews
to establish trust with developers and
then uh we will need an orchestration
and coordination layer to manage
interaction between in all these
different parties so uh U yeah I was
asked like what is the meaning of yan uh
Yan means uh Dependable diligent or
loyal worker someone who does a great
service is a part of the dictionary
definition Yan the name is inspired by
Yan Waters and U the yeah Tower of
London they've been um tased with God in
the crown jewels for centuries and
things so yeah so that's the end of the
talk so thank you so much guys get in
touch um this is I to say
Q&amp;A time yes um are you the paler of
autonomous
world is that a question yeah are you
the paler of autonomous world yeah we
could be we started as a a a dashboard
system all this data is a really onchain
everything is visible uh unlike paler
which which probably works on private
data that you don't want access to here
everything is on chain you really public
all the data out we just put it all
together in a usable format for users
really that's yeah that's the focus all
right and I think this one is uh yeah
how can other people add their the games
they build to Yan yeah there is some
work involved in adding a game to the
dashboard so all you have to do is go on
to our website there's a link if you
don't see your game in there already all
you have to do is go to the bottom of
the page and say add my game to the
dashboard we will need a few things like
your ABI or something like that so we
know how to index it what your world
contra contct things like that and we
could get started straight away all
right so next question is really funny
because it's like it's kind of just
questioning the entire category it's not
even a human question but uh why are
autonomous roles important like why are
we doing all this how is this
valuable at all yeah uh uh it's great so
uh yeah in my view U we have people here
there is a lot of energy there's a lot
of activity we're producing a lot of
data and then we could do things like so
maybe maybe this could be the perfect
place for an agentic system to take life
like they polish their agent
capabilities do something so there
probably a lot that can come out of
autonomous worlds
yeah can yman command R run on my
browser or Cloud that's a great question
uh we've been debating it internally for
quite some time where should it run at
the moment y command runs entirely on
your browser so it's on your device your
keys your your rules all that is on your
device which is pretty pretty cool for
uh from a uh decentralization point of
view the only annoying thing is if your
laptop switched off or something like
you cannot it stops running uh but on
the flip side I have Yan command running
on a remote desktop on a server and and
I and I ran it earlier today so it it
does stuff so you just have to get a
remote desktop like open up a browser
and it could run on a cloud really okay
so the next question is one I'm also
personally very interested in um go into
detail in how intelligent agents that
you create can can get integrated into
these games how do you how do you bring
them into the world yeah yes uh there
are there are a few ways we think about
it first is like an agent who owns an
agent like so in terms of an agent who
controls it so I spoke about different
owners so there are there are people who
provide the hardware there people who
who bring who develop it there's IP
there's quite a few things so uh in in
there so you we see those people as the
people who control and own the agent and
then then like how do you bring them in
they're already in they have access to
the apis and things like that that's how
we interact with the world and uh yeah
we could yeah that's okay and I think
this is probably the last question what
is your vision for the next two plus
years of yman yeah so Yan's been uh it
takes time to build a platform like this
and then we've been looking at it for a
while I think everything that I showed
you in the first part is all there uh we
have an app store and we have um a
Sandbox environment which is pretty
secure uh that was our first step our
next vision is to build the services
layer to power autonomous worlds and
possibly Beyond autonomous worlds to web
take a couple of years probably
and uh does that answer the question was
there anything yeah and I think that's
it I think I want to close off by saying
Peter theel says that if you want to win
you got to be contrarian and right the
problem with Peter theel is paler run on
one world but over here we create 100
worlds and Yen runs on all all these
worlds so Yen can its market cap is 100x
paler um and so Peter theel needs to
invest and oh cool stuff thank you thank
you guys thank everyone
uh and this was the last Talk of the
Day Cafe Cosmos gaming Corner uh try out
the game it should be really fun he's
got a lot of cool ideas about balancing
the physics of a world using gas prices
so check it out
he oh
