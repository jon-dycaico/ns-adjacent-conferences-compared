a bunch of tests in solidity then
Foundry is probably better but in this
case I'm just going to deploy a simple
app so I just went with hard hat but it
doesn't either either one is just as
good I think uh hard hat is catching up
to Foundry in terms of speed but Foundry
is faster right now and great for uh
like I said writing your test in
solidity uh but I just went with hard
hat today but it was just a random
decision it could have been either one
so uh we're g to let this install and it
will take a little bit uh definitely
there will be time for Q&amp;A but if you
have questions along the way just like
shout them out and I can repeat them and
try to answer them so so feel free to
just shout questions out this should be
like very open-ended I'm going to go
through building something with the
tooling and just kind of show off both
writing the smart contract and the front
end and then deploying the app
to a chain we're waiting for it to
install right now
though and actually while it's waiting
for that I could pull up
cursor
or VSS code whatever your uh preference
is I kind of like cursor because I can
throw some prompts at it and it'll do a
little AI stuff for me here and
there let's see
okay uh let's see I want to CD into to
Devcon app nope not demo app done this a
few times
before
Devcon there we go and I'm going to do
uh so after you clone down the repo you
get this list of commands you need to
run so we're going to do a yarn chain
and that's going to spin up our local
blockchain and then we'll do a yarn
start and that will bring up our front
end and then we'll do over in this
terminal uh here whoops we'll do a yarn
deploy and that's going to deploy our
example smart contract to our local
chain oh
CD Devcon
app yarn deploy let's see if this
works okay so this is this is kind of
the starting point you have your uh your
code up here oops Devcon
app you have your code here and you kind
of have scaffold eth over here and uh
let's get right
into the smart contract so here is our
smart contract uh scaffold eth comes
with a uh kind of example smart contract
that has uh a handful of different
concepts already built into it um
Primitives and data types uh you've got
events uh modifiers Constructors all the
all the good stuff here is kind of just
an example smart contract for you to
quickly just kind of Tinker around with
solidity uh but it's a greeter contract
right classic greeter we can set the
string and uh looks like there's some
extra logic here keeping track of how
many times and maybe this uh this is an
interesting thing here if you send in
money it's going to set some premium
flag to True right so let's go let's go
test that out let's go play around with
it so if I go to Local
Host our web app should come up
here and what I'm going to do is just
dink around with this uh set greeting
first just to make sure it's working the
way we think it is okay so here's our
app this is how it uh comes out of the
box and I'm going to jump over to this
debug cont contracts Tab and that is
where you can really kind of iterate and
see your contract and kind of poke at it
so uh there was this set greeting let's
say hello world this is going to
complain that I don't have gas but
that's okay let's let's hit it and let's
see what it says it says oh you don't
have any gas so uh scaffold eth uses
burner wallets when you're working local
when you're doing local Dev it's a lot
easier to just use a burner wallet
rather than have like metamask and have
to set the chain ID and you know have
all those problems that come along with
that so you'll see here I just have a
burner wallet here this is just a an
address that's generated and to show
that off if I just open up Local Host I
get another address see that there's a
new address there let's do that one more
time let's just open an incognito window
and go to our app and you'll see I get a
new address every time because of that
incognito window uh because it's stored
in local storage so bad idea to have
burner wallets in production great idea
to have burner wallets for Dev because
you can quickly uh just kind of like hit
buttons here and make transactions
happen without having to uh you know
have the metamask prompt come up so uh
right here is a faucet that's the second
thing I need so I've got my burner
wallet here and I'm going to hit this
button and it's going to give me some
eth so now I have eth for gas now let's
try this set greeting one more time and
see if this works there we go hello
hello world so we were able to uh let's
say Hello World 2 let's try it again
we're we're able to send a transaction
and that's going to update the greeting
in our smart contract and uh let's go
try that that premium thing let's go
look at that one more time right here it
says if if there's value it flips this
premium flag to True whatever that is so
let's send in some value and you'll
notice I can't do
amount of eth it's a decimal you have to
multiply it time 10 18 and so scaffold
eth has that little button over there
that takes it times 10 to the 18 now of
course you wouldn't want your users to
have to type in you know 0.1 and then
hit the times 10 to the 18 this is very
much built for a developer and it's
meant to kind of expose you expose to
you what's happening kind of underneath
the abstraction but I need to hit that
button to take it to way and then let's
see what happens all right hello let's
say let's say Hello World 3 even in
value now you can see that there's money
that's getting collected in the contract
and that premium flag got set to true so
this this is kind of like the the core
game Loop you want to get in with
scaffold eth is you want to have your
smart contract up over here and then
your front end up over here and as you
add things to your smart contract your
front end will Auto adapt to it so let's
just go uh add some thing here uh let's
say
um maybe we want to make a mapping
balances that looks good so for any
given address there's a un 256 so
there's balances and then let's make
sure let's make a function called
transfer right and hopefully just the AI
writes this for me and I don't have to
do anything but basically we made a
mapping that keeps track of balances for
any given user and then we have a
function that allows us to transfer that
balance and let's deploy it and go to
the yarn deploy we'll get some more
stuff over here there we go so now we
have balances here let's check my
balance it's going to be zero right yeah
I'm gonna I'm going to need an initial
balance so let's copy our address and
let's go back to the
Constructor and let's set this dude's
balance so we'll say
balances of
this address and and trying it out so
what we want to do is say hey do we have
a balance for this address we do okay
and then if we wanted to transfer let's
send one to vitalic
right you'll notice this does ens
resolution it has a nice ens Avatar this
is something that you get out of the box
with scaffold e it's made for uh
building apps so it has all of these
components that you'll use to to build
your app quicker so let's send one to
vitalic here we
go uh oh uh oh
uh uh actually it's a thousand way right
so I should not have done this thing I
should just do one there we go yeah I
didn't have the balance to send to him
and then if I go check my balance again
it should be $9.99 right okay so we're
kind of in this Loop where we're able to
write some solidity and Tinker around
with it and the front end and try things
out so let's let's let's think of an app
to build let's say we wanted to make
like a a really really silly prediction
Market we might need uh an address that
we would call the
Oracle okay we're going to say address
public oh
man uh and I'm GNA call this the
Oracle and I'm going to set that to I
don't know this dude's address I guess I
don't really know what I'm doing right
now I'm just kind of tinkering around
trying to figure out what I want to do
and then let's say there's like maybe
three possible outcomes in our
prediction market and I want people to
be able to buy into any given one of
those uh things so let's see maybe we
have like a
function called like purchase I don't
know and then let's do like a u
index and it will be
payable hey that's pretty good let's see
what this is no I don't think we quite
want that let's see what we want to do
is keep track
of uh how much someone has paid
into this so it's payable yeah so let's
see let's do this let's do let's see how
should we do this maybe like an
Ane uh let's let's do it like this let's
do a
mapping for an address to a number and
then actually I want another mapping
inside of that maybe uh maybe this is
too complicated maybe I should do
something simpler uh maybe I shouldn't
uh build a prediction Market maybe we
just uh let's just sell some things how
about that how about we let someone buy
a thing in our contract and uh we
trigger an event for it or something
like that maybe they purchase an item
and the index is that item and so we
might want to emit an event here um
maybe we want to trigger some other
action um let's yeah let's get rid of
this Oracle let's just go with purchase
and let people buy something and we'll
uh trigger an event and we'll let them
send in money but uh I don't know maybe
maybe there's like five or six different
items and they're buying those items
maybe we want to require how about we'll
require that they send at
least uh
send at least there we
go okay and then yeah yeah maybe we yeah
increase let's see
balances yeah maybe maybe let's do a
mapping and we'll have an address to
account and this would be like items
bought I I don't know we're just kind of
dinking around around here playing
around so we'll keep track of a mapping
of items bought and so then when someone
goes to purchase this item we will set
items bot message.
sender plus equals
one and uh yeah I don't know I don't
know what else we'll do but it's it's up
to you you guys are the solidity devs
it's up to you to really write this
logic in you can build uh you know
whatever you want I'm just kind of
showing an example app here so I guess
we let people purchase something and we
keep track of the items uh bought let's
let's go play around with it and see if
it works so let's go ahead and deploy
this and let's go see if we can buy some
items from our contract uh oh what did I
do
here uh balances right yeah get rid of
this kind of like the prediction Market
idea I should have uh prepared it a
little bit better but for now we'll just
have a little store that let people buy
things so let's try that out so we've
got this purchase function now that lets
people put in an index we'll have that
in the front end so let's say you're
going to buy item three and you're going
to need to send in
we go so it did work I was able to
trigger the transaction and the money
went into the smart contract but now
it's got me thinking H what happens if
that money gets locked in that smart
contract I should probably set up some
kind of kind of like owner and it looks
like there is an owner already here uh
looks like it's passed in through the
Constructor let's go look at that it's
the deployer let's set us up as the
owner
okay and let's redeploy it and see how
that looks what I want to do is make
sure I don't have money locked in the
contract I want to be able to withdraw
the money I guess so if we were to put
this on a live Network we wouldn't want
a bunch of money to get trapped inside
the contract so let's see we're going to
buy item two for Point
goes into the contract but now the
question is can we withdraw that money
back out and I'm going to there's a
withdraw function here let's go look at
that in the code real
quick it was built into the contract
before it looks like it checks to see if
you're the owner and if you are it sends
you the balance uh of the contract
that's perfect let's try it and see if
it works so we have what like $3 in the
contract and then we hit
withdraw and hopefully the money's gone
Okay cool so you'll spend a lot of time
in in this Loop where you're tinkering
with your solidity uh you're you're in
the front end poking at your contract
you're adding new things to your
contract uh kind of like what I was
doing there where I was like oh I'm G to
make a prediction Market okay now I'm
just going to make some items that you
buy like you're you're still kind of
playing around but scaffold eth lets you
get in this Rhythm where you can make a
small change in your solidity and then
go Tinker with it uh in your front end
with this nice Auto adapting front end
but let's say we're we're pretty happy
with it right let's say that we like the
way our little store works here um and
we are going to now maybe work on the
front end a little bit okay so what is
it it's not happy about this oh you know
what we should do we should uh maybe
emit an event right
emit yeah something like that and then
let's throw that event in
here yeah there we go nice and then yeah
the index is there it's still not happy
about that is it let's see let's see if
this
works as long as it compiles I'm happy
okay so now we have an event that is
emitted when we buy things but let's go
try to buy you know item number one for
works okay cool so uh you'll spend more
time on your smart contract but let's
say that I've spent weeks or at least
days working on my Smart contract
getting it right uh really I'm just kind
of tinkering around so I have this
simple uh little little bit of code but
you you'll take more time you'll spend
more time on this you'll you'll get it
working you'll probably want to even
write a bunch of tests for it and stuff
but let's say we're happy with it let's
say that smart contract basically does
what we wanted to do let's let's now
move on to building the front end and
have uh some react tuck to our smart
contract so uh the front end will be
over Let's see we probably want to let's
just have like a couple of buy buttons
and a thing that says how many You'
purchased or something like that right
that'd be a very simple front end so if
we get out of hard hat and get into
nextjs we can find our app
here and this is this page so if I go to
home there this will take me to this
this front page here so what I want to
do is kind of clear this stuff out and
prepare for adding some
code let's see let's clear all of this
out
who let's see down to
about
here how's that look there we go okay
and so then instead of Welcome to
scaffold e will'll be like welcome to my
cool crypto store or something like that
right all right oh I spelled it
wrong c r y p t there we go all right my
cool crypto store is ready for business
now uh you'll see that we're using wag
me for the use account I can get rid of
some of this
stuff and so uh the wagm docks are are
always really e uh really nice if you
need to look anything up we can just go
uh look that stuff up right now uh for
instance we're using use account right
we could go look that up see how that
works but what it's doing is giving us
um uh the basically the logged in user
here the connected address is what we're
renaming it to and then we're displaying
it here and that's what creates this
nice thing right here and so just to
dive into that a little bit more look
look at how this address looks if we
were to take this address component out
and just have the raw address right in
our front end it's going to look super
ugly but let's do it just to do it just
to see it okay connected address if I
hit save oh
no uh there we go yeah that's what I
want there we go so now we have like
this really ugly address right and you
don't want to display an address like
this in your front end for your users
you'll want to have that nice address
component wrapped around it let's do
that again I think I can just undo a
couple times just to see the difference
between this okay so instead of just
just displaying the raw address we're
going to pass it into this nice
component and when I hit save here then
we get this nice looking component that
has the block key or the ens Avatar the
nice little copy button and then if I
click this it's going to take me to the
block Explorer so right now we're on
Local Host so it's just the Local Host
block Explorer but if you were on a live
network uh and you clicked that address
it would take you to that address on the
Block Explorer whatever Network you're
on okay so uh let's set up our store
right I'm guessing we probably want to
have some like buy button and then we
probably want to like read how many
items we've purchased or something so uh
to do that let's go look at the scaffold
eth docs normally I would probably
already be just like prompting cursor to
write this for me but I think it's a
good practice to show y'all off y'all
how it works uh so instead of prompting
the AI I will actually just like build
this thing
okay so what I'm looking for is the
let's see interacting with your smart
contract and I want to specifically do
use scaffold read contract right so this
is how we're going to read from our
contract I'm just going to copy this
code exactly and paste it into my front
end if I can grab a hold of it there we
go okay and we're going to put it with
our other hooks here okay
and we're going to uh import it okay and
so uh this is really nice because
anytime you make a change to your smart
contract those artifacts are
automatically injected into your front
end so watch this if I go to this
function name and I do open quotes it's
going to give me a suggestion for all
the different items that are in my smart
contract this is really nice and I can
go here and say you know total what like
items bought I think is what we're
looking at
okay and then that's going to come back
here and let's see does that take in
what do that smart contract look like
items bought takes in an address right
so we'll need to
have uh our address here and we'll say
this is the connected address right so
hopefully with just this line this line
of code right here basically what we're
doing is we're going to our smart
contract and we're reading how many
items we've bought and we're storing it
in this object right here so let's go uh
maybe down
here uh let's see maybe we'll make a new
div hopefully I don't have to center
it okay uh let's say items bought
something like
that and then that and I think I need to
do a two string here I think I've done
this a few times before and had that
mess up
but let's look and see what we have here
probably one okay there's one item
bought it's really funny that that's not
centered and I was joking about
centering a div but I'm not going to go
Center it it's going to stay like that
and let's go purchase like item five for
make sure we're correctly reading the
state oops begin right you need to hit
that button okay so let's go back and
look here now our items bot is two Okay
so it's keeping track of how many items
we bought and it's putting that in the
front end so we're successfully reading
from our contract now we want to write
to our contract and to do that I'm going
to go to use scaffold write
contract and we'll bring this in
here and we'll import
it and
and then we'll grab this button which is
exactly what we need it's for setting
the greeting so we'll have to do
something a little different but we're
getting close maybe we'll set up another
div here and then throw this in here and
then uh you can
[Music]
see oh oh boy oh boy I don't think I got
all of
it make sure I get all of that
that and then paste that in here please
work okay there we go so uh this is a
button and uh when you click it let's
see we're going to say
buy um a hat okay yeah this will be for
a hat and so that will be uh index one
maybe right and what's the function we
need to call we can do that same thing
where we open up the quotes and it goes
and looks at our contract and gives us
that purchase
function and what does that that
purchase just takes the index right so
we're just going to say hats are index
one for some
reason uh why is it not oh maybe it
needs to be a big end okay and then uh
value here we're going to have to send
in some money right 0
for
this and import parse ether from VM all
right let's look and see what we have so
far how is our app
looking so uh if I hit buy hat what's G
to happen here hey pretty cool yeah item
spot goes up and the hat uh and and this
increments right so maybe let's then
copy a couple of these buttons
oops okay so by shoes
whoops okay and maybe that is uh even
more expensive I don't know and this
will be item two for
instance okay let's go let's go look and
see how that looks so now I can buy hat
and notice like there's no metamask
popup because we're using those burner
wallets but eventually like we'll have
metamask and we'll have all that stuff
there so uh let's see if this
Works uhoh what did I do so I think it
needs to be exactly 01 doesn't it let's
try that okay cool so we have our cool
crypto store we have the uh uh items
that we've bought so far and then
buttons that allow us to buy more items
right very simple stupid app you're
you're the builders here you guys can be
creative you can write some good
solidity you can build the front end all
I'm trying to do here is to show you how
scaffold eth can help you build this
thing very quickly so uh we've got our
store basically working it's super ugly
but it's uh it's it's pretty good so now
I think the next step would be uh to try
to deploy this so let's see if let me I
I've got plenty of time I could
definitely like make this a little bit
more advanced but uh Maybe not maybe
let's just get this thing all the way
out into production and and try it out
first oh you know what I need is a
withdraw right I need to make sure that
this withdraw works but I can always
just come into the debug and do it so I
I think I'm happy with that yeah yeah
let's just go with that o maybe events
how about we list events that's a good
good thing to do here let's go
to yeah event history and I'm going to
grab this
and I'll throw it in up
here
okay and what is our event
name item purchased
cool so we're going to listen to your
contract item
purchased I don't really need much of
this stuff definitely don't need
that uh I don't think I need any of this
stuff let's see what happens
so we should get some events here and
then if I wanted to list those
events uh let's just like output them in
a really ugly way here oh hey how about
that oh thank
you let's see what that looks
like uh oh oh I need to import use
scaffold event history so I'll import
that there
there we go items bought we definitely
don't see our events though what do we
need to do to be able to see our
events event transaction hash what is
this I don't even know Let's do let's do
something like uh just like a pre and
just like spit the event out oh I mean
that looks all right let's go to console
log I don't know what it's
doing let's see uh what this event well
I don't even really care about this key
to be honest let's see oh man it's
freaking
out uh yeah let's get rid of that so
let's just have this div and let's
have uh let's see yeah let's see what
things we have on this
event
dot
Arc Dot
uh
buyer yeah let's see it is not liking
this what do I have wrong
here yeah okay no evance I'm scratching
it for now let's let's get this thing
built and
deployed uh I'll come back to the events
if I have time later
let's get our store deployed that's the
key
here okay how's that looking do we have
the store can I buy a hat can I buy some
shoes does the items go up does the
contract hold the money looks like it is
looks like it's all working still okay
so now uh
whoa Let's uh let's deploy this thing
let's uh let's put it all the way out
into production so there's going to be
two parts of that right we need to both
deploy our smart contract and deploy our
front end so that that will take
multiple steps here um oo I'm going to
venture into the yarn generate real
quick this is something new to scaffold
eth I hope this works I might have to do
some weird stuff here let's see if it
does Okay cool so to deploy an app I'm
I'm going to need a deployer account I
can't just use the like the zero account
on hard hat or whatever I'm going to
have to actually like create an account
and fund it and that's what this does
here it is yarn generate created my
account for me and then I'll do a yarn
account and that's just going to show my
deployer account okay and then I'm going
to send some money to
that what what network should we deploy
too bass okay anybody I'm I'm gonna go
to Bass here we go so I'm GNA put like a
dollar worth of Base into this deployer
account okay
$1 I'm going to use a punk wallet at
Punk wallet.io it's uh built with
scaffold e
one okay so now we have our uh smart
contract ready to go and I just sent a
few bucks to this deployer account so
now I'm going to do a yarn
deploy Das Dash Okay so yarn deploy is
what I've been doing this whole time
right if I hit yarn deploy it's just
going to deploy it locally but if you do
yarn deploy D- Network and then pick
whatever Network you want to deploy to
let's let's go to
Bass okay so hopefully this will deploy
our smart contract to Bas like a live
Network we're going to spend real money
and we're going to deploy a real smart
contract to a live
network with lots of time left I could I
could uh make a much more advanced app
if we have time okay so I I think our
app is deployed now but we still need to
do that front end part we need to set
the app to uh the right network uh and
you do that right in here there's a
scaffold config file this is really
handy this is where you set up all your
configurations for different uh
different things within your app and
we're just going to change this chain to
base and if I hit
save now come look come look at our app
uh you'll notice that uh the burner
wallet went away and now we have to
connect and we'll use
metamask okay and I'll connect
that o I'm not the owner though we
should redeploy this with my metamask as
the owner so I can withdraw the money
I'm going to do that so over in my
deploy
script uh it's setting who the owner is
right here I want this dude to be the
instead and let's redeploy our
contract and that that means that my
address will be able to withdraw it was
set to the burner wallet before and I
don't want the burner wallet to be the
owner because then I would have to have
burner wallets in production and it's
you you'd rather not okay now let's
check this out so if I go to debug who
who is the owner okay I'm the owner
great and if I were to purchase an
item like a
hat this is a real transaction now I'm
spending real money I'm putting money
I'm loading $3 up in this
contract uh yes I want to
proceed
bro okay there we go so we just made our
first transaction on our our smart
contract and let's see if our items bot
goes up and hopefully it does and also
hopefully yeah I can see that I just
executed on a contract too it's pretty
cool when it's a live public
network uh items bought is now one
fantastic okay let's let's buy another
Hat real quick just to load the contract
up some
more okay make sure that works make sure
items spot goes uh up again and then uh
what we want to do is go make sure we
can withdraw the funds back out of the
contract let's go do that next so if I
go to debug contract I can kind of like
go poke at my contract here and what I
want to do
is make sure I can withdraw this $6 so
let's make sure the $6 comes back out to
me when I hit this withdraw button
so we're watching this money here and
this money here to make sure that that
works yep got our money back okay cool
so our app our smart contract is already
deployed to base but our app is still on
Local Host like I said there's kind of
like two pieces to deploying this you
need to deploy your smart contract and
your front end so to deploy the front
end I'm going to
yarn
versel YOLO prod this is my my favorite
command uh and what that does is just
like it um ignores like type safety and
stuff is what that YOLO prod stuff does
I think there's some kind of like um
checks and stuff and I just don't want
to even deal with that okay so let's see
now uh
sure
no
no uh it's called Devcon
app okay and it's located
there and we'll no we don't need to
modify anything okay so now it's
deploying so we've tinkered with our
smart contract where we could set it up
so we have the smart
contract uh uh here right we had our
smart contract here and we had this nice
uh debug page and this was like our
initial game Loop right we wanted to
Tinker with our smart contract we wanted
to build our smart contract we weren't
quite sure what we wanted yet but we
could kind of like add things into our
smart contract and then come over here
and uh kind of feel how they how they
work right we can kind of see the things
here here and we can poke at them and
try them test our assumptions that was
kind of phase one was building out this
smart contract with this uh feedback of
the the debug Tab and then phase two was
kind of moving into the front end and
writing uh some buttons and some some
read and write functions right that's
that was kind of phase two and then
phase three was deploying the smart
contract and the app and that is on its
way to be deployed but we're waiting on
it for a little bit so uh there's
there's quite a bit I could do um to to
show off more uh scaffold e stuff but
let me just kind of like pause there and
open it up for questions and maybe those
questions will take us down some other
Rabbit Hole uh yeah go ahead
so uh you're saying like when I hit by
hat it immediately updates
uh uh there's there really small block
times on base so it's not like ethereum
where you make a transaction and you
have to wait 15 seconds for that to
finish like the transactions are
happening immediately because they're
going to like a central uh sequencer
does that make sense it's just an L2
it's just faster cheaper
L2 on eth it would it would take 15
seconds I would hit by hat and it would
wait you'd have to wait for that block
to get validated basically so it'd be
like a 15sec time between when I hit
confirm here and when it actually like
lands on chain
the scaffold
whoa uh so in a case where it takes like
on another chain like longer scaffold e
is like pinging the chain at all times
to to get the info yeah that's what that
that read function is is like constantly
reading and looking for changes uh let's
look at that right here this the items
bot right yeah all we said is go to your
contract and read items bought for this
address
and from then on this items bought item
is up to date with whatever is on chain
okay thanks does that make sense yeah
cool more questions anybody have any
more questions about what we've done so
far about how it works reading and
writing to the contract anything
else might just have to build oh here we
go we got a
question okay thank you very much uh
I've learned many things uh but but as I
was wondering whether uh I can choose
the account to use for
deployment because uh when you you
wanted to deploy the smart contract you
generated an account and send some it to
to this account before deploying yes so
is it possible for me to set uh the
account which I want to use to
deploy it's yeah so um that is a good
question so I just generated an account
and this is what I like to do is I I
like to have an isolated deployer
account that is just for this deployment
so I don't want to use another address
from somewhere else I want to create an
address just for deploying this contract
and put just enough money in it so it's
kind of like a one-time use account but
technically uh uh you could like set
some other uh deployer account in here
the the way I'm doing yarn generate and
yarn account is it's kind of handling
the address for me but I could get in
here and like change the private key if
I wanted to I think does that does that
make sense but you you really don't want
to do that it's best not to do that it's
best to have a nice isolated account
that you put just enough money in and
deploy with it does that make sense okay
thank you I have a a second question uh
as for the front end so you deploy the
the smart Contra on the blockchain which
is a
decentralized decentralized platform but
for the front end you you want to deploy
it on Vel so are there solution to
deploy the front end on the platform
which is also decentralized that is a
also a great question and I think that
it's kind of an elephant in the room
when we look at like decentralized apps
and they all just like live on verel or
something uh you can I think export this
you could do like a static build and
upload it to like ipfs or something like
that it's just not something we have
like I don't know let's if I do a yarn
ipfs does this work I used to back in
the day I don't think it does though is
Carlos and crew here I don't know if the
sand Garden's
here no I don't see them uh you yes I I
think the the short answer to that is
you could make a static build of your
website and upload it to like ipfs or to
other services but it's okay if it's in
versel because it's open- source and
really forkable so if someone wanted to
redeploy this somewhere else they should
just be able to Fork my code and bring
the front end up in versel or whatever
they want but good question though like
versell is centralized for sure and so
if you're trying to build a
decentralized app you need to make it in
a way where people can spin up their own
front ends or Fork your front end and
bring it up uh on any service but we we
just deployed to verel for for
this okay thank you very much yep good
good
questions okay let's see where our
deployment is did I did I do the yarn
versel did that
go maybe that already happened up here
let's see if our thing
deployed uh
yeah here it is
okay hey hey there it is okay so if you
wanted to go buy something from my store
you totally could right now uh I could
share this URL with you and of course I
would want to shorten the URL and uh
make it look nice but uh I don't know in
about 20 minutes we were able to Tinker
with our smart contract we were able to
deploy it to base and then we were able
to deploy our front end to a live URL
and let's go buy some stuff from our
store real
quick okay let's do a buy hat let's see
what happens here yeah spend some money
$3 okay and now this is at a live URL so
this this app is decentralized as far as
base is decentralized and versel is
decentralized someone could definitely
like Fork this and bring up their own
front end on Local Host
so uh but it is in versell and we were
able to buy a hat and buy some shoes
from our
store and we're making transactions and
they're
working uh and then maybe we should go
sweep that account uh and empty the the
contract let's let's go do that next
so let's go look at our contract has
like $10 in it
now and if
we withdraw that let's see what happens
please
work man that's annoying I don't know
what I'm doing why
it's okay now we're watching to see if
this money comes out of here here and if
successful then we built our first
decentralized store and deployed It All
The Way live and sold some shoes and
hats and then we withdraw withdrew our
money and it worked so I was able to buy
the items I have the buttons I could
even like send this URL to you guys you
guys could navigate to this and you
could buy hats and shoes
also uh more questions anybody have any
questions about scaffold
e I'll be doing a uh yeah yes
builtin sorry saw briefly show the
built-in block Explorer yes I think is
pretty awesome if somebody was using say
they wrote their own tests against Local
Host could they use the block Explorer
or would that would that work like if
they weren't using scaffold e if they
had some pre-written unit tests but
wanted to sort of take a peek into the
transactions with possibly yeah so let's
go well my now when I click this it's
not going to go to the block Explorer
it's going to go to the base block
Explorer but let's go put the app back
on Local Host and then we can look at
that so let's go
to yeah we we just barely touched on
that block Explorer let's go let's go
look at it so what I need to do is go to
my scaffold config and I need to let's
set this back to hard hat and hit
save and then our app is going to just
by doing that one change our app should
go back to Local Host oh I'm at the live
URL there we
go here okay and it's going to have me
switch uh networks this is really nice
by the way if if a user comes in and
he's on the wrong she's on the wrong
network uh you need to bump them over to
the right Network and so scaffold eth is
gonna handle that too notice this nice
switch but let's go look at that block
Explorer again so uh yeah I guess that's
for that
address what else can we see
here this would be all the transactions
here right and I can click in and see
you know there's a purchase of
so yes I think that to answer your
question you could use this block
Explorer to do some local inspection on
things uh I'm not sure if that was
exactly the question but hopefully that
answers it like think I've just been in
situations where I've wished for a a
local host block Explorer yeah yeah uh
what you can do uh so block Scout is
also another one you could go get Block
Scout it's an open-source uh block
Explorer and you could run that also
like bring up a Docker container next to
it and it would uh also work but yeah
this this is kind of rough but it would
work it would do what you want I think
it would kind of tell you you can kind
of see all the transactions there that
are happening
cool okay so our store is up uh we put
it on base kind of just to recap sort of
like phase one is editing the smart
contract and uh playing with it in this
debug
tab so you'll get scaffold eth
downloaded you'll Tinker with your
solidity and you'll kind of play with it
here getting it written correctly maybe
you know do I want to use arrays do I
want to use structs like how do I want
to build this thing that's kind of like
phase one is tinkering with your smart
contract testing your assumptions poking
at it with this debug side then phase
two was that front end right we had to
do the read contracts we had to do the
write contracts and to do that I just
like jumped into uh the docs and kind of
copy pasted
them you you wrote The Block Explorer
right
yeah that's that's
Port uh so phase two was kind of that
front end where I uh was putting in
buttons and reading and writing from the
smart contract and I just Ed the docs
here to copy paste uh to read from a
contract how to write to a contract and
that was kind of phase two getting my
front end going and then phase three was
deployment right we deployed the smart
contract we deployed the app and uh now
they're all live talking to each other
and you can do this anytime you want by
just going to scaffold
e.
and uh you can clone down the repo or
you can do this MPX create e okay more
questions any any more questions yes sir
if you would want to integrate more
common building blocks maybe like uh uh
chain link functions or like a graph or
something is there anything we have to
pay special attention to or would it
just work out of the box that's a great
question um so the the short answer to
that is there is an external
contracts file right here and so
whatever contract you wanted to talk to
like in this case we have die on mainnet
uh what you would do is whatever
contract you wanted to talk to you would
put that in here and then you can just
talk to it with the read and write
functions from from scaffold e so
uh uh let me see like chain link
functions I don't think I could put that
in right now
but
uh yeah I I think the short answer there
is if you want to go talk to an external
contract there's this external contracts
file uh here in nextjs and you can use
that to list out the contract you want
to talk to and then the read and wrs
from scaffold eth would work the
same does that sort of answer that
question you you may even like possibly
have multiple contracts here uh you
might like inherit from another contract
or something like that but uh yeah the
the things to look out for would
be I don't know you need to be on the
right network uh just have have that
contract in your external contracts and
then start talking to it
normally more questions about scaffold
eth about building on eth about what we
did
today any any other questions maybe I
could go back and uh work on that event
page for a little bit we kind of I kind
of did the speedrun it was a little bit
too fast but uh
let's see here let's see if we can get
this history going I kind of want to
dink with that see if I can get it
working sorry they have one question yes
please where are you yeah is there
anything that lists the full stack that
um scaffold eth uses uh yeah it it's
here on the website so nextjs rainbow
kit wag me
typescript uh anything in particular
you're looking for or just wondering if
if there's a list of like all the
different tools that are floating in
there like I see there's a difference
between Foundry and hard hat I don't
know if the differences between them or
anything like that so yeah you uh at the
beginning when we did that MPX create
eth it gave me the choice Foundry or
hard hat and uh you you basically can
choose and scaffold e kind of keeps that
abstraction above so when you do yarn
deploy it's going to deploy whether
you're using hard hat or Foundry and it
kind of takes you know abstracts that
away so it's easier for you you just do
yarn deploy whether you're using one or
the other is there anything else to know
with like versell just ran popped in as
well anything else on the
side it's hard it's hard to be able to
think about all the things you might
need to know um well that's included in
scaffold I mean yes yes scaffold e comes
with either hard hat or Foundry for your
orchestration and then next JS for your
app and and within that you know we have
rainbow kit wagm typ
strip cool
yeah more questions any other
questions yes is this available for
react native uh I think there is a a
scaffold e react native yeah I've tried
that but I couldn't get it to work Rea
native yeah I don't
know we had one a long time ago but I
don't know if we still have it uh a good
way to find these things is to go to the
uh build Guild like our actual app here
and then go look at builds maybe we
could even search this native let's see
what comes up
here yeah scaffold E3 act native you
said you've already tried that one and
it didn't work yeah but it was probably
was doing something wrong probably it's
pretty old
yeah yeah yeah because this is you have
to like reinvent a lot of things here
yeah isn't this like the first version
of scaffold yeah yeah this is like an
older version of scaffold e too yeah so
I don't think we have an upto-date
react version
yes any more
questions so uh later today I will be
doing a similar talk but I'm going to go
through um building your first five apps
so let me just introduce that before uh
before I take off here
uh it's speedrun ethereum so if you
haven't heard of speedrun ethereum
speedrun ethereum is a curriculum that
will help you learn how to build on
ethereum by having to actually build a
bunch of things it'll take you through
building uh a simple nft a decentralized
staking app a token vendor a dice game a
DEX so this will take you through and
have you build the thing and it won't
let you just copy paste you'll have to
like think for yourself and actually
build the thing and so this is a really
good way to learn how to build things by
just building a bunch of things and I'll
be going over each one of these in more
detail this
afternoon uh I don't know what time that
is later later
today but uh yeah so build Guild is the
Dow that's kind of around all of this
stuff that's how we're funded we're
funded through the ethereum foundation
and we work on tooling like scaffold eth
um let's let's look at the extension
system too so when we did that MPX
create eth command
uh here let me show this when we ran
command uh there's an option to do a
dash e which would be an extension and
that lets you bring in uh a lot of other
uh tooling so for example let's go look
at yeah here we go onchain kit so here
is an onchain kit
extension so let's even just like copy
this I'm just going to create a new
folder and run this again let's
see uh oops I don't want to do
that uh yeah okay so
MPX create eth latest and then we have
this Dash e onchain kit and so what this
is going to do is it's going to use this
onchain kit extension and bring in the
onchain kit stuff along with scaffold e
this is really handy you can build oh oh
oh
no oh
no uh
oh that's not good let's let's try
another extension let's see if one of
these other ones works
I think something's broken with yeah say
you wanted to do subgraph you'll look
for Kevin Jones he'll be doing a talk
not tomorrow but the next day and he'll
do uh something with the the graph where
he does some indexing let's see if all
of this fails
or uh
oh we're gonna have to fix that
something is definitely wrong here where
the extensions aren't loading in I'm not
sure what what's that Pro what that
problem is but the extension system is
really nice because you can bring in
some extra components uh for instance
you could bring in um like we were
looking at onchain kit there right so
you could bring in uh some of uh bases
uh like their smart contract wallet
their uh swap component their token
selector you can kind of just like with
one line when this is working I'll need
to fix it I don't know what's what's
broken right now but with one line you
can basically install scaffold eth and
these extra extensions and it's just
going to speed up your process of
building even
more but I can't show off extensions
because it's broken right now I will
have to figure that
out okay so uh to recap uh scaffold eth
is a great tool for prototyping but also
easy to deploy to production uh we saw
today in only like 20 minutes I was able
to write the smart contract test it out
a little bit build a front end that
talks this smart contract and then
deploy that whole thing both to base and
also to versel and so you should be able
to do this at home also just go to
scaffold
E.O and you can get started today uh and
then speedrun ethereum is a good way to
kind of double click on that and go a
little bit deeper and learn about more
concepts by actually building some
things um that might be all I have any
more questions definitely open to
questions uh I'm Austin Griffith on
Twitter I'm this
dude oh man Internet is slow oh no maybe
that's what this is or maybe it's just
like the internet's
nah what's
that oh really the MPX d e is let me do
I need to make a directory or something
let me
see let's do test and then CD into
test uh oh I wanted to show that I was
dude uh this guy Austin Griffith yeah I
can't do it right now I don't know
what's wrong okay
anyways uh let's
see and then let's run that
again nope I don't know I don't know
what it's
doing it could be
oh it's telling me that there's rate
limits
yikes on GitHub is that what it is oh
yeah wild
okay that is a new one we'll have to
we'll have to look at that one I'll I'll
pass that on to the scaffold e
team um yeah okay so in recap scaffold e
shipping apps it's uh a great way for
you to Tinker and kind of figure things
out as you go um once you have scaffold
eth and you figured that out go to
speedrun ethereum and take on these
challenges there's a bunch of things to
build here and that that's going to
teach you a lot of things uh and and
then at the build Guild as you go
through speedrun ethereum we even have
like onboarding batches and small grants
available and I think that's it I'm very
open to questions though if you guys
have any more questions I'm 20 minutes
early but the the app it was quick it
was it deployed
fast yeah oh thank
you we we do have time to kill if
anybody has any questions uh just leave
it open out there shout them out if you
have
them I'll some what do you got what do
you got so what's the kind of oh thanks
I sound kind loud enough already right
hi oh that's too loud for for the live
person hey um yeah so when you when you
Fork from scaffold e and you make your
own apps obviously there's going to be
improvements released to scaffold e so
um how easy is it to benefit from those
improvements if you for the project
there's a lot of the improvements so
they like scoped into dedicated
libraries and stuff like that that's a
great question and it sets me up to talk
about our extension system let's
go so so going back to that extension
system that wasn't working right now cuz
it's rate limited uh the the point is
you can have so an extension is
basically just some solidity and some
front end and the solidity and the front
end aren't probably going to change that
much but you're right like if a new
version of wagm comes out you'd like to
have that new version in your app uh so
with the extension system you basically
build an extension out of your stuff and
then it stays state-of-the-art whatever
new stuff comes in from scaffold eth uh
just comes in could Fork it but then you
have to like keep that merged down down
wind down chain down whatever it is down
Downstream I think that was what I was
going for yeah
so I guess the the answer is yes you
will have to keep merging new changes to
scaffold e if you end up forking it and
there are you know improvements that
happen regularly that you would probably
want to pull down but the best way to do
it is to make it an an extension and
then have just the latest scaffold e at
all times and just just your smart
contract and your front end injected
into that latest
version any other questions
yeah suppose I wanted to uh use scaffold
against like a a hard hat fork of say
base is that yeah let's go so instead of
the so here's my blockchain right here
right if I kill
that oh oh no my screen's not there
that's okay uh so you just do a yarn
Fork the the too long didn't read There
is instead of yarn deploy or instead of
yarn chain which is what we use to bring
up our chain you do a yarn fork and
that's going to Fork main net or base or
whatever you have to supply like what
network you want to Fork but yeah yes
that's not going to work but yarn Fork
is is the answer yeah yeah and Foundry
works a lot better I think than hard hat
at that it's a lot
faster any other closing
questions thank you guys for coming out
and checking out scaffold eth make sure
to hit up scaffold eat.io make sure to
hit up speedrun ethereum.org
and uh yeah keep keep your eyes out for
the build Guild and the stuff that we're
building any final
questions what are you working on right
now oh ah that's a good question uh um I
I think that
um we we as the build Guild want to do
better medium to hard curriculum
speedrun ethereum is a good start but it
really doesn't quite prepare you
for building your own protocol for
instance and so what we would like to do
is create some medium to hard curriculum
that gets you closer
to mainstream apps and building your own
protocol and I think that looks like a
handful of different things um we've got
Elliott working on the ethdev tech tree
which is a really cool kind of tech tree
that's built out uh that's kind of a an
offshoot of
this if you go all the way to the bottom
of build guild.com there's a tech tree
here and it's like this really gross
miror Board of mine um but it takes you
through all these different concepts and
kind of like the tech tree of of all the
different concepts behind like
tokenization and Defi and all of that
stuff so this is kind of what we're
working on right now it's just medium to
hard content we've got the tech tree we
have a CTF uh capture the flag that that
we'll be playing tomorrow keep an eye
out for build Guild we're going to have
um a morning session where I do
something similar that I did here and
then an afternoon session where we'll
play the capture the flag and uh you'll
you'll take on some challenges uh from
the build Guild and uh a third thing I
think in terms
of medium to hard content and what we're
working on there's like this idea that's
brewing in the back of my head that's
kind of like this agent-based game where
it's like you have to build a Dutch
auction and there's like hundreds of
agents and they want to use your smart
contract and it's all just like Local
Host and for fun but it helps you get a
feeling for what a live protocol might
be like and having lots of users use it
even though it's just Local Host and fun
but I think some somewhere in the
cross-section of the ethdev tech tree R
CF and this like agent based idea
hopefully we Converge on a good medium
to hard curriculum and kind of extend
we're not going to call it the speedrun
because the speedrun is kind of like
beginner we're going to call it
something else maybe e Dev tech tech
tree is what we go with but it'll be its
own meme but something along those lines
medium to hard get people prepared to
like build their own
protocols yes
sir yeah okay that's a great question
it's
misspelled um so it's like going back to
the old like Hodel meme right like back
in the day with Bitcoin someone would
say hold or
hodol and then someone from the e space
kind of reframed it to bidle and so we
were just we thought it was a cool name
and we went with bidle GID but I just
say build Guild but yeah it's a play on
that old ho hotal meme from
y can we use
a I'll I'll restate the question
maybe
long oh yes yes chbt is way better let's
let's just go do that real quick just to
show that so let's say we were like on
the front right and we had uh those
buttons let me just clean this out real
quick yes uh with cursor and chat GPT
it's so so smooth but let's say uh let's
go down here let's just tell it to add
another button
right add another button
for buy coats or something like that
right let's see what it does
okay and then I just hit
apply and
save and now hopefully our app can have
a buy coats button too there so yes it's
way faster with chat
[Laughter]
GPT oh how is uh testing unit testing
yes uh so that will rely on either hard
hat or Foundry depending on which one
you want Foundry would be your tests are
in solidity hard hat would be test in
typescript but there is just like a test
folder here that has like an example
test in
it right here and so yeah so here's the
test right here and then you can run
that by doing yarn
test oh maybe not nope it is it is not
yarn test maybe I need to hard hat test
oh I'm in the wrong one yep let's go to
that Dev
folder yarn
test yeah there we go so then it runs
your tests for you yeah so it it relies
on either hard hat or Foundry depending
on what you use but again it kind of
abstracts it away to just yarn test cool
cool
yeah only 11 minutes left
yeah uh oh you want to look at the T
yeah yeah yeah you're saying this this
test here right
yeah is that is that code big
enough so yeah let's see what it's doing
so it's gonna
like yeah set up the signers and get the
contract
ready deploys it and then it's going to
expect that some certain thing so it's
going to you should be able to
set the greeting right so we do a set
greeting here or maybe we're just
getting the greeting and we're expecting
it to be that string so when we deploy
it it should have that as the as the
string so it's basically just checking
that the greeting is correct and then uh
here it
is setting the greeting and then
checking that it's set
correctly all right last chance answer
for questions if you have any more
questions you got one you got a spicy
one let's go so why do you uh have hard
hat as the default option cuz I I would
kind of consider it sort of not
deprecated but kind of Legacy true uh so
to defend the hard hat dudes yes they
are like Foundry has kind of big respect
to them by the way yes it's great Tech
but I just mean I I feel like Foundry is
so much more popular now yep I agree and
um I think that the hard hat dudes are
speeding up like they're I think they're
even using revm now underneath so
they're using some of the The Foundry
stuff and I think that heart hat is a
little bit better for deploying
contracts but the the the short answer
is when we built scaffold eth we used
hard hat at first and we're now
transitioning to Foundry and it will be
Foundry by default very
soon no not that spicy
yeah I guess not
yeah anything
else all right thank you go speedrun
ethereum go use scaffold eth and go
build something cool thanks a lot
what's that see youat afternoon it
worked yeah thank
you
e
e e
I
m
some some small things with that and
then we're going to go through speedrun
ethereum and we're going to kind of just
like look at this curriculum and kind of
talk through each of the like learning
moments that you'll go through when you
go through speedrun ethereum so let's uh
let's get started with scaffold eth
first scaffold eth is a Dap developer
tool it's great for tinkering with your
smart contracts and it has this Auto
adapting front end that is really nice
when you're tinkering around with your
smart
contracts so I'm going to run this what
Devcon two this will be my second demo
today maybe we'll do Foundry this
time so uh scaffold eth
is uh a Dap building tool like I said uh
it uses nextjs rainbow kit wagy
typescript and you kind of have the
choice between hard hat or
Foundry uh
um
it's a a a great tool for prototyping
you can quickly get something out uh uh
out the door I I think I deployed
earlier I deployed an app in like 20
minutes and uh we had lots of time left
for questions so I'll do the same thing
probably uh uh now it'll probably go
pretty fast but let's uh let's let's let
this thing install and then we'll go
Tinker with scaffold eth
Devon
okay bringing the code up here it's
still installing so we've got some
time but let's go look in here you kind
of have these two main packages there's
either Foundry or hard hat that's kind
of like your back end that's your
orchestration tool that's your deploying
and testing and then nextjs is your
front end scaffold e does some really
nice things where when you compile in
Foundry it injects those artifacts into
your app and we'll see that in a little
bit but it's really nice when you're
working on your front end and it knows
about all your smart contracts and all
the variables and you can kind of it'll
Auto suggest how to fill in
stuff there's I see a couple of people
that were in the last talk sorry this
will be a refresher for like 10 minutes
here and then we'll get into speedrun
ethereum okay so uh let's see is our app
up here we're going to go look at our
contract and it's a basic
contract uh has a lot of uh initial
Concepts that are here like Primitives
and data types and events and
Constructors but it's a greeter it's a
greeter contract
and let's uh fire everything up so we'll
do a yarn chain to bring
up um let's CDN first Devcon
that will spin up our local blockchain
and that's what we'll deploy
to and then I'm going to do a yarn start
and that will bring up our front
end and it's the two things kind of
working in Symphony that is kind of the
magic side of scaffold eth and then we
can yarn deploy
here and what that is going to do is
ship your contract to the local
chain compile and deploy there we go
okay so so we're compiling and we're
deploying and kind of the the heart of
scaffold eth is that you can
have uh your app up here and you you can
have your code up here and you can make
small changes to the code and you're
going to see those changes reflected in
the front end so if we go over to the
debug contracts tab again sorry for the
repeat for people who are at the last
one but it's good to run through the
concept here uh let's uh let's look at
the greeter contract real quick what do
we have here so there's a
greeting and it gets set you send in a
string and it gets set so let's just do
that real quick it's gonna
it's going to yell at me for not having
gas when I hit this it's going to say
something like oh wait wait wait wait
wait wait we're still connected let's
get out of here we want burner wallets
okay so I just disconnected my metamask
uh and the first concept here is burner
wallets uh you'll use these in Dev
rather than in production you don't
usually use burner wallets in production
very often but they're really nice and
Dev because you can just like hit a
button here and it sends a transaction
without having to uh
have the dialogues come up and have your
chain ID right and all of that in
metamask uh it's telling me I don't have
any guess but if we click this little
faucet button here now we have some
eth and let's see if we can set hello
world yep there we go so now we see
Hello World there right and that was
from this thing here and uh like I did
in the last demo I always like to look
at this little premium flag and Dink
around with this so there's this piece
of code here that says if they send in
some value then we set a premium to true
there's some flag called premium and so
let's just send in some
eth and uh also there's no decimals you
need to convert it to we by multiplying
times 10 18 and there's a little button
to do that of course you don't want your
users to have to do that this is
something that you'll do and this is
like a developer kind of thing but in
the front end you would just do this
behind the
scenes okay there we go so it's true now
we were able to send in some money and
now there's money in the contract and
we're able to uh set the greeting and
have that little premium flag set okay
so um debug tab like this is really nice
because now I can go and I can add some
code right what if we wanted to uh make
an
public
uh uh I already have owner what will
this be beneficiary
beneficiary and we'll set that equal to
some other address let's just set it to
this address
oops oh man I don't know what I did
there copy
this okay paste it in there we go okay
and when I hit save and deploy this now
Watch What Happens we're going to get a
new uh beneficiary over here oops deploy
so I'm watching for that to show up
here and sure enough there it is there's
the beneficiary so notice how that just
Auto adapted like all I all I did was
add a line to my contract for
beneficiary and deploy it and then my
front end recognize that new variable
and display play it here so you can
really kind of Tinker with stuff and
play around with however you want your
smart contract to work and kind of test
your assumptions um let's see let's do
this let's uh let's test some
assumptions here so there is this
withdraw function down here that lets us
pull the eth out of the contract and
it's checking is owner I'm going to take
that is owner off of there and I'm going
to write a different require statement
I'm going to require that the message.
sender the person calling the function
has to be equal
to the
beneficiary or it'll say not the
beneficiary so instead of the owner
we're going to have this beneficiary
that can do this withdraw so what I want
to do here is I want to try to test this
I want to see how this works and test my
assumptions and make sure this works the
way I I think it does so the way I would
do that is uh I need to sort of withdraw
as the benefici iary and then I'll I'll
kind of try to withdraw as a bad guy and
it should not work as the bad guy and it
should work as the
beneficiary so let's do that let's try
that out real
quick okay so now uh let's let's set the
greeting real quick and send in some
money just so there's money in the
contract okay so now there's a couple
bucks sitting in the contract right and
then uh let's call withdraw but let's
call withdraw as a bad guy so to create
a new account you can do this really
quickly by just opening up an incognito
window and going to Local Host notice I
got an address here kind of C2 C4 now if
I close this and do it again new
incognito window I'm going to get a
another new address there okay so let's
grab some faucet funds and let's go over
here and let's try to withdraw this $330
something like not the beneficiary very
nice and real quick let's see if this
dude can withdraw it should let's find
out uh did I click it there we go and
the money's out of the contract okay so
like I said testing your assumptions
right like I made this line of code that
said only the beneficiary can call this
withdraw function
and then to test it I basically tried as
the beneficiary and then tried as
another account and proved that it only
works with a beneficiary not for the
other one now that's not exhaustive
testing of course you would want to
write a more extensive test Suite
eventually but for just thinking around
trying things trying to figure out how
you want your smart contract to work
this this is a really uh kind of quick
way to uh iterate and try things okay so
scaffold eth uh
uh is great for uh this this kind of
prototyping that we're doing here then
eventually you'll move over to your
front end and you'll write some react
I'm not going to do that uh I already
did that earlier we'll do that tomorrow
and yeah let me show that real quick so
tomorrow like all day long we're going
to have a build Guild community-led
session I'm not even sure where it is
which where like that way do you know
where the CLS is oh it's upstairs Okay
cool so we'll have a big room and we'll
do intro to building on ethereum in the
morning and then in the afternoon we're
going to have a capture the flag so it's
going to be a um challenging uh uh
challenge it's going to be a challenging
challenge but the the the guys at build
Guild have built like 12 different
challenges starting from easy and they
get harder and harder so come come by uh
the community-led session tomorrow just
look for build Guild where we'll
probably be upstairs
um okay so scaffold eth is kind of the
underlying tool here but what I'm really
going to show off mostly is speedrun
ethereum today and we'll go through each
one of these
challenges uh but let's see have we have
we basically covered most of the
scaffold eth stuff let me see if there's
anything else I want to talk about here
with scaffold
eth probably aren't going to deploy any
contracts I think the front end will be
taken care of for us I I think we're
good I think we're we we've tinkered
enough with scaffold e uh let's go ahead
and start working on speedrun
ethereum like I said uh the underlying
technology here is scaffold eth but this
is uh a nice curriculum that'll take you
slowly through building your first uh
five apps on ethereum uh starting with
just like a simple nft app so what
you'll do here is uh you'll deploy
uh uh an nft smart contract so you'll go
through these settings you bring up the
chain you deploy you'll have a front end
uh gas and wallets we've kind of already
covered this but we're using burner
wallets you'll go to uh the faucet to
get some
funds uh yeah again we're using burner
wallets not
metamask so you just kind of like
learning burner wallets here first and I
think maybe even you send around some
eth here and you use the fos it to to
fill up your
account uh and there's no code in this
first challenge this first challenge is
just about kind of calibrating your uh
the tooling and getting used to uh how
scaffold eth works but you'll go to the
my nfts tab and you'll hit this mint
item button and that mint item will mint
you an nft and you can get in and look
at the Smart contract and see how that
all works uh maybe we'll run through
some of these in a little bit but let me
just kind of
cover H maybe maybe we should just run
through it why not we got lots of time
uh we'll we'll go through this slower
tomorrow if you want to follow along but
um I'm going to just go ahead and clone
it down might as well go through the
first challenge
here oh I already have it there huh
simple nft 2 all right
oh boy that might be too slow okay well
uh let's just follow along here maybe
that'll come down eventually oh yeah it
okay what do we do a yarn
install uh here let me just follow the
instructions even
better
okay so we cded in O I need to get check
out the simple nft branch
then I yarn
install okay I'm going to close the rest
of this stuff from the old terminal we
don't need any of those
anymore okay and we'll do the same thing
that we do with scaffold eth where we
bring up yarn
chain and that that's going to run our
local chain and then we'll do a yarn
deploy and that will deploy our smart
contract to the CH
whoa
sorry okay and then we'll do yarn chain
wait we did yarn chain now we'll do yarn
deploy and that should deploy our smart
contract to our
start and that'll bring up our front end
and it will look familiar it should be
very very familiar to scaffold eth
because it
is okay so here it comes let's see we're
going to have our app up at Local Host
go here is our app here is the burner
wallet stuff we can hit this button to
fund our
wallet let's see what does it have us do
it has us go through and get some gas
is it sending yeah I think oh I see this
is just the faucet we can skip this if
you I I would recommend uh on your own
time going through speedrun ethereum and
going through each one of these
challenges I'm going to kind of like
briefly go through them but I'm probably
not going to go slow enough that you'll
get everything from it so I would I
would recommend like going home and
going through speedrun ethereum at home
sometime okay but let's see what we have
so it's going to tell us to what mint
some things let's do it let's go to my
nfts and let's hit mint what's going to
happen
here yay there's our first nft let's
mint another one okay and I think the
directions say to send them around yeah
yeah okay so we're going to create an
incognito window right so we have a
second account
and we'll go to Local
Host and you'll notice there's kind of
like this like kind of red and teal guy
and then there's kind of like this green
dude here so we're going to try to send
the Buffalo to the green dude I think I
can do my nfts
here okay let's let's try to send an nft
to this dude so I'm going to copy his
address then I'm going to go here to
Let's send him
Buffalo uh I need to put in an address
so paste that in now hopefully this
fires off a transaction and sends the
Buffalo yeah all right he got it okay so
that's that's most of the first
challenge I think is basically just like
I said kind of calibrating your your
tooling and getting ready uh you don't
really have to actually write any
solidity but let's go uh look at the
Smart contract real quick just to see it
see what the nft contract looks
like okay and if we go to packages again
and you either have hard hat or Foundry
and then you have
nextjs if we wanted to look at that
contract your collectible is what it's
called notice we import a bunch of
things from open Zeppelin to make that
then we inherit all of those things
and you can see there's sort of like a
base URL so what happens is it it stores
a base URL for the nft and then it puts
the nft in ipfs and then puts the hash
of it in the smart
contract and here's the mint item pretty
straightforward we're minting something
incrementing the
counter uh some before transfer
hooks but that's it there's the there's
the token Ur right URI right there let's
go let's go actually debug that and look
at that token URI real quick so if I go
to here and I go to
debug and let's see what what can we do
we can get our balance whoops didn't
mean to
disconnect I'll take the burner back
please there we go so we could check our
balance let's see what it is it's one
right we own one of them and then if we
maybe look at who the OWN owner of token
ID one is it's that other dude token id2
is us
okay and then let's get the token URI so
if I say I would like the URI for token
and if I follow that it should be a
description about the the nft and uh an
external
link to the zebra there it is very nice
okay so that lives in ipfs and then this
stuff is also an ipfs but it's kind of
like a manifest and then the hash of
that goes onchain and lives kind of
right here it's kind of hard to see but
it's this
qmv thing it's that right there that's
the unique identifier of the
content okay so let's see is that
basically challenge one let's see what
else we need to do
we minted it we sent it around oh okay
so what it's going to have us do now
would be uh deploy the the thing to
sepolia so instead of deploying locally
we would deploy to a public network and
then probably do the same thing where we
send it around I'm going to skip this I
think
um just because it's it's going to be
the same thing it's just nice to have it
on a public network and that's how the
autog grading works when you're doing
this at home you'll hit this submit
challenge at the end and you'll put in
your deployed URL wherever the versel
site is that you create and you'll put
in the um link to your contract on ether
scan and we have an autog grading system
that will then go through and grade your
challenges and let you know if you got
it right or not and so each one of these
challenges you turn in and then the auto
grader grades it uh but I'm not going to
turn this in and I'm I'm probably not
going to ship this even to polia but uh
it's it's uh right here in the
directions pretty easy to
do oh even contract verification very
cool what you can do is verify the
contract so then when people see it on
the test Network or when they see it on
the Block Explorer they can actually see
your code which is really
nice okay let's just let's call it let's
say uh this is this is good let's let's
move on to the next challenge and uh
really start
looking at some code or looking at um an
actual challenge I think this this first
challenge was just like basically
spinning things up and sending them
around but the decentralized staking app
you will have to write some
code so uh this challenge is about
building a smart contract that allows
people who don't trust each other or
adversarial parties to
coordinate uh in this case they're
coordinating to uh a group funding
effort basically you maybe you need to
buy let's just say you need to buy
something for $500 and you need to get
five of us all together to put in a 100
bucks but the thing is we don't trust
each other and we can't and and it's
important that you can't get griefed
basically or locked up right if someone
can figure out how to lock your money or
steal your money that's really bad so
you want to build the the smart contract
in a way
that everyone stakes in or everyone puts
in their money and if you get enough
together then it will go into a
different state basically like a
successful state but if you don't get
enough money together by the deadline
you need to figure out how to put it
into like a withdraw state so then
people can withdraw and get their money
back and so you have to just like think
of all these different possibilities for
how this could play out if people uh
uh don't
coordinate but the cool thing is all
they have to trust is the code in the
smart contract they don't have to trust
any other players all the players have
to play by the rules of the smart
contract and this is kind of like
hopefully starting to show the kinds of
things that you might build on ethereum
the nft is kind of like a simple
collectable and honestly
like nfts are more like passport right
like your passport or your digital
credentials I feel like the
the digitally scarce art thing uh wasn't
as cool as we thought it was when we did
it I think nfts were a little overhyped
okay uh so what we're going to do or
what you would do if you were going
through this at home is you would uh
build a Staker do Soul okay so what
you're going to do is build this smart
contract that allows everyone to
stake and we're going to keep track of
everyone's balances and then after some
deadline we need to have at least some
threshold of eth stored in the contract
and if it's uh and then after the
threshold passes you call complete and
then that checks to see how much is
staked and if there's enough staked over
the threshold then you put it into like
a successful State and it what it does
is it just calls some external contract
and like buys something with the eth but
if there's something wrong maybe you
didn't get enough money together uh then
you want all the your users to be able
to call withdraw and get their money
back right okay and it will have a nice
little front end for
you and yeah let's uh let's let's go for
it let's uh
let's clone
it so um there's there's kind of this
interesting thing that you learn when
you're going through this and it's that
contracts aren't
automatic you always have to like make a
transaction to make something happen so
when we're thinking of the state machine
as we're in the staking phase and then
we're either in the success phase or the
failure phase uh
you to move from one of those phases to
the other you someone's got to click the
button someone's got to pay to make the
transaction work right and this kind of
brings up the idea of a web 3 Cron
job uh in in the web 2 world when you
want to run a Cron job oh man what's
called here we
go in the the web 2 world you might want
to run a Cron job to say roll your logs
or something like that like every night
we want to you know roll a log or uh I I
don't know in in the web three world we
might want to do something like compound
in interest every night right so you
you're not going
to you're not going to just run um a
service that checks in to compound your
interest or something like that because
if that machine Falls over then the
whole system doesn't work you have to
you're you're only as as strong as your
weakest link sort of and so if you have
uh if you have a really hard and strong
blockchain and then you have this like
service that's calling it and that falls
over and everything breaks then it's
it's no good right so what you need to
do is you need to create a a
system where you write the rules
correctly you say anyone's allowed to
check
in at once once every 24 hours anyone
can check in once and you write the
rules so that happens and then you the
the key here is that you incentivize
someone to hit the button and that's
that's a good like aha moment when
you're building these smart contracts
basically you write the rules to say
that someone can only check in once and
then you make sure they get paid for
checking in and that's the key that that
causes the this system where then you
can share this code and anyone can run
it and at least one person is going to
run it because they're financially uh
incentivized to do so and so if you want
an automatic task to run on ethereum you
don't just run a computer that does it
you have to write the rules correctly
and build incentives around those rules
to get folks to behave the way you want
them
to okay let's see let's see what we got
here yarn install
yarn oh I think I need to check out
o yep and then I did
that uh let's
see let's just remove this then try it
again yes then yarn install
oh man oh man I can't type here we go
here we
go okay now we're installing all right
so challenge one is about building this
staking app and it's gonna operate like
a state machine as I've
explained we'll let people stake money
and then at some deadline we'll check
and see if we've reached the threshold
or
not okay and let's go ahead and deploy
our
contract and we'll run a yarn start
right here I don't know I think maybe
the chain is not running oh wow okay
we've got a couple chains running here
this is uh this is kind of a mess let me
clean this up a little
bit okay there we go so then we'll do a
yarn chain to bring up our
chain and a yarn start to bring up our
front
end and let's go look at
it okay and this is the old one I'm
going to close that
out okay so here is the front end for
the Staker app there's some staking UI
that lets people stake 05 ether and then
either withdraw or execute and then we
see all the events here and just like
scaffold eth you have this nice debug
contracts page let's go ahead and deploy
contract let me just follow the
instructions here is that what's next
yep that's what's
next there we go okay yarn deploy here
it goes there we go so now our contract
is
here uh let's see what we
have but there's no no code written yet
I think we need to write some code to
get this uh to work
okay so let's see let's edit the Staker
do Soul yep okay yes okay so this is
where it's like you're going to need to
know at at by this time you're going to
need to know some solidity syntax you're
going to need to be able to write your
own solidity it's it's not going to let
you just uh copy paste the values in you
actually have to uh like learn like you
have to know what you're doing you have
to like think for yourself and actually
build the thing so let's see what we
need to do here uh it's telling us we
need to edit
the
Staker
doso and that's the old one let's bring
up all let's use cursor this
time okay and then let's go look at our
smart contract here it is okay so this
external contract is just an example
contract and it's to know that you've
completed this it just like sets this
Bool to true so don't worry about that
contract we'll we'll call it from the
Staker contract okay and
then all right so it looks like there's
some scaffolding here there's some
comments about what you're supposed to
do but basically the code is not written
yet it does
instantiate uh that smart contract and
one of the things you're learning here
there's like a handful of different kind
of Mo learning moments here but contract
to contract interaction is kind of a key
thing here and that's what's going on
we'll we'll have this Staker
instantiate this contract and then it
actually calls it right here so right
here it's actually calling that function
nope right here it's creating the
contract or it's creating the
instantiation of it and then later on
we'll call we'll call some function on
it okay so what do we need to do it says
you'll need to track individual balances
I guess we can copy paste this right so
we we want to keep track of
balances and what
else and we have some constant
threshold
okay so we're keeping track of all the
money that anybody puts in and then we
have this threshold where we need at
least one ether in the contract to be
successful okay all right now it's time
to write our stake function and we're
going to test it with the debug
contracts
tab so what do we need to do
here let's see does it give you any
other hints not
really we've got the threshold
okay so what should the stake function
do right we should let's just look at
this first goal here we should see the
balance of the Staker go up right so
let's do that let's let's create a
function called
stake and it's payable oh we've already
got look at that just going to fill it
in I don't even know if that's right
let's see no
event does it want me to oh yeah here
are the events here yep
oh huh oh here it is yeah okay there's
this event right
here oh it already did it okay so I just
need to create the event here event
stake there we go so we Define the event
here and then we emit the event here so
someone calls the stake function with
some amount of money it's a payable
function so people can send eth in and
we increment their balance based on
however much money they send in and we
emit an event let's go test this let's
go deploy just this
contract and let's go uh try to stake
some money in and see if uh our balances
show
up okay so I'm just going to use a debug
contracts tab for
now ooh where is our staking function
okay something's not right did I not
save this hit save here try
deploying uh it's just reusing
it uh is this yeah that's the first oh
here we go okay I'm looking at the
example contract I need to click here to
look at the Staker contract okay now I
can read the balance for this
guy and it should be zero right and then
I can stake so let's put in
e okay and hit send oh I don't have any
money I need money first we'll go to the
faucet and get some money now we're
ready to stake okay so now what we're
testing here is does our balance go up
we're supposed to have this balance
that's incremented by the value let's go
look and see if our balance went up by
hitting read here there we go it did
okay so we're correctly tracking the
balance let's hit it again and see if it
adds up like it should yes it does now
it's 0.02 I don't know if that's too
small it's pretty big you can see it so
so far we're allowing people to stake
money into the contract we see that
we've collected $67 in this contract
already and uh we keep track of their
balances so oh here we go Let's do let's
do an incognito
and let's go to the staking
app and let's grab some money from the
faucet and then let's try staking as
this dude too so let's go ahead and
stake another 01 what I want to see here
is that the money in the contract goes
up but we're tracking individual
balances and that's the key oh need some
money from the faucet and then there we
go transaction successful okay so now
there's even more money in the contract
right now it's uh at 0.02
wait oh I need to hit the thing yeah I
need to hit this dude right here right
there we
go there we go now now we have 0.12
there we go so now we have $400 in the
contract and what's key here is that
it's tracking
the balances of the different addresses
separately so let's see what this guy's
balance is yep so his balance is
balance should be that .02 right just
making sure that that's tracking and and
keeping track of everything right okay
that looks good all right what's next in
the challenge it seems like our stake
function is at least tracking uh
balances right
and is that and do you see the events oh
there's events let's
go stake events oh yeah there we go we
can see the two events right let's let's
let's use the a let's let's let's use
this let's see stake point5 what happens
if I hit this
button so I've staked oh yeah it's
keeping track of my individual
stake
and there's that event okay so it's it's
working so far we're we're able to uh
stake and see the events okay now here's
where it starts talking about this smart
contract being a state machine and how
the timing works right now what it wants
us to do is set a deadline of so the
block.
timestamp would be the time at
which the block was mined or validated
so you can get like kind of like the
current time of of the chain so we're
going to say current time plus 30
seconds and let's see here let's just
copy paste
this okay so we're going to have a
deadline of 30
seconds and what are we going to do
we're probably going to need a require
statement oh yeah here's where it talks
about the smart contract
doesn't do anything automatic someone's
got to poke it
okay okay so what do we need to do here
we need
to have an execute function that checks
if the deadline has expired let's just
do that first let's just just just that
simple function right there so we need
uh a
execute okay and it will be
public and what do we want to do we want
to oh it's trying to do something let's
let's just let the a I figure it out
let's see
here if the block dot okay I don't want
to do that what I do want to do I want
to write a require statement and I want
to require that the block like the
current time we want to know that the
current time is after the deadline and
let's just save that just straight up
that's all I I'm not going to do
anything else I just want to test this
little piece of code and this is nice
with scaffold e because you've got it
all locally you're on your own block
explor you're on your own blockchain you
can dink around all you want so even
though I I know I need to write some
more code here I know there's more to go
here I just want to test this one thing
does this require statement only let me
execute after the deadline has passed
that's what I want to test okay so if I
go to debug contracts and I hit execute
uh time should have passed oh there's
one other thing you have to do here it's
kind of
tricky when you're looking at block.
timestamp there's no blocks so when
you're deploying to like a live Network
like ethereum there's blocks every 13
seconds or whatever so this is
constantly going but on your local chain
there's no blocks happening so we can't
get the time so just a little trick that
I do is just hit this uh faucet button
and that basically forces a block to get
mined and then gets your time stamp
updated so now if we go here and hit
exit it should just work yep okay now
let's redeploy it let's try this again
and I'm going to do a D- reset so I I'm
on a fresh
contract and let's see that so so there
is the contract there let's do it again
let's do it again watch for this to
change there we go Okay so we've got a
fresh contract now it should fail to
execute because it's not within the 30
seconds even even if I increment this
and hit this it it shouldn't yeah
deadline not met okay cool that was what
I wanted to test I basically wanted to
test like does this thing keep track of
time correctly and does it only run the
function once the time has passed and it
does so we have that
working okay
now
okay yep we're going to flip a a bit in
that okay so if the address this okay so
address this this is going to be the
address of the contract do balance so
this tells you the balance of the smart
contract and what we want to know is is
it over the threshold by the deadline
okay so we know uh and and if it is then
we're going to call this code right here
and I'm just going to copy paste
that okay so we know we need to do some
stuff in the middle of this but there is
our contract call and this is really
cool it's going out to this other
contract and it's calling the complete
function on the contract and it's
sending all of its money okay so we have
the Staker contract and then we have the
example external contract and the Staker
contract will call a function on the
exter or the example contract and send
all the money to it but we need to do
some stuff in the middle here we need to
do this whole
uh this thing here is the contract over
the threshold by the deadline so we need
to check the
address.
this.
balance okay let's do that so we want to
say um so we'll do if I think address
balance is greater than or equal to the
threshold this would be like the
positive state like they oops oh yeah
actually oh I do want that line
there there we go so if the balance is
greater than the
threshold and you can't get past this
require statement if the deadline hasn't
passed right so we know the deadline has
passed and we know that the balance is
threshold then we're going to call this
example contract complete
and if not right so if we're not able to
get the threshold worth of eth we need
to put it in a different mode thinking
of our state machine it's not a success
it's going to be kind of a open for
withdraw mode okay so let's go ahead and
bless you let's go ahead and set this so
else right
if if we didn't get the threshold we're
going to need to set open for withdraw
to True which means we probably need a
Bo up here called open for
withdraw yep and it'll start out as
false okay uh so let's see what happens
here we call execute it makes sure that
the block Tim stamp is after the
deadline and it checks to see if we have
collected enough eth in the smart
contract and if we have we send it to
our external contract and Trigger the
complete and if not we open uh for
withdraws and we let users withdraw
their money
back okay and we want to you let users
withdraw okay so now we need a withdraw
function
probably okay
yeah and whoa and we know open for
withdraw needs to be
true and what is it going to do it's
going to send the balance to the user
and then it's going to zero out the
balance uh now this is uh this should
give you a little bit of Goosebumps in
terms of re-entrancy there's this thing
that you can problem you can run into
where you have re-entrancy where the
trick what you want to do is create uh a
temporary variable here called amount
and then you want to zero
out the
amount and then transfer the
money like that and what that does is
just make sure that the balance is zero
by the time you call transfer because
people could it's called re-entrancy
it's kind of like a rabbit hole to go
down but basically you could set up an
attacker contract that when it receives
the eth it actually goes back in and
calls again and what you could do is
withdraw multiple times end up draining
the whole contract let's let's say
there's five eth in the contract and
your balance is only a half an eth you
can use that half an eth and you can
withdraw multiple times re-entering so
kind of a weird little attack there but
that that will fix it so that doesn't
happen all right let's see let's see if
this works so we need
to let's see time left create time left
function you want to resum zero okay
let's let's yeah let's do a time left
too that that looks like a nice function
to
have it's really nice that the AI just
reads the comments and fills it in maybe
we shouldn't have those comments thin
there so in line it's pretty easy to
just kind of let them let it do its
thing huh so what's happening here is if
the time stamp is greater than the
deadline we return a zero if not we
return deadline minus timestamp and that
should give us uh a report on how much
time is left in the round and so now we
should be able to go here and we see
time left right and this won't change
unless we do that thing where we cause a
block to get mined and then time left
goes down see that let's do it
again okay so it's getting there once
once that gets to zero and by the way I
can't call execute yet right it's going
to say something like deadline not met
yet because we're waiting for this to
happen Okay and by now I bet we're set
let's see time left now goes to zero
Okay cool so that is doing what it needs
to do it's correctly reading how much
time is
left uh let's let's have a failure case
and then let's withdraw let's do that
let's test out if we're not able to
coordinate and we put some money in
there and the time expires can we get
our money out that's what we want to
test right now okay so let's just go
ahead and deploy a fresh
contract all right and then let's go
ahead and
stake one or
something and send and then we're just
watching for this time left to be
ready again if I hit execute it's going
to say it's not not enough
time we're waiting for this got to wait
seconds three seconds okay here we go
it's got to be ready now all right so
we've staked money in we can see that
there is $300 sitting in this
contract and uh when I call execute it
should work
and it should set open for withdraw to
True right we weren't able to get the
threshold of eth so it needs to put it
into withdraw mode and so open for
withdraw gets set to
true and then uh when we call withdraw
let's try it hopefully we get our money
back so let's keep an eye on this and
this right oh that's hard to
see what is it 8.3
it should go to
here okay so we've kind of tested the
the sad case we staked our money and we
weren't able to get enough money
together from all the players and so
then we put it into that withdraw mode
and we test it out and made sure that uh
they can withdraw their money and it's
not going to get stuck but let's talk
about the happy path what we want is for
a bunch of people
to uh uh
stake by the time the deadline happens
and then we'll hit execute and hopefully
it will uh it will work let's let's try
a fresh
contract okay and let's get a couple
let's get another player in the game
here in an little incognito
window we'll go Local Host
faucet
and go to the Staker UI
and we're going to go ahead and stake
point5 ether and I'm going to do the
same thing over here stake point5 ether
now there should
be you've staked 0.5 and you've staked
eth so now when we hit this execute it
should not put it into withdraw mode
withdraw should stay false basically it
should send this money on to this other
contract let's see what
happens uh oh deadline not met I need to
do that thing there we go it's kind of
kind of annoying oh there we go look at
that you
staked and let's go look at Contract
balances so the Staker contract is empty
now and the
external uh example contract has the one
eth and the completed is true okay so it
was able we were able to get the
threshold together and then by the
deadline we hit execute and it sent the
money onto this contract and called this
complete function so it seems to be
working pretty well let's see what it
wants us to do now it seems like we've
tested both the Happy State and the and
the sad State and it seems like I don't
I don't think anybody can grief us it
seems like it's pretty
solid uh yeah can you see time left
yes if enough e is staked does it work
yes and if the threshold isn't met are
you able to withdraw yes we've we've
checked all of those boxes okay so to
improve the user experience set the
contract up so it accepts eth o this is
cool okay so we're going to have it it's
called The receive function it's kind of
like the fallback function where if you
just send money to the contract so what
we're doing is we're calling normally
we're calling this function here we're
calling stake and we're sending in money
but what they're saying is we could set
it up so you just send money directly to
this uh address and it will still keep
track of it for you and the way to do
that is to I'm just going to let the AI
do it I don't even have to type
it yep I do yeah I'm G to call stake so
if someone sends money into the contract
we're going to trigger this uh staking
here and it's a payable fun function
okay let's see if this works so let's go
ahead and deploy again and what we want
to do is just like YOLO some money to
the contract and see what
happens so here is the contract right
there and I'm just going to go to the
faucet down here and I'm just going to
send in like 0.5 eth and hit send so I'm
not calling the function I'm just
straight up yoloing eth to the
address and it was
successful the money is is in there but
what's interesting is it's keeping track
of the balance for this user if we go
look at this user which is the zero user
on the chain and we check its balance
it's 0.5 so nice little piece of ux
there instead of having to call that uh
function you can just give people like
an ens name right it could be stake.
build.com and anyone can just YOLO eth
to stake.
build.com and then someone
still has to hit the execute button but
like I said earlier if you figure out a
way to incentivize it you can make that
work uh in a decentralized way all right
use the receive function to catch that's
working okay if you send eth directly to
the contract does it update your balance
it
does can execute get called more than
once this is an interesting one so what
if and you really have to think about
all the different edge cases but if
someone calls
execute oh okay this could be really
tricky let's
say the deadline has passed but no one
has called execute
yet and there's not enough money in the
contract if someone calls execute it
would open the
withdrawals uh but what if someone
called execute again after the
balance uh was over the threshold you
could end up getting in a weird state
where both of these things become true
so maybe we could make a variable called
like has executed or something like that
and then only let them execute
once yeah complete I like that and then
we'll say completed is true here and
then we'll also
require not completed right so we
require that it's not completed and then
we set completed to true so that means
that we're only ever going to go into
this function once
basically and it can't get called
multiple times there's probably like a
more elegant way to do that but it's
straightforward simple let's just do it
that way all right all right it's a
triap make sure your funds can't get
trapped in the
contract yeah o here's one try sending
after you've executed o that's tricky
okay let's let's run let's run the whole
thing and go down the happy path let's
redeploy
okay and then we will just use the
Staker UI and I'm just going to stake
twice and that will get us to the Limit
there we've got our one eth and now
we're just waiting for this time to run
down while we're doing that let's look
and see what else we need to
do okay yeah it looks like we're moving
on to deploy the contract so if if this
works I think we're happy 3 second
seconds left two
one zero okay now what what was it
saying it was saying if we send some to
it yeah yeah yeah yeah okay so what
happens if we
execute and then we send more money into
the contract so basically the the
staking is done we've moved into a
complete state but that still doesn't
mean that someone can't come along and
send money to this cont cont we
basically don't want that to happen
right we don't want money to get locked
up in here goodness what's happening
over there uh so what we want to do is
probably have some other variable here
let's see what do we want to
do o completed we could use completed
right we can uh in the staking function
we can require not
completed there we go
and that fixes that problem so now once
the game is over it makes sure no one's
allowed to put any more money in and
let's let's go triple check this let's
have the whole thing work and then let's
try to send some money to it and we
should get a good
failure so let's see grab some money
from the faucet withdraw that's not
going to work stake two
times okay here we go so now we've got
our eth and we're just waiting for the
time to tick
down yeah good time to retweet Dam's
tweet good tweet Damu
retweet okay let's see are we
out zero okay time left so now we
execute okay and it puts it puts the
money into the other contract everything
is good now what we want to do is make
sure we can't send money to this address
now I'll do that same thing with the
faucet I'll put in the destination 0.1
now this should fail this should realize
that we're completed and we don't want
people to stake any money or get any
money locked yes already completed Okay
cool so I think our contract is pretty
solid we've kind of like worked through
the edge cases and protected ourselves
from from uh those things o create a
modifier okay hold on let's go create a
modifier called not completed
and it will check that the example
contract is not complete oh in the
execute and withdraw okay so we actually
did that a little different if you go
through this at home uh maybe you'll do
it a little differently but we kind of
just wrote our own thing so it doesn't
do that it doesn't check the external
contract completed it just keeps a local
state okay let's deploy this thing huh
let's go uh let's see so uh the first
thing we need to do is uh yeah I'm not
going to edit the default Network I like
doing just D- Network okay yarn generate
should give us an A deployer account
okay and then yarn
account should tell us about our account
and I need to send in some sapoia so
I'll use a burner
wallet and I'll put it on sepolia
nope it's
loading
internet all right sorry here we go
sepolia and we're gonna send
um uh yeah I don't
know how much do I want to send
like a 100 bucks or something it's aoia
it doesn't matter okay let me scan this
dude's
address all
right okay so we sent $100 worth of
sapoia to our deployer account and now
we can do yarn
deploy D-
Network
sepolia good old test
network but but uh yeah this won't be as
fast as like an L2 we're going to have
to wait for the block to get mined so
this will be pretty slow and I think Sao
is pretty expensive too isn't it oh no
what did I
do not enough not enough funds okay $100
was not enough let's send some more
sapoia gas is pretty crazy let's let's
send $1,000 let's send
$10,000 okay that's definitely going to
be
enough and then let's trigger the deploy
again in and see what
happens so we're waiting for a block to
get mined on sapoia oh no no
way I
mean how how
much that can't be right how much let's
check our account yarn account how much
money do we
have it seems like it shouldn't cause
that oh no it's zero okay what's going
on here let me scan this dude's address
again maybe I have this
wrong send in a thousand
again 7e okay let's try that again
hopefully we have a balance on
spolia nope uh maybe the RPC is messed
up let's uh let's do a different network
okay quick quick fix Quick Fix I'm going
to put this out on a live Network I'm
going to pay pay real money uh so what I
want to do is adjust the threshold to
point
want to spend like three cents here
right because I'm this money is going to
be gone forever so I don't want to spend
too much
money uh yeah this looks good okay uh
let's try deploying this to uh base or
some maybe optimism let's see so we'll
do yarn account again and get that
account let's go with optimism I did
base
earlier okay so yeah sending real money
here this is uh not not the best I'm
going to send $1 that should be
plenty because that money is gone for
well this money won't be gone forever
but once we lock it up in the contract
it will be gone forever maybe I should
just make a
withdraw in here
right let's just make one real quick
function I'm just going to set it up so
anybody can call it someone's G to steal
my money that's cool let's do it all
right yarn
Network optimism all right we're going
to use the optimism L2 we're going to
pay a couple cents we're going to deploy
our contract there instead of using it
test Network because that was not
working we're we're going to straight up
pay for it and by the way if you're
doing this at home uh go
use optimism sapoia I think that's what
we recommend folks use it's a it's a
test Network so you're not burning funds
like I'm doing right
now okay we deployed our Staker all
right this thing is live now I want to
edit that uh config file right the uh
scaffold config big where we set what
network we're on right now we're on hard
hat if we change that over to
optimism and hit save the whole app
should now move over to
optimism all right here we
go
yes bless you and it's going to have a
switch to
optimism and let's go ahead and stake I
don't want to stake 0 five I got to be
careful here because I could spend some
real money and I don't want to do that
uh let's go to the stake function and
let's do
threshold and let's send it
in what's it going to cost
us 34 cents not
bad
okay
so there goes the money it's now locked
in there right if we hit
reload it should be sitting right there
right there's the 34 cents okay and then
we're waiting for that time period to
happen right time left is zero uh now
there should be the execute function
let's see what
happens all
right all right the 34 cents should
disappear from here completed is true
uh hit reload here this should be empty
yep and this dude should have the 0.1
right there and anyone in the world can
call this button right now and make 34
cents uh I'm gonna go ahead and do it
though before anybody else gets to it I
could even get no I can't get front run
because it's
a sequencer centralize
sequencer if it goes to the MIM poool
and someone's watching the m poool and
they see me put a transaction in and
they can just copy my transaction and
turn the gas up a little bit and front
run me and steal the
money okay it it worked basically uh we
were able to I bet I can't turn this in
on optimism though can I let's see Can I
submit the challenge no so so what you
will do is you'll you'll deploy your app
whoops I kind of want that back you'll
deploy your app
uh and then you'll turn it into oh yeah
it looks like yeah you want to do this
longer yep and then we'll deploy yep and
then it has you ship the front end so
you'll do a yarn verell and you you'll
upload the app so once your contract is
up you need to upload your app then you
submit that here and that is the staking
challenge kind of a a a neat little
simple but
powerful uh uh tool or concept powerful
coordination
mechanism okay let's see here now let's
let's let's go through the rest of the
challenges a little bit faster I think
writing that one was nice it was good to
get in and like write some code but
let's just kind of like speedrun the
speedrun for for the rest of the
time so let's go look at these
challenges let's
go I'm just going to go to the GitHub
oh scaffold eth challenges is it that
there we go okay so uh let's look at
challenge two so we've already done
decentralized Staker we're going to do
challenge two now and this is a token
vendor so this is really cool you're
going to have
um one smart contract that acts as your
token and then another smart contract
that you'll send the token into and it
will sell the token a little token
vendor
right yes so smart contracts are kind of
like always on vending machines that
anyone can access let's make a
decentralized digital currency then
let's build an Unstoppable vending
machine that will buy and sell the
currency we'll learn about the approved
pattern in ERC
interactions work okay so we need we
would basically create a
token uh let's see is that here yet oh
no no no no we're we're just going
through it let's let's let's not write
any more code let's just go through
it then you would edit the front end to
display
it and very verify it okay cool so uh
yeah same thing right you would clone it
down you check it out you install it you
run yarn chain you run yarn deploy you
run yarn start and then you have a front
end that comes
up and uh you'll work through you know
can you check the balance of can you do
a transfer just making sure like balance
and transfer works in the token you can
send the token around now it's time to
build the vendor right this will be the
second contract you're going to build a
vendor.
Soul so a second
contract and you'll have some exchange
rate so this is tokens per eth right if
you put in one eth you should get a 100
tokens
back and looks like you'll have them
you'll write a buy tokens function that
will look at the message.
value so
you'll call buy tokens and you'll send
in some eth and it will look at the
message.
value and then do the
calculations of tokens per eth and then
figure out how much of the token to
transfer to you so you'll send eth in
and you'll get tokens
back looks like there's even an event
that's
admitted yep lots of good stuff
here um pretty pretty simple and
straightforward you're basically
building a token and then selling it out
of another
contract let's see o vendor buyback okay
the hardest part of this challenge is to
build your vendor to buy the tokens back
the reason why this is hard is because
of the approved pattern so the way ERC
accept the token you don't just send the
token to it that that would make a lot
more sense but that's not how it works
you basically approve this contract to
take your tokens and then you call a
function on the contract and it goes and
gets them really weird pattern you just
get used to it after a little bit but
this this is going to help you kind of
get over that first bump or hump so yeah
you you would have to do two
transactions right
so buying tokens is easy you just YOLO
some eth in and you get some tokens back
but selling the tokens you have to call
approve on the token in one transaction
and then you have to call a second
transaction that calls the vendor and
tells the vendor hey I've approved this
token you can take it and do some
stuff and it it
will there we go so if you ever want to
deploy a token and sell it for eth this
is a a way to do that but uh only on
test networks don't don't be don't be
deploying to tokens on live networks
unless unless you really want
to okay so that is challenge one that is
the or that's challenge two that's the
token vendor we're learning about ERC
contract we're learning about that
stinking approved pattern all right
Challenge
three uh is a dice game so Randomness is
particularly tricky on a public
deterministic blockchain basically the
chain shows everything so if you wanted
a random number it's hard to do in a
deterministic blockchain you can't like
Randomness is very hard so a weak form
of Randomness is to use the previous
block
hash and the problem with doing that is
you can set up an attack our contract
and that's what you'll do here so
basically there's this dice game you pay
some money and you roll if you win you
win some money if you lose the money
stays locked up and so how you attack
this is you build a second contract that
looks at the same thing that this
contract is looking at in terms of
Randomness to figure out
will I win or not and basically you set
it up so your dice contract your
attacker contract only pays to roll on
winning uh numbers basically so you you
just sit there and you uh call roll a
bunch of times on the attacker contract
and it waits until the block hash is
just right and then it calls it and you
win so you basically only roll on
winning roles and so that's not good
right if you wanted real Randomness this
is kind of falling apart and you can
attack it but this kind of teaches you
how that works you're going to make a
rigged contract and you'll call this
rigged rooll
function and yeah it's a really fun
really fun little challenge I think Mr D
did the dice pretty cool dice like a
dice Challenge and that teaches you
about Randomness and about about how to
make an attacker
contract uh that can predict the
randomness basically or only pay if it's
going to
win okay we're getting there so now is
the decks the decks is probably one of
the most important builds you will make
uh through speedrun
ethereum um thinking of our token and
our token vendor we were able to Mint
the token and put it into the contract
and let people buy it but uh what if you
wanted people to be able to swap put in
some tokens get back some eth and you
wanted the price to be variable well uh
aex is a really really cool smart
contract where it um keeps reserves of
both tokens so it'll hold a whole bunch
of your token and a whole bunch of eth
and it will hold them at a ratio that
tells you what the price is right so if
this token was exactly one for one eth
you would have 50% of each of the tokens
in right but maybe the token is worth
one token in basically but you have
these reserves and these reserves allow
you to do these swaps and for the first
time ever you can do that in a
decentralized way you used to either
have like an order book system or some
kind of like centralized choke point
that could fall over but in this case
it's fully decentralized and it's all on
chain the there's some bad things like
impermanent loss but that takes uh
you'll have to really dig in and kind of
like learn all of that stuff um maybe a
good too long didn't read is that those
reserves are important for making the
swap work and the more reserves you have
the the uh cheaper the swap is or the
less slippage there is basically so you
want to incentivize folks to be
liquidity providers so the way it works
is someone puts in some uh eth and some
tokens and every time there's a swap a
tiny little bit of that is left behind
and so slowly the contract actually like
gains value as people are swapping back
and forth because they're leaving a
little bit behind and that is to
incentivize the LPS the liquidity
providers to provide that liquidity and
this is uh this is expansive by the way
so a really really cool uh concept is
the idea of a hyper
structure boy I didn't get it
structure uh from Jacob from Zora but he
talks about how hyper structures work
and they're Unstoppable they're free
they're valuable they're expansive this
is this is what I was talking about
expansive basically the protocol itself
incentivizes people to LP so the more
money you put in the more money you make
and that's how it's supposed to work and
therefore if you build it correctly and
you put it out there lots of people will
provide liquidity because they're
financially incentivized to do so it's
permissionless it's positive sum it's
credibly neutral check out hyper
structures it's a it's a really cool
concept
okay so uh in this one in this Dex we'll
put in some liquidity I think you end up
let's
see whoa what do we do so the structure
there's going to be like a swap
function yeah so you're going to be able
to do eth to token or token to eth and
balloons are our
token yeah and here are the reserves
right you have to uh so there's a
function to swap but there's also a
function to put money in or a function
to pull money out in terms of
liquidity yeah and you also need to
initialize it with some initial
liquidity and that kind of sets the
starting
price and yeah here's this this this is
a the very popular uh what happens here
if so this is the old position and this
is the new position you put in token a
and you get out token B and you can see
by this curve the farther you go this
way the more slippage there is so the
more reserves you have the smaller that
little chunk
is uh but yeah go go take on the Dex
challenge there's a lot of intricacies
here that I'm not really getting into
this like constant product thing there's
a lot of great stuff to learn here go do
this on your own sometime go through the
decks and uh you'll you'll learn a lot
and it's really like one of the neatest
contracts let's see liquidity we already
kind of know about let's see if there's
anything else here before Oh here does
this show the swap yeah so it's going to
kind of give you a little drawing for
the when tokens go in and what comes out
yep and then you deploy it live and you
verify it and you turn it in and uh our
autog grader will go swap some token on
your decks and make sure everything
works
right looks like there's even like a
YouTube video here I wonder what that
one is okay so those are the most
important challenges everything else
from here is like uh like dessert
basically challenge for taking on the
decks is like the challenge you you you
if you can build a deck you can build a
lot of different things like this is a
good like am I ready yet kind of test
like can you sit down and build a Dex
okay uh there's three more challenges
here um there's a state channels
application this is really cool because
it uses signatures you don't always have
to put everything on chain sometimes you
can do things between parties with just
signatures and and sometimes you can
even have like a smart contract that
those signatures settle to and uh in
this one you kind of uh learn about
State channels and about kind of like
how scaling could work or uh does
work and then I think is multisig next
let's see what's
next yep multisig so multisig is a
really cool let's go look at this uh
let's go look at this
code so a multisig is a smart contract
and you can send money into the smart
contract and multiple people need to
sign to make that money send out
basically right you have to get like
three out of five signatures let's go
see what the code looks
like yeah there we go and then if we
look at
some function here yeah so you're going
to keep track of signers you can add and
remove
signers there execute transaction this
is really interesting let's look at this
function here so you pass in some two
address and some value and some data and
signatures and then it actually goes
through and validates the signatures and
then if everything is valid and you have
enough valid signatures right you'll
need to
have uh valid signatures needs to be
greater than or equal to signatures
required and if so you can call the
function it actually executes whatever
you want it to just some arbitrary call
data gets executed there and that's a
multisig really really cool co uh little
multisig really handy uh especially uh
for storing large amounts of money like
a dow has a treasury so uh like a
multisig is like a Nosa safe if if you
don't have a Nosa safe yet you should go
get one uh nois safe it's it's a great
way to uh hold your money in an account
where it takes multiple signers
basically to move that money around so
it's just a lot safer let's say you have
three accounts and one of them leaks you
can just remove that leaked account and
then put a new account in whereas if
that leaked account had money on it the
money's gone forever right so the
multisig is a a nice way to kind of
safely hold your
funds uh here yeah it's an
ecdsa uh let me find
it there there's a function called
recover right here
so what this function does do you see
that is that big enough so it's
um so you can sign any arbitrary message
so uh Austin likes beer I sign that
message and then I send it in here and I
take uh the thing I signed which would
be in this case is just a hash but it
could be like a string I I think this is
a hash of a string and then the
signatures so with the message that they
signed and their signature you can do a
recover and it will give you back the
person who signed it and this is like
really powerful uh tool for a lot of
things but doing ecdsa recovery in
solidity is really nice like it leads to
things like meta transactions and all
sorts of other cool things you can
do does that make sense did that answer
cool okay all the way to the bottom SVG
and F this is kind of like the the
ending challenge uh
oh what did I do
here this is kind of the last challenge
uh you're supposed to make an nft just
like those nfts that we did at the
beginning where we were minting the
little Buffalo and the zebra those were
going to ipfs though when you minted
those the image is actually stored on
ipfs and it's like the hash of the image
is stored in the smart contract cont
ract so it's kind of like not as cool
with an SVG nft you actually put the
contents like how to draw it like if you
go look at an SVG it just looks like
some code but you put all of that code
right into the contract and then the
contract itself can render the
SVG pretty cool little challenge yeah
you make some lugies I think optimistic
loues is that what they are
classic but that is the last challenge
and uh I would recommend y'all going
through this on your own time at home
you can go to the scaffold eth repo and
find scaffold e two challenges or just
go to speedrun
thee.
uh and I think that's that's
mostly what I have to present but uh
maybe open it up for questions if
anybody has questions about anything or
concerns or anything um I'm all ears
yeah uh what about the uh can I do some
like PR to add some more challenges
because for example I work with snarks a
snark compiler so maybe an example for
verifying Stark or like extending the
something is so you're saying could you
PR into scaffold eth some new challenges
uh possibly we I mean that state
channels was actually made by someone
else and they PED in so it's possible
but it's more likely that you just like
Fork speedrun a the and make speedrun
starware or something I think actually
someone did that exact thing let me
see did you say
starkware SN oh oh snarks I see yeah
yeah there there is scaffold yeah so
maybe you want to do some ZK stuff or
something like that
yep uh speaking of that let's go to um
if you go to build guild.com Biddle GID
and you go down to the bottom there's
this mirror board there's this text Tre
link right here it's kind of
buried but uh it has all sorts of other
challenges Beyond just the the speedrun
challenges all sorts of things that you
can build uh on chain and yeah there's
like a whole section here on zero
knowledge oh man how do I
move no no no no dang it oh there we go
that'll work okay so yeah you can do
like this this just like covers like all
these different concepts within the
space and how to just like test your
knowledge and build things there's like
a little circom starter kit and um the
the guys who made Dark Forest are
actually here they're the Frog guys the
guys with the Frog hats actually made
this game Dark Forest it's like one of
the coolest games ever made on
chain uh using ZK snarks and or ZK Tech
in some
way okay uh I think I'm about done but
definitely open for more questions if
anybody has any questions go speedrun
ethereum that's the important
thing yes
yes uh this is a beginner session I
think I'm going to ask very very dumb
question if you don't mind I'm very
beginner um I was trying to understand
more on the storing on chain and how to
use that instead of utilizing any
database is using uh chain as a database
like how does it work and which parts
actually is advis to store and chain
which parts not or how that that's
that's this this is this is a kind of a
moving Target because you know a few
years ago I would say you're making a
mistake if you're storing lots of stuff
if you're using it like a database
you're making a mistake it's not meant
to be a database it's a very expensive
slow asynchronous database right um but
the the needle has moved and l2s now
exist and l2s are super cheap maybe it
starts to make sense to actually start
using them like a database again I think
you have to be careful because this is
all public right like everything that
goes in there is going to be visible to
everyone so if it's like medical records
or something like that that's all like
no way can you do that right or like
anything that could dox someone like
connecting an account to an address and
someone shows up at your house with a
wrench like there's a lot of things that
you don't want to put on chain just for
like privacy concerns but you can store
strings you can store numbers it works
kind of like a database and on an L2
it's a lot cheaper with blobs blobs are
going to get a little bit more expensive
so it will get a little more expensive I
think but I think they're trying to push
it cheaper and cheaper
too but does that sort of make sense it
does make sense but again like so I
should not really treat blockchain a
database or can I I think you can yes
like if if you wanted to make Uber on
chain you would have a very hard time
right that's like a con a constant thing
we see at hackathons it's just not very
practical oh no what did they do uh but
maybe there is other places where you
could use it like a database and it
makes sense I think it comes down to the
application and how sensitive the data
is and how much you're willing to store
like pay to store it but thanks to l2s I
think yes you can use it like a database
again
thanks more questions
yes okay thank you uh on challenge zero
uh you said that the image zipi image uh
was still on
ipfs it was on
ipfs here let me let's see is it still
up the the image okay so what happens is
you have a manifest which is like your
name and your image link and it's like a
Json object and then inside of that was
an image link and that's what we're
using to
render that goes into uh ipfs and you
get a hash back and
so it's not stored on chain like the
image itself is not stored on chain it's
the hash of the image that's stored on
chain so you go to the blockchain and
you get the hash and then you take that
hash ipfs and get the information back
but it's not stored on chain it's stored
in
ipfs does that make sense it's just like
the hash that goes on chain yeah okay
yes uh I would like to know uh to
understand the interaction because when
you hit on the the mint button yes it
means an nft yeah now I would like to
know uh where
does the interaction between the
contract and the and ipfs is located so
at which level is this interaction so do
I need if I want to implement it in in
my code do I need to to get a such um an
API key to drop my image on the ipfs no
okay so ipfs is like a distributed
storage system and what happens
is you're you're you go look up content
it's content addressable so like an
image goes into ipfs it's not like going
to the cloud somewhere it's going to
some machine somewhere right so you you
actually have to run an ipfs node and
you have to pin your images on that node
to keep them to stay there so if you you
can add things you can upload things to
ipfs but you have no guarantees that
that thing will stay in ipfs so you end
up having to run your own Pinner usually
which is uh just like a an ipfs node
that you add files to I I still don't
know if I'm fully answering your
question like so yeah maybe maybe you
could
ask yeah how am I answering your
question yeah yes yes I think you go I
have another question on the second uh
the first challenge number one yes you
implemented uh a protection against a
reany attack yeah yes uh I read
somewhere that uh the S function uh is
subject to a a limitation the gas limit
of
didn't understand you something about
reentrancy yes when uh this is something
I read I don't know if when you use send
to send ITA or to
address yes it is subject to a
limitation of
gas yes yes when you do a DOT send here
the best place to look this up is go to
solidity by
example and there's a really good
example here about sending
eth where is that right here sending
ether and this explains it really well
uh this 230 this 2300 gas you're talking
about if you use transfer or you use S
it basically locks it at this much gas
and so if you want some other execution
to happen on the other end of that
transfer say you're transferring to a
Smart contract and it executes some
other stuff you will run out of gas so
what you need to do is do a DOT call
instead so the way you send eth looks
like
uh where is the dot call I didn't even
see it there
oh here it is yeah here it is here it is
so you do two address do call and then
you send the value in so really weird
kind of thing it looks like you're like
calling a function on this contract but
you're just sending money in uh but
that's the way you do it if you want to
forward along all your gas like if it
needs to do a bunch of execution on when
it receives that and uh needs to spend
some gas you'll want to use
call instead of do sender.
transfer okay
okay so at this moment when I use call I
should not Implement reic
protection uh it depends on the the
application like you you need
the the reentrancy stuff is kind of
different than this stuff this is this
is just like how to send stuff you need
to implement re-entrancy protection if
someone can re-enter your app and uh
like attack it
like the what we did to mitigate it was
create a variable and store the balance
into the variable and then zero out the
balance and then send the money so by
the time the money gets to them their
balance is already zero and they can't
re-enter so it's not it doesn't have
anything to do with how we're calling
send or transfer it's everything to do
with how the code is structured and if
it's structured in a way that is
vulnerable to reent
princy okay thank you
yep any last
questions thank you for the build Guild
coming out to support me you guys it's
probably pretty boring listening to this
talk we got a got a four more hours of
it tomorrow
too all right thank you all thanks for
having me go speedrun ethereum
what AI do you use for
the was very good to find a solution the
AI yeah it's
c yeah if you're not using GPT every day
you should be for sure
go to
for e
h
B
o
a
sh
for for
go e
m e
e for
me
t
oh e
that
