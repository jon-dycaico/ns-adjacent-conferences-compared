o
[Music]
is
for
oh
for for
a
than
oh e
[Applause]
n
right
n for
I my laser while using
the so yeah I'm have to look this m
testing testing hi
everyone Hi hi
um yeah I'll take this mic
actually thank you for thank you for
coming to this early morning talk um
it's going to be a talk on formal
verification and like some basic methods
in um distributed systems and reasoning
about faulty distributed systems
um all of the everything presented here
has been formally verified by the uh
team at runtime verification uh and is
like available to like click and check
uh and you can look at the uh the proofs
in talk but this talk is not going to be
focused on the proofs more just
definitions and theorems and um not
really walking through the proofs um but
you can check them
out and there's a
so I've separated in a bunch of sections
a section on validation Theory a section
on equivocation Theory and then on uh
relating and uh reducing Byzantine
faults to equivocation faults in the
context of
validators
um so let's kick it off so let's talk
about validation um and this so here's
the here's these slides are I actually a
little disorder this so This is the this
is the name of the paper
uh um validating label um State
transition message production
systems um so it's for fault for
modeling distributed systems faulty
distributed systems and all these
amazing people worked on it for a long
time here you can scan this QR code and
pull up the PDF if you
like um I'll show this also again
later so
here's the validation Theory section
outline basically we're going to go
through this the definition of this
model uh its compositions and then the
definition of validator and then we move
on to the equivocation
section so here's the first definition
here um so of a vlsm is uh topple you
know as we often like to Define these
things um it's sort of like a state
transition system like you're normally
used to except for it has a few other
things like the lab a label which is
also not too unconventional and uh but
it has a first order message set in the
definition uh it has initial States and
initial
messages and then there's a transition
function that takes labels States and
messages optional messages and gives us
States and optional messages this is
like the state transition SL message
receipt and production uh function that
like describes you know for a particular
VSM you know sort of what's Happening
computationally uh you know you could
imagine and then they're also equipped
with another thing which is why they're
called validating this beta which is a
validity condition and it basically
says when it's going to be valid to
transition on a label from a state to
given a message so when you're a
particular State and you receive a
message and you know you might want to
transition it might multiple possible
transitions each identified by a label
um and some of them might be basically
banned even though they're defined by
the
transition the validity condition won't
let you take that transition so this is
like a state transition system with
Native messages with initial States and
messages and with a transition uh like a
transition function that's you know
totally defined over these
over this domain and then and then we
sort of restrict it effectively making
it partial uh with this validity um
condition this is like the validation
condition
basically we're going to imagine that
these things don't transition even
though the transition is defined when
the validation condition is not
satisfying um and so that's a that's a
definition but actually oh uh I haven't
told you um uh sort of how to get the
states and messages but you know sort of
what you would expect you start at the
initial States and the initial
messages and then we build up this fix
Point um by taking the union of all the
states that you get from the Transitions
and all the messages that you get from
the Transitions and transitioning from
those States using those messages so
basically starting from the initial
States and messages um transitioning and
sending all them uh all the messages
I've produced from there uh and
receiving them and doing it over and
over again basically until you know you
even get stuff like a node in an early
State receiving a message from some
other state um uh this really is like a
a big fix Point um and so so so there's
an interesting thing that can sort of
happen which is the validity condition
um can be
satisfied even when a input message is
uh
invalid um so we have to slightly
distinguish between just this just the
validity condition being satisfied and
the actual Trace being valid the trace
is valid only if uh all the input
messages are also
valid
um so you
know no no no no no garbage in sort of
allow in a valid
message so so so that's basically the
definition of vlm and then they have a
pretty natural way to compose them um
and so now I'm going to go through that
definition unless you unless someone has
like a question now before the before
composition okay so basically what we're
going to do is we're going to take a
disjoint sum of the components for the
label so we identify the label which
component is the state is a
topple of the component States the
initial States is a couple of the
initial States and then the uh we have
like a union of the messages for the uh
for the initial
messages um and then here actually we
we're composing U vsms that have the
same message uh type um this is just so
that all so that all their transitions
are are defined and everything and you
know to let them send messages to and
from each other so they're not just uh
independently like if that was a
disjoint Union they wouldn't be
communicating so have a dint union for
the labels uh tupple for the state and
then a regular Union for the
messages um and then in the in the in
the free composition we have a
transition that basically just affects
only one component exactly according to
the transition that would have had
before the composition and checks the
validity condition only of that
component exactly like it was before so
very little uh basically nothing being
done by the composition except for uh
transitioning the individual components
and checking their
individual composition uh sorry sorry
their individual validity conditions uh
individually there's no composition wise
constraints they but they but they but
they can message each each other in this
uh thing and then you know note also
that this is also a
vlsm um and that's why it's like sort of
a it's a composable model um you know
same tople definition and everything
yeah
so the question is is the split up
between the transition and the validity
uh purely mathematical I mean I guess
it's for the sake of convenience when
dealing with the math and um so I but I
mean uh in more more traditionally in
math you wouldd use like a partial
function I guess whereas here we're
we're about to get into this
conversation about validation and um um
distributed systems and what can happen
in a distributed systems that you might
not be able to tell locally about and so
it gets um there's there there is a
reason why we are thinking about the
validation at different levels and
actually um and and that actually does
sort of spell it out basically there's
going to be actually the next slide um
we're going I'm going to apply uh we're
going to talk about composition
constraint compositions where there's an
additional constraint on the uh so
basically like this constraint
composition just basically conjuncts a
constraint on top of the uh validity on
top of the validity constraint of the
free composition which just is the
individual con constraints applied
independently so this this this
composition constraint um you know let
us sort of analyze uh things a little
bit more conveniently than just a
partial function
approach
um gu guess you want to be able
to would be possible but it's not
valid um yes so the question is if we're
doing this to try to see if a
transaction is possible but not valid
and yeah you're very much going the
right direction um and uh we're getting
there with this definition here so this
is the defin this is the def def
definition of validator it's very
natural simple definition of validator
um which is kind of useful in many many
many different contexts um so in a in a
and and so the components are a
validator for the
composition basically they're checking
if they're truly a part of that
composition or if they're like um and
they're sort of you
know only transitioning as if they are
part of that composition even though
they don't know it per se so let me just
go through this definition so basically
a component in a constraint composition
is a validator if
any transition that that component can
make
can be lifted to a valid transition in
that uh
composition so if the component has a
valid transition then uh if if a
validator has a transition which it can
take then there there's also a
transition in the composite system where
that validator can take that transition
it sounds it sounds kind
of it sounds weird but basically the
it's it's not the local condition lifts
to a distributed one
um and so basically um this local
component is checking about a condition
that's distributed across the whole
composition and that's sort of um uh non
non-trivial because of information uh
disparity between the
nodes so um
there's um
a message here being received and this
is the message being sent and this is
the label and this is a a
constrained transition which doesn't
necessarily mean that m is valid however
it's lifted to a valid condition
transition with M being
received so basically
the validity condition of the component
is enough to guarantee the validity of
the message received in the
composition so basically the component
locally is able to verify whether the
message has this distributed property
and that's why it's called the validator
because it's basically able to check
something that's outside of its
scope um and it's again defined here
with respect to a particular composition
and a particular constrained on that
conversation so you might have different
validators for lots of different
different distributed settings but we're
specifically going to be interested in
focused on uh equivocation for um you
know a reason that I've already talked
about but like sort of like reveals at
the end like uh why equivocation is so
uh particularly interesting to look
at so um this the the equivocation
Theory section talk about evidence and
then using evidence to describe
composition constraints that limit uh
and validity conditions that limit
equivocation and then we talk and then
we'll talk about models of
equivocation and then all this
will tie in nicely um the in the when we
start talking about Byzantine
fonts so this is sort of um what we're
used to seeing in uh blockchains when it
comes to slashing conditions um this is
a a starting point um or was a starting
point in in in our uh Pro stake
research um basically when messages have
the same
sender um they' they've been they're
like collected by the same node or like
in the same smart contract you can
imagine and and and they and they
basically could not have possibly been
produced by the by by this by the sender
in a single round of the protocol so if
you run a trace of these things there
isn't a single trace where those two
messages are produced by that
note uh and so and and so this is
evidence of equivocation this is somehow
um we have two messages that couldn't
have been produced by their sender uh
and we have them sort of in the same
state um this is sort of a sort of
faulty behavior and this is local
evidence and here's an interesting
definition yeah yeah of
course sorry um uh if if we don't have a
history how do we check that
what uh yeah yes so it's so that's a
good question I mean it's I think it's
undecidable in general but uh the
question is whether it could not have
been possibly
produced by so basically you need to
sort of quantify over all traces and say
there is no Trace uh where these two
messages can be produced so in practice
you know we're going have lots of
simplifying assumptions like you're
indic like you're guess thing you know
um but the the definition doesn't say
how you know how we can how we can come
to this decision about whether a message
could have been
produced
um you know it's okay we that's actually
another nice thing about having the
validity conditions as uh sort of like
predicates you can have undefined sorry
undecidable um conditions whereas uh you
know if you were using partial functions
that would be an issue
um so uh there's there's uh Global
evidence is a little bit more
interesting and a little bit more
uh um maybe a little more decidable
right because you in in this this we
have like a sort of global view
of uh of the of of of the trace so we
can basically check uh that the message
was not
observed uh in and so
um yeah
so so so so so this is this is this is
getting into some later content that I
was hoping to I think I've slightly
misordered this
um but anyways uh if if you have if you
have a if you have a God's eye view of a
vlsm uh trace and you and you and you
have a message that wasn't sent by a
component but but it was received by by
some component um that's an equivocation
sorry Denisa can you go ahead
no
MH um yeah
um so here's a uh theorem right that the
the the the local equivocation is always
going to be less than the global
equivocation and all these are checked
in the theorem provs but you can sort of
imagine why why that
is um and basically we can use these
Global and local definitions of
equivocations to limit the uh
equivocations to create basically a
composition constraint where The Faults
Are um are limited
um we can easily just say okay well
there shouldn't be any equivocation and
and talk about DSM traces where there
aren't any
equivocations um and we also use the
full mode assumption um to reduce the
amount of equivocations because then you
can only sort of get an equivocation
from the sender of a message because
you've already received all of its
dependencies um we can limit
equivocations um to just a subset and we
can also assign weights to the nodes and
then limit the equivocations by their
total weight um these are like
example conditions in composition
constraints
um or a local
constraint so this is a composition
constraint for a validator on on on a
global constraint that looks like this
um and so like in this particular
example this validator is just checking
the local equivocation weight and if
it's less and T when the and the
composition constraint is checking the
global equivocation
and the the validator property is
basically that from the local one there
should be a global a state where the
global one is also
satisfied um basically the lifting
property of the valid state from the uh
local to the distributed
property so you know this was talking
about basically what what what
equivocation looks like and how to
detect it and therefore how to talk
about you know non-construction
traces that have limited
equivocation um but we do have uh a very
nice constructive sort of uh approach to
where we can describe uh equivocator and
um basically there's two models for
equivocation there's a state equivocator
which basically splits its current state
up or has many Poss many states uh for
the same validator um and it can do that
by foring or by starting new machines um
and it also has and there's also the
message equivocation model where instead
of the state splitting and having
multiple copies of a validator um
validators can receive messages that
haven't been sent um and and sort of
this this sort of
um uh is is is what is is is what we're
observing um in that Global in that
definition of global equivocation um and
and it turns out that these two things
are equivalent
actually um the traces that you can get
from the state equivocations and the
message equivocations are the same uh
whether you are like receiving messages
that haven't been sent or splitting up
States uh if you like project down to
those equivocator States we get uh
exactly the same traces um and it's kind
of it's kind of interesting basically
like splitting a timeline and
communicating across timelines um uh end
up producing uh exactly the same States
and so these two are um models of the
same uh phenomenon um equivocation and
that's why we have those two definitions
there where one of them seems uh a
little bit different than the other
um um you know somehow uh two messages
that couldn't have been produced in a
single trace evokes a state equivocation
and uh a message that hasn't been sent
yet being received evokes the message
equivocation but um they are uh they are
equivalent they are
equivalent
um so that's um a pretty cool pretty
pretty pretty cool result that's going
to be useful later um but basically to
repeat it um the models of
equivocation that um where that split
the state and models of cocation that
allow communication from other traces uh
lead to the same traces for uh
validators um for a limited
equivocation so um that means that when
you have um evidence of equivocation
being
produced um you know you can produce
that equ uh that evidence either with
state of equivocation or message
equivocation and you get exactly the
same state exactly the same uh evidence
great so that's first two sections any
any questions before the next
one excuse me so here we
go yeah
please your microphone's off sorry you
try okay I guess in in the previous
discussion you kind of assumed finite
branching which means that you cannot
make infinitely many copies at the same
time no we have we have an unbounded we
have like a list like unbounded list of
copies okay but still finite right yeah
finite but finite unbounded yeah yeah
yeah because when it comes to infinite
messages and states I was like um yeah
um that's a that's a good question I
think we have possibly infinite
uh traces but not States and messages
moment yeah I guess so sorry about that
yeah we'll get we'll get
there um yeah so so so so now basically
we're going to do yeah go
ahead yeah please use
M microphone microphone just close just
hold it
closer oh no never mind sorry
hi can you hear me yeah great this is
sorry um I think the States can be
infinite but not reachable it's a matter
of which are the reachable states but
the it matters how many labels you have
and that gives you how many moves you
can do but in reality yes it's bounded
and
yeah great so let's move to the
Byzantine uh the Byzantine
faults so um basically we can model
Byzantine faults in VSM by uh replacing
a node with a a node that basically has
a free behavior that uses labels to send
uh and receive any message at any time
um the important behavior is that it can
send any message at any time um
basically uh modeling uh someone that
can send uh you know any sort of
malformed in uh invalid message at any
point um and we do have a little bit of
constraints which is that we we don't
let them Forge messages on other nodes
and uh we do have a full note
assumption
um but
um uh you know they can send any message
you know signed by them um from from
from them basically without Forge
messages inside um and so we can replace
equivocation uh limited validators uh
with Byzantine components and find that
they have exactly the same
traces um the ones that aren't replaced
have the same traces um so
the if you have a trace in the
equivocation limited uh composition
where like some set B of of validators
is uh Byzantine um they have a the same
traces um uh as if they're composed with
equivocator instead um and basically
that's because of the validator
property so if you have a validated
property um on a receiving a message
from a Byzantine Center that means that
there is a composite state where um that
sender as an equivocator um can validly
send that
message um because here we're validating
for a limited equivocation setting so
you know some amount of equivocation is
valid in that
setting
um and so we can replace
this these Byzantine nodes with uh
equivocating
nodes and then look at the traces of the
of the validators that aren't
equivocating and show that they have
exactly the same uh
traces
um um Dena do you have a question okay
um and the same result also holds for uh
uh weight limited uh equivocation model
um so it's not just a for fix set but
for under T limited equivocation
weight um all the behaviors uh that of
of non- equivocating components uh due
to equivocating components is uh exactly
replicated uh by uh bantine
Behavior Uh with the same t uh uh
limit um and so that basically means
that Under The Limited less than T
weight equivocation we get all of the
same traces for the validators as uh
Limited less than T way butine
vaults um so that's sort of
uh the uh sort sort of magical way that
we can not use Byzantine fall
tolerance um basically for these
equivocation limited validators
equivocation faults are exactly as
expressive as businessing faults because
by validating for that limited faulty
setting um uh you know they're
uh restricting their transitions a lot
and if a Byzantine Byzantine node can
sends some malform message that they
receive that means that that transition
can be lifted to a valid state in the
composition Under The Limited T
equivocation condition um which means
that there are nodes in the composition
distributed that satisfy that less than
T threshold um but uh um you know AR
aren't butine notes but equivocation
notes and then um you know do like
putting those transitions together to
get traces we can rebuild exactly the
same
traces um and so basically this forms an
alternative to for analyzing faulty
distribut systems to bantine fault
tolerance and quite uh um simply you
know um um by studying uh equivocation
limiting instead of and equivocation
faults instead of uh Byzantine faults so
somehow equivocation Faults Are like a
special kind of fault where if you
validate for limitating equivocation
that's just as good as validating for um
limited Bustin faults oh sorry that's
just that's just as good as um sorry
that actually lets you throw out bantine
fault tolerance analysis alt together
when just when thinking about like what
traces you can go to um you can sort of
just go to the protocol defined ones and
um
um it doesn't really matter what the uh
Byzantine nodes do they're basic
basically just protocol following
equivocator as far as uh the analyst is
concerned and so instead of having
misbehaving nodes they just have either
like you know a state replicator or a
message uh passer that sort of uh
crosses timelines um which is sort of
much more tamed types and well defined
uh Behavior so later we're going to
relax the full note assumption and treat
synchronization faults I'm out of time
thank you so much uh thanks for coming
really appreciate it
if you have any questions you can find
me outside later thank you
for e
m
[Laughter]
good
hey good morning
everyone uh thank you for coming to our
Workshop
today uh before we start if you have any
questions just throw your hand up it'll
be pretty relaxed so
uh let's just look into the workshop
overview uh introduction that's us right
now uh we're going to go into zaru
Genesis um see sort of how it happened
why happened uh and then we'll look into
the data sets that have emerged
since um we'll then progress into uh how
we're using the data how others are
using you uh using the data uh Leo over
here will then present uh he's from the
meal laabs team uh he will present the
Big Blocks test that happened last year
uh and then we'll have a live tutorial
from Tony uh he'll go through how he
uses pis2 to run his analysis
sweet so a little intro on who we are
I'm Sam that's Andrew he's hiding uh
we've both been doing devops on the
panda Ops Team for the last few
years uh and we both have a deep
appreciation for things like ethereum
and observability
as for our team eth Pand drops uh we
started out in
deep end with the merge uh we're
embedded in the F and do devops for the
protocol uh and we post blogs
semi-frequently on our website we try to
keep them really high signal um they're
the best way to keep up to date with us
scan the QR code and we'll jump you
straight
there our team has a wide range of
projects cooking at all times you've
probably come across a couple of
them uh for example if you've ever run a
node you've probably checkpoint synced
from an mpoint that was running
checkpoint z um you may have also see
Perry and Barnabas whipping cevs in the
cev calls uh yeah there's a lot of stuff
going
on so let's move on to the workshop
to set the scene uh it's late 2022 and
the merge has just happened um we've
switched from proof of work to proof of
stake um but in doing so our consensus
mechanism has become a lot more
sensitivity uh sensitive to time uh
suddenly the when of things happening
has become a lot more important uh and
this D this data at a global and network
level doesn't really exist um it's easy
to check that a block was seen but it's
much harder to see when that block was
actually seen in Sydney compared to
Berlin for example um and now that we're
clear from the merge researchers start
hacking away they want to upgrade the
beacon chain uh but yeah they need this
timing data to validate their
ideas and they start capturing it
themselves um varying scales different
implementations um it's it's hard to
expose it's hard to validate there's a
bit of yeah potential errors in there
so we started to brainstorm ideas on how
to solve our problems um we needed to
somehow integrate with existing Beacon
node implementations as neither of us
were really too Keen to implement a full
Beacon node um as devops Engineers would
usually just Implement a few Prometheus
metrics put the feed up and call it a
day um but millisecond level Precision
is pretty important um so that rules out
Prometheus metc
uh log aggregation was also another
option but it's definitely a moving
Target uh these things change all the
time it's not really something that the
client devs really pay too much
attention to um and we'd also just have
to turn on debug level logging um we'd
be throwing the kitchen sink at our log
aggregation Pipeline and it would
potentially be an unreliable result
anyway uh so that rules out
logs so we started to look at other
options uh turns out that the beacon API
has this thing called the event stream
you can subscribe to it and when the
beacon node sees things or does things
it will emit an event so blocks
attestations voluntary exits everything
it was all there uh the beautiful thing
is that the beacon node implementation
all supported this uh endpoint in a
standardized
fashion so what we landed on was zatu uh
we used go
grpc uh and we thought that it would be
responsible for just collecting ethereum
timing
data uh it definitely wasn't going to be
trying to store or query that data um
but the the plan was to derive events
and ship them somewhere else to do this
we initially created two modules uh zatu
server would create events from other
modules oh would collect events from
other modules and send them somewhere
else and 2 century was our first module
uh it would run as a sidecar next to
every Beacon node uh subscribe to events
and send them off to zaru
server we wanted to make sure that all
of the events followed the same
structure so that it was much easier to
add new events into the future and also
really importantly uh since this is like
a distributed system we wanted to make
it clear how much you could trust the
data so data coming from a client is not
necessarily trusted but if it's running
if it's been derived by zaru server
something that we control uh maybe you
can trust a bit
more uh this example event is for one of
our Z2 centry nodes running on mainnet
uh subscribing to a beacon node uh and a
new block has just come in uh I've
redacted a couple of the fields but yeah
that's the general
idea that's all great but we still
hadn't really solved where to send the
data um and it turns out it was a lot of
data fortunately for us click house
exists uh and it is goed uh it allows us
to store events at a scale that we
didn't really think was possible um in
July we hit four commas of attestations
in our click house cluster with just 14
terabytes of dis usage which is just
ridiculous uh given that those at the
stations we don't keep the signature
because we're getting it past the
trusted Point uh but yeah still it's
it's
crazy right data sets I'll hand over to
injury data sets
so we just started with Beacon API
events and sort of over the last two
years we've been uh trying to collect it
all all the data as the project name
suggests
um there's there's some overlap between
the data sets um for
example the beacon API event
stream and the lib PDP data sets sort of
collect uh
events at the head of the chain uh as
they're
happening
um whereas canonical sort of Beacon
events and execution events uh is sort
of the finalized data
um which can be
referenced from other data sets so
there's a lot of sort of cross
uh sort of queries that happen
um the there's also so the module Sam
talk about like the sentury um and the
lib PP centry uh we run lots of them uh
we collected lot of the same event from
lot of different regions around the
world
um and that sort of gives us propagation
times
um timing
data uh Regional data sort of what's
happening in Europe what's happening in
us what's happening in Australia sort of
allows you to
uh sort of differentiate sort of what's
happening around the world um we also
collect uh me relay data sort of bids uh
proposer
payloads um
we we have a sort of uh Discovery
module that sort of crawls a execution
layer
uh captures mol from different regions
around the world um and we also
capture uh canonical execution sort of
data
um we like to use open source projects
uh a couple here
so uh homies by Pro blab uh is a sort of
lib
PP uh Sentry I guess you could call it
that you run uh connects directly to the
lib PP sort of Gossip sub Network and
you can sort of capture that
data uh right off the network so it's
it's pretty good um and we also use cryo
by
Paradigm
um it allows us to get the sort of
canonical execution data pretty good we
just
uh sort of backfilled all the way to
Genesis basically made that public a
couple weeks ago which is a lot of data
um also check out Storm from Paradigm
talk later
today uh on data sovereignty should be
good uh also check out prob laabs talk
yesterday on how they do a lot of work
around the peer-to-peer Network uh it's
pretty
interesting
um yeah so we were
collecting uh a lot of data for
researchers
um we didn't really know what to do with
it uh there's sort of internal EF
researchers and a few uh researchers
outside so we decided to open source it
and sort of put in paret
files um um and make it available to
everyone uh you can read more there
there's a bit more sort of docs on how
to sort of access and but sort of
every uh some some tables will be like
per day or per hour depending on how big
they are so you can grab for example uh
Block events for that date and you'll
get the sort of raw data in park file so
if you want to do analysis uh it's
pretty easy to get
started
um yeah uh couple months ago
we allowed so we have we have a lot of
centries around the world
capturing uh Beacon API event stream
data um it's quite costly because you
have to run obviously a beacon node and
a touch of
Sentry um we sort of allowed the
community
if they want to to run this entry next
to their Beacon know
um you can opt into sort of how much
what sort of level of uh giip data you
want to send us whether it's
uh uh City uh country continent or none
at all uh so it's up to you guys but if
you want to sort of contribute we're
open to that as well uh it's just good
to get data from a wide variety of
regions and
setups and it just helps research as
well and all that data we anonymize so
uh you
can uh so no one can sort of track what
Beacon node you're running anything like
that but we also publish that data so
you can also check it out yourself as
well all right using the
data uh this one's pretty
interesting we use uh
Sig P's block
Scout uh block print block print tool um
which you can check out there it
basically us machine learning to try and
uh assign a consensus layer client to a
validat
index uh we then use that data because
we've got all this data we know who's
supposed to be a testing we know who's
not a testing we can then uh link that
to client data and it gives us pretty
quick response time to figure out what
if there's an issue with a particular
consensus client
implementation uh because you'll
see uh thousands potentially thousands
of valad days of flying for a
certain uh client implementation so this
is really actually useful uh we've got
other sort of dashboards grafana
dashboards we use uh for Dev Nets Nets
main
net um around block timings and stuff
like that that we use internally but
yeah there's a lot of monitoring goes
on sort of about the network about
timing um just gives us another view of
network
um there's also a pro blab which I uh
mentioned before so they do some cool
work so they have uh
uh weekly report that uses Z data
um it shows block arrival time I think
there's also uh the size of the
block uh and the distribution there uh
check it out it's pretty
cool
um yeah they're doing great
work uh after
a uh ESP data challenge um um which is
basically write a a blog post about the
uh the blobs upgrade um there was
definitely some cool blog uh post there
I just picked out one here which is
pretty interesting uh but yeah in the in
the future there could also be you know
more opportunities for data challenge
just keep an eye
out
um also
there's another one from Evan from I'm
going to put you that I don't know if
it's prev or prime v um but he did a pre
and post sort of analysis of
data uh
lastly uh some randoms user data um on E
research which is cool so yeah that's
basically
it thanks for that uh I'll pass it on to
Leo to uh talk about his awesome
work thank you Andre um so good morning
everyone uh thank you for coming to this
session um so um yeah I'm Leo from maps
and um by the way uh we have a booth uh
on front of classroom e in case you want
to drop by and keep um asking questions
about um what I'm going to present here
um or something else of the work that we
do um so yes I want to talk a little bit
about this um research that we did with
the chatau data uh just to put you in
context this uh happened uh last year in
Foundation researchers about um data
availability sampling and one of the
things that um we wanted to know is how
much time does it take to disseminate a
huge block in the ethereum network so we
were building a simulator uh that
disseminates um huge blocks uh over um
over the network and we managed to you
know after some months of work to have
some idea about how much time does it
take to disseminate uh the data of the
network uh but then we needed to somehow
um validate these results that we were
getting with our simulator and so we
were um you know scratching our heads on
how to do that and uh one of the ideas
was okay how about we pay a huge
transaction into a huge block in the
ethereum network and we you know see how
much that propag um how much time does
it take to propagate over the network so
we kind of artificially injected um and
by we I mean the inter ation uh injected
um Big Blocks on the network and then
thanks to the chatu um uh you know
Sentry noes and shatu we managed to um
see how much time does it take to
propagate uh then a couple of weeks
later I was looking at the data and um
you know we were recording the block
sizes for the last kind of six months or
or something like that and um we noticed
that there were plenty of Big Blocks in
the network and then at that moment I
contacted the the EF researcher so I was
working with uh Danny Ryan and danr uh
at the time and I say hi you guys are
still injecting blocks and they told me
no no that was that is over and I said
well I am seeing these huge blocks on
the network what what is going on and so
this is when we kind of discovered like
um that there is quite a significant
number of Big Blocks that occur
naturally organically in the ethereum
network and so this figure that you see
here is an example of that so this is 6
months I think from April to August 2023
and we are plotting all the blocks that
are over 250 kilobytes uh in in this
distribution so please notice that this
is a logarithmic scale on the on the Y
AIS right and then you see that we go to
up to over two megabytes um of size for
some blocks now um we also found quite
weird to see blocks over 2 megabytes
because if if you know how the um gas
system and the cold data works on the
blocks um you know that usually you have
and um you have um and and then if you
want to store one bite of of data you
have to pay 16 G and so if you make the
computation that says that the biggest
Block in the network should be only 1.8
megabytes and so um we look at that and
but in fact the reality is that if you
pay for zeros uh then that's for uh gas
so
yes this is preap yeah so this is this
was last year in 2023 so the question
for uh it was whether this is pre denap
or after uh 4844 this was last year so
this is before that and um yeah so and
then actually in in reality you could
actually construct a block that is up to
we had all these blocks uh then we kind
actually had a lot of fun and Tred to
analyze how these blocks propagating the
data and that give us a lot of
information about how much we can
increase the number of blobs in the
future uh for data availability sampling
and so on so uh thanks to chatu and the
centry notes uh that the uh devop guys
deploy over the uh over the planet as
Andrew was mentioning you can analyze
how things behave in different regions
of the world right and so so um we took
this set of uh Big Blocks and we tried
to analyze what is the you know the
distribution of a Ral in different
locations so uh one of the things that
you um can try to analyze is for example
okay how much what is the difference of
the blocks arriving between Amsterdam
and for example Sydney and you see it's
more or less like half of a second um
for um for this particular case and uh
uh you also see that most of the times
the block arrives within the 4 seconds
uh within 4 seconds which is great
otherwise um uh this uh things will not
work uh because the slots are 12 seconds
so you need this data to arrive quite
fast um that was one kind one uh type of
analysis that you could do but then uh
the other thing that we were actually
really more interested is how blocks
arrive um according to their size so we
put the blocks in different beans in
different colors from 0.2 megabytes to 2
megabytes right and then we analyze how
much time does it take for those blocks
according to their size to propagate
over the network and um this is more or
less the distribution that you see so
you see for example that there is
between 200 kilobytes to 2 megabytes
There is almost like a 2 seconds
difference uh right there um for for
that difference of of sizing blocks
right so that is interesting because
then that give us information about okay
what is going to happen when we activate
this was actually really great results
because 2 megabytes is actually a lot um
uh right now we have maximum six blobs
uh which is about 700 something
kilobytes and so we say okay that's fine
if we already have two megabytes blocks
that propagate over the network without
any problem and we didn't even notice it
that means that we can
allow for six blobs to uh to run over
the network and and and we will be we
should be okay okay and then um we
deployed tenun and we noticed that yeah
that actually works uh and then this
kind of data um give us information also
about how much further we can go in the
future right before we Implement data
sharding or Pras or whatever we want to
call them um so this is why this kind of
data is important for researchers and
and this is what um uh why this is
important
and another thing that I want to show is
so we we created this uh shatu dashboard
you can access it on the on the on the
QR code if you want uh that give us
realtime data on um on on data that we
get from from chatu so we have a bunch
of uh different things that I'm not
going to um go into detail but I just
wanted to mention uh maybe just a couple
of them and then you can go and look at
uh at the details later or again if you
want you can come at the booth and we
can discuss about it um so things you
can uh see here um so for example uh
this is a difference of how the uh the
number of blobs looked at the beginning
uh so this was during the first uh three
months of um after uh Denon was deployed
and this is how it looks today so at the
time you had like 56% of the blocks with
zero blobs and today you have like 40%
so the blue color the blue size here has
reduced significant L from the initial
uh you know the first months of Denon uh
up to today so this is the last month uh
just just like October um and you have
seen that the other colors have
increased in size on this pie chart
right so this has changed the number of
blocks with six six uh blobs keeps more
or less constant so in this case I think
it was 20% right now we're are
consta but the other ones are increasing
inside on this pip chart while the
number of blocks with zero blobs is
decreasing um Tony has also a very nice
post that shows uh how this distribution
changes over time not only for the
counts of blocks but for many other
things so I also advise you to check on
that
one and then you can also uh see in real
time the propagation of um of blobs over
over the network right so you have all
these events that chhat is recording and
then uh you can plot all that uh for the
last month for example you can plot all
the blocks and all the blobs and see
what is the uh latency uh of arrival for
all the all the blobs in the in the
networ right again you can access this
uh this data on our dashboard and we
also have an API in case you want to
play with the data as
well um another thing that you can do uh
is try to look at how much uh blobs are
used so that means how much data is
actually put inside so when you have a
blob and then at the end you have um
like 50 kilobytes of zeros then we are
assuming that that is not used right and
so you can look at those details and and
see what is the usage of um of the blobs
and uh so this is how it looks from the
last month so I think uh they are very
fairly good uh use of the of the blobs
so that's like almost 90% uh of the
space is being used in the blobs uh that
was not the case uh some months ago uh
the the it was something around 60% I
think uh some time ago so this is also
evolving uh you know as rollups and
layer TOS get more familiar with how to
use blob data um um they this is
changing so again if you interested uh
please look at the dashboard and another
question that was uh interesting to
analyze was how many M blobs sorry how
many M blocks occur after some number of
blobs right and this is important
because if it takes too much time to
propagate a block with six uh with six
blobs then what are the chances that the
next one is going to be a Miss because
the the block proposal was busy
downloading blobs or or whatever and and
and so this is something that we we
looked at uh this was actually a
question that was RA that was raised
during the interrupt in Kenya and and
and that we wanted to analyze and so
chatu allows you to do this kind of
analysis uh and so this is again one of
the pie charts that uh is is shown in
our dashboard in real time and you can
see that you know most of the blocks
that were missed um in the last month uh
occur just after a block with zero blobs
okay and and again you have the
distribution over here uh but it is uh
not such a strong correlation that you
will believe that okay every time you
see a block with six blobs then the
chances of missing the next one are very
very high that's not what you see in
this data and again there is a post by
by Tony uh on on that so also advise you
to look at that maybe he will mention it
later um yeah so I think that's uh more
or less what I have today and then move
on to the to to Tony thank
you
okay can you switch to my computer ah
perfect yeah hi everyone um um so my
part will basically be about how I use
KATU for my daily analyzis and I want to
focus especially on Padu which is
basically a library um in Python very um
if you're familiar with web free.pie for
example this is basically what I Tred to
achieve here allowing users to have a
very high level very easy access to the
P to the ex database and then yeah
coming up with some functions abstract
in the complexity of KATU although KATU
is not very complex but of course you
can always make it simpler by by
wrapping in within a python library and
yeah so let me show you the GitHub so
you can find um my GitHub there is a p
Patu library and you can install it very
easily by simply doing pip install Patu
and then you have to run KATU do setup
which will copy a configuration file
into your home directory there you have
to put in your credentials and then
you're um ready to go so if you need
credentials for xatu I would just say
reach out to the to the um e pands team
i' um they are very happy to provide you
those
and yeah so as soon as you have the
credentials in your home directory um
you can already start by doing something
like this um we basically okay now I
have to kind of
pardon ah the diming the lights is that
possible can we dim the light if that's
possible okay let me see how I do you
want to hold it
okay okay let's see oh it's taped it's
taped to the table okay then very nice
maybe you want to use that chair okay
okay so how I would start it's basically
importing the KATU database
import
Patu then I would create
a um the object that basically inherits
all the functions which is um Patu
do
Patu
sorry right and then you already see
okay I'm now collected to this um
endpoint and I will then call this
endpoint point so in the background it's
actually using SQL queries but the
python Library should allow you to make
that as simple as possible and the first
use case that I thought would be uh
maybe appropriate for having a quick
demo is what if we want to know what are
the Miss slots over
time so first thing I would do is I
would have to find the right function
everything is documented in the GitHub
but basically it's kat.
getm slots
right and of course I don't know which
columns are actually behind this data
set so there's a data set called um
Beacon slots or something similar and in
order to know which slot was actually
missed the simplest thing to do is we um
we query all slots and then we check
Which slot doesn't have an execution
payload right because if if there is no
execution payload then this means
basically there is no um yeah nothing
from the El in that block which means
either the block was Reed or the block
was missed so what I would do is I would
first get the docs from this specific
specific
function so I would just check okay I
need the get M slot I copy it paste it
and then I can see all the different
columns I can get from this data set
that is behind the getm slot function
for example I'm now interested in
actually only one thing I only want the
slot number right I don't want to I
don't need anything of any other column
I basically only want to know which slot
number was
missed so the query would then look like
the following I would have um kat.
get
missed
slots first I would specify the slot
range that I want to query which is done
like this let's say 9
million to 10 million
and the second thing is the columns I
want and this looks like
this and now let's see if this
works wonderful so what we get here is
basically now a python set with all the
slots that have been missed within slot
continue by putting it into a pandas
data frame
let's do that very
quickly oh I haven't imported pandas
yet
okay um
see the
F hundas that will be like missed
slots oh I called it
DF and then I think I need to specify
the column
here let's see if that works already
looks good okay that's nice now I have
um everything in a panas data frame and
the next thing I will do is I want to
map the slot number to the actual date
right this is yeah
please um this is all mayet yeah so the
yeah I I could mention
that um when you query for this for um
sorry it's actually here you can also
always specify additional parameters
I've skipped it now for um Simplicity
but basically you could say I only want
it for um a specific test net you could
say seoa heski but um per default it's
always main net because this is also
very important if you quer you always
have to make sure that you're not mixing
different um Nets up with each other
right because suddenly you get very
strange things I can tell you um where
you're like okay is that actually bro is
main not broken but then you find out
okay it's actually a test net but thanks
for the
question okay so the next thing I want
want to do is basically add a date
column and there you can do the
following so I will use um the um
Python's Lambda function that's very
handy for use cases like
that and then there is aat to helper
function
um let's see how it is
called get
slot daytime I guess yeah let's lose
this one and I would basically throw in
the slot number because every slot you
know we have 12 seconds so knowing the
Genesis time we can exactly tell at
which time a slot um appeared let's see
if that works wonderful and now we are
already quite far so we have the date
the slot and the last thing we need to
do is then to group by the
date um let me quickly
check
okay let me
see get
slot okay there is another helper
function that will be simple slot today
okay actually let me use another helper
function because now I got a very
precise timing with seconds and
everything but in order to visualize
this m slots over time we don't need the
minutes the hour and everything we
basically want to have it grouped by day
so there is also slot
today right and there I would do the
same right that's already a little
better and now I want to group that
whole
thing let's see
Group by I want to group by date I want
to sum up the
slots basically I want to count them
actually because otherwise I would just
add the slot numbers and then reset
index just this is all this is basically
all some Panda stuff to get a nice data
frame in the end index and in the end we
can sort it by
date right let's see that
works perfect and then to make it 100%
realistic I show you exactly how the
workflow works you can already see chbt
is ready I would basically do something
like give me uh I like the library
plotly a lot plotly
Express
chart
visualizing
my m Lots
over dead
days paste in the the my data that I
have and then yeah my um I had quite
good experience with cgpd so chbd is
really good at quickly quickly creating
those charts so first let's copy the
thing so I don't need the sample data
that jet gbt gave me but I can see it
put it into a DF variable so I would do
something like DF is my group
DF and then let's see if that works
already perfect right so this
is so this is um actually very simple
example how you get to the Mist slots I
don't know how much time it now took
like 5 minutes 10 minutes but it's a
very realistic workflow so this is how
how it looks like when I do many of my
analyzes of course it gets a little more
complex um especially if we want to go a
little deeper but for the Miss slots um
that's actually already it the next
thing we could do is maybe I should ask
is there a validator in this room or
someone who has a favorite
validator validator number one okay
let's do
Val okay yeah and they are not yet
withdrawn okay let's see because one
very interesting thing that you will not
get anywhere else but you get at exato
database is you can check when your
blocks are seen in the network so you
can check okay my validator proposed a
block and I want to know when did this
block arrive in Europe when did it
arrive in the US Australia and so on and
this is very interesting especially if
you want to check um who is playing
timing games um are your blocks late for
example if you build your blocks locally
you don't use MEF boost then this is uh
in particular particular interest of you
because you might want to know okay is
my block out there at the network in one
second into the slot or three seconds
into the slot right because if your
block is very late then you might want
to consider using either MF boost or
yeah looking for better peers and just
to make sure that you will not be be
reared okay I see validator number zero
is active let's let's do it with
validator number zero so there is
called.
get Block
event lock event that's the one I will
just do the same slot range again which
was where do I have it I got it
here let's do 9 million to 10 million
okay now we have to hope that this
validator had a slot in this range
otherwise we would just deviate to
another one he proposed in something
heos he proposed a block in August yeah
okay okay then we should find
something first I do the get docs again
because I'm um this is always handy to
see what KATU is actually offering
here it's actually do get
docks and then I paste in the function
name okay what I need now is they event
day time so there are many different
nodes all around the world different
clients everything and and I want to
know when are blocks seen by those
different clients and the block and the
time scene is here the event daytime
because it means when was this event
recorded and because the events are
recorded in real time as soon as they
are seen we should be able to use this
event
daytime then let's see what else we
might need
columns is equal to event daytime we
also need the slot I guess and we might
need the
we also need the
proposer ID right we want to know the
proposer which validated ID had did the
proposer actually have but you can see
this is I think not included in this
data set so we might need another query
proposer which tells us when which
proposer was supposed to propose in
which
slot get proposal
range and again that's how it works we
go into the docs again quickly check
what is there there is a slot and
there's a proposed a valid dat index and
I would then query those
two slot plus propos a valid data
index and then I should get a pandas
data frame that shows me the slot and
the proposal index now we can go on and
merge those two um data sets so here we
had the the block event which looked
like a slot and the event
daytime okay I should have not run it
again okay looks
good perfect and then we can do
something like pd.
merge
proposer we merge um left and we merge
on the slot
number left on
slot and then write on
slot looks
good right and then we are already
getting very close right now we have the
slot number the proposer that proposed a
block or was supposed to propose a block
in that in that slot and the event
daytime when we when the block was
seen the next thing we would need to do
is basically group another time because
for example if you want to know when it
was first seen right this is very
interesting because for example if you
want to know if someone is playing
timing games you want to know the first
time the block was seen in the network
usually that's in second like one one in
the slot but if you play timing games
then it's like a second three in the
slot and what we can do here is
basically group the whole thing we Group
by slot
and I think it works like
this regroup by slot and propos a
validator
index and then we take the
minimum of the event day time
oh damn
okay okay let me quickly
check let me make sure that I didn't
forget anything here yeah it looks
good um the maximum would be very
different because sometimes a node sees
a block let's say 20 seconds after it
was actually proposed right for example
if the nosis is slightly behind or
something so you will find sometimes
numbers that are much higher for example
let's say the I don't know Nimble SC
combination in Australia had some
problems right at that time then you
might see numbers that are way too high
but usually all those notes should agree
on yeah some rough number and I'm here
interested in the first time um we saw a
block because this tells us
um with a very high likelihood that this
is the time when the block was proposed
the block was actually proposed a little
um earlier but usually this should be a
quite good
approximation okay let me check because
I just see I I should have done reset
index set
index um let's do in place
true okay okay
now maybe there is no in place let me
try it like
this oh okay that's
fine and now one very interesting thing
is um you've all seen on Dune dashboards
on my dashboards we always use those
validat labels right and it's it's super
hard because you need those different
hristic to create those labels but you
can also use Kato in the future you can
have you can access it under kat.
validators and
mapping and what this gives you is
basically um the valid dat ID public key
the deposit address and all the labels
um that you see on D dashboards or on my
dashboards um about all those validators
so what we could do now is let's first
check um we can let's just merge it to
our data set what we have so far which
is the same again merge DF we Pro we
have the labels we merge on the valid
ID so
left then we do left
on okay the left hand side it was called
proposal validator
index and on the right side it was
called um validate
ID
right okay this looks good now we have
all that information in now data frame
and what we can do now is we can already
start looking for um what is our Target
validator doing valid dator with the
ID um
zero
oh okay we want
validator ID is equal to
zero oh there was no block let's try one
okay validate ID one had a block in that
time so for example we can see um the
time when it was seen um all the other
information that we need and finally
what we can do is there is another
helper function for you that is telling
you at which time in the slot the block
was seen so seconds
in
slot and then we do DF do apply so I
apply a function over the whole
row and then Lambda
X and then then I have to do ex to
helper
helpers and then I will do get time and
Slot
okay get the time and slot and what this
function wants is basically the slot
number and the actual time it was seen
in the slot so the slot number we got it
in the slot and then um the event dat
time
okay actually I forgot one important
thing here just see that I should have
converted this daytime into a actual
Unix Tim stamp but this is very easy we
do it like event
daytime is equal to event
daytime and then you can do something
like
um panas has a function that make sure
that your um field is
actually um at eight form
so daytime we can say UTC is true
because the all the times you find in
our
UTC UTC is
true right and then we can do something
like S Type which means we convert from
daytime to um
integer um
integer and this now gives us
milliseconds we we 1 seconds which means
we do something like um yeah 10 to the
power of um six this should be good
enough let's quickly check if our data
set looks like
expected the event daytime yeah we now
have uh the date time in unix's
timestamp and the final thing we do is
exactly this here we continue with x
daytime right um let me quickly check I
didn't forget
anything looks
good okay this is everyone who is
familiar with pandas knows why I do
certain things for example ply one
because we now put in the whole row and
not only one cell and let's see if that
works okay this is kind of expect that
let's see where the bug
is oh it's access one another ply
yeah right and what this what this does
is basically we tell him the slot we
tell him the exact time we uh recorded
the event and using that information you
can then tell at which second in the
slot was the event actually
seen and now we have all the information
we need for example what we can do is
let's actually do something like group
by we Group by
label and then we do something like
seconds and
Slot we take
the let's do the
median and we reset
index okay let me quickly check I think
median without the brackets
no Group by label seconds in
slot okay there's a typo
huh oh I still called
it ah I called it event
daytime right no I didn't do that
seconds in slot yet right this one ah
the S oh thank you thank you
so this should work perfect and then we
can do
median right and then we get the median
time when every validator slot is seen
you can see we've got a lot of yeah
looks like some solo stakers but then we
can also check like okay we all know
that P2P key there are some entities
playing timing games right so what we
could do is we do something like this
label
equals let's do
K so for K the median time when the SL
when the block is seen is
same let's see for
example okay no block in that time ah
wait
then you can see okay thatly with uh
especially pushing for a blop increase
in pcture analyzing big blops analyzing
Reks
and I
we
have so you can supply each
don't you get really like
um but do you
ever feel like you have a need for
better more accurate time because you're
using Google like maybe
there's or maybe maybe it's
middle yeah so we I don't know what we I
think we use Google on
uh yeah we could uh inter okay
but it's
ACC very accurate but I don't know if
Google would be
considered I'm just kind of curious
there's
yeah we
are en
I
all
you here
a e
e
back
oh oo
w
br
h
oh for
to
oh oh
your
spe e
he
oops all right good afternoon everyone
I'm super excited to be here with you
today uh and I hope that you're as
excited as I am uh so my name is is uh
Clement or Clement with the French
accent uh and today we are going to talk
and actually we are also going to write
some H
so uh first I would like to ask you
whoever or first like who knows what f
is okay that's pretty nice and whoever
like tried writing some have
already okay so we have a lot of
beginners that's perfect uh one last
question like are you like knowledgeable
do you know how blockchain works are you
like a developer uh what would be like
uh do we have like many beginners in
blockchain development
here oh like okay inary
maybe
experts oh W okay I'm impressed okay now
I have a lot of pressure all right so
yeah so now you might be wondering like
what the hell is H maybe you know a
little bit about it maybe you already
wrote some have
contracts um well we are going to start
with like uh the basics with the
definition that you can find on the
website so basically Huff is a low-level
programming language designed for
developing highly optimized contract
that run on the evm so well since you
guys are experts you know exactly what
this means but maybe it would be a bit
obscure or isoteric for some people so
we can have a look like a deeper look so
when it comes to Smart contract
development you have like many different
choices you can use like the most common
ones like solidity or Viper the like the
the usual languages that people are
going to use but there's a bit more to
it you can use for example like inline
assembly
so just like adding some assembly like
this like on top of your solidity code
you can lose like a solidity Standalone
assembly gold Ule you can use half so we
are going going a bit deeper uh in the
iceberg and if you're like a crazy
person you can write a memonic by code
directly but I wouldn't recommend
it so obviously you guys know this is
just like a very simple solidity smart
contract
uh very basic we just have like one
value we can read uh write this value
and then we can read this value uh
pretty high level very simple to
understand we have like the equivalent
Viper um same thing kind of high level
then here we have something a bit more
interesting so here we're using inline
assembly so we are trying to double a
little bit with the
evm um pretty straightforward also just
some uh different ways to to do
things this will be the complete
um assembly or Ule so it's like the
Standalone assembly uh version so it's
we have a bit more code but things are
still like a bit
simple uh then yeah if you want to have
some fun you have like uh the memonic
bite code we just like all the
instructions with some exad decimal
values and this is just like uh what the
compiler will output you can also write
this by hand but it might take some
time so now you you might be wondering
like why have why should we use have
because we have many options they seem
to be quite reasonable they seems to be
quite flexible we can do like most of
this things with them like most like
Unis swap is written in solidity we have
like curving Viper we can do pretty much
anything well we have to go back a
little bit into history and basically
Huff was created at first by the Aztec
team it was in 2018 and they were
working on like a smart contract called
um bear with me wire strudel I don't
know what this means but that was the
name of the contract and basically just
like a elliptic curve something similar
to zcash and they they they wanted to
write this in solidity they tried it but
the results were not convincing they
tried to use some assembly but still it
wasn't there so they started to think
about making some kind of way to be able
to write assembly but with extra
function extra features and so this is
uh how they came with the idea of
writing Huff of making
Huff so this is like uh the I think the
first half code ever written so you can
see it's still it looks like a bit what
we have now some stuff were removed I
think like yeah like template we don't
have this anymore but most of the the
things are still there up to up to this
date but when Aztec decided to create
half they had like very different
intentions at what we have now and like
I think I took this quote from their R
me actually so they said like half was
designed with a complete disregard for
semantics safety or basic consistency so
any similarities to production code are
purly incidental and have should on new
account be used by anybody so yeah this
is more or less what they said about
have they just wanted to build this tool
for them and the goal was not to really
to spread it it was open source but it
was not meant to be like
shared but what happened so we know that
obviously if you hear today uh like the
the story and like the road that that
was like taken is quite uh quite big and
actually have evolved a lot since then
uh one day like some guy decided to
write to take the code and write like a
new compiler in JavaScript and some
people decided to write then a new
compiler in typescript and more people
came and they decided to write a brand
new compiler in Rust and then more
people came and they said maybe it's
time to write like a new comp ER in Rust
again like from scratch so we have like
many different people many different
contributors uh just took this picture
from GitHub I think many of them are
missing but it's like maybe the main
contributors uh that contributed to the
core uh many other people contributed to
other things like writing libraries or
like making uh I don't know like writing
articles or making presentations to have
but this is more or less like a what all
the people that
contributed and this is what I showed
you earlier in solidities or in Viper
and this is like the same code in half
so as you can see it's not that big it's
it's maybe a bit scary but we don't have
much code actually it's kind of simple
uh we are going to go through it in a
bit but uh first uh let's answer this
question so like really why the hell
should I use
H uh I think that's an honest question
and uh yeah let's answer this question
so first I think what's really nice when
you're using Huff is that you have
access to like all the up codes it's not
the case when you're using inline
assembly even if you're using like
Standalone assembly you cannot choose
like all the up codes uh you cannot like
manipulate the stack for example you
have like many restrictions um when you
are using half you have access to well
pretty much anything that that you want
that's the the first thing um also we've
been talking about gas costs so this
chart might be it's not very like a
precise it's maybe a bit outdated I took
it one year ago I think uh Patrick
Collins shared it on Twitter so I just
like been reing it but it gives you like
an idea like this is like the we
comparing the cost to like create a uh
contract to deploy a
contract and here we're just like
comparing the cost to read and write uh
like um read and write operations so
using half Viper solidity Etc so it's
not exact but it can give you like a
rough idea of how we can optimize the
code obviously there are some stuff that
are in the solidity and Viper code that
we don't have but yeah more freedom you
can do whatever you want want if you
want to remove many safety features you
can do it so you can make your Cod like
more
optimized so some very specific use
cases if you're into me if you want to
write buts if you want to do like very
specific smart contracts you can use
half because it will be like purely
optimized to exactly what you want to do
and you can like reduce the gas cost
uh in a interesting way
uh yeah you can also do some crazy
things like this guy for example wrote
Unis swap V2 in half which is quite
impressive actually uh I remember some
people wanted like to deploy a DEX uh
that was purely written in half I don't
know if this ever happened but that was
like a crazy
ID uh we have this also heridity which
is like a way to run uh half code inside
of solidity by injecting the code yeah
it's a bit isoteric exotic I don't know
you will call it uh the way you want but
this is like a at the boundary of uh of
the the what what we can do and maybe
it's not a good idea to do this either
but I think like the best uh use case
for uh Huff basically is just to teach
you how the evm works so you can become
the evm
Chad um yeah because what we have been
seeing that
uh since Huff has been created or
revived we can say it this way many
people like me got interested into have
and we can learn a lot about the evm and
then we can get more familiar with it
and just become a better developer so
when you will be writing solidity code
you know exactly like what the code is
doing uh you can maybe write some
optimizations in inline assembly or if
you're debugging something so it will
give you like a better understanding of
like how the evm works how under the
hood everything is
happening and yeah like today uh I mean
it's been a while already but I mean
like nowadays there are many tools like
for example if you want to write some
Huff uh you can use like Foundry uh to
test your contract so it's it's
extremely simple there's a template for
that and then there are also like
libraries like hemate so if you want to
write something then I don't know like
an ec20 there already like a template
that was made uh but I think like the
best use case for this library is to
just go through all the contracts and
try to understand how they work I think
it's like maybe has like uh all the same
contract as soulmate maybe I'm not sure
but many stuff like ownable like many
create three libraries stuff like that
so it's very impressive
also so yeah
I think now it's time I made like a
small introduction so I think now it's
time to maybe start going deeper into
half so I think we're going to do this
in two parts actually first I'm just
going to go through like all the
features that we have in Rust so you
guys can get like a more uh like a
better understanding of what we can do
and how we can do it and then we'll get
to write some actual code so yeah as I
said basically like half is like some
kind of Assembly Language with many
convenient
features
and yes first I'm just going to go
through like how the evm works I'm sure
like all of you know but maybe there's
like one two people that are not very
familiar with it so I just want to um be
sure that we're all on the same page so
this is a stack this is where uh most of
the manipulations or handle like if you
want to store values if you want to
compute stuff like everything will be
happening into the stack so the way it
works is very simple you have here like
a pile you're just like stacking values
from like uh the top the bottom to the
to the top so you're just like adding
new values on top if you want to remove
a value you will pop the last value that
you just added and what is going to
happen is that let's say we have like a
b c and d and then you want to multiply
something so you're going to use the
multiply up code then what is going to
happen is that the evm just going to
take like the two latest values and it
will multiply them and it's going to put
them back into the the
stack uh yeah this is just like another
representation of the stack so still the
same thing um just be aware we have like
uh plenty of space like
only get like the three uh two first
values because we have only like up
codes for now we only have up codes to
get value up to the 30 uh second value
this will change maybe with the eof but
for now this is the way things Works um
and this is why we have like a stack too
deep in solidity also um then we have
the memory which is like another area to
save some values the memory is very
simple you have like an address and
value addresses and values they are
using like 32 bytes so basically you can
just store whatever you want uh wherever
you want just have to follow the this
pattern uh the storage is following the
same um pattern and we also have the
Tren in storage which is also the more
less the same
thing uh and this is the call data so
call data when we are referring to to it
it's just like a value that someone is
passing to your contract when they're
calling them so this is a swap on unisab
V2 uh obviously if you don't know like
um you might not know what are this
numbers but basically in your contract
you're supposed to so don't don't worry
too much about that but yeah basically
we can see like the the first bites just
the signature of the the function and
then all the other values like after all
the zeros these are just like um values
like amounts for example that are passed
around or maybe
addresses uh yeah just like a very cool
website if you want to be or get more
familiar with like the how The evm Works
uh you can go on evm do codes uh there
are many different sections the first
one is like up codes which is this is
what I showed you earlier just like a
list of all the up codes just explaining
exactly how they work how they work it's
like a very very convenient uh and then
you have the playground so you can write
some solidity code uh U code I think
also like uh memonic by code and then
you can just hit the the Run button and
you can see like what's happening step
by step into the memory the stack the
storage Trend and storage the return
values so it's it's extremely convenient
and it's a great resource just to to use
like to to learn how the evm works
there's like a half uh fork for this but
might not be updated so I'm not going to
to show it here and yeah I guess it's
time to just go through like all the the
things we have in half so first like in
half you can like have um you we have
the interface definition which is
something very similar to what we have
in solidity or whatever you can just
like Define functions you can Define
events you can Define uh errors also
it's not there but you can also do it um
and then you just have to pass like some
parameters so this will be useful in two
cases either to Define like a function
so people can call your smart contract
or if you want to call like another
contract let's say like an year C20 then
you can Define the transfer function and
then you will use this definition later
on to call the
contract uh we do have some built-in
functions in half so we have the
function signature the even hash and the
ear function uh these three functions
Works more or less the same way and it's
related to the interface definition once
you define let's say for example approve
and you want to call approve then you
will be able to use like function Sig
and you put just approve
um inside of the parenthesis and it will
give you the signature of the function
so you can call it the same thing for
the event if you want to emit an event
or if you want to revert then you can
use that for the error and get the the
selector we have also a right pad which
is just like shifting a value from the
left to to the right and then we have
like table start and table size
basically it's like a way to write a
switch statements uh in half we'll get
to that uh in a bit
though and yeah this is what I showed
you like uh at the top we're just
defining like two errors Panic error and
error like that's very original uh but
yeah then later on we want to revert and
then what we are going to do we can just
do like a underscore underscore a and
then we just put the um name of the area
you want to use and then this will add
the selector inside of our code and then
we can just like uh in this case we are
reverting with some parameters so we can
just like sort these parameters inside
of the
memory then we just have to call the
revert
function so another thing that we can
Define actually um constants so I think
it's pretty straight forward you have a
number you can just Define like a number
so it's like o x 4 20 this is an likea
decimal value but you can also Define um
numbers uh using like decimal values
most of the people do it this way and
then whenever you want to use the your
constant then you just have to put the
name inside of some brackets and then
we'll just like uh input the the right
value uh then we have jump labels so
jump labels are defined within a macro
or a function we'll see what they are a
bit later but basically like it's very
simple you have just like a piece of
code like for example uh success here uh
success is just defined by this um
instruction so like we we store
something and then we just return and so
what is going to happen if you look at
the top I think there's like a pointer
yeah if if you look here basically we
are doing something here and then we say
okay we want to jump to the success so
we just have to call the label SU access
and we jump to it and this piece of code
will be executed so it's quite
straightforward
also you can also do it with jump e so
you can add like a a condition to to
this
jump and then we have functions so
functions can have like uh arguments
that you can pass here and yeah there is
one weird thing here so takes and
returns so this is something that can
help you know what the function is
expecting um from the stack and what the
function we left into the stack so
basically what is going to happen is
that this function uh is expecting like
three um values in the stack and after
its execution it will left uh it will
leave sorry like one uh
value uh in into the stack so as far as
I know this is not enforced by the
compiler but it's more like a way for
you to just like know uh more or less
what you should have how you can manage
the the
stack and yeah so basically functions so
we have functions and macros and like
the big differen is uh that functions
they are um copied only once uh the
compiler is going to take the code of
your function and it's just going to put
it at the end of all the the bite code
and whenever you're going to call a
function then um in the execution of
your code it's going to jump to the
where the function is and when the
function has been executed is going to
jump back and keep on with the execution
of your
code which is different from macros in
the case of macros what is going to
happen every time you're going to invoke
this macro then the compiler is going to
copy the all code and directly put it in
your bite code uh what was compiled so
this means that if you're using like
macros then the size of your smart
contract might be a bit larger but might
be cheaper guys wise because you will be
like avoiding like jumping around back
forth and also by the way yeah so uh we
don't have it here but basically macros
they accept like parameters and you have
also the takes and returns uh
indications so we have like two
important macros that you need to know
we have The
Constructor it works the same way as
solidity actually so basically if you
want to execute some code uh when you're
deploying your contract then you just
have to put it into the Constructor um
and we have the main macro the main
macro is uh well quite simple this is
like the entry point of your smart
contract so whenever someone is going to
call your smart
contract the main macro will be executed
so this is where you want to do like a
the the function uh dispatching or
things like that but we we're going to
see that in a in a
minute uh we have jump tables so it's
pretty small and a bit long so yeah just
a way to do like um um switch statements
uh in half so maybe we can see that a
bit
later so yeah let's go so I think it's
time now to write some actual code so
yeah we need uh I hope like you guys all
have a laptop otherwise it's going to be
a bit boring for you I'm sorry so we are
going to write some code uh we are going
to use the template that is using
Foundry so if you don't have Foundry you
can install it uh using this
commands I'll just give you like a few
minutes to start installing stuff
so if you already have Foundry you can
install directly uh have like this is
like the
version manager I would say so you can
run this maybe I should have put this to
into the same slide I'm
sorry it just tell me if you guys all
have the first step done then we can
move
forward if you have any questions uh
about Huff or about how to install
things you can just ask me now I think
oh which version do you have
page okay is this like the yeah half up
should be like the okay check check your
Wi-Fi because I know like the Wii is a
bit long now
SC
 try again
