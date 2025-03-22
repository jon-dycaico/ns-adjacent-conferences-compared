whether it's zero knowledge proofs
multi- party FHA IO how to mix stuff
like frogs how to use zass how to use
like kind of like the next um version of
the data stack of zerox Park there's
going to be a lot of cool stuff it will
be split into two rooms with two
workshops running in parallel I will
give more details on this later but the
important thing is this morning it's
talks this afternoon is you do stuff so
uh we only have 30 minute break before
between the morning and the afternoon so
it's pretty important if you want to
come back to be back on time next slide
please um this morning we have four
talks the first one would be from
vitalic on the far future of
cryptography then we will have Albert KN
on also the future of cryptography but
this time on the real The Surreal and
the super real Barry wad will come next
with a whiteboard on stage to do some
white boarding and we will close with
goop sheep on contact next slide please
so the afternoon will start at 12:30
p.m.
the lunch break is only 30 minutes
so please be back on time we will have
as I said before four workshops two of
them running in parallel the first set
of workshops will be multi-party fully
homomorphic encryption in practice and
the other one will be programmable
cryptography from a software engineering
lens next slide please I will break them
down next slide
please so the first Workshop will be
from 12:30 p.m.
to 2: p.m in breakout 3
so that's this room um the main content
will be a workshop from GOP sheep on
extending the Frog zone so if youve been
to the Frog shop downstairs and You'
have seen like this this these two
tables with four computers each and
you've played this game where you little
frog trying to kill the dragon that's
the Frog Zone uh goop ship calls the
Frog Zone the slowest and most expensive
video game ever made the Frog Zone
requires about 1,000 CPU cores for four
players to run in parallel um in a bunch
it's all running in a data center in uh
Singapore actually close by and uh
gubship will walk you through okay how
do we add new features to the Frog Zone
like this application is pretty crazy
from the cryptography devops client side
perspective so he work through doing
that and we'll have a bunch of
additional talks on mpf rewriting the
cryptography library that is used by the
Frog Zone and so forth next slide
please the other Workshop that will run
in parallel in breakout 2 which is a
much smaller room so it will be first
comes first served will be a workshop by
from myself on part two which is um
basically a new way of expressing data I
can compose using both formal proof and
zero knowledge proof so we will work
through how we built it how to use it
Etc and then we'll have a bunch of
additional lighting talks around how
what was part two put together from the
circuit perspective uh we'll have a talk
from aish Gupta on ZK email which is a
way to import emails as cryptographic
data and we'll have a talk from Kevin
quar on the construction of the hardware
frog which is this little chip that you
might have used to get Cyber frogs next
slide please we will have then two
workshops running in parallel after
these two next next
slide one on building consumer apps with
programmable cryptography in breakout 3
so that's here at 2:15 p.m.
you only
have 15 minute break between the first
batch of workshop and the second batch
we'll have two talk on two application
built with the Zupas API and pods in GPC
and then uh a talk on how the fogs were
put together a talk on how to import
pods on chain and a talk on how mircat
was put together which is the Q&amp;A
application you probably have used
throughout the conference next
slide and F no that's
previous okay the title is wrong it's
not programmable cryptography from a
software engineering ALS the last
Workshop is on iO so the main content is
going to be a workshop from Barry White
Hub and jamama jaaya mall on the io
Bounty Deep dive that they've announced
this week and then we'll have two other
talks on uh cryptographic assumptions
from for iio and Oram which is another
tool in the cryptography stack next
slide so that's it these are the four
Workshops the first batch will start at
at 2:15 one Workshop running here and
Breakout three and one Workshop running
a breakout two if you're interested in
breakout two workshops please be on time
because the room will probably get full
next slide so up next we have our four
speakers and with that I will give the
stage to vitalic thank
[Applause]
you okay um
[Music]
okay great so the far future of uh
cryptography um
sorry next slide okay great so I think
first know we'll talk we'll talk about
the uh very recent uh past and I think
still ongoing pres of cryptography right
I think uh the biggest change that we've
seen over the last few years is
basically the way that SARS have really
taken over everything right and one of
the analogies that I've used is I've
thought of SARS as being similar to a
Transformer right so this is know the
gbt architecture that's now famous from
AI land and the analogy here is
basically that if you think about what
GPT did right it basically took a whole
bunch of different use cases for which
thousands of people have been putting in
years of hard work years of application
specific algorithms application specific
data Gathering application specific
expertise and it just like swept all of
that away with just a really dumb system
where you just like put like take half
the internet like throw it into a funnel
and then like run the G run a bunch of
gpus for a while and it just manages to
magically outperform all of them as a
general purpose architecture right and
snarks you have done basically exactly
that same thing for cryptography right
so we've
seen ring signatures we've seen range
proofs um you know we've seen all kinds
of different use cases just basically
swept away and subsumed under this
umbrella of I am just making a proof
about a computation about private data
that is expressed as some kind of
standard um arithmetic circuit in a
standardized language and that you can
you you can make a fair a fairly short
proof that just proves whatever claim
you want to prove about private
information that you have in zero
knowledge and oh at the same time it
also solves scalability right so it's
this extremely powerful general purpose
technology and the ethereum road map has
already changed completely as a result
right so if you look at the plans that
ethereum has for the next few years all
of the far future stuff really uh
depends on Sonar existing the uh road
map for replacing veral trees with
something Quantum safe depends on Starks
the uh road map for long-term full light
clients depends on Starks the and
rollups started off being optimistic
rollups and now there's ZK rollups and
they demand on Starks or depend on
Starks they're um also plasma before
sarx it was a a very limited
architecture that that could only do a
little bit after snarks it just be it
actually has become something quite a
bit more powerful so snarks have really
overturned everything and in a lot of
ways they've also simplified a lot of
things right like if you remember trying
to design protocols in the prear era
like you really need specialized
cryptographers putting in a lot of
specialized cryptographic work to make
specific applications work whether it's
range proofs or it's ring signatures or
it's linkable ring signatures or it's
cheli and blinding every one of these
Primitives would require
a cryptographic professional to do a
whole bunch of work and even still you'd
only make something that works for a few
particular sets of applications snarks
indiv non- cryptographers can just go in
and they can do their thing put in their
code and it just works next slide so
let's talk about what happens what
happens Beyond snarks so in one of my
recent posts talking about the future of
the ethereum protocol I made this uh
analogy to these uh Egyptian god cards
from yuil right is like extremely
powerful monsters that just have these
incredible Powers right and uh you know
in Yu-Gi-Oh Legend these cards are so
powerful that it's physically dangerous
to actually attempts to create one of
them and that you're not actually
allowed to use them in Du right and uh
like these three protocols I think are
exactly that powerful in the same way
right so we talked about sarcs but let's
talk about the other two items in the
series right so the one in the middle is
uh fully homomorphic encryption fully
homomorphic encryption lets you do any
computation on encrypted data without
being able to learn anything about that
data this is extremely powerful this
basically lets you take a very wide
class of applications and just Express
them very easily as an FHA problem I
have private data and I want you to do
an algor run some algorithm on the
private data and give me the results
without um actually learning my private
data that's an FHA problem um I want to
be able to train on people's data
without learning the data that's also an
FH problem you do need a little bit of
cleverness to make sure that like the
thing that the model actually learns
about you doesn't uh actually itself
reveal your data and like that's a
differential privacy thing right but the
bulk of the hardness like actually is
just captured by the fhe piece if uh you
want many kinds of like privacy pres
preserving architectures privacy
preserving Dows as long as you're
willing to accept a certain certain
trust assumptions it becomes an FH
problem f is like actually an incredibly
powerful technology another thing that
it gives you actually is uh uh it gives
you private information retrieval so the
ability to make queries against a
database without the database learning
what you're asking for and one use case
of this is uh privacy preserving light
clients right so you can have an
ethereum light clients and your like
clients can go and like ask for like
some piece of data about history without
the server actually learning what you're
asking for so very powerful stuff but
you know we also have to get to the
third Egyptian god protocol which is
alisation right you can encrypt a
program in such a way that the encrypted
program has the exact same functionality
but if you have a copy of the encrypted
program you can learn nothing about the
internals of it like basically except
for what the inputs and outputs are now
technically like that exact definition
is uh like not exactly achievable but
like in real like for any realistic use
case it's like basically close enough to
that right and so alisation lets you uh
be actually do everything that FHA does
but it lets you kick out like even more
of the of the trust assumptions almost
all of them you can do down that have
secrets you can you can actually use
offis cation to implement basically any
other cryptographic protocol you can use
offis cation to implement encrypted mols
you can use offis cation to implement a
ZK SAR scheme where verifying the SAR
only requires verifying a signature um
it's it can uh let you implement like
any kind of uh FH MPC two party uh
two-party computation it's uh like
basically is a superet of like almost
everything else cryptographic so in
order to try to make this a little bit
more concrete let's look at voting as an
example right so I think of voting as an
example because I mean obviously voting
is important in itself but also voting
um to me is like a standin for basically
any kind of onchain mechanism that that
is not purely financialized right so me
I yeah I wrote this is like one of my
own fra uh Frameworks right so I wrote
an article about this um I think this
was uh the one on Nathan Schneider's
cryptoeconomics or coordination good and
bad but the B what I call financialized
is basically mechanisms where you don't
mind people arbitrarily colluding and
one example of this is like if you
compare money to let's say like like
likes on Reddit right if you think of
money I give you a dollar in exchange
for you giving me a
is not a problem it's working as
intended on Reddit or on Twitter I
upload your post and in exchange for you
uploading my post especially if it got
optimized to Infinity would just
completely break the system right and so
if you want to support any kind of
mechanism that is not financialized then
like that means that you have to be able
to prevent uh collusion in some way at
least make it difficult to trust and
that requires as it turns out exactly
the same type of uh properties that
voting requires so let's look at voting
as an example so base case put it on the
blockchain so what does putting it on
the blockchain give you right it gives
you public verifiability so anyone can
check that the result was computed
correctly and it gives you censorship
resistance if you're an eligible voter
no one can stop you from voting so it's
a good starting point Dows have been
doing this for a very long time very
basic now of course voting on The
blockchain has a lot of problems so
let's talk about adding cryptography on
top let's add
casar keep the previous properties but
you also and you keep public
verifiability but you and uh you also
have censorship or resistance okay sorry
I wrote this incorrectly um the thing
that you add is privacy right basically
if you vote then no one will uh be able
to tell who like which person made a
particular vote you'll still be able to
see the contest of the votes but you
will not be able to see like who
actually made a particular vote right
and this already is a very significant
privacy gain it already makes uh many
types of collusion much uh much much
harder and like it's already a really
significant Improvement right but it's
still not enough right and the reason
it's still not enough is basically that
if you really wanted to sell your vote
then if you made a CK snark you could
still prove to someone else that you
voted for some particular candidate very
easily so let's add the Macy mechanism
the Macy mechanism does not rely on any
new cryptography it keeps the previous
properties but it also adds coercion
resistance right and assuming that the
server is honest so assuming that the
server is honest you add this new
property which is that you cannot prove
who you voted for even if you wanted to
make that kind of proof and this adds
like a very large friction against
actually trying to implement any of this
kind of bribing because basically either
they have to do some kind of like side
Channel attack against you directly as a
voter or they actually have to like
attack the server now let's add fhe
right so with fhe you keep the previous
properties but you if you add FHA
together with threshold decryption you
can make the coercion resistance
guarantee only depend on an mfn
assumption so instead of relying on one
operator you can rely on potentially
like say seven operators out of which
like four need to be honest right now
there are voting protocols that have
existence that's why 2002 that have
given all of these uh properties
depending on an mfn assumption with
simpler technology but those protocols
they gave all of the prop all of these
properties under that assumption this
kind of design actually gives uh um
every property except for corosion
resistance an even stronger guarantee
and if you do it with general purpose
cryptography it generalizes much more
naturally to any voting system you're
not if you H have a system that's
designed for doing simp simple vote
counting you can switch it over to doing
quadratic voting quadratic funding with
like a few lines of code you can switch
it over to doing pairwise bounded
quadratic voting a few lines of code you
can switch it over to doing cluster
matching a few lines of code you can
switch it over to doing the community
notes bridging Matrix factorization
algorithm with only the lines of code
that you need to actually Implement that
Matrix factorization algorithm I me if
you want to do it efficiently it's a bit
hard but the algorithm itself like
basically about new lines of code right
so FHA basically together with sarx you
actually create this like very general
purpose uh design and you keep all of
your all of these properties that you
want out of a voting system except cion
resistance depends on an M an assumption
which is like not ideal right because M
out of n can still collude silently and
they can collude silently they can like
pass all of the information over to the
NSA and uh like no one would be able to
actually tell that any collusion is
happening so now let's add aisc so with
aisc you can keep the previous
properties but you can make you can make
it so that extracting or proving any
information at all about individual
votes requires blockchain consensus and
you can even make it require some amount
of proof of work per bit of entropy that
you extract so how do you do this
basically when a user votes instead of
sending their vote to a a threshold key
um
or like FH encrypting it to a threshold
key they FH encrypted to a key that is
inside of an offis gated program and uh
the so this is a trusted setup but but
there are ways to make the trust setup
be one of one of N and you can make the
N be like extremely large right so f um
encrypted into this key that's held
inside of a program and then that
program only gives the total output of
all of the votes and in order to give
the the total output at all and even
there it's not going to give the full
number it's just going to give like the
one bit basically who won right and or
potentially a few more bits if it's like
quadratic funding right and the way that
this program works is it Tellies the
votes and it also checks that there is a
proof that the blockchain consent has
finalized it and on top of that it also
can check for like some little amount of
proof of work right so you could do it
like say like $500 worth of proof of
work or you could imagine like ethereum
eventually adding like maybe like
$10,000 proof of work on every finalized
blocker like some simple uh simple
amounts right and so then even if the
blockchain consensus all colluded um
even if like everyone colluded they
would only be able to extract a very
small number of bit of bits of entropy
from the system right and so actually
deter and then you can also make the
program add a little bit of gy and know
noise and so extracting any information
about how an individual voter voted will
basically just become extremely hard so
this is like very close to Ideal right
so but there's more so we'll talk about
onot signatures oneshot signatures are A
Primitive where you can make you can
have a key where that key can only be
used in order to make one signature one
such signatures require users to have
quantum computers so this is a milestone
that will come at quite a bit after the
bad guys have quantum computers right
when quantum computers come they're
going to be like hundred million dollar
things you know the the bad guys or at
least the people that we consider
threats will have them first right and
so you'll have to wait quite a bit of
time after that until regular users can
also have quantum computers right but
you do is what what this ISS is
basically you know you can have a public
key and it's a mechanism by which it's a
public key such that the you for any
given Nots you're only allow it's only
possible for the owner of the private
key to sign exactly one message with
that Nots and this all depends on the
quantum no cloning theorem right if you
have a Quantum State then you cannot
actually copy the quantum State there's
mathematical proofs that this is
impossible and the signature scheme
depends on solving a problem which is um
infeasible with classical computers but
doable with quantum computers and so
you're basically like Pro proving that
you have and that you're spending one of
these unclonable Quantum States so this
could actually be used to make Quantum
money without a blockchain now it
doesn't remove the need for blockchains
completely it still doesn't solve
sensorship resistance on its own but
this is the thing that like I'm not I
don't want to call an Egyptian god
protocol because like this is not just
in the land of computer science this is
like in the land of physics right and so
it's like it's some kind of tier that's
like even more powerful than these
things
so when will we get all of this
technology right so zekia sarks we're
seeing an increasingly high level of
maturity I mean I personally look would
declare Victory once we're able to
actually have ZK EVMS that are proving
blocks within one slot currently we're
probably still like a couple of orders
of magnitude away from this but there's
a huge amount of progress there's a huge
amount of work in binary field proving
systems like basically the race is on um
f we're starting to see iable
applications so if anyone here was at H
City you probably got one of those like
Square wristband things and there was an
application called cursive where
basically you could provide a list of
what your interests are someone else
could provide a list of what their
interests are and actually used FHA to
compute the intersection so we're
starting to like see toy applications
that like right consumers can actually
use on local devices the FH has roughly
a million Factor overhead and so you can
run business logic inside of it but you
can realistically you canot run
cryptography inside of it right so it's
like at that interesting level where
it's like you good for some things not
it's still not good for a lot of things
it's uh you know in that middle Zone
alisation the big news over the last few
years is that we're starting to see
viable protocols in 2020 there was the
first protocol that was dependent on
only standard assumptions and this
protocol someone actually tried to
implement it and they discovered that it
would take 10 to the power of 27 years
to run a year later someone created a
slightly improved protocol and someone
else started to implement it and they're
estimating that it's going to take one
year to run now there's also a separate
line of work that's trying to make offis
protocols based on slightly more exotic
assumptions and it's like actually more
debatable in the long run whether this
is more or less secure right because
it's like on the one hand you have more
exotic lattice based assumptions that
are like based on multi-linear mapin
instructions and like zero testing and
like that whole line of stuff but on the
other side you have like Normy
assumptions about lates I mean you know
go go out and like ask anori what they
what they do in belt lates right that
kind of stuff um and but at the same
time you have to like assume and that
and eliptic curve pairings and like one
or two other things right and so but
that stuff you know if you want to
office get a program it takes like a
couple of weeks right and then one shot
signature is obviously no idea
definitely a long time and we'll see
Quant of computers break half of
existing cryptography including anything
lip to curve based long before this
actually becomes possible so basically I
think the takeway is that all this stuff
that was like extreme science fiction a
decade ago is like slowly coming into
view right every single piece is like
with every single passing year is
becoming slightly more and more clear
and I think we can actually really start
getting excited about these things right
and we get excited about a world where
cryptography actually can get to the
point of in a general purpose way
actually being able to replicate the or
replace the functionality of any
interested third party and uh I think
that future will be amazing thank
you thank you vitalic um so we will do
three minutes of Q&amp;A uh we have the Cure
code here you can scan to both add
questions and up vote questions um there
are only two questions so far and one
was I I'll start with the fun one which
is vitalic if you played the frog game
and if yes how many frogs have you
collected unfortunately not this time
I've had like zero time to do anything
other than jumping around Devon stuff
but but but here it's been fun um okay
what advantages will the snark ification
of uh the beacon chain um have I mean I
think uh the big the big one is
basically that you will have light
clients that will be able to fully
verify the ethereum protocol right so
like on your phone on your watch
anywhere anywhere that you wants to do
things with ethereum you'll be able to
like actually fully verify the rules of
the chain and uh like you'll be part of
the mechanism that ensures that the the
chain and like even 51% of the of the
stakers are not changing the rules on
you and uh that's uh so and this will
all just like happen passively and
automatically um to invite me to a
conference to speak out how does one go
I'm not not answering um one signature
on the book possible not answering can
we call beam chain ethereum 3.0 I think
no and I think this is like an important
misconception right because I think like
a lot of people like got this weird
Twitter impression that like oh you know
in the be the beam chain it will only
happen in
nice Ivory Tower Properties about the
consensus layer and so it doesn't even
mean anything for users and like this is
ethereum 3.0 right and the reality is
like very different from that right the
beam chain is only covering the ethereum
consensus layer which is only like maybe
one3 or one quar of the ethereum stack
right the execution layer that so the
evm has its own road map and then layer
own road map and uh even on the
consensus side all of the key things
that are actually meaningful for users
so especially getting dank charting um
up I think can happen a lot sooner than
uh
what do I think about tees I mean I
think they're definitely interesting for
some uses though I think it's always
important to remember that like they
depend on a lot of trust in specific
manufacturers and they get frequently
broken right and so you wants to use
them for like applications where they're
either just additive in terms of
security or where the cost of them
breaking is like not too high right you
don't actually want to use them to like
literally replace cryptography so you
know use them responsibly um
what can on shot signatures plus sisc
plus blockchain not do it cannot give
you true love thank
you thank you
vtic so while our next speaker um is
going to prepare the connection with
their laptop um I've been sent to
entertain you guys
so uh one thing I found interesting with
vitalik's presentation is when you start
listing down these cryptographic
protocols one by one um you don't need
to like scint your eyes that hard to
kind of like see some form of
mathematical computer emerge right like
each of these Primitives are synergistic
with each other um as an example one
primitive V did not talk about is or Ram
oblivious RAM and one thing that's
interesting with that is the same way in
traditional computers we could put all
of our state in CPU registers but we
don't because they're hella expensive
and we have like you know multiple
layers of storage we have CPU registers
Ram uh blog storage network storage Etc
it's probably going to be the case that
with cryptography we will have to do the
same so while some of these protocols
can technically do everything we'll
probably compose them with each other in
order to like reap the best performance
possible and so who knows maybe in a
decade we will have cryptography
computer Engineers whose entire job is
to build computers out of polinomial and
not out of silicon uh which and they
will one thing I was thinking about
yesterday night when I couldn't sleep is
who's going to be the TS m c of
cryptography you know kind of like a
polinomial Constructor For Hire that put
together the biggest cryptography
computers um I will also check with a if
we're ready we're ready okay cool so I
will introduce our next speaker to the
stage um so Albert NE has been many
things to many people at both the
theorem foundation and zerx park but
above all he's someone who pushes us all
to think in more Direction and I think
he's going to do that yet once again
with this talk title the future of
cryptography the real surreal and super
real thank you
Albert like I said we have to do
this there we
go all right hi everyone thank you
Justin for a uh very fitting intro today
above all I want to share some
interesting ways I think about the
future of
cryptography some many perhaps are ways
people have not considered um this is
going to go to some interesting places
as the title hints at but before I dive
in I want to emphasize that while I want
folks to consider more directions the
point is not to replace how you
currently think about things this is not
new thinking in a totalizing sense it's
not declaring it's not even predicting
at least not in the that people usually
interpret the concept of talking about
the future this is just thinking
creating awareness for what may be
possible and may be true because
sometimes that awareness is what makes
something unexpectedly possible we don't
have much time so I'm going to talk as
fast as possible uh just kidding but
seriously buckle
up so part one the
real let's start with some easy stuff
things many of you know if you've been
exploring modern cryptography here are
some slogans if you will come for the
encryption stay for the signatures or
come for the security stay for the
interoperability like today https is a
statement of security but maybe zps or
pctp programmable cryptography transfer
protocol will be a statement of
possibility how about this come for the
nuke proof paint stay for the
superconductor we've known for a long
time that cryptography is digital nuke
proof paint but but it's the
superconductor aspect that we are only
beginning to realize and
understand now I want to go in a bit of
a different direction here's a quote
from Steve Jobs recorded in the book
Valley of Genius an oral history of
Silicon Valley that I'd highly
recommend one of many things that stands
out from this quote is this phrase
medium of
expression today what is the thing that
this thing we call computer techn ology
what is it a medium of expression for
consider all that's been built around
computer technology especially the
companies the organizations the products
the institutions what are they
expressing or this is a bit more of a
leading question what have they become
everyone senses something has gone a bit
ay with our relationship with the
digital a relationship that's largely
mediated by what we broadly call
computer
technology and so I want to take this
immune system lens when we think of the
word immune system we naturally think of
our physical immune systems this
predates literally Humanity itself but
for much of human history there's also
been this implicit notion of an
intellectual immune system you could
also consider calling this a
philosophical immune system think about
how you respond intellectually to
various things how that's changed
developed over time sometimes it
strengthens sometimes it's probably
weakened kind of like your physical
immune
system what about the digital right now
we think of digital stuff in terms of
security and protection but as our
digitally anchored and oriented
experiences become increasingly
intertwined with our lives perhaps the
notion of an almost organic digital
immune system is a way to think about it
notably a digital immune system
conceptually wouldn't even have been
cogent a 100 years ago probably less
it's simply much newer almost primordial
so we need to remember it's going
through things that are more associated
with the very early stages of a system
or ecosystem
developing for instance one might say
that the interaction between the
physical and the digital currently leans
parasitic this is partly because we
haven't realized the full potential of
digital Technologies and and I guess the
digital realm to be more symbiotic with
our overall existence but I think this
can and inevitably inevitably will
happen especially as our intellectual
immune systems co-develop or co-evolve
with our digital immune systems remember
one of the most underrated things about
evolution is that symbiotic coexistence
is literally a more effective
equilibrium than Total Takeover this is
true even when the specific organisms
fundamentally remain in competition such
as predator and prey if the Predators
start doing too well they crowd each
other out same goes for the prey now you
might think okay cool digital immune
system cryptography that makes sense the
connection is relevant but that's not
exactly where I'm
going what I want to consider next is
literacy consider this word and why it
even exists it used to be notable when
someone was literate as in could read or
write for most of History it was rare or
definitely not universally expected for
people to be literate that's why the
word exists to point out an unexpected
thing of course today it's notable when
someone is illiterate it's not just
notable it kind of feels wrong like
Society has failed that person keep this
in mind going from default illiterate to
default literate happens all the time
off then slowly then
quickly one of the most well-known
company slogans of my childhood was from
Bill Gates and Microsoft as you can see
the slogan was a computer on every desk
and in every home 30 plus years ago this
sounded incredibly ambitious it was
almost awe inspiring as it turned out
this was nowhere near ambitious enough
should have been a computer in every
pocket computer with you at all times a
computer the first thing when you wake
up the last before you sleep computer
while you're on the toilet when you're
in a meeting or attending a talk a
computer every where at all
times computer literacy as in being able
to make use of a computer for your needs
was rare until very recently when I was
a kid aptitude with computers was
actually loow viewed as low status
phrases like computers are for
secretaries were common today everyone
below a certain age is computer literate
but not in the way that you might have
naively expected 25 years ago and it's
definitely not that everyone now knows
how computers work it's that every
computers became a thing everyone knew
how to use thanks in large part to the
iPhone and the subsequent smartphone
Revolution again default illiterate
becomes default literate but how it
happens is often hard to predict even
when the iPhone came out many thought it
was going to be a total
flop consider also how the concept of
photographic evidence has only existed
for like a hundred years imagine telling
someone in 1850 that there's a
photograph or video or audio recording
to prove or disprove their version of
events today that idea is entirely
second nature most of us have never
known a world without it of course
there's a storm bre brewing with
progress on what we call AI because we
don't know what else to call it the
current concept of photographic evidence
definitely won't last another 100 years
might not even last 10 if you naively
extrapolate you might think we're going
to revert to the world of trust me bro
just like all of history before the
photographic evidence
era but naive extra almost never
actually plays out a couple Generations
from now cryptographically grounded
evidence will be second nature to people
the same way iPhones made computers
second nature to kids today the same way
photographic evidence has been second
nature for decades but it's not even
really the cryptographic evidence era we
kind of have that already to some extent
it's the cryptographic literacy era
remember literacy doesn't mean Mastery
and widespread cryptographic literacy
doesn't mean widespread understanding of
how cryptography graphy Works similar to
how I noted earlier that widespread
computer L literacy doesn't mean
everyone knows how a computer
works still what's really going to
happen is not actually going to be
thought of as cryptographic literacy
what will it be thought of
as I consider this one of ital's most
underrated blog posts should be pretty
easy to look it up given the title
within the post metallic defined
legitimacy as a pattern of higher order
acceptance Loosely speaking people
expecting other people to expect the
same things and therefore we can all
expect
something recall that smartphones are
what unlocked computer literacy they are
the form and mechanism through which
computer literacy became near Universal
for cryptographic literacy or legitimacy
literacy the form and mechanism is
something we don't know yet what is it
that makes things more high order
accepted in this broader sense product
and Technology Innovations will unlock
this future and I bet some of them will
feel just as surprising as the iPhone
would have felt just 30 years ago to
someone still being AED by Bill Gates's
computer on every desk
Vision also remember the value of the
wheel it was unlocked by the invention
of the axle people weren't idiots they
long noticed that round things can move
more easily but that's not what it takes
to make use of the wheel we don't know
what the axles are to cryptography's
Wheels
yet one consequence of all this is that
something that feels like cryptographic
writing will exist I'm sure it won't
feel literally like writing combined
with cryptographic signatures in fact we
already have that but what's important
is it'll have the property of being
inherently higher legitimacy than
conventional digital writing we will not
think of all things written digitally as
being more or less the same this is
already true to a limited extent
depending on the context but the
distinction will be much more
substantial and there will be a
reflexive feedback loop that causes even
more widespread legitimacy literacy
throughout Society all of this will
contribute to another shift in how
people feel about cryptography even if
they don't know that's the thing that
they are feeling something about
so everything so far I've put under the
real now I want to start to segue
towards the super real to do that first
I want to revisit some miracles of
science here I'll Loosely Define Miracle
as something where if you didn't know
something existed or was possible it
would be very surprising that such a
thing exists just as it would be
surprising if magic existed my first
example is fire the existence isn't a
surprise since it spontaneously occurs
in nature but the ability to control
fire was a significant development to
say the least
next is electricity this one is a bit
surprising I guess people had seen
lightning but what reason was there to
believe that this thing could be harness
that it would turn out to be magic juice
that moves infinitely fast and basically
gives us permanent light communication
across vast distances or to be able to
construct things like
computers then there's nuclear power
which was I think truly a surprise like
wait a second effectively infinite power
is everywhere mass is literally
energy but there's one more source of
quote unquote power that gets overlooked
because it's a fundamentally different
type of power each of the first three
Miracle power sources can be viewed as
as symetric offense it's a lot easier to
burn something to make than to make it
fireproof and we know how powerful a
nuclear weapon can be but as I noted
earlier cryptography is digital nuke
proof paint cryptography is an almost
infinitely powerful defensive or
protective technology and the fact that
it's the digital superconductor is like
the icing on the cake so I do think it's
reasonable to consider cryptography
of Science and one reason is because
cryptography is a physical realization
of the potential of
mathematics now let's consider the four
fundamental forces of the physical
Universe we've got gravity a force that
was definitely apparent to humans since
well before we were humans then there's
the electromagnetic force which was the
fact that that was a force was not
actually really clear until about 200
years ago then we've got these two crazy
forces that operate at Atomic scales the
weak force and the strong force we
actually didn't even realize they
existed until the 20th century and we
didn't confirm how the weak Force
functions until like
all there's even like a digital strong
force strong nuclear force parallel here
you know cryptography holds things
together at a level that overcomes the
inherent collapse of Digital Data kind
of like the strong force overcomes the
repulsion that positively charged
protons otherwise would experience when
packed together in an atomic nucleus so
that's why I wonder if it might be apt
to think of of cryptography as like a
fifth fundamental force of the universe
especially a universe that is
increasingly becoming a combination of
the physical and the
digital and so that takes us to part two
the super real and I I like this
particular definition of the word marked
by extraordinary
vividness so if cryptography is a force
of nature then to actually utilize that
Force requires implementation our dat
day us usage of electricity isn't just
some like General usage of the
electromagnetic force you know there's
voltage there's how what decisions
around batteries alternating versus
direct current and so much more there
are a lot of specific things so when I
say Crypt here what I'm gesturing at is
the specific form that of things that
actually harnesses the cryptographic
force this is one reason I kind of like
to think of cryptography as a digital
duel to physical realities electricity
the transition we're undergoing can be
likened to the transition from a world
that only knew fire to a world where
electricity is everywhere back when
people only you fire if someone told you
about electricity that we could somehow
harness lightning you might imagine
better lights better heat perhaps better
cooking ironically because fire is
actually better than cooking for cooking
in a lot of situations you can imagine
lighting up a city and heating a city
but you wouldn't really imagine powering
a city you wouldn't imagine computers
the Internet or that electricity
actually kind of runs even through our
brains you wouldn't you definitely would
not imagine artificial intelligence and
you definitely wouldn't imagine
cryptography so in the future digital
stuff such as data computation
information transmission that makes use
of programmable and other future
cryptography will feel like electrically
powered objects in comparison to what we
have across the web today Computing that
is cryptographically charged or maybe
Enchanted is far from what we currently
think of as Computing same with data
that is cryptographically Enchanted and
Beyond now why is this even more
important than it might seem at first
blush because the tech industry as of
now has philosophically flattened in
fact we can see remnant of the higher
dimensional space it it fell from if you
look at any Tech startups pitch they
pretty much all still contain a mission
and the mission is never build the most
valuable company now if you've ever seen
a hedge fund like a new hedge funds
pitch deck they never have a mission
it's all business it's how they're going
to make the most money the whole tech
company Mission thing at this point is
kind of a Remnant from a philosophically
higher dimensional era of Silicon Valley
and at the same time and not
coincidentally while computer technology
has improved dramatically it has
regressed from the standpoint of how it
feels counterintuitive
counterintuitively using computers going
back to like Doom or civilization 1 or
the well or IRC or Ain or text-based
multi-user dungeons in many ways felt
more expansive and enriching not that
things were anywhere near perfect back
then don't get me wrong but there was a
hard to quantify feeling of moress that
feels so different than how the web
feels now it's fascinating a how
differently and in so many in some ways
better I felt using a dialup modem with
terrible bandwidth and latency than I do
now on my 5G pocket superc computer now
a common response to this is technology
is bad and we need less of it I'm open
to that perspective but I don't think it
should be a totalizing one we've got to
also explore how the digital can return
to being an expansive and enriching
experience we've gone from it being
symbiotic to parasitic how do we go back
to being symbiotic that's the real game
and the future of cryptography plays a
vital necessary though certainly not
sufficient role in this and it's why
looking at cryptography strictly through
the lens of what it can technically do
is
incomplete instead or in addition I
think we need lenses such as this no one
today thinks of cryptography in terms of
nourishment um it might sound crazy but
I think we not only can but perhaps must
think of it in these terms because only
then can we potentially discover or
realize that it's actually a valid way
to think about it we might even find out
eventually it's the only only natural
way to think about it and as for
enrichment this is a cryptocurrency
conference so I want to emphasize I'm
saying enrich you know kind of like the
soil got enriched and we were able to
support much more people on Earth not
the uh the other one um one last lens
from the super real is how can
cryptography help us reenchant the
digital it's not just now we can do
programming on cryptography even if that
is very cool it's that cryptography
itself is fundamentally a bridge between
math and physics between the digital and
the physical and perhaps between
computation and lived
experience so finally I want to spend a
quick few minutes on what I'm going to
call The Surreal I've got a quote here
from Italo calino um that closes with if
a new world were discovered now would we
be able to see it and the definition of
surreal a definition at least is beyond
reality so I want to start somewhere
again probably a bit unexpected what's
the greatest invention in the history of
mathematics in my opinion it's the
polinomial the ancient Greeks Romans
Chinese they were all excellent in math
but they were held back by not having
something like polinomial
representation but here's the
interesting thing about polinomial even
though they were invented close to a
thousand years ago and even though they
were instrumental to things even like
the invention of calculus we didn't
really understand how awesome they were
until around 200 years ago what happened
then we got the first rigorous proofs of
a theorem about polinomial that's so
important we call it the fundamental
theorem of algebra
the thing about the fundamental theorem
of algebra is it doesn't even work if
you only have real numbers it only works
when you have complex numbers and it
turns out pols are just one of many
things that make way way way more sense
with complex numbers that's why I say
the most unbelievable realization in the
history of mathematics and arguably the
world is that reality itself consists of
more than just real numbers that the
real numbers were nowhere near all that
was required to Simply describe and
reason about reality accurately complex
numbers show up everywhere from
Electronics to fluid dynamics to quantum
mechanics and more what's more the reals
themselves became more spectacular once
we completed or algebraically closed for
those are who are familiar with that
notation once we completed the reals to
form the complex numbers e goes from
being the number that's defined as like
the derivative of e to the x is still e
to the X to being a fundamental basis of
rotation in the complex plane Pi goes
from circles being cool to being far
more significant in part because the set
of points equidistant from the origin
becomes far more interesting in a
two-dimensional complex plane than on a
one-dimensional number line where you
just have X and negative X and that's
barely scratching the surface of
examples so consider this if the real
numbers aren't the full picture of
reality should we expect anything else
to be does the digital the internet the
web and perhaps more not really make
sense until we complete it with a unit
of cryptography as the reals were to
form the
complex if physical realities built on
physics can we enrich a complex super
Reality by bringing elements of the
physical into the digital realm just as
we've clearly brought elements of the
digital into our physical existence and
can this be a symbiotic relationship it
almost can't not be to actually feel
like super reality is there a complex
big BL bang will it look like a Genesis
block or something else is cryptography
where silicon based life really comes
from and what's more real places in the
physical Universe we can literally never
reach like we get light from plac places
that are so far that if we traveled at
the speed of light towards them because
the universe is expanding we will
literally never get there what's more
real those places or places in this
perhaps more vast complex reality that
we actually can visit and so the last
thing I'll say is in science fiction you
know we see this phrase outer World
sometimes will we one day think of outer
realities and I wonder when we hear a
voice from an outer reality what we will
look like by then and who will be
listening and so I'll leave you with
this final note as we uh take a few for
Q&amp;A thanks a lot for
coming thank you
Albert so to start the Q&amp;A session the
first question is how does cryptography
as a fifth Force interface with the
firmy Paradox are all the aliens
encrypted yeah I love this question
actually because I've always thought the
firming Paradox was a little bit simpler
than people make it out to be because
the key is why aren't we observing
things and given that for example we can
observe an ant farm
without it having any sense that we're
observing them there's a pretty big
assumption that it should be like that
easy to observe stuff out there so
that's not exactly what this question is
saying but I just kind of wanted to
point that out like what if you could
cryptographically be like encrypt your
mind onto like neutrinos and then flow
through everything maybe that's
happening right now and maybe that's
where things will go so even just at
that level like cryptography has helped
me with my thinking around the firmy
Paradox not saying that's the answer but
I think it's people kind of skip over
the whole like oh of course we'd be able
to see it even though it's actually it's
like literally trivial for us to observe
life that is probably closer to what we
are than you know maybe more powerful
intelligences are to us thank you Albert
um reminder that you can scan the C code
to ask questions we still have two
minutes of questions so many things you
can ask Albert um there's one question
want vot which is what's your suggestion
for individuals to contribute to this um
so this can mean a lot of things right
it can mean you know a lot of the stuff
that people are showing here or it can
mean the thing that I just talked about
but I will actually focus on what I just
talked about I I think as simplistic as
it sounds my goal here is for people to
recognize that sometimes just taking a
moment to think about things can be
surprisingly valuable that sounds really
obvious and yet like how much time is
spent trying to just take a moment and
think and the talk here the goal of
nothing else was to give an example of
how many directions that can go in and
and not in a way where I'm like I'm
trying to convince you of something or
or sell something or anything else like
that so think you may be able to
contribute more than you expect by just
taking a moment to think about what you
know and what and your perspective and
see how that might intermingle with
stuff as for other ways I think there's
a lot of great opportunities to ask
folks about that overall so we'll go to
the next one thank you um anyone you
care more about what you want to
answer um sure I'll go with how do you
see cryptography contributing to an
Internet that is joyful symbiotic and
expansive to use um I don't have much
time but the quick answer here is uh the
physical world has a lot of properties
we take for granted and if nothing else
we're evolved to like Orient around that
even the fact that like non-f
fungibility is like default on in the
physical world and we need like
sophisticated constructions to make
things like essentially fungible like
words are fungible in a sense two apples
are more or less fungible that's only
because we've gotten good at putting
them all in a market and so on the
digital world has like these inversion
of a lot of properties so if nothing
else I think cryptography uh is
underrated its potential to enrich
because it's a way for us to imbue the
digital world with physical world
properties and that's a lens that I
think we haven't really explored much
yet yeah there's the fungibility
scarcity stuff but I think there's a lot
more to go in that direction thank you
Albert thank you another round of
applause for Albert please thank
you all right so we have a special treat
next or next speaker is Barry White Hat
a self-proclaimed Street cryptographer a
longtime collaborator with the EF and
zerx Spark Barry will wideboard out his
thoughts on how to build with IO and
more um I always a treat to hear what
he's cooking up please welcome to the
stage Barry White hat thank
you okay folks H can you hear
me okay okay we're going to do some
whiteboarding stuff um so like basically
the plan for today is to like architect
some simple things using
IO um can I turn this around so like do
people have things that they would want
to architect so like a couple of things
I was thinking about doing is like how
to do a how to how to oh p goes the
other way how to use uh zero knowledge
how to use iio to uh to make zero
knowledge proofs that are just like a
single signature to verify so you have
this IO box it it does some stuff and it
spits out a signature and like once you
check the signatures it's enough it's
enough to say to to to know that that
computation was Onre directly so that's
one thing that we could do other things
we could do is like a a trusted
setup uh other things we could do is we
could do like a Bitcoin Bridge which is
kind
of more block
chainy uh anything else people want to
do this is supposed to be like
interactive so feel free to like shout
stuff out and interrupt me like I I want
to have more of like a conversation here
than like a a
presentation Asos gxy oh no that's too
much can I encrypt my thoughts and send
them as neutrinos across the Galaxy uh
not
today anything else okay well if there's
nothing like just shout at me later I'll
ask you again in a while so let me try
turn this
around oh yeah it's
okay okay so basically the toolbox of IO
is that we have like some program that
we express as like Gates
and we have some ins and some outs and
then we do like the io
thing we do this IO kind of like almost
like encryption step and on the other
side we get like a whole bunch of whole
bunch more Gates or more more
information and it still has ins and
outs but the like what's happening in
the middle is impossible for us to
figure out so this you can think of this
as like an encryption step that takes
program it encrypts the program such
that the
output is like unknowable it's like all
you can all you can do is like put stuff
in and get the
outs and you can like see stuff that's
going in and coming out but you can't
figure out like what the original
program
is uh so one example of this okay so
let's take like a really simple example
and let's say that our gate here is just
like
a uh and gate
yeah so we have a really simple program
as an and gate and we put it into our IO
encryption
box iio and then we get out this like
more complicated
representation right so this is this is
also just like a list of like operations
like M maybe it's Matrix multiplications
that's what uh schemes
ADP uh and Matrix branching programs you
tend to use but maybe it's just like
other binary Gates that's the local
mixing schemes tend to use those so we
get this encrypted format of our program
but we have like blackbox access to it
right so we can put inputs and we can
get outputs so like this one this one
takes just two inputs but there's like a
whole bunch more gates here and the
gates are really
complicated so we don't know what's
happening inside our circuit but we are
able to do like blackbox access so I can
just put like I can just because there's
only two inputs I can just go just
calculate the whole truth table right
because I have the encrypted program I
can just put in 0 and I get out uh I
don't know what I don't know what the
truth table of and gate is well let me
try and guess so 0
that's it source of Truth this is and
gate okay so we can just like uh these
are ins
out okay so we can we can just put that
in and and like that's XR oh
 huh we good yeah
