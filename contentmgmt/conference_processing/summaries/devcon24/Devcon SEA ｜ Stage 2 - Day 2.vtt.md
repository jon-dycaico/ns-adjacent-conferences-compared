[Music]
a
oh
SC
you
come
[Laughter]
m oh
[Applause]
true
over
you all
oh o
she m
for
m
to
is
h
m a
the
oh m
sh
see oh
is e
w
go oh
good morning
everyone I hope you guys had a very
well-rested uh day one of Devcon I'm
sure that you guys all went to bed super
early um so uh today we're going to um
have a few talks on um core protocol
stuff and uh I want you to remember to
take any conver ation outside um the
bathrooms are down and to the right um
and there's going to be a QR code on the
screen uh for anybody to ask any
questions and so if you have questions
you can submit them during the talk and
then after the talk we'll go through the
most up uh upvoted questions um so first
up we have uh Han from nethermind who's
going to talk to us about State expiry
right cool so it's the first session so
I want to kick things off a little bit
of fun I'm going to give away 0.01 if to
whoever that remembers the first ever
Smart contract that they have
deployed you can raise up your hand if
you still remember the address okay I
actually expected a few but I didn't
expect like none but it's but it's okay
like I didn't remember the first ever
Smart contract that I deployed and
that's normal when we enter the space we
probably think that smart contracts are
cool we play around with a template or
two um deploy some um like fake token or
like nft contracts and just send some
test transactions yeah that's totally
fine but I just forget about it but the
thing is that the data is still there
right but you me and the rest of of the
ecosystem will likely never use it again
so why store it on chain so today what
I'm going to talk about is really I'm
going to go through the problems that we
have with State growth the proposed
solutions that we have with State aspir
and where we are HED next so here's
everything you need to know about State
aspir let's get
started first let's do a quick revisit
on state what does state mean on
ethereum is that state is represented by
a mer ped try npt so um we call first we
call it the state try in the Lea notes
of the state try we have all the account
objects so each account will contain
balance nons root hash and code hash and
if it's a contract account then it would
has its own storage trial as well it's
also an MPT and in the leaf notes of the
MPT of the storage trial will contain
the 32 bytes slot values right so this
is the overview of how state looks like
on ethereum let's zoom in a little bit
by focusing on individual account object
and Slot keys
so given an account address we can
actually Traverse from the root of the
state try down to the leaf note and we
will get the corresponding account
object right likewise for slot key um we
can Traverse from from the root Noe of
the storage try down to the leaf note
then we can get the corresponding slot
value So This Is How We Do the mapping
so really if we really zoom in and um
just be abstract right ethereum state is
really um consists of like a mappings of
um um series of mappings between
addresses and account objects and also
slot keys to slot values so these key
value PS you can really think of it as
the basic unit to measure State on
ethereum when started from Genesis um it
started with a small set of key value
pairs as the chain progresses as more
blocks are included you get more more
and more key value Pairs and the number
just keep increasing increasing and
increasing it will never stop because
state is unbounded and this phenomena is
called State growth right so this is the
problem that we are trying to solve
today but why is this the
problem to quote Peter from GFF ethereum
is slow because the state grows like
crazy what happens when the state side
grows is that the number of notes in the
MPT Grows Right so in the client
software implementation that means that
for every read write event um what
happens is you it will require more
database lookups it will require more um
hash calculations so all these are
expensive operations so when when you
have those scenarios then your node will
become slower and it's just not just
that right you also think about Hardware
storage every few years you probably
have to change your Hardware to upgrade
your SSD so that uh it can contain more
um
state so if you really think about it as
a flow when the state grows what happens
is that running a node costs more
because you have to upgrade your
Hardware every few years whether it's
storage or like CPU or whatever um when
you have that kind of scenario that
means that um less people will be
incentivized to run noes like normal
people like maybe just you and me and
when less people run noes then um e
become less decentralized right so
that's like a effect of State growth but
I know what some of you may be thinking
right some of you may be thinking that
it's fine right um The Innovation in
Hardware will probably outpace State
growth and that's true but is it really
as simple as changing hardware and your
um note will magically run again it's
not as simple as this the reality is
that you have to first go to a physical
store or online store purchase the
hardware you have to once your Hardware
arrived you have to reassemble your note
take out the screw take out the cover
swap the hardware
put aware back I don't know like put a
cover back put a screw back then um
maybe you have to migrate your storage
from the old disc to the new disc during
this process if you messed up if you
made a mistake what you need to do is
that you need to wait hours to resing
again from zero and yeah it's just a
very terrible user experience so no it's
not as simple as people may think yes if
your technical is simple to you but not
for normal people no writing notes
should be easy or at least we shouldn't
make it harder than what it is right now
so looking back at the state if you look
at all the key value pairs ask yourself
this question how many key value pairs
were actually accessed in recently let's
say in the past one
year based on the analysis that I did is
it was only about 20% so really what we
are storing right now for the execution
clients are 80% of the state they are
unused in a long time and what happens
when we eliminate this 80% of the state
wouldn't we get a slower State growth
wouldn't we be able to reduce the
hardware um storage requirements
wouldn't we be able to build better
execution client a more efficient one so
that is what we are trying to do with
State
aspiring the concept of St expire is
simple it has one key objective which is
to expire now and revive later we want
to provide a way to expire the still
data on chain while providing a way for
users to revive those data there are two
key question that we we need to answer
for this objective first how do we know
if a state is expired second how do we
revive expir State and let's think this
true together first we can look at the
current npt right so this is the
structure of the MPT we are only going
to focus on the values because those are
those values are the ones that want to
expire to answer the first question how
do we know if a state is expired well
you can take a few seconds to think
about it
the most straightforward way is to add
some sort of a metadata to measure the
state or the values right so here what
I'm going to do here is to add something
called an access period to it so an
access period can think of it as like
measure in blocks or basically like one
period is equals to six months maybe so
when you have um a period that
corresponds to each value then we can
already answer our first question in
regards to the expiry rule we can simply
set like for example a value is
considered expired if it hasn't been
accessed for maybe more than a year
right you can change this rule so we
answer our first question what happens
when a note or a value expired right so
for leaf node we can simply replace the
leaf node expired Lea node with the hash
of the Lea node or um if the for branch
node if all the all of the children are
um are expired then we can simply
replace the branch with the hash as well
so that's a relatively straightforward
um expir rule so for for the second one
which is to revive how do we need how
can users revive the state is by perhaps
submitting a transaction or here we will
introduce a new transaction type to
revive um certain state that user wants
so in the revive transaction um what
user needs to do is to provide the key
value and the period if it's a expired
Leaf note or if it's a expired Branch
then they will have to provide a Merle
proof of some sort so yeah um we seem to
be able to answer these two questions
but is this really the best solution
that we have if you really look at the
before and after it's not really that
effective because if you only look at
the leaf Noe you are simply replacing
the value with the hash and um not just
that for all the values that we have um
in the try we are adding an additional
metadata so in the worst case we can
actually have the opposite effect
instead of reducing State size we might
have a scenario in the worst case where
we are increasing the St St in sa
because of all this metadata so this is
not
the best solution we that we can have
let's look at another solution instead
of putting the metadata the period to
each of the values here we actually just
put it on the branch node so the expiry
rule is similar right but here for each
child index we are going to have the
excess period and the concept of period
is still the same the concept of expiry
rule is kind of same as well it expires
when a child it was considered last
access for example a year ago so and
what happens when a child is expired
right same thing we replace the entire
sub tree with the hash so just by
looking at before and after you can
already see from the diagram right you
are replacing a bunch of notes with the
hash itself so we are saving up quite a
lot of space in in regards to the revive
part is relatively straightforward you
simply provide the path and the moal
proof to the expir sub tree so yeah it
seems like a viable solution GG easy
seems like we got the best solution and
this is actually one of the um solution
that BMB chain uh raised last year I was
part of that team we had a slight
variance of this solution but the core
concept Remains the Same but if this
solution was truly viable why hasn't
they implemented yet of course there are
hidden issues um one big issue is with
proof
size EMP proof size is too large so when
we have large proof size that means we
will inevitably increase block size as
well increasing block size will have
effect on network throughput and network
latency so in the worst case where um if
a block is too large then the validator
couldn't process it in time then we
would make the network to become
unstable and might potentially even halt
it so in regards to State expir solution
npt from all of the um solution that I
have right now it's probably not viable
because of the proof size so we have to
look for the next one and thankfully we
have one which is veral
so I'm not going to go through
everything about veral if you have no
knowledge about it you can check out
viral.
info web page to know more about
it or you can check out gom's talk later
in the evening um to go through the
veral structure right um You have
internal noes which are similar to mpt's
Branch nodes and you have extension Noe
which basically contains a group of
values why veral is important just to go
through it briefly it has small proof
sizes so it solves the problem that we
have it allows for stateless clients it
reduces um Hardware requirements
improves node thinking experience ZK
friendly and more one major change is
that we are for in worko we are using a
single tree approach instead of double
layer what this means is that we no
longer have the concept of State try and
um storage tries but we put everything
in veral tree so without even
understanding how veral tree works you
can come up with a state asir solution
as well and we do the same thing by
looking at the
structure what would you think we need
to add in order to answer the two key
questions that we
have it's simple we do the same thing by
adding the period to the extension node
because in verot tree one very special
property is that values are grouped
together so because you have this very
nice property then it makes this um
solution very effective and let's go
through the flow um like before for the
expir rule the concept period is still
the same it expires when the no the
extension note was last accessed for
example a year ago so we got our first
question done the SEC um so what happens
when um an extion node is expired it's
the same as well we replace it with the
commitment of the expired node the
commitment you can think of it as the
same as hash of the npt yeah and in
regards to the revive rule what users
need to provide in the revive
transaction is to provide the path to
the extension nodee the period And also
the all the values in the extension node
it's pretty straightforward and this is
exactly what um we have proposed in EIP
trees um um yeah so it's a relatively
straightforward solution the advantage
of this solution is first is simple
relatively simple second is it has clear
gas cost um the revive proofs are
relatively smaller as well because you
just provide all the things that you
need in the extension node and then it's
also Backward Compatible with veral in a
sense where if you choose to enable it
together with veral that's good it's
possible
but if it choose to enable this EIP
after veral it's also possible right so
that's what it means by back compatible
one major disadvantage is it only
expires States partially because you can
think of a scenario where majority of
the leaf values are hasn't been accessed
for for a long time but there could be
one single leaf value that has been
accessed for right quite actively so in
that case the extension Noe is not
considered as expired so that's why this
solution is called the partial show
State aspir solution what if we want
full State aspir solution well we have
to go back two years ago to vitalic
multi period Tre approach published in
the approaches that I've shown here so
you have the concept of like multi
period Tre the concept of period is
still the same um here what's different
is that for every single new period a
new state tree is created the expiry
rule here is that um the state older
than two periods are expir spired so for
a client software what they need to
store at a time is really the state
three of the current period And also the
previous
period okay for the revive part it's
more complicated than this if you look
at the original article but essentially
what we need to do is that we given an
um expired account for example you will
require the last known stage three of
the account then you also need to
provide the proof of all the subsequent
periods up until current periods minus
one that's a very simple
explanation my problem with this uh
proposal is that first it's super
complex and that's why I believe that um
the research in this direction has been
stagnant in the past few years secondly
it requires something called address
based extension so address based
extension by itself is already a very
complicated um and controversial
proposal because it brings many Breaking
changes to our etherum protocol so we
are literally stacking problems onto
problems and secondly what I can um what
I can foresee is data medication because
you are storing two State Tre at once so
in some cases or in even in the worst
case you might have um duplicated data
which again in the worst case you can
actually double the state size instead
of like reducing it so that that could
happen and compared to the partial State
expir solution you will have larger
proof size because you have to prove
different things now so yes we get full
state aspir but is it worth it I don't
know the future where are we HED next so
we know that for State expiry we get
slower state goow or even eliminated we
get reduced Hardware requirements and we
get a more efficient execution client
but to get those benefits we exchange it
for worst user experience because now
users have to care about Reviving their
state they have to submit another
transaction to in order to revive it and
those transactions will incur additional
State revive costs right and the another
thing is that how do these users like
normal users get those proofs from right
the first part is definitely centralized
providers um yeah but we don't want to
relies um rely on centralized Solutions
we have to come up with a decentralized
solution and that's why in order to
really enable State expiry while still
providing a good enough user experience
we need a decentralized proving service
such as the portal
Network so yeah and we might not even go
for veral tree in state we might go for
binary tree so if we go for binary tree
then EIP 7736 wouldn't work um depending
on how the binary tree structure that we
would want to go for we have to rethink
um another csir solution if it's similar
to the veral tree one it will probably
work if it's totally different then we
have to rethink it but if you follow
through the thinking process that have
shown here we can probably come up with
a few
variants so
yeah by the way ethereum State just grew
by 1.9 megabytes throughout this talk so
let's find a viable solution to State
growth and let's build an ethereum that
scills in time thank
you thank you so much so we're going to
go through the Q&amp;A now um and we're
going to go for uploaded questions first
um so why do you need State expiry if
you can have stateless clients in the
future and have a smaller subset of
nodes store the full T yeah so in a
stateless world what would happen is
that um even with epbs is validators
will be stateless then only B Builders
will have the full state but even that
we are not solving the root cause which
is the state the fact that 80% for
example um of the state is still
considered as still or hasn't been used
for a long time so State stess um
stateless Nur doesn't solve this root
problem but state asiry does right we we
want to eliminate it so in the world
where we have stat list and state asiry
we can give a better experience to um
even block Builders as well and make it
more efficient yeah great um is State
partitioning an option I think State
part partitioning is a like um general
term like I need to know like in details
what what you mean by state partitioning
but because I don't know the details I
will say maybe yeah
um and would it be possible to charge a
yearly fee to the account if it has no
eth delete the whole state this would be
a financial incentive for efficient
State use so this is something like a
renting model um it definitely is
possible um but the thing about ethereum
is that if you are adding such a renting
model you are changing the entire
economics so it might break things as
well and um in my perspective I don't
think the community would uh be ready or
would support such a feature um because
it might break a lot of things and
economic wise is so might not align to
their incentive so it is possible but
it's a social problem
yeah and how about using snarks to
compress proofs for re revivals and do
batch revivals um that's possible but um
again in regards to how we want to use
snars it really depends on how we want
to um change up the the again the 2 key
questions that we have like how how
first how do you want to maure State um
how do you want to I mean how do we know
if a state is expired and secondly how
um can we um revive expired States so
here you seem to have answer the second
question but how about it first we have
to explore that yeah um and the next one
is kind of a question only right will
alter the No No not read um in our
proposal yes because if for example if a
read operation um changes the the period
in the extension node you are
essentially doing a right operation so
if if you are doing something like that
you um you have to change up the gas
cost for that particular read operation
because it's read but it's actually
right um so there are a few proposed
solution for example if if it's the
first read on in the new period then we
consider as for the gas cost we consider
is as the same as right but yeah um
there could be other potential other
Solutions as well yeah what would be the
incentive of running an expired State
provider node expired State provider no
so uh I'm guessing is that you
um you have to provide you are running a
service that provides the proof um
honestly there are no incentive unless
you're running like a you if you're a
centralized provider um that's why I say
um we probably have to rely on a
decentralized service p network perhaps
to be able to provide those proofs to
everyone yeah good intro to the next
talk what was uh was the 20% State turn
measured on BC or mainnet and if mainnet
have you tried measuring Beyond 14
million um is e main net measuring beond
crashed are there any gas refunds at
State expiry and gas costs involved
while recovering State at a later time
um in regards to funding or we haven't
explored it yet but yeah that that would
be a good direction to look at yeah how
about archiving Old State compressed in
cheap slow storage instead of expiring
it if you're talking about um like a
client implementation level is
definitely possible but if you're
talking about um protocol level um I
foresee there are plenty of tack that
can that can occur so I'm not too sure
about this direction yeah who is
responsible for Reviving an old's
expired value from the hindsight it's
going to be a users but if you have like
a sponsorship kind of model then the
sponsors can revive it for you Eon
attraction thing so yeah that would be
ideal for the users but by default I
guess the user have to revive it
themselves and where does a node fetch a
sub tree from uh when Reviving it from
some centralized or for some provider
not centralized provider sorry yeah from
some provider yeah perfect thank you so
much Han thank
you uh and we're going to have a um
short break until the next talk
e e
the e
right
hello hello hello so um next up we have
um somebody who I'm actually really
excited to tell you came up from the um
ethereum protocol fellowship program and
he's working on Portal networks please
welcome Corby uh Kobe moraz
liel uh hi uh I'm Colby Mor liel and I
wanted to give a talk today onc
decentralizing access to ethereum
utilizing ethereum's portal networks
which might sound a little weird but it
will make sense through the talk uh so
the origins of ethereum is it's like was
creating a programmable blockchain or a
world computer instead of just having a
simple Ledger or colored coins which
were basically like coins with random
features you could program many features
and ethereum's emphasis on this this was
decentralization and censorship
resistance uh but how did people access
ethereum this was done through full
nodes which provided you a gateway to
the ethereum protocol through the Json
RPC full nodes were often long running
processes because if you turn off your
laptop and turn it on you have to resync
which is kind of hard if you want to
send a transaction you have to wait a
few hours uh so full nodes weren't
always unaccessible at the start you
could spin up a node very fast but then
as requirements grew over time it became
harder uh I would say one of the
greatest inaccessibility to ethereum is
knowledge being able to run a node is a
feat which all of us in the room can do
but can your grandma do it and if for
etherum to be accessible you need it to
be like you don't want to run this thing
but you need to know something uh time
you you need to sync a node as I was
saying like if you turn on a laptop like
on and off syncing a node to send a
transaction is very unreasonable and the
it costs associated with with that
updating your node for hard Forks is
kind of annoying when it's like
repetitive every year and then the
biggest one I guess is Hardware costs uh
it's projected in the next four months
by East stakers
that that validators will need to update
to 4 tbte diss
and my little picture of like the man
holding the world which is like a GU
node it's like pretty sizable and really
annoying that you need to buy a SSD just
to use
ethereum so because ethereum was
unaccessible this created wave for
centralized providers which took down
the barrier of Entry to access ethereum
but it came with this consequence of
centralization which uh earlier when I
said the origin it's something we didn't
want
so with the one of the main concerns
being the storage requirements there is
this Nifty thing called e for forer
history expiry where in The Purge path
this is basically what if instead of all
node storing all the data we lowered the
costs by not requiring them to store old
data what's no longer reibly needed to
run a
validator uh this doesn't mean nodes
can't store the history but it means
they're not responsible for it all and
but how do we achieve E4 fors and enter
the portal network uh what is Portal
instead of depending on phone loads
which hold all like the whole pie of
data uh what if it could only hold a
slice of that data uh portal distributes
this responsibility amongst numerous
small nodes what are independent of each
other so you could think of it as like a
slice of a pie but the whole pie is
still accessible through
portal uh portal is also sustainable uh
it's both a server and a client which is
very important because this problem has
been here for a very long time uh
previously in the past there's been
attempts at this for example Lees which
the concept of it was an alra an
altruistic full node would host the
server to a bunch of light nodes but the
problem that occurred was there was a
bunch of users who wanted to run a light
node but not enough people who wanted to
run a full node so they were all
overloaded portal switches this up by
making all the participants contribute
back to it so it's sustainable into the
future we also get the benefits before
as having lower storage requirements and
lighter CPU
usage uh but how does this work a portal
uses a fundamentally different
peer-to-peer model than ethereum
today uh through distributed hash tables
uh distributed hash tables and enabled
decent decentralized storage and lookup
system uh where each piece of content is
addressed by a unique identifier and
stored and stored in multiple nodes for
redundancy uh dhts make it possible to
be able to look up the data even if you
don't sort yourself which is what I was
going by when I said you could sore a
piece of the pie but still have access
to the whole thing uh and as I was
saying a totally different peer-to-peer
model portals also a replacement for the
Legacy Dev peer-to-peer network uh in
that imagine de P top is this triangle
where you have to you have to
participate in everything to access
anything uh portal breaks us up into
different networks uh one of our first
ones what we'll be launching is Portal
history
uh and then there's
others uh but what does each Network do
portal history contains headers bodies
and receipts portal state allows you to
access the state such as your trans such
as your balances and contract storage
portal index is if you want to find
which block body your transactions in
and the portal transaction mol will be
very interesting with fkl and stateless
clients uh currently there's no hard
solution for how we'll handle sending
transactions in a stateless world and we
believe that portals uniquely is in a
unique position to solve this problem
and we will solve this problem but
anyways with having access to all that
data you also gain access to a full
archival node but like distributed
trademark and the cool thing about that
is it's like you can you can basically
run a p portal node and have in access
which is massive because in the past if
you wanted to have full archival access
which was provable you would need to run
a GU node but to run a GU archival node
that requires 20 terabyt of storage
which is massive and it also takes like
over a month to sync which if you just
want like quick access to this like to
archival ethereum data that sucks
especially if you're a researcher and
you just want to research stuff instead
of waiting a month to start your
research
uh so portal is fully provable which is
huge uh there's kind of two paths to do
this uh so you could use our portal
Beacon Network which will be very useful
for w for wallet use cases where you
could basically put portal directly in
place of a centralized provider uh
portal Beacon network is an
implementation of the consensus layer
lik line protocol and it will be
integrated in any implementation so if
you want to use portal you don't need to
think of anything else you just
integrate our libraries and it's proven
uh a big use case though will as I said
before will also be for uh full nodes
and for that they're already running an
ethereum consensus layer client which
they can just repurpose to prove this
data so as I was saying before there's
all these portal networks but is there a
dependency to prove and there is so for
state if you wanted to get your balance
you would get a proof to the state route
which would be in a header but had how
do you know the header real uh there's
accumulators in the beacon Network like
consensus client called historical
summaries which is in the beacon state
so depending on your use case if you
only needed historical data well then
you would basically have this two node
dependency but if you needed State you
would have an additional one and by
doing this you can you only need to run
a portal network of what your
requirements are for the use
case uh how do you portal clients
initially get the data uh currently it's
through Bridges bridges are basically
full node full nodes which have access
to all the data but as portal gets
adopted in execution layer clients which
I probably can't talk about it but like
an announcement on the way but anyways
uh so execution layer clients already
gossip blocks around the network portal
is kind of the same in that execution
layer clients will be able to CIT blocks
on the network but they'll only need to
gossip us to a select few peers where if
they have 50 peers now that nodes Only
Store a slice it would they' only be
required to gossip this data to maybe 10
or 5% which saves
bandwidth uh incentives so why would
people want to run a portal node uh well
Financial incentives are hard uh it
leads to a race to the bottom and it's
very easy to game in in that let's say I
want to maximize my my income from
running a portal node well then I could
offer the worst service but also allow
for the most whatever metric you use to
reward people uh there are other
projects trying to achieve this approach
and wouldn't it be really cool if
everybody could participate in
ethereum's protocol for free because I
don't want to pay someone to send a
transaction or pay someone to get my
balance when I open my wallet uh eth we
believe that ethereum's protocol has
innate value uh that that innate value
is being able to send money uh fetch
your balance use
l2s and portal gives you access to this
on cheap Hardware so if the value of
ethereum is high enough and the cost of
running a portal node is so minimally
small uh I we think the incentives are
aligned for people to run these
nodes uh use cases as I said earlier
lighter full nodes uh with storage C
with storage requirements increasing uh
being able to add for fours while
maintaining current day ux uh ux by if
you just implemented 44s your node would
have no idea of what the past history
was with
like you could fully respond to any
request and it would be like nothing
ever
happened uh another thing is nearly
instant think time
for full archival for full archival node
access and the other is a replacement
for centralized providers and use cases
such as mobile
wallets which is pretty
cool uh but what's the catch you may be
asking I'm selling this this solution
what seems too good to be true uh is it
like so the trade-off is between latency
and storage uh nothing is as fast as
having it on disk but for most of the
data you don't actually need to access
it that often so we believe that the
tradeoff for a majority of use cases
is correct is like actually there and
like the only time you really need quick
access is if you're block building and
for mobile wallets if it's fast enough
it's good
enough uh so for the first time you can
choose how you participate in ethereum's
protocol uh I think think this is kind
of analogous to the infinite Garden
analogy that is often told on ethereum's
future uh instead of basically running a
full node and requiring everything
there's tons of possibilities how portal
can change how you access ethereum's
protocol whether it's only subscribing
to a few parts of the protocol only
history or accessing the for full
protocol it's finally a choice instead
of a requirement to handle it all which
is yeah really
annoying uh who's building portal
clients well the ethereum foundation has
been at the center of this from the
start but we have all but from the start
we have also been assisted by status and
ethereum JS which has been massive uh
recently nethermind has been taking the
stage and for execution layer clients
they have been working the hardest on
this from the from pretty recently like
last year which is really cool there's
open source teams from around the world
who are building clients uh clients
being built by EPF members and I guess
you guys could build portal clients as
well uh we have clients being built in
all these languages so if you want to
use portal you can uh I'm sure everybody
would be like happy to answer questions
and I think we covered like the whole
stack which is cool uh portal history is
ready for developers to start using and
we have the data to back that up uh so
we built a St a statistics platform for
like seeing if our stuff works and we
call that GLaDOS uh for the past few
months we have we had zero failed audits
on our Network and what that means is
the data is available on the
network and there hasn't been any case
where we couldn't find it so the system
has been robust for months and that's
really exciting uh there's a QR code
there but you should be able to find it
on our website as well another exciting
use case I was talking about earlier is
wallets we're building Trin desktop
which is Hope hoping to Target
everything but the browser so hopefully
like ethereum Gs does that for us uh
here's the front screen you turn it on
and it's like woo stats but you can also
you do e get block by number get block
by hash uh get balance but in the next
few months we're hoping to integrate a
wallet as we want to be like the test
bed to show people this actually works
and what better way to do that than do
it yourself and show
people uh and it's also as I was saying
earlier you can configure your storage
requirements so if you set 2 gbt you'll
only ever need to contribute 2 gbt you
won't need to buy a disc in a year which
is really cool cuz it sucks to buy a 4
tab disc when you already bought a 2
one uh so now anybody can participate in
ethereum's protocol uh as I was saying
earlier you could just integrate that
into a wallet and the user wouldn't
doesn't have to know it's running which
is really
cool and where to find out more we have
a QR code for our Discord like invite
which is really useful if you want to
ask questions we have our website with
guides and like blog posts and how to
set up most of the clients already uh we
have we have a Twitter which uh our team
hates Twitter but it's like good for
like getting people to know stuff and
then we have specs so if you want to
contribute every team is super open to
it uh and they'd be like super happy uh
we need to improve our issues a little
bit but that can be fixed and yeah so uh
thank you for coming to I guess this
talk on Portal uh and yeah thank you
okay so let's go through some questions
I'm going to read them for you um can I
use portal Network today to check my
balance if not when same question for
doing an eth transfer uh so you can
check your balance if it's within the
first million block so if you guys are
if you guys used ethereum 9 years ago
you can check your balance today uh we
expect balance for like latest account
for like checking balance for the head
to be available in q1 or Q2 uh we just
need to finish some infrastructure to
support that what is the biggest hurdle
to getting all clients to adopt the
portal Network and how can the community
help portal get adopted uh I would say
the biggest thing has been awareness two
years ago people are like what portal
and then it's like a minimal
implementation and all these questions
what never really made sense but
especially this year people actually
know what portal is and it's really cool
to see people like referencing portal
like the like actually about it and we
don't have to do all the Talking
ourselves so I think just talking to
people about it is awesome awesome uh
what is the minimum percentage of
network data that a portal network is is
expected to have uh so we have thrown
numbers like 100 megabytes but that's
fully
configurable uh since the requirements
are so low for our client at least we
wouldn't be surprised if we set it to 1
gab because realistically someone
wouldn't notice like most apps or 500
megabytes on their phone so it's like if
we use like a gigabyte like they
probably wouldn't notice but it's
configurable um and I think the next two
questions can be combined how does
portal Network compared to Classic uh
peer-to-peer file sharing Network such
as bit torrent uh so one of the problems
with bit torrent is it doesn't have a
inherent way to like prove the data or
validate it so you run into problems of
you need to download this huge section
of data and it's very uninformed
uh portal is different in that all the
data you can fetch from the from the
network is provable so it's much easier
for a client to like let's say fetch any
piece of data they they want where
through torrent they would probably have
to Index this data and do some kind of
like out of- band proof which would be a
lot more complex and have a much worse
ux experience and you answered this one
in your presentation but it was asked
before so is there incentive model for
running a portal net network node uh for
writing a portal network node I guess
like if you wanted to use it in your
wallet and you used a language what
wasn't there yet uh I guess that would
be the incentive like accessing ethereum
with instant sync times decentralized
very cool could one Implement an archive
node using portal as a
backend uh yes so the idea is like
portal would have all the act all the
data that a archival node would have so
you could just use portal as your
archival node it would be a little slow
but you
could what are the expected hardware and
network specs in gigabits for running
portal nodes and who do you think uh who
do you think will be ready to operate
these
altruistically uh I think that the the
top three execution layer clients would
be running all these so by default so
that's like a lot uh other than that
like if if you're running a wallet on
your phone I guess that's like an Altru
that's not really altruistic you're act
you have actual utility in that uh so I
think we can do quite fine with while
ignoring altruistic use
cases has there been engagement with
ipfs Community it sounds like there's a
lot of overlap with dhts accessing
content address data Etc uh so some of
the issues with ipfs is since they have
no validity scheme all one of the things
is data is constantly cycled off the
network and because of our strong
validation conditions it basically means
if we have enough storage it's on the
network and it won't be flushed off
which is really important for the
longevity and robustness of portal uh
which isn't there with ipfs also they
use TCP which has much higher latency
we're I forgot to mention our talk but
we're based off dis V5 which is the
current day no Discovery protocol for
ethereum and it uses UDP which is much
quicker for like getting responses back
especially like if you have to Ping
multiple peers that adds up don't some
nodes need to sacrifice for portal
Network or in Portal Network for this to
work not lots will run archival data but
may Lots May query it and these might
get spammed uh so a portal node would
only need to hold a very small slice of
the data so if a full node is only like
storing like 1 gab for portal they
probably wouldn't really notice it uh
there is no real requirement that they
like store all the archive on their node
uh the idea is that all the like full
nodes on ethereum store like way less
and it's like they all contribute where
currently it's like every node has to
sort all the data what if we did this a
little like more smart I
guess what are the guarantees that the
data will not be lost over time uh I
think the guarantees is kind of
analogous to what I said earlier about
validation uh any storage we have above
the minimal requirement is used for
redundancy uh uh but if worst case
scenario there's other archival
Solutions uh portal is really good for
accessing the data but in a worst case
scenario you can use archival formats
such as era or era
wasn't on Portal there's optimized
formats for
archival portal is really good if you
want to access
it uh what is the most resource
constrained device that has been a on
Portal
uh for us it's basically been I guess
raspberry pies I know raspberry pies
have gone a little strong but I don't
like when we run it we don't even use a
core and we use like 300 megabytes of
ram so like something with maybe like
run portal on and we haven't even
optimized it
yet does portal support websocket
connections uh through the RPC uh that
would be dependent on the implementation
ours does but it's I guess the
implementation's
choice cool can we get another round of
applause for kobby thank you so
much and we'll be back in five minutes
with uh pus on epbs
hi everybody so our next speaker um is
one of the most vocal people on the all
core Dev calls and on Twitter um and
we're very grateful for him for doing
that with all core devs um this is uh
pus from Prism talking to you about the
status of
epbs thank you but just in my defense I
open my Twitter account only to pitch
this and as soon as this is shipped I'm
going to shut up on Twitter anyway so
today I'm going to be talking about the
status of epbs and epbs during this talk
is going to mean enshrined payload block
separation this is not the usual meaning
and you'll notice that I'll only mention
proposers and Builders towards the last
couple of
slides um the talk is going to be
divided in three
sections the first section I want to
convince you for a while that um
dividing the payload the execution
payload from the consensus block is
something that is necessary in ethereum
it is highly beneficial it is a scaling
factor and it enables other scaling
Solutions like PR Das to actually
fulfill its full
potential we have this problem that we
have since emerged which is our Tech
Dept that we adopted this minimalistic
way of merging out of proof of work in
which we included the execution block
the one that has the trans actions and
everything that we need to like modify
the ethereum machine inside of the
consensus block that has the
attestations the deposits the exits
everything that we need to decide what
is our current head and we distribute
them both together this makes for a
large Chun of data that is distributed
among the
nodes when this data has logically
different purposes and logically
different
validations what a node does when
when it reaches gets a block it needs to
get to consensus in two different things
one thing is what is the status of the
network what is the execution status of
the network the validity of the block
and the other thing is given two
different views of the network which one
even both of them possibly valid which
one is the one that we consider the head
of the chain these two validations are
completely independent and they are done
by two different clients even two
different soft pieces of software the
validator runs in the running in the
computers the execution consensus is
about validity the consensus consensus
is about which one of the world the
viewers of the world is the current
one because of our Tech Deb the way that
we validate blocks puts all of the
strain of the network in the very first
few seconds of the slot a block is
broadcast at the beginning of a slot and
it needs to be validated it needs to be
downloaded in irely by by the whole
network and by 4 seconds validators need
to have already checked consensus
executed the execution check that the
blob data was available in the future
check that inclusion lists were
satisfied and ATT test for this the rest
of the slot is useless time essentially
we're just counting attestations
aggregating them the node doesn't do
anything if anyone here runs a node
you're going to see hear the fans going
off exactly every 12 seconds
so that's what the ethereum validation
is today and the question is can we make
this better can we make the timings
better presumably yes we have four
seconds and actually we don't use those
four seconds but the problem is that
validators are incentivized to actually
propose their blocks as late as possible
so that they can extract more M out of
them and these timing games make
twigling with this these timings for
attestations a an impossible problem to
solve if we gave more time to actually
sync better blocks larger blocks have
more blobs in the network what would
happen is that validator would just
propose later and extract more
M so why separating them since we do not
need to validate execution to decide
what is our head why not just broadcast
the block which is a minimal block which
is just consensus validate consensus
decide what is our status of the of the
chain and then use the rest of those 12
seconds to validate execution check if
the blobs are available validate
inclusion list do all of the stuff that
is actually heavy in
the high latency path and the low
latency path which is validation of
consensus that takes two seconds you
just download the tiny block validated
immediately it takes 7 70 milliseconds
today to validate the consensus side and
just a test so that's that's a scaling
feature of separating the the payload
From the
Block so that was the first part of the
talk I want to I hope I convince you
that the separation gives us a lot of
benefits for ethereum now the question
is what H how can we achieve separating
the block from the payload and the
minimum features that we want that we
need if we want to separate them would
be this so what's what we desire of such
a s of such a separation we would want
to have this validations done completely
independent we want to validate the
consensus side in the fast path and the
execution side in the low in the in the
slow path we want to separate the
propagation of these two blocks the
large chunks of transactions might take
longer to come the blobs that are the
huge chall of transaction might take
longer to to to come we do not need to
have a very high uh Uplink bandwidth to
submit the blobs because it takes 12
seconds to be disseminated so we solve
the bottlenecks that we have we have
today in things like perer D or full
D and we see immediately one problem and
is that well since now you cannot sign
the block with with the payload because
otherwise we would have a free data
availability problem we need to have
those two objects being signed that's it
that's not so hard verifying signatures
is not a
problem here's a real problem the real
problem is that now whatever the situ
whatever this design the mechanism
designed to separate the block from the
payload you will have to deal with new
features uh with new situations uh today
a slot either has a block or it doesn't
those are the two possible status if you
have a consensus block you have a
payload and if you don't well you don't
have a payload but in a situation in
which you have validated the block the
consensus block you attested to it and
it's your head and the payload might be
invalid or might not come or the blobs
were not available or it didn't satisfy
an inclusion list the situation is that
we have two we have one extra status
which is the status in which the
consensus block was valid and the
payload was not and this gives a problem
which is a for Choice problem you need
to change for choice to account for this
for these statuses you need to check
that if I attested to a to a block that
whose parent did not have a payload well
that attestation this does not count
towards a parent that did have a payload
and this is completely independent of
any auction mechanism this is the
complication of for choice
of course you need to still provide
security that you're not going to be
reared for free but anyway so in such a
word the other complication that you
have that client implementers will have
is the fact that we have it enshrined in
our coding that we get the blog we
validate in certain order we we can
validate in parallel execution and
consensus and we all do because the
validations are independent but then we
wait until both validations are done and
we ATT test now one would naively think
that uh that's easy to separate because
you just send the things that we're
doing in parallel you just no just
validate consensus ATT test and then
validate execution in the rest and
that's it but that's not so easy because
unfortunately the merge was minimalistic
but then we had capella and in Capella
we added new messages that came from the
consensus layer to the execution layer
in Capella we have withdrawals that are
deducted in the consensus layer and then
later on are well and and our credit in
the execution layer if we have them
separated we're going to have to do that
logic theed duct first MO with throws
and then uh credit on the execution
layer when we see a payload so that's a
complication and Electra gives us many
more headaches now in Electra we have
messages in the other direction and in
future Forks we expect to get more and
more messages in the direction from the
Y triggered in the L towards the
consensus layer these are for example
deposit requests withdrawal requests and
so forth which you will have to change
your code in such a way that when the
payload comes you process those
okay so the point I'm trying to make is
that the complication has nothing to do
with neither me and the auction
mechanism so now we're going to start
moving to auctioning but before that let
me tell you what the slot will look like
in a in a way in which we separated the
payLo From the Block regardless of of
auctioning mechanism we will have a
broadcast you're going to have to
validate quickly execution which is fast
and then you have the rest of the slot
to just get consensus on whether or not
the payload was
there okay so that was the part of
payload block
separation now we achieve we come to the
section
of proposer Builder
separation so I've described the problem
the big lifting of separating the block
and the payload is in two sections
changing for choice to achieve consensus
on what is the head of the chain and
changing clients uh implementations on
how they sync their block because they
they need to do things in a in a
essentially different way they need to
access the databases in essentially
different way but now the question is
well how do we implement this how do we
achieve an implementation that separates
the block and the payload in a
minimalistic
way and I want to convince you well
which is probably hard but I want to
make a case that with minimal
assumptions uh EIP 7732 two is a system
that achieves this in an actual minimal
way
so we need to decide a way of how the
payload appears and I'm going to talk a
little bit about options there are many
ideas going around on they all have
acronyms that that are hard to remember
epbs slot auctions APS ETS ATS I don't
know but they all more or less are in
the same way there's someone that sells
a right to produce a payload in Block
auctions the proposer submits a block a
consensus block with a commitment to a
particular payload and the Builder
that's committing for that particular
payload promises to pay uh a value to
for the rights of producing that payload
in slot auctions the proposer does not
commit to a particular payload it only
commits to a particular Builder and then
the Builder later on produces any
payload that he wishes to produce
there's execution tickets or execution
auctions in which the auctioneer is not
a validator but it's the protocol itself
the protocol sells far in advance 302
slots in advance either tickets and then
there's a lottery that is run uh by
Randomness and we choose who later 30
later who proposes the payload or you
can actually sell the protocol can sell
can hold an auction and sell the rights
to propose a slot 32 slots in advance
and all of these mechanisms have their
trade-offs none of them come for free
they all of them impact the m chain and
they all of them uh produce different
kinds of
centralizations all of these mechanisms
that I'm describing here you can or may
not run them with M burn that means that
even if the proposer is choosing and
getting some value out of the Builder
you could in principle include a burning
of that value towards the protocol the
one that I didn't include is no option
but that's certainly possible we wanted
to set it was about enshrined payload
block separation in principle I could
just enforce that the proposer is the
same signature as this as the
Builder keep everything exactly as it is
today in the M chain and keep using me
boost nothing would change except that
we have all the Machinery to separate
the block and the
payload however if we've already did the
heavy lifting which is changing for
choice and changing block processing
changing the auction is zero work for us
changing the auction is nothing because
the auction we already have it we have
the code that requests header from the
Builder we don't need to change that the
only thing that we need to check is that
the signature will be different it's
coming from a particular
validator so the heavy lifting is done
in a minimal way and adding an auction
to get Block auctions is
Trivial so what are the things that
actually change the the problems that
adding the auction increases is that in
a world in which the proposer and the
builders may be different then you need
to give certain safeties to the Builder
if the proposer and the Builder is the
same then you don't care about
protecting the Builder if the payload
came late or if the payload did if the
Builder wanted to withhold the payload
this is because well the proposer is the
same as the Builder he should have sent
everything together but in a world in
with the in which the proposer and the
Builder are different you need to
protect the Builder you need to give
assurances to the Builder that if the
Builder submitted his block on time the
block is canonical the payload is
canonical and you need to give
assurances of hard one is a new
situation this was a previous slide
where the three phenomenas could happen
this is the full the block was full here
the proposer of slot n is building on
top of an empty slot here the proposer
of slot n is reorg entirely the previous
blog but now we have a new situation in
which the proposer of slot n is trying
to make make the Builder pay for a
payload that he didn't reveal because
the previous block was weak so we need
to prevent that situation from happening
and this is a minimal change likely for
us uh EF researchers on for Choice are
very good and we have minimal solutions
for this that are a tiny bit more of
code to the previous heavy lifting which
is dealing with the whole
tree so how does the PB epbs slot
actually work on an auction mechanism
then
builder at the proposer at the beginning
of the slot requests exactly as with me
boo today with the exact lines of code
will request directly from the builders
not the relays their best bid it would
choose whatever bid he wants it would
included in the blog and submit is
consensus blog that can be validated
immediately before 3 seconds we could
have been two seconds actually because
we don't need time to propose blocks
consensus
blocks the rest of the slot well the the
Builder would now have to be protected
is going to count attestations for that
block it's going to count for one second
until he reaches enough attestations in
practice it's going to be 40% of
attestations once the Builder saw 40% of
attestations for the block the Builder
knows that that block cannot be
reor therefore the Builder Reveals His
payload this is a 4 seconds so you have
since then until the very next slot to
validate the payload you can just
increase inre the gas limit a lot if we
could manage to solve the this uh the
state growth problem uh you can increase
the blob number a lot because now we
have 12 seconds to distribute the blocks
you don't have two two seconds to
distribute the
blobs later on there's a light vote
there's a light vote by a committee of
signal the rest of the chain that the
payload was on time that the next
proposer should not reort the
payload there are other designs that do
not include uh that do not include a
light vote there there were previous
designs that included a full vote an
aggregated vote an attestation of the
whole committee for the payload or not
uh but this design is robust enough and
it requires only 512
signatures so let me tell you of
implementation status of uh I'm not sure
if I can ah yes it's an empty video but
uh let me tell you about the
implementation status of this so we
wanted to have a proof of uh yeah a
proof of concept model for epbs and we
have it there's uh we are finalizing
epbs locally constructing blocks so
we're not contacting a builder but we
are finalizing a Network that has the
payload and the block separated um two
clients two consensus clients have have
already the implementation is underway
um te I believe is close to being an
interrupt uh Nimbus has two EPF uh
working on this uh loer and Lighthouse I
think they initiated at least they have
the typing but they haven't Advance much
more but the point is that it takes it
took us a couple of months of sitting
down and coding not more uh it's not
production code but it's certainly ready
the the EIP is ready to
go
uh as I described there's no changes I'm
only mentioning consensus layer changes
there's no changes on the execution
layer that's why the execution layer
guys are happy because we're going to
give them a lot of time to validate the
blog without anything on without them
writing a single line of code
however the interaction with fossil is
not trivial if we want to include
inclusion list which is something that
we really need in in ethereum we're
going to have to involve the execution
layer and the interaction of fossil with
the IP with epbs is not entirely trivial
it's not uh something that I'll describe
today here all right thank you very much
guys
all right we'll go through some
questions from most upvoted are there
any other protocols or message
propagation mechanism being explored
other than Li P Tob not that I
know simple
answer after implementing epbs on prism
how would you rate the complexity of
changing the entire consensus execution
validation sync Etc while still
maintaining backwards compatibility
that's that's a great question
uh it was much harder than I thought uh
for chice was the problem and uh but uh
we have now a because we iterated
several times until we realize what is
the right way of doing it so now
backwards looking there was a very
simple way of doing it so my original
implementation was hard but now we have
a very simple
change as I said in two months we did it
now I believe knowing what is the right
design we could have done it in two
weeks what if there's a reorg larger
than
of one nothing changes uh absolutely
nothing changes for Choice uh my
original design used boosts to rely on
the if the block was poor and the pay
the the Builder did not want to uh
reveal the the payload my original for
Choice design uh relied on the network
reorg the whole thing uh luckily
Franchesco came up with a simplest
solution that doesn't touch for choice
at all it's the usual lmg ghost
mechanism without any boosts so for
chice is not change is not different in
the way that we count weights the only
difference is in the way that there are
nodes that may or may not have a
payload what do you think about
implementing consensus execution
separation without epbs uh I so the I
think that I the the way I phrase this
talk is that uh there's a big chunk of
changes that are completely independent
of any kind of mechanism for auctioning
and those changes are going to have to
be included in any known road map for
ethereum ethereum in all of the known
road maps for ethereum we have this
separation between payload and block and
that's the heavy lifting that has been
done now you need to put on top of this
an auction just to as an implementation
detail and the way the reason why we
chose uh block auctions is because I do
not know how to implement any of the
other ones and if anyone gives me an
actual spec to implement execution
tickets or future slots without single
slot fin it I'll be happy to code it but
these are the only two that we actually
have a spec and we know that it's robust
and safe what about the impact on the
late block of proposer boost uh what
about the could you repeat that one what
about the impact on the late block of
proposer
boost we I'm not sure if I understand
the question but uh so perhaps oh okay
so the the question is perhaps that if a
block comes late proposer boots can reor
yes and this is something that we do
today today in order to not incentivize
seeing late blocks we actually have seen
blocks coming in the early days at 12
seconds trying to reor the next block in
order to not incentivize this we
actually actively reorg a block that
comes late and that's not going to
change here uh the only thing that is
going to change is that the Builder uh
has a safety mechanism that if the block
came late with a commitment to its
payload then the Builder might not
reveal it because because he knows that
it's not going to be forced to
pay because it has to be reordered does
this proposed change require an eth spec
change or an EIP and or does it only
require client client implementation it
is a it is a consensus breaking protocol
it's a it's it's not backwards
compatible it requires ANP the IP is
anybody has a Live question that they
want to ask
oh that's uh that's a great question can
you repeat the question so the question
is whether or not we have we if we've
implemented syn no I have not uh
purposely because I really wanted to
have the the proof of concept before
Devcon it nothing really changes though
because for sync what you you don't you
can p piig it you can pck it back what
we already have today so for syn you're
going to send the full block
together anymore yes
are you afraid that given the changes
and introduction of new features of the
offchain PBS uh pipeline we are soon
going to reach a point of no return
where epbs is pretty hard to even be
realized uh I'm not sure I'm not sure I
understand the question I'm sorry for
example when PBS started we had the
relayer just do one thing but then we
did stuff like optimistic relays
recently there have been proposals of
stuff like gateways which again relays
do so we keep adding complexity into the
offchain PBS stuff that would need to be
matched or very or improved within epbs
do you is this a problem that you see or
forese or is this a viable risk for you
I I don't I don't see this I I can tell
you something that I see as a risk uh I
don't see this particular thing a risk
because complexity on the relay all that
it will CH change what epbs the way
we're proposing is what does is it
allows the Builder to be a relay
directly and permissionless so what what
you're describing to me sounds like
builders in the protocol which they
already are because relays are Builders
uh they will have to have this
complexity if they want to compet be
competitive in the market but from the
pro protocol perspective we don't care
what I do see as a risk though is other
things that are being piggy pack on PBS
say for example uh pre-confirmation uh
and all of these extra markets that are
being done I would require I would ask
for the teams that are working on pre-
comps to make it compatible
forward-looking compatible with
mechanisms of
separation and if the person who um
answered the multiple current concurrent
proposer question wants to ask him
afterwards we're out of time for
questions um but he'll be around in the
room um thank give a hand to
pus and next up we're going to be doing
ZK proving at the history of ethereum in
real time um and that we'll start at
e
for e
hello
hello uh so next up we have the
co-founder of co-founder polygon working
in the ZK he's been working in the ZK
space for some number of years and he's
here to talk to you about ZK proving the
history of ethereum in real time please
welcome Jordie BINA
hello everybody
um we need fast
proving at the beginning was we need
proof we need to generate proofs at some
point we need to generate cheap proof
this was the beginning of the zkm but
what we are seeing now is that no proofs
are would say it's cheap enough
especially if you are doing a roll up
and you have transactions but we need to
prove them fast why we need fast proofs
I would say for many reasons
uh the the reasons I mean in polygon for
example we need it very much for the ACT
layer when you when you want to transfer
funds from one chain to another chain uh
two things needs to happen first you
need to one chain needs to commit to one
state so that the other chain can use
the fonts of the first chain and the
other thing is that the second chain
needs to be sure that this state is
correct okay so it has two options the
first thing is that the second change
just follows that chain and then
guarantees that this this this state is
correct or the other option is that the
chain a provides uh zero knowledge proof
that uh his estate is correct in the
first case well it works well maybe if
you have to networks but if you have
hundreds or thousands of networks that
are appearing or disappearing every time
it does not scale well I mean you cannot
ask all the all the all the all the
validators of all the chains to run a
validator of all the other chains that
are in the aggregation space so the way
to the way to U uh scale that is by
having a zero knowledge proof that uh
warranty is at state is valid this is um
um and then but then this means that the
user when he's doing some interchain
communication uh in the user in the user
interaction I mean in the user in the ux
you will need this uh you need to wait
for this time okay so and uh so we need
to generate these proofs as fast as you
want other context I mean yesterday in
uh in the presentation of The Bean chain
was a ZK uh chain so that means that in
in this context you need a lot of places
like clients needs to validate so needs
to prove that the the full execution
chain it's another case that's important
so in many cases this chain uh so
generating fast proof is important so
how fast can we go and I want to present
here so an internal project that we have
been working for uh the last
five six month uh inside ethereum we
call it internally ZK and is very much
about that is how much we can push the
proving system Z is also based U it's a
system that can uh prove u i mean you
can build a pro programming rust it's a
RIS five uh compiler is a RIS 564 bits
it's a little bit different from other
projects but the full idea of this
project is how fast can we uh can we
move how short how fast can we generate
this proof this actually are these three
different I would say three different
pieces or three different projects
itself one is the pr itself Pro is a
generic PR so the idea is that you can
build uh your own PR that can proves
anything would say it's kind the
hardware layer you you we have the pill
two pill2 is based on um pill two is
based on um the pill one language that
we use in the zbm and allows you to do
an arithmetization and way we extended a
lot of the a lot uh of the we extended a
lot the pill to language the the pill2
language uh I mean making them more easy
for auditing uh this arithmetization and
mainly including um one thing that's
called vops that mainly means that
instead of having uh monolithic proof we
can divide the proof in sub proofs this
is very important because then we can
paralyze very well so we have a proof we
divide the work in different sub proofs
and then we AG them together this is the
main idea of how we can accelerate uh uh
the things okay so the the prover I mean
it's a generic prover so how it would
work okay this is the process that if
you want to build a any proof it can be
from a Fibonacci series if it's a kind
of a Hello World until uh I mean a VM
project that's in there or maybe some
whatever you want to build mainly you
need to build two things so you need to
build that intiation there imization is
in this um in the in this uh so we just
write the pill so is imization itself
you need to write what we call the
winess computation this is at the end is
filling it's a program that's actually
filling um the trace of this and that's
very much and with that you already have
aover so with this um well you compile
the pill okay so you get a kind of a
pill out format you get the rust you
compile uh a library I mean you get a a
dynamic Library
okay from the pill you get some helpers
so that allows you to build this Windows
computation easily okay and then here we
just run a normal setup Pro setup here
the setup is the configuration of the pr
itself some Starks configuration that's
just a configuration file here we
generate a normal approving key and a
and a verification key and then we have
the normal thing we have a aover for the
prover has an interface that you get an
input and this Pro generates the proof
and the public uh uh and the public
outputs and you can take the proof from
the public or put some verify in the
verify you see that's correct here okay
so this is the so this is would be the
schema that would that would work okay
um thing is that this Pro is generic I
mean you don't need to recompile the pr
it's just a u just a program that's
running there but can be a program can
be a service uh can be I mean um this
progr and this program can have like
different versions I mean it can be in
GP GPU in I mean you can it doesn't
change I mean you can have it's is a
generic for any the the idea is that
it's generic for any for any
circuit this program is I mean is is uh
it's open source um and is uh everything
is designed to minimize the latency okay
we will see later uh the different
things on related to that okay so and
then um let me just go back so
um this would be the pro okay but on top
of the prer we have a specific circuit
so it's a just just one uh so we are
using it's like a so the specific Circ
using P2 and that's implemented in P2
and we can use the pro that's actually
this um uh this dis is this uh let's say
R5 emulator kind of actually it's not I
would not call it an emulator it's a ZK
processor the thing the only thing is
that uh there is a direct conversion
between R 5 or even wasm or or other or
or lbm to this ZK processor it's a
processor that has only about uh 50
polinomial so it's very very lightweight
uh processor and really fast and and
really fast processor okay so
um and then it works very much like any
other VM in there so you can build a
program so you you build the the circuit
in in a normal program of course you can
test your circuit at the end it's a
deterministic program so you compile the
the the circuit you get a program and
then you have an input and an output
it's a deterministic program that
generates the circuit once you have that
that's the only thing you need you can
take this program you can generate I
mean you can compile using rust and some
setup and then you get a kind of a ROM
or if you want a you know an elf kind of
a program
itself um and then uh you can use the pr
I mean the pr that we saw before of
course here the the the zis the private
key the the verification key is already
already done because this is an a
specific application a specific circuit
for the approver but the prover is
exactly the same and then of course you
have an input uh a proof an output and
the verifier the only thing is that the
input includes the the priv private
input and and the ROM so you can prove
any any program that you want and of
course in the verifier you can you can
use the ROM hash so you you can use the
verifier
itself okay so let's go deep in how
uh Z I mean how how the architecture I
mean how this um uh circuit works well
as I told you before the circuit uh is
based on uh vcops actually it's many
there are many sub proofs each this
subproof there are different kinds and
this this works very much like a normal
processor we have like a a main
processor with a program with a ROM and
then we have a ram we have arithmetic
operations we have a lot of
co-processors um uh that can be
connected here okay uh so each one of
these is one some proof and actually you
can have for example arithmetic if you
have a lot of arithmetic operations you
can have a lot of subcircuits and all
them add them to the bus and they
connect them together this bus I mean is
not an electronic bus but this something
would say similar I it's more an
algebraic boss but this um we are using
here lock ups and here the idea is you
can have different subproof so you can
have the main processor you have the
arithmetic processor each one is like
sending things to the B the main
processor says okay I'm assuming that
this arithmetic operation is correct
okay and then there is the arithmetic
processor that's saying I'm guaranteeing
that this arithmetic operation with
these values is correct okay so the full
system is correct so one is adding to
the boss the other is subtracting to the
boss and at the end the boss means zero
if if everything is uh uh warranted and
the cool thing is that I mean in this
boss I can add arithmetic operations I
can add memory instructions I can add
whatever you what whatever you want we
can have we have a kind of identifier
but with the same polinomial we are just
adding and substracting different things
all all together okay you see the
arithmetization I'm not going to go in
detail on the arithmetization but I give
you the the big idea I mean um the
processor is not based in registers
registers in zi are relatively expensive
mainly because in one instruction you
are using in general one or two
registers so that means that there is
like if you have 32 registers you may
have like 30 30 columns that you are not
even using in that line so doing
registers in ZK is quite suboptimal so
the main idea here is okay we have like
so in so in each instruction what we do
is we go directly to memory we are doing
two access to memory we are reading two
things and we are storing back to the
storing back to the memory and in this
and this so this is the the the main
idea okay so we have only we have only
one one register actually we have a
couple of registers a program counter a
kind of a frame pointer or stack pointer
um in there we have this main so this
main instruction that can be an
instruction there so we have a way this
is a way to load the first register load
second registers I mean you can load
from memory or you can load maybe from
an immediate value or other um uh things
maybe we can take just the preview see
and things like that okay and um we um
we store the memory we generally we
store to the memory we can also for
example store to a program counter so we
can do a dynamic jump in there okay and
um we have the operations the operations
at the end is just throwing to the boss
the operation that you want to build so
the the the main stain machine is quite
uh simple in there and then we have some
um conditional jumps uh somehow I mean
this this logic there at the end we are
just so the operations is maybe plus b
equals c maybe with a carry or with a
some flag that you where you can do a
jump to one line of cord or a different
line of code so this is very a little
bit the the the the deepness the big
idea of the this itself okay and as I
told you this goes through this through
this bus okay and one of the advantages
and I want to see here I won't give you
details about the why uh this
architecture is very optimal for example
when you have an um a
multiplication so the six processor is
sending that and uh the arithmetic is
also somehow proving that specific
operation in there okay so you can have
this arithmetic operation but one thing
one optimization that we can do is okay
for example in machine there are a lot
of uh operations that are uh usual when
I'm doing for example 1+ one or uh 3+
one I mean I'm doing the small numbers
I'm going to do a lot of them in the in
the processor so instead of proving all
of them in the processor I can have um
another steam machine that's can of a
cash where I have precomputed operations
that are used quite often and then so so
the processor it's always it's it's
sending the same thing but then these uh
basic operations can be sended can be
proved back to the bus so that means
that for these small operations or for
these usual operations the cost I mean
the number of cells that we are doing
are uh very low okay can extend this
idea so we can have this processor
imagine that have a operations I can
have a usual operations table I can have
operations that are doing so a specific
State machine that's doing 32 bits
operations and another state machine
that are doing 64 uh State machines
operations just to save here just to
save uh space
okay this idea for works for example for
memory for the memory memory alignment I
mean what I'm doing in general most of
the process are doing reads and bries
that are aligned well no problem the the
processor is doing some memory operation
and the memory that just works in in 64
bits 64 bits uh words then you're doing
a read aligned read you get it from the
memory align read you get it from the
memory but what happen when you are
reading an an align it well we can have
a special St machine that's solving
these un aligning things and actually is
okay so you want a non-aligned operation
this solve so the the arrow to the bus
means adding to the bus the uh the the
other arrow that goes in the other way
is subtracting to the BS so okay I'm
proving this but in order to prove this
I need to do two reads operations and of
course some Logic for check I mean for
putting these two two reads in the same
in the same way and then of course the
same memory machine is doing this uh two
reads in there this allows us to do this
kind of techniques it allows us to do
for example continuations in a very easy
way so if I have a processor I mean I
have a I can I can I I can divide the
tion in different different slots
different different faces okay so it
this the first 100 clocks second 100
clocks and so on so I I can't I can't
divide them but at the end of the
processor so I need to connect I mean
the the next slot needs to have the same
state that when I finish well what I can
do is just send this uh state to the bus
uh and recover this state from the bus
and then connecting all them together
okay the final one the first one this is
because it's cyclic I mean Zine cyclic
and then disconnects the same with uh
continuations in the ram continuations
in the ram of course is not time frame
in the ram you want more address uh face
but so I can divide the proof of the ram
that can be big in smaller pieces and
but the idea is the same I have an State
transition function that goes line by
line but uh from the one chunk to the
next chunk I'm I can um send this the
state of the run to the bus recover the
state of the run to the boss the last
the last address that you are reading or
writing and then you can continue so we
can split also for example the ram in
there so this allows us to divide all
the work I mean there is no big state
there is no State machine that you need
a big things so you can divide always
the work uh in
everything okay here I as I mentioned um
this there is a direct conversion this
is important direct conversion that
means that you can use Ras or or any
other Pro or any other compiling
language is 64 bits you can use goang or
you can use C++ or you can use uh uh
even Java I mean there is a so um um uh
this 5 64 bits is is quite a standard uh
in there and as I told you there is one
um direct conversion one to one from uh
risk uh uh from risk to thisk we're also
have a kind of a side project that we
are um evaluating converting from wasam
to CIS and even Direct from LM to6 this
is perfectly possible and it can be
quite optimal because when you go to
intermediate code U you don't need these
registers and then you can uh have
better code in the processor but in
general um the cost of the
proof um of course the processor is
important but I would say that the
operations that are doing the processor
are even more important in general so
also the the mean the well it's not that
you are optimizing the processor and
then you get a better proof you need
it's the whole thing that you need to
mites okay um well this Advantage we
already talk most of them okay it's low
latency low latency low latency and um
yeah we integrate with the recursor we
didn't talk about the recursor but the
recursor is the idea is that you can
take the the any proof and then you can
uh build kind of automatically uh uh a
proof that uh Aggregates both proof for
example if you are proving two blocks uh
of ethereum you can get a a proof that
actually Aggregates this proof okay and
we have this recursor that's a tooling
that allows you to do that automatically
uh uh on this okay so latency how we uh
push hard on the latency actually there
is four pieces have not much time but
I'm going to try to go fast the first
one is the one that you cannot paralyze
okay it's like okay if I want to prove a
computation I need to compute that thing
okay so I cannot paralyze that
computation very much okay
uh and also if we are emulating for
example 5 I need an emulation so here I
can go as slow but we are trying this to
go as fast as we can currently we are at
running let's say the minimum Trace that
you need then to generate the winess
computation uh we can go I think that
there is margin here for at least one
order of magnitude Improvement then we
have the windows computation the windows
computation this is already done in
parallel so this can be paralyzed Um
this can be paralyzed uh
uh very much and you can even start
building this Windows computation while
while you are executing that also the
windows computation the idea is that
we're doing that work in the worker we
are not have like a central Pro we can
do that in the worker that means that
here we limit a lot the the the
bandwidth so we have one bandwidth we
don't have bandwidth requirements it's
minimal the quantity of information that
goes from the uh uh between the the
workers or aent I mean the coordinator
and the and the workers okay then we
have the Su proof building actually this
is the high work but the cool thing is
that because we can we can we have
control of what's the sides of the sub
proof then uh it's just a matter of
putting more subs of course if they are
cheaper and faster you will need less
Subs if are slower you will need more
and that's very much a matter of a cost
but not a matter of a latency because we
can control very much this uh proving
this proving time okay and then the
other last is okay then we need to
aggregate okay this is probably where we
have the bottleneck but uh I mean the
good news is that we are getting much
much much better and uh this number 10
seconds we already get lower to that
here as mentioned plony 2 has very good
circuit for there and optimizing this
aggregation circuit is uh super is super
important okay there is a talk I think
in 1 hour or so I think it's in this
room that will give more details on this
U uh uh optimization parallelization all
the proofs that I mean all the proof we
are running in a super computer and
doing experiments and see that all these
numbers get very very good and this
scales uh very well okay future plans
lot of things to do a lot of things in
the B lock a lot of optimizations that
uh we want to
implement and uh you can try it it's
working right now we have a basic thing
it's working the last time I said that
in the in the in in a in the scenario
somebody created a tornado cash and was
it with a nightmare but but but just
this is work in progress okay so I would
say at this point it's the status that
it's working requires some refactors of
the pizzas some cleanups some
documentations and we hope that let's
see if in the coming weeks everything
looks nicer and uh we want to build the
it has no promil I mean know these State
machines are limited but you can build
any program and you can prove any
program for these pre compiles or for
this specialized State machines we we we
wait uh I mean take maybe uh two three
months still to to to to complete okay
and that's very much my presentation
enjoy
it thank you very much let's go through
some questions so what issues did you
run into using risk V 64 that risk V 32
wouldn't have
I mean well these are we have been
checking what's better what's worse here
there are uh I mean there are pros and
cons I would say that the big the big
Pros is that when you are doing
especially when you are running rust you
are doing a lot of M copies I mean you
are moving a lot of uh memory
information and when you are using 64
bits this is much much much more optimal
I would say this is one of the things
that we saw that there is a lot of uh
copies uh in uh moving back and forth uh
uh in the place and because uh also the
the the corrent kurrent uh I mean
corrent systems are 64 bits so
everything is much more standard for
example if you want to build I mean if
you want to use rust is 32 bits is okay
but if you want to do go for example you
cannot do it in 32 bit so you can do in
but again the the different test that we
did is that
we're slightly better doing in 64 in 64
bits so that's why we stick it at 64
bits and how will this be different than
sp1 risk
zero uh well uh we need we still need to
do some benchmarks and compare but uh
here the thing is that we are designing
not for cost I mean that we are here we
are want to push uh as hard as we as
hard as we can in uh in doing the speeds
uh as fast as as as as fast as uh we can
so it's difficult it's difficult to
compare is difficult to compare yet also
we have some um this uh machines that
this special State machines that needs
to be finalized but uh I mean the
numbers that we have seen that that we
are much faster especially in CPU uh we
are working very much in the GPU and the
the numbers are quite promising but
again I don't like to talk yet about the
numbers because it probably would not be
fair and and and uh things needs to be
more um set it uh I would probably both
sides to start getting some real
comparations from a developer experience
point of view what does the developer
need to do to encode the chain rules
into zis just write the RAS code I mean
just just write a program that do do the
whatever rules that's in there uh just a
side note here is take care on the
security of that is um um when you are
proving when you're getting some input
and getting some output the input uh you
can you can still have soundness
problems if you are not writing the
right way so you need to understand a
little bit how the things work even if
you're writing a programming rust
because there are some security issues
that can happen there but yeah at the
end is but at the end is writing a rasco
and are there any drawbacks that come
with
cisk I mentioned these security things
that uh but this is common in anym okay
you need to you still need to understand
a little bit what's behind but uh it's
much more practical and it's I mean it's
it's much easier to to to write a r code
and AIT an a Ras code that not an
assembly written in some specific
special processor
there don't all these improvements by
build built specific Hardware are they
better than making optimizations on VMS
I think that's what that
says maybe uh if they do uh we will We
Will We Will We Will uh Implement them
but they are not hard to build this
Hardware I mean this is not like a a
real Hardware that you need to build
like uh machine a machinery and this is
just a program and it's Electronics you
need to have them the right way and once
you have it you they're already there I
don't know what these mean so maybe you
could read them out if they make any
sense to
you um yeah this is uh I we would
probably need the the context but this
is at the end is uh is the position of
the this is the position of the
registers because we are emulating
register registers in R 5 so we are
setting a specific positions in the
memory that actually are the registers
and this is just defining the this is
just defining the constants that defines
the the registers in in there there
question in there yeah that's very much
the the thing I mean I can't we can give
you the tail I mean there is on that but
that's yeah that's the developer needs
to write uh P do not at all not at all
unless you want to build maybe some
specific State uh some specific uh State
machines I mean some co-processors or
things like that that then you can
extend that way but the idea is that the
the final process the final person
that's writing in R just write in R and
that's it great give a hand uh for Jordy
Bina and we will be back after lunch to
talk about client diversity with Daniel
erner from Basu
oh a
h oh
bre
a oh
oh oh
and m
SC all
m m
n
oh e
welcome back from lunch I hope everybody
ate um so next up we're going to have um
from Basu Daniel learner talk about
client diversity welcome
Daniel so hello everybody my name is uh
Daniel larner I'm a b developer at
consensus and I'm going to talk about
the benefits of client
diversity so first of all let's start
with who here knows what client
diversity is can you raise your hand if
you if you
know okay I think almost everybody so
for the people that do not know in
ethereum to to use ethereum we have
different software programs
especially since the merge we need two
pieces of software we have the execution
layer which is basically the evm or
whenever you call an RPC endpoint
normally like gut balance if call and we
have the consensus layer which is the
proof of stake
part and for each of those two pieces of
software we have a lot of different
implementations
on the execution layer side we have GF
which is written in go NE mind in net
Basu which I'm working on in Java Aragon
in go ref in Rust and etherium CH in
typescript and the same on the consensus
layer we have prism which is in go
Lighthouse rust te Java nimbos is
written in Nim which is like a variant
of um C or C++ no I'm not sure we have
loar in typescript and we have
grandine um in terms of distributions on
the execution layer side historically GF
is what we call a majority client this
means the majority of users are using it
um on the consensus layer side the
distribution is more even mainly because
they have all started at the same time
they have all started more as it
emerge um so that's a bit better so in
the end why are we doing this so what
are the benefits of doing the same piece
of software several
times and I'm going to use this Iceberg
metap for here basically starting at the
the tip of the iceberg which I think
might be the most obvious answers to
this and then we are going down to the
less uh obvious benefits
so the first one is stability that's the
very top here we have an example where
vitalic himself wrote on readit
on the 24th of November
have identified the problem and now we
are in the process of testing a fix for
a release so basically what happened
is there was just a bug in G and at the
time of writing this there was already a
second client which um which was
parity and basically what happened is
the two clients processed the same chain
and at some point because of the bug
they they forked
off and we had two chains so after a
while of debugging they needed to find
out okay which is the correct
one and basically fix
it so what what happened here is that
even though GFF which was at the time
the majority client had a bug the chain
never went down because there was parity
was still there basically to continue in
meantime parity continued to correct
fork and once GFF was fixed um GFF
rejoined this
Fork so here is is basically I think
maybe the the most obvious one if you
write software more than
once every every piece of software can
have a bug but the two versions of the
same protocol have exactly the same bug
is rather unlikely so we
can um basically make sure that one of
the versions will work normally one one
at a
time then the other thing is correctness
and error
detection how do we even know that
something the protocol is wrong so I
mean there are very obvious errors in
software that's normally when the
software is
crashing but what if the software just
has a bug and it calculates
something
incorrectly here we have an example from
the 15th of August 201 10 long before
ethereum has existed this is the Bitcoin
talk forum there is a user that says the
value out in this block is quite strange
and then here at the bottom it says 92
b233
m720 368
Bitcoin basically what happened is there
was a bug in the Bitcoin
software and
somebody triggered the bug we don't know
if it was on purpose or not twice and
created 180 billion
Bitcoin even for people that do not know
a lot of Bitcoin they most probably know
that there is a very hard limit of 21
million Bitcoin so 180 billion obviously
is way too
much and why I chose this example
is Bitcoin traditionally
chooses only to run one client
normally what happen here is that this
client had just a bug It produced in
this case too much
Bitcoin but the chain still continued to
run there was nothing obviously wrong
with the chain just that this one user
was really looking at the transaction
was looking at the output and that's how
the error was detected in the first
place
this in the example before from ethereum
was very different
in ethereum two pieces of the same
software run and then we could see that
they diverge so it was very very obvious
that something is wrong here it was
really by luck that somebody checked
this and then at the end at this time
Satoshi was still around they fixed the
buck basically rolled the chain back um
there were like 50 blocks afterwards
produced they they were afterwards
invalid um
and then the were the head Val chain
again then the next
point is not just avoiding
errors but especially avoiding
catastrophic
errors here
um six months before the merge dunrod
fed one of the ethereum foundation
researchers wrote an article that says
eum merge run the majority client at own
Peril so why did he write this
um before in proof of work in the first
example that we saw when one of the
clients had a bug it in the end produced
an invalid Fork but you could always go
back with the merge and with the change
to proof of stake we have a New Concept
which is called
finalization finalization means at some
point normally after what we call two
Epoch which is around 12.8
minutes the chain finalizes if it has
more than 2/3 of the votes and you
cannot go back
anymore this is a very very nice
property because you know for sure if
your transaction was in a block that has
finalized it will never revert
again but there is one one problem with
this I I don't want to go into too much
details because it's basically not the
goal of this talk but in the
finalization process if a client a
majority client who has more than two3
of the notes or of the stake has a bug
it will produce the invalid chain a and
it it will attest which is basically
vote for the two blocks these are the
two error uh the two red
errors even if the bug is detected
because we have other clients who will
let us know
that and the bug is
fixed all the clients that were on chain
a cannot go back to chain B anymore
because in order to do that they would
need to vote Here For What what is
marked as the
X and this is not allowed by the
protocol because they basically jump
over one of their own
votes and this is what we call a slash
offense slash offense means the
validator does something that can cause
the chain to not find consensus so we
are not sure which of the two chains is
correct and this is what could happen
here okay so this this this was a very
very serious problem and D Ro wrote this
like half a year before the
merge so the most logical outcome was
probably would be that people would be
aware of this and people and validators
would make sure that no client had more
than two F at least that's what we
thought the reality looked very very
different so this is the the client
distribution from beginning of this year
and GF had around 84%
of the of the stake of order the nodes
so this means we had a ticking time bump
for one and a half years but basically
one consensus bug in
GF would have triggered the outcome
before and if this would have happened
we would have
destroyed billions of dollars of value
in if in order to revert to the correct
chain Okay so now we had this ticking
time
bomp what what what should people do how
how I I I'm one of the developers of a
minority client so we tried our best to
to make our software
competitive but then unfortunately Murph
is law hit and we had inbo on the 6th of
January a bu that basically took the
note down and the second one is from
nethermind which is the number two which
was two weeks after So within two weeks
the number two and the number three
client had a problem so we had now the
issue that GFF was had already this
huge majority plus we had two
problems
surprisingly those two
events led to the outcome that people
finally were talking about the problem
with the
finalization of a super maturity
client here a big shout out to the to
the if Staker Community to nixo to
yoron they they really educated people
about this
problem and stakers and validators
finally realized okay that's that's a
huge issue we need to do
something and that's
why right now it looks like this so G
has gone down from 84 to 52 so it's
below the 23s the issue basically this
was outline before it cannot happen
anymore B and Ne mind have both
increased a lot so now the situation
looks much better um but what this also
means is cant diversity is a choice the
community has to choose it if not even
though we have several implementations
of the same software it will not
happen um here is one example where this
does not work if people are thinking
about Bitcoin they must probably just
think about one client in reality
Bitcoin has 14 different clients some of
them just on mobile because Bitcoin is
more light client friendly others are
full nodes but despite
that
Bitcoin core so even
though a lot of clients would be
available the Bitcoin Community chooses
to run only
one which basically means they do not
get the benefits from client diversity
that they actually could have very
easily um then here is another Point
that's maybe already um a bit more
hidden is to make the specification of
the protocol easily
accessible um
when several teams across the globe work
on the same piece of software you are
basically forced to first start with a
specification you're basically forced to
First write down okay what actually are
we going to do
it and we have several resources in
aerum for that we have The aerum
Magicians Forum which basically normally
is where discussions are starting about
changes we have the EIP process which is
then the actual spec of the
changes we have the etherum execution
spec tests on the execution site which
basically means all the changes that we
are doing and all the protocol rules are
available really as as tests that you
can run so all the clients can run the
same test and this is very clearly
defined what is the expected Behavior
um another thing that we have that is
less blind spots with Cent diversity you
will never have no blind spots but at
least you can reduce your blind spots um
what I mean with this special um
is when we look where core developers
are located we have um a big number in
North America big number in Europe and a
big number in Australia this means
geographically more more or less the
distribution is not so bad but we have
for example right now no team in Asia no
team in Africa no team in in South
America um if people were yesterday at
Justin Drake's talk about the beam chain
at least the situation should improve
for Latin America and for Asia and we
will have two new
teams and basically the goal is that
they can bring their own
view their own life experience into the
process and they can help us reduce our
blind spots which developers from the
from the Western World maybe do not see
so for example people who use stable
coins in Latin America or Asia I think
most Cavs right now are are not in
situations where they would really need
this um then when you have different
clients those clients can do
different Improvement and experiments
here I have just for every execution
client one there there are a lot of them
but we can quickly go over that NE mind
has for example done a lot of
performance work recently they have
reached one gigz which is like our goal
for layer twos in bestu we have a
parallel transaction processing so right
now on etherum inet you can do parallel
transaction processing without problems
which is also something
um that was long ago also for l2s Aragon
has worked very hard to make archive
nodes run on consumer Hardware
especially the dis requirement went down
from like 16 tab to three or
four ref has introduced execution
extensions which basically allow you to
modify the client without forking it and
another example is
EF um if you don't know much about youf
if you're a smart contractor you will
like it because it basically gets rid of
the stack to deep
errors and it finally allows us to
safely increase the smart contract size
limit eventually and this is mainly
driven by the minority
clients and then if you think okay I'm
running majority client what benefit do
I have the benefit is that the majority
client
eventually
can copy the Fe features for example
here this is Peter the team lead of the
go ethereum of the G team tweeting out
that they will the XX the execution
extension support from ref will also do
it to G so because one of the minority
clients introduced it finally the
maurity client gets it at
well here is another slide which is a
bit more abstract but you have a lower
risk of protocol capture or failure
there are if you have just one team
there are different times of of of
of attacks a government could do they
maybe cannot detect the protocol but
they could
infiltrate the team or they can pressure
somehow the team to do to push a change
that uh they like a team can withhold
updates something that the community
maybe really wants that the team cannot
force the community to run a specific
software but the team can say okay this
one update we do not like it we will not
ship it and then the community will have
a very hard time to get it and simply if
you have one team they can just
eventually abandon the client so then
again you have a problem then we go to
the last point which is in the end
permissionless
contributions uh to the protocore this
is very abstract but in the end what
this means if you have client
diversity it means everybody can become
a ctive including everybody here in the
room so if somebody is interested in
this here in the slide we have the
different repositories of the clients
this is if you are interested in in
programming um there also another things
if you want to just keep up with the the
protocol on Twitter you can follow Timo
or Christine Kim they they always share
updates you can join the Discord
server you can look at the EPS there
there are a lot of things to do so
that's basically it so thank you for
your attention
and we will go through questions um if
voted in Fork a can later attest in Fork
B when the fix is released can they do
that without getting slashed yes so this
means if the if the majority client has
less than two3 um that is possible yes
so the the the main the main thing is
really no client should have more than
two3 of of the staking votes
um so we have some more time for
questions we have more questions in the
queue does anybody want to ask a Live
question we have one over here oh there
is one oh how do you get the numbers on
different clients running different uh
running nodes yeah okay so that's a good
question um so we have no reliable way
of of of doing that
um people do some sort of fingerprinting
where they analyze different blocks that
are proposed post and then they they
they can basically estimate which sale
clients they are uh for the execution
clients we do not have that um there
were recently proposals we have like one
field when you propose a block where
people can basically write random data
um there are proposals to basically
write in which which e and which CL you
run and then we have a best better
estimations but the numbers that I
showed before they mainly rely on
self-reporting so the big staking
providers in the end report the numbers
and then there is like a huge chunk of I
don't know one3 of the network we we do
know um but the for for the worst case
assumption we we just say it's the
majority client and and still with this
ver case assumption no client has more
than two FS but yeah it's we do not have
exact numbers we only have approximation
of the numbers
thank you um could you Steelman the
argument that Bitcoin puts forward for
having one client and why it's wrong
yeah so one client um in the
end
means um there is less politics involved
maybe in discussing changes so in a fum
case you basically have to convince
different teams that they they want to
change although Bitcoin is quite
resistant to to change by itself
um the other
approach I don't know I mean is is is
like what I mentioned before with with
the capturing of a team um but yeah so
so for me is actually
hard to Steelman this um you you just
avoid maybe I don't know certain errors
by using more than two clients but yeah
as I said for for me the benefits far
outweigh the the downsides of of having
just one
client any more live
questions great can we give a hand to
Daniel for his talk thank
you and in seven minutes we'll have a
talk from um an Aragon client Dev
all righty our next speaker is a core
developer at the Aragon execution layer
client and he is here to tell you about
the newest version of the client please
welcome Mark Holt
where do we
go okay hold on a sec I get the slides
in the right
place um yeah hi I'm Mark Holt I work on
the Aragon team um and basically what
I'm going to talk about today is Aragon
incarnation of Aragon which is just
coming off out of alpha so we're
expecting by the time we get to um Petra
to have that as the client we would like
everybody to use so the um purpose of
this talk is to talk about Aragon and
what it's doing and why it's slightly
different from other clients
um and what do I oh so yeah so Aragon a
bit about us Aragon is a um is a is a
client team now although we're
principally used for execution in fact
one of the things about later versions
of Aragon 2 and Aragon 3 is actually
it's combined client it basically does
both CL and the L in one application um
now it was based on a turbo Turbo gu
which was a project which I'll talk a
little bit about um but it's essentially
built to become mainly an AR us as an
archive client which is you see where're
down at 2% of usage um and that's
because basically we get used for um
people who've got who've got an interest
in the whole history essentially and
historically we've not been quite so
good at at operating for people who are
purely doing validators or interested in
the tip of the chain now hopefully with
Aragon 3 that will change a bit um so
what I'm going to talk about today is
just an overview of what Aragon 3 is the
journey we've been through from Turbo
which is where we started from to where
we are now um I'll explain a little bit
about the architecture of of Aragon 3
because I think it's important in um in
understanding how we think it's
different from other clients and and
what what the implications of that are
and then I'll talk a little bit about
the future of of what we've got um
so I called this um this talk a Aragon 3
a paradigm shift for clients and that's
partly because I think within the Aragon
team itself we think about the clients
slightly different from other clients at
the moment especially in I I guess the
ethereum space in that we don't really
think about consensus versus execution
because we've got a combined client um
what we think more about is what happens
at the tip of the chain and effectively
what happens after that because a lot of
the technical work we've done is about
the transition of data as it goes
through the um life cycle from coming
out of a mempool to getting into
consensus and then you know what happens
with all of the data afterwards as it
gets into the um in in into the archive
space because I mean for us we never
throw data away and that includes both
CL and E data so we're basically working
out the how do we how do we store and
distribute this stuff so we've kind of
got a model that chain has an
application that thinks about chain
dissemination which is you know the live
chain and what happens when it operates
in real time and how do we work that
effectively and then there's a whole
process of once you've basically got the
chain data how do you then distribute it
efficiently to other nodes um and we
kind of split that and we don't
necessarily do that through the entire
the um the same life cycle as everybody
else so um I'll talk a bit to start off
with about the Aragon Journey because I
I think it's interesting it's also
interesting in terms of the last
conversation we had which was about
client diversity um I think one of the
interesting things about client
diversity in the context of Aragon is
it's not just for the live chain I mean
one of the things about client diversity
is has had quite a long journey to get
from where it started from to where it's
ended up now and that's effectively been
funded out of the community because it
accepted there wasn't a one one siiz
fits-all and because there's not a one
siiz fits all if you believe enough
about something you'll get the backing
to keep going although there are several
other people doing the same thing and
that can lead to different
outcomes um so if we um if we talk about
this where do we start from so um I
think Alexi who's actually in the
audience here was was talking in Devcon
which was a change the way guest stores
data so that was in you know Devcon 4
we're now several iterations through the
um through the Journey and we've we've
probably finally come to the point where
we're delivering on the original Vision
um and I think that's that's another
thing about the
um the space that we're in is that that
actually if you look at Aragon it's had
the space to kind of learn over seven or
eight years to get to a point where it's
actually delivering a product without
the kind of pressure of you get you got
get time to Market and if you haven't if
you failed within the the first couple
of years you kind of you've got to go
off and do something else so there's
there's longevity in this process now I
think if you look in Turbo gu that what
it was doing was looking at the data
storage and saying if we have a look at
the way data is stored in and do
analysis of it in in the um in the
clients we can do better with a storage
model effectively and I think the the
turbo gu piece of the journey was about
essentially how do we make storage more
optimal and if if you look at the
numbers um the the lesson there was you
look at the majority client and we we
with the analysis that we did and and
the work we got down to a fifth of the
storage model so you you get to a
situation where the effort was worth it
to get something slightly different
essentially now I I
think what that does is says right
there's a product here and people start
using it because there's a there's a
benefit for people because an important
process so that's what got the whole
thing kicked off and then essentially
what we ended up with there is an
ongoing development of Aragon which took
that original idea and de pushed it to
its um next conclusion and the the next
stage of this journey was the
realization that actually if you start
caring about the data and the data going
into a database you start thinking about
what the day space is and asking
yourself the question can you optimize
that and one other thing de pushed it to
realization that actually
if you start caring about the data and
the data going into a database you start
thinking about what the database is
doing and asking yourself the question
can you optimize that they pushed it to
caring about the data from the data
going into a database you start thinking
about what the database is doing and
asking yourself the question can you
optimize that they pushed it to its um
next conclusion and the the next stage
of this journey was the realization that
actually if you start caring about the
data from the data going into a database
you start thinking about what the
database is doing and asking yourself
the question can you optimize that they
pushed it to its um next conclusion and
the the next stage of this journey was
the realization that actually if you
start caring about the data and the data
going into a dat database you start
can you opt de pushed it to its um next
conclusion and the the next stage of
this journey was the realization that
data and the data going into a database
the the next agage of this journey was
about what the databas is doing and
optimize
that where We've Ended up um so more
about how that works by giving you about
how that works by giving you um a bit
the way that the um eron architecture
works so you can see what we're actually
doing inside of the model so
essentially a lot of um what arigon does
and a lot of what the team work on is
this kind of process where of what the
team work on is this kind of process
where um we we think the model
so essentially a lot of um what Aragon
does and a lot of what the team work on
is this kind of process where um
we the model
is this kind of process where um we the
model
is this kind of process where um we
is this kind of process where um we we
think the model so
essentially a lot of um what Aragon does
this kind of process where um we the
think about essentially Distributing a
verifiable binary version of the chain
from one machine to another essentially
and what this diagram is is showing you
you you've got a set of pages and
they're all hash
verified uh now what what are the
implications of all that um uh process
well they're basically what you end up
with is very quick sync performance
effectively so the big difference
between Aragon 2 and Aragon 3 is the
amount of time it takes to s something
and this is um you see this particularly
on uh large uh chains so um basically my
role in The Aragon team I'm mainly
working on polygon rather than rather
than ethereum than rather than ethereum
page cache effectively operating the
chain and I think that with that I'm out
of time and I'm done thank you
so two of these questions I'm going to
combine um which is uh how do you
compare in terms of speed and cost
efficiency um and storage uh compared to
the other execution layer
clients um depends which client so
like so we're we're I think we're
probably still and don't quote me we're
about a fifth of the storage for guest
on on a reasonable size size chain um
the others I'm actually not quite quite
sure about um are there other pros and
cons of running um Aragon versus any
other execution layer clients um yeah so
Aragon is good in in storage performance
and its RPC layer it's not so good if
you're doing things like validation
because we simply haven't worked on that
as a you know we've optimized the
storage not the interactions um but I
think that is less to True with Aragon 3
effectively great thank you um how how
much bandwidth overhead does Aragon
introduce to push verifi data across the
network
um as much as you want to give it so
basically what you can do when you run
an Aragon node is you can tell it how
much bandwidth it wants to give away um
and it
basically if you don't want to have that
turned on it doesn't take any it doesn't
take any overhead if you if you're if
you're conversely a seeding node you
know it'll it'll run as much bandwidth
as you want to give it um basically got
a lot of questions coming in at the last
hour is Aragon 3 going to make the
support of other EVMS more easily what
about
l2s um yeah I think it is I mean one of
the things that we're explicitly doing
with Aragon is doing L2 support I think
the the big difference for us in um in
is we'll spend a lot more resources in
in in actually actively working with L2
chains to get an L2 version of of Aragon
and one of the reasons for we work with
more chains we're simply building
components because what we want comp
componentization is so that we can we
can have a core Aragon that does the
database thing and then as we work with
more chains the componentization is so
that we can we can have a core Aragon
that does the database thing and then as
we work with more componentization is so
we work with
he
blockchain test can not only have
individual trans transactions but also
um they have individual transactions but
also um block contain blocks and these
blocks con contain one or more
transactions so they test slightly
different things or test slightly
different things or concentrate on
different things so state test can test
op codes or gas usage and a main part of
our work is really to verify smart
contract interactions um and we can
verify that trans transactions that
should get rejected do get rejected
and blockchain tests validate block
progression from block to block block
rejections and Fork
transitions so before we go to the new
let's have a look at the status qu at
the merge and see what the state of
things worth for testing at the El um
back when we met a Dev in Bogota in
Devcon
repository that's managed gen test
generation or the body of tests is eum
tests and this is a huge Corpus of tests
mainly curated by Dimitri who's sitting
right over there um who did created an
amazing body of tests um later joined by
Ai and you can see that there's almost
Cancun and this these test cases are
written in yaml and typically by hand um
and they can contain they contain
comments as well about what the test
does and then they get generated by uh a
tool in another repository called retest
eth which generates Json test fixtures
using a reference evm
implementation so the test fixtures are
then so this process is called filling
the test and the reason is that the test
fixtures contain um much more
information about the test in particular
all the changes in the post in the state
and in importantly the state rout which
is basically the fingerprint of a change
that you can really verify that every
client did exactly the
same so in
complicated tests and so instead of just
writing these yaml files by hand he
started generating uh many yaml files
using a node nod script like using
JavaScript and this allowed him to
create many test cases
um by looping over op codes for
example so we get to programmatic tests
and generating tests
programmatically so around the same time
in 2021 like client was at one of the
first interupt meetings in Greece and
was working on account abstraction and
wondering how can we test that there's
so many parameters that we need to
change in so many test cases that we
need to write how can we possibly manage
this complexity by writing yaml files
and he also came to the same conclusion
that we should have programmatic test
generation so what like client did was
um he sat down after the interrupt and
wrote a testing framework in a
repository called testing tools which
specified the tests as Python and then
generated Json from the python and so
this makes it easier to Define new test
cases and parameterized test
cases so he he worked on this for about
two months and then this repository kind
of went into hibernation and didn't see
much work on it well actually no no work
until Devcon 6 so at Devcon 6 everyone
was ecstatic that the merge had gone so
well and it was very forward-looking
that people were seeing what how are we
going to handle testing all these
complicated features that are coming
into the evm in the upcoming hard
for and so there was a discussion about
what what kind of framework can we what
can we use or what should we write in
order to handle this and like client
piped up and said oh I I think I've got
a project that that could be useful and
so this became ethereum execution spec
test which is the repository that I work
on
today so Mario sat who was a protocol
tester at the time sat down and um um
started writing the first test cases
building out the test test framework a
little bit broader and was then late
like soon joined by uh Spencer in
January of
eips included in the Shanghai hard fork
and in the first release for Shanghai or
the final release before the fork you
can say they had 194 test cases to
handle the new features coming into
Shanghai
so Shanghai really showed us how
powerful a programmatic test uh test
framework can be and how easy it is to
write test cases in
Python at that time the repository used
completely custom code to collect all
the test cases and like generate the
test Json and although we're not writing
test like unit tests we had the idea
what if we just use a standard uh uh
test framework to job for us and so we
rewrote the framework to use py test um
which is like the de facto um test
framework for Python and pest has a lot
of advantages it's extendable via
plugins and there's a large existing
ecosystem for plugins so if we ever need
a new test result format we can just
install a new plugin and get the test
results in Json um or an XML or an
HTML um you can also add your own custom
uh plugins which is very important to us
because that's basically how we've
implemented all our commands with in
East in order to generate tests and
later we'll see execute
them it allows for easier debugging and
last but not least it means that we can
really easily parameterized test cases
and as you can see in the screen chart
which is from our
documentation um how heavily we
parameterized um um blob transactions
for example so what you're looking at is
test valid blob transaction combinations
and so this is a blockchain test that um
has one to six
transactions um and each transaction
contains a different number of blobs and
we test all possible combinations that
they're accepted by clients and we have
an accompanying test for invalid blob
transaction as well and so essentially
to parameterize this test becomes one
one liner and if the spec would change
and the max blob uh count increases we
can change it in one place place and
generate many more nice
tests so this is really accelerated test
development and you can see in the
Cancun release we had over 2,400 tests
included in that just for
Cancun so this has also really helped us
to create a contributor first
repository we really want this should
not be a dark corner of protocol
development we really want EIP offers
EIP implementers even white hat hackers
anyone to come along and use this
repository we want them to come and
write tests there going to soon going to
be a new tool to help you get started
interactively thanks to Rahul who was
being an EPF fellow and we'd also like
people to be able to generate tests from
a transaction hash of a bad transaction
on a devet for
example um automatically so you generate
the python code directly and we also
want people that even if they're not
directly contributing to the repository
implementers after they've been working
on their implementation and wondering if
Corner cases are covered in the test
cases they can come to our repository
and look at our documentation browse it
and really check whether the coverage is
there that they expect it's the corner
case they just thought of is it already
in the tests or should they come and
pester us to make it or even add it
themselves this has really helped us
unlock parallel like development for
multiple Forks in parallel um and for
Prague we've got 2,500 test cases and in
parallel we've been also implementing
tests for the upcoming fork for the evm
object format where we added a new test
format to validate validate eof uh B
code and we have n 9,000 new test cases
already for eof and this is really a
huge thanks to the ipsilon team and to
Dano whove done an amazing job of um
writing these tests and contributing to
our reposit
also a big thanks to ignasio and Gom and
Spencer from the testing team um who
have contributed to adding the
infrastructure to the framework in order
to test vericle so it's already possible
now to fill and run existing tests until
Shanghai for the vericle transition and
the witness has already been added to
the fixture format so we're ready to
test that when we move closer to verle
so at this point we had a relatively
usable filling framework for generating
tests but we really missed something we
really missed the feedback so if you
want to really test a client you can't
just fill the tests that's just
generating the tests and we mentioned
before that we use an evm reference
implementation to fill out the features
so we can get a state route that we can
compare to other implementations this is
a differential
test and if you want to really test a
client you've then got to take this
Jason and then test the client by
getting this other client to consume the
Json that the first client produced so
it's a two-step process and we were
missing fast feedback within our
repository so we then added three uh
commands for um us as test developers to
quickly run the tests against a client
the first one consumed direct you can
execute or run run the test against the
client's native consumer and the last
two consume rlp and consume engine um
allow you to test a client in the hive
test environment using different C-
paaths either by loading rlp encoded
blocks upon startup or via engine new
payload these commands were in thank
thanks to the modal AR architecture
we've created using US Pest plugins and
um we really use combinations of these
plugins in order to achieve um the
commands that or the the tooling that we
we need in the reposter and Mario came
up with an excellent idea that to extend
the framework to allow execution of
these tests on live networks so he added
the execut a command which is allows us
to attack live Dev Nets which we just
did in the framework uh in the workshop
a couple of hours
ago so the execute
command doesn't generate Json fixtures
it takes the test cases generates a
transaction and executes it against a
client using the its RPC end
point this really unlocks a totally new
use case for our tests and really allows
us to get out of the staging like
setting that we've been executing these
tests in until today and run them in a
more production-like setting so we can
really run these tests against Dev
Nets so we've done a lot of work over
the last year or two years to improve
the lives of test
implementers but we're not done yet we'd
really like to also help improve the
lives of client
developers one large job what still not
done is we'd like to merge e the the
Corpus of tests from ethereum tests into
East and um we'd also like to um this
would mean that clients can then they
only need to download one artifact
because ethereum tests are still they're
still very important to consume and um
at the moment client teams have to
develop uh to consume tests from two
different sources and once we manage to
merge these tests we can catalog them a
little bit a little bit better and
clients only have to depend on one
artifact to test their
clients and as you can see we've
developed quite a lot of tooling over
the last couple of years and we'd like
to be able to provide this tooling to
client teams so they can use it in their
test Flows In order to get faster
feedback on on their performance on a PR
basis so they can rapidly iterate on
their
development for that we also would would
help if we had faster test execution
Hive is quite slow for example because
this test environment is a system test
which instantiates a client
in a Docker and so and this this client
gets the docker container gets pulled
down and started up for every
test we'd like to make this a bit faster
so clients can get faster
feedback additionally we'd like to
enable uh easier test debugging so that
clients can really run um the same test
hopefully if possible in their native
environment so they can drop into their
debugger um when they need to in order
to detect to find out what the problem
is when they're running the test
we also like to improve the development
cycle so our team has recently the east
team has recently merged with the
execution specs team the eels team that
handles the py implementation of
ethereum specs we we've merged with them
to become one team called
steel the specs and testing of the
ethereum execution
layer
and we now def uh fill all our tests the
reference implementation F filling test
should really be eels and it is for all
Forks up until including Prague and Su
prag this would unlock a kind of test
driven development it's a rather coarse
test driven development because you need
an endtoend test obviously for your
client but it does mean that when a
client imp implementor comes to write
his Implement his code for
thep he will have tests ready to go and
he'll be able to check whether it's
there so the F feedback will be f fast
instead of having to implement it and
perhaps wait for tests to arrive from
another
client another thing that we'd really
like to add would be EIP versioning so
there's many different places where an
EIP is defined or implemented there's
the ethereum eips
repository there's um the
tests and then there's all the client
versions and the specs of course so
there's multiple versions where the eips
are defined and if we can track the
versions across all these components
more easily we'll be able to make a
statement about whether these whether
these components are even compatible
before we test runs uh run tests sorry
so we can even just
basically um xfil the tests and we know
that we expect a failure and we don't
have to try and debug something that
doesn't make sense because the specs are
just
incompatible and last but not least we'd
like to improve coverage it would be
amazing to be able to hook a fuzzer into
the tests so we already have a whole
bunch of edge cases for
eips and if we could hook like Define
which parameter you'd like to fuzz for
these edge cases um it would allow us to
run these via execute and um get more
test coverage and we'd like to improve
our documentation even more and
encourage people to come and look at our
test cases and try and contribute to new
ideas ideas to increase
coverage so I hope you see that the
title of a talk is not just a meme um
our repository does protect by allowing
clients to consume the tests but now we
can also attack clients on dev
Nets so thank you very much um one of
the main messages of the talk is really
that we're here and any client ever
anyone who's interested in testing on
ethereum can reach out to us and you can
find all our contact details in our user
document or in our repo document ation
just go to the docs you'll find Linked
In the repo go to getting started and
getting help all right thank you very
much let's take some questions starting
with the most upvoted can you
programmatically check test coverage
that's an excellent question and uh
Dimitri's been working very hard on this
and uh we now have um a GitHub a GitHub
action that actually does exactly this
so it detects if um if a test has
changed and then it will basically fill
test um before and after and run the
fixtures against evm one from the
ipsilon team and get a test coverage um
on evm one before and after and then
literally Check Line like what's the
line difference in in coverage so yes
were significant bugs found using this
testing framework
I mean we hope to catch the bugs early
right so we we don't want to catch the
bugs on devet really we want to catch
the bugs as soon as possible while the
client is implementing and so yes but
hopefully you'll never hear about
it up until Petra which EIP was the most
challenging to
test up until P not including Petra not
including
pectra huh
let me
think I would say probably 48 for four
yeah our test fixtures in ethereum Spec
tests already included in ethereum tests
um yes but um we'd rather go the other
way so
um we consider the future of testing
ethereum spec tests and so we'd rather
get ethereum tests in execution spec
tests as an interim like solution
Dimitri included or filled our fixtures
from retest e using our framework and
included them in retest e uh in ethereum
tests like the test repository but
because our tooling is our repository
and we can generate releases more
quickly I would prefer to keep our
releases in execution spec tests and I
think that's the approach we're going
for now and hopefully soon like before
eof we'll have ethereum tests and
execution spec tests can you give some
insights into the testing limitations
like what is not easy to
test
um I mean definitely one of the
challenges is keeping up for specs so
it's not easy to test a moving Target
which is maybe not the answer you expect
but um it's definitely very hard to to
keep up with the pace of ethereum
development and to have tests ready for
clients to go is the reference evm
independent of other clients
yes and I'll just say again the
reference what does filling from eels
mean filling from eels means that we
have a test case which may just be a few
lines of
code um that describes the entire test
case thanks to the framework and Eels
and Eels
basically um so the the way it's done is
there's a tool called the transition
tool otherwise known as t8n and this
gives a doorway to the evm and we give
it um inputs in a transaction and that
and this evm the TN tool gives us the
expected output and so this this means
that we generate a lot more information
as an example um the test framework
can't tell you what the balance like we
could add it but we don't tell you what
the balance of an account is after it's
sent TR Network because we don't know
all that we we could add all the gas
costs but there's a lot of complicated
things that we need to track and we
don't track all of them so we wanted to
track all of them the test framework
sent transactions to a network because
we don't know all that we we could add
all the gas costs but there's a lot of
complicated things that we need to track
and we don't track all of them so if we
wanted to track all of them we'd be
implementing an evm and we don't want to
do that it's not our Focus so we use a
reference in evm eels that gives us all
this information including State
Route will the engine API get
incorporated into this version testing
mechanism um it is partially um because
we generate different test formats and
one of the test formats is in uh is
called the the
blockchain blockchain engine test format
and um these these fixtures can be sent
to a fully instantiated client that's
running within within a hive environment
and they're executed using engine new
payload
but the engine API specifically this is
really about more evm specs rather than
engine API specs there's a separate
simulator in the hive repository that
handles these
tests great thank you so much we are out
of time for questions but if you have
one of these questions find Dan
afterwards and we will be back in 5
minutes because we generate different
test formats and one of the test formats
is in a is called the the
and they're executed using engine you
payload but the engine API specifically
this is really about more evm specs
rather than engine API specs there's a
separate simulator in the hive
repository that handles these
minutes this is really this is really
about more evm specs rather than engine
API specs there's a separate simulator
in the hive repository that handles
afterwards and we will be back back in 5
minutes have time for questions but if
you have one of these questions find Dan
minutes of time for questions but if you
have one of these questions find Dan
minutes
welcome to the afternoon session
everyone I'm Ahmed I'll be your
MC um so our next speaker is going to be
talking about using W execution
extensions for Next Generation indexing
please give it up for alexe from
itha hey everyone I'm Alexi I work uh on
WRA at Etha and today I'll be talking
about W execution extensions for Next
Generation indexing
so let's start with what is indexing why
do we need it uh ethereum is a database
in itself it has uh history State and
receipts and it sounds like it's
sufficient for all our needs but it's
not because history is too large and um
as an example when you want to query all
the transactions for user you need to go
through all the transactions in the
history same with State uh you can query
the account balance and account nons
very easily but for example to Square
the erc20 balance you need to actually
index every smart contract for the erc20
and uh calculate how many tokens does
the user have um receipts and logs are
good they work but unfortunately
sometimes they lack all um the required
data in them and uh you still need to
know what receipts to query so you can
have some transactions that meit the
locks about the deposit for example into
the biton chain uh depos contract but
you need to query uh the transactions
for uh this for this
contract so people usually build
indexers uh indexers are third party
solutions that uh store the data
Elsewhere for example it's ether scan
that we all use uh it's Dora um and also
wallets wallets are indexers they
usually Outsource it to someone else
like infura ether scan whatever API but
to show the token balances you also need
it and uh if you think about it um a
rollup can also be a kind of an indexer
because you need to keep track of the
deposits from L1 to L2 you need to uh
derive the data from L1 to get the L2
State uh for example when syncing um so
yeah it's an outof note uh
infrastructure that indexes onchain data
uh to get some useful data of
chain um so how do indexers work today
you as an index developer have several
choices and the most obvious One is
using the Json RPC Json RPC has the E
subscribe method that allows you to get
notifications for new blogs uh that
arrive this will get you the
transactions and you can also Trace
these transactions later you can inject
your code into the node source code for
example you can have G or W or
nethermind code you Fork it you inject
your code for Story the uh data from the
from the transaction into your storage
of choice pogress Kafka whatever and uh
you process it later and you can build
on top of the existing node components
and create your own indexing node that
runs in the same uh binary in the same
process as the node itself so let's go
through all of them and uh talk about
procing cons Json RPC subscriptions very
easy every note has it this is the
uh the thing that's almost specked so
people uh expect the behavior from every
note to be the same um the cons of this
approach is the poor performance mostly
due to Json RPC uh serialization and
data transfer because you need to
serialize to Json you need to uh make an
HTP request then you need to desaly all
things um it's difficult to handle the
chain reorgs because when your chain
reworks you get a notification on the E
subscribed um e subscribed web circuit
connection but this notification doesn't
tell you a lot about what was reverted
and what was committed now you need to
figure it out by your own and also it
requires a ad hoc solution some like
rust python JavaScript uh code that
trans alone sign your note uh listens to
this Json RPC method and uh stores this
data
somewhere okay we have like a better
idea uh we can inject our code into the
node Source we solve the problem with
overhead on serialization and the data
transfer you basically do not leave the
memory that the note uses and um all
data is potentially accessible so you
have the access to the database um to
the transaction pool to everything that
the node has access to and um G has it
today it's called life tracing and um as
you can can tell it's very easy you add
your own uh Doo file to some directory
um you run gu as normally and it
produces your locks the cons of this
approach are maintaining the fork of an
original uh repository so you need to
Fork gu you need to add um a dogo file
into some directory but if for example G
introduces some new feature you need to
um pull the changes you need to uh
resolve the conflicts and then you can
uh start running your note again and the
con is also that you aside to the
programming language that you use uh
that the note is written in so in case
of gu is go so we have our own answer to
that and it's execution
extensions so let's talk about what day
um executions extensions require um
allow you to consume a reor aware stream
of notifications coming from the node
basically you get access to all not
components same as in the approach with
gu you get access to evm database
transaction pool payload Builder you use
shareed memory for communication so the
node sends a notification about chain
commit it has one block this block is in
memory and all xaes for example you can
have five execution extensions they
share the same memory so there is no
copying uh going on and it's also
compiled into the same binary as W and
um it's it's run in the same process
so as I said there is no forking uh I
didn't say this there is no forking
because we use W as a library um that's
the main I think difference that we try
to um that we try to talk about more
that um wrath is an SDK not just a note
and you can import wrath you can use it
in your own small project uh 100 lines
of code uh 1,000 lines of code doesn't
matter and uh when uh W updates you just
do cargo update and it updates your
dependencies you also have the access to
all the note components as I said and uh
what's also very cool that you get
access to the state divs uh right from
the evm execution so the evm finished
executing the block it um it produce
some State divs and TR divs and you can
consume them the issue is that you are
try you tie to the programming language
um of Wrath which is rust which is not
bad uh
so as I said you can do whatever uh you
want as like an indexer you can do an
indexer a rollup for example a base
rollup an AVS or an Oracle and uh you
use the power of the node builder in R
SDK to introduce a new RPC method for
this uh indexer that serves your data to
extend the payload Builder or add a new
CLI argument um to somehow configure
your indexer without modifying the
source
code this is an example of a of an
XX um what happens here is that you
consume the stream of notifications
there is three variants for the inam
chain committed chain reor and chain
reverted and and as you can see in the
reor we have old and new chain so you
can uh undo all the all the state diffs
from the old chain and apply all the
state defs from the new chain and then
the uh node is started in the FN main
entry point function which is like 10
lines of code and and it runs the full W
node just as a normal W node but with
your extension uh that node sends data
to so people today are are already
building stuff with xaxis we have uh Tao
experimenting with the uh base trup
built on x-axis we have Kona which is a
Ops uh project for duration of uh L2
blocks from the L1 and it's also an nexx
uh we have Shadow uh working on Shadow
logs when you want to have additional
logs in your app that are not in the
source code of the uh contract itself
and you on every uh new transaction with
this contract you modify the VM
execution of it uh and um wewm also
doing some stuff and we and they have
like three four blocks uh four block
posts in their uh block about
it and draw ups are also can be seen as
just execution extensions as you can see
and uh that's a future I'm personally
very uh looking forward to that people
buil into one piece of software uh many
pluggable pieces and you run a rollup
inside your own note without
communication via some API so let's
build an
indexer uh what we want to do we want to
index uh the beon chain deposits for
example and serve them as a list of top
depositors to the contract through an
API uh deposits are recorded in the
events of the contract we can take out
them and the API will be the node Json
RPC and we extend it uh using our own
that we will build and this is the
screenshot from theer Scan they already
have
this uh so the idea is that the power is
in the stack that we buil and uh we can
use uh as I said X access for listening
to new blocks uh we decode this uh these
transactions and chain events um using
using in alloy for storage I will use
sqa just because it's the safest uh
choice for a small project and embeded
database uh for the API I will use a
custom Json RPC method um and we will
bundle it all together with a nodeb
builder and test using cast from Foundry
to send the RPC method to send the RPC
uh request to our node so listen into
new blocks basically the same as I
showed before same bowler plate you have
the notifications Channel consume it and
you react on different events uh deing
the chain events we have two uh
definitions here we Define the deposit
contract address which is uh done with
the address micro from alloy uh which
represents the address in memory
efficient way and not as a string and uh
here the coolest thing is the soul macro
which parses the uh solidity source code
and generates the RAS code from it
basically you'll have a stru deposit
events with this Fields Pub Key
withdrawal uh
credentials Etc and it will not generate
the code into a separate file but will
have it in the um same file accessible
through your LSP or whatever uh you use
and during the compilation it will uh
generate this
code uh for storage we use SQ light and
uh what we store is uh one row per uh
per deposit
so every time we have a reor we have a
revered chain and we delete all
transactions that are in the revered
chain from the database and we do it by
the hash for the commit we do a bit more
we go through blocks in the chain
because for example if it's a 2d preor
block you will have two blocks in the
reverted and two blocks in the committed
chain you go through the blocks you go
through transactions with receipts you
go through the logs in each transaction
and you also filter only those
transactions that are uh sent to the
beon chain deposit uh contract you
filter the locks uh you decode the locks
and uh then you insert this data with
the amount uh from the lock into your
database API we Define a trade uh that
has a name space of Defcon and the
method of
depositors um there is one argument
count for limiting the output length uh
how many top depositors do we want to uh
get and all the me that this method does
is squaring the database uh with some
simple SQL web to uh we have node
Builder to bundle it all together we
create a new ethereum node uh we install
the XX that we build we extend the RPC
with our module that we build and we
start the Lo the
node so so when the note is up and
running it needs to sync but if you
already had the synced re Noe you can
use it because it's still W mayet
ethereum node you just have an extension
on top of it so if you already had a
sync node it will not uh have anything
in the database but it will backfill uh
all the required blocks uh from Genesis
and then you will have the
sorry and then you'll have
the depositors that you can query with
cast and cast RPC is just a common to
query the Json
RPC so the result is one file with less
than 200 SI lines code for builds in the
indexer and uh the power here is that
you have the whole WRA code base with
thousands of lines of code that's uh
hidden by the input and um in the corner
there is a QR code you can scan it and
check out the
repo so what else can you build with
xais uh we have a couple ideas that we
would like people to experiment with and
uh if you have any other ideas we are
very welcome and um we would love to
hear it from you so the remote XX is
about streaming the data out of the node
into some data Lake for example you have
a a JPC server or you have some Kafka or
any other queue and you just simply
stream this data out and consume it on
the other end I believe this is what uh
companies like ether scan will do
because they will not plug the uh the
indexing Parts into the XX because they
have a more complicated system Oracle XX
uh you listen as an XX to some offchain
data source for example you query the
New York Times uh web site you attest to
this data as a one user uh of this XX uh
so you sign uh that you saw this kind of
data uh you gossip the stations using
the dq5 uh topic to other people running
the same exx and what you have you have
a small network of uh of oracles trying
to agree on something and when they come
to consensus uh when the Quorum is
reached they post their data on chain
with these uh signatures so you can tell
that uh it's actually signed but by by
all these people who uh said that they
oracles and it's very similar to how
avss work and you can build a bases with
uh with xais based trups um you expose
your own RPC to send transactions you do
not post transactions to L1 but instead
you execute them on top of the state of
your rollup then you bdch them and you
submit the the transactions and the
state to
L1 and uh on the QR code we also have a
bunch of examples that we build for
people to play with uh they're not
production ready but they uh serve as as
an inspiration for people to start
working with
exxus that's it for today uh thank you
and let's
build thank you very much for the
wonderful talk Alexa so let's uh move to
questions as a reminder please scan the
QR code and submit your questions so
this is very Dev friendly but uh you
still need to run a full ref node right
even just for running a simple
indexer yep that's
true that's basically true what yeah um
you can either run an archive node to
get access to all history and all change
sets or you can have a full ref Noe yes
okay how does backfill
work right so when you start your XX
there is an option to to subscribe to
Notifications telling what's the latest
hat that you saw is and for example if
you start your XX on block 21 million
but you didn't start your start your XX
on block 21 million but you start XX on
block 21 million but you do start your
XX on block speed I would say it's um
some number of
gigas mentioned uh per second and uh
this is the speed that you can get new
updates
at how do you handle
reorg it's handled inside rest noes and
we basically maintain a structure the
tree that says this is the canonical
chain this is the side chain and at some
point the side chain becomes canonical
so we uh reverse the canonical chain and
make the side chain canonical um that's
a rough explanation and what you get is
the next X developer is a nice def old
new
chain uh does back filling require
running XX in archive mode or is a full
Noe enough it depends on how deep is the
back fi so in uh in the full note we
still store some change sets and uh if
it's for example 20 blocks deep it's
fine but if it's from Genesis you need
an archive
notes how do offchain oracles coordinate
data sources
that's up to you and um it should be
some protocol that agrees uh what to
query uh how to agree uh how to
communicate this data between each other
Etc
um if uh did you see that g uh has a PR
for this now too yes I and unfortunately
it's closed now because Peter wants to
move it to his own small repo I respect
this
um this is good yeah I like
it okay um if XX runs as an independent
process what's the difference um between
that and other indexing tools such as
the graph or other ETL
tools you basically can choose what
methods of communication it uses and for
example you can use protuff that's more
memory efficient and space
efficient uh what are invariance of the
XX interface are notifications
guaranteed to be ordered and contiguous
yes
okay um similar to the plugin in hyper
okay that seems to have been uh does
backfill still work if you enable
pruning again depends on the depth of
backfill okay um can you alter execution
with XX for example execute some custom
Logic for each store uh yes you can you
can override with a node Builder using
the custom evm executor uh it's
independent from the XX and your XX will
get the result of your evm
execution and uh I think a final
question uh how is XX compared to hook
from G or Plugin from
nethermind right G hooks I think require
forking and plug-in from nethermind is a
cool idea that works via Dynamic
libraries and I think it's very similar
in terms of performance and just a
approach all right well I think that's
it for questions thank you very much
LSA
um so we're going to have a 5 minute
break before the next talk uh stay tuned
hey guys guys welcome to the session um
so just as a reminder there's going to
be a QR code on display please scan it
if you have any questions to
ask so our next speaker is georgeos from
Paradigm who will be talking about W 1.0
how we got to it and what's next
good afternoon everyone it's been a
wonderful day and it was really
inspiring to see so many great questions
to Alexi just to see what's going on by
show of hands who here is a Ros
developer
amazing and again by show of hands who
has contributed to any of our code bases
W Foundry alloy anything like that okay
fewer people who runs a node or has run
a node
okay more people great excellent so
we're going to have a high context
conversation here I'm going to talk
about re 1.0 re is a new node that we
started building two years ago and I'm
going to say how did we get here and
where are we going from here my name is
Georgios I'm the CTO and the GP at
Paradigm I'm also the founder of vaka
which is a project aimed at accelerating
crypto so I want to start from like what
is a node and from a very abstract sense
a node is the soulle of every Network
transactions come in it re executes
things it produces a state commitment it
streams the thing out and this thing
goes on and on and this is what gives us
the so-called decentralized Cloud
decentralized Web the crypto that we all
came and
love now today nodes are or have been
slow they're rigid you cannot really
modify them they're kind of scary like
when you see somebody is running a node
you think there must be some crazy
system Engineers developer and they're
actually expensive it's really hard to
run a node as we saw a small amount of
the room only running a node and it
doesn't need to be like that nodes must
be not can be not should be they must be
fast so that they run the chain quickly
they must be extensible so I can go and
override it and add additional
functionality to it must be welcoming
very important a node must not be scary
must be a place where you go and you're
not afraid to modify to go unblock
yourself and nodes must also be cheap it
must be able to run on cheap Hardware
they must require you to like get a
cheap Cloud box if you need or even your
laptop we've seen people running R nodes
in their MacBooks and that's really
inspiring we're really proud of
it and so we built W to fix this problem
we want the nodes to be fast so we built
a fast
node and re is a contributor friendly
implementation of ethereum you can see
here I have the GitHub repository it's a
repository we feel very proud of and
we're spending all of our efforts on
every
day reth was buil to be fast extensive
ible contributor friendly and cheap and
that is for many reasons and over the
last two years we've been shipping and
shipping and shipping and we shipped a
lot of software and I'm excited to talk
to you about a lot of this stuff
today so we started the W project in
development of Foundry and I went to our
colleague Oliver I'm like okay my man we
fixed Foundry we fixed smart contract
testing what's next and uh I told him
why don't we build a node and he saidou
crazy
well a few months later we came up with
a node we announced it in 2022 and later
in 2023 we released it and the first
Alpha version doing that in 2022 was
insane I didn't know anything about
nodes but we went and studied and we
learned a lot and today we're we're
seeing the benefits of learning how all
of that stuff
works in 2024 re hit its 1.0 Milestone
it was something I worked really hard on
we work with other Cod cev teams use
automated client testing tools we did
everything we could to cover every
single edge case downtime was not
acceptable some slow transaction taking
us down was not acceptable the P2P layer
taking time to sync taking a long time
to fund Pi was just not acceptable the
bar is very
high and we also worked with the sigma
Prime team our good rust friends on the
consensus layer who are also Auditors
and what we did with them is we told
them okay you guys really like the
execution layer well we gave you a rust
execution layer now go crazy on it and
they found a few good things but what
was really remarkable is that the
original assessment was scope to say
this long and they end up spending way
more time because they like the project
and that's how we want people to be
working with us we want the W codebase
to be something that people are excited
to work on and not something I find
scary and like kind of like weird to be
in in 2024 re is being adopted in
ethereum main net the data source for
this is the ethernet node crawler
depending on what source you see you
will see different thing so bear with me
but basically re is a note that appeared
in 2022 and is already starting to be
live and existing on ethereum main
people believe in WTH to stake their
assets with it RPC providers use WTH
because they find it exciting to provide
better performance to to their customers
and we did we did all of that because we
want to make crypto better and it seems
that we must make crypto go faster and
that goes from all the way from the
infrastructure to the developer
experience
so I keep talking about contributors
this chart is kind of remarkable because
this has been a chart from a few months
ago from August and actually I tried to
pull it up today but I didn't have time
to update the screenshot but we had even
more contributors and like even more PRS
we have 500 PRS and over 50 contributors
every month which is a really exciting
metric to be hitting for an open source
project with no grants no subsidies it's
just cool code and this is not a simple
project this is something complex but
somehow people keep coming to it because
they like it because there's something
about like being a part of a
community and we really care about this
community about our open source
developers we have 400 contributors so
far 400 people contributing to a node
the thesis that we had when we started
developing W is not that we wanted to
build a fast node to go and take over
the stake or to have 33% or whatever it
was kind of an education project
honestly it was what what if we grew the
pie of open- source developers that get
how ethereum works and what if we also
tapped on a group of people that care
about high performance and the result
was the W
project so to US Open Source means a few
things a there's an age-old tale about
from Linux I believe where in the eyes
of a thousand people every bug is
shallow we get consistently bug reports
for our code and we love it we take the
bugs we fix them and we go to the next
and that's the nature of building such a
critical project we're very excited that
we have teams like the ethereum
foundation security team which goes and
sends us emails to our security email
and we we need to fix things and that's
the beauty of Open
Source re enables third party Builders
the open source community that we have
built continuously builds things on WTH
and WTH as Alexa said is not just a node
is an SDK and it's an SDK for building
high performance nodes and so much more
like EX ution extensions the other very
exciting thing about the open source is
that the community gives the project
life I used to be one of the main
committers in The Foundry project and
nowadays the project just lives on its
own it just goes on and on and on and on
and it's kind of like remarkable again
the beauty of Open Source and finally it
has this very counterintuitive thing
that if you really figure out how to
solve it the problem starts moving
faster because of the third part is
contributing not slower you don't spend
all your time trying to find like great
talent to come into your code base they
come to the code base because they find
it cool and we hire the best of them
like we have with a team that we have so
far many people ask us okay Georgio what
you guys have done is really nice like
we also want to replicate this in our
code base how how do we go about this
you know do I hire a community manager
do I hire a devil what do I do and and I
think there's like a lot of things that
you can do I think that most important
things are on the this board and it
starts with a polished issue tracker the
moment that you go to the issue tracker
you must be able to go and filter by
label good first issue and like go pick
an issue what happens in our code bases
when we open a good first issue is it
gets picked up 10 minutes later people
are proud to be like putting W on their
resumes and they're Racing for open
source tickets that's really exciting
but how did we get there we got there by
having great documentation in the rust
code bases that we have we have lint
that doesn't allow for any publicly
exposed interface to be undocumented the
pr just fails if you don't do that and
that sounds like a small thing but it
really makes the developer think about
it twice and what I really love about
the RAS programming language is that it
doesn't let you be lazy and parts of the
things that we are trying to do is
prevent the open source devs from being
lazy when they come to our
projects thirdly great tests tests
matter we build The Foundry project
again because we thought that tests
matter more than people think and here
again we think that test matter a lot it
means that I can look at the pr like on
the plane or like when I'm like on a
bicycle or anywhere honestly and I can
know that the test that the pr is going
to be good for the pr that the marginal
open source contributor brings and that
is what allows us to bring on more and
more people without really having to
like deal with a you know taking hours
for like PR reviews that's really
powerful fourth the maintainers matter
if the maintainer is not on a chat room
that like you can reach that's a problem
if the maintainer is an that's a
problem because if the maintainer
replies to your PR and they're like no
that PR is garbage well you're probably
not going to go back to the repository
because you think that PR was an
so Good Vibes they matter it matters
that when you go to the repo and you say
hey can I take this the person that is
maintaining says thank you for the pool
request or thank you for the issue what
about doing it this way instead of
shutting down requested changes 35
comments on the pr and then go to the
next uh roast it's kind of uninspiring
and demoralizing I think the problem
with aite developers is that they think
that the newbies are not worth talking
to I think that's a cultural Pro problem
that must be fixed and if you want an
open source repository you need
that finally um the chat room the chat
room matters the chat room is where the
Vibes happen the chat room is where the
communication happens the chat room is
where the design happens if the chat
room has non teex spam the chat room is
not good if there's people trolling the
chat room and they make the experience
uncomfortable that's not a good chat
room God forbid there are ads in the
chat room somebody post a job ad or an
event ad or anything like that no bueno
it's terrible to have a bad chat room
you start ignoring it you archive it you
don't talk about it our chat rooms they
have thousands and thousands of people
and somehow we managed to keep it
together and in the beginning it
required me or others on the team to go
and do like manual support for a lot of
people and we were always very careful
about when somebody enters the chat room
they have a good experience the
developer in an open source project as a
maintainer is your customer and you got
to treat them with Excellence because
for every bad developer you lose 10 for
every dissatisfied developer you lose 10
future contributors and that matters
again this is a chat about W but like a
lot about this is about how to build
successful open source projects and
communities and how to ship increasingly
complex projects with like small lean
crack teams that can do a lot of good
work without having to hire 50 or 100
people like go and burn insane amounts
of
money we learned a lot firstly ethereum
is just really hard you might think that
it's easy building a client it was 100
times harder than I thought like when I
told Oliver heer we building a node I
thought it would have been like a
six-month project it took 2 years and I
think building the next phase is going
to take a lot longer and that's why
we're here for the long run
big shout out to other client tees U
that have been doing this for many years
and I think we we're two years in the
journey it's really humbling to see how
hard this stuff
is secondly testing is extremely hard
especially when you need to interoperate
with nodes in other Implement in other
languages which may have different
architectures maybe you're like built
with a trib maybe another DB uses the
Argon style Sync It's really interesting
like this cross client interrupt but
again they it's like really what makes
the problem hard and exciting to work on
again the best Engineers want to be
working on mey hard problems and this is
one of them so when we see hard we see a
challenge and we go for it thirdly
benchmarking is extremely hard I think
benchmarking is one of the underrated
things nobody in crypto profiles people
just like go and do Cowboy modifications
without thinking the one thing that you
need to do is a flame graph a flame
graph is a bar chart that you see when
you run a profile or when you run a test
and it has big red boxes showing where
time it spent so I I don't really know
how to optimize but I know if I see a
big red box I try to make it smaller red
box and samply is an excellent tool that
everybody that cares about performance
should be using you run samply record
your command and it outputs a flame
graph and not only does it output a
flame gr it also outputs a Firefox share
link that you can send to your teammate
to continue debugging with you it's
really powerful you need
that and fourthly contributor
friendliness is hard I think in other
languages being building successful open
source projects is particularly hard
because you don't really have like a
bunch of like access to like easy
developer tooling to make it easy to
review a PR but we did it and we're
really proud of
it all right we got here where are we
going and I have six minutes and I hope
it's going to be
enough so three things for the future of
re stability performance
extensibility we think of feedback loops
as the most important thing you talk to
your customers that's a feedback loop we
talk to the core devs that's a feedback
loop for our stability if we can pass
ethereum main net that's very powerful
because it means that people should
trust that our software is good
similarly if then what is our
performance feedback loop we built op re
for that which an OP stack
implementation of the W project and we
laid out the gigas road map earlier this
year on all right where do we need to go
let's put a Target on it not
transactions per second gas a real unit
of account for compute and go and like
like optimize that
Loop and thirdly extensibility we have
the re SDK op is one implementation of a
node using the r SDK the W SDK is a
framework for building high performance
and extensible nodes and they're stable
because you know that they share code
with the most important like system like
in crypto which is
ethereum and execution extensions you
heard Alexi talk about so I'm not going
to talk more about it
so how did we get stability we got it
with cross client tests and cross client
benchmarks big shout out the curosis
project and the pound team for the
ethereum and the optimism package they
let us bring up chains with like as many
clients that we need as many nodes as we
need like main op stack like fuzzers
like any kind of like third party
tooling like in two commands these are
wonderful tools anybody in node infra
should be using
them performance is again I'm like
citing the documentation on how to run
for op chains and how to run how to look
in our road map or our perspective on
how to build high performance
nodes thirdly extensibility the r SDK we
provide big uh examples showing a lot of
things so on the right you will see that
the exact examples for the back fill uh
for the exec we have backfill we have an
oracle we have the remote exec we have a
rollup example we have a lot of stuff
similarly on the rsdc side we have all
sorts of things we can show you like in
a new pre-compile we can show you how to
do P2P for BC for polygon even though re
was not built for them you can do such
crazy modifications without forking the
node and you can access any chain in the
ecosystem so 2022 we started with a rl1
node we were able to sync something by
the end of the year but the end of the
of 2023 we had a rest node that can sync
ethereum L1 and op St
good nodes and we're giving it away with
Apache MIT license because we think the
industry needs
it our vision is to accelerate crypto
alongside the open source Community
that's why we started itha which a new
project that is basically taking our
existing team and we're empowered to
start running experiments where we're
going to start by solving the ux problem
we think that the thing that's missing
thing right now from crypto is the ux is
the ux and really to fix the front ends
we had to fix the back ends first your
front end is only as good as your back
end and it took four years but we think
that finally the stack is ready and
we're ready to finally build great
experiences and here in the right you
will see a tweet from Thea account where
we demonstrated what we think next
Generation ux can be where we showcase
EIP 772 and p256 which are two proposals
like one one is already on l2s and other
is coming to ethereum main net in a few
months well the idea there is that what
if we had endgame wallet ux what if like
in any device in any chain I can batch
no rpcs no Bridges no gas like no key
management just works and it's an
interesting question can crypto ux be
better than web 2 and my claim on why
people haven't been able to do that is
because the pieces of the stack were not
quite lined up so far
and you know if you see the user and the
developer anytime the user tries to do
something they go through connect wallet
then they go through metamask then they
go to through Fiat on boarding then they
go through like a thousand layers and
some something always quite feels off
and think there's a time to fix it and
the time is
now and we're going to do that because
we have built the industry's most used
open source tools we built alloy rev
Foundry re cryo we just
solar and new solidity compiler Ox
wagney VM we know ethereum and we're
going to fix it so our nordstar is to
solve ethereum's hardest problems we've
been doing it for years we think the
time is now to go and build the best
open source software for the industry
and for crypto to become something that
we feel proud about thank
you thank you very much for the great
talk georgeos let's turn our attention
to questions are there any are there any
current disadvantages of running W
compared to other clients totally there
is a trade-off that you make when you're
running a w archive node which is that
you give up historical e get proof when
you run it um and right now I believe
that sometimes on the RPC performance on
the websocket subscription is not always
state-of-the-art so sometimes other
clients can have better performance than
us on the RPC and we're working on it
what novelty does re bring other than
the language it's written in oh tons um
firstly reth again is an SDK right so
the Ross language is kind of like
independent here the fact that reth is
an SDK means that I can literally go and
build other node implementations using
it what it gives you is a runtime RPC
P2P DB and you can choose how to put
them together and would just give you a
nice Builder pattern that you can use to
do everything um so people have done uh
things with red for example I think the
Tao team has done things with our stack
the schull team has done things with our
stack so it's not necessar really the
rust programming language it's that we
built it to be by default performant and
like we give all the nice abstractions
for people to go and build whatever the
developers need again without forking by
being a library so it's it's really
critical to land this point re is not
just an L1 node like there's not much
that we need to do like to to like grow
adoption on L1 we care for the stability
but like what we care about is developer
tools first and foremost to empower devs
to build things and W in every way from
the SDK standpoint is a Dev tool and Dev
tools don't need to be
scary so I can run a local ether scan
with Aron called utos scan when would
ref be friendly to local privacy
friendly block explorers that's a great
question so on Anvil which is the test
net node that we built which um predated
ganache um you we have implemented the
otter scan API and you can run otter
scan using Anvil I'm not sure um what
happened with the I'm not sure what H if
we have that implemented in in rest but
like maybe we could add
it uh what was your thinking in starting
the W project rather than building on
aula I love re but I feel bad for the
akula team totally uh we were looking
for a very easy to contribute project
and uh we we had a hard time like
contributing to that project okay do you
have any thoughts on the beam chain not
many not
many okay then when w light node uh
that's a great question um I don't know
should we do
one okay we'll take it back to the
team um why do you keep advertising that
re is the most performant one when
clearly nethermind is the better
one we love the nethermind team and
they've been taking our ass lately so
big shout out the nethermind
team um any plans on making a consensus
client under Paradigm portfolio Paradigm
should dominate e ecosystem just
relaying this by the way not my opinion
totally totally totally totally H these
are good questions H you know firstly we
I see me on the crowd and we love the
lighthouse team so no plans for anything
like that some somebody asked us around
the beam chain should we do something
about that oh like it's a good
opportunity I don't know man I I really
don't know like we maintain so much code
it's kind of going even consensus is
hard like all of the stuff so far is not
like the hardest but like consensus is
actually
hard any technical decisions on ref that
regret I I need to think more about
it okay how' you pronounce if
it's not ithaka Cornell uh it's ithaka
Greece which is an island that Odus from
The Odyssey went back home uh which is
the home of ad disu when he came back
from
Troy okay is there any combination
planned for w and Lighthouse from the
perspective of VL and cl oh
yeah we've been calling it red house but
like I don't know that it's like
planned okay um what specifically about
W allows it to scale to higher gas
throughput and do you specific
specifically measure gas in the engine
we do use gas as our current way H to
measure things uh we think that gas is a
good enough way to address to cover our
benchmarking needs um I think it's a
good question like whether like that's
an sufficient metric for example the gas
does not express whe like well enough
like whether it's storage or compute
operations um and sorry what was the
first part of the
question um bre and Lighthouse no no
okay let's go on yeah all right how'd
you look at a PR on a
bicycle uh with without hands you know
like
you okay uh when will rest support
non-op stack EVMS and why was op stack
prioritize versus other EVMS yeah so I
had worked on the optimism code base for
many years um so I knew how it worked uh
op stack then was designed very nicely
in the sense that I can just touch the
execution layer component without
anything like above it which is like the
derivation function or how you do fault
proofs or anything else so it had just a
nice separation where we only need to do
like a few modifications to the codebase
um and that felt easier uh and when non
op stack trains I don't think we have
plans for us to do it but we've been
refactoring the codebase to have no
feature flag so it's a pure SDK as much
as possible such that people can go and
uh do it themselves and we're already
seeing that for example with the scroll
team where the scroll team PR a state
commitment jaliz pull request and that
state commitment journalizing pool
request allows them to unblock
themselves and go and import re as an
SDK and like make it work with the the
Merkel tree that they have which is
slightly different than the one that we
have so nothing that we will do but like
we're making the SDK available for
people to do it all right we're out of
time for questions thank you again
George
us uh we'll reconvene in about four to
five
minutes e
I
hi everyone welcome to the next session
current session of stage two so our next
speaker is uh Gom of um Gom the core
developer of gas and he will be talking
about the veral advantage please welcome
Gom everyone
uh yeah so thanks for coming um I assume
if you're here or uh that's because you
might have heard in the past few months
some uh some voice saying maybe veral is
uh you know should be replaced with
starked binary trees and the purpose of
this presentation is to give you some
arguments to understand why uh now is
not the the right time to do
this uh let's briefly go over the
current status of veral trees uh the
veral tree implementation in ethereum uh
we launched a devet two two weeks ago
it's uh chugging along fine uh we have
something that is pretty close to the
final spec we're missing a couple gas
costs here and there but nothing uh
nothing that won't be fixed by uh by the
next devet um and you can go have a look
at at this address it will be displayed
again at the end
one of the biggest things we achieved
during the last uh during the last year
was a holis sky Shadow Fork uh we
validated that the transition model
works so we're really proud of that and
big shout shout out to devop for helping
us through this because that was uh that
was quite uh quite something and yes the
elephant has landed that's uh that's
because the spirit animal of the
stateless Fork is uh is the
elephant we simplified clarified so
there was a big work of uh
simplification clarification of the gas
cost EIP so veral is split into two eips
one of them is 4762 the gas cost they
pertain to stat less and then there's
the tree um so you know we we had a lot
of questions uh about it it caused a lot
of corner cases we addressed all of that
uh so I'm not going to say it's
completely ready because we need to take
into account eof 7702 and I'm sure a
billion things that will come in the
next two forks but um it's it's looking
pretty Advanced and pretty mature at
point we also implemented execution the
the execution spe spec test framework so
until now when we wanted to make sure
clients agree that we don't have any
consensus bugs we used to uh we used to
launch a test net and and verify but now
we don't even have to to do this uh we
have tests that Target a specific use
case so big shout out to ignasio and of
course the testing team for for working
on this one because uh we found
countless bugs before we even had to
launch um so yeah that was that was also
a great progress this year and then uh
there's been experiments in uh
implementing uh veral friendly sync uh
so this one was actually done by nether
Mine by Tanish and nether mine and uh
it's the first feature full feature that
has been implemented in a that hasn't
first been implemented in guest so big
uh big sh shout out to to Tanish
again um right and the last uh the last
thing that we achieved last year was the
state expiry um like we there was an EIP
that was uh published by hand he did a
very good presentation this morning
about it so I if you haven't seen it I
suggest you go you go and watch it but
just to give you a quick rundown uh the
idea is that that veral veral trees um
are pulling their um their leaves
together by groups of
extension stem on top of it uh and the
commitment which commits to the to this
the orange uh to The Orange Box which is
commitment um what we do is we add a new
field um that used to be zero and now
it's the epoch number so it's backwards
compartible it's really good and uh when
you you want to uh delete some data you
just delete the whole
commitment and because everything is
polinomial based you can re uh provide a
proof of the entire subtree so you have
to resurrect the the whole sub Tree in
one go but uh it's great because
effectively you only keep the internal
nodes and the internal nodes is where
veral trees especially shine this is
what takes the less space in the whole
in the whole thing so it will provide a
state expiry scheme that is efficient
that that is pretty much TurnKey we
could activate on day it on day one of
veral and uh and yes it's uh it's very
simple in the sense you don't need
address space extension you don't need
to do any modification it's really
working out of the
box so the conclusion is that after four
years uh veral is pretty much uh ready
for its prime um of course I'm not going
to pretend it's uh ready to ship to
tomorrow we still have a couple things
to do but I think um within a year we'll
we'll be uh we'll be you know a year of
focused work of course uh we could be
ready to we could be ready to ship um
let's go over the pros and cons of veral
to for the rest of this discussion the
first pro uh is that if you take the
veral proof and the veral witness this
is really small and this is like much
smaller than anything any alternative
you can think of uh we had several
experiments
uh and we found some encoding that is
especially efficient so it's it's known
as type three here um the average size
is uh to like 400 KOB less than 400
kilobytes and the worst case that we
observed so we replayed historical
blocks uh caveat of course they did not
because they're historical block they
didn't have the whole veral gas cost in
activated but it's still a very
interesting uh um yeah like reference uh
what we see is that the worst case is
less than 1 Megabyte uh the theoretical
worst case is 3 megabytes but on average
it's less than 400 uh kilobytes which is
really good because you've probably have
heard about increasing the gas limit uh
increasing the blob count all the all of
this is going to have an impact on the
bandwidth so the fact we have a very
efficient um proof structure something
that like we will add some some size but
adding very little compared to any any
other option is a is definitely a plus
um the trees itself is small um we it's
like on average from measurements we've
made so we take an MPT we convert it to
veral and we see what the end result is
it's about 25 uh% smaller we have
optimizations where we could shave yet
another 10 maybe 10 20 20 gigaby still
um but more importantly it's uh also
changing the way we store the data so
you can write to the DB DB more
efficiently at least the guest DB this
is my my reference uh so this is
something that's very useful um one of
the really good things about veral or at
least stateless actually it's not even
just veral but you can immediately join
the network when you want to sync and
then uh you can download the data you're
missing if you want to build a full node
you can download the data you're missing
in the background but unlike the current
uh experience where you just wait for
the blocks to be downloaded and then the
state and then you hope that you've got
everything in in order to be able to to
be able to to follow the chain you start
following the chain right off the bat
and only then do you uh do you worry
about downloading the data um so if you
want to compare the the idea of a veral
sync to the current state of snap sync
what happens in snap sync is that you
start downloading the the state here uh
this and uh I'm using Sprouts because uh
I want to point out that the data at
this stage is fresh it's the latest data
you've got but as blocks keep being
added to the chain uh the node keeps
downloading data but the old data uh
like the data that was downloaded before
is actually becoming stale so this is
represented by uh by uh dried leaves so
what you have to do is go to the network
and ask nodes that are synced to send
you the data that is obsolete
