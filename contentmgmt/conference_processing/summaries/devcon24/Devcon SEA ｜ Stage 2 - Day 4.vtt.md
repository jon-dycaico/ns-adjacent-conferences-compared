[Music]
the
o oh
for
for e
e
h
yeah we'll be beginning in 5 minutes at
looking forward to getting started with
the day
GM
GM really glad to see so many faces on
the last day of Devcon uh this is the
meev stage we'll be having a lot of
research around crypto economics uh over
here um the format is going to be two
quick talks of 5 minutes and then
there'll be long talks for the rest of
the day um our first Speaker who I'm
very thrilled to introduce is Pascal
stia who's worked on uh single slot
finality for me and he works on Research
at a very high level so it's a good
start to the day to just have a quick uh
to have his talk on uh on on the
research that he's presenting um for
questions we have mircat so you have to
scan the QR code I'm sure all of you are
familiar with it already ready um and
once you scan the QR code you'll be able
to um ask questions and it's much more
efficient way of doing it um so yeah
with that Pascal you can kill it now
take the
floor thank
you hi everyone great to see that
already Friday morning quite a few
people make it to the me stage seems
like there are quite some me Ultras um
looking forward to it um I'll be doing
quick intro on multiblock me just quick
lightning talk um to Dive Right In quick
um recap what is multiblock M actually
multiblock m means uh one block Builder
has multiple slots in a row and can
extract more M um by having the slots in
the sequence then by yeah having
individual slots this arises due to the
fact that me a Cru um exponentially um
if we look at the data we can see that
over time it slightly exponentially
crows um for example one strategy could
be to manipulate prices a block Builder
can for example buy certain token in
slot one then only include buy
transactions on the one side and not
include the sell transactions and then
in his last slot captured me of selling
the token first um this is one potential
strategy of manip manipulating the price
there other ways to do it uh we can do
liquidation attacks of also um forcing
the price to go below a certain
threshold and thereby liquidating assets
and capturing the liquidation gains um
so I won't go too deep into it but there
um yeah a whole set of strategies um
what did we do we looked at data since
the merge um 4.3 million data points of
MEF Boost payments um and did on the
other side a monal simulation of daily
market shares of Builders to see what
would be like a statistically um yeah
normal distribution of multi slots um to
have a Baseline and yeah based on this
what we saw is interestingly we have
less multi-lot sequences than expected
um we see especially on the chart on the
right we see the blue blue bars being
the Ed distribution of multi slots um we
see less of them um also yeah
interestingly what we saw however
longest sequence was 25 slots in a row
by the same Builder Beaver build and for
the same validator and same Builder it
was 11 slots in a row March of this year
so what we see just by yeah statistic
there are long sequences which would
allow for multislot M strategies um so
in the next step what we looked at was
the payments the MEF Boost payments for
longer sequences so this is basically
for sequence of length five for example
what was the average payment uh what we
see interestingly it increases for
longer sequences so it seems to be there
is a value in longer
sequences um however why this is the
case so far we can only speculate one
hypothesis could be that MF boost at
it's a continuous first price auction so
it basically from an economics
perspective works like a second price
auction from the value where we end and
so it could be actually driven not by
the highest bidder but by the second
highest bidder who has an increasing
value for the blocks based on private
autoflow me captured in private autoflow
um so it could be the case that actually
the intrinsic value of the second um
highest bidder increases and that drives
uh yeah this increasing values um so
what we also did is looked for the
payments per slot so in longer sequences
what was the bit for um yeah the slot at
a specific uh Point um there we saw so
far there is an increase but only a very
very slight increase so this uh yeah led
us to the conclusion that so far we
don't see dedicated multi-lot strategies
um we also looked at the top 10 Builders
to see if there's a certain pattern for
the top 10 Builders if there's there are
builders that are deviating from the
mean uh we didn't see any yeah very um
yeah outstanding data the case a few
builders that have more slots more multi
slot sequences or that are particularly
strongly correlating with um the same
validators um however from our
perspective that's probably based on
things like latency and collocation and
not based on other types of uh yeah
strategies that are run um last thing
that we looked at was autocorrelation of
MEF Boost payments to see if we can use
historical MEF Boost payments to predict
future ones um there what we see is
based on different correlation uh
metrics um that it strongly goes down
after the second or third slot so it
means there's a very very low yeah
autocorrelation so a low predictability
um so we don't have times of high or low
me but there's a fast reversion to the
mean
overall um yes there was the quick run
through um if the topic in general is
interesting there's a post on E research
I'm going into the details also a link
to the to the Jupiter notebook with all
the data and I'm also doing a workshop
today in the afternoon on execution
tickets agent-based simulation of
execution tickets so whoever is
interested feel free to join otherwise
happy to take on questions I think I
have around one and a half minutes or
one minute left for questions feel free
to scan the QR code or ask them
[Applause]
directly so we already have two
questions we want more you can just scan
the QR code and put it and one quick
question Pascal like where is your talk
so that the audience is aware of the
room that the talk is in uh the talk is
in classroom B so just down a yeah so
I'll read out the question for those who
are joining virtually um have you
studied arbitri time boost do you think
Dow should be capturing meev
Revenue um to be honest I haven't looked
deeply into arbitrum time boost I think
there are people in the audience that
have much more knowledge of this so um I
can't really give there an in depth take
um unlike proposer Builder is not
guaranteed to win PBS auction multiple
times in a row would you advocate for a
random proposal allocation which does
not allow the same proposer in a row in
general I think it makes sense um
however I think there is um so I mean
that's a bit of a um Outlook already on
the simulation what we saw is that the
secondary Market um usually reduces
decentralization um which means there
should be some component of Justus in
time auction um however I think with the
current boost setup what we have is the
problem of inflight variation um so I
think a combination of both could be
interesting um but I think some
component of randomization does make
sense to prevent multislot M
strategies thank you so much that was a
great talk and a good start to the day
uh to meev day I like the name that you
gave this is me room you know yeah thank
you
put
um so we have our next talk coming up
really quick with Felix lold um the talk
is on uh do we really even need PBS and
how we can solve uh meev at the app
versus infrastructure layer uh this is
going to be a full day of uh hardcore
research so really glad to see all of
you here and engaging and asking
questions uh make sure to scan the QR
code if you have any questions for our
speaker and with no further Ado let's
welcome Felix on
stage hi I will have to speedrun this
talk so if you want a more relaxed
version of it you can scan the QR code
or go to Tiny url.com
stepcon uh where I gave this talk in a
version Let start with the problem that
I have with proposer Builder separation
why I think it's not a good idea there
are three main arguments in my point of
view first the trust and centralization
um problems that it brings onto the
ethereum base layer for all types of
transactions not even the ones that
actually contain me ethereum today is
proud to have more than one million
validators um proposing and validating
the chain and you know we are one of the
most decentralized chains or the most
decentralized chains in the world but at
the end of the day today if you look at
it there's only two very well-known
entities beaver and Titan that propose
more than 90% of the blocks contents and
how valuable is it really to have a vast
validator Network when the most
important part the content of the block
is decided by two entities moreover PBS
adds this trusted component to the
supply chain the Mev relay that Builders
have to put their faith in and even if
we trust the research that's ongoing
that's trying to propose ways to
enshrine the Mev relay into the base
layer and get rid of that trusted
component I think there is a couple of
issues with that first it adds
complexity to the core protocol one
thing that we're trying to avoid and
second of all it's not even clear that
if implemented it will find adoption
because meev is a very latency intense
game and any decentralized peer-to-peer
gossip based solution is always going to
have latency disadvantages and also
feature disparity um Builders today want
to have bid cancellation as an example
they want to make a bid and then cancel
it if they if they change their mind and
such a feature is simply not possible in
an enshrined PBS version because once
you gossip the message you cannot take
it back and let's not forget that PBS
actually maximizes the harm that is
inflicted on users in order to win the
PBS auction you have to create the block
that is extracting the most values value
via sandwiching or other types of Mev
attack and thus we've created a system
that really favors the worst possible
outcome for the user okay enough of a
rant what do we do about it first let's
maybe St take a step back and try to
find out why does meev exist in the
first place and here really the
fundamental reason is that in today's
system every token trades at many
different prices within the same block
here I brought you an example block from
a couple of days ago in which ethusd
trades at least seven different times
with seven different prices and so
you'll see sexex arbitragers that are
able to access for instance the unisa
pool at the previous Block's outdated
price and then the rest of the block
will trade at the new kind of fair
equilibrium price you will see
Liquidators that are able to get um bad
collateral at a fixed liquidation
penalty 15 20% below fair market Price
and the rest of the block trading at a
different price and last but not least
you have sandwiches that front runner
user to buy a token at Price a the user
then prize it at Price B and the sand
wicher sells it at Price C all of these
strategies have one thing in common the
same asset trades in the same block at
different
prices and the reason for this is that
we basically took our well very well
best known standard first come first
served mechanisms that work in
traditional continuous time markets and
deployed them on blockchain and this was
the key mistake ethereum doesn't have
continuous time there's only new
information being released every 12
seconds and then it's released in one go
and The Ordering of the information
within the block is up to a unilateral
party the proposer to decide how to
order things there and so it's unsafe to
deploy any kind of mechanism that works
on continuous time on on a discrete time
blockchain so what what's next what what
how can we do to fix this well as you
might guess we need to come to a point
where trading the same asset in the same
block should lead to the same execution
regardless of trade ordering or put
differently we need to get to one price
per token per block this design requires
to be able to batch trades together so
it doesn't work on Raw ethereum
transactions instead we need trade
intents or just signed limit orders and
batch those together in a
multi-dimensional auction which can
later be cleared at a single price for
details on how this looks I encourage
you to look at cow protocol the trading
mechanism that powers cow swap which
pioneered and implements this mechanism
it's processing many billions of dollars
in transaction volume every month and is
basically proof that this mechanism can
work on
chain cow protocol provides me
protection for all the cases that I
mentioned on two slides ago um we
protect swappers by having buyers and
sellers um that trade the same asset
receive the same price regardless of
their ordering and we can even match
them together in what is known as
Coincidence of Once by making amm part
of the batch and treating them like
swappers LPS no longer trade at outdated
prices but instead get the fair new
equilibrium clearing price and
liquidations are just stop loss orders
which you can also add to the total um
liquidity pool and make sure that
collateral recovery happens at the most
efficient and fair price I want to leave
you with this number which is a dune
query that you can check for yourself
that shows that more than 97% of me
today is trading related and that is
sandwiches sex sex Arbitrage back
running liquidations and those can be
vastly reduced if not completely
eliminated at the application layer by
not using pseudo continuous time
mechanisms so I'd like you to join me on
my mission to convince this space that
we should fix the mechanism rather than
making the chain more complex and with
that thank you very much
thanks for that great talk um if any of
you have questions you need to scan the
QR code and uh ask the questions
remotely uh I'm going to read out the
question for those joining virtually do
you have an estimation of reduction in
me if only Dex used is cow yeah so right
now cow swap focuses on Swap me
protection um I didn't break the number
liquidations um so right now it would
probably be you know less than 97% but
the mechanism itself not the product as
it exists today but the mechanism itself
would be able to reduce Me by that
number that I that I
showed um the second the other question
is do you think PBS causes Cent
calization or is it correlation I think
PBS causes centralization um mainly
because it's a winner takes all latency
game um I wouldn't say it's correlation
there's also a reason I couldn't get to
that slide because I didn't have enough
time for why I think cow protocol or an
application specific um auction is not
going to cause the same centralization
or even if it would not affect kind of
all types of transactions so if I want
to make a transfer I'm not kind of
subject to the censoring that happens
today in the in the Builder Market um
but yeah for this I would refer to the
longer talk yeah um how would you
compare cow with what sella is doing to
fix meev on the application layer via
Unis swap hooks yeah I would I mean cow
is working and out there and live um I
think the mechanism is relatively
similar um and uh yeah I think that's
the the just you can deal with the last
question how does cow deal with
multiblock meev um it it doesn't uh
because basically the batch itself has
its own um has its own kind of heartbeat
its own time and so if you were to try
to do multi batch me I think you're
running the risk that the whoever solver
will win the batch is going to um
execute the trade before you so it's
there's no real incentive for you to to
to censor or try to delay execution to
another
batch thank you so much thank you very
much
so great to see the energy there were
more questions than the speaker had time
to get through so really engaging like
all of you are really engaged and uh and
taking part in this uh we're going to
take a break of 10 minutes so if any of
you need to take some coffee and become
alert and uh or have like um uh kind of
go to the restroom or anything this is
your time uh and let's be back in 10
minutes and continue with the energy
that
I
GM GM I hope you got some ability to
just stretch yourself out and uh it's a
long day this is the meev room it's a
series of me talks here um next up is
actually a highly speculative talk which
is the tension between me and censorship
resistant gadgets uh it's by Julian Ma
at the robust incentives group so come
on up
hello everyone today I'll be presenting
the tension between me and sensitive
resistance so as was mentioned it's
slightly speculative more speculative
than I'm used to this is an idea that
we've been trying to formalize a little
uh but it's turned out to be quite
difficult so let me take you through an
introduction and see uh what your TOS
are at the end so for this um session
I'd like to frame meev as an aligning
values problem m is the maximum value
that some extractor can extract from
building the block uh and this is some
private benefits for this uh actor and
the etherum protocol has some other um
benefit function which we call the
Social benefit and in principle the Ean
protocol aims to maximize this social
benefits but it's very unaware of
anything that happens outside of it so
it doesn't know the external state of
the world and it fully relies upon this
actor the extractor is an agent uh of
protocol sensorship resistance is one of
the core values of the social benefit
that that ethereum has you can see as
either an a means to an end so maybe you
want to have sens resistance to obtain
some other properties uh for example
being able to have applications that
rely on this sensorship resistance
within real time or you could see it as
the end goal so have sensorship
resistance for the sake of sensorship
resistance whatever way you see it the
ecosystem needs to align the private
benefits which is the me that the
extractor can extract with the social
benefits which is what we as an ethereum
ecosystem want the ethereum pr tool to
do
so here are some observations on
censorship uh without any normative
statements I'd say um so there are three
sorts of sensorship that we see uh
happening possibly is economic
sensorship so maybe s some attractor
wants to sensor a transaction because it
can get more value uh by by doing so uh
an example is multi M that we've seen
earlier today uh or the leading example
that I wanted to use here is if someone
has some loan for example on a and it's
um it's it might get liquidated soon
they want to send a transaction in order
to heal their loan uh but the extractor
sensors this transaction because it
wants the loan to go bad in order so
that it can extract some me from it then
there's accidental censorship and this
may seem very weird how is the
transaction ever accidentally sensored
but it turns out that this is actually
something that we observe uh right now
so there are many many messages floating
around in a mempool and sometimes
Builders just simply Miss transactions
for whatever reason that is uh and if we
take it to the limit uh builders in
principle want to keep their block as
lightweight as possible so any
transaction takes up bandwidth and
especially some transactions that are
very um very heavy for example blobes
take up but also of bandwidth if you
take up more bandwidth it means that
your your blood takes more time to send
to the other uh to the other nodes
meaning that you have to send it earlier
meaning that you can't delay your block
submission as well as you could if you
were to play optimal timing games so
potentially a builder is is sensoring
transactions because it thinks that it
may get more value if it doesn't include
this transaction but but includes a
transaction in the future and this is
timing games taking it to the limit uh a
builder may actually miss its slot uh
which means that no transactions in the
slots end up on chain and this is
obviously censorship and then there's
regulatory censorship which is what most
people are probably familiar with is
there's some government that says these
sorts of transactions cannot be included
by this actor and where the actor is the
extractor who's an agent of thean pro
schol but apparently also has other
constraints uh enforced upon
it so uh um given that we observe these
sorts of censorship or at least that we
know that these thetically exist the
conclusion should be that the values are
currently not aligned aligning private
and social uh values is something that
economists have do been doing for ages
uh so there's a lot that we know about
this but within ethereum we are
relatively constrained in what we can do
for example giving um rewards for it is
difficult because it means that we have
to issue tokens and if you issue tokens
it means that possibly there is some
delusion uh that could benefit from this
so the way that we've been doing it is
analogous to regulation kind of uh and
this is our value aligning design
philosophy we do so by creating rules
that constrain how the actor can act
within a a certain
slot so for the for the framing of this
talk we'll use the state transition
function as how NV is attracted so gamma
is a state transition function it's
publicly known the extractor candel
alterat um and what it says is which
transaction sorry which state transition
are valid and which chals so for example
you can't put an invalid transaction in
a state transition function and obtain a
valid State transition s here is the
state of the previous block which is
also publicly known and T is an ordered
list of transactions that the extractor
inserts into the state transition
function to obtain some S Prime which is
the new state the extractor in principle
has full control over this T and this is
the key part where we'll try to align
values by getting more information about
T and then making some opinionate it
choice on what T should
be so if we map uh the states that that
you could enter into uh which is very
high dimensional it contains all of the
account and all of the balances into a
two-dimensional plane with just private
benefits and social benefits you may see
that SAR which would be the optimal
solution that some extractor uh employs
uh should rank very high on private
benefits this is clear because um this
is the objective function of the
extractor there's no objective to
maximize social benefits in principle
but perhaps there is some social benefit
here it's relatively low but it could be
higher uh the the values don't
necessarily have to be
underlined the key problem here though
is that ethereum doesn't know what the
social benefit is and what Which social
benefits are possible this is because
ethereum has no knowledge about the
external state of the world except for
the T that was inputed by this extractor
and since this extractor doesn't have
the same values um it can't really know
what the social benefits are so on a
high level the idea of the current ways
to to increase cens resistance is by
first of all making this more legible so
you could think of for example having
multiple inputs into t uh and not
necessarily acting upon it uh just
making it more legible in the first
place so the red part here is some St
transitions that are very undesirable
from the social benefit uh point of view
the orange part is maybe more desirable
the green part is good and the dark
green part is where the ethereum views
as the
best and this slide is supposed to show
that uh making things legible doesn't
always mean that it's perfect you can
see that the dark green parts for
example has the same social benefit as
some parts above and under it uh yet
ethereum the protocol might think that
these are better uh purely because it's
constrained in the knowledge that it has
about the external
world one way that we then want to try
to align these values is by imposing
some constraints so you could think as
ethereum saying okay we've seen now some
of these um these possible states of the
world uh and we for sure do not want you
to go into this red and this Orange area
and maybe we we're not so careful and we
cut off some of the green area as well
it's very hard to make constraints that
are uh binding at the exact points that
we want uh and achieve the right goals
and you can see as well that in this in
this very stylized example I must say
there's a straight line it's difficult
to make uh constraints that are more
bounded around for example circles or um
that have more nuances uh because
etherum has to remain very neutral so um
it it cannot it can only cut off um
parts of the possible states that are
obviously bad and cutting parts of the
state that are potentially good in some
future would be uh bad for
neutrality so now I'll go through some
case studies the first one is inclusion
lists we have an Erp out for fle which
is Erp 7805 which is our inclusionist
design the high uh the high level design
philosophy behind inclusion list is that
we allow uh the most decentralized sets
of participants that have some input
into centralized blood Construction uh
and the idea is that the inclusionist
shouldn't be able to attract any any me
so uh we do this because it kind of
aligns the private uh benefits and the
social benefits of the inclusionist
Creator and of the etherian protocol if
the inclusionist Creator were able to
extract me then it would probably do so
and we observe that meev leads to some
centralization uh and makes it difficult
to ensure that we don't have these sorts
of economic accidental or regulatory
censorship so the goal of inclusion list
is to increase the chain neutrality and
we do this by having some list of
transaction that constrains how the
execution payload is
created and this gets us at the notion
of unability which is one of the main
points of the talk unability is um is
something that we're trying to explore
more uh and it informal definition would
be that the inclusion list creates more
value for the inclusionist Creator if
used as intended it's very related to
incen of compatibility but incen of
compatibility assumes that you know
exactly what point you want to go
through and ether protocol again has
very limited knowledge of the world and
it wants to be very neutral so it may it
may prefer to be neutral over getting
perfect in sense of compatibility it
just doesn't want some very obviously
dominated things to happen for example
using the inclusion list for meev
extraction and maybe less obviously so
using it for prec confirmations which is
that the inclusionist Creator tells
someone okay if you're in my
inclusionist you're guaranteed to be in
the block uh and you should pay me some
fee for this we don't want this to
happen because we believe that if these
sorts of markets pop up then we might go
into a similar set setting as the MF
boost like markets that we see for Block
production uh which would lead to
centralization and defeat the goals of
censorship resistance so the idea is
that inclusion list must be minimally
invasive such that the intended
constraints are achieved uh otherwise
the private benefits of inclusion list
May uh differ from the social benefits
and if the private benefits of different
inclusionist creators differ a lot uh
then it will lead to centralization with
the Meb like
markets and a nice example here in my
mind is unconditional versus conditional
inclusionist unconditional inclusion
list states that if uh all transactions
from the inclusion list must be included
in the block regardless of whether the
block is full and conditional inclusion
list states that all transactions must
be included unless the block is full you
may intuitively think that unconditional
inclusion list gives you better
inclusion guarantees because any trans
transaction in the inclusion list must
be included within the block but
actually unability gets at an earlier
notion of what goes into the inclusion
list so if you make inclusion list
unconditional meaning that they have
better inclusion guarantees and for
example uh to take the most achieving
example you could say that this
inclusion list must be included at the
top of the next block because these
transactions were seen earlier perhaps
this is some notion of fairness whatever
way um you could make this argument that
inclusionist transactions should be
included at the top of the block and
this would mean that creating the
inclusion is now becomes very valuable
and now there will be a market for
outsourcing this uh inclusionist
creation which perhaps going to exactly
the same person as the one that
constructed the block and so we EXP
ially want to prevent this uh by making
the inclusion is conditional so I I
would say that the constraint is maybe
more relaxed within conditional but the
way that the constraint is created uh is
is is more likely to gain what we
intended as a protocol to
achieve does that Mak sense and then the
second case study would be most spur
block producers which is a whole topic
these days uh the basic idea is that
there are multiple block producers
producing subblocks simultaneously
instead of inclusion list where the
inclusion list is created sometime
before and I would actually argue that
this sometime before is a is a feature
and not a bud because precisely uh the
arguments that I'll show here is that uh
multiple tutor block producers relies
upon some sophisticated parties whereas
inclusionist does not Foster the same
environment so the goal of multiple
concurrent block producers would be to
prevent economic censorship the idea is
that if we prevent uh transactions that
are sensored for some adverse selection
reason so transactions uh that need to
be very timely uh where there's for
example like high frequency trading uh
types of ideas then we can achieve a new
set of applications that we haven't been
able to realize today an example of M
mulp Block producers is mackenstein
which is the proposal from barnab and
Mike which means that one person creates
a top of block and the other person
creates the rest of block and another
example is braid which is proposed by
matnik andco uh which is a deterministic
merger of K chains uh where each payload
is merged deterministically according to
some predefined ordering
rule how this scores on the unability
table is is very speculative I say
because we don't know that much about
multiple blood producers yet but to me
it sounds clear that mcbp since it's
specifically there for the gain in
censal resistance for transactions that
are very meev sensitive so these are the
high frequency trading transactions that
may suffer adverse selection if they
were put into the inclusion list where
it takes a little bit of time for them
to get included it would allow any blood
produc to extract me equally well this
is basically one of the designed goals
of multiple block producers this means
that these partial blocks are a vehicle
for M and you can't expect uh a large uh
unsophisticated and geographically
decentralized set of participants to
have competitive private valuations for
these property rights of making these
partial blocks that carry meev similar
to how we see now in Mev boost that
there are only two Builders who are very
good at this there are returns to skill
of being um a blood producer in mcbp
which means that my marginal benefits of
gaining an extra seat in these K consec
in these K parallel change increases
with the amount of seats that I already
have and there returns to sophistication
so it's not easy to build these Bloods
even when blood building is constrained
it doesn't mean that blood building
simple there definitely still returns to
sophistication and there are barriers to
entry which we now currently know mainly
in the form of private order
flow so that's why uh most pooran block
producers in my mind depends on a tested
propos separation and multiple blood
producers is very crowd so you can't
expect uh decentralized sets of
participants who are unsophisticated and
willing to uh willing enable I guess to
contribute to Central resistance to
build partial blocks so we need to
ensure that its creators are not also
the testers because that would then
centralize the tester set if you put
some centralizing force on a
decentralized set of
participants um then the decentralized
set of participants will become
centralized and it's not that magically
the centralized uh property becomes uh
gets some decentralization properties so
that's why a tested proposer unlocked
some new block construction pipelines
that are currently not possible you
could for example allocate the attesting
rights to a set of ATT testers uh and
allocate building rights to a set of
Builders
separately so what are some of the
consequences of this unability notion
well this is I think uh a very fun part
to explor and one thing that I've been
thinking about a bit is applications
consuming consensus information so now
assume that we have this uncodable
inclusion list meaning that it's very
unlikely that it will contain uh me
transactions since it's specifically
designed to not be a vehicle over me
it's very unlikely to include Arbitrage
transactions therefore so an application
who may see this may treat transactions
that came via the inclusion list
differently from transactions that came
in via the main block it may do so
because it's it's more confident that
transactions from the inclusion lists
are uninformed and won't uh take their
liquidity in general if if you're
designning a trading mechanism it's
important to distinguish between those
who are very well informed arbitr and
those who are not because trading
between two parties is is in general
Zero Sum especially if it's Arbitrage so
if an arbitrager is making money it's at
the cost of some other person in the
static World
Vision so what what you could possibly
do is you could use an asymmetric speed
bump which is something that's been
developed within traditional Finance uh
and what it does is it speed bumps
certain transactions and it doesn't
speed bump others um so the inclusionist
a natural speed bump and again I think
this is a feature not a bud so what you
may say is the inclusionist transactions
they are able to take liquidity whereas
the transactions From the Block they're
able to provide liquidity taking
liquidity is the Arbitrage path where um
providing liquidity is is not the
Arbitrage path unless you look at for
example just in time liquidity uh but
you could set up the training rules so
that you uh aim specifically for this
meaning that liquidity providers would
face less um adverse selection meaning
that there would be more liquidity lower
trading cost for
users seemingly though it seems to be a
bit of a paradox it's um if the exchange
believes that the inclusion list is
uncodable then it's suddenly very
valuable to make the inclusion list
because now your transactions are
treated differently uh so then maybe
inclusionist becomes Crow again but then
if the inclusionist is Crow The Exchange
thinks okay well this is not so valuable
anymore I won't act upon it so it seems
to be kind of like the the Spider-Man
meme you know where you're pointing
towards each other and expecting the
other person um to do something
something or to remain static I would
say though that this is not a paradox uh
because the application uh plays a
sequential game and also simultaneous
game the application must commit without
regret uh to its strategy of um of
handling transactions you can't imagine
an exchange saying okay if you send me
your transaction I have no clue what
I'll do with it maybe I'll do this maybe
I'll do that you need some commitments
of how the exchange rules are set up and
so the The Exchange will only commit to
uh using such an asymmetric speed bump
if it believes that the inclusionist
would still be uncodable after its
commitment so it must commit without
regret so there shouldn't be a paradox
even when applications specifically use
uncodable inclusion lists we can still
have uncodable inclusion
lists so some of the um statements that
I'd like to leave off with is that if
cenal resistance gadgets are incredible
then its creators can be decentralized
so if there is no other um use case
that's better than uh using um the Cent
resistant Gadget specifically what what
it's designed then you may ask some of
the decentralized participants to create
this because it won't centralize the set
further if the cens resistance Gadget is
cable then it's creators will be
centralized this is not a centralization
is not a feature of Market mechanism
although Market mechanisms can change it
a little it's mostly a feature of the
intrinsic property rights it doesn't
matter how you allocate for example
building rights uh especially within the
ether protocol because there can be
secondary markets um it's the fact that
building rights are inherently
sophisticated and there are inherently
barriers to entry so it's not about
proposer Builder separation it's about
the building
rights and finally uncodable censorship
resistance gadgets seem stable uh so
potentially there's a whole new set of
applications that we can unlock if
applications can consume consensus layer
information so that was it uh I hope you
enjoyed and it's part some conversation
uh and I'd be happy to take any
questions
so does inclusion list with an
inclusionist committee members making
economic sship end times more expensive
uh this is a property that's not
currently in fossil fossil relies on
boosting the signal of solo stakers
fossils are uh Erp so we made this
decision because um putting this uh
property that you get an inclusionist
committee makes it nend times more
expensive um as protocol complexity we
don't think it's warranted at this point
because we see a revealed preference of
people willing and able to make uh to
even take an economic penalty to provide
sensitive resistance getting this
property though is an easy extension to
Fossil um so if it's necessary we could
implement it
easily um yeah just scan the QR code for
anyone who wants to ask any questions
and it'll show up uh yeah we have a
second question uh which I'm going to
read out for the audience joining online
how do you achieve unability of iil is
that a property enforced by the spec or
achieved through the selection of Il
creators how to select who creates the
ilel yeah so uh the design philosophy
behind inclusion list is that you select
the most decentralized sets of
participants to have input into
centralized block construction so
unability is not achieved by the
selection um because um this is again
it's it's achieved not by the market
mechanism but it's achieved by the
inherent property rights of creating
this inclusion list and so what we do is
we make the minimally invasive uh way
that the inclusion list could be
structured in order to still attain the
centri resistance properties that we're
looking at so specifically in our Erp uh
there are three seconds between that the
inclusion list last can be committed to
and um the block produced so it's
difficult to include any transactions
like Arbitrage uh because these would be
relevant within the the 3 seconds you
may face adverse selection if you were
to do so secondly there are multiple
inclusionist proposers so there's not
one inclusionist proposer who has
unilateral power over inclusion or or
exclusion which is the general
definition of me there's no private
order flow possible because
inclusionists are broadcasted publicly
uh and they are only enforced if they
are broadcasted publicly um so you can't
get any private transactions into the
block and most importantly inclusionists
don't have any ordering rights so incl
inclusion list is just a set of
transactions inclusion sets I guess uh
and it doesn't say anything about the
ordering within the block meaning that
uh there there is there's no meev to be
extracted it's the minimally invasive
inclusion is
possible um the next question is do you
think that if we don't uh incentive ILS
with some part of the fees it might lead
to a scenario where everyone creates
empty ILS so um I don't think this is
likely uh why I don't think this is
likely is uh in for we select 16
validators so if there's we we run some
numbers and conservative estimate of
solo stakers is 6% uh which means that
in 63% of SLS there's at least one solo
Staker we currently see that solo
stakers and others are are willing to uh
take some economic penalty to contribute
to cens resistance we see people locally
building blocks and we see people
setting a Min bid within meth boost
meaning that if the MEF Boo's revenue is
lower than some threshold I'll just
build my block myself so you here an
economic penalty inclusionists don't
impose any economic penalty but they
also don't gain you anything given that
people are willing to take an economic
penalty and inclusionist basically give
you zero we expect at least some people
willing to participate if only one of
the 16 is willing to participate we
already get the Cen resistance
properties that we're looking
at um how can I be unconditional in the
presence of the block gas limit yeah so
this is I think just a a semantics
question unconditional um could I
conditional basically means that the
transactions have to be included
regardless of uh whether the block is
for or not you could make some separated
uh gas for it which was proposed in the
Erp 7547 which is M inclusionist CP
where there's just a dedicated amount of
gas for the inclusion list and this
usually comes with u uh a somewhere in
Block property uh so potentially you
could put it at the bottom of the block
uh you could also say which is more
complicated for the Builder but the
transaction just have to be in the block
I don't care where they must be in there
uh this would force the Builder to
reconstruct the block more often and it
would be slightly more complicated in
principle ILS with unconditional and
block as limits are not mutually
exclusive because you up the block a
limit to accompany the unconditional
I um if I selection does not take fance
into account could fil make the max EB
increase less effective so actually this
makes it more effective if you don't
take the balance into account you you
select more people who have lower
balance you probably want to select more
people who have lower balance for
censorship resistance because they are
more likely to be unsophisticated maybe
geographically diverse you you probably
don't want to select coinbase even
though they might contribute to the
economic uh and The Accidental
censorship uh so in my mind not taking
balance into it account makes f a lot
more effective
actually wow that was really good talk
and really detailed
um give a round of applause for Julian
yeah thank you
um so we'll be back here at 11:00 a.m.
uh you can just go stretch out go to the
restroom do something and let's come
back here with full alertness and
engagement and amazing questions really
loving how engaged All of You Are
w m
oh
m
um so just a quick announcement um the
next session was supposed to be how
crypto solves real world me but real
world issues have stopped the speaker
from being able to come so um so all of
you can just take a break and go out
stretch your legs um talk to some of the
other people in the room and we'll
resume at 11:30 a.m.
hey
he
o
back
is
sh a
[Laughter]
show
sh
to
a
d
w
GM GM
um I heard it's raining outside so
really good to see the packed room uh
it's kind of it gets crazy in traffic in
uh in Bangkok um so all of you should
now take like a deep breath
in filling your blood with oxygen is
going to prepare you for this really
ambitious talk of how we can fix meev by
Jon abuan uh who is a researcher and
investor at blockchain Capital um it's
an ambitious talk so let's see what he
has in store for us
hi everybody my name is Jonah buan um as
he said I'm a researcher and investor at
a fund called blockchain Capital um we
were actually the first Venture fund
focusing on blockchain period started
about 11 years ago um so the topic of
this talk is ambitious is going to be
can we fix
me and I'm going to assume some baseline
understanding of meev in this talk I'm
going to assume people are roughly
familiar with a sandwich attack roughly
familiar with proposer Builder
separation if that's not you I'm sorry
that you're trapped here with me for the
next uh 30 minutes um so the layer of
the talk is going to be we're going to
set up the problem what is the problem
with me today as it stands then we're
going to say okay well there's a problem
what's the root cause and we're going to
try to get to the root of where me comes
from We're then going to propose two
different schools of thought on how to
solve the problem finally we're going to
talk about all the different
subsolutions that each of these schools
of thought have presented so problem
root cause two schools of thought all
the research around it um so without
further Ado me as it stands today is a
real problem the first problem is
there's an allocation problem and what I
mean by that is me is value that is
extracted did from users yet where does
the value flow in the current market
structure the people that end up with
all this value are the proposers so you
have value being extracted from users
and flowing to proposers who are simply
agents of the protocol that's kind of
weird you would assume well you would
hope maybe the users would get it if not
maybe the applications who are
generating it if not at least the
protocol but the idea that these out of
protocol kind of agents of the protocol
are getting all this value that's kind
of a weird Market
structure and the second problem with me
as it stands today is a centralization
problem what I mean there is first off
there's an oligopoly in the current MV
structure about two Builders represent
about 85% of all blocks built that's an
oligopoly um
and the other big problem is there's a
in incentive to collocate there's a
centralization problem that's
Geographic um so the idea here is a
little bit nuanced I'm happy to talk
more about it in the Q&amp;A section but the
idea is there's an incentive to propose
your block as late as possible you get
more me that way and if the incentive is
to PO toos the as late as possible you
want to be collocated with other
proposers to make sure your block is
accepted so slowly over time you should
accept expect geographical
centralization and we're seeing that so
that's not so good for the sake of the
network we really hope for geographical
robustness and yet the current state of
me is actually putting pressure to
centralize geographically so there's an
allocation problem there's a
centralization problem it's not looking
too good so how do we solve this well to
solve any problem we need to understand
what is the root cause of the problem
right so let's understand the source of
me and this next slide's going to be
probably the most important slide if you
walk away and this is the only slide you
understand
perfect me originates from a monopoly on
the right to propose a block that is the
root cause meev specifically it's the
Monopoly on the ability to include
transactions and to order transactions
in a slot so every 12 seconds or so in
ethereum one proposer gets the right to
propose the next block and with that
Right comes you get to choose all the
state transitions that go into that
block all the transactions and The
Ordering of them so take a classic me
example like a sandwich attack what's
going on well let's say there's a big
buy order the proposer and by the way
it's they're now Outsourcing this Ro to
the Builder but in concept the proposer
is saying I want to put my buy order
right before this big buy order my sell
order right after put the three of them
together and put them somewhere in the
block so they've ordered three
transactions got their three
transactions included and strategically
placed in the block right or including
and ordering this ability this Monopoly
has given the ability to do the sandwich
attack so me originates from this
Monopoly this is the fundamental place
where it comes from so then how do we
solve
me well there's two schools of thought
the first school of thought is me is
intrinsic any decentralized system any
any blockchain is going to have me in it
somewhere it it is going to be exploited
there's me somewhere in the system and
you can't fix it the other school of
thought is no no no me is not an
intrinsic property of blockchain it's a
function of bad design MV is extrinsic
you can actually solve it with proper
engineering so under the me is intrinsic
Camp it's it's something fundamental how
do you solve the problem well we said
before me originates from a
monopoly well sell the Monopoly right so
the idea here would be the monop is
worth something you can extract a
certain amount of value so how much
would you be willing to pay for the
right to extract value well up to the
value you can extract so if you can
extract $100 you'd be willing to pay up
to $100 to extract $100 so the idea is
there's a monopoly in the system we're
not going to get rid of it so let's sell
it by the protocol selling the me it
gets back the value that's being
extracted at the protocol layer and now
you can probably solve the allocation
problem how well you could redistribute
it to users perhaps maybe back to the
application maybe just to token holders
by burning it there's different
approaches but at least you probably
solve the allocation problem and then
from the centralization problem of is
there centralization and protocol we
have to take each solution and and ask
that question it's not clear on the me
is extrinsic camp that me is just a
function of bad
engineering how do you fix it well it
comes from a monopoly break the Monopoly
right simple idea if me is a function of
a monopoly break it so So within each
school of thought there's been many
different ideas that have been proposed
and by the way these two schools of
thought probably exist on a spectrum so
the idea them putting these in two
different camps is more stylistic for
the purposes of these talks but there's
about six big solutions that have been
proposed and they kind of roughly fall
into these camps and the goal for the
rest of the talk is going to be to cover
each of these Solutions at a high level
to people have a understanding and an
intuition of where these ideas are
coming from
so one quick pit stop before we go and
through these six
Solutions today's me pipeline in some
sense falls into the intrinsic Camp of
selling the Monopoly so the way meev
works today is proposers are not
sophisticated enough to kind of exploit
these meev opportunities so what do
proposers do they sell the Monopoly they
sell the Monopoly to builders so
proposers are holding on to this very
valuable Monopoly they can't use it so
they sell it and in turn they
effectively get the value associated
with this Monopoly the builders are
paying that value in an auction process
which means that that's why proposers
end up with all the values and we talked
about the allocation problem at the
beginning this is the reason why and the
reason the protocol isn't getting the
meev is that this whole entire proposer
Builder separation process is happening
outside the
protocol so that's the current market
Market structure today so the kind of
obvious place to start when you're
thinking about how do you fix the me
problem is what if we take the exact
same idea of proposer Builder separation
and run it in protocol right super
simple idea you just at block n you sell
the right to block n you run proposer
Builder separation and protocol maybe
we've solved me unfortunately if you
look at the research and I'm not going
to get into all the reasons why there is
real problems with this from an
engineering perspective it's to do it
also might induce some other weird forms
of me there's you might even be able to
bypass this protocol it's it probably
doesn't solve the problem go on eth
Research you can read a million reasons
why but the intuition here is that
there's this deterministic way of
selling the block perhaps you can
capture me that way right selling the
right to me in Block n at block n h
doesn't really work but what if we could
sell the right to a future block so at
block n maybe we sell the right to a
block 32 blocks later so the idea here
is execution auctions you sell the right
to the Monopoly in advance and having
this buffer from an engineering
perspective might fix it might fix the
problems associated with epbs and Shrine
proposer Builder separation that was the
previous solution I discussed so the
idea here in execution auctions is sell
the Monopoly just do it a little bit in
advance um I've personally done a lot of
research on this put out some blog posts
but there's a great formalization of
this by and Max Resnik and they
basically show the the the highle idea
unfortunately you create a real
centralization problem here where in
kind of selling the blocks in advance
you you you don't really fix the
centralization problem you may be fixing
the allocation problem you may be
capturing some M centralization problem
isn't fixed and on top of that there's
been another school of research about
multi-block me which is the idea that if
you have controled two blocks in a row
you can extract more me than the sum of
the two blocks um that's a very
malicious type of me because it leads to
some pretty bad centralization problems
happy to answer that in a Q&amp;A section
and it seems like execution auctions are
the most exposed to this type of me so
there's some problems here not at dead
end necessarily maybe there's some more
research here we can fix some of these
problems but that's where the research
kind of stands
today so we just discussed a whole
school of thought about
deterministically selling them Monopoly
well and kind of had a dead end so what
if we non-deterministically sell the
Monopoly and the idea here is there's a
couple of ways of selling something you
could directly sell it or you can run a
lottery for to kind of receive it so
under this Lottery intuition there's
idea of execution tickets execution
tickets
are a effectively a lottery for the
right to propose a block so this is
another proposed solution I've done a
lot of research here and the way the
lottery works is there's call it end
tickets in existence every block one
ticket is selected that ticket whoever
got whoever is holding it they get to
propose a block their ticket is removed
from the circulation a new one's sold so
at all moments there's end tickets in
circulation you have a one overend
chance of winning if you're holding a
ticket and you basically have a one
overend chance until finally you win um
so that's the idea you're effectively
hosting Monopoly it's non inter
terministic this actually helps a lot
with multiblock me happy to address that
in the Q&amp;A section um does this solve
the problem so I did I wrote a research
paper with DVID crapus at the um
ethereum foundation and thead Salah
who's a fantastic blockchain researcher
and financial
researcher um what we showed in our
paper is unfortunately regarding me
capture it doesn't seem like execution
tickets are able to really capture all
the me as a result you can't exactly fix
the allocation problem on the
centralization side it seems that
execution tickets these lottery tickets
will probably be concentrated amongst a
couple of actors or maybe even just one
actor so that kind of oligopoly we spoke
about earlier will exist now in another
setting for execution ticket holders and
that's a whole new actor in The
protocol that might cause some problems
so unclear if this really fixes anything
but again we're discussing the vanilla
implementation of execution tickets
there's been questions about what
happens if we extend the model and maybe
we uh sorry extend the idea and maybe
have a unbounded number of tickets that
was a paper by Kristoff uh and it
actually kind of fixes some of the
problem so there's probably some more
interesting research there I don't have
a slide on this but Pascal's in the
audience and he's written some other
extensions to the model that are also
there's there's something in there
there's uh there's potential Solutions
in there um um so the other
non-deterministic school of thought is a
concept called Rand EAS or random
execution auctions it's kind of a blend
of execution tickets and execution
auctions it was a new idea it was just
proposed recently um there's not been
tremendous formalization of it my
intuition is that it probably Falls prey
to the same problems that execution
tickets and execution auctions face um I
think some research is needed to to
really make sure that's correct um but
we'll sa that for another talk um now
the other kind of concept the other
school thought this entire four
Solutions we just discussed are under
the me is
intrinsic um it's always going to be
there so sell the Monopoly the other
school of thought as you guys recall is
me is extrinsic this is this is a
function of bad engineering so the
solution is break the Monopoly how do
you break a monopoly well the Monopoly
is there's one proposer how do you break
it more than one proposer super simple
idea that that that's the concept um and
within this kind of Paradigm there is
two different solutions that have been
proposed the first is fossil I'm sure
over this past week if you guys been
going to sessions you've heard a lot
about it but the highlevel idea is we
have one
proposer and a group of proposers that
are allowed to force to include some
transactions and by doing this you
effectively break the inclusion Monopoly
that proposers have today and there some
other Downstream effects I'm not going
to get too into it but that's the
intuition there and what's interesting
is that fossil if you look at the
research actually works very nicely in
tandem with execution auctions or
execution tickets you can actually begin
fixing some of the problems I discussed
earlier by meshing these two approaches
together um happy to talk more about
this later um but the other big idea is
I would say a more extreme version pting
the multi- proposer idea to its logical
conclusion of no no no no we're going to
really have we're not going to have this
subcommittee we're going to actually
have multiple proposers the idea here
is for Block n you have call it I'm
choosing a random number you have eight
proposers for Block n and every proposer
what they do is they choose a subset of
transactions to include based on their
own local View and then what is block n
you merge all the transactions from the
eight proposers together and you apply a
special sequencing rule to it so by
doing so you've actually fixed two
things you've broken the inclusion
Monopoly and you've broken a sequencing
Monopoly now uh an easy question to ask
is wait a second why can't we have break
in the sequencing Monopoly the entire
time right you can always apply a
special ordering rule to a block there's
no reason that the proposer has like
needs to do that and the reason why we
can't do that when you don't have
censorship resistance is well if a
proposer knows their blocks and have a
certain sequencing and they don't like
the order of a transaction they just
won't include it so you can't apply a
special sequencing rule to a block
without having censorship resistance and
that's something that braid or multi-
proposer solution gives you so again the
idea of braid high level is take a bunch
of proposers they all propose some
blocks some sorry some transactions to
be included into a block merge it all
together apply a special ordering rule
presumably this should break
the sequencing Monopoly and the
inclusion Monopoly so there's a bunch of
questions about this solution um the
first is and this is a me is intrinsic
type of question wait a second I don't
think you can break this a monopoly
there probably exists hidden in this
structure another
Monopoly and in braid the proposer that
proposes last in some sense they have a
monopoly because they see all the other
things that'll be included so they
really know based on what they do the
end result of the block so so they have
some power over sequencing and including
not necessarily the full power that
today's proposers have but some power
and the question becomes can you have
simultaneous release where you don't
have somebody with the last look open
question in the research another
question is that there's going to be
some exclusive orderflow auctions that
are going on how does that affect it
another big question is how does the gas
limit work when you have multiple
proposers that's another um open
question so if you take a bird's eye
view again and just going back through
the talk we began by saying today
there's a real problem we have a
allocation problem we have a
centralization problem this all Spurs
from a
monopoly and within it we had two kind
of ways of solving it let's sell the
Monopoly let's break the Monopoly and
with each within each of these
categories there has been a bunch of
in literature
again I don't know which one's the the
right one um I think a lot of work needs
to be done but I encourage everybody in
this crowd to do some research here and
one of the reasons why I personally love
me research is that meev research is all
about how do you break a system how do
you break consensus how do you kind of
exploit consensus but through this
research you end up learning a lot about
how consensus works and a lot about how
the execution environment works so it is
a interesting form of research that
really gives deep intuition about how
these systems work so I encourage
everybody to dig in I kind of baited
people by saying can we fix meev and the
answer is I I don't know um there's a
bunch of solutions out there um but
hopefully I motivated people to do some
further digging um so I guess finished a
minute early um so I'll leave room for a
little bit more
questions um if I already see a lot of
questions in but you can scan the QR
code and we'll quickly tackle the
questions there's quite a few I'm going
to read them out for the audience
joining online would inclusion lists or
obfuscated encrypted meme M Pools be a
solution to solving
meev yeah so this is a a good question
um the one of the questions when it
comes to encrypted me pools at least is
as a proposer do I have to accept
transaction from the encrypted men pool
and if the answer is no then you could
only accept unencrypted transactions and
propose those and you end up with the
same Monopoly if you're forced to accept
transactions from the encrypted M poool
you could theoretically create side
deals where you have people prove what
the encryption represents and then the
Monopoly comes back there's some ways to
circumnavigate it is my point um so it
is possible that at a first order
attempt encrypted M Pools does solve
some of these problems but it is circum
navigable doesn't mean people will do it
but as we see people go through crazy
lengths to exploit me so wouldn't
surprise me if they
do um in Lottery based proposals what
determines how many tickets one entity
can hold aren't we Reinventing proof of
work so it's very funny the uh the proof
of work comment is is correct in a lot
of ways a lot of writers have written
about this but um what's the most amount
of tickets someone can hold there
there's zero way um maybe unless use
like World ID that you could uh that you
could um enforce um a limit of how many
tickets you can hold because if you say
everyone can hold one ticket create
multiple accounts now you can hold 12
tickets right so there's no way of
forcing a limit here so one one actor
could really have all the tickets and
what we showed in that research paper I
was talking about before is that that's
probably going to happen at least with
the vanilla attempt of how um execution
tickets are uh
proposed um is bra napkin mat
I think braid is an interesting idea I
think it's definitely worth exploring I
mean as we showed in the kind of the
presentation breaking the Monopoly is
one really interesting way of solving me
doesn't mean that meev is extrinsic it
really could be that me is intrinsic and
we're kind of going down a false Road
and we'll never fix it but the intuition
of there's a monopoly have multiple
proposers to break it is probably a
correct one and there's at least a
nugget of Truth there so I definitely
think it's worth exploring and a related
question question how does special
ordering work in braid um so that's a
interesting open research question so
the kind of the dominant idea right now
is just do a priority ordering where you
kind of just rank order transactions in
terms of their priority fee um but
that's just one idea of an ordering rule
there could be many other ordering rules
um and that's an open area of research
of what ordering rule limits how much m
is exploited what captures most me
there's a bunch of questions there so um
there's future research to be
done uh and the other is why can't we
just order transactions based on time
stamp and why is that not a proper
solution it's hard in a decentralized
system to guarantee like the that the
time stamp is accurate and also if you
collude with some other actors you can
you can forge a Tim stamp so you're just
asking for other games to be
played uh isn't it hard for Builders and
proposers to bid the right me value in
advance for future block space rights so
yeah this is by the way this is a
fantastic question so today in the
current meev pipeline if you if you
think about what Builders are doing is
they know expost what transactions they
have so when they're bidding for the
Monopoly right they they they they they
know they know the value of what they
hold so they're they're not bidding
overe expected value they know exactly
the value they have and can make a bid
as such in the case of execution
auctions when you're bidding for
something in advance or execution
tickets when you're bidding for
something in advance you're you're
bidding exante um and you don't you
don't know the value of what you're
going to get as a result you have to do
an expected value
calculation and if you look at the paper
that I put out with David and Fahad we
show that in when you're doing the stuff
in expectation there's a lot of weird
properties first of all um there's
probably more centralization that takes
place um because not all actors can do
these xante calculations and on top of
that certain actors consistently have
higher EX anti- valuations but only exp
poost do other actors have a higher
valuation um you can see that in the the
research um and also part of the reason
why we can't capture all me is that
people are might be risk averse and
downweight the M they will capture
because it's an expectation as a result
when you pay for this Monopoly right you
won't pay the full
amount um the next two questions are
related um if we want to give me back to
users is ass the only practical solution
um and rather than removing meev could
we uh approach in a different way where
the protocol captures some value from
from the ne from the
me um I guess I'm going to answer the
first question I don't fully get the
second question um like guess this this
is a Cella proposer of how applications
can capture their own meev so
application me capture is by no
means um it works together with protocol
M capture so one one nice way of
thinking about the Cella proposer is
that they're just running PBS on an
application like at the application
layer and that definitely should capture
me but I don't think that is um
non-compatible with protocol M capture
um I I this this talk was mostly about
protocol mie capture of how a protocol
fixes a problem I'm not as well versed
in how applications kind of fixed a
problem so I'm not going to comment
further but I want to speak and and and
be
wrong and yeah this second question is
down if
you yeah so the if the goal of the
protocol is to capture 5% me like it's
it's hard to design an approach where
like you're able to Target 5% and get it
what's most likely going to happen is
you try to capture all of it and if you
only want to capture a percentage you
can rebate some or you could just say
that whatever approach is going to
happen is probably not going to capture
everything so this is an 80% approach
but you can't necessarily Target a
percentage per
se um currently meev is not a priority
in the community compared to other
topics how can we increase the attention
on the
topic um actually I don't know if that's
true um I mean fossil has been getting a
lot of attention
recently um execution auctions execution
tickets I've seen a lot of writing
recently I think that in today's world
um interop is probably one of the bigger
problems that users are facing and I I
think it it makes sense why that's kind
of become the priority recently but I I
think I think me has gotten sufficient
attention obviously bias I I love
working with me researchers so they're
more the merrier but I think it's
getting the attention it deserves the
next question is an interesting one but
we've run out of time and um he's a good
guy he's a good guy yep so give it up
this was a really edge of your seat
talk thank you
so we'll have the next talk beginning at
can just get up stretch and then come
back this is the meev room all of you
should continue staying here if you're
interested in the topic
he room
so next up we have Joseph punon who's
been working for quite some time on uh
l2s and it's an interesting talk right
after the last one of how we fix meev
and now we have L2 specific meev
mitigation strategies um so you've all
been a great audience so far like super
engaged I can't get through all the
questions so let's keep that energy High
yeah
Joseph hi everyone so my talk is about
uh L2 specific mitigation strategies and
it's actually a wider talk about you
know me how to mitigate a lot of me and
the general approach that the me
Community has been focused on is how to
live with me um this is a talk more
about how we can really try to get rid
of it as a community and why ethereum is
well positioned to do that Beyond other
efforts L1 chains
Etc um the general approach is fairly
simple um you know we're talking about
you know perhaps below 50 lines of code
encompassing you know everything we're
talking about here and I genu believe
that simple designs are what are
effective and often times are you know
the nut of the problem right it's very
fractal you want to keep things simple
initially and then some complexity comes
out later I think we've over stacked the
complexity too hard today initially and
I think we should take a look at
everything from fresh
eyes ultimately what is this about this
is ultimately about building the world
Ledger right what is the world computer
today it's the Global Financial system
and you know that basically determines
how much wheat may make next year you
know when when you know the the
satellite feeds start showing you know a
lot of brown Fields you know the the
prices start going up for September
delivery and then Farmers start planting
more that's effectively a global
computer and it's driven by a ledger and
the opportunity is for to you know drive
that through crypto blockchain Etc and
we ultimately need to be thinking about
the opportunity of growth above any type
of s short-term uh yield generation
or value maximization because that's
really the promise you know in terms of
serving
Society I believe most MAV is
pathological you know it's a chronic
issue that we're facing um if we believe
that we want Grandma to be using you
know these types of technologies that
we're all building um Grandma's not
going to have fun getting sandwich and
she's probably going to hate it more
than you do um these types of activities
are not permitted in trafi um we need to
be putting effort into fixing this
algorithmically and Via incentives
rather than you know through legal means
obviously and that requires some effort
in terms of our community to try to fix
the problem as opposed to live with the
problem because they're not going to get
on board without actually resolving
these things um let's look at what's
going on in The Wider ecosystem in terms
of an L1 heavy approach right me is over
half the transaction costs paid by users
in aggregate in salon
even ethereum is nowhere near that L1 um
my thesis is that the users have a
choice to go to l2s and then there's
there's uh there's parallel choice in
terms of that um and you know to
properly compare transaction costs
between these two chains requires
including the total roundtrip cost
including aggregate
me token terminal recently came out with
these stats don't really look at how
high the bars are because the the um you
know the axes are different um what I
want you to really focus on is the green
versus the the pink and purple right
what we what what what this is really
showing is that you know the green is
effectively me activity this is not an
accurate representation just it's fairly
loose because you know how you can you
know properly measure it is somewhat
subjective but what you're looking at on
salana is that meev is over 50% of the
the value capture this is a very very
very important point to look at um on
eth you know it's somewhere between you
know let's say 20 25% something like
that right but what's interesting on the
salana side is that it's
growing now why is this really important
it's that me cannot be efficiently tuned
it's a very binary issue right either
you have it or you don't it's not like
transaction fees or gas fees which you
can adjust right you all you can do is
okay I'm going to raise the bo a gas cap
I'm going to raise you know the blob
size I'm going to reduce it or increase
it and and by increasing or tuning that
by let's say 25% well you can see
transaction and gas fees go down Comm
measuredly based on capacity and demand
and there's no knob for mvv like this so
as you start scaling up l1s and l2s me
is going to perhaps remain at minimum
remain static but more likely capture a
larger and larger share of the roundtrip
cost for users and this is a big problem
because chains with pathological me is
going to be less competitive long term
it's not something that you can
effectively
resolve unlike unlike things like you
know how how how much how much
throughput you want on your
chain so that brings us the question is
ethereum position to effectively
eliminate me detectable
me I think we've already solved the
problem to some degree you know I we
been working for the past several years
in ethereum um inadvertently or or
intentionally depending on you know who
you're talking to it to resolve me um
you know I had a talk with like um with
like a you know large VC focus ethereum
focus VC and it was like do we really
want to be talking about this because a
lot of people in you know in in in the
l1s are sort of misguided in terms of
this approach but you know it's you know
we're open source community so let's
talk about it right again this is very
very simple right it's very very very
simple if you have no no l2s in an
environment with no me it's
straightforward if you have me it's it's
pretty complicated you have no choice
it's not it's not complicated you have
no choice
right when you have an environment with
l2s like we do in ethereum if a rollup
starts performing me and might I remind
you effectively no rollups today are
performing me a lot of people are
talking about it EV like maybe half or
more of the rollups are talking about it
none have done it why because the moment
you do it people are going to switch
over like you need to be thinking in
terms of game theoretic incentives and
not complex algorithms what you need is
parallel sequencing and that's what l2s
in inly get you it's really that simple
so I genuinely believe competitive
parallel sequencing solves pathological
Ms you know these types of sandwiching
type of attacks um multiple l2s are
actually multiple sequencers this brings
about sequencer Choice um if one starts
conducting MAV um users will Route
Around damage there's a credible threat
of routing around this damage um
ethereum l2s are actually an me solution
and it's not just for scaling if you
want to be solving parallel sequencing
you're going to be rein Reinventing l2s
that's what's going to happen um I
genuinely believe that projects such as
salana and other emerging projects that
have an L1 specific Focus um will
basically have me dominate their their
total roundtrip transaction costs um and
approach and and approaches to resolve
this will basically reinvent the wheel
right like so if you're like okay let's
just have some type of you know parallel
sequencing on the L1 and not do this L2
thing well then you have a you have some
type of conflicts that arise between
transaction ordering with contracts that
overlap right you're going to have
disagreements of that um and then it's
going to be like well let's SE separate
these contracts into separate name
spaces well you've just reinvented LT
right with with less performance um the
work that the ethereum community has put
into l2s rollups Etc um requires years
of investment across contracts user
Behavior wallets infrastructure and it's
an ongoing process but you know this has
already been years in the making um you
know other efforts such as tees don't
solve this problem either um tees you
know you might as well locate collocate
all your validators Intel Intel's data
center um the sequencers can still
control the input you know it's not a
credible solution forced inclusion
basically forces collusion right um you
know like if you look at how me propos
work today you're basically dealing with
a handful of entities that collude with
each other it's not a credible solution
parallel sequencing solves this in a
much more credible way I'm much I much
prefer you know a choice between 10
different L2 sequencers rather than you
know a cabal of let's say three or four
proposers
right what does this mean if you're
working on an L2 you should publicly
commit to refuse to do pathological m
everyone is already refusing to do
pathological meev but it's a competitive
Advantage for you to do so um and what
do I mean by that why do I think this is
important not just in terms of getting
rid of this problem um but I think it's
also important
because if you don't acknowledge that
this is the incentive and the state of a
lot of
l2s the if you look at where the where
the sort of how this is going to play
out um I really think um entities such
as you know Bas and Inc and OK xchain
okx chain are going to be dominating
because their incentive is to play the
long game their incentiv is to say hey
we want to get users we want to get Trad
find board we want to get the entire
world on board we don't care about this
me thing because it's relatively you
know dimin comp compared to the real
opportunity um if you're operating in L2
you need to at least you know commit to
be on the same level in the long term in
terms of acting in your own users
interests what else can you do um you
need to reduce switching cost between
l2s in order for this to be true choice
you need to ensure that the choice is
tangible effective and and and credible
right so I think there's a shift in The
Wider space right now from amms to rfqs
intents and Order books this is the
effort that that I'm particularly
interested in but it it's it's something
that you're going to be seeing in the
next year and what I like about this is
this breaks the Monopoly and network
effect power that amms have the amm has
significant Network effects where you
know the cost of sort of switching from
one L2 to another is somewhat tangible I
think over the next year as you see
efforts move in these directions towards
newer Technologies split liquidity is
not going to really be an issue um but
what's interesting is that in order for
these new things to work we actually
need revert protection which nearly no
um no L2 supports right
now revert protection is important I
cannot emphasize this
enough everyone actually wants revert
protection um you need it for the new
emerging systems and the M guys want it
too right the M guys want it because you
know um they they they need it in order
to do their itive auction system and
I'll get into that in a second but let's
look at rfqs in tense and Order books
right currently RFQ spreads are wider on
L2 um there's a greater risk in terms of
using these types of intense
constructions on l2s because transaction
contention is a big problem you know if
you have several transactions trying to
get in only one of them is going to get
in right and what in in order to do
revert protection essentially all you
need to do is the sequence or even the
RPC server just says if this transaction
reverts I'm not including in the L2
block um speed helps a lot reverse prot
action helps so much more um in my
opinion decentralized intents account
abstraction are basically broken without
revert protection um this is easy to do
on many l2s they should be doing this
immediately um there's been a paper
recently from the meev guys about you
know um you know it's called quantifying
the value of revert protection um
they're effectively talking about how to
maximize meev um on these l2s I I'm I'm
personally I I think they're math is
solid it seems reasonable I think the
issue is more about eliminating me
rather than you know optimizing it um
and I think you know hey everyone wants
this if you're doing an L2 do revert
protection ASAP it's very very very
important um if you want to be doing
revert protection on the L1 in a
decentralized way um me and a couple of
friends have a proposal EIP 7640 it
hasn't been merged poll request
protection on
bl1 um this is relevant because you know
I'm mostly F I genuinely believe a lot
of tracks move to L2 I think a perfectly
eliminating me on l1s is borderline
impossible um but there are ways to sort
of mess with them there are other
techniques such as um Shifting the state
state tree uh proof to the next block
and then you allow multiple um
transaction routes um that'll also mess
with the Meb on L1 there's no proposal
for that but there's a lot of things you
can mess with them on L1 But ultimately
the real battle is going to happen on
l2s um but in order to understand why
revert protection is interesting and I
cannot emphasize this enough is really
how do you think about me right and this
is going to be fairly obvious um you
already know this but I'm more talking
about a model and how to look at the
problem from a different angle right
everyone talks about Searcher sequencers
proposers what is me right like there
like that's sort of what everyone's
looking at but the first step to
understanding me is actually revert
protection that's why everyone's like
pushing for it right now even the me
guys um you know you already know all
this but you know let's say it's 2022
you want nft five people are trying to
get it broadcast the transaction only
one guy gets it what happens to the
other four guys right their stuff gets
reverted we had this because we had a
public M Pool and there was you know a
Dos attack Vector but if you have a
centralized sequencer this is not a
problem this should not happen right um
if you have a decentralized sequencers
there's ways to mitigate this as well um
it starts looking a lot like the 7640
type stuff um but um but effectively you
know if you don't include anything that
gets reverted the one gets in the other
people don't pay anything right this is
key to actually how the me people think
because they're focused on the fact that
in an auction system there's one winner
and four other losers right those four
other losers trying to sandwich attack
people need to not pay any money because
if you're an auction and you pay any way
when you lose this is not a functional
system this is the core of me design
revert protection is the core nut of how
everything works and this core nut is
also necessary for things like intense
rfqs and Order books in order to break
this type of like Network effect Str
angle
hold and basically the point is is that
if you're doing some type of intent or
any of these types of new things what
happens is okay I'm feeling an intent
right if I'm feeling an intent and four
other people trying to fill this intent
I'm going to lose money if I'm not the
winner right like a lot of the intent
people like are not focused on this this
is the main issue to look at right now
this is the core thing this is the
dialectic this is the conversation this
is the root of it
all but wait what if we move to
decentralized sequencing what happens
then right we need choice and sequencer
in the sense that what you need to do
similar to the prior example is just
extend it down to choice within the L2
as well if we move to if we move to
multiple sequencers within an L2 then
all we need to do is say okay I'm going
to have a contract within this L2 that
says which sequencer my transaction can
get included in if another sequencer
includes it that I haven't authorized
then that's an invalid block on the L2
right and then they get slashed or
whatever it may be right it's that
simple you don't need that complicated
math all you need to do is give the
users choice
right so if one L2 this is the same L2
rollup if there's several validators if
one of the validators starts acting
pathologically then you say that that
that that validator can't include my
transaction right it's not complicated
don't do this on the L1 this is going to
be centralizing if you if you do this on
the L1 because on on the l2s the set of
participants tend to be smaller in in a
lot of these you know if you do
decentralized sequencing and also if you
um you know the fact that like the entry
and exits are going to be less less
frequent
um
so I genuinely believe that meev is
poised to dominate transaction costs
from any l1s without l2s um ethereum is
already very very well positioned for
mitigation to get meev due to Prior and
current hard work that the community has
made um via you know building the l2s
new market exchange mechanisms and
wallet designs if you want to be solving
me this is the effort that needs to be
done ethereum has you know five six
years of effort on this you know like if
you want to be replicating this you need
to be playing back this effort and that
means that ethereum's L2 work is at the
Forefront of the current crypto
dialectic you know this is basically a
conversation that's being had between
people that want to extract value from
the system and people that are defending
against that for the user
and this effort is happening on ethereum
now I think that it's stacked maybe 10
to one in terms of like who's fighting
for what right but I think that
basically the you know this is going to
play out in a way that you know you
can't really game out against you know
you can't create complex things against
once you give the users choice and
maximize users Choice which ethereum is
already well on a trajectory to do so
ethereum has a very very strong
advantage in order to do that and I
think it's very important work because
you know we're all trying to Build a
Better World on chain for everyone and I
think that's the real
opportunity
thanks thanks for that great talk we
have a lot of questions so we're going
to try being quick to get to more of
them we can combine the first two which
is what is revert protection and does it
open a do attack Vector on the sequencer
okay so um it's easier for me to go
number two and then number one obviously
um so Reverb protection is essentially
if your transaction doesn't go through
like like in the in the uh nft example
right someone giving away an nft and all
you need to do is just pay the money to
buy it on chain um there's only one of
these um one everyone broadcasts at the
same time one guy wins the four guys
loses um right now the current status
quo if you just broadcast it on the
public m poool is that you will be
paying gas in order even though you
don't get the the thing you wanted and
this is in the reason why this was done
in you know 2015 2016 right like this is
in the beginning of ethereum is because
there was a Dos of hack Vector in the M
Pool when you when you propagate the
transaction across different computers
if you don't attach a cost to it then
you can keep spamming things and then
eventually you know like the system
starts starts breaking down
um so for the first question this is why
it was done if you have a centralized
sequencer this is not a problem if you
have a decentralized and and I would say
me Services by the way also think this
is not a problem because me
services are basically doing this revert
protection themselves and if this was
not a solvable problem no proposer would
exist right definitionally the fact that
proposers exist means that this is a
solvable problem problem you can do
things like flow control you know like
saying like hey you can only do a
certain amount if you have a certain
locked up per address it doesn't matter
the specific mechanism all I want you to
understand is that revert protection
exists on these me Services right
they're not getting dossed out this is
all very
solvable and you there are various
techniques um uni chain I don't know if
that's a question um but maybe your
thoughts on uni chain uh and its
approach to solving
meev um so I guess I can combine the
next two um I'm not particularly
convinced that te is a credible approach
um I think the uni chain they're doing a
lot of great work right uni chain for
example has proposed revert protection
um they're the first ones to propose it
um I think that's a lot of good work um
I'm not convinced te is a credible thing
like you might as well just run it at
Intel's data center it's not
decentralized
it's effectively a version of PayPal the
the interesting about thing about tees
is that what are these things for right
like these are basically like kind of
like Hardware wallets these
constructions when you when you put it
on Prem on in the premises of a user
that's adversarial to you they always
get broken that's why DRM always gets
broken right this has been like 30 years
of History this stuff gets broken when
you give people a box and and you don't
trust them right these these boxes are
great when you don't trust yourself
right why do you why do people buy these
like Hardware wallets because they is it
because they don't trust someone it's
because they're they're afraid of
themselves screwing up that's what te
are great for it's not because you're
afraid of some other someone else trying
to screw you over it's when you're
afraid that you're going to screw up
yourself um how is rort protection
relevant for
sandwiching so
essentially this is such show okay um so
so thinking about how to answer this um
so when you
have when you have this fight right over
you know this this uh this nft example
there's going to be four people four
people losing and one person winning
this Maps out also to something that
someone can take advantage of someone
can sandwich this one transaction and
five people want to do it four people
are losing out on it and ultimately the
four people losing out on it will change
their behavior if for example they're
paying a cost to it you kind of don't
want them to pay a cost to it uh is what
the Meb people ultimately are thinking
about um now revert protection is also
needed for intents right and intents are
necessary to you know remove these
certain types of network effects and
switching costs um but if you have this
question we can we can talk a little bit
later about it as well and last question
uh how do we know the growing me
proportion on Solana is because of
design rather than mcoin meta I mean
obviously everything is a mix of it um
you know the mcoin meta is Alive and
Well on ethereum as well um I would
argue that you know um ethereum mem
coins are are fairly just almost as
strong as the on salana when you view it
as you know able to sustain you know a
large market cap right um but rather
than you know the the Zero Sum cycle um
but uh yeah I mean that's a factor um
but you know that that doesn't preclude
the points of you know me uh meme coins
rather are a large portion of Bas do you
see me as part of Bas no right it's it's
not a complicated
argument thanks Joseph you can give it
up for Joseph thank you so much and I
think we have an opportunity to really
build something great in the
community uh so we'll have our next talk
beginning in 5 minutes at 12:30 uh until
then you can just uh take a break get a
coffee we have one more hour to go
before lunch so let's go strong
so our next speakers are quite famous uh
flash Bots everyone has heard of them uh
we have Kristoff from flash Bots and
scen working on teliport which is a
which is a new project that flash Bots
is working on um it's a very short title
I like brevity conditional recall so I
think it's going to be a great talk and
it's quite an intriguing title let's get
them on
stage
hello I didn't know that I was famous I
doubt that very much
um chin is
famous
yes so we will talk first about
X here's a story Anon so in the naon lit
nights of 2025 Johnson and Johnson
unveiled x a pill not larger than a
snowflake but it promised a tempest of
change the miraculous truck didn't just
allow people to sherick memories to
erase from their minds it also can
credibly leave a reminder in people's
mind that those memories has been
vanished forever and it's the iconic red
brick walls of Harvard Law School you
with books in one hand and dreams in the
other are on a mission you're not just
another student you carry the hope of
revolutionizing the aaric chambers of
the legal World each night as you pour
over the terms of law you wonder what
greatness Society could have achieved on
a cold evening your phone buzzers it's
DX your old college friend turned
underground dealer his message is simple
got X special price for you the
Temptation swirls around you would you
trade the lessons of the past for
clearer yet incomplete future the
decision rests in your hands and on
okay what is conditional
recall first let me tell you about
perfect recall so perfect recall is the
assumption that we usually make in human
cognition and Game Theory in all kind of
strategic interaction right we assume
that we remember what we have
experienced and we
cannot uh choose what we remember or
what we don't remember so we assume that
humans just remember or at least don't
have control what to remember all of
that will change in
but then you have a technology that
allows you to conditionally recall
information and in particular to
credibly forget and that is the
exploration we do in this project which
will be a paper soon um we want to
understand what are the Strategic
implications or social implications of a
technology that would allow you to
credibly forget information and you can
do that in such a way that you forget
information you commit to forgetting
information if certain kind of
conditions are met in the en
environment so Johnson Johnson xill will
be 2025 before that already have
artificial agents who have access to
conditional recall so we are very
bullish on tees um sort of as a
commitment device because that is a
technology where you can use an
artificial agent put it inside of a te
and then you can generate um
attestations or proofs that that agent
has erased a certain kind of memory or
has um sent some some um
Um send a request to to REM remove
memory from an external um storage
device okay and so if you have these
artificial agents having access to
conditionally recall information then we
can do magical things with it and we
want to present some magical things that
you can do with that um I talk about
more more about philosophical ideas but
in all of them I think there is the
potential for an actual application in
them and then Shin will talk about
already existing applications that um
that use the power of conditionally
forgetting
information okay first
application that's a classical problem
from this guy is canaro and he um
described for the first time this very
famous eror information Paradox which a
very very basic but fundamental idea so
you want to sell a piece of intellectual
property you have an idea you want to
sell it to somebody but in order to sell
it to somebody you need to convince that
some somebody that that is actually a
good idea and so if you start telling
that person to about the idea more and
more and more and more and more and more
at some point that other party has
learned the idea right and then
Contracting breaks down because he
already knows the idea and then he
doesn't need to pay you for it
okay conventional works for this cont
Contracting problem usually is IP law
like um you hire some lawyers and they
protect your intern intellectual
property you have patent law and um you
need to rely on the legal system or you
can do like the classical Contracting
stuff right you can contract only on the
outputs of the technology but not
actually on the actual out um technology
right and then you have all the problems
of asmic information and Contracting so
that's no good but if you have
then you can conditionally recall
information right you can solve this
transacting problem you commit before
the actual selling of the idea that if
you don't like it as a buyer you commit
to forgetting the content of that idea
right and then the only thing that after
the negotiation you remember in case you
don't buy the information is that you
didn't like it but nothing
else here's another class of broad class
of um ideas that you can do with this
technology onetime use of information so
previously I was telling about selling
information now we can also think about
um renting out information using it only
once or twice or conditionally or uh
five times six times and shin has
beautiful examples of that as
well another
quote I don't believe that this story is
true but I would like it to be true so
one of my favorite writers J Le bores
wrote this about a 15th century Italian
Warfare so in 15th century Italy he
claims War has reached a Perfection that
many would call ridiculous once the
armies were assembled the generals
compared the numbers strength and
position of the troops and decided who
among them must suffer defeat um they
decided on on the outcome of that um
that um that war chance and bloodshed
were
eliminated okay that is an instance of
the power of reducing asymmetric
information and bargaining if we are
perfectly informed about each other's
capabilities in the bargaining situation
we can
improve um efficiency we can avoid war
going to war because we can just decide
who has the better Army right without
actually conducting the war okay this
illustrates a powerful idea of this
symmetric information and bargaining and
for better negotiate
outcomes and we have a lot of social
institutions around right ndas and these
kind of things are a way of making sure
that some information only remains in a
particular bargaining in a situation
where it can help improve
efficiency
so that is the conventional work around
ndas and lawyers sharing information for
a particular situation so that it is not
used outside of that situation but with
conditional recall we can can just use
the information put it in a te let the
Bots negotiate and they achieve a good
outcome and after that we forget what
they did
okay another example of onetime use of
information this was constraining the
other party to rock you you can also
constrain
yourself for commitment you can forget
and being for forgetful can be a very
useful commitment
device how so this is a forget um
monopolist example shout out to way die
who put it on his website so suppose you
are a a vendor of some good for example
you sell exps to the local market right
so you run the local pharmacy and you
have a large supply of those experts and
each day same customer enters your store
and you're wondering okay how much is
this willingness to to pay for this
technology you're not sure about that if
the price is too high he will not buy
and if the price is too low then he
could have charged more extracted more
Monopoly rents
right repetition makes it even more
interesting why because if you sell
today you can take that as that gives
you information about the willingness to
to to to to to pay off of the buyer
right so if he buys today under the
current price you know a lower bound on
his value okay now here here's a
strategic interaction if the customer
actually knows this he might not buy
today because he doesn't want to get
rent extracted tomorrow right so in this
case you harm yourself by remembering
that the guy was uh uh willing to buy
today okay this Dynamic can be broken by
a forgetful monopolist so forgetful
monopolist can extract more rent than a
monopolist that
remembers okay
quick one on
reputation I uh witnessed recently two
days ago my colleague Tessa negotiating
um price of a taxi of a tuktok of a Tuk
Tok so here's the story about these tukk
negotiations he did it she did it the
right way so she stubbornly stubbornly
stuck to her price she was always saying
correct thing uh to to do this because
if you appear very stubborn in this
situation at some point the opponent
will give in okay because you have a
reputation of being a very stubborn
maybe even irrational person
okay a great substitute for uh or that
that's that's that's on um on a on a um
that's on a reputational level so Tessa
built a reputation of being stubborn but
here's a Twist on reputation it doesn't
work on the forgetful so if the Tuk Tok
driver wouldn't remember how long they
were negotiating for an hour two hours
three hours if he can credibly commit to
forgetting how long this negotiation has
happened and how many times the already
went back and forth he's in a
strategically better
situation
okay now I pass on the floor to shinan
thanks okay so we've just seen a lot of
like
I I would say like fables and then like
I'm game the are fables and then um uh
yeah those stories kind of help us to
build some of the intuition but now I
got to diving diving into some of the
like actual games and social games that
we play in reality together with some
examples right so like I think wait how
how does this
work oh I I click okay great okay yeah
so um first of all I guess like Kristof
went through a bunch of like economics
examples but there are also some
cryptography examples so um uh I will
say like one of the biggest applications
uh you can see is this from 2008 paper
called like onetime programs so in this
paper you can see uh they specifically
listed some some of the real games that
we play right oh like you want to go on
vacation and then you would like to give
your assistant or your or a friend the
power to decrypt and sign emails on on
your behalf so this is like very
realistic I think um yeah a lot of
creators have this problem
uh a lot of uh just uh uh people who I
guess run companies also have this
problem like I've heard contest times
from uh from uh def5 Founders how
they're uh how every day they wake up
they have like a thousand plus
notifications on their telegram groups
um so obviously like using onetime
programs that allows the other person to
uh reply messages on your behalf under
some condition is uh a classic game for
this um yeah and then next I I would say
for but to to implement this we can see
there's a
uh
um there's like this conditional recall
uh mapping into onetime programs and
then you can see sometimes conditional
recall apps are actually so powerful
such that it's against the AI safety
policy to even discuss it this happens
at one time when I wanted to make the
email recall game um together in with
Cloud uh okay and then some real social
games I think the first one is uh Social
Capital right so social capital in
today's world is really tied into
reputation which is a form of I would
say like sticky uh recall game because
you know us as humans when we play
social games we don't have the ability
to do conditional recall which is why U
reputations are scky and which is why
social capitals kind of accumulate
however with ability to the conditioning
recall we can do something more
interesting right so we uh we know we
all know like Ral is kind of obsessed
with this microeconomics analysis right
like oh social commitment is St dep is
credit and credit is money um and of
course you know R alio has a lot of uh
those quotes So we see like those kind
of Social Capital social games are very
um prevalent Mo but so that means today
most of the social capital is locked up
in um let's say accounts for example in
Twitter right you um a lot of people
right like grow Their audience and
engagement um so a lot of social capital
is locked up in one account in one repap
two platform where you have both like a
liquidity problem and interest rate
problem interest rate meaning that once
you already have a following it's easier
for you to grow and then liquidity
meaning that you cannot really exchange
your social capital or transfer it to
another person right it's kind of like a
a a so bound token is thing um yeah and
you cannot also move them because well
the account has sec information which is
your uh like your identity is actually
tied to the account and the account's
posting R is tied to this password that
you have which uh goes back to the
previous I think example of
uh yeah of onetime programs that when
you go on a vacation you do not wish
your friend to just take your content
and go with it you want to put some
constraints um so then you know using
the a example you can just force your
friend to submit you with a proof of oh
taking a selfie that I have taken X
today after posting on your account U
but of course a more realistic way to do
this is uh uh using using something like
tees so we have done this like I would
say like a research experiment of uh uh
implementing uh an app like this so you
can see over here you could uh for for
example you could put your Twitter
account inside of te and then the Min
nft that represents the ownership to
post once from your account according to
some kind of AI filter so in this way uh
you can Implement all of the uh
conditional recall examples and one time
program examples from the 2008 example
so uh you can see over here you know uh
maybe I want to land my account to
somebody who wants to talk a joke about
te right because uh I'm a b but then you
would like somebody to increase the
diversity of voices in your community
yeah so you can see over here you could
like actually redeem the F and then
therefore you have the uh um entire
flow um yeah so here is an example um of
uh how many people have actually um
joined and then used the tees to
decentralize their voice um and uh yeah
I I think I want to touch so Kristof had
a lot of examples about like um I think
arrows information Paradox right and
then like all kinds of social
interactions but in reality we also see
a lot of those um that just happen very
casually like for example when you are
watching football together with your
friends sometimes you want to roast
other people but you don't really have a
good way of implementing this uh easy
social game however with like you know
conditional recall as guaranteed by um
tees you could do something oh like when
you mean then after you do aot post that
roast my football knowledge if Germany
wins against Spain in the Euro Cup uh a
lot posting if I'm fat
that if that I don't exercise in the
past seven days um a post in qcat a lot
post that about uh aot post that talk
about ethereum Foundation if the nft
Redeemer submits email proof that they
own ethereum email right so in this way
you can kind of implement blind natively
on Twitter um yeah so those social games
couldn't actually be played before due
due to that you have to take over the
other person's phone and send it right
um or trusting the other person to
actually keep up the promise is despite
some incentive problems uh another quick
example is that this terminal of truth
I'm sure a lot of you guys have seen is
that like it's an a mark and and tip I
think one Bitcoin into it um but then
the problem with AOS uh is that despite
their very interesting just social games
right like you can see them as mass
massive PVP version of Turkish carpet
salesman game um the AI essentially acts
as like a coordination of correlation
device for Twitter discussions for reply
guys uh and this game is only playable
if the mechanis is credible and not
riged like if the human player is a if
the human owner of the account is able
to wreak the as replies then uh you know
the game suddenly becomes uninteresting
um so then the using the same technology
we could Implement uh a conditional
recall agent essentially you have the
same terminal true spot however you uh
give
it yeah essentially uh you make it such
that the human developer cannot do uh
conditional recall to credit L
relinquish the
control yeah so then we implemented some
of those as an example um and uh uh you
can interact with
at
okay see you and uh let's have some
questions I think who had
time yeah Kristoff if you want famous
before you're certainly famous now after
this amazing talk uh um you can scan the
QR code and submit questions we already
have two of them one is more of a fous
comment but still funny um any chance of
collectively forgetting that Trump was
ever elected um which is more like um is
there a difference between like group
forgetting and individual forgetting in
the yes ABS great question so two two
takes on that um I didn't put it in the
talk but because I thought it was too
spicy but there was a forgetful
negotiator example and so we were very
bullish by in 2024 but yeah didn't work
out um on the collective forgetting we
have a beautiful example in in um in in
the paper where basically collectively
forgetting about something is sometimes
helps uh helps the collective for
example in reputation games so the
example is somehow um example of
extortion Mafia wants to extort resource
from a community and so if we credibly
commit to forgetting that the mafia is
sort of Reckless and we collectively act
not fearfully then uh Mafia will
actually not extract um rents from from
our community so there are examples in
the paper that very much go in that
direction um the the other question is
also a distinction that is there a
difference between committing to forget
a piece of information and committing
not to use a piece of information um my
take on it maybe shin has a different
take um I think a committing to forget
information is in some sense more robust
right so it's cannot be broken that
easily but there is in principle a
general equivalence right if you never
use a piece of information and make that
credible that would be the same as not
like not on a psychological level for
yourself but behaviorally it would be uh
equivalent do you have a different
answer uh I would say it's more yeah
it's becoming more equivalent if you
move into the future right like one
Trend we have seen is that like in the
past property is defined by what you can
Define what you can defend yourself
physically so like in the stone ages
it's like you know oh what I can beat
the others up and you know if I take the
other the other person's Rock then
that's my own property um but then as
you know Society progress it's more like
a law kind of be became this way of like
you defending yourself and then like
that that some kind of piece of paper
defines what your property is and then
in the information age it's more like oh
like my password actually like my
Twitter account is my property so then
like oh the password is just a piece of
information right so then like if I
commit to forgetting that information uh
would be more equivalent to committing
to never use it right because in the
past we can only commit in to not use it
and none of those things are information
related um yeah so I guess my answer
would be like um it it's becoming more
and more equivalent in the
future um we can maybe combine two
questions so one is how do we know a
Twitter account is actually controlled
by an AI agent in a in a t and not
another schmuck just claiming to be an
AI agent but it's actually some dude TR
extract oh yeah uh absolutely you can do
you uh so you should do some kind of uh
you know always trust by verify right so
you should uh download So how T is work
is remote remote at that station and
then how uh currently um in the example
that we implemented is that you should
go to the GitHub and then you um you
know you you you produce the code hash
yourself and then you compare it with
remote adapation hash that you got from
the remote adapation service which is
essentially kind of like oh like this is
uh currently the memory and data running
uh and code sorry running inside the sgx
and then Intel kind of Science and you
compare um that oh they are indeed the
same you can of course do more fancy
stuff which is like um oh you post
remote atation onchain such that anybody
can slash something if um because
somebody proved that Intel at this uh at
at this time signed like um a statement
essentially saying oh this is a code
running inside the te and you know once
you can prove the code you don't you
know that it is not a human
developer I think yeah you answered the
second question also here so we have one
last question which just more fun
application
ideas use a source of fun yeah yeah yeah
there's a lot I mean um uh for example
like we see a lot of like anal accounts
so you can do like essentially a group
owned anal account that that part I
think is interesting especially like in
um today's world I think like a lot of
information sources are very fragmented
so you can do like oh like um whenever
this message gets I don't know like a
eight emojis on it then it get Auto sent
from the group uh group own the account
another one I think is uh just
combining this idea of um you know the
current mem coin meta together with t
and conditional recall So like um what
if like for somebody to trade the mem
coin they must let's say oh take take an
IQ test and then like post something on
their Twitter once so then in this way
you like you know you you you feel more
comfortable doing the PVP meta on
ethereum great let me quickly also show
the paper if you want a pre-print um con
connect with us and it will be out soon
very
soon thanks that's a great talk let's
give a round of applause
yeah so we will be reconvening in 5
minutes for the last talk before lunch
um this is the meev room uh we've had
great questions throughout uh the
morning session and um like it's like
true stay for the next talk it's going
to be a good one
so we have our last talk now before
lunch and it's a really good one uh it's
by Andrea canido who is from cow
protocol and it's a new mechanism which
they've designed for auction based uh
settlements and I'm really curious to
know what their research and what
they've
cooked hello
everyone all right so uh yeah today I'd
like to discuss with you new uh auction
design that we plan to implement at C
protocol um and a little bit of uh kind
of the thinking process behind it so how
did we get to this specific auction
design uh which has to do with the fact
that you know uh blockchain is an
environment where there may not be a
numer and of course I explain what it is
uh in a
second all right so many talks uh that
has to do with defi um start by saying
okay look look we have all these
mechanism from traditional Finance but
they don't necessarily quite apply to
our environment because say you know in
the context of blockchain transaction
can be reordered uh and therefore we
have MV uh I'm going to follow a similar
template but I'm not going to focus so
much on the usual suspect uh and instead
focus on a different element which is
the absence of a numer a first of all
what is a numer a a numer is an asset
that in your Market or in your mechanism
your environment you can assume that
everybody likes and is happy to receive
and can be used to Share value between
people okay now offchain there is
usually a numer in the environments you
consider if we want to look at financial
markets well typically all stocks are
traded against the national
currency so the national currency is the
numer rare uh a possible ex ex exception
could be Forex Market um where people
exchange National currencies but when
you look carefully that's not quite
exception in my opinion because first of
all there are very few assets
exchanged and then uh essentially the
vast majority of this trades is anyway
settled against the US dollar so it's
even in that environment there is
theoretically there's no numer rare
anybody maybe demanding different asset
and exchanging any to any currency for
any currency really most of the volume
goes through the dollar anyway now on
chain things are very different uh there
may be specific concept environments
where you can ass assume that there is a
num R but I think in generally this is
not you know it may not be the case um
because we have Anonymous participants
that could live anywhere in the
world when you look at financial markets
on chain people may want to swap any
asset for any other assets and there are
like thousands I don't know if there is
a number out there I know that uh uh cow
swap in its history has traded more than
least that many different tokens on
chain at the moment and probably even
more uh which makes it very different
than any uh kind of the Forex Mar for
market for example Al because here what
matter is not the number of tokens is
the number of token pairs so that's kind
of blows up the complexity of the
problem so why does this matter because
uh the numer rare and the absence of the
num uh determines how easy it is for
people to share the benefit of
collaborations okay this is something
that we know from a branch of of gameing
theory called Cooperative Game Theory
which is the branch of game theory that
has nothing to do with auction in fact
uh but it turns out that it also matters
when you're designing certain type of
auctions such as trade intent auctions
now what is a Trad intent a Trad intent
is uh essentially an order uh in which a
user specifies a sell token and a buy
token and might specify also a limit
price or a slipage
tolerance and then then it delegates to
another uh agent a solver uh the exact
execution of that order and this is done
in the context of an auction where
solvers are going to propose prices for
each order for the different orders um
and let's say know this the details are
important but for the moment let's just
say that the solver that proposes the
best price wins the auction and then has
the right to complete this order and
actually execute it on chain okay now
this is an environment where uh you know
you can have separate auction for
different trading tents okay an order
come in you run an auction another order
comes in you run an auction and this is
how protocol like 1in fusion and Unis
swop X work however there are typically
additional efficiencies when order are
executed together this could be in the
form of Coincidence of wants maybe
people can trade directly with each
other without really having to access an
external Market it could be in the form
of gas savings uh Coincidence of ons can
also arise as intermediate hope of
Trades anyway generally you can squeeze
out additional efficiencies by executing
trades
together but of course the problem
becomes in which assets those tradition
those efficiencies materialized maybe
it's extra e because it's gas gas
savings maybe it's something else but
then not everybody may actually want the
asset uh in which those uh efficiencies
are actually generated and the question
becomes then you know is it how do you
share those extra efficiency if it's in
an asset that not everybody's de
demanding okay and then yeah then the
question becomes while do you want to
execute the two order togethers even if
there are efficiency because you cannot
really share them and if you do then
what is the fair share of this extra
efficiency these are the type of
question that motivated our research
paper that I wrote with a colleague at
cow swap called uh Felix hanek where we
build a theoretical mathematical model
of this uh type of auctions we use this
model to compare the two most common
auction formats which is batch auction
and separate individual auctions and
then we use uh the model to then St
propose and study a new auction format
would be called the fair combinatorial
auction which if you want I'll get in
the detail later but it's a kind of a
merge between a batch auction and a kind
of indiv having separate individual
trade
auctions and you know this is a bit like
cooking the say you're putting two
things together whether it you generate
something with nice property or not kind
of depends on how you do it and it turns
out that you know if you do it in a
specific way um this Fair combinator
auction can actually provide strong
fairness guarantee so you have a notion
of fairness that has to do with how the
efficiency from batching are shared uh
and that the auction can guarantee if
you do it some other ways you have
absolutely no benefit of doing this now
for today's discussion I'll just give
you a high level discussion of the two
most commonly used auction formats for
Trad intent and I will discuss then the
fair combinatorial auction in the case
where it does provide fairness
guarantees okay but knowing that if you
change the design you should know that
maybe does not provide any fairness
guarantee
anymore and the QR code here is the link
to the paper if you want to kind of dig
into the mathematical details and the
additional results
there all right and by the way to
reiterate this is something that we are
planning to implement a cow protocol so
we you this will be live at some point
uh in the next few
months all right so let me start with
how things are done currently at C
protocol C protocol runs a batch
auction that works in the following way
and apologies for the bit primitive uh
kind of Graphics here so there are user
that come in and submit
orders these orders are added to an
order
book and uh as time intervals which
correspond to the closing of a batch uh
we the the auction starts and solvers
can bid on groups of orders or even
individual orders that are uh on the
order book
okay solvers may be somewh specialized
in certain type of order so they don't
need to be done the exact same
order and however they are they can
submit a single solution uh and which
here can be a collection of orders with
prices
for those orders now they then send the
proposed prices for the orders that they
want to execute and then uh the
auctioner uh ranks this proposal by the
total value return to user we have a
concept called Surplus but for today
this is you know you just can think of
it as just really the total value of the
asset return to users this requires some
price feed of course because you know
one order may want to buy Dodge the
other order may want to buy something
else and Sol as might propos different
execution if you want to be able to
compare them sometimes you need to have
a price me a price that allows you to
rank those solution okay and okay there
is one winner and this one winner goes
and execute the solution on chain and
the other solver okay they are losers
they don't don't get anything right this
is the batch auction there are a number
of additional rules for example uniform
clearing prices you know if you have the
same token pairs in the batch then they
the the same so all Traders trading on
the same token pair on the same batch
must have the same price but for today's
discussion this is not too
important okay so yeah so this is a
summary of what I just said now compare
this with what other people are doing um
uh the other people are essentially
running uh trade by trade Dutch auction
the fact that it's a Dutch auction is
not too important but this is really
just separate auctions for each trade
that comes in okay and just to give you
some numbers if uh this markets handles
about more than5 billion of value each
months uh I think bit three of them is
like C C protocol so goes through the
batch auction mechanism and the
remaining part is split with this the
other two so the remaining part is
executed using this individual Dutch
options all
right what are the pro and cons of
mechanism now obviously B auctions are
better at exploiting whatever
complementarities and additional
efficiencies there are when you get to
execute multiple traits together
Coincidence of whats gas saving so on
and so forth precisely because a solver
has the view of the entire order book
and can actually in the solving logic
start thinking oh look if I take this
order and this order and this order
maybe I can make a ring trade
example this is not possible to do if
you have separate
auctions now
ER but on the other hand if you have
separate auction there is there is a
benefit there because you can allocate
different order to different solvers
even orderer that are received at the
same time so say that you have a type of
order for which one solver is very good
another type of order for which another
solver is very good you can you can
specialize you can give one order to one
guy the other order to the other guy but
in a batch auction you always have one
solver winning potentially multiple
trades so it's harder to exploit this
benefit from solver
specialization now batch auction this is
we show in the paper and it was you know
maybe you need the mathematical model
for that but one result is that the
batch auction is better at generating
competition between solvers because
again if you have somewhat specialized
solvers and run this individual auctions
on each on one auction per trade then
really just the solvers that are good at
that trade will compete okay you have a
subset of the solver in each auction
essentially where the batch auction
forces everybody to compete with
everybody else so there is a higher
competition between solver and more
value return to the user in General on
batch
auctions and on the negative side like
in batch auction can be unfair if you're
not careful let's put it this way
because in the vanilla batch auction you
are just ranking solution based on this
total value and you're kind of oblivious
to the fact that perhaps you know yeah
this total value is very high but one
guy is getting a pretty shitty deal and
another guy instead is getting a great
deal and maybe that's not something that
you want okay you Agate everything and
you are not you don't see it now the way
this is currently uh handled at cow
protocol is through a thing that we
called ebbo essentially we have a uh um
a routing algorithm uh that checks after
the fact uh whether the execution of
each order was better than our own
routing algorithm and if it is not uh we
call up the solver we tell him off and
we ask them to reimburse the user for
this kind of ebbo violation and the hope
is that then they will be more careful
in how they actually split the benefit
of of of this so how they allocate value
between the user this is time consuming
uh it is a vector of centralization we'd
like to be more
decentralized and also from a more like
 theoretic mechanis design