okay okay so we can we can just go
through and like do the whole uh State
space enumeration and we can find out
the truth table but we don't know if
this is actually an anate or it's a more
complicated circuit but like what I'm
getting at here is that like you're able
to you have blackbox access to the thing
right like the goal here is to try and
build up this model so you're able to
sit down and be like ah I can I can
imagine how to make things with IO okay
cool okay so let's do our first example
then of our
zkp right because like I don't know if
you've seen the kind of like tree of uh
different the tech tree of different
cryptographic perim
but IO is kind of the the one at the
very top because you can use it to
implement all of the others so like as a
way to just introduce the concept let's
do zkps okay so let's say that like oh
yeah let's introduce this other model of
how to think about it
so so we have our setup which is what we
just talked about and now let's talk
about like how we think about the io box
so we have this IO
box okay the io box do does some things
right so the first thing that it will do
that it does is it it does some like we
can Define some computation we wanted to
do and then given that the computation
succeeds we get the io box to produce a
signature so this is kind of like an if
if
computation I have to move over to the
other side then produce the signature so
if the computation succeeds then produce
signature so like this IO box has been
encrypted and I have given it to you
right so you have this box on your
computer you're able to give it any
inputs and the output you get is a
signature of something okay maybe the
signature is maybe we just signed the
computation right so basically if we
want to make a zero knowledge proof what
we need to do is we need to I have other
colors we need to take this computation
we set that to be whatever the whatever
the the the thing we want to prove is
right for example if you want to prove
that you have like 10 signatures from a
certain public key what you do is you
take your I box you set the computation
to be the verification of 10 signatures
and then you have this Clause that like
well if 10 signatures are here produce
this other signature and pass it out so
one important thing to remember is that
we have a secret inside the io box yeah
so let's do
secrets we have secrets inside our IO
box and inside our IO box what are our
secret our secret is the uh the the
secret key of this signature right and
we have this uh it's not secret we have
the public key so at the at the setup
phase what I do is I create this IO box
and I do the encryption step that we
talked about on the previous slide and
and now what I
do is I I publish the public key and I
say hey look if you ever get something
that's signed by this public key you
know that it has passed this this check
right because the only way that you can
produce this signature is if you execute
the io
box okay so this is how you do Zer
knowledge boost do we have any questions
so
far yes there we go
so the question is how do you trust the
output of the iio box if you don't know
the computation so like I'm using the
computation as like a placeholder here
but like when you do the setup you would
Define the computation and you would
sort of show people that like oh this is
the thing that I set up so like iio
inherently has this kind of like setup
phase which you can think of as like
similar to the zero knowledge proof uh
trusted setup where you set up the
circuit and you set up the com the
program that you want to prove but you
also need to set up the kind of like
private key right you set up the private
key and you you publish the public key
and this is like part of the of the
setup that you need to go
through good anything
else okay oh Jordy oh no okay all right
later Jordy um Okay cool so this is how
you do Z know proofs uh so like a quick
aside is there any other things that
people are interested in architecting we
have 10 minutes so I I have enough stuff
to go through but if there's something
people are specifically interested in we
can think about
them okay well feel free to interrupt me
if something comes to
oh Dow signing things okay let's do that
then at the end um so you want to have
oh so you want to have like a dow that
that has a private key and it wants to
sign things but like what's the point of
doing that is it like a you want to have
an
EA EA is externally owned account like a
private key for a dow but like I don't
like the the reason I'm I I don't I'm
concerned about doing this is that like
well you can just have the Dow be a
smart contract and you can just verify
the smart contract did something as
opposed to like verify the signature of
something but like maybe Jordy means
that he wants to be able to have stuff
encrypted for the Dao that the Dao
can
yeah uh so Jord saying that he has he
has an external file he wants it to be
encrypted uh but he only wants you to be
able to decrypt the file if you send
funds to the Dow right yeah and and this
and nobody knows I mean this file was
encrypted and nobody knows the key
except that yeah yeah yeah okay okay
okay this is kind of like is this
witness encryption I'm not sure but yeah
okay we can do that let's uh let me what
was the other things I had written down
here okay trust setup okay so let's do
the trust setup and then we'll then
we'll talk about Jord thing okay
okay
so okay so historically like we've done
trusted setups for a whole bunch of
different ZK applications and this
basically means that we like gather
Randomness from a whole bunch of
different people and then we compute
this kind of like uh special key that
has certain properties and basically
what I want to talk about now is how we
can use IO to do that uh in a way that
we don't need
to in a way that's that's like more
programmable that we can have this like
Universal setup that we can gather
Randomness and anyone is able to use
that Randomness to do whatever they want
with so here's how we do it uh so again
we have our IO
box okay and our IO box does some
compute and if the compute
succeeds it produces a
signature of the
compute okay but in this case it will
also uh encrypt
something encrypt the output of the
compute
yeah and it's also able to do like a
decrypt so this is kind of like similar
to what Jordi was was getting at so it
takes a input it decrypts it
uh it it uh oh hold on I want to put
this the compute at the end I want to
put the signature at the end so it gets
an input it decrypts it it does some
compute on the
thing and then it uh encrypts
it and it signs
it and that's that's all that it does
this is our whole compute so it takes an
input it does this and it outputs the
signature and it also outputs the uh
this
out also outputs
out okay so like it's important to
remember that like the io box is created
with the with the process that we
described at the very start where you
have some some like binary circuit you
like encrypt the binary circuit and you
have this like encrypted circuit that
you're able to execute but you're not
able to like understand or comprehend
you're able to do like blackbox stuff to
it but you're not able to see you're not
a able to see what's going on inside so
this is like the the the core API of IO
and this is the thing that you like once
we combine this with the ability to take
to make signatures we have this like
authenticity that we're able to use the
bootstrap basically the
whole almost everything that a trusted
party can do so like one way to think
about this is that like you you have
like a trusted party like IO can be like
a really trusted trusted third party
right where you can just say to the io
people the io box hey do this thing and
sign this thing and then just give me
the signature and because no one is able
to see inside or affect what's happening
inside this becomes a really powerful
tool that we can use to build like all
the systems that we ever wanted like
imagine that if you could really trust
Facebook or if you could really trust
like these internet services that's kind
of what we're getting at with IO okay so
how do we do the how do we do the random
number how do we do our random number
generation so basically what we do is we
we we we have this box and then we say
to people that like okay you take a
random number and encrypt it and put it
into the box and then Inside the Box the
Box will you encrypt it uh I have to put
the secrets here so we have a public key
and a secret key these are secrets so no
one knows the oh well no one knows the
secret key but everybody knows a public
key so basically the user encrypts for
the public key they put it into the iio
box the iio Box does the compute where
it decrypts it it it it combines it with
the with with the previous Randomness
that that was oh we need to have two
inputs right one is not enough so this
is input from the user and this is input
from the current state so you have two
inputs so it takes the input from the
user it decrypts it it takes the input
from the state it decrypts it it joins
the two random thises together and then
it encrypts the output and it it returns
that and assigns that so this is the so
then what we do is we make it like a
chain where like we have like this iio
box kind of pass the value to the next
one which pass the value to the next one
and like what we're doing is that we're
just stacking Randomness up on top of it
of itself right and this is kind of like
phase one of our trusta setup where
we're generating this random number that
no one knows and like the assumption is
that like if any single parity uh
includes uh honestly passes a random
number then there's no way for anyone to
to to know like to to to to calculate
the random number right because in order
to calculate the final random number you
need to have all of the intermediate
random numbers okay so this is how you
generate the random number then like we
have to make another box to actually use
the random number because like with the
with the trust setup that we've
historically done they need to have a
special property uh it's not enough for
them to just be like random or whatever
they need to be able
to they need to have this like for the
TR for the powers of to it needs to be
like the G to the x equals G to or gt to
the to the x or something like that I
can't remember but like it needs to have
a special property so we just we just
make another IO box that does
that so the io box has the same kind of
like uh uh public key and secret
key so we have the same
secrets so it's kind of like these two
these are two different trusted parties
and they're able to talk to each other
so this one encrypts some values for
this one and this one takes those values
and some stuff with them and then we can
have like our arbitrary compute
here and we do our compute and we and it
and it outputs the actual Tres
app okay okay how is this any
questions
yes I think secret key is included in
iio box but is it make able that no
one's know that secret key yeah that's
an important property here that we have
to make sure that no one is able to know
the secret key and that's one of the
properties that we get from the like the
encryption Step At the very start yeah
so this is like a programmable
encryption oh thank
you
yep hello so if you are uh ofos K in the
program does the programmer have any
advantage by knowing the actual program
and if so like how can other people
agree that the program is correct if
it's
sophisticated yeah okay so this is I saw
this in in one of the this is a question
earlier uh that vitalic didn't answer
but yeah I I think this is a good
question so basically like in general
what we would do is we would publish
most of the program the the only thing
that we really care about about about
hiding is is is what this person was
getting at that all we care about hiding
is that is a private key like we're okay
with someone like the property of IO
that we care about is not that the
program is like indistinguishable it's
that the private key is
indistinguishable like in most cases we
want to tell you everything about the
program we want to explain everything
except the private
key
cool uh so questions like some intuition
for the the blowup so if you let's say
you implement CPS with this iio box uh
and then if you have a more complex CP
how does it relate to sort of the
exponential blow up like what is a good
intuition for how how much say efficient
it become as sort of the logic inside
this box
changes oh so it seems like you're
asking two questions here like one of
them is like what's the overhead of IO
and the other is that like is could IO
potentially be competitive with zkps in
terms of like Pro time with are you
asking both or are you asking one of
them
on the logic inside I
box huh it's basically both questions
that you you okay okay let me answer
both questions then uh so the first
question is that it depends upon the
Assumption like different I different IO
schemes have different overhead like
some of the more like extreme
assumptions are actually pretty pretty
efficient in terms of execution the
setup is the main
cost um but it remains to be seen it's
still very early so I can't really give
specific numbers or whatever um I'm not
sure if like I suppose that like the
thing that you're gaining from the io
zkp is the succinct verifier the
verifier is really easy it's just
verifying a signature so it's much less
overhead than traditional zerge proofs
uh which tend to be like a couple of
pairings uh the best gr 16 or F Lan is
like a pairing and like some other scal
mes and stuff so it's better uh it's
faster verifier but the appr time is
likely going to be like really a lot
worse at least in the short term uh but
it depends on the the assumptions that
we end up using or the bases that we're
end up building things on so not really
clear yet I don't think that Zer
knowledge proofs need to worry about
anything anytime soon I think that they
are going to remain like this is more an
example like this is more an example of
what you can do I'm not saying that like
oh this is what we should do yeah okay
Barry it's Q&amp;A time ah okay sorry Jord
no it's great that was the first
question um I'll read them from the ones
with the most votes but feel free to not
answer or skip to the next one okay um
the top one is can you explain IO as
explain me like I'm five and why do we
need to use IO instead of other KPS ah
ah like oh you know what like I feel
like we got into so much trouble cuz we
abused the zero knowledge proof not or
name for such a long time then that like
this question just it's hard for me to
understand what this means by like other
Zer not proofs because I suppose that
this person is thinking that like oh
they just have this blanket term for all
like privacy technology and that's zge
proes so ah so I think that the key
thing that iio gives is a non-
interactivity I think that like that's
the missing piece of of the puzzle but
zkps are that people use are non-
interactive I think I think the person
doesn't understand that yet that zkps
cannot do everything far from it yeah
yeah zero zero knowledge proofs are a
single player technology iio is a
multiplayer technology this is what
we're this is what seems interesting
about this we can take the other one
which is how do we get from weeks to
seconds for Io uh I suppose we just have
to like try more we haven't really tried
at
all um I think I don't know no like I
mean well come on I know like we just
need to work on
it you heard that just go work on
it the next one is what are exotic
cryptographic assumptions
oh I think they're like more like like
do they want examples or they want like
the vibe I I just think they want to
know what you mean by that ah so there's
like standard assumptions which are
assumptions that people have made for a
long time all like all cryptography is
based upon assumptions because like
there's this open problem in math that P
is not equal to NP and that basically
means that like some things are hard and
some things are easy so because we're
not able to prove that some stuff is
hard and some stuff is easy we're not
able to prove that any particular thing
is hard and because we're not able to
prove that any particular thing is hard
we have to base everything we're doing
on assumptions we assume that things are
hard so there's different things that
people assume there's things that been
people being assuming for a long time
and people are much more open to these
assumptions because we've been making
them for a long time but then there's
newer assumptions that are more radical
uh that that that and those are what I
mean by exotic assumptions yeah and if
you're interested in that uh Brian
Lawrence will give a talk about that in
one of the workshop the iio workshop so
there will be a talk about cryptographic
assumptions um so that's it we're
running out of time thanks everybody
thanks
folks and with that I will introduce our
next speaker to the stage goop sheep um
gship is one of the co-founder of zerx
Park and the creator of Dark Forest
please welcome him to the stage thank
hi everybody thank you for joining us
this morning for the programable
cryptography
CLS uh the title of my talk today is
contact and I'm going to be explaining a
little bit about what that means
shortly as a quick introduction I'm gub
sheep I'm one of the co-founders of Dark
Forest uh I coined the term programmable
cryptography about two years ago and
ever since then we've been exploring a
lot of its consequences
so this talk is going to be a little bit
more of a mental models and Frameworks
talk it's not going to be a a
whiteboarding session or a session where
we go deep into the cryptography um we
are going to hear more about the
technology in this afternoon's workshops
uh and what we're going to do in this
talk is you know we're going to look at
some history and some worked examples of
how we've come to build up even the ways
that we think about programmable
cryptography um at the end we'll also
tag on some highly uncertain speculation
of what we might do with those works in
the
future okay so the title of this talk is
inspired by a Sci-Fi series this is the
culture series by Ian Banks raise your
hand if you've read or heard of these
books oh actually it's pretty Prett
pretty decent number so the premise of
the culture series is that explores
adventures in this universe where this
transhumanist post scarcity Society
exists and you know it's sort of there's
a uh G galaxy-wide culture of all of
these humans or transhumans that are
involved in this Society um and one of
the most interesting sort of agencies
that exists in the culture civilization
is the contact Division and what the
contact division does is they're the
ones who are essentially at the
Frontiers or the fringes of the
civilization uh handling all kinds of
interactions with any other
extraterrestrial life or intelligences
or things that they're finding at the
fringes and one thing that I kind of
want to prompt is what does it look like
for ethereum or applied cryptography or
programmable cryptography to have a
Contex Activision what does that look
like okay so let's first take a step
back and ask what are we trying to do
here with programmable cryptography um
the the various organizations the
various individual contributors the
various people thinking about
programmable cryptography you know what
is what is sort of the goal here with
programmable cryptography we've seen a
couple of instances of goals maybe it's
realizing the the real or the super real
or The Surreal um one framing that I
really liked actually from Albert's talk
and that you know I've been thinking
about a bit myself as well is this idea
of programmable cryptography as a fifth
fundamental force and as we saw in
Albert's talk um cryptography represents
a set of extraordinary new capabilities
that would a priori seem impossible much
like how something like nuclear
technology or the ability to harness
electricity might have seemed impossible
as well and my question in terms of what
do we actually what are we doing here is
we're trying to figure out how to even
grapple or come to terms with this how
do we even think about this what does
this enable what are the right mental
models for this technology techology
what will the different path
dependencies be to realizing this what
are the right abstractions for the
technology and how do you design the
interfaces between each level of the
stack here um in short you know we have
to we have to Grapple with the same
problem that nuclear technologists had
to Grapple with you know in the last 100
years are we first going to make a bomb
or are we going to make infinite energy
and what are the sort of cross-
dependencies both technologically and
socially that are involved in figuring
that question out or something like
Computing you know it's it's very
non-obvious in the days of something
like the aniac one of these giant room
scale computers that the descendant of
this 60 70 80 years out is going to be
something like you know virtual worlds
like Evon line where hundreds of
thousands of people are battling in a
virtual space reality for control of
virtual space planets right how do you
even begin to start thinking about what
might take you from the left hand side
to the right hand
side okay so there's a lot of stuff that
we could do that that wouldn't make
sense um in particular easy to Rabbit
Hole down one particular kind of
programmable cryptography technology uh
or to Rabbit Hole down like one
particular sort of use case or or
product or something like that but
ultimately it's really important to to
keep a solid head on your shoulders when
you're approaching this question because
this is a decades long civilization
scale technology and we need to approach
it and and take it seriously as such we
need to build some foundations mental
models in a way that takes seriously
that a mental model needs to be useful
on the time scale of potentially decades
that doesn't mean we need to get those
mental models exactly correct today but
how we think about this should be
credibly progressing us towards the goal
of understanding how to think about this
from a from a multi-decade civilization
scale kind of
scope now the other thing you have to
avoid while doing that is you have to
avoid getting sucked into the perfect
system trap especially in a way that's
not grounded in reality so the other
thing that we could do is we could be
like all right programmable Crypt graphy
allows us to do this crazy stuff this
crazy stuff with Turing machines with
these crazy guarantees let's sort of sit
down and and theorize for that theorize
about that for a really long time and
build some sort of like crazy like
category Theory type Theory like you
know correct by construction sort of
thing um and then you know that that's a
real mouse trap too we don't want to go
down that rabbit hole but somehow we
still want to be making progress knowing
that this thing has as Grand of a scope
as it does okay so I want to talk about
some of our thinking on how we've
approached this problem over the last 5
years so beginning about 5 years ago we
started to get the sense that there was
something interesting happening in
cryptography we didn't have the words to
describe it we didn't have the the
Frameworks you know nowadays people talk
about the idea of oh you know ZK enables
data interoperability that was not how
we were thinking about ZK at all when I
started building a game called Dark
Forest in 2019 the way that I was
thinking about this was I had just
learned about ZK snarks from Jordy
actually and I had this idea wow you
could use zero knowledge proof and
blockchain to build this really specific
and very strange game so dark forest was
a game built on zero knowledge proofs on
blockchain um it was one of if not the
first non- cryptocurrency application of
zero knowledge proofs and it just seemed
like a total one-off hack at the time so
um we spent this time we spent some time
building uh Dark Forest and what we came
to realize was actually there was a
general principle going on which is that
zero knowledge proofs were not just
enabling this one specific game
construction they were enabling this
idea of incomplete information games or
games where players have some private
State on a blockchain or on a
decentralized system where the whole
state is public so that enabled us to
you know that that came through building
a bunch of other prototypes of of some
other games this is a screenshot from a
game we built called boat fight um and
unlocking that realization allowed us to
suddenly see what was going on with dark
forest and this category of games and
suddenly it became actually a lot easier
to build the different kinds of features
and even figure out what kind kind of
features we could add into Dark Forest
so for example you know early on into
the game we introduced this idea of
procedural generation that was enabled
by this mental model unlock of what ZK
was fundamentally doing
here okay so then we get into uh so dark
force was at 20120 this idea of
incomplete information was about 2021 in
a second can we apply this principle
across a bunch of other kinds of domains
not just games so you know we built a
bunch of these circuits we built um
thing we had folks in the Xerox park
community ecosystem building things like
private message boards um ZK reppel over
here is a developer tool for working
with zero knowledge proofs there's
stealth drop which was like private air
drops and we got the sense that what was
going on was you know the Common Thread
between all of these things and between
the game thread was this idea of
programmable privacy right and I I use
privacy in quotes here because I I sort
of am referring to a specific
connotation of privacy which is oh I
want to hide something I want to have
anonymity or pseudonymity or something
like that
and we kind of distilled this down into
this idea that ZK snarks turn
cryptography problems into programming
tasks it was much like what vitalic was
sort of saying in the morning where uh
we don't you know need a cryptographer
to invent for us a new protocol for
every feature you can have someone write
code and compile that into
cryptography okay so from there once we
had this notion of programmable cry
programmable privacy we were like well
let's step on the gas pedal here the
point is now a bunch of people can make
privacy preserving applications and
those people specifically don't have to
be cryptographers so we got a bunch of
people together started bringing folks
into this ZK ecosystem and we produced
things like the first zero knowledge
machine learning demonstrations stuff
like hanon with pseudonymous or
Anonymous speech ethos which was the
first demonstration of recursive zkps in
a consumer social graph kind of use case
um things which would allow you to Port
RSA identities into zero knowledge
proofs and so we did probably like you
know 5 10 15 of these projects and
that's what got us to arrive at this
other concept called proof carrying data
the idea that actually the thing going
on here with zero knowledge proofs is
not something about privacy or
scalability like yes those things are
very relevant particularly in the
blockchain context but after building 10
or 15 of these apps we realized that
what the zero knowledge proofs were
fundamentally doing that was a Common
Thread in each of these apps was they
were enabling permissionless data
porting from Source a to destination B
so now you can move things like a GitHub
Identity or an email or anything like
that from this Destin um from this
origin Source over to this destination
without needing to call apis or things
like that okay so that gets us to proof
caring data um we built this framework
called the proof caring data software
framework so this is a mental model that
then got actually translated into a
library and the beginnings of a software
abstraction and then we started building
a bunch of stuff on proof carrying data
so this is kind of the the the Blind Men
and the elevant sort of thing we
realizing that all of these eight things
were instances of this common
category um so a lot of our proof caring
data experiments led us to Zulu which
was a community that wanted to adopt
decentralized identities cryptographic
identities work with cryptographic data
and we built this thing called zup pass
which everyone here has used to
basically uh claim their ticket generate
a zero knowledge friendly identity um
and store zero knowledge friendly data
and we built a bunch of apps on top of
this concept of proof carrying data with
zoo pass as one of our levers so we have
things like you know the frog game you
can make zero knowledge proofs about
your frogs we had Zoo pole which was a
polling app for the Zulu community that
also expanded to a couple of other
communities zcast or zookat which were
these social sort of private social
Message Board apps for these communities
um just these various different
things and we built a bunch of pcds
proof carrying data uh instances and we
tried to build a bunch of stuff with
them and then we ran into more limits
and then we started to factor out well
what are the common threads where those
limitations are holding us back and this
is what really led us to programmable
cryptography so for example with proof
carrying data and with ZK snarks we
could only enable individual people to
make proofs about operations on their
own data but there are a bunch of places
where we would want say two people or
multiple people to be able to jointly
compute across data that I have in my
zup pass and you have in your zup pass
and that led us to realize oh there's a
very natural connection with these other
of general purpose programmable
cryptography Primitives like multi-party
computation and more another realization
that we had was that even though we had
this abstract concept of proof carrying
data PCD um it was actually in practice
really hard to use pcds what we'd have
to do is we'd have to write one more
bespoke circuit for every kind of
cryptographic operation or every kind of
you know proof carrying transformation
we wanted to do and so we ended up with
this whole repository of all these
different circuits and PCD types um and
we were back to kind of square one on
well you do need a cryptography aware
developer uh in order to even be able to
engage in this
ecosystem so that led us to programmable
cryptography um which is the subject of
this community-led session here today um
and concretely what it means to say it
led us to the mental model of
programmable cryptography or this this
way of thinking about programmable
cryptography is it allowed us to figure
out what the problem was and what the
capabilities would be un what
capabilities would be unlocked if we
solved those problems
so you know me and Andrew we took a look
at all the stuff going on with pcds and
we were like well this needs to become
generalizable and this needs to become
much more flexible so now we have pod
and pod 2 as a result which we'll learn
about more today in the afternoon
sessions um we have uh yeah if you can
go to you can go top.org to see sort of
the latest on that um and then we
started carrying out other experiments
to see well now that we've been led to
this next line of Investigation what
what what might we do if we take FH or
obfuscation or these other Technologies
to their logical conclusion so uh this
Devcon if you've gone down to the Frog
Hub you've might you might have seen
this game called frog Zone which is as
far as we're aware the first game where
the back end is running entirely and
fully homomorphic encryption like Justin
mentioned we've basically built this
four player game where you've got four
uh four frogs on a 32x32 grid the frogs
can move up down left or right they can
collect items slay monsters Etc and all
of that is happening inside a fully
homomorph encryption with 1 billion x
overhead on top of what it would take to
run this kind of a game normally on a
you know plain text ordinary computer
and that's unlocked some really
interesting thoughts and it sort of that
is one of the thing the things that's
actually led us to obfuscation because
one of the huge pain points of building
something like frog Zone if you've
actually tried the game downstairs is
that there is a ton of interactivity
there's a ton of multi-party computation
decryption that needs to happen the
Wi-Fi keeps going going out downstairs
our Hardware switcher thing keeps
failing and so so there's no way that
you can take this technology and scale
it to something like a billion people
unless you bring in a non- interactivity
technology like obfuscation so each of
these things has been essentially some
sequence of figuring out what's really
going on here trying to generalize what
we currently know and looking for what
is the general category of thing that
this is and how do we solve that
problem um each of these steps in the
understanding tree for programmable
cryptography has taken about a year
and uh each of them has been a concrete
step towards a grounded conceptual
framework for how to think about
programmable cryptography and what you
can do with it so again like I said in
the beginning none of these are complete
Frameworks none of them are you the end
all be all of how to think about
programmable cryptography but each of
them does build on each other and and
we're starting to get hints that this
might be a generally pretty good way to
think about what you can do with this
technology you know first starting with
zkps let us build incomplete information
games and decentralized systems then
generalizing that to saying ZK snarks
turn privacy math problems into coding
problems then generalizing that into ZK
snarks are about data interoperability
and as vial said actually earlier on a
pan panel earlier this week rather than
calling them ZK snarks we might just
call all of these things proofs and then
finally we we've you know come to this
sort of model of programmable
cryptography as this general purpose way
to think about computation between a
network of
people okay so in essence what we've
been trying to do over the past several
years is build a machine to produce this
kind of thinking and what is the
mechanism by which this machine operates
that mechanism is what I sometimes think
about as contact with reality right so
rather than sitting in a room and and
theorizing a bunch about what might be
an interesting ZK system or what might
be an interesting thing to put it put
inside of a snark you know we'll sit
down and we'll try to we we'll build a
lot of stuff we'll take as much of that
stuff as we can we'll deploy it whenever
possible in as real of a setting as
possible even if that's just to few
hundred or a few thousand users and then
we'll constantly go through this process
of looking back auditing pruning and
synthesizing and trying to figure out
what is the general principle what's the
line that you can draw between all of
these
points here are some forms of what
contact with reality might actually look
like one is building a first end to-end
prototype of some technology that we've
never tried before so something like
frog Zone again let's let's just try to
put a server inside a fully homomorphic
encryption even if it's a billion times
slower and we'll figure something out
another one is trying to build something
that folks for whatever reasons will use
or need or ideally love even if it's a
small group of just a couple of hundred
people um another one is teaching
developers and providing them with
different tools or sdks or abstractions
and seeing if that actually enables them
to do something that they couldn't do
before or understand something that they
couldn't do before maybe maybe even
build something that we could not even
have anticipated if we can do that then
we have some sense that oh this
abstraction is actually something that
makes sense that is is maybe worth
refining and building on top
of um by the way as uh sort of you know
in reference to that that last
particular point I think that Folks at
Devcon should think very hard about the
fact that every Devcon attendee now has
access to a ZK friendly EDSA and
semaphor key you know there's there's
essentially you can think of what will
you do with the Merkel route of all
Devcon attendees in addition thanks to
the Frog QR code scanning thing that's
been going on there are hundreds of
thousands of self-issued attest stations
now between attendees that form a dense
social graph each of those frog requests
is essentially your your key pair
signing someone else's public
key okay so yeah it's important to make
a lot of stuff equally important is not
to get distracted so if something that
we're building doesn't fundamentally
make sense but has the potential to you
know make a lot of money or score really
highly on some notion of model as of
metrics like users um knowing when that
is not the the right track to keep going
down um another thing that we think
about is if we're really here with the
goal of testing out a new mental model
not compromising on the mental model and
getting that goal mixed up with
something like adoption it's better to
have a test with a thousand people that
tests the right kind of framework or
mental or mental model than to scale to
you know 10,000 or 100,000 in a way that
is testing a different thing now the
ideal thing would be to you know test
with 100,00 people with the right mental
model but that's what we're working
towards trying to scale up
um and yeah the last one is being
willing to constantly reassess
resynthesize and move on from things
that don't make sense or aren't working
so we've had plenty of false starts in
terms of how to think about what you can
do with programmable
cryptography okay so with that um I want
to talk about a couple of new mental
models or Frameworks that have uh come
up even just through discussions over
the last week with Folks at Devcon um so
one is again this idea that
interactivity really kills this is
another one of those motivations for
obfuscation like I mentioned we've been
running this frog zone game in the
basement of Devcon four players can get
around and you know it's just a real
difficult problem to get all four of the
clients doing the decryption multi-party
computation with every single operation
in the game now when we think about
something like interactivity versus non-
interactivity that's something that
doesn't sound as sexy as like now I can
do arbitrary programs on encrypted state
but it just turns out that for scaling
these systems to millions or potentially
even billions of people um you need need
some strategy for actually dealing with
the fact that only the people involved
in a computation should need to be
involved in the actual process of
running the
computation and an interesting
connection that actually someone made at
at a mpf panel yesterday was wait maybe
this is actually one of the reasons why
ZK snarks have been such a powerful
technology that's been so accelerated
compared to FHA over the last years
especially with respect to blockchains
we've actually had general purpose zero
knowledge proofs for a long time now ZK
snarks one of the additional things is
that they're non-interactive you can
make a One-Shot publicly verifiable
proof and this is a thing that's
actually unlocked a ton of use cases and
a ton of actual you know in the real
world developer
activity um another one that I think
about um and I know I'm running out of
time I just have I have two more of
these um one is this idea of global
private state so we've noticed that with
things like FH or MPC you can build
these decentralized applications that
have state you know imagine like a
variable or a location of a monster or
something where none of the participants
in the application actually know that
state but the state is being computed on
correctly so in frog Zone there's
monsters around the map that move around
but nobody knows where they're moving to
or from the servers and the machines are
just sort of executing in fully
homomorphic encryption advancing the
state of the game one step at a time and
the bat is just sort of its own like
autonomous agent that's that's just
moving around you know so one question
is like you know I I had a moment when
we got the bat moving around on its own
working where I was like wait a second
like what is the subjective experience
of this bat like is this a new kind of
agent it's somehow moving around in
encryption there's literally no single
computer or person or program in the
world that knows where the bat is or
knows anything about what it's doing and
yet it somehow has this like independent
objective experience where it's doing
its own thing um it raises a bunch of
interesting questions about cryptography
and agency right like one thing that I
think about also here is you know a
cryptographic agent has a different
flavor or affordance to it than an AI
agent um a thought that then was
prompted from that from some other folks
who looked at frog Zone was like well
what's actually going on with encryption
we think of encryption as a technology
for hiding messages but maybe that's not
what's actually going on in the same way
that zero knowledge in many context is
not really about zero knowledge or
hiding it's about proving and it's about
data interoperability
so maybe the thing going on with
encryption here is you know if I mind
uploaded my brain in encryption to you
know some server somewhere in plain oh
sorry not in encryption in plain text to
some server somewhere the operator of
that server would be able to do surgery
on my neurons to really like with
my subjective experience but if I
uploaded my brain in encryption or an
obfuscation somewhere the only way for
the person operating that program to
mess with me specifically would be for
them to essentially take down the whole
system system cuz now all of the gates
describing my brain are intimately
connected with the rest of the off
fiscated program you can either turn the
crank on the entire program at once or
you can just like destroy it completely
that internal logic of the world is
somehow preserved because of the fact
that it's OB fiscated and the hiding
thing comes out as an accidental
property so you know going back actually
to to one of the things Albert was
referencing as well there's this idea of
we call something X because we don't yet
know what to call it it's it's pointing
at the idea that the words that we're
using to describe these systems are
placeholders and they represent the fact
that we just don't have a better
understanding yet so we called it zero
knowledge because we didn't know what to
call it um now we're moving to a world
of some maybe something like proofs
maybe we call it encryption because we
don't know what to call it and maybe
it's actually about creating worlds with
somehow mathematically unwind
codependencies between
everything maybe we call it cryptography
or programmable cryptography because we
don't know what to call it
so that's it basically for contact um
you can find out more about what's next
uh this
afternoon uh we will be talking about a
bunch of these different systems that
we've put into varying stages of
production um hopefully over the next
couple years we essentially take these
mental models and we can start building
out a lot more mature systems uh and
thank you everybody if you want a little
froggy gift feel free to scan this QR
code as
well not any froggy gift
I'm it's not any froggy gift this is
most probably the most powerful froggy
gift so oh yeah this this unlocks some
really special stuff in frog crypto so
this is a reward for staying through to
the end of the programmable cryptography
CLS morning sessions so awesome thank
you everyone all right so we don't have
time for questions so we'll wrap it up
here um come back in 30 minutes either
in this room for the workshop on
extending uh the Frog Zone which Brian
just talked about or go to breakout 2
which is on the other side of the
corridor in a much smaller room for the
workshop on programmable cryptography
from a software engineering lens thank
you guys enjoy lunch and see you
later e
I
for for
for
is for
me
I for
yes for
it's e
e
for I
sh e
I e
cheuck hello one two 3 hey
everybody uh we are just running a few
minutes behind uh so we'll be starting
in about five maybe 5 to seven seven
minutes max and uh so get seated feel
free to Talk Amongst yourselves if you
haven't snagged one yet grab a
programmable cryptography textbook
because I'm looking at the table right
now and that's the last of our inventory
so if you don't get one right now you
might not get one there's water at the
back also a great time to take a quick
bathroom break like I said about 5
minutes and we're going to get started
here so thanks for your patience and
tell your friends to come join if you
think they'd like the content we have
coming up
next also those on the live stream if
you can hear me 5 minutes and we'll be
back thanks
e for
hello hey everybody everyone who's new
in the room thanks for coming in uh as I
said before we're just running a little
bit behind we should be ready in about 3
or four minutes just getting our
whiteboard set up and uh doing some last
uh final touches so as I said before if
you haven't had a chance grab a
programmable cryptography textbook at
the back that's the last of our stock if
you don't get one now uh that's it and
uh if you need a quick drink or quick
bathroom break 3 4 minutes we're going
to get started so thanks for your
patience for
get for
pap
all
right hello everybody uh and hello to
those streaming and hello to those
streaming in last minute if you guys
could grab your seats um my name is Remy
I uh have the privilege of working on
the uh operations team at zerox Park and
uh I'm going to be your MC but I'm
really just a uh timekeeper for today so
you'll hear a little bit from me just in
between each speakers thank you guys so
much for coming to our afternoon session
and uh we're going to dive right into it
um I'm going to bring on to the stage
Xerox Park's
co-founder sorry come on in folks come
and get seated I'm going to bring to the
stage Xerox Park's co-founder gub sheep
he is going to kick off this whole
afternoon session which is titled
multi-party fully homomorphic encryption
in practice as a lay person that is not
easy for me to say and uh I I I do want
to uh extend a warm thank you for all of
you for coming out I think this is going
to be an awesome series of talks and
without further Ado if you guys could uh
give a warm Round of Applause for gub
sheep as we bring him to the
stage all right welcome everybody to the
uh welcome everyone to the afternoon
sessions in this first 90minut session
we're going to be talking about
uh which is a new technology that a
handful of our developers researchers
and partners have been working on and
prototyping with so I'm going to start
off by um just kind of going AC capella
on a on a quick introduction to
multiparty fhe or I'll refer to it as mp
fhe uh and after that we're going to dig
into frog Zone which is the demo game
that some of you have seen downstairs on
the uh if you've seen like the tables
around the Frog Hub there's two tables
each of them has four machines and you
you know you might have seen people
going on there trying to either debug
stuff or play stuff uh I'll be talking
about that game which is our first end
to-end demonstration of using this
technology and then we will hear several
lightning talks um from folks who are
involved in building either this game or
some of the technology Stacks that this
is built on top of and uh yeah so let's
let's dig right into it so um we can
also make this because this is a a uh
more casual session it's not as much of
a like prepared like delivered talk
where I'm just going to be talking at
everybody um feel free to ask questions
at any time maybe if uh the staff is
available to help hand microphones to
people when people have questions uh
you're very welcome to just raise your
hand at any point another thing is uh
I'm I know that we have had a couple of
different F related sessions throughout
Devcon so to start off with I just want
to get a bit of context on proxy Ely
where the audience is at um can you
raise your hand if you know what fully
homomorphic encryption
is okay so that that's most of the
audience I'm probably going to go ahead
and assume that can you raise your hand
if you came to the previous how to
hallucinate a server talk yesterday that
was about frog zone so you show hands
there okay cool so what I'm going to
actually start off with then is I'll
start off with a quick multi-party fhe
introduction that assumes that folks
know what fhe is and then uh I'm going
to dig into this set of slides as kind
of an
introduction to uh the Frog Zone project
and then at some point we can either
move depending on what people are
interested in we can either move into
some code or we can move over to the
Whiteboard to kind of conceptually break
down the system so there's a bunch of
different levels of the stack here that
are at play and uh our goal for the end
of this first 55 minute session is to
get an understanding of what are all the
different pieces involved in this in
building a system that is built as an MP
fhe
application okay so um just to get
started folks here it seems like most
folks know what fhe is the idea uh in
short is that I can take some piece of
data and I can encrypt it and send it to
a server that's something we've been
able to do for many decades one of the
problems is once I encrypt data uh a
problem that I might run into is it's
impossible for a server that's holding
my encrypted data to actually run any
kind of computation on that data so you
might imagine something like let's say
that I have some um you know I'm using
an encrypted chat app right or an
encrypted document store so I'm writing
all these documents locally I save them
to the cloud the cloud stores them an
encryption and now maybe I want to issue
a query to the cloud that says you know
give me back all of the documents that
have this keyword in the title now
because all of my documents information
is encrypted um the server has no way to
figure out which of the documents have
the contain the keyword that I'm looking
for enter fully homomorphic encryption
if we have fully homomorphic encryption
the server can run an arbitrary program
on top of that encrypted data so for
example here it would be a keyword
search to check which of these documents
contain the substring you know frog or
something like that right and the server
would be running this program over data
that it has it has no idea what this
underlying data is it's going to get as
output some in this case set of
documents that are also encrypted and
then it's going to send that back to me
and I can decrypt the result and get my
operations so in some sense what I'm
doing is I'm kind of delegating
computation to the server but the server
is able to perform that computation in a
privacy preserving way okay so this is
how people have thought about FHA for a
very long time people have thought about
like well maybe we can do some sort of
like private neural network training
with this kind of thing um maybe we can
have like you know hospitals that are
able to share data with each other and
compute aggregate statistics on
encrypted records what we have been most
interested in lately though is kind of a
different way of thinking about fhe so
in the normal model you know you've got
your client in your server the client
sends up some sort of encrypted data to
the server the server computes on it
sends it back the client decrypts it's
like a delegated computation with
privacy strategy is what FHA is being
used for now we're interested in
multi-party F uh what multi-party FHA is
is it's essentially a way from for
multiple people to get together and
perform a computation or execute a
program over a mutually private state so
how many people here have heard of
multi-party computation MPC okay so
again most of the room so this is
basically using FHA as a way to achieve
this sort of general purpose multi-party
computation right so FH we usually think
about as client and server and
delegating some privacy preserving
computation to the server MPC we often
think of as multiple parties jointly
Computing something together we're
saying here FHA is almost a
cryptographic backend to achieve what we
want out of multi-party computation
which for various reasons we think could
be could be a more interesting direction
for um some reasons we'll get to in this
first set of slides actually okay so
let's dig into this um the particular
thing that I'm going to be first
introducing is this concept of a
hallucinated server which is the sort of
thing that we want to be able to run
inside of um mpf or using
mpf so
so as mentioned uh we've built a game to
demonstrate end to end what using mpf in
this way could look like that game is
called frog Zone you might have seen it
downstairs uh you can feel free to come
up at some point to try playing the game
up here there's a table that has the
setup all these computers are networked
together and they are running frog Zone
on them um the game is very very simple
I'm going to describe the game
um and I have a demo that's booted up
right here so the first thing is if you
saw the game downstairs oh oops it's
like I'm getting a little lag um you you
might have seen that in its steady state
the game has a QR code up that basically
is going to allow you to log in with
your zoo pass so that way you know once
you're in the Frog zone now the Frog
Zone knows that you have this EDSA
public key or semore ID okay so I've
just logged in I can start and you can
see there's a very simple interface here
so the idea is it's a four player game
there are four frogs uh each of us
playing the game will control one of the
frogs and you can see over here in the
upper left hand corner my frog has like
five health and it has one attack and I
can move my frog around up down left or
right so you know now I'm moving around
um I'm like only able to make a move
every couple of seconds that's because
fhe is just extremely slow we'll talk
about that in a bit and um yeah I can
the other the other kind of key thing
going on here is I can only see in this
map all over the map there's things like
various monsters you can see this guy is
an imp a cute little guy just having a
bad day he also has five hit points and
one attack um this is a prickly prickly
Bush I can attack the prickly Bush so
there's monsters that are just sort of
hanging out throughout this 32x32 map
right so I attacked the prickly Bush I
destroyed it so I got one attack I lost
one HP
let's go over to the Imp now and attack
the Imp
oops well the game is very brittle you
can see I I just took the imp's health
down um can do that again so now it has
three
Health attack it now it has one Health
and then if I attack it one more time
the Imp is the Imp has been slain and I
have one more attack okay so so um this
is essentially the core game play we
have this map there's a bunch of
Monsters the monsters are actually
moving around on the map so while
they're in the fog of War they're kind
of doing their own thing um and then
you've got their four players and then
you've also got items so I can go and I
can like here's a wooden sword um
and once I move onto the sword I get an
upgrade so I get one more attack
Point um at the top of the map if I went
up to the top I would see there's
there's actually like uh an ice biome
and in the ice biome there's a dragon
and that's the boss monster of the game
so if you slay the dragon you get a
bunch of you get a bunch of score and
you you win the game so that's that's
the goal um very simple game uh and you
know the total size of the game State
actually is also very small there's
about 150 bytes that represents just the
total state of the board and all of the
monsters and all of the items um the
front end is just a react and phaser
front end and the source code for the
back end uh is about the equivalent of
you know 500 lines of C++ and yet this
game took about a month for a team of
devs from gaus labs and zerox park and
psse to put together which is kind of
crazy right because this game looks
almost like what a kid's first
programming project might be you know if
I'm if I'm like learning to code in
grade school or something and I want it
to put together I'm like maybe a
particularly enterprising student I
could put something like this together
um and yeah this took multiple devs a
very long time to build so what's going
on here why is this hard well the reason
that this is hard is because all of this
game state is actually executing inside
of fully homomorphic encryption and to
our knowledge this is the first time
that someone has built an application in
this fashion where you have an
application that involves multiple users
and the back end is essentially being
hallucinated it's being run inside of
fhe so that means all of that 150 bytes
of state is encrypted and all of the
player actions such as a a request to
move up or a request to pick up this
item or a request to attack this monster
that's happening inside of encryption
cool so any questions so
far Yeah question in the
front and again for those coming in feel
free to this is a interactive session
feel free to raise your hand at any
point ask questions so it says that the
server is hallucinated but it also
mentioned that you're running like a
th000 CPUs so how does that work we'll
get to that we'll get to that in a bit
when we break down kind of the the
architecture of this but great
question um okay so like we mentioned we
want to use mpf to simulate this idea of
a hallucinated server and to motivate
this you know we can think about how
applications are run today today the way
an application will work is um let's say
at Devcon someone wants to start a
social media site right for a social
network for attendees of Devcon to be
able to post and add friends to each
other and send messages and stuff like
that well the traditional web 2 way of
doing things is someone would go and
they would rent an AWS box and then they
would write some backend code and they
would deploy that code onto the box and
then each of us via some you know
website or client we would talk to that
AWS machine and we would be able to
engage in in The Social Network that way
now one of the promises of programmable
cryptography is that we'll be able to do
this but just with the users
collectively simulating the execution of
this virtual server so we could imagine
a billion people coming together and
being able to hallucinate the backend of
a service like Facebook or Twitter or
whatever else and in this world what
might be going on is everybody could be
storing some sort of cryptographic Shard
of the total server State and
programmable cryptography you know
Technologies like obfuscation or fhe or
ZK would be used so that everybody can
in lock step Advance the state of the
computation one step at a time while
preserving you know its correctness
while preserving its privacy ensuring
that everybody is only able to know or
make you know get requests to the things
that they're supposed to be able to know
and so we'd be able to hallucinate Zuck
out of the equation for this particular
example um and yeah we we can have this
idea of like almost a perfect computer
it's a server made of math rather than
having a physical footprint specifically
somewhere it's perfectly secure privacy
preserving verifiable it's interoperable
with every other server that's
hallucinated um but of course we're very
early in our journey right now so what's
going on is the the Frog Zone backend is
basically being collectively
hallucinated by nine machines Each of
which is playing sort of a different
role right so there's the four MacBooks
over there and there's also five 192
core AWS machines these are six c6a 48x
larges and it costs about you know $200
an hour to keep this up so what's going
on under the hood is that these nine
machines are collectively running the
FHA computations together necessary to
perform the action of the server um one
sort of to put some numbers to this you
can think about this as like every
binary gate that is involved in the
computation takes about 10 milliseconds
to evaluate that's about a billion times
slower than regular computation so you
know I believe that on on Modern chips a
binary gate might take something like
about 10 to the1 like 10 Picos seconds
to evaluate so we're nine orders of
magnitude off and then the other thing
is that for every bit of PL Tech State
we're we're storing we have a blowup
factor of about several several thousand
so every plain text bit of state is
going to correspond to about 3,000 bits
of Cipher
text I kind of think about this as um
it's almost like we've built a
cryptographic equivalent of like the uh
a particle accelerator where we have
this like enormous amount of resources
that is existing in order to suspend in
the middle of all of these computers a
very small number of bits that we can
operate on consistently um just like you
know with a particle accelerator we have
this like enormous like magnetic field
build and crazy stuff just so that way
for a brief instant in time we can uh
you know get some evidence of the higs
bow zone or
something so yeah in short we've built
the slowest and worst performing game in
the history of human Computing and we're
going to talk about how we did that so
like I mentioned um the ideal here would
for would for uh would be for these four
machines to be able to just collectively
hallucinate the game through multi-party
fhe but in reality because of some of
the constraints performance- wise that
we have today there's nine machines
involved now the same kinds of or very
similar kinds of guarantees are still
preserved but we're doing this so that
the game can actually be accessible um
and we can get sort of the performance
we need to perform the so let's look
at what's happening um so there's
essentially this Fleet of AWS web
servers that is storing the encrypted
state so these web servers they don't
see any of the actual underlying
computation uh and in theory in the
future they could be substituted out for
just a local computation running on
everybody's machines but we do that so
that the moves can take under you know
about 1 second or so otherwise it would
be maybe like 10 seconds so whenever uh
a machine wants to send an operation up
to the server let's say I want to move
my frog up right uh oh the game lasts
only five minutes
so let me go ahead and log back in
here and for those who are interested in
how the zoo pass login Works without any
kind of zoo pass popup going on uh there
there's a session about that it
following this mpf session so you can
see what's going on exactly with this
page um so let's say that yeah I want to
move my frog up I'm going to press this
up button and what I'm going to do is
I'm essentially going to send I'm going
to encrypt this enum up right which I'm
going to serialize as two bits and I'm
going to send those two bits of Cipher
text up to one of these five fleets of
servers so now that that server is
receiving two encrypted bits doesn't
know what those bits are um what it's
going to do is it's going to you know
forward that request on to all of the
other servers so basically all of these
servers have are just replicating all
the requests that are being sent from
the clients and then what those servers
are going to do is they're going to you
know run that move in FHA on top of the
state so essentially there's some
function that takes in two inputs the
first is you can think of as a 150 byte
string that represents the state of the
game and the second input is this
encrypted you know two bits and uh I
guess a player ID as well so it' be like
four bits right and there's a transition
there's a state transition function much
like a blockchain has a state transition
function that applies that move onto
this 150 BYT state to get a new 150 BYT
state right and now I flush my you know
store my memory and you know that's the
new state of the game is this 150 bytes
worth of encrypted um game State okay so
finally whenever players want to
retrieve some State how does that that
work well what I can do is I can send up
a query to one of these five AWS servers
that says get me the 5x5 area around my
frog that's the only thing that I am
allowed to see right I'm not allowed to
see the positions of other frogs the way
that this game should work is that none
of the frogs should be able to see each
other or see what each other is doing
unless you know you're in the 5x5 area
around where something's happening right
okay so what I'm going to do is that's
equivalent to basically some sort of
view function execution on the state so
uh I'm going to send up you know this
request to execute a certain view
function on the state and return it back
to me one of those servers is going to
take that request it will execute that
view function over that 150 bytes it's
going to get out some representation
essentially of a 5x5 grid that has a
cipher text corresponding to what's
inside that tile whether it's a monster
or player item or uh you know whether
it's an impassible terrain or not and
it's going to return it back to me right
now the problem is it's executing this
view function over some encrypted data
and what I'm going to get out of that is
also encrypted data so I'm the client I
receive some encrypted data back I
cannot decrypt that data alone you know
the guarantee of fhe is that you put
some encrypted data in you run a program
over it you get some encrypted data out
um if we had something like you know
program modication I'd be able to get
plain text Data out but this is the
guarantee of FHA so in order order to
decrypt this data what I have to do is
the way that this mpf protocol works is
all four of the machines that are client
machines here are storing essentially
one you can think of it as a Shard or
like a secret share of the protocol
decryption key so all four of us need to
put our shards together to perform any
single decryption so that's exactly what
we're going to do um again if you were
downstairs you might have seen that you
know in between all of the four machines
there was this kind of uh this switcher
in the middle that the all the computers
were connected to that was helping to
coordinate a multi-party decryption
ceremony that would essentially take the
encrypted output that's been returned by
The View function pass it around to all
four of the machines and then all four
of the machines would uh collectively
send some decryption shares back to me
and I can use that to decrypt the output
so for those who are familiar with you
know trusted setup in zero knowledge
protocols that's something kind of anal
to what's going on here to decrypt the
result okay so um let's talk a little
bit then about now now that we know that
this is what's going on um and this is
what the the function of each of these
nine machines is uh let's kind of talk
about the trust model here so earlier we
had a question which was we talked about
this idea that theoretically we want
these four machines to be hallucinating
a server together but there's some AWS
machines in the mix here what is the
trust assumption on those machines what
are they doing what are we relying on
them for what are we what are we not
relying on them for does anyone want to
take a
shot yep over
there yeah if you just store in the
whole state of the game in like a little
just be using AWS to um process the next
dat right yeah exactly so each of those
AWS machines is storing the cipher text
encrypted version of that 150 plain text
bytes um in fact it's replicated across
all of the AWS machines and if we wanted
to we could also replicate that state on
each of the the local machines as well
so all that we're doing with the servers
is we're simply delegating computation
to them right so each of those servers
can run that state transition function
where it takes in as input the cipher
text and the encrypted move the
encrypted State update and then output
the new state any server could do that I
could replace this server with that
server I could have a marketplace where
different people are providing servers
to to perform this computation or even
if FH was about 30 times faster then we
wouldn't need the servers at all we
could actually just have all of those
calculations replicated and running
locally on all four of those machines
and those machines would simply at every
step run the FHA process and then cross
check with each other that the ending
you know resulting Cipher texts of the
now we're doing this because we want the
move it was a designed goal to make it
so that each of the moves takes under
one second to process um but this is one
of the things that we can do if FHA gets
better okay any questions about this yes
over
there um what about onboarding and
offboarding parties like how easy it is
to join the service that compute and
store the uh State and do we have to
regenerate the key and like re
reinitialize the whole setup every time
yeah yeah so that's exactly right
another limitation of this system right
now with the protocols that we have is
that you need to sort of set up the
group in advance so you need to
designate which are the parties to the
computation then they run this almost
kind of not quite trusted setup like
process but something like a ZK trusted
setup process to instantiate all the
protocol parameters and those protocol
parameters are for that specific
group however it's it's for that
specific group it's not for the specific
program you can actually be then take
that group and have a bunch of different
programs running as well does that
answer the question yeah so if we were
to talk about like an ongoing setup
let's say um M MMO RPG game that is like
ongoing then and and it would be like
permissionless to join and like be a
part of the verifiers who compute the
state uh that would me make sense to
organize it into EPO or something right
like and to re regenerate the setup uh
for every epac yeah yeah I I think that
um you could imagine doing something
like that I I believe that it's also it
doesn't seem too Out Of Reach to also
upgrade what we have you know literally
running right here uh to be able to
accept you know adding participants and
deleting participants and setting
thresholds on like what is the number of
key shares you need online um one kind
of world I could imagine is I don't know
if folks here have seen you know
torrenting websites like The Pirate Bay
but uh at any given time for any given
torrent you might have some subnet of
some number of seedar and leechers and
as long as you have enough seedar you're
able to access that data well we could
imagine a world where you have you know
that sort of setup but as long as enough
people are online for the particular
program subnet you have access to that
particular program um so but in order to
do that you would need a protocol that
admits participants joining and leaving
at arbitrary times now again you know
hint hint nudge nudge wink wink this is
the sort of thing that becomes very easy
Once you have functional encryption and
obfuscation and that's why projects you
know this project and the precursor to
this which was called the chicken game
not instead of the frog game
um sort of that that sorted to point us
in the direction of actually wait many
of these problems would be solved if we
had this even more advanced technology
does that answer the question yes thank
you awesome any
others okay so let's keep rolling uh
oops so the servers are I guess they're
being trusted here not to go down
hypothetically though we could be
replicating the computation on local
machines um they're only performing a
fully deterministic operation with no
Secrets um and uh that's basically how
this whole setup
works okay so uh I want to get now into
some of the tricks that we use to
actually make this game you know this is
a very simple game but it is a playable
game that does have some minimum number
of of consistent mechanics um so we use
a number of Tricks basically uh to make
this work even in the context of a
highly constrained Computing environment
and for me this is a little bit
reminiscent of you know stuff that I've
read about the early histories of video
game or computer game development you
know back in like the '90s or even
earlier when you had these arcade
machines um or the very first personal
computers you would have these game
developers who had very very limited
amount of memory very very limited
amount of compute and they would have to
try to simulate some kind of
self-consistent virtual world with a
bunch of different rule sets and back
then that's that's how we got a bunch of
advancements in things like Graphics uh
or I think things like you know
efficiently Computing square roots or a
lot of that kind of stuff came out so
you know perhaps we might see something
similar come out of fhe over the next
few years um oh and as one other note um
for those who have been uh looking into
or following along with blockchain
gaming in the last couple of years for
me this has felt very reminiscent also
of developing uh some of the first like
onchain ZK games as well where you're
working in an environment where ZK
snarks are super slow five years ago
there's like no l2s you have like a tiny
amount of gas budget for your game how
do you build something that has a
self-consistent universe we might be
about two orders of magnitude more
constrained than the 2019 era of let's
say like blockchain onchain gaming um or
autonomous worlds as a lot of you know
these these games are now like starting
to be directed towards um but similar
style of thinking so what are our
constraints our constraints are we can't
really go above 200 bytes of State due
to the fact that um you know once you
need a lot of bandwidth requirements and
interactivity requirements because
there's this you know 3000x Cipher text
blowup You're simply transmitting too
much over the network and again for
those who have who have actually tried
the game you might have noticed that
downstairs um especially when the Wi-Fi
was uh you know kind of dodgy the game
would stop working or moves would stop
getting processed or or all of these
things you know that's the result
basically of the fact that all of these
these constraints need to combine
together the biggest constraint though
is that we have this 1 billionex
computation overhead and actually more
than just a 1 billionex computation
overhead I would secretly think about it
as like a 10 to a 100 billion
computation overhead because there's
certain things that you can't do in fhe
that you would naturally do in a normal
programming model so I'll explain that
in a bit as well so um and then our goal
was given all of these constraints we
still want to be able to build a game
where each of these moves takes under
one second right so we' got four players
each of the players uh moves takes about
a second to process an FHA when it's
distributed across the five machines
that means that I can move you know my
frog once every four seconds or so and
that's you know going to be rate limited
by the client here um and four seconds
is about the limit for like this to feel
like a playable game so we're we're
right in there um okay so um one thing
that I want to talk about here first is
the idea of the circuit model versus the
memory model of programming and actually
is it is it possible to switch over to
the Whiteboard now is that something I
can do
okay all right so um how many folks in
this audience have seen or programmed ZK
circuits can you raise your
hands okay so so folks who have tried
working with ZK circuits has some sense
that when you're writing a ZK circuit
you're sort of fundamentally doing a
different thing than when you're writing
a program right a lot of stuff is
basically like more annoying in some
vague way well guess what you're in luck
stuff is still more annoying in exactly
those ways or at least very similar ways
with FHA as well um so let's talk about
what it means to be programming in terms
of circuits well with circuits what I
have is I basically
have a bunch of
gates on the left side I take in a bunch
of inputs you know in this case it might
be
bits and then you know I can run these
through some other
Gates and then like some of these Gates
might come together in like certain ways
and then I might like get some sort of
you know some sort of outputs
right now you know in in some sense this
also looks maybe a little bit sort of
like you know something like a neural
network I start at the left and then I
like go through all of these operations
these operations depending on what kind
of execution environment I'm working in
they could be stuff like you know an
arithmetic circuit has Gates that look
like times and plus right so I would
take these two bits um oh actually let's
do
this I would take these two bits and I
might multiply them to get the output of
this bit or I might take these two bits
um and I might like add them to get the
output of this bit other kinds of gates
that we can imagine are Gates like um
you know logical operators so or and you
know not stuff like that this is
approximately what a circuit is so I can
go from left to right and evaluate all
the bits um now this is pretty different
from how I think about a program right
in a program let's say I'm writing in in
you know some high level language I
might write something like uh you know
um int
B4
equals 0 one 1 0o and then like later
down in the program I might be ble to do
something like you know check like if
you know C equals equals B of
I then like do something right and then
like maybe like uh or maybe this is like
some variable I'll call it like uh like
X and then X is some variable here that
like X is f of blah blah blah like some
computation okay so um for those who
have coded using something like circom
uh you might start to see where the
where the difficulty comes in where the
problem comes in
um when I'm trying to write something
like this in the circuit model in this
model what we implicitly have access to
is this idea of memory right so I have
you can imagine I have this big like
memory tape with a bunch of addresses
addresses like 67 68 69 70 71 Etc um and
like I might put this array into memory
and then if I want to read out the the
number at location X then I can simply
pull that out of of memory over here now
let's talk about why that doesn't work
in
FHA so let's say that I try to do kind
of a naive construction where I
oops where I implement this 32x 32 grid
by keeping a 32x 32 uh grid of Cipher
texts so you see how like each of these
tiles there's like some stuff in the
tile right you see these tile details
this tile has coordinates 224 it
contains a monster that monster is a
prickly bush has one HP one attack
imagine I take all that and I try to
basically encrypt that with my FHA
scheme and then I store it at the
position 2 comma 24 in my
array now let's say I want to perform
some action that causes me to modify the
state of that 224 tile in encryption so
I'm going to move my frog over
here
yep and I'm going to attack the prickly
Bush and that like destroys the prickly
bush right what's the problem if I store
this map as a 32x32 grid of Cipher texts
does that is am I keeping private what
I'm wanting to keep private from the
server and the other players when I
perform this
action yeah over
there sorry can you say that again
um yeah so so if we got together and we
decrypted the whole map we would be able
to decrypt it which is why there is at
least sort of a one event trust
assumption on the four players but I
guess what I'm saying is that there more
than that so sorry to interrupt but H
you might they might not know what
you're trying to do but they will know
exactly where you're doing it yeah
that's exactly right so the issue here
is let's say that the whole kind of the
whole mechanic of the game is you can't
see where other people are right like
other people's coordinates are not being
revealed to you they're not being
revealed to any party that's like
inspecting the traffic of the network um
so let's say I say okay well I'm going
to take my frog and I want my frog to do
something to tile 6 comma 3 but I'm not
going to tell you what I'm doing to 6
comma 3 or like I'm like I take my frog
and I say I want to take my frog and I
want to make it do something to the
tiles you know uh like 3 comma 24 and 3
comma 23 and I tell you what I'm doing
that's a secret that's encrypted well
this is going to leak a lot of
information right this is effectively
revealing to all the other participants
on the network anyone looking at the
traffic if we're delegating you know tra
if we're delegating computation to any
server this is a pretty obvious tell
that you are moving from 3 comma 23 to
three uh sorry 3 comma 24 to 3 comma 23
does this make sense to
everybody yeah so somehow memory doesn't
quite work the same way inside of fhe
that it does inside of regular programs
and again for those who have seen ZK
circuits this is this is a similar issue
here we don't really have access to
memory in the same ways so instead what
we have to do is we end up having to do
this sort of check for every single tile
right like I have to say uh well if I am
moving on to tile 3 comma 23 um do this
thing if I am moving on to tile 3 comma
outputs of all of those results and then
add them together um M like and take
like a DOT product with a with a vector
that basically selects which one of
those options is true so let me let me
write that down actually on the board
here um so let's say I have some
function and we can literally go and
look at this function in the code right
after this actually that says um
Collision right and what that function
is going to take in is it might take in
um two values it's like some
chords this is a two integers right and
then the other thing that it takes in is
it might take in um you
know let's say uh not allowed
tiles and maybe there's like a hundred
not allowed tiles each of them has like
two
coordinates right so what I essentially
have to do here is is I might have some
other circuit the like is equal
circuit that takes in chords one and
chords
two and it returns you know one if
equal and zero
otherwise what I'm going to have to do
is I'm going to have to return this
value Okay so
chords two so I'll say is
equal of chords 2 comma not allowed
tiles zero oh sorry have chords not
allowed tiles zero plus is
equal
chords not allowed tiles one and then
etc etc and I go all the way down to
plus is
chords comma not allowed tile index 99
okay and now if you can imagine like I
might and then you know this is going to
Output basically like a one or a zero
depending on whether or not the
coordinates uh were contained inside of
array so that's basically a linear time
operation I'm doing a linear scan of
course what I would like to do in a
normal program is I might store this
thing as a bit map and then I would
simply just look up X and Y of the
coordinates and determine whether the
bit map contains
um a a tile I can't collide with here I
have to do this linear scan now this
blowup is basically what happens for
every single operation so let's say that
I have some rule or some logic in my
game that when I attack a monster I have
to subtract that Monster's Health by my
attack well the way that I'm going to do
that is I'm basically going to Loop
through every single Monster in the game
and then I'm going to check does my
coordinates equal that Monster's
coordinates and if so apply this attack
does my coordinates equal that Monster's
attack if so apply that attack and then
I'm also going to have to do that for
every single item so anytime I interact
with any coordinate tile I basically
have to simultaneously run all possible
branches of the program inside of
FHA so that's why the overhead of f over
regular programs is not just 1 billion x
in the sense that a binary gate takes a
billion x more time to run than a or
sorry a binary gate and encryption takes
a billion x more time to run it's also
got this overhead of the fact that we're
working in the circuit model and not the
memory
model does this make sense are there any
questions so
far cool oh yes question over
there the question might not have uh
legs but if we go back to the actual
frog zone game I'm seeing on the right
all all of the encryption decryption
happening and it's almost as if the
program is basically checking for every
single tile and encrypting it decrypting
it and I'm wondering if that's necessary
or if it's there is any optimization and
you chose not to do the optimization or
whether this is actually necessary yeah
yeah so yeah the ideal world would be
that I can make some moves to the server
and then I can request for the state
that I want from the server and the
server just returns to me somehow the
PL text you know the plain text like
information of the tile um instead what
we have to do here is I'm getting back
an encrypted version of the tile and
then I have to do the four-party like
multiplayer decryption to actually get
what is in the tile so there is an
optimization that allows me to just get
the tile back in the clear that
optimization is called
indistinguishability obfuscation so if
we can crack that then this become this
problem becomes a lot easier and that's
what's actually one of the reasons
that's motivating us to start looking so
much at obfuscation is because we're
trying to do these things and we realize
oh wait this is really going to suck if
we try to scale this up Beyond four
people thank you cool um so it's it's
actually that line of questioning that
also drives a good amount of what we
think of as the the research agenda in
programmable cryptography so a practical
question we can ask is like well what
would it take to not have to do this
four player networking or for example to
not have so much difficulty instantiate
it with instantiating a new group every
time you want to do a new computation
that leads us down the direction of
functional encryption this sort of thing
where like the circuit model is just way
harder to work with and adds an
additional 10 or 100x overhead on top of
the programming model that is going to
actually motivate another Direction
which is the direction of oblivious
random access memory which we'll also
hear about later today in these
afternoon sessions if we can crack FHA
or obfuscation friendly
Oram then we can basically do fhe but
where the indices of the memory that I'm
trying to access are in some sense
homomorphically encrypted in the same
way so yeah a little demonstration of
how even just building a simple little
game you run into all these problems
that you don't anticipate and that that
just opens up and tells you about what
to do next in programmable
cryptography okay so um we can actually
look at the move function that's
implemented as a circuit and this is
also going to be a good segue to talking
about like the development stack of this
whole thing
so um yeah I want to talk about the
stack here so frog zone is built on top
of an fhe Library an mpf Library called
Phantom Zone um I believe Phantom Zone
is one of the the two libraries that
exists for multiparty fhe I recently
found out I think open fhe also has
something here um yeah the the wonderful
Folks at gaus Labs um mostly Jay as uh
leading this has have been working on
this mpf library and what it essentially
does is it's a rust library that exposes
all these functions that look like stuff
like you know fhore or and the rust
function fhore or takes in two encrypted
bits two FHA encrypted bits and it
outputs another FHA encrypted bit okay
so you can start to build these programs
that basically look like uh I'll show
you here so this is sort of analogous to
like looking at like an R1 CS um you
know if you're if you're deserializing
what's coming out of like a circom
compilation or something so um this
stuff basically is going to these are
arrays of all these FHA operations that
we want to do and these are going to all
get compiled down into basically a bunch
of um you know fhe ores and fhe Knots
and FHA ands now it's you know as you
can see like this is what the binary
circuit for moving a monster round would
would look like and I really don't want
to write this by hand right like this
looks very painful it's also
automatically doing some optimization
and parallelization what we would like
to do is write in some kind of higher
level language in the same way I don't
want to write R1 CS when I'm writing in
circom so what we have is um some of the
wonderful wonderful Folks at psse
essentially built a compiler tool chain
that allows me to start by specifying my
uh the the circuit that I want to
execute in C code and then it uses a
combination of compilers to basically
take this C code and compile it down
into a binary circuit and then it uses
Phantom Zone to execute that binary
circuit inside of
fhe so if we look over one of these
functions we can see some of the things
that we were just talking about over
there with like the pain of running in
the circuit model so in fact right here
I have that something very similar to
that very function I was talking about
apply move check Collision so the first
thing that I'm going to do is I'm going
to take in some of my old coordinates
which is two 8 bit numbers um and I'm
going to taking a direction and I'm
going to run you know the uh coordinate
incrementing procedure on this and then
what I'm going to do is I'm going to
have to take in all of these obstacles
that are up here so this is essentially
right now the map is hardcoded we'll get
to later how you can make it so that the
map is not hardcoded but it takes all of
the coordinates of the water tiles and
you can't run into the water tiles and
it just checks to see does your
coordinate equal to one of the water
tiles and then it does the same thing
with all the players and if you did not
collide with anything it will return the
new coordinates if you did collide with
something it will return your your
current old
coordinates but rerandomized the
encryption so that you can't tell that
you didn't move um so this is C code
that's written and then it's going to be
compiled down into a binary circuit and
then that binary circuit is going to be
you know turned into this uh piece of
rust code that uses uh Phantom Zone and
then we're going to call that rust code
inside of our um
inside of our sort of backend rust code
that's actually running the game in
encryption right so you can see over
here I'm calling into this apply and
move function that was autogenerated by
my FHA compiler tool chain so um yeah I
think like edu and Han spent probably on
the order of several weeks working on
just getting this thing working um and
there's a lot of basically like
optimization work that happens at that
step where for example we saw over here
if we go to the apply move function that
I have this like hardcoded list of
obstacles what that enables the compiler
to do is it enables the compiler to
compile an optimize binary circuit that
assumes that all of these coordinates
are hard-coded in so you can start the
compiler can start automatically you
know intelligently um making it so that
maybe I can do a batch check of a bunch
of these because a bunch of these all
start with the y-coordinate three so
rather than checking each of them
individually one by one maybe I do like
a range check so this is the sort of way
that we we op we um take advantage of
existing like Hardware synthesis and and
compiler type tools
so that's basically what's going on at
the bottom level of the stack that is
how we end up running stuff inside of
fhe um any questions so far
here cool let's keep rolling okay so
using this kind of of Stack we can write
all of the Transformations that we want
to do in the game which is basically
like you know making a move for a player
another one is like the monsters move
around on their own inside of encryption
so basically we can like write the
function that determines you know given
some random input for how the monster
should move uh figure out if the monster
is able to move to that location and
then move it um and uh yeah you can
essentially model this this C code as
like running or C++ code AS running
inside of fhe um so a level above that
uh we get to
the actual back end of the game and the
back end is basically just this big
harness around those FHA functions that
sort of handles the input output from
the different players and does a bunch
of the various tricks that we need to do
um to you know Factor different kinds of
State Etc so one thing that we found out
very early on in development is that it
is a real pain to try to build and
iterate on top of this kind of game and
debug things when you're actually
running the whole thing inside of
FHA so you know if I want to test
something each of the moves takes about
trying to do local development this is
this is really tough um so what we
quickly sort of landed on was we also
built out a mock plain text version of
the back end that just simulates the
exact same functionality that the um you
know fhe backend is running but here
it's in plain text and we sort of just
artificially take the benchmarks from
that Fleet of five servers we see how
long it's supposed to take to do a move
and then we just sort of artificially
introduce these rate limits or these
these time delays in the mock version of
the game so that makes it much easier to
program but that was that was one small
thing that we noticed and it's it's the
accumulation of a bunch of small things
like this that accumulates into a
fullscale developer tool chain which is
what we're sort of thinking about as a
result of having gone through this first
exercise once
okay so
um let's talk about a couple of the
things that the server is doing a few of
the tricks that it's doing
so one thing that's going on is like I
mentioned the blow up of plain text to
Cipher text is huge it's like at least
three orders of magnitude for every bit
I want to transmit of equivalent plane
text state I'm transmitting like
kilobytes of uh encrypted Cipher texts
so I really would like to minimize the
amount of bits that I have to pass back
and forth and you can imagine if I was
sort of writing this application in the
natural way with tools that we have
today um the way that I might return the
have some sort of data structure you
know imagine some sort of Json that for
each tile just contains does this tile
have a monster or an item if it's an
item what are the items like properties
if it's a monster what are the monster
Properties or maybe it has a big
checklist of all the monsters and all
the items and you know I go down the
list and I check off if there is one of
those entities inside of this tile now
that's going to lead to lead to a lot of
this sort of communication blowup so we
basically have to be very very um sort
of Thrifty with our data structures here
it's kind of similar actually to writing
some stuff in solidity when you have to
minimize the amount of call data or
minimize the amount of stuff that's
stored onto the chain um so
approximately and this is not exactly
right but approximately what is returned
for any given cell is about 32 Bits And
depending on what is in that cell
whether it's a player or an item or a
monster or nothing these 32 bits are
interpreted differently so for example
the fourth bite of the state if this if
the first bite had uh basically the
entity type player in it so that's an
enum that takes two bits to serialize or
three bits to serialize um then I know
to interpret the fourth bite as the
player score on the other hand if the
entity type of the thing was item then I
know to interpret this bite as the
number of points that a player ought to
get for picking this thing up right so
um we using this kind of thing we're
basically able to design the game around
this idea that we should just have this
and we just have to fit whatever
mechanics we can into this 32-bit
structure
a last thing that I want to talk about
is the idea of Randomness in this game
this is sort of the last backend
component
so like we've talked about there's these
four players that are living inside of
the Frog Zone and they can each see the
the map is 32x 32 which means that
there's a bunch of this fog of war that
none of the players can see right all of
these dark areas in between all of the
respective players viewports stuff is
still happening inside of those areas
there's monsters that are moving around
of their own accord so how do we make
that happen when the game is being
hallucinated by these four players right
like how can we make it such that we can
essentially have like an autonomous
flying bat that's going around despite
the fact that none of the players
actually knows where the bat is because
here at least with the frogs it's a
little bit of an easier problem right
you could kind of imagine that well in
terms of where the frog is at least I'm
going to know where the where my frog is
and you're going to know where your frog
is so each of us collectively we're
going to know where the frogs are but
somehow we have to simulate the
execution of this bat flying around that
none of us knows so the trick for that
is to basically introduce some notion of
Randomness you know and this is some of
the idea that goes behind things like
procedural generation as well so every
time I send okay so actually let me back
up a bit uh what we're going to do in
order to set the foundations for these n
PCS to be able to move around on their
own is that the server is going to keep
some encrypted bite as essentially a
random seed at all times now whenever I
a player wants to make a move what I'm
going to do is I'm also going to client
side generate some random bite and I'm
going to encrypt that and I'm going to
send that up with my move what the
server is then going to do is it is
going to in encryption exor the random
bite that sending up with the current
bite that is representing its random
seed state so in this way I'm sort of
doing something kind of like a a Rand
Dow sort of thing where I'm mixing this
uh encrypted random State again very
blockchain esque sort of construction
here so now at regular intervals what
the server can do is it can take that
encrypted random State mod it by four to
pick a direction up down left or right
mod it by the number of monsters to pick
a monster to move and then execute
moving that monster in that direction
all without having any idea of what the
monster is or what the direction
is did I hear any a
question cool um so yeah this is very a
lot of this actually turns out to be
very reminiscent of blockchain
development but rather than having to
execute inside of this smart contract
execution environment we're executing
inside of FHA where we only have access
to circuits certain kinds of determinism
Etc okay so that move for example Not
only was I encrypting the enum
representing right I'm also encrypting
this random
bite the final thing that we weren't
able to get to in this version because
uh we didn't have the necessary compute
to do it but if instead of having five
of these massive aw machine AWS machines
if we had 50 we would be able to do this
is right now the map for this game is
hardcoded right so if I
log back in again here you can see so
I'm starting a new game you can see that
it's going to be the same map and my
frog is going to start spawning in the
same place now theoretically with this
kind of Randomness strategy that I've
just
described we could embed a procedural
generation algorithm that takes in a
random seed into the fhe circuits to
generate the map only when the players
have joined now this is theoretically
possible it would take about 10x more
computations so it's not completely out
of range
um but the point is we we couldn't do it
here given basically the amount of
compute that is accessible right now for
reserving off of
AWS um this is also very reminiscent to
a trick that we use sometimes in ZK
games where we essentially procedurally
generate the game by implementing a
procedurally generation procedural
generation algorithm inside of a ZK
snark so you see there's all these
different parallels between the
different kinds of programmable
cryptography and the different kinds of
guarantees that they give so the
eventual version of of this game that
you could
imagine once we have obfuscation memory
this sort of Randomness this sort of
performance is we could imagine a
billion people getting together to be
able to hallucinate and procedurally
generate an entire world and this world
would have all sorts of NPCs and those
NPCs would be able to move around
autonomously like of their own accord
and I think that's really really
interesting I think that there's some
like interesting implications um for uh
for what it even means to be an agent in
this game so for folks who were here for
the morning sessions we touched very
briefly on the end about like is there a
different kind of digital agent that
becomes unlocked by uh something like
the Frog Zone you know I I had a little
bit of a moment the first time that we
got a bat moving around on its own in
encryption which is like no one knows
where this bat is or what its properties
are and yet this bat is somehow still
part of objective reality like what is
what is the subjective experience of
this bat what is it like to be a bat
like flying around in encryption it's
like a genuinely like very interesting
question and I think it presents another
alternative view on things like uh you
know digital agency where we we often
times we think about AI agents and llms
and the fact that intelligence is one
way of conferring agency but another way
could be you know if I were to obfuscate
or encrypt my entire brain and put it
inside of a cryptographic program
somehow I have a self-consistent to that
program that is not that is an
orthogonal Dimension to the to the AI
sort of thing going
on um yeah so that's about it for the
back end I'll say one more quick thing
about the decryption and then I will
hand it over to edu to talk about some
of the
circuits um
so one thing that's going on is if you
look at this this is this is just bad
window management this is not actually
like strictly necessary um but the
reason that to run this game right now I
have so many terminals open is because
what's going on is that each of these
clients needs to basically be running a
FHA decryption client locally and we
have FHA decryption clients running
locally in Rust so what's going on is
essentially there is a decryption
program that's running on all four
machines those decryption programs are
talking with the AWS machines that are
carrying out the fully homomorphic
encryption operations and then those
four uh uh the four decryption programs
and the four machines are linked
together on a tail scale Network and
they're sort of doing this peer-to-peer
Communication in order to get um all of
the respective decryption shares every
single time I need to retrieve you know
new cells in my viewport or refresh the
cells in my viewport so um this whole
thing basically has involved you know
spinning up something like somewhere
between 12 and 16 total programs that
are collectively running all of these
different parts of the operations
necessary to hallucinate a server and
all of this just to get four player
playing a four player frog game in a
grid um so yeah that's about it for uh
the overview of frog Zone and with that
I will stop
here all right um let's get uh another
round of applause for gub
sheet oh and um maybe one more thing
that I'll say is I just want to shout
out a bunch of the contributors who made
this project possible was real team
effort across the stack we had uh John
maayah from Gaal Labs we had Han and edu
and CC from psse uh we had help from
small brain games um we had help from
Marion over there it was a a bunch of
things coming together to put this demo
for you guys at at Devcon so thanks
again to everybody who was
involved all right we're going to do a
quick little 30 second change over um
one of the fun things about uh
interactive workshops is we got to have
a fresh machine every single time so
thank you for our lovely AV staff who's
actually been doing an incredible job
actually I'll take this moment can I get
a round of applause for the AV staff for
this whole uh this whole conference the
volunteer staff all the people behind
the scenes let's give them a little clap
because they've been doing an amazing
job we came to them this morning and we
asked if we could have a whiteboard on
stage can we swap out different machines
and they've just made it all happen so
you guys have been amazing
and uh now I've killed enough time for
us to have our machine set up so uh can
I get another round of applause uh for
excuse me sorry messed up my sheet here
uh Edward Soo I think I pronounced that
wrong but Here We Go Round of Applause
for Edward and he's going to talk to us
about Boolean and ZK circuits Round of
Applause please
hello so um I've spent the last three
years mostly working on writing ZK
circuits some of these was circom and
some most of that was Halo to and in the
past months I've been playing with
multiparty FH and writing cites for
those and I will give a talk about some
differences and similarities between
writing FHA circuits
um which also applies to um NPC in many
cases and ZK
circuits so one of the first differences
is that in most ZK proof systems you
don't actually write circuits you write
a system of constraints so the process
is that you have a problem you compute
the solution to the problem and then you
write some constraints that verify the
solution to this
problem um so in this case
uh actually I would say not all proof
systems are like this for instance gkr
is not like this but the ones that most
people will be familiar with R1 CS ccs
blanish and a arithmetization are like
this and an example of this behavior is
that if you want to prove a division you
don't write a division constraint you
write a multiplying
constraint on the other hand with MPC
and FH we actually have bu
or arithmetic
circuits and in this case we need to
create a circuit that encodes the
behavior of the program and the circuit
will be fully evaluated from the inputs
to the intermediate wires and to the
final output so we cannot skip any
computation there we cannot inject some
witness and use
it one similarity that Brian already
discussed is that doing branching is
hard in like technically we don't have
branching so if we have a loop we have
to unroll it if we have a condition we
need to explore both paths and then
converge um in constraints we'll
probably assign uh do constraints that
assign the possible results of every
Branch to a signal and then constraint
that signal to be the result with
Boolean circuits or arithmetic circuits
it's going to be similar as a circuit
that textb pass and then
converges uh another difference is the
uh the ownership of the data in ZK
there's a single owner of the data so
you only have to think to think about
private data and public data but in NPC
or multi party FH the data that is used
as input can come from different parties
so it's not just private but it's
private from whom or for whom
um and this applies to the inputs but
also the outputs you may want to write
some Logics that uh where the output is
only revealed to some parties to a
subset of
parties another big difference is that
in uh
ZK usually we get parallelism in the
proof system level but in NPC and FHA we
can do paraly paralyzation in the
circuit level so for instance if we can
organize our Circuit by
layers where there's no dependency
between nodes in the same layer we can
evaluate all the gates in one layer in
parallel which is a great way to
accelerate the
performance another Point most of the ZK
proof systems use field
arithmetic uh in FH or
NPC there are some solutions that use
bull that use arithmetic circuits but
others use Boolean and when we work with
booleans we are in a world that is more
familiar to regular programming because
we can simply emulate the 8bit integer
these um maybe harder to reason wrapping
behaviors uh another difference is the
state of circuit compilers I think in ZK
the current Solutions are quite mature
there's many options they have very good
Integrations I think part of this is
because um a lot of people have built
applications using ZK so this has uh
driven a lot of investment in developing
this tooling on the other hand FH and
MPC has been less used in practice so
there's a lot of tooling that I would
say has received less user feedback and
hasn't had the opportunity to mature and
get easy here but there there's some
tooling but probably we can get
better and this is the end of my
presentation thank
you all
right great closing
slide another round of
applause uh I'm going to quickly plug as
we set up our next computer I'm going to
quickly plug plug the programmable
cryptography textbooks you've probably
all been able to snag one if you haven't
been able to grab a programmable
cryptography textbook they're in the
back corner there that's the last of our
stock uh so when it's gone it is gone
and um trying to think if there's
anything else left to plug if you've
been collecting the frogs our frog shop
will be open uh probably for just a
little bit after this CLS so please stop
by there and um yeah we uh we're just
going to
get the next session started in about 30
seconds after this machine is set up we
will have a little break so at the uh
end of this particular block we will
have a not this talk but this block of
talks we will have a little break so
there will be a time for grabbing a
quick coffee and bathroom break before
we get into the next session after this
led by Richard from the zup pass team
and are we good to go all right our next
session is going to be from Han Jen and
he's going to talk to us about rewriting
Phantom Zone let's let's give it up for
H hello I'm H from PSC and today I would
like to share uh some experience during
the rewrite of fantome and I will try to
explain the coast breakdown of it to
show you more idea why it is
still and as as you can see the Frog gam
like the Frog mov slow because each one
bit binary operation text off resarch 30
millisecond on a laptop with the FI uh
fhw scheme we are using and here's a
reference uh parameter for for reference
and 30 millisecond is roughly a billion
uh times overhead compared to a commoda
laptop so uh that's why the Frog zone
game looks a bit slow and among this 30
millisecond uh there almost 80% of time
is consumed by a repeated uh routine
that uh I I show you uh quickly so this
routine looks like this uh we take a a a
polinomial from the cyer tax which is a
vector of a
u64 integer and we decompose it into uh
multiple polinomial with small lims in
order to do some multiplication with the
Boost trapping key we need to do fft it
uh and send it to evalation domain and
multiply with the Boost driving key and
finally get back to Co efficient form
and this looks like a simple and quick
to compute but actually in a single
boost trapping we have to repeat this uh
routine for around 1770 time and that's
why uh and and that takes roughly 80% of
the 30
millisecond and if we break it even uh
smaller and you can see that the point
wise M and sum takes roughly 40% of the
whole boost driving
time so if we can try to improve uh each
of of this component with signif
significant uh amount then we can
improve the the Boost driving time and
and for the the the
fren so here's the uh tricks that uh we
in Fon currently we have already applied
so for example we use uh complex fft
instead of number Zing transform to try
to reduce the number of uh uh modular
reduction to do to speed up the the
overall REM
multiplication and also we try to reuse
the pre-allocated memory for uh for the
routine I just show but uh we haven't
done there there are more still there
there are still more stuff to do for
example on engineering side uh as we can
see the most like there are roughly 40%
of time we are doing the pointwise
multiplication and sum so maybe the auto
vectorization is not so good yet so we
can try to man manually make everything
simd or we can even try to code the H
evaluator into
GPU and application wise uh maybe we can
try to make custom Lookout table
generate by the compiler if they are
many repeated uh gate so we can merge
multiple trapping into a single
one and on scheme side uh recently there
are many cool paper that can try to uh
boost trapping multiple cyber Texs at a
single boost trapping so it can get
faster adti boost
trapping so yeah there are still many
stuff to do to improve The Phantom Zone
uh performance so if you are uh
currently looking for project to ha
count and the the problem is interested
uh is interesting to you maybe you
Fantan zone is a good place to
go so here is the links to the Fantan
Zone repository and some paper that uh
we are
using and that's it thank you
thank you Han uh you've got three
minutes do you want to take any
questions or do you want to yeah yeah
yeah do we have any
questions don't be shy not a okay we've
got a question back uh here all right
this guy's faster than me he's
practiced thank you Han it was really
cool what is the final more or less
speed difference that you got uh of
entity versus complex fft in your
experiments I'm sorry could you repeat
that yeah no worries uh after running
the benchmarks between ntity and complex
fft which is the Improvement that you
got approximately and do you think you
can do better than that or like this
like ends there yes so on on computer
like not on CPU I think uh fft already
give a huge Improvement on entity and I
guess that's already very good because I
believe people already optimize fft for
a long while so I think it's it's I mean
my imagination is it's roughly there so
I guess the next step will be GPU or
like other mathematically Improvement
yeah that's how I feel thank you all
right thank you H another round of
applause thank you thank
you all right before I uh introduce our
next speaker just a little bit of hoste
keeping so this is our last uh speaker
for this block and as I mentioned before
we're going to have a little break in
between where you can hit the washroom
grab a coffee and then afterwards we're
going to have a whole second half of
programming the theme for that one is
building consumer apps with programmable
cryptography and uh Richard Lou who's
one of the members of the zup pass team
has curated a whole afternoon of kind of
like more uh Hands-On and explanations
around building consumer apps with
programmable crypto
cryptography obviously through the zup
pass lens so that's going to happen here
uh after Riley's talk we're going to
take a break and then we're going to
come back for
that and uh I'm going to keep talking
for a little bit because we're still
figuring out the machine swap keep
talking
yeah keep going okay
um oh man I should have prepared some
jokes or something like that this is a
great little LED thing you've got going
on your frog br Beret right now um
another fun little fact now that I'm
seeing the Frog Berets and I know we ran
out of frog hats which a lot of people
were after fun fact in the second
section we're going to be using mircat
for the Q&amp;A and also the folks at mircat
have been given some swag and we're
going to be giving that swag out to the
people who are number one on the mircat
leaderboard so you know get asking
questions in the second session if you
didn't get a hat and you want a hat and
I think at this point we're good
um all right uh we're going to bring up
Riley she's going to talk to us about
mpf as a privacy preserving framework so
let's uh give a round of applause for
Riley and welcome her to the stage and
thank you to all of you guys for
sticking around for the whole session so
let's uh let's put our hands together
Riley uh hi everyone my name is Riley
Wong my pronouns are they them um I'm
going to give a heads up this is going
to be really fast
and there is a section about reporting
abuse if you need to like emotionally
prepare for that um so for an
introduction about me my background I'm
an independent researcher I'm the
principal of emergent research which is
a research lab and consultancy for
privacy and governance and I'm also
currently a research fellow ZX Park so I
investigate applications of emerging
privacy and cryptography tools with an
emphasis on co-designing for vulnerable
communities as well as building
infrastructure for Collective agency and
consent so I think a lot about how
emerging cryptographic tools such as ZK
MPC and fhe can be built in tandem with
cultural and Community work especially
around topics of consent digital
intimacy and Community
safety so I think we can kind of speed
through this a little bit um yeah MPC uh
good for multiple parties um
contributing private data towards a
joint computation it's relevant for
collectives involving multiple people
and it also creates opportunities for
Collective consent mechanisms that are
mathematically guaranteed
um FHA makes it possible to run
computations on encrypted data so the
data stays encrypted throughout the
entire process including while in
transit and m f is the best of both
worlds and that you can compute on
encrypted data for multiple parties um
yeah so as demonstrated um we do have
working demos and libraries for this it
is still in development and not quite
production ready that being said I think
now is a great time to steer the
direction of how these tools are being
developed by prioritizing real world
applications that benefit existing
communities most in need of privacy
protections so uh we can cover some
potential applications of this for
vulnerable
communities um so mpf is really great
for coordination problems where if
you're one person there's a penalty to
taking some kind of staner action at the
same time when you have multip multiple
people with the same staner action you
now have Collective power written
numbers so uh one example would be for
labor organizing so if you want to
unionize your workplace if you're the
only person publicly taking a stance
about being pro-union you probably will
get fired even though it is illegal um
using something like MP fhe we can make
it possible to privately commit to being
pro-union so you can say I'm Pro Union
and I only want this information
revealed if at least 20 other people in
my workplace or at least 50% of my
workplace also makes this commitment and
that information is only revealed if
that threshold is reached and otherwise
stays private
and privacy is important here because if
your employer finds out that they're
unionizing efforts they might fire you
hire a union busting firm they can you
know put you on leave Etc but if you
have enough people and only uh unionize
when that threshold is reached you have
now built Collective power at your
workplace you can collectively Barden
for better working conditions better
wages
Etc um MP fhd is also really great for
coordinating win-win outcomes for any
kind of prisoners dilemma style
situation um which is like a situ where
Collective cooperation is the best case
scenario and we want that um but only on
the condition that the other party
cooperates and so you can reduce the
risk um of penalty by saying I'm willing
if you're willing and having that be uh
privacy preserving and one advantage
that mpf has over something like trusted
executive environments for example is
that you can build uh governance
mechanisms based on Collective consent
so because the information can only be
decrypted with enough decryption shares
um whether you grant or revoke consent
you your consent becomes backed by this
cryptographic
guarantee um other applications for mpf
um coining protest is a good example
also if not enough people show up that
can come with a lot of risks of you know
arrest doxing police brutality physical
harm so you want to keep your identity
private um uh and only have that be
revealed When You Reach some kind of
threshold um so for example at least six
of the community organizers in Ferguson
mysteriously died um similarly with
whistleblowing two of the Boeing
whistleblowers mysteriously
di um also useful for this idea of data
striking so um it's a way of
coordinating
um uh in response to Major platforms or
authoritarian institutions so you can
coordinate mass deletions of like
deleting your account deleting your data
Mass unfollowing certain figures Mass
 up the AL gthm at the same time