War that's that's pretty annoying I'm
sorry I don't I'm not sure how to how
uh let's
see what is the Ripple you you
opened
oh yeah it's a bit weird we're going to
use Foundry so it's just going to like
uh do everything but I think like the
yeah yeah it should be working try yeah
try just like uh have
C Dash capital V and then just to see if
yeah I mean it's saying it's saying
compiling so yeah you have the right
version yeah yeah I think if you want to
output something there's like a command
if you check if you try help would tell
you yeah there is something like an
output yeah bite code stuff like that
yeah it's a bit it's a bit weird no wor
is all right so if you guys have Foundry
we can move forward uh then you just
need to install half and once you've
done this uh you can install uh so this
is installing the package manager not
the package sorry the version manager
then you can install the latest version
and this should be working so you should
get like have
whatever like should should be working
should be giving you like some
outputs
Yep this
one let me see if I can give you like
all the commments that would be easier
it's not
loading all
good you have now you have L okay oh
it's still installing oh yeah I
hope it's not going to take too much
time worst case scenario like I I still
have some slides so I can show you guys
but it would be better if we can just
like code
along yeah all
nice yeah installing
downloading
okay all good over here yeah
nice uh it's half
C nice
Perfect all good or installing that's
nice
all right I'm just going to give you a
few more minutes because I see many
people still downloading it takes a few
minutes I think to install
everything uh did you
okay oh perfect
nice all
good all good here yeah
okay do you guys need help or you good
good yeah thank you okay yeah you have
like both
versions everything is working H
Perfect all right all right yeah let's
move forward uh where's the
clicker yeah we're just going to be
writing like two very simple contracts
today I don't know how much time it will
take like we have two hours but yeah
since you guys are experts I'm joking
but like I feel like it will be pretty
straightforward so maybe it will not
take like the whole the whole time uh
yeah if you do half up you do havec uh
Dash cap capital V Forge Das capital V
you have if you have everything working
here then uh what you can do you can
clone uh this ripo just like a very
basic template uh I've made using the
actual Foundry template so you should be
able to clone this I just hope it's
public so just let me know if it
works and when you have this uh there
will be like one um extens if you're in
vs code there will be one extension that
is that is suggested uh it's called like
a half Language by half language uh and
it will just give you like a syntax like
uh colors stuff like that there is also
debugger but we're not going to use that
today so yeah just let me know if like
uh okay perfect good I'm relieved
nice uh it should be so do you have vs
code if you open the repo in vs code it
should like pop up the suggested
extension other otherwise it's called
like half language I think
got it
perfect yeah it would be better to be
using some having some colors otherwise
it's going to be a bit hard just to see
what what we're
doing uh yeah I just give you a few
minutes because I think the slide just
after this yeah like after this we're
just going to be cooking so I just want
to be sure that everyone can follow
work EX
okay good yeah it looks like we are all
set so what we are going to do we are
going to be writing our first half
contract so I think there might be a
source uh folder if
maybe it's not there anymore I don't
know but you can just make like a CR um
SRC folder then you can write the first
uh like create the first file you can
name it the way you want compute.
half
or whatever you want and then we are
going to be writing some
code so this is the first contract we
are going to be writing today it's uh
extremely comp licated you will see this
construct is just going to take two
values and multiply uh yeah no not
multiply actually add these values
together and then just going to return
them so as you can see it's extremely
hard to understand um yeah so let's just
like follow along if you guys have your
setup already you can code at the at the
same time so the first thing we want to
do that we are just going going to
define a function so here as you can see
uh this is what we're doing here let's
call it I don't like compute you can
call it ad or whatever just it doesn't
really matter um and so this function is
going to accept two parameters so we
need like one u in
it's going to return well something very
original one uint
that uh we Define and this definition
will be used by US inside of our have
contract but it will also be used by the
people that want to interact with our
contracts so then we have this which is
a macro here that we are calling comput
um so we can find this macro here just a
way to organize our Cod will be also
another way would be just to shove
everything into the main macro but
that's now we are like a educated people
so we are not going to to do that uh I'm
going to go through what's in there in a
second but first I want to talk about
the main macro which is just here so as
I said earlier the main macro is the
first thing that is is going to be uh
called when someone is calling your
contract this is like the the the entry
so in our case uh it's pretty simple so
let's go let's go through it so okay you
guys can so maybe you're writing at the
same time so I will slow down I'm
sorry so yeah first I think the the
easiest thing is just to write the first
uh function definition on top and then
you can go directly to this don't write
this so now we'll do it just
after yes
yeah uh
here
oh yes yes so why are we returning
nothing here we are not like leaving
anything in the stack it's because we
are returning here and this return is
actually uh the end of the call so we
are when we are returning something in
half we are actually like returning uh
values from the call so it's like the
end of the
call it's it's I know it's a bit the the
names may be a bit confusing right yeah
because we have returns with which is
not actually turning but just leaving
stuff in the stack so that's true that's
it can be a bit
confusing so yeah I'll just uh are you
guys ready or not to go through the the
macro all right okay let's go so now we
are going to do what we are calling like
function dispatching uh we have like a
very basic implementation but it works
the exact same way for example in um
solidity of Viper there are many
different ways to do this but this is
like the most common way so
basically uh what is going to happen is
that someone is going to call our smart
contract that will send us some C data
and we just want to know okay what do
they want to do like what is going to
happen so what we are going to do is
very simple we say we want to load the
cold data so all the values that were uh
given to us but we want to load it uh
starting from like the the first the
first bite we want to load it from the
start and then I maybe you know this or
maybe you don't know but basically like
uh function signatures they only have
like four bytes so how does it work when
someone is calling a contract in
solidity or like uh in the evm like the
the standards that when you're calling a
smart contract the first bytes the first
uh um the four first bytes are the
function um
selector so what you are going to do
that when you receive the call data you
are like okay I want to know what which
function we should uh call inside of our
contract so I'm going to check uh in the
C data what the guy wanted me to to talk
wanted to to call so we are going to
load the all call data here and this
like magic number um the value is like
uh 20 24 bits so it's like 28 bytes and
so what is going to happen here we put
in the stack like the whole like the
whole C data so we have everything and
then we say we want to move to the right
like all the C data so we are going to
move everything to the right but we are
moving to 28 bytes so we are going to
leave uh a value which is only well you
can do like 32 bytes minus 28 and you
have four bytes so this is like the the
function selector and so yeah we have a
function selector so we know which
function the sender wants to call but
now we need to check okay so do we have
this function maybe we don't have it
maybe it's a mistake so what is going to
happen here we are going to uh do
exactly like the function dispatching so
we are going to load here our function
signature so this is what we have
compute it's here this is what we Define
and this is what we are expecting and
then we're going to do like equals so
equal here is going to check if what we
loaded here what we sliced from the call
data the function signature function
selector we have is equal to this one
the the function signature that we are
expecting and then we say okay so if
it's equal then we'll have a zero here
uh no sorry um we'll have a one if it's
not equal we have a zero and then we are
just going to call the jump if up code
and the jump if upod up code is very
simple if this is zero then we're just
going to continue if this is one we are
going to jump to here compute the jump
label I showed you uh I explained to you
this earlier so maybe this is a bit
confusing just let me know if we need to
slow down okay you have question uh go
ahead what is it doing exactly
there on the on the function signature
how is is that could you explain dive
deeper into that yeah sure so basically
uh this is uh the same thing as solidity
when you have like a uh encoding
something or if you define a function in
solidity you can get like the signature
you can get like the four bytes and this
is the same thing here uh we Define this
function here like this is like our
function and oh I see so it's actually
Computing the signature function
signature from the compute exactly it's
it's Computing the hash
so the hash of this and then it's just
going to slice and only get the four
first byes okay could you go back a
little bit on the call data piece so is
it just leaving on the stack the call
the four bytes of the function uh
signature so basically here we are going
to it's a bit weird because like you
know you have to add the value on the
stack and then you call the instruction
so it's a bit hard to explain because I
need to explain like uh back and forth
what the values are but basically you're
like I want to from the start I want to
load the cold data so you will be
loading the cold data from the the first
bite from the bite zero uh but you are
going like to load 32 bytes what is
going to happen is that this function is
going to take like a slice of 32 bytes
and put it into the stack so you will
have uh so four bytes for uh the
function uh signature but then you will
have 20 28 bytes which will be like uh
non yeah it will be in our case it won't
be nonsense but it will be this uh the
first parameter but even it won't even
be like the whole parameter because this
is like 32 bytes so yeah maybe yeah I
should have put like a graph or
something it's it's hard to explain this
uh just like this but yeah it would be
helpful if you had like the stack on the
on the right hand side IDE I'll see if I
I can do something uh uh yeah I'll see
if I can do something actually after but
yeah basically the idea that you're
loading here 32 bytes of cold data
starting at the position zero but in
this case we only want the first four
bytes so we say okay let's just move to
right uh this element in the stack and
we want to move it to 28 bytes so we
move it like this and so we are left
with four bytes which is the function
signature so on the stack all that's
left from the call data is the four F uh
the first four bytes which is the
function signature exactly got it and
after we just check okay is this like a
valid function signature because someone
can just be like spamming our contract
so we need to to do like a proper check
uh which function do they want to call
um so we are going sorry we are going to
use uh to sorry we are going to load our
own function signature what we Define
here into the stack so basically the
stack will be their function signature
our function signature on
top and then we'll just do like equal
and both values will be removed and
equal would just leave a zero if they're
not uh equal if they are not like the
same and it will put a one if like both
signatures are the same uh I just want
to yeah there is like d here duplicate
one uh this is not needed here so I'm
not going to talk about it we'll see
that after but this is not needed here
so don't worry about it um and yeah so
we are are checking here and yeah like
the the final thing to do is just to
jump accordingly if the um function
signature if is valid if we have
something that we are
expecting then we jump here to compute
and in our case we decided to make
things the proper way so we Define like
a macro for comput the other solution
would be just to shove all the code here
but uh it's just cleaner to to do it
here and yeah if they don't have like
the a valid function signature we're
just going to revert uh we don't care
they they don't uh they're not like uh
asking for the right function so we are
not like uh reverting uh with any extra
data we're just returning zero value
just reverting the transaction but we
could have been like reverting and say
like anything you want like wrong
function signature or
whatever um all right do you have any
questions yes I'll give you the
mic I see by the looks of the function
and the main functions you have a revert
and return it's all recursive inside of
the evm or is just for showing they have
a r or function this are this are up
codes yeah I refer this H the AVM is
recursive when the when the codes oh do
you mean like uh is this going like to
fail the whole transaction or continue
the transaction the execution until you
put the return on robt or revert yeah if
you revert here I mean it's the same
thing in solidity you can revert here
but then uh the call can continue it's
the same continue infinitely until the
gas is oh no sorry okay I I understand
it uh not the right way uh this is the
end of the the transaction but it will
continue if there are like more things
after uh other uh up codes to execute
but if you just if you reach like the
end in this case we are rever
but it depends on like uh well how
you're writing your contract and who is
calling your contract because like if
you I don't know like
uh I mean it it depends I don't know
exactly how to enter this but uh yeah
like basically uh it will consume gas
but if you reach the end of the goal
then it will just stop consuming gas
know because it's only consuming gas
when it's like executing operations but
if there is nothing left to execute then
the transaction will just stop okay so
if I remove the return or or the revert
H it just stops completely uh if you do
that uh if you remove the return here
I'm not sure what you will do actually
um that's a good question I think we'll
stop because uh this is here actually in
like the the code this will be compiled
at the end of our contract and then if
you do this then after the contract has
ended so I think it will just stop but
otherwise you can if you forgot
something you can make a loop uh if you
put like here something then it will
jump here and go here and jump here like
it will be a loop he will consume all
the gas and just River twist out of gas
actually okay perfect thank you uh
question about the 0x00 c a load uh yes
so that sounds a bit heavy is that the
most efficient way of getting the
extracting the the selector mhm okay
cool yeah because you can when you're
are using like cold data load you can
only load like 32 bytes you're loading
like a whole piece of information into
the stack then you have to move forward
to um to get uh the the the actual
function selector there is another way
actually and I think you can load like a
single bite uh from the C data but that
that is not standard so you can do it
but it's not like the standard way so
you you could be like loading I don't
like the first uh uh you say okay this
is like one and if this is one we
compute or we we go to something that we
add if this is two then we can go to
something that will do minus uh subtract
things like that but the standard way is
like four four
byes um yes so we can continue so
basically once
you uh yeah once you are going to
compare here and then you have like as I
said like two different cases two
different scenarios either you can
revert so we are just reverting like the
the hard way oh we we might be going to
our macro
here and the macro is kind of simple so
we know that we have like two uins uh
because we want to add them together and
return the sum of these two values so we
are going to do the exact same thing as
we did here uh I mean call the same
function and so in this case we know
that the four first bytes or the
function uh signature so we are going to
ignore them and we say okay put into the
stack so called Data load but put into
the stack the call data starting at the
bytes uh for so ignore the first four
bytes and then put uh the call data so
this will take 32 byes of C data and put
it into the stack then we just have to
compute and we say okay we already
loaded four bytes for the function
signature we already loaded 32 by byes
for uh the first parameter the first
uint
byte that we already loaded so here's
the value
to load into the stack uh the next value
which is located uh after 36 bytes
um so am I clear I know this is a bit a
bit heavy if you have any question feel
free to ask them I don't want to lose
any anyone or maybe I already lost some
of you I don't
know so uh back to the first couple of
lines inside main um so I get that we're
putting uh the the function signature on
the stack yep and
then so at the end of the second line is
that uh if it's equal then compute
or it or does it say if it's equal
compute I I guess I'm I'm getting
confused a little bit the naming
conventions and like you've got you know
the your defining function compute and
then you also have a a label compute and
so yeah don't I'll explain so basically
yeah okay I I I understand what you mean
okay so yeah the the naming was maybe a
bit wrong but basically here compute we
have our
function and this this is only related
to to this this and this are
related that's it and then this compute
is the jump label that we are defining
here so these two are related but that
that that's it there are no other
relationship um and so okay sorry one
final thing on that so go ahead where
it's doing the the equals uh does it
know automatically to just pick the
first one off the stack and then compare
it to function signature compute so
because here we loaded like the function
signature from the call data so we have
like at the top of the stack we have one
function signature the one that the
sender gave us and then here we are
loading we are putting into uh equal and
we'll say okay I need two elements from
the stack two values from the stack and
we'll just take like the two first
values which are the values we need and
then so we have into the stack like
either one or zero and we say okay we
might want to go to the compute jump
label which is here and then we say okay
go for it but only if uh we have a one
uh if you have a zero then keep on
reading the next code so we will just
keep on reading the next code which is
just like reverting and revert just say
uh okay I want to revert do you want to
return some values from the memory
but we say yeah return zero like zero
value from the memory that that's it the
return here is very very
simple uh more questions
yes uh yeah basically yeah yeah and so
this is
like the most I think convenient thing
uh when you are like writing stuff like
this because because if you want to try
to write like a uh memonic bite code
basically you can you you can write all
of this without H but uh uh instead of
having like compute here and here uh
instead of having something that you can
read you will have to put like a value
and this value will be like a location
inside of your code so you will you will
say for examp for example sorry I want
to go to uh like the the in my code to
the location I
like 148 but if you add more code here
then you have to change this value you
know so this like this is just uh for us
to be able to do this like a very in a
convenient way um yes so we are jumping
to compute and as I told you just like a
macro so it's very very simple in this
case we are loading our two values here
we know that we are we have to avoid the
first uh four bytes so this is like the
next 32 bytes this is the next 32 bytes
after the first uh 36 bytes and what is
going to happen is that we have value a
and value B inside of the stack so we
just have to call add and add is exactly
what I showed you earlier so it just
like a with multiply just taking like
two values from the stack it will add
them together and boom there put back
into the
stack and what is going to happen here
is that it's pretty simple you'll see we
have one value into the stack and well
we now we want to return it because we
did all of this but now we need to
return our value so return here is very
simple uh you can only return stuff from
the memory so we have to put our uh
result the the sum that we just computed
into the memory it's very simple we are
going to use the M store up code and M
store takes one value here and one
location inside of the memory and then
we just call M store so what we've done
here that we are putting here um at the
location zero the value of AD so the
value of AD can be anything up to 32 uh
bytes obviously but it can be anything
and yeah we have like value in the
memory
yes wait for the mic sorry isn't there a
cost for putting that value in memory I
mean it's not like yeah obviously yeah
but why don't why not return it from the
stack because it's not possible it's not
possible yeah the way uh you can see
like uh I'll show you okay let me just
go back a little
bit um
are okay we are here so basically you
you can see like uh we don't have the
return um function here
obviously uh okay but if you go on this
website it's evm code you will see like
all the up codes are explained here and
you will see like stack input so
basically this is like when I was
talking about the the stack this is like
what is expected and this is what will
be uh left into the stack so in our case
we are taking Like A and B and we are
adding them so we go from two elements
uh from two elements to one element into
the stack and you can see like a there
is a description here and if you go down
let me share my screen actually because
this is like a interesting question can
you uh
yay all right all
right all right let me see
evm all right so if you go down here I'm
not going to take like too much time on
this but basically let's do
research M store here you can see like
um this is explaining how uh M store
works and if you go to uh return you
will see like
uh uh the explanation it will it will
just tell you okay stack inputs uh so
the definition is like the offset and
the size so basically this means that uh
we need to tell uh where we want to load
the value from so in obviously inside of
the memory and the
size that's uh that that's it so if you
can you go back to the can you go back
to the presentation thank you perfect
uh yeah so it's just how it works we
don't have a choice in this case but I
just wanted to show you the the website
because it's going to explain to you
exactly like all the like all the op
codes uh work actually it's pretty
pretty interesting and even if you are
not doing like going to do like some
crazy things with have if you just use
like evm codes and this um and half then
you can just learn and have some fun
understanding how things work but it's
still quite uh quite interesting oops I
went way too
far uh yeah no wait this is the second
one uh this is the test that's the one
uh yeah that's the right one so yeah and
then we have uh yeah as I just just said
like return so return return is
expecting two values so we have the
first value which is the size uh uh what
we want to return so in our case it's 32
bytes so it's like 0x 20 in EXA decimal
you will see like many half code are
return like all the values are in exod
decimal I guess because it's cooler I
don't know but it's like more by
convention so you know that you want to
return a uint 256 so you have to return
memory you can see we just stored it
here uh the zero like like mad B um and
so we can just like call return and and
that's it we have our whole contract so
if you guys have the code ready you can
try writing a test
actually so this is how tests are
working with
fundry uh and half uh so we have
something called like a half deployer
and this is pretty convenient because
it's going to uh take your contract
compile it for you and then you can just
deploy it so if you're familiar with
Foundry you you will see it's the exact
same experience as writing regular tests
very easy very simple very
convenient uh the only small difference
I think that might be a better way to do
this but we'll do it like this today we
just need to redefine our interface here
so it's say this is our contract compute
and then we just like copy paste what we
defined uh here we just need to put it
again here in an interface I think
that's a better way to do it but I'm not
going to to show it today
because yeah we might be running out of
time so yeah this is quite
straightforward you make like a a new
test uh file
then you just have to put like compute
test is test whatever uh just like a um
storage value for your your contract and
then what is going to happen is that uh
you just have to cast it so we Define
the interface here so you just cast it
or you can keep the address as you want
and then you're just going to use the
have deployer and you do like that sorry
you do like that deploy
and you put the name of your contract I
think the name of the contract the
contract is actually the name of the
file um yeah so if you do this the
contract will be deployed and then you
can write your F first test so in this
case we're just like expecting uh random
values that would be fuzzed and yeah we
say Okay so the contract should return C
and we we can just check that c is the
sum of a and
B I'll give you a few
seconds do you have any questions or
anything like that you're struggling
with like I I know this is a lot of a
lot of things all at once uh it can be a
bit tedious to set up everything so if
something is not working uh we still
have like a less than one hour but we
can take some time
to to fix some
issues can you just explain the math a
little bit uh obviously um you've got
unchecked there so so all of these un
explain the bounds on the uh is it just
yes so I'm I'm just uh doing here uh
unchecked because uh if we go here in
our I'll go back to the next slide I'm
sorry for this are copying the code but
if you go here like add we have no uh
overflow check so if we are just doing
like a uh a like the sum here and we
have we don't have unchecked then
solidity will do like a overflow check
and then the code will revert or we
won't have the same result as our half
code uh but yeah that that's an
interesting question because here in
solidity now we have the Overflow check
but we don't have it in in half so maybe
like something that you guys can do is a
way to prevent the half contract from
uh the sum from overflowing so that
could be an interesting exercise I think
there's already a li uh like a small
library in half mate that can allow you
to do this but it could be quite simple
to to code
actually hey sorry one more question um
you mentioned that over here um bit off
topic but you mentioned that
uh advantage of using Huff is you have
complete access to all the op codes um
what is one use case that you've found
where you can particularly exploit that
to achieve something that you haven't
been able to do in another
language uh it's so personally I haven't
been like doing I haven't been coding
for production things uh I was more as I
said like in the
beginning I really wanted to learn how
the evm was working and actually just
like writing some have was like the best
way because writing resources is a bit
tedious but otherwise like I've seen
many people doing like um uh yeah um me
boats boats or things like that they're
using half and yeah I mean like you have
more you have access to many things and
what what is interesting also is that
you're not writing solidity code you're
not riding like uh or even Viper um so
you can do like as we we saw earlier
like the function dispatching if you are
just writing your own bot for your own
purpose you don't care about that so you
can remove like uh a lot of the safety
features from solidity because if you
know exactly what you want to do you can
achieve it this way but uh yeah like
some some stuff also in uh like main
difference is also you have access to
more up codes I don't have like an exact
example here but I would say yeah like
it there are so many uh other cases but
for this one specifically I'm sure we
can find it but I don't have it in
mind
yeah yeah could be a example
yeah all
right so yep okay let me
see oh you put like a uh you went eight
yeah just put like a
yes I think yeah if you have like
compilation failed I think there is one
step that we haven't been doing yet and
it's just
installing uh the packages so if you
have this obviously if you have the
first contract and then you have this
then you can try uh just be sure to have
everything installed so you can just run
like Forge
install uh because now you might not
have the have deployer module or
whatever it's called uh and then if you
run like Forge test it should be working
I hope so I tried in my
machine same thing like uh here you went
eight the result you should just use
you it will work
all right let me know if it's
working yeah the test is passing hell
yeah yeah you have the the
mic is there a way to uh write half
codes like in line
in solidity yeah actually there is one I
this is something I I showed earlier uh
like there is something called
idity I guess it's called this
way but this is very very experimental
and like this is leading to many uh
where is
this it's here yeah so it works but I
don't think this should ever be used in
production because like the way it works
that it's just injecting it's compiling
your code it's
injecting uh your code so I I think I
mean if you uh so if you really want to
use have for something in production I
guess like uh something interesting
would be just to have like
a deploy maybe a library or a contract
so I like some kind of precompile you
just make a contract
that is Computing something you deploy
it and then you can call from solidity
you can call this contract but yeah like
this is highly
experimental uh it hasn't been updated
in a year so I think it was more made
for for fun that than something
else so are all the tests
passing
no you forgot the unchecked
sorry I just I just saw this yeah if you
because so basically you have the exact
issue that I was explaining so like here
if you don't put the uncheck then the
test will revert because um adding these
values will cause an overflow and we
still have like overflow checks in uh uh
in the
test any issues
okay all right so we covered the first
contract uh yeah I have another one if
you guys are are interested and we still
have 45 minutes if you want to suffer a
little bit
more failing test okay let's
see uh okay did you put the unchecked
yeah yeah yeah that's
uh okay let me okay the code I think the
H code looks
great yeah yeah it doesn't
matter uh yeah that's unfortunate
okay if so if the tests uh or failing uh
you can still check uh if you open on uh
you can open this uh like a URL in your
browser and you can check or you can
change the branch directly I've made
another branch called
finish and you should have the first
test uh this one I mean the contract and
the test I hope they will work but if
they don't work maybe there's a bug in
my code I don't know so if you can find
it then that would be amazing maybe I
made a mistake
somewhere yeah so it's passing so what
I'm thinking now
maybe I don't know maybe some values
yeah found
it that's that's really funny do you
have
yes yeah when you are returning
something yeah but like what
like what if it's like there's operation
happen on these
two
and you canot from the stack you need to
put into memory this is the way return
Works return can only read from the
memory where's your
oh uh try to rename this to Source
SRC yeah here you put contracts I think
it won't work it's just naming
conventions try try this and let me
know
yes uh
compute is the name of your
file
yeah yeah you uh yeah yeah actually I
think I know maybe it works okay
perfect okay let's
see what the issue ah cont example
that's that's
funny okay go back to the file have yeah
let me
see yeah yeah no the problem is in the
code now let me see call data you're
loading the right oh you forgot ad uh
after call data uh no no before
before uh yeah yeah nice all right any
any
issues still failing oh gosh
yeah what was the
issue oh no compilation try to do like
uh uh yeah try to run uh do like force
test Das Dash
Force oh
sh that's that's weird why is he running
a test if you don't have a test oh it
says
revert oh
yeah I'm I'm not sure exactly check on
the other Branch uh you can switch the
branch go to the finished Branch if you
want uh yeah if it doesn't work after I
can I can look into but I think we we
are going to move forward because feel
like you guys have the code
working uh so yeah we still have like 40
minutes so maybe we can go through
another contract
uh yes so this one is more or less the
same thing it's not exactly the same
thing but we are going to cover one
extra uh one extra up code so now in
this case what we want to do is
that we you will see it's very simple we
just want to be able to get a value from
the sender and store this value and
if the sender wants to read this value
then we are just going to return it so
once again very very basic contract but
this will allow us to uh cover a few
different
things so in this case well we are going
to start by the interface definition
once again so we are going to Define two
values the first value is just uh two
functions sorry and the first function
is just set value so in this case we
want well youu into 56 which is
very original and then we're just going
to make like another function called get
value and in this case we don't want to
get we don't want to set something but
we want to return
something and then we are going to cover
something else so we are going to make a
new constant called uh value location
and so we are going to use this which is
like a yeah some kind of built-in
function that we haven't seen yet called
free storage
pointer and basically what this function
does uh it's very simple it's just going
to give you uh the location a location
where uh the storage is free so in this
case if we call it now it will be zero
because the first uh location that is
free is located at index zero very
simple if you call it again it will be
one because we have this value already
taking the first slot so the slot zero
and then after we can take the slot zero
one two
Etc any questions
no all
right um and then we are going to
directly to the main entry point so this
is going to be almost the same code as
we as we did
actually so we are loading the C data
from the start we are shifting to the
right uh 28 bytes and what is going to
happen here that uh I told you earlier
that we don't care about the uh
duplicate one the DB one but in this
case we need it because what is going to
happen here that here we have the
function signature that we received from
the sender in the
stack and we want to keep it for later
so we are going to duplicate it so what
is going to happen is that we will have
two times the function signature we
received from the
sender then we're just going to be doing
exactly what we did earlier here so we
are going to load uh for example the
first set value the signature of the set
value function so we want to check okay
maybe the sender they want to set the
value okay let's see so yeah we load the
set value function signature and we do
equal and yeah maybe it's equal maybe
it's not we don't know so we said okay
you can jump
to set if the value that we just
received is uh equal to set value and
then you know the drill it will do it
will go here and then to the macro set
value and it will go here but if it's
not the case then what is going to
happen is that well jumpy is just going
to do nothing and so we will go back
here and in this case also dump one here
like like ad d one sorry is not needed
but yeah don't about it but this means
here uh when we called equal we we
consume the first value that we loaded
here and we consume this value too so
luckily we duplicated this value into
the stack so this means that we have
value a two times the value a then the
value B then they all consumed so we are
left with the value a so then we can
load the function signature of get value
then we have the value a and the
signature of get value and then we can
do the same thing again equal and if
it's equal we can jump to the get uh
macro and so we go here and then we
execute it
here it is clear or not
no I'm I'm sor sorry I'm sorry do you do
you maybe you have a question and uh you
can answer like you you have a specific
point that you don't understand and
maybe I can explain it like in a
different way can we have a mic over
please thank you clo um so dup one is
that duplicating the okay it is
duplicating the stack exactly the dup
one is duplicating the first item of the
stack on the stack so it's duplicating
the call uh the function signature of
the sender yeah so it's duplicating the
function signature that we received and
so basically the D one here uh is just a
way for us to avoid doing this again
because we could be doing this and then
we do this we don't duplicate but if uh
it's not like uh if the standard is not
willing to execute that value then well
we have to check if they want to execute
get value so we we need the function
signature again so we could be doing
this again but it will be costly it will
cost so then don't you have the function
signature on the stack three times uh
because you call duplicate one twice
yeah this one is an error oh okay okay
I'm sorry about that this one is an
error because I just like uh copy pasted
that that line and then I change I mean
there's no there's no harm because
you're not doing anything after that but
you do have the function signatures this
could be leading to some issues in our
case we are just reverting right after
so it doesn't matter but I can show you
after like for example in the case of
erc20 or something like that uh but yeah
you can have like uh many different
things so you will duplicate every time
but on the last time it's not needed
you're right okay all right that makes
sense so um a question so when you do
the equals it's actually taking two
values that's on the stack well no well
taking one value that's already on the
stack and the other value is the one
that's computed uh as part of that call
uh it's taking like when you're doing uh
yeah equal is going to take so uh this
so we have this value in this that's on
the stack and then so you can imagine
that here we duplicate so this means
that this value is here it's like we are
cloning
it if you don't mind I'm just going to
interrupt you really quick because the
question I have is the function
signature that looks like a macro is
that putting the value of that it's
Computing the the function signature of
get value right and is it putting it on
the stack and then the equal equal
function is Computing the equal between
those two values that are on the stack
okay thank you yeah because so this is
exactly what you said here equal is
going to take the first element of the
stack and the second element of the
stack so that was uh duplicated from
this so we have like uh here our stuff
that was computed and added to the stack
and then the stuff we just computed
ourself perfect thank
you uh yeah and then it's kind of simple
here like uh to set the value well we
just go to the macro here set value and
well this is exactly what we've been
doing earlier we know that uh we need to
avoid the first uh four bytes because
this is the function signature so we
don't really care about it so we just do
okay we want to load uh 32 bytes
starting after the four uh bytes and
then we are going to use a different up
code that we never used called s store
so you can see like previously we've
been using M store which is very well
explicit memory store and in this case
we want to store in the storage because
the user us is setting a value so we
want to keep it for a long time so we
are going to call sore and sore Works in
a very similar way to M store it takes
like one U location and one value and so
what we are doing here in this case I
showed you this earlier when we talked
about constants we are just going to use
like uh within brackets we are going to
call a value
which was defined by free storage
pointer which should be zero so this
means that we want to St store in the
storage at this location the value that
is starting at the cold data after the
first four bytes so kind of simple it's
just weird that I think the weirdest
thing here that you're just doing things
in Reverse you have to put element in
the stack and then you have to call a
function that will will take all the
elements uh in the opposite direction so
it's a bit weird to think that way but
to get used to it and yeah like you
mentioned like many times like the the
stack how it works uh and so like a
convention some people are doing and
actually I think there's a tool for that
uh some people here like uh add comments
and within the brackets they just put
what is in the stack so they will say
okay here
we have a value here so because we
loaded this value and then they say we
have a pointer here so the stack is like
the pointer and the value and they they
say okay we are calling uh storage uh
store so it's going to use two values so
then the stack is empty so it's like
also a nice way to be able to track what
you're actually
doing question yep so um on the stack if
what is the first argument is is it the
one at the topmost and then the second
argument is the one below it yes so when
you're calling a function you will take
like the one at the top and it will go
like it will remove them one by one so
it will always take what is on top okay
so the topest one is the first argument
in the function signature and then the
second yeah in this case yeah would
first use like the function signature so
if you are doing like minus you will do
this minus
this um yeah so this function this macro
stor is kind of simple and then
uh I
think I think there might be an issue
actually with the code okay let's let's
see how it how it works WR this uh the
test was passing actually but I think
there might be an issue uh from what you
were saying earlier so let's see uh then
uh the
get value macro is kind of similar to
what we've been doing but yeah we're
just going to use like a new up code
called uh storage
load uh and it's it's very simple you
just say I want to load into uh
the uh the stack I want to load uh the
sorry I want to load into the stack the
value that this stored at this location
so we're just going to use the our value
location constant here we put it into
the brackets then we just say yeah I
want to load this value and the value
will be put into the
stack and
then same thing as before we put this
value at the position zero into the
memory and then we call return and we
say you can return 32 bytes starting at
the position Zero from the memory and it
will return the value
so kind of straightforward yeah just a
different kind of question here uh if I
if there's a smart contract that's on it
that's been deployed but the code was
not published can you um decompile it
into Huff uh I think there's a
decompiler yeah I'm not I'm not sure if
it's really uh powerful but I think
there's one yeah there's one because I
was just thinking in terms of reverse
engineering the smart contract right you
can use it actually that's pretty pretty
nice and more convenient that reading
the the bite code
directly um yes so I think that's it for
this contract it's kind of
straightforward we already saw like the
dispatching uh and like to store into
the storage or to load from the storage
it's very simple um yeah do you have any
question so far yeah
oh you put a
stop I'm not sure yeah I think it's
needed I'm not sure if it's needed or
okay let's let's see we can check with
the other
Branch uh go to the Finish C is the
same okay I'll let you check and I'll be
after uh any extra
questions yes how does uh Huff compared
Yol uh well I think like
well the main difference is that uh as
we were saying like earlier you have
more uh Power in a sense that even in y
you cannot manipulate the stack I think
uh there are a few things that you
cannot do uh in half you can like you
you can like duplicate elements in the
stack you can like swap them yeah you're
free to do whatever you want so you you
can do like more optimized things um
would say that's about it but yeah I
guess it's also depends on the use cases
but yeah I'm not aware of many contracts
that were written in pure Ule but uh
yeah if you're using like Ule like
inline assembly in solidity then I mean
the the obvious reason would be just to
you to be optimizing very small uh
portions knits of of
code uh if you want to
yeah so this is the test for the
contract uh that we just wrote so still
very very simple straightforward we are
also using the half deployer and yeah I
did some console log just for the the
sake of it
but basically still uh quite
I'll just give you a few minutes if you
want to write the the test and try out
oh you this you
don't yeah
yeah confused are you running the oh but
you running the test from counter and
then you're checking that maybe the
other test
okay
okay yeah just let me know if the the
tests are passing or if you're having
any any
issues for
how is it going
more things it's uh oh you added more
things yeah nice okay cool all
right yeah that that's uh I don't have
another contract after that so if you
want
to we can just be like uh talking if you
have more questions or if you want to I
don't know add something else into the
code and you want me to let you know how
we could work feel free to yep
what what's uh the issue
now
failing
increment what is doing in
yeah oh okay you want to oh I see nice
Okay cool so yeah you're loading the
cold data then you
loading uh it's good actually it should
be working it's
there yeah
yeah to be honest try try adding like a
return I think that might be the the
issue I'm not sure
here we're not adding it yeah I'm
just I think we might need it
uh yeah I copy paste the just uh return
nothing just to see this will return
something so just
uh so
what you need for example if you put
like zero zero return it will just end
the transaction so you don't have to
return something we can just like uh put
this to return
transaction uh to yeah to stop the
transaction and if uh are you familiar
with
fundry read okay oh it works perfect
okay that was is it nice okay all good
yeah if the tests are failing you might
want to add uh here I think it would be
better especially if you change the code
uh here you can do like uh you can add
after that line uh return so like this
but instead of having like 20 here you
can just like put zero zero return so
here you can just like return nothing so
this will just let know that uh after
calling this macro then you just have to
end the transaction cuz otherwise what
could happen is that uh set value is
executed and then you go here to the
jump label and then get value is
executed also so you have some weird
scenarios so I think it would be just
better to do like a add return here just
return nothing just Z zero
return this should fix things if if you
have this uh it's not working try to do
what I just said yeah uh function just
yeah yes stop also works but I'm not
sure about the gas
cost yeah you can stop also but I'm not
sure about the gas cost we should check
because sometimes stop is just like
consuming the rest of the the gas or
things like that so what yeah you can
yeah you can just research and see like
a alt execution oh yeah yeah you can if
you click here you have more UHS
details yeah successfully yeah you can
yeah it it works with you can also add
stop yeah that's another way to just uh
uh end the execution of the macro
safely for
yes
sure uh
mtip number of yeah if you're like
overloading you mean uh I think you
that's a good
question that's a good question I need
need to check to be honest I have never
done it in half so I I don't know but uh
that's uh I I don't even know if it
works
actually let me let me check but I
that's a good question
yeah I don't know I have I don't have
the answer now but uh
like 10 minutes left 12 exactly but uh
yeah I think
maybe you had
enough is want if you have more
questions feel free to ask them I will
be happy to answer them if you want to
cut like a few more minutes but
otherwise uh well just want to say thank
you guys for I lost the clicker
again uh thank you guys for attending
this Workshop I was pretty excited to
see many many people and I was happy to
see that you guys were staying until the
end and working and building the the
contracts and even adding more more
stuff so that's pretty pretty cool so
yeah that's it you can if you are
interested you can follow Huff on
Twitter uh there's the website there's
the Discord um we all working on half
two uh the new compiler is being uh the
compiler is being re R return uh from
scratch actually uh we are going to be
working also on the E F support and many
other uh things so yeah feel free to
follow for for more good stuff thank you
guys thank you
but uh so basically like we are building
a differenter
but trying to help
join are
almost
hello oh it works um nice to meet you my
name is
Sasha today um we will have a little
presentation about waku uh it will be
two presenters me and Ian uh we will
explain you
um overall problematics of peer-to-peer
networks um we will go
through
um uh common parts of peer-to-peer
networks challenges that are faced
usually and uh uh how they usually are
dealt with and the common tradeoffs uh
then we will explain a bit about waku
which is a functionable peer-to-peer
network uh that has uh some answers to
some of the problems that will be
mentioned and we will show you some
examples
and uh we'll try to do a bit of
programming so uh yeah uh how are you
guys familiar raise your hand if you are
really familiar with peer-to-peer
networks you build one by yourself uh
you know ins and out of f P2P or Dev P2P
or you build your stack so maybe you can
uh uh enjoy this talk I hope as well but
uh otherwise it's more of an
intermediate level so um yeah uh let's
start so uh why do we even care about uh
peer-to-peer
networks so first of all is um that due
to architectural uh decision of going
voice PTO pure uh we guarantee some uh
potential decentralization and
censorship resistance that comes out of
it and uh why do we even want it is that
because we are in crypto space right I
think this is like something that does
not need a lot of answers but then
um what usually this uh solution is made
um to introduce some set some degree of
privacy and that data ownership it's to
provide this service to the users of our
applications networks
whatever uh other properties that peerto
P networks guarantee that usually they
are full tolerant or uh resilient and
this comes out of the fact that uh we
don't have single point usually there
and uh we um uh can survive as a as a as
a set of nodes if one two or even half
of the nodes are offline or down uh and
then uh potentially we can get some
scalability out of this decision uh this
is questionable actually because
peer-to-peer networks are known to be uh
difficult to M write uh but U
hypothetically we can reach a high
degree of scalability
naturally um what challenges there so um
first one is that we need to build one
and maintain ourself uh this is
challenging because uh the peer-to-peer
networks has a lot of complexity in it
like some set of protocols being
implemented so we need to make sure that
all the peers understand each other and
then if we let's say release a new uh
version of our software we need to make
sure that it somehow like gets
propagated or something this is quite
challenging uh as well as there is a lot
of devops involved like whenever we um
whenever we upgrade something uh
something might be down then it impacts
some some other people so uh it's
difficult to to to do right um
reliability is also a big challenge in
peer-to-peer networks um why uh because
uh it also depends on the degree of
nodes amount of nodes in the network the
less there are there are more
reliabilities so like if there is note
it's quite reliable if there are more
then um it becomes challenging um to
make sure that all the protocols to
function correctly and the notes
propagate the messages in the right way
then uh Network discover is a huge bottl
NE there um all projects made uh
different decisions there but more or
less there are some patterns that
everyone follows um and security and
traffic management like depending on the
architecture of the peer-to-peer Network
we go with
uh we incur different uh pattern of how
uh data will be propagated so let's say
for the case for vaku that later will be
explained by my colleague um Wago goes
with gossip sub architecture and it
incles some particular way of how
message is going to be exchanged in the
network uh other people might go with a
mixet or something else so depends and
uh for the security uh there are more
parts than just you know encryption uh
any that other people cannot read your
data there is also a security of overall
Network how like identity Seft like
let's say if someone can pretend to be
someone else in the peer-to-peer Network
it's quite challenging and has to be
addressed on a software level somehow uh
so we can use different uh um algorithms
here uh the other problem there is that
um how to make the network not to go
down because of like some some someone
malicious there let's say if uh we have
a PE that produces 90% of the traffic
overall right uh we don't want single uh
node to consume all the resources of the
network yeah this is a security question
as well um uh so um how to build a
peer-to-peer Network so these days there
are couple Solutions usually everyone
goes with CT do it yourself diyi um and
many projects just go there try to
figure it out they figure it out somehow
because all of us are quite good
Engineers I I I hope and uh uh all of
them just answered the questions uh just
sold it and uh release they use just not
Network stack whatever is available in
the language of their choice and um
that's it uh but other projects has
figured out that it can be scaled
somehow so uh Dev Dev P2P and Le P2P got
born so they uh they appeared
approximately the same time def P2P is
very dedicated for etherium stack and
it's like something that all etherum
nodes implement but there is also l2p
which was um more of a generic stack
like it can be used by any project it
does not have any dependency on any
blockchain
whatsoever and it's very modular uh for
waku it is the case that we built on top
of l2p and we extend it with uh our
protocols we we continue building from
there um so shared Parts uh it also
somehow related to the challenges that I
mentioned and uh usually we care about
peer Discovery in the peer-to-peer
networks right this is obvious unless we
know our peers we cannot form a network
and there are multiple choices that uh
projects go with uh some of them are DNS
Discovery we call some particular we get
retrieve some DNS records from there we
understand like this is a set of noes
that we can use and we go go on with
them uh some might some choices might be
like an exchange further exchange like
we ask the nodes if they know other noes
mod right so very natural way of uh of
discovering a network same as humans
behave uh then uh informational exchange
um a format uh usually the networks try
to converge into one format so hence
there is some specification for a
package of data that is going to be
populated throughout the network uh then
uh something specific to the networking
in the in the internet is that some
peers might be hard to re reach uh so
hence we need to uh use some whole
punching techniques uh which means that
if I cannot dial you directly maybe we
can bypass it somehow like you dial me
instead or uh let's say uh if uh it is
not possible it's approximately I think
the case for uh some protocols we may do
relaying so which means that I am going
to ask some other peer to relay you some
some data that I want you to see and you
do the same so we bypass this uh this
this this W in between us um then the
other uh shared Parts is that all the
networks try to somehow secure
themselves from dos so hence some Doos
protection come comes in play and spam
protection how it should how it can be
addressed by different meanings usually
it might be like some tokens token
exchange there might be some uh common
shared uh uh record of uh peers that are
like reliable whatever they can be used
can be trusted so different ways um but
one of the most difficult Parts here is
that it's hard to make it uh in a
privacy preserving way so that we don't
uh release some Identity or we don't
even know who is pure actually is uh and
vaku has found some answer in
partnership with other projects in the
space um other shared Parts is that
transports transports so uh this one is
very important because uh if our nodes
in the network uh Implement more
transports such as websockets websocket
secures uh TCP UDP uh web RTC web
transport the more they transport they
Implement uh the more clients they can
reach uh like let's say if uh we have a
websocket implemented we can be sure
that our node can function not only
between like some uh uh some Ser servers
right but also with browsers so hence we
uh can serve more users um and much more
so there is a bandwidth management like
how to make sure that our nodes are very
ecological in the resources that they
have uh the reputation like we want to
make sure that the peers which we are
talking at hog right now uh are more or
less fine or not uh encryption this is a
huge question as well like we don't want
the whole network know what we are
talking about about what we exchange
right and and routing uh more or less um
so hence there are some tradeoffs that
we make uh while building the networks
and one of them is that do we want to
have a one huge Network or we want to
have like uh some Sub sub networks that
somehow talk to each other later on I
don't know um if we do some sharding how
many of them we want like one two two
groups three groups depending on the
content content Exchange maybe right so
this is a conscious choice that we as
developers have to make uh here then uh
a message size right the data data
packet the bigger it is the slower
propagation of it will be through the
network regardless of the architectural
choice of it right so we want to be
cautious of it and we want to make the
best choice for our particular
particular
need uh and then rate limiting right we
don't want uh anyone spam the network
and some all resources so which
technology we use are we fine with
having let's say common Ledger of
trusted nodes or we want to be more open
like publicly available Network that
anyone can join uh so in that case what
do we do uh how do we address it I don't
know it depends uh incentivization right
so some of the projects public networks
have no incentivization but they still
function well uh and why it happens is
that because people share a common cause
they want to be part part of this
network because it let's say gives some
privacy it gives uh underprivileged
people access to internet without them
uh fearing for any consequences or
something or just buying drugs whoever
whatever
um and Discovery protocols like there
could be a different way of how we can
discover so we do some tradeos here as
well some can be slower how can be
faster uh and uh what waku does so here
I'm going to pass it down to
Ian and he will tell
you thank
you thanks hello everyone um okay and in
this part of the talk we are going to to
overview the the actual implementation
of the the Wu protocols as my colleague
mentioned is um um an opinionated
implementation of the uh of our view how
we consider is um good to to solve the
the well-known problems such as the
discovery the the problem to of a nut um
or a firewall the problem of routing uh
this is covered by all of the the
protocols that are shown in this list
and aside from that uh we introduced a
new um a new one which is the RN uh red
limiting one and we are going we are
going to to cover in a few
seconds okay uh regarding Discovery uh
we have three main uh Discovery
protocols one is uh peer exchange uh
this is uh pretty centralized and is not
ideal but is um is useful in in certain
conditions and what what it does sorry
what I'm explaining is not shown in in
the screen but uh what exchange protocol
does is it asks to other peer to share
the the peers that it knows and it's
just a request response uh protocol
where the the other peer responds about
the information of each peers and then
we have the DNS Discovery uh which is um
very interesting protocol that uh is
powered by DNS and then we have the
Discovery V5 which we consider uh to be
more uh decentralized and more uh
convenient for the web three um scenario
and it's um it's based uh its
implementation is based on cadmia and
well as you know it's uh DHT and uh what
it does it retrieves a random set of um
en enrs and um yeah this is um very
intensively used in in
waku okay then
regarding
um uh another family of protocols that
we have in waku is the request response
protocols uh which are um you will see
in in this talk that we have two main
families of of nodes we have what what
we call a full node um which is
basically a note that um is part of the
of the overlay of the of the network and
and produces the routing of the data and
then we have the The Edge nodes and for
this Edge nose uh such as um a mobile
phone or a browser is um it cannot
participate in the routing uh protocol
because it's um data consuming and for
that reason we we created this uh
request response uh protocols for for
helping in order to help these Edge
nodes in in different ways for example
in regarding sorry for the typo
regarding the store note its main
purpose is to um allow nodes uh to come
when a node come back to to participate
in the network to get back the the late
latest state of of the the
messages then we have the sync and the
main purpose of this protocol is to make
sure that all the store nodes have the
latest State and the same state of of
messages uh then we have a light push
the purpose of this protocol is for Edge
clients to to be able to participate in
the network to publish messages and
filter in the other way
around okay if we go further to
the routing
protocol
sorry anyway okay uh okay regarding the
routing protocol is um we we call it
relay and is uh kind of opinionated
version of of Gossip sub uh which is U
uh great and it's very interesting and
we're going to to cover very briefly how
gossip sa Works in in this talk
um okay uh okay this is uh uh very
simplified schema of
um U pretty interconnected Network and
the dots uh just represent nodes and as
you can see all of the nodes they are
continuously exchanging control messages
like for example uh the the messages
that I saw the messages I'm I'm
interested in and I the the control
messages um names are I I want or I I
need
no and and then we have the the W
messages that these are the the actual
messages that transport uh data in in
the in the in the network something
important to to bear in mind is that
um we can have for example 100
connections to to 100 nodes but one
single note will and spread um data Wu
messages to up to six eight notes
maximum and every note will pick up the
V from each neighbors will pick up the
best notes regarding the according to to
certain parameters
such as latency um number of messages
per per second uh how responsive a note
is and and so on
and okay uh and how does it work um
every note has uh appear um hard bit
that happens every second and on every
second every note measures or um that
gives um a certain score to to all of
its nebs and according to this score if
the score is too low then it ignores the
the the the note it doesn't mean it
completely disconnects to the note it
keeps um uh gossiping say asking what
messages do you have what what what I
have Etc but it doesn't participate or
interact share sharing um um important
data no and it only establishes a mesh
with um amplification factor of um of a
value between four or eight this is how
we we are configuring at at the moment
and and
yeah and in this slide um it's just um a
simple example of how a single not um
establishes
um at certain point in time uh what what
is the about his its nebor uh what is
the the P score and for for example if
not a receives a
message then uh given that the relay the
sorry the
overlay uh network is uh established
with b and d it will only H deploy or
sorry spread the the message to to b and
d and not not others and something
important to bear in mind is that this
can change every every second it's not a
fixed uh overlay network but it's
something that is
alive okay
and uh okay uh then we have the red
limit nullifier uh this is a very
interesting uh topic and very
interesting technology
because it it allows um to protect the
network against spam in a in a private
way so that
uh the note can prove that it belongs to
to the network without actually
disclosing uh its information or it's
very very cool how how it's um
implemented and it's based on cnar
technology and we keep a smart contract
currently in sepolia where the the
membership set is configured I think uh
we are about to release um version two
of
rln and uh and yeah it's um basically to
this is a quite complex um topic and
it's be beyond my knowledge but just to
to get an idea the main purpose of it is
to protect the network against spam in a
private
way uh okay
um regarding the the waku message the um
as you remember this is the the one that
is being uh sent across the the overlay
Network um basically it contains it
contains a bit more Fields than
uh shown in in the left but basically we
have a
payload uh which for which we don't
impose
any um additional encryption we leave
the encryption to the app um developers
and regarding encryption is important
something to to notice that uh there is
pointto point
encryption um inherited by the lip P2P
um which is made um following the noise
protocol and we have the the content
topic uh which is a field um useful from
the for example in the filter protocol
um anage note uh subscribes to a certain
content topic and from all the
information that is shared across the
network this uh the messages the The
Edge note is interested in is going to
be sent to to them
okay and regarding this
point okay so um to build on top of waku
uh I just going to introduce you a bit
to cdk that we have and languages we
support uh so this uh QR code leads you
to documentation website there is a lot
of information uh links to our
communities and such if you have any
questions about anything like vaku
related uh code is
failing uh behaves unexpectedly reach
out to us uh everything is there but we
do support JavaScript and typescript
right now and Nim is uh and second
language that U it's more of first
language but still uh it's the language
of our choice and we have an
implementation of waku in Nim language
and it's compilable to C and you have uh
the C artifact that you can consume
later on we're also working on uh better
go uh binding and cdk and uh rust and
python uh they work in progress but can
be used to some cases right now um so
for GS waku we have like a couple of
packages main one is waku SDK just uh
install it use it it's going to work I
hope so then uh we have a a wrapping for
react also uh deals with react life
cycle methods and stuff that busts a lot
of uh creates a lot of unexpected uh
Behavior uh then we have a create app
that can boost up your application quite
easily uh might be useful as well so the
main users right now are status status
is uh uh a messaging
application which is dedicated for one
to one chat as well as communities uh
and and uh uh it uses Vu underneath it
has its own uh set of nodes that are
operating uh there are a bit different
guarantees than uh defaults that we
provide propose uh projects to use uh
such as a bit extended uh store
retention right because such
applications W to retain uh data longer
then a second project that uses waku is
run this is privacy oriented defi
project and the vaku is used for
broadcasting fees in the network so that
it's uh um not known where it originates
from uh then the graph also uses vaku
for uh information exchange between some
of their notes um yeah so um and use
cases uh there can be anything such as
defi as I already mentioned Community
Run apps as well uh some social
interactions uh wallet to wallet
communication gaming you name it so uh
we saw interesting applications even
with uh ge location position such as uh
uh users GE location gets mapped to a
particular namespace in vaku network and
then you can talk to the room in which
you are located quite interesting
approach to create a layer on top of
reality um so today we're going to show
you some of the examples uh this link
will lead you to a repository with uh
our examples that where we experiment
where we play around and uh as well as
do something for users I will show you
um application named body book uh we
created it for as a PC just to show
people around here at
Devcon and uh uh there will be more
examples uh and we can try to do some
programming if you are interested
otherwise I will just walk you through
some simple onepage JavaScript
application with uh request response
protocols uh that are used uh do you
have any questions at this point maybe
we can do a quick Q&amp;A before we go into
some code presentation
oh yeah there is a question
sorry something specific for Native
mobile ATK so do we have a mobile C J or
cut or or Swift your plans I mean not
now we have it in plant yes uh
JavaScript version can be used in react
native we did some bindings um we didn't
prove it working reliably so this is
also work in progress we had some go uh
vaku being adopted for running is also
in react native or uh other stuff but uh
also status is using um vaku as well but
uh they did a little bit more work than
just you know installing it so it is
work in progress
yes so please is there a public network
uh that the the waku nodes run on or are
you expected to run your own nodes for
the applications that you run yeah so
the main difference between waku and
let's say lip2p as I mentioned lip2p is
a stack that we are using and anyone can
let's say me you we together want to
build a network we create an application
out of lip lipid right uh what waku does
differently is that it provides a set of
protocols like solutions to some
problems that we observe and we want
users to uh have dealt with as well as
we have a running Network which is
called the waku network tww and uh I
will show you how to join it let's say
from JavaScript cdk in a couple of lines
of code and you can hook in your own
nodes to it or use it as a signaling
note let's say to create your own sub
Network or something like that
anymore okay um so we going to go to my
laptop and uh let's see what we can do
with the code
today so so this one is uh for uh
example with rust it uses n version of a
um of of vaku uh some bindings and uh
you can scan it and see how it is
implemented later on Ian will go and
present himself the code and walk you
through it
um so uh body book uh if you scan uh
this will lead you to the source code of
the simple one page of application
otherwise you can visit body book.
fun
and uh what it does is that once you
open it you can create um a book and
then later on at the conference or
somewhere you can come to people and ask
them to sign uh your book like collect
signatures these signatures will be
created from a wallet right so let's say
a metamask wallet or something and the
interesting point about this application
is that the signatures will be exchanged
through waku and they won't be committed
to to the to the blockchain hence there
will be like an easy propagation of uh
this information and it will be stored
in the in the store protocols that Ivan
mentioned about so here we have like a
couple of U you know just Just Books
whatever and there are some signatures
attached um yeah so if you create it
it's going to appear here and uh yeah so
this is very simplistic application but
still uh very use case very interesting
use case
okay so uh then
uh uh you can run a note this is another
application uh example of how waku can
be used you can be uh just a node
operator so uh contributing to the
network let's say if you have a spare
Raspberry Pi for gigs of RAM or
something just uh opening uh a Docker
and doing one line can already
contribute to the network quite a bit uh
though I'm lying it's not on line it's
uh more of of one line to run in your um
terminal and uh now if you open this
link it will show you a basic JavaScript
application it will lead you to this to
the code which I will go and show now um
I hope you see it
well yeah is it readable should I
increase it a
bit okay A
bit um this is just
single one file application which
consumes JavaScript cdk and uh uh uh
you have to create an instance of a node
first right so hence uh this create
light node function is used uh it it
accepts like different parameters there
you can pass particular coordinates of
the network that you want to use if uh
not default network is in use so by
default Network I mean here
tww and if we want to use a default set
of configuration we just pass default
bootstrap other thing that uh vaku has
in it is um uh the message that the data
packet right it it gets propagated
through the network and there are some
properties uh of this uh data packet
that help uh to do routing and uh one of
them is content topic and uh content
topic should be perceived as the
namespace under which uh data should be
exchanged from the perspective of an
application so let's say if I mean an
application like uh telegram right uh a
Content topic can be uh one chat one
group in which the messages are getting
exchanged so hence uh I am as a user
have a set of chats and only from them I
want to receive messages if they are
coming from different chats but I don't
want to receive them that's the simple
idea here so uh and as anything uh uh in
the uh computer science we want to
create a reader and writer we have uh a
blop of uh bytes being exchanged in the
network and this two lines are doing
exactly this they create decoder and
encoder and they are configured to uh be
uh using one
particular uh content
topic later on we have to start the node
would like just to initiate the
processes part of API and the second
line does uh an important part is that
we block execution of application until
we receive some peers uh this is just uh
one way to do it uh another way might be
to uh not to do it and uh rely on you
know lazy uh connect connection that
will be managed by uh GS waku in that
case um so uh then here I I going to
show two protocols through uh two um
lightweight protocols that we have for
Edge nodes as I one mentioned one of
them is filter and another one is light
push they come complimentary and uh for
filter uh the main use case is that you
want to receive only those messages that
you are interested in without uh
consuming a lot of um bandwidths Etc uh
and the filter exactly does the same we
uh send a request to a service node and
we ask it to later return a messages to
us uh the whole uh uh interaction
happens over websockets as of now in
future we might go into uh having a web
transport which is work in progress
right now as well as web RTC might be in
use uh for some cases but regardless of
it we rely on the service node to return
us messages uh in that case um we can do
a lot of H ristics as I mentioned uh
peer-to-peer networks are not ideal uh
some of the this uh problematic parts
are uh having uh unreliable nodes one
Noe can pretend to be reliable by
advertising itself uh with some
protocols that we are interested in but
it might not do what we want what we do
in that case we Implement some
humanistics inside such as if I sent a
message and I didn't receive it back
from that note it's probably not
reliable are going to drop it so this is
a part of overall umbrella term
reliability which we were working for
the past six months
so um yeah this is a simple callback
from JavaScript perspective nothing
fancy as to pass uh data inside we just
uh oh yeah Waiter on white push so here
just one for Loop sending 10 messages
from from our site the send is exactly
sent it's just one request over existing
uh transport in our case again it's
websockets it just creates a blop of uh
of byes and and sense it yeah so let's
see inter
connection
uh okay so I'm going to open Local Host
I have it open and yeah there are two
tabs
uh here we want to re
connect here we want to reconnect as
well um to do we are waiting for pier no
Pier available something
happened good here we subscribed and
here we subscribed so now we are sending
some messages in the loop and we are
receiving some messages as we see uh one
of the properties of the network is that
um Haku functions is that we going going
and receive our own
messages uh and uh this can be quite
useful for some of the applications
um yeah so this does its thing so it
works uh one of the interesting things
is that um there are a lot of logs uh
error logs they expected as for they
cannot be uh ignored uh are there any
questions right now yeah
please
um light node instance can you repeat to
yes yeah the light node instance it's
not a P2P instance no actually it is so
uh but it depends right uh there are
some tradeoffs that we have to make in
the browser one of them is that uh set
of available transports uh for for the
browser tab right browser is very
restricted environment there are a lot
of things that we cannot do such as we
cannot re do atcp uh connection directly
or UDP connection directly we have to do
either HTTP or uh a websocket connection
that's it web rtcs but there are limits
right so um and also resources uh
browser is very limited in how much
computation we can do like heavy
computation right uh the browser tab can
become uh suspended uh quite easily by
operational system everything stops
working in there right uh and uh it
cannot be a fully functional uh part of
the network hence we call it an edge
node meaning that the traffic kind of
ends there right it does not participate
as a full node it's not full but
it is peerto peer in the meaning that
the the browser tab is independent in
how it discovers the network it uses uh
almost everything but uh discovery
withies that Ian mentioned um it
discovers the network through DNS and
peer exchange and as uh for our case
right now we have 24 peers so right now
we have 24 websocket connections to 24
full nodes that we can use
interchangeably or in rotation or if we
observe that some doesn't not work we
can use others and if others does not
work we can do something else and also
the per exchange is an abent pure
Discovery meaning that it happens always
in the background so and uh we can see
that we have quite a few nodes collected
right now right now 25 but the longer
the browser tab will be executing will
be open the more Piers we're going to uh
discover and use eventually so from that
regard it is peerto peer and it owns its
own stack as to like uh encryption uh
yeah so so this provides like a
websocket server so all these nodes
provide a separate websocket server for
these Edge nodes yeah exactly this is
very interesting because we can uh
reason about it as to having a server W
application we don't have kind of server
but we still can have a connection in
between them right it's back endless yes
and I mean one thing from the previous
uh uh slide I have was the the syncing
right so how how does the syncing works
because you said you only send messages
to like four or five uh peers at a time
so how does it know
me yeah so uh how does the node knows
where to send the messages yes was it
the question yes so um uh gosip up is
not Direct Ed way of routing the traffic
and we rely here on eventual consistency
let's name it like that
we we know that the node will relay
messages to its peers in our case it's
four 5 8 something like that right and
we know that uh all the peers kind of
connected to each other right we uh have
it as a a graph um so if someone
originates with a message on one end uh
by the rules of Gossip sub it's going to
propagate till the other end but it can
take a lot of time as well as little to
time right we don't know where the note
is placed in the network um and I don't
mean geographical position but like
logical from the theu standpoint um yeah
so in our simulations we had simulations
like up to 10,000 noes and we had the
numbers as to uh in average uh from 200
to 500 milliseconds was the message
propagation in current tww
uh which supports rlns for the meaning
to uh shield from the do we have like uh
propagates quite fast yeah and so if the
node is offline and comes in right does
it get the older messages that were
broadcast yeah uh so um this is why we
actually came up with store protocol
right in peer-to-peer networks we kind
of think about the transport right this
is uh these are they talk to each other
a store everything else it's like
application logic we agree with that
right at each application that uses
let's say vaku stack uh or the network
uh needs to implement its own like uh
stuff on top a store including but we
still understand there is a need to have
a short LIF uh like while I'm offline
let's say for 1 hour right I still want
to get back these messages so uh store
is for full nodes and it's it's uh going
uh once let's say your full node goes
offline uh and goes online back it's
just going to ask the Pierce around for
the missing messages through the store
protocol and it's going to do the
thing thank
you any more questions no um let's see
something with rust been done and uh if
you want we can do some programming or
something I think
okay thanks Sasha
um uh okay in this uh part of the
session we're going is it
visible we're going to to cover um the a
few examples uh regarding the uh wagas
bindings uh by the way accredits to to
Richard for the great job in this repo
and uh this is the uh in in there well
in um QR shared earlier on by by Sasha
uh you you will get
um uh a branch to do this uh where this
implemented and let me let's uh first of
all uh overview the the repo and what we
have in
there basically we have wuis bindings
and the examples and in guaguis uh this
is the the one that um implements the
nwagu
uh this is the the N
implementation and from from here we've
H created or we are working on the
creation of um C library
that exposes all the functionality that
that is available from from aaku node
the discovery the creation of a note
connection to another Pier um H punching
um yeah Etc all all the all the lip2p
protocols that we've uh mentioned uh
earlier on are covered by the N
implementation and in this C library
what we are doing is we are exposing
this uh features uh through ffi to any
any other languages uh at the moment uh
as Sasha mentioned we are covering uh
golang rust uh python uh
C++ and no
GS and okay let's go let's carry on in
this particular case um uh then we have
the Wu bindings crate and what it does
is um uh Li gr uh which is just um a
grab a wber around the
woses and in there we have the the
implementation of the of the bindings
stuff and all the the complexity is uh
tackled within this this
module
yeah you will see that uh we we apply a
technique called
trampoline and that helps us to uh to
interact with with
rust sorry with the lip guu library from
from
rust and then we have the in in this
particular case we have a few
consumers and this is
the just a simple
application um well it it uses Tokyo as
a sync um framework and what what it
does it basically at first it creates a
a waku note with uh certain
parameters then it establishes the DNS
Discovery um URL uh this is for
retrieving the B strap nodes in order
for the node to start participating in
in the network it needs um an initial
help and for that reason we we have this
um and from there many other nodes can
be
infer and then we start the this
Discovery V5 uh protocol which is in
charge of um uh discovering other nodes
in um in a decentralized
way okay this is part of the just of the
example of of this
application um
uh maybe the the example is not super
idiomatic in terms of rust at the moment
but it's just uh a proof of concept uh
to to see how a Wu note can be
integrated in in
Rust and in this particular case the
main purpose of the application or what
the the Wu note is used in this case is
just for for sharing the the game State
across
users across the the players
and okay and given that we have uh a
user interface and and something
important to to bear in mind is that the
the incoming messages by the note these
messages are being handled by by the LI
Li wacu which is implemented in Nim and
something important to mention is that
this um
guacu note is running in a separate uh
thread and we need to and the Le guacu
establishes a
communication uh with this threat this
this is needed because the name run time
uh should run separately from any other
run time such as the the rust golang uh
NOS Etc uh in order to uh to to make it
work properly
uh because um as we are using nowadays
Nim we are using it with a garbage
collector and it's need it needs to to
run on its own
thread and something I wanted to
mention is that um all the incoming
messages sorry
for they come in in this
closure in here um as we as the example
is implemented now it starts the waku
node and then we
pass uh we subscribe the node to a
certain topic just the game topic and it
we pass uh a closure which is in charge
of um getting the incoming
messages and with this uh what we are
doing is we are um notifying the the
main threat about the incoming message
so that the game State can be
um updated when when you and now let
let's do a a quick a small
demo uh in this uh in this case uh just
we have two inst instances of the TIC
Taco
application uh on the left um each of
them is running a a waku note
then we say this is going to play as X
and this is going to play as
O
then they
can they can play and well it's a very
simple example in this case player X1
one and okay uh something else I wanted
to to share is in
this in this presentation
sorry feel free to to clone this
example uh because we are going to to
play a little bit with
it is just um you will find it in the in
the same Wu Ras bindings uh repo
and it's it's a bit uh more simpler and
what it
does it uh creates um it's more or less
the same but um more
simplified it creates a w um waku
note we are passing uh
sharts uh this is uh the the chart thing
is uh something that is uh needed to
split traffic in in a certain way
um it's um it can
be understood as a way of um channels or
communication channels in in Gossip
app uh then we are establishing um
maximum of 1
Megabyte uh L level
uh content topics uh sorry no uh this is
the P subtopic we set the keep alive to
true and as we show uh saw earlier on WE
enabled the DNS Discovery and dis
B5 okay and in this case uh after that
after grading the note uh we just
started and then we establish uh we
subscribe to to the waku to the to the
topic and that's it and in this example
it just uh creates a note starts it
subscrib to the topic and just wait um
until a control C is pressed and if we
if we run it we will see
that uh yeah these logs are coming from
the implementation of nim
guo
yeah okay and as you can see the note is
starting to receive um relay messages
because it's subscribed
to and yeah and that's it and we are
receiving messages from from the
um they I believe they come from estatos
because I I connected to to the estos um
Network and well um
just uh that's that's it I don't know if
there there there are questions or
comments or would you like to to see
something else or
how how is the DHD look for the
network like what flavor of DHD how is
the the DHD lookup um being done or you
mean um yeah we have a discovery with
five client and it it performs um a a
request to to the
is but so
what like how does it decide where to
Route the message just on the peer
scoring or what uh um you mean the yeah
yeah exactly
the the the messages are being routed by
a healthy
mesh if
the um if there are uh peers that are
misbehaving or are are spamming the the
network then they they are blocked and
they don't participate in the in the
network okay um in that case uh if no
more question think ah yes
uh uh yeah thank thank you for the
question uh good question indeed um the
as Sasha mentioned um the gossip sa
itself it doesn't guarantee the um a
certain message to to reach uh a certain
point and for that reason we are working
on uh on implementing uh what we call
reliability protocols and uh somehow we
had um an additional layer of
redundancy um and one there is
um sorry I forgot the precise name but
one uh previous um uh implementation of
or one enhancement is to um um consider
that one message is has been received
properly if it has been received uh by a
store node so we uh somehow we use the
the store node as a leverage to to
reinforce the the transmission of of a
of a message but but yeah indeed this
this is a um a very big problem that
that we need to um
overcome
and uh yeah we we are working on on it
and thank you thank
you um any other question
um okay in that case thank you so much
for the time
and and see you see you around
pap
next
sh
see
no e
B
m m
ch
on
yeah for
t o
w e
in e
all for
h e
here m
