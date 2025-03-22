[Music]
w
back
back back
e
back back back
he
oh back
good morning everybody um I'm Stefan
kbut I'm the founder um of sterium and
Ro logic and we will do a workshop
together to set up an ethereum node with
different kinds of
services um first of all some facts
about about us uh Rog logic was found in
company but an IT infrastructure company
devops company
um we develop steum since
proof of stake of um steum happened we
started with the development we are
institutional node operator so we use
theum also for our um own
operations which include um light which
include the uh staking efforts in
Lio uh we already performed couple of uh
security audits for theerum to ensure
that everything is running fine and we
don't oversee um some Overlook some
major uh security
vulnerabilities we also won um some
awards I guess the most recognizing at
least in Austria is the Austrian
blockchain award
separate company for this great
product um and also this year we
launched a steum plus which which is an
addition to steum a hosting service that
you don't need to care anymore about
where you uh get your own um machine for
sterium so some use cases for steum
itself steum is open source everybody
can look at the source of course and
everybody can use it in whatever way
they want to it's MIT licensed it means
you can also Fork it Rebrand it whatever
you like to do with with the source code
it's up to you um some use cases of of
course are staking we as mentioned um
use it uh for ourselves for our own
operations with Lio and other protocols
there are also protocol node
operations uh for Obel and SSV so it's
very easy with stereum to set up a Lio
CSM um operator as well as obal or SSV
operators then it's also possible that
you run your own clusters with Obel and
SSV in case you don't know Obel and SSV
are dvts distributed validator
technologies that help you spread one
key one validator key over multiple
servers um to ensure more reliability
more resilience to technical issues or
other issues that you might face of
course you can also use theum um as an
RPC
node um maybe some of you guys already
um use infura or some other RPC provider
and you know that you're limited with
them but with your own node you're
basically just limited by the hardware
you're um putting stereum onto we have
users that run Arbitrage bots on it we
have users that um connect their
metamask on it um that's pretty easy and
will be explained also later um of
course you can um start developing your
own decentralized app with theum because
you have the full range of RPC uh
requests that you can use as well of
course as
websocket um and of course um steum runs
everything you want to you're not
limited to the stuff that we provide you
you can also um come up with custom uh
services that you integrate pretty
easily that will be also explained a
little bit later
on as you may know ethereum has multiple
clients first of all we have EX Fusion
clients and and consensus
clients um both clients are needed to
ensure that you can run a full node or
an archive
node we support um most of the most of
the recent clients most of the major
clients we also look always into some um
smaller clients but um up until right
now they were a little bit too unstable
to integrate and we want to make sure
that the user has a seamless EXP
experience um in running an ethereum
node so how do you run an ethereum node
first of all you can run it on cloud or
um on your home PC or um your office
computer wherever you want um of course
with Cloud you have AWS gcp hna um and
our new product serum plus of course
which makes it very easy um to to use
with sterium with arm it's a little bit
complicated you could run a full node
with Raspberry Pi 4 but it's a little
bit slow so I would not recommend it if
you want to use Arm I would really
recommend the orok P 5B or the orange
pi5 it's a much smoother experience
especially on Main
net with x86 machines generally just
choose um a CPU with a benchmark over
a lot but if there are um uh some
network issues then you will be happy to
have some some more CPU power to to
actually um deal with these issues 60 G
gabt of memory are in my opinion a must
to run on Main net everything below that
it's it's already a pain uh 2 terab SSD
um I want to emphasize SSD
here um old hdds they don't work well
with with with nodes also not with um
full nodes like um and especially not
with archive notes two terab might be a
little bit on the short side uh for the
long run as well as um to less for some
of the clients we know that some clients
don't prune very well like um delete all
old data that they don't need
anymore
um we we would if if you want to be like
future proof then go for three or four
terabytes that's that's way better but
two terabyte should at least give you a
a head start and and make sure
everything runs smoothly in the
beginning ah sorry wrong
Buton okay then thank you very much um
welcome to
David thank you very much I'm take your
thank you thank you
stepanie okay um as this is a beginnner
workshop um we now want to go into um
the whole staking process we want to
walk you step by step through it because
we have enough time and um yeah so the
next point is taken with steum
setup so there are four four overall
steps you have to do for um to to stake
yourself first of all um yeah you uh you
have to have 32 e but that you already
know maybe that will change in the
future but at the moment it's 32 then
you have to create your validator keys
um with a seat Trace um we will show you
this today with um a tool called Vue um
then you should um do your validator
setup so a full node run with a
validator that you can do with steum but
there are other tools as well then and
then afterwards if you have a running
setup you should um load up a validator
key with the 32 e and of course always
should start with um test net um if
you're new to the stuff and the fourth
step is then afterwards enjoy the
journey
okay so um I
try to um emphasize the whole process
again um in a in a picture
so you create here the key
then after you have a running setup then
you um in this uh in the key you um uh
do uh you give there the withdrawal
address um where the where the 42e view
um will be sent back and where the um
attestation rewards and the syn ComEd
rewards will also be sent in which
wallet um so it's kind of safe after um
you load it up with the 32 e because if
you ever um exit your validator key it
will only go to uh that wallet so um
yeah you're safe afterwards
then um then you um um yeah after after
that process after you up the key um you
have some time to be um um after you
deposited the 32 e you have some time to
be approved um on mayet that's I think
um around 7 days and in the meantime um
you can start the validator client and
um uh set the fee recipient address so
that's another um uh possibility to earn
rewards and there you get the on and and
the fee recipient is a wallet where you
can get the block production
rewards okay so how now um to create a
validator key you might be
interested um there are different tools
we will use today
vagu and maybe um yeah um as I will show
you you shouldn't do it because you
should do it on an extra machine uh best
set up only for creating a key with no
internet connection whatsoever um but uh
for today um um as we do it only for
test we will we will I will show you on
that so um Vu is an open source tool I
think you can easily
find um as I said um if you're a
beginner you should um use a test nut
for staking holes is really Pleasant to
use and then first of all you need to
create a new recovery
phase and and as you see the tool um
already wants me that the internet is
connected so you you should really have
emphasize on
that so you see it's it's really easy to
do just create a secret recovery phas
and then um like every C Trace you
should write it down um put it um in
steel so that you can't lose it and
never ever share it to with anyone
except two
I
okay takes up to 30 seconds or
longer
yeah okay yeah could be oh
yeah that's hacker tools they're only
always dark mode
so but maybe that's also securing the
the seat race
some okay
um after you have written it down you
have also here the the option to copy it
into a file as I said I wouldn't I
wouldn't store it on any um digital
device I would really craft it in paper
or in
steel but I will copy it now for the
ease of the
process thank you thank you everybody um
yeah I
am I I I wouldn't now go back because
then we have to do a next se phas but I
think from now on we're good okay so
then you go
next um it really asks you again if you
if you ped it up I'm
sure that I'm lying no um and um then
you have to confirm that you have this
um secret recovery phase so it makes so
this tool is
really now you can check
it and you can use your um seat phrase
um for generating more than one key and
what the cool thing is you can also
generate it to generate further key if
you're in need on a later time so just
um remember the seat phrase put it in
here again and um then you you can
already you can say how much Keys you
already um created and the number of key
new keys you um you have yeah
it's so I set the password
and in ifer withdrawal
address you might want to take your own
one perfect already some hesky Eve here
okay take a password that is longer than
eight
characters and remember it better write
it maybe also
down so and then you're done just have
to say where to put um the files I
will um
yeah it
there and create
them and I should have created an
on fold
up okay that that
might take some
time and in the
meantime yeah we we done the
setup you can also see it in the slides
the Q code is shared I think
afterwards um so there is the whole
tutorial
again and we're done with creating the
validator key so the next thing is to
doing the setup the validator
setup okay
ah yes
here no yes so I'm
done um yeah you you get um two two
files the the one is the deposit file um
you will you will use to um um to to
load up the validator key I will show
you our I walk you through the process
as well as there
um um yeah um I walk you there um there
um we will use Launchpad for that uh
later
on okay lights are and now we are now we
are starting um to to use theum and
making our not setup so what you need is
um you need a um yunto server machine um
that that runs on um on on the new yunto
version stable version um you might also
use other um Linux distributions um but
it's not tested so um we can't guarantee
you
anything um so yeah then just give into
the
credentials
and if you if you give um the
credentials the first time there's this
option to save it with the plus
sign and and
connect and of course first load down
the steum launcher which you can find on
website or in the
GitHub so let's
see okay and now you can see how really
really easy it is to um set up a a steum
node um we because we have this oneclick
installation but of course if you want
to do something more um fancier or
expert you can do your custom
installation or even um you can export a
configuration um after you have set up
an eum note with stereum and then import
it there so can but we will go up for
the beginner session today with the one
click
installation okay um we have uh then you
the first step is to select the network
we support of course if few main net and
both test Nets the polion and
heski and um we also support kosis mayet
so you might want to um start um start
start staking with koses so it's it also
a good feeling and works exactly the
same or very similar so we are starting
with a hes test net
today and now you have um different
options um you just can set it up for as
a staking note um that's the vanilla
staking setup everybody is talking if we
are talking about staking um there's
also the opt to um do a MF boosted
version so you have um a client
installed that help helps you to connect
to relays that um will help you to um
math boost so that's maximum extractable
value so um the block building um is
done by relays and you get a little bit
more of rewards because you're an a own
whole entity is a little bit faster than
probably what how you set up the um the
the the block
yourself then uh we already um talked
and if you afterwards have question to
it um um we can show you um um a DVT
setup so that's where the key is split
into four parts or more than four parts
and every um entity um is uh is taking
and uh thinking and agreeing on uh on on
on on their work and and then it's um
and then it is uh deployed to the
network so it's it's kind of safe and uh
not every uh part of then not every no
and this um have to be up all the time
so they are a little bit um risk- freeer
and and not so reliant on the on on the
up
time yeah we we we we have an own setup
for steum on arm as we said um for for
Raspberry Pi or a little bit better
machines um it's it's a little bit of an
experimental stuff but um try it if you
if you want to it it worked quite well
then you have the archive node um so um
fully set up and then we support
protocols um like the Lio DVT um
protocol where you can do note
operations for Lio um um emphasizing the
um the DVT protocol so you get one share
of um of a key and do note operation and
securing the and and and do staking for
for Lio and what's quite new and
starting an early adoption phase on Main
it is the CSM the community staking
module where uh there is some some kind
of bond um you um yeah you just have to
um add a bond and uh create the keys and
uh Li will load your will load your K
with 32 e and then
you and uh and then you'll get uh part
of the um of the Rewards or shares of
the rewards which is
quite quite good yeah so I will take now
the vanilla
staking um it's always possible to add
um yeah stuff in the expert mode so we
can show you afterwards if you if you
want uh to go from staking to M boosted
for example um we I will show you in
afterwards so and uh after you made your
decisions your almost set
completely um what you now as we before
said um we are client ofers so their the
setup is chosen randomly um I mean yeah
it chose randomly GF which which which
you shouldn't use because I mean it's
running good but it's um at the mainly
adopted um client and um yeah for
decentralized reasons um we should take
something else so you just click on it
it and choose something else for example
basil um and you can do the same thing
for the consensus clim so yeah instead
of prism I
can use load
star and the validated client is set as
well normally you um you set up your uh
ethereum taking note um with consensus
and validate a client um from the the
same um de
ER yeah and there are other um Services
um installed as well that um yeah
visualize what is happening in your node
so and after
you you you click next um you only have
to um uh uh choose a a checkpoint sync
which is um we have pre-selected um
sources that we know work quite well but
you're also able to um yeah um sync with
your own checkpoint if you want to so
you can use a custom
source and yeah that's only an overview
where the things are stored or installed
and
then you can press
next okay in the meanwhile while
everything is setting up what would you
what you will see in a a moment I will
shortly um tell you a little bit about
launchpads so if you are if you have
created your validator key and if you
have your setup ready then you want to
load up your validator uh key with 32 e
and um for beginners we would um we
would uh recommend you the to use it
from the the if you the launch pad from
foundation and um there's a really
really easy setup you have to choose um
which wishnet in
the in the first place so I'm I'm using
heski and then it will really walk you
to everything it makes a lot of um it
explains everything again um it makes a
lot of checks if everything is set up
correctly it warns you I think it's very
nice way just to
uh to memorize every everything again
and uh and and deep dive into staking
again but I you might as well click
through it but it's really yeah I would
recommend you to read a little bit into
it um it also tells you about the risks
the early adopter risks Etc there's
checklist involved so there's really
some cool stuff and then in the end you
confirm um yeah yeah and then you can
choose your even your execution client
we set up
basil
and get the con
documentation then we took consensus
client load
store yeah right it's it's kind of it's
a kind of optional um
um what you choose there then the number
of value
daters then you set the withdrawal
address we already talked to should be
the same as in your key
files yeah what's your curent operating
system yeah and then download keyan GUI
app we already used so it's also
recommended from the theum
no come on I D can find it also so
that's probably something
good yeah
and I'm keeping my key
safe and now you
can
um get your
deposit
file and keychan is very user friendly
so it already tells you which file to
use so you use the deposit file open it
up every information is stored there
correctly and
continue and everything you then have to
do is yeah connect your your wallet of
course um probably if you if you're
doing the real thing you should connect
with a hardware wallet um um but you as
well might use metamask
I don't have now 32 holeski Eve so I I
will finish here but um you then press
continue and everything is set up for
you okay so now look look back to to the
steum launcher and we see everything has
start running and at that point I think
I will hand over to
[Applause]
David hi hi hi okay nice uh uh thank you
David I'm also David so it's pretty easy
to
remember um I'm going to show you like
uh basically we are going to I'm going
to show you how the staking page works
I'm going to show you the rest of the um
setup itself I'm going to show you some
management options at the end I'm going
to ask like Martin to join me for some
questions you can ask whatever you want
about staking you can also ask me like
personal questions but I would like ref
from that um let's just see as uh David
already explained basically you deposit
your key uh as soon as you deposited
your key this key goes into activation
queue usually takes a few days during
this time you can basically but you can
already if you want to import this key
in the setup itself so to do this you
would go on the staking page on the
bottom as you can see there's like a
click to insert the key uh as soon as
the key you basically click this you
select the key
itself I cannot read this I'm a little
blind I'm
sorry you basically select the Chason
key file you go into e and then you
would uh basically go for the other
steps as I can see we have like a little
bit of a thing here
um what did you use
password okay this it's a good password
thank you um I'm going to go here
Bam
Bam on the bottom as you can see you're
already like inserting the key on the
bottom you can select which validat
client you want to import to uh steer
gives you the option to run multiple
clients at the same time uh when it
comes to validate the clients I would
ask you um or like please um please
please please please please please if
you're run two validate the clients
never import the same key in both
clients you're going to get slashed
that's just how it is uh slashing is um
especially here uh usually not that much
of a problem I know a lot of people like
are really uh intimidated by the idea of
getting slashed but it's usually really
really rare uh most people you see
getting slashed or if you see someone
getting slashed it is because they
thought they were too smart or wanted to
like build a backup system that got
online suddenly or um tried to like uh
do some great engineering stuff I can
tell you uh when you want to stake keep
it simple uh even if you go offline okay
um let's say you go offline for 1 hour
you will get back the rewards basically
you lost in this one hour in one hour so
it's around the same
time um and if you get slashed there's
no this happens basically immediately so
that there's no uh there's no good you
cannot recover from this so keep it
simple try to like stay with one client
pair if you especially don't uh
especially if you're beginner and uh
don't go for multiple valid dat clients
if you want to uh do a backup system you
can do this by like running extra
execution and consensus client pair you
basically just change the connections I
will show you this after as well you can
do this inside of the UI as well so we
just select here uh the client we want
to import
into this
case see if I get the password correctly
one
second so uh put in the password you can
see you click here then uh you have the
option uh to import with a slashing
protection database uh at the beginning
when you first set up you don't have a
slashing protection database you get
this if you remove a key from a valid
dat client you have the option to
download this slashing protection
database as you might like guess from
the name it's supposed to be an extra
layer on top of this uh you also have
the uh double G doubleganger protection
running um this is basically uh every
client as soon as you import uh a key
basically checks the chain if the uh if
the valid dator key attested in the last
two eorts this can take depending on
client actually quite long I think te is
the longest I think it could sometimes
take up to half an hour some of them are
really fast doing it uh if you have like
um if you're in a hurry you can always
deactivate this I will also show you how
to do this uh in this case as I said we
don't have a slashing protection
database so we're just going to import
it here and basically it's just going to
run through I hope I did like did the
password correctly and as soon as this
is uh is done it's going to just uh um
it's just going to be imported the you
can do this before the activation C
queue runs yes perfect you can do this
before the the keys through the
activation queue meaning as soon as you
uh as soon as you uh went through the
activation queue you're already online
so you basically just import it wait
wait till it's activated it's just going
to be automatically online and then it's
uh then you are basically
testing um on the staking page itself as
I said want to go through some like uh
some other features like some management
features um on the staking page itself
you have the option to like just open
Pon sh the end it's just a quick link uh
it's the most common used tool to get
like a network view on your um on your
note or on your key um because this case
um you have a note it's a peer-to-peer
Network okay it's it's it's not seen uh
it's not seen everywhere uh the pacon CH
basically gives you like a good overview
of how the network CES your key um you
can also copy the public key um
basically identifier quite common I
think everyone know knows what a public
key is uh you can give the um valid data
key a name uh this name is if you have
multiple Friends u you all want to stay
on one
note um you can give this give this one
name let's say you have two keys you
give one you can call uh name one like
your name you can name one the other
it's just like some management options
uh you can set a block fee recipient for
individual key there's also the opt uh
usually what you do is um set up a
default fee recipient uh in the uh
validat node Cent settings uh but if you
don't want to use this as I said if you
have multiple key maybe you St with a
friend to get on one machine you can
like set it up in a way that uh your
block fee recipient for your key so your
block production reward for your key
sent to your address and the uh block Fe
reward from the from your friends keys
to send to their
address um then you can always remove
the client uh validator always remove
the validator key and you can also
easily like exit and withdraw just click
this button it sends a it creates a exit
message gives it to the consensus client
consensus client broadcasts it to the
network and it's basically it it's
already exited uh you then go through
the exit queue also takes a while so if
you have like huge swings in the value
or price of Eve you might want to this
is hard to like plan ahead in this case
but uh you won't be able to like
instantly sell it or something like this
so keep this in mind please um you also
have the option as you said this is for
the individual key you can do the same
for the uh whole client so you can set
uh a blockchain graffiti actually uh
whenever you're um whenever your note
produces a block you have the uh option
to like include a small me message in
there this could be anything uh it
should be up to 32 uh 32 key uh 32
letters
actually um in this case we what we
usually do is uh set set it as default
st.net it's also basically if you go on
PCH at DN and you put in like st.net you
will see how many blocks what were
produced by people who are using steer
and didn't change that as I said you can
change this whenever you want uh it's
was nice for us to have like some
numbers but uh if you if you just want
to like have a fun message in that is
absolutely fine um also option to remove
for all the every single uh validator
key from the client option to withdraw
every single valid the key from the
client and as you can see there's also
the option to import remote Keys uh we
support web free signer um I can say
personally I don't use it and I don't
think anyone of us uses it uh because
with this it's uh basically really
really easy uh to switch the uh switch
between the switch between the client
pairs anyway what people usually use the
web free Center for is like they use
this as a extra layer so they can import
uh switch the import the keys into the
valid dator CL and just switch it up uh
but if you want to do this it's just
click you can show this
off just a click you can do a local one
you can also like choose an external one
if you want to so if you have the web
freesign on extra machine you can just
uh put in the uh
UL uh to the to the machine itself on
the right side you'll see a little bit
of uh some stats as you can see you can
see the EPO you can see the slots uh the
curent slots on the bottom if you would
get a uh if you would be part of the
sync committee or you would be part of
the uh the block
production uh is like um going to be
soon you will see this on here this is
basically uh like an extra help for you
to know when you have to do updates
because uh blog production is kind of
rare it's basically uh once
the chance to do this is one in 150 days
so uh you get it on average twice a year
some people are more lucky some people
are less lucky it's basically a lottery
on top of the attestation rewards you
get
anyway so um you also have the option to
uh group these so if you have like as I
said if you have friends or you have
multiple or you do some staking for
other people you can group their keys as
well you would basically click here then
click here
uh you can filter the clients uh this
works with public keys and uh the names
you can set and you can also uh just
switch between the showing the names and
the public keys so um now we're going to
go a little bit into the note page it's
probably a little bit more exciting uh
steum uh supports you having actually
multiple configs at once or how we call
them is uh
setups uh meaning you could in theory
run a heski node and a main node on the
same machine given your machine is
strong enough they obviously need still
the resources they
need um in this case we only have one
setup they we just set up it's basically
setup one where we can go in you see the
three client pairs uh Bas is already
syncing loar is already synced with the
checkpoint sync um and us can see also
like the VC has here it's one key uh um
what you usually would do after um going
through the going through the setup is
also set up a uh default fee recipient
because you need this if you don't set
the default fee recipient and you
produce a block uh you're going to burn
your block reward basically which is
nice for everyone else like happy about
like losing some Eve in the network but
uh for yourself you're going to like uh
bite yourself in the ass basically
because as I said one in 150 days
especially if you use meth boost this
could be quite some money uh we we
ourselves like produce blocks um they
are like multiple hundreds of e
obviously usually it just happens when
we have like a hack on the network and
some some hacker sends it like as uh as
fast as you can it doesn't care about
the priority FEI at all um you would
basically get this if you send it back
that's like I guess your decision I
never like got the process quite but uh
what you would do is you would go in
here uh you see you see here uh default
fee recipient you would just replace
this uh Ox o address uh then you would
confirm and restart you can see uh we
can set the gas limit here is actually
important the current discussion like to
set this higher and lower um then we
have the doubleganger protection as I
said the double ganger protection is
supposed to protect you from slashing
yourself as so getting slashed for the
keys is like just an extra layer if you
would import and it like detects that
you tested in the last two EPO it will
basically just give you a warning hey
are you sure you want to import this uh
obviously you can still import it but uh
usually it's a pretty good warning you
should probably keep that in mind uh if
you don't want to wait um also as I said
uh some clients really need long like uh
if you're if you're in a hurry there is
usually no real reason to do but if
you're really in a hurry uh or like have
multiple hundreds of keys uh you can
always like deactivate this also just
confirm and restart and then you would
it would just like import it without
doing this check as you can see um also
really
interesting uh we built the whole thing
in a in a way that you're are capable of
like seeing what it does actually if
there like a small task manager so um
you can you can always just if you run
into like any air for example uh could
be it's it's a client software it's in
development usually like sometimes
they're stable One release sometimes
they gets unstable the next release then
they get stable again it's nice
obviously that they uh get still like
this that much like development time but
uh this leads to some could lead to
always like some problems during the
version if you run into a problem uh we
usually recommend you to just uh check
out first if the uh in the task manager
you can copy this data you can come on
our Discord you just copy it in if it's
an
error uh you can always also uh go in uh
for the clients themselves uh you can
always go into the log Pages the log
pages are basically your bread and
butter when it comes to maintenance
whenever you run into any problem with
the clients themselves you will
basically find this in here uh you can
switch through the clients
themselves this case you can see see
we're already like uh sinking here on uh
lot here sinking it just tells you uh
the the
um errors happen quite uh quite rarely
usually this uh the not usually only
breaks if you have like a blackout for
example or you um run into any like uh
syncing problems um if you run into
syncing problems we have uh easy command
to do this you can always go into the uh
resin button is basically the same as
the thing in the setup themselves you
can if you want to think from Genesis I
don't recommend this it's also not
recommended by the client teams to do
that because a it takes forever and uh B
you just uh sometimes you could run into
problems during the sying from
geneses um then you can uh you would
just select like a checkpoint sync uh
recommended one you go with for example
loar or something like that and uh it
basically just deletes the old database
it attempts to uh attempts to syn from
this uh checkpoint
itself um another some other things we
have we have like a uh link to the
documentation so if you're interested uh
to like uh configure your note a little
bit more deeply maybe you use it for
development uh we do this we have like
the option in theerum you can uh in the
settings themselves you can go into the
expert mode it's basically uh Docker
compost config a little bit of a
glorified one um you can see you can
like set up the options here we give you
the full control uh but if you play with
this and you break your notes uh you
basically I think you know what uh we
hope that you know what to do that's why
we call it expert mode uh you can like
add from the documentation some stuff if
you need like for example uh long longer
block retention you want
uh uh you want to change uh some like uh
parameters you need different name
spaces for development or want to get
different data you can do this basically
set this up in
there
um then uh the next one we have like a
simple start and restart button pretty
uh pretty basic and uh from this the is
basically the note page uh what David
explained to you also is um you can go
with a meth boost is really easy to set
up so this is now a solo vanilla staking
one if you let's say you decide after
like a week of running this hey actually
I want to use meth boost you you you
don't have to set up the whole note
again you just go in here uh we have
like a edit note page it would go in
here as you can see this is uh you can
see the connections you can also change
these connections on the right side you
have the option to just add stuff like
me
boost
okay uh you you can choose the
installation path then you would go next
uh you choose your relays these are
obviously different on Main and they're
depending on the network you're
currently on you can take all of them
there's usually no reason to not take
all of them because me boost takes the
best block from these relays just uh
chooses this automatically if you're
American you might want to go with the
over compliant one um I don't know how
I'm not an American I don't know what
happens if you don't I will be honest
but um just going to go with all of
them then you would go
next you have to connect this to a
consensus client you can only connect
the me boost to one consensus client if
you want more me if you have more
consensus clients and you want you have
to add more M
poost Services uh then we go with load
star we confirm and um as soon as we
confirm the changes here it basically is
going to install this it's going to
connect all of this and um then uh your
note basically choosers or your
consensus client chooses if uh usually
the me boosted block first the one
that's suggested by me boost if it's not
fast enough to do this it will just take
the one that's actually provided by its
own uh execution client as you see you
have like the small like little um icon
here to indicate that you are like
connected with this you can always
change this connections inside of this
so let's say if I wanted to uh let's say
if I wanted to add consensus clients
like
lighs
okay like
lighter uh it's the same path you choose
the installation path you choose the
sync options in here we can also go for
like just checkpoint sync as I said I
would recommend this to use this always
client teams recommend you to always use
this if you don't need the data itself
you go
next you can
connect this with execution clients if I
had more than one execution client I
could um basically choose this in here
as well this case I'm going to just go
with the baser one it's the same thing
just confirm the change and after this
um I'm going to show you how to modify
the connections meaning let's say uh
let's say load star would fall out for
some reason Could Happen um then I could
like pretty simply switch to uh using
lighthous with like two clicks of a
button
see I'm going to go in here I can
obviously also delete this I can switch
the client itself out uh usually don't
recommend doing this either because you
have to do some config changes as well
so if you're expert you probably could
use this if you're a beginner delete it
and just addit new it's it's basically
the same time it doesn't like take any
longer uh you can go here into the
modification and this as you can see if
I wanted to change this I can just go
here go here and
now it's as soon as I confirmed the
changes here it uses the lighthouse
client instead of the load star one so
you can build multiple client pairs if
you have the uh storage and the
resources on the um server itself you
can build multiple client pairs run them
on Parallel and then just switch between
them you can do this over multiple nodes
you can also uh multiple servers I can
show you this in a second as well soon
as we have through
this takes a little bit uh we have like
the option to uh make this a little bit
easier um so you would go in here you
can go here for
external if I can write it external here
uh you will set up our external Source
um there's a little bit of a difference
between the clients uh the all of them
are the same except prism for prism you
have to set the extra value though this
is going to change soon as well so soon
this is not going to be a client
selection anymore this is going to be
agnostic um the external Source you
would basically set up a IP like where
server server p with the um uh with the
port you could go in here just set it up
I'm just going to put something in
there matter it's basically like a
placeholder you then can connect your
client with meaning if I had another
machine with another IP with another uh
with a port to access the uh client
inside of my network I could run
multiple servers I could run multiple
servers multiple client pairs on One
servers I can run execution client on
one server can run a exe consensus
client on another a validate client on
another and just connect them through
this and then just switch depending on
actually my own uh needs in this
case also again takes a little bit but
it's quite fast so if I wanted to now
change use the external one I would go
the same way go in here select the
external one confirm uh and then just go
further so um David talked a little bit
about using the uh using the uh note
export option uh you can if you run this
setup you would just click here it would
basically give you this one setup let's
say you want to migrate your node you
have a new machine okay and you're a
little bit lazy you can uh it also
doesn't take that much longer but you
could just click here you would download
uh ZIP file with the configs you would
go into the setup again and then you can
uh just with the import config option
just import this uh ZIP file and then it
just sets up what you had before uh you
obviously have to uh import the key
again because we don't have your
password we don't like store any data
you don't send any data this like pure
uh your stuff and you also have the
option to like import like a single
config this would import all of them uh
export all of
them um as you can also see we use
grafana promeo we have like a nice
little uh control page it's it's
basically it just gives you basic view
uh with really really simple stats if
you want to go more complicated you can
always build your own grafana dashboards
if you want to you be deliver the client
grafana dashboards with them they are
basically default and uh def to use uh
you can set the alerts in grafana you
can like actually like get some EX
external notification going on in there
um you can see uh you have here the the
current sync status it now it loads like
the your your noes view on the network
uh usually I don't uh recommend taking
this as a how should I say as the most
source of Truth when it comes to like
the network status because it's just
your own notes view on the network if
you want to actually know the network
status please like visit peing chart at
the and great Tool uh you can see on the
right side you can use uh you can uh use
your RPC provider uh because theerum
uses SSH to connect from your launcher
to your server uh you have to open the
tunnel here uh then you can copy this uh
copy this
string would put this for example into
metamask um I could show this
just uh we will take this one you could
go in here you have like the network
option you go in here you go in here you
can go in
here uh you should go where is
it I haven't done this in a while have
to be honest uh you would basically go
into the uh options
themselves
uh
okay uh you would just put this for the
RPC connection you would put the E
symbol you would choose a uh blockchain
Explorer to basically uh show you the uh
the uh
the the transactions and how they are
used can you go back this to
yes okay um then you obviously also have
the uh websocket endpoint and the data
API this one is from the this is
provided by execution client the RPC the
uh web socket and the data API is
provided by the consensus client if you
run multiple ones you can uh switch
through them uh you can also see here a
little bit of stats um from the key
client themselves so some of these are
currently a little bit uh these are Curr
wrong because uh your key obviously
didn't like start the testing and it
didn't go to the Keys it's to the queue
itself uh when it comes to updating uh
because you constantly are having a node
is a mainten is mainly maintenance uh
maintenance is really really easy with
steum itself uh you have two options to
do this uh you just as soon as there's
upcoming hardw for example you would
just go in here and you can update like
your clients you have multiple update
options you can go with your Sero
updates uh you can uh steum consists of
two parts the launch and the Not So if
there's a new stereum release you will
have a new launcher version this usually
happens as soon as you open theum it's
going to go into auto update mode just
downloads the newest launcher version
automatically you would then log in go
into the node updates could just
download it here if there is a service
update let's say F has a new uh new
version you would see it in here you
could just click it you can just also
update all of all at once uh except the
uh Servo as updates they on extra page
uh for good reasons because um probably
is going to restart your notes might a
lot of people don't want to do that um
if you are really interested we have a
lot of people who actually uh steer
provides you with the option inside of
the server management page uh you can
switch through the servers here as well
as you can see we have multiple ones uh
you can also change your password here
um you can set up uh you can create SS
SSH key you can delete SSH Keys here you
can manage these as well and um you can
do the opun updates here just going to
check for them if it's going to find
some
nope um but with serum you have the
option to always go with the automated
not updates these are actually going to
pull down all the um stereum Note
updates and the client updates we have a
lot of users who put this on and then
never look at it again uh Works quite
fine we also have like some noes we have
we have this open they still attach to
this day so um even if you're on your
way let's say you travel a lot this is
like a easy option to actually check
your notes you can uh and automatically
update it without having to constantly
look into it uh we also have a
experimental 2fa feature um to use this
please do actually this there some still
some problems with it uh that we're
currently working on um you also have
the option to like just add a new server
connection here you can switch through
them if you have a SSH key setup you can
actually go with a quick switch which is
really really
nice um
then uh with this this the update
process uh if you are a little bit of
expert we have uh the option for you to
go into a secure shell so you can
actually also use this here you don't
constantly have to switch between uh
terminal and uh terminal and steer room
it's just for us we build this
especially for us because gets annoying
after well um then you also have here on
top uh a help button so if you need any
help you can go from here we have like
uh a GitHub obviously open GitHub so if
you find any mistakes please be kind and
just report them and we also have a
documentation
itself um we also have the option for
the notification we support two things
uh we have like a small little mobile
app it's really really small uh you
basically set up a grafana alert um this
uh this comes over encrypted over relate
to us and we send this out but you also
have the option for the more common what
most people use is Ping chart DN it's
not hard to set up you basically click
here then you would uh then you would
select you validate the client here set
the machine and API key up you have to
set the API key on the Ping ch.
website
itself um then the um updates are
already
showed and uh you have also the settings
you can change some languages we didn't
uh uh we don't we translate as much as
we can so um if you're not English
speaker and know someone is not quite
that much of an English speaker you can
also use this
yeah uh the option maybe if you run into
problems uh what we usually do or I at
least usually do um if there's like
something breaking my notes I'm a I'm a
All or Nothing kind of guy um I like to
just nuke the notes um we just basically
press here and this kills the whole
thing you can dump your locks here as
well and as soon as I click this it's
just going to delete everything on there
it takes a little bit uh it's quite a
nice animation you can thank that guy
for that um just takes a little bit I'm
going to then uh show you some of the
other options we have as well like just
go through them one by one and then uh I
guess in 5 minutes if you have like some
questions I would love to to answer them
all so um
just just get down to this node again uh
this is now
this is now a nuke node meaning if I as
soon as I go in here I go basically
through the whole process again it's
just going to check is there not
installed if there is no node installed
I'm just going to go through through
this page again uh the options are
pretty pretty simple uh this case I
don't have much time sadly to show you
the other stuff uh if you're interested
we can always talk about it uh but the
basic like difference is uh this
installs uh extra validate client SSV
uses not the standard valid dat client
they use their own valid dat client to
do this obal uses an extra service that
is connected to your validator client so
if you go in here you would like
see here this installs the OBO Chon Serv
Chon
Service uh then uh the steer arm you can
uh basically uh this is installing just
the node clients without uh monitoring
uh services uh the archive node usually
just sets extra stuff in your expert
mode config so you actually retain the
blockchain data uh the LI CS uh the LI
stvm modules uh both use SSV or um OB
respectively and in the end we also have
the LI
CSM uh itself where we have like a uh
the valid dat cheor Li users we have the
LI Keys API and the CSM monitoring
service we build for this as well as an
ipfs service to just keep the data
forward
so okay okay um with this I would say
like we have like 15 minutes left um I
would love uh if you any of you guys
have any questions um we're going to
answer them all uh Mar is going to help
me with more technical questions it's
not quite my so um
hi uh when you use uh this installer for
arm devices when you would like to
deploy an ethereum node on arm devices
uh because you have very limited
resources resources for example on
Raspberry Pi 5 uh I guess you have
limited uh options about uh execution
and consensus clients and I'm curious
which one you recommend or which one you
use as default
um so um I actually set that up um quite
a while ago uh it was back in girly and
um what I used was gath and Nimbus
Nimbus is very very lightweight um and
especially if you run on like these
small devices um running on arm I would
recommend Nimbus for this kind of cases
um but um it depends it it really
depends this machine was like even a
smaller spe it had like only 4 GB of RAM
and it took like two months to say I two
months two weeks to sync so probably not
the best but if you're like have a PR um
device um you can have like more options
open um maybe even um NE mind or like
depending you have would have them to um
experient with all with all the um
settings steum provides you um or all
the different Cent nether mind for
example um Run's great but if it comes
to pruning you will probably have to um
reduce the used load while pruning um
but yeah it is possible you're limited
um but it's definitely
possible one more question about path to
the storage this two terab Drive uh when
I would like to use uh two drives one
for uh operating system and the second
one for the blockchain copy uh can I
provide um a path where the blockchain
uh should be stored if the partition is
um correctly mounted this is definitely
possible steer room will check um your
petitions and will use the biggest one
um out of
default um but you can change it up the
way you want okay thank
you uh do we have another
question okay
perfect
so all so uh thanks for the presentation
um quick I mean idea if let's say you
have more than one validator key or
sorry you want to run more than one
uh uh the terminology eludes me a bit
but let's say you've got 64 eth you want
to run two validators is it best
practice to run it on two separate
completely separate things or is it best
practice just to use one sort of setup
for both keys I would I would um so the
validat client can in theory hold
infinite valid dat Keys um I usually uh
the more validate the keys you import
into the client the more resources it
will use to basically uh sign for them
because it like has to sign and then
send this to the consensus client but
you you will not notice this until you
have like a 100 keys on one note uh
which is quite rare for some people for
obvious reasons
um so I would recommend you actually to
use one machine because you run the
problem is uh your biggest risk is the
slashing risk and if you for example
forget which key you import in which
client you could always like a human
error is your biggest enemy basically uh
so having them on the same machine is
probably like the best way to go in this
case
and one quick followup to that then um
by running two validators on the same
client are you running a risk of both
being slashed at the same time or would
all it would only be one or the other in
most cases um the so you you don't
really run a if you just have one
validate the client and you only have
this two keys in this one client there's
no risk of getting slashed whatsoever
the risk of getting slashed is for
example if you have both the as you
described your scenario if you have both
of these nodes running okay and for some
reason you forget which key you had on
which
uh which client and you import this
again okay it's going to warn you okay
it's going to tell you hey the
doubleganger protection is going to say
Hey you are like testing the last two uh
epos uh but if you if you just like
mindlessly click through this okay you
you're going to get SL you're going to
get slashed just by having the key in
two two different validat clients active
at the same time otherwise slashing is
basically it's a really rare event and
it's actually really hard to like
actually run into if you don't try to as
I said be smart about it or try to some
backup setups or something like that if
I may make just one one other scenario
quickly um so in certain parts of the
world let's say so these Asia power
outages are somewhat common you know I'm
worried about my machine running it uh
we lose power it doesn't reboot properly
um you know in such a case if you've got
both of your keys on the same validator
then both would be SL for being offline
is that correct uh slashing is never for
offline um slashing is really just the
uh it's just the penalty you get for um
trying to cheat the network in this case
uh if you try to as I described uh sign
with the same key on two different valid
dat clients uh what you go what you run
into with uh getting offline is leaking
uh which is basically your uh note goes
offline for let's say your note goes
offline for 24 hours for example or 84
risk for you to just like actually set
this up again if you don't get stressed
about it okay you're going to the the if
you lost in the 72 hours as penalty you
will get back in 72 hours so that
there's really no risk as as long as you
don't try to uh as I said build backup
system there are way too over
complicated and go online at the same
time that you you will never run into
into slashing yeah you're
welcome
um
oh what do you need when staking with
lier CSM yeah that's a good question
actually uh lier CSM you basically go
through the same process David showed
you uh the only difference is instead of
the etherum Launchpad you go to the
lighter CSM Launchpad uh there's like a
test lios CSM I could probably share
this
with can probably can show this after or
like I'm just going to like if someone's
interested just come to me I can share
you the link with you uh you take the
empty key you go to the LI of CSM page
uh you upload the key in there you pay
your bond and that's basically is and
then you just import the key it's it's
the same process as I said just instead
of the Launchpad you go to the LI of CSM
stuff uh how many people use theum uh we
are it's it's really really hard to say
we don't collect any like user data we
are not interested in your user data we
don't want that um the best indicator we
would have is actually as I said the
blockchain graffiti you only said as you
only like see when the relid DAT key
actually gets to produce a block which
is one in 150 days you could see we
could you could estimate it um I would
probably say around uh 1,000 1,500 based
on the download number numbers but I
also have say I have to say we have a
lot of uh because the tool makes it a
little bit maybe maybe even too easy uh
we have a lot of lazy users who don't uh
do the updates all the time they just
like as I said put the auto update on
it's going to like get the client uh
client down uh updates automatically
it's going to take the Note updates
automatically so uh they never showing
our like actual download numbers from
GitHub and this is really the only thing
the GitHub number num and the blockchain
graffi we can use to estimate
that are there guides or tutorials for
steum yes we have like a documentation
page with like a uh guides uh we also
have like uh a little bit old tutorial
videos but they basically still work the
same uh the UI changed a little bit
between this maybe interesting to see
what we did in the like uh years we uh
working on this uh so uh you also can
always come if you run into any problems
whatsoever we have a Discord server we
are 24/7 there uh basically when it
don't sleep most of us are Europe based
so if you write to us at like 3:00 a.m.
in Europe time we might not like answer
directly but as soon as we wake up we're
going to see your message in our Discord
and to just come and actually try to
help you there was never a problem we
couldn't fix really uh as as long as you
like actually give us all the
information we ask for and you just Comm
communicate with each other it's really
really easy to go through most problems
and yeah
um if there's uh no no other question I
would like end it a little bit early if
that's fine for you guys uh so anyone
else
anything okay perfectly I don't know
thank you everyone for listening um
thank you for your attention if you have
other questions like personal question
or like specific question to like setup
you can just find us we also have like a
booth on Thursday and Friday uh you can
try it out yourself if you want to we
have like machines here to actually try
it out we also have some nice like merch
if you want to come here um and yeah
thank you very much and I hope you all
guys all have a nice day
back back back back
a
that's
o
yes
h
oh
right
back back o
back by
o back
is
back o
hello everyone well today we're going to
be talking about waku H waku is a
decentralized protocol for messaging
that allows you to send a message from
point A to point B in a privacy
preserving way and rln you may have seen
it in the title stands for rate limiting
nullifiers and allows you to rate limit
the users in a network to prevent spam
so first of all I would like to
introduce you Frank Le of waku H he'll
be he will be presenting the second part
and I will start with an introduction
and some small Workshop where I will I
will show you how to join the waku
network by running a a note and
participating in in our Network
so H this is the agenda for today um we
will I will start with a waku
introduction telling you what waku is h
what waku is not the future the problems
we have already solved in the past years
H then we will continue with uh the
small demo that I told you before it's
going to be a quick Workshop I will
share the commands with you in case you
want to run them and in case you want to
become an operator in the waku network
and relay traffic on it and then Frank
will talk about uh yeah the need for a
flexible rate limit in rln and the the
economics behind the behind
waku so uh before H explaining what waku
is h can you guys raise hands h who
knows what whisper
is okay I see a bunch of hands up I
think I know
everyone okay so waku is some kind of
fork of whisper and it fixes most of the
problems that Whisper had originally
back in 2016 17 something like that so
yeah waku ER right now is a suite of
messaging protocols and it's meant to
deliver as I said before a message from
point A to point B or from point A to
multiple multiple points like a group
for example a group chat it does so in a
privacy preserving way without relying
on a central entity and it's generalized
for any use case you can build a chat
application but you can also build any
decentralized application that you can
think of if you need to connect as I
said before point a with point B in with
these properties you can use waku so we
are not really bind that to a specific
use case and uh yeah the coolest thing
is is that it's permissionless for for
anyone anyone can join the
network so um as I said before Whisper
had some problems and waku has solved
most of them in the last years first of
all
latency um so in a network with the
properties of waku latency is very
important because the messages don't go
directly from point A to point B right
they travel through many nodes uh
jumping multiple times right so so to
fix this we have limited the the message
size to 150 kilobytes I will explain
later why and um yeah for the latency
there is also a trade-off between the
replication factor and the bandwidth I
will explain this later but yeah long
story short um we can guarantee to some
extent that every message in the network
will arrive within one one second second
problem that we have solved is the rate
limiting so H in the web two world it's
very typical to rate limit with IP right
so if I see that your IP is sending more
than x requests per second I will stop
you right because you are not making a a
fair usage of the resources but in the
web three world it's a bit more
different because um waku H sorry um in
in the web 3 world it's a bit more
different because you don't have an IP
to rate limit because you can't connect
the messages uh to an IP so H we are
using rln which stands for rate limiting
nullifiers H this was originally Al
designed uh by the etherum foundation
the PS Group and we have adapted it and
we have also uh some peer scoring so to
every peer in the network that you
connect to you keep assigning an score
and if the score drops below a given
threshold then we will kick out this
pier from the network so the third
problem we have solved is the offline no
so your note could be offline for a few
hours days minutes or seconds and uh
someone may have sent you a message
during this offline time so for this we
have a store protocol and store sync to
fetch these messages that you missed
while you were
offline um so running the four problem
we have solved is the running waku in
resource restricted devices because um
running a full Noe as you know in like
in ethereum right uh you can't run a
full note in your phone it will drain
the battery and you will run out of
memory uh super fast
so for waku we have designed light
protocols they are called filter and
light push these light protocols allows
you to use the network and publish a
message for example on behalf of uh
another peer um this allows you to run
waku in a mobile phone for example
without consuming battery and and data
uh yeah I will be talking about this on
J Merkel 3 a bit later and yeah last but
not least we have scalability H we have
sold the scalability of the network NW
by Shar in the network a multiple chart
so we have splited the network in
different sub
networks so I will zoom in in each of
the previous point that I have explained
latency uh let's start with the diagram
on the left H here we have in the lower
axis we have the outbound degree D if
anyone knows about gossip sub you will
know this D this is basically the
replication Factor so the the how many
times uh the traffic that you inject
into the network netw is
replicated and on the other axis we have
the amount of hops that a message will
travel in the network uh before arriving
to all the peers so the thing here is
that let's say that you set an N of
this would be the the red uh the red
plot right so let's say that you want uh
a replication factor meaning like the
the times that you uh replicate the the
bang within the network of of uh six for
example then you will have a worst case
amount of hops of four meaning that a
message after traveling four hops it
will arrive to all the peers so as I
said before there is a trade-off in here
between this and this right because you
can't have um low low latency and also
low bandwidth consumption so we we're
playing with this so uh we have done
some simulations you can check them here
uh this is the distribution times of of
arrival of a message in the network we
were using different sizes 2 kilobytes
the distribution so uh in these three
first plots you can see that the in the
worst case every message arrives uh
within 1 second this is why we have
limited the the maximum message size to
case with 500 kilobytes the the average
time goes quite quite up uh close to
like 1.7 seconds and this starts to to
go quite quite high so if you send in
WhatsApp it takes less than a second to
send a message to your friends right so
we We should strive for something yeah
similar cool let's continue with the
rate limiting um as I said before we use
rln right limiting nullifiers to write
limit the users so a rate limit example
could could be like okay we allow a user
to send 100 messages every
hour um the cool thing about rln is that
it does so in a privacy preserving way
using zero knowledge proofs and um we
can also act upon the rate exceeded for
example if we detect that a given user
has exceeded the rate limit we can slash
him or her H yes as I said before this
was initially started by the PSC at the
etherum
foundation so um I will explain more
detail about rln what does it mean what
what it's a membership so basically a
membership it's your key that allows you
to participate in the
network um this membership it's stored
in a Merkel tree that is on chain and
anyone can register its public key on
chain you have to only pay a fee H we
have deployed it in in ethereum by now
it's a sepolia it's a testnet which is
called sepolia but anyone can do it
after paying a fee so yeah basically we
are storing this in the in the
blockchain we have the this is your Leaf
this would be you and we have aerle tree
representing all the memberships very
easy so um the thing about um rln is
that only the one who knows the private
key of this public key can generate a
proof right you can see this proof as
some kind of a stamp that you will put
to a letter you will stamp to a letter
this stamp is in reality a zero
knowledge proof and it allows every node
in the network to verify that the
message is correct and is respecting the
rate limit so yeah uh itach to the
message and it makes it valid in the in
the network you can think of it as an
stamp that you have to buy in the post
office and put it to your to your
letter um since the Merkel route of the
tree that I showed you before is public
anyone in the network can verify that
the message is correct so you get the
root you get the message you verify the
Z knowledge proof and you can decide if
you want to accept or reject the the
message so yeah offline notes uh
basically what I explained before if
your note goes offline for some time you
will have to to fetch the messages that
you missed H we have two protocols a
store and store sync and yeah the latter
the later is um based in a Range based s
reconciliation
um regarding res restricted devices uh
we have yeah we want everyone to be able
to use waku even if you are running on a
mobile phone so for this we have these
two protocols light push and filter a
light push allows you to send a message
to the network via another node and
filter allows you to receive you can
think of it we call them light protocols
or Edge nodes you can think of them very
similar to what ethereum light clients
are uh if you have I heard before a talk
about the portal Network so this is very
similar to that because we we can't we
can't assume that people are able to run
both ethereum and waku in their mobile
phones um we have H one feature uh that
we deployed to the waku network quite
recently that I think it's worth
mentioning so um in order to generate a
zero knowledge proof H you need to
insert the as a witness if you know
about Z knowledge proofs you have to
inject the merel proof of your Leaf the
thing is that if you're are a light
client H you don't have this information
right you would need to synchronize the
whole tree locally and then be able to
generate the merel proof so long story
short we have done a modification in the
in our contract and in this contract now
we are storing the whole merker tree and
you can get both the Merkel root and
Merkel proofs directly from the contract
meaning that a light client or Ed no can
go to the contract get whatever he or
she needs and then generate the proof
and send the message to the
network so yeah as I said before uh you
can generate proofs without sinking the
tree locally this is very nice because
Sy in the tree as you may imagine you
have to synchronize many events and this
can take several minutes and um yeah
this you can get the Merkel root and
Merkel proofs from the contract and
these calls are gas free because you are
not writing you are not changing the
state of the of the
blockchain
so um the cool thing about this is that
the gas increase in the membership
insertion is very reasonable so we we
can deal with it h waku may move to a
layer two to make H yeah to lower the
fees but even right now the fees are not
that crazy so yeah rln it's working for
uh light
protocols and yeah scalability nothing
to add to what I said before uh we split
the network in multiple charts and right
now in the waku network we have um eight
charts basically if you know about ER
gosip Saab we have one topic per
chart okay demo time I hope this wasn't
very
painful 15 minutes not bad uh if you are
interested in following along you can
scan this QR code I will leave a few
seconds you can also browse it it's uh
waku org and waku
compose yes if you have any questions up
here I can take few
uh yes uh in the in the demo I will show
the I will show yes
yeah just a quick question uh you say
you generate a zero knowledge proof
every time someone sends a message yes
correct how much time time does it take
to generate the proofs on average any
idea yes H we we wrote a paper actually
about this it depends on the platform
blah blah blah ER around from 80
milliseconds to 150 milliseconds
depending if it's a Macbook Raspberry Pi
whatever but yeah 100 milliseconds it's
the it's a very basic H seral proof
because it's just H proving that you are
part of a given Merkle tree and that you
respect a given rate limit it's not like
you know in ethereum they are trying to
prove blocks and this takes like two
hours right but yeah
thanks don't be
shy cool we will take also questions at
the end so no worries cool so as a good
engineer I don't rely on the internet so
I have a video because I don't trust the
internet so yeah what we are going to do
now um we are going to H run a Docker
compos setup that that runs a waku node
and we will also show you how to
interact with your waku node with a
simple front
end and with this you will be part of
the waku network and you will
join other nodes relying traffic so
let's
start you can see that the terminal is
open on the right side on the left side
you have the QR code
link We start with copying the
configuration the environmental
file now we open it and we have to
modify couple of things we are using an
ethereum endpoint H you have to provide
your infura API key for example you can
copy this it's fine you have to provide
also your ethereum private key do it
only for testnet you can copy this as
well this is the account this account
has to be funded with some ether in
sepolia and now we are going to register
your rlm membership this is a
transaction that goes on chain to
sepolia and we'll give you the right to
use the waku
network it takes few seconds because
it's also waiting until the transaction
is validated by the nodes we will We I
will show later the the fees we are
paying for
this H you can see also that it will
appear here right now H you register
your membership for a given rate limit
in this case we have one 100 meaning
that you can H send 100 messages every
have defined but you know waku is open
open source if you don't like it you can
Fork it and have your own rate
limit so yeah you can see that the
credentials are persistent you can open
the the key store it's a key store very
similar to the ethereum one it's a bit
different but yeah you can open it a
bunch of exad decimal numbers
now yeah this is the transaction uh this
is the Smart contract the rln smart
contract this transaction is the one
that we just uh submitted we have 21,000
members in the
tree and I will yeah open the
transaction you can see that the gas
it's yeah wait one second yeah it's
consuming 150k of gas this is quite
reasonable even for ethereum mainnet the
function that is being called is the
register function this is your
commitment so it's basically the the
hash of your secret more or less and the
rate limit which is 100 as I explained
before here we configure the store H
size I said one gigabyte meaning that I
will store only one gigabyte of
messages and now we are ready to spin up
all the services this spins up uh some
grafana promethus dashboards to monitor
some metrics the waku node the most
important things thing and also a front
end that allows you to interact with
your node you can check the logs if you
are interested for now this is like you
don't have to really understand
it and yeah the first time that you
start the note it will take some time
because it has to synchronize the smart
contract it will index all the events
until it goes to the it reaches the
latest head of the blockchain and once
done uh your not is ready you will be
relaying traffic of other people you
will have
the rln 3
synchronized yeah you can see here this
is the front end Local Host 4,000 you
can enter your
username and then you can join a group I
suggest if you want to join Defcon group
you can talk with other people here you
can input your message and when you
click Send it will be sent to anyone to
everyone that is subscribed to the topic
Defcon you can see that the message is
there cool so this was the this was the
demo H if you have any problems with
this uh later when we finish the talk we
can help you if you are
interested uh quick note before I pass
the mic over to to Frank this is cool
right but I mean I have WhatsApp it
works that's the same the user interface
looks nicer so why do you care about
this so first of all H you are running a
full node which is cool uh you are
relying traffic in the network so you
are helping others to communicate with
each other you also store past messages
and you have your own rlm membership you
don't have to rely on anyone and um and
yeah with this you are allowed to use
the network up to a rate limit this is
cool okay but yeah what's the advantage
of using waku so first of all the
messages are not linked to any Identity
or IP every time you send a message this
zero knowledge proofs doesn't connect
your identity to the message and also
since we are using gosip app uh to some
degree we can guarantee that no one will
know your uh IP or will be able to
connect your message to your IP also
also you are fully Sovereign you don't
have to trust anyone in order to use
this and uh it's decentralized because
there is no single point of failure and
you are connected to multiple nodes
using H gosip stuff and uh yeah with
this I will pass the the mic over to to
Frank he will be speaking about rlm
version two and the economics of of
waku thank you so uh yeah so R&amp;V one is
is what we actually presented at last
Devcon I've been working on that for for
a while and the past year we have done
several Improvement and what we call R
and V2 I already touched upon the fact
that now we have a market Tre on chain
which means that you can just do a smart
contract smart contract code to get your
Market proof and generate your proofs
another change uh change that we we have
is around the rate limit so
with as um as you mentioned the idea is
that to to proof and it's attached on
neoch so neoc is just a time stamp with
a granularity of choice the first
version of rln You Could Only R liit to
one message per Epoch which means that
um in term of smallest practical Epoch
once G would be the best under that will
be difficult especially considering
Network latency and anything above one
second uh you know if you go for 10
second 1 minute then becomes uh
impractical for chat app right because
if you the user has to wait you know 1
minute or 10 minutes uh to be able to
send the next message uh not really
useful so um also in terms of of traffic
so why we using RN again the idea is to
rate limit how many messages can the
publisher send the network so that you
can you can have you can cap the
bandwidth on the network so that when
you use waku on your mobile phone on
your laptop on your household Broadband
you know that you're not going to
consume all your data as well as you
know that you can still be part of the
network if you let's say you have um you
know 10 m per second at home and that's
that's what your internet can support
and someone comes in and inject a
terabyte of data you will not be able to
to receive all messages and forward them
as goip sub tells you to do which means
that we misbehave in terms of goip sub
terms and then you get kicked out from
the network all right so if we have
unlimited bandwidth you know um there's
no capping of the bandwith on on the guu
network or on any G sub Network then you
may get kied out which means that
basically you are you have an outage you
get um dust from the network right so
with woku um as mentioned we want to be
able to have a decentralized peer top
engines but also for laptop and and
mobile we don't want people to have to
use a centralized rest API so back to
the to the numbers so with one message
per second and let's say we have a 5
kilobyte message size average and let's
say we have a size user so we think we
can go up to 10,000 user on given chart
but just let's say just 10% of user just
continue to message you know non-stop
you end up with 5 G per second of steady
traffic so non-stop steady traffic and
you can imagine when you go back to a
mobile phone or just having this this
non-stop traffic uh on your on your
Broadband um is know a
problem so with rv2 the um like from the
technology point of view the Improvement
is that now we can do n messages by so
we're able to choose a a number and that
allow us to have have a wider ook right
so in our case so we we chose a number
of parameters and we're going to start
with that of course we can change them
as we learn more as we use them in in
various applications So currently on a
smart contract we went for 20 to 600
messages per 10 minute so we went for an
EPO of 10 minutes where we can use 20 to
they insert a membership um they insert
a public key to the smart contract uh
they can decide what rate limit they
want to pay
for so we also have um a rate limit on
the contract so on the smart contract we
have a parameter which is the number the
total number of messages uh pero so we
set to 160,000 message
byoc and on on the network layer so more
as a consensus between the operators on
the gossip sub layer we went for 150
kiloby Max message size so now we have
um more of a an API token like all right
so when you go for to infura and you get
a free token to for your RPC API or when
you pay for something uh usually you're
not going to get you know you can do one
request per second it's more like you
can do X request per hour or per day or
per month and sometimes actually a bit
of bus so now we have an API which is
pretty much the same so like you can buy
a membership and this give you let's say
minutes all right so just to to go back
to um we see here there you go so the
EPO are sliding right so 10 minutes so
for everyone an Epoch starts and then
last for 10 minutes and during this
Epoch we can send we can attach new
proof to each message uh each proof will
be different and every not in the in the
network knows that this um this this key
uh has used one 10 up to 100 Proof
because we use Z own technology you we
don't have um we don't know what
messages all right are linked to the
same proof to the same key okay so you
still have this uh this anom so someone
over having traffic can't see that oh
these 10 messages are coming from the S
sender from using the proof but we do
have the right limit in place um and
then when after 10 minutes when a new
EPO start um then we can forget about
all these Pro messages and we can start
to count
again so with r&amp; V2 so the for a node to
verify that someone is not exceeding
their rate limit they need to remember
the nudifier so nudifier is um is a
piece of data in the proof so for every
message that goes through the network um
the can check the proof and then store
the unifier for this Epoch until the
epoch finishes the unifier is 128 by so
one looking at you know why 10 minute
question why not doing a th messages per
day for example which will be much more
flexible for user right um a user mosty
you know if let's in the context of a
chat app you use your chat up you know 6
using it so um every 10 minute at night
that you're not using it you can lose
the opportunity to use the CH up right
so ideally 24 hours will be better but
we do have some limitation and and that
is around storing unifier for the epoch
so if we look at um let's say 600
messages for an Epoch which is maximum
limit for one publisher this would be
around 75 kilobyte per user which means
that for 10,000 users it will be 700
megabytes so 10,000 user why 10,000
because we think this is um um kind of a
good maximum size for a go sub Network
so for one given Network you have to
remember you have to keep in memory up
to 700 megabyte of data um for this
Epoch and if
you if you if you can't keep that in
memory it means that you can't verify
proof anymore and if you can't verify
proof it means that you might forward
spam and you might then get disconnected
but other not that did so the the memory
usage is very important in term of just
we're clear here this is about node on
the RO Network in our case it's both nod
as no VPS in the cloud as well as on the
desktop uh on mobile we don't for
traffic so we don't need this on mobile
but
um but so yeah so if you know if you R
by P if you start to use more several
Gaby of data we try to be very
lightweight client so that's why we went
for 10 minutes for now we could always
increase the EPO size or or reduce use
it depending on you know when we use it
um with with users and getting control
getting a
feedback another another thing with a 10
minute which is good is that if you go
for a rate limit per day so per 24 hours
one risk you may have is someone uh
injecting like publishing all the
messaging he can uh at once and in this
case you can have a peak of traffic and
this P of traffic may again lead to do
protection I we think for with this
numbers we think it's fine um however if
we were one day able to let's say you
know compress the or something like that
and move to 24 hours then most likely we
may have to have like a dual rate limit
where uh we we may say we can do s
message per day and a and you know 100
message per 10 minute or something like
that so yeah so basically like a lot of
parameters to to think about one on
deciding for R
limit all right so just trying to to uh
to do some prediction try to do some um
um some statistics so in average in
average uh just doing some uh some
distribution we could look at a traffic
of 266 message per second and average
message size of 4 kilobyte so maximum
message size is 150 kiloby but we we
don't expect every single users to send
maximum mess message size of the time
and actually 4 kilobyte looking at the
status uh chat applications that uses Wu
is actually a good average that we can
see in our in our
infrastructure um so goip Sub goip sub
we use goip sub like ethereum uh six the
the out degree is basically number of
peers that you're connected to and
foring message to and also the number
and this PE also for the message to you
so which means that with these numbers
we can uh we get around like a six megab
per second Network right and we split
our Network as I mentioned we split our
Network per shot
um in eight Shard so which means that
now we assuming uniform distribution
between The Shard so assuming that
network is uniformly distributed between
The Shard we end up with um a traffic of
much lower that's what we discussed
before with the one one um one message
per second um and that again you know
here it's um these are statistics right
so that what we think would happen um
but then of course it depends on the
application that use a
network all right any question so far on
RN V1 versus r&amp;
V2 so V1 we had to do one message per
EPO and now we can do any message byoc
and it's much more
flexible so um yeah so that's one of the
so we basically three three main
Improvement one was the message size the
message number of messages and the
second one is the market Tree on chain
and the last one is we have defined some
economics around the
memberships so the just going back one
again so what's the point right so the
point is when you want to send messages
to the network you have some rate limit
so you don't overwhelm the network you
don't overwhelm participant in the
network and and practically uh does them
out of the network
so if we have a system where anyone can
just and grab any membership then you
end up having the same problem right
someone can come in and take all the
memberships or take a high number of
membership and attack the network so you
have to have some friction to ensure
that you have to rimit that as well
right in some way or another have some
friction to ensure that no one just come
in and grab all the memberships in web
two right in in the normal classical I
would say
world you usually have some R limit by
IP um and that's why quite often you
know when I try to use VPN or toour you
you may have to have capture capture is
another rate limit right so uh rate by
IP rate limit by capture and sometime
you do have to provide some personal
information uh your phone number your
email address social security number and
all of that um so in the case of of waku
we are trying to build privacy and
Anonymous censorship resistant um
infrastructure and of course so we want
it to be decentralized for that so don't
really want to collect people's phone
numbers to allow them to have a
membership and that's why we use a Smart
contract so now in term of smart
contract um I think there is many ways
to do it right so we are currently
looking at pure Financial
solution um but that's just like one
example that get us going without making
too many assumption but you could
definitely have things such as um
actually I would mention that at the end
all right so economics so we we now
assume we going to make people pay to
buy membership so we went for for six
month membership when you have to buy a
membership and it's valid for six months
and the end of six months you have a one
month Quest
period at the moment we went for a
linear price all right so we say okay
let's pay 5 Cent per message per EPO for
your limit so if you go and buy the
lowest membership which is 20 message
per 10 minutes you pay $1 and if you
went for the highest rate limit uh you
pay $30 in term of gas cost so um I
think about demonstration was using a
contract that didn't have yet the
economics in there so now actually we
just look at the test and it's around
um gas uh to insert the membership on
the smart contract with the economics in
there which is around $10 Manet um which
is you know for 6 months it's not the
end of the world um looking at a2s you
will be more like around 70 cents of
course depending on the to and the
current gas
price so at the end of 6 months the
membership can be extended during the gr
period um at this point in time we are
not trying to look in money like to make
money from that so it's a deposit all
right so at the end if you want to
extend your membership you just close
the contract you're going to pay gas to
cose the contract but you don't need to
to put more deposit
in um and if you want you can also
withdraw uh your deposit during the
grass period during uh after the grass
period um the if if if people just inert
membership and they just leave it there
as I mentioned there is a rate a global
rate limit on Smart contract right so
smart contract will not accept uh
membership above a given limit which was
no more space in the merket tree then a
Coler can override expir membership in
there so that if people don't Rue um we
don't have to ex to extend the
membership on the contract we can just
uh Coler can just
override uh a quick mention so we do
have you know cap on the number r on the
contract what happen if we have a
network with that many users right as we
mentioned we do split the traffic in
eight shards so the idea is that if we
end up at a point where the smart
contract is full and we do see this
traffic on the network then it's always
possible to potentially deploy new smart
contract or maybe modify the current one
um exchange some parameters and add new
shards and to add new shards is just a
consensus between operators so just
saying okay operators let's have a new
Shard on the network maybe a new smart
contract with a higher rate limit so
that we can scale the network and get
more users
in cool so all right so that's that's
the current um uh the current status we
we have we are still refining the smart
contract more or less ready um we we try
to deploy it on Manet very soon probing
an audit first in terms of um of the
future so we went for six months
membership probably we can do one year
membership but it's still quite early on
and we didn't want to know look in
parameters and having to try to get
people to migrate if we change things
drastically but most likely uh a yearly
members we make more sense um at the
moment we have linear pricing right
so um you know 5 Cent per per message
per Epoch we could have nonlinear
pricing so actually we already prepare
the smart contract for that so that for
example you could have a bug discount uh
if you go on the higher end or on the on
the contrary force uh try to make it
more expensive to have a higher right
limit um now we need to basically get it
used so we can get some feedback one of
the change
so the reason W was bat was for the
status chat app which is a chat
application both mobile and desktop uh
new version 231 just released so go give
it a go um so right now the next step to
have rln um used is um for us to get it
in the status chat app and the main
challenge here is to look at the crown
chat protocol and understand what would
be the impact to uh to reduce to rate
limit know to add this uh this hard rate
limit
all right so another point is that you
know especially when you think about
chat
application um I know WhatsApp used to
cost $1 a year long time ago I don't
know if you remember that is it sounds
it sounds you know okay um anyone you
know anyone project developer that wants
to buid on waku and want to take
advantage of this decentralized
peer-to-peer Network might say I don't
want my user to pay and to do own ch
transaction before they can use
application which is which is a fair
command so we we have considered having
you know message going for free on the
network but it would just makes the
network more
unreliable so instead we you know how do
we question like how do we how can we
offer a free membership to users which
is counterproductive right because again
it is a right limit to avoid people
floing network but there are some
options so one t option is test
commitment so State commment all you to
have someone else in certain membership
for you and revealing very little
information about your uh your own
membership um could use pay Master right
so if you um if you look at you know at
Layer Two uh you could deploy a pay
Master to say all right if someone try
to iner membership and they have some
unchain history for they already they
already bought enss name or they do have
some e or they have some specific token
that uh you are interested in to related
to your project you could say okay this
user has onch activity they're already
part of my ecosystem uh when they go and
try to buy membership I will pay the gas
pay the fee for
them I a referral system so one one I
think very interesting one is um at the
end of the day you you just have to
enter specific no specific number in
smart contract like the P key and there
is way to do that as well without ring
too much about it so you could have a
referral system where someone that is
already uh already has an wallet already
has gas is to pay gas uh could insert
the membership for someone else uh again
once the membership is inserted you
don't have to do anything onchain
anymore all you have to do is do some uh
calls on the contract to get mer proof
to get um your your index and then you
can generate proof and publish on the on
on the Wu Network
all right so that's that's the most part
for the presentation part um any
questions
on cost and
membership don't be
shy or Crystal
Clear ah yes
Q&amp;A are are you doing it or
all right awesome questions awesome love
question if you're not closes often do
you need to reink every time before
sending no you so you do not need to
reink messages per se before sending at
least as the writing layer okay so um
you if you miss messages from the
network then you miss messages and then
it just depend on what is your
application and in this case um
um and then it's up to your application
if your application is a chat
application then maybe you will want to
retrieve messages because there are chat
messages you're intering in in term of
the smart
contract when you uh when you restart
you you do need to um to check the
latest Market proof from a smart
contract because you do need to have the
latest Market proof uh to generate the
proof right if you use an old M proof
the new message may may be rejected so
you do have to uh recall smart contract
to double check um what to to get the
latest Market proof and you do have to
watch the smart contract as well right
because every time someone inserts a new
membership the market proof change uh
sorry the market route change and hence
you have to have a new market proof uh
you have to use a new market proof to
generate to proof locally so you don't
need to do a big reing per
se first question done is a deposit
necessary since the transaction is
needed anyway wouldn't just a gas paid
be in a friction yes no that's a good
point um it's a good point especially on
menet where it does cost uh some money
to uh to interact with smart
contract however the the here question
is about security assumption right so
how much should people pay to get a
membership and send on the on the
network uh that's not something that
that's something that we know we have
some theory around it but we need to see
practically what happened um and most
likely you want you prefer to you know
use the L2 so thing can go faster like
most application more and more are using
l2s and on L2 it's very very cheap and
hence you know question become smooth um
so because our aim is to deploy L2 and
we deploy we develop this uh this
strategy if indeed someone wants to use
rln on the L1 they might decide that the
gas cost is enough and that's no fair
enough so I think rep this one is there
way to pay the membership for another
user SL account as a way to onboard web
to users for example yes absolutely so
um so buying a membership you you just
interacting with a smart contract right
and you are sending just sending a a
commitment right so you're just sending
a number to the smart contract um with
the payment to have the rate limit so
you you can get this number directly
from your um
uh from your from your friend and then
do the SMART contract call for them all
right as long as they know to check the
smart contract they don't have to pay
gas and with test commitment you can
also have a bit more privacy around this
this action so yes absolutely you can
onboard other users um and and pay their
gas fees and their membership
fee are you considering limiting by n
megabyte per Epoch rather than messages
count per Epoch so so yes we actually uh
we actually thought about that I we to
look into that uh if I remember
correctly and I'm looking at my uh
researcher yes or no uh is that it just
it just makees it more complex much much
more complex right it makes it much more
complex uh so that's why we instead
instead we went for message count and we
uh I think our vory right would help for
that as well or am I confusing maybe
okay so yeah it's much much more complex
uh so instead we we have an like
agreement between not operator of the
message size so that they can decide to
drop messages which are too big from the
network and and you have the message
counts on the smart
contract is there can you scroll down
please I think I rep all these questions
I think there was there's more yeah
scroll down a bit more scroll
down yeah okay are there any more use
cases that can be applied with r yeah AB
absolutely absolutely um so again you
know RNN comes from the privacy and
scaling um exploration uh group from
from EF so at the end of the day with RN
is you you you rate limit the number
valid proof you can generate for a given
number you know in our case number is an
Epoch and we use that uh so as a time
stamp right but um let's say you could
do uh voting right you could have a
proposal the number is
the number is a proposal number and and
you can say okay only we can do one vote
per uh uh per membership and and you
could vote in a Anonymous manner um I
haven't looked lately about R
applications but yeah it can definitely
be used for other applications how we
consider R RIS taking to secure this
instead of introducing a new token
economy
do yeah
answer
so yeah that's an interesting question
we haven't we haven't that's the short
but could be interesting
actually there you
go would upgrading from rv2 to V3 in the
future be a breaking change that would
make nodes on the previous versions not
work with the new ones okay so first not
sure we would ever upgrade to V3 but in
any case um it it is a consensus right
so in short you you when you run a
gossip sub node all right you are going
to have rules to validate messages and
any everyone needs to have the same rule
because otherwise uh you get spam and
you're going to say okay this guy
sending spam so I'm going to disconnect
from him um so whenever you want to
upgrade Network and change a smart
contract there are several ways to do it
you can just start to point to the new
contract and you're going to disconnect
people that still pointing to old
contract and connect to people pointing
to the new contract uh you could have
and I think that's basically like the
main the main strategy here um because
as soon as you I mean you you could have
strategy as well where you um where you
say okay from this point you know from
this time stamp or this from this block
we are going to start considering
messages valid from a new contract or
from a different contract so it is
somewhat of breaking change but goip sub
does has uh safe healing properties
right so it would not last you know for
days and you have a hard fork or
anything as that um it would be more
about the question of having the gosip
sub peer scoring mechanism uh to to kick
off and and heal the
network can you scroll down please yeah
yeah all
right do we pay in e or some other token
how is it 30 USD paid yeah it was on the
slide but I didn't mention it so at the
moment so
erc20 token all right um this is a
parameter of a smart contract so when
you deploy the smart contract you can
decide uh which s20 token you want to
use um in our case we thought it was
important to use a stable coin so we
went for D because we are know
decentralization Maxi so we went for a
decentralized coin so we we suggest to
use D but it is a parameter of smart
contract and you can just choose
whatever you want when you deploy it
potential way can feed the tree with
membership very quickly is there way to
mitigate
it I I'm I'm remembering the discussion
we had quite a few discussion on that so
yeah at the end of the day a whale could
come in and fing the tree and this is
one of the reason um I think expire is
very important right because if they do
um then we have to cost enough that to
do it again and again and again so in
term of security at the end of the day
um any security problem the question is
what is the you know what is the cost
opportunity um versus what could you
gain right um quite early stage here so
someone would do that it would be just
quite annoying but we just deploy a new
smart contract and just get the notator
to to point to the new smart contract we
we did we did think as well about um
limit like you know saying okay one
membership per ACM address for example
per wallet right but this could be U
could still go around by just you know
dispatching your your mon wallet so I I
think at the end of the day expir does
play there I wonder if
um Serge has more to say about
that was the W problem no okay it is a
fair it is a fair command this is a fair
command
okay I think no more question more
question from
here awesome anyone has tried the enaku
compose all right now do you want some
help is it working or you try it in the
past you need some uh
some say yeah
is yeah we can we can help
so okay cool I think we can stop the
presentation for now and then we can
help anyone that wants some help or some
cool okay
good back
is this working it is great
back back back back back
this is for experts hi everyone thanks
for being here uh it was about a year
ago that I was at the solidity Summit in
Istanbul and
introducing the the work that was just
getting started to build a debugging
data format and so I figured it would be
appropriate to come back a year later
and report my progress and hopefully you
know disseminate information about what
I've been working on in hopes of getting
people to to adopt the
standard um I'm going to try and get to
the interesting technical stuff but
first I'll do some high level overview
and that's we'll we'll probably run out
of time but I'll make sure to leave room
for questions uh yeah just just to get
into kind of the the high level go over
you know what what is this project what
is it for why is it important uh making
debuggers is hard and brittle and it
takes a lot of guess workor like for I
don't know if you've ever looked at evm
bite code before but it is entirely
opaque and even and
so uh I mean of course this isn't a
problem just with ethereum and and smart
contract Computing environments but also
for traditional Computing environments
but on traditional Computing what they
do is they have the compilers provide
more
information and that has worked very
well since the ' 80s we have debuggers
debuggers even in the last 10 years are
are really quite impressive these days
uh but for smart contracts the the
question is a little bit less or it's a
little more non-trivial like what
information do you actually need the
compiler to output and how should that
information be structured for this like
our unique Computing
Paradigm so let me introduce the project
maybe not get ahead of myself so
ebug uh the ebug format is an effort to
build a debugging data format a
debugging data format is the term that
they use for the information that is
output by a compiler that enables
debuggers to exist at least to exist
without spending way too much money
building them so that's what the ebug
format seeks to achieve uh we are funded
by the EF right now we are uh proudly
part of the Argo Collective spin out uh
you should all go to stage two at 500
p.m.
to hear more about that that's the
last thing I'm going to shill apart from
my own work uh just I get this lot I put
on there we're not building that debug
is not building a debugger we're
building standards uh I yeah just we
might build a debugger in the future but
debuggers already exist I just want to
make it a little bit easier and cheaper
to build a debugger so who am I well I'm
Nick nice to meet you all thank you for
coming uh I'm the lead for the ebug
project I am a member of the Argo
Collective uh I have built a solidity
debugger and then I uh oversaw saw it
for 5 years and it is a
nightmare uh I have worked on projects
that are now ancient history and I just
kind of work in the dev tooling space
you know stuff interests me quite a bit
so just
to try and churn through these
non-technical things project goals yeah
we want to make a universal format I
don't want a solidity bugger only I want
a solidity debugger that is also a Viper
debugger that is also a feed debugger a
Hof debugger I you know and I don't just
want to Target the use case of I am a
software engineer that needs to figure
out why my code went wrong I think it is
also important that we target use cases
such as why did someone else's code go
wrong and lose a billion
dollars so things like auditing tools
analysis tools are very important and I
would lump them into that same kind of
category uh on that topic it's very
important for ethereum and smart
contract platforms that we target not
just like debugging in development but
as I'm sure you all can understand it is
extremely important to be able to
understand why a billion dollars
disappears because of software so that's
you a little bit more challenging than
your your G debugger and and your your
local build of your your C project or
what have you um and because this stuff
is hard
it's clear to me that we we have to make
it a goal to really
optimize for adoption right I'm I have
the solidity team in the room here
supporting me in this talk and I feel
very bad for the work that they will
have to do to support a project like the
eth debug format and on the debugger
side it is only marginally easier but
again it is orders of magnitude cheaper
and simpler to take an approach like the
one we want than debugging today
ultimately right the idea is we want to
lower the cost of understanding the
blockchain right we want it to you look
at the evm and understand what's going
on or or have like a dozen tools to
choose from that are all reliable and
and are well architected right like this
is a future that would be nice it's a
future that or it's like a present
unlike your x86 architectures with your
traditional languages and so I I hope
that we can move in that direction for
smart
contracts so this is
a a series of steps that I have followed
many times and I would imagine that a
significant number of the people in this
room have also done this where they need
to understand how solidity Works some
like strange feature like how the
mappings get stored in solidity or
strings or or what have you and and you
know many times the documentation is
thorough and many times it is like even
the solidity Engineers don't exactly
know how modifiers work all the time
stuff like that it's quite bizarre so
what do you do if you're trying to do
some blockchain like smart contract
analysis well you sit down with salce
and a bunch of input examples and you
compare it to the output examples and
you scratch your head head and you think
is this how solidity does it I think
this is how solidity does it and then
you go and you write your code and you
you implement it and you you start like
slurping blockchain transactions and
figuring out what's going on and then
you realize that oh actually in 0.8.6
there was a change but turns out I was
just wrong actually also and then you go
back and you spend another few weeks
trying to make sense of how solidity
behaves and how your implementation
should behave and you know this is kind
of annoying because people do these
steps for the exact same problem
like finding strings in
storage like many people have done that
same thing and why why why do you have
to repeat the
work so also that's just solidity people
don't even try to the same degree with
Viper like like yeah there are some
Viper tools but like people spend a lot
of time like I would argue wasting time
making sense of solidity and there just
isn't that for Viper but you know Viper
also is responsible for billions of
dollars of assets so I I think this is a
pretty significant concern that we we
cannot
ignore uh here's an example this one's
at least documented uh like the the
solidity docs are quite clear on how
this works but it's still very bizarre
yeah uh solidity has two different ways
of storing strings if the string fits in
word if it goes if it's longer than 31
bytes it goes into at least one word and
then then you know at least two words
and they're those words are not
consecutive right so like in the the
first example it's what I have slot zero
and then the second example is slot one
followed by a a catch a cash and then
you start counting you know incrementing
at using the catch cach this is very
weird uh how does it work well that last
bite at the end tells us two things it
tells us the length of the string and
whether or not that length is longer
than 31 bites and well the the second
point is whether or not it's odd or even
I mean I don't necessarily need to go
into the examples you can look this up
in the The Docks or you can see the gist
uh but it's weird this is and this is
not the only weird thing that evm
languages do so how do you accommodate
that when you know the the last 30 40
Years of De debugger development has
assumed that people are organizing data
structures with like normal ways of
organizing data structures well we don't
have that privilege so here we
are shall we get into
it uh here's kind of the model that
we've been working with right is like
there there's there's ebug format and
there are compilers and debuggers and
there's some interaction between the
three and uh I won't assume that the
people in this room all know how
compilers work so you can imagine well
there's a source code that goes into the
compiler in a highle language and there
is machine code that comes out of the
compiler in a low-l language and in
between there is a long pipeline of many
different steps uh some very complex
some straightforward uh the compiler
does things like when you make a
function call and the compiler has to
convert that function call into machine
code it well it generates at least two
jumps you know one jump to enter the
function one jump to
leave uh or if you are storing a struct
or an array the compiler has to take
your single assignment statement and
converted into a series of like
individual word
assignments uh and in order to you know
what you're left with if you're looking
at the evm like the raw running evm is
you don't necessarily see any way to
translate back right who knows it's you
just moved a word I don't know if it's
part of a struct assignment or what uh
but if the compiler were able to keep
track of every single transformation as
it performs it right oh I i' have to
convert a function call into a series of
jumps
well if you annotate those jumps to say
this was the start of the function call
this is the return of the function well
and manage if the compiler can manage to
preserve that information all the way to
the the end of the compilation Pipeline
and produce like a nice Json object well
then the debugger debugger can read that
information observe the running uh state
of the evm and basically see oh we're
executing this instruction what has the
compiler told me about this instruction
oh it is a jump that is part of a
function call so with that debuggers can
actually make sense like a coherent
mental
model of like the this like fictional
highle world that is lost once the
compiler is done uh and the idea is
hopefully this should be sufficient for
debugging missing billions of dollars in
optimized
code uh we do have
challenges uh the the first significant
challenge that has been on our mind is
the fact that when you debug something
you are debugging runtime and
unfortunately the compiler is not
capable of predicting the future and
knowing what runtime will be so like if
you want to allocate an array in memory
you have to put it in memory where does
it go the compiler cannot guess what
address in memory that array will have
at compile time because maybe you are
allocating five arrays or n arrays so
we are limited in that the compiler can
only know so
much and there are these gaps that like
we have to take these like runtime
observations like okay how do I take the
the the running evm pair it with this
compile time information and produce a a
cogent model of the highle
world that one's not too bad maybe of
course optimizers make it even more
complicated right when you have
techniques like bite code D duplication
right I mean optimizers are very
important for smart contracts because
you have to pay for every operation and
it is significantly more expensive than
than most
computers
uh so you know you might look if you're
writing a compiler you might be tempted
to say well oh this this series of of
source instructions like this source
code is very similar in its output to
this other part of the source code so
maybe I can reuse the bite code for
those two same pie like the two
different Source ranges that
like you know maybe they're in two
different files maybe they're in two
different functions whatever but they
would produce the same exact bite code
and the compiler would jump into that
bite code in either situation so how do
annotate the this like lowlevel
information suddenly you're going from
well this instruction didn't necessarily
just come from here it came from either
here or here so we are effectively stuck
with this like
disambiguation situation where we
debugger will not be able to necessarily
understand with full
Precision like what what the debug
information is saying but the goal is to
uh ensure at least accuracy with that
like maybe we can't be fully precise but
we we can at least Target not being
wrong and so it's like hopefully if you
have a a block of bite code that
corresponds to two different originating
sources you the debugger will have other
information in its internal state to be
able to say oh okay well I know that we
were in this state
so we must be following this code path
and then another time we are in this
state we must be following the other
code
path uh what do we have so far uh well
we have a bunch of Json schemas I would
estimate probably about 60% of our like
working data model is implemented in
schemas and the 40% is is a lot left but
at least we you know have been working
pretty hard on it like we have examples
for every schema those examples are all
tested you know I don't want to have to
fix things that I didn't realize were
broken in the future right um and on the
opt like the adoption concern I do want
people to use this format I'm glad
you're all in this room listening to me
because maybe I will convince you to to
go and implement this
uh if you do there are explainer
document like uh documentation sets for
all of the
schemas and we have right now at least
one reference implementation for what is
the most uh tricky schema so far but the
idea is that I think it's very important
that we build reference implementations
for all of the schemas hopefully on both
the debugger side and the compiler side
so if you're maybe you're inventing a
new language or something and you can
just you go to the ebug website and and
see okay this is how an example compiler
might implement this stuff I will copy
that or I'm building a debugger I go on
the website I see oh this is how a
debugger might implement this technique
and you know I really just want to make
this as easy as
possible these are the the schemas that
are furthest along um oh I'm running out
of time all right well I'll have to run
through it so we have a program schema
which represents a single piece of bite
code and it's structured as uh a list of
instructions with annotations for each
instruction uh we have a type schema for
describing variable types hopefully
that's self-explanatory and then uh the
most complex complete schema so far is
uh the pointer schema which is to
describe data allocation
strategies uh from a highle language and
I'll go into a bit more detail on those
so the program schema here if you want
the direct link to the the explainer
documentation for that uh this this
scheme is quite incomplete but uh the
foundation is there
already uh the key concepts of the
program schema or it's one program is
one bite code programs have a list of
instructions
instruction annotations those
annotations allow the debug like
describe a high level context and allow
the debugger to basically have a lookup
table when it reaches an instruction in
the bite code it can go and consult the
debug data and see what is happening
with
that um ultimately informing the high
level
State this is uh an example if you want
to see so it's like the offsets the
program counter I think with the they're
not really calling it program counter or
it means something different so I just
called it Offset you can see the
operation that that instruction is doing
you might recognize this as the start of
every single solidity contract uh in
this in this example case I also added
uh a source range so you can kind of see
oh this is where this is the
corresponding line of code and uh it
looks like in this example we already
have a storage variable available to us
so that's like got the first instruction
we can read X which is of type string
and it's in storage slot zero I'll get
into the type and pointer schemas uh two
slides probably first I have to give you
this warning yeah we haven't tested a
lot of our assumptions here just full
disclosure but we we think it's viable
but stay tuned you might see me very
happy or sad next
evcon all right the type scheme is
pretty
straightforward uh you know you have to
just describe types so we got known and
unknown types like there's like uin
strings like all the normal ones are
supported by the format but we also
allow compilers to Define custom typ if
they have you know some Advanced type
systems uh from there types are divided
into either Elementary or complex uh we
do need algebraic types but they don't
exist yet in this schema uh Elementary
types are just like a single thing and
complex types contain at least one other
type uh types you know to D duplicate
representations like there's a lot of
data that we're talking about uh we
allow types to be referenced by ID if
you don't want to just copy long
descriptions of arrays or structs over
and over you can just give them an ID uh
and of course if it's a user defined
type it it can point back to the
originating
Source here's a couple examples it's
straightforward uh on the left is an
elementary type for a fix Point number
and then we have an array of uent as a
complex type there's more examples on
the the website if you want to find them
um but this is really what I want to
talk about is the pointer schema because
this is uh uh I don't know I think quite
interesting and suggests that this
approach might be viable so we need
to represent where variables
live oh I should probably get this over
with yeah
so yeah I mean you guys can probably
just go unless you like this kind of
insanity then please stay uh but yeah so
we kind of put uh Lambda calculus in
Json schema and that's because of the
compile time constraint
uh which is you know the compiler
doesn't know where something's going to
be before it
exists um right so uh basically you we
get uh an expression syntax with the
schema to
describe like where is that string
storage how do I know based on the state
of the machine whether or not the string
is short or long let me show you an
example
see oh yeah here here's the example
actually
yeah uh don't look at the slide just
grab the QR code I I did document this
there are comments there uh but you can
kind of see at the very top this this
string
storage uh Al this this pointer starts
with a storage slot slot zero and then
we have a group of other data regions
and variables I mean I'm really running
out of time maybe I'll just supposed to
ask for questions now uh but you can you
can see is there a laser pointer on this
well I could just
point I really
can't uh so so you have you have groups
of basically the way the pointer scheme
works is you have regions and
collections regions are a single like
continuous range of bites and then
collections are this like abstract thing
you can have groups of regions you can
name the regions so you can have
conditionals so you can do things like
check the remainder is it odd is it even
if it's even we know it's a short string
so do this otherwise we know it's a long
string so do
that remember the example from before
great all right I swear it's less bad
than you think I mean the idea is that
these are actually static
representations so the compiler will
only need to Output this once
fortunately you know and then instead of
zero it would just be a template
variable and then the compiler can say
use this pointer with this variable in
place of uh string storage contract
variable slot and this way you know any
supporting compiler can just output like
have a library of these template these
pointer templates and just output them
whenever they're
necessary uh and if they're not
necessary it can omit
them uh yeah apprehensive but we tested
it end to end I like I put a string into
a solidity contract in an automated test
and I step through the evm and I observe
after every string assignment that the
value changes and matches the
expectation so if you want to see how it
works you can look at the uh the
implementation guide hopefully it's
coherent all
right anyway there's a lot of work to be
done um feeling very good about it you
know I think I think this is a solvable
problem if you want to learn more please
join our Matrix chat we meet every other
week you're welcome to join the calls uh
you can also just watch the repo
we got questions yeah thank you uh
exclude the optimizer yeah so that's the
approach we're taking uh will these get
recorded I should probably repeat them
uh the question is can we exclude the
optimizer and just focus the debugger at
compiler level Optimizer should not be
alterating code functionality
unfortunately I think it does alter the
code functionality but the approach that
we've been taking so far is to start
with just unoptimized code uh while
thinking about you know how what do we
do about the optimizer and making sure
that we're not painting ourselves into a
corner
uh when we do want to support optimize
code when is ebug format done
I after
Devcon others this is so impersonal
biggest blocker uh I mean the the the
tricky thing with some with work like
this is that it's
periods of challenging like thinking
figuring out like how can I make this
meet the
requirements followed by months of
tediously documenting and so it's like
there could be blockers in you know
either of those and and the different in
both situations the blockers are are
quite different uh can the debugger
identify the function arguments if the
format is followed yes that is the idea
right so uh if I didn't have only a
you all with way more examples they are
on the web site you you can kind of see
um if you look at the program schema I
actually handcrafted a pretend highle
language source and the corresponding op
code output so you you can kind of take
a look at at what that looks like
um how do I scroll
down is there looks like there's
uh any plans on decompile decompiling
deploy by code with no original Source I
mean this is a cool thing it's not
really what I've my area uh I know there
are decompilers that exist I I just
haven't you know thought about that too
much oh any
more well thank you for your time
everybody
let
hello welcome thank you for coming by uh
this is Lucas and and I'm Connor and
we're here from the base team uh the
smart wallet specifically and we're here
to talk about this new feature we're
launching soon called spend
permissions so spend permissions oh that
title got messed up sorry uh spend
permissions allow you to create oneclick
or no click experiences that can spend
users tokens this is important because
we all want better ux within web 3 it's
kind of annoying to have popups all the
time when you're doing a
transaction and so with spend
permissions you're able to give
permission to an app to spend your
tokens so that the app can do fancy
transactions to pull your assets and
then do fun things with them and this
Workshop is going to show you one of
those things is a social app few minutes
talk about our road map when we're
launching this and when you can get
started building and then we're going to
talk about some fundamentals this is
where the workshop actually begins we'll
be doing some live coding and you can
Fork our starter repo and then we'll
also going to be finishing with an nft
micro payment use case at the very
end so for those of you not familiar
with smart wallet it is a smart contract
account that has self custodial pass
keys this means that users can easily
onboard if they have a device that
supports pass Keys which is most people
in this room you can scan with face ID
if you have iOS or thumb prints if you
have uh your computer or your phone with
a thumbprint Scanner with smart wallet
you can also sponsor gas for
transactions so users can convert easier
and not have to fill up their wallet to
get started and you can also batch
transactions to make it easier for
people to do things with lesseps but one
of the problems we've encountered with
smart wallet and all wallets in general
is that there's still too much friction
to transact people really are addicted
to one-click experiences like we have in
web 2 so there are two ways that we've
actually explored doing these one-click
experiences and session Keys is where we
actually started and it's this idea that
you can give permissions to apps to
transact as you and so literally the
popular way people implement this is
they can take control over your account
to call other contracts and it's
incredibly flexible but after exploring
the steeper we realized that this
actually has some security discomfort
for us and we don't want to let apps
call random contracts on our behalf even
if we inform the user what's being
called and what functions we just don't
believe that users are informed enough
to give approval to those uh kinds of
permissions and so that's what brought
us to spend permissions it's a way of
tightening the scope of what we allow
apps to do on behalf of our accounts and
it's focused only on spending assets we
think that spending assets is actually
the majority of the reasons apps need to
interact with accounts and after an app
has assets from the user it can then do
things like mint nfts swap tokens
staking on defi whatever you need uh and
in this sense we actually feel way more
conf confident with the security posture
of spend only permissions and you can
still solve a majority of the things we
care
about so what are the use cases we think
people want to build with uh the first
which we'll demo today is
microtransactions these are
highfrequency interactions that you want
users on your app because they're high
frequency it's naturally very annoying
if you have a popup every single time
and so use cases like this in Social
would be Azora app where it's basically
Instagram but instead of liking you're
collecting nfts you may be liking all
the time other micr transaction examples
would be gaming very high frequency
people want to go through many
operations uh for a game potentially and
do it quickly and so before you would
have a popup every time but now you can
just give permission once to spend some
eth or an ec20 and then whenever you
click a button or do something in the
background it's just going and
transacting without you noticing the
Second Use case we're really excited
about is subscriptions this is an
example of a pattern where users don't
have to be on the app anymore and this
is where permissions really shine and
you can do things uniquely that we
couldn't do before with wallets and so
in a subscription case you will give
your app permission to spend your tokens
on some recurring basis and then even
when you're outside the app it'll just
pull money from your wallet no pressure
needed and so in this case uh
subscriptions are not the only
background process you need to do um
other background operations could be
automated trading copy trading things
that are more defin native also shine
very nicely with background transactions
but these are the two that we think are
most relevant uh
immediately so how does this actually
work so this is a sample diagram of what
onchain looks like and typically a smart
wallet we think of having one or a few
pasy owners and so you can see the smart
wallet contract in the bottom left it
has an owner relationship to a pasy and
we typically reference that pasy by its
public key so 64 bytes smart wallet also
supports owners that can be ethereum
addresses which include smart contracts
and so for the spend permission system
we're actually adding a new contract as
an owner to Smart wallets called the
permission manager and through this
ownership system we're able to delegate
other permission to Spenders and so you
can see the spender relationship between
our permission manager and a spender
entity which is itself another ethereum
address and so once you have this
ownership relation relationship set up
the flow of a transaction looks a bit
different than normal so originally
transactions for session Keys originate
from the smart Wallet account but this
time a spender is calling through the
permission manager to spend some tokens
and then the permission manager being an
owner is able to call execute on the
smart wallet to get it to call anything
it wants in this case we want to call
the smart wallet to transfer some value
and in this case back to the spender and
so
yeah and so how do you actually use this
offchain to the first thing we need to
do is approve a permission from the user
we do this with eth sign type data it's
using EIP 712 signatures we chose this
path because it's the easiest way to ask
the user for a signature of structured
data um before we were working on a
standard called IRC 7715 we felt that
start but we're still open to working
with 7715 in the future but the user
sees a very simple approval here where
the app is just asking them to allow to
spend some currency on a recurring basis
in this case 10 usdc every month could
be a very simple transaction um
subscription experience and we also have
a start and end time so in most cases
you'll want the start time to be right
now and the XBR to be some sometime in
the future the apps we've been talking
to typically want the xre to actually be
infinite which is something we think is
interesting where users would have to
revoke if they ever want to remove the
permission but that's up to every app to
decide for
themselves after the users approved a
permission and then therefore signed it
with their Pass Key the signature is
given back to the app and now the app
can use that signature to apply it as an
approval onchain and that's that first
optional call in the top after a spender
has approved the permission with the
signature from the user it's able to
spend and so then that's number two on
this diagram where the spender is
calling into the permission manager to
use the permission the permission
manager will then validate it call
execute on the smart wallet and
depending on if you're using native
token or erc20 token the smart wallet
will either call directly back to the
spender to transfer eth or call the
erc20 uh contract with the transfer
function to send the
tokens the third piece here is revoking
it's very important that users are
always able to revoke permissions after
they've approved them this is
fortunately a way we can actually
differentiate from trafi and the
existing world because it's very
frustrating that you can subscribe to an
app but not easily unsubscribe a lot of
apps make it very difficult but we
believe that in the new world users
should always have control of their
assets and have control over their
permissions so permission management is
always easily accessible within their
smart wallet settings and we also went
through the effort of making uh revoking
an entire app permissions in case you
have multiple easier with a Boke as
well so when can people start building
with this well as of today we have well
as of last week we have um Bas AOA
supporting Ethan
ec2s and in December preferably at the
start of the month we're going to have
this live on Main net um on all main
Nets that smart wallet supports right
now that includes Bas arbitrum op Zora
eth main net and a handful of other
chains that are less used right now but
also in December we're exploring ways of
doing batch permission approval so ways
for a subscription for example that you
can both pay now but also give
permission for the app to take your
money later which is a more typical
experience that we have with permissions
um for subscriptions and then in 2025
the road map is still pretty open we're
open to user feedback developer feedback
on how we can improve spend permissions
and build other systems that complement
it cool well that's the brief overview
of how the system works Lucas is going
to take over and give a sample Workshop
of our basic demo app um you can open
this on your computer it's github.com
luucas Rosario um SLS spend permissions
demo we'll leave this open for a moment
for people to pull
up and also before continuing are there
any questions about the overall idea or
setup of spend
permissions yeah what's the difference
between batching
transactions what's the difference
between uh batching transactions and uh
having like a spend limit uh for let's
say you have a $10 spend limit or $20
spend limit for the entire month uh I'm
trying to understand oh of that last
point I had of batching permission
approval yeah that one yeah so right now
when you approve a spend permission
you're just signing a 712 object and
nothing's actually happening on chain
and so an app could use that um that
permission and immediately start
applying it to pull money from you uh so
the batching permission approval idea is
that you can use a transaction based
approval and then therefore batch other
operations with it so I could transfer
ec2s directly to the app and then also
give it permission starting next month
to withdraw my tokens so it just makes
the ux a little bit easier for the app
is it like let's say approved
transaction as well as like swap
transaction bat in a single transaction
and then you approve that corre is that
oh yeah yeah and there are other ways
we're also exploring batching where you
could sign you could still do the 712
path and sign over multiple tokens at
once um so a use case for this would be
gaming we've know we've talked with
ctown and they actually need eth and
kibble which is an erc20 because they
use the kibble to fish but they need the
eth for chain link vfp and so we'd still
want to provide an easy way for users to
sign once and approve multiple
permissions at the same time so that's
the other pattern of batching
yeah another question actually like I
already implemented the spend
permissions in my app like where I buil
an session Keys based uh prediction
markets where users just swipe left and
right for their action and the app it
does the whole thing under the hood
using the session keys and spend
permissions like each transaction is
an allowance of 0.18 every day and we
automatically abstract for 0.018 so the
issue we occurred was like regarding the
finality of the transaction like how
does it occur like uh sometimes the
transactions May Fail but we show the
user like the transaction is succeeded
because of the finality
issues so if I understand the question
you have an app already on spend
permissions yes you you have a daily
refresh cycle and then you're using the
money to do some prediction Market use
case and some of the time the
transactions are failing yes and yeah we
should talk after then yeah okay thank
you yeah I can help debug later
yeah cool well I want to hand it over
Lucas now we'll take more questions
throughout as
well cool uh yeah so again this code uh
that I'm about to be showing is
available at this repo um first I'll
just demo the app real quick uh so yeah
this is a super simple app this was spun
up with uh onchain kit and I have a
smart wallet connected here and I can C
I can click the Subscribe button and
what this does uh this pulls up the 712
message to sign that Connor was talking
about uh that describes the parameters
of the spend permission so you can see
uh the limit per day uh is a lot uh
starts on like forever ago uh not sure
what that's about uh and it's on Bas
aoia um so I can sign over this and
again this is offchain so it doesn't
cost any money uh or or gas to uh
approve a spend permission so I can sign
this and then this signature is going to
get shipped off to this app's backend um
who can then use uh the signature along
with the the parameters of the spend
permission to start um pulling funds
from uh my account so that's what these
are these are all uh Ops that are
landing on
chain um yeah so like every 5 Seconds
the app will pull the back end to tell
uh the apps like spending key to pull
funds from the the user's account uh so
that's like the short demo and again
this is we're excited about this for
like subscriptions and this could show
like uh this is kind of like a streaming
payments kind of use case uh that I
think could also be really cool uh so we
can go over the the code actually real
quick um so we can start with the the
front end piece here uh there's nothing
like super interesting here uh is this
big
enough maybe that's better um yeah so so
uh as mentioned this is just like a
regular 712 message uh the parameters
for these you can find on Smart wallet
uh dodev and there's a we have a guide
up on spend permissions now so you can
see exactly how these are uh
parameterized um so basically when the
user clicks this button uh we Define the
spend permission uh the account this is
the user's account the spender this is
my uh like if I'm an app this is the the
account that can pull F funds from a
user's account
um we have a spent permission for eth uh
for 10 a day um and this is the these
are the like recurring uh the recurring
parameters um and then we have some
extra Fields here which you can find
more about on Smart wallet.
uh so we
request a signature from the user and
then we uh make a request to the app's
backend uh with that signature and the
spend permission and we can go see what
that looks like um
so uh the account that we're using to
actually do the the withdrawing from the
user's account is a smart wallet
actually so so we wrap a private key uh
in a smart account and the reason we do
that is because uh it's it's easier to
do than like batching we can do atomic
batching um and uh we can also use pay
masters so when I was setting this demo
up I spent like 30 minutes trying to get
uh basoa eth and I actually just ended
up wrapping the account in a smart
account and using a pay master so that's
much easier um so you can see here we
have like a bundler a bundler client and
we send these calls to the permission
manager uh that's the contract con uh
Connor was was uh mentioning that's an
owner of the uh smart the user smart
accounts uh so we have an approve a
signature so this actually approves the
spend permission on chain which needs to
be done so that when the um when the
withdraw all calls get to the account uh
then the spend permission manager has
like a record that the user actually did
approve the spend permission and then we
have the spend call uh which is saying
hey I have the spend permission um given
that I want to withdraw uh 100 way uh
from this from this account and like I
mentioned we have this setup with a
smart account and a pay master so that I
don't have to think about gas uh this is
just going to be sponsored by uh by my
pay master and then return the hash to
the uh to the client so that we can see
that list of of withdrawals in this case
um and then we also have this other
simple route uh that uh does collection
um when the spend permissions already
pre-approved so you can save some gas
here uh by if the the permission the
spend permission has already been
approved on chain uh you you only need
to call spend uh to withdraw uh tokens
from the user's account and again using
Pay Master uh and then we return the
hash to the client and that's where we
get this uh this list of uh of hashes
and then we just render those hashes and
Link them out to a uh a block
Explorer uh so yeah again this is
available on uh this URL feel free to uh
just pull it down and and play around
with it and again we have a a guide
available on Smart wallet.
uh and that
goes into all the parameters of the
spend permissions uh and goes into more
detail um and you can find out more
about like use cases we're thinking
about there
any uh any questions about the
demo hi thanks I'm wondering is this uh
this pending permissions is creating a
session key right not no uh because
session key um we we're trying to be
very clear that spend permissions don't
allow you to arbitrarily execute for the
user's account uh in other words like
the the key the spender account is not
an owner of the user smart account it
just has the right to withdraw uh some
assets from the user's
account okay so it's a extremely scoped
uh uh key that can only spend assets of
the user's account yeah that's right and
that that goes to like the uh we we just
felt much better with the security model
there uh but you can pretty much get to
session key parody and just build like
you know if if you wanted to have some
State tied to the account you can
imagine in this back end having you know
some database set up that's like uh you
know I have this spend permission for
this account uh and I can just have my
state there and I don't need to execute
directly from the user's account uh and
I just I just need the assets which I
can do and so last question the
signature here is happening on the
client side yes the the user signs uh
over the uh the 712 message uh which
basically like gives the ability for the
the the apps spender to like pull funds
okay so at each spend is using the
signature that the user gave in order to
use the permission you actually don't
need the signature after you approve it
on chain so you just put a record into
the the manager contract that says
here's a signature for this spend
permission this is valid and then next
time when I want to pull funds I don't
need a signature again I say here's the
spend permission and there's a record of
that on chain that it was approved okay
thanks yeah
any other
questions so this will only work with
the coinbase smart
wallet uh currently yeah well there's
nothing stopping other wallets from
implementing this uh this feature but
you would need to have the owner added
as on your account what
else there it like here
too so maybe not
so the contract that we've written and
audited only works for coinbase smart
wallet however we wrote it in a way
that's easily forkable where other
people can just Implement override a
specific function of like what the
execute looks like on their smart wallet
so for example if you want to use I
guess like the I think probably like a
zero Dev 7579 account has a specific
execute function you can just Fork the
spend permission manager reimplement the
execute function whatever that interface
looks like and then everything else can
just work as work the same pretty much
so one thing oh no yeah one thing we are
exploring is if spend permissions needs
something like an ERC to make it easier
for apps to work with other Wallets on
this kind of feature uh We've held off
from doing that to make sure that the S
the design is actually sane
first um but that is something that
we're open to talking about and working
on okay yeah thank you
cool uh do you want to do your thing now
yeah uh if there are no other questions
uh Connor is going to show another demo
of how you can tie this into like a
social uh kind of app actually I think I
may just like Wing in on this
okay so do you want to plug in stay
actually want to take a chicken
yeah for
cool we are back all right so we're
going to do this like half live um we
want to show a more concrete example of
what it looks like to actually do
Advanced operation serice side with
spend permissions and
so what we're going to build is
effectively something like this where
your smart wallet has some money but we
want to withdraw that money and spend uh
to use some kind of operation and
so Lucas was showing how earlier we
could use a coinbase smart wallet server
side with a key that we can sign on
demand and with the smart wallet in the
server you gain two main things you can
use batch transactions which we're going
to show in this example and you can also
subsidize gas through pay masters to
make it easy to not have to worry about
topping up some random account you have
with enough gas to submit transactions
in an automated way and so for this
specific example we're going to work
with Zora's nfts uh that just go good
goto protocol for anything nft related
and incentive alignment with your
creators and for us the call Flow is
going to look something like this where
the entry point because it's a 4337
account is going to execute on our
server account which then has a server
key we'll be signing with to verify and
then we're going to do two calls and
batch them together the first call is
going to be spending on the smart wallet
which will prompt transferring some
assets into it and then the second call
is going to be minting to the actual
Zora nft we need to do the spend call
before we do the mint call because we
need eth to perform the mint the zor's
contracts will ensure that uh it will
only allow you to have the nft if you're
paying for it and the mint two um
emphasis on the two here a lot of
contracts out there allow you to Define
recipients for token related operations
and so in our case we're not going to be
minting back to the server account here
we're going to be minting the token
directly into the smart wallet itself
and by doing so we Pro create
effectively what a session key
experience is like with one click mints
where the user only has to approve the
permission to withdraw eth then whenever
they click the mint button they're going
to have the cloud account withdraw their
eth mint something and get it back in
atomically this kind of model can also
expand to other operations so for
example Dex trading on swaps uh the Unis
swap router allows you to define a mint
to like Behavior as well where you can
Define any number of recipients you want
for your tokens and so this is a case
we're actually exploring with the team
um Dracula where they support both swaps
in their app and nft mints and we're
working to move a um these operations to
the server so that you can batch
withdrawing money and buying something
and giving it back to the user and we
think this model can actually be
replicated across many other examples as
well and so what we want to do to start
is I have an nft collection on Zora I've
already done some sample mints uh in
anticipation for the demo but we have uh
this is just my pfp and we have a
contract address here and so what we're
doing let's make that
bigger cool
and so the first step here is rather
simple it's just the usual Grant
permissions
experience again you're just approving
some eth and then you can do
allow and then from here we have
my pfp this is the nft I'm going to be
minting and then when we click mint it
should be making a query to the server
to Mint the token which will then
pull the assets if we have the route up
here uh two calls that we need one is or
three calls rather so again we're
approving the permission with the
signature we only need to do this once
after we have this approved on chain we
actually don't need to apply the
signature anymore but then we're pairing
together both the spend uh of calling
the spend per manager to withdraw the
amount we need for the mint and then as
soon as we have that mint value back in
the spender client that we have we can
do a mint call and then the mint call
itself is going
to make a call to the Zora Minter
contract uh with the mint cost and some
data which then just takes a bunch of
stuff but really what we need to Define
is the recipient the nft contract we're
going to be minting on and the token ID
we need we want to
Mint and after we have all of this then
we get user op hash user op receipt and
return this back to the
client
so oh that's not supposed to happen
apologies
let's do a
live well this was working just before I
came back up unfortunately for
us but I have this pushed um a working
version of it
to a repo that if you go to smart
wallet.
we have all this documentation
here on spend permissions including a
basic overview the quick start that has
the sample experience Lucas just demote
as well and then within here if you go
the sorry this
one Zora
Branch you can access all of this code
here within the app and then we have a
mint route that is doing this kind of
API work
I'm curious from the crowd are there any
applications that people are Keen to
build with something like spend
permissions SL session
Keys yeah we are building a generative
art platform so ah so we are building
like a generative art platform so like
the idea could be that like you as a
collector you can like approve spending
and each time like new meets come it's
automatically minted on your behalf so
you don't need to wait in front of the
like minting button and refreshing the
page so that could be probably like idea
I would have like with this that's cool
so this is something where as soon as a
new token becomes available like on the
drop I can me yes yes yes exactly so we
have like weekly drops so users don't
need to wait like at for example 3 p.m.
they don't need to wait you see all the
mouses going around cuz we have like a
party kit so you see all the like
pointers so they are impatiently
clicking on the m and it becomes like
pink so yeah you approve your minting
and that's it so at 3 pm sharp you can
mean for everyone who approv the limit
yeah I love that be nice I I like how in
particular it helps people not be
perennially online and so this is a good
use case of like the back transactions
use case and we are already live on Bas
so happy to try it
on I love
it well we skipped most of the workshop
by having the code pre pushed because we
didn't want people to worry about typing
live with us so if people would like to
build something together we're here to
finish the rest of the workshop but
otherwise
I think we have most of the content that
we wanted to cover actually and then
leave the rest of it open-ended for what
people wanted to build
live so are is the batch Atomic or not
or how does it work uh the batching on
Smart wallet is atomic yeah it's only
Atomic nice
thanks um was the account you were using
to execute the Unis swap transaction in
the example an eoa account or is that
another smart
wallet in this one um the mint 2 or the
Unis swap yeah yeah the server account
what kind of account is that it could be
any account that supports batching so
for us we would just use the smart
wallet because we know those contracts
but you can use anything as well up
there cool yeah it also doesn't have to
be a 4337 account it could just be a
contract that supports batching so like
multi calling for
example who is the one that calls
execute on something like a server
account uh if it's a 4337 account it
would be the entry point because it's
what's validating that you are actually
you uh with your server key and so after
you validate your user op then it'll
submit a transaction or a call through
the server account to then execute
whatever batch you
have yeah another
question
cont yeah correct this entry point is
the 4337 entry point yeah and uh so you
guys created one more contract which is
the spend permission contract is uh 7528
I'm a little confused can you explain uh
like what exactly is uh happening in the
spend permission contract yeah what is
happening in spend permissions we can
actually look at the code to show you
some of the logic
apply It's relatively simple but when
you call spend on
it okay this actually is going to be
more complex than I was thinking so when
you do spend uh it's going to do to two
things is you want to validate all of
the internal logic of is this spending
the right token is it spending too much
of it for the current period um part of
the logic of spend permissions that's
different from something like permit 2
or normal erc20 approval is that there
is a natural refresh of the permission
over time and so when you have a
permission I guess from what Lucas
showed you earlier it was a typescript
object here's the solidity struct we
have uh this period value is actually
very important because it's what defines
how long you go before you reset to zero
so for a subscription example you would
want the period to be your billing cycle
so one month one year bi-weekly whatever
it may be uh for something like micro
microtransactions we've seen daily as
like the most common way to do this and
so what the spend permission manager
needs to enforce is that for the current
period have you spent more um have you
spent up to the allowance so if we go to
use spend
permission that's what it's trying to do
so we just make sure that it's approved
in some state that we have if if it's
already approved in state we look at
what is the current period is the total
spend for this period greater than what
the allowance should be and then if it
is it will fail and otherwise we can
update our last track spend for the
period and so we would take the total
spend and set it to the value save it
back in storage and then emit an event
that the spend permission has been used
and then after this we would actually
execute the ec20 or eth
transfer so you mentioned in the
beginning that uh we could focus uh uh
contract and then uh change something
what exactly was that oh okay that would
be this one the execute so the transfer
from uh is just a normal transfer of
either if it's native token it'll call
on the account to transfer value to the
recipient if it's an erc20 it'll call
the token contract itself with the
transfer function defining the recipient
in the value it's really this execute
internal that you can switch so for us
we just import the coin B smart wallet
interface and we call it it's execute
function so whatever account you have
you can just replace
this you have more you want to go
through yeah try to fix the
D yeah
actually maybe we can help devote his
thing as well red
sh I want to take a moment to see if I
can actually debug what was wrong with
this minting because it was working
momentarily
before I thought I commented back in
yeah that's
call we all have the Subscribe
case actually there is one more thing we
should probably touch on as well that
wasn't hit which is
people who want to build applications
that have a without without a database
hopefully that's like a lot of apps at
least many apps they can use the
blockchain as their database one thing
we've noticed is a need for providing
index data about how many permissions
have been used or how many permissions
does your app already have and so we've
created a new RPC wallet fetch
permissions that allows for that where
via API uh you can always ping to know
what permissions your spender actually
has and so you just provide the chain ID
you're asking for uh in this case it
only supports basic POA but soon
everything else um your spender address
that would be the server account and the
examples we've been giving and then what
you get returned back is an array of
these permissions and for each
permission you would have all the fields
and then the signature you need to apply
and for something like this you would
imagine a subscription would pull all of
the accounts I have permissions for on a
routine basis and then for each of them
prepare this massive batch call to call
spend
on all the users and so fetch
permissions is something that we're also
hesitant to go too deep into with
something like an ERC because we'd
rather make sure the interface makes
sense first through production
experience but patterns like this we
also see as important for building full
stack apps um kind of completing the
crud where you can create permissions
you also need an ability to read
permissions um soon we also need to add
an ability for you to update a
permission for example if you have a
subscription that's $10 a month but you
want to upgrade someone to Pro you need
to say would you like to upgrade you
were on 10 we're going to remove that
and only conditionally on removing it
will we add a new permission for $50 a
month um and then the final of delete we
already support revoking but also being
able to prompt a revoke from the appside
as well
cool uh yeah if there there are no other
questions I think we can end early here
but uh Connor and I will be around if
anyone wants to uh try out the repo or
just have has any questions about uh
spend permissions in general we're happy
to hang around and in
chat cool thank you
o back back
w w
back e