um another really useful application
would be an mpf statistics Library um
where you want to collect uh information
about your community um at the same time
if that database of uh community members
as leaked you've basically created a
list of people to Target um at the same
time you want to be able to make
informed decisions about your community
like how old are we where do we live uh
what are our finances like what's the
race ethnicity gender dis ibility status
these are all things that benefit
community building and organizing um in
a way that involves uh very sensitive
information around identity um and I
really want to emphasize that these
communities listed here um are very much
directly impacted by not having privacy
Protections in a very real material and
physical way um particularly at this
point in history um privacy protections
have always been important for these
communities and I also think that these
needs are about to be heavily
exacerbated on a pretty wide scale very
soon so if there's one takeaway from
this talk I really hope it's uh this um
from my personal experience being in
privacy in cryptography there's a huge
gap between people building the Privacy
tools and the people who need them the
most so I really urge you to work
directly alongside communities that are
most directly impacted by not having
privacy
protections um and one way to do this is
through participatory co-design and so
instead of Designing for communities
you're uh designing by and with
communities so it's about communicating
and interfacing with community members
directly
listening deeply and building a holistic
understanding of the full context of how
and why these privacy needs exist what
the specifics are in terms of challenges
risks and
priorities so given that background um
we can take a look at a specific use
case so reporting abuse is a situation
where as an individual there's a real
risk of danger and consequence at the
same time when multiple people submit a
report you can build Collective power
written
numbers so this problem is relevant to
many communities uh true truthfully and
unfortunate including this one and the
current state of affairs is that people
who experience abuse by a vast majority
do not report um for reasons including
risk of retaliation escalation of harm
risk to physical and emotional safety
there is some prior work to this called
project Kalisto that also uses
cryptographic techniques such as Shamir
um and this paper came out in 2018 so a
lot of these tools and technologies have
not been made yet and we've made a lot
of progress in the past six
years so a sample system design for
something like this uh may involve
identity ver identity verification uh
using ZK email which is a privacy
preserving way uh to verify identity um
submitters uh can privately submit a
unique identifier naming the perpetrator
through some kind of community directory
um and having a unique identifier um is
really helpful for simplifying the
matching process on the like MP fhe side
becomes a simple integer equivalence
check um and when there are matches uh
submitters can choose uh next steps and
in terms of wanting to share contact
information um setting thresholds for
how many matches they want before they
uh share information and being able to
make a collective decision about what to
next um so here are some additional
Technical Resources uh I think ZK email
Phantom Zone haunted psse uh all these
people are here this week
um thank you yeah I'm really interested
in building out this kind of
infrastructure so please come talk to me
I'll be in that back corner after this
talk um thanks
amazing thank you so much Riley that's
awesome um these guys will take your mic
Let's uh let's give another round of
applause for Riley that was a really
awesome talk I think um frogs are fun
collecting frogs is fun games are fun
and those are all awesome and they push
technology and I'm really happy that we
got to end with that presentation to
provide some balance for for other stuff
that this Tech can be used for um we are
going to take a break
uh it's going to be an 11-minute break
so it is 2:04 and at 2:15 we are going
to come back here and Richard from the
zup pass team is going to show us how we
can uh build consumer apps with
programmable cryptography so back here
in 11 now 10 minutes and we're going to
kick off that session uh as Riley
mentioned she'll be hanging around some
other folks that you saw present will be
hanging around so feel free to chat to
them I know we have condensed time for
q&amp;as thank you guys very much thank you
so much for your time
that's
amazing awesome all right thanks for
coming back for session to building
consumer apps with programmable
cryptography I see a few more people
trickling in so I'm just going to give
one minute for people to get seated and
get sorted you'll notice for this
session I've got a QR code up over my
shoulder here that QR code takes you to
this session link inside of the Devcon
app if you scroll to the bottom of the
session link you'll see a Q&amp;A section if
you click on the Q&amp;A section our lovely
friends from mirat have created a uh
basically a q app um so the way this is
going to work uh we're not going to have
any q&amp;as for Richard but everybody else
that gets introduced after uh we are
going to have q&amp;as for them so if you
scan this app you go to the event link
you scroll to the bottom you click on
the Q&amp;A button you can submit and vote
on each other's questions and uh I will
ask them to our panelists uh so without
further Ado we're gonna give a uh warm
Round of Applause for Richard liou from
zup pass team and he's going to come up
to us sorry he's going to come up here
and introduce the uh session topic and
the uh folks we're going to be hearing
from so let's let's give him a round of
applause
please hello everyone um thanks for
coming out last day of Devcon I know a
lot of you guys are travel
internationally so it's not easy to come
out on a Friday afternoon um one thing
I'll say before we start is if there's a
lot of open seats in the front here
um there's desks too if you want to pull
out laptops so people coming in just
want to move up towards the front fill
it up uh that'd be great so um this is
actually mid presentation but what I
wanted to do is um start off with a bit
of an intro to this session and and why
we're doing this we have a you know
really big cast of folks here from xero
Park from ethereum here today and I
think one thing I wanted to you know
maybe set the stage for and because I do
want the actual developers of the
different apps and Frameworks to speak
more on the details but just sort of
more why are we doing this um what is
the significance of all these apps we
deploy at this conference so I'll start
a bit with that um but first actually
just a bit of an anatomy of this session
so we have an hour and a half for you
folks here um and for those live
streaming also thanks for tuning in
we'll start with two um after my session
we'll start with two lightning talks
from uh one from the Frog net by Forest
and the other on mircat which is this
Q&amp;A app we're using that uses zass um
following these lightning talks we'll
get into the workshops so these will be
from the library developers Veronica and
Rob who will introduce um one is going
through and building a kyc system with
pods and gpcs a ZK kyc system and the
other is introducing this zapi which is
the framework that both frog crypto and
Mir have used for building on top of zup
pass cool so I want to just
um spend some time on why we're doing
this and I come back to this uh
interview or blog post by italic which
is talking about sort of what he sees as
a future of ethereum and one thing that
stuck out is you know how do we actually
make a theum something that people use
Beyond just sort of like the interesting
ideas we had for the past decade um how
do we actually scale this up and I think
that there's been a lot of really
exciting Direction in terms of um you
know defi stable coins prediction
markets all those many things that other
people have talk about but this
direction of making the internet more
interoperable more legible um this
direction this other direction of
ethereum has been kind of in our opinion
underexplored and um adding on to sort
of you know gub sheep's talks on uh
contact with reality I think a lot of
this effort around zup pass and pods is
very much in this direction of how can
we get to making something useful um in
this other area or space of ethereum's
values and one thing I want to talk
about is how you know we're all at a
conference and how we're how conferences
can serve as essentially you know early
glimpses of reality for the future right
so folks might be familiar with these
two pictures on the left is Doug
Engelbert who was uh formerly a pretty
unknown Cornell professor who in 1968
introduced essentially personal
Computing to a wide stage um and again
was all hard-coded there's no actual
product right but people got the people
saw For the First Time The Mouse um um
you know objectoriented programming you
know typing on video calling all these
different things on the right I have a
screenshot of Twitter which was first
available which was available at South
by Southwest at 2007 and it was the
first time a lot of people were
experiencing social media um which had
come to Define so much of this decade
for better than For Worse um so one
prompt I want to say is what you know
given we're on a theum conference what
did it feel like going to an ethereum
conference 5 to 10 years ago and I'll
preface this with I actually wasn't part
of the ethereum uh ecosystem 5 10 years
ago so I'm I'm sort of guessing here but
uh and I'll focus on it from a
technology perspective um so you kind of
have a few different you know core
functions of a conference right you have
your ticketing system who's allowed to
come in you have your Communications
there's things like talks events
whatever right and you got these people
that come in um and there's data that
lives here there's for example your
ticketing data are you allowed to come
in there's messages you send to people
um and there's things you do at talks
for example and and you know that was 5
about 10 years well the main thing
that's changed is really just this
bolded Arrow here which is now you can
you know pay for your tickets in
ethereum and I I think we can do a lot
better right we can do a lot better than
just just payments um so just to explore
what could it look like in the future to
go to an ethereum conference right um
well all these different functions you
know can be smart contracts we can all
our data stored locally right um
everything is composable uh essentially
an ethereum conference or eventually the
world should run on a theem or actually
have some plausible story for running in
this in this manner and my take is that
if we can't actually get to something
like this uh then that's an indication
of something being seriously wrong um in
terms of what we're all building here
right so here's one exercise which is
what would it take to run a conference
like this entirely on Main net rollups
um you know what are the benefits I
think people probably here already you
know pilled enough to to go but I'll
just I'll just sort of go through
composability ownership
permissionless everything's verifiable
which means it's portable across
different platforms including all
transformations on this data um but this
is obviously not possible because of a
bunch of obstacles uh everything's
public except for cryptography um unless
you use Advanced cryptography you know
which others have explored in this
session a lot of the data is still out
there on Google um and other services
development is really hard I mean just
to like the kind of extremely
adversarial environment of smart
contract development um and it's
expensive gas fees etc etc um so in 2024
going all in is still too high friction
and that doesn't mean that we can't
start taking steps in this direction
right we can't start you know 8020 in
ways to uh start getting contact with
reality and start deploying these sorts
of um you know mechanisms and and one
observation is uh applications like zup
pass have have really started to make
this possible um but specifically
because of two different things one
thing one of these things is called pods
which essentially interoperable data uh
this interoperable data format that lets
you specify essentially arbitrary
statements of the world and a proof of
it existence and an ecosystem of apps
which we're currently calling zaps and
the data is not stored on ethereum the
compute doesn't happen on ethereum all
the time but it's easily verifiable on
different Computing platforms it's
easily portable across different
applications and just to give a quick
primer um kind of repeating what I said
here's these vocabulary terms that you
don't have to take notes on because uh
folks will be diving deeper them into
them in the next few uh in next two
hours so um here's some examples of PODS
you might be familiar with just from
this week right your tickets other
tickets to other events have you've been
to frogs collecting you know essentially
poap like uh event Collectibles from
going to certain talks um and also
different kinds of zaps we have
everything from getting testet eth to uh
things like mixing two frogs together to
things like conference infrastructure
like zcat which determines you know
who's allowed to be in the telegram
group um and given all these new
technologies what can going a Devcon
really feel like
right well you know these applications
essentially form a network um where the
data is stored locally within your zoo
pass as pods but you can take them at
will between different applications and
you can use proofs of them in order to
get access to Services um which is a
really interesting you know which
obviously not like the full scope of
what's interesting with uh you know
program cryptography but it's at least a
step in this direction um and one
interesting that's thing that's sort of
organically happened with net is that
it's sort of expanded into a tree of
different apps that consume frog data to
right there's things like necklace you
know this website that stores necklace
QRS there's things that let you m mix
two frogs together there's things that
let you uh verify frogs on chain so
that's been really exciting to sort of
see that happen because of the new
capabilities from
pods um and you know obviously
predicting is really hard uh but what's
a projection of what this looks like and
at a grand scale Beyond conference data
well you know things like check-in
things like Communications things like
voting uh Games social social right they
they have analoges in the real world
Beyond what's going on at Devcon so um I
think you can pretty quickly sort of see
the pattern match into like how this is
actually relevant um and why it's
actually worth caring about even if you
don't care much about just this uh you
know things that happen within this
conference um that's the sort of primer
on you know introducing these topics and
why this is interesting uh I'll sort of
move more into a kind of uh just fun
phase of requests for projects I know a
lot of folks here are developers um and
I just want to throw out some ideas uh
ahead of these sessions so the first
thing is a frog social graph so um you
know I can see my friends in my screen
right but I want to be able to see sort
of more analytics information about
what's going on I want to be able to see
things more visually right and um on the
left here was uh a graph from the the
actually actually the mircat team when
they were at e Berlin they created this
sort of social graph of Zupas attendees
and I'm wondering if you know that
should be an extension of the Frog
Friend Finder on frog social uh another
direction is you can have something like
Discovery be better right um you know on
the website where where people have been
posting their QRS what I realized that
this is this is really exciting and cool
but it's not really like a a fun easy
interface to explore around so there's
there's this direction of like hey maybe
I have five swipes an hour to go through
and make friends with people refreshes
every hour or something like that um
that would be a cool sort of front- end
project to explore um one thing we're
thinking about as well is moving beyond
uh what what we've been calling pod one
which is sort of the ZK friendly version
of this data and extending into more
real world data that is more
cryptographically difficult to verify or
to prove and verify on uh lighter
devices um so things like ZK email and
TLS notary are are things that would be
exciting to get into the Pod
format so that closes off a lot of um my
introduction I want to sort of seed the
floor to our presenters for today um
specifically Forest who's coming up next
to explain FR FR crypto and on that
light I want to show this little
surprise here uh
into the froggy
void thank you
all all right awesome another round of
applause for Richard
everybody we will if you didn't get a
chance for that QR code we'll try to get
it back up at the uh the end of this
session
amazing as Richard mentioned mentioned
we're going to be having a series of
lightning talks uh actually just a
couple lightning talks and then we'll
get into some longer form sessions uh if
you need anything to drink there's a
whole table of water at the back uh
they've got the little cans of water so
help yourself I'm also seeing some frog
plushies being laid out so if you
haven't been able to get yourself a
little frog plushy necklace and you want
one we've also got some at the back
there as well and uh how we doing we're
looking good amazing so let's welcome to
the stage Forest uh Forest is going to
tell us more about frog net and frog
crypto and all the fun stuff so round of
applause for Forest
please
hello hi uh so my name is Forest um I'm
the main developer for the FR crypto
um and uh if you were at Dev connet last
year you probably have played FR crypto
um and this year it's kind of a similar
game but it's also kind of quite friend
underneath so I will be talking a little
bit about that uh during the session um
so first of all what's for crypto you
probably already seen it uh when you use
the zo pass this year there is a button
that just says score and when you click
into it you are brought into this
experience and if you have stopped by
our frog physical Bruce you probably
receive this planet uh which explains
there are kind of three main ways of
getting frogs this year uh so the first
first uh way is you click the click the
button every 15 minutes and then the
second way is there are physical frogs
around the venues which you can scan
with your phone or rather tap with your
phone and then the Third Way is uh many
of you have already had the Frog
necklaces uh which has a QR code on it
and by scanning the QR code we'll be
able to connect with other froggy uh or
rather make any uh make other uh froggy
friends uh and then finally once you
have lots of frog points uh you can go
to our frog shop to get more
swags um
so kind of dive deeper a little bit um
so last year this is might be what you
have seen and then this is this year's
um the main differences is actually um
last year this was actually part of the
core uh uh zass applications um and then
this year uh this is actually built as a
zap so what is a zap a zap is a kind of
a dedicated um
yes oh yeah
um so the the so the zap is really kind
of like a Dap if you will uh where it is
a kind of a standalone applications uh
but can be connected to the zass which
if you remember it's it's a kind of
endtoend
encrypted uh kind of data St storage and
more than that um but that's kind of one
of the primary go uh use cases for us uh
where you can kind of create these um uh
store these pods um in in the sup pass
and also refr it uh so kind of one of
the significant uh thing you can see is
that uh you probably access the the fra
crypto through the the zup pass uh
interface uh but you can similarly just
the same access this as a standalone app
which um it actually happens uh the the
other way around where it in when you
visit in this mode uh it actually has a
hidden zoo pass as if frame in this
domain versus when you visit in the zoo
pass um the Frog crypto is lives in a ey
frame within the zpass um but in either
case that they both establish a
connections uh so that your data can
move around between uh your data
storaging zass and the zap of the far
crypto zap itself um so there is this
wonderful documentation that being put
put by the core developer uh of pod and
and Z API um and dive more deeper into
how you could build a similar zap
yourself uh and even consume data from
um data that that's produced by other
apps which is kind of the whole point uh
of of of pod and
zass um so here just is a quick view
view of kind of the S of the core data
structure of the the Frog uh on the
right this is what you see uh in the app
and on the left this is like individual
entries uh to to kind of represent uh
where your frog underneath uh and then
finally we have the signature and the
center public key uh again kind of one
of the cool use cases is this is a ZK
friendly data structure so you can use
this um kind of frog to build any kind
of H app that you might want that
whether that is that leverages Z
knowledge or not uh like Richard just
mentioned uh in the earlier
session um jumping onto kind of the
second way you can clap frogs uh if you
have seen these uh physical frogs around
the venue uh you can tap with your phone
if your phone have nsse chips um and
that will give you a frog um and so
underneath it what really happens is if
you remember uh you have the buttons you
can click to collect frogs every kind of
these physical frogs is acts like their
own button so really what happens is
there's these invisible buttons that you
can uh you can click on uh and then
every these NFC chips H uh creates a
signature uh whenever you tap it and
also create a nuns and so this serve
become a nullifier we use so that uh
every T tap can be consumed only once uh
and then the back end would uh the
server once verifies that that will
issue AP part uh to
you uh and then the thirdly is kind of
um this is a um great new feature that
we made this year called frog social uh
where people can connect with each other
um the way that works is actually you're
assigning a frog yourself uh so up to
now all your frog are signed by a single
private key that's stored by in our
server uh and as you probably know every
zoo pass has your yourself have your own
private key pair uh so what frog social
leverages is that allows you to sign
your own special frogs and send to each
other uh and in fact this has taken off
uh quite widely for us um uh people are
have been been super creative on how
they can kind of uh create more more
connections uh and then there are lots
of enthusiastic uh people who kind of
build app around it and even write blog
post around it um and uh in fact they we
had uh 5
uh over these only four days um where uh
four 400,000 out of them are frog uh
connections prods uh where uh more than
regular pods that you collect from the
button and cyber
frogs uh finally I just want to quickly
plug on uh the two of the amazing
applications uh one is allows you to use
the pods from frog crypto to create new
pods and then the other one that uh
build from our build Guild uh friends
which allows you to uh kind of take pods
and put them on chain um yeah so kind of
that's the uh end of my
sessions all
right if you'll if you'll entertain us
here for a second Forest um we have got
some questions Visa our mircat app
um backstory of frog lore I'll let you
pick do you want to answer the question
what is the backstory of the frog frog
lore uh so um if you're asking about
frog crypto itself this is more just
around like programmable cryptography
and and people said we had the prog
crypto conference last year and that's
where the Frog crypto came from um but
if you're asking individual lore of the
Frog themsel we have amazing person
called John and he's The Mastermind
behind a lot of creatives here
um can you model simple CPU like Intel
session uh tell us the secrets of the
Void yes uh the secrets of the Void is a
great segue to the next session amazing
okay is there is the other session that
you said this uh CPU question might be
answered is there an actual session or
is that a I think that's that's Brian's
question from all right well we'll get
the answer to that during Brian and uh
scan those void QRS and also stay tuned
for the next uh session to get your
answer to the void I'm going to wipe all
these questions clean and allow you to
ask new questions for the next uh for
the next segment and that's actually a
great segue uh because up next we're
going to have the mircat team so if we
can have a round of applause for Richard
we'll let him get or sorry Forest we'll
let him get uh get his machine unplugged
and we'll swap in a new machine and get
the mircat team up here so than thank
you so much Forest there's uh there's a
little bit more lore behind the Frog
crypto it's actually debated I was
hearing it debated at a dinner the other
night as to whether it was a typo in a
telegram chat H or uh you've got their
machine set up okay whether it was a
typo and a telegram chat or a marketing
stunt or something like that but we'll
we'll we'll talk about that a little bit
more later I thought I had to kill more
time these guys are too quick these Pros
are too quick for me to ramble on all
right Miriam and florium from mircat
let's give them a warm Round of Applause
they've been working their butts off
conference okay does this work yeah okay
hi thank you for coming to our talk
today we created mircat you might have
seen it on Twitter as a meme you might
have seen it at a talk you actually
intended you might have engaged with
mircat by letting us prove and verify
your uh Defcon ticket and give you an
identity
um you might have collected cards
attendance parts and generated them into
your zp pass you might have created
speaker feedback pots and collected
those and also let speakers collect uh
their side of the
thing mircat looks like a web app it is
in a way um mircat itself and its main
functionality is a speaker audience um
engagement tool for live audiences and
our vision really is to take in real
life events in the connections and
interactions and engagement that people
have there and uh speakers have With
Their audience and bring it into a
virtual world and make Virtual Worlds
more real and because we are humans and
we care about our privacy we wanted to
make sure that anything we build within
this um yeah worlds uh we make with
privacy in mind and use the
cryptographic tools available to us and
so mircat is also um using the toolkit
the prog programmable cryptography
toolkit from from ZX Park and it's a zap
that's use that uses the zapi that
generates and consumes pots provable
object data sets um as Parts but also as
P pcds which is then the proof carrying
data that gpcs can run on and on top of
all of this or wrapped uh we take the
pots and wrap them in um supas so it's
integrated with
supas to give you an overview of the
mircat app and the parts we generate and
consume when users or attendees go to an
event they scan a QR code they right
away see the functions we have so to
join the Q&amp;A to collect a card to
generate and collect a speaker feedback
card and they can see their questions
but to interact with them they need to
um prove their defc ticket so the first
um part PCD that we use and do is the
identity is for identity the second one
that we generate is an attendance part
when you click collect um card and it
looks like this in your zad and then on
the back side of it you can see all the
attributes um for example because mirat
is a fully open source app when you go
on our Twitter profile you can get
access to the GitHub repo and create
extensions on top of it it has an open
API and you can also use the um parts
that yeah people created for example you
could be wanting to reward your users
for attending 10 tracks uh 10 sessions
of the um Cipher Punk track um just this
one idea and then this is the first part
which is an ownership part and then the
second part that we let um people
generate is the speaker feedback pod
which is a peer-to-peer pod where both
the speaker and the um attendee gets it
into their zpass as we see uh yeah a vir
um a mircat talk space is kind of a
world where everybody has a role so the
speaker the attendee but also the
moderator so the moderator has an inter
face there as well where they can play
around and there could be more pods um
that we could generate for example
contribution pods for all the questions
asked or also for um the hearts that
people click for liking or reacting to a
talk or the up votes and we might do
this down the road or you're all invited
to build on top of mircat as an
extension or on top of the pots um and
there's also some limitations within
supas for example um for certain data
limits and um I'll let Florian dive more
deeper into the technical
details yeah hello everyone also for me
I'm going to try to speedrun technology
now um so we have three levels of
integration that you can do and you can
use for your applications and I want to
go through them um so the first one is
uh using Zupas as an identity provider
that's basically what we did for you to
ask questions for V for voting and also
for reaction um this roughly is like
what the flow looks like so basically we
uh we create a a ticket proof on in side
of the the web up this proof will be
sent to our backend it will be verified
and then you get credentials that you
can use to um create questions react or
vote however quick reality check this is
how it was implemented until Monday
night uh Tuesday night um and then we
realized that uh it can be hard uh so
there's a few challenges that we faced
once we roll this out to 12,000 people
uh one was like there's an extra popup
screen that asked people to proof stuff
which from the ux side everybody's is
like what is ticket proving even what is
GPC so one thing that was was hard and
we also like had to remove at some point
the other thing is that uh GPC proving
on ticket proving on mobile took
sometimes up to 10 seconds something
that is like from a user experience
point and we're talking about consumer
applications here can be a very long
time and and lastly there was some
setups and specifically older devices
where this even failed in the end so
this is the reason why we actually
changed up the flow and then allowed
people to provide us the pots instead of
creating the ticket proofs right on on
device however going on I want to go to
the second level of integration that you
can do with your app which is the
ownership part so um collecting the
attendance pod um this is roughly what
it look like on our end so when you scan
the session QR code you will be able to
request an attendance Po from our
backend this is this session QR code
that you see next to the screen usually
has a secret in it so going through the
pdas and clicking every single link will
not help you um but once you do that the
back end will allow to create a pot that
is signed by our server and then be sent
uh to your uh zpass I wanted to quickly
also show you what this pod looks like
and hint a few things here so one thing
that is recommended to have is the Pod
type we use the reverse domain and then
slash the type uh as well as the version
number for people that are consuming it
and there's a few special Fields you can
make to look it to make it look pretty
uh and last but not least the owner is
really important here uh because
otherwise we have we could have people
basically sharing pots with with other
folks but we really want to make sure
that the owner is bound to like one of
suest moving on um last integration step
that I want to talk about and something
that we Al also heard about in for
crypto already is the P P2P approach um
so basically this is what we do with the
feedback pots so attendees can sign a
pot which is sent to our server acting
as a relay basically so we will forward
uh the pot later to the speaker and then
the speaker can pass it or like save it
in their in their Su
pass again here's a quick summary of
what we're doing so there's a pot type
and then also a version uh this one
doesn't contain an owner because uh we
we uh we didn't got to the ability to
share actually the the owner key of the
speaker um but ideally you would always
have like an owner inside of a pod so
quick takeaways for you uh and and
learnings um that you can uh use for
your apps uh one is like integration key
so for us a major push was that Zas was
the ticketing Zas was the identity so
coming to this conference with this
integration was key um the other thing
is like client side proving as I
mentioned can be uh sometimes difficult
and that's why we needed to make
adjustments uh and the last thing I
wanted to talk about is uh keep your
Downstream consumption in in mind so who
else will be using the pots that you
create um because probably have already
thought about it a little bit but our
parts that we have could also be used in
other use cases
um uh around this event thanks so much
awesome thanks so much M
cat we we uh we're a little tight on
time so I think we have time for one
question the top
question how how many spoofs does suass
mirat frog crypto have the server
verifying proof can it be decentralized
somehow or run
locally uh is this one of us I'm not
sure maybe we can talk about it off
offline but uh I think like the
deratization one might be good uh the
dazation part might be uh where it comes
tricky because we we still want to uh
authenticate basically a certain
attendance pot that you can then use and
say like hey this is was actually
created by us or in in case of the
feedback pot something that's always
that's been created by a certain supas
uh identity but I'm happy to hear any
ideas how how we can bring it there
basically in the end
all right uh I think this DNS ens
question was actually for a previous
talk so let's just skip to the Pod
related features and then we're going to
have to say thank you guys and if you
guys have more questions for the mircat
team this is what they look like they'll
be hanging around after the after the
workshop you can come chat to them I
should answer that for future
conferences we have ideas such as
letting um people answer questions after
the event is over and while the talk
space is still open like for example if
you click into the passport app now onto
a mircat link you can still see the
questions so they didn't automatically
shut but speakers could be unable to
answer there or get more in touch with
the audience members uh there's also a
dip that we wrote In order to a Defcon
Improvement proposal that lists out some
of the extensions idea we had if
somebody um is interested in that or
yeah thank you awesome thanks so much
um so for new oh can I have the QR code
back for a second just for 30 seconds
so uh just for newcomers once again that
was the mircat team we are using mircat
for Q&amp;A for this whole session you can
scan this code it'll take you to the
session Link in the Devcon app if you
scroll to the bottom of that session
link you'll see there's a Q&amp;A section
you can click on that Q&amp;A section you
can ask questions and then upvote on
your guys' questions now because we're
using the same Q&amp;A session for all of
these talks I'm actually after each talk
going to go through and wipe the
questions away because we don't want
questions from a previous talk being
answered by someone who wasn't talking
about that stuff um so basically I'm
going to go check all of these questions
out H and as our next presenter talks
Veronica you can put in questions for
her and we'll have a Q&amp;A session at the
end so uh without further Ado I'm going
to bring up uh Veronica Zang and she's
going to talk about Zoo kyc so let's
have a really warm Round of Applause for
Veronica thank you so much
hello uh I'm Veronica so I'm pretty sure
like you guys have been hearing about ZK
zero knowledge this entire week as a
builder you might be curious uh what
kind of applications you can build with
ZK and how to build it so today I'm
going to show you how to build an end to
end ZK identity
application um we are going to use two
libraries
uh pod provable object data and also GPC
uh general purpose circuit uh so how
many of you have been to the talk uh I
guess yesterday on P and GPC I think the
title is like introduction to provable
object data and ZK proofs of General uh
uh ZK proofs of Parts raise your hand if
youve been to the
session okay so for those of you who
haven't been there uh check it out when
they post the videos uh online so those
sections are very
informative okay so p and GPC are built
by zerox Park so in the past few years
zerox park has been experimenting and
building many different ZK applications
for end user use cases and during this
entire process we've been asking
ourselves how can we make this process
super super easy for other Developers to
build ZK apps and uh pod and GPC is our
answer so here is the link to the
developer documentation uh go check it
out okay so in this Workshop I'm going
to show you this app called Zoo kyc this
is a demo app I built uh using pod and
GPC I'm going to first uh show you to
demo this app show you how this app
works and then I'm going to show you how
to code this app step by step so here is
a link to the GitHub reple uh so all the
code I'm going to show you today is
going to be here um I so I really hope
after seeing this example you guys would
be inspired to build your own ZK apps
I'm always amazed by how creative people
can be uh so okay so here is also a link
to our telegram group um if you have any
questions we will be there to answer
your questions
Okay cool so let's start with the
demo um so before the demo let me tell
you a story uh so one day I have this
frog uh Tod he would like to buy a house
for his family um but he couldn't afford
it so he is looking around for a
mortgage and then uh can you guys see
let's
see okay uh so then he saw Zoolander so
Zoolander says to qualify for a loan uh
you need to have a valid government
issued ID you are not in the sanctions
list you are at least 18 years old have
at least one year of consistent
employment and have a annual salary of
at least this amount uh as some of you
who applied for mortgage before you know
you have to uh give lender lots of your
information your ID your pay stops your
lender would like get your information
from like for example ACA to to get your
credit information uh but in this case
to doesn't want to do any of those
because Todd has never heard of
Zoolander before what about what if this
thing is a fraud uh so Zoolander says
Tod don't walk away let's use this
application called zo kyc uh this is the
third party application so how does this
work you can take this piece of data we
call it proof request and then uh we
give this proof request to Zu kyc so Zu
kyc can generate a zero knowledge proof
according to this proof request and once
Todd uh gets a zero knowledge proof he
can come back and then um put his proof
here to verify that he satisfy those
requirements and uh once he verify those
requirements he would get the mortgage
uh let's take a very quick look about
what this proof request is okay so you
can see this proof request it says you
have to have parts so this is using the
library like uh approvable object data
we talked about and then you need to
have like two parts one is a government
ID pod uh and the other is pay stop pod
so for government ID you can see you
need to have like ID number uh is not
revealed so we are hiding it and this is
not a member of the sanctions list we
have like sanctions list here uh and
similarly there's like data of birth you
have to prove it's in the rench uh so
it's like to prove you are at least 18
years old uh and then we are uh skipping
to pay stab so pay stab also need to
prove this like social security number
not revealed this entry equals to the
Social Security number uh in the
government ID I'm not going to go too
much in detail here I'm going to show
you uh in detail later while I show you
the code so here uh Todd takes the proof
request goes to Z kyc and then put his
proof request here uh now you have the
proof request so to generate this proof
uh so here we are using the library
general purpose circuits GPC uh so we
are going to make proofs about two pods
one pod is ID pod the other pod is a pay
sta pod how do we get the ID pod so we
are going to get ID pod from this zuo go
Z go is like a government for the zoo so
it's like they issue like ID to the zoo
animals and that's where we are going to
get the ID pod uh so we are going to
this new government website zav and then
Tod is like putting in his information
like credentials and then log in uh so
he would he would need to like upload
his ID card here uh I'm not going to
upload it uh now but then he need to
provide his public key so here for the
identity information we are using sop
for Library okay so uh we we are going
to get the public key from here
and then this is Tod's public key and
then we are generating a ID pod uh so
here is the ID pod you can see like
there's entries um the entries has dat
of birth first name uh ID number uh last
name and social security number those
are the information we normally see from
the ID and then here we have the owner
public key this is the public key we
just pasted here so this this is like
okay we issue this pod specifically uh
to Todd and then we can also see there's
like a signature and signer public key
so this piece of information is actually
side so this signer public key is this Z
gav's Public key um you know so like
other people cannot temper with this
information and it also proves this ID p
is issued by
zav and uh so let's copy paste let's
take this ID pod and then uh put it here
the ID pod uh and next we need pay stop
pod similarly we are going to get this P
up pod from this organization called Zoo
deal what is Zoo deal Zoo deal handles
all the HR information in the zoo uh so
we are going to go to zoo deal still we
are going to putting our credentials
loging uh and then uh we are we need to
provide the public key for pod
um for Todd and then let's issue a a new
Paya pod so for payop pod we can see uh
we have like annual salary current
employer first name issue date last name
social security number uh started and uh
similarly we have this owner which is
Todd's public key this info piece of
information is also SED the signer
public key is the zoo deal public key
okay so let's so Tod take this um past
pod and then put it here so now we have
the parts uh we also have like the proof
request so we are ready to generate a
proof so here we are using like the GPC
library to generate the proof we can see
like the proof is here uh so it has like
three pieces of information the first
piece is this proof so for those of you
has been uh used like circum before you
know this is like the result from the
circum like using uh gr 16 and then we
have this like a next piece of
information is called Bond config so
this is the same uh same thing this this
matches the uh the same uh proof proof
request so basically this piece of
information is exactly the same as proof
request and then we have another uh the
last piece of information which is the
reveal the claims so here uh what we are
revealing we are revealing like uh
inside the government ID pod we are
revealing the signer public key all the
other information are hidden here we are
not showing like the data burst we are
not showing the social security number
and for pay stop pod we are revealing
the signer public key here so we are
also now revealing you know like a TOD
salary or something like that and then
here we have like owner uh membership
list and the watermark I'll expl later
okay so now we have this uh Todd has
this proof so he takes this proof and
back to the Zool lender so he give back
the proof to the zoo lender and then
Zool lender can verify the proof okay
congratulations now Todd has this uh uh
uh proof verified he can get a
mortgage cool uh thanks so like uh so
like let's uh go to the code so this is
the GitHub repo I just showed you it has
all the code
um the application I just demoed is
actually deployed so if you go here you
can go to see this deployed application
and you can try it out yourself uh and
uh then uh you know it explains the code
and the code structure and here um you
can actually run this code locally so
those are the commands you can use to
actually run it and try it out okay so
next let me actually uh show you the
code so you can see the code
um okay let's
see can you see
this okay uh yeah so let me know if it's
too small you can you can see uh
so okay so in this like apps folder uh
there are two uh there are four things
here so uh when I built this app I first
built this like P is your client and P
is your server what does it do it
actually like issu the pods uh so for
example like this this code like for the
zoo uh Zoo G and the zoo deal uh those
things leaving this like P is your
client and P your server so there there
has to be a server here because like
first for normally the government
website it needs to the server needs to
talk to the database to verify okay you
are actually to and then let me generate
a uh ID pod with your information so
that's first and the second is like
because a pod needs to be side uh so you
have to have like the private key The Zo
government's private key you can put it
on the client otherwise you would leak
the key so we need to have a server here
uh okay so let me show you the the uh
the piece of code which actually would
uh generate the Pod so this is the code
to generate the
Pod uh you can say it see it here this
is using the Pod Library so it does like
p.
side if you uh sorry if you look at
this thing side by side right um let's
see you can see like
uh like this side by side you can see
this actually matches all the
information here so for example there's
ID number there's like type and value
there's first name last name so this
part should match like this thing you
want to generate here uh and then and
then like you have to provide the
government's private key to S this piece
of data I I hope this is
self-explanatory so it's like clear how
to generate the Pod uh so that's the
first thing I did and then uh I started
building this uh Zoo lender uh because
in order to generate a proof we need a
proof request so what kind of proof you
want people to generate right uh so this
is the verifier provide a piece of
information like a proof request so this
piece of code um is inside this folder
called GPC verifier uh so let's look at
the uh code for how to generate proof
request oh okay it's here so uh to
generate proof
request uh let's see the code
here so uh if I put this side by side
you would see like this piece of code
would match exactly this piece of
information uh so basically you need to
have parts so we are going to make
proofs about two pods one part is like
this government ID pod and uh another
part is this pay St pod uh for
government ID pod what are we going to
prove okay we are going to prove that
this ID number uh revealed is false so
it's hiding uh this is not part of the
sanctions list so the sanctions list is
here right we are sanctioning those IDs
and then um there's this date of birth
also now revealed in this range so it
means you have to be at least 18 years
old uh and uh we also have social
security number also not revealed uh we
needed to provide the owner here we are
using the Sam for Library uh for the
owner so and then for pay stop uh we
needed to have social security number so
this payop social security number has to
match the government ID social security
number so it's for the same person to
and for we have start start date so this
we want to prove that like have uh like
we want to say okay have at least one
year of consistent
employment and we don't want this uh uh
let's say if someone has pay stop like
from last year and he's been unemployed
for this entire year right so we want to
know the uh issue date and have some
like rench requirement for the isal date
and this last thing we want to prove is
the annual salary at least 20K okay so I
hope I can convince you that like those
requirement we specified here is the
same as like this requirements specified
like by Zoolander so no more and no no
less um okay so there's there's also
like a a two extra things one is nulf
fire so we need to generate nulf fire to
make make sure like Tod doesn't use this
proof to get many many uh mortgages we
only we we don't want him to use this uh
p uh this proof like more than once so
nullifier would hash this external
nullifier which is kyz and also a secret
derived from uh Todd's private key uh so
we can use this NF fire here and then we
also like have a water mark uh this is
go to be carried uh to the
proof okay so that's all about the proof
request so when we have the proof
request um the next thing I'm going to
do is to generate a proof so zo kyc is
this app is a piece which generates a
proof it's aover so the code is in uh GP
uh GPC appr
client okay so let me find the code to
generate
proof
uh okay so uh this this piece of code is
inside a GPC prover client and then the
uh this is using the GPC Library so the
M call is here it's like GPC proof so
it's going to take three things one
thing is this proof config so this proof
config is a is is a proof request I just
showed you and then it's going to take a
proof inputs so the inputs uh we can we
can see the inputs here it needs to take
the parts so those are the two parts
again and it's going to take the owner
uh and also like this uh external
nullifier membership list and the water
mark those three things are also from
like the proof request uh and then the
last piece of things is called going to
take this is this artifacts URL so it's
go it needs to like either download or
somehow get this artifacts uh if you are
familiar with circum you'll know like
when you generate a proof you needed to
like have banies which is like your Z
key uh to to generate this proof so this
this is what it is so if you call this
then you would have the proof so this is
the uh what this piece of code does okay
so now you have a proof now we are going
to go to the last part which is verify
the proof uh so verify proof this piece
of code is inside a
verifier so it's here uh and then let me
show you the code let me find the verify
here okay so this is a code for verify
proof it's inside GPC verifier um so the
main piece of code here is called
calling like GPC verify uh so this is
also using the GPC Library uh so it's
going to take the proof the config and
claims so those three piece of
information is the thing I just showed
you here so those results remember has
like the proof has a config and also has
a revealed claims here uh so it's going
to take those three things and also the
artifacts URL so this artifacts URL has
like the verification key here uh so and
then you can gen uh you can verify the
proof but uh calling this like a GPC
verify is not enough here right because
it uh it basically checks okay your
proof is correct but you need to do more
things so one thing I need to do is like
I get this signer public key here like
this is a government id center public
key I have to make sure this public key
is actually the government's public key
it's not just from anyone not from to
himself uh we also need to check
similarly the uh pay stops public key is
like the Z Public key uh here we need to
check okay the water mark is uh
calculated correctly and lastly we are
checking nullifier so basically I have a
database which saves all the nullifier
I've seen so far and here like where I
get this piece of proof I check have I
seen this nullifier before if I've seen
this that that means like okay uh this
is from someone who already got a
mortgage I can't give him mortgage again
right so okay so those are all the code
um those are all the code I have I hope
like after seeing this uh you are going
to take a look at our code base and uh
uh you know check it out uh Try It Out
Try to build something and uh maybe also
like John our uh telegram group here uh
cool thank you that's my
talk all right we have some questions
for you
Veronica uh does this system require the
data issuer to sell part it possible to
dictate from some EX listing side data
source like passport and verify the
signature as a part of a pod uh so so
you can you can it's possible to take
data from some existing oh I can't see
it anymore sorry yeah yeah it's okay uh
so so like so like you you have to one
thing is you can you can anyone can
issue a p right you can also take a
passport and then issue P about the
passport but you have to trust whoever
ISU the P so like if you trust in my
example you trust the government zav so
like that's the only thing you are going
to trust but you can you can say okay
I'm going to trust this other
organization like for uh like if if this
organization like issue a passport part
I'm going to trust that organization
that's a public uh key you are going to
check so it depends on like who you want
to trust I guess uh okay uh doesn't this
imply that Zoolander needs to accept the
claims of all this proof providers are
valid what tells them these providers
are legit U so it's a it's a same thing
it's like for this Zoolander uh it's
basically the Zoolander says okay I'm
going to trust the ID issued by this Zoo
G I'm going to trust like the pay St
issued by this Zoo deal uh so that's a
trust assumptions here you have to trust
someone right like uh the IDE is issued
by by the government basically basically
um does the burden of proof for
truthfulness fall on the verifier what
happens if the verifier part issuing a s
yeah that that's yeah if like if like
zukav just like issue something like
totally doesn't make any sense like a
fake ID then you know then then this
whole proof would have fall apart okay
so uh do I still have more time you have
time for one more okay uh will the
proofs work if the request data is only
a subsite of the data if all you wanted
was to prove that someone oh yeah uh
definitely so let's say like I want to I
only want to prove like this to is older
than 18 I can still use the same uh ID
pod I just showed you like for my proof
request all I need to say is like okay
this data birth is in the range so like
just check this this thing you still
need to check like owner like the uh
public key but like for this for this
piece of information you can only check
data of birth you don't need to check
like other things you can just ignore
the other things you don't want to check
uh yeah that's amazing you're right on
time excellent job let's give a Veronica
a warm Round of
Applause excellent demo finished on time
finished Q&amp;A on time I I think that
might be uh one in 10 thank you Veronica
um well we get the uh next machine set
up we're going to keep this QR code
reminder we only have one mircat
instance for this presentation so the
same one we just used for Veronica's Q&amp;A
we're also going to use for Rob's Q&amp;A
Rob is up next so PSA I'm going to go
and delete all of these questions so
that there's a fresh set of questions
that you can be asking Rob as he's
presenting uh but the way you get to ask
those questions and upvote is you scan
this QR code and you go to the bottom of
the event link that it takes you to
where it says Q&amp;A you sign in with your
zoo pass and you can ask questions and
you can upvote on questions so if uh you
get sparked during this conversation um
presentation I should say uh drop your
questions in there and we'll leave time
for Q&amp;A at the end and without further
Ado I'm going to bring up my friend Rob
Knight and he's going to talk about Z
API so let's give a round of applause
Rob thank you very much Remy um and
thank you to all of you for uh for
turning out um I'm going to talk about
the uh zapi so this is uh the system
that you use basically to integrate some
of the zass features into your own apps
um so just you a quick recap on on what
is zup pass um zup pass is is a private
data store which has a UI for
visualizing that data it has a suite of
cryptographic tools so you can sign
verify make proofs about that data um it
has UI to allow the user to do all of
those things uh in a in a clear and easy
to understand way um and The crucial
part that I'm going to be focusing on is
is that there are apis for requesting
updating and sharing that data which you
can use to build your own applications
so here we have a bunch of different zup
pass use cases and one in the top left I
think you will all have done uh which is
that you've checked into Devcon uh if
you didn't check into Devcon you
shouldn't be here um so that is
something that you do using zass
directly you know you get your zass uh
QR code and you show it and someone
scans it but all of those other use
cases that we see here those are
implemented in other apps that that use
zup pass so we have uh the uh voting for
the hackathon winners at eth Berlin that
was done using zoole which uses zup pass
to prove uh that the voters are
legitimate attendees of the event um but
it's not done inside zup pass it's done
in an external application frog crypto
if you heard forest's uh talk earlier
you'll understand how that uses zup pass
um there's the zurat which was used at
devc connect last year uh you basically
make a ZK proof that you're an attendee
of the event you send that to a telegram
bot and it posts an anonymous message
for you you in a telegram chat uh
distributed trials at zconnect last year
they built a system for uh participating
in clinical trial so they had wearable
devices on your wrist that you would we
for two weeks and then at the end of
that it would collect all of this data
and you'd submit that data with a zero
knowledge proof that you are a
participant in the trial meaning that
they know that that data is coming from
someone who did really register U but
they don't know which participant
submitted which data so you get you get
to preserve your uh your privacy there
Zoom was used the edge as mlda to enable
people to share their straa running
routes so you could see how fast people
were running but you didn't know who was
running um in uh gitcoin there was also
the Zulu uh Q2 Grant round where people
in order to vote for projects in the
quadratic funding round uh they could
vote for you know events and and Tech
projects to receive funding that
requires you to prove that you've been
to a previous Zoo event so again zero
knowledge proofs being used to preserve
uh privacy
and then uh the the final example bottom
right is is mircat again you will have
heard a a presentation about how that
works for them and and what their
experiences
were so how does Zupas actually
work it kind of works a little bit like
this this is a very simplified
architecture diagram um but we have zup
pass and inside zass there is a
cryptographic identity a semaphor keyer
um there's a collection of PODS pods
provable object data so this is the
things like your frog things that you
might have received for attending a talk
in miacat your tickets are also pods um
and all of that data that identity in
the pods that gets backed up and and and
synchron and synchronized across your
devices using this end to end encrypted
Backup Service um so that's how you can
go from your phone to your laptop and
you still see all of your data there
that data never leaves your device in
unencrypted form it's always encrypted
um it's never shared with anybody else
zubas also has this system called GPC
again we've we've just heard from
Veronica you know really good example of
how GPC is used um to make to make these
kind of customized ZK proofs and then we
have these apis that tie all of these
things together and allow external apps
to leverage this functionality for
themselves so in Zupas kind of API 1.0
basically how we were building things
earlier this year and and last year uh
it kind of worked a bit like this you'd
have an app so here we have again an app
that was built at devc connect last year
um and that wants know is this person a
Dev connect ticket holder was was this
person actually here cuz we're going to
give them some test net eth if they can
prove that they were an attd so what you
do is you click the button and then this
this green popup window opens up so it
opens up a popup window on zup pass.org
um that then synchronizes your data down
it then decrypts the data using your
password um and it allows you to make a
proof about that data if you click the
proof button then the spinner spins for
a few seconds while it makes the proof
proof and then it sends the proof back
to the to the original app and that
allows people to to kind of build these
kind of simple authentication workflows
which works kind of it works pretty well
for things like uh you know requesting a
ZK requesting a single ZK proof um but
it doesn't work so well for more complex
interactions so frog crypto uh 1.0 last
year again you know you might have seen
this at devc connect for crypto needs to
do something more complicated it needs
to be able to write data to your zup
pass and it needs to be able to write
multiple pieces of data to your zup pass
you know you're tapping that like search
the swamp button you get a frog you get
another frog you get another frog you
need to be able to insert those into zup
pass uh very very quickly and if you
have to open up a new pop-up window
every time you want to do that it's not
going to work that's a really bad user
experience so we solved that last year
by just building frog crypto directly
into zup pass and then frog crypto has
access to these private apis where it
can directly insert things uh into
storage but that's not really a scalable
solution we couldn't then come back this
year and say okay the devcom pwa is
going to have to be built into zup pass
mircat is going to have to be built into
zup pass all of these applications have
to be you know committed to our code
base so we wanted to come up with a
solution that would allow apps to
leverage some of this functionality uh
that's in zup pass in a way that allows
them to be independent apps that consume
zup pass using an API that feels like
that feels like under the hood it isn't
but it feels like like using an API
that's talking to a remote server or is
talking to a browser
feature and this is something that we
call the zapi and this is the this is a
new thing that is being used basically
for the first time at
devcom and this allows you to build your
own app you basically get to integrate
all of the features of zup pass uh so
you get access to that pod Store the
store of all of the data you can read
and write uh to that you can run queries
over it um you get to use the uh at
least request the use of the the user's
identity so you can request that the
user sign something or that they make
appr proof that uh that uses their
identity and you get these UI Primitives
that for instance you know visualize a
proof so the users being asked to prove
something what are they being asked to
prove that that that UI is is pre-built
for you and you can see some examples of
things that people have built um one of
my favorites is the shulan do
engineering which like takes your frogs
and uh develops psychedelic substances
from them uh it's it's pretty cool
um so this is a slightly different uh
architecture to the to the kind of the
V1 um in this the the app is like a
regular web app and it can do regular
web app stuff it can talk to remote
servers it can do you know all of those
those usual things it has JavaScript um
but it also has this embedded zpass and
the embedded zup pass can do all of the
things that zpass can do um so that can
you know query things from your pod
store it can access your identity it can
it can invoke these cryptographic
gadgets to to generate proofs and so
forth so now your app has basically all
of the capabilities that zup pass does
and it can it can use and reuse data
that other apps have created so I can
create an app that with the user's
permission will read from their frogs
for instance so I can create an app that
consumes that frog data um and makes you
know new novel proofs about it I can
combine frogs and tickets and make novel
proofs about those and I can insert
things into that same collection so
these games or these inter interactions
and experiences
become open worlds that you can extend
uh and combine and create uh new
variations
on so how does this actually work um you
connect to zup pass using a hidden
iframe so zup pass basically loads up in
this iframe um behind the scenes and
communication between your app and zpass
is done by sending messages so the
browser has a built-in post message Api
and this allows for Real Time message
exchange between between the two
applications so this is actually much
faster uh in many cases than doing a a
network request the uh the request is
kind of basically occurring on your
device so you you ask Zupas to do
something and on and all of the
computation necessary to serve that
request is happening on the device it's
happening on the phone on the laptop
it's not going over the network and
asking a server to do something because
in the case of Zupas the server doesn't
know anything all of the data is is on
is on the client so you can do things
like you know read in query uh you can
insert you can delete you can request
signatures you can generate
proofs now this sounds a little bit
dangerous so there is a permission
system uh that allows the user to decide
you know which things are you is your
app going to be allowed to do uh pods
are divided into collections so frogs
are in a different collection to Devcon
tickets for instance and an app might
have permission to access frogs but not
Devcon tickets or vice versa you can
also create new collections for your own
app um or you can request access to a
collection that was created by another
app uh you can also request the
permission to sign
pods so this is basically the whole of
the API uh if you if uh if you see this
this is basically everything you can do
um so we have you know pod operations
query insert delete subscribe and
unsubscribe basically gives you live
updates to the Pod store as it changes
and sign uh kind of asks the user to sit
to sign something sign prefixed is a
kind of special type of signature um for
kind of unsafe uh signing uh you can get
the user's identity you can get that
public key um and you can request a GPC
proof so querying kind of looks a little
bit like this uh let's say we have the
frogs collection um we can request a
frog with a jump score that is between
five and 100 minimum five maximum 100 um
or we can request a frog with a certain
mood uh that must be a m M of a a
collection it must and that means it
must have a value of either angry or
lazy if the frog is neither angry nor
lazy then it's the wrong mood and you
you won't get that one
back you so you can use conditions like
is member of is not member of in range
to construct your your queries you could
use this uh on on tickets for instance
to uh select tickets from a particular
event uh if you have frogs you can use
the Rangers in particular to get frogs
with particular attributes that have
particular scores
you can also create your own pods so
we've seen examples of of PODS earlier
you can create your own pods with
arbitary data any type of data that you
want that is supported um by the Pod
data types so here I'm just creating a
pod with three entries greeting magic
number and email address and then I'm
asking the user would they like to sign
this pod uh if they do it will be signed
with their key um and I'm going to
insert that into a collection called new
pods
I can also then make a proof
request which looks something like this
so again taking that same type of pod
that I just created um I'm going to give
a set of valid greetings so we had a
greetings entry uh we're going to then
specify you know these are some valid
greetings um there was a magic number so
I'm going to specify a range of
acceptable numbers um and I'm also going
to say there must be an email address it
must be a string but otherwise I'm not
going to constrain what I what I need
that to be um and I want to know what
the email address is so so what I'm
asking for here is a is a proof that dis
uh discloses an email address of a pod
that has uh entries that are in the in
the ranges or satisfying the criteria
that I've that I've specified when I
invoke uh that function so when I call
the prove function um that will then
cause a popup uh model to appear in the
app where the user will be asked to
agree to make that
proof so this looks uh something a bit
like this um you can see that the proof
request uh is asking for the email
address and in this case it it shows you
know test example.com is your email
address so that's what's going to get
revealed in that
proof um importantly this is um
transmitted via messages between frames
as I said before so this data doesn't
leave the device it never goes over the
network um it is it is uh you know very
much a local
operation so this enables uh a bunch of
different options for you you can build
apps that you use zass as a primary data
store for example so frog crypto uses
zup pass as a data store frog crypto
doesn't store your frogs on a server it
stores your frogs in zup pass and that
is the only place that those frogs uh
can be
found uh you can use it to then query
data so again you know take frog crypto
as an example when it lists out the
frogs it's running a query against that
data store uh we've seen a whole bunch
of apps that are using zero knowledge
proofs around whether it's around
tickets whether it's around frogs
questions and answers um that can also
be uh requested and uh visualized using
the the built-in UI and then you can
also request user signatures a pod so in
frog social and in some of the the more
kind of uh peer-to-peer communication
scenarios I can sign my own pods and
send those to somebody else they can
then receive those and verify that they
have my signature uh verify that my
public key was
used one way to think about this is that
um what we're trying to build here is
something that sort of previews
something that we expect the whole world
will have you know some years down the
line so if you think about what browsers
could do 30 years ago they could
basically render text and then someone
figured out hey maybe we could do images
and then tables and then like maybe we
could do like stylesheets I think
probably was one of the things that came
next and then after that you know
JavaScript um background requests and it
kind of rolls for now we have like
cryptography in the browser we have
real-time communication in the browser
we have local storage we have access to
the file system uh we have a whole bunch
of things that that weren't there in the
original browser and that process is
going to continue um our thesis is that
programmable cryptography is going to go
everywhere and so it seems quite
reasonable to me that in the future
programmable cryptography itself will be
built into the browser you'll be able to
make ZK
proofs using you know built-in browser
apis but right now that doesn't exist so
you can use zapi to get that window
window onto the future um that we think
uh everybody is going to have pretty
soon so how do you get started with
something like this it's it's actually
pretty simple uh I'm going to walk
through a small example and this
involves installing basically two mpm
packages so we install the app connector
package and we're going to install the
ticket spec
package this is how you connect so you
import the connect function you define
your zap um you give it a name Devcon
ticket verifier it's not a very
imaginative name but uh it'll do you
specify the permissions that you want so
in this case we're going to request uh
proofs that's the permission that we
want and we want to be able to do that
for the Devcon sea uh
collection so then we create this object
zob uh by calling the connect function
we pass in the details of our app and we
give it an HTML uh element on our page
that it can insert the if frame into so
this is I don't know what 10 12 lines of
code um we then Define a proof that we
want to make so uh we want to make a
proof about Devcon tickets so we're
going to specify that there must be a
public key so this here is the uh the
Devcon uh public key that was used to
sign all Devcon tickets um we have the
unique event ID that specifies Devcon um
and we want to reveal the email and name
attendee so when we run this uh proof
request we're going to get back a proof
with a name and an email but also a
guarantee that that name and email is
attached to a legitimate Devcon
ticket so then we call this function we
call prove we pass in the uh proof
request that we just saw um and we we
want to restrict that to the Devcon sea
uh collection so we're saying like only
only use inputs from that collection um
and if that's successful we can then
print out the email uh and the value and
what we've got back is this proof um so
we're not just getting some data back
without being sure where it came from
we're getting a full ZK proof we can
send that ZK proof to a server that can
send it to another server whole long
chains of distribution can occur and
every step along that chain we'll still
be able to verify that that's a legit
proof we'll still be able to verify that
there really was a Devcon ticket behind
all of
this so I'm going to recap uh kind of
briefly over some of the things that
you've heard already and and over the
the zapi in general
we have pods and pods let you define
your own data structures you can Define
any data structure you like um you can
give things their own names you can
create numbers you can create dates you
can create strings you can create uh
EDSA public Keys you can um you can
specify constraints on those things you
can specify ranges on those numbers you
can specify um you know lists of valid
uh public keys and so forth um and that
allows you to say this is what makes
something a frog this is what makes
something a ticket this is what makes
something um you know a record of
attendance and you can share both the
structure with other people so you other
people can then take that structure and
say okay I'm going to make an app that
reads that structure that knows about
what a frog is that knows how to work
with tickets um or knows how to make
frogs and knows how to make tickets
um GPC is let you create your own logic
so this lets you create your own own um
you know ways of interpreting those
things ways of deriving meaning from one
or more pods collections of PODS where
for me what I care about is you know I
just really want to know like did this
person attend this event somebody else
might care about uh you know what
specific type of ticket do they have you
know maybe we want to create something
that's just for speakers maybe we want
to create something that's just for a
particular subcategory so you can create
your own custom logic using GPC proofs
and and build your own uh ZK proof just
using this very simple configuration
language and then with zapi you can
build apps that leverage these things
you don't need to worry about building
your own pod store you don't need to
worry about managing cryptographic
artifacts which is actually a slightly
difficult thing um there's a lot of pain
and and and difficulty that we've that
we've kind of figured out how to work
around uh we're doing those things uh
that is now packaged up for you uh by
zapi and users will come bringing their
existing pre-existing in personal data
store that they already have you know
with their frogs with their tickets and
they can use that to interact with your
app and
then where might this go
next so this interface is defined there
is a a library that defines this is a a
GitHub repo um called parket client
which defines uh this API there's a kind
of RPC Library um what's interesting
there is that you could take that and
build your own client you could take it
take that and build your own thing that
does the same job as zup pass so there
was a question earlier uh about
decentralizing uh zup pass and you know
is it possible to you know replace some
of these components with others well if
you have something that implements this
API it will do the same job as Zupas so
if you have a better idea for how to
store pods you have a better idea for
how to synchronize them between devices
um you can build your own client and it
will be able to serve that same role
instead of signing in with zup pass you
can sign in with something you built
yourself um that will be able to respond
to queries and and produce uh GPC
proofs so that's uh basically everything
I have to say about zapi um I'm hoping
you have some questions um I'm hoping I
didn't go too fast through all of that I
know that was a lot of stuff to cover um
but yeah I'd be really Keen to uh to
hear what it is you you have to ask and
also I want to highlight um um we have a
telegram chat so if you're interested in
building on zup pass if you're
interested in learning more about pod
GPC zapi any of these things um please
join our telegram group uh we'd love to
hear from you um and yeah uh that's
that's me thank you amazing thank you
rob I've literally been flying around
the world Rob for the last maybe year
and a half while he's and the zup pass
team have been implementing at pop-up
City and Zu Berlin and Y zo prog or
sorry eth Berlin and eth Prague and now
Devcon and devc connect before that so
it's been a wild ride the amount of work
you guys have done both behind the
screen but literally on the ground has
been really cool um you don't have to
hope for questions oh wow they're here
so I'll I'll let you uh answer them
based on the up voting and well uh
before Rob does that I'll just remind
you if you go to that link and you
scroll to the bottom and you click on
Q&amp;A you will be able to ask and vote on
the questions you want to see Rob aners
so uh would you want me to narrate them
for you rob or would you rather just
read them what's easy for you I I I'll
I'll pick these up so okay so that top
question is a really good question uh
where does the zup pass data store live
um so it kind of lives in two places um
the primary place it lives is on your
device so um when you create an account
in zup pass um you have no data it's a
new account um the first thing we do is
we create a cryptographic key pair for
um and you choose a you select a pass
you add a password to your account we
then take that cryptographic keeper use
your password to encrypt it and then we
synchronize that to a uh basically a
cloud backup so that's just a like that
is just a backup of that data it's not
the primary store of that data it's a
backup for that data but that allows you
to sign in on another device download
that backup and enter your password and
you'll be able to decrypt it so the data
in terms of being usable is only ever
really usable on your own devices um
that backup server is operated by us so
I suppose in that sense it is a single
poter failure and that's something that
you know for decentralization reasons
it' be good to have uh more uh options
for where that data might live uh we do
also have an export function so you can
just export your data directly and
import it directly um so I think
thinking of the data as living somewhere
I think it lives on your device and
there's a sort of Cold Storage backup
that is that is totally
encrypted uh I think the second question
is basically answered by the first
question so the server can't see your
data the server only sees an encrypted
blob uh your password is necessary to
decrypt that blob the server can't see
uh can't see what's going
on did you answer this that is that what
you're referring to can you send pods
what if I want to move remove and send a
pod so I mean you can send pods um I
mean you can send pods by just copying
and pasting so I think we we have like a
a I think we have now a copy pod button
that just gets a sort of Json export of
the Pod you can copy that you can put it
in an email you can send it over signal
or telegram um there is no kind of like
buil-in like send somebody a pod in zup
pass functionality right now that's
something that we we're kind of very
interested in adding in the future but
pods are provable object data but
they're also portable object data in the
sense that um because they have
signatures you don't need to care about
like how you got the Pod you need to
care about whether or not you can verify
it um so does it have the right public
key um so in that sense the the
transport is it's kind of Transport
agnostic so I think this this this
question is sort of relating more to Z
kyc but I think it's a relevant question
for just any situation uh like this
there is definitely a challenge of like
getting people to agree on structure so
like what is a ticket or um what makes
something a valid ticket for a given
purpose that's a question that comes up
a lot um I have this Devcon ticket uh I
make a proof about it how do you know
that that's actually a valid Devcon
ticket well you do need to know some
information you do need to know some
things like you need to know what's the
Devcon public key if you don't know what
the Devcon public key is then I could be
presenting you with a proof and you you
just can't can't interpret it so there
is some information that is needed um
that would obviously be published by for
instance you know the Devcon organizers
might publish that key um we uh in the
past have published lists of of
interesting keys for for kind of certain
authorities like Zulu um Dev connect and
so forth uh you also need to know things
like unique event IDs again we've we've
also published lists of those in the
past uh this is something that in the
future I would imagine you know
Registries kind of springing up to to
serve this use case
um embedding all the data's client said
yes I mean like yes in the sense that if
you if you end up with like gigabytes of
data and you have to be synchronizing
that back and forth all the time I think
that would end up um being pretty slow
one of the reasons for making uh for
sort of breaking pods up into separate
collections you know I mentioned earlier
it's like a frogs collection Devcon
collection and so forth is that we want
to be able to synchronize those
independently so if I say you know I
have an app and it needs to be able to
read frogs instead of needing to
synchronize like everything in my pod
store we can synchronize just the frogs
just the thing that we need uh for the
purpose of making the current proof or
for interacting with uh with that
data uh mobile app mobile app the next
question so right now there is no uh
direct kind of mobile app equivalent of
the web app functionality um obviously
you could make a you know uh like a you
know embed some some some web code
inside a Native app but there is there's
not like an iOS native iOS or Android
library for this right
now I'd be interested in the so this the
question is um about you know hacking
hacking on Android in relation to
iframes uh I'd be really interested to
talk to whoever asked that question uh
about the specific uh things they've
encountered with with that because we
we're very interested in uh you know
trying to test out some of these uh
these security risks if we can if we can
create a reproducible uh hack uh we'd be
very interested in trying to figure out
how to close that uh close that loophole
just to interject Rob we're probably
going to have a few extra minutes before
closing ceremonies so is it fair to say
whoever asked that question or if your
question doesn't get answered you can
meet Rob in the back corner am I allowed
to pitch that oh yes yeah don't shell
out your time come and come and come and
come and bother me after the Rob will
hang out in the back corner if you don't
get your question asked or if you ask
that question
okay so how to build and verify custom
computation
so right now so the point of something
like GPC is it's general purpose
circuits which means you get these kind
of like Lego bricks basically to build
up um your
proofs that gives you a reasonable
amount of flexibility it doesn't give
you the same amount of flexibility you
would have if you writing your own code
in circum for example so uh right now
there are a few different ways this uh
that kind of flexibility could be
achieved
um but it's not easy to support using
certainly using the zapi it's that's not
uh an action that you'd be able to take
right now so you can't put totally
custom circuits in there you you are
limited to what you can configure uh
using the the options that GPC gives you
having said that uh GPC is very uh
configurable and flexible and you can
compose some pretty interesting uh
proofs using that so I'd recommend
reading the documentation on on GPC and
just getting really familiar with uh
with what that can do we'll make this
the last question this uh this top
question here Rob and then wrap it seems
users can log into zass by email
verification even when they lost their
passwords this is correct uh you can do
that uh you can log in so if you lose
your password um you can reset your
account in zup pass and that will reset
your account you will lose access to
whatever encrypted data you had
previously so your endtoend encrypted
backup will no longer be accessible to
you uh because the password is the
decryption key for that uh entend
encrypted
blob because a lot of what we do in zup
pass involves tickets um there's a kind
of complicated uh authentication system
here where if you prove ownership of an
email address to zup pass by verifying
your email we give you a cryptographic
credential that says this person has
proven ownership of this email address
and then you go to like in the case of
Devcon you go to Devon's ticket server
uh this is kind of you know behind the
scenes in zpass but it will go to the
Devcon server and say like hey I have
ownership of this email address do you
have any tickets for me and then they
will issue you a ticket to the identity
that you're presenting uh if you reset
your account you'll get a new identity
so you'll get a new public key but you
will be able to prove ownership of that
email address again you become
effectively the new owner your new
account becomes the new owner of that
email address so when you go to the
Devon server and say hey like can I have
my tickets please uh you will get those
tickets back but they will now be
assigned to a different public key so
you can't take over an existing account
by resetting the email
address even if it belong to you amazing
your Q&amp;A stamina is impressive Rob I
know you could keep going but we're
going to wrap and and we're going to
give Rob a round of
applause thank you
um just scrolling through this is only
showing a snapshot just scrolling
through mircat there's a bunch of
awesome technical questions that remain
as we mentioned
uh after Rob jumps off the stage he'll
be hanging out in the back corner if you
didn't get your question answered if you
want to find out more please come talk
to him and uh that's it for this session
there is another QR code that's going to
come up over my shoulder in a second um
this was from Richard's presentation
some of you might not have got a chance
to scan it um this uh this QR code will
will take you to the void um and if you
were listening intentionally to Rob's
presentation um there's been some
third-party apps built on zup pass where
perhaps you can go craft some odd
substances or psychedelic substances you
might want to find out what that app is
you might want to craft some substances
you might want to bring them along with
you to the void and you you just don't
know what you might find there um thank
you everybody for coming out the closing
session starts at 4:00 there's going to
be an incredible panel including our
co-founders Justin and gub
with a from the EF and a friend of Xerox
Park Nicholas Paul uh who is the uh
former executive director of the long
now Foundation founded by Stuart brand
and Brian Eno I think it's going to be
uh a really interesting Phil
philosophical and uh engaging talk to
finish out Devcon so I recommend that
you go to mainstage for 4 o' check out
the void first thank you all for coming
out and spending your afternoon with us
we really appreciate it have a love L
lovely rest of your day thank you
