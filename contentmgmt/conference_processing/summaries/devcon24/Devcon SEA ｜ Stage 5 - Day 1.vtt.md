[Music]
testing hello hello how's everyone doing
today
woo amazing amazing energy so my name is
Teresa very excited to be here for
moderating the layer 2 talk tracks for
today's event so we actually have a very
special guest from optimism today to
give the very first talk um he has a
very interesting title crypto Twitter is
wrong this is how rollups really work so
let's give the warmest Round of Applause
to Kelvin Fisher
okay where does this go all right click
um where are
we there we go okay oh wait wait wait
that's this that's a all right so um
I've been kind of ill the last couple of
days uh sitting on the toilet so if I
seem defeated and disheveled that's why
um but this isn't the first time I was
getting ill on this trip I've been in
Bangkok for about a month or in Thailand
um and the last time I was doing this I
started tweeting and getting really mad
at people on the internet and I realized
that I'm not the only one that needs to
get their [&nbsp;__&nbsp;] together uh we better
start agreeing on stuff or ethereum is
cooked so that's the new talk I'm going
to start this talk by telling you a
little story um you know it's December
canaval Florida and some NASA smart
cookies at Nasa are going to send a
Orbiter over to Mars right so they throw
that thing on the on the rocket and then
send it off wow yeah neat right great so
it's a long tense journey to n Mars this
whole thing takes like N9 months $500
million a bunch of people's entire lives
built into this thing goes all the way
to Mars and then it's finally time for
orbital insertion right so this is
what's supposed to happen right rocket
goes like this oh look it orbits Mars
right that's what we expect yeah that's
what we want but what actually happens
is this oh oh oh no it's way too low and
then bam you know
thing falls apart um the whole thing
slams into Mars's atmosphere Falls to
Pieces so why what happened what
happened to this thing well the smart
cookies at NASA went over to Lockheed
and they said hey Lockheed you know what
can you pass me that meter stick and
lockheed's like yeah and locked gives
the meter stick to NASA and NASA's like
hey Lockheed what this is a bleeping
yard stick it turns out that Lockheed
the whole time was building instruments
that were returning data in us customary
units why everyone would uses metric but
the moral of this story right oopsie
sorry the moral of the story is that
shared definitions make or break
projects if you don't agree on the words
that we're saying you're never going to
get anywhere and today while ethereum is
facing more competition than ever we're
wasting so much time talking past each
other we're all saying the same things
with different words and everyone hates
each other so I asked the internet on
Twitter what they think an L2 is is and
here are some of the responses I got an
L2 is a chain that settles to an L1 an
L2 is a cultural extension of
ethereum like Cutlery a layer two is a
function description not a specific
design or form and I give up on the
other definition let's just stop saying
L2 it's a
nightmare the reality is that we can't
build the future of ethereum if we keep
using these differing definitions we
can't do it unless we have shared clear
definitions shared clear definitions
allow us to see the whole picture right
and you can fill in the gaps if you're
building a puzzle what do you do you
build the frame first and then you fill
in the gaps right now we're building
ethereum by just putting puzzles in
random pieces and so we better start
writing a dictionary or we're going to
end up like the Mars
Orbiter so you know call it whatever you
want but I think we need to build this I
think we need to build the encyclopedia
e theia and I think we need to get on it
now um like any good dictionary the
first word in any encyclopedia is arvar
that's right and Arthur is an arvar I
don't know what doesn't look like an
arvar looks like a bear I don't think
that they should have called him an
arvar but whatever the next word is
rollup now why rollup well when I ask
people on Twitter what an L2 is nobody
could agree when I asked people what a
rollup was I actually got surprisingly
coherent answers and kind of the average
that I got was this a rollup is just a
normal blockchain that uses another
block blockchain for ordering and data
availability all right that's that so
let's kind of walk through it let's
explain this right blockchain 101 what
even is a blockchain right let's crack
open ethereum what is a blockchain well
it's composed of three main parts we
have state that's what the world of the
blockchain looks like we have
transactions that's how people change
the blockchain and we have the state
transition function which is the rules
by which a transaction actually modifies
the state
we have two properties that are really
important for any blockchain we have
ordering right now let's say that wizard
hat sends one e to Timmy and Timmy sends
one e to pretty hat person right that's
fine we know that that works but if we
swap the ordering and we say that the
first transaction happened second and
vice versa and Timmy tries to send one e
a pretty hat person well if we look at
the initial State we know that Timmy
didn't have any eth and so this doesn't
work right so ordering is really
important no ordering no blockchain data
availability is critical right what is
that well it's really just a fancy way
to say that you can actually download
the transactions if you can't download
the transactions and they fade away then
the whole blockchain Fades away right if
you if you can't execute the
transactions because you don't have them
in the first place you can't compute the
state no transactions no
blockchain all right so blockchains use
consensus mechanisms to establish
ordering and data availability and
there's an asterisk there but don't
worry about it but it basically works so
you know we know what a consensus
mechanism is we have Bitcoin right so
whoever has the most money and lights it
on fire wins that's proof of work we
have ethereum whoever has the most money
wins that's great very human love that
it's not plutocratic at all uh so these
futuristic systems are complicated and
costly and the reality is that they're
very difficult and expensive to build in
the first place I mean you try to build
ethereum's proof of stake from scratch
Good Luck then they're also challenging
to maintain so even if you didn't build
them in the first place just to run them
is really hard and I think this is
underappreciated but usually you need a
token to reward participants right
Bitcoin has Bitcoin eth has eth and the
reality is that a lot of people for a
lot of reasons don't want to make
tokens cool so rollups solve this
problem by Outsourcing consensus to
another blockchain right this is all
that a rollup really does
let's explain how a rollup works by just
giving an example so Timmy wants to send
a transaction what does Timmy do he
sticks the transaction into the me pool
on the rollup just like you would in
ethereum and then the validator or
sometimes the block producer and we call
it the sequencer sometimes uh takes that
transaction and shoves it into a block
with lots of other transactions and then
it puts on its little Timmy hat and it
grabs that
block and it goes over to the ethereum
men poool where it tosses the block into
an ethereum transaction puts the block
into the ethereum men poool gets picked
up by an ethereum block producer puts it
into a block right this is a bridge but
it gives you the basic idea validators
come in they say okay sign off looks
good take the block shove it into the
ethereum blockchain now if you open that
transaction back up there you go there's
your rollup block right and now there
might be older transactions that have
older rollup blocks and older
transactions that have older rollup
blocks and because all of these blocks
and the block data is just being shoved
into ethereum transactions you get all
of the the guarantees from ethereum
about ordering and data availability
about ethereum transactions right if you
know that ethereum transactions are
going to be ordered then you know that
if you put a rollup block into an
ethereum transaction it'll be ordered
too so to kind of recap that rollup is
just a normal blockchain that uses
another blockchain for ordering and data
availability right okay so if you've
watched this talk and you kind of have
some idea of what a rollup is then you
might be asking where does the ZK or
optimistic bit come in because we always
talk about ZK rollups and optimistic
rollups and and I never mention ZK or
optimistic stuff at all in that
description in order to understand this
we first have to talk about bridges
right what are Bridges well you've
probably used one before we kind of know
what they do right they're applications
they let you send tokens and data and
stuff between different blockchains how
do they actually work well all bridges
basically work the same way you have two
chains and then you stick two smart
contracts one on each chain right these
are two independent
chains and someone comes by Timmy comes
by and puts an eth or whatever into the
smart contract on the first chain and
then Timmy goes to the smart contract on
the other chain and says money please
and now the smart contract in the first
chain needs to think well how am I
actually going to verify what happened
on op mainnet the problem is that this
is a smart contract I mean if you were
going to do this you would probably just
run an OP main net node and it would
love to do this as well you could just
run a full op main net node inside of
the smart contract but it's a smart
contract it can't do that it's a
resource constrainted environment and
we're not able to actually verify the
full chain explicitly like this so
instead the smart contract asks for a
proof it asks for a succinct way to
verify the state on the other chain and
then Timmy comes up with a proof gives
it to the rollup or to the uh gives it
to the bridge smart contract and the
bridge smart contract takes a look at
that proof verifies it according to some
rules and then you know poops out some
eth on the other side right
so Timmy walks off and now you've
completed your Bridge transaction this
is generally the way that all bridges
work whether it's a multisig proof or an
optimistic proof or a ZK proof each time
what's happening is that a smart
contract is using some a bridged metric
to decide what's going on on the foreign
chain so what I want you to get out of
this is that proofs are things that
Bridges use rollups don't use proofs
Bridges use proofs right and this has
some really weird implications I really
want to want to have you internalize
this because it sort of means that this
word that we've been throwing around ZK
rollup or optimistic rollup doesn't make
a lot of sense because rollups use
proofs or rollup sorry rollups don't use
proofs Bridges use proofs right so if
it's the bridge if ZK or optimistic is a
descriptor of the bridge then why are we
applying that descriptor to the
rollup well where does this come from I
think that there's a lot of hisorical
context the answer thing is that
basically rollups think that bridges are
useful this is because it's useful to be
able to pull economic activity from one
chain to another and so rollup teams
build these official Bridges and these
Bridges because of the special
relationship between a rollup and its
parent chain can be these kind of
special bridges that are more secure
than Bridges between two arbitrary
chains now the fact that it's the rollup
teams that build these Bridges is just a
coincidence of the fact that the rollup
teams know the most about the thing but
there's nothing really stopping any
arbitrary person from building that
bridge because it's official and because
it is The Branding of the chain it
becomes naturally popular and when
people put more and more assets into
that bridge it gets more and more
influence over the social consensus of
the L2 if the L2 wants to Fork the
bridge has to agree right or all of
those assets on the bridge are not going
to be worth anything on the fork
chain so and then of course at the end
of the day the official Bridge has some
sort of proof system and the result is
that the rollup gets its name from That
official
Bridge all right so really to hammer at
home one last time proofs are things
that Bridges use rollups don't use
proofs Bridges
do so what what's the point of all this
well you know like I could I'm glad I'm
disheveled because I can look really
crazy when I'm saying this but
essentially all this stuff about ZK
rollups and optimistic rollups and there
being a war in fighting between all
these teams it's kind of fake news and
and we're just creating this tension
between teams for no good reason right
and the other thing is that ZK and
optimistic rollup is just really
terribly limiting if you think this way
you can't imagine new things like what
if there's a chain with two massive
Bridges at the same time and one's a ZK
and one's an optimistic Bridge what is
it a ZK rollup or an optimistic rollup
who knows what if it's a chain with no
bridge at all and then someone puts a
bridge on that chain but the person who
does that is just a random person person
what if there's a chain that posts
blocks to two other blockchains or if
there's a bridge with more than one
proof system all these things are things
that you can imagine if you're not
constrained in this
way so again at the end of the day
Vicken Stein good quote limits of my
language are the limits of my world and
the reality is that our language just
doesn't leave any room for novel
constructions when people want to build
something new they can't because they
don't have the language to do it and so
you're stuck with two really bad options
options and you can see this option
number one is you make up a completely
new term right so you first you get L1
L2 L3 optimistic rollup ZK rollup plasma
validium optimium volition Sovereign
rollup like no one knows what any of
this stuff is if I quizzed half of you
you'd all be wrong right no one knows
what this stuff is how am I supposed to
convince a user to use my product if
nobody knows what it is and the the
other option which if you have less
grupal you just do this you just co-opt
an existing term you take a term that
other people like like evm equivalence
or you know rollup or L2 or whatever and
you just decide that your chain is going
to have that too and because we don't
have good definitions everyone loses
right every single person loses teams
lose users lose the reality is that
everyone's confused and so our language
just isn't flexible enough for people to
be able to build these
things the end result of all this is
that no one's working together you know
how many times I've heard that quote
the fact that there's an I think in
front of that is insane what do you mean
I think we're all just building the same
CH same thing we should know if we're
all building the same thing right it
doesn't make any sense why are we doing
this to ourselves and we're doing it
because we don't have good shared
definitions so I was trying to figure
out you know a couple weeks ago I'm I'm
scaffolding these slides I'm trying to
figure out how to end this talk um and
then this thing happens and it kind of
fits perfectly with the rest of the talk
booster coming in hot for booster
[Applause]
catch booster fds is
safite 13 of those rapor engines and
this view is incredible right now I
can't wait for us to hear the sonic
boom your Landing burn start up
we can see those Chopsticks now this is
absolutely insane on the first hour of
attempt we have some
H super Happy
Booster Gilla has caught the
booster chip Power ninal Star has enter
the
atmosphere those people those people
share definitions all of them they all
agree on the same thing and if you're
ethere ethereum today can't do it but we
could right we could catch boosters we
could do
it whatever but we have to start working
together to create shared definitions if
we don't do this it's never going to
happen so please join me try to help
write the encyclopedia Thea we've got
two definitions right we've got roll up
in arvar that's a really good start um
and thank you please help formalize
stuff scan the QR code there's an empty
GitHub repo I'll add art to this later
on uh and I'll take any and all
questions thank you very much much
appreciated that was a great talk
Calvin all right so we have some great
questions over here let's go through the
first one wow very interesting is
lasagna layer
too I mean if if your lasagna has two
layers I don't think it's very good
lasagna let's put it that way uh is a
croissant a croissant a
rollup yeah why not what I mean it might
as well be like that's you could ask
someone on Twitter they' say yeah um can
we see the rocket launch again I feel
like it might take up too much time but
I'll send you the video afterwards if
you come to
me all right so I'm going to mark this
as answered what about croissant is that
a rollup cuz we do have one vote over
here um is a wait which one is a ciss
rollup yes a ciss is a rollup yeah um
what are some other terms and Concepts
that need to finding that's a really
good question I think L2 is a hopeless
term so let's not bother with that one
at first but things like Bridge is a
really easy thing to define the stages
for rollups right stage zero stage one
stage two I think those things can be
defined very very well and that would
help a lot of people
um and kind of just I mean honestly at
the end of the day more than defining
new terms I'd like for the ecosystem to
start throwing away terms and redefining
things like Sovereign rollup or validium
or whatever in terms of these simpler
things that we can all agree
on cool and when these questions guys
when will I be bleaching my hair again I
don't know I mean today I guess yes why
not great I'll bleach my hair today and
I'll whatever why
not what are some other terms and
Concepts that we talked about that
rollups don't use proofs Bridges use
proofs but rollups use Bridges right
without a bridge what distinguishes a
rollup from a foreign chain well all
chains use Bridges right the fact that
we have Bridges is not unique to rollups
the unique thing about rollups is that
it allows you to build a special type of
bridge that has better security property
than if you just had two completely
unrelated chains um but the fact that
that's true doesn't mean that that
bridge has to be built by the same
people that built the rollup and it
doesn't mean that you can only have one
of these and you don't even have to have
any of them if you don't
want um since rollups Outsource
consensus does it mean that
decentralizing the rollup doesn't make
sense uh this is kind of a contentious
topic I would say that the correct
answer here is that decentralizing the
rollup means a different thing than it
would on the layer one uh because you
have most of your security properties
even if you have a
centralized you know block producer
centralized sequencer you don't lose
liveness right because you can do this
special thing between the rollup and the
parent chain and you don't lose safety
and so this is generally why doing stuff
like decentralizing the sequencer has
been relatively low on the priority list
of a lot of R rollup teams because you
have very good security properties and
you don't really lose much except for
this kind of short-term liveness now
eventually short-term liveness will
become the most critical part uh but
usually focusing time and effort on the
bridges and making those bridges robust
takes up more time for
people all right I guess we have a few
more minutes for one more question um
how does sharding fit into this it's
what I do on the toilet all
day um how does sharding fit into this I
don't know I this is such a confusing
question I could spend a whole minute
working on it um I'm gonna skip that one
perfect let's mark all right we can
leave it there yeah great all right
great thank you
K thank you
uh so for those of you are leaving thank
you for coming and for those of you who
are staying are next talk will start at
for
y
three two one all right you can go help
all right so time for our next talk for
today our next speaker represents a
company that has been at the Forefront
of privacy in blockchain I actually hold
great respect for their commitment to
advancing privacy in the space um
powered by incredible team of
cryptographers uh today we have Adam
dumad who is deeply invested in applied
uh cryptography he will be giving the
talk on public private hybrid rollups
let's give a warm welcome to Adam to the
stage hello everyone um yeah as was
mentioned I'm Adam dad from Aztec I'm a
Staff engineer uh salap as we say in
Thailand or others say in
Thailand and the talk today is public
private hybrid rollups what I think a
lot of people consider the next ethereum
Frontier I don't think this is just
people working on privacy I think a lot
of projects realize that privacy is a
real problem in the ethereum space and
that in order to protect users in order
to attract more real world use cases
privacy is absolutely
critical and there's sort of a story to
be told here um back in the day steam
was using Bitcoin for transactions and a
lot of the problems that they had were
related to gas Fe spiking the volatility
of the price of
Bitcoin and we at here at ethereum have
done a lot of work to try to get a good
user experience on ethereum I would say
the current Frontier of etherum is very
much
scaling and we're almost at the stage
where we can say hey organizations look
over here we solved scaling theorem is
great but basically what I would say
would happen is that they kind of do the
same toy experiments that they've always
done
real business stays where there's real
privacy I think the difference between
the Steam Bitcoin story and today is
that back in the day Bitcoin was kind of
considered private you have
pseudonyms you don't have you don't have
all the things like chain analysis that
collect all these touch points and I
would say that today it would be a real
risk to do Mass business on chain and
you know you think of v and he buys a
silly game and then you know suddenly it
pops up on Twitter that's like an
annoying use case or annoying situation
but you can think of much more dangerous
situations where people's entire net wor
worth is being
tracked
so at Aztec we kind of have this
definition Mike ad AE came up with it I
really like it it's
ethereum is an open system so in an open
system you are broadcasting to people
there's a minimum Mark you could say
that you are at the very least singling
an intent to do something and our gold
standard at Aztec is that is all you're
revealing about your
intent when someone
looks at the blockchain and all that
they see is that someone did something
in some state in some function of some
contract I would say that's the highest
level of privacy that we could hope for
in
ethereum and I I'd say theorem needs
privacy I I think I wouldn't disagree
with our current focus on ux and scaling
but I think it's kind of known that
privacy is a big problem that if we want
people to work on ethereum do real
things you know for the average person
you could every so often withdraw to
coinbase get yourself in a new
eoa and that gives you enough privacy
but that that's not a great situation to
be
in and ethereum ethereum has its
tradeoffs in terms of priorities it has
to balance Innovation speed and
scope and basically where Innovation
happens right now is with layer 2 are
rollups which we've got a great talk on
the definition of but I'm just going to
stick with the term
rollups and we need to lead the way with
private
Roll-Ups and just a quick
caveat privacy is a very large topic and
we do consider it holistically at Aztec
but I won't be talking about for example
which jurisdiction to worry about uh
when you're deploying your app and you
need to have compliant privacy we
actually have our amazing Crypt native
legal team here they they're big privacy
Advocates and privacy Advocates very
rooted in reality they uh they have some
very exciting meetings with governments
um talking about privacy in
ZK and they're happy to talk about real
world deployments I'm going to be
focusing on the technical
matters and uh sort of the journey we
had at Aztec is um well Aztec started
with wanting to do bonds on chain and
quickly realized that no one wants to do
bonds where all of their moves are
trct and that sort of led us to needing
privacy and doing privacy on
ethereum and there's sort of like the
evm model doesn't necessarily work
nicely with
privacy uh what does work nicely with
privacy this is sort of the zexi model
and I think all private chains
essentially use a model like
this and this is sort of taking a step
back because ethereum originally moved
away from this these Bitcoin sell notes
or
utxos and move to um you know an account
model an account model makes a lot of
sense for public State because
um if you're there's sort of uh a race
condition if you're trying to work on a
note and your intent signals a certain
note while things are happening in a
shared matter and sort of these These
Chains that have public state with notes
kind of have limitations on what you can
do in the same
block um essentially because because of
the limitations of using notes for
public state but actually for private
state turns out Bitcoin has has near the
right model uh the missing pieces are I
mean I say nullifiers in ZK it's
basically ZK uh you can't really have
nullifiers without ZK so the idea of a
nullifier is that okay we have our
chunks of money that's maybe a very uh
easy way of looking at what a note is or
a
utxo and you want to use in some way a
chunk of money it could be data but just
for an easy example say it's chunk of
money and you can only use it if a
nullifier doesn't already exist and what
is a nullifier it's essentially a
relationship mathematical through a hash
function and only you really see whether
a nullifier exists for your note
if and you provide a ZK proof um so sort
of ZK in the sense of actual zero
knowledge because you want to prove in
your transaction
that um you have emitted a nullifier
maybe for a note you're using and that
also that
nullifier uh corresponds to your note
but you don't want to reveal anything
actually about your note the way that
this um this bar of something happened
as achieved is
through the fact that actually no one
looking at the system knows which notes
are active which ones have been
nullified so to someone looking in it's
just
hey this note was created here you don't
know who owns it this nullifier was
emitted here you don't know which for
which note and this is sort of the
underpinning I would say of private uh
smart contracts and computation
and for a you know practical example
that isn't money um we have a example in
our repo at a Tec with a card game and
we kind of have like this cute strength
and point system and that's sort of the
user data and then everything else I
would summarize as being uh important
for the protocol and then this
um then this is encrypted only you can
see it as a user and on your own device
you can't compute with
it okay so the the premise is public
private hybrid
rollups and really we would love
everything to be um done privately as
you know as much as makes sense
sometimes you do want to reveal stuff
truly to
everyone
but we're gonna for this talk we'll use
a narrow definition that anything that
doesn't fit
into this idea of something happened
you're revealing the amounts of
transactions that we're calling
public that means any other
information that's not just you know the
parties transacting if you send someone
a notes you're encrypting it in a way
that they can see it but any anyone not
part of the peer-to-peer transaction
gleans
information and can everything be
private I I think there's there's you
know
there's answers on both
sides
um
so if you talk about it very
strictly I alluded that ethereum when
moving to uh smart contract
computation there's a reason they move
to the account model and what we're
talking about is taking a step back to
more of a note
model so kind of but by definition we
are undoing some of the benefits
of what
enables
multi-party uh systems like Unis Swap
and and it's for a good reason because
privacy the only real way to do a
privacy is that the
users execute and prove their own
transactions and um particularly I'm
going to focus on ZK here I think it's
the most mature Sol privacy Solution
that's uh can really take the world's
transactions
okay
but uh so at Aztec actually we have both
we have uh we also have public State and
sort of this butt is okay something
happened that we considered the gold
standard
but it's often okay to say okay someone
did the specific trade but we don't know
who there's plenty of times that's not
okay if you're trading in such size that
well maybe you tip off the Market or
maybe you're the only person who could
trade such size so actually you've
revealed your
identity then it's not okay but we take
a very practical standpoint we have a a
public um part of our chain on Aztec
because it is we definitely believe in
the gradients of
privacy and then you can say you can
make an argument for actually
yes that you can get privacy until the
last M Mile and do
public shared State I think the easiest
way you can consider um okay you may
maybe you can't do something like Unis
swap like a fixed function Market maker
but you could have a signal chat and you
could post prices on that and at least
from the
chain the the chain still has the
something happen property and only your
peers that you're advertising to know
details and then there's obviously other
privacy Technologies there's T's FHS on
the horizon although still very
slow that can get us to this property um
i' say mostly because there there's
always a tradeoff here when you're when
you're dealing with multiple parties and
you want
privacy okay so what would a hard no
world be I mean a hard no world really
is sort of the status quo right now like
the chain is being tracked more than
ever and there there's little incentive
for a business to do stuff that reveals
their business Edge on chain right now
because and we see cases where user
safety is compromised because their
actions are
unchain really the good news is really
there's no hard no for holistic privacy
on any chain ethereum did not start out
as a private chain but here we are at
Aztec
building a a system for holistic privacy
but that being said
that there's many of these rollups even
the ones that co-opted the terms ekk I
mean they use EK technology but really
they're just validity
proofs and especially looking at you
looking at Z ZK sync I I I mean I love
the company but their their marketing is
muddling things by using the term
private and associating that with ZK
which is private but really they're just
a validity rollup and these chains make
basic privacy hard and holistic privacy
very hard
still and okay
so what's the middle ground and mostly
the middle ground that this is largely
the way you can think of the public part
of Aztec is that you have some private
identity you have portions of your
transaction that come from the private
World namely you have private account
abstract ction you
have um you know you can start something
like in a card game example you may
unilaterally work on your deck and hand
and you're able to do that privately
that information is private and then you
want to kick off a public event which
would be you know revealing your card so
other people can work on um can play the
game and um so yeah as I said identity
is always private on Aztec and I think
that's that is something that any chain
can have private account abstraction as
long as you're comfortable with users
doing client side proofs which is
something we take very seriously we like
having we like to build things that
actually work on commodity Hardware we
go through pains to make sure that our
proving system is practical for the
people that are using stuff like phones
because the reality is that that is the
only way to do real privacy is that you
know not only is there the ability to
privately uh approve your transaction
but
that you're able to do this in a way
that works for
everyone and another important thing we
do at Aztec is that we have the same
smart contract framework that works in
public and private land and we do nice
things like being able to share States
being able to use the same semantics
being able
to as cohesively as possible work
through what are very different
execution environments
because um the we we try as much as
possible to abstract the fact that these
are just running on very different
devices the public part is proven by
code by by code and it work works on
sequencers whereas the private State can
only really exist on users devices
and transactions can be a mix they
typically just if you think about it
logically they kick off from private
State because well that is the user to
just encode their event they have to
execute everything that is going to
happen in private State the sequencer
can't execute that and the whole thing
either succeeds or reverts so if you
start something out in private State and
you call something in public even though
you executed you're the only one who can
execute that state luckily to just
revert that state is to just pretend
your transaction didn't come
in and the way we execute this so we had
a very successful nocon we had V there
it was super energetic I'm super happy
about it uh we have the language nor
which sort of you can think of it as I
like the term circom Plus+ it has
everything that circom can do in terms
of create
circuits uh
I think uniquely we also uh translate to
a more of a zkv m b code as well and it
looks like rust so it's code that
developers are used to you can kind of
think like targeting commodity
developers uh
and um and on top of that it
integrates with a variety of proving
systems so you could we have the roll
itself for an inir and I think this is
sort of the the main way we're making
sure this is ready for complicated use
cases other rollups other other people
in web to uh we're very much making Noir
as a public good and so this is sort of
the the proving scheme in a diagram
for the client side where we kind of
just verifi we have this folding scheme
it compromises like has a bigger proof
size but it tries to be the the fastest
thing possible um proving systems are
getting faster and faster but still we
have we want to work hard to make sure
this works on commodity hardware and
then the folding is recursively verified
in the rollup circuit also with Noir
which actually uses a different proving
scheme we call Mega
honk okay so just the last bit um I
don't have as much to say here I think
this is sort of
I I would say that you get a lot from
the scheme I described but there is that
last Model I
think we do want to get to the point
where okay you want to use something
like a DEX it should be as private as
possible and I think we can do even
better by combining Technologies and
sort of having multiple layers
here the gold standard is to do
everything with privacy Primitives uh
all of them have trade-offs but using
together I think you you can get as far
as possible to The Last Mile result and
here we have stuff like multi-party
computation uh definitely we have people
in the Aztec space building um building
stuff like a multiart party order book
and we have fully homomorphic encryption
which has caveats it's slow right now
but some something definitely to look
out in the long term we have te's and I
think I would just lump in the same
category
uh you know app specific rollups like
this Bank diagram here I think they're
kind of the same thing like once you
have um if you're willing to have
someone centralized doing the matching
and you could St that in a te I mean
that has good trade-offs because you're
no worse if the te is
broken um then you can certainly kind of
keep working in the private mall and
then you also have uh you know just like
okay you could use signal and you can
find peer-to-peer
people to work with um and that is
completely
offchain um so yeah thank you for
listening that's sort of
um the point of the talk I guess is to
just let you know about the different
techniques that um can bring privacy to
ethereum and it's sort of mission
critical I would say um I think it's the
next big thing everyone should be
worried about thank you
So Adam I'm just going to direct you
over
here okay all right cool so we do have
some live questions coming in um oh
there we go we will be able to see that
so I can tell public state from private
but can I also do the reverse Shield to
private do you want to take an answer
for this oh yeah sure so yeah as I was
saying the um so you have to think about
the mall here the private state is
operating locally
so what you're able to your intent also
encapsulates everything executing in
private so doing the reverse kicking off
something from public well you can
certainly do that but what the usual
pattern is that in public State you give
yourself something like a permission
that's going to be privately uh verified
because to operate privately you have to
react to that do stuff Bas on your own
device the sequencer can't do it for
you all right cool so if anyone have any
live questions feel free to scan the QR
code over here and the question will pop
up on this side I think we can give it
another 20 seconds to see if there's any
more questions
oh there's yeah the uh so the word
hybrid the reason I'm using the word
hybrid in the presentation title is
because we
have a we have a well first of all
describing a rollup that has both
private and public parts and how we can
cohesively work those together and then
also sort of um straddling the gradients
of different privacy techniques and kind
of varieties of um full privacy and I
think you can combine these techniques
you can have client side proving uh
client side proving is sort of the the
main part of privacy you don't need you
know you could have privacy without a ZK
validity rollup you can just have um for
example like the ZK apps on
ethereum and the idea is that there's
any any chain that has public State and
uses privacy is a hybrid um but there's
sort of more and less holistic ways to
do
that all right great um I think we're
almost at time so thank you so much Adam
um yeah so our next talk will actually
starts at 4: so feel free to hang around
if you want to stay all right thank you
Adam
W hello welcome back so so next we have
Connor McManaman from nethermind to give
us a talk uh on a revenue model for base
rollups and before directing um Connor
on the stage I just wanted to tell
everyone when the slide shows up there's
going to be a QR code at the very right
bottom corner so feel free to scan for
that if you have any questions for our
speakers so let's welcome Connor on the
stage
hi
everyone uh there's a little box here
just in case I I need to see down on top
of the front
row Okay cool so uh yeah my name is
Connor that's not my
slide perfect okay so yeah uh I'm Connor
I'm from nethermind and today I'm going
to talk about uh Revenue model for Bas
rollups uh now I wrote this title uh
before I really sort of had an idea of
what I was going to talk about and then
I realized that Revenue probably just
refers to income but base rollups are
not just about or when you're thinking
about rollups in general it's not just
about income it's about income and
expenditure and comparing those two is
is how you decide if you want to be a
part of the Bas rup and I guess not only
are we going to talk about like the base
rooll up as a sort of an entity but also
the entities like the real life people
that are that are participating in Basse
rollups um so a quick primer on base
rollups for anybody who isn't aware but
they're lost uh is a rollup is said to
be based or uh L1 sequenced when it
sequencing is driven by the base L1 um
so basically the ALB one proposers are
in charge of of of producing the
proposing the blocks for for this rollup
and the rollup derives its state from
the from the the sequence of
transactions that appear on L1 now a lot
of rollups might actually you could you
could squint and say the mots are like
that already uh but I guess the key
thing is that the Elum proposers aren't
supposed to be sequencing the chain
uh so the goal of today's talk uh is
introduce the players in base rups so
we're going to look at each of the
players and and like think about the
income and expenditure that they have
and should they be playing should they
be playing this game uh identif yeah
identify their income and expenditures
uh discuss How likely they
are how these income expenditures are
are going to change on the road map
that's like upcoming uh the big change
that we were expected to see and then
motivate you all to I guess participate
in Bas rups and be thinking about these
income and expenditure problems that
exist uh and then yeah I mentioned fat
stacks for all but really what that
means is everybody has positive p&amp;l when
when they're playing these
games um okay so who's who do we have
here uh so we have the users they're
like the most important right we we're
always trying to sort of make although I
was on a panel yesterday where we're
talking about uh where we're talking
about who should be gaining the revenue
in a system and users were the with the
bottom of the list but users should be
the ones that are gaining something from
playing the game so they're going to be
the ones that are going to be like
driving the revenue for a Bas R up uh
proposers and sequencers and putting
them in the same bracket um ZK provs uh
so we have this proposal over here and
this based uh this based uh blockchain
that's accepting the blocks uh we have
ZK approvers uh because I guess a stage
two rollup should have ZK proofs uh
the Dow so I guess when maybe some of
you are here and you're thinking about
the revenue model for base rup and
you're thinking that it's the Dow that
we're trying to like create revenue for
but I think there's just too many
players in the ecosystem uh to like
fully focus on just a dow or like
whatever this the treasury that exists
on a d on on a base we're going to be
thinking about them along with everybody
else and then also we're going to have
to think about these other chains and
rollups because they are actually a Big
Driver of the revenue the income and
expenditure for a rollup so I have this
this shark from Finding Nemo uh so
depending on how you look at it it could
be a friend or it could be a foe and
will be cases where they are they are
both uh okay so setting the table uh so
I guess maybe one of the reasons why why
I got accepted today was because I
basically when I when I submitted this
talk we were in we were around June or
July and we were in a situation where
Tao was losing money by posting blocks
to L1
uh which people were focusing on and
people were getting really scared like
Bas rups might not have a future uh
what's happening here uh but there was a
good reason for this Tao wanted to make
sure that uh users were getting a
reasonable ux that they were getting
updates every 12 seconds because base
rollups can only confirm blocks when
they get posted to the L1 now again
there's this concept of pre-confirmation
but they aren't live yet but at the time
Tao was force forcing L1 blocks onto the
uh sorry L2 blocks onto the L1 uh while
they were only half full less so they
weren't actually generating enough fees
to to sort of uh compensate for the cost
of posting to L1 uh so but again this
was this was sort of the the p&amp;l that
grow the P grow the pie was generating
right and the the pel that they were
looking at was L2 gas fees collected uh
minus the L1 fees that were paid to post
data and proofs to the L1 uh so that's a
relatively simplified model uh of the
the revenue the income minus expenditure
for a base rollup uh there's actually a
lot more components that we need to
consider when we're thinking about is a
is this Bas rollup uh viable to
run so if you want to get a bit bit
deeper NE mind research did get a little
bit deeper at one point and I guess
we're we're getting deeper uh by the day
um we had this sort of maybe a little
more complex model where we were looking
beyond the onchain cost and looking at
the sort of the the running costs of
running a for example uh like running
aover is not cheap uh not only do you
have to actually pay the electricity
cost for running the approver you
actually have to buy the prover in the
first place uh so most people today
aren't actually buying provs they're
Outsourcing to like AWS or or any of
these internet Cloud providers um so
there's there's add additional cost that
need to be considered there but there's
also additional incomes so I'm going to
get to those in a second um so again
like I guess we're we're in a situation
where maybe okay someone says your
income your your income minus
expenditure is bad so or someone else
says it's not actually that bad and
really everything that's everyone is
looking at this in sort of a quite
imprecise model and we're not actually
able to consider all of the all of the
incomes and all of the expenditures and
I guess you could say that we're
shooting from the hip a little bit um
but these metrics do do provide us with
some indication of how things are
changing right if they're getting bad if
they're getting really bad or if this
really is something unsustainable and in
this in that sort of early stages for
Tao that was an unsustainable model but
it is getting better and that that's
that's the key um so again setting the
table this is the fourth slide that's
setting the table I was struggling for
titles uh so thanks to rollup
competition uh users can Bas users can
migrate easily between rollups that have
similar Network effects so Network
effects are a key part of of why why
users will stay on a ro up uh today or
base rup today but bass rups sort of by
the warm fuzzy feeling the bass rups
give us is that they're actually very
connected with the L1 and other Bas
rollups so this network effect is
actually Pro potentially strongest uh or
like shared between all Bas rollups so
the individual rollups don't actually
have much Network effect so Bas
rollups sorry users on Bas rollups
actually have B basically not much
switching cost between Bas rups so in
this setting the the provider profits so
the providers I mentioned were those the
the provs the sequencers and the D in
this setting the H the hypothesis that
I'm that I'm claiming is that these
profit profits of all these people must
tend to zero because it's easy for
another base rollup to come along
replicate all of the functionality that
exist in that base rollup um and and
basically just remove some of those
overheads that the previous one was that
the profits are the overheads uh that
that base rollup was trying to generate
um but this zero profit Paradigm is far
away uh there's still a lot because
because of all this haziness because of
this wild west that we're in uh it's
still possible that provs and sequencers
can actually be making money um but
again we this is going to be sort of a
long a long road and we're going to get
there uh
incrementally uh and again depending on
how you look at the
road uh like income income is tending
towards expenditure you can see that as
a bad thing um but you can also see it
as a good thing right especially in the
case of Tao uh like was when they
initially launched where the expenditure
was really uh greater than income
getting it close to income and and maybe
even getting a true past income uh uh is
is definitely a good thing so how you
look at these things is very important
okay so on this path to the end game
this zero profit end game uh there is
going to be increases in income and
there's going to be decreases in
expenditure the format supposed to be
decreased in expenditure uh a little bit
on theme with Kevin's talk earlier on uh
but not like HD video so uh with music
so anyway we have as as we shed some of
the the technical data or shed some of
the sort of inefficiencies of early
stage based rollups we're going to
decrease the expenditure um and we're
also going to come up with new ways to
increase the income um and yeah
basically that that that's the summary
of what the sentence at the bottom okay
so uh here's the list right so there's
no real model as as such right it's just
just a list uh you have to basically sum
up all of these Peak components that you
have in your Bas rollup and check is the
left hand side greater than the right
hand side and again there's F there's
like multiple players in the system so
when we're thinking of Base rollup
Revenue we have to look at it but uh
player by player so the users have this
warm fuzzy us extra utility that's hard
to quantify but they pay like very
quantifiable fees uh but we just need to
make sure that there is still some
utility that these users are getting and
if they stop paying uh fees then we
probably have the question are we
charging too much or are we actually
generating any uh benefit to the users
uh proposers the proposers have
relatively straightforward costs as well
uh fee well sorry as well they have they
collect fees uh they generate me or they
collect they execute me H they also
potentially collect issuance issuance is
a contentious debate uh like in terms of
who's paying and who's receiving uh but
l2s can base rollups can create a token
and uh and issue it to the to proposers
and they their costs are L1 posting and
running costs provs again they can
collect fees as well issuance as well um
but they have another cost which is the
setup which is quite a little bit more
significant than a proposer uh because
again zik provs are are sign pretty
significant pieces of Machinery uh the
Dow
uh the Dow sort of actually does have a
sort of unique income source which is
investors uh so when Bas rup launches uh
you'll see that there might be a seed
round or multiple seed rounds uh and and
that Revenue that that investment does
pay for a lot of The Upfront costs which
again you see the provs and potentially
the the proposers when you don't when
you don't know what the fees are going
to be you do need some some money in the
bank to sort of get things rolling and
and that's what sort of tyo we're doing
at the start right and that makes sense
you need to get the users make create
the utility make sure that the ux isn't
too bad and then you start to generate
the fees and potentially the Dow can
recuperate those for the those losses
for the uh investors uh but the Dow also
has significant uh I also mentioned
proposal fee proposal fee is sort of
more of a complex topic but uh it is
possible that the Dow can be collecting
money from actually charging proposers
on L1 for the right to be a proposer but
that's not going to be a focus today h
they also have to pay so the dou is
important though because the dou does
have to pay up for things like R&amp;D we
can't keep depending on ethereum
Foundation uh for for funding uh we have
to sort of go beyond that especially
when we're trying to create base rups
sort of parallel to the ethereum
ecosystem uh so some R&amp;D money does need
to be generated uh and that comes out of
the D and there's also governance
running cost of the DP um and then we
have this all these all chains and
rollups so what do they actually mean so
when the these all rollups comp compose
with the base rollup that could be seen
as income right you're creating ux
you're creating improved utility for
users um not can allow you to charge
more fees but similarly they also create
competition and and with competition
comes uh sort of tighter profit margins
uh so is income greater than expenditure
I've already sort of touched on what why
it should be uh but in general if it's
not you can pack your suitcase uh and
you can go to the some other ecosystem
some other rollup and the proposers is
an expectancy yes it should be right but
uh
we can see that there is new technology
coming along and there's probably going
to be more where proposers may not
actually H be profitable in the short
term because they may commit to offering
pre- confirmations for example and if
you offer a pre-confirmation too cheaply
uh it may be significantly more
expensive to reneg on that
pre-confirmation than just posting it at
a small loss on the L1 the prover in
expectancy and long term yes but again
it may be a substantial cost to to pay
for proving uh proving Hardware so the
appr must invest and see that there is a
substantial chance of of return uh and
the Dow again mentioned this investment
model uh long-term is not sustainable so
they need to be investing in I guess
sustainable infrastructure for for for
these fee mechanisms these proposer fees
these uh uh sequencer fees and we're yet
to see what that's going to look like
but it's definitely going to be very
interesting if if the if the do can
actually recuperate those uh costs uh
so the the cost right now are relatively
straightforward uh but our hope
considering the sort of the the type
profit margins from Tao uh is that these
will change right so I I quote this uh
sort of ancient philosopher or alter
eego philosopher uh who says Bas income
and expenditure is always in flux you
can't step into the same B based Revenue
model twice uh what that means is that
depending on the day like as obviously
today every when I go to the toilet I
hear people talking about how what the
markets are doing like revenue is
changing all the time right the fees are
changing all the time uh but also the
technology changing all the time so when
we think about the based Revenue model
we need to have a Dynamics way a
framework for thinking about these
things uh and that's what sort be the
focus next uh so here are some of the
big big changes to base Revenue that I
expect to see in the future in the near
future uh we're going to see cheaper L1
costs uh we're going to see proven
becoming more efficient we're going to
see Pro and Builder markets maturing uh
so a lot of l2s Bas rops uh will have
run their own PR uh but we are there's
there's Whisperers about PR markets uh
and and potentially also Builder markets
right so Builders and L1 are generating
generating revenue for the uh for the
proposers and that's probably going to
happen as well on base rollups as well
uh so that's going to be an income
source for proposers uh and shared
everything okay so I mentioned this
composition but it's it's definitely
going to be a significant area uh for
income and reduced expenditure so with a
Shar with with shared uh resources or
shared like shared blog space shared
proving we're going to get bigger
Network effects we're going to get
better utilization of of of the
resources that we're using um but we may
also have higher costs right so how are
we going to balance these things it's
going to be very interesting so let's go
through each one in a little bit of
detail I'm I'm running out of time uh
okay so cheaper L1 costs right
so EAP 4844 was relatively
straightforward you just have this sort
of uh sort of temporary data that's
being posted to L1
and it makes it cheaper for l2s to post
uh data to data to L1 and then we're
seeing proposals like Pier Das I don't
really know what it is uh but I hear
it's going to reduce cost significantly
uh but it's uses some pretty significant
sampling or pretty pretty high-tech
sampling uh procedures you can check out
balic recent blog post for more
information um zika proof is becoming
more efficient this is a bet uh I I
can't speak for uh from personal
experience with e proofs I don't have
any uh
but again we're constantly seeing
cheaper uh improved uh cheaper proof
generation and cheaper proof
verification uh we're also seeing
increasingly bad naming terminology but
again it looks like they're getting
better so the worse the names get the
better we're going to see these proofs
uh be coming and we're seeing also more
and more investment more and more teams
deploying people to ZK so I I expect
this to to continue uh a mark a marker
that I saw this morning but again it's
been it's been taken down no one's
trading on this thing um so the prover
and Builder Market maturing I mentioned
this already um so Uncle Ben mentions
that with great competition comes
efficient pricing and
Innovation and again that's just what
we're seeing on L1 and that we expect
that to see that in L2 as well uh so
proof of competition user and sequencers
have to pay less less fees um and
Builder competition we're going to get
better ux through more efficient block
building and sequencers are going to get
higher
fees um and then shared everything right
so with shared sequencing comes more mbv
more users we're going to get uh better
higher fees we're going to be able to
charge higher fees right so this is
again increasing the income of of the
the providers in our system uh share
blobs so right now Tao is is creating
their own blobs with if you can share
your blobs you can get approximately
longer paying a you're paying a fixed
cost but you're now getting 100%
utilization you're able to claw back
some of the cost that you're paying um
shared proving we're going to get
economies of scale
uh and cheaper L1 verification so again
these are all sort of things that you're
trying to do as a provider to uh
increase your bottom line or improve
your bottom line uh and composability
uh so less risk complexity for proposers
you don't you no longer have to use
someone like a cross you can just
basically uh sign a smart or sign a
transaction that interacts with a a
shared smart contract and pre-comp
that's that's a it's a big area of of uh
efficiency and reduce the cost that we
expect to see and improved ux that will
it will definitely improve uh the
revenue model for base rollups uh but
it's also going to increase expenses
right uh so we're going to get there
there's definitely a great greater cost
for sequencing two rollups together then
sequencing them in both of them
independently uh just because the
increased search base uh the the more
the the greater amount of MV MV
opportunities that exist um Shar proving
again similar similar concept as far as
I understand if proving two states uh
together uh is more is more expensive
than proving two
individually uh but the big question
will be are the some of the benefits
greater than the increase in improving
cost we're only going to see that uh
when we see what the results of the of
this R&amp;D are but we definitely are
optimistic that we can get these ZK
proving costs low and the the utility
from shared sequencing high and
centralization I guess that's sort of a
that's sort of a tougher one to to uh
quantify but it's definitely a
significant risk and risks are affect
risks are costs in our model uh so
centralization poses a risk uh and we
need to be conscious that all of these
shared things uh will add to
centralization risks uh so conclusion
when you're thinking about the revenue
model for your based rollup you want you
want to basically get caught up all of
your incomes take away all of your
expenditures and ask yourself why am I
playing this if I'm losing and how can I
play more of this if I'm winning uh base
here is assemble so again do your own
calculations uh and in innovate on
increasing income and reducing expenses
so remember heroical strike you can't
step into the same based Revenue model
twice so we want to see less trickles uh
and and more waves crashing all right so
thanks very much and uh yeah app
appreciate your
time all right great talk Connor I'm
just going to direct you to stand over
here for the
QA yeah this one will'll be good all
right so we do have a few questions
let's go from the most voted question
how can we reconciliate Revenue models
with the decentralization of zkp rollups
where multiple sequencers and validators
will need to be
compensated uh did the person that write
this question could they explain what
they mean by reconciliate
yeah oh sorry I I yeah we can we get can
we get a mic to that person
or okay uh maybe we can go to the next
question while we're waiting
uh well maybe I can I can touch on on my
interpretation of the of the of the
question so maybe when in the case of
current current rollups where we have a
centralized sequencer and centralized
appr it's it's still not clear if the
incomes are greater than the
expenditures okay but yeah we have the
mic now let's go uh essentially how do
we is as there's a risk of um fees
increasing with um higher number of uh
validators uh in l2z k um
rollups how what what are the risks of
that making the situation like more
unsustainable and what are ways in which
we can interest at well the good thing
about B specifically uh is that we we
don't have any validators to pay right
it's just the L1 proposer uh now in
terms of the multiple provs that may
exist uh
we we're basically going to be creating
a market right and it's it's a bit like
Bitcoin and some of the old Arguments
for Bitcoin where you're like okay well
I have uh my hash rate and I have the
expected Bitcoin rewards and if it's if
it's uh if I'm losing money there I can
go to bitcoin cash I can go to an
Alterna
uh blockchain the the same applies to
any of these Prov markets so if it
becomes too expensive user user will
stop uh users will stop paying for it
and basically you're going to have to
spread out your spread out your costs or
just wait until uh Things become cheap
again uh so it's definitely a risk um
and in a fully decentralized system yes
we're going to be exposed to these
things being too expensive uh
so the only thing we can do is try and
make sure that we have uh fallbacks like
maybe cheaper fallbacks in the case that
that those thing we are Expo very
exposed to fluctuations uh but I think
pre- confirmations and things like this
that allow us to wait maybe 16 blocks or
or 32 32 blocks L1 blocks uh where we
get to sort of pick and choose where we
include things and maybe pick and choose
which provs to pay uh that can maybe
help to reduce the risk to maybe spikes
let's say um but not sure if that
answered your question sorry great uh we
do have around two minutes for another
question um which one would you like to
take Connor um well I'll go for the
shorter one first uh if Bas has a
sustainable and positive Revenue can it
become a defa design for the layer
one uh
well I I guess so right like at some
point if if there is one base rollup
that is taking up all of the all of the
L1 block space uh like is in that that
is a theoretical possibility with uh
base rups uh that all the computation is
being done like off chain in on the base
rollup uh so in that
sense it could be doing all of the
execution for the for the L1 but I'm not
sure if we can actually replace the L1
because it is it is being still being
sequenced by the L1 uh so
yeah all right do you want to answer
another another one okay uh I go for the
short one uh just uh what is the plan to
increase the income but with the scale
and expenditure uh with SC with scale
the expenditure also increases uh yeah
that is a tricky one so it's like again
we have to take a BET right um and we're
looking in the fact that a lot of people
like flash Bots uh like all of the ZK
teams that I mentioned they're plowing
ahead with improved mechanism design or
improved proving systems improved
mechanism design regardless of let's say
like any specific end game that that
that may be likely uh they're they're
trying to get make things cheaper um and
if things do become incredibly expensive
with scale we can always scale back
right in there will definitely be a
limit to the amount of things that we
can merge the amount of state that we
can merge uh but right now we can see
that single rollups can survive and then
it's just the case of how can we
actually just scale up that uh the
merging of all this state and that's
definitely going to be a really
interesting question but we can always
scale back that's that's the key all
right cool so we're right on time thank
you so much Connor uh
yeah so our next talk will begin at 4:30
feel free to hang around
we actually really strong
come
test
all right all right all right welcome
back so next we have a speaker from
chroma he said that his Korean name is
really hard to pronounce so he just goes
by ta and he will be giving a talk on
advancing op stack to ZK rollup um so
once the speaker slid shows up you're
going to see a QR code on the side so
feel free to scan that QR code if you
have any live questions for the speakers
we will be addressing them
um during the uh QA session so let's
give a warm welcome to TA from
choma oh
oh show too many slides um hi how are
guys doing so I'm ta AKA fake Dev I'm a
ZK engineer from chroma so today I would
like to share our experience of
advancing allp tag into ZK rollup so
we're trying to enhance efficiency and
security with zero knowledge
proofs so for those of you who don't
know about chroma I want to First
celebrate our successes from last year
our maintenance
launch
so uh uh we were one of the projects
built on op stack so we're one of the
first I mean we're the very first
optimism rollup optimistic rollup with
an active fault proof system so we
utilize CK proofs for it and so ZK
enables to solve some problems in
traditional fault proof systems and for
first we approach with a circuit circuit
based implementation of ZK provs but it
has a very very big issue so we're
trying to Transit from circuit based
approach to zkv and based approach and
lastly we all we're also building a ZK
backend library to push the boundaries
of proof generation
speed so why ZK faal proofs So In
traditional uh fault proof systems it
requires various of if requires a lot of
interactions which leads to high bond
amounts which decreases the level of
decentralization so with ZK fault proofs
we can just narrow it down to a block
level instead of instruction level which
requires much more much less uh
interactions so uh it not only reduces
the operational cost itself since
there's less interaction so we need less
computation but also it can
significantly reduce the bond
requirement so it it naturally leads to
better decentralization and security of
network so moreover for like arbitrum
spold if we apply ZK ZK technology into
it we can we would be able to sign
reduce the bond requirement
significantly that is usually used for
uh blocking Cil attacks also optimism is
uh putting a lot of resources into
exploring ZK fult
proofs so we have a uh announcement that
we have received uh retro prjf round
five from optimism to explore more on
the CK fall proof size and this
recognition I think uh shows how much
important and uh possibilities are there
into building a permissionless fa proc
system with
ZK so we've looked at like our
achievements since last maintenance
launch and now I would like to share
some our lessons learns and challenges
that we've experienced for building uh
ZK fallproof systems in our main
net so the very important fact that we
learned is that the circuit based
approach is just just not sustainable so
we currently have about like 100k L of
code which are for custom circuits so we
have to write in a circuit language like
plish and it's very very hard to uh
write and debug and verify so what we're
trying to do is check the Integrity of
evm St State transition function but we
have we need like several uh specific
custom circuits written in circuit
languages to verify that the state
transition function given the input is
done correctly and back in 2022 uh vital
even mentioned at the time there was no
like uh production ready zkm circuit
codes but they had a POC version of it
in eum's psse and back in the days it
was like 35k lines of code but even
vital mentioned that it's never going to
bug free for a long long time so it's
very prone to errors very prone to human
errors so to sum up there are two
challenges writing the circuit itself is
tough because it's hard to audit and and
debug and also since optimism and
ethereum keeps keep brings upgrades to
their main net to support like full
compatibility we have to keep up with
the protocol upgrades they're making
which means that we have to modify
circuits again and again every time the
upgrades come up and this could lead to
like possibly if we make more modifies
modifications then there will be
possibility of more errors which would
like harm our security of mainten
it so we need a better approach so now
we're trying to take a ckvm based
approach because ZK VMS can give us
generality and auditability what it
means is as I mentioned in a circuit
based approach we need to write circuits
in a circuit language like plish which
is very
unfamiliar and because of that the
Auditors will have also have a hard time
auditing and even us can't
really verify well that our code is
written well but ZK VMS allow us like
flexibility we can write any program
that we want to verify the computation
in Rust and since it's written in Rust
it's very very better to audit and
debug so now I would like to dive in
more to ZK VM area so how we're trying
to move on from circuits to ZK VMS
so as I mentioned ZK VMS can provide a
general purpose environment for
verifiable computation so uh what it
means is that we don't need to implement
circuits anymore we can just write rust
program and ZK VMS can basically execute
the program and give a proof which
proves that the computation was done
correctly so how it works is first the
each ckvm vendor would have a compiler
tool chain that can compile a rust
program into let's say if it's based on
risk 5 it would turn into a machine code
based on risk 5 and then inside of ZK VM
there's an Executor which executes the
program and generates what's called an
execution Trace execution Trace is
basically a polinomial Bound by some
constraints so back then we have we
would have to write like circuits to
represent some input data into a
polinomial and then have constraints for
it but now zkm circuits could handle
that so now we can just write rust code
there's more
flexibility and then in the proving
stage where the ckvm gives a proof based
on the execution trace it would commit
to the trace and then generate a
proof so I have a like a summary kind of
uh picture that we can compare like how
it's different so the colored green
parts are the code that we used to
maintain and we have to maintain so back
then we would have to maintain like zkv
ZK evm circuits written in plish so
there would be like evm circuit RP
circuit MPT circuit and transaction
circuit which could uh which kind of
replicates the behavior of evm so it
will verify the logic if the let's say
the transaction body and like transtion
I mean like the block header and block
body comparing with like hash it and
then like compare with the block hash uh
that's what we used to do it's very very
tricky but now since the on the right
side there are ZK VM circuits so zvm
circuits would handle that and instead
we would just write a blog execution
program which would which for us as a
ethereum layer 2 we would derive the
batch from L1 and then execute it on L2
too so that would be the program we were
trying to
write and uh some of you might ask like
vitalic mentioned in 2022 we launched
our main it in 2023 and then like why
didn't you guys first approach with ZK
VMS at first right like why did you guys
write circuits and do all that hard work
that's because back back then uh ZK VMS
were not like performant so since the
proving time is long in in within the
challenge period we have
there can be possible
volum possible attack Vector for delay
attacks so that's one of the reasons why
we chose a circuit based approach but
now uh RIS risk zero calls it
continuation and like sp1 calls it
sharding like there was a breakthrough
called sharding which with the full
execution Trace you can now divided into
a a unit called shards so it's usually
represented in the number of cycles of
risk 5 so sp1 they kind of have an
optimal number of like 2 to the^ 22
cycles for each shart and since we can
divide it into charts now we can uh
parall generate a proof for each Shard
and then compress it later Into A Single
Shard so now there's more more uh upside
in terms of throughput since we can
paralyze proofs
so that's what we're trying to do and
we're almost there shipping it to the
main net and now I want to like share
more of our of my thought that what we
can explore more in the future to
overcome like barriers to become a from
a optimistic rollup to a z
roll so my concerns about zvm based
approach is since ZK VM venders uh
vendor business model is usually running
a pro Network so they get a delegated
proof and then they generate a proof for
it and then return the proof to the
client but there might be a situation
where zkv and pro Network might fail so
uh usually zkm vendors since they've
built their zkm they're very very good
at uh like giving a good performance so
usually they would have like a cluster
of machines and then they would like uh
split the workloads to each machine
and then like orchestrate it and then
create a proof and return but since most
of the such Pro Network related codes
are close sourced uh maybe to handle
this kind of network reliability issue
we might have to we might like us chroma
might have to implement uh a code to
orchestrate multiple machines so that
every validators could
run by run I'm not sure if this correct
but they they might have to run a
cluster to generate proof for the
network so uh another concern might be
so now then now there's going to be more
stage one rule ups but for stage two uh
we we we only want
the uh Security Council to come in and
resolve like the problem if the failure
is only onchain improvable but currently
in my perspective for the zq VMS
currently there's no way to to make like
the network failure to be onchain
provable so that's that's another
concern and also since we cannot
Overlook that the fact that ZK VMS
itself might have a bug uh so what I
think is we need a multi-prover system
so that we can compensate the bugs for
that
so then in that case the goal would be
to enhance the security of the network
but not much with the overhead so we
don't want like uh periods to be longer
so there might be like three types of
multi-prover schemes instead of like
having a single prover so one I think
most of the networks like scroll and Tao
is trying to use teth but in my opinion
uh there's a trust issue that we have to
trust the T implementation itself so and
there's also like Hydro centralization
problems so we might have to come up
with a clever idea to maybe use like
three vendors of te's and then like have
a multi kind of thing and another one
would be kind
of very very labor intensive but come up
with another circuit B another circuit
based ckvm so instead of plish and Halo
code circuit code with another language
uh I don't think no one will try that
and I think the best would be uh our
approach to have another zkm based ZK
evm I'll tell you why like why we think
this is the
best uh and if if we have a multi-prover
system and if we have like ZK VMS now we
could really really easily ship ZK
rups then like past one or two years but
I've did some benchmarks with several ZK
VMS but there's still a feasibility
issue so first there's a cost barrier
which is very very important and in my
opinion it would be really really hard
to like charge the users to use it since
like most of the layer tws and most of
the optimistic rollups now have very
very
cheap uh fees so there are three types
of costs that we need to pay to run a
zqq rollup first it's it's the biggest
bottleneck which is the proving cost so
uh I've tested with like a network with
about like three TPS and you need about
a million dollar for proving the blocks
for a year so I think it's not that
feasible now and also we would have to
com commit to the batches we've uh
settled into layer one so there will be
settlement fees also and to finalize the
blocks we would have to send the proof
to the contract and verify on chain so
there's also going to be verification
piece but that's going to be really
really small because we will be able to
agre aggregate proofs inside a ckvm
which will be way cheaper but there's
going to be trade-off between
finality and also we could Explore More
on future directions where I introduced
the multipro system and
also uh the ZK VM vendors would have to
consider more about Pro
decentralization where they don't keep
the Clusters running on only their
Network and getting proof requests but
instead of like have a incentive
mechanism so that Pro Network can be
decentralized a bit
more uh and like we're also pushing the
at the same time pushing the boundaries
of proof generation so we have our own
very unique uh open source Library
called takon
which is a particle that's known to be
faster than light uh and it's it's
basically a modular ZK VM ZK backend
library and we also have a feature of Z
GPU acceleration so since we've built
our ZK VM based on Halo 2 we first
optimized Halo 2 a lot and we have about
like 1.5x 6X faster
Benchmark and we also are trying to
utilize sp1 ZK VM at the moment so we
also optimize planky 3 as well which is
used by
sp1 and last since circum is very very
widely used in the community we also uh
optimize a lot in terms of Rapid snark
so it's also
faster and we could wrap up into this
one figure where if if chroma has a
multi ckv improver back uh backing the
network we would also have takon which
is a modular ZK backend Library which
could support all all kinds of ZK VMS so
we would only have to
maintain the very front like ZK VM main
which is written in Rust and which
mainly uses the library Kona which is
main from maintained from optimism which
has block derivation logic and execution
logic so we could easily write uh a
program for a main net within like 200
lines of code and we would have an input
with which the which would be the block
we're trying to prove and we would have
a multi-prover like one of the Frontiers
risk zero sp1 om VM uh valida maybe and
then we have a takon which is backing
with powerful GPU optimizations which
will accelate accelerate the proof
generation
speed yep that's it for today and you
can contact me with fakee 9999 on
Twitter telegram please contact we could
share more about uh fault prooof systems
I would like to hear your ideas and
that's it thank
you oh you can just stay over here all
right uh great talk to so thank you to
the crowd for submitting all these
amazing questions uh we do have less
than five minutes to go through some of
them
uh let's go through uh the most upvoted
one how is it different than op6 sync
yeah uh some of you guys might know and
not know but uh opung and us we have a
very very similar logic actually we were
working
underwat like for about like two months
and then like we shared it to the S1
team about oh we have a chroma sp1
improver repository you could take a
look if the logical would be correct for
ZK VM based prover and they were also
working on the water with the same thing
and like it comes out that like we have
almost similar logic and they have an
additional feature of what I mentioned
of aggreg aggregating the proofs so the
logic is very similar but basically we
built the same
thing uh so I'm going to mark this as
answered any stats homeover cost specs
and time
so the Pro cost
for uh the for our fault proof system
for about a block with a TPS of three to
prove a faulty
block uh of tps3 I think it costs about
like uh currently if you so it depends
on the pricing of the net the approver
network you're trying to use but if
you're just using an ond demand plan
which would be the
most expensive per Cycles uh if I
remember correctly it's it was about
like 20 20 bucks for a block with like
about like uh
tps3 and uh the their the stats and like
the machine specs it's not revealed at
the moment for SP Andover Network so I'm
not sure about that all right do you
know if the ARB ecosystem have similar
plans yes I I definitely know and I also
uh know the fact that they have a fast
withdrawal feature now with ZK proofs I
didn't have much time to like deep dive
into it but I I definitely think like
arbitrum
also is going through the right path so
maybe we could collab more and talk more
about
it all right great so we we can go
through I guess two more questions real
quick uh in your prior implementation by
pish circuit you mean Pony 2 or three or
something custom oh it's it's actually
uh Halo 2's plish arithmetization
uh it might have like confused you a
little bit but it our we're using a
backend currently Halo
happens if the guest program panics can
you still produce a proof so if a guest
program panics then uh you can't produce
a proof
so uh I'm not
sure uh the person who ask who's asking
the question like is intentionally
panicking the program or not but
like yeah if if it's a bug that's
causing panic
then proof is not produced so this is
one also another thing I mentioned in
the slides before is we need a way to
like uh like overcome like if the
program panics like but if it's a bug
inside a ckvm or if it's a bug in a
program then like you would need to wait
to uh verify it on chain or like have a
way to prove it on chain so
that so that Security Council could like
intervene or what all right great so our
time is up thank you so much ta
uh so our next talk will actually starts
at 5 so feel free to hang around
all right welcome back everyone so up
next actually very excited for this uh
we have another amazing speaker from the
Aztec team and his talk is on
decentralize your sequencer a guide for
l2s um when the speaker slide shows up
there will be a QR code on the side so
if you free to scan that if you have any
live questions we will be addressing
them in the last five minutes in the um
FAQ so let's give a round of warm
Applause to Joe Andrews the co-founder
of Aztec on the
stage all right thank you everyone for
coming I know uh there's a big talk next
door about the ethereum road map so I I
appreciate you guys for coming to this
one um my name is Joe I'm one of the
co-founders of Aztec um we're building a
privacy laay for ethereum um but today
I'm going to talk a bit about a general
guide for l2s and how to decentralize uh
sequencers uh you can follow me on
Twitter um and let's dive
in so first of all we're going to look a
bit about our journey um uh kind of the
journey that Aztec's been on what we've
learned and I'm going to try and
convince uh hopefully the al2 in the
room people who work at our twos to care
um and I'll also talk about why we care
um we'll talk about why we can't rely on
trust me bro um this is something kind
of it's a bit of a pet peeve of mine but
we'll go to that in a second
um we'll just debunk the myth around
forced inclusion um being the same as
decentralized sequencing um we'll look
at the different components of a
sequencer um and then you know
decentralizing a sequence is just the
beginning and hopefully we'll have time
for questions
so back in 2023 uh we started kind of a
process at Aztec you know for the last
we decentralize and launch Aztec as a
decentralized L2 uh we're doing this all
in public on our forums um you can check
check out these various rfps and the
responses uh on on our Forum I'll share
a link in a second um we've had to think
about this a bit before everyone else um
you know being a privacy focused layer
to like the regulatory climate is is
slightly hostile towards us um we can't
be a central point of failure uh for all
of the private transactions that go
through Aztec um so we've been thinking
about this uh and hopefully I can share
some of the learnings with you uh
today um our latest kind of uh block
production designs are now live on the
Forum um you can scan this QR code um
spoiler alert like we use a random
leader election to decentralize our
sequencer there's also a payload timing
committee on the L2 uh to help with fast
finality um and kind of better ux for
pre-c confirmations uh but ultimately we
use L1 to verify everything um and so
trying to stay firmly as Z rollup um all
right so first of all let's look to see
of other al2s care um I pulled some June
dashboards uh last week and alltime
sequence of profits for kind of other
al2s are north of 150 million um this is
kind of a crazy stat but you can kind of
see all of the kind of top l2s um you
know they're they're printing multiple
millions of dollars per year um and they
may say one thing publicly um you know
we're working on it um the next version
will be decentralized um there kind of
like not really the right incentives to
decentralize here uh and so my goal with
this talk is to try and convince you
that a we need to care and maybe look at
some of the options we have available to
us uh for a meme uh Yoda says it better
than me so yeah too much money the
centralized sequences they
have um in terms of kind of like where
we've got to and how much money these
l2s are securing um users trust l2s with
$38 billion today um and so you know L2
beat is is great at kind of showing us
what's happening um uh but it's also
kind of it's just a scary number when
you think about it uh when I think about
this it's $38 billion that doesn't live
up to the vision of rollups um this
doesn't inherit the censorship
properties and the liveness properties
of ethereum maybe it gets some eventual
safety properties from ethereum But
ultimately this money just relies on
trust me bro you know there's a central
entity in the middle of all these
transactions that we all trust to
sequence tell us what the state is um
and promise inclusion and for me that's
it's just not okay um you know this meme
says it as well there'll be lots of
memes today
um why is this not okay um I think that
in order to have like a credibly
decentralized uh L2 like we need to
decentralize the sequencer to inherit
the properties of censorship resistance
liveness and safety from ethereum um you
know eventually we get safety um when we
verify a proof uh or we have the flaw
proof window if it's implemented on uh
like an optimistic rollup
but a lot of these transactions are
happening you know sub ethereum block
times and so there's a lot of pending
chain uh finality that is not safe
currently so we need to look at how to
make that
safe some more reasons why we can't rely
on trust me bro um yeah centralized
sequences they can lie um they can lie
about whether your transaction will be
included in a block they can lie about
the transactions that are before or
after your transaction the state of the
L2 uh and this can happen for minutes
hours or days depending on um the state
of the system um we've also tried this
before right most people are at Devcon
because we're fed up with the web 2
ecosystem um and like if we wanted to
just trust someone with our data we can
use our favorite like new banking app um
we can use the database for that so
hopefully we can do better I think in
another reason here is in 2024 that
censorship is is is very real like as we
start to get more and more usage and
Adoption of crypto um the chance of one
Central entity sharing the same beliefs
of everyone in this room or all of the
transactions on the network it's
vanishingly small um and so you know as
we start to get more interesting use
cases sequences will start to prioritize
one type of transaction over the other
um and we we can't have that and the
last one this has been said before um
but aliveness failure is still a failure
right you know if you get used to you
know subsecond block s and then it goes
down for 5 hours uh you can't send a
transaction you can't use your money
your funds are stuck um and so this may
be okay for today when we're trading you
know Meme coins but if you're trying to
get to work or use real value um this is
not okay um this has been said before
but I I like this
meme okay so this is like a personal pet
peeve of mine I think sometimes
centralized rollups uh rely on forced
inclusion to say we'll do it later or to
keep printing the the millions of
dollars that we saw saw earlier for me
forc inclusion is a bit like this uh
this traffic jam you know if
everything's great and uh your friends
with the centralized sequencer you can
use the fast lane you can get to work on
time uh and everything's working
perfectly um as soon as something goes
wrong uh you get stuck in this traffic
jam you know the capacity is not there
you wait for hours um and really like
you can only use this in emergencies you
may use the right hand side to flee a
country like run away from a storm but
you're not going to use it to get to
work um and forced inclusions are are
pretty much the same they can only be
used for um transactions which have a
long duration um and so we want to make
sure that every transaction has the same
properties for censorship resistance and
liveness um and forc transactions are
kind of a second class citizen um all
they guarantee is like an eventual
sequencing um and we need to
decentralize our sequencer to ensure
that these properties are the same for
all
transactions so yeah if you leave with
anything please leave with this forced
inclusion is eventual sequencing not
decentralized sequencing and we can't
rely on it okay so a lot of why
hopefully you're with me now and you
want to decentralize your sequences so
let's look at some of the core
components there's four main components
um we have leader election uh da uh
slashing incentives and consensus um
we'll go into each of these um in a
little bit more detail um but I think
the the key one is is the one on the
right with consensus um we need to
verify that everything uh to the left
here these first three uh happen
correctly um and how do we do that you
know how do we verify that the correct
leader was elected from a decentralized
set how do we verify that they published
enough data for the next sequencer to
publish a block um how do we verify
where slashing occurs if we do that on
L1 a separate consensus Network or use
economics they all have different uh
assumptions around where we inherit our
security and liveness
from so let's look at the first one uh
leader election um you know if we have a
white list like a sequencing white list
and you're not on the list you may end
up like this guy uh waiting to be picked
a sequencer and we can do better than
this so leader election is all about
picking who's going to be the next
sequencer um and there's a few different
ways we can do this um the simplest is
around Robin uh we can kind of have an
ordered set and just cycle through them
one after the other um in a
deterministic order it works but you
know the determinism is actually a bit
of an issue um you can have denial of
service attacks because of
this a better Mo model maybe a random
shuffle you know you can Shuffle uh
either sequences or block proposals um
both can work uh um but they rely on
some sort of random Beacon to
work uh another interesting one is kind
of let anyone be a sequencer um and
actually just vote on the proposals so
you could pick the proposal which makes
the most money or you know uh solve some
sort of optimization problem and the
last one is kind of a combination of
some of these um you can take a random
shuffle but weighted by some Factor it
could be weighted by reputation or stake
um so these are kind of the different
options available for the first uh
leader election this does need to be
verified somewhere so it's important to
kind of take that into account when
choosing okay so the next one is uh is
also equally important um if I'm the
sequencer and I'm centralized and I want
to build block n on as block n plus1 on
block n I've already got the data like I
don't need to send it to anyone I made
the last block so I can just keep going
uh kind of for all of time being this
this centralized sequencer that doesn't
work if someone else is the next
sequencer so we'll run through a little
kind of chain here um the purple blocks
are finalized blocks um they're either
finalized because there's a validity
proof or you know there's a fraud prooof
window that's expired to build a block
on the finalized chain um I just need
the side effects of the rollup um I need
to you know all the transactions that
have happened uh throughout the time I
need to have a database of those uh side
effects I need to move the state from
the old side effects to the new side
effects to to build the next block so I
can build block four here and then
imagine we have like a pre-confirmation
chain where the sequence is changing
quite quickly um but these blocks have
not been confirmed now they've not been
confirmed by A1 they're just kind of you
know uh they've been confirmed between
maybe three different sequences uh but
there's a lot of data now that needs to
be shared to build block six we still
have to share the rollup side effects
um you know we have to have block five
State and then we need to you know apply
the the state diff from the transactions
in Block six to get the new side effects
but there's this other type of data
which usually gets swallowed um in a ZK
proof um or uh it's not posted on chain
um called transaction off data and this
is where the problem kind of starts so
for a public rollup you know optimism um
rollups that don't deal with privacy ZK
sync like public ZK rollups have this as
well the data is quite small um so you
have a TX request and a signature it's
around 400 bytes you can post that data
you know you could put it on ethereum
you could send it to um you another da
lay you can put it in lots of places for
a privacy rollup um the data is a lot uh
it's a lot larger like the transaction
ACC compan uh a zero knowledge proof
which can be you know 32 to 64 kilobytes
depending on the proving system and so
sharing that data between sequences
becomes a bit of a problem which we'll
go on to in a second like if you don't
have this data you can't verify that the
transactions in Block five are
authorized which means you don't know if
block five will happen so you don't know
if you can build upon
it so in terms of Da like where can this
data go you know we can put it in core
data it's been around for a while um
it's kind of the only way we can put
data on ethereum if we want to use it in
a smart contract uh it's very expensive
though and limited in capacity blobs
came out uh last year I believe um we
like these they're a lot cheaper um and
it's very useful for kind of uh posting
this side effect data um it can also be
used to post uh the transaction
authorization data we talked about
earlier but only for kind of public
rollups um there's not enough capacity
for private rollups to use
this um payload Tim committees these are
like an L2 specific committee like the
sequencers can join together um and they
can sign off on the fact that enough
data exists they've seen this data to
prove the block um you know if they if
they give a signature and you know a
majority of the committee signs off then
a sequencer can look at that signature
and be like I don't have the data but
you know I trust I trust this committee
it's like a mini da layer but it's very
shortlived and then you can also put it
on an old da um so there's lots of
capacity on these but they don't Bridge
back to ethereum very quickly um so it's
only really usable for kind of side
effect data and you can't use it for
kind of data that's critical for Block
production because then you won't be a
rollup this is just a quick kind of
table of the different comparisons um
yeah you can see kind of you have to
pick and choose based on you know
security uh throughput that can fit on
these different Das and uh what they can
be used for
cool so the last part is you know uh is
the most important like we have to
verify everything we just talked about
and so usually when we think about
consensus we just think about verifying
what happened um you know did these
transactions produce this state um and
that's kind of you know that's fine uh
but when in when we're talking about
decentralizing sequences we have to
verify a lot more than that we also have
to verify like how did this happen um
you know if we're waiting for a validity
proof which can take 10 minutes um in
some blockchains in some rollups sorry
it can take several hours um or
challenge periods in a optimistic kind
of fra proof scenario could take seven
days what do we do in that time to
verify that the blocks that are pending
um actually happened like we need some
data it's the data we talked about on on
the last slides and so depending on how
we can trust what happened we may need
to kind of also verify data locally as a
sequencer to know what happened
and then lastly like we need to check
who did it like you know did the
sequence of who proposed a block
actually have the right to propose a
block um and so we need to come to
consensus on all of these three things
um to make sure that the blocks that are
being proposed by a decentralized
sequencer are valid and follow the rules
of the system um if we don't kind of
verify who did it like you know someone
could just keep proposing a block who's
not able to they could monopolize
sequencing rights
and so depending on where we verify
these things we inherit different
censorship and different liveness and
different safety properties uh and
they're not all equal
um so I think just looking at the
different options we have here you know
the most secure is to be an a based
rollup you know let's try and inherit
everything from L1 um this is great we
can you know defer sequencing to the L1
proposing set
um we can kind of inherit censorship and
liveness from L1 like if ethereum's
running you can always propose a block
it's also quite easy to do um however
this is only really possible for public
rollups and it's also quite slow um so
you're limited to a block every ethereum
block most l2s have a lot faster
finality than that um or sorry faster
pre-c confirmations like they have
sub-sec block times so this doesn't
really work um
another alternative is use L1 for
ordering um but for this data which
doesn't fit on L1 introduce like a
payload timeliness committee um for the
transaction off data you know have this
committee that sticks around for just
long enough uh to make sure that a block
can be proven um and this is possible
for public and private rollups it has
some pretty nice properties um you know
we get the censorship properties from L1
because l1's deciding whose sequencer um
liveness properties are pretty good if
the committee is Still Honest um and if
you have a decentralized sequence set
this is actually a pretty strong
assumption and we inherit safety from L1
as well um other ways of doing this you
know are less less good some people talk
about putting you know a tmin cosmos
instance in front of the uh L2 um you
know have an actual consensus Network on
the L2 this kind of has uh I guess it
doesn't inherit the properties we want
from our one um you know if you have a
separate consensus Network that's
deciding whose sequencer is deciding if
the data is available um and it's
deciding you know is the state of the
pending chain correct um you only
inherit the properties of that staking
Set uh in the short term eventually you
may settle to L1 and have you know a
validity proof of all of this that's
very complicated to do you have to prove
the consensus of the L2 on L1 and like a
mega proof um I think the the other
thing that's worth saying is that like
you also would have to reorg your L2
consensus network based on whether that
proof succeeds or fails on L1 so it's
just messy um so where you sit in this
kind of uh chart depends on you know as
you decentralize uh what what you want
to kind of give your
users uh all right we're running out of
time so I think a few slides left um the
last thing I wanted to go through is
like this is just the beginning like you
can pick where you are in this kind of
map of like da uh leader election uh you
know slashing uh you know Implement all
these different things um but it's just
the beginning like there's no point
decentralizing your sequencer if you
don't think about the entire kind of
like stack um so sequencing is one part
um we've got provs right if you're a zk2
and you're relying on someone to
actually prove the validity of all of
this happening and you have one prover
then it doesn't matter how de your SE
sequence of set is because no one can
actually Advance the chain so yeah
decentralizing proving is is a key part
of this um and governance is the last
part like if governance can overrule any
of these two things or change the system
uh and that's centralized like there's a
centralized multisig um it also doesn't
matter if you have decentralized
sequencing anding because the results
can basically be thrown away and so to
actually fully decentralize an L2 you
have to exist in this middle part um and
so you know any one of these in
isolation uh doesn't really work and
this is kind of what I wanted to leave
you guys with um maybe next year I'll
give a talk on on the other
two thanks for listening and uh yeah you
can look at our Forum post here um if
you want to follow along for some of the
other designs on uh governance and
decentralized proving and follow me on
Twitter and maybe scan the QR code if
there's questions thank you
all right so we're actually a little bit
short on time but we can still take some
questions let's go from the very first
one ckp sequencing still costs a lot how
do we guarantee sequencers are run by
different actors in different locals
even if decentralization is supported
yes so the cost of sequencing um there's
two there's two things that I think are
important in the cost of sequencing it's
like the you know cost of the hardware
and the cost of like um the bandwidth
needed to run the node um you know
sequencing zero knowledge proofs or
anything else there shouldn't be any
more additional like Hardware um
requirements than that of like an
ethereum node there may be more
bandwidth requirements just because
there's more data um if the proofs are
larger um and so you know you can still
get Geographic decentralization if you
just focus on hubs like universities or
areas that have good fiber connections
but the hardware is is pretty easy to to
get all right and which of your users
are most excited and empowered by
decentral sequencing on
Aztec um this is a good question there's
I guess there people who want to run
sequences but that's uh maybe a an
obvious one but I think like the reason
we decentralizing sequencing is because
it creates a neutral layer where you can
have you know very different uh apps
inter interoperating with each other and
so I think if we look at the types of
applications that uh people are building
in in kind of azte Pilots like there's
things like proof of passport things
that like you need a new neutral Bas lay
and so I'd say that any application that
kind of is at The Cutting Edge of its
field uh probably needs a decentralized
sequencer and is excited by this cool
and how easy in technicality your
opinion that ZK sync op and other move
to decentralized
sequencer yeah this is a tough one so um
two three years ago we had a product
called Aztec connect um and we built it
centralized and we said we were going to
decentralize it later um that never
happened um so I think this is this is
harder uh than than it looks I think the
the research is there to do it um I
think it's more of an incentive question
um so if you're in these communities I
think this has to come from users um
it's not going to come always from core
teams because you know centralized
sequences make a lot of money it is
possible today um but it does require
pretty serious
upgrades awesome and what should be
decentralized first sequencer prover or
governance yeah this is a this is a
tough one uh my last slide kind of hints
that maybe all three have to happen at
once um I think uh in a privacy rollup
that's definitely true um for for public
rollups I think um you can get away with
um you know decentralizing them a bit
more one at one at a time um I've I've
seen some pretty interesting uh Prov of
decentralization where proofs are
happening in tees um as like a second
proof like a multipro model um yeah I
think it can happen one at a time but uh
only in a public roll of
context all right so here we got a
question actually from token 2049 the
cost is a big reason why l2s are still
centralized sequencers decentralized L2
will increase cost and users don't like
it and what is your opinion on
this uh I don't know if it will increase
cost it may increase or make the ux uh
slightly worse um but I think it depends
on um the type of application so you
know if you think about um uh micro
payments or fast fast finality payments
they may need a centralized um uh like
sequencer to process transactions but
those things should exist as an L3 or
like an app chain so I think uh it's
more of a ux consideration than a cost
consideration like with decentralized
sequencing we're targeting like between
and 10 cent transactions on Aztec so I I
don't think the cost argument is is
there all right I think time for one
last question there is incentive
misalignment for centralized sequencers
to decentralize how do we solve this
that was kind of the point of the talk
so uh it's on us to kind of uh talk
about this and um I think push them to
to do it I think yeah it's it's easier
to not do it um but one day something
will go wrong and we we wish we had done
it so I think you know if you're in
these communities um yeah kind of push
push the push your kind of uh Cavs to
decentralize and and start the process
all right I think unfortunately that's
all the time we have thank you so much
Joe for giving us this amazing
talk um our next talk will begin at 5:30
so feel free to stick around if you are
interested
all right welcome back everyone so our
next talk is on the topic our l2's
extractive to ethereum so a little
housekeeping rule there's going to be a
QR code showing up right over here so
please scan that if you have any
questions for the speaker so you guys
have like these interesting names that
like I don't know what to do so let's
welcome Ren crypto fish on the
stage cool uh thanks for coming um I
know it's been a long day uh today I'll
be talking about the topic of R l2's
extractive to
ethereum my talk I'm going to cover
three main areas um the first is um on
the topic of l2s keeping fees and not
paying enough for blobs this is quite a
nuanced topic and I'm going to dive into
it the second um what I think is a more
important question is are l2s generating
eth denominated activity in terms of eth
being used as a gas token eth being used
as an asset and has it generated new
holders of eth and I think the the third
topic I'm going to touch on is what is
the D dynamic between l2s and
ethereum so if you go on crypto Twitter
if you read forums blog posts Etc one of
the most popular narratives is l2s are
keeping the fees that they're generating
and they're not paying enough for
blobs and you can kind of see this when
you look at the margins for layer 2s
post EIP 4844 going from 20 the 30%
margin on on fees to upwards of
this is that blobs are still in the cold
start period and what that means is that
it is a byproduct of the mechanism of
start problem actually last year and he
ran a simulation from March 2023 using
assumptions from the transaction volume
on arbitrum and optimism at that time
and it would take roughly 250 kilobytes
per block to get into price Discovery
for for blob pricing that's roughly
the later charts what I'll show you is
that we're basically there on average
per day but not yet on a block byblock
basis
and actually there have been some
notable periods when blob pricing has
gone into price Discovery um this is an
example from earlier this year which
shows the blob fee breakdown between
blob space fees and execution fees
during the layer zero airdrop and you
can see that for a period of roughly 1
to two hours blob fees actually
dominated compared to the execution fees
and actually most more recently blobs
have been getting really really close to
the Target amount of
blobs past which The Blob pricing would
go into price Discovery and you would
see this drastic increase in the cost of
blobs uh face by the
l2s but one of the interesting Dynamics
behind this is that layer 2os are
fundamentally businesses um and when you
see a fee Spike for blob
pricing um we tend to see that layer
twos actually start to uh slow down the
pace that they post blobs in order to
dodge these high high Spike
moments another way to see this is
through the distribution of blobs per
block so the gray color um are blocks
with no blobs um these are kind of these
blocks serve as a temporary buffer where
for for instance you might have a day
where the total amount of data posted
might imply that the blob fees should go
into price Discovery but if you uh but
that mechanism is actually triggered on
a block byblock basis but we're we're
going from a world where half of the
blocks had no blobs to a world where
only 20 to 30% of the blocks have no
blobs and and the same is true on a
capacity basis so in the summer of
roughly roughly 20 to 30% um of the data
capacity in terms of bytes um was unused
and now we're approaching a period where
only 10 to 20% is
unused and overall blob's inflow per day
are quite healthy they're actually well
above the 1.8 gab Target tget um through
which if that were true block by block
blob fee pricing would go into price
Discovery um um so I think we're
actually well on our way to
that so now that I covered some of the
nuances be behind the blob fee market
and that it's not necessarily a
byproduct of the l2s not wanting to pay
for blob storage it's more that the way
that the mechanism is designed
um is what uh is precipitating what
we're seeing um for the blob fees at the
moment um so the second topic I want to
dive into which I think is the more
important topic is are l2s generating
activity and usage of eth the
asset so if you look at L2 beat um and
various block explorers I'm sure
everyone has seen a chart that looks
something like this where the L2
activity has grown tremendously over the
the past year going from around 50 TPS
um up to 170 180 TPS across the
l2s but l2's usage of eth as a gas token
has only grown modestly due to lower L1
settlement fees despite higher activity
that's partially contributing to things
like lower burn a lot of uh concern from
the community um but again this is more
of a byproduct of the mechanism of 4844
and less about any nefarious
intention but I thought this chart was
actually pretty interesting so if you
zoom out and you look at the collective
fees in terms of eth being used as a gas
token and you compare that to uh the gas
fees used on mainnet you can barely see
the L2 line um which is great for users
in that they're transactions are quite
cheap um but potentially some concern um
around the security of of main
net on the flip side the L2 usage of eth
as an asset has grown tremendously so
what we see here is a chart of the total
value locked stacked by type uh the
purple on top is a canonical bridged eth
um and that's just gone uh pretty much
up only since l2s
launched so in summary to cover the
first half of the talk in terms of the
current state there is not enough L2
blob demand to consistently get blob
blob space into price discovery that
requires consistently block by block um
l2s consistently posting blob blobs in
order to trigger the price Discovery
mechanism behind 4844 but I think we're
almost there blob pricing today is
currently in a bootstrapping period it
has shown periods of price Discovery
this is known it's been posted on the
eth research forums in 2023 there's
nothing inherently wrong with the
network or or the way that the pricing
is working and it's actually approaching
data inflow levels that would actually
start to trigger and begin price
Discovery um and looking at activity on
the l2s we do see a lot of new usage of
eth as an asset in terms of being used
in staking protocols in Defi and Etc but
very minor usage of eth as a gas token
relative to main
net so the second half of my talk I'm
going to talk about the dynamic between
l2s and
ethereum so at the limit l2s and mainnet
appear symbiotic Tim Tim Robinson had a
great post um and he actually built this
really great calculator where he showed
shows that he's showing a scenario under
which ethereum um for ethereum's blog
Market post surge um so what this shows
is a simulation for 10,000 TPS across
l2s which is pretty feasible and
reasonable I think 16 megabytes of blobs
per block and that would imply a 6.5%
yield on eth given some reasonable user
price sensitivity assumptions so what
that means is is when the transaction
fees go up uh a smaller percentage of
the users are willing to transact at
that price because they might be
sensitive to higher transaction
fees but I think where we are in reality
is here where um we're at this temporary
lull where the L2 fees are very low and
we're in a period where we're probably
most likely going to exit the
bootstrapping period of blah pricing and
we we'll likely see a period where L2
fees tick
up so for example in this scenario here
um this uses the current specifications
for based on
rollups 300 TPS per rollup the same user
price sensitivity assumptions and what
you can see in this chart and I think
the interesting line to call out um is
the green line which is the actual TPS
um that that reflects user Sensi user
sensitivity to higher transaction fees
and in my opinion five rollups and 300
TPS if you look at the number of
projects kind of in the pipeline that is
uh pretty doable in terms of what we
might expect to see over the next year
um and what we can actually see in this
chart is it implies that the ethereum
blob Market could potentially serve as a
constraining factor on the ability for
these rollups to increase through
throughput and increase
activity so in terms of in terms of the
question are l2s extractive I think I
think the question is actually very
nuanced and is actually quite
complicated and I think the true answer
is that we don't actually know and I
think there are three reasons for that
the first is the L1 settlement fees have
never actually been high enough to test
ethereum's Network effect so what that
means is we've never actually seen a
scenario where l2s have been faced with
increasing L1 settlement fees so we're
really uncertain about how the l2s might
react in that type of scenario whether
they might look to an alternative da
solution whether they might uh be forced
to decrease their margins whether they
might um potentially even become an L1
on their own so I think that first
scenario we've never actually really
seen that in practice so we don't we
don't really want to impose that
judgment um upon the layer
twos so the second point is that there's
a there's a lot of value for for l2s
being l2s and I think um Beyond just the
label of what people might say oh like
I'm going to launch an L2 on top of
ethereum what they actually get is quite
a lot so
imagine having to write your own block
Explorer your own virtual machine your
own smart contract programming language
recruiting developers to learn your
smart contract developing uh language um
and I I think the reality is that the
l2s are relatively new and because they
are relatively new they benefit
tremendously from being able to
bootstrap their virtual machine tooling
developers users Community assets from
ethereum and even in terms of
application as
well and I think the third reason why we
don't actually know whether l2s are
extractive today is that most of the
analysis in terms of even Tim Robinson's
dashboard um tends to assume that you
have n equal siiz l2s um which one might
consider the current state because we're
kind of In This Moment In Time where
there isn't a clear breakout L2 winner
and whether you look at tvl whether you
look at transactions whether you look at
number of wallets whatever metric you
look at generally you tend to see
fluctuating periods where you have three
dominant l2s and they're all splitting
market share at different points in time
um and I
think and I think that type of analysis
and thinking about the current state is
probably not likely to hold into the
future so it doesn't really consider it
a case where you have one or two l2s
that 80 to 90% of activity and and and
economic value whereas the remainder
have marginal economic activity and I
think this is actually a really
important case and scenario to think
through because when you look at these
Financial networks generally you do tend
to see Power law effects and I think the
scenario in which you have one or two
very dominant l2s the question about
where does where does the market power
and The Leverage between the l2s and
Main net at what Point might that flip
um and I think probably more work has to
be done on that
side so in in the final few minutes here
I want to talk about some of the
hypothetical conditions uh where l2s
could become more attractive more
more um so so the first is um about if
the L1 has limited transaction
processing
capability um and I think this is
important because I think first off the
economic situation of e the asset could
become more risky if the if if the
amount of fees that are being generated
on Main net um are not high enough to uh
ensure that a large portion of the
network ends up being staked I think l2s
also tend to benefit from highly
developed Financial system on the
L1 um and I think the second scenario
which I talked about a bit earlier is
the case where you have a power law
effect for L2 so for example a dominant
L2 would be the majority blob purchaser
and with very clever batching they could
potentially pin blob pricing below price
Discovery that's actually happening
organically today so if you look at how
the l2s behave in periods where blob
pricing does Spike we're already seeing
uh behavior that suggests that they're
willing to spread out how quickly they
sync their state
across time um and the consequence of
that is that users who might want to
look for a
unilateral exit from the L2 might not be
able to do that um if the if the l2s are
being more cautious and doing more
optimization about how frequently they
post the next hypothetical uh scenario
is a case where the incentive structures
for L2 tokens or non- eth gas tokens
become more prominent so if you look at
the breakdown of activity on l2s and you
look at the split between the l2s that
are using eth as a gas token and the L
l2s in quotation marks or l3s that
aren't using eth as a gas token today
that split is actually
every single rollup necessarily has to
you use eth as a gas token we're already
seeing some scenarios in which that
might not necessarily be the
case and I think that's related to one
of these other points which is the
notion of a siloed L2 with their own
settlement kingdoms for l3s or similar
types of similar types of rollups that's
another scenario in which um the l2s
might uh push for an alternative gas
token which again would not benefit eth
as an
asset
um and and I think the final point is um
potentially uh incentive structures for
l2s um in which they start to develop
competing security models in terms of
being able to use their native
governance token for things other than
just governance could potentially uh be
a condition in which the l2s could also
become more
extractive um so that concludes my talk
um I think it's still ultimately too
early to tell in terms of whether the
l2s are extractive or not the reason for
that is we've never actually seen a
scenario in which uh the l2s have been
put in a position to make a choice
whether they stay as an L2 or they use
an Alda layer or they become an L1 or
they do something else um but I think
that time is actually coming very soon
so probably likely over the next one
year we'll start to see some of these
choices being forced um just by the
nature of the blob fees going into price
discovery
thanks all right thank You Ren uh feel
free to come to the center over here
yeah this one will be fine so let's go
over some questions uh let's start from
the first one do you think the exact
copy of EIP 1559 mechanism determining
L1 fees is the right approach for
determining blob fees
yeah um I think this is a really tricky
question um so I think where my mind
jumps immediately is I look at the
amount of execution that has been moved
off of from the L1 to the L2 and the
amount of transactions on the L2 today
greatly outweigh uh the amount of
transactions ever in ethereum's history
in terms of like per second or per block
um but in terms of the denom or in terms
of e being used as a gas token for those
um it's actually quite minimal even
compared to like the earliest periods in
like ethereum's history so I think um
one of the things to consider is that
that ratio might be slightly off um and
I think the only way you really see that
settle is blob pricing has to go into
price discovery which means there needs
to be more l2s and that will likely
happen over the next year cool and
another question currently the L2
mainnet seems symbiotic but what if they
started paying fees in their own tokens
they have a fair amount of incentive to
keep assets logged in their system
without
interoperability yeah um I talked to
this point in the last slide about
hypothetical scenarios so I think some
of the highest forms of risk um are
exactly that so for example l2s in their
current state as having their tokens as
a governance token it's highly likely
that's it's probably more likely that
changes in the future than stays the
same so I think that is a that is a very
real
risk uh have you or others been able to
isolate the decrease in L1 execution
demand due to real transactions from the
reduction in call data demand will L1
execution demand go to
zero uh so I don't think L1 execution
demand will go to zero um so a chart
that I didn't include um just because
it's a very basic chart is that the
transaction the number of transactions
on ethereum has actually not gone down
and the amount of gas in terms of gas
consumed has not gone down it's that the
nature of the transactions have changed
so um historically the transactions on
ethereum had been uh transactions that
had a lot more right conflict or right
contention and right contention leads to
higher fees because people want to um
people tend to uh be rushed in terms of
those types of transactions so for
example like if people are trading uh
various forms of assets there's a high
degree of urgency that those
transactions land um um but most of that
activity at the moment at least has has
shifted to the l2s perfect and how to
prevent a single L2 from eating up all
the space or Spotlight AKA base not from
the tech perspective but from the
marketing public
perspective uh yeah so I don't
necessarily want to call out a single L2
um but I think uh the hypothetical
scenario of an L2 becoming the dominant
L2 where 80 to 90% of the economic
activity flows through there I think I
think that's a very real risk um there
hasn't NE I don't believe there's been
very many payment networks in the past
where you haven't seen a monopoly or
oligopoly type of structure just due to
the nature of network effects in in
these typ types of financial systems so
I think that risk is very
real perfect and I think this is a great
comment to close off the speech thank
you so
much all right thank you guys our next
talk will begin at 6
he
you w
wow hello hello how's everyone
doing wow high energy this is our last
Talk of the day so very excited we have
Remco bluman from the world Foundation
to give his talk on exploring proof of
personhood privacy Biometrics and why an
needs ethereum so a little housekeeping
rule we're going to have the QR code
here on the right right so feel free to
scan the QR code if you have any
questions for um Remco throughout uh his
talk um we will be addressing them at
the um very last five minutes so let's
give a warm Round of Applause to rco on
the stage
hello
Defcon so Remco from the world
foundation and I'm going to be talking
about a thing we're doing which is proof
of human otherwise known as proof of
personhood but that's a bit of a
misnomer we'll get into that and how we
do this in a private way using
Biometrics and why we need ethereum to
make that happen so quickly what is
proof of
personhood the short version is it is a
way to limit account registration to a
few ideally one per human
being um that in itself uh doesn't give
you any kind of privacy in fact it
usually gives you the opposite but you
can add a layer of zero knowledge proofs
on top of that to get a slightly richer
primitive which is being able to sign
messages as a unique Anonymous human for
example within some context you can sign
message proving that you are a human
being that has not signed a message in
this context before you could do let's
say hey dear project please claim my
airdrop to this address signed Anonymous
human or dear Dao please allocate my
voting shares to this particular vote
signed an anonymous human or dear faras
please register my handle as belonging
to a unique human being and not a bot or
dear forecaster and this is where it
gets interesting please register this
other handle as my ALT because it
doesn't necessarily mean that you're
restricted to One account per human
being you can have multiple accounts
it's kind of up to the application
developer to specify what the desired
behavior is it is a programmable
primitive that we're adding to the
blockchain
what is it not it is not very
importantly a
capture a proof of personhood does not
prevent a bot from doing something it
just means that this
action was
initiated and kind of signed off by a
specific human being so you can still
automate your
account now why do we want proof of
personhood at a high level AI will make
it impossible to distinguish on
behavioral features
alone at least in the digital
domain and AI fueled economic
disruptions require us to get much
better at creating human oriented
Financial Solutions to solve any
economic hardship that might happen in
world therefore we need to add
individuals as a programmable primitive
it is also critical to get strong
decentralization
because the only way to make sure that
many many people are involved in
consensus making is through a form of
personhood this in turn unlocks
Financial Primitives with a concept of
individuals and a lot of them have that
insurance loans pensions Universal basic
income none of these we can currently do
with programmable money because we do
not yet have programmable individuals
we're changing
that and that allows you to do cool
things that kind of I didn't even expect
when we started this like um the world
chain L2 that we just launched has
prioritized block space for humans so if
you're a human being you get priority
over the trading bots in the
sequencer and then of course there's the
basics like simple resistance and
preventing spam
bols now why would you not want proof of
personhood
unique human can often just be a proxy
for something more precise that is what
you really want like when it comes to
let's say under collateralized
loans you're not necessarily interested
in a unique human being you're
interested in someone's credit
worthiness and there might be better
tests for that that you could use
directly that would in the end create a
system that abstracts better what it is
aiming to do um you could also have a
like you could also Imagine a social
media platform where you don't really
care whether someone is a human or a bot
as long as they make valid meaningful
contributions to the
discussion so here again there is a
trade-off for the app developers to make
like is is proof of person not actually
what I need
here and there's kind of like a an
argument that you can make that um if
you really aim for maximal anonymity not
even the number of humans that are
currently in your system should be
transparent which is something that of
course prove of person not
achieves okay now that we've covered
what it is how do we build it how is it
constructed um the main problem you're
solving here is the Oracle problem
you're trying to build some information
in the platonic ideal cryptographic
trusted domain that comes from the
outside that comes in in this case from
the physical real world of
humans and solving Oracle problems
always means some form of compromise and
the question is what is the best
tradeoff for the specific problem you're
trying to solve the three main
approaches for proof of personhood are
Authority based where you use some
existing Authority like a government or
a email provider or a bank as a trusted
entity to
have a list of all the humans others are
graph-based um these are
decentralized and here you have humans
essentially verifying other humans or
you take some approach to pair wise
distinguish humans from each other and
then turn that into a larger grab I'll
get into more details on each of these
um in a moment biometric based is
recognizing that humans have a physical
body and doing measur ments on that body
to distinguish it from other
bodies now the authority based this is
the conventional solution this is what
the whole web 2 world the non crypto
World uses when they need anything
remotely resembling proof of personhood
for example when they issue you alone
they will ask you to K see yourself
using your government issued ID and so
on um this is an advantage because this
means that the average person is
familiar with them that a lot of people
have access to these means of uh these
modalities they're easily scalable and
easy to implement the downside is that
um they are imperfect when it comes to
uniqueness passports are relatively good
but still people have multiple passports
and definitely over lifetime people
renew their
passports they also have weak
inclusivity a lot of people don't have
access to these means and of course
there is the central Authority problem
we've all heard of sim swapping phone
numbers kind of suck in general for any
kind of authentication it's also active
um you need to go through this process
you need to actually make sure that the
person presenting you the passport
matches the document um you also need to
make sure that document itself is a
valid passport and not some copy and
this becomes substantially harder in the
digital domain and a lot of the current
solutions could do a better job on on on
these steps and if we don't deploy any
kind of of zero knowledge proof methods
in here of course it's enormously
revealing in terms of privacy
fortunately the rzk solutions for all of
these and you can get them to a very
high standard which is
great now the graph Bas ones their main
strength is it's decentralized that is
the the superpower of this particular
class of solutions the downside is that
uh the main downside is a so-called
click attack where you have a group of
bots that keep verifying each other as
real humans so you get a lot of signals
on these Bots that they're real humans
and once you have a network like that
it's very hard to get this out of your
graph BAS system um there's a couple of
different approaches here soci graphs is
an easy one where you just go to your
friends and provide proof to each of
your friends that they're all real
humans and you collect it from your
friends and this body of evidence built
up over time other solutions that don't
require you to reveal your circle of
friends um are based on video calls
where you either post a video of
yourself online showing that you're a
real human and then have other
people uh accept or reject that or you
go into Zoom calls with people cross
verifying each other that they are
indeed in this Zoom call and indeed are
are real humans and building the graph
that way um I think both of these are
very flawed ultimately because we have
deep fakes it's very easy to nowadays
create realistic video
calls um it's also just an awkward
non-scalable process um one that I do
want to highlight because I just think
this is such a clever solution is um
simultaneous capture solving so the
captas I mentioned before are designed
such that only humans can solve them now
if you through a blockchain or some
other means trigger um let's say five
people to solve a capture simultaneously
now you know that there's at least five
different people
there biometric base this is the um the
strongest approach it gives you near
perfect uniqueness it is nontransferable
you know that it is um this human and
this human
cannot give this modality away to some
other human or sell it or so on the
weakness is it's immutable it sort of
sticks to you for your entire life which
might not necessarily be desirable you
might want to have like some ability to
reset it also relies on trusted sensor
if you need a way to capture this
biometric information and and it
requires physical interaction the other
thing is the um so-called false match
non-match rates where faces with the
current algorithms are only unique up to
maybe a million individuals and after
that the algorithms will not be able to
distinguish them
anymore um same thing with fingerprints
they're not as unique as you would want
them to be irises however have an
enormous amount of entropy in them so
they work at a world population scale
and that is the main reason uh World
went in this
direction now two common Mis
misconceptions about Biometrics I do
want to address a biometric is not a
private key your fingerprint is in in a
sense not a secret like you you leave it
on every glass of every restaurant
you've ever been to and this fingerprint
is not what is you the thing that
authenticates you is the fact that you
have this fingerprint on a real life
finger attached to a living breathing
body the second thing is um irises and
retinas are not the same thing so please
get that right if you criticize
World um world's Approach at a high
level uh we have a tiered system we
recognize that there's different
trade-offs to these um modalities and we
offer a tier list of what we think
covers the whole spectrum of what you
might want we have the the orb you see
one right there which is a um Hardware
based biometric irisk based system that
gives you super high guarantees but um
you need to go uh find an orb in order
to sign up we're now rolling out um a ZK
NFC passport based system that gives you
high privacy and can leverage existing
national ID system and then we have have
a very low tier system that uses the
tees in your mobile phones to prove that
you have a unique mobile device now with
that last tier you can OB see the issue
there uh you can just buy more phones um
and that is kind of the thing with a
tiered
system you want to make your tradeoffs
as an application developer based on
what your needs are and how you want the
onboarding experience to be how did we
implement this so we make use of um
modern cryptography um generally when
state is local or Global or public or
private um there's different things we
can do but we now have a full set of
solutions here we can kind of take any
kind of problem and come up with a very
adequate solution the high level
strategy is we take our modality uh this
always starts with some form of um
trusted sensors either The Trusted
sensors are other humans in the network
or The Trusted sensor is an um um so The
Trusted sensor is an NFC chip in your
passport or it is the
orb the orb uh orbs are manufactured
they're registered on chain which is how
you can verify that they are authentic
through their public key these then
produ these then interact with the
user's wallet to produce uh secret
shares in zero knowledge so we
know that all of this is done correctly
and we now have secret shares of the
modality that we can then send to a
private uniqueness solution this is
implemented using multiparty
computation uh which also runs in tees
which also goes through onchain
governance and that verifies the
uniqueness critically it does this
without ever seeing the raw modality it
only sees encrypted and processes
encrypted data in the encrypted domain
which gives you a tremendous amount of
privacy here um it really sets a new
standard then we have um as a second
layer of defense for your privacy we
don't issue you some sort of ethereum
address that is now blessed we issue you
an anonymous credential you become a
member of an onchain set that you can
zero knowledge proof membership of and
this makes it such you cannot track the
behavior of any human that signed up
through the system you cannot um
associate them to the modality that they
signed up with and so
on now already covered the orb this is
our um very sophisticated device there's
other talks about this that I recommend
go in depth to how it works I do want to
highlight a little bit about the
challenges of doing this biometric
uniqueness check in in multiparty
compute the scale is enormous we're
talking about a 24 Nvidia h100 GPU
cluster that uh requires almost a
terabyte of GPU memory and terabits of
communication bandwidth just s to
sustain the 8 million users that have
signed up at a rate of 10 new users per
second multi party as you may know has
trust assumptions it is important that
the nodes are operated by non-colluding
um entities for that we are working with
reliable third parties we found they
operate the notes for us the world
organizations do not have access to
these
systems and as a further layer of
Defense we have uh we have developed
techn technology that allows us to run
these Cuda MPCs on gpus in tees so
inside trusted execution environments so
that they can prove that they're all
running the pro protocol honestly and
they cross verify each other before they
even initiate the protocol then the
question is okay what protocols are they
allowed to run can they do a uniqueness
Check Yes um maybe in the future we want
other functionality we want have people
the ability to recover their accounts
through a biometric for example that
requires some form of governance that
can then onchain sign off on what are
the allowed protocols to run which
protocols meet the criteria for privacy
and the commitments made to the users so
this is where Modern cryptography and
ethereum specifically programmable
consensus are critical in making all of
this work now to summarize World ID
offers by ometric passport and
device-based proof of personhood tiers
you as an app developer can integrate
this depending on your needs we
implemented all of these such that the
modality the actual underlying
information never leaves the user no one
outside of the user learns about the
passport learns about the iris or
anything else and then we have this
additional layer of zero knowledge based
anonymization on each use so even if you
have a dowo where you have a one person
one phote you will not be able to track
voting patterns of users each vote is
individually unique by
default but of course as an application
developer you can ask the user if you
want different Behavior
here now covering some next steps um the
we've recently rolled out mini apps
which is a good way for people that have
a a a a use case that requires proof of
personhood to immediately reach an
audience of millions um as I mentioned
we have World chain which is our L2 that
uses by default get an account on and it
it is um experimenting with ways that we
can integrate individuals and humanness
in how sequencers prioritize uh the
transactions and how fees are allocated
we're currently working hard on in
improving the technology of client side
proving to get really fast clients side
proving so on device on on your mobile
device producing zero knowledge proofs
and we want this because there is a big
future in doing programmable zero
knowledge identity meaning that not only
can you prove that you're a unique
person but you can prove things about
yourself you can prove that you're of a
certain nationality you or not of a
certain nationality or um of a certain
age and so on without revealing anything
else about
yourself um and with that I want to open
the floor for any questions thank
you all right thank you gu thank you so
much for the amazing talk we do have
five minutes to go over some of the
questions that people submitted so it
would be great if you can come here in
the center yes so let's
go from the very first one at the top
what if human creates a proof and sells
it to AI as there's no identity attached
and it's zero knowledge proof there is
no consequence to sell the proof or Keys
associated with
it that is correct um and that is
intentional like I said this is not a
capture this is uh you're still allowed
to have a bot operate your account but
if you were to do this um you cannot buy
pass rate limits for example you would
still be a single account on whatever
system you're running it on so if you
want to bless your if you want to run a
Twitter bot as a unique human you can
but if it starts spamming the system it
is obvious that it is one
account cool and what if World ID system
gets hacked or becomes hostile on its
own AKA Evo warb so World ID as a system
is a set of smart contracts and a self-
custodial wallet um that doesn't mean
it's unhackable but it means it's
subject to the same assumptions as
hacking an ethereum hacking the ethereum
network and hacking a self- custodial
wallet um but the other question about
the orb itself is a good one um and the
way we tackle that is uh like I said
through transparency in how the orb
itself operates on chain so first of all
the orb is fully open source uh open
Hardware open firmware um it has a
removal SD card so you can verify the
build and so on they're all um
registered on chain
and while the process of users and the
user signing up is entirely Anonymous
the behavior of the orb is not so it is
public how many um um signups a certain
orb does and if there is any suspicious
behavior that can be flagged and the
multi-party compute setup can actually
revert these fraudulent
signups uh another question is Iris
froto hard to capture can it be scanned
when I'm sleeping no it cannot is
actually um surprisingly hard uh the orb
um despite being open Hardware
unfortunately contains um custom Optics
uh that you can't really get off the
shelf you need to find someone
specialized in making lenses to get this
done it's it's it's a hard problem of
getting a high resolution picture of of
something the size of a sugar cube that
is bouncing around a meter and a half in
front of you uh and the ARB does it it's
quite amazing um this is a good thing
though uh because this means that that
there is a strong form of
consent um cons yeah kind of consent in
getting your iris pictures taken it's
very hard to take Iris pictures of
someone who doesn't actively and
willingly participate in the
process how does World earn income I
pass no really um this is we we
currently don't have any uh any issues
uh here um Everything is Everything is
in production everything is running and
this is such a the the space of identity
is such a gigantic opportunity that goes
Way Beyond the entire current crypto
space um and then itself the world
project will on board already on boarded
tens of millions of people into into
blockchain but on board many many
more um how about artificial fake irises
the orb could theoretically think it
registers real humans yeah I think I
haven't covered enough how important it
is for any kind of biometric sensor to
fify that it is a it's not enough to
just take a picture of Iris or a
fingerprint you need to make sure that
this is from a real life living
breathing human body because otherwise
it could just be someone holding on an
iPad or someone trying to squish a
silicone mold on a fingerprint scanner
the the hard part in designing any kind
of biometric system is not so much the
capturing of the raw data but it is
invalidating that it is actually came
from a real human
being cool uh we have 30 seconds to go
through one more question can someone
with an orb produce IDs for non-existent
irises no the um even if you have an orb
in physical possession
it is um near impossible to to make it
do those kinds of things it it has like
a very strong amount of physical
security in it and temper protection and
so on all right cool so I think that
concludes our talk today from Rimco
let's give another round of applause
Remco for his talk to end the day
yes yes um thank you everyone for coming
just some closing remarks um how does
every want
feel oh amazing so thank you guys so
much for attending today's talk um
tomorrow the talks will begin at 10:00
a.m.
so usually we start at 10:00 a.m.
sharp so see you guys
there thank you
it's all your oh really on the same
stage right
me
[Laughter]
o
oh
e
m m
m
is
oh e
is e
e e