perspective it uses information
available to us so it's our uh uh
routing algorithm but the experts here
are the solvers so we are building this
reference for fairness from our
information but we are not the most
informed party here the solvers are the
experts so we'd like to instead build a
mechanism that elicits this reference
for fairness from the solver
themselves yeah and therefore you know
each mechanism has its Pro and cons uh
and therefore this really begs the
question can we really think of a third
type of mechanism where a you might have
in equilibrium either batching or
specialization so it leaves open the
possibility of having watching or
specialization depending on what is the
most efficient thing to do in that
context uh it generate competition
between solvers and has a notion of
fairness so you can Define fairness and
say okay the outcome here is
fair and this is the new this is exactly
the fair the the fair combinatorial
auction it works in the following way ER
first it's a combinatorial auction so it
allows multiple bids per solver so
solver here can submit a single solver
can submit say a bid for order one which
is how many tokens I'm willing to return
if I only win win order one a a bid for
order two a bid for order three but also
a batch bit say okay but if you give me
the three orders together I can generate
so many token for the first guy so many
token for the second guy so so many
token for the third guy so this is a
multiple bits per
solver and then the important step here
is a filtering of batched bids where
what you do is the following you first
consider only bids on individual orders
okay and then you ask yourself well
suppose I have uh really separate
options one for each orders and those
are the bids for in that auctions and
say that the auction is in first price
how many tokens this guy would have
received okay this is then the reference
for fairness okay because you say well
you know if I was really to just have a
first price auction on order one with
the bids that I got order one would
receive that and you use this ref and
repeat for every order and use this
reference to filter out batch bids
whenever uh the batch bids propose an
execution that is worse for at least one
Trader relative to this fairness
Benchmark
right and then what then at the end you
have some surviving batch bids batch
bids that were not filtered out and you
have a bunch of individual trade bids
and you want to recompose a solution
with multiple bids uh in a way that
maximizes an objective for example total
Val value that you return to the
users if this was fast let me bring back
the great graphics I had earlier here I
have two solvers um and importantly they
are allowed to submit multiple bids in
this example solver one has uh uh so
each solver here has three individual
bids okay uh solver one sends one
individual bid on on the green order uh
an individual bid on the yellow order
and one on the red order this says I'm
willing to return to the green Order X
many token if I only win that order
similarly solver two send some
individual bids and then in the example
each solver sends one batched bids which
contains a collection of orders okay and
typically the amount returned in the
batch bids uh for the same order might
be different than the amount return in
case the solver wins only that
order then you construct your reference
outcome as I said if the auction is
first price essentially you always want
to just take the maximum of the
individual bids okay that's the
reference outcome you use the reference
outcome to do the filtering so you say
okay in this batched bids is any of
those bid uh a value lower than what the
guy would receive if I was to consider
this outcome instead and in this example
let's say that the first be the bat B
from the first solver survived this
filtering so it's fair quote unquote
relative to this
reference while the batch bid of the
second solver does not uh perhaps I
don't know in the yellow order what
solver 2 proposes here is worse than
what the order yellow order will receive
if you just looked at the individual
bids so it's filtered out and then
finally you have this is the composition
of the winner the you have the comp the
the the the solver ones batch bid
together with solver two individual bid
on the purple order okay that's how you
reaggregate everything in the
end now there are this is a new type of
auction so you really need to study okay
and it sounds maybe good in practice but
then you really need to be careful in
what is the uh the Strategic
consideration that uh solvers are going
to make when bidding in this auction and
therefore what is the equilibrium that
you expect to emerge now in terms of
strategic consideration
there are two important things first if
you compare bidding on these individual
uh trades here to Simply Having separate
auction per trade period here there is a
higher incentive to bids in the
individual trades bids because you
anticipate that the way you bid on the
individual trade will be used to
determine the reference for fairness and
might end up kicking up your opponent
bch bid as unfair so typically you want
to bid higher in this individual bid
then you you will do in the standard
like uh simultaneous
auctions at the same time you might be
lower here in the batch speed like lower
value um than in a standard batch aution
precisely because if you expect the
other guy's batch bid to be kicked out
as unfair then you don't need to be that
high because you think there's going to
be less
competition the composition of these two
effects generates an equilibrium that uh
in which you have fairness guarantees
meaning that in equilibrium each So Sol
has always return strictly more to the
Traders than in if you had done a a
standard uh kind of simultaneous first
price auction this separate auction so
it's always better for everybody than
having the individual
auctions you may get batching or
specialization depending on the relative
benefit it could be that different
solver wins different order or one
solver wins a collection of order
depending on which is more
efficient and it is however true that
there is if the equilibrium is batching
the winning solver might return less to
the Traders than in the batch auction so
in a sense the takeaways that this
auction format generates fairness
guarantees but this is sometimes at the
expense of the total value returned to
the user which if you think about it
makes sense because here if you just
wanted to maximize total value you
should just do a batch auction here
instead you are introducing a second
element fairness and of course the
second element means that sometimes
you're trading off a bit like on the
total value you're are generating
so to summarize and conclude uh trading
tent auction are cool and they the
future like this is a short time to say
that they're really at the center of
many of the discussion we are having in
these few days there a center of
discussion about me there are a center
of discussion about liquidity
fragmentation uh now there is this
extension to cross chain that is slowly
materializing so it's also at the center
of the discussion about uh kind of chain
abstraction and all that so the really
kind of very important element I think
in in in Defi and blockchain in general
you usually there are efficiencies from
batching but of course then how do you
share this efficiency it's not obvious
there are fairness is a is a concern and
uh here is a proposed solution the fair
combinatorial auction which hopefully
should be live in a few months thank
you thanks that was a very meaty talk
and we have equally meaty questions um
in the current version of cow swap why
do solvers make bids on subsets of
pending orders and not on all in one
batch at once is it possible for a
solver to make multiple bids right now
so I mean uh I don't know if it's
technically possible but it doesn't
really make a lot of sense right now
because anyway there going to be a
single solution chosen so if a solver
comes up with multile possibility it
should just return the one possibility
that generates the highest value because
that's how the auction will R rank all
the solutions
okay um the next question is uh is this
model scalable you have two race to end
possible batches each time can solvers
manage the load EXC excellent question
so there is a general question about
Comal aution of this thing called winner
determination problem so the
computational complexity of the problem
can expand a lot now this is why I said
uh uh here the important part is the
from the auctioner is the filtering part
okay so you want to remove some of but
some bids from the auction based on this
fairness argument um which on the one
hand should make the the the determining
the winner easier okay because you have
fewer bids to work with in the
recomposition stage um and it's also
some orthogonal in exactly how you want
to do it you can use some hor istic to
determine you know the collection of
bids that wins uh which might not be the
exact Optimum but it's easy to calculate
and this is similarly with the
with the with the solvers of course
there is a theoretical Optimum that uh
you know make require a lot of time to
calculate uh and in the same ways the
auctioneer will use some shortcuts to
you know make everything manageable uh
solver should should come up with some
Shortcut as well uh your auction doesn't
seem incentive compatible so the first
price is not a good measure of fairness
feds could also bid non mono tially I I
disagree so I can assure this is not uh
nap research that is a 30 page paper
with all the proofs um so unless this is
stif comp compatible in some non obvious
way but in terms of uh deriving the
optimal BS the best responses in the
equilibrium I can assure you everything
is is there and and shown can solvers
pretend to be users and game the batch
er uh so this is an excellent question
that doesn't quite apply to the
theoretic to the discussion I had uh
it's true that it applies to another
aspect of a cow swap um batch auction
which is that now there are SOL receive
rewards from the protocol because of
these rewards it it could be the case uh
there are attack Vector such as the one
discussed here but in a sense I didn't
discuss reward so let me not bring up uh
this thing now does it make sense to
decentralize the auctions behind cow are
you working in this direction so it
makes sense and we are working in this
direction how will you order different
solver Solutions in one batch so
actually yeah so you could have um it's
a tricky problem um because obviously
the first solution gets an advantage
when
executed in a sense
um yeah so the problem is that a solver
submit a Sol observes the state on chain
and then submit a solution then you know
next block it goes and execute uh the
solution but then other thing happens
before the solution is executed that
might actually change the state of the
blockchain for example the liquidity
available in am H and make the solution
proposed not executable anymore or more
costly than expected blah blah blah so
in a sense there are zillions of things
that might happen from the moment where
you think of your solution and when the
moment you execute it which means that
you need to be kind of conservative okay
when you propose a solution and now you
need to be a little bit more
conservative because among the zillions
things that may happen when you before
you submit your solution there is a
zillion plus one which is another solver
also submitting his solution so yes it
introduces some additional risk for a
solver in an environment that is already
fairly risky and so yeah just general
advice is to solver be conservative
anticipate that things might change from
the moment where you choose your
solution and the moment where you
execute Your solution is there a public
record for historical
ebbo uh ebbo prices or ebbo
violations uh ebo prices I don't think
so EB violation is an excellent question
uh these are onchain transfer done by
solver just to a user a bit out of a
context of a of a of a batch so this is
for sure recoverable somehow but I don't
know if there is a like easy to access
uh repository or like data that one
could be bad um so we are out of time uh
but there are at least like four more
questions that I can see um it is lunch
break now so um you can easily go and
talk to Andrea as well um but it was a
really meaty talk and we all appreciate
it and uh thanks all right thank you
much so we'll be back in uh 1 hour at
meev room for anyone interested in this
this is the place to be
oh oh
m n
oh a
m m
SC
a oh
I oh
h m
br
n
GM GM welcome to me room as we've
informally been calling uh the space
since morning um it's now post afternoon
on the last day which is always the
slump period but we have an absolute
Legend coming up to talk next one of the
original Visionaries behind PBS and A
lot of other fundamental research the
one and only Pabi mono um who's going to
be talking about changes to the
consensus layer and how that would be
going forward uh he's with the ethereum
foundation and leading some of the core
research on that front come on
now yeah thank you for the introduction
and thank you for coming to the session
this afternoon it's the tail end of
Devcon I hope it was really nice for you
and I know we all a bit tired so I'll
take it slow uh and show you some of our
results so the talk is titled Fair
rewards for more decentralized ATT
testers uh I'm replacing one of our
Coors who unfortunately couldn't make it
but I'm really excited to tell you about
our
work so why do we need uh decentralized
ATT testers so validators are the ones
who participate in proof of stake in
ethereum uh as part of their duties
sometimes they are asked to be a testers
so you can think of it as the swarm of
people who are making sure that the
chain comes to consensus um you have
thousands of people uh speaking in every
round every every 12 seconds they cast
votes and it's really really important
for these votes to remain as truthful
and as unbiased as as possible there are
many many mechanisms in the protocol uh
that would horribly break uh if the
attestation layer was was not in a in a
good shape and so we need these votes to
remain truthful uh which means we also
really need to ensure that the voice of
these ATT testers is secure and heard uh
the paper discusses uh an attack which
I'll present in the in the next section
uh essentially trying to show you that
the mechanisms we have today are perhaps
a little too brittle uh and so I'll show
you how to how to fix that or at least a
possible uh Way
Forward uh most of the talk is adapted
from the paper that we released earlier
this year breaking the balance of power
this is Joint work with rusbe who was
supposed to present today news R Casper
my colleague and
Bart so let me start the talk with
showing uh one of these attacks that may
endanger let's say the health of the
attestation layer uh it's a somewhat
simple commitment attack um yeah and if
you if you don't know what a commitment
attack is it's it's sort of an umbrella
term we use to describe any tag that
looks like this somebody deploys a smart
contract or some kind of commitment or
threat uh to try and warp or modify or
hijack the incentives of other
validators to to do the correct thing so
I'm I'm trying to incentivize people to
to do the incorrect thing for my um
let's say benefit uh usually this is a
rough pattern but usually looks like
this so there's an attacker who commits
to a certain course of action for
instance via a smart contract uh the
victims as a result of the smart
contract being published uh need now to
adjust their behavior if they're
rational it might be more um let's say
incentive compatible for them to to to
deviate to a different action and what
what happens as a result is this really
coordinates the victim's Behavior
towards um yeah just it induces the
outcome that the attacker wants to
happen in the in the first place so
there are many interesting questions on
on this like there's many ways that this
reappears um there's questions Also
regarding the credibility of the
commitment this matters a lot for the
attack to be to be successful but in our
space we don't like ways of making uh
such kinds of credible commitments for
instance via Smart
contracts all right so to describe the
attack a little bit uh I need to give
some of the basics of our consensus
mechanism which is called Gasper um the
consensus mechanism is basic Ally built
from two components there's one
component which is the finality service
that's known as FFG the friendly
finality Gadget and another component
which is the availability service which
is uh lmd ghost and so on the chart here
you can see that the chain progresses uh
there's a part here which is highlighted
in yellow which is the finalized ledger
so every so often we come to consensus
over yeah this is the prefix of a chain
we have Economic Security on um yeah on
that that the the this prefix will not
change in the in the future so this is
like very very robust uh let's say
finality but we want ethereum to make
progress even if we don't come to
finality immediately and this is why we
have this availability component so we
have a live Ledger that makes progress
and this live Ledger can diverge so we
can have Forks because we're not
finalizing blocks every slots so this
allows the chain to to Fork once in a
while so so how is this uh constructed
so to progress the chain we need to
assign duties so we have our set of
validators which are the people bonded
with a proof of stake mechanism and we
ask them to produce blocks so every slot
we sample one validator to be uh the
proposer and the proposer is responsible
for outputting a block the block
contains both user transactions and the
votes of ATT testers and the attester
votes they carry data relative to the
two services that I described previously
so FFG data what should we finalize like
what should we try to make uh fixed and
lmd ghost data which is where is the
current head of the chain so lmd ghost
is the service that allows the chain to
progress there can be many Forks so the
ATT testers need to give their views on
where the current uh head is in their
own
view so in the good case this is what
happens so the first proposer makes a
block then we have the ATT testers in
green who cast their vote on the Block
they say okay the head is this the first
proposal that released the block and
then the second proposer comes in links
to the block that was issued previous to
them uh so the first one and includes
the votes of the ATT testers so here all
of the ATT testers are honest in green
uh and the next proposer just simply
includes uh the votes of the ATT testers
so this inclusion of a votes allows us
to yeah recuperate the votes on chain uh
and Dole out the rewards for the for the
ATT testers at the end of every Epoch so
it's very important for these votes to
be to be
included but now let's describe an
attack so in this commitment attack a
proposer can threaten to ignore the
attester votes if the ATT testers don't
vote for the proposer chosen block so
the attack goes in in a few steps uh the
first proposer issues their block that's
the one on the left uh the second
proposer issues their block two linking
back to the first proposers block and
the ATT testers of that slot are honest
so this is the nine green votes that you
see in the in the bottom left and they
all say okay this is the current head
and they get included by the proposer in
the middle so that's the first step in
the Second Step the proposer on the
right the third one uh wants to reorg
the middle proposer so roring is
essentially trying to kick out the block
that was produced by the middle proposer
from the canonical transcript of the
chain and so to do that this third
proposer can commit previews to even
this uh situation happening to say you
have to vote my way and my way will be
that instead of linking to the middle
proposer I'm going to link to the
proposer that's in the left so I'm going
to try and reor the middle proposal and
you need to vote for the fact that I'm
right like that this was the head the
rightful head for me to to build on so
this block on the left and if you don't
vote my way I'm not going to include uh
the votes in my own block and so that's
the threat that the proposer is making
and what we show in our paper is that if
the threat is issued there is a Nash
equum where this attack succeeds where
essentially all of the ATT testers that
are supposed to vote uh in between the
middle and the right proposer are going
to want to follow um the the outcome
that the that the malicious proposer is
trying to to achieve which is uh reing
the middle proposal so it's a pretty
simple attack it's really based on let's
say very weak uh properties but it can
do a lot of damage like rearing blocks
is not so nice first because the middle
proposer gets ignored so they lose
whatever MV rewards are in his block for
instance and second because yeah we lose
a bit of throughput at the at the same
time so these are really things that we
we want to defend against even if again
the the purpose of having this
availability or live Ledger is for the
chain to to make progress and
potentially to to get into these
situations uh yeah in addition the so
the the testers that are ignored by the
malicious proposer they lose their
reward because they don't make K on
chain uh in
time right so in our paper we discuss
this attack we also discuss some
extensions uh we show that the attack
can actually happen over multiple blocks
uh where one proposer uh incentivize
both the proposers before them and the
ATT testers in the slots in between uh
to follow some kind of yeah prescribed
script to to reog uh a large amount of
blocks this works when we consider their
fixed attestor sets so when the players
don't rotate between rounds but in our
current protocol the players do rotate
we have different ATT testers uh every
every slot and so we also consider the
attack when we have uh players that are
that are not fixed we also show an
attack that's a bit inspired by the
selfish mining attacks where you are
trying
to destroy the progress that some of the
players some of the Hest players have
been making by by being um malicious
right so we have this attack which is
potentially yeah a bug that we can fix
uh and the way to fix it is essentially
to decentralize the role of a proposer
in terms of including these attester
votes on chain and so we show how we can
do that and by the same um fail swop uh
fix the rewards and try to yeah save our
ATT
testers so how do the rewards work in in
etherum proof of stake uh today the ATT
testers are rewarded when their head
vote so the lmd ghost vote the vote on
the state of the available Ledger uh is
both timely so the vote has to be
included by the next proposer and
correct so their vote agrees with a
majority of the testers right we're
coming to consensus so there's this idea
that you want to vote with a majority of
everyone
else what we see here is that the
timeliness constraint gives a lot of
power to the to the next proposal right
since they are the one who decides
whether this timeliness constraint will
be uh achieved by the testers that gives
them the tool to to make this credible
threat of saying that yeah I know you
want to be timely uh so if you don't go
my way I'm going to to screw with your
with your
rewards and so how can we try to to make
that um yeah less dependent on them
here's the strowman ID we could say you
know we could relinquish this timeliness
thing and say the vote of the attester
could uh be included on chain at any
point in time so that would work that
would remove the Reliance on the next
proposer as the ultimate includer of the
of the ATT testers we do really care
about knowing the timeliness of the
votes like we want people to give us our
view quickly and so as protocol designer
we also do need the attester to do a
good job and to do that job as uh timely
as possible and if we allow any proposer
to include them then we don't know
exactly when the attester votes would
have been um issued so a solution to
that is to have the next ATT testers
vote on the timeliness of the of the
current attester so instead of having
the timeliness property be only decided
by the next proposer we can have a full
set of attester voting on the full set
of a tester so essentially there's um
this group which is the group of the
same people that's like keeping each
other uh in check and what we achieve
via this is decentralizing the role of
the next proposal so making such that
the next proposer is not the only one uh
who is um responsible for the for the
timely
inclusion so we achiev that by proposing
this uh new mechanism which we call Dag
based votes uh it's quite simple so the
ATT testers at slot T issue their votes
as they do today so their votes
containing the head votes for lmd ghost
source and target for FFG uh and then
the ATT testers of slot t+ one will
issue votes on votes so the t+1 ATT
testers issue an object that says I have
seen the votes from the following ATT
testers blah blah blah blah blah um that
gives you this dag it's really like a
yeah twostep dag um and yeah so that
gives you the dag and what we say next
is that the dag votes so the ones on the
on the right column uh the evidence can
be included at any time and so now even
if we don't have time inclusion of the
evidence if the evidence tells us that
the attestor vote was timely we know
that it was that it was timely and this
is actually pretty nice because uh these
votes have this evidence being able to
be included at any time means that uh
the rewards can also be given at any
time even if the yeah in if the vote was
was timely whereas today uh if the
proposer misses their block the ATT
testers that were not included in this
block that was missed uh lose their
reward and what we really want is to
ensure that the ATT testers are fairly
rewarded for their work again in the
spirit of um keeping this attester layer
as secure and decentralized as as
possible so a quick note on performance
obviously these dag votes are a new
object uh we can use the aggregation of
signatures to make it a bit lighter but
that does create overhead still uh you
have to write these objects on chain so
that takes space you have to communicate
these objects on the gossip layer that
creates communication overhead uh but
there are a few ways that we might tell
ourselves okay in the average case this
is still potentially a good thing to
have so in the good case where the
proposer is honest and includes all of
the votes in a sense the evidence is not
required like we already have proof of
the timeliness and proof of the
inclusion so the D votes uh we don't
even need to have them uh on chain if
the proposal is missing or doesn't
include everything then you need to have
these dag votes and you need to have
more of them the more let's say
dishonest the proposer is and doesn't
include uh the votes in the worst case
you have you can have a pretty large
object like this evidence can get large
but we think it's still reasonable if
this is something that uh doesn't happen
too often so you can think of it as
insurance it's something that most of
the time you don't need and once in a
while it comes in handy to to have in
your back pocket and it can also serve
as a as deterrence against these these
attacks happening but there's more on
this uh in the paper as
well uh yeah that's it I made it four
minutes to uh to go but uh thank you for
listening check out uh most of our work
on our website and find our paper on
archive as
well so if you all have any questions
you can just scan the QR code and um and
write your questions in um the first one
which I'm going to read out so that even
the virtual audience can uh follow along
how much are the profit and the costs of
attack yeah so the so let's say the
revenue of the attack uh if I can pull
it off as the malicious proposal there's
two things I get so first I get
essentially the me of The Proposal that
I Reed because I'll be the one including
their transactions uh and and capturing
some of the m so I will take that from
the previous proposal and I will also be
able to get the source and Target
rewards from the ATT testers who were
not included by the by The reor Proposal
so yeah to make it simple in the
attester votes there's like these three
things that they vote on head source and
Target the head has to do with the lmd
ghost source and target with FFG the
head has to be included immediately but
the source and Target can be included
over many slots and the proposer that
includes them first gets rewarded for it
so if I manage to reor the proposal
before me uh I essentially get these
source and Target rewards from them
where they should have got them so yeah
that's the two revenues I get then the
cost of the attack is actually only the
cost of deploying the smart contract so
it can be pretty small I can even maybe
not deploy it on ethereum I could deploy
it on some roller or something that's um
even cheaper or another chain if the CR
if yeah if the if the if eum State rout
can be uh verified there so so yeah the
cost is pretty minimal the revenue can
be pretty high I think we give some uh
estimates in the paper let's say the m
per block is $100 something like this
that's what you would get extra as a
proposer and I think about $50 for the
vote so maybe yeah
$150 uh do you have some idea how often
we would expect dag votes to be
required um yeah so today uh many slots
are not missed I think the missed slot
rate is something like 2% so that's when
we would need them the most most of the
atest stations are included on time like
things are pretty tight so I don't think
we would need them that
much yeah so most likely not a lot and
also uh again in the spirit of this
works as a deterrent even less if we
have this mechanism in presence so so
yes we commit to have this mechanism
that's potentially pretty heavy and that
leads us to using it less than than we
need
to uh the other question we have is how
might an attacker threaten the
testers uh so they don't need to
directly threaten it so the attacker
just needs to deploy the smart contract
and ensure that the ATT testers know
about it
uh I think in the paper we discuss what
happens if some of the ATT testers are
just oblivious like they don't know that
this is happening and they don't um yeah
they they just don't know that the
attacker is trying to uh to hijack them
um so yeah simply deploying the smart
contract and telling the ATT testers
that the smart contract is there uh is
sufficient for for the attack to to
happen and um the last question is that
is this compatible with the beam chain
plan yeah that's
I I was reading in a group chat that
everybody's getting a beam chain
question so I guess that's mine uh yeah
it is compatible but maybe like to say I
mean yeah it's obviously compatible
because it's what I what I'm suggesting
here is a is a pretty small change not
small but yeah it's a change to the
consens rewards maybe to broaden the
picture here so the idea of beam chain
is to to essentially go to like this
single SL finality uh which is a little
different from the current consens
mechanism we have which is Gasper
but I think there's a lot of intuition
and mechanisms that kind of need to
extend to this so if we have single s
finality we have obviously like a a
different um let's say rhythm in the
chain like we finalize more often so
things need to be even more tight so I
don't know maybe yeah maybe once we
think more specifically about the
rewards for for ssf like we realize that
such things are are helpful I think they
should be helpful again this idea of the
ATT testers checking the work of other
ATT testers I think is is an intuition
that seems to reappear quite often so I
would say will reappear for ssf as
well uh we have two more questions which
just came in uh given the attester set
per slot is set at the start of epoch
should we be concerned the main risk to
proposers uh griefing the block example
folk the last slot of previous block to
find the prefer
Set uh okay let me think about this one
because the main
risk not sure I'm getting right I
see so yeah so v test sets are decided
quite in advance like not just uh in the
slot before the one that you're
proposing the schedule of ATT testing is
decided by Rand which is decided
essentially in the epoch previous to the
current Epoch so I think it's actually
pretty difficult to to do an attack
where you try to find the most favorable
attester set for for you as a proposer
there are some thinking around okay if I
can change the last slot of an Epoch
then I can bias the Rend a little bit
but I think it's yeah it seems somewhat
difficult to pull off in
practice and the other question is uh to
talk more about insurance and whether
transactions have some amount of
Economic Security before
finalization right so Economic Security
I would Define strictly as finalization
so whenever you finalize you have the
amount of stake that was involved in the
finalization as economic security behind
the the transaction but doesn't mean you
don't have anything when the transaction
gets on chain the more ATT testers are
voting on the Block block uh in which
the transaction was included and the
longer the chain gets that's built on
the Block where your transaction is the
more you have confirmation so we have
this work on confirmation rules uh which
tells you yeah almost like a level of
confidence that you can have uh before
you get to the to the finalization but
until I think until you finalize you you
have zero Economic Security in uh in in
that sense is how I would Define it for
for myself I think that's that's a clear
mental
model uh and the and the other question
we've got is how tag votes distinct
attestors who deliberately delay their
vote if there is no timing
reward uh yeah so if if I'm an attester
and I delay my vote uh the dag vote
evidence will say babe was not around to
vote he will say yeah that vote is not
part of the of the evidence so if I as
an attester delay my vote uh the
evidence will prove to the rest of the
network that I was late to to do my
duties so I won't be getting the reward
so so it it is resistant to
that great like really meaty questions
and a really meaty presentation thank
you so let's give up a round of applause
Babi so we're going to reconvene in
about 7 minutes at 300 p.m.
uh this is
the last two talks of the day and then
we'll have the closing ceremony so just
like you know freshen yourselves and
like stretch a little bit and get the
blood pumping before the next two
sessions
um so everyone should take a deep breath
in because our next speaker is
absolutely lovely and she's going to
take our breaths away um give it up for
maram who's a mechanism design
researcher at ritual who's going to talk
about agentic versus automated block
building come on
up well thanks for the intro sorry for
rugging uh changed the title and the
content isn't that different but this
was more exciting um cool so um I'm
Mariam I work with ritual uh this is
based on joint work with naven uh also
at ritual and
Columbia so let's get into it okay so
one mental model for uh what blockchains
do for us is providing this
fundamentally new uh primitive uh which
is permissionless verify viable
computation on a shared Global State and
this computation is sold in these
indivisible units called
blocks so you can think of that as a
supply side of this exciting New
Market and on the demand side we have
users who want to use this comp
computation um so this is all the apps
all the people whose uh happiness and
Welfare we care about and we want to
onboard and naturally we need a fair fee
Market to sit between these two sides
supply and demand and ideally uh figure
out how to allocate Supply to demand and
how to price things in an efficient
way and everything would be great uh if
the picture was just these two sides but
there's a third set of participants in
the system called agents or what I will
call agents and these are not users or
the computation providers uh they are
facilitators of the market but the role
is pretty complicated they can be useful
they can be adversarial and I argue
they're necessary and the reason they're
necessary is that to get the
permissionless verifiable all these like
new properties of blockchains we need
the centralization and that means we
need to distribute power to like
geographically and across nodes and that
means every part of the blockchain
including its fee Market might be run by
a selfish party with its own objectives
so we need to design markets with um
these agents in
mind so this a nice diagram by froner it
shows just how complex the ecosystem of
Agents involved in Block building is
they have specialized they have uh into
like little parts of the
market and um yeah like have a mixed
influence I would say on the quality of
um user experience
and I guess this is kind of at the core
of what meev is um these agents have a
different set of objectives than the
network or
users all right cool so here's a
narrative that I think is pretty
prevalent and it's that agents are bad
and MV is toxic so I will just outline
the narrative um I think it will be
familiar um so these agents have their
own objectives they have outsize control
over block production and as a result I
guess first let me show you the outsize
control this is I took this maybe an
hour ago um the most recent ethereum
blocks are built by two Builders um
that's not fully
decentralized and because of this
potential incentive misalignment between
agents and users user welfare can suffer
and this is a an old tale that has been
told many times I will mention this
paper that um we kind of formalized this
the the challenges posed by this
incentive misalignments where we show an
impossibility of Designing any like no
matter how clever you are you can't
design a good market so that this
incentive misalignment doesn't cause
issues the user welfare will always
suffer okay so in response to the evil
agents and bad meev people have um taken
some approaches to
um reduce or mitigate or democratize me
where reduction is at the app layer
let's make new applications let's use
bat auctions um instead of like the amm
we use now just to have less me less
value available on chain for these block
producers to extract um mitigation is
things like encrypted M Pools sve this
is where you tie the hands of the agents
limit their power so that they don't
have that much leeway to extract value
and democratization is kind of throwing
your hands in the air and saying this
evil is inevitable it will be there
because there is this degree of Freedom
these agents have so at least let's try
to reduces negative side effects let's
make sure we don't get
censorship uh let's make sure that at
least the validators validators are
decentralized so I think this is kind of
um the lay of the land
and what I hope to do here is give some
form of a counterbalancing argument I'm
not going to say agents are amazing and
there is no Meb issue but I'm hoping to
argue that agents can be useful and
sometimes crucial to use and me is more
nuanced than just toxic and
evil and I guess more concretely I will
give a framework I will Define this
concept of aenis M and we can give a
framework for how to talk about the
degree of agentic ism in different block
production paradigms and then follow up
with a way of reasoning about for a
specific application or chain how do you
choose which block production Paradigm
to use more agentic or less
agentic cool let's get into definitions
um so automated is something I haven't
mentioned I'm using that as the opposite
of aent
so let me Define what it means to be uh
an automated block building um function
or Paradigm you have users they insert
transactions into a me poool called M
this m poool then there is some function
that looks at the menol and generates a
block as simple as that so there is some
let's say even deterministic function
that goes from the men pool to what the
final block will be the point is there
are no agents in this slide at all no
one has power over what goes into the
block so an allocation is automated if
it takes this format it's a function of
the me pool okay so agentic block
building we have this second category of
Agents they also give an input to this
allocation rule and their input is
abstractly defined here as a vector of
actions they're sophisticated their
actions can be complex and the point is
that this function now depends on the of
the agents this is very abstract not
very useful but the point is that
depending on the structure of this
function agents can exercise more or
less power over the output that is the
block so let me now Define what it means
to be agentic it's defined as a relation
we say an allocation rule f is more
agentic than an allocation rule G if um
I guess maybe the picture is more useful
if the set of blocks that agents can
generate just the range of blocks that
they can generate is a super set of the
range of blocks of the less agentic one
so this is saying G is less agentic
because if um the agents collude
together and range over all possible
action vectors the set of blocks that
they can generate is limited it's a
smaller
set good so that's um and the definition
of agentic and automated it and
naturally there's a spectrum from
agentic to automated it so let's throw
some example projects onto this I will
throw some acronyms don't worry if you
don't recognize them the hope is that if
you do recognize any of them hopefully
it will help you understand how the
Spectrum works but it's not important if
you don't recognize them so at the very
agentic end I've put in Bitcoin and
salana and why do I what let me
the way the Bitcoin fee Market Works in
case you don't know it's a first price
auction transactions submit bids if
they're included they pay that bid there
is no restriction on what the minor can
include in the Block it's agentic
because it's just not restrictive the
set of blocks that the minor is able to
create is just all valid blocks salana
similarly doesn't have any like the
protocol doesn't impose any restrictions
on what blocks are
valid and ethereum I think is very close
to the agentic end uh it's almost a
subtle Point why a559 is slightly to the
right because currently a valid block is
not allowed to include a transaction
with a bid lower than the base fee so
that is some form of restriction maybe a
block producer wants to include a maybe
like there is me in a transaction they
want to include a transaction and
subsidize its bids that is not allowed
right now so Mev boost a lot of the
block production pipeline in uh ethereum
is very agentic get M out then figure
out how to democratize and distribute
it all right so I think the shared
sequencing marketplaces also like
espresso take a very agentic approach um
let's Outsource this to a market of
complex agents and um yeah hope and
sequence that way all right on the other
end of the spectrum um automated block
building there's ordering rules that are
enforced by a combination of consensus
cryptography and trusted Hardware so for
example chain links Fair sequencing
service it's the first com first serve
service it's kind of dictating The
Ordering of transactions most L2
sequencers are this way swav Prof are uh
use cryptography to encrypt them M Pool
and then um enforce a specific ordering
these are fairly automated there isn't
that much room for um block production
um markets there isn't that much
Freedom okay I've put fossil and braid
in the middle I think these are somewhat
restrictive of what the block producer
can do so in fossil there is a committee
that enforces a template on some
fraction of the block and what it can
include EMB braid the power of any
specific proposer is limited um so both
of these are they they're still a market
agents altogether can uh affect the
outcome or like the block that is
produced but they can't produce any
block they want
cool so how do we choose the right place
on the Spectrum for our specific app and
to do that we need to Define benchmarks
uh so what do we care
about these are some properties that
people like in fee markets none of them
is new low latency is pretty obvious you
want fast turnaround times uh
tractability uh this is maybe less often
cited as a property that we need but if
we have an automated
um rule if it's requires solving very
complex MP hard problems we can't run
that on chain so it is crucial that um
the auction itself is computationally
tractable to
run simple ux is capturing a bunch of
things but roughly speaking we don't
want users to have to do very complex
stratz to participate in the mechanism
um and then there are these two points
that are addressing efficiency one of
them is Surplus maximization and if you
remember the first slide was supply and
demand um there is gains from trade the
possibility of generating Surplus by
matching supply and demand effectively
and ideally we want to create the most
Surplus possible and simultaneously to
be efficient we don't want extraction so
users are the people whose uh utility
and Welfare we care about agents are not
so we don't want all of the Surplus to
go to agents and if we're not careful
with Market design the Surplus will go
agents and I guess let me highlight the
fact that the these two are they
interact in a subtle way they're kind of
a dual objective both trying to Target
welfare and the tension between them is
at the core of when you use a gentic
versus automated block building and the
reason is that sometimes one end of the
spectrum is really good at maximizing
Surplus but at the same time it will be
extractive so you have to figure out how
to trade these two off based on your
application so I have some time left I
will go through two specific dii based
examples and use them to highlight the
trade-offs between the two ends of the
spectrum the first one is front running
if you're not familiar I'll quickly
explain what it means um there's a user
wanting to buy eth on uni this is the
current eth price is 3200 USD
usdc and um the User submitted this
transaction to a public men pool an
agent sees that transaction and puts a
sandwiches it with a Buy on the left and
the cell on the right and the effect of
that is that the first agent transaction
drives off the price of e on uni then
the user transaction happens at a worse
price and then immediately the agent can
turn around sell the same amount of
eth basically make $300 a profit at the
cost of $300 loss to the user this is a
perfect example of purely extractive me
it's a zero SU game between the user and
the agents this is the kind of M we want
to get rid of avoid as much as
possible okay so should be pretty clear
that agents will extract this m so
agentic block building will be bad at
this um whereas automated will be pretty
good at this the design principle of
Prof for swav and these Inc the mols
were exactly to mitigate this maybe if
we hide the direction and size of the
order we will like leak less information
and there is less front running and
sandwiching happening okay so the second
example is arbitrage between a
centralized exchange and a decentralized
exchange again I'll kind of defined it
quickly
um basically you have um you can have an
asset pair again ether and usdc or USD
trading on two different exchanges in
this case binance a centralized exchange
and Unis Swap and so block times are
discreet uh centralized exchanges are
not they operate continuously with wall
clock time so here the orange line is
the price uh on binance and the red line
is the price on uni basically the price
was as of the previous block 3200
nothing has happened since because this
is the deadline for the next block and
there can be a discrepancy a gap between
the prices on the two
exchanges so what an agent can do is for
example at this point in this slot
observe that oh the price is lower on
uni higher on binance I can inject a
transaction on chain to buy East and
sell on binance and collect a profit
simple and I guess first of all Why is
good I'm arguing there is possibility
for generating Surplus this arbitragers
are providing a service and it's the
reason is the same reason markets being
efficient is good right you want the
markets can be viewed as an A and a
venue for aggregating information and
you want prices to be uh reflecting the
true value of um assets and so for the
health of the market it's good that the
price on uni is reflecting the price on
binance and they're all reflecting the
overall Market sentiment and everyone's
information but um at the same time
there is a possibility for extraction so
this person is making money where does
the money come from you can't print it
uh there are liquidity providers on
uniso and this is coming kind of at the
at a cost to them uh I won't be able to
like fully Define this but this is what
lever loss versus rebalancing refers to
and I chose this example because it
shows the tradeoff between the two
welfare objectives um you yeah like you
can't simultaneously satisfy both of
them at
once and yeah there's a tension between
them okay and maybe one other
observation here is that to successfully
run this trade it's important that this
agent knows that they will be the block
producer so remember in this step the
selling on binance I can do at any time
the buying on eth in the middle of the
slot I'm not sure necessarily that I
will be able to do this side of the
trade and if I can't do it if I'm
uncertain about that uh there are a lot
of costs I will pay in fact like my this
trade is negative EV it's bad for me so
the more uncertainty arbitragers have
about their ability to do both legs of
the trade the less willing they are to
do it they will require higher margins
larger art
bounds then the price between uni and
binance will deviate more and more that
is less uh accurate pricing that's less
Surplus and that's
bad okay so this observation um I want
to highlight and ask you to remember
because it will be relevant to the next
slide um I am short on time so let me
maybe pick
a specific point to
make
um okay so let me focus on this point um
so the claim here is that automated
block building will not be able to get
Surplus
maximization and be computationally
tractable and here let's consider a
specific way of automating block
building based on priority or ordering
there's this nice post about why this is
a pretty good idea um so the way this
works is every transaction comes with a
single bid you order transactions in
decreasing order of bids and that that's
all it is and the hope is that this will
be efficient but as this post also
points out this scheme is vulnerable to
reversions the issue is that if
coordination has to happen through the M
poool instead of of by delegating fully
to an agent who has full control and
knows for certain that they will be in
charge of this block and they can for
sure do all legs of the trade there is
some risk that these people don't know
for sure whether their trades will go
through uh there is some loss efficiency
loss because of that I think I'm about
out of time so let me skip to the
conclusion I've introduced aism outlined
the spec between agentic and automated
block building roughly speaking
automated block building is good with
respect to latency there isn't there
are't a lot of parties that have to
communicate uh and also generally
it's there's less
extraction but they might not be optimal
they might not uh generate the most
economic value so what's an application
where we should opt for automation for
if you want nison chain you want low
latency you don't want front running you
should be more and more automated agents
on the other hand are very good for
maximizing Surplus especially when the
user preferences are complex but they
will be selfishly trying to extract as
much of the Surplus as they can and one
example of where a aism is good is um
ritual uh the ritual resonance is a
Marketplace we designed for AI
computation the setting is nodes and AI
queries all have very complex
preferences and there's a because this
allocation problem is very hard uh
because it's a large complex matching
problem so there's a lot of potential
for generating Surplus and there isn't
that much toxicity or defi activity
going on so perfect example for being
very agentic and that's the end of the
spectrum that we were on and defit is
coming out today so check it out all
right thank you for
listening my
me um thanks a lot for that talk super
detailed and um and and gets into like
nuances and also like the examples were
good you can scan the QR code for your
questions and let's quickly get to them
talking about Surplus maximization and
decreasing extraction how do we draw the
line between a user and an agent what
determines whether we think of an
extracting entity as a user or agent
that's a very very good question is
exactly the trade-off I was trying to
highlight um I think it's an art not as
science um for example in the SE
Arbitrage example if we want to think of
the liquidity providers as users as
welfare we care about it's a different
story than if we just care about the
Traders and how accurate the price is
for them so I think what happens is for
a specific application you um try to
decide just draw a boundary that uh
includes the people who whose welfare
and utility you care about the most and
yeah so you draw the line based on uh
the purpose of your application
right um the other question will Jared
from Subway be out of a job with
automated block building um no comments
uh uh can you talk about the resources
the ritual is selling and what
preferences the users might Express over
there yeah so uh ritual selling uh AI
inference uh basically but it could be
different AI models and there are nodes
that are very heterogeneous so they have
different resources CPU GPU uh bandwidth
um it's very high dimensional so much so
that it didn't make sense to design a
specific multi-dimensional fee Market
it's just too many dimensions um and
users have
uh infer queries and ritual is providing
this or this Marketplace to match
queries to nodes uh and the preferences
can be as complicated as a user might
have privacy concerns so it might want
uh an MPC containing a set of nodes to
run its inference uh a user might have
uh latency concerns where I'm patient
I'm willing to wait a while or not and
all of these preferences should be able
to be handled um why is it bad for
automated strategies to give up on
Surplus maximization in the front
running example the Surplus capture
appeared to be bad for user welfare yes
I would argue in the front running
example there was no Surplus generated
it was a zero sum game um it was
basically a transfer from the user to uh
the agent so in many extractive Zero Sum
examples uh it's just not good to have
agents but uh a good example of a GU
Surplus is maybe in the case of ritual I
describe these very heterogeneous um
nodes and users and if you write any
piece of code to try to match these
together the problem of optimally
matching them is just MP hard hard to
approximate as well so doing that on
chain will lose out on the efficiency
you could get by having a more
sophisticated agent find a better
allocation I hope that answered the
question uh seems a very L1 problem do
L2 solve this by running a centralized
sequence I think it's um not just an L1
problem I guess like if an L2 runs a
central sequencer that is committing to
a first come first serve ordering they
are choosing a very automated approach
they are potentially missing out on uh
complementarities between transactions
or
like so yeah I think it applies to other
layers too and the last question what
sort of support or major changes do you
expect from the chain or the
foundation um I don't know that this
applies to me is it ethereum chain or
Foundation um yeah I don't understand
the question okay yep
yeah and the last one if you want to
comment I didn't mean to uh someone was
offended by my introduction so apologies
for that didn't mean anything I didn't
think anything was wrong but thank
you yep let's give a round of applause
TR
the e
so we are finally at the last talk for
the me room uh it's actually a very
special friend uh one of the first
people I knew in crypto uh William
George or big brain George as he's
sometimes called by the people in claros
uh he's going to talk about how we can
use oracles for when we need a specific
number or when we need to compute it so
come on up Jo yeah
okay hey everybody uh so I'm going to
talk about oracles for number values uh
my name is William George I work for the
claros Cooperative uh so what do I what
what's like what are we GNA what's the
goal here like the district called the
basic blockchain Oracle problem you
probably all heard about many times uh
blockchains don't have access to
information about the offchain world if
you want them to know something about
the off world you have to tell them that
information uh a classic examples you
might want an oracle for for prices of
defi of of like aets for defi contracts
uh you might want other kinds of uh
mechanisms to bring offchain information
onto the chain maybe the amount of
rainfall on some given location for some
Farm insurance contract the mechanism
used to do this is called an oracle uh
and uh sometimes the thing you want the
Oracle to Output is a number often in
the case of price oracles uh just to
give a bit of my motivation and like
sort of how and why I'm thinking about
this problem so for those of you who
aren't familiar claros is a
blockchainbased dispute resolution
platform imagine Alice the small
business owner hires Bob as the
freelancer uh to provide her some
service build her website whatever she
puts Bob's payment in some smart
contract escrow and if Alice is happy
with Bob's work she just clicks a button
and it's released if Alice is unhappy uh
then she raises a dispute that means
that there's like some crowd of users of
the Claris platform a few of whom are
drawn and they decide who is right uh
and the right answer to this dispute the
correct resolution uh may be a number uh
it may be some kind of partial
settlement how much should Bob be paid
uh if you have some kind of
decentralized insurance contract you
might have disputes about how much of a
compensation someone should get uh and
then basically you have this offchain
question you know like the answer to
this offchain dispute and you want this
like Oracle that's specialized in
dispute resolution and notice that these
questions can be you know more
subjective more maybe individual than
the kind of price Oracle question uh and
as a result maybe your like Oracle
design might be slightly different for
these slightly different questions
okay so now like digging really deep uh
how how should we design an oracle what
are like the basic ingredients going to
an oracle uh well on just like a
fundamental level you would ask who is
participating in the Oracle uh obviously
you're bringing information from the
offchain world onto the chain somebody's
got to be uploading that information who
what is the format of the information
they provide and assuming you have more
than one person who's providing
information how do you aggregate their
information if they don't provide
exactly the same thing how do you put it
together into some kind of collective uh
value that you use as the number in your
in your system and people probably
aren't doing this altruistically they're
so are they what's what's in it for them
like are they being rewarded or
penalized
somehow uh and as one makes these
choices what are you trying to optimize
you for well obviously you want the
Oracle to produce good information fast
cheap uh you want it to be attack
resistant uh to whatever attacks are
sort of relevant for your system I'm
going to talk about different choices
people have made on these and these
design choices uh over time where some
of the open like ideas are and like the
attacks can vary from one idea to the
other I I hit on a few uh and so far all
of this is relevant like everything I've
said could be true for oracles whether
they're outputting number values or not
uh I could have some discret information
uh that all everything I've said so far
would be relevant for and where you
really get into the number question what
the specifics of the number question uh
is this question of how precise you want
your information to be uh how many
decimals um and this is very relevant
for incentive functions if you have
people rewarding people to participate
in your Oracle uh say you want a price
Oracle and the you know you you say tell
me the price and of like Ethan USD and I
say you know the price is like $3,200
more or less and I say
should I be penalized uh so this
question of like you know for for a
number you can always have a more
precise closer answer and there's this
question of how close you need to be uh
and over the course of the talk we'll
hit on a few different Notions of close
uh that you can build into different
kinds of incentive functions like maybe
the most basic one would be to say okay
you need to be within x per of the of
the output value 1% you're rewarded
Beyond 1% you're you're penalized uh and
that's that's a simple thing you could
do there will be other ideas that I
people have
done okay uh now to hit on you know the
sort of next ingredient that goes into
your Oracle uh this question of vote
information and aggregation uh so again
I I think a lot spent a lot of time
thinking about dispute resolution for
the claros platform sometimes the
disputes have binary answers uh or
discret answers that are non-binary uh
and as a result I spent a lot of time in
research thinking about how you
aggregate kind of disc discrete
non-numeric answers together uh and this
draws from the field of social Choice
Theory frequently this like academic
field of how to design good voting
systems uh voting systems that handle
vote splitting well that don't have too
much tactical voting there's all kinds
of complicated questions when when
you're trying to Define find a voting
system I bring this up because in the
number case you have similar problems uh
that are you know they have their own
spin on on these kind of vote
aggregation questions uh in some sense
the questions get easier of how to
aggregate people's slightly different
information together because now if your
participants are submitting numbers
again you know maybe the question is
what is the price of Ethan USD and
everybody submits a number now you can
do number operations on those num
numbers you can take the average uh or
better yet you could take the median uh
so if you think of like the numbers
people provide to you like lining them
up from highest to lowest you take them
take the middle value that that's the
median and that's a particularly popular
choice for people that have done number
of oracles because it's resistant to
outlier effects uh if somebody puts some
like crazy extreme value that's not
going to affect the median too much so
in some sense this question of like vote
aggregation is easier than in the
discreet case but also there are
specific challenges like that that sort
of precision question I had from a slot
or two ago okay uh and now hitting back
the sort of last ingredient uh before I
get into the choices different projects
have made uh this question of who is
participating uh and I would argue that
there's like two basic models you could
have here maybe you can do some some
combination of the two uh but you can
have either a crowd model or a delegate
model uh with the idea and I would say
that there are like parallels here to uh
kind of different proof of stake systems
uh delegated proof of stake versus
something that's more like ethereum
style proof of stake uh so the question
is who is doing the thing who is
providing the information uh in in the
proof of in the proof of stake systems
and the consensus algorithms who is
producing blocks uh in an oracle
question who's producing like Oracle
values uh with the delegated model sort
of taking the point of view that like
you know these tasks are hard uh maybe
you want an oracle that produces like
Fast values very frequently you never
you want like zero downtime uh and to
have that kind of reliability you want
like a beefy institutional actor uh that
has uh you know like really high
performance Hardware somewhere and some
data center uh and thus you know maybe
it's not like appropriate for like
random people to be doing the task of
providing the Oracle information or
producing the blocks and the consensus
algorithm uh so instead you have them
vote on who you like on delegates who
then do the task for you uh and um you
know then the crowd model is the
opposite of that you know everybody's
doing the task I can get 32 E I can spin
up a validor I can I can be part of
proof of stake or in an oracle I can be
the P person that's providing values for
the for the Oracle uh and there are of
course pluses and minuses uh and the
crowd model uh you know if you have like
lots of people that are doing like a
task constantly that takes gas uh maybe
you know like normal Hardware they're
not like super fast as fast as an
Institutional actor in a delegated model
you know there's some risk that the
delegates could use their role sure they
can be voted out uh but you know in any
given question they're they're they're
delegated and you can mitigate that
somewhat by aggregating like a bunch of
delegates together uh so that you know
you'd have to have like some collusion
or something for them to corupt and
answer uh and now to sort of summarize
some of the different choices people
have made over time uh I'm going to
start with like the beginning of the
history of this problem uh which is a
blog post by vitalic back in 2014 called
he called shelling coin so this is the
dawn of ethereum this post was actually
a lot of the like one of the big
Inspirations for what became claros
ultimately uh and he was thinking about
this sort of like price or question
again uh where his proposal is okay I
have people that each submit a number of
value uh you output the median so far
that's kind of normal uh and then his uh
incentive function was that you reward
people in the 25 to 75% range so people
who have middle values are rewarded and
people who have extreme values are not
rewarded maybe they're
penalized uh he didn't explicitly say
who the participant should be uh he
assumed that you had some kind of simple
resistance tool so this could be either
delegated or crowd depending on exactly
what that resistance tool looks like but
you can certainly imagine like a crowd
version of this uh and now here note
that this like 25 70% rule uh now the
notion of being close to the answer
being rewarded uh close enough to be
rewarded is being closer than other
people not just close to the value but
like I have to beat out somebody else
everybody can be within 1% not everybody
can be within the middle 50 50
percentile uh so moving on in history uh
like the big Oracle provider at least
for Price Oracle now is chain link so
I'll I'll summarize what they do and how
that's kind of you know there's choices
evolved from from what Shing coin
proposed uh so here they have like a
Marketplace of nodes that provide Oracle
information those nodes are supposed to
take information from reliable sources
coin gecko Kao whatever uh and then a
given price feed has a bunch of nodes
that are sort of delegated into it uh
and you output the median of the
different nodes and those nodes are
rewarded for their payment for services
uh so in some sense this is crowd is uh
because there's this Marketplace
everybody can participate I to can spin
up a chain chain Lane uh node uh but in
practice uh it winds up being more like
a delegated system uh because any given
price feed has some some nod selected uh
and then if you want to get rid of them
that that goes back to this question of
like voting them out through a
governance process uh if I have like a
price fee that's used by a big defi
application like compound or something
like if one of the nodes does a bad job
then you correct that by going on the
compound forum and having a proposal
that looks kind of like this where
you're like please change the price feed
update and get rid of that
note um so now to like to like just wrap
up this question of like delegated
versus crowd uh here's a sort of partial
list of different projects over time and
there's kind of a spectrum you can be
sort of in the middle but like more or
less clustered into the two sides uh
maker had an internal price Oracle for
their their die stable coin uh and it's
older than anything else on this table
so like they had more of a delegated
model uh really all the price Oracle
things have this this delegated model
which is probably the only like
practical choice you could make at least
historically uh because if you want a
price Oracle that updates you know in
real time for defi applications you know
you can't have huge crowds of people
voting constantly the gas would be crazy
people aren't performant enough to do
that uh the stuff on the other side
that's more crowd uh claros and Uma you
know have more like individual one-off
cases involving human efforts so it's
not super important that people are up
to you know voting in real time uh Nest
has a sort of inter thing where um they
are specific to price oracles uh because
they use like an arbitration an
Arbitrage game uh to U as part of their
mechanism so it depends on being a price
Oracle okay now getting back to the
other questions aggregation functions
incentive functions uh which ultimately
comes down to what are the attacks if
I'm trying to manipulate the system like
what can I do and which systems are more
robust uh so an attack that was already
highlighted by vitalic in uh in his
shelling coin article is what he called
micro cheating it was this long quote
I'm not going to read the whole thing uh
but basically the idea is that you can
just nudge the value provide just a
little bit like you you know what the
true honor answer is but you as an
attacker you uh provide a value this say
slightly to one side whatever side you
want to nudge the Oracle uh and if
you're sophisticated maybe you stay
within the 25 to 75% range so you're not
even penalized uh and maybe you can move
the the output a bit uh to give a bit of
a more visual to this uh there's some
distribution of how honest people people
who are really trying will provide
answers some people are better at this
task than others uh so uh in the absence
of attackers it all kind of average out
uh here the the median answer is the the
spot on people uh but if I have an
attacker that has a few votes not even
like a majority the vot's only three out
of I think 12 or nine or something here
uh then by sort of going to one side you
know if they're like a sophisticated
actor that can anticipate the
distribution of the honest people's
votes uh they can kind of unwi ly wrap
the people that are confused and off to
one side into an attack Coalition
against their will uh they uh they can
take the like confused people to join
them together with the actual attack
votes and collectively they have a
majority that moves the uh the answer
from spoton to okay um and then as the
attacker gets more and more votes you
can drag the the like answer that much
more uh and if you think like you know
like algebraically how much can attacker
with K votes move the answer like this
well if your aggregation function is
taking the median uh then an attacker
with K votes can drag the result to the
distribution of honest participants so
this gives us a like a measure that to
judge okay this is the resistance of
median as an aggregation tool against
this kind of attack and then we can
compare that to like other attacks and
see which ones are more or less
resistant uh and a natural question is
it ever make sense to do anything other
than check the median uh like the median
seems like a really bu robust mechanism
like lots of projects have used this uh
and uh I would say probably not if your
voters only give you a single number uh
but if they give you multiple numbers
you can do something that's more
interesting uh and now uh getting to
kind of like research that I have done
uh I've thought a lot about uh how to uh
have voters provide intervals of
precision uh or now they provide you
some like lower and upper range where
they think the True Value lies uh and if
everybody sort of intervals overlap well
the answer should be somewhere in the
overlap uh if there's some point of
conflict uh where there's one interval
that's like the upper bound is strictly
less than the lower bound of some other
interval uh then they're like they
disagree uh and you can essentially have
the users vote on whether you're higher
or lower than a point of disagreement I
will sort of quickly go through this
because I don't have tons of time uh but
um you know you can think of if my upper
bound is less than the point of conflict
I vote less if it's my lower bound is
higher than the point of conflict I vote
higher uh and if my my interval just
contains the point of conflict well then
I didn't vote at all I gave you less
precise information everybody can vote
like this you can kind of resolve the
points of conflict and you can come up
with a collective answer so this is an
aggregation mechanism that isn't just
taking the Medan uh this is based on an
academic article I wrote with a
co-author Clon laange several years ago
at this point uh that was based on a
version of this that was slightly
different because at the time we wrote
this with um basically trying to be
compatible with claros V1 as it existed
at the time uh as of a few days ago
claros 2.0 has been launched uh which
has much more flexible mechanisms for
being able to encode things like this as
modules uh so now we have you know more
flexibility to do things like this in
the future um uh so how does that
aggregation mechanism I just proposed
how does it compare to taking the
meeting is it better or less attack
resistant uh without going too much into
the details I will just say that it kind
of depends on whether on your
distribution of the honest participants
uh like how they how they act uh B
particularly if people who are confused
know they're confused uh if people who
are like out on the edges of the
distribution or providing impr
information if they give you long
intervals because they they realized oh
I I'm I don't really know the answer to
this question uh then they uh then the
this sort of voting by intervals
performs better than just deing the
median uh if you have like a um like if
people that are wrong are really
convinced that they're like super
confident in being wrong uh then uh it
performs not as well um there's slight
effects either way but you know like
this is the sort of analysis you can do
of attack resistance for these different
systems um now that was all about the
aggregation rule you know even even
before you think about is the attack
going to be penalized or rewarded uh for
doing an attack or like how much are
they going to be penalized you know like
this is the sort of basic question of
how much can an attacker that's willing
to sacrifice some amount of money drag
the answer uh with some kind of minority
attack Coalition uh when you get back to
the incentive function there are all
kinds of Interest interesting questions
uh and getting getting back to this
question of how close do you need to be
rewarded uh ultimately every sort of
incentive role you come up with encodes
a notion of distance to say whether like
a given participant is close or not uh
and uh for the voting by intervals thing
I have this really complicated formula
that I use as an incentive rule uh at
least like tentatively uh that tries to
balance the fact that you want to
encourage people to submit really small
intervals uh which is the first term and
at the same time you want to encourage
people to be you want to like really
reward people if they vote on the right
sight side of the points of conflict uh
so that if there's like like a point
where the system could go a different
way and choose a different answer uh you
want to like raise the six on people so
that an attacker that winds up losing
like loses a lot of you know that much
more um so if anybody's interested in
that formula feel free to talk to me we
can we can dig into it uh and then like
the different metrics that people have
used uh just to summarize the three that
we've looked at so there's this notion
of being close if you're close to like
as a percentage of the output uh there
is a notion of being close if you're
closer than other people uh these are
different things and then there's that
crazy formulate from different page
which is about being on the right side
of points of conflict uh so sort of
being close when it matters and if like
everybody kind of agreed it doesn't
matter so much and the formula doesn't
care as much about whether you know how
you voted uh summarizing how different
projects have taken the different things
they've done on on on these choices uh
so so shelling coin and chain link like
the format of the vote is just a number
as such the only real reasonable
aggregation mechanism is just to take
the median uh for the interval approach
I have more complicated information that
means I can take more complicated
aggregation
rules um some projects I didn't talk
very much about uh other projects also
have you know that have vote vote
formats of numbers also take the median
P which is an interesting example they
also have something where you have
submit something that's kind of like
something like an interval uh they a
different aggregation mechanism uh and
um you know I just want to say there's a
lot of sort of room for experiments
here uh so concluding uh historically on
this like delegated to crowd model most
people have been interested in price
oracles if you want a price Oracle that
updates like really fast you probably
needed a price like a delegated model
particularly in like a high gas
environment maybe even in a low gas
environment just because you want people
to be able to provide information with
like very low lag time uh but as you
consider more bespoke questions
subjective questions that you might have
in a claros select platform that you
know now you open up this design space
and you get back to this question of
like digging in like what kind of
oracles can we design and it does it
make sense to go back to a crowd model
uh we've come up with measures to talk
about how micr cheating varies from one
sort of approach to another uh the
delegated approach it leaves its
incentives to just like the threat of
being thrown out of the platform so they
don't really have explicit incentive
rules uh but if you want a crowd model
you really have to think like what are
my what's my incentive role and there's
a lot of open interesting research there
so if you're interested in that you know
reach out uh and I'm happy to take
questions so we've got quite a few
questions streaming in um as a wider
variety of RWS get tokenized How
concerned are you that oracles become a
point of
failure yeah so
like the more things you have that like
that are integrated in like important
ways in your system the more attack
service you have uh you know if you have
real world assets that people are really
engaged with and they're providing
information you have lot of lots of
Watchers uh you know opior it shouldn't
be so bad but we definitely want to like
think about how rigorous our oracles are
uh how do crowd oracles typically
Implement Cil resistance yeah so I mean
it depends uh for claros in in claros
so there's a token that participants
have to have and you can't take over the
system unless you have you know a large
percentage of the tokens uh in claros
social mechanisms that like that token
mechanism is still there but also uh you
can use sort of proof of person tools
layered on top of that so and we've
we've had sort of interesting results
that I can point you to if you're
interested uh such that you can design a
system that where you both have to like
break the proof of personhood and break
the the token way to draw to like aot
mount a large scale Cil
attack um is there an actual objectively
right answer or truth for numbers or is
it something that's always subjective
like I would argue on some level uh if
you have like a discret question uh you
know you can you can talk like truly
about having a right answer uh that like
an answer that's better than any of the
other answers if you have a number
question uh you know people if you zoom
in enough can always disagree uh people
might say okay yeah we agree up to like
the you know thousand decimal place but
like in the 10,000 decimal place you
know I'm you know I'm right and you're
wrong uh so on some sense there's always
some amount of subjectivity in any kind
of Norm number
question um how do Oracle
implementations typically check that
they have a sufficient quum of
answers yeah so uh for the delegate
systems I mean like they have like some
some number of delegates that they think
is appropriate uh individual system
might have a quorum if in case there's
like some like big out
where like okay I have n delegates at
least four of them have to be online or
something so for you know when you have
like a small number of delegates uh it's
straightforward uh in a crowd system you
could build something like that in uh in
claros we don't have a quorum system
because there's an appeal process so if
for some reason like everybody was like
censored you know there was like an
outage it was like bad network
connectivity and nobody voted you can
just appeal and try again uh but but
certainly something to think about in
some systems yeah and it's and the last
one is a great question uh if I'm a
participant in the voting crowd what's
stopping me from just copying another
answer as my vote and essentially free
riding yeah so again this will depend on
on the system uh so in claros um like
there again there's this appeal
mechanism which gives people uh extra
rewards if they were on the right side
of a of an answer that is like where
they lost their voting round and
ultimately like appealed and they were
proven right by the by the appeal round
uh so that you know gives an incentive
to people to be contrarian if they think
that they're right uh other approaches
can be taken uh there
are like you you can use commit reveal
systems uh there's still questions if
you do that about like what happens if
someone pays you to reveal your vote
even if you know like the commit and
real system allows you to technically
hide your vote you reveal anyway uh
there are lots of interesting sort of
properly cryptographic questions there
uh but it's that's a that's like a
subject of research uh but there are
approaches so I might require a fact
check on this last question that poly
Market has a highly centralized Oracle
and seems to be the largest do you think
sentiment will drive crypto crypto
products to this model instead of
algorithmic is it a centralized Oracle
first I think they use z uh
so like like that's I think I I you know
like people can can fact check me I like
but uh I I believe they use a like a
crowd model uh so you know if people are
interested in that product uh then um
you know like there could be demand for
you know that much more
decentralization um you know it's you
know if some if something is takes off
people will have greater scrutiny of
course but in general what do you think
about centralized oracles versus
algorithmic or decentralized ones yeah
so I mean it sort of depends on what you
mean by centralized uh do you consider
like a delegated model like centralized
I mean it kind of depends you know it's
it's it's not a question of like
absolute centralization it's about who
has the power to do what uh if you have
just like a pure one actor is
responsible for providing you like the
truth uh you know you don't have a bunch
of delegates and you don't take the
media of their answers uh you don't have
a Marketplace to join or be Dro kicked
out as a delegate uh then yeah obviously
if you just have like one absolute
source of truth that's not necessarily
in the spirit of the ethos that we
have thanks yeah that was really good
and quick rapid fire questions as well
well appreciate it George
thank so with that we come to the end of
the me room uh we can now all like head
to the main stage where there's an event
till 6 and there's also a music and DJ
night after 6:00 so be sure to stay for
that as well and until then the next Dev
con yeah
e e
