he
[Music]
w
everybody everybody
o
coming coming coming
oh oh
oh
ohing cominging
n
cominging
oh coming coming
you
coming coming
you you
ohing coming
to
bodybody
coming coming by
he a
everybody
everybody everybody everybody
coming
body
e
back
back back back
back back
hi hello um so I'm M or you can call me
Matt like the short for Matthew uh I'm
from al2 beat I'm half of the tooling
team in the al2 beat um and my workshop
is on the Discovery it's the Tool uh we
use we build um to help us research uh
projects and it turned out that it is
really useful at uh solving all of our
problems I mean not all but like
majority of uh problems I'm going to
later talk about
um so a funny story is that I almost
lost the demo part of this presentation
and the only surviving copy of it was
like some random VM buffer so I just
wanted to point it out um okay so there
is a lot of projects on L2 be um you
know the the amount of project is
growing and we internally expect there
to be at least a, l2s uh So currently
you can see that there is uh 51 rollups
and um 66 validum and optimums um so
around let's call it uh 110 projects um
of only l2s we also track Bridges um not
to the same standard but um for all of
those l2s we have uh a minimum bar of
data we want to show and that would be
uh the risk croset um we want the risk
rosette to be obviously correct and the
standard for this data is actually quite
High we want um to show data that is
correct so you know you don't lose your
funds you don't make a decision based on
our data that is
incorrect um so how how to even maintain
all of this right uh so just like a
quick um a quick um math lesson right so
imagine that we have 110 projects and
every project has a single update uh
every two months right so it's actually
quite um Spar we see projects that are
updating way more often um and even if
every project had a single update every
two months we would have an 84% chance
of seeing at least a single update in a
day right so it's basically guaranteed
that every single day something new will
change on chain we need to be able to
detect it see it see what's changed and
act upon it and also like even if we
assume that um an update happens every
six months the chance is still 45% right
so it's like a Coos basically um and
these chances are basically always
working against us the more and more
projects are going to be added uh the
higher those chances are basically to be
I like I said there is a high chance of
an update happening and we need to be
able to fastly see that it happened and
we need to be fast in reacting to it if
for example arbitrum or optimism right
any of the top docks has an update and
we take like three weeks to process that
update or to even like see that an
update happened then we are showing
incorrect data for 3 weeks which is
actually a quite long amount of time
when it comes to web 3 um when an update
happens we need to know what changed so
it's not enough to see that something
has changed we also need to know what
has changed right so so that any of the
risks assumption that we had before are
now different um so also we need to be
able to look inside the project and
compare to the previous version um and
as always we want to automate as much as
possible you cannot get to 110 projects
listed on a website and do all of them
manually like um it is possible with
human effort but we don't have the
amount of resources to do it so right
now we have four researchers and we
maintain all of the 100 projects with
only four people and we also manage to
do stuff uh that's you know
additional um so Discovery essentially
like I think is at the core of solving
all of those problems of course
Discovery is not a Panacea it does not
solve all of the problems by itself um
but of the problems that I listed um
Discovery is always at the core of um of
the solution um so the mental model of
Discovery is um like this like I like to
think about uh Discovery this way and
also I like um understanding things from
the low level so let's try to understand
the inputs and outputs of
Discovery the input of course is the
ethereum state we want to see uh what is
the state of each project on a given uh
let's say block number um so the input
to Discovery is that ethereum State uh
of of course we are not sending like an
snapshot.
zip to Discovery we are doing
something like uh I mean we we use RPC
providers which is essentially uh having
the entire theme State at your
fingertips you can do uh any call you
would like um and to facilitate the like
querying uh the data from uh the state
we have a config Json which uh instructs
the uh the Discovery program which data
we are interested in and um how to
process it um and after passing those
two inputs to Discovery uh and output is
generated which is a discover Json file
uh of course it's all a
simplification uh the more like the
actual mental model which I don't even
think is correct and there's missing
some parts is more something like this
um so that's what I mean when I say like
the discovery is at the core right uh
like all all roads lead back to
Discovery um I'll try to during this
workshop I'll try to um touch upon all
of the things that are listed
here um so you'll be able to understand
at least how this flowchart uh
happened okay so since um I myself am a
visual person I want to create I want to
show you a uh demo of
um of something nice to look at so this
is something we have been working
on uh which will um enable us to move
from um command line to a uh graphical
user interface um so right now we call
it we are calling it Discovery Y and um
let's uh see like all of the projects
that are listed here are projects that
we are uh tracking with uh Discovery so
so I have picked uh Zora for the project
we are going to be using D this during
this Workshop um so let's see what kind
of data we can expect to see in in this
tool for Zora um so of course there is
like a lot of things to take in um but
let's start from the left and keep going
right um there are uh on the
left the things the thing is that they
look like files but they are actually
contracts uh they are kind of inspired
by uh the file view in visual
studio and um you can
see maybe I don't know the contrast is
not the best but I hope you'll see that
uh we have two contract contracts which
are the initial contracts and by initial
I mean the contracts from which we are
going to be starting and all of the
contracts that are on the left have been
found uh based on uh those two initial
contracts so it is as you can see like
it is quite um useful to be able to find
two contracts used in uh in a project
and then basically find all other
contracts used by that project um and
also this updates automatically so if
anything new happens um new is added or
is removed um they automatically updated
um each of those contracts uh has some
vales right so uh each contract has uh
an address a name a description given um
by a researcher and uh let's focus on
the fields uh for now so fields are um
State variables that we have found in
the ABI which are um either public
variables or um functions which which
don't take any arguments and just return
something so we are trying to build the
uh state of the contract through the
there is also one more part which will
be important later during the demo uh I
mean during like the workshop part which
is that we try to build um arrays from
um functions which take a single
argument which is of type integer so we
just assume that this function is like
get something by index and we try to get
all of those things um um and um you can
see that there are actually addresses
inside of those values U and those
addresses lead to other addresses um and
this is how Discovery works it gets all
of those State variables and if it finds
a address it assumes that this address
is also connected and just uh keeps
discovering uh on those addresses um and
the third view here is like a graph view
so all of those projects here um are us
used uh in in Zora and uh the way that
um it works is for example let's focus
on the security Council maybe not that
that's not the best but the system
confli right uh so you can see that
there are some um State variables and
they point to um other contracts through
the through this view it is really easy
to understand how the project is built
what contracts reference each other um
and how the data flow inside the project
happens um of course this is not the
default view kind of like the view
allows you to select them move them
around you can color these um whatever
your heart desires to make it easier for
you to understand we have two layout
algorithms since it's a graph view you
can use like D3 uh we called it slow
because it is not that fast it uses for
Force um Force simulation to lay out the
graph we also have more like a
hierarchical uh view which just lays the
uh graph from left to
right and the third thing is um the code
so um all contracts have um source code
and uh let's go back to the L1 standard
Bridge example and we want to show the
code to the researchers because to
understand what a contract actually does
you need to look at the source code
um and you might be weirded out by the
fact that there are only two files um
I'm going to touch uh upon this a little
bit later because it is actually quite
important uh why there is only two files
and not like more um so yeah you can
just view the code in here um the part
that I want to also show is that we see
that it is important to be able to
switch between views right so I can
click L2 output Oracle on the left in
the list View and it is selected in the
values and the nodes panel uh vice versa
I can select something in the values and
it is selected in the list and the noes
View and I can select something in the
noes View and it is selected on uh every
single audit
view um so this is something which is
like um really graphical and nice to
show and it basically is only the look
inside the discovery Json this is just a
nice way to visualize what's inside the
discovery Json um but it doesn't touch
upon
the way of how uh we even got that
Discovery Jason right so uh it is
something we are working towards it's
not yet ready you can only view thing
it's basically read only at this time uh
but in the future we hope um to make
Discovery this uh so you'll be able
to do your research in a nice uh
graphical environment um and do anything
need um so yeah let's goodbye to yeah go
ahead yeah yeah so the question is how
do I get the source code since it's not
on chain so um I kind of skipped uh one
assumption is that from by the etherum
state we also kind of consider um The
Ether scan source code
database um even if you go to L2 beat
and look um um into the projects that we
list if a project does not verify their
source code on eisan we give them like a
big red warning uh so we expect you to
verify your source code to show
transparency to uh the users and to the
researchers so they can do their stuff
so it is something that I omitted but we
do use ether scan or like ether scan
derivatives like block Scout or stuff
like that to get the source code and uh
we heavily rely on the source code
because if we didn't get the source code
we wouldn't be able to call anything
because we don't know what the adbi is
right um so yeah if you have any
questions do please shut them up during
the workshop um but I'll get back to the
presentation
yeah uh we don't try it end you don't
try it deile um no I mean
there was one case where we knew what
the source was it just wasn't verified
so we like forcefully like we verified
the source code for the project because
they didn't want to do it for some
reason so we just did it um and we are
not trying to decompile the um the bite
code in any way I mean if it's something
that we can't get the project to verify
and we need to look inside we might de
compile it but Discovery does not try to
do anything uh like that it just assumes
the happy case where
the the source is on Ethan or whatever
Explorer the chain is using um and just
go from there but yeah if we hit a snag
like there is no Source we just either
accept it as we cannot look inside or we
talk with the team to verify this let's
go okay if there are no more questions
I'm going
to uh keep moving forward so um going
back to the mental model because I I
think it is really important like the if
you um leave this place with a single
thing it's just
that Discovery is just a program it has
some input it has some output right so
the output is this discovery Json and
the input is the config Json C and the
way you can think about Discovery if it
like makes easier uh makes thinking
about it uh easier for you is that it's
like a scraper for a website um so
scraping a website looks like uh you put
some address of a website it downloads
the the content of that website it tries
to find any links and it follows those
links recursively Discovery essentially
does the same thing but it doesn't
download websites It downloads the state
of contracts and it's follow and doesn't
follow links but follows addresses to
other um
contracts um and of course Discovery is
not just like a simple thing that is
like a blackbox there are things
happening inside uh that we are going to
be talking about a little bit so
discovery is able to detect whether a
contract is a proxy uh it does the
source code flattening I'm going to be
talking about it later like I said um it
does template matching it is something
that also we are going to be touching
upon uh during the demo part uh it has
custom honders which it executes we are
also going to be doing that during the
demo and it has Type casting I left type
casting out because it is really it
would take like 20 minutes or 25 minutes
to explain all of it um so I just left
it out if we have time or you were
interested you can hit me up after the
workshop and I'll be glad to talk it
talk about it with
you and of course there's like an engine
engine that orchestrates
everything but yeah it's like there are
things inside that black box um so I
have a demo prepared um there's a QR
code if you want to follow along with me
please do um and if you get stuck I'll
be able to help you gladly
um I'll be going over the same thing
personally so if you just want to sit
and just listen no problem the website
has instructions so you can do it now or
later whatever um and also I really hope
that the website is works for you
because like it selfhosted so if it
doesn't work try it disabling your VPN
try a different country uh I tried it
like five times it worked uh without any
VPN so I'm going to give you like a
minute to uh get to the website if you
want to follow along and yeah
okay I expect everybody to be on the
website right now um if you didn't
manage to uh scan the QR code or type it
through just ask your neighbor for
uh a nice deed so they'll be able to
show you the URL okay so um uh like I
said I'll be going over the same thing
uh personally I have it um on my iPad so
I'll be going over all of the things
that are written in here and also I'll
be like uh adding some additional
context for it um and also this is a
important
part um I for Discovery uh from the l2b
repository just for the purposes of this
demonstration uh if you actually want to
uh use Discovery yourself please use the
original repository because I'm not
going to be maintaining this Fork uh and
this can get really St really quick
um and why did I fork it it's just
because we are not no it's an internal
tool tool we will try to make it more
available to the public it's just it is
in a rough state right now but it is
still cool to uh show what is what this
tool is able to do
okay so um is this
visible like the contrast is okay okay
um so I have downloaded the uh the only
thing that I have done is just npm
install uh and if you if it worked you
should be able to just do npx
Discovery um and something along the
lines of this should appear here uh so
there are two subcommands you don't
really need to worry about them so there
is the single Discovery
it's it's just for convenience if you
really need to discover something like a
single address um you put it there but
if you want to build like a project uh
you'll be writing a config Json either
way so there's also invert invert is
like we used it to build those graphs
you saw we used merid before before we
got um the protocol bit I was showing um
so yeah don't worry about those the only
thing that you're interested in is this
cover um
so the most boring part of doing
anything fun is setting it up and
configuring it um unfortunately I'll
have to leave uh the part of
configuration to you um you need to
configure two things uh you need to
configure the ecan API key so you can
actually call Ether scan and you need to
configure an RPC URL and the sad part is
that um only few uh rpcs work that well
with Discovery um I'll say that the fre
tier of alchemy worked for me without
problems uh so if you have Alchemy do
use it there is like an asterisk where
rpcs that only support uh block ranges
of 10,000 uh when you're cing for logs
uh do not work with discovery for
Simplicity we are essentially expecting
you to have an RPC where the block range
uh for log squaring is basically
infinite um so yeah the you'll have to
set this all up I'll just copy my uh n
from
um uh from the previous tries of that uh
so I have an n and you should probably
do the same you can always like export
the same variables if you want
um so now we can get to the actual fun
part um and before we actually configure
anything um you know we need an initial
address uh the address in the website is
already there but like this is also a
good question like how do you actually
get a hold of like any address that
belongs to a project and I'm going to
show you like a simple example that you
can uh find addresses belonging to a
contract uh to a project um so we are
going to be doing it this way so like I
said I chose Zora for this presentation
um so let's just go to the best website
and find
Zora um and how I do it is just go to
their website of any project and try to
bridge
something and also it is important there
are multiple Bridges um for for example
but what you want is the official bridge
I know it's touch it attaches subject
but in L2 beat we assume that the
official bridge is part of the rollup um
I don't want to get into it but make
sure you have the official official
canonical Bridge uh to um to use and uh
we just want to bridge uh like the
smallest amount of if and do please
don't Bridge anything uh we just want to
get to the part where it says sign and
don't sign please uh we just want to get
to the part where it shows us the
address we are going to be interacting
with so let me just uh Bridge some
East yeah
whatever okay so this is the address of
the uh contract we are interested in and
we can just copy it and uh store it for
later um so now how do we configure the
uh Discovery to start um at that address
so um we need to create a um folder
structure um that Discovery is able to
understand so this folder structure
looks like this so just uh I'll type it
out here so Discovery is the folder
where all of the projects that you will
use live basically uh and there're like
configurations uh results flat files
source code anything that uh pertains to
a particular project lives in uh
Discovery um and the actual project is
like that so anything related to Zora
lives in there but there's also one more
level which is uh ethereum this is the
actual chain you're going to be doing
discovery on
um because we have the ability to do
discovery on multiple chains like I
showed maybe I'll go
back um and the discovery why so if you
look here most of these projects say
ethereum but for example zik link Nova
says 10 chains that's because um a
project can have contracts on multiple
chains and
and the way that Discovery works is any
evm chain just works it just you don't
really need to think about it you just
say that you want to use uh that chain
of course you need to configure the rpcs
for it and the Explorer for it but
otherwise it just
works so yeah this is the uh path we
want so Discovery SL z/
ethereum and in that path uh we want to
create a config Json
C file the C is for comments it is also
there is many parts where you can see
that it's not that ready for public
release
um I think Discovery will fail if you
don't provide like if you just do dot
Json it will fail so it is
touchy um okay so what are we going to
put into uh the config Json so it is an
object where you have to Define two uh
redundant Keys which is uh
chain and that's
ethereum uh and also name of the
project so why do we have to type the
name uh twice um since it's already in
like the
uh folder
structure it's just for
um Simplicity if you want to uh read
this config Json in a different tool
you'll still know for which project it
is um and now we get to the simple part
there is also one more key which just
says like what is the initial addresses
you can have multiple we're just going
to put the single
one um no so the way we do it uh in this
in L2 be is that we have a bunch of t
tests that just validate if the config
you have created is of what we expect we
also have like a bunch of assumptions
where the name of the chain in the
config is the same as the slag on the
website but we have tests for all of
that but you can put anything like you
could put your name inside and it will
just work it's just like um there is
some schema that they that the discovery
needs to see uh and it's just like fing
it out
but yeah it's just a string like as as
um Discovery is
concered okay so we have put the L1
standard Bridge uh as the initial
address and since this is a Json C file
you can put comments so L1
standard uh Bridge we are trying to uh I
know that half of the research team is
trying to enforce this standard and the
other half doesn't really try but um
yeah um so now what we need to do is we
we need to run it
um and this is another part which is
like uh not the best which is um the way
that the ordering is done in the folder
structure is Project chain but on the
CLI it's the other way around so you
need to do eum
Zora um and if you did everything
correctly it should start spinning out
logs um the first run takes a little
while um and if it fails you'll probably
know it failed um but um this the
interesting part is here that we have
gone to this
um address through the source code we
have found that it's named L1 standard
bridge and we have found four relatives
uh that four relative contracts or um
entities like also EAS um referenced by
um this contract and as you can see like
we are putting those relative addresses
back onto the stack and we are rovering
them all um and ideally at the end we
have 61 uh contracts or EAS uh and the
discovery is done um we have like limits
so there is like a depth limit uh of I
think seven and and there's also a Max
address limit so for certain projects
that we don't really know uh or for like
big Bridges the amount of contract is
really big um the biggest um project we
have is transporter uh which has 350
contracts and is really like it is
mostly just a stress test for Discovery
um so also Pro tip um since like I
showed you before the mental model of
Discovery is this input output like a
functional programming Paradigm or
whatever is that you'll need to be
rerunning Discovery a lot so um like you
saw it takes some time but uh if you
look there is a handy dandy cache so
Discovery caches all of the calls you
have made to a file so if you need to
rerun the same Discovery um it already
has all of the RPC and eest kind of
responses so if you just pass D- Dev I
know the name is not the best um it will
just reuse um the block number uh of the
previous Discovery and if you look at
the speed difference it's night and day
so uh please use D Dev on uh
any uh call any reruns which are not the
first uh
run um so let's is there a way to do
this
where of logs blocks yeah blogs but uh
by blogs what do you mean oh my RPC yeah
that's that's the problem that I was
referring to are you using Alchemy uh
quick yeah so quick Noe is something
that we don't so we are using quick node
for everything except Discovery because
it has this problem of only 10,000 blogs
um we had uh code uh that managed the
thing that you referring to which is
like we did download by uh thousand
block batches it's just it's really
stupid like we had more time spent on
trying to make it work than just like
paying for a high Alchemy tier and just
like doing whatever so like I said try
to make a free Alchemy account uh you
can put Gavin bellison at gmail or
whatever it'll just it'll be easier I
know that there are also like some
public
rpcs uh that support like infinite block
range for example EnV um
it's so
N.D but they only support logs they're
like really like a static indexer um but
if you look into the readmy of this
discovery you'll be able to set it up
you can put like two ipcs one is for
everything except logs and the second
one is for only
logs Okay so uh let's look uh we have
run uh the discovery so let's look what
it
created um so we have two uh new entries
one is a discover Json file and the
other is a DOT flat
directory uh I'm saying this I think for
like a millionth time I'm going get I'm
I'm going to talk about flat files uh
but let's focus on the Discovery Json
for
now so in this uh file are basically all
the things we have found during
Discovery uh and we just like uh put
every single thing into this file to try
it m to try and make it as redundant as
possible
um if you look through uh the things um
we have of course repeated Zora ethereum
the block number at which we
um have run this discovery uh the config
hash so if the config changes we have
course need to rerun the uh discover
Json um and the contract list so the
contract list is the thing that you're
most interested in but there is also the
an EA list so all of the EAS that we
have found and an ABI list so the list
of all apis uh attached to uh any
implementation that we have
found and use templates I'm going to
talk about templates later um
so each contract is an object it has a
name it has an address it has Source
hashes um not really that useful to talk
about it right now during the workshop
if you want to know approach me later um
since stum stamp it's like when was this
contract deployed um and values values
is the thing that we are after basically
it's the state uh of the contract at a
given block number so the state of it
like do dollar sign something is like a
virtual field we have created it ourself
based on some other values um but
anything else is a state that we have
been able to get just by um calling the
methods provided by this
contract um as you can see there you
know addresses like this and uh some
version stuff whatever whatever uh there
are things that are really useful in
here and stuff that is completely not
useful in here so you'll have to you
know uh go through it and see
uh if anything you would want to use is
here um so um as you can see like
looking at all of this is not that uh
you know Pleasant um so we have also
made um I mean this was like before
anything else um I mean before this uh
thing this is the OG way to view the
Discover Json so
um if I just oh my God like I should
find the guy who made the decision to
make finder like
this okay so we can pull this uh into
the protocol beat Tool uh protocol beat
is the same thing as node View and here
so this View and protocol beat is the
same it's just uh it is easier you can
just drag and drop your discover Json
into here
uh if you want to use protocol beat uh I
didn't think about it but I don't have a
QR code you can just protocol beat.
lb.com
uh and it should just should just work
for you uh you can do all the things
that I showed in the discovery UI
um but yeah let's go get back to um to
here so there are a lot of errors and
what we want to do is get rid of
them and the thing that I was talking
about maybe you remember is the errors
are here because uh of the way that we
build some of the state like I said we
do some assumptions during the initial
Discovery so we made some assumptions
that were faulty um one of the
assumptions was that you know there is
some finite amount of uh elements in an
array turns out maybe it's not an array
maybe the amount of elements is bigger
so if we look so let's try to find this
is finalized in the discovery
Json okay so we we have is finalized and
we can see that there is an error um and
here it is um sanitized because we have
problems committing our API keys to
GitHub um but in the API if we look for
the same thing we can see that we put an
L2 output index and it index and it just
says to us whether this index is a
finaly there is like too many indexes uh
to contain and also it is not that
important um
if we are really interested in what we
much rather see is like the count of
indexes uh that are on this uh project I
mean L2 output uh how many of these are
there but we are not really interested
in any single one so we can just like
tell Discovery Hey listen don't call
this function ignore it um because it's
giving me errors right now so I'm going
to show you how to um tell Discovery
just to ignore uh this method when um
doing Discovery so what we need to do is
we need to find uh the contract on which
this error happened so as it happens in
the error output we get the address
right here so we can copy that address
and get to the config so let's go to the
config and now we need
to um do some configuration per contract
so to do that you need to create a new
key which is called overrides
and now we need to specify that you want
to overwrite some things inside this
contract
um and now we need to say what you want
to uh override so for this contract we
want to say hey ignore methods and we
are going to supply the methods we want
discover Discovery to ignore so just
copy
paste uh and rerun discovery
okay we are down to six
errors um if you want you can try to
ignore more errors yourself
um I'll give you like a minute to see if
you uh got the hang of it I'll leave you
with the config so you have a cheat
sheet
they like andu like that they don't
have yeah so the biggest hurdle we have
is mappings like you say um if um there
is some mapping and there are basically
no Getters for it it is really hard so
we what we usually do is that
if the source code is sensible it'll
basically always emit an event when it
inserts something into that mapping on
or when it overrides it we then build
that the value of that mapping based on
the events so we create for all of the
events and we rebuild the mapping State
based on those events but there is like
no automatic way to do it you have to
look at the source code you see which
events are there and um rebuild it
yourself we have I'm going to talk about
handlers later but we have handlers for
that uh so we can do just that
so while sorry uh while we're waiting um
you have a long list of l2s and you've
said that you expect you know a thousand
or or more that's probably right so how
do you get started with this like how do
you find all the l2s how do you find new
l2s that pop
up um that's a question that is asked
really often I mean and this ston at
least to me um and the
um the answer I think
is way less interesting than it appears
like I think that half of el to be is
just chronically online so we are on
Twitter and we just know what is new um
also projects just come to us and ask uh
to add them also projects just make a PR
to our repository to add an their L2 uh
so right now we have um also we have
public Discord so like there are many
ways to basically message us about like
hey can you review us
um and right now we have around like 100
upcoming projects so anytime this
project will go into uh into the main
net will you know move it from upcoming
to um to the main page but yeah like I
don't think there is any way we don't
have like a discovery for l2s it's just
like seeing what happens in the space
and that's it so how do you prioritize
that how do we prioritize
um if so the thing is that certain uh
projects if a project is an offshoot of
an OP stack it is comically easy for us
to find it it's like less than an hour
um if a project is more
complex so the prioritization always
depends on how big the project is how
easy it is for us to add it and also uh
you know how many times they message us
on telegram per day
uh so yeah the was Center projects for
example I know that ziky link uh Nova
has been in the waiting C for a long
time they had a mainnet and they were
waiting for a really long time because
we just you know we never saw this
project before
so yeah like we have to prioritize
anything else
so the funny thing yeah so the funny
thing is that
certain so I'll tell you that so certain
projects come to our GitHub make a PR
and they have you know their config
jsonc ready they discovered all of this
they made they made the uh config file
in in typescript and I don't think we
had um uh a single instance of an
external team getting this right so I
mean they do try but um maybe it's you
know a fault on our part because we are
not we don't have the best um tutorials
on it because like we didn't expect
anybody to be using it uh and we are
expecting only us to be using it of
course this could change in the future
and we could say like you need to uh
provide a config Json C file but at the
same time
if if they provide a config Jon C file
and it's small like I said it takes less
than an hour for us to do um and if they
provide a config JSC file and it's huge
then we still need to look into it
either way so it's just
yeah okay I hope that for people that
are uh way too ambitious they manage to
do it I'm just going to like flash
things on your screen to go through
it for
okay if your config looks something like
this and you have no errors except the X
domain
messenger uh then good job um
so uh the X domain messenger error is
also a fairy tale to be told I guess
um it's just it doesn't provide anything
useful and we ignore it it revers if you
do a delegate call to it you need to
call the implementation we always do
calls uh through the proxy uh but the
output of it is not useful it like
returns I think some chain ID which we
already know so we just ignore it also
uh for any op
stack
okay so we don't have any errors um and
we can now move on to handlers so uh
handlers are a way to get more State um
like there was this great question about
like how do you
um how do you find the state in the
mappings uh because mappings don't have
a good way to um see what's inside so we
have handlers for a lot of things so
there are handlers like um this is the
uh event count how many times it has
appeared uh and put the number as uh the
state variable um but these are really
complex handlers and I think like it
will only confuse uh most of the people
if I just start uh using handlers that
are way too in depth uh to be honest
some of these are really really complex
just because we try to no cram as much
things into a single Handler as possible
so to be honest some of the handlers I
don't even know what they do
so a simple Handler that I can show is
if we go back to Discovery
Json and you know let's look for example
let's say I'm interest interested in
nosis saves right so
um I find me a nosis safe and I see that
there are members of this nosis safe the
which are the same as
owners and you know I'm just thinking
okay so these are some raw addresses but
the thing is what I'm interested in is
like is a given address an admin right
so let's say there's some actor with a
known address and you just want to know
whether he is an owner or not of course
you could do like contrl f and find it
but there's like an a better way to do
it so um if we look in the API of any um
of any nois save so we you need to to
get the API you need to copy the
implementation
um if you look into the implementation
of any nois safe there is a function
like this is
owner you give it an address and return
returns you whether this address is an
owner or not
so we'll try to see if vitalic is an
owner of some random multis right
so let's copy the name of the function
and let's go back to the config
and um oh maybe yeah we also need the
address of no say we want to do it on um
so first let's get the
address so this is the address we are
going to be checking for is vitalic an
owner maybe this one I don't want to
break my presentation because I know
there is one address which is different
but
okay so we are going to check is V alic
an owner on this uh NOS
save so it's the same as anything else
you just go to the config and you um do
some additional configuration for this
contract so now you need to say that
what you actually want to configure is
the fields part so
Fields um and in the fields you want to
create a new field right so the name of
that field is like
is vitalic and
owner and the value of that field will
be generated by a Handler so to say that
we are saying
Handler the type of the Handler is a
call Handler because we are going to be
calling some function uh to get the
value of
it and there are two additional
arguments which is like what is the
method you want to call
want to call is owner and also we want
to pass in that address uh as an
argument right so we say
args
um and you know now we need to get the
address of italic so let's just go to E
scan copy the address and add it um the
args is an array because you know
functions can take arbitrary amount of
AR args so for this example it's only a
single argument function so if you do it
like this and then rerun
it uh it
should okay maybe that did not work let
me
see okay I guess I didn't uh save the
file um so you saw this little hiccup
that was there like um most of those uh
reruns are like really quick it hiccuped
because it was actually doing that call
it didn't reuse it from uh the cache
because it didn't cash that call because
we never did it before right so now is
vitalic an owner false right so good job
so
now um I'm actually going to get to the
uh flat files uh because it's going to
uh know move us nicely to uh the last
part which are the uh templates so flat
files um I have some slides for
that um
so we have uh built a custom flattener
for the discovery um and I'm just going
to try to convince you maybe I don't to
you know why we need this so we are
working on this L1 standard Bridge
contract and as you can see there are 33
files um which is the result of you know
teams reusing code uh open Zepp link
being the standard Library they are
trying to make the module smaller and
smaller there is a lot of in inheritance
implementation of uh stuff there's just
also one thing I'll talk about which is
you know ballooning the amount of files
in each contract and if you try to
visualize like it's a single contract
like do you know what's happening like
imagine you're a researcher and you're
like expected like yeah good luck
um and the funny thing is that if you
look really closely we are only
interested in basically the blue
contracts and anything else we are not
interested in so if you look on the
right hand side there is super chain
config it doesn't do anything with the
implementation of the super chain config
but the thing is that teams more and
more are basically reusing contract
implementations as if they were
interfaces so when you do that every
single thing that this implementation
uses is now also pulled
in um
and it doesn't have to be this way right
so if super chain config changes their
source code it doesn't it doesn't affect
the bite code generated by the solidity
compiler for the L1 standard bridge in
any way right so if you cut all of this
out if you only leave contract libraries
stuff like that that will affect the um
the bite code produced uh you'll get
something like this right which is way
more uh manageable you have
like eight contracts I think um and um
if you take all of those contracts and
like concatenate them together you have
like one big L1 standard Bridge so this
is the reason uh why when we were
looking at the code we only saw a single
file that's because all of the files
that um we do write out from the
discovery are flattened by default
so um it's really useful because we rely
on those flat files a lot because if you
know that the source code in that file
when changed will affect the bite code
you can just focus on um that source
code and and
um the way we do it is we have uh we are
using
a uh a parser for solidity it parses the
solidity all of the the files uh coming
from E scan uh then we get an ASD we
interpret the ASD to find all of the
contracts starting from the L1 standard
Bridge which uh do actually affect uh
the bite code
so let's look at those uh flat
files they are here and they are um in
folders if um they are behind a proxy so
for example address manager is not
behind a proxy it is
immutable but the L1 standard bridge
that we are focusing on is behind a
proxy so the proxy get proxies get also
uh plen and uh this is the entire uh
thing you would want
so uh what I'm talking why I'm talking
about this is that b if you flatten the
sour code of every single uh contract of
every single project you have you get
some Nifty
uh bonuses basically for free right so
um since I see that we have a lot of
time I'll so show you something that we
have in L2 be and that we use sometimes
um or maybe I'll not be able to show you
that yeah but the initial idea is
that we have built a script uh that will
take all of the flat sources and then
compare the similarity between those
flat sources to each other so then you
get um like a big
um list which tells you okay so this
project has this percentage of
similarity this to this different
Project based on the source code uh let
me just try to see if it maybe will
work
okay if the internet Gods will bless us
we'll get
it unfortunately
so uh if you really want to see this
I'll try to get it working and I can
show you this after the workshop we are
able to basically cluster projects
together based on their source code and
we get automatic uh clustering of um
let's say op stack uh projects and uh it
works really well you actually get like
different clusters for projects which
use um fraud proofs and for projects
which doesn't use use fraud proofs um so
it works exp uh surprisingly
well okay but let's get back to the
workshop so um let's see uh the
conflict so let's see let's say that you
are not you know you're not so certain
about the single no safe and um you
think that maybe they'll try to sneak
vitalic as the owner into some different
uh no save so what do you do if you want
um manage this Handler into two
different um into different no saes so
the first instinct is just to uh copy
this entry and just repeat it just
change the address so let's just do it
okay so we are going to be checking for
metallic in this
um and this not so safe so now in
Discovery Json is vallan
owner is in two places right so it's
here and here right on line 45 and
the amount of things that we have
changed it's only the address so um just
as with code like there's some
duplication right and if some
duplication happens in your source code
what you do is you create some
abstraction that says uh that all of
this functionality or behavior can be
encapsulated to a single function a
single class whatever right so how can
we uh do the same how can we pull out
this configuration call it something
and and reuse this across uh contracts
across components so this is where the
templates uh come in so in Discovery
I'll have to show you this this way so
in Discovery we have uh Discovery here
and if we do uh if we list we only have
Zora but we have to create a
directory
um underscore it's temp it's templates
yeah underscore templates uh in
Discovery and it will just as Discovery
houses all of the projects that we have
uh templates will house all of the
templates that we have uh inside right
so let's create that and let's create
our
template with some something that's
weird is that templates are not files by
themselves there are uh folders um what
why this is the way that it is it will
appear it will you know explain itself
in a
second so I'm just creating in the temp
templates I'm creating a single template
called my
template I mean
the the directory for it so we are
creating this directory for my template
and let's create a new file inside which
is
template.
jsonc and uh we can just as
with um code refactorings we can just
take out in the config the fact the
thing that we need to uh pull out pull
this out into a separate file
and that's it basically all we need to
do right now is say
extends and we say the temp the name of
the
template and we can do it here
also
um if we rerun and check the Discover
Json
it is still in two places right so what
this gives you is a lot of Leverage so
let's say that you know I don't I want
to see if maybe somebody else is also uh
an owner in nosis safe so let's see if
uh a different address is an owner so um
since I don't know any addresses I'm
just going to use donor.
eth
and it's the same thing as
before we are creating new field we are
going to call it is
Dono an
owner and pass in uh the argument and
let's rerun every single
thing okay and now in two places there
is is is vitalic and is Dono right so is
Dono is Dono um as you saw we only had
to change a single file and in the case
where there is only a single project
it's maybe not that useful but like
imagine that we have thousands of L2 and
we want to check something across those
thousands of l2s uh changing only a
single file um instead of all of the
configs for different projects is way
more
useful um and the way that we use this
template is um we um said manually that
okay use this template um and this can
also get pretty boring and let's say how
many noses saves are
here uh there are nine nosis saves
inside of this this Jason so I could
either repeat myself nine
times and um the config or I could you
know allow Discovery to somehow
automatically uh associate this template
with any um contracts that you know look
a certain
way so this look a certain way is where
flat files again come back in 2D picture
so what we can do is like I said like if
we flatten a file and we know that this
uh the code inside that file when
changed will change the bite code and if
we say Okay so the source code of this
thing is something so for example here
we'll be saying the source code of this
is a nosis save so um we can in the my
template this is why it's a uh it's a
folder we can say okay we have some
shape files which essentially means if
anything looks like this shape
um m match that template automatically
so to uh do that let's just go to the
flat files and pick the implementation
the only thing I have to do is uh copy
the implementation and paste it
here and now when I rerun uh the
discovery you can see in the logs
that there are logs about uh certain
nois saves being uh associated with a
template and the reason being by shape
mat so essentially what what has
happened is we have downloaded the
source code for this contract we have
flattened that source code and what we
did is we found that the shape in this
contract uh in this template looks like
the uh source code for this contract so
we have automatically assigned this to
to um this contract and this going to
get pretty powerful this is why I'm
saying that for certain op Stacks like
it's less than an hour so the only thing
that we have to do is just like input a
single address and the Discover adjacent
like the output looks the way that we
want right so if the team did not do
anything fancy did not do anything too
custom it just it just works right so if
we now look into the Discover Json
there are seven instances of uh is
vitalic an owner the reason being like I
said um some teams change the
implementation of certain things just a
little bit and if if it's not even uh
even if it's like a little close we
still don't do it it has to be 100% the
same we also have run into problems
where um the source code is the same but
for example one team uses a certain
Style of indenting or one style of
formatting their comments so we also
have a formatter like a really um maybe
not human friendly but really a computer
friendly formatter that takes uh the
source and formats it into the same
Umi like minified yeah yeah yeah um and
then it can compare ac across uh across
um files
and since this works so well we can also
remove uh these two don't forget
the comma at the end and we
run we also have uh seven
entries um so I see that I'm way uh do
it way too fast like I have still 14
minutes so um like it's basically this
is the end of what I want to show
um I can try to show you some of the
things that we have in L2 beat um that
make
uh
researching uh the things simpler so
maybe let's start with uh going back to
um diagram so we have talked about if
you look on the left side on the inputs
um templates are also inputs to the
Discovery we also have talked about
about FL flat sources um and flat
sources like I said are used uh to
compare project similarity uh we talked
about uh protocol be the only thing that
we didn't talk about is update
monitor so I said that our uh needs uh
are that
to have the ability to react quickly to
changes inside the project and update
monitor does that um like solves this
problem so what update monitor
is maybe I can show
it I hope I don't have anything
embarrassing
embarrassing I don't know do I have an
embarrassing internet or is this is
Discord embarrassing
yay
okay
um
uh this is our update monitor so what
update monitor is uh is a bot or like a
program that takes uh each project
reruns the discovery on it every single
hour and then does a diff on the
Discover adjacent to see if uh any
anything has
changed
um and this way we can get like the
maximum uh amount of time for which the
update can be stale or the data can be
stale for on our website is one hour
um um and you know even here in the
Discord Channel you have
uh quite a good understanding of what
has changed for
example yeah so this is all this is an
amazing example so Molton has done a
upgrade uh of
their Aro to a new version and like we
have uh descriptions and severities to
help us understand
um what has actually changed right
because somebody has um put the time and
effort to understand what is a wasm modu
rout what is an RS from uh okay this is
basically the same but it's like
translated um so somebody has put in the
time and effort to understand all of
and we add like additional descriptions
uh to the um config Json so you can know
uh after the fact what has changed to be
able to understand the change even
quicker um and we do something like this
where uh every single day we have a
um like a summary of all the changes we
need to look at so as you can see for
example this is actually a lot of
changes we need to look at um and
um the way that it connects to our
website is that if um any project has an
implementation change so you can see for
example that Tao is right here and the
waiting que um
and the way that it works if uh a
project has
um an implementation change it's
automatically moved to uh in review on
our website so if you go to L2 beat and
check out Tao it is in
review right here and nobody has moved
it to be in review it was automatically
moved to in review
uh and we want to show to our users that
look this implementation has changed
some of the things that we are saying
might not be correct and we even I think
show to the user um which
implementations have been changed in the
smart contract
section yeah so now you know that the
implementation of these two contracts is
different so now be careful uh either
you can wait for us to take a look at it
or you can just accept the um risk that
comes with it uh and
yeah um so that's update Monitor and uh
I think I'll end it at that unless you
have any
questions um so we were really ambitious
to categorize every single field inside
the Discover Json uh and assign it a
severity right so for
example let's imagine um there is
vitalic an owner right or like we have
that somebody cannot become an owner
because the world will explode or
something like that right uh then we
would assign this field a high severity
so anytime this would change we would
sort this project to be higher because
something with high severity has changed
um as you can see there is also this
fourth column which is nobody has
assigned any severity to it uh and most
of the projects don't have any
severities uh I mean most of the fields
don't have any severities assigned to
them um because it's just a lot of work
um to do
so but
um but yeah does that answer your
question the fields are
Prett
uh yeah yeah yeah
um we associate templates with a given
contract I mean of with a given
implementation of a
contract okay and
um maybe I can show how templates look
in L2 beat um because the all the things
that I showed are not uh maybe amazing
um leave me
alone um okay
so this is the uh can you see it right
here it's good okay so um we have uh the
templates uh that are in L2 be and what
you can do you can uh create U
directories inside the templates and
then try to categorize um each template
for like a given stack so for example we
do associate templates not maybe with
l2s but like the stacks that they use so
we do have an OP stack template like
there are a lot of uh templates so for
example the L1 standard Bridge has its
own uh template right here it looks
like um okay yeah
uh no I mean all of this is like every
single thing um so for example let's go
back to the UI so this is Zora right so
every single thing that we are showing
for Zora is um on my laptop and would be
the same result uh if we were to uh run
it for on the data that we have found in
the workshop session right so we are not
making any additional calls to anywhere
else it's all local
basically oh yeah so there are two tools
I know it's
um maybe confusing so
this is Discovery Y and it has protocol
beat in it uh but to load something into
discovery it shouldn't say Discovery Y
at the top but uh to load
something you just take the Discover
Json and uh drag it on the
website okay any more questions
um so I specifically chose Zed for this
presentation because any single time I
try to share uh my terminal and because
I use Vim uh so it would be just way too
distracting to like try and show you
know uh Workshop stuff um on the
terminal but this is Z with uh V
bindings okay thank you
[Applause]
hi I just want to say
from the OB session that I
I'm back I'm
back back I'm
back I'm back I'm
let
back o
o back back
a
back back back back
o back
back back back o
oh back
W back
what back
sh
let back back
back back back back back
W back back
back back what
back back I'm back
okay okay I think now it's on um so hi
everyone welcome to the workshop it's
going to be um we're going to building a
lot of cool stuff but just for a quick
intro my name is Eda and I'm part of
build Guild which works on tooling and
education in the theory ecosystem and
what I'm going to be showing today is
building an gases NFD minting
application where we go over smart uh
coin basis smart Wallet create like our
app from start so uh hopefully we'll be
going from like no app to like an app uh
in the next one 1 hour and a half or so
and I just want to see even before we
start anyone has worked with scaff E
before okay one two oh awesome okay nice
yeah we have quite a few workshops
during this Devcon uh but that's cool uh
well hopefully this will be a nice intro
um it's not necessary to have worked
with it before we'll be setting it up
from scratch um okay so let's directly
jump to it is
my so this is the workshop which I'll be
following you're welcome to like go to
this URL I'll be doing everything from
scratch so no need to like go there um
but if you would like to like follow
along um e
o4 Devcon 24 I have the instructions
there in case I get stuck I will be
defaulting over
here okay so hi everyone it's nice to
see like a larger crowd especially on a
rainy day I don't know if it's still
raining but it was raining when I was
here cool so I actually did download it
just to make sure that we have it set
before we start the workshop but I want
to show everything from scratch once
again um in case you know anyone wants
to follow along you're welcome to follow
along with your laptops um if it fails
we'll default to the one which I already
downloaded but hopefully the internet is
quite fast so we won't be having that
issue uh okay so for scaffold e a quick
intro you can go over to scaffold eat.io
and this is like your starter page kind
of explaining what the tool is all about
um so the key here is that it gives you
a a fast way to to interact with your
smart contracts and to create a front
end especially if you want to like work
at hackaton and build you know Tools in
a short time uh this gives you a starter
template for anyone new getting started
uh what it is is like it has like an xjs
component which is the front end and
then it has your smart contract piece uh
and you can either choose hard hat or
Foundry so when we set up the wizard you
can choose like your development
environment of choice and um just yeah
let's head over to the docss to give
like a quick intro yeah hard or fanry it
uses wagm VM nextjs uh rainbow kit and
some Daisy UI for outof the boox
front-end development if you're not like
a front end developer you can still like
hit the ground running with using scaf
um I am not so it just provides me a lot
of benefits directly out of the box and
even before getting started I can
actually like go to speedrun
ethereum.org
of scaffold and like building with it uh
what we always recommend is to go to
speedrun ethereum.org
built by the Builders of uh builders
that build guilt and basically it walks
you through different applications to
build on ethereum starting with an nftd
application a staking contract token
vendor so for any developer who is
getting started with ethereum these
challenges are a great way to work on
your smart contract work on your friend
end tool and just to kind of get
building uh quite fast and uh is there
anyone like who's hacking at the
hackaton this weekend okay I think this
might be useful um perfect cool let's
get started so um what I'm going to do
is I'm going to use the MPX crate eth
and then I'm going to follow the wizard
to help my app get started and as I said
I just downloaded before but I'll be
doing everything from scratch in case um
like we have any issues with the
internet which I don't think
so uh I got the command from scaffold e.
I just copy the create latest command
I'm going to set up my app from scratch
and then I'm going to show what the app
offers um my project name let's call
this Bangkok
Devcon uh I'm going to use Foundry but
if your development environment is hard
hot you're welcome to choose that uh I
generally default a
Foundry and it's going to get everything
set up for me and I'll I'll be walking
through it but the main components are
it gives you like an outof the-box
burner wallet so you don't need to like
connect your metamask or any other
wallet uh it just makes your life very
easier especially when you're like
developing and you don't want to like um
connect your metam mask on every
transaction uh it also has like a
built-in faucet so you can directly get
it like it starts your local Devon uh
local development environment so because
we chose Foundry it will directly like
get us like an annual chain um and then
every time like you make changes to your
smart contract you can redeploy them
like you will just run run a uh command
to redeploy your smart contracts and
then it will automatically inject the
changes to your next JS app so like you
will have like a debug uh contracts tab
uh on your front end to kind of work
with it out of the
box just a few more seconds to install
everything and to make sure like I said
everything about scaffold um for any
developer interested in ethereum I think
it's a great place to get started you
can learn more about buildg at build
guild at bg.com as well I say build
Guild but it's actually
ble and you can see like speedrun
ethereum scaffold all the stuff that you
can kind of use for
Education this is almost done so we're
going to get to like the VSS code
soon and once we have it what we're
going to be doing is we'll be adding
like new smart contracts we will be
building an nft application so I'll be
using like an ERC 721 contract uh I'll
be working with that and then uh we're
going to be showcasing the smart wallet
capabilities by having it like uh gas is
minting so you don't need to pay for gas
this way like um hopefully if everything
works out in time and we have enough
time for it to work out uh I'll send the
link and then everyone can like mint
their
nfds uh cool okay so we have this set up
uh let's go into
our let's see what this
is and I want to move this
here let me first run it actually so to
run it I'm going to move a bit fast but
all the information is available in the
docs I'll still try and go like slower
but if anything is missed everything is
already available in docs and the link
that I shared um so I'm going to do a
yarn chain to start my local chain and
as you can see it starts my annual local
chain over here um it's all on Local
Host so no connecting to we'll be
deploying to baseo in the end but right
now we're just working on Local Host um
I'm going to do a yarn deploy because
there's a default smart contract which I
want to deploy directly
and then I just opened like a new tab
and doing like a yarn deploy blah blah
blah okay this deployed I'm going to
open like a new tab and do a yarn start
to start my next JS application on a new
uh Tab and you ALS you always need to
have like yarn chain running because
that's where the contract is deployed
and that's where like your front end is
looking
to okay this will hopefully open
up it always takes a moment longer and
live workshops than working at home but
perfect so this is what we kind of got
set up uh to showcase the features we
have like here the debug contracts tab
which introduces a basic smart contract
um you can kind of test with it you can
set a new greeting this is a burned
wallet so I'm not connected to my
metamask it comes directly out of the
box it's stored on your local storage so
you don't need to worry about connecting
to your metamask there's a built-in
faucet so I can just click it and I'll
get like one
ethon on my well I I clicked it twice so
I got two uh but I can get some eth
because when I want to make a change
like let's set a new greeting hello
Devcon send as you can see I changed the
greeting this is basically a variable in
my smart contract um and yeah I uh my my
balance is lowered because I had to pay
gas for the transaction to go through
and uh this is what comes out of the box
with scaffold the main features
especially like now you have like the
smart contract tab where you can edit
your smart contract
uh you have the burner wallets and then
you have the faucets which I think are
the most useful and as you can see like
I spin up like a full web3 application
in just 10 five minutes I think it would
have been a lot faster if I didn't talk
this much um but this gives a lot of
flexibility to move fast when you want
to build a onchain app okay so what
we're going to be doing today is we want
to add like a new contract we will be
working with an ERC 721 um and for that
I'm going to go to open Zeppelin
contract wizard this is a really great
site by open Zeppelin where you can kind
of craft your smart contracts uh you're
welcome to follow along as well um you
can use this or if you want to use like
soulmate with Foundry you can go to The
Foundry docs and like get a like a smart
contract of your choice as well I'll
just be using the open Zeppelin smart
contracts cuz I think they're sufficient
and um one other thing is I want my nft
to have an image uh for this Workshop I
think I'll be using like the image we
already have so I'm not going to be like
getting a new picture and adding it on
ipfs but instead I'll be using this buff
aorn image which we already have
somewhere
here um
sorry okay let me just add it a bit
later but for now I'm going to be call
calling this nft this is just changing
my smart contract I'll be copying what
the visit says to my application uh
let's call this Eda cuz my name is Eda
uh I'll be adding a base URI in just a
bits I want to make this minable so it
automatically like mints like it
automatically adds that future uh let's
also have autoincrement the ID so then
every nft we add like has a new ID which
is automatically incremented and then
I'm also going to make it in innumerable
which directly allows me to um track
which uh like which own like who has an
uh nft you can also use other tools like
the graph or Ponder for like offchain
doing this uh getting who has which nft
offchain uh but for the sake of this
workshop I'll be using uh the
in my English is limiting but that smart
contract so then we automatically have
like the the people we can keep track of
the people who have the smart
contracts I think this is all we need
I'll be adding the base URI once I get
like the image as well and I just want
to kind of quickly show this I'm going
to copy this to clipboard and then let's
go to our application which I actually
did not show just yet uh so this is the
sca application which we just downloaded
I called it Bangkok Workshop when we
were running the wizard as you guys saw
um am I talking too fast I can
definitely slow down I feel like
sometimes I tend to talk too fast okay
it's good um so we have two packages
over here we have The Foundry and we
have the nextjs uh The Foundry is where
we'll be working with our smart contract
the nextjs is our front end piece so I'm
going to first of all work with the
smart contract piece I'll be adding a
new smart contract and then we'll add
that to our front end in a bit so I go
to The Foundry folder I go under
contracts there's this your contract
dool I'll zoom in a
bit this is the Smart contract which we
were just interacting with uh I want to
add a new smart contract here and I'm
going to add like a new file I'm going
to call this nft do Sol I'm going to
copy paste what I got from The Wizard I
don't want to make it ownable so that
anyone can mint um you like I will just
like omit extra stuff for the sake of
like making it simple uh you can have it
ownable and you probably want like some
owner uh when you deploy the smart
contract to be the owner of that smart
contract you deployed but for this
Workshop I think it's okay to not have
like an initial owner I'm going to
remove this from The Constructor
oops and then I don't want this ownable
and I need to remove the Oni on your
modifier blah blah
blah Okay cool so all I did was I went
to open Zeppelin wizard got an ERC 721
contract and pulled it here uh now I
also need to update my deployment script
the way scaffold it works is you have
the deployment scripts which deploy the
smart contract and they're under I think
scripts okay perfect so to deploy your
smart contract this is what deploys a
smart contract which we just had um what
I'm going what I need to do is I need to
create like a new deployment script for
a new uh contract which I added and I'm
going to take the easy route and I'm
going to copy paste this and I'm going
to call this deploy nft
contract I need to remove the
copy so we do this we change this to
nft deploy helper deploy nft contract
scal deploy let's call this
nft one one mistake which I generally
tend to do is like mismatch with the
renamings so like the contract we named
was called nft over here as you can see
so like sometimes it's called like your
nftd so be careful with when you do the
renamings I feel like that's a common
mistake which I tend to do and we remove
the constructors or actually I think
this is this is
fine we don't need the deployer do we
okay I think this is good now uh this is
not enough because when scaffold it runs
it actually runs this code so we need to
add like a new line over here saying
that also run the script when you run
the deployment script because what we
did was we created like a new deployment
script but we didn't indicate that that
should also be
run and uh thank you to the developers
who actually added it easier like deploy
Mar contracts here so all I'm going to
do is I'm actually going to deploy my uh
I think it's called nft contract right
that's what we J named
it deploy nft contract we probably need
to import this as
well I'll just import this I think oh it
didn't give me my gsub copilot
is it usually gives me the error
perfect okay hopefully this will work
let's see uh as you can see all I did
was I added a new erc721 contract this
is like the nftd contract which you can
make uh you can use directly out of the
box um and I added the deployment script
so that it actually gets run and we can
add
it and hopefully this will work let's
see if it doesn't work it will give us
an error so we'll see what the error is
uh I keep my chain I keep my yarn app
open this is the yarn start
uh I have over here the yarn deploy tab
uh as I said before like the yarn chain
is always open too so I'll just leave
this here so our yarn chain is running
and then our yarn start is also running
but here we will deploy the contract
once again I'm going to do reset just to
reset like anything that was saved and
deployed cool so execution was
successful so let's see what this means
okay so as you saw I didn't change
anything in the front end but now I have
this nft tab so this directly comes
because it's like this is kind of the
main uh reason of using scaffolded um
now I can directly test the smart
contract on my interface over here so
you know it has the NFD the symbol the
total Supply um and this is a basic NFD
contract which we just added and now
it's available for us on the front end
uh I want I do want to add the the image
so I'm just going to go over here I'm
going to oh not
here I'm going to close this I'll go
back to
this okay so this is the image which I'm
going to use for my
NFD uh and I'm going to go back to my
Wizard and where where did we add it we
had our visit over here I'm going to add
it here it's basically just going to add
the base you like the base URI so I'm
going to copy the this once again uh
what I did over here is I want like my
nft to also hold like an image you can
definitely have it uh on ipfs or like a
decentralized server for my case I'm
going to just use the address like where
it's
available and then I'm going to go back
here I'm going to change this back I'm
going to remove the ownable stuff which
we just
did not ownable I'll remove the
Constructor so our Constructor argument
do doesn't take anything the modifier
here now one other thing which I want to
do is I want to limit the number of
times this NF is minted so I want like a
Max Supply uh there is no Max Supply by
default so I'm going to be adding this
uint to 56 public oh wow it already
added it I don't think we need to make
it constant I want to make it like
this I'll make it like 30 30 is good uh
I'm also going to change this to public
uh even if it's private you can actually
access it but I want to access it from
my front end so I'll directly change it
to public so then I can get the next
token ID in my front end as well I added
the ma Supply here so I also need to
update my minting function so that it
doesn't update if it's past the max
Supply so uh we need some kind of way to
make sure that we are not like if if
it's a 31st token it does not um like
mint it
so I'm going to use like oh gsub
co-pilot is helping me I'm going to use
a require statement so if the next token
ID now this is automatically incremented
whenever a new token is Minted as you
can see over here the token ID Plus+ one
so whenever we mint a new nft the token
ID is incremented and if the token ID is
like less than the max Supply we
continue but uh we added a required
statement to make sure that the max
Supply is not
passed cool so whenever you make changes
to your contracts you need to
redeploy nice
okay so we R redeployed our smart
contract now we have a Max supply of 30
like let's test this this person like
this is the pink green person uh this is
a burner wallet so it's not my metamask
um and let's see if like this person can
deploy where where do we add it
mint mint I want to Mint to this
address I'll send this person already
has like some funds in their burner
wallets so they won't be getting a gas
error
hopefully uh okay so we minted an nft
and as you can see the token ID
increased now the token Supply is now we
have one token which is minted and I can
continue to Mint and then it will be two
and then I can open like an incognito
window let's go over here a new wallet
address is generated because it's a
burner wallet and it's my browser's
local storage uh I go over here to the
debug contract toop I copy this address
there's two contracts we already we also
have the your uh your contract which we
didn't change the nft one down down down
copy but it will give me an as gas error
because this person does not have any
money to pay for gas yeah gas required
no available and again the f ET is very
helpful here I just click I get money
from the faucet so now I have one e but
it's on Foundry so my Local
Host save mint okay as you can see the
next token ID is increased so um
whenever you open a new browser you
don't really need like a a wallet over
there but you can test with different
users which makes it quite
easier okay nice so I think we have
quite a a few things already um what I
do I'm going to have a look at my notes
to make sure I'm not missing anything uh
but I think we can slowly move on to the
piece the Buffalo we have this this is
our nfts image the Buffalo icon uh this
is my no not this
one too many
tabs so we we create we set our we set
up our scap application we tested it out
we added a a new nftd smart contract we
added a Max Supply over there uh we did
add it to the contract so this is
probably some like you uh this is just
an example it's not the smart contract
we used so if you do follow this like
read me guide be aware that the the the
code is more like for example so that I
don't give the whole answer but I will
be pushing everything to get up so like
I'll be providing the code in the end we
added a new NFD contract we updated our
deployment script uh now we can start
building our front end awesome so so
let's let's do
that now to update our front end we were
previously in The Foundry folder I'm
going to be going to the next folder to
be working on my front
end um okay so I have the app over
here
um what what I need to do is I need to
create a new folder called nft and then
whenever I go to Local Host host dnft it
will automatically go to this page I'll
also add it to my header so then it's
easier accessed um and shout out to
these people who are the Builders of
scaff actually so thank you for making
the lives
easier new folder NFD uh I want a basic
page.
TSX I'm just going to copy this
and paste this
um in case I went fast just to kind of
reiterate what I did is I went to the
nextjs a Dash app dash like created a
new folder called nft and I added the
TSX over there but we can actually
just remove all this and we can just
say hello b
g and then I don't want to have the
stuff we don't use imported because it
looks
bad I do want to change this to
nft okay hopefully this will work we
actually also don't need this let just
or let's let's leave this
there
um so now when I go to Local
Host I can do a dash
nft hello B so we will be working on
this app over here we'll of course like
be editing it so it will not be this
view uh and one other thing I want to go
even before editing is I want to add it
to my Heather to just make it easier
accessed so then you know you don't like
when you're testing you can just click
the header like home and I think that's
in the the header somewhere here let me
just modify the
header let me
see I can actually search for
debug I'm going to add it here so it's
my header.
TSX I go over here I add like
a new nft tab and let's go to
nft uh hopefully this will work and now
we have like a new tab on our header
called nft which we can directly go to
instead of just like going to Local Host
dnft and let's
see okay perfect as you can see we added
this the nft tab uh and now we'll
actually be building this because this
is not what we want yeah this should
be
um okay so what I want to do is I want
like a basic card which shows a button
which says says mint and I want to
provide the details of my nft so like
imagine a website where you go to Mint
an nft application that's what we're
going to be building and then hopefully
we'll also show what nfts the user owns
and then we'll make it so that one user
can only have one nft and uh that's kind
of the goal we'll be working with the
front end a bit now and for that let me
take this in like this back to have
the so then I kind of used the
default stuff
available or
I'm I will be removing this part but I
just wanted to divs already to make it a
bit easier for
me and let's say hello
here and now what I want to do is I want
to add a card oops it has my automatic
settings uh what I'm going to do is I'm
going to go to Daisy
UI so as I mentioned scaffold uses
dayi uh which are pre-built Tailwind CSS
components so you can click to Daisy y
to kind of see what components you have
out of the box and actually this is I
directly want to go to components can I
click on components here uh so this way
you can directly pull in these
components into your front end so I want
to pull a card
component like there there are different
components such as the you know the
bubble the checkbox the countdown uh
divider stuff like that I'll just be
using a basic card I think I've used
this card so much that I remember the
joke and I never thought it was funny
anyway um so I'll copy
this I added the card all I like I
didn't change anything I just went to
the dayi website I chose the components
I want
uh I copied the card component and I
added it here so for now like no
modification and then we can close this
now nft tab okay we have the day Ur card
which is the shoe card which we are
going to
erase uh I'm going to delete the
figure I'm going to delete the
joke and then what we have okay shoes
buy
now uh I actually don't want want this I
want this to be in the center for
now this will be like a mint button no
functionality just wanted to like
showcase the front end a
bit
um and then what is
this I always feel less creative when I
have like when you're on a live Workshop
or something uh so I'm going to call
nft app
and let's call it Speed Run
ethereum Okay cool so we kind of have
our um maic G but you kind of want to
show the max Supply or like how many
tokens are left right so if you imagine
like an NFD like an application where
you can mint an NFD you come over here
you're like oh I want to Mint but like
what am I minting uh you kind of don't
want that um so I'll be like adding the
details of the smart contract and then
obviously the mint button is just a
placeholder for now it doesn't really
work um but let's let's make this a bit
wider let's make this 96 is this too
wide okay maybe
like Okay cool so uh what I want to do
is I want to pull the details of my
smart contract onto my front end now for
that I'll be using the Scala hooks this
just makes it a lot easier uh to kind of
work with uh it's using wag me in the
back end to use the to create the hooks
uh and you can go over here to
interacting with your smart contract
first we'll show off the read hook and
then we'll also work with the right hook
so that you can actually mint your nft
uh now the read Hook is over here you
can see like we have the default example
uh it goes to the contract your contract
and it gets the function use greting
counter we'll be changing it so we kind
of want the max Supply and the token ID
details for ours and then it our our
function won't be taking any arguments
but you can come over here you can get
the read contract hook let's do that
coming over here just add it here I'm
basically doing copy paste most of the
time whenever I
program uh
import we directly import it uh this is
not going to be total counter but this
is going to be from contract name I
think we named it
nft and we called it Mac
Supply Mac
Supply and it doesn't take in any
arguments so deleting this uh I don't
want to call this tottal counter but
I'll call it Max
Supply and then what should we do let's
added like a header over here
so Supply left Max Supply this is
actually not supply left this is total
Supply but we'll add the total like
Supply left
afterwards uh and then let's also show
the connected address for now I'll
delete that cuz it's already in the app
but I want to show off the the like the
components available in scaff like the
account component which makes it very
easy to have like a like tailored
account component which matches like
your if you have an ens account link it
automatically like makes ens resolution
it shows like your avatar if you have
one so um I do want to show that as well
and let's add like a new header here for
account and first of all before showing
that let's see how it looks without like
the the scaff component so all I did was
uh connected account this is use account
from directly wag me um so very easy to
like get the account details I just call
use account and then I display it over
here and this will not be nice because
it will show like a 0x string which will
be like outside the card
border yes and the total Supply is
actually not shown CU I think we need to
make it like number because it will
result like a b big in which will not be
displayed
okay yes so um but this the the way this
looks is not pretty right like you
wouldn't want to Mint an nft from this
page so I kind of want to make the
account a bit more prettier um and what
I'll do is instead of like having it
like this I want to use the account
components we'll we'll be removing it
afterwards but I think it's nice to
Showcase over here I come to I think I
can search for account component here
recipes
um oh I keep saying account but it's
actually address so I'll be getting the
address component here um account
address uh now what this does is as you
can see you can directly use like the
address component and then add
it and here I
go address I need to import this
okay I think this is taking a
moment co-pilot is slow today I should
get it from scaffold
e directly getting the address
components let's leave the connected
address just to show the
difference okay perfect so as you can
see there are two different ways you can
display the address and I'm directly
using the address component so this
looks like way prettier uh this address
doesn't have like an ens so it doesn't
like resolve uh but if it did did you
would kind of see that over
there and I'll delete the the ugly
one okay cool so we're kind of getting
somewhere uh we still have like over an
hour so we'll get to like the nft
minting part um I'm going to cheat and
look at my notes for the next
step but basically what we have is we
can kind of work towards we we want to
do a a few more things like when we
think about like our nft application we
want to allow gases minting that is one
thing which we want to do uh the other
thing we want to do is we want to keep
track of like um when you log in and
let's say you have an nft you want to
see that right like you want to see like
your nfts part uh so that is the second
thing we want to do and maybe I'm
forgetting something but the rest will
be in our
notes we still have our debug contracts
over here and then we will of course
like ship this app so we'll do like a
yarn verel like YOLO and like host it on
versel so then I'll give like a QR code
so everyone here can mint the nft um
it'll be on Bas of OA so no money needed
and actually a big gas sponsored so you
don't even need to have any money to
like any uh basoa eats to SP like to um
to Mint
it okay I will go back to my
instructions we did this oh we didn't
add the minting function okay okay let's
do that
first I'm going to go over
here I think it's here so uh we added
the read hook which allows us to read
from the smart contract but we should
also add like the right hook which
allows us to
Mint so I go over here as you as you
remember we used like the read contract
hook now I'm going to go to the use
scaffold right
contract um this this docs really makes
my life very easier I can just copy
paste it's pretty simple to understand
um and as you can see like I'll be using
this um I need to add some functionality
to my button and I'll directly be
getting it from here so you basically
need to add the hook to your application
let's do it it's quite similar to the
way we added like the the read
hook we do need to change the contract
details so instead of like your contract
it'll be nft and it's giving us an error
because we didn't like import it
yet um okay so we directly got the right
hook now we can basically add the the
functions to like change the state of
our smart
contract uh I I might be going a bit
fast I think that's what happens when I
talk live but I will be having Q&amp;A in
the end so hopefully will answer
questions and if there are like any
questions feel free to like kind of stop
me on the way as
well and okay so this is called set
greeting which I want to change I'll be
calling this
mint uh the function is I think safe
mint but we'll the it'll give us an
error if it's not I think it's
underscore
savementa
saf mint and it takes in an address okay
so um we can pass in our connected
wallet address over there you can see
the details of the the the function
here value um we we'll make it
free and then I'll just pass the
connected address
here I think we do this and then this
should
work oh do I just do connect
digress okay cool so I think we have
like a a button actually ready to Mint
I'll be making this a bit wider because
I just like it when it looks a bit
wider um and let's see if it actually
mints so how do we understand if it
mints like let's add like nfts left here
instead of like just the total Supply
and to do that I'm going to get the
token ID as
well so this will be not Max Supply but
I think token ID I might be misspelling
it let's double check next token ID
so we'll be oops not here
here this is going to be our token ID so
we get the max Supply but we don't get
the token ID so we don't really know how
many nfds are left so it doesn't really
give us like an good
indication and I kind of want to add
that over
here and then let's also add like a
token ID maybe we can do this e here
um nfts left
and then I just do like a minus
number and then I do the token
ID I'm not sure if this is correct but
we'll
see okay this is correct uh let's see if
it mints right like we added the minting
functionality um but if this person
mints the nfds are decreased
in so I can continue with the mint and
then you know this other person with the
other colors on the wallet can also
mint well this doesn't have any balance
so they won't be able to Mint before
grabbing funds but then we can mint and
then this basically kind of allows us to
um show how many nfds are
left okay this
is we have more time I feel like we will
be finishing before the time finishes as
well but let's make sure I'm not missing
anything and just defaulting to the
notes which I shared to you guys so over
here so we basically added link to our
header we updated our nft we updated the
front end um we actually didn't do this
yet but we'll we'll do it in just a
bit or sorry we we did like I think I
did it before in the previous step
uh now before adding my Holdings I first
want to show the gases transactions
or or we'll do that in a bit later
because to Showcase gases transactions
we need to use base so I want to find
kind of finish everything we do on Local
Host before moving on to like a
development and where we deploy the
contract to Bas aolia and work with the
smart contracts uh so for that I'm going
to be uh first of all like just making
sure like we have we can see the nfts
the person has minted on their page as
well
and to do that I'll be going to this nft
app which I which is already here and uh
we're going to be using a component from
The speedrun ethereum Challenge like the
first challenge where you buildt an nft
up and that actually showcases how you
can keep track of your nfts so we'll be
using the component from there
directly and um what I want to do
is I want
to I will get it from here my Holdings
TSX I'm just going to copy this code um
and let's let's showcase how you can add
like a
component I'll be creating a new file
here I'm moving this part a bit fast
because uh it's not the main part of the
workshop but I think it's good to have
and as I said like whenever you go
through the speed ethereum challenges
you'll see it on the first once you get
familiar with the challenge over there
you'll see that this component is used
and you can create new components for
yourself as well so I'm creating a new
folder components
and then I'll create like a new file
called my holdings.
TSX okay I got
my um the My Holdings code over here
let's showcase how this looks
like I also want to well I need to bring
that component into to here let's add it
just
oh this doesn't actually take an
argument let's see what this looks
like oh this actually directly connected
my smart contract wallet okay so we
directly bought in the component um the
other one directly connected my smart
wallet on coinbase so that's why you
didn't see it but I've been I have too
many browsers open but this was the one
which where we minted the nfts so as you
can see like 0 1 2 3 I can mint more I
will see
them um next we'll also add like a
functionality where any one person can
win one nft because we don't want like
like one person to me all the nfts you
can but not in our apps case uh but I
can continue to Mint this just like
shows it nicer uh I want to add a header
over here to say that these are your
nfts uh so this is my
DOT I'll copy this well I'll delete the
card title but
let's make
this I'm not exactly sure the top we can
use but I'll get it from over here like
let's get this
page let's use H1 actually like this
will be better
let's give some styling to that I'm
going to directly copy from here
I'm just going to add top
margin Okay cool so you can see like
your nfds you can see like mint more so
this kind of displays over here um this
is basically um is kind of almost um
ready there we still have a lot of time
but we will be showcasing how you can
mint gas ly so you don't have to pay gas
or have any money um so okay
let's let's go I think I'm missing
something but hopefully that will come
out once we once we're working in fit
breaks we'll go back and see what's
breaking
um so I have over here the the function
to Mint the nft which I directly got but
I want to sponsor the transactions and
for that I actually went and got
my so let's deploy this app first on
base Saia and then add the smart wallet
piece or let's see
how um I'm going to add a new button
over here it's going to be quite similar
I'm just going to copy this
I'm going to call this gas list Min for
now let's remove what it has inside and
then we'll add it
separately oh okay we removed the
formatting which I actually did not want
remove uh I'll just remove the
functionality the on click
action cool so this when we click this
this will be a gas as mint so then
basically what will happen is you can
click it and then you won't be having to
pay gas because every time we main an
nft as you can see like our balance
decreases so you need to have like some
e in your account already to be able to
Mint the nft itself uh and what I want
to do once again um I remember what I
forgot is basically I want one person to
Mint one nft so then I don't want like a
person coming and like minting 20 of the
same nfts um
because there can be a lot of like AI
agents or something like that and I'm
going to directly go over to the code
which we have over here before um I'm
just going to get that
part this will be by the mapping so what
I need to do is I need to add a mapping
to keep track of all the addresses I
already have uh well all the address
like the addresses who have minted the
nft and then a Boolean as like true
false meaning it does this person
already have an
nft and I'm going to go back to my smart
contract over here I'll add it here
already mented I want the formatting
better so the already mined and we need
to update our saf Min contract to see
like our saf Min function to see if the
contract was already minted and I'll
directly get oh this already gave it to
me so if already minted is false it's
like it's true it's already minted and
what we need to do is we actually need
to set this so once this person is
minted I need to add it like true over
here and I think this is good an
important thing to do is like not to add
this after the save M line because then
like someone can like come in and like
they can create a re-entrancy attack and
then they can always like mint so um
this is important to have it before the
function is
run and I think this is okay
now live workshops are always a
bit scary um cool let's redeploy every
time we change a smart contract we need
to redeploy otherwise it will not be
reflected
uh I'm also redeploying because I want
to make sure that only one person can
mint the nft uh so then now when we have
like a new person we'll test to see that
they can actually only Mint one
nft okay so we redeployed the contract
it's a new contract that's why this
person the the pink green person does
not have an nftd at the moment uh let's
see if we can
mint okay one uh let's see if we can
mint again okay already minted so this
person can only Mint one nft uh let's
see just make sure that I'm not only
saying this but this blue person let's
see if this can
mint so a new person can actually mint
but the same person cannot mint and
instead of already minted like I like to
I want to have like a bit more
please don't siil attack
me okay so if someone tries them in
twice they will get that error uh I'm
just going to get a bit water
cool okay we're actually going a lot
faster than I imagined um took a lot
longer when working on
it so what we can do is um now the
important part probably which what
everyone is also curious to see is how
we can do the gases minting part and um
basically what happens when you mint
again just to re rate is that you pay
for the gas of the transaction but we
want this to be sponsored so we want to
use a pay Master which will be our
application which will be like okay like
no need to pay because this app is
paying for you and for that I am going
to follow my steps over
here we built the front end we updated
the NFD contract now uh only one person
Comm ined one time there is a Max Supply
so you cannot pass the max supply of the
like the the the
count and then now we need to add like
uh the gases transaction piece now for
that we also need to make sure that our
app only uses uh coinbase smart wallet
so we've been using like local uh Local
Host and the burner wallet thus far but
I don't want that because I want to be
showcasing smart wallets and that's
functionality so let's go ahead and
update like our wagm connector to use
the coinbase smart wallet only and I'm
going to go to do that I'm going to copy
this code over
here and then by default even before
showing that I can show you what happens
by default I'll disconnect cuz I think
is my application
oops oh I think because it has a burner
wallet it directly connects to my burner
wallets I say disconnect but I can kind
of choose the different options so you
can see like there's like all the
different options you can choose from
but I only want it so that that my app
uses coinbase smart wallets and for that
I'm going to go somewhere here I'm not
exactly sure but to my next JS to the
wag me
connectors that is under not
here the wag me
connectors is it this no sorry I I think
it's here okay cool so wagm connectors.
TSX and then what we want to do is we
only want the coinbase wallet as you can
see like it Imports all the wallets we
don't want that and uh we just want the
coinbase one so I'm going to delete all
of them besides the coinbase one and
I'll I'll just like basically post what
I
copied so the wallets will only be the
coinbase wallet I delete this and then
the pr yeah preference is the wallet's
only I think this is fine to leave
I don't want to have extra Imports which
we're not
using I think we can remove this so we
we we will no longer have the burner
wallets because we want to test with the
smart wallets it's going to be a bit
like you will actually be testing with
the smart wallet so um not as easy um
it's still easy
but okay so hopefully this will only be
the smart wallet I actually think we
were just discussing this morning it
will show the other options too but
that's on rainbow
kit okay we need to connect our
wallet yeah so it does show the other
wallets and I'm not exactly sure why but
for now we can continue with the smart
wallets I choose coinbase I think I
already have a smart wallet set so I
approve
this perfect I think I need to change
the switch to found oh I don't I'm not
sure if I can switch to found but
basically like now I want to make it so
that my app is only on seia and let's
also deploy this smart contract to seol
um to Showcase
that so A few things I need to do do
here I've been running yarn deploy since
the beginning of the workshop and that's
only deploying on my Local Host so I
didn't need to like worry about my
account or whatever is going on there um
and you can always default to the scaff
docs to see how like you can get the Run
deployment scripts as well I'll just
search for
deploy uh
so what you need to do is you need to
run yarn generate to create an account
for you I already did that so what I'll
run is yarn account to show the account
which I already have so as you can see
this is the Account Details uh this
creates like a m file which has the
details of it and then you can see like
my balance I actually have quite a bit
of balance on different
networks and what I want to do is I want
did I do it wrong need
to oh yes I need to update the REM me
file it's good to have you guys in the
front so I think I used the custom the
default hook I need to use the custom
one so then it
doesn't uh I'm not exactly sure where I
think like this
okay and The Foundry
folder okay so I needed to change my e
key store to use the custom one and uh
we did that so we can R run it again um
so when I do a yarn
account it asks for my password I
already said it before you set it when
you create when you run yarn account the
first time so that's why I'm not setting
it again um it's stored with a password
so that makes it easier but I should
have some balance which will allow us to
deploy the smart contract uh you can see
My Account
Details base
aolia I just am waiting for base aolia
to appear and then we'll run the command
Okay cool so we have some balance on
baseo I have not deployed my contract
yet so this time we will actually run
yarn deploy D-
network network
base sapoia and hopefully this will
deploy the app if everything goes
well it's pretty fast and cheap to
deploy to Bas well Bas deoy is already
like cheap I mean Priceless but
I entered my password
again cool so our contract is getting
deployed nice so one other thing I want
to change is uh my scaffold Le
application is pointing to Local Host I
want to make sure that it points to like
base aolia because as we were working
before it gets the contract details from
The Local Host which where files are
generated but now I wanted to like put
point to base
and I'll do this by I Local Host I
think I'll just check the over here as
well it's in my next JS
up I think it's in my next config
no
oh not
here I'll just close this
Foundry and then I
will so the tar the tar networks over
here is change.
Foundry uh if you had
chosen hard hat it would have said hard
hat but because we chose Foundry it says
Foundry and then I'll just delete this
and it automatically gives me like
little base SEO yeah so this is my scal
of e application configuration which now
points to Bas apoia I'll also lower this
because base block times are lower so
enough so then our app updates much
quicker than waiting for like 30,000
seconds it can update in
okay nice let's see what we have it
doesn't it didn't change much um we'll
create this like a con so that it
doesn't show na afterwards like We'll
add it as a states to our application
but for now this should be
okay so I'm going to connect wallets
okay it asks me for my coinbase
wallet
approve now my wallet is connecting I
think this is doing like ens resolution
which maybe need to change but uh I
actually don't need the address here I
can mint over here but I'm on the switch
to Bas all y' this uh this person
doesn't have any money so they can't
mint but the good thing will be is we
don't have like for now it won't be able
to Mint because this person doesn't have
actually base does base already offers
uh sponsorship but we're going to do it
ourselves so then you can also see how
you can do it in Europe but uh because
like Bas already covers the payments
like if it's less than a certain amount
I don't remember how that what that
threshold was but if it's under a
certain amount base does cover the
network fees so they already have like
as you can see supported by base but
when we cover it it'll actually be say
like exported by scaffold e app so
that's kind of what we want to do um we
can say confirm to see like if this
actually
works cool so this was actually paid by
base um but we want ourselves to pay for
it but this was pretty cool I actually
didn't realize that we could showcase
like basis pay Master as
well but I want to showcase how we can
pay like add it as well uh now I'll
directly copy the code which I have from
before now I know I'm going fast a bit
as I mentioned but all the instructions
are available in the the read me so you
can totally like follow along I have
some extra links over there so you can
kind of check to see where the details
are coming from but this this read me
over here should be like a nice guide
for you to like look for or if you have
any questions about anything we're going
on in the workshop um so hopefully that
will be like a nice resource and we
might have some quite time for Q&amp;A
afterwards
too um
okay I want to make gases nfts uh I'm
basically done with everything I did
with my contract side so we can just
close The Foundry folder and let it
be um I'm going to go to my app I'm
going to go to my nft I'm going to go to
my page.
TSX and I'm going to add like a
new button here I'm going to copy the
code which I
had and
then I will remove this gas
Min nft is left nothing changed here the
mint button so I added a new button now
what we do what we need to do is we need
to get our pay Master URL from
coinbase's coinbase developer portal
um I can showcase
that coinbase
CDP you need to create an account over
here and uh it gives you like different
tools to use I think I already have an
account so that should be fine hopefully
this will log me in uh but the coinbase
developer portal offers you like
different tools such as like how you can
use the onchain tools the pay master and
like the faucet Etc so I'll be using the
pay Master URL so then I can
automatically that covered the cost it's
it's they actually also pay for the
first um like I think for the $100 or
like $500 so that's pretty
cool I go to the pay Master onchain
tools I go to the configuration tab it
will expose my API key but I will Reed
like I will make
it like redeploy it afterwards so I go
over here I'm on base seio so I need
like a pay Master endpoint to make sure
that my uh costs are covered by
coinbase right async did I forget
something so first things I'm going to
do is I need to add this as an
environmental variable I can actually
add it like as you can see this directly
goes from uh the public pay Master URL
so let's add this over here we can add
it to ourm file we have I'm just going
to copy this command
copy M I'll create like
a and then I'll go get my API
key so this should be okay and then we
don't need this
anymore right contract
asnc uh so I do need the right contract
as and let's get that from scaf Le I
think we're missing the
Imports
oh oh from wag me
okay I remember so uh you can go to wag
me and I will actually show the
documentation as well
so this is under the experimental
tab um and I will
import do I can I import it from here
and I guess I need to like pull the
right contract A6 from here
I'll delete the
notification just going to copy from my
code as well I think I'm missing
something but we can quickly cheat from
the code I have before
so I basically close the coinbase
developer portal we don't need that
anymore and then I go over here to my
I'll just go back to gab I think I close
that tab to just make sure that I have
the right code over
here I think I'm missing something but
I'm not exactly sure
I'm going to go to my app to my
nft my page.
TSX and then I have the right contract
async oh I didn't get my used deployed
info okay so basically you do you can
use the scaff hook to get the use uh
like the deployed contract information
which is going to be like your nft like
your contract address and API
information and I need to import this
this will give me where to import it
from I think we're
good I don't think there's a mistake but
if so we'll see
I go over here to my nft tab wrong
Network let's switch to base but which
wallet is this let's just disconnect to
make sure we have the right one I
connect my coinbase
wallet okay cool I need to do like a gas
as mint hopefully this should work
Okay Okay cool so this does work no need
to panic um so as you can see what we
did was we got our pay Master URL from
coin bases and you can uh I forget which
um which ERC it's defined it's 5774
I think but I have it the details over
here uh Devcon
transactions and gas sponsorship and
then the 7677 which shows it on your
user interface when you go to the
coinbase wallet and it directly says you
know sponsored by scal or sponsored by
coinbase um so this is pretty cool now
everyone who has this app can actually
use it and mint an
nft and it is sponsored when you click
mint it's sponsored by base but when you
click gases mint it's sponsored by S
that's actually just hellow like that
it's sponsored by
us um and I'll remove the gas mint
function like let let's actually try
that it's actually
minted cool so we can basically like
mint and nft we can have it here um and
you can do it like when you click mint
it's actually sponsored by coinbase um
which is cool as well oh okay maybe they
all oh so we got the message because
already minted please don't siil attack
me but another like if we open like
another Tab and a new wallet it should
be able to work um so that's when
coinbase is sponsored let's delete this
mint Tab and then let's make it only our
app is sponsored and then let's actually
ship this app to versel so that you guys
can access it and mint the Buffalo for
free I'm going to delete this we don't
need this
anymore I don't like to have Imports
that I don't
use I think this is
fine let's delete
this I think we're good so just to
reiterate like all the we did was we
created a new smart contract ERC 721
smart contract and then we deployed it
to base we added like some extra
functions we used the open Zeppelin um
wizard to kind of follow along but as I
said you don't need to like create the
index and the people tracking over there
but you can use like the graph or Ponder
for um getting that information off
chain as well like easier without like
having your smart contracts there and
then we had like we added like um the
coinbase pay Master URL to sponsor
transactions we had some stressful
moments there but it was solved so um I
think this is good all we need to do is
we need to ship our app to verell so
then I can give the the link to access
but this is basically completed so
far and to do that we actually have just
one simple command yarn verell
YOLO uh I think this is fine
uh I already have my uh versel account
linked but if you don't I think it
actually asks for you to like link your
versal account first I'm going to do no
and I want like a new project let's call
um Buffalo or let's let's let's call
like
Speed Run
ethereum
nft yes
I want the default settings uh now one
thing is I do actually need to add my uh
pay Master URL to my versell account so
we will do that in just a bit but
besides that it's pretty okay I can
actually follow this
link uh I'm going to go to my Brave
browser where's my Brave
uh I'm going to go to my project I think
on my so this is building this takes a
while well not a while but like a few
minutes and I need to add my uhv file
details over here somewhere here okay
somewhere here sorry environmental
variables blah blah blah and we add them
here so it's actually pretty cool you
can just copy paste from from my code
let's go
let's go let's copy this we can directly
add this we can directly add this here
this will
save okay nice so this should be added
we do need to redeploy your
application I think I can go over here
and like
redeploy oops Speed on ethereum
I'm redeploying because I added like a
new environmental variable so uh it kind
of takes that in otherwise it wasn't
going to use my uh because it doesn't
push the EMV file uh it won't like know
which process vir able to look at and uh
this takes like just a few minutes and
then afterwards hopefully you guys will
all have access to the link and um you
can try it out
any questions like maybe we can like
answer oh the deployment is successful
or yeah if anyone has any questions like
happy to answer any questions you guys
might have while this is deploying for a
moment
hopefully it will deploy fast I feel
like pauses are
awkward and uh just to mention once more
time where when you go to the scaffold
talks all this information is available
over there like how you can do like a
versal YOLO a versal deploy um
or you know anything all all the things
we went through are actually available
here um we added our own smart contract
but you can also like interact with
already existing smart contracts and
find the details here it's quite easy to
pull it in your app I guess the biggest
feature is that you can kind of iterate
quite fast you can like PST smart
contracts make changes to your app like
we built like a whole NF gas NFD minting
application in like an hour or
so and we deploy the contracts we even
like have a live URL in just a
moment once this is
built and um what else am I forgetting
something I think we did talk about a
lot of the things I can show
speedrunning theorum one more time so um
we the
the uh to get the components which shows
like who has the nfts already we
basically use the simple nft example
component there so I know I went through
that really fast and I just copy pasted
it but when you go to the simple nft
example it will show you the details of
that component so you can kind of
understand how to build your own
components such you know such as the the
small card which shows like the nft and
then you can basically follow through
you can create like a decentralized
taking app a token vendor dice game um
join the build Guild and other
challenges as well and then to follow
more about what's up in build Guild you
can also go to B gle.com to kind of see
the stuff we work on um and you'll have
over here scaffold e you can start using
start building um this kind of gives you
all the information you need we have um
an extensions feature as well and Hunter
the creator of the video is also here um
so basically extensions allow you to add
new features without modifying the
existing
code uh it's funny to see yes your face
here as well but um basically you can
kind of follow along to see how to
create extensions um and what I mean by
extensions is let's say you want to
extend your scaffold app like add a new
smart contract right like we added like
the erc721 contract and then you can
kind of be like you know I want to make
it easy for anyone to create like a
scaffold app with the ERC 721 contract
so that's kind of what the extensions
allow and this video teaches you how to
do that uh very simply so highly
recommend it and you can learn more
about
extensions you can create available
extensions so there are like some which
are available out of the box such as
like the subgraph uh the onchain kit one
the oh ERC 712 is also available here um
but 721 is not so maybe we can create an
extension
afterwards not live that would be a bit
too
stressful but I hope verel has deployed
oops Rell has not
deployed but um
I have like yeah I have like a something
error on my page with extra quotes but
I'm not sure where I have that
error yes because YOLO shouldn't scream
for the linting errors right
oh okay so I got it um these are like
warnings which I should do it again
which will redeploy because YOLO is like
not checking for like linting
errors but now this means we have like
an extra
minute so but yeah hope the the the
reason was I think I have like some
wrong quotes or something with which was
creating like a linting error which
blocked me from like deploying to verel
um and yes I I think it's okay to have
it for now uh that's something you can
fix
afterwards I would have known the
a true uh just yeah in case it didn't go
through like the video but that's a good
point like you can do like a uh yarn
like yarn versel build or is it yarn
next
build yeah let's look at that since we
have a few more moments we can do that
but that's a good point thanks for
mentioning
that I think it's okay I'll just go to
my
so you can run like a build command
directly to make sure that you know it
um it doesn't have any
errors and then this will directly give
you the errors so before you push them
you can fix
them and it tells you all the scripts
like like when we run like yarn start
Etc this is kind of the commands that I
run but I didn't do that so I didn't
really realized I had a error before but
that's like a good feature to well best
practice to do
before uh but now this is actually
deploying to a new link right like the
disc create like a new application let's
see inspect not that
one so I might need to actually add our
pay Master URL or is this creating the
same one
okay I think this worked
but but we didn't add
the let's see we'll see and try if it I
I I think we it created like a new app
so we should add like the pay Master URL
here as well oh it directly created the
same one okay so it directly used our
environment variables already available
in that case oops not here let's just
follow
the or I want to use this link actually
this I'm going to connect to coinbase
wallets
we're going to do gas
assment going to
work so not going to work Mak
expensive okay as you can see sponsored
by scaffold e that's mint unknown nft
you probably don't unknown
stuff okay nice so all of you guys can
actually go to the URL here and I think
I have like a better share right if
I the what the
project I'm not sure where I think the
URL
is but where does it show that
one the
settings okay so I go to the nft C so
everyone can actually go to this domain
and like mint and nft um it's speed and
ethereum line line uh Dash or line nf.
verel
DOA nft uh we should have actually
removed like the home page and the debug
contracts before we did a deployments
but we did do versel YOLO so we didn't
really check those stuff um so yeah like
this is kind of the gist of the workshop
happy to answer any questions you have
um before doing the verel deployment it
is very important to run like a yarn
like a build yarn build I think um so
then you can check the errors before you
deploy but our error was like a small
like linting error so it didn't really
matter like it didn't it was a warning
um and um yeah this is happy to answer
any questions anyone has but we're 25
minutes
early I think it's okay to be early
and you can send questions through here
I think right that's
the the
thing hey um can you go through the my
Holdings component how do you fetch the
nfts for each
user yes can we connect again
so what I did there is that's a good
point because I moved through it really
fast but uh we have over here the app
components my Holdings so this should
this um this uses like
the innumerable right like when we were
using the when we were deploying the
contract we also make sure that we can
have like tracking the IDS of who was
the account that was minted it we have
like a mapping over here on our NFD
smart contract and I can show that as
well but uh we added we made it
inumerable and then we have like a
mapping to kind of keep well the mapping
is actually not how we track it but uh
that's kind of the functions we get out
of the box to allow it okay does that
make sense yeah um just wondering if we
had like uh let's say 10,000 nfts or
through all of them checking which one
is the
owner there the for Loop so yes right
like that would create so that's why you
probably want to use like uh honder or
like the graph or something like that uh
this was an easy way to do it at the
workshop um You probably don't want to
have those smart contracts it's just
extra workload for your smart contracts
uh but it does make it easier for like
smaller projects or like for workshops
but yeah you probably want to use like
Ponder or
graphql okay thank you actually the the
there's an extension for both of them so
you can directly use the extensions to
create like your app out of the box with
those features so you know we mentioned
about the extensions and um how you can
use them so the available extensions are
like you both have the subgraph
extension so then that way like it just
indexes this uh so with subgraph it uses
like onchain indexing with Ponder like
it's offchain which kind of makes it
really faster uh so you can kind of do
that okay cool well if you have any
questions we're here and thank you than
you to um to everyone at Bild Guild
especially Shi for like helping out
super much with the application I'm more
representing us both here so um yeah if
you have any questions about scaffold
about Bild Guild happy to answer we do
have like most the developers here so um
I hope that they can provide any other
like Ultra Deep dive technical questions
um but yeah I guess this is kind of the
end of my if there are no more questions
like we are done
back I'm
back I'm back I'm back
B
t
see
h
to oh
bu
up
m
o oh
w oh
