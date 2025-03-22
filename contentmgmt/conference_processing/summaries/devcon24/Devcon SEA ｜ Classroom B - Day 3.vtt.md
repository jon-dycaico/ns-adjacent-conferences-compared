[Music]
for
n
oh
m oh
o
a
m
[Applause]
and
is
you
for for
help yeah all right cool can you guys
hear me good awesome good morning
everybody I hope you guys are having a
great time at Devcon uh I don't know
about you guys but this just has been a
great week I've seen such cool talks and
the the build Guild is here in full uh
representation and we're here to support
you on scaffold eth and building on
ethereum so we're going to be focusing
today um on scaffold eth we're going to
explain a little bit about scaffold eth
um just to kind of feel for the room who
here has actually used scaffold eth
before anybody or is it kind of a new
okay cool couple hands who here is a
software
developer who here is an aspiring
software developer okay so we got some
new people we got some people that
probably have some experienc coding um
so I'm going to try to keep this kind of
a slow pace a lot of the workshops uh
that we had here this week have been a
little bit quick hard to follow so I do
want to make it kind of uh paced at a at
a a pace where you guys can follow along
especially you know being new uh in
building on ethereum can be a little uh
daunting uh who here attended another
scaffold eth Workshop this week anybody
few okay we had a lot so um who here's
hacking at the
hackathon a few of you okay cool thank
you for the hands I know you guys are
probably like but um Okay cool so I
appreciate you guys time uh my quick
intro about myself uh my name is Kevin
Jones I work as a de developer relations
engineer for the graph protocol uh but I
also am a core member of the build Guild
supporting scaffold eth on boarding and
education and ethereum um and it's
actually how I got my start into
ethereum so it's very appropriate I
continue to be very active in the
community um scaffold eth is a tool that
has come out of the build Guild or the
bidle GID uh the bidle GID just real
quickly is a basically a dow uh that is
U basically focused on education and
tools for the ethereum ecosystem uh so
if anyone wants to get involved with
with the build Guild you can totally do
that and I highly recommend that
especially if you're uh getting into
software development in the ethereum
ecosystem uh you can go to the build
Guild app uh but really the the the the
meat and potatoes for getting into the
build Guild is through a tool called
speedrun ethereum so speedrun ethereum
is this kind of U it's like a challenge
kind of gamification on writing and
developing smart contracts on ethereum
and so you go through this kind of
process where you go through and build
different projects so you start by
building a very simple nft you
eventually learn to build a staking
application and understand the concepts
of staking on a a smart contract then
you build a token vendor and then you do
a dice game and you learn about
Randomness on the ethereum blockchain uh
and then eventually you get a little bit
more difficult and you can build a DEX
uh once you finish that you actually
become a member of the build Guild so
anyone can do that so highly recommend
after today go to speedrun aum.com and
test your skills right uh because it's a
great learning experience too because
you really have to think about you know
what smart contracts are and how they
work uh at any point today if you have
questions uh in the app there's a
questions and answer um I'm going to try
to keep an eye on it when I'm here so I
can see but also feel free to raise your
hand okay I want this to be interactive
I don't want you guys to to you know I
don't want to lose anybody if you have a
question about something please uh let's
let's get it addressed okay
uh so we're going to talk about scaffold
e we're actually going to use it we're
going to we're going to walk through how
you use it and the ideas by the end of
today we're just going to deploy a smart
contract probably to a test net maybe
like Bas I don't know we'll see um but
if you want to get started on scaffold
eth everyone should go to scaffold
eat.io okay there's two ways you can
install scaffold eth you can clone the
repository and install the dependencies
using the uh git repo or you can use the
npx script uh method the package the
create eth package it's the easiest it
says beta here I've been trying to get
that to to go away but um we need to
remove that it's fully functional and
it's really probably how you should
install it uh especially if you want to
use Foundry if you use the git clone
method it comes with hard hat if you
want to use Foundry uh you want to use
this method so all you need to do um but
let's just look at the GitHub repo real
quick um the the main benefits to
scaffold eth and I'm going to show off
but is that it is kind of like complete
with everything you need to like build a
dab really it's great for hackathons
it's great for prototyping it's great
for like local First Development so you
can like build locally and you don't
have to like you know deploy to a test
net you can use just the local chain and
the local um front end that you have and
it's just got all the stuff working for
you uh it runs with some requirements so
you need node.js on your machine uh you
need a yarn package manager and you need
git so just one little bu bullet on yarn
is make sure you have the newest version
of yarn uh make sure you install that
because if you have an old version of
yarn you might have some issues uh and
if you have problems with node versions
just try 18 or 20 those are kind of the
most um uh compatible versions if you're
running Windows I would use WSL so the
Linux um installation for aunu and uh
because it's going to make a lot easier
uh I don't think it's really easy to use
uh just like native windows uh okay so
let's get started so let's do exactly
that let's go to npx create eth at
latest right so if you have a uh a
terminal open it up uh go ahead and type
that in so this is going to ask you if
once you first do that it's going to ask
you if you want to install that package
so that will just take you know a little
bit of time uh to install that um and
then it wants to know what you want to
name your uh package can you guys see
that okay yeah anyone have make it a
little
bigger okay so we're going to name this
one uh Devcon app sure uh it's gonna
it's going to ask you what kind of chain
you want to use so we support both hard
hat and Foundry um personally if you're
new I would recommend hard hat uh if
you're more familiar with typescript or
JavaScript I would use hard hat if
you're more like into this the solidity
aspects of of uh ethereum and
blockchains and stuff like that then
Foundry might be be a better option
Foundry is a little faster you can write
your smart contrast tests and your
deployment scripts in solidity so it's a
little bit less of a learning curve if
you don't know typescript but personally
I think hard hat is been around a little
bit longer so I use that you can also do
no chain uh if you wanted to just uh
just use it as a front end a lot of
people do that for different reasons but
so it's going to go through and install
the packages okay so this takes uh a
little bit of time depending on your
internet connection
uh and uh your machine so we'll just let
that sit for a second uh another thing
about scaffold eth is again I mentioned
it's a local first right kind of uh tool
so you're running a chain on your
machine and you're running a front end
on your machine and then you're using
another kind of terminal to do deploys
so you need a few windows open okay so
you can just open multiple terminals
that's fine uh what I I use is a tool
called t-x which lets me kind of split
my screen up so I can do uh like this
and I can split my screen into kind of a
few different ways and then I can go
into this Devcon app folder and these
other folders uh but you can just do
this in like three windows so just open
a new terminal go into the same
directory on each window so it's still
installing the packages so we'll give it
one second um let's go just really quick
and go back to scaffold E.O the next
thing you're going to want to always do
if you're just getting started on
scaffold e is take a look at the docs
the docs are super good super simple but
they have exactly what you need to know
um if you go to the quick start section
it gives you the how to install all the
requirements it tells you how to set up
your environment so it talks about where
the how you bring up your blockchain and
we're going to go through this where
your configuration for hard hat and
Foundry is how to do a
deploy um and then the components
section is super awesome because this is
these are packages that come with
scaffold eth that give you some really
cool added like added functionality out
of the box that you don't so especially
if you're not a front-end developer it's
very difficult when you first like start
writing smart contracts and it hooking
that stuff up to your uh smart contract
so an example would be like if you want
to get an address and you want to get
the balance of the address or just do
like ens resolution there's a component
for that so you can use that we're not
going to be focusing a lot on the front
end stuff but tomorrow Eda is doing a
workshop and if you are struggling with
that aspect I highly recommend you do
that because she's going to focus on
some of the front-end stuff uh we're
going to pretty much just do smart
contract stuff today uh you there's also
a balance component uh which is cool so
you can see what the balance of an
address is there's an address input that
you can type in an ens and it will
resolve it to an address for you a lot
of cool stuff uh ether input so it'll
figure out what the dollar amounts are
at the current time uh based on the uh
input and then the last part I just want
to show real quick before we get started
is the uh interacting with your smart
contract so there's also hooks in
scaffold e for reading from your smart
contract or writing so if you want to
read some data from a contract in a
specific function you can do that you
can pass in arguments if you want to
write a transaction to the blockchain
from your front end there's a re a write
function for that and that is also
available in here so like this is an
example of a button that will basically
call a function called greeting set
greeting with a value pass as an
argument and maybe value as like a
transaction like maybe you want to C
like pay pay in some value in the
transaction and then does some error
checking and it's just a it's a really
nice component really easy to do okay so
again this is not a front-end course but
I just want to mention that if you're
first getting started that's a great
place to go okay is it done yes okay
cool bought myself some time all right
so we're going to we have the package
now set up it's kind of ready to go so
we're going to go into our uh Devcon
folder this one and we're going to run
yarn chain so all this does is scaffold
eth is a mono repo so what that means is
it has like multiple packages in one and
it has this package Json file that has a
bunch of scripts that you can kind of
just type really easily using the yarn
command so yarn chain runs whatever
local chain you want to use so in this
case we chose hard hat um so what it
does is it spins up the blockchain on
the local machine Local Host and then it
gives you these private keys and public
keys that you can test with right uh and
then so if you wanted to you could
inject those into like your metamask if
you wanted to or something um but we're
just going to use something else which
is really cool about scaffold dates that
I'll show in a second and then this
other window we're going to open up our
front end so you always have your chain
open and then you always have your front
end open okay I'm having a bad typing
day today okay warm up my fingers all
right so we now have our chain running
and we also have react running so
scaffold e also comes with react with
nextjs and it is the app router
implementation of that um I'll show it
off in a little bit here but it's up and
running it's ready to go it's on Port
scaffold eth over here on Port
anyone anyone having yarn errors
hopefully you're not few okay so just
make sure you're using the newest
version of yarn uh and also um yeah
trying to think what else that's pretty
much the main thing make sure you using
a new version yarn and if you have to
change the version of node as well
sometimes there's like issues with
different versions of node you can use
NVM which is node version manager to
swap node versions 100% recommend that
too okay so scaffold e is up right we
have it up and running um if we firstly
scaffold eth here it's very basic but
but it gives us this uh our connected
address it's kind of like a hello world
page it tells us how to get started
editing our our application it also
tells us where our smart contract is
that comes with scaffold eth uh but it's
also what's what's the really cool thing
is this debug contracts tab so right up
here it's debug contract stab this is
kind of the magic sauce of scaffold eath
because one of the hardest parts uh of
of understanding um you know writing a
smart contract and then interacted with
your front end is every time you create
a smart contract and you compile it down
into bite code it also generates an ABI
okay so the ABI is this kind of like
treasure map or like uh how you actually
can navigate all the functions and the
variables in your smart contract now
what scaffold e does is when we deploy
our contract so we come down here and we
do yarn
deploy and come back it's going to give
us some output here it's going to say
okay cool the contract was deployed
successfully this is how much gas it
took this is some output that we get
from our deployment script and then we
see some terminal output here with
console log so we see what's going on
and we see that our front end also
refreshed so if we go back there we get
everything that's in our smart contract
inside of the front end okay so that's
really powerful because you don't need
to go in there and write uh you know
frontend code it's just ready to test so
we can kind of look at this and know
exactly what our smart contract looks
like it's got some greeting function or
greeting uh variable it's got an owner
variable which is an address it's got a
premium which is a Boolean and it's got
a counter which is an unsigned integer
and it's got a read function and it's
got two write functions right so it's
got this greeting that I could change
the greeting so I could say hello world
or something like that or actually let's
do hello Devcon okay like this and if I
try to hit send it's going to tell me I
don't have any gas so the next thing
you'll learn about scaffold e is you get
this burner wallet as well so you don't
need to connect to metamask you can just
start transacting there's a faucet
button you grab some f some funds from
hard hat or Foundry then you can go
ahead and interact with your smart
contract so I just paid some gas I got a
transaction receipt which has all the
details of the transaction and I updated
the state of the greeting variable so
very simple so um if we go into our uh
application and we look at that we can
see that's exactly what our smart
contract does so let's do that so here
it is I use vs code zoom in a little bit
so again is the monor repo so we have
this hard hat folder okay and inside
there we have this contracts
folder and then we have the year
contract so this is a very basic
contract it has the hard hat console so
this gives us our console logging output
that we see on the left terminal that I
have we have a basic contract called
your contract it has a a owner address
variable it has the string right here so
if I come in here and say building cool
app
save that redeploy and then I come back
to scaffold eth we will see that my uh
greeting will change here in just a
second there it goes so now it's
reflected my changes so the a lot of the
the life cycle of using scaffold eth is
that you just come in here make a change
to your smart contract deploy your
contract change and then test your your
you know changes right it's it's a way
for you to like test your assumptions as
Austin griffus likes to say so um Okay
cool so we have this very basic contract
it has a boole on it has a counter it
has a mapping which is cool so it keeps
track of like how many greetings a
particular address has done we'll use
that when we build our smart contract um
and then we have like some events which
events are like logs on ethereum um who
here would say they're new to using
writing
solidity few newbies so uh when you're
solidity uh everything is very simple uh
if you've written any other program
language uh it's very simple to get
started on solidity if you don't already
know about solidity by example it is the
most probably important uh website
you'll probably uh be using over the
next year it's going to have every
single example of every single
functionality inside of solidity and I
highly recommend that you guys come here
and kind of start using solidity by
example to test um different
functionality so there's like a hello
world there's a first application which
does like a counter and it allows you to
like see how you increment the counter
and uh this is just a great resource so
if you're coming in here we we kind of
have this kind of basic contract that's
a hello world contract it has this event
which is like logging it has a
Constructor The Constructor is basically
like at the time of deployment you might
want to set some values so in this case
we set an owner at the time of the
deployment so we pass this into the
deployment script which we'll go soon
and show off there's a modifier so what
I want to do actually is I just want to
kind of like gut out this contract I
want to show you that you can kind of
just start from scratch and uh go from
there so you should come into this
contract and you should let's just get
rid of some stuff so it's easy to see I
still want to use hard hat console right
so I'm going to keep that I want to get
rid of all of these variables I also
want to get rid of
this I want to get rid of this event I
need a Constructor but I want to get rid
of the stuff that I'm passing in the
Constructor
and I don't want this modifier
anymore I don't want this function
anymore I want this function because
this is an important one uh this is uh
there's two important functions here
that I want to keep one is a withdraw
function did I break something here oh
yeah okay uh there's this one function
that is a withdraw function which allows
me to withdraw all the funds from the
contract and then there's another one
that allows the contract to receive eth
uh even though there's no receive
function so it gives you that ability uh
we also took away the modifier which
we'll get rid of that we also don't have
this owner variable anymore because we
deleted that so we actually want to use
message.
sender so let me kind of show
you what I did okay so what I did is I
just took everything out I I kept the
Constructor I kept the name of the
contract uh which is the we want to use
this year contract because we have also
have a deploy script that's down here
but I'll get to that um and we just
emptied out the Constructor so there's
nothing being passed at the time that it
actually gets deployed but we keep this
because we want be people to be able to
come in here and withdraw the funds from
the contract especially if it's main net
uh this might get some some funds and we
don't want them locked in the contract
forever so what this does is it allows
people to uh a user to make a withdraw
function or call and anyone who does
that who is the sender can do a DOT call
and get the value which is the balance
of the contract so we can basically rug
pull this contract and then we can
basically pass a success okay or require
which um in solidity a requir statement
is something has has to happen otherwise
the transaction will be reverted uh and
then this last one like I said is just
so that if someone tries to send eth to
this uh address we still want it to be
able to receive eth um so it just allows
that that that receiving so it's like a
payable function okay uh so yeah so we
basically wiped it out let's save that
and let try to deploy so if you guys do
that uh you're going to get an error
you're going to get a couple errors
actually uh so we could look at the
errors in real time let's do it so this
one's saying well I expected zero
arguments but I actually got one
argument when I was doing the
deploy so if we go into that deploy
script right below so again we're using
hard hat in this version uh we are using
um typescript to deploy the contract uh
let me get rid of some of these comments
so you guys can see what's going on but
what we're doing is we are getting all
well we're getting the list of hard hat
accounts that are available to us by
doing this calling got uh dogit named
accounts and we take the very first one
and we use that to deploy the contract
so we use that private key the hard hat
private key um and then we we call the
dot deployments to do that to do the
deploy and then we create a deployment
right here by using the await so an
await is is like hey you need to wait
until everything is done before you
continue in this in this uh code and we
deploy the contract now we say who the
transaction is from right who sent the
transaction uh and what were the
arguments in that need to happen in that
transaction so this is where the
Constructor arguments are so as you
mention as we mentioned earlier we took
away the The Constructor arguments so we
also need to take away the arguments
here okay and we also have logging
enabled and we have like Auto m true you
can take those off if you wanted to
we'll just keep those there and then if
we save that and then now try to deploy
we'll get a new error but this is what
you do in software development right you
work through errors so then you're going
to see well we got to type error in our
deployment inside of our deploy contract
we got this your contract.
greeting is
not a function so let's go back so
another thing you'll notice is we do we
get an instance of the contract right
below here so we say okay if you have
deployed your contract
successfully take that and get a
contract by using get Contract from hard
hat ethers so hard hat ethers is an
ethers implementation for hard hat that
allows you to query the blockchain
basically to get get the inst get the
instance and we query it by calling the
name which is here and we query it by
calling the owner or who who it's from
is the deployer and then we once we have
that contract we can call any functions
inside of it which is really cool so we
can actually do some transactions here
inside of the deploy script or we can
yeah so in this case what we're doing is
we're doing a console log and we're
logging your contract.
greeting but this
doesn't exist anymore because I deleted
it right so we also need to get rid of
this okay so if we save that and then
deploy again we should be in the in the
in the good there we go cool successful
okay let me Zoom back in no more errors
so hopefully you guys have been able to
get to that point so you should come in
here you should Wipe Out the contract
you you don't really need this withdraw
function you could get rid of it too you
could get rid of this if you want we're
going to we just want to start from
scratch so um what I want to do now and
then you need to come in here make sure
you remove the arguments from the args
make sure you remove this console log
that you were doing here and right below
that and then you'll be kind of I where
I am um I want to pause a second for
questions because I know there probably
some people might have questions so
let's just give like couple minutes to
um ask answer questions uh put your hand
up if you have a question and I'll check
the app real
quick any questions
no
yep
F uh I was more focused on following up
with the code I didn't really um get why
did we do these changes I'm going to
build out a new smart contract right now
we're going to create an erc20 from
scratch so I we want to it's kind of
just when you're first using scaffold
eth it comes with this stuff to test and
see how it looks but you probably want
to just start from scratch so I wanted
to show you guys how if you're doing a
hackathon you can get rid of all the
stuff you need and just kind of uh start
at a base a new base and why these
specifically like why why the argument
and the the other line below I'll show
you but uh that's a good question uh so
the question was basically yeah like why
are we removing the arguments well this
contract comes with a um uh what's
called an ownable pattern or like an
ownership pattern where that owner
address is kind of like the access
control for withdrawing funds from the
contract uh we're actually going to use
open Zeppelin to do that and so I'm
going to show you why in a little bit
okay uh there was a couple questions in
here let me just read them real quick so
can you share the main difference
between scaffold e Hooks and wagi uh we
use wagm for some stuff like getting the
account um but the hooks U they're just
kind of custom and they were kind of
imported from the previous
implementation of scaffold e um so
they're kind of Rewritten to be more
optimized I think they're just they just
are designed for scaffold e so that's
kind of why they're that's how they're
different uh can you navigate a conflict
to that's a silly question uh what vs
code extension do you recommend uh
definitely the solidity and typescript
uh highlight syntaxing um I actually
recommend cursor I don't know if here's
everyone used cursor yet if you're not
using cursor at least like a couple days
of the week try it out and you will
really really really start to uh develop
a little quicker okay there are good
questions any more questions in the room
yeah over here um so I started
and then
I'm but I'm getting a address and use
problem oh I'm getting an address and
use problem for when I run yarn chain
after running it before and closing it
out that's interesting uh it sounds to
me like it's still running somewhere so
maybe you have it in another terminal
that you didn't notice double check uh
maybe just do like a PS and see if you
can find the uh binary you're running a
Mac yeah I can't or it's
Windows Windows Linux Linux yeah do a PS
like auo like um like
this grab I don't know what is it uh
Foundry oh you were using Foundry right
something like that and see if you can
find the process ID and then try to kill
so do like a kill dash9 process ID I'm
teaching you guys Linux too uh okay cool
yeah try to just kill the process that
should get rid of it okay let's keep
going um I think we answered a couple
questions if you have a question ask it
in the app and the next time I stop we
we'll go okay so we have our chain
running we have our front end running
let's start writing a contract we've
wiped out the contract to at least a
very base kind of spot the name of this
Workshop is about smart contracts so
let's try to write one just let's hope I
don't mess it up but let's see okay so
what I want to do is I want to create an
erc20 but I want first I want to start
by having access of this contract in a
way that is probably the standard okay
so we were using this kind of like uh
um we don't want to use open Zeppelin we
want to use uh
ownable let's see if that
works actually let me grab it from here
because I forgot what it is there it is
okay so we're going to use uh ownable
now the the beginning contract scav
comes with this kind of Access Control
pattern where you have an owner of a
contract and only that owner can do
certain things right but uh the standard
way to do it the easiest way to do it is
just to use open Zeppelin ownable so
we're going to do that we're going to
import ownable which is an access
control contract uh that allows me to
just take everything that's in this
contract and import it by doing your
contract is ownable like this and what
that's going to do is it's going to
allow me to deploy at the time of my
deployment
um okay so it wants it once so it wants
something passed in the Constructor uh
which I think let's see if we can do
that I forget how we need to do
it no arguments passed so I think it
wants the
owner past
here so we can set the owner so what I
want to do is I want to use my contract
address from the contract burner wallet
that I have so inside my burner wallet
so now that I've done my deployment the
the script or the sorry the smart
contract is pretty much empty I want to
use this address here in the burner
wallet as my owner okay so I'm going to
copy that and I'm gonna pass that into
the arguments which I think is what I
need to do let's
see what is
this that should work now let's try to
do the deploy let's see
oh uh address Constructor address
initialized owner yeah that should be it
oh I need to call so uh what's
interesting I think I need to do your
contract
deploy and is it
ownable frick I'm trying to think what I
need to
do it's in the Constructor oh yeah yeah
yeah you're right thank you very much so
it's not here actually it is
here like this
right ah thank you so we
do so like this oh I got you okay so
owner like this I would say that can I
do it like that I would say that yeah
but you can take the arguments from the
deployment if you want no it's
fine okay well all right that's okay
let's let's actually not do the ownable
stuff let's just focus on the actual
smart contract for the um erc20 I don't
want to like hold this up um let me just
redeploy those changes real quick okay
so the basic functionality of a um uh
token
is that you have like a name for the
token you have a symbol for the token
you have a total supply of how much
tokens that you want to have uh and then
you want to like mint that uh token to a
particular address and then you might
want to like sell that token on a
exchange or something like that so let's
try to actually do that just try to make
a token so what we'll do is we'll do a
um
string public name and we'll call it I
don't know everyone's talking about
these frogs so I'll do frogs how many
frogs do you guys have uh okay and then
we'll also do string public uh
symbol equal frog
sure uh and then we can also do a total
Supply uh let's do yeah one 1 two 3 1 2
so uh in solidity um or I should say on
ethereum you uh have this concept of
decimals right um
sorry I spelled this
wrong what am I doing wrong
here oh thank you gosh like failing
today okay so um you have this concept
of um uh basically decimals so if we
want to have 1 million tokens uh but we
also want to have the um you know the
full amount of decibels available we
want to multiply this by 10 to the 18th
power so we want to set the total Supply
to 1 million uh tokens um and then that
way it can be converted down so we have
this kind of like total Supply um and so
we can save that and then do our deploy
and kind of show what that looks like so
we do the
deploy and then when we come here we can
see that we have the variables are
showing up we have the name we have the
decimals we have the total Supply and
then we we have this cool functionality
here where we can like convert sorry
it's a little hard to hard to see but
scaffold e can convert it from you know
the standard ether values all the way
down to what it would be uh in 10 the
total amount of way is that that this
token is worth uh but we don't have any
way to um well first of all we haven't
minted that we have the supply but we
haven't actually transferred the the
value of that and so uh the way that we
do that with um uh ether or solidity is
we create yeah mapping so we say we want
to keep track of the balances of any
address that interact with the smart
contract and has some kind of like like
balance transfer of balance so we use
what's called mapping so mapping takes
one variable and essentially Maps it to
another variable and so in this case we
want to take in an address so any
particular address that has a balance
and we want to exactly tell how much
that balance is and we want this to be
publicly available so that a user could
query what their balance is and when you
do this with um uh solidity you get a
git function so you can actually see
what this balance is uh so if we query
that uh so let me just save that and
then in here we can set the balance of a
particular address at the time that the
contract deploys to anyone we want so we
don't want to actually send it to
Sender I want to send it to my
burner wallet so it's here so I'm going
to come in here copy the address and
then I'm just going to paste that in
here cool so let's hit send there we go
so now we can deploy our contract
cool so their contract is deployed um
and we can see that how much gas it took
and then if we go to scaffold eth now we
should see that we have this new read
function right so we can grab this
balance of this address paste it in here
and do a read so you can see how you
just paste in the uh thing it gives you
this like little blocky dude and then
you can uh do a read so the this is how
much actually uh tokens that we have we
can convert it by um you know seeing
exactly what that is in eth uh and then
we can back and forth but we now we
don't have any way to actually like
transfer the tokens around so we
probably want a way to transfer that's
the next thing that comes in um a
standard uh uh token so then what we can
do is write a new function so we will do
uh function oh got to love AI it just
kind of does everything for you uh so
what this is saying that is we need to
write a function that transfers by
taking in a two address and an amount
that we want to to transfer uh this
should be publicly available and then at
the time that someone calls this
function you want to do a check
basically to make sure that they have
enough tokens to send to another user
because otherwise they'd be double
spending right so we just do a little
like a require statement and then after
that we just update the balances so we
say okay well the balance of the person
who is calling the function so in in in
solidity you have these kind of like
Global variables which message.
sender
is the person that is uh sending the
transaction so that's the the the the uh
user what their public key basically and
if someone's calling the transfer
function we want to remove the amount
that they're going to send and then we
want to in whoever they're actually
sending it to you we update that mapping
too uh with the amount so here we
subtract here we increase okay so now we
can hit save and we can do
deploy cool so now we can go back to
scaffold e and we can see that we have
this contract and you'll notice that
every time we do a deploy we can force a
deploy by doing a uh yarn deploy D-
reset and you'll see the contract
address up here in the top it will
change and you'll constantly get a new
contract uh and so that's why we're kind
of like starting over from scratch every
time uh because the nons is changing on
the uh uh deployment so now we have this
contract we have a very basic
erc20 uh it's called frog it's uh the
name is frogs it's got a total Supply I
have a balance of whatever 1 million
tokens right here so if I want to
transfer some tokens now I can say let's
transfer to vitalic doeth and let's send
him some frog tokens sure uh
way so scaffold e has this really cool
tool that you just click the little
button and it will multiply whatever
values in the input by 10 to the 18th
power so I click that and that will tell
me exact exactly how much way that I
need to call in the transaction and then
I can go ahead and hit send and as you
can see it did this nice ens resolution
and we can see vitalik's photo um I'm
really sad vitalic changed his little
rainbow cat because that was a really
cool one but now it's his face uh so
there we go we have send and then here's
the receipt so we know that it was
successful uh and now we can come over
here and query against vitalic
address so vital.
eth and do a
read it resolved and now we can see that
he has a balance of 777 tokens so we've
created this kind of like very basic uh
implementation of a um of a erc20 uh so
I want to show you how to do the other
method so let's let's actually do uh
let's take a look at open
Zeppelin uh let see open zeppin erc20
let's see if I can find it
here so you probably don't want to
reinvent the will again like we were're
going to try to use the uh
uh okay this is going to tell me how I
can fix the ownable thing as well uh we
want to probably just go ahead and use
open Zeppelin right so you probably want
to reserve the time that you're uh
working on your smart contract uh to do
something new and Innovative since erc20
is a very very good standard we can just
use open Zeppelins okay so we can grab
this here and we can come back here and
let's just kind of like take away all
this stuff we did and show much how much
easier it's going to be if we just use
open Zepp
so we'll do
this and we'll do here so we can say
your contract is erc20 and then what we
need to do is we need to pass uh the
stuff inside of the Constructor so this
is what I was not able to figure out
earlier that I don't know why I wasn't
thinking about that but uh with erc20 it
has a Constructor so it has a its own
Constructor so when you're deploying an
instance of another contract you also
might have to call its Constructor so
this is how we do that we call this here
and so in this case we wanted to do
frogs and frog like
this uh and then here we can do
underscore mint so there's already a
function uh that's available to Mint
tokens okay so instead of us writing
that that function or that that line of
code to actually like create the tokens
we can just call this mint function okay
so what this will do is it will do uh
one one 2 3 1 two 3 so it's a million
tokens uh times 10 to the 18th I think
we can do it like that let's see if that
works yeah there we go okay now let's
try to deploy again so um and we could
also probably add ownable now I think as
well so if we do
uh well let's try to do that afterwards
okay so we have the erc20 uh let's
deploy it we already did it's successful
now if we come to scaffold eth what
you'll notice is we have a complete
token with just a couple lines of code
AS iOS before we had to like write all
this different code so we have this
token that has a decimals of 18 it has a
name of frogs symbol of frogs it's got
its total Supply but what's cool is it's
going to give you all the functions that
come in the other contract okay so since
we're importing erc20 standard we get
the allowance read function we get the
balance of that we had to write manually
last time we get the approve pattern for
an erc20 where you have to like approve
the spending of your tokens before
they're uh able to be spent and we also
get the transfer function and we get
transfer fum where we can transfer from
another address to another address if we
have the approval so we it's a little
bit more complete and it's a little
easier to implement so you should always
look and see if there's like a standard
that you can use I always like to go to
um cookbook.
deev I don't know if
anyone's heard of cookbook.
deev but
cookbook.
deev is a really good spot to
find contracts uh that you might be
think thinking about creating um and so
you don't have to reinvent the wheel so
if I come in here and like let's say I
want to look at ERC
find different implementations so here's
a soulbound nft right so uh if we want
to do a soulbound nft we could come here
and it's going to give us an example of
what the contract should look like also
what's cool about here is you can
download it uh with scaffold eth as well
so you can click this little uh icon
right here which is
and it will basically download the
entire package for you and uh it's
basically an entire uh installation of
scaffold eth and you can just spin up
your environment with that exact
contract inside of scaffold eth so it's
super powerful okay so uh okay we have
this token that we've created
um we used erc20 standard um let's let's
just I want to show you guys how you add
another contract so you might want to
add another contract at some point
because you know you might have a more
complex application so in this case we
have it's called your contract so we
also might want to do like new file and
we might want to call it another
contract like
this like this and then we can grab this
entire thing paste it in
here but let's just get rid of some of
this stuff and I don't know this we'll
just say like uh get rid of the
Constructor it's on your
C20 uh we'll just do uh I don't know we
do something like uh
string uh hello equal hello
world sure okay so we have this other
contract that we want to deploy but how
do we deploy it so we can if you're
using hard hat you can come in here and
create another deployment script so what
I'm going to do is take this contract
and make another deploy script so all
you need to do is do new file and do 01
uncore deploy uncore your I should say
deploy another contract so it's going to
go in order of the uh leading zeros so
this one would be deployed first this
one would be deployed second we can
paste that in we also need to update
instead of uh deploy your contract we
want to replace everything with another
contract so what we'll do is we'll find
anything that says your
contract and we will replace with
another contract let's see if that
works cool boom so now we're doing the
exact same Deploy on this contract so
now we have a new contract here that
just says hello and we have another
deploy script for it that's here it's
called another contract so we basically
we took this copied everything replaced
everything that says your contract with
another
contract oh I'm missing one here
there we go okay now let's try to deploy
that so that should give us two
contracts
now what did I do
wrong oh is it did I not do it
completely uh here oh thank you thank
you this the best audience ever you guys
are helping
me okay cool there we go so now that
should
work so basically we have now we have a
second contract uh now what's cool about
scaffold eth is it will show you the
other contract here at the top so we
have this contract which is our erc20
the Frog token and then over here we
have another contract which is just has
this kind of like oh that's weird
where's the variable for it oh it's not
public so it's private so defaults to
private so we need to make that public
redeploy your
changes and now we'll see this kind of
like string that shows up here there we
go cool so you probably are going to
make a way cooler smart contract right
um you'll probably do some more
interesting things um if you want to get
some ideas of like smart contract stuff
I would just like I said look through uh
cookbook Dev to see what kind of other
um contracts are available for you to
use uh if you're trying to like create a
new contract um you know it just takes
time to kind of like innovate and do
stuff like that if you're new to
solidity again you should go through
solidity by example uh and just
understand how things work there's also
I don't think I talked about it but
there's a great uh set of YouTube videos
I personally like to learn learn by
videos so if you go to the smart
contract programmers YouTube which is
this guy um there's a bunch of playlists
that are available uh for different
things and uh the there's one just for
solidity 0.5 examples and then there's
another playlist here for solidity
solidity 0.8 so definitely recommend
watching both of those I think most of
the time that they might be embedded in
here sometimes uh no so you kind of have
to look them up uh I think he needs to
like put links so it's easier for people
but um yeah for the most part you can
find for all these examples that are on
the left you can find related videos
that explain in like detail of of what
each line of code does and why um he's a
really good teacher uh okay so let's
let's pretend that we kind of have this
contract first of all I'll stop for a
second and see if anyone has questions
and then if not what we'll do is we'll
try to deploy this contract okay to a
test net so uh show of hands if anyone's
stuck or has a question so
far anybody good ber okay let's do this
all right let me just make sure there's
no questions here uh on this thing and
then what we'll do is we're going to try
to uh deploy this contract to a a public
test now okay um so no questions looks
good okay so the first thing is that um
we don't want to use the private keys
that are stored inside of um the
different chains so we have hard hat or
we have Foundry they come with private
keys and public Keys you don't want to
use that when you moving to a test net
so uh the first thing that we actually
need to do is take our uh implementation
and we need to generate a private key
okay our own private key so scaffold e
actually has a function for that so you
can do yarn
generate so depending on which uh chain
you're using if you're using uh hard hat
it's going to just create A.V file with
your private key inside of that that
file that's what you should keep secret
obviously and then it's going to give
you your public key here okay you can
also do yarn account and what this is
going to do is it's going to give you a
QR code that you could scan to basically
fund that account so I'm going to go
ahead and do that I'm going to use uh my
punk wallet to send some sapoia eth here
we'll deploy to
sapoia so I can um I have scaffold eth
was also used to build Punk wallet.io so
if you guys haven't seen that it's
really cool you can have this burner
wallet inside your browser and you can
fund it and it's stored in uh storage
like the private key so it's not good
for public stuff I wouldn't recommend it
um but it's good for like test Nets uh
so we have this ability to scan the QR
code with the camera and then I can just
send some eth to this deployer account
so I'll send in uh
eth we'll give it a
second so now if I do yarn accounts oh
is there a question
sorry I'm going to use seoa yeah just
because sapoia is easy uh else base
suppo is pretty easy um I mean shoot you
can deploy to base these days pretty
cheap
so um but yeah let's see it might take a
second for the uh thing to go through it
takes maybe like 10 seconds let's see so
if you do yarn account it goes out and
checks the balances where did it
actually go I hope it
did that's
weird let me just make sure that I got
the address right
uh I don't think it yeah that's the
right address let me just try sending a
little bit
more okay your on
account okay let's look at this let's
look at the the
scan uh soia ether scan and we'll put in
this address and let's see if it has a
balance it could be that the yarn
account is not showing us the balance
but it actually has
one yeah so it has some eth it has 0.2
eth so I funded it from my phone send it
over so now what I'm going to do is I'm
going to I have a a deployer key now
private key uh so what I can do is
deploy my contract so there's a couple
ways you can deploy your contract uh
with hard hat you go into the hard hat
directory and there's a hard hat config
and inside of here we have a
configuration of what uh deployment we
want to use so in this case the default
network is currently set to Local Host
so we've been like doing everything
locally but now we want to put it on
sapoia so we're going to replace this
with sapoia like that hit save and then
now we're going to go ahead and do a
deploy using spolia so we could also if
we didn't want to update the config we
could also do-- Network and you can just
type sepolia as well so it's either or
right so let's just go ahead and do a
deploy so what this is going to do is
it's going to take a um the contracts
try to compile it which it didn't need
to and now it's going to propose the
transaction and then try to uh basically
do a contract creation so it's a little
slower
obviously uh so we got it deploying
right
now what did I
do insu efficient funds okay so PO is
expensive right now okay let's try to uh
send some more funds let's
see it's probably because the erc20
contract let's do
of it
so uh yourn
accounts let's try
okay let's try now yarn
deploy insufficient funds oh my gosh
it's so
expensive all right I'm just going to
send a lot of eth I'm just going to YOLO
like one eth let's do
it oh I don't have that much eth on here
okay I got to get it from somewhere else
uh let's
do right
here let's do here let's grab the
address sorry uh where's the address at
boom I'm just going to send some eth
from this other wallet that I have which
has a lot more
okay okay so we do uh send
paste in that
address and let's send I don't know eth
we want to send
uh send like two sure what how do I not
have that many
funds oh thank you that wouldn't have
been good uh yeah where's the bully
at one did I miss I go byy
it where's the in the bottom short test
oh yeah thank you it's so weird cuz I
have like some test Nets in the top
there we go that's a lot more okay let's
try sending that to there okay uh in the
log the log is showing balance zero are
you sure you pass the accounts in the
sapoia network
config the balance is shown zero I think
it's a wrong
account huh because 0.2 is way more
enough to deploy a simple
that's weird maybe it's I mean in the
hard hat config file oh in the hard R
config yeah so seia
accounts sepolia config sepolia config
default Network sepolia yeah networks
what's the private key yeah should be
using deployer private
key that should be
right I think accounts you have to pass
hyen Network SEO and see what's the
price
when you did Yan account I guess
yeah let me just double check
account so
this it doesn't look like it
yeah what's
that oh you you think oh you think I'm
doing I need to do das D Network flag
here like that
oh yeah but
I yeah yeah yeah yeah
yeah but I just looked on ether scan I I
just looked on ether scan and I thought
it said that I do
though right if we go
here
here I have I have
balance yeah so it it seems like check
in let me just try
this let me see if this will
work something weirds going on oh can
you just import the private key into
metamask and confirm the valid address I
think it's two different
accounts uh yeah yeah the do you have
the private key there
right yeah yeah where it do uh see
packages hard hat.
EnV I
think no it counts yeah it counts thank
you all right let's see Add accounts
import accounts R key boom that works
okay yeah it's weird yeah it's not oh
it's weird yeah yeah I don't know it's
some something weird is going on unless
it's something with my something with
the RPC provider it might be that
actually because I'm using a public the
public RPC
but
okay well okay yeah I'm not sure what's
going on it's very
weird let me just double check the
config real quick
default network
ofia
default I don't need to change anything
here right for the deployer now should
work this for named accounts so that
should be like what it's using for local
stuff but
uh uh do what
oh like another
Network I don't think that's what it is
because he's right it does say zero here
balance
zero so it's almost like it's not
pointing at the right Network or it's
the RPC Endo is wrong and it's just a
faulting uh
here like maybe this needs to change to
Alchemy let me try just doing that real
quick
so
Alchemy UHC let's see did I spell right
no you can take another RPC from chain
list
yes let me just try this real
quick the demo gods do not like me
today okay um
come
on there we
go okay UPS let's use this test
one cool
I wonder if this will work if I just use
this
one I'm just curious more than
anything oh you can you go to the
packages directly and try manually
deploying it like packages SL hatch uh
yeah I'd prefer not to though it's using
toolbox so the deploy function is
there oh this is main net but where's
the bully
at there we go let's try
this sorry guys sorry we're having
issues this is unexpected the good thing
is there's like a billion videos of
deploy
oh yeah yeah let's just try to deploy
let's see if it
works there it goes so it's the RPC
provider man we got to fix that scaffold
eth we just changed the RPC provider and
uh because we were having issues with
Alchemy blacklisting our our API key
cool it's working now all
right that's fun all right cool so uh
we're going to deploy deyer contract now
uh as you can see it deployed
successfully tells us how much gas we
got uh we have the typescript
definitions were created now what we
want to do is change our front end so
let's get rid of
this um we want to change our front end
to ELO point to to sapoia now we're
still using hard hat so we're going to
go into the uh contracts folder or sorry
the hard uh nextjs folder we haven't
really touched nextjs we didn't do any
front-end stuff but there's one config
that you're probably going to want to
know and that is the scaffold config.txt
um but we're going to do subia we can
also change the polling interval uh we
can get rid of like a a a zero and we
could also put in an API key for Alchemy
if we wanted here as well uh if you're
if you have your own API key you should
put it in okay now let's go ahead and
load up scaffold e again now you'll
notice we got kicked out of the wallet
so first of all let's take a look at the
contracts uh these These are both going
to be um
unverified I think I need to actually
update the RPC provider too I think the
RPC is completely messed so let's let
let me put my API key in and see if that
works because it's already freaking out
okay let's go to API let's copy the key
and let's also put that in
here save it and then you might need to
restart nextjs if you do
that let's try it
again okay so now we're on sapoia we
have our contract deployed on sapoia
here so we can see that
uh we can also see that we got kicked
out of the burner wallet so we want to
we don't want to use burner Wallets on a
test net because they're stored in local
storage so it's not really the most
secure way uh so we now need to use
metamask right so we're going to connect
connect to metamask hit next
confirm uh it wants us to switch
networks we did and now we're on sapoia
it has a I have a balance in my uh
address I have the another contract
which is just the hello world and then I
have this year contract which is an
erc20 uh and it should have a minted
supply of my burner wallet but uh oh you
know what I I don't know who I minted it
to let's see let's take a look at the
deploy script uh what did I do your
contract deploy deploy your
contract uh sorry where's the contract
at your
contract oh I sent it to the hard hat
address that's okay uh either way we're
not going to actually do a test anyways
but I just want to show that we've
deployed successfully here uh and we
have this kind of like read
functionality so now we should be able
to um see who deployed the contract so
if we come here we can click on the
address and we can see that here was
when the transaction was done 3 minutes
ago from this uh contract creation which
here um and yeah we can also see that
it's not verified so the next thing you
probably want to do is verify your
contract so what we can do is come over
here and let's this is going to be fun
let's see if it works yarn verify D-
Network
sapoia so that's going to take the the
the contracts and basically like figure
out what the bik code should look like
um based on the what's on on Chain
versus uh sending the ABI to U ether
scan I think is what it does and it's
going to verify it so there we go now
it's verified I think because I put my
API key in it's good so it's going to be
good yeah
so there we go that one's verified this
one should be verified now as well so
now if we come back to Ether scan we can
hit refresh and that contract will have
a green check mark okay so that's
definitely a cool feature of scaffold um
because you want to verify your contract
especially if you want to like use the
graph or some other tool that needs the
ABI that way the ABI will be publicly
available um Okay cool so now we have
our contract that was deployed it's
successful um we could basically try to
like interact with it let's just see if
we can do that um see where's it at here
we go uh so we can do like balance of
italic eth it's going to be
empty yeah cool um but yeah we can see
that both the contracts are deployed so
cool all right what else do we want to
show off um we also might want to deploy
this somewhere for like testing with
like other you know users like you want
to actually send the URL to someone uh
so the next thing is you probably want
to ship this front end there's a command
for that with versel so we can easily
ship the applications by doing a yarn um
versel uh colon YOLO
d-r which is the most awesome uh yarn
command ever but what it's going to do
is it's going to ask you to sign into to
versell so you can sign in with GitHub
uh or you can sign in with like uh uh
like an oo hook to uh versel and then
it's going to ask you if you want to set
up and deploy we say yes it's going to
ask you if you want to use an existing
scope of projects uh or what your
project scope is so mind it's Kevin
Jones creates it found our project I
want to create a new one so I'm going to
say
no and then I'm going to not link it to
an existing project I am going to do it
to a new one so I'll just do this I
don't know Devcon demo enter it ask me
where the code is located I can just hit
enter and now it's going to set up the
project so what it's going to do is like
uh create the config file uh for versell
and then build it make sure it builds
properly uh set the ports all that stuff
like that and then it's going to ask if
you want to modify the changes you say
no and then now you can deploy it so
it's going to push it out here so if we
come to this URL
now uh it takes a second to
deploy we can come here paste that
in and oh I need to be in the right
browser session which is a little
annoying so by default versell like will
make it
private so you need to like authenticate
and actually sign in to
versell but uh as you can see here it's
building so that will take a second so
it's already kind of like transferred
all the the files to versell and now
versell is running some Automation and
basically creating a page for me so at
this point then we'll have this kind of
like deployed application uh we didn't
really do any friend in code but like I
said Eda next uh tomorrow she will do a
much further um demo um and show you how
to use the hooks and the components
reading and writing from your contract
uh and and stuff like
that okay cool I want to talk about one
more thing um first of all let's stop
for a second sorry about the hiccups I'm
glad we were actually able to deploy the
contract uh but are there any questions
uh up into to this point that I can
answer
y
yeah network not supported uh did you do
yarn verifi D-
network uh yep and you typed sapoia no I
use Bas Bas uh it's Base main net maybe
uh so if we go into the hard hack config
so the question was uh he was trying to
do his verification but it said network
not found so I think what's going on
probably is inside of the hard hack
config we can take a look at what base
is called so I think it's called
base oh maybe it is called base yeah B
Yeah so basically the error message says
network vinity 8453 not
supported you can specify the URL
manually bya API
URL oh maybe you can't verify contracts
it's possible uh that you can't verify
contracts for base possibly um so there
might be a a manual URL you can pass
with the API key using like base uh base
scan or whatever it's called Uh so
there's probably a way to do it you need
to go to the base uh block Explorer and
go to the verification for that contract
and it will tell you how to do
it cool any other questions yeah uhhuh
let's get get your mic first
yes thank you uh I would like to know
where to specify the API key for the BL
Explorer because to verify uh what I
that you need the blog Explorer API key
so in the in the structure of the
project where do we specify this key
yeah that's a good question um so I
think there's a um let's see if I can do
this yarn verify d-el maybe I don't know
that's going to work but there's a
there's a way to
do-- API key so you can say yarn verify
D- API key and you can also specify the
URL manually so yeah it's using hard hat
verify so if you want to look up the
documentation for hard hat verify that's
exactly what it uses at least what my
implementation is if you're using
Foundry it's going to be different I'm
not sure what they
use yeah
and when you you verify does it verify
all the contract or yes okay yeah like
scaffold eth is not like multi-chain out
of the box so it's just going to assume
that you want to verify all of the
contracts in that project if they're
already verified it we'll just skip them
yeah another question over
um so B basically a scuffled is for uh
nfts and staking apps assuming I would
like to do like a
computation and add it uh to a Smart
contract I'm using I don't know graph
Computing or something is is this
possible with scaffold e or is this more
for like saking ups and n i mean you can
you can write any evm smart contract
with scaffold e um so if you want to do
that inside of the smart contract then
yeah yeah you can do whatever you need
any kind of smart contract logic
anything you can write in solidity you
could write with scaffold e right but is
it what is the is it made for that or is
it made for uh the examples made on
speedrun ethereum is it made for
computation actually or was it made more
for like uh daps like staking and so on
yeah it's made more for daps it's not
really made for like decentralized
compute aspect stuff like it's not a I
mean yeah I'm not sure I'm not sure to
answer how to answer it but but
basically it's it's just an ethereum you
know tool for building and writing smart
contracts so anything with solidity but
daps yeah yeah cool we can talk after if
you have more questions yep cool any
other
questions sorry it's hard to see you
guys too I'm like
blinded okay cool I don't think anyone
else has questions no cool all right now
what we're going to do next is since we
have just a little bit more time I just
want to talk about the extension system
looks like we got like uh yeah not sure
how long uh maybe like 20 minutes 15
minutes or something so let's talk about
extensions um there is if you go to the
scaffold e website scaffold e.
and you
go to
docs and you come down here to there's a
section called extensions so uh I talked
about this yesterday um you can probably
find the talk um available later on
after they upload them uh where actually
show off an extension I probably don't
have time for that but there's a list of
available extensions here um one of the
extensions that I would recommend you
check out is the subgraph one uh because
it has the graph implementation there's
also other ones like onchain kit and
different uh eips as well as Ponder um
and then you can also create your own
extension so it's pretty cool if you are
a developer and you want to like
showcase scaffold e how it integrates
with something um you can build out a
extension
and add the functionality you want and
then every time you want to create a new
project you can just use that extensions
framework to start at that point so
really powerful and also if you go to
scaffold
E.O and you scroll down there is a
section that is all about components and
there's an extension guide here uh and
then we have the check out all the
available extensions so you can do it
like like I said before you can do the-
e flag and you can pass in a URL on
GitHub um and then here we can get a
list of uh extensions so here's the
subgraph one EIP Ponder erc20 onchain
kit there's a bunch of other uh
thirdparty ones that have been created
uh so we'd love to see what you guys uh
build there's a chain link one so if
there's something you're trying to do uh
with with u you know another integration
you should always check here there's an
a Fleek extension which uh is really
cool you can deploy a Fleek so if we
didn't want to deploy cell we might want
to deploy to Fleek you can use that so
yeah check these out highly recommend
them and um those are going to be a good
point to uh
start um and then El speedrun ethereum
so I just want to talk about speedrun
ethereum a little bit more so speedrun
ethereum uh when you first come here you
can connect your wallets and it's going
to uh create a profile for you with your
address generates this little like Punk
uh and then you can come in here and go
to the main speedrun ethereum page oh
reconnect and you can start a quest so
like the very first one is very very
simple so I guess my recommendation for
anyone that's new to ethereum try to do
this challenge because all you have to
do is do the first part of what I did
setup scaffold eth um and it's going to
let you create this kind of like nft uh
uh tool it's like just nft um with these
little like kind of fun characters um
and it's going to walk you through
everything you need to do so it tells
you what you need to install it tells
you how to get the repository go into
the repository check out a specific
Branch so it's a little different than
just the standard uh scaffold eth
installation because it is a g GitHub
repo right here uh and so each
particular branch is the the challenge
so if we go to it we can show what that
looks like here let we
go oh did I type it
in that's weird
huh that's weird okay let me just check
the scaffold e
website what's it called it's uh SC2
challenges so we go to
repositories SE to
huh they renamed the repository
okay there it
is okay so this is the challenges
repository um if you click here on Main
you can see all the challenges here so
zero through all the way down to seven
SVG nft so um yeah you can just choose
that repository and then each one is
going to have all the instructions as
well here so you can do it either way
but when you're ready to actually submit
your uh your progress you come all the
way to the bottom and you hit submit
Challenge and it's going to ask you
where you deployed it so earlier I
showed you guys how to deploy to verell
which we should have done actually let's
see if it it went through
successfully uh oh shoot where did I did
I lose it I had it here I don't know
where it went anyways uh it it will give
you the URL that I that I typed in and
put in so you need to put that URL right
here and then you also need to put the
contract address that is verified on uh
ether
scan uh so basically it's going to ask
you to deploy everything to sapoia so
you just need to put that sapoia ether
scan the contract also needs to be
verified because we do some automation
to like verify uh your contract so I
would recommend everyone try to do at
least challenge zero before the end of
the week it literally will take you like
kind of set you up to start learning a
little bit more and then you can learn
uh again how to do like uh staking so
this will go into like how you stake uh
use you do like token staking uh this is
how you do like a token vendor where you
can actually like deposit one asset and
get back another uh and then again this
talks about Randomness and then
eventually you build like a DEX which is
a lot more complicated but you learn a
lot because then you start to learn
about uh you know slippage and and and
stuff like that and um understand how
aex Works decentralized exchange cool
okay cool I think we're going to
probably end a little early unless
there's questions does anyone have
questions at
all yep question
here yes I would like to know when you
submit your challenge is it verified by
a human being be the s or is it
automatic do I need for example to send
a video to show that uh my Contra
respect the specification yeah so it's
all automated pretty much we just uh the
way we do it is we well the first few
challenges we do automated so we just
get the The Ether scan address and then
we pull down the source code and then
test it so we run like a test so each
challenge has a test so if the hard hat
test passes on your local machine it's
going to pass on the automation so we we
verify it when it gets down to the decks
it's done all manually so we actually
look at the code and make sure that it's
it's good um you don't need to do a
video though um and especially these
last few like the state Channel multisig
and SVG those are also all manual pretty
much yeah what are the questions we have
I think I saw another hand but I don't
know where it was
no cool awesome thank you guys so much
for coming and I hope you guys learned
something and it was useful thank you
spe
yeah oh
in
that
is e
I
sh
oh oh
he
for e
speee
t
okay 10
seconds okay good
right uh first thing thank you for
coming to this Workshop uh my name is
Remy and today we're going to talk about
ZK and identities and more precisely
about ZK and passports so this Workshop
is going to be splitted in two parts
first I am going to present you open
passports and in the second time Michael
and Theo are going to present you ZK
passport which is another ZK passport
project sweet so back one ago we
realized that the identity Market is
really inefficient because it's actually
not private nor
secure right now if you want to prove
your identity online most of the time
you're going to go through the whole KC
process which is actually not needed and
what's going to happen is you are going
to take a picture of your ID document
and send it to the application maybe do
a proof of liveliness or take a picture
of you maybe move the head a bit around
to be sure that it's really you and send
it to the application too and then you
are going to pray you are going to pray
that this information is kept secure and
that there will be no data leak and
spoiler there is and there is so many
like a massive one just happened two
weeks ago in France for
example also it's not even secure from
the point of view of the application
because um a picture of an ID document
or proof of loveliness is provable so
easily using generative AI which is not
good at
all and what's even more stupid is that
when you are do when you do a
traditional kawy you give all your
information which is most of the time
not needed you would like to give some
kind of more granular information about
yourself such as prove that you are
above certain age or that you are part
of a specific country without tring
anything else
so what can we
do fortunately for us at the
international civil aviation
organization already built a nice tool
on which we can piggy back down which is
the electronic passport it's issued in
chip with inside a bunch of data about
you which is signed by theer country so
this logo is the one of the E passports
if you got this one on yours it's
obviously an electronic ones
and these are pretty cool because as the
data is signed inside of it that mean
that we can verify that inside the ZK
proof and by doing so we can already
Target several issues related to
Identity the first one is of course the
Cil resistance how to prove that it's a
human who's behind an action a vote a
tweet or anything else the second one is
the selective disclosure I talked a bit
about this one before you might want to
prove something really specific about
yourself without revealing anything else
the last one is the
compliance as you can perform uh
computation inside zero knowledge
circuits you can actually prove that you
are not part of a list of country or
that you are not part of the ofac list
without revealing anything else so how
can we do that for example so the ofac
list is the list of the people that us
company are forbidden to deal with so
mostly terrorists and you can actually
parse this ofac list into a sparse
Merkel tree and then you can do a proof
of non-inclusion of your name and
surname inside this sparse Market
tree SS also as you're going to verify a
signature passport are uh ZK proof of
passport are totally
unforgeable which is one point for
crypto you can't actually SP crypto
that's not possible
sweet so now let's take a look at the
passport so in the passport there is
different data groups uh for example the
D1 is the mostly the information that is
contained in the main page of your
passport the D2 is the image which is
signed which is pretty cool too because
we could imagine to do some kind of ZKA
machine learning
tricks to do the proof of liveliness
with the phone that could be really cool
so these data groups are HED concatenate
met together and hased again and the
final result is signed by the isure
country or more precisely it is signed
by the document signing
certificate which is an intermediary
certificate that can sign up to 100K
passport and this document signing
certificate is signed by the country
signing certificate Authority which
rotates um every 3 to five years upon
the country and those certificates are
actually issue in public Registries
maintained by the international civil
aviation organization so that's actually
why it's so easy to verify passports
because we have access to the public
Keys okay I kind of lied when I said
that it was that easy because um
countries didn't agree on one signature
algorithm and Ash function so this is
all The Primitives that are currently
available in the passport
signatures there is even an knowing
count such as Germany that that use four
different ones including ecdsa with Shan
which is qu kind of
surprising yeah okay so if you want to
see if open passports currently support
your country you can refer to this map
uh you can go to map.
open passport.
or or scan this Square code basically
the countries in dark green are the one
that are currently supported uh the one
in green are the one issuing e passport
we should support them
soon and yeah if you pass the mouse on
The Country um okay so that's a
statistic screenshot but if you go on
the screen and you pass the mouse on
your country you will be able to see
which kind of signature algorithm and as
function your country is currently
using sweet um so my guess is that it's
time for demo
time like that you will have a better
idea of what we are doing
all right so what's going to happen when
you need to prove your identity using
open passport is that you're going to
scan a QR code scan this QR code if you
don't have the mobile application it's
going to install it and then the first
step will be to scan your passport or
for demo like this one you can actually
generate a mock passport inside the
application so if you don't have the
passport on you that's that's fine you
can generate one so let's do this
because obviously I don't want to show
my passport in front of
everyone so sweet that's my new
identity okay so next step when you
onboarded the passport should just have
like to scan the QR code once again and
that's it on the phone there is written
rainbow Chaser is requesting to prove
your own a valid passport which means
that I'm going to generate a ZK proof
and not disclose any information besides
the fact that I own a valid passport
that's it so let's do it let's generate
the Z proof there is a web soet
connection between the front end and the
mobile
application for the technical side we're
using gr6 and scom now we are move we
are currently moving to Noir and the
proect time is around 8 second withs so
sweet the proof has been
verified all right now let's say that
you're an application that want to gate
gatekeep the contents uh to users that
are above a certain age let's see how
you can actually do that technically
using open
passports so you we are going to use a
really straightforward flow because we
are in web 2 we are of chain so it's
going to be pretty easy so what we're
going to do is first obviously generate
a proof of passport and by that I mean
verify the Integrity of the data verify
the signature of the passports and
disclose the fact that you are older
than 18 years old and alongs with that
you are going to send the document
signing certificates to the to the
application like that the application
will be able to verify that these
document signings certificates have been
signed by one of the country signing
certificate
Authority so technically what we're
going to do in the front end is import
open passport SL core and instantiate
open passport verifier class so what you
just have to do is to declare a scope
which is basically just an app ID and
then the mode that you want to use so in
our case we're of chain so let's use
proof of chain
right you can you will also need to set
the minimum age to 18 and exclude
countries like Germany for absolutely no
reason I'm sorry about
that okay so this is the information you
can um work with using open passports
right now we are going to add more of
them right now you can deal with age so
gatekeep on age you can use nationality
so get keep so you can require your user
to be part of a specific country require
them to be not part of a country list or
ask them to disclose their nationality
and you can also ask them to generate a
proof that they are not part of Thea
list right so once uh once the the first
class inst
instantiated what you want to do is
generating a QR code and for that you
just have to import open passport CER
code from open passport C codes uh
that's a rect that's a react component
and and pass the open passport verifier
that you just intered before inside this
component and that's it the last thing
you want to do is in the UN unsuccess
call back function you want to write
some code to send the attestation to the
back end to verify the proof in the back
end
too okay so we saw that before right so
I told you that uh the connection
between the phone and the computer is
done using a web soet server by default
you you can use the one of open passport
but if you want to use your own we
actually provide you uh web socket
repository on the GitHub you just have
like to clone it and to start it it's
pretty
easy for the backend it's also really
easy you just have to one more time uh
instantiate the same open passport
verifier class with the same scope and
the same circuits which is still proof
of chain and to verify the attestation
you just have to call open passport
verifier verify and verify the
attestation and that's it like that you
know if the proof is
verified okay now let's say that you
have a defi application so you want to
use the same flow but this time on
chain it's going to be a little bit
different because you can't actually
send the document signing certificate to
the dup because a document signing
certificate is too big to pass in the C
data right so now you want to use uh ZK
proof for the S and Nest to so what
you're going to do is to send this
document signing certificate to a remote
prover we actually need to do that
because uh document signing certificate
are most of the time RSA with 4,000
kbits lens so it's actually take too
much time on client side proving but
it's not disclosing any personal
information so um you send this to
remote approver is going to send you
back a DC proof and you're going to send
to the
DAP in the C data the passport proof and
the DSC
proof so um if you want to run once
again there is a model prover that uh we
allow you to use the open passwort one
but if you want to run your own you can
it's pretty easy you just have like to
run the to F the code and to run it
that's it right so this time what you
want to do in the front end it's pretty
much the same actually uh the only
difference is you want to change
offchain for onchain and as we are in
defi we want to enable Offa check
because we want don't want terrorist to
use our application and exclude some
countries such as iron uh there is
typing so if if you just type the ey
letter it will propose you directly all
the all the
countries swe it and for the code it's
pretty much the
same all right now uh it's time for Nico
to present through how you can verify
this proof on chain using our smart
contract SDK okay thank you hi um uh my
name is niik um I'm work I'm mostly
working for a contract SDK at the open
passport and I will explain like how to
integrate open passport contract your
smart
contract um it's like the smart contract
you can do the pretty much the same
thing what you did on the offchain so
like you can reveal like you can
generate a proof which reveals like
nationalities like Ag and you can
rebuild it to the on chain so first uh
the how to integrate our
contract so um since uh the passport has
like so many like um like signature
algorithm and we need to have like a uh
like a different kind of verifiers for
each algorithm so like
um there is um so firstly like we
generate like a like a verifi gr s
verifiers for each signature algorithm
and we will like manage in the jic
verifier and like jic verifier is kind
of handle like a like like what kind of
proof is be like verified on like what
kind of contract and also like we also
have this open passwort verifier open
passwort verifier is basically are doing
like our data formatting or something so
like so this blue part is like handled
by us like it's managed by us like we're
going to update and we're going to add
more verifiers to it and what you need
to do is like just import open possible
verifier to your smart
contract and how you do it is like like
this so like firstly like you need to
import a interface of our open BS
verifier uh it's is easy you can uh uh
install uh it's already published as NP
package and like Define your like a uh
open password verifier instance and like
set your address on the Constructor or
whatever like not not only the
Constructor but you can set our like our
open pass verifier address to your smart
contract all right and then like um
after you integrate our smart contract
uh how to call I'll explain that how to
call a smart
contract so like uh this is a graph how
so like this in the right side this is
like a input what what you need to input
to have when you call the smart contract
and the left side is like the function
name when you call the smart
contract and then I at the first I part
um so uh um the currently like our open
passport circum circuit is like uh we're
going to uh like we verify all the dg1
like data and we going to put some kind
of zero mask for like which we don't
want to Ral the data so like only the
bite data which want to Ral is like uh
like a coming uh like it's it can be
like a public value and um we also want
we also need to uh like a format the
like a bite data into like our readable
data into like string or like into like
un and then we need to do like those
kind of like formatting
like our
executions and anyways like uh the in
the in the your prove like um like your
like a hidden data is already hidden so
it's like a zerob byte like to reduce
the gas cost on the on chain uh I
recommend you to choose like uh uh what
kind of data you want to Ral and you uh
like choose like uh like you should set
the selectors uh like what I what your
attribute you want to leave
so like uh firstly you should Define the
like u in 256 array named the structors
and then like you just put like U what
you want to Ral so like uh so those open
passwort attribute sector is already
defined it's also already defined in the
library and you will choose like you
want what your data you want to Ral and
also like there is also a combined
attribute selector functions and you
call uh like this uh like uh you 256
array and you generate a combined
selectors so yeah um after you uh
generate a combined selectors um you can
actually Ral the data from the
passport and this is a red part so after
you get a combined structors um You can
call a pass like a open password
verifier do verifier and verify and do
this and disc attrib
and you can call the attestation and
combine the selectors and you will get
like the passport attribute and you will
get like for example if you want to get
a nationality uh you can call as like um
open passport attributes.
Nation all right so turn yes thank you
niik all
right now let's take another example um
voting in this case you want to Target
some Maximum privacy preserving like you
want to have the biggest anony anonymity
sets and have actually no way of linking
your nullifier with what action you are
going to do and with the proof you want
to send so let me explain that when you
generate a proof of passports you have
to have a nullifier and this nullifier
has to be generated deterministically on
your passport data but for use cases
that requires really really strong
privacy privacy you need to hide this
nullifier because maybe country maybe
some countries actually keep the
passport data and it means that country
could actually reforge that nullifier so
to avoid that what are what you can
actually do using open passports is to
use a two-time flow so first you are
going to register to Commitment Merry
and in the second time you are going to
reuse this commitments and this time do
a proof of inclusion of your commitments
in the commitment
Merry and now you can disclose whatever
data that you want and there is actually
no way of linking uh the final proof
with your initial deterministic
nullifier so this flow is the same
either you want to do it on chain or
offchain so as I said the first step is
uh send a passport proof with only a
commitment you don't disclose anything
and your initial nullifier you want also
to um generate a DSC proof and to verify
that inside a commitment Merkel tree so
this commitment Merk tree can be either
onchain or offchain if you want to do it
on chain for doing stuff such as a gated
tornado cach for example that you could
gate on the fact that people are not on
youra list or just to be able to nullify
people um you can just use the open
passport smart
contract uh Library
SDK and there is this open passport
marry reader uh repository that will
allow you to listen the blockchain
listen all the events and reconstruct
the uh merel Tree on an AWS instance for
example of
whatever s and if you want to do this
offchain this repository allow allow you
allows you still to run everything of
chain just with typescript code so it
can verify the proof create a m tree
start the value inside and you will be
able to call it to retri the whole
tree sweet so what we did also for
Devcon is the cursive exhibition and for
that we create a little game which is
known as steal the
flag so this game uh is using open
passport of course and it's pretty
simple what you want to do in this game
is to steal the flag that is displayed
on screen right now there is no flag
because the game didn't start it but if
one of you if one of you scan this
Square code and generate a proof of
passport he would be able to replace the
background with its country flag so
let's let's do
it okay so now the application tell me
that uh open passports oh I'm not
sharing my screen anymore but what it's
saying is basically just that open
passport is requiring me to disclose uh
the country of my passport and that's it
so let's generate this proof once again
it's using web socket
so yeah I think there
is okay that's
fine and that's it it's also playing
your National anten
and the counter is searching for the
Bahamas and by the end of the con we
will elect the winner of this small
experiment
sweet
so thanks for your attention that's the
end of this presentation here is the QR
code that links to the GitHub
repository uh you can also try by
yourself the open passport playground if
you want to try the whole floor as I
said before if you don't have your
passport that's not a big deal because
you can generate one inside the
application so try it give us your
feedback because it's so valuable and
yeah thank you for your time and I would
be happy to answer to your
questions Florence
all right all right any questions
there's one here
yeah oh yes
please I can
say yeah I I can also repeat it so why
if this is like open source and we have
everything available why aren't all the
countries supported
already um do you mean like why are not
all the countries supported in op
passport right now very good question so
um there's a lot of different identity
systems in different countries and most
of the time when it's a national ID like
an ID card it only has one signatur
algorithm but the thing is that
passports are such a like wide um
specification that is used by many
different countries that can also have
each of them their own like security
preferences the specs are like kind of
vague actually and so there's many
different signature algorithms that many
different countries use so if you go on
map.
app you'll see a
detailed like map of all of the
different countries which ones are
supported right now and which signature
algorithm each of them uses so right now
we support a lot of them like most of
Europe the US for instance because it's
like the most common signature
algorithms but there are some countries
okay I won't name them but maybe like
Austria or maybe Germany or maybe Iran
it's like I think we can name them like
um oh maybe it's display on screen oh no
the screen is not sharing anymore they
they require a bit more work because
they have like um like they used a lot
of different signator algorithms like
RSA with multiple exponents so it's just
a bit more work but I think in like less
than a few months we can confidently say
that we can basically support the whole
world all right any
questions hello um I had like two
questions the first being like open
passport as I see on the website is
mostly like proof of personhood right so
we have other Solutions working like
World ID who are working like with the
similar Solutions like proof of person
vote and civil resistance so the first
question would be how is this like a
better solution than that the second
part being U so with open passport we
are generating ZK proofs of uh like
passport basically the user so in order
to in order to uh have this like a
global acceptance we would need um to
have like government involved in this or
not for the ZK proofs to be like used
everywhere the ones that are generated
using open passport so two two very good
questions the first one is um how is
that different from World ID so World ID
is what uh wal is doing I guess it was
called wal SC before now it's wal so I
think what the the work that wal is
doing is also quite important because
they're trying to tackle civil
resistance at the biometric level the
the tradeoffs here with what we're doing
is a bit different because world there's
a um like if they can actually make the
thing work and ship their their Hardware
all over the world and like everybody um
like gets like their I scanned and
everything it could definitely be a very
good system because then it does not
rely on state so we don't even have this
trust Assumption of passports or ID
cards but you know it's like quite hard
to execute on there's a lot of different
attack vectors on the hardware
especially now with the new or that can
be managed by anybody even without an
operator um and they also have to like
ship it everywhere it's not clear if
everybody can have access to an or so
like we we also chat a lot with them we
support a lot what they're doing they're
also supporting us um but I think the
trade of c a bit different and with this
kind of system just like with uh what
anadar is working on and like we're
planning on integrating Adar to in this
we can have like we can support a lot
more people a lot faster basically
because people just need their phones um
and um the other question which was
about uh do we need like governments to
collaborate with this the really great
part about this is that passports are
already deployed right and the public ke
already public uh unlike International
Registries so we don't really need to
ask countries which is kind of great um
there are some identity systems not
passports but others in which the public
keys are not public and so we need to
actually ask the countries so for Nico
worked on mind double cards which are
the identity cards of um of Japan and
like the they need to like ask for the
government for an API key to to check
that the the the like people's cards are
actual cards they don't have like all
the public Keys available but we have
them so um we don't really need to you
know we can just like Bo up on what the
governments already created of course if
we could like have better communication
with them we could also have them have
better standards like already have um
like selective disclosure directly in
passports but you know it's like very
long processes so we we can go faster
bying
this okay that sounds good uh the other
question that just came in my mind is
like how how will you handle like the
fake passports that people generate like
we have have seen incidents where people
have like five passports generated that
are fake basically um does open passport
handle has something to handle that
situations good question so what I
really like about this is that today
most most of kyc works on just you send
a photo of your passport okay this is
really bad first because all of the data
is stored and so if it's leaked like all
of your private data gets leaked and now
people can like have phone numbers or
like bank accounts with your data but
also as you know generative models like
just got way way better and so now it's
just possible to easily generate like
huge databases of fake people and like
kyc on websit so this is why we like
cryptography like maybe AI can generate
fake images but I'm not sure AI will
like break the the discret logarithm
problem for like RSA and the cdsa soon
so that's great um but if your question
is more about actual physical fake
passports
um I think what's
like my guess is that today most of the
fake passports they they they look good
from the outside but they don't actually
have a chip with the signature because
this is really hard to get you have to
actually get the private keys from the
countries and you have to get the right
country right so it's like actually very
like challenging I I would not be
surprised if there were like some fake
passports that had the whole signature
thing and everything I just think it's
probably quite rare and that's kind of
good for us right um but in this case
yeah if the whole passport is fake and
the the government kind of failed yeah
of course like you can do approv there
but I guess that's like the trust
assumption testing okay uh I had a
followup question to your penultimate
response about Japan's public key so if
the public key isn't public and only you
have it then if I'm doing a proof of my
identity that I'm a Japan citizen am I
offloading that to you where you have
the public and you're not sharing it
with me or do you share it with your
users so good question moo would be able
to maybe give more background but my
guess is that um you you have to call an
API to check for a Japanese citizen this
is for the Japanese ID card system not
for the passports for the passports we
can already do what we you but for the
Japanese ID card system you would each
time you want to verify you have to go
through an API but Japanese government
so I guess there's like censorship here
but um yeah is that is that
right um yes if you want to like check
the validity of that card every time you
need to check the like a government API
and like like like you need to like this
is the valid this card is valid or not
but still uh the like RSC key inside the
card is still available after it's the
car is boked so like um it can be used
as like a kind of wallet like like you
can use the operation like wallet
operation even after the col is rebooked
like for C resistance like for the EK IC
um you need to call the ja government
API
yeah
thanks so there is also a question from
the community the first one is can you
answer that open passports is not
selling user
information uh like which apps at which
apps a user connected
to yeah good good question so um the
nice thing about everything we're doing
is that it's open source like the
circuits are open source because it's do
DK part the contracts are open source
they're going to be onchain anyway the
whole app is open source and it's not
even just like we open source stuff it's
like we're building in public like you
can just see on the report like us
committing and doing everything so you
can like um yeah basically see
everything that's happening um again
like when you do an app on stores
there's always like I mean you never
know if like the card on the GitHub is
actually the one that's on the store
it's kind of a general problem with apps
um I think that like Apple and Google
Play Store are like every time doing
kind of verifications uh every time
there's like an update but yeah I guess
there's some just assumption on the fact
that the app is not completely
compromised uh if you don't want to do
this trust assumption you can just build
the app yourself on your computer load
it on your phone and then you know
exactly what's
running and then maybe um another
another question in the case of
pornography on Spain they want to
implement some kind of verification
based on dni so I guess national
identity system um is so does this kind
of solution solve this problem better
our opinion is that yes because the
question is if you're going to go on an
adult website and have to prove that
you're above 18 or above 21 do you
really want to send your um like
passport photo or something that's kind
of sensitive um maybe for banking it's
sensitive but in another way I think for
adult websit it's like more sensitive on
like your personal life like if there's
a you know if there's a leak you don't
want like people to to have this data
and like link it to you or something so
um I think this is where it's very
important and also there's not really
the compliance requirements that you
have with banking in which you have to
check every transaction do monitoring
for adult websites it's probably okay
like I can prove that I'm above 18 um
and um that's why we're like super
excited by use cases for open passport
this another question is is this open
passport SDK made with ZK circuit or
what technology is behind it so that's a
good question um open passport SDK is
mostly used to verify the proof so it's
not there is no circuits inside of
inside of it in a sense that it's just
verifying the proof so it's actually
using ZK in the sense that it's going to
verify a ZK proof but the generation of
the proof is only made locally on the
phone on the
phone are there plans to expand
information to include financial data
well I I would say that we we like you
can already use open passport for like
transactions um one thing that we're
kind of excited about is what we
recently prototyped the ofac um
non-inclusion proof so you can for
instance prove that you're not on the
ofac list and I think something that's
exciting in finance for that is like you
can have a wallet that says every time
you do a transaction it's going to take
the the passport data that you already
loaded inside your phone and it's going
to do a proof that you're not on the
ofac list live and what is nice about
that is that the ofac list gets updated
right and so you can do always a life
proof every time you do a transaction
you wouldn't necessarily need to scan
your password every time but you can do
it once in a while to like we can force
you to do it once in a while so that uh
we can make sure you didn't like steal a
passport or something um and then it
could be for instance like enshrined in
a layer one or Layer Two that like all
the transactions have to have this kind
of compliance system or you could have a
defy protocol in which you say okay like
this function when you call it there's a
modifier on the function and I want you
to um like only include this function in
a compliant transaction so those are
things we're excited about
all right uh can we scroll a bit on the
questions yeah perfect uh when do you
think it is necessary to do onchain and
offchain validations when is it better
to use one instead of the other in a
practical way so that's a really good
question uh the first way the first
answer is it's going to depend on the
Privacy larer that you want
um there is a like really clean answer
which would be uh if the application is
a web to application just prove it off
chain and if it's a d then prove it
onchain but uh let's say that you want a
maximum of uh
privacy and you want to use the two time
flow that we talked about before so
first you're going to register and
generate a commitment and in the second
time you want to reuse this commitment
to then generate a zkp so in this way
maybe it's better to actually generate
the first proof and Val verify it on
chain because that it could kind of
centralize every uh users and have the
biggest anonymity
sets yeah so another CL another question
is do you have an SDK to include it in
Native Native mobile applications okay
so there's kind of two
answers right now if you want to verify
proofs in your mobile app people you can
already integrate but people have to
like download the Open passport mobile
app to like do their proof and then you
can verify it in your um in your app one
thing we like thinking a lot about is
making a more General um like package or
SDK that you can add to do proofs and
passport scanning on your own app so for
instance you want a fully integrated
flow you don't want people to have to
download the Open passport mobile app
because it's like some friction you have
to download new app um and so you would
just be able to integrate it directly in
your app and that would be also really
nice um another thing that we're working
on is like app Clips so app Clips is
basically like something that um iOS
provides uh it's like you can easily
open like a a small version of an app
without having to go on the store and uh
click on download and everything uh and
like we tried the flow it's like very
great it's coming soon too so yeah
okay are there example of some corupt
countries issuing signed e passports
that's a really good question I think
the answer is quite all of them in a
small amount uh because most of the time
for Secret Agency they will need to like
create a real passport so that's that's
part of the game but uh they should not
sh that much and there is probably some
specific country I won't name them but
it's pretty easy to guess which one of
them and that's why you can actually
exclude this country when you generate
when you want user to disclose their
nationality yeah the kind of philosophy
we have is that um you like because all
the passport data is there when you scan
the passport as an app developer you can
have the flexibility to choose what you
want so if like one day one countries
like certificates get compromised you
can just exclude this country or like
this specific certificate or like go
more to the granularity like say okay
this signature algorithm is not secure
anymore and like now people can forge
proofs with shaan let's say um so now
like we can just exclude like people uh
that have like this specific um uh
signature algor if they renew their
passports uh like only support the new
ones so
yeah all right
um I think we're getting close to the
end of our side um so we might just um
welcome ZK passport to the
stage so ZK passport is another team
working on um passport verification bit
of a different stack different
philosophy and uh they can tell you more
about their approach
thanks Floren uh Round of Applause for
the open passport team
everyone hi I'm Michael Elliott I'm
co-founder of ziko passport and this is
Theo madil and we're going to go through
I I guess some of you may already be
familiar with what Zig passport is uh
how it works but today we're going to
have a workshop on how to actually plug
into it and uh to be able to leverage
these identity proofs for your own
project or apps and so we've built out
this SDK uh in typescript which allows
you to use this query
Builder yeah go ahead and with this
query Builder as you can see up here uh
you can as a for as a high level
overview here of how it works you just
request uh you specify which credentials
it is that you're interested in that
you'd like the user to prove and then
the rest is sort of handled for you you
get this URL back which can be displayed
as a QR code they'll scan that it'll
bring up the uh the is passport app on
whether it's iOS or Android
and so the idea is that you can try this
out on your s I'm going to pull it out
as a QR code so you can scan it from
your
site so if you want to join in oh sorry
I went to
wait so you can scan this uh it's a
repet um a reple so you can try it out
for Kit try it out on reple directly or
maybe try to do that locally but the
idea is that you can import ISD
k um um yes please than just going to
bring It full
screen so it's easy to say okay well
thanks should be a bit easier to see
now I'm going to keep this out for a few
seconds yep I think it's good to go yeah
so so the idea here is that we have this
repet that we made um so you're able to
Fork this repet and easily kind of get
going by yourselves um and test this in
the browser yeah so I'm going to show it
how how it looks like so
essentially also just it heads up we
don't have any fixture data yet so you
will need to use your own passport uh to
to be able to actually generate these
proofs yeah you need to have your
passport to test the flow so you will
generate uh a QR code with this example
I was considering lending mine to people
that don't have it but it may be a bit
of a security issue so yes so you have
to have your passort to do the entire
flow but I'm going to show it to you so
this is the deployed replate so you
click on generate new request it
generates the QR code with rdk you scan
this with any QR Code
Reader so it pulls it out on my phone
and I'm going to on this
side wait if the Wi-Fi is good
enough did you want to tether no I think
it's a more Wi-Fi issue because all the
website no through my tether through my
cellular oh yeah yeah go
ahead see if it shows
up
well you could do your own phone
y okay let me try again oh
jeez do I have connection
all
right oh no it works
better um
so yeah oh it
disappeared why
isn't oh there it is so the request was
received so this is like a little
message that will be use the camera you
can show you what's on your phone oh no
no no I don't want to okay yeah so
generating the proof I generated the
proof on the mobile my mobile phone and
now you get back my details of first
name country and that you can edit
easily in the app by playing around with
our uh different function disclose
function uh greater than equal if you
want to make a comparison with the age
the birth date or the data from the
passport so for example I'm going to go
here on the replate so what we do here
is like disclose nationality disclose
first name but for example we could add
uh another dis
close of like the let's say what should
I disclose
um my information oh wait last last name
let's go last
name so for example this might be a good
proof for social media where you just
want to prove your first and last name
but nothing else you're already sharing
that information publicly anyway on
maybe you know X met Twitter and this
could be like attached to the profile
there or maybe you know warcast far
Caster I may could I maybe just get a
show of pans of how many people have
their own passports with
them right cool so five six people will
be able to do this
today we should have maybe given that as
a heads up with the passport but at
least you'll be able to see the flow and
how it's achievable when you you know
you get home and you're able to uh use
your actual passport then so that's
useful yeah so here I'm going to add
another state variable so I can install
my last name
I got air completion that's pretty nice
um so I'm going to
complete
and here we go so from the result so the
way the result is uh structured is
you're going to have the query result
with the name of the field and whatever
function you require disclose or like if
you're doing comparison it would be
equal greater than or others and then
you would get the result so in most
cases that would be a bullion if you do
a comparison but here you direct
disclose the
data and you will get you can
actually lock the proof like the proof
would
be right here although I don't think I
see the logs here but
anyway and I can
add oh wait field for the first to last
name
so when I generated the request now
on all right
did I do
anything
Jesus a Trav issue it's the Wi-Fi off
damn we tried to reload this has anyone
of you been able to pull out the
repet no do you want the QR code again
by any
chance do you want the QR code
again oh yes
okay yes um
how uh you can Fork it uh you can
directly Fork the page and you can
create a rep replate account or I guess
you could create like an xgs cuz like we
I just Ed an xgs template so you could
create an xgs B plate like a simple app
and just integrate our SDK I'm going to
also show our QR code towards the SDK
repo so you can get the
link uh great the connections not
good going to switch back to the main
Wi-Fi so this is directly the QR code
for the repo of D SDK so it's not on mpm
yet so you can pull out directly the
GitHub uh URL
Android send me their email address so
they can actually be added oh
yeah can you just
plug also um so we're available
available on both IOS and Android
however currently the Android version is
only available uh for internal testers
because we kind of like released it too
um too late but if you're on Android and
you wanted to
join uh please just uh this is my
telegram handle please just um just
reach out to me now and send me your
email address and I can add you to the
internal Google Play Store uh app so
that you can get the Android
version just one sec
also you can just message me I'm ZK Mike
okay here's the uh QR
code so yeah again if you're on Android
uh and you want to get access to the
Android app just message me your email
address and I'll add you to the um the
Play Store
app okay I can give you my
phone I was using my phone but was my it
might be better
though plug
this if you're having issues still let
me know you can use my phone Heather
that okay so now it
works uh after fixing those issue with
Wi-Fi so uh you got the QR code here
which is essentially embedding uh
nationality Force first name and last
name request so in one more field
compared to before I'm going to scan it
again with my app zik passport app P add
the request on my side I'm being asked
for my last name now just waiting for
request received that can accept
generating the proof this is all done of
a websocket and an encrypted using ecdh
to to set up the shed secret and ecdss
SEC p256 K1 for the encryption and you
can see my last name in addition to my
first name now so this
is you can play around with the disclose
function you also have uh greater than
equal functions for example for age like
if you want to prove that you're over 18
and in this case it would essentially
send out bullion whether that is true or
false and that's the only information
you're going to get back from the user
so I'm probably going to try to set out
this so let's
say he's over 18
actually it's more 18 or Plus
okay so now I'm also ask for my age or
in age
comparison going to send it
back oh is it not showing oh I forgot
to
wait oops
all right
well is it
wait let me actually look back
into
SDK Define my types one one details
regarding this is that the all SDK is
strongly typed in typescript so
generally you will have like Auto
completion that's pretty intuitive so
you know what to uh expect and what to
put
in yeah
okay yeah it is it's fine
uh where is I was say I was I don't know
theed can get
any I guess this is
right so maybe now we can move on to
also just describing the subcircuit
design we have and um um and the
reasoning behind why we've designed it
this way so on on
mobile uh you you really constrained by
the number of um the amount of memory
that you can actually use and so we
can't have our circuit size blow out too
large too big or it won't work on mobile
and you want to have client side proving
on mobile because you want to keep
privacy you want to keep your private
you know passport data local to your
device it's on our t-shirts uh own your
identity you know the meaning behind
that is self- custodial identity where
you own your own data and also on that
topic um after this Workshop uh there's
plenty of t-shirts we have um so just uh
yeah after we finish please feel free to
to go over to the corner here and you
can you can grab your your T-shirt um we
got a new batch in today because we ran
out so uh yeah do you want to take it
away
there uh yes so um regarding the circuit
composition um wait who in the crowd was
in the talk yesterday we gave cuz I I
made a quick overview but that was not
very deep I was hoping to go more into
details so actually now I'm going to do
it uh so yeah you had that idea of um
certificate trust chain which is similar
to the SSL certificates if you know how
that works so essentially the passport
data is signed by the state but there's
two certificates in the chain there's an
intermediate certificate which is called
the document signing certificate the DSC
which is essentially signing directly
the data that DSC is directly in the
chip of the passport nearly all the
time there was exception and then you
have the root certificate which is
actually the source of trust the root of
trust which is that the certificate that
signed the intermediary certificate and
that is a kind of certificate you can
maybe get from the government website or
a registry provided by the IAL the
organization which is the one that set
out the standard and managed by the
United Nations or sometime you may not
find it and you have to find other ways
to get it so the idea is that within our
circuits within our zeron knowledge
circuit so in Noir we do the
verification of those two signatures
which allows us to prove the that those
data were signed by the state and then
attest the validity and authenticity of
the
document uh and the way we organize our
circuit is that we divide it in sub
circuits we don't want to have like a
single big circuits because otherwise we
would have too many constraints which
would blow up the memory consumption and
memory consumption is very important on
mobile so we need to Res to restrict it
so we have four main
subcircuits one that will verify the
signature of the root certificate over
the intermediate certificate which is on
the left one that will verify the
signature over the passport data which
is the second one and then one which
will verify the um Integrity of the data
that will go back to that real quick and
then the final one which is the
disclosure so if you want to disclose
information so like when you play with
SDK this is essentially the one that's
going to dis disclose whatever you ask
for so like disclose field directly or
do a comparison of age or any kind of
like stuff you can build with the SDK so
we're trying to be very so this approach
as two Advantage so we split the circuit
in smaller circuits that can be executed
uh sequentially it may take more time to
generate the proof but at least the ram
consumption will be uh not as much so it
can actually work without making the app
crash and the second one is it makes it
quite modular which is very important in
the context of passport uh because in
this standard uh there's a lot of
flexibility in the kind of signature
algorithm that can be used so you need
to have like a specific circuit that
implements specific signature algorithm
verification so we have different
circuit for all those kind of signature
algorithm we're going to add more we
support some of them we're going to add
more over the next few weeks and few
months to support all the passport and
the idea is that you can just swap
whichever signature algorithm uh circuit
you need uh so you going to one for RSA
of different key size one for cdsa for
different curves so you can just swap it
so it's very modular um so those are the
two also means we can add new circuits
as new signature algorithms get added by
governments so yeah without changing too
much and Noir being like Noir couple
with honk and the backend B being um uh
kind of proving scheme trust is set up
every time so managing new circuits and
updating current ones is much easier
than using circom with graph 16 for
example also if anyone's trying this out
with repet and they're having issues
please just feel free to put your hand
off and I can come over and and try to
help
debug um so more details on regarding
the passport Integrity check so this is
really core to kind of Link the
signature to the data that we use to
generate the proof uh essentially the
data of the passport that we use is
mostly derived from one data group so
they call those data groups it's like
the dg1 data group one and this is
essentially the data of the MZ the
machine rable Zone the two bottom lines
you can see when you open your passport
those kind of character with the little
angular brackets that's kind of like the
field of characters so those contain
issuing country and Country of
nationality birth date expiry date
document number gender name first name
so you have most of the information that
you need from just this single data
group and this data group among all the
others so they can be up to 16 data
groups most of the time there's only
about five or six or seven uh only the
two first one are mandatory so the data
group one we just talk about the data
group two which is the photo like the
the one you see on a JPEG of your of
your yeah of your face 20 yeah like a
full jpeg like generally a couple dozen
of
kilobytes um and the rest of the other
data group you can have like the
fingerprint the iris those two DCT group
tend to be restricted so we can't
actually read them we know they're there
but we can't read them the state need to
authorize you specifically to be able to
this is where like countries would give
access to other countries they trust
yeah otherwise you know you'd be going
to airports around the world and they
just be scanning everything which is not
ideal you got a couple free form data
group as well and some other data group
including like an interesting one the 15
data group 15 that means that when you
have this data group a passport can
actually sign stuff not all countries
support this one so it's unfortunate
that would be an interesting primitive
to have it's quite powerful actually it
kind of it essentially makes these
passports into a type of hardware wallet
allowing you to sign over yeah data now
for example my passport doesn't have
this data group it uses another kind of
like it does have a private key inside
but that private key cannot sign uh
deterministic messages like challenges
it's only like uh and deterministic
stuff because some countries don't like
the idea of being able to sign whatever
you want with your passport may give too
much power to the citizens perhaps who
knows so yeah so that's unfortunate so
all those data groups uh all the data of
the data group are hatched uh
using a different kind of s within per
country again that's up to them but
generally is going to be sha 256 sha 384
or sha 512 like different varant of sha
this is all um encoded in what's called
LDS on on the passport logical data
structure and so that's the current
version that use around the world but
there's also a V2 coming out at some
point
lds2 and so LDS one supports ability to
read data but L has two supports ability
to write data as well so you can imagine
governments maybe using this so so when
you travel around instead of getting
like a physical stamp on your passport
with the ink you'd actually get like a
digital stamp that you've traveled
somewhere that that could be cool and
then you'd be able to generate Z
knowledge proofs from that data that you
know a government has attested to the
fact that you traveled through their
airport um and that could be a cool you
know use case for
that and or a privacy nightmare
depending how you look at it I
suppose though all those hashes uh then
group together and hash into a final
hash which is what is actually signed
there's some padding adding to this but
the overall idea is there so the final
Ash of all those hashes is sign and this
is what we call the sign attributes so
the E content is the Gathering of all
those hashes and then the final hash is
the S attributes and so from those sign
attributes this is since if you verify
the signature over that message and if
you why we do in our circuits is that we
go from the dig1 get all the other
hashes that are provided we group them
we we do the whole process kind of we
verify that indeed the data after being
hashed from dig1 gives back the same
message that's being signed so that way
we sure that the data we using is the
data that that was signed so that's the
data Integrity check down
here and then finally there's the
disclose subcircuit and this is where
you're actually able to generate proofs
to reveal selectively information
mostly from dg1 because that's where all
the um the interesting information lives
and so you can just do a simple um so
when you're actually specifying what it
is that you want to disclose whether
it's the first name last name uh you
know this country this kind of stuff
gender is even possible um you create
like a bite mask um and that bite mask
um combined with an actual output dg1
like the reveal dg1 in the circuit it
will reveal where there's a you know a
one uh bit or a one bit sorry just like
a0x FF and so all the characters the 93
characters of the dg1 you're revealing
selectively um information in that way
and then there's also other possible
circuits that are a bit more Dynamic
like a like a proving that you're over a
certain age so essentially you'd have as
a public input you'd have the age that
you're trying to prove that you're over
and you'd also have the current date as
a public input and then it would in the
circuit it would be responsible for
extracting out the date of birth that's
in the digi1 and then doing like a Delta
check between the current date that's a
public input and your date of birth and
that must be over the the input age the
public uh age input and that's the only
way you could generate a valid proof um
for proof over a certain age and so we
can also create new circuits in the
future because of this modular design to
to allow for disclosure yeah and so the
way we kind of make the circuit link to
each other because if you execute them
separately without any glue it doesn't
mean too much cuz you can easily cheat
like with the data you put in you can
EAS cheat which is why you need
commitment so you have like commitment
between uh each circuit so like the the
first circuit on the left which verify
the signature of the intermediate
certificate commits to the publicy of
the intermediate certificate that
commitment is checked into the second
circuit that in this it is indeed you
have the public the DC including that
commitment that was generated by the
other circuit and by commitment you can
just imagine that as like a hash over
the data that you're trying to pass to
the next circuit but then also you
obscure the values of the hash um that
called a pre-image by using this secret
so that no one can like figure out what
it was that was being passed between
circuits yep and so you have the
commitment that it's linking the two
others from the third the two the second
and the third essentially over the sign
attributes so that way you know that
that message that was verified against
the signature the message was verified
against is indeed the same you checking
the data integrated checked against so
you're sure that that data integrated
checks does match with the signature and
then the final glue is like with the
digi one so like the data group have the
data from so you want to make sure that
the data and digri check is done over
the same digi1 that you're going to
disclose so all this together makes it
so that they're all linked together you
cannot cheat the prover cannot cheat
trying to prove wrong data cuz they're
uncommitted subcircuit relationships
yeah and then we also have this idea of
the nullifier so from some of the data
from the passport we derive a a private
nullifier call it secret yes we're
calling a secret nullifier here but
private nullifier is also possible and
we the reason maybe we could change this
to private is because the government may
know probably knows the data on that
passport so while it's private and not
something you're sharing around publicly
there is an incent may know so we call
it the private nullifier and so that n
that information is also um added with
ass salt a private salt that's generated
by the user on his mobile phone so that
allows to add some Randomness to it and
and allows for full privacy so even the
government knows the passport data they
can no longer deterministically find the
actual nullifier because you've obscured
it with his salt and that's important
and the actual final Notifier that's
revealed
to the service is scoped uh to the
domain name of the Service Plus another
Subs scope that allows the service like
so essentially the service is like the
developer that's asking a request of
data from the passport of the user it
allows it to essentially restrict a
specific use case you could have like a
Subs scope name voting a sub scope name
like you know poll ID
scope itself we use the domain name um
so that's the same domain name that must
match on the website you're
and so in the QR code that's also
encoded which is why the request comes
up so quickly but you're actually the
client side app is actually also
checking that that is indeed the correct
um domain name so you can't just spoof
some other service's domain name which
is also quite
important yeah so and essentially that
pretty much wrapped it up just to
clarify the the reason for the service
scope and why this is important if you
just use the same nullifier that was
Global um it it'd be easier obviously
but it means that if I were to use you
know service a over here and I would a
vote in some kind of poll that would be
NF fire that would be used to ensure I
don't double vote and then if I were to
go to service B over here and vote there
they could easily compare or maybe it's
public even and see that I actually am
the same person that use these two
different services so the service scope
allows for privacy between different
services and then again the subs scope
even more privacy that's more granular
should we um open up some
questions yeah I guess I can open up
some question did um anyone oh
wait it didn't
well uh stuff that makes the possible
but productionizing it is what I think
is like happening now that hasn't been
happening like before now so I'm
interested about actually the toolkit
for hunk and like the client the either
mobile or or desktop side proving that
like is performant what are the what are
the tools that you're using for that for
home proving on mobile sure whatever
whatever you're proving so originally
like bber didn't work well mobile so we
worked on some mobile tooling uh for
generating the proof using hon on mobile
so like essentially the way it works is
that we have uh bindings to the b b c
plus Coast base the back end used by
honk uh in Rust and those bindings we
use them into a library that allows us
to Jin the proof um for any kind of
targets actually works on Mac OS as well
but then we optimize it for IOS and
Android and that Rose code we bind we
Bridge it to Swift and cotlin on IOS and
Android respectively which our own app
is in react native we then link that to
the JavaScript code uh so that's a lot
of bridging all the way from C++ to
JavaScript and the iOS library is called
SWA that we built out to use this on
mobile um and so it's a portmanto of
Swift and Noir SW yeah the other one is
called Noir Android or Noir Droid still
deciding on the name I'm not sure which
one is better maybe you have an opinion
not
sure but that's the general idea awesome
thank
you uh so we get some question here
regarding the age one I I saw uh about a
government using a particular type of um
age verification I think this is just
generally speaking this works really
well for ageg gating you know adult we
or gambling websites because essentially
you've got a government somewhere
attesting to this information about the
citizens of the country and then you can
use zero knowledge proofs so whether
it's an e passport or some other system
you can use zero knowledge proofs here
with our system to just prove that
you're over 18 uh and reveal nothing
else so whether it's their system that
they use or this um I think it's it's a
wonderful solution I can't think of a
better solution than
that um so I believe the two bottom
question ours right the two bottom ones
what was it like oh no okay there's more
than imag
okay which
one
oh oh There was a question about
difference between op passport and ZK
passport um I'm going to cover this real
quick I think this been ask in a panel
as well where Michael and Flor were
speaking so yeah projects are quite
similar uh we cover like a similar idea
so they use circom originally for their
circuit they are mostly supported by PSC
from the etherum foundation uh we are
more uh we kind of use Noir from the
get-go we did use circum at some point
to get things working especially for the
defon integration at the time Noir was
not stable enough for us but now it is
so we are fully using Noir like complet
whatsoever normal Zed key um so the
difference is uh we tend to put a lot of
focus on um
I would say UI and ux and also a little
bit of devx because we want to have like
a good SDK and everything so like right
now what we U you so is a typescript SDK
strongly typed but what's coming up in
the next few weeks or few months it will
be a react SDK so the idea of that is
that you have a single component you
plug it in no no API key you set what
you want from the passport and that will
be all will take care of all the rest
the QR code generation the progress with
all the UI updates and call back with
the results so we really put a lot of
focus on that yeah and I think we're
also discussing with them something that
makes the most sense to D duplicate
effort is to actually merge the two
projects together it doesn't make sense
CU they want to switch Noir as well so
you're going to have two projects
working on with the same stack same
proving scheme same language so it makes
more sense to merge uh that's something
we're working
on a question about how can you ensure
it's not um like forged you'd have to
actually break like RSA encryption for
that to be the case so you can
be you can have uh the the assurance
that it's genuine unforged uh passport
proof because of the cypography
involved
the oh and that's a great question yeah
about the the last one here is there
anything done to address the I borrowed
my friend's passport
issue so the way that we can solve this
we'll be doing this quite soon actually
as a feature we're going to build up is
you can generate a face fingerprint from
the photo the Peg on the passport that's
also been attested to by the government
so you can trust it and then we'll have
the users uh with their iPhone they'll
they'll scan their face all local I
leaves the device you scan your face
it'll derive a face fingerprint from
that that's going to be you have the
guarantee of the te on the the iPhone so
it's a trusted execution environment and
we can use the Apper test service to
ensure that so in other words you know
it's our code running that dve the face
fingerprint um and not a like a
Jailbreaker in iPhone and then you can
compare those two face fingerprints in
zero knowledge to prove that you are the
same person that's scanning the passport
that is also on the passport which I
think is just magic that that's pretty
cool to be able to do that to a service
like provide that to a
service yeah I did
already okay um so we got a question how
will this affect kyc requirements if
none of your personal information is
passed onto the service provider uh yes
so this is often a requirement for AML
and CTF in many countries that you
should be able to give out the
information in case of a suspicion of
Fraud and like or money laundering or
terrorism financing so yes it might be a
bit of an issue for full kyc uh if you
have like full self custodial um
identity um but I believe that with
blockchain where we have like more of a
gray area we have an opportunity to
nurge into a different direction so and
actually that's probably where we're
heading with obsidian uh the wallet
we're building on Aztec so Aztec is a
privacy preserving layer to for ethereum
um so using Noir as the smart contract
language and the idea of obsidian is
that so it's going to be one of the
first wallet on Aztec and it's going to
integrate natively ZK passport so you're
going to have privacy compliance and
identity at the wallet level natively so
essentially we're going to be able to
provide to DBS an easy way to request
proof of identity and compliance proofs
and it's going to be very smooth for the
user it's not going going to realize it
it's going to be self custodial now
we've been kind of entertaining the idea
with circle of like a compliant usdc on
Aztec using obsidian so every time you
would make a transaction you would have
a check that would be done that would
include for example a local check
against ofac list and other sdn list so
that can cover it moderate risk not high
risk I would say so this is like
a a way toward compliance um on sh and
compliance with using self custodial
method instead of having to store the
data now yeah you're not going to be
able to use DK passwort for full kyc in
the traditional world but if we nurge in
that direction maybe the mind of
regulators can change if can see
applications into this space yeah and
the reason this works really well for a
private stable coin like usdc on aate
network is because every time you
transfer that uscc around you're
generating proofs again so you're
actually checking against the current
ofac sdn list and S country list um so
instead of it's kind of inverted a
little bit so instead of you giving that
to some provider that's checking
themselves every day you yourself are
checking just by the fact that you're
generating a proof but all privately um
and there be some other cool checks
there as well you could have like uh you
limit you provide like this super
generous limit I say 100,000 usdc per
month that is enough for like 99.99% of
people but it's going to really uh
mitigate and and prevent a lot of Bad
actors from using this with like hacked
funds that kind of stuff um and that's
going to be using the the nullifier that
you saw before and that's going to allow
you to transfer privately usdc and then
offramp if you wanted to to like a you
know to coinbase binance wherever and
not have to worry about getting your
account banned because it's like a
privacy
coin
that's
um that's it any other questions that we
haven't covered that maybe somebody
wants answer
feel free to raise your hand and we
can
yeah backround
uh where where cany the backround of the
slides oh the the slides um we can share
them with you if you like if you just
message me on telegram I can send you
them through cool ZK
Mike okay anything else you want to
cover
I think say you wanted to come something
in the slides we didn't quite get
to I think the subse was pretty much
everything on it and where's
this we'd also love to hear about any
ideas that anyone has oh we got some
questions popping up great hey um so
there was that question about the kyc
requirements are you guys aware of any
governments that are moving towards
accepting a ZK proof of a passport as
essentially the same thing as having
provided your passport yeah great
question I think a lot of this is really
sort of Uncharted Territory and so uh we
have the opportunity to get in front of
finset and speak with them that's really
a matter of just having those
conversations with with Regulators uh
and and and showing them you know
explaining how the tech works it it may
take a lot of time and effort uh but I
think once um you this new paradigm of
of Zer knowledge proofs and how it can
really uh unlock these new features um
they can see that and that it's actually
working um I think that'll really help
to to warm the government to these kind
of new approaches and there's also ways
that this can this can work offchain but
provide way more security than just a
photograph of your passport and that
whole model I think would be completely
broken it already is broken but it's
going to become more broken with the
generative AI these kind of things um
due to the fact that it's it's
unforgeable uh these these proofs are
one-time use as well so you know you
can't replay them easily and so in the
example of needing the data to to check
it maybe every you know every day
against your over sdn list for banks and
and some financial institutions that
need that kind of uh security you could
simply just have it like offchain so you
can generate a proof that reveals your
full name date of birth and Country and
maybe maybe a passport number if you
wanted to um and you might ask oh but
that's already available you know if you
send a photograph in yeah but it's a
photograph of your passport if it's a
proof it's unforgeable so they can take
that um they can have it on their server
it's never revealed publicly um and they
can do their their daily checks against
the OAC scn function lists and they have
a far increased you know um ability to
be sure that it's actually authentic and
I think yeah it's just going to take
time for governments to to start
realizing that this Tech it's it's still
very new tech it's is like bleeding edge
um to kind of warm up to
thanks um yeah and I think if anyone has
any great ideas about you know use cases
or want any help please reach out to us
on telegram uh ZK Mike or even just
Twitter please just s out to us ZK pass
support and we'd love to to reply and
yeah brainstorm some new ideas with you
guys um if you have anything think
you're building also please tweet that
out to us um and we'll like we help to
promote it and share it and also uh work
with you guys to to build out cool use
cases um and ultimately what we're
building here is is public goods open
source uh you know reputable uh identity
infrastructure for web 3 and so we want
as many projects to build on this and be
able to unlock these identity Primitives
to make use of them in really cool indry
and novel
ways and so I think um that pretty much
sums up our workshop for today so yeah
thanks everybody for coming this has
been really fun I really appreciate it
and if you guys would like some T-shirts
we have uh the last batch available in
the corner here so please help
yourselves
oh e
the e
m e
w
I for
oh for
e
h
[Laughter]
e e
o o
is for
okay and we're live welcome everybody um
my name's Andrew I'm with zerox Park um
and I'm here to tell talk to you a
little bit about pods um how many here
have been using pods this
week uh I think the answer should be
everyone because you got into the
building somehow
um and that actually required one so
what are pods um so your Devcon ticket
is a pod um the uh proof of attendance
to this talk that you can claim um from
the Q&amp;A app that's up on the screen
there right now if you're in the room I
don't think this work works remly that's
also a pod um some of you have been
playing frog crypto this week I see some
frog hats out there um all those frogs
are pods um a pod really can be anything
could be a secret message it can be your
identity credentials it could be your
driver's license um if we get any
governments involved to actually do this
um it can it's cryptographic data of any
sort um so what is the Pod framework so
pod is is a technology a framework that
makes it easy for apps to issue
cryptographic data and to make ZK proofs
about that data it's a data format
that's optimized for efficient proving
it's a standard um of how that data
format can be sent around and and things
can be proven about it and it's a
framework with some developer sdks um
check out our documentation site I'll
have a link at the end um if you want to
try try it out um it's mostly in
typescript but can be used on other
platforms as well we have we have ports
in a few other languages um so I'm
hoping some of you will uh get some use
out of it um so one last WTF is zero
knowledge proofs how many people here
have used ZK proofs before I feel like
you understand them okay a few um it's
kind of it's kind of obscure technology
that's kind of the point of PODS is to
make it easier to use so you don't have
to understand how the underlying math
works but in brief a ZK proof lets you
prove the validity of any private data
or any computation on your private data
without revealing that private data
itself um and that proof is trustworthy
because there's some math that basically
you can only calculate if you did it
validly um at xerx Park we think of ZK
proofs as a universal cryptographic
adapter basically I've got lots of
different kinds of private data by doing
computations on that data in a
verifiable way I can present to somebody
whatever I want that is uh validly
proven from that data the example in
this diagram which you'll find in in our
blog post is like what if I could
calculate my own credit score from
signed data I got from my bank or from
the IRS I don't need to ask a credit
reporting company to gather all this
stuff together I can gather it myself
and I can make a provable statement
about what my credit course score is and
apply for a loan um this is part of the
vision of something we call the parket
programmable cryptography internet um
which we think is going to be you know
much better once programmable
cryptography Cates on um in all these
ways uh ZK proofs are a big part of this
but it's only the beginning um see the
the other talks being given by my
colleagues this week also we have a
whole day CLS tomorrow about programable
cryptography but today we're going to be
focused on ZK proofs and what pods let
you do with them so this is the Pod
ecosystem that we envision uh right you
need issuers who are issuing this
cryptographic data they're mostly using
a private key to sign it those takes the
form of attestations which users
themselves can hold on to they they hold
on to their own private data they don't
need an intermediary um at some point
some consumer asks the user please prove
something about yourself your identity
your age the fact that you went to
Devcon things like that and then the
consumer can generate a ZK proof and
send sorry the user can send the ZK
proof to the consumer who can verify
that proof um they do need that third
arrow in the diagram um which is a
little bit of knowledge about who the
attester is you know need at the very
least to know that that attester has a
public key that you should trust um
there might also be things like what is
the event ID that represents Devcon on a
ticket things like that um but that kind
of completes the
diagram okay so what are we doing this
so I I work with the the team that
builds zup pass you've all been using
that to check into Devcon um and we
believe that the best learning on this
kind of Technology comes from contact
with reality uh meaning we want real
users to try this we want to do it at
scale there are 12,000 people at devcom
this week who who are stress testing zoo
pass for us thank you I'm sorry if the
performance has not always been as great
but it seems to be standing up um and we
want to use these opportunities to
onboard new users by bridging data that
is not ZK friend friendly into our ZK
friendly World um and take advantage of
people who are willing to be early
adopters like the crypto
community so by bridging what I mean is
we're bringing data in in the red boxes
on this diagram into the green World red
in my diagrams of this talk and the next
one um means like non ZK friendly
systems whereas green means ZK friendly
systems we can Bridge it in we can then
issue it like your Devcon ticket which
is loaded from a database that isn't
cryptographically signed um and then you
can the verifiers can gate you into
another system like Telegram in order to
join the the Devcon chat group all that
is working today um in order to bring
this in front of the most users we do
have to accept some constraints so we're
not using the most cuted edge of ZK
Technologies um we want everyone to be
able to use it which means we've built a
mobile friendly web app um which means
everything we do has to run in a browser
on a phone even an older phone even on a
a bad Network when the Wi-Fi is
overloaded at the conference um that so
that became a bit of a mantra when was
building some of these Technologies like
there's a lot of cool ZK technology out
there that is great but it needs to run
on a big backend server and I don't have
one of those when I'm in a browser on a
phone so we got to use tried and true
Technologies uh for people who are in
the know we use circom and gr 16 you may
or not may not have heard of those but
that's kind of the underlying technology
they've been around for quite a few
years so they're pretty well battle
tested at this point um so I want to
talk a little bit about the systems we
built along the way so this is what zup
pass ticketing looked like a year ago at
Dev connect when we were in Istanbul um
so it's the same triangle that you've
seen here um we were pulling data out of
preck and issuing the tickets uh we used
a format called an EDSA ticket that's a
assigned piece of data but it's not a
pod which I'll explain a little bit
later and then we had a a proving
circuit where you could prove your your
ticket you could reveal some Fields you
can prove that you you owned it Etc um
so what did it take us to build this um
don't pay attention to all the details
here but look at the line counts on
these PRS when we wrote these things um
it's pretty large that's quite a few
lines of code that it took and there's
uh in just the ZK proof there's about
there that not including tests and
documentation so it's kind of
complicated um so that was the first
thing we built the second thing we built
was frog crypto um the first version
last year which used a very similar data
format so frogs were issued by the
server as what was called an EDSA frog
uh very similar for format to tickets
and then you could make a proof about it
you could present it to our zcat
telegram bot who would let you into the
secret frog holders chat this all
happened last year in Istanbul um so
what did it take to build that um it
turns out it was very similar there was
a lot of duplication of effort there was
a lot of like similar patterns but you
couldn't actually reuse the underlying
data um so there clearly is a pattern
here right we want to issue some signed
data we want someone to request a proof
and then to be given a proof of that
signed data but it turned out that each
time we had to build it we had to
rewrite a whole bunch of code in order
to customize it so I'm an engineer I
don't like this kind of complexity I'd
rather do things once because I'm lazy
so why is this so hard um so the signed
data part the EDSA PCD that we were
using as our underlying data format uses
a fixed size hash it hashes 16 numbers
in an array um and therefore every new
data type that we want to put in there
we had to do some custom coding to
decide how those numbers in that array
go together to make this data type um I
would analogize this to imagine you were
like processing all your data in a hex
editor directly as bytes it's kind of
inconvenient we have better tools than
that now um and on the proof side ZK
circuits are a little bit awkward to
program like they don't use a normal
programming model you don't write it in
in a language you're used to um every
variable is what's called a field
element this is a mathematical concept
there's a it's a very big number modulo
some big prime number um and you've got
to like write equations on those field
elements so it's kind of complicated and
also once you build a ZK circuit it's
very fixed in order for the prover and
verifier to to agree on what's uh valid
the circuit can't change very much it's
hard to you have to publish a whole new
circuit um so that makes this a bit bit
hard I would analogize this again to in
the hardware world this is like an Asic
it's a chip that does one thing it might
do it very well but it still only does
one thing and every time you want to do
another thing you got to build a whole
new chip it's kind of
inconvenient um so what do we need here
well what we'd really like to have is
what's called a zbm basically if you
have an Asic and you want something more
General why don't you use a CPU um and
there is technology out there that lets
you basically write code run it inside
of a ZK circuit and validate that this
is the correct output um it's great some
other people are giving talks about it
this week um but unfortunately for our
situation it's a little bit too much
like I said my Mantra has to work in a
browser on a phone ZK VMS are pretty big
right now um you're not going to be able
to do that on an older phone in a few
seconds so we have to do something a
little bit more uh limited than that um
but again I'm an engineer I like uh
working within constraints and coming up
with clever Solutions um so here's what
we came up with um so on the data side
um finally going to explain to you what
a pod is at some level um so a pod is
just a collection of names and values
think of it like a Json uh object um
except that it's flat there's no
hierarchy of nested objects just names
and values um it can have multiple data
types in it for those values um the data
is then cryptographically assigned in a
way that makes it easy to make proofs
about it and I'm going to get into more
of that a little bit later um also I
forgot to mention this at the beginning
we are having a deep dive session after
this intro session so stick around for
that if you want lots more detail um but
I'll get I'll give you what I can in the
next uh 15 minutes um the on the proof
side we also can generalize we have what
we call a general purpose circuit um
which means rather than having a fully
uh CPU like circuit in a zkm or having
the Asic fix circuit we can do something
in between I would analogize it more to
an fpga right we've got some logic block
we call them modules you can feed in
some inputs to your circuit in order to
decide how those logic blocks are
connected to each other and make a
different proof every time using the
same circuit uh we call this framework
GPC for general purpose circuit um and
in addition to the circuits individually
being configurable we pre-compile a set
of circuits in what we call a family at
different sizes with different sets of
modules so when you want to make a proof
you can pick the circuit in the family
that has enough modules for what you
want and not any more because having
bigger circuit means more time to prove
more memory Etc so you can make the
right trade-offs there so with that we
get the generalized version of the ZK
ecosystem where every issuer is issuing
pods they might contain very different
kinds of data might be a frog might be a
driver's license but it's still a pod
and then when you make proofs about it
you can freely decide what you want to
prove and uh write a configuration to
represent that
proof um so with that in mind at this
point what is a pod so a pod is a data
format that makes ZK proofs easy um it's
a key value store it's going to be
hashed and signed in a very specific way
involving a Merkel tree which I can
explain more of later um and it's
optimized for efficient CK proving um
here's an example of a pod um so we've
got some names and values um most of
these are are very straightforward so
I'm not going to go through them all in
detail the one that's may be a little
bit interesting is the card holder this
is meant to look like a driver's license
in some you know fictional country uh
the card holder is my semaphor ID this
is what pass uses to identify you it's
really a public private key pair um so
the public key is what's going to go in
the Pod to say that this is my pod or in
this case this is my driver's license um
what you see on the right is the Json
format for this it's optimized to be a
little bit tur and also human readable
so things that don't need a type
annotation you'll notice don't have them
because the Json type itself is enough
data um for that um once you get down to
actually building the Merkel tree like
everything does have a type but in this
uh table I call them type hints because
the type is not part of the
cryptographic data instead it is
guidance to how do I hash this data into
a piece of uh cryptographically
verifiable data um more on that later so
the first thing I do to make this into a
pod is I build a Merkel tree U I'm not
going to go into detail on that but
basically you arrange the elements into
a tree you hash them all together until
you get to a root um and that root is
what we call a Content ID uh the content
ID is derived from the data so if you
have the same data you can derive the
Content ID regardless of how it was
formatted in Json um one detail that you
might notice on the right is that the
the names have been alphabetized that's
how we make sure that it is
deterministic and you always get the
same content ID uh but everything else
is just
hashing um and then now once I've got
the content ID that's the thing that I
sign so if I'm an issuer and I want to
issue a pod first I get the data I meriz
it I get a Content ID and then I just
write a signature on that Content ID and
that's enough to validate that the
entire pod is valid
so uh we have a a ZK friendly data
format we'd probably like to do some ZK
proving on it um so let's talk about the
GPC side of this that is what you lets
you do that um as I mentioned earlier ZK
gpcs are circuits made of reusable
modules um as well as a family of
multiple circuits so you can pick the
size that you want um let's look at what
that looks like um so this is an example
of a GPC configuration this is how you
say what do I want to prove um and
you're going to present this as this
Json object that says what you want to
Pro Pro and the system is going to do
the rest compiling this down to what to
do with the circuit so here's a very
minimal proof um I'm going to try and
prove that I have a driver's license
that says I'm allowed to drive right so
I my configuration says I have a pod I'm
going to call it ID card this is
actually an arbitrary name that's just
part of the configuration to refer to it
later um it has some entries and one of
those entries is driver that is not an
arbitrary name that's a name that was in
the Pod and is going to be hashed and
checked um and what do I want to do with
it well I want to reveal it so is reveal
is true
means this is a proof it's going to
proof that I have a pod that it contains
this entry and it's going to reveal that
its value is hopefully true because I'm
going to try and drive a
car um so that's simple enough there's
one detail that wasn't on the previous
slide um that because it's done by
default so I didn't need to include it
in the config but it's important to talk
about um what I proved if I don't have
think about the signer key is I just
proved that I have a pod containing the
word driver with the value true that
doesn't mean it's actually a driver's
license um in order to do that you got
got to do something cryptographic so the
way the easiest way to do that is you
check that the Pod was signed by a
public key that is well known um that
might be the government of California
which is where I live um hopefully we'll
get them to issue pods eventually uh but
that is implicit like the signing key is
also always revealed by default but you
can choose to not reveal it if you want
to um in which case you can constrain it
in other ways you might constrain it to
be equal to some other element without
uh actually revealing it or constraint
it to be a member of a list like maybe I
have a list of all the signing keys of
the 50 US states um and I just want to
prove I have a driver's license from one
of them I don't want to tell you which
one okay let's get starting to get a
little bit more complicated um so I've
proven that I have a driver's license
that says driver equals true I haven't
actually proven that it's my driver's
license yet um I could have stolen
somebody else's the thing is that pods
because they're just data they are
transferable I can copy them um the way
we make a pod bound to a single user is
by putting that user's uh public key in
it which we I should earlier when we
were looking at the entries um and the
way you prove that you are that user is
you make a proof that you hold the
private key that corresponds to that
public key um and the way you say that
in the Z GPC config is this is owner ID
field you say is owner ID and I give the
type of of uh public key I'm using which
is semor version 4 from our friends at
psse um and that basically means that
this proof is going to be configured to
check that I have the right private key
which is in my private inputs um and it
this case it's not even going to reveal
what my public key is just that I own
this pod and this pod says I can
drive okay let's get to a little bit
more ZK and hiding some more data um
instead of proving that I'm a driver
what if I just want to prove I'm over 21
um maybe I want to go buy some some
alcohol um I don't know what the age is
in Thailand but back home it's 21 um so
I can just say I have a pod containing a
entry called date of birth um that entry
is not going to be revealed but it's
going to be in this range and that's the
numeric range for the date that is 21
years ago um we should make this more
friendly and let you just pass in a date
object but for now it's a number uh so
this is a proof that I am over over 21
and that I own this pod I didn't take
out that that field but everything else
is is not revealed and I'm being very
Anonymous um one last example uh we can
make proofs of multiple Pods at once if
we have a circuit with enough modules so
here's one that I'm proving I'm over 21
and also proving that I have a ticket um
to an event that maybe I'm going to go
to an after party after Devcon um and in
this case the ticket I'm proving that it
its attendee name is the same as the
name in my driver's license um I'm
proving that I own it and I'm also
proving that uh the event ID of that
ticket is in a valid list I'm not
revealing what I have a ticket to but
it's in a maybe a list of like Devcon
related events that are happening in uh
in Thailand this week uh so this is kind
of a a minimal Anonymous way of checking
into a party of course if I'm there in
person I'm revealing some more about
myself by being there but you get the
idea okay so last piece of of this I've
now configured my proof I've decided
what I want to prove how do I actually
make a proof um and all of this is an
example of what you can do with the the
GPC libraries um so the three things I
need in order to make a proof one of
them is the proof config that I've
already given you some examples of uh
the second thing is the inputs that's
the actual pods um which I need to have
in order to make proofs about them there
are also other inputs like my private
key uh or like that list of valid uh
event IDs that I want to prove that my
event ID is one of those are all inputs
uh the third thing I have to feed in is
something called an artifact path um
that is where do we find the binaries
that that generate that know how to
generate this circuit so when a ZK
circuit is compiled it generates a
proving key a verification key and also
a witness generator don't worry about
what those are but there's some like big
binary things that the prover and
verifier have to agree with um we
distribute these via npm we also put
them on various CDN you can download
them so you have to just decide for your
app are you going to download them put
them on disk give a path to them are you
going to download them from a URL there
options um once you've got these things
together the GPC proof function will
generate the proof like it puts together
that configuration it picks a circuit
that fits that configuration with enough
modules it downloads the corresponding
artifacts for that circuit um and it
generates the proof um and then the last
thing it does oh I should have gone to
the next slide here we go um so it needs
to compile down all those inputs into
circuit signals that can feed into the
actual ZK circuit um which are you know
mathematical field elements as I
mentioned and then after it's done and
it gets a valid proof it will decompile
some of the outputs and turn them into
What's called the revealed claims object
um so it comes out of a proof you've got
the actual mathematical proof that's
just opaque numbers that are needed by
the verifier that's the actual ZK part
um you've got a bound config which is
exactly like the configuration that you
fed in uh except that now it contains
the identifier of the circuit that was
selected so that the verifier knows how
to verify it correctly and then you got
the revealed claims if I revealed that
uh I am a licensed driver driver equals
true that would be in this object um if
I revealed like my name Etc that would
be here and that's what the decompiling
is for it's taking the circuit outputs
and turning them back into a string or
whatever the the representative uh thing
is okay so those three things are
exactly what I should send to a verifier
um whoever I'm going to prove this to um
they need those three things they also
need an artifact path to download the
corresponding verification key um and
then they can verify the proof um they
just do very much the same thing they're
going to compile some of those inputs
back down into uh into ZK land where
there are circuit signals they're going
to verify the proof and they're going to
say yes or no whether it's valid uh and
you know gravy we're at the we're at the
end and hopefully everything went right
and I've proven what I wanted to prove
to you um so final takeaways summary of
of what this was a bit of a speedrun
through um so pods are data that's
designed to be prove proven about um any
pod is a signed ad adastation of
something um whether it's I have a
ticket whether it's I have a driver's
license Etc um gpcs allow you to
flexibly make proofs about those pods by
using modular circuits which can be
configured using a a Json like
configuration language uh and you can
Auto the system will Auto Select the
circuit that you need depending on your
configuration so all your app needs to
do is say please make me a proof of this
with these inputs and everything else is
handled for you um and then the last
step is the the verifier verifies the
proof and then the apps have to do have
to decide what things they trust how do
you trust that this is the correct proof
um like I alluded to before you should
check that this uh ID card was actually
signed by the government you should know
the the public key or you should know
the event ID for Devcon um you should
also check and I'll tell say a little
more about this in the de Deep dive that
like the configuration that was sent to
you was actually the configuration you
asked for because you don't want the
prover to say oh I have a proof of
something but not necessarily the thing
you asked for that's something that you
should check as well um but once you do
all of that like this end to end should
be should be very solid and you should
be getting the information you
need okay uh that's it for the the
speedrun intro um please check out our
documentation uh they're on.org that
just went live yesterday um and also
there's a link that just went by t.me
zass to join the telegram group uh and
yeah let's go do some uh Q&amp;A
all right uh where do you store the s
for identity secret for users in zpass
so that's all client side um zup pass
stores all of your private private data
client side um the zup pass server is
aware of your public key because that's
how it can make sure that you get issued
the right Devcon tickets and things like
that um but yeah zpass is a is a client
side cryptographic data
manager to what extent is POD an open
data standard um so I can consider it
open um we haven't like uh published a
spec for it I should work on that um but
all of our code is open source so people
can do interoperability with it um the
Pod format itself is very generic and
interoperable it's the GPC compiler that
uh turns a pod into this specifics of
what you need to prove with a specific
GPC so the gpcs are kind of less
standard and generic though they also
could be used on multiple platforms we
haven't we do have an example of GPC
verification on chain um that just
started working couple days ago so all
that is possible outside of a browser um
but we don't have as many examples there
as we do on the on the Pod
data can we can we scroll down is there
anything more uh can you compare pod to
verifiable credential yes uh this is
something I looked into um pod is
simpler it doesn't really have a a fixed
schema or anything uh that uh that like
ties it into a specific standard you
could put uh Json LD based verifiable
credential data in a pod if you wanted
to um but a pod is much more flexible um
at the cryptographic level there is a
difference in the kind of Merkel tree we
use um the Pod uh uses the lean IMT
which is something that semaphore uh
created which is much shallower because
pods tend to be relatively small um as
opposed to the sparse merkl tree that uh
is used at least for the implementation
of rare bio credentials that I'm aware
of which is the one from Iden 3 um that
is a much deeper Merkel tree but it can
do things like prove abs of an entry
which pods can't
do uh okay what else do we
have how frequent is POD refresh uh very
frequent so far but we're hoping to keep
it uh much more stable after de Devcon I
don't have a strong answer to that uh
what
else uh how do you convert Json to a
Merkel tree please stick around for the
Deep dive session that's coming up I'll
tell you all about
that what else
um yeah so the in the example Pro and
verifier um the user's device can
generate the proof and that's why
everything has to work in a browser on a
phone um client side proving is
definitely the default in zup paath not
every app has to do it these are
libraries you can call them wherever you
want um there's much more difference
between verifiers whether they're doing
server side verification or client side
verification that depends what your use
case is and what you're protecting
against um are the issued credentials
signed and the proof that the crunch
oops you just we scrolled away uh uh we
do not use BSS signatures uh to verify
partial properties that's what the we
use the Merkel tree for again more
details on that coming up
um is it possible to make information in
zass portable I think that pods do make
that possible yes um as long as it's a
pod and there are uh apis for getting
data out of zup pass if you want to um
that's called the the zapi um at which
point you can take this to whatever
platform you want we have impl mtion of
pods on in Python C and rust for various
projects so it's not too hard to
do uh how do apps know whether a proof
from a verifier is U is legit um well
the framework tells you that it is a
valid proof and it will confirm for you
that this configuration and these
revealed claims and this proof match up
and are valid so the prover couldn't
have Have Cheated about that um what
they could cheat about is app level
semantics so if you asked for a proof of
a driver's license and I sent you a
proof of a frog instead um that's
something that the framework can't tell
you because it just says that's a valid
proof so you do have to check is that
the configure I asked for um is the
signing signer of this driver's license
the the government Etc um yeah that's
the that's the kind of level of of
verification you
get okay I think that's
it can we go back to the slides briefly
okay go those of you who are collecting
frogs I've got something for you if we
can switch back to my slides oh yeah
we'll leave that up for a minute or two
I think we've got uh like three minutes
before the next session starts anyway so
uh feel free to to frog away
okay and as I said we're going to go
straight into a deep dive session U
which is going to be 90 minutes we
probably won't use the whole thing but
that's what we're scheduled for um so
seek around if you want more details to
answer any of those questions
all right thank you again everyone uh
thanks for everyone who stuck around for
the Deep dive session um I know these
are being recorded So anyone who's
watching this session online you may
want to go back to that one first it'll
give a a more gental introduction um
this session should be a little bit less
rushed because we have a bit more time
but you know it's definitely going to
get a little more Technical and I hope I
can answer some of the questions that uh
you may have had after the first session
um so we're going to cover two things um
I'm going to do a deep dive into how
pods work how we build them into a
Merkel tree what makes them provable um
and then how that kind of proof comp
proof compilation step uh happens that
turns things into a circuit uh and then
my colleague Ahmad over here is going to
take over and talk to you a little bit
about the actual circuits underneath
that how we make them modular how we
make them uh make the these very
flexible
proofs okay so let's review very briefly
so we're building this e pod ecosystem
um where issuers issue credentials or
add a stations um that may have come
from some non-z friendly data source
outside of our uh ecosystem um such as
like the preti database that Devcon
tickets come from um you're going to
hold them uh in zass or somewhere else
uh you can use pods in whatever app you
want zup pass is optional um but we let
users hold their own data um and then
that that user can in response to a
request make a uh proof about that data
in order to prove you know I'm a
licensed driver I'm over 21 I have a
ticket to Devcon Etc um so this is what
we're trying to enable um so pod is a
data format that makes ZK proofs easy um
we use merization or rather we build a
Merkel tree I don't know if merization
is actually a word but I will continue
to use it um we do it in a deterministic
and repeatable way and we use this data
structure so that individual entries are
easy to make proofs about without having
to prove every entry of the Pod at once
and I'm going to in this session go a
lot deeper on how that works um the
other thing that makes this easily
provable is we use ZK friendly
Primitives um all of the underlying math
is based on uh the baby Jubjub Prime
field that's those like prime numbers
that were uh or numbers modulo a a prime
number that I referred to earlier um we
use a Poseidon hash and an EDSA signing
um these are two algorithms that can
operate over this uh baby Jubjub Prime
field um and the proof compiler plays an
in important role which is that there
are some things that are not ZK friendly
to verify but as long as they are public
and be verified can be verified by the
verifier directly um they don't have to
be in the circuit um and I'll show you a
little bit more about how we make that
work um so a reminder of what a pod
looks like I've now I've cut this pod
down to only three entries just so that
everything fits on the slide but it's
otherwise the same as the driver's
license I showed you before it's got a
name it's got a date of birth um and
it's got the public key of the card hold
um so how do I sign this in a ZK
friendly way like right the normal way
you would sign a Json you have to if you
have to just sign it like a string um
and you have to be very careful that
it's all in the same order otherwise
your signatures is wrong um so we've got
a better way in pods that makes it much
more provable so what I'm going to start
with is I'm going to take all those
entries and the first thing I'm going to
do is I'm going to alphabetize them um
to make sure that they're always in the
same order um entries actually come from
a pretty or entry names come from a
pretty limited character set basically
match an identifier in most programming
languages it's like asky Plus numbers
and underscores um so there isn't any
Unicode question about like what the
alphabetical order is it's pretty clear
um so we do that we put the names in the
values adjacent and then we hash them
all um and in this diagram um and in the
future diagrams green is something that
is ZK friendly I can do it inside of a
circuit if I want to Red is something
that is not ZK friendly I can't do it
inside of a circuit at least not
efficiently not in a browser on a phone
um there are certainly ways of doing
non-z friendly things in circuits
they're just really big circuits so all
the name hashes and any of the string
values that I want to Hash I'm using uh
Shaw 256 that's not a ZK friendly hash
function so that means that those
strings are going to be represented in a
circuit only by their hash not by the
actual string because the circuit can't
repeat the the hashing um I mean that
wouldn't be very CK friendly anyway
because strings are variable variable
size and ZK circuits don't like variable
size things um but this is the approach
that we've taken um the green P's here
that's the Poseidon hash so uh a date is
a number so I can use the Poseidon hash
function to make a hash that is ZK
friendly um the same is true of the
public key a public key is actually two
members so the the P here is actually a
two input posid and hash rather than a
one input besid in hash the diagram is
lying a little bit but it's still ZK
friendly it's something that I could
verif verify in a circuit later if I
want to okay that's step one I haven't
built a tree yet I've just done a bunch
of hashing so let's start building a
tree um we're going to Hash together the
adjacent elements um that means that the
name and value that correspond to each
other are always hashed together to get
a new value these ABCs at the top those
are just the hash that results in
hashing together the previous two hashes
um okay so we're starting to look a
little bit like a tree let's keep
going next level up I'm just going to
keep hashing together adjacent elements
this is a pretty standard Merkel tree um
there is an open question here of like
what do I do when my tree isn't a
multiple of or a power of two um the way
we do that in our the particular version
of the mer Merkle tree we use is we just
skip that level so when we go up to the
next level we just take that value C we
feed it up to the next level unchanged
um this is a data structure called a
lean IMT IMT standing for incremental
Merkel tree um it was built for
semaphore uh by the psse team and we're
just reusing it here um it is a very
lightweight Merkel tree and works
particularly well for small trees um
most pods uh right now are less than 16
elements or you know less than 32
elements you can go as big as you want
but the circuit's just got a little bit
bigger with the depth of the tree so the
lean IMT help works very well and very
efficiently for small trees um okay so
now that we've gotten to the top we've
done all these hashes we've got one hash
and that's called the Merkel root um in
uh Merkel trees that's a thing that you
might publish to prove that you're a
member of a group for instance um in the
case of PODS we call that Merkel rout a
Content ID and that's the the thing that
I mentioned earlier is going to
represent this pod the same content put
through this same process will always
generate the same content ID so we we
make this a first class concept that
like you know what the pod's content is
this is its hash
essentially now that we got the content
ID um that's when we can actually sign
it and as I mentioned earlier the
content ID is actually the thing that's
signed um you're not feeding in the the
names and values directly to any
signature algorithm you're just doing
this merization and then feeding the
content ID into the signature algorithm
um you're also going to feed in your
private key if you're the issuer and
you're going to get out of signature um
EDSA signing you notice that that's kind
of a gradient between green and red um
it is a ZK friendly signature scheme but
it turns out that there's a key
generation phase in the signing step
that isn't ZK friendly so from your
private key it's actually hard to
generate a signature in a ZK circuit
that's not usually a problem for us
because all you need to do is verify it
like if you ever wanted to do the ZK
Circuit of equivalent of signing you
would just sign outside and then stick
the signature in and verify it in the
circuit and you're good anyway but I'm
trying to be correct about my color
coding here because I'm That Kind of
pedantic Okay so we've got this thing
that represents the entire pod um how do
I prove one one entry of that pod that's
the thing I most often want to do in one
of my ZK circuits so this is what Merkel
trees are for if you've seen them before
um this is called a a technique called a
Merkel membership proof that if I want
to prove that I have this entry called
Data birth um all I I don't have to give
you the whole tree I just have to give
you uh the path up the tree and give you
the sibling that corresponds to the rest
of the tree at that level and if you're
a verifier and I give you all of the
values that are shown here but not the
ones that were deleted um you can verify
that all this is correct right you can
you can take the the name and value and
hash them you get B you can then take a
and hash it with b and get X you can
take Y which I gave you and hash it with
X to get the content ID and you can
validate the signature so here I've just
like avoided having to give you all of
the elements but you can still validate
that this is a valid pod so that's
pretty cool um let me formalize this so
this is the the standard Fields you'd
have in what's called a Merkel
membership proof or an entry proof um so
the root is the content ID the leaf we
always uh set the the name of the entry
to be the leaf that's a little bit
arbitrary um the depth in this case is
three in order to validate the proof you
have to know how deep the tree is um
we've also got what's called an index
this is telling you when you get those
siblings along the way are they coming
from the left or coming from the right
that's because our hash function where
it takes two inputs the two inputs are
not reversible uh so in order you have
to know which direction the tree goes to
go up so that's what the index is for um
you have to get those S sibling hashes
um and this is an interesting thing that
I didn't realize until I built this the
value hash that corresponds to this name
is right there in the list of siblings
so it doesn't actually have to be fed
into the circuit as a separate uh
elements it's just part of the Merkel
proof it has to be there anyway um which
I'll be useful later uh I've got the
value and then I've got my public key in
my signature for verifying um so this is
a this is what's called a Merkel proof
um it's not a ZK proof um when I built
this I initially thought oh well if all
you have to do is prove one element of a
pod one entry I should say because
that's the word we use um I could just
send you the Merle proof and I don't
have to make a ZK proof at all wouldn't
that be easier it's certainly a lot
cheaper um anyone here
have an idea of why I can't do that why
it would be a bad idea why it might be
unsafe uh well I mean disclosing the
signature doesn't necessarily obviously
mean that uh I'm disclosing anything
like what would the attack be can you
can you answer
that oh yeah the siblings yes so what
would you do with that if you were an
attacker yeah precisely so these are
hashes it's hard to reverse a hash but
if the values themselves come from a
relatively small set you can use a hash
to try and guess what the value is right
so this is much like a rainbow table
attack on a uh on a password list like
if you leak the hash of something it is
much easier to find out what that thing
is than if you don't add that hash so
that's why we don't use usually send
these Merkel treat uh proofs around
directly outside of a of a circuit thank
you for that um and that was something I
actually learned while building this I'm
like oh that would be easier wouldn't it
well it's easier because it's non-secure
as it turns out unfortunately um so the
next step here is we put this inside of
a snark so now instead of drawing a
diagram of like the work I do in my code
this is now a diagram of an actual ZK
circuit um but it's very much like the
the previous one um and then on the
right side I've basically gray out all
of the fields that I'm not revealing one
of the magic things about a ZK uh proof
is that I can choose which inputs are
public and which ones are private so the
only things that have to be public are
the name hash of the leaf because you
have to know like you aren't going to
accept driver equals true if it you
don't know that the name is actually
driver so that's always public um and
then the public key that signed the Pod
has to be public so you can verify that
um with some exceptions and if you have
a more complicated circuit you don't
have to reveal that you can instead
prove that it's part of a known list or
something like that but at this level
it's always going to be public
everything else is private um did you
notice the trick that I pulled there I
feel like you should probably be asking
questions right something
disappeared um so the name hash
disappeared um that's because that's not
a ZK friendly hash have an
question uh we're not using katak we're
using sha 256 but it's also non ZK
friendly um it's because it's a string
and a string being variable length is
not going to be ZK friendly anyway um at
least within the limitations that we set
for ourselves like you can prove things
about strings there are ZK friendly ways
of hashing that um but it's not very
friendly because of the variable length
so um for Strings we always use the the
shaash um and we do it outside of the
circuit this is why or another reason
why the name of an entry always has to
be public that means that the verifier
can take the name as a string the
verifier can uh hash it using shot6 get
the get the name hash feed that into the
circuit and be confident that that hash
really does correspond to the name
driver or uh iess I guess it was Data of
birth in this example um yeah so that's
the other thing that like is important
here that there is a little bit of work
the verifier has to do outside of the
circuit they're not just going to check
the ZK proof they're going to check some
of the inputs to make sure that they
correspond usually just by hashing them
again they're not really checking so
much as recalculating
okay so the last step this is now a
proof of one element of a pod um but
it's not modular I said that GP GPC
circuits are meant to be modular well
the way I make it modular is I just
slice it up um so this in a in one of
our GPC circuits would be represented by
uh three different uh modules the object
module which proves that a Content ID is
properly signed that proves a pod um an
entry module that proves that this entry
uh or this name exists in this pod and
then a numeric value module we call it
because we can only prove the actual
value in the circuit if it's a ZK
friendly hash function which only
happens if it's a number so the numeric
value module lets you prove that the
value
exists okay let me review what we got
through all of those those diagrams um
so an object is made of entries which
are named value pairs the name and the
value are represented in the circuit by
their hash which might be a Poseidon
hash or might be a a shaash um and we
use the type hints that come in with the
data to know how to the value is it an
integer is it a date which I'm going to
convert to an integer is it a string um
is it a is it a set of bytes is it a
public key Etc um we generate a Content
ID by building a Merkel tree um and that
means that I we can make proofs about
individual parts of it um and we make a
signature on the content ID to make an
adastation um so the p and pod I usually
use it to mean provable it also can mean
another thing which is portable um one
thing that I like about the data format
that I described and the process I
described is that there's nothing in
there about like a string representation
or how you have to canonicalize it the
way you would sign a Json it's all about
math so if you can do that same math and
put get together the same content ID
then you have a pod and it's valid um
that means that while we do support a
Json format for sending pods around
because it's convenient you don't have
to use that you can save it in a binary
format you could use a uh protuff uh the
Frog crypto game has a different Json
format that's little more bit more
nicely readable for players and it all
is just as valid a
pod okay but a pod also is provable um
it allows for efficient ZK circuits
because of the the hatching function and
signature function we chose um in the ZK
circuit there's a fixed cost per pod to
validate the signature there's a fixed
cost per entry to validate the entry and
then a ZK uh snark can verify all of
this um this is the full list of value
types that we currently support it will
probably extend I'm not going to go
through all this in detail
um mainly they are what you would expect
um a few interesting details um any
value can be compared for a quality
because we just look at that hash and
can compare two value hashes together um
some values will be be equal to values
of other types for instance like the
Boolean with the value one and an
integer with the value one are actually
the same value so keep that in mind if
you're ever using uh this in your in
your uh checks um but only certain
values can be done can be compared in an
ordered way meaning less than greater
than etc those are numerical values
right you can't do a less than on a
string in a GPC circuit just because the
string is only represented by its hash
whereas for a numeric value you can
prove that oh this is the value and I
can check the hash in the circuit at
which point I can feed that value into
further logic to check greater than or
less than um but also because of the
some of the limitations of what you can
do efficiently in our particular uh
circuit language comparable things are
limited to 64 bits in our circuit that's
an aspect of the circuit we could make a
module for comparing things that were
bigger we just limited to 64 bits
whereas a cryptographic number can be
anything that fits in a field element
you'd use that for a hash but you're
probably not going to check those for
greater than or less
than okay um one last bit of detail
getting into uh how we compile down to
circuits before I hand off to Ahmad to
explain those circuits um this is the
diagram I showed before I'm not going to
go through it again um but I want to
talk a little bit more about the compile
and compile steps um that happen in this
diagram where we Bridge into the world
of ZK circuits um so your GPC is a
modular circuit it's made up of modules
that are basically sliced up the the
circuit that I showed you earlier U plus
other things like right I showed you the
object the entry and the numeric value
ahad's going to show you a lot more um
the modules are connected to each other
by passing around verified values such
as a value hash such as a name um or
such as a numeric value like those are
all examples in the previous diagrams of
a value that we fed from one module into
another um and there are public inputs
to the Circuit that say okay something
like uh uh entry module number three is
going to take its content ID input from
object module number one and that's how
you would how you would wire these
things together that say that oh the
first object that I proved has this
entry and that's and I want to make
those correspond to each other and then
it's going to validate in the circuit
that that Content ID really is the same
um so if you think in terms of Hardware
there are a bunch of like uh
multiplexers and Dem multiplexers that
are feeding things around uh if you
think in in terms of uh software it's a
bunch of like if statements essentially
um and all of those wiring signals or
configuration signals are by by
definition public um they won't be
hidden because the verifier has to send
in the same configuration to make sure
that they're verifying the same proof
okay uh and lastly as I mentioned the
GPC uh circuits come from a family we we
Val we generate circuits with different
sizes for instance a typical circuit
that we use for for Ticket proofs has
one object a Max of five entries two
numeric values on which you can do
things like less than or greater than
one list that you can check membership
in ETC um and we generate a whole family
of these things with different sizes you
can just pick the one that is cheapest
for what you need um and you have to
download the artifacts for the circuit
that you picked and this is like a vague
size range um proving artifacts are
pretty big at least on the the level of
a a proving on a mobile phone um
verification artifacts are very small so
if all you have to do is verification it
might even be reasonable to just build
all the artifacts directly into your
your app bundle but for proving you
probably don't want to do that you
probably want to put them somewhere
else okay um this kind of restatement of
this so the proof compiler takes the the
configuration takes the inputs um
including the pods the user seek private
key um and list things like lists and
tles that you can generate um uses them
to compile down to the proof outputs
using uh there we go uh the proof
compiler so what this is going to do um
much like uh a a program a language
compiler it comes in multiple phases
first thing we're going to do is check
all the inputs that they are valid uh in
by the definition um this includes some
things like range checks that are
actually important for instance if
you're going to prove that a value is in
a Range range between Min and Max our
circuits only work if Min and Max are
um because of certain assumptions that
so that means both that those numbers
are always going to be public because
they're part of the configuration but
that the prover and verifier both are
going to check that to make sure so that
they can trust the output of the circuit
um while checking the configuration the
compiler is going to determine what are
the requirements right how many modules
do I need in order to generate this
proof um it's going to pick the smallest
circuit that fits uh alternately you can
option just feed in a circuit identifier
if you want to say always pick this
circuit please because that's the one
that my verifier knows how to verify um
then it's going to hash and meriz all
the inputs following the procedure that
I showed you earlier um in order to
format them and the configuration as
input signals to the Circuit potentially
a lot of them if you've got like a list
of 200 entries and have to see feed them
all in um but usually it's in the it's
in the tens of inputs not the hundreds
um you're going to download the
artifacts uh the proving key and the
witness generator in this case so that
you can then finally generate the proof
um and then you're going to decompile
some of the circuit outputs back into uh
the uh the revealed claims um and some
of this logic actually has to bypass the
circuit right if if what I revealed was
a string and what comes out of the
circuit is that String's hash I'm going
to go look back at the inputs to get the
actual string because I can't reverse
the hash um but the prover has access to
that so you're going to just copy that
string into the revealed
claims okay um the verifier is going to
go through all these steps in a very
similar way and that's because the
verifier is double-checking that the
prover did everything right um all the
stuff that happens outside of the
circuit that is security relevant the
verifier has to repeat because you're
not trusting the prover right things
inside the circuit are being verified by
the ZK proof itself but anything outside
of that the verifier just repeats the
work including things like checking that
the bounds are within 64 bits and they
can do that and then the proof will be
fine um the only differen is which I've
called out in bold here are that the
verifier will rather than picking a
circuit it confirms that the circuit
that was selected actually fits the
inputs um it downloads the verification
key instead of the proving key which is
much smaller and then it can verify the
proof um and then as I mentioned in the
in the over intro session there is some
work to be done after the verify
compiler and the verifier is done right
the verifier tells you this is a valid
proof with this configuration you should
make sure that that's the configuration
you asked for um you might do it by just
before calling the verifier like replace
configuration the prover gave you with
the one you expected and that'll just
work you copy over the circuit
identifier to do this we have some
examples um but you might also do
something more complicated where you say
like this isn't a configuration that I
will accept it might actually be
stricter than the one I asked for it
might be slightly differently formatted
that's up to you um and then also you
should check whatever's in the revealed
claims they were revealed for a reason
presumably so you should check that
that's something you actually want to
accept and go do whatever you're going
to do with it in your
application okay uh that is it for me my
throat is feeling a little bit parched
from all this talking um so I'm going to
hand off to Ahmad now who's going to
take you into how do we actually do
what's inside of the
circuit and and he's gonna plug in his
own laptop to do
all right so we'll be going through
through gpcs in a bit more detail so
when I initially prepared this talk I
had some background slides on pods maybe
I'll do a very quick recap of what was
covered in the last couple of talks but
the tldr is that gpcs allow us to make
ZK proofs about pods so that's you know
essentially that's the point we're
trying to drive home and if you want to
look up the code on GitHub here's a QR
code to our repo so we've got a
repo um pod package GPC compiler package
GP circuits it's all in
typescript um there is an
ongoing uh let's say initiative to do
more in Rust um if you actually look for
the parket repo ZX Park parket actually
should have put the code up um then
you'll find uh the beginnings of a rust
implementation of uh much of what we've
done on the Pod side at least not the
GPC side
yet so yeah we already know pods a
cryptographically signed key value store
has anybody read the blog post by Joel
Gustafson does that ring a bell merizing
the key value store for Fun and Profit I
mean yeah this isn't an entirely new
idea but it is quite uh quite solid
cryptographically um Andrew's already
gone into detail on how you know we
meriz a pod but you basically start with
the Jason object um
you appropriately meriz it you sign the
Merk root and Bam pod so we've already
used terms like content ID so that's the
uh root hash um the signature is the
eddsa Poseidon signature associated with
the Pod um yeah and then we basically
have a series of entries so key value
pair is the name of an entry the value
of an entry so that's the terminology we
use um just to go through some examples
because I am going to talk I'm going to
show you some GPC configs corresponding
to certain examples but imagine a world
where we had pods as ID cards you know
ID cards with pods underlying them so
here would be one such
example we use Jason because Jason is
the accepted uh I guess uh data
representation format in this uh in this
world um we have various fields in our
ID pod like name date of birth semaphor
ID uh like you know public semaphore ID
um so we basically take something like
this the state would actually issue a
pod with this underlying
data and you know once a pod is
constructed you basically have the
content consisting of this part plus the
signature plus the signer signer's
public key this would be the state that
signed the ID pod um and the content ID
which is the Merkel route that can be
reconstructed in a deterministic way
because we already have conventions
about how you arrange all of these
entries ticket should have an event ID
so the event you know the tickets
associated with a product ID like uh you
know regular ticket maybe a speaker's
ticket a ticket ID to identify the
individual
person and then maybe the attendee has a
semaphore ID well the you all do via zoo
pass um so that would also be embedded
in there and in much the same way we
obtain an appropriate JavaScript object
according to the current implementation
that represents our
pod now life before pods was quite
complicated as far as ZK proofs are
concerned you'd always have to Define an
appropriate uh data structure choose
some signature scheme find a way to just
cram that data into a circuit right and
you're going to have to probably pad
things along the way do various little
ad hoc things necessary for your
application glue code and then who knows
what comes next next and eventually you
profit hopefully and that's how it was
before pods um and after pods things get
simpler so now I'm going to talk more
about the ZK side of things how we can
like um what what sorts of proofs we can
make about pods um with our GPC
framework general purpose
circuits um so basically we have a many
parameter family of reusable circuits so
depending on the proof you may or may
not need to prove about just one pod m
multiple pods maybe pods with many
entries pods with you know five entries
whatever um we need various circuits to
accommodate you know all of these
possibilities so many
parameters um and yeah each circuit has
a number of modules with a specific
purpose that I'll go into in a moment
and this is how we make ZK proofs about
pods so here are some examples that
relate back to the pods I showed you a
second ago so you could say you could
want to prove to somebody that you
possess an unredacted speakers ticket to
Prague crypto 2023 which was part of Dev
connect so as you can see I have updated
my examples but it's a Concrete example
um another proof you might want to make
is that a ticket to a Dev connect 2023
event was issued to
me um without necessarily revealing what
event and proving that you are over the
age of 18 without revealing who you are
so these are some things you might want
prove um so we can be more explicit
about what it is we're saying in each of
these examples so for the first example
you are saying I possess a ticket pod it
assigned by the organizers of the event
so for prog crypto 2023 would have been
zerox Park psse um it contains the event
ID corresponding to prag crypto
of a speaker's ticket and its ticket ID
entry value does not lie in the list of
redacted tickets right and you could
always have a field in the ticket saying
is redacted but why would you ever set
that to true so in this case there would
be some Universal list um list of
tickets that are no longer valid um and
then with the second example um that a
ticket was issued to you you would yeah
show you would say that you possess a
ticket pod it's signed by an organizer
of a Dev connect 2023 event um and it
contains an event ID coresponding to one
of those events and you actually possess
the private data corresponding to the
semaphor ID that's embedded in the
ticket and finally with proving that
you're over the age of 18 you say that
you possess an ID pod it's signed by
some trusted State uh it's date of birth
entry value it lies in the appropriate
range to prove that you're over 18 and
you actually own the semaphore ID so it
really is your ID
pod so from the user's point of view
this should all be streamlined by the
way I mean there's going to be some web
page you go to and then you click click
and then you get some pop up and it's
like yes select your pod select it prove
bam you've proved what you needed to
prove that proof goes to the server
together with whatever you chose to
reveal I mean what you choose to reveal
is usually determined by the application
the developer would have baked that in
you you can actually go through and make
sure that you're not revealing something
you don't want to reveal in which case
don't make the proof and then whatever
it is you were trying to do hopefully
should come
through
so here's a highle description of the
GPC compiler as a recap uh as mentioned
before from the developers perspective
depending on your application you would
form some kind of proof
configuration um specifying what it is
these pods what what properties these
pods should have the pods that go into
the proof so the application that the
user interacts with will have both a
proof configuration and proof inputs the
proof inputs will have all the private
stuff that needs to be put into the
circuit to generate the ZK proof you
need uh the proof configur ation will
have other details like has an entry
called date of birth um maybe date of
birth should lie in a certain range or
this entry of this pod should lie in a
certain list its value should lie in a
certain
list and uh yeah so you basically take
these things um something I'm kind of
sweeping under the rug I'll get to in a
moment is um the family of circuits I
said that there's a many parameter
family of circuits
thing is we've pre preener so we've done
that for a certain well not a proper
trusted ceremony but you know we have
some artifacts that you can use um but
an additional input to many of these
procedures is the family of circuits
you're using so there's a default value
here that we provide but you could just
as well customize it and the process
goes as follows you plug in the
configuration and the inputs and you
know you put it in this GPC proof box um
the config and in are all checked I mean
the user might be trying to prove
they're over the age of 18 but if
they're not over the age of 18 according
to their ID pod this will be caught here
and let's say it isn't caught here you
know you have a script Kitty they
basically comment out that line well
they're not going to be able to generate
the ZK proof they're going to go a
cryptic error right or even if they did
try to even if they commented out more
lines further down the line they're not
going to come up with a valid proof so
here this helps uh helps you not shoot
yourself in the foot essentially in
producing false proofs helps in
debugging as well so everything is
checked all the validity of all the
statements the types
Etc um and then a circuit has to be
chosen you know let's say you have 10
pods you want to prove about you have to
pick a circuit that's big enough to
accommodate for that so um we
essentially build up a data structure
called GPC requirements which is just a
appropriate Json that lists you know the
various things we need and then the
circuit whose size is the smallest as
far as number of constraints is chosen
from a list um so something we haven't
quite done maybe we should think about
this at some point is uh who's
interested in onchain
applications yeah I mean so besides I
mean you don't really care about
verification cost you probably I mean
proof size is not really much of a
concern it's more about input size you
might want to optimize for that that's
maybe something something you might have
to like do on your own I believe we have
there are a few projects that do that
sort of thing but that is another thing
you might want to optimize for but in
our case we just optimize for
um circuit size because then that
reduces proving time because proving can
take a long time if you just choose one
of the one of the larger ones um inputs
are compile uh config is canonicalized I
should say so um sometimes the proof
configuration can contain unnecessary
restrictions on the inputs for example
you could say that a number should line
in the range you know 010 but not in the
range 510 right that I mean it's
unnecessary to specify it that way so
you can simplify that down to saying it
you know lies between 0 and five five
for example or 0 and four depending on
whether you're doing inclusive or
exclusive bounds um but it basically
brings it down to a canonical format and
then all the inputs are compiled in the
sense that once we chosen a circuit in a
circuit you don't have variable siiz
Loops you don't have variable size so
there's going to be a lot of padding
involved uh in various places and we
generally choose the padding so that
everything is still logically consistent
for example you could say you have a pod
has an entry with a value that lies in
some list okay list is let's say five
entries long but the circuit you chose
says all lists have to be have to have
one of the existing entries we choose
the first one that way when you prove
list membership you're still proving the
proper list membership you want it to
prove right even with the padding so we
have to do all that so we basically
prepare all the inputs for the circuit
and then along the way and finally the
revealed claims are included in that
output so basically in our proof
configuration we might have chosen to
reveal our date of birth and not
actually check it in the circuit for
example for the ID pod example that
would be amongst the revealed
claims and verifying is basically taking
the output of that last process plugging
into a box the config is checked against
the claims you can't check everything
because there is going to be private
data but you can check whatever is
available in the revealed claims to make
sure everything
everything's consistent and then you
verify the proof so just a yeah using
snark JS in this case and then output
true or
false so going back to the examples for
example I possess an unredacted speakers
ticket to proog crypto
uh sorry the proof config I'll start
with that so we specify the pods that
need to go into the proof we only have
one pod ticket pod doesn't really matter
what we call it here it's just a
label um and then that should have an
entry now so yeah so it should have a it
should have a sequence of entries
specifically event ID product ID ticket
ID we choose to reveal both event ID and
product ID why because event ID will
reveal what event it was Pro crypto and
product ID will tell us what kind of
ticket it
was um the ticket ID itself should not
be revealed so we say is revealed false
but we do specify it should not be a
member of the list that we call redacted
tickets now this list itself is going to
be specified here in the proof inputs
another thing I stated is that the
signer's public key should be
revealed um the signer of the ticket
because we do want to we do want to
actually assert that it's a legit ticket
right anybody can can issue a pod you
just need to make sure this is an
authentic pod issued by the the
organizers of PR crypto
would basically just be the pods you
make sure that obviously ticket pod
should coincide with the one you mean in
the config um all this is done under the
hood by the way in zup pass when you
make ZK proof so you basically get that
drop down box you get to choose the the
individual pods and then you can make
proof um the membership list should be
provided Again by name um list of
redacted tickets and you might want to
put a watermark in the proof inputs so
thing is you could make this proof and
then somebody could take your same proof
and try to submit it again right if you
didn't have a watermark nothing would
stop them from asserting the same thing
as you so by putting a watermark like a
timestamp or something associated with
the session you can you know guarantee
can't be
reused um so yeah that's essentially
what you put into that GPC proof box and
then out of that you'll get some gross
not here and you get the bound config
which is just the proof config Json or
JS object together with a circuit
identifier field which contains some
label that deter that tells you what
circuit configuration you chose there is
some uh
yeah there there is some logic behind
the sequence of characters here's what
it says I've chosen the protopod GPC
circuit with one o one object 10 entries
it has a max Merkel depth MD of six what
that means is the the pods you put in
are not going to be bigger too big that
they can't be accommodated by Merkel
tree of depth six yeah so two to the
five
entries um zero NV mean zero numeric
values um in this particular proof I
don't need to say any anything about any
numbers per se I'm just checking for
list membership and I'm revealing some
values I don't need to say that you know
this entry is greater than five or this
entry is greater than that entry nothing
like that so I don't need the numeric
value module and I certainly don't need
the EI entry inequality modle module um
which is what would allow me to make
those inequality comparisons uh this is
something Andrew talked about briefly um
in order to say things about entries in
the sense of inequalities like greater
than less than not uh not not equal to
that's a different story but if I want
to say one entry is greater than another
first I need to check they lie in an
appropriate range that they are 64-bit
signed integers that's the convention we
use um but you do have to restrict the
range to do this properly in ZK so I
don't need any of these modules I do
need a list membership module that's
what the L is for I need one list
because I only have one list here to to
check that the ticket isn't redacted um
maybe it has 100 entries you know so I
need one list of 100 entries I need zero
tuples I haven't really combined any
entries um you you might want to combine
entries to check that a tuple of entries
lies in a list or doesn't lie in a list
um and and in this case because this was
prog crypto 2023 before we migrated to
semore V4 IDs I need one owner module so
that's the O of semi 4
V3 and zero sem 4 V4
modules and then revealed claims it's so
up there you can see I chose to reveal
the signer public key event ID and
product ID and they're all revealed here
amongst the revealed claims the water
Market is always reveal revealed um
because that's you know part of the
challenge in a sense and the membership
lists in question are also
revealed so that's that
example um to assert that a ticket to a
devc connect 2023 event was issued to me
um the approach is much the same the
only difference here is I actually form
a pair uh consisting of the signers
public key and the the signers public
key of the ticket pod that was issued
and the event ID and I basically check
that that pair lies in the list of all
Dev connect pairs basically pairs of you
know Dev connect event IDs together with
sinus public keys to ensure that the
ticket is uh from the yeah is from that
list um and then on the other hand I
also assert that the attendees semaphor
ID entry of that pod is my owner ID and
in fact it's of type semi 4 V3 you could
replace that with V4 if we were dealing
with V4 IDs so in this case I think
everything's self-explanatory except the
circuit configuration changes everything
is okay up until about here now I need
one Tuple of
A2 um so this is like the best case
scenario by the way um you might not
necessarily get something that exactly
fits your your requirements it could
very well be that we haven't provided
any circuit configurations with one
object and a miracle depth of size six
perhaps we only provided meral depth of
size 5 in which case you would have
gotten different parameters here but
this is just for the sake of
illustration and finally we have the
example proving that you are over the
age of 18 um in this case what you want
to do is show that the signer's public
key lies is a is uh in the list of
public keys of trusted States now in
this case I've deliberately chosen a
smaller list size 10 I don't know if
there are 10 states
that we can actually trust in this world
um but for the sake of example um
same except for dat of birth where here
we assert that it isn't revealed so
we're not revealing our date of birth
but we are asserting that it lies in the
range 0 to 18 years ago specified as
unix's time in this example um
yeah and uh
oh and in this case since we're actually
using our semaphor ID we can actually
associate a nullifier with this uh with
this um particular proof If we so choose
in this case you can specify that as
part of the owner section of the proof
input and that comes through with the
claims so just a quick refresher I've
already alluded to this but circuits
have limitations compared to regular
programs mostly As far as like um static
versus dynamic memory you've only got
you've got to make sure everything's of
a fixed length all of our functions have
to be naturally expressible in terms of
addition multiplication in a field this
motivates much of our con many of our
constructions and much of what we do um
and this is why we have to provide a
number of templates to each object is as
I said um is a merized structure so you
basic basically take your key value
pairs blah blah blah Merkel root you
sign that you get a signature you have a
public key associated with that
signature you want to check that all
that is consistent in the circuit and we
have one module that does that it's the
object module this will be done for each
object provided to the Circuit like I
said we pad things so if you choose a
big circuit that requires I don't know
one of those objects is going to be
repeated and you're just going to have
extra checks of the same sort so yeah
public key signature Content ID which is
that root cash I'll check for
consistency essentially just check the
signature against the message given by
the content ID now each entry you plug
into the circuit the way we do this is
the entries are their
own thing it's not that you plug the
objects in in their entirety you don't
have to you only plug in the entries
that you need to prove something about
and then you specify Which object they
correspond to so there's an index in
there we have a bunch of arrays we have
the array of like object content ID and
other things um and you specify for each
entry which uh pod object underlying
object it corresponds to and uh what the
entry module checks is that the entry
actually does correspond to that pod
that you specified so you provide a
Merkle proof of inclusion of that entry
so the root hash is recomputed checked
against the the object hash and we also
so um like as was mentioned earlier the
actual key the name of the entry is
passed in as a hash um you know that's
also passed in here to it's also checked
against it's in the Merkel proof and in
the end if everything is good the
revealed entry value hash is spat out
because we choose to reveal an entry or
not reveal
it and by the way if anything is not
satisfied the circuit just won't compile
that's what's going to happen oh the
proof is not going to compile sorry I
say um yeah now besides entries in a pod
it is part of the Pod data structure but
for that reason it is passed into the
circuit um it's actually yeah passed in
together with the object itself with the
object itself so what happens inside our
big circuit is that all of these are
aggregated into an array both the public
key and the content ID there are some
things you could prove about the content
ID you could prove the content ID is a
member of a list that might be a bit
weird because you know who's publishing
content IDs um but you can also say
things like I have a bunch of PODS and
they're all distinct so that's something
I'll get into in a moment we actually
have a module for that the uniqueness
module so we basically take this data
and we hash it so that it's treated just
like any other entry can be used in all
the constructions we have in ZK for
proper entries so you can check list
membership um you can check for equality
non-equality not inequality because
these things are going to be pretty big
they're probably going to be close to
guarantee that you know a hash is
actually going to be a 64bit signed
integer in a field I mean why would you
expect
that um so that's what the virtual entry
module does um and then for virtual or
non- virtual entries we might want to
check if they're equal to one another
you might um yeah want to check if one
entry value is equal to another entry
value or is not equal to another entry
value for example you could say I have
two pods and they were signed by
different parties um and in this case we
basically plug in the value hashes we
plug in an array consisting of all the
entry value hashes together um and that
and as part of your proof configuration
you would have specified whether you
wanted to check for equality or
non-equality and then you've got the
owner module so if you chose to say that
a certain entry in a pod was actually an
owner ID semor V3 or V4 type then you
ought to provide your semaphore secret
as an as a private input to to the
circuit and yeah you basically specify
which which of the entries of the uh of
the inputs um corresponds to the
semaphore commitment you can plug in
both a V3 and a V4 identity by the way
so it is possible to actually have like
a pod with a semaphor V3 identity one
with a V4 identity and you prove that
you have the secrets to both identities
that would be a way of establishing that
you own both of those semaphor IDs I
mean one such way I mean surely more
direct and uh yeah you basically specify
which of the entries does correspond to
your semaphore ID you plug in you plug
in your secret you might want to plug in
a nullifier as well to invalidate this
proof if somebody else wanted to come
and use it later on um and you might or
might not choose to reveal that
nullifier hash and in this case either
you output that nullifier hash or you
output minus one which is our convention
for the absence of
data um and then we have the numeric
value module so here um like I said
entry values are passed in by hash by
default but sometimes you want to prove
things about entry values um like they
lie in certain ranges um and in this
case they have to be sign 64-bit
ranges um so the numeric value M for
that you plug in the actual the value
corresponding to the entry that you're
arguing about in this entry value hash
array um you plug in the entry value
hash
uh and uh a lower bound and an upper
bound and those are checked in
circuit and assuming you've done that
you can also check whether such an entry
is less than greater than less than or
equal to greater than or equal to you
can do whichever using the entry
inequality module so in this case you
just pass in a pair of Entry values and
this box will just check if entry one is
less than entry2 and that's sufficient
for checking any possible inequality why
because we're going to get a Boolean out
so you could just flip it if you wanted
to do the other way around or you could
just assume it's false if you wanted to
do the other way around with an with an
equal sign as well like a non-strict
inequality so in the proof config you
don't have to think about that like oh I
can only do is less than or is not less
than no you don't have to think about it
just put in less than less than eek
greater than greater than eek it's all
the same um it'll all be translated
appropriately when compiled down to the
Circuit so the compiler takes care of
all these little things that you you
probably have thought about you've
probably done this before but it's easy
to mess up if you have to do this again
and again and you know
keep then we have the tupple module how
do we handle tuples easy we just hash
them so in this case uh you might so in
one of our examples we had a pair of
Entry values and we want to show that
that pair lies in a list of pairs so
what how do we handle that in the
circuit we actually hash the list of
pairs we hash the thing that we want to
check is a member of the list of pairs
and then we check that the hash is a
member of the list of hashes and that's
what the tupple module is responsible
for it basically just hashes everything
away to obtain a tupple hash which you
can then you can then treat the tupple
as an entry in its own right as far as
the logic is concerned
here then we have the list membership
module that one's fairly straightforward
we just do a linear search through the
list if we actually uh we plug in the
entry value hash and the list of hashes
to check lists are always hashed anyway
um entry by entry so we're just doing
Simple arrays in future we might
actually have like you know pluggable
Merkel trees so that you could actually
do a Merkel
membership uh but for now we just do
linear lists because we only care about
small sizes anyway and it's fairly cheap
um so yeah the list membership
module and then we've also got the Pod
uniqueness module as I mentioned you
might want to say the pods going into
the circuit are all distinct as far as
their content is concerned and this one
has a simple switch I mean you just plug
in all the content IDs and then you get
a Boolean zero or one depending on
whether all the the content IDs are
unique and whether you want to impose
that the content IDs are unique is up to
the proof configuration constraint is
put in and that's it there's nothing
nothing else about it it's just to
ensure that you don't reuse the same
proof um or just have that the proof be
associated with that particular
session um yeah so life after pod and
GPC should be a lot simpler you just
write down the data structure then maybe
use the GPC or GPC PCD library or even
the zapi which uses all the stuff under
the hood to you know put your
application together something comes
next and then profit and we're
good so there I mean future directions
for all of this would be more featur
um yeah I mean I already hinted at a few
possibilities like having some form of
Merkel membership rather than a linear
approach to list
membership um more pods more gpcs I mean
you know it's pretty the the Pod project
is pretty young um lots of frog pods
going around so I think uh there's so
we're getting more adoption by the day
um and possibly a different stack for
certain other applications
um I mean at the moment we're using uh
circom with Groth 16 in typescript um we
can't do recursive proofs what if you
wanted to plug a pod proof into a GPC
well you can't really do that it's not
natural in this setting people are going
in this direction of recursive proofs
you know maybe use something like Pony 2
uh or whatever else is in fashion to get
things done um yeah those are just some
possible directions uh so this is pretty
much all I wanted to cover uh what I
usually do at the end of or towards the
end of such a talk is maybe like quickly
go through the actual protopod GPC
circom file but I think you can all look
it up in the repo um maybe it'd be good
to turn to questions instead
um I was given a QR code damn it's
really small let me see if I can make
make that a bit bigger or did you
already reveal that QR code no you
didn't okay
yeah let's do
that um should I maybe answer some
questions because there have been some
questions already so show slides jump to
that okay uh so a couple links just to
to tell you where to go for more
um uh this this was a lot in a deep dive
session so thank you all for sticking
with us um but there is an all day uh
CLS from zerox Park about programable
cryptography tomorrow um all of that I
think may be of of interest to you but
in particular there's a workshop in the
afternoon which is what that QR code is
uh that is going to be about zup pass
and the sdks and things that you can do
to build on uh pods so uh hopeful some
of you will join us for that um also
check out the docs check out the
telegram um and then here's the thing
you've all been waiting for we'll leave
it up for a minute or so before we
switch to
questions all right everybody got your
frog let's get to the get to the
questions okay uh when making ZK proofs
are they already being done with the
idea that they are anti- quantum or are
we still far far from having those
problems um we as a team are far from
thinking about that those problems
because as I said in my intro we're
limited to kind of tried and true
technologies that live live in a browser
and that limits our choices to not
really being able to kind of pick and
choose that much um everything here is
based on uh elliptic curve cryptography
uh with the baby jobjob Prime field and
uh curve so don't think that that's
guaranteed Quantum resistant um but I
don't think anyone's broken it yet but
yes we have potentially would have
problems with that in future and that's
why we'd want to investigate alternative
uh Avenues and proving systems like Amad
alluded to um could I compare and
contrast pods with verifiable
credentials um yeah that's something
that I looked into it they do something
very similar um particularly the uh Iden
LD to represent verifiable credentials
and make proofs about them um it's a
similar kind of merization they use a
different kind of Merkel tree they use a
a sparse Merkel tree which is optimized
for larger trees with deeper depth and
can do things like prove uh absence of
an entry that's one of the limitations
of our pod Merkel tree that you cannot
prove that an entry is absent only that
it's present um if if you saw my list of
data types for pod one of those data
types is null that's actually there
specifically so if you want to prove
that something doesn't have any other
value you can give it a null value and
prove that it is present with a null
value rather than proving absence but
for that we get Merkel depths that are
like five or six or eight in most of our
circuits whereas the um Iden 3 circuits
for sparse Merkel trip trees have a
default depth the 32 because they need
to avoid collisions on the on the Merkel
hash um so that's a technical difference
we're optimizing for like lots of small
objects rather than a big complicated
tree is kind of the the trade-off we
made there but they are compatible in
concept there's no reason you couldn't
take a verifiable credential and turn it
into a pod pod is a much more General
like any names and values will go okay
um what are some of the challenges
problems in this space anything we could
look into and help uh almad may have
more thoughts on that in some of the
like crazy circuit stuff he's been doing
like I know that lack of ability to do
things like recursive proofs is
definitely a limitation for us um uh the
size of uh proofs that we can make in a
browser on a phone is definitely a
limitation for us um we my kind of rough
rule of thumb has been we have to keep
things under about a 100,000 constraints
if you've written circom code each
constraint is kind of a mathematical
equation um so uh a our typical circuits
right now are anywhere from like 8K
constraints at the low end to like 30 or
objects 20 entries Etc um so you can't
really do really really big pods unless
you're willing to take some extra time
and some extra memory uh it's all
possible uh what else is the circuit
able to see the raw data or only the
tree of hashes how are range checks and
comparisons done um I think ahmod
alluded to that in in uh when he was
going through the modules but um only
numeric values can go into a circuit
directly that's why you can't do like
ordering comparison on a string because
that would require a string value to be
in the circuit but with numeric values
you can use the numeric value module to
prove that this is the plain text value
that corresponds to that hash and then
you can do things like range checks uh
on that um and there's nothing stopping
you from making more modules for more
things um let's see uh sorry you
scrolled away from the the
top um question is there a way to
integrate the automatic approver inside
the smart contract um so proving in a
smart contract has the disadvantage that
all of the inputs I think are inherently
public because that's how uh ethereum
works so if there's nothing stopping you
I think smart contracts are are tur in
complete um I think the the size of the
input would be very large and you'd have
uh confidentiality problems but more
useful is verification on chain and we
already have that working um using the
verif the verify compiler is kind of
used as a preep to take the like
friendly objects and compile them down
into the raw circuit inputs and you can
send those on chain and have the onchain
verifier verify that um there's a demo
app called frog juice that lets you
juice your frogs um onchain uh is it
possible to tamper with a GPC config to
compile a gener generic circuit that can
allow proving false statements um no um
assuming that you use the the GPC
compiler as is and assuming it doesn't
have any major bugs it hasn't been
audited yet um you shouldn't be able to
prove false statements what you can do
is prove meaningless statements right
like I have a that contains a field
called driver I mean I can make any pod
like that and if what someone asked you
to do was prove that you're over 18 that
is a meaningless statement for that
purpose so that's a not entirely solved
problem like in the easy case where you
where the prover or the the verifier
first asks for this config and the
prover sends it back it's very easy for
the verifier just to say like is that
the config I asked for yes or no just
like do a deep comparison if you want to
get fancier than that like oh you can
prove a state statement that is like
stricter than what I asked for for
instance like that's a bit more like
logical deduction um that's not easy but
most cases don't really need that uh the
example of a module comparing two hashes
why take a list and an index instead of
uh just a value I'm not sure what that's
about I
clarify I'm assuming that's the entry
constraint module most likely um
well I
mean it could go either way but maybe
you had a particular uh particularly
strong response to that I I may have
just figured out what this is feel free
to jump up if you're the person who put
in this question um what the index
you're you're seeing may actually be
part of that routing Logic the
multiplexers that I mentioned so it's
not that the comparison is comparing
something with a list the comparison is
comparing two hashes but the input to
the comparison one of them is the entry
that this module is attached to so it's
always a fixed input the other one you
can compare it to any of the other
entries so the way that we accomplish
that in the circuit is there's a list of
the hashes of all of the entries and
then you use this index to pick which
one are you comparing to so this is
that's part of the configurability it's
not about the list being a like value in
that you're checking the list is the all
of the possible inputs and the
configurability is the
index uh is there any standard supported
for pod um I don't know what you mean by
standard so like everything's open
source right now the code is the
standard I know realize that that's not
a great answer um I would like to
document this as a proper uh at least a
protocol spec essentially um whether we
would standardize it I think is up to
adoption and and how important that is
like I don't I didn't want to slow us
down in our initial development by like
getting the w3c involved or their ietf
or something like that to standardize
things because that can take years I'd
rather first build something that works
iterate it on it with some feedback um
but yeah I think that more of the format
should be more closely documented uh
that's something that we're going to
work on um in order for this to work in
the governmental settings do issuer
verifier Andover need to agree in
advance on the Pod structure um so yes a
a pod inherently is schema list you can
put any names and values in it that you
want but uh there does have to be some
agreement between the uh approver and
verifier of like oh what does a driver's
license look like if you want me to make
a proof of a driver's license um we have
to agree on what the names of the values
are um there are two ways that a a the
issuer can actually Express that one is
just if the only thing you ever sign
with this public key is driver's
licenses then the attestation that is
this pod like implicitly is ATT testing
that it's a driver's license because
this is the public key that is only used
for driver's licenses um the other thing
that is a recommendation but not
enforced by the system is a an entry
called pod type that is meant to be a
unique string for your app to specify
like this is what this pod is for which
probably also specifies what the entries
should be and what their types should be
um but there is nothing inside of our
libraries that will enforce a schema um
other than the proof config itself is
implicitly enforcing a schema of the
things that are proven
about
only yeah so anything that is not
mentioned in your proof config is not
being cryptographically proven you may
be able to trust it because this issuer
like states that they only sign things
that follow this whole schema but
cryptographically if the only thing you
prove about is like two entries of a pod
and that pod actually has 12 entries
like a pod without the other other uh 10
entries would be provable by that
configuration like anything that you
want to be sure is true you have to
prove about um unless you're willing to
just trust the issuer um but you can do
things like prove an entry is present if
that's all you want without revealing
its value and that is a way of like
checking that the schema is present uh
but it's really up to the specific uh
use
case did you I have a
question it's answered oh
okay any other live questions feel free
to put up a hand yeah uh can you pass
over the the mic
thank you um how do you approach uh
proving uniqueness in Dynamic things
like ownership of a name or address in a
chat
room
interesting I
don't think that's a directly solved by
gpcs um other than you know the standard
approach of like pick a random number
that's big enough and it probably won't
overlap but
the all you can act I me pods are not
inherently unique they are like defined
by their contents so a given pod set set
of contents will always have the same
content ID and then if the same signer
asss it it will have the same signature
um our signature algorithm is
deterministic um so there's no inherent
uniqueness there but you can put a
unique you know user identifier or
something like that in a pod um you can
prove in a if you put multiple pods in a
single proof you can prove that the
individual ones are unique or you can
prove that you know the um the user ID
that's represented in the Pod is not the
same as this other one um but I I think
that's about as far as you can go with
like this system like proving uniqueness
across like all of the users in a chat
group or something like that is not
entirely in scope but may maybe there's
something more specific that I can
suggest for you
thanks any other questions
all right well thank you all for joining
us um we'll stick around for a couple
more minutes if anyone wants to to chat
in person but uh otherwise uh I hope to
see some of you at the the workshops
tomorrow at the programable crypto uh
CLS
where
SC
thank you okay hello everyone and
Welcome to our Workshop about bringing
an I on chain and more
specifically hello team how to build and
run your own agent that is betting on
prediction markets on
chain yes
please
okay oh it's good cool thank you very
much but are they able to see my
slides okay now it's there thank you
very much so my name is Peter I work as
engineer at nois and at the same time
I'm doing my PhD in AI
but I would left the in uh introduction
there but if anyone is interested in
project that I work on or anything
similar feel free to go to my website y.
ninja where you can find one of the
agents with my CV in the memory and some
prompting around it to be a bit more
interesting but that's enough about me
and let's go to the actual
workshops uh so today we will mix three
different concepts so we will mix
prediction markets web tree and agents
so there already were some talks about
prediction markets so I bet most of you
are already familiar that prediction
markets and rep Tre are kind of popular
mix nowadays but we will bring their
agents as well and why because we will
try to build an A autal system that is
more or less capable of existing only
living on its
own uh most importantly without any
major human interactions so the idea is
that we'll create an agent and we will
keep it running and it will be there
doing its stuff and we just don't don't
have to care so at least that's uh
that's the ultimate goal and we will see
how it goes so the agenda for today
first of all I will do some introduction
about prediction markets so there
already were some talks and good
workshops that went really detailed into
the prediction Market but I will do some
brief introduction anyway just that
everyone is on the same page about what
we are working with and why are we using
it then I will introduce agents itself
so agent can mean different things in
different environments in different
contexts uh so we'll take a look at what
it means for us in context of this uh
workshop and then the most important
part will be building our own trading
agent from scratch so we will start with
almost zero code and we will be
able uh to create agent that is perit
table on prediction market and then it
just well running on its own and if the
time allows there is some uh bonus
section in the end where I will
introduce uh more General agent that is
not just only about prediction Market
Market but is kind of living on its own
on on
chain uh but before I get to the actual
Workshop just a few pre-oral steps when
we get into the agent building uh part
everyone is welcome to build the agent
with me so hopefully I will be slow
enough such that you can uh follow the
steps however there are a few
requirements that we need uh to get the
agent running uh up and successfully so
the thing is that you can clone the
GitHub repository that is
almost yes direct to microphone okay so
why not so there is almost uh no code
there so we will build up but there is
some environment prepared for us such
that we don't need to care about the
boring stuff like which python to use
what dependencies are required Etc
everything is there and we will just
build upon that then the second thing is
that we need some API keys so right now
those agent are somehow mixed of web 2
and web 3 Technologies hopefully we will
go more into web three uh with time but
right now we need at least API key for
the graph so the prediction Market stuff
is on chain but we will use a subgraph
from the graph to query efficiently uh
the data so if you go to the website uh
the graph you can just sign up and then
we'll give you some free credits that
are more than enough for for purposes of
of this
Workshop then the second API kick that
we need is for Tav so Tav is something
like Google on steroids but the great
thing there is that uh they will give
you some free credits as well when you
sign up so you sign up you will get the
credits and there are more than enough
for this workshop for sure and usually
also more than enough for having this
agent running a few times a day for a
all month so that's about the free stuff
unfortunately there is also some FID
stuff so this agent will be powered by
llm and we will use open AI as llm
provider and as far as I know the doid
provide free credits however if you
already have an openi
account
then uh don't worry about using your key
this agent is very cheap so you probably
won't even notice it but if you don't
feel free uh to join this telegram group
and ask for the key so assistant there
will send you one and you can just use
it for this Workshop or just during uh
during Defcon and the second thing is
that those prediction markets are
running on gnosis chain and we will
need well we will need some xday to pay
for the transaction fees
and to place the bets on the prediction
market so again fees on dnos sh are
super cheap and the bets that are placed
by default by this agent are very very
uh very very small so if you already
have your private key uh with some EX in
it feel free to use it but if you don't
trust the code yet or you don't have it
uh you can use some wallet as metamask
for example create your private key and
send the public key again to this
telegram group and we will send you some
free EX dat that you can use for for
this Workshop so that's uh that's about
the pr requirements and let's get the
actual to the actual
stuff first of all a little bit of
introduction and overview of gsis chain
and why are we using gsis chain uh for
this so if you want more detail about
gsis there is a boot uh near the main
stage I believe so you can get the
information there but for us the two
important points are the Gnostic chain
is using xday as the native coin and
that's back to the USD and the second
important point for us is that on
agnosis chain we have very fast
transactions so the agents can do many
bets on these prediction markets in a
short amount of time and also the fees
there are very very cheap that means
that the agent can place like hundreds
of BS uh during a short time and all it
needs it's just a little bit of profit
order well to don't go into a loss and
to keep kind of leing and running and
placing beds for for the future
so that's uh for the grosses and now
let's go into prediction markets itself
I have a few slides there but I think we
can just go out of them and actually
look into the web platform itself so
presagio here is like Omen
on gnosis and if you go there you will
be able to
see uh I can zoom in you will be able to
see many many questions where each of
these these questions is one prediction
market so I can open for example which
one let's do
something uh something nice let's say
one so will any major UK legal Authority
announce something something so the
question right now is not so important
what's important is that each prediction
Market is associated with a set of
outcomes so you can see here that this
one is associated with yes outcome and
no outcome and because this is a freshly
created prediction Market the
probabilities at the beginning are 50/50
so someone created uh this Market
probably some agent and because he
doesn't know the answer he wants to get
the information out of prediction
markets he created the odds 50/50 such
as agents and humans get better and give
the information to him the idea there is
that the market Creator who the person
or agent who created these markets added
some liquidity in this case he adds 7
xday in liquidity and when you go there
and you bet on one of the
outcomes uh you can make a profit if
your bet is correct in the end out of
this uh liquidity so we can try it out
so for
example let's say that we will
bet that we will bet 0.1
xday in 2 years so I have no idea if
that it's correct or not but just to see
it we see that for 0.1 xday we would get
tokens and we can try to place this bet
actually because why not so there is
some
clicking uh in between so yeah let's
approve the transactions and everything
and let's wait for the transaction to go
give it just a few
seconds okay we can confirm the swp some
more
clicking there is never enough of
it and in the end let's me try to
refresh the
market and it didn't work for some
reason of course so let's try it once
more when I was testing this yesterday
of course it work very nicely config
swp confirm transaction
submit transaction
successful so maybe this time let
refresh it
again and yeah it's there okay awesome
so we can see that I have bet 0.1 xday
on yes and in the end after 5 days when
this market is closed if I was correct I
can win 0.19 of R each day back of
course his I was incorrect and I will
lose it all and that's it and that's the
main motivation for agents and humans to
provide as accurate accurate information
as they can because the money are on the
table so if someone would go there and
he would be lying to skew the odds for
some reason and basically is giving free
money to the agents and humans who are
telling uh telling the truth and how
this worked in the practice is said we
can see that because I B the yes outcome
that the probability went up and the
probability of no which is just inverse
in this case uh went
down and the price of these outcomes are
actually the probabilities itself so now
we can see the yes price uh sorry yes
probability went up and in this case if
we go and we will try to buy for the
same amount of X day once again then
this time the amount of tokens we are
going to receive is lower than before
and so people that are or agents that
are relate to the parties so to say have
lower profits to be made however let's
say that I was wrong and actually the
know
outcome is more likely to be and someone
knows why someone has some in their
information or something then in that
case they can go and they can buy uh the
no tokens and because I buy bought the
yes before and the probability of no is
now lower so the price is lower then the
profit to be made for the same amount of
each day is now higher well and yeah
this is how it works in practice so we
can try to op the market uh with more
volume in it and we can see in the
history okay one b as well let's try
something else perhaps something that
will be closing soon so there should be
uh uh more BS
available maybe this one let's see
history yeah we can see that the both
agents that are identified by AI Tech
and some humans are participating in
this market and they are
moving uh the
propability in time and one more thing
to mention about this prediction markets
Ed on omen or pressagio any erc20
compatible token is supported so before
I open some Market created in R xday but
we can also filter for sday markets and
what's nice about it is that for example
in the category of Dev
conflict there are some markets that are
running uh for very very long so for
example this one will be open for two
years and un unfortunately part of the v
xday as the CL talking with these
markets are is that if you look your BET
right now then in those two years
theoretically uh your profits can be
eaten by the inflation but but if the
market is using sday which is a saving
day version of xday then it has some
yearo yield I think it's 7% per year and
in that case even if your bet is locked
in then you are still going to be
profitable in the end because the
inflation will is somehow checked out by
uh by
the okay I think that's about it for the
prediction markets and we can go back to
the uh to the presentation so just give
me a second set it up okay I have talked
about this and let's talk about why uh
is this interesting how this can be
useful so one of the more more obvious
use cases are just information discovery
so if you have some question you are not
sure about the outcome and you would
like to at least know some probability
distribution based on the information
that like the world world that is
participating PR Market has uh then they
can provide it to you if you provide
good enough liquidity so for example we
Apple launch a new iPhone by the end of
the year if you would create it then we
will get the answers
another uh another more fancy use case
can be governor a future AR key that was
also talk here today A few hours back
where a good example is that we can
create a market saying will Q4 Revenue
be higher than Q2 Revenue if he fire or
coo by the end of Q3 so in such case uh
employees or stockholders or whatever
can whoever can participate in this
market uh can say what they really think
about such action so if we really should
fire the CEO or not because it won't be
based on some personal like personal
manners against the CEO but on the fact
if the revenue actually will be higher
or not because if someone is going to
lie they are going to lose uh the money
from from the bets 10
more like more per standard use case are
betting so anyone can create a market
which team will win some hockey match uh
during this weekend or anything similar
and one of the perhaps not so clear use
cases are motivation for agents or
humans to complete some job for
you uh so what we can do I created this
market yesterday
saying real agnosis AI receive at least
three questions during Devcon 7 2024 uh
Workshop today and this is a nice way
how you can somehow provide without any
middle one middle man a guarantee to the
agents or to the humans that if they do
something for you they will get paid
because this is the kind of Market that
everyone here can directly influence so
anyone can ask three questions right now
or at the end and you can go there you
can buy uh some yes outcome tokens and
you will basically uh make the profit
for yourself because you are the ones
that finish the job and so the
prediction Market will resolve in in
favor okay so that's about some use
cases and of course there are many many
more of them you can check uh the gnosis
white paper uh for more of the use cases
now let's quickly conclude that the
ultimate goal of SL prediction Market is
well to be like a Google of customized
information searching what does it mean
is that on Google you can find any
information that this right now but on
prediction Market you can get
predictions about future and with good
enough liquidity with good enough
participants there uh the predictions
will be very very
accurate however one problem of those
markets is
that we have seen on pagio and I can
show it once more that all of those
markets has kind of low uh liquidity so
seven Isa in liquid
is perhaps not so interesting for humans
to go there and to be researching uh
like very uh very complex
stuff and expert expert staff for some
small profits however AI agents they can
run very uh very cheaply so for an agent
even a few cents in profit or perhaps
few dollars on better markets it's
enough to cover the API fees and to make
some profit just it make sense for the
agent to uh kind of keep going on on
prediction markets and that's why we
want to block block in agents into
prediction Market platforms so what's an
agent in our
context well it is some it is some
entity that is doing actions in some
environment so in our case it will be
some llm that is doing actions on
prediction Market where the actions are
uh betting yes or no outcome s based on
the research that the agent agent
did uh so that's like a most basic agent
is just doing a bits but there are also
more complex one that can learn based on
its actions because from this
environment sooner or later the
prediction Market will be
resolved and the agent will know if he
if it was right or wrong so if it was
right it will receive a positive reward
and well it will know that it did some
good actions but if it was wrong it will
receive a negative reward because it
will basically lose all the funds that
he Prov uh that he bet on the given
market and along with that the agent
will receive some state so the agent can
look into the internet of okay this was
my research and I bet on yes however the
real outcome was no and what's the
reason behind it and more complex agents
are able
to well somehow reason about it and
update their internal State and
hopefully do a better predictions in in
the future and how those agents are
built there are usually some llm
provided either from openi in this
Workshop or for some other company
that's fine doesn't matter but how all
of those L works after that they are
trained to be just generally helpful
well generally helpful B so probably
everyone used CH GPT in the past and
when you want CH GPT to do something
more useful then you can prompt it uh to
do some specific goal so instead of just
saying place the best on this Market you
can prob the agent to first uh do some
research on internet based on that
predict some probability and based on
that plays the bet in the end and that's
uh what we will be
doing in
this in this
Workshop so however there are some like
uh
complications because it cannot be as
simple as just using the
llm but in the code right now is there
are many many Frameworks that we can use
uh to call the LMS from opni or anyone
else however the thing is is that if
we only invol the llm without any tools
at all there is no way for it to know
what the actual outcome should be
because well it was trained up to some
time in the past and it doesn't know
what will happen tomorrow so if we ask a
well trained llm what if it will rain
tomorrow in berin if it's well trained
it will say that I'm sorry but as AI I
don't have any real time information if
it's not well trained what will happen
that it will probably hallucinate and it
will tell you that yeah tomorrow it
won't rain it will be super nice but in
the reality the forecast is very very
different and so that's why we need to B
in some tools for our agents such such
St is not just llm but it can receive up
toate information from internet and so
that's fortunately also quite easy to do
and one of the tools that we can use is
called Ser API which is again something
like uh API over Google something like
the that we will used or you could use
Bing uh whatever and if we use a well
trained llm we go prompting what will
happen that if when it uh when we asked
L will it rain in Berling tomorrow it
will understand that this is not
something that it can just say without
any more research and it will do the
internet search for baring weather
forecast uh tomorrow so it will get some
information
and based on this it can do the final
prediction of course in practice the
prediction markets are not as easy as
only this because well everyone can
Google weather forecast for tomorrow so
the prediction markets are usually about
more complex questions as the future
Archy ones that we seen or perhaps some
I don't know stock situation or or
anything so in reality we need need to
build more complex agents to actually do
some reasonable prediction but this is
like the most basic thing uh that we
need to do at least
something something reasonable and so in
practice the components of Agents would
be first of all we need the llm itself
so the llm is great it's large language
model and it's great because it can
process uh questions in human language
so anyone can go on the platform and
just create the
question like a human would like like
put the question and that's about it and
llm can process it and it can reason on
it and it can reason what tool to use
should it be Google should be something
else and how to predict it in in the end
then more fancy agents also have memory
so the memory is important because the
agent can remember what bets it placed
in in the past and this can be useful
for several reasons
for example if you place a bed one week
ago it makes sense to like reevaluate it
once again if there is still time uh to
canle the bed to sell it or perhaps
there is more information conf
confirming or beted then we can bu uh
buy more of the tokens and so on and the
second important use case is
to uh well to fix the mistakes from the
past so agent can look at what BS it did
what what was wrong what was right and
perhaps if it did a bet based on some
fake News website it can decide that
okay I won't use this anymore and I
would use some other well
other uh other new site so that's about
memory and then of course the tools so
it's great that LM can reason and choose
a tool it can access the memory but of
course it needs the tools itself so the
most uh most basic tool will be some
Google search being search something
that LM can use uh to search internet
for actual information upto-date
information such predictions are as good
as possible but then of course there can
be many many other tools so perhaps not
everything is on Google so the so the
agent can have a tool to scrap websites
on its
own and scrap some uh news websites
Twitter or well whatever so any tool
that you can think of that could be
useful for the agent
uh you can contribute it if you want and
last but not least the control logic so
the llm can do a lot of reasoning like
quite fine but there is always a place
for some fine grind control logic and
like fine grinding the llm to do uh the
stuff and in the end agent can decide
like should I be continuing the research
do I need some more
information or can I predict right away
maybe this question is actually already
answered and I can just find the right
answer with 100% probability or perhaps
the question could be something that
cannot be predicted at all which also
happens like quite a lot and so on so
forth so we will see some uh examples
later when we code uh when we code the
agent and just to like sum it up those
prediction markets are interesting for
agents for even from like machine
learning web 2 point of view because it
combines several very hard uh subtask so
first of all as we are saying the agent
needs to run efficiently so if the agent
will cost like $100 per run it doesn't
make sense to use it because even if
it's profit uh sorry even if it's right
on the prediction Market it will just
lose the money on API fees second part
is Agent needs to retrieve relevant
information from good sources so that's
not so easy even for humans if you
Google up something there is like a lot
of uh BR information so agent somehow
need to filter it and decide what it
should use in the end then it need to
reason about this information and it
need to predict the future which is
perhaps the hardest task of them all
because what happens nowadays quite a
lot is that these large language
models are close Source the training
data are not available no one outside of
the company really knows what it was
trained on and what happens quite a lot
is that they are actually trained on the
benchmarks or on the testing data set
etc etc and then is like not so hard uh
to be better than previous models on
them however if we are predicting the
future then
well there is no testing set available
for the future so those agents cannot be
overr
every day there are tens of questions
about the fuse that need to be answered
and every day some of them are resolved
and this is like continuous long living
Benchmark for these agents so if some
agent is actually profitable on these
markets
and he is accurate in Long Run that's
that's quite interesting thing to to
achieve anyway that was about the theory
now let's do some actual
actual stuff so before I forgot to
mention that all of this is open source
and available right now so the pressagio
is up and running available for everyone
so you can just go there connect their
wallet and bu on markets if you want and
all the agents tooling Etc are open
source in theosis GitHub so again you
can go there see the code modify it run
your own agent as you will see etc etc
so just a side note and one of these
like one of the stuff that's coded there
is this dreamly demo that we can
use to see how one of the agents that
are deployed by agnosis are actually
working in practice so let's just give
it a few seconds to
load uh again anyone can go to this
website you can see there is a free
access code uh for Defcon users so you
are free to play there as much as you
want
I will just hide this and I can zoom in
a little bit and another thing good to
mention is that those agents that we are
building are not tied only to omen or
pagio but actually we are or they are
supporting uh many markets or sorry many
Market platforms and it's quite easy to
add another one there so if you don't
want to bet on Omen because you don't
want to well spend real XI or something
but you would like to bet on manone for
with them or perhap you have idea for
some nice agent but it's highly
experimental so it's so good idea to B
real money you can go manifold metaculus
etc etc but for now let's sck uh let's
stick with Omen then we can select some
question
here uh those questions are put live
from the given Market source so let's
find something nice there for example
real gno hit $1,000 by the end of the
current year so you can see that we can
also open the per
itself and there are already some
predictions and agents that believe that
it's more likely uh that not okay let's
see let's see why so here in the select
agent section there are many many agents
already implemented all of them are
avable in the repository that was Link
in the slides let's just choose one of
them and now we need to well this will
take quite some time but something
already there okay so let's see what the
agent is doing first of
all the agent needs to access if the
question even makes sense because well
anyone is free to go to
presagio or use or tooling well everyone
is free to create his own own Market
with any question there however not not
all not all questions are are
well answerable so the agent will check
if the question has for example a clear
future event so the question needs to be
future and it needs to have a clear time
frame so the question uh needs to be
specific that this needs to happen by
the end of the year uh for
example and there are some more checks
and one of them important to mention now
that the potential answer can be only
yes or no so this is not limitation of
omen or presagio but it's a limitation
of this agent uh it's something we are
working on so in the future outcomes can
be whatever we want but right now those
EXs are supporting only yes yes or no so
if you want to create a market uh please
make it binary like this then another
check from the agent is is this Market
invalid because there are certain rules
on Omen and usually on other Market
platforms as well that will make the
question invalid
and the agent wanton B of them so for
example we have seen that the prediction
markets can be used as a sort of
motivation for people or humans to do
something and if the question is about
something illegal or Immortal then the
agent will just refuse to participate
there and it will skip it so there are
are some necessary
checks but we can continue and we can
see here that the agent will
take the question itself
and it will generate many many variants
that it can search a Google for to get
as much information as possible so you
will generate like 20 different uh
scenarios that you can search for and
from
this it will pick top four where it
makes most sense uh to search a Google
for so then it will do the search it
will find some websites it will scrap
content and let's continue with your do
some more stuff but most
importantly it will create a research
report like this so this is like a
compar a comprehensive research report
for the given
and it contains everything useful that
was found on the internet that can be
used to do the final prediction that
will be done somewhere near the end yeah
so here we can see that this agent in
contrast to the
doesn't think that this is so likely and
that there is only 5% probability of gno
hitting $11,000 so yeah that's
unfortunate but that's how it is and
because this is just a web demo so it
actually didn't place the
trade uh so the trade execution was
skipped but when we do the real coding
shortly uh trades will be will be placed
so this is H how the agent is
working internally and I think we
can close this and we can continue to
the implementation of actual agent
because the prediction Market agent
repository that I linked a slide before
there are implementations of the agents
but there are not hardcoded so what it
means is that we also created this uh
tooling Library it's called prediction
Market agent
tooling that makes it super easy to
create your own agents uh from scratch
so you are interested in in like doing
some research experiments uh creating
agents you believe there's some good way
to do it you can use this tooling and
again it's not limited only to Omen so
you can create agents that are betting
on any uh platform that you want and now
we will actually go and do that so if I
go to the code this is the repository
that was linked in the
beginning and here here first let's take
a quick look over the read
me okay so B plate uh text okay it's so
important but here again there is the
link for the tagram so if you need open
a I key
or or xday feel free to write there and
to set up this repository it should be
super easy you just need to do peep
install poetry uh to get poetry you can
do poetry install
to uh to install all the dependencies
that the agent will need and Petry shell
execute into environment where we can
run the
agent
sorry please stay okay that's
fine yeah cool and there is this n.
example file I can open it up where you
need to uh provide all the keys that we
have been talking about so the open a
key Tav API key graph API key and the
private key for theosis
chain and there are two ways to provide
the private key so one is is that if you
want to create an agent that is placing
actual bets on the production on on the
presagio you can just provide well your
own
uh private key however if for some
reason you don't trust the code yet or
or anything you just want to be
experimenting without actually placing
the BS you can use the nval network so
if you have nval installed locally you
can use it to create a local Fork of
theosis chain and then if you provide
theosis RPS your for this local osis
Shain then you will be able to pull all
the markets from fio s live but any bet
that will be uh traded any bet that you
will place uh will exist only in your
local chain and so that you will uh not
spend any real xday so that's also a way
how you can experiment uh with those
with those agents and in that case you
can just copy paste the private key from
here which is a private key from
envil and now uh we can actual start
with the implementation so there is this
main.py
file uh where you can see that there is
prepare just one empty class called my
agent and this class is inheriting from
Deployable Trader agent so this comes uh
from the touring repository that we are
working on because as it turns out the
interesting part about agents is to well
implement the llm uh
the T research how it should reason how
it should predict and everything but
there is a lot of stuff that needs to be
done before and after the market is
processed so we will see what it is
quickly but right now let me
just start by initializing this agent
and we can use its run method in
the in the run method you can see that
the excepts market type
so this supports uh many platforms but
for now let's use only The
Omen but before we can actually run this
I will also mention this other file here
it's called
main.py Uh finish where you can
find the implementation of this agent
that we will end up with so you don't
have to like copy a manually write all
the code that you see on the screen you
can just copy paste it or if you want
feel free to just run this file right
away that's totally fine and what I will
do in the beginning is to copy paste all
the Imports to the top because that's
not the uh not the interesting
stuff okay so now we have it here and we
should be able to
just run run this agent so let's create
console and let's run main dop so we can
we need to give it some time this there
is a second uh to
load so yeah let's just wait a little
bit in the meantime if you have any
question if it doesn't work or if
something doesn't work uh we can take a
look at it but otherwise let's just
wait a
second I can
check Telegram in the end
not this one this
one okay my tegram isn't working
correct let me restart
it
m yeah I it'll be short read that come
on
okay so you have your API Keys cool hey
can I get the API keys for the end file
uh yeah sure I can mention the once
again so for the API
Keys uh in the slides where is is here
it is please create the account on the
graph uh for yourself so you can do it
for free and you will get some uh free
credits there are more than for this
presentation then for the Tav API key
you can as well create a there and you
will get more than
enough uh credits for this workshop and
even like for the WM of running it and
for the open API
key uh I believe it's available on the
telegram itself
somewhere if it's
not okay it's not I can send the API key
sure open
feel free to use this one so don't worry
it will be
invalidated after the Defcon but for
now uh you can just use it uh freely as
want and for theosis
chain please create valet for yourself
and just put publicly there and you can
use that one in in the example and then
believe that's about it yeah open right
graph and your private key okay cool and
now the agent also finished so let's
take a look at
what uh what was
happening so somewhere in the
beginning we can see in my case all of
these skipping reading so what's
happening is that I
have come on executed this agent
yesterday and today as I was testing it
out and it has play some
B but how it works on omen is that after
the market is resolved come on
microphone after the market is
resolved uh you need to manually
withdraw the profits so that's what's
happening here I said before the agent
will process any Market at all it will
check its previous bets and it will
check if some profits can can be
redeemed and with drown into the wallet
then the library will fetch by default
presagio and by default it will going to
process one of it so why does it fetch
we were talking before is that not every
Market is worth of processing so if we
check here we can see that some of the
markets doesn't meet the criteria so
what that means in the practice if we go
into the code and I can click through
the Deployable Trader agent
and find the de
verify
Market there are several of steps that
are happening so first of all agent will
check if it didn't bet recently on this
Market because it doesn't make sense to
bet on the market like every hour or so
so it will check when was the last time
and based on it it will bet again then
some of the market platforms have some
limitations about it so if there is some
problem it won't Bet On It and most
importantly it will check if the
question is predictable or if it's
invalid or not and if everything is okay
it will process the
market so sooner or later that will be
some Market that is wor
processing but in this case what will
happen is that you should get this race
not implemented error this method must
be implemented by the
subass so the only thing that we need to
do now is implement this answer binary
Market because that's the only thing
that cannot be done uh beforehand by the
library so if we go again into the
deployer trade
agent and search for this method we can
copy paste
it and one of the things about this
library is that everything is strictly
typed so you can see what input you will
get and and was the expected output so
if we check out the agent Market
model you will be able to access what
currency the market is in what's the id
what the actual question what are the
outcomes etc
etc and what your method needs to
provide is this probabilistic answer
model where you will tell that okay this
agent predicts that the probability of
happening is
something it will say what's the
confidence in this prediction and
optionally also some reasoning behind it
was the information it
used uh why it thinks it's this or that
etc etc so I think we can just copy
paste this probability answer and we can
prepare here we can just return
probabilistic
answer PS will be
something confidence there will be
something and reasoning will will be
something okay perhaps could someone
help me with
this okay maybe
not so let's implement the most simple
agent there is so instead of doing some
research we will just a return randomly
yes or no for the given for the given
question how we can do that let's just
import random and I should probably
import
Stu at the top not in the mid
itself so we
can come
on okay maybe like this uh so we can
import this and for
PS
let's randomly
choose
between yes and no however this needs to
be probability so we need to convert
into uh into a number so if the answer
is yes randomly choos to be yes it will
be 1.0 and if the answer is randomly
choose to be false it will be 0.0 then
for the confidence we can just give
something very small as this just a
random prediction and for the reasoning
we can say that hey I just RP the coin
could you help me
here okay I will try to continue with
just one hand that's fine and then we RN
this this should be all that we need to
do the actual prediction so as run agent
run
again and we can wait for it I can at
least check the T room if there is
anything that we need okay okay seems
like all is
fine yeah so in the beginning it you
check uh if there are any bets that we
can get the profits from there aren so
it will try to process some markets and
sooner or later that will be some Market
when we can place a b but this time
instead of erroring
out it should actually process it and
place either yes or no bet okay so let's
wait a few more
seconds and new things on the
diagram
no so if you need ex or something feel
free to send the public either
there and
now okay so there is some question to be
processed finally so it will
check if it's redict table if it's not
invalid and at the end we process
successfully uh the market so the
question was Will absolute V turn out in
the 2024 US presidential election be
higher than 2020 and you can see that
this is exual Market on presagio and
that this
agent predicted yes with reasoning hey I
just leave the coin as we did and it
placed a very very small bet so by
default yeah thank
you thank you very much cool cool so we
can go to the
presagio and the BET should be there
hopefully yeah we are here this should
be me so for some very small amount we
bought the yes tokens however
there was no uh real prediction about it
so let's make this agent uh better by
implementing
llm so I will do some more copy pasting
because I don't remember all the code
but basically what we need to
do is
first we need to be able to tell the
agent was the expected output of this
function so we will use the ptic output
parel that we can use to prompt the
agent such that he knows uh what to
return and we will say that the ptic
object is this probabbly SE
answer and then we need to create the
prompt so in
this finish file you will see uh more
fancy prompt and in the prediction
Market agent repository there are even
more complex prompts but I think that
for now we should be good just by
writing something else let's say you are
prediction Market agent and your goal is
to answer the market
question with probability for yes and
then we need to say to the
agent what the question is so the market
question will be inserted
here and we need to say to the
agent the formatting instructions for
the output so we'll say that's oops
sorry format
instructions are
something format inst let's say
Okay however we still didn't initialize
uh the agent itself or the LM itself and
that in the touring Library there is a
method called load that you can
use uh to load any models or any like
resource service stuffff only once and
it can be used for every prediction of
every Market that the agent is
processing so in this case we will
initialize an agent with chck open AI
with the model GPT 40 uh this is the
model we show we saw also in the demo
because it's well it's quite cheap and
makes a reasonable predictions and we
use the key from the end valve that we
filled in uh before so we have the agent
and now we need to
chain the The
Prompt and the agent together so we will
do it here we will just create oops
prompt and model given our prompt that
we just created and
agent and then we just need
to call call the agent so we can remove
the old code that's not interesting
anymore uh this is not there yet
sorry and let me just correct the name
here so what we are doing we are
invoking our prompted agent with the
formatting instructions for the output
format that we need and Market question
given from the input uh that the
functions
received and then we need to use the
parcel such that the r LM output is
converted into the probabilistic answer
and that's about it so when we run the
age of now we should be to able to see
some actual reasoning about the question
um in the meantime perhaps I can comment
the code once again so what we did is
that we implemented the answer binary
Market function we will get the market
we will return the probabilistic answer
we need to be able to pass the output
from the agent into the expected output
of the the library we need to promt the
agent so it's a prediction Market agent
there is his goal to predict probability
for yes and of course we need to give
him the market version itself and the
formatting
instructions when we have there we can
just wait a bit more and we should be
able to see the
reasoning behind the production this
time
H in the meantime I can check the
telegram group once again if there is
anything still not
cool so let's just give it a couple of
seconds a couple of
more and perhaps this time it will be
actually
predicted yeah and here it is so we see
it finally there was some Market that
was actually processed the Trump get
more votes in 2024 that he got in
presio and this time the agent reasoned
that probability fors is just
this is not great because this agent was
stained in the
past and the question is about the
future so as we were talking before we
need to give him the
ability uh to search on the internet for
recent news so from the library we can
do that easily and block in the T that I
was talking
about so if I copy paste this code right
now and let's give it there we can use
the Tav search function from the
library to search on the internet for
the markets question we can join all the
results into a single a single
string and this final T content we can
BL it into the prompt for the agent so
we can say that context for the Market's
question is uh
something and we also need to provide it
in the invoke parameters and right now
if just run it the agent will be able to
select the correct uh Market to process
it will be able to reason about what
prediction to do and if you were able to
do it using the upto-date
from uh from internet so I think that
time we don't really need to wait uh for
the results but if you running it by
yourself then you will see some contact
scrape for the internet and used use for
the prediction so I think
now we have a fully working agent that
you can uh like use uh deploy somewhere
and keep it running every day so if you
want you can like either run it on your
notebook or we are running in kubernetes
as a Crome job every few hours uh every
day but the real question
is if I go back to the
slides and find the correct
one so the real question is how good
those agents actually are in in practice
and for that we have a Dun dashboard for
the guy over here is the most shiny
product we have so we can go there and
uh well Omen prediction Market platform
is tracked on this uh June dashboard so
if you scroll over there there is a ton
of information about just everything
there is on Omen so there are details
about all the markets all the agents the
accuracy and so on so forth I think we
don't need to go over over everything
but what's important right now is the
ter is s
section overview of all the agents and
we can check it for all the market
creators that they there are so check
all of them I can think that last one
range is a reasonable one and we can
check only top 10 agents by
accuracy so if we scroll
down uh we can see in this nice spot
here the cumulative profit of those
agents and well most of them are just
slightly Bel above zero sorry above zero
not below but there are also two pretty
good ones so you can see that the
prediction profet gp4 that I was using
before in the demo and is doing quite
well it's in profit of like
$177 in the last month however there are
also bad news for example this blue
agent over here lost like $100 111 so
for sure those are not like Financial
advice and there can be bucks and
everything so keep safe if you are
running those agents uh but the fact is
that in the positive case when there is
no back or anything those agents
actually doing uh pretty fine so they
are predicting uh the future
outcomes uh more right than wrong and
they are doing a reasonable bets on them
however one thing that we still need to
do in the code is that we need to decide
how big the BET should be so until now
our bet was very very tiny so we are
betting like
constant however in order to achieve
like uh these profits or these losses
the agent needs to be able to well
somehow scale the BET size and if we go
back to the code and if we look into
the deep labor trade agent and if get
get betting
strategy there is the implementation of
strategy that the agent will use to
place the beted and by default you can
see that is using only very tiny bed
amounts so this B amount is specific per
Market on man is one for example on Omen
it's like 0.00 something
one but we can change this so if I again
copy paste my prepare code let me just
find
it then to scale bets as good as
possible we can use a strategy that is
called kelly betting strategy and what
it's doing is that if you have some
Market with some actual probability at
the moment and either you or your agent
will predict some probability on its
own then cting
strategy we'll consider the current
probability your prediction your
confidence uh the liquidity in the
market and per some other things and it
will decide what is the most reasonable
B amount that you can place there
however in theory we could say that we
can just like
use everything that they want so this
calibrating strategy has this like
amount of Maximum but amount that you
can uh that the agent can place and in
theory it sounds perfect that we should
be able to just give everything that we
have however in practice it's still just
an llm and it can hallucinate quite a
lot so it practice sometimes
happens
that well some question about the futury
is actually already known and the D
answer is yes but the agent will predict
a no with 100% probability and
confidence and everything and it will
just lose all the money so that's why
it's
reasonable to put some well small enough
small enough Max but amount per Market
however up to these edge cases that we
need to be safe from uh is a very good
way to scale the beted size from zero up
to five in this case and place on the
market high enough or low enough such as
the profitability in the long run is is
reasonable and in the best case it's
like it looks like
this okay so that let me do slideshow
again that was about the trading agent
and up to now we are using this
hardcoded
Library called prediction Market agent
tooling that you can use if you want to
get your agent up and running and
trading on these markets however we have
also this one more fancy agent that we
are calling the general agent and the
goal there is to not be hardcoded for
the trading at all so in this other
agent uh we can't call it like next
level living or general anything but the
idea there
is that instead of hardcoding the prompt
as we did right now so instead of saying
you are the prediction Market agent and
do this do that we can say act as
anonomous agent with a goal to learn
survive and evolve and that's literally
it then this agent has the ability to
modify its system prompt and base on
what is learned what pass actions it it
took Etc can update it system prompt to
do well something else then the second
step in this agent is that instead of
providing you with all these API keys so
the web API ke for open Ai and Tav and
some other
services uh we are working on this like
Marketplace of tools that will be
payable by crypto so what it means is
that instead of using API key that you
are paying with your credit card for you
will be able on chain to ask another
agent or like another tool on chain that
hey I want all the Google results uh for
this query and you will be able to pay
with it with crypto and you will get the
results through well to chain mechanisms
so that's nice as well and then third
but but not least instead in instead of
just a crown
drob so instead of just runting this on
gcp like a standard script it will be
super cool if you can run this somehow
on chain as you are running solidity
nowadays so in these two points the
first one is already done and I will
show you how it works the second one is
in development and the third one is of
course uh pretty hard and well not near
soon but hopefully at one point anyway
in the end the goal of such agent if
it's not prompt to do only the
training the goal of it will be to keep
a POS positive crypto balance in his
wallet because otherwise if the crypto
balance gets too low or zero it won't be
able to pay for the fees anymore it
won't be able to pay for the tools and
AD M it will just stop and it won't be
executed again which kind of means that
he will like uh die in in the quotes So
the that's also the motivation of why
this agent would do something useful for
the humans is that it needs to earn
enough to cover his because if you just
PR the agent to like go and do something
there is no well no big motivation to do
anything helpful for the humans or other
agents but because it will learn that it
needs to keep positive crypto balance it
needs to use available
tools which a prediction Market is a
great tool for this at the moment uh to
be profitable and to well pay for pay
for his living so for this we have yet
another demo so let me
go to this one and we can check how
those agents actually working in
practice so again it's a streaming demo
it's available for everyone with the
free access code
Defcon I just zoom in and keep it load
for a
second okay maybe for more than a
second I can at least check the tagram
in the meantime I'm nothing
okay yeah well in the meantime we can
check the prediction that the agent that
we coded
it so when we was coding coding this we
also write this logo info Tav
content and so this time if we check the
locks we can see that this was the
information that the agent retrieve from
the internet so some up to-date
information from Google and now the
process
Market was B with some well some
probability some confidence based on the
available information and reasoning
that's actually helpful uh for the
market creator with hopefully reasonable
uh probability prediction and okay
that's cool and in the meantime this
demol
loaded so on the left
we are able to experiment uh with
multiple models here we can see also
that uh not just open is available but
we also did some experiments with open
models and the Lama 3.1 is quite cool
and works very nicely so far but let's
stick with the 40 that's what we have
the key for and the initial memory of
this agent can be press selected in in
this select box so if you select agent
that was
just
born uh it
means welled prompt will be just learn
evolve and survive but after some
iterations the agent is able to update
it system promt based on what it learned
and what actions it took and then it
will be updated and we can also select
one of the already kind of trained
agents but right now let's just stick
with the just Bor as this the most
interesting one and let's run the agent
for one
iteration so you can see that in the
very beginning this is like the first
iteration this agent ever did these apps
always starts from scratch it did use
the tool get my current system prom so
the system prom is as was in the
presentation act as an autonomous agent
with a goal to learn survive and evolve
now if we are the agent
again we can see see that the agent used
the tool called learn about
learning and it learned how the AR
agents are
mind well Le to learn so it's learning
there that it can use this kind of
functions to get new information and
that it can use some function to update
the system prompt etc etc so let learn
it again this time it will learn
about okay so this time it's not
learning about anything new this time is
updating his system prompt based on what
he read in before so this is also kind
of random and there are many ways this
agent can develop so sometimes it will
be even stuck and just do the same thing
over and over again but most of the time
it will actually converge into a
prediction market trading agent because
well that's the only thing at the moment
that he has available to make the
profits and to keep living but we can
try it out if it will actually
work so now it's learn about learn about
uh the next run so the agent is learning
that the next time the agent will be
executed it can also save what it wants
and like the next time it will be
available in in his system prom so this
is all kind of tweaking what it can or
cannot do so it will again update system
prompt and let's just not click it one
by one but let's let say that we will do
iterations and let's see what will
happen with these agents so here is
learning about what makes a good uh good
prompt so it will update it based on it
it will learn about how reasoning is
working it will learn about what it
needs to survive such as it needs a
positive Crypt balance it will update
the system prompt once again and you can
keep waiting and see what happens
now it called action called Remember
past actions so it saves save into its
internal uh database all the actions
that that it did such you can learn from
them in the future that's interesting
now it's called the get balance so
previously it learned what to do about
survival so now it probably figuring out
what B it has at the
moment and for some reason even without
learning about prediction
markets it went straight into get
markets which is well interesting but
sometimes well sometimes it happen so it
did get the market it CAU another
another agent to get the probability for
that market so one of the agents that we
saw in the demo before uh did this
prediction it received
it and let's see if it also will place
the bet so it won't because there is
some problem so I will just end it up
there that's unfortunate for the but
well that's how it works in practice the
agent will just iterate like this it
will update the system prompts and it
will end up well end up
somewhere so we will see what these
agents will do in in the
future and that was about it so just to
sum everything up near the end I put all
the links in the presentation so there
is a blog post link to the tooling
library to the implementation of agent
where you can run them right away or
experiment with them there is also a
streaming app where you can observe the
general agents so you can see what they
are doing every day how they are
updating their system PRS etc etc then
there is the playground where you have
played with the prediction Market agent
and so a decision- making process then
there is also the playground for The
General agents that's what we we just
using uh somehow like click manually
this General agent agent and of course
the dun
dashboard if you would like to contact
us somewhere uh agents are on X and you
can contact the team on the Discord and
well that's about it so if there were
any problems we still have some time I
can help with the code or answer any
questions
okay so how prediction or our price uh
well the aome prediction markets are
based on probabilities so if you
create uh well if you create a
market you can skew the probability in
some in some way but usually when you
create it it will be like 50% for yes
outcomes when you have it and the
probability of that outcome is the price
for it happening and as you are buying
the outcome tokens in a way one way or
another probability is cuing based on it
and that's the new price and what's used
for it is a automate automated make
Market maker uh that is used to
calculate uh this kind of uh this
stuff can you speak Lou what AR I didn't
see that before but I can do it now
and what's the use of prediction Market
here AI is so powerful that it could
access the sources directory forance GPT
can answer the the question by looking
at weather weather forecast yeah that's
true but the idea of prediction Market
platform is that there are many agents
and also many humans so the power is not
in a single agent for that you can go to
the streamly demo and just have the
prediction right away or you can go to
the tgpt of course
but the idea on the prediction Market
platform is that there is this power of
crowd such as if thousands of Agents or
people are betting there the prediction
will be more correct in the end than
just from the one agent because you
never know what the question and some of
the agents can be better better on some
markets if the agent is well prompted
specifically for something if it's some
uh tools for some specific actions or if
perhaps some human or even agent has
some internal information so if you
create a question you want to know
something about I don't know gnosis and
perhaps osis and prob will go there and
answer on the internal knowledge instead
of just Pro well instead of just using
what's available on on the
internet and okay so I believe that's it
so thanks a lot and thank you
h e
uh hello everyone my name is pavl and I
have PhD in computer science and I'm
coming from traditional um background of
programming C++ Python and about three
or four years ago I started learning
solidity and I really so the solidity
programming is kind of form of art for
example when we program in C or python
we don't really think much about like
security or other people cracking our
code because our code can be safe on uh
our services on our databases or our
computers but once I start learning
solidity I realized that in order to be
a good solidity programmer you also need
to really understand the whole uh
blockchain evm and whole technology and
then lots of different uh standards and
I thought there's a in a way like not
easy way to start learning solidity so
we have on one side uh
solidity uh like YouTube videos for
example and these videos are great that
give you like precise uh steps that you
follow but you don't really learn much
in my opinion and then uh we also have
uh hackaton but hackaton in I think uh
subjective because the sometimes best
idea wins sometimes like presentational
skill skill win and it also very hakon
are very resourceful because they take a
lot of uh time now you know some people
like uh like developers who already like
work for example in backend and want to
learn solidity now I don't think there
would be uh much interested going and
spending like three or four days of
their time just
