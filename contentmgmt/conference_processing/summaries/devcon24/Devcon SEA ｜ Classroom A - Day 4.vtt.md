e
[Music]
e e
for
I
yes
yeah I think so
hello everyone my name is p and I will
be your MC for today so I'm H I'm happy
to yeah I'm happy to uh announce our
first Speaker of day who will present a
new method to construct a folding
schemes for Stark proofs uh please uh
give a welcome Applause to our speaker
Albert garetta
okay we're going to start a little later
o
back
uh hello everyone uh thank you for
joining us today at Defcon so my name is
pavil and I will be MC uh let me
introduce our next speaker uh who will
introduce a new method on to construct a
folding scheme for Stark proofs please
uh welcome Albert
Getta thank you thanks everybody for
being here on this Friday
morning so yeah I will talk about how to
folding in the context of starks so
let's start with the
basics wait one second
all right so what is folding so in
folding we have a relation R relation of
Interest which consists of pairs x w x
is an instance or a statement of a
problem and W is a witness or a solution
to the problem and a folding scheme for
this relation R is an interactive
protocol between aover and a verifier
where the prover and the verifier have
two instances X1 x two and the prover
also has two witnesses W1 W2 and they
are valid Witnesses for the
instances and then the pr and the
verifier interact and at the end of this
interaction they out they output a new
instance witness per XC W3 with this key
property so this output instance witness
pair is valid so it is in the relation
if it is the if it is in the relation
then the original two instance witness
pairs are in the relation as well well
except with negligible probability so
this is the key prop property of um of a
folding scheme so basically what's going
on here is that we have two tasks we
have to prove one instance witness per
and another one and we have applied an
interactive argument that reduce these
two tasks to a single
task uh so if this folding step is very
cheap then you are basically gaining um
you are gaining work right you have to
do less work because now you only have
to prove one instance witness pair okay
so commitments play a crucial role in
this type of schemes at least in the
modern ones and in reality in practice
all instances include a commitment to
the witnesses so in reality in practice
we we have the instance witness Pur look
like this so the instance is a true
instance XI Prime and then it also
includes a commitment to the witness
okay so a folding and then a folding
scheme looks like this we have two
instance witness pair where the instance
contains a commitment to the witness you
fold you get a new instance witness pair
okay and the commitment most of the time
is homomorphic and this is a crucial uh
point and homomorphic means that the
commitment to the sum of two vectors is
the sum of the commitments to the
vectors okay so if you've never seen
folding this is everything you need to
know to follow this talk let's look at
how folding looks from 5 ,000 kilm away
so as I said in folding you have two
instance witness pair of this form
there's aover and a verifier the prover
knows the instance and the witnesses the
verifier knows the
instances and now the exchange messages
doesn't really matter what's going on
here for the purposes of this talk and
at the end the verifier sends a
uniformly sampled
Challenge and then the pro and verifier
output new instance witness pair the
witness is only not to the pro and
crucially the new instance and the new
witness is a linear combination of the
initial two using the last challenge
sent by the verifier so we have these
formulas in here X3 equals X1 plus Alpha
X2 and so on and the verifier computes
the so the verifier needs to get the the
whole instance right at the end of
folding so it's easy for the verifier to
get X3 because knows X1 and X2 but how
does the verifier get the commitment to
W3 well here you can use the homomorphic
property of the commitment scheme the
verifier knows the commitments to W1 and
W2 and because of the linear prop
theomorphic property of the commitment
scheme it can obtain a commitment to W3
without any interaction with the
approver just by performing
this this uh linear combination of the
commitments so this is how folding looks
from 5,000 km away many many folding
schemes look like
this okay let's discuss commitments in
folding schemes in more depth so usually
the commitment scheme is a pson
commitment or a kcg commitment so it's a
elliptic curve based commitment or some
variation of Pon on kcg for example in
Nova hypernova protostar Proto Galaxy
Etc this is the commitment of choice and
this commitment scheme has some inconen
conveniences one is
that here you are forced to to live in
large Fields so you need fields of at
least 250 bits because otherwise you
don't have if you want to go lower than
curves with pairings if if you need them
and committing this these type of
commitments can be extremely expensive
if the vector has large
entries and it is expensive to recurse
over so us in folding you you apply fold
you do folding and then you do IVC and
then you have to prove that the folding
is done correctly and so on so you have
to prove statements about elliptic curve
operations which are quite a
headache and yeah because of this
setting you are kind of bound to using a
kcg based nark when to prove a folded
instance right because you you are you
are using large Fields you you have uh
elliptic curve based commitments and so
on but maybe you want to use a different
proof system right so that would be
that's an
inconvenience okay so yeah let's say we
want to use Starks to prove our folded
instan our folded instance witness
Pur so by Stark I loely mean a snark
that uses codes and Merkel Tre based
commitments for example the Stark
protocol from starware plun it through
two on three buum R zero and so on these
Protocols are configured on small fields
and they are getting smaller and and
smaller for example goldilux for plunky
Circle
Stark this is a the the attractiveness
of small Fields is that well the
attractive attractiveness of this field
is that you you get to you get smaller
arithmetization due to special
properties of the primes of these fields
uh you also get cheaper computations
because field elements
never get very large if you invert a a
most 32
bits um but there are some problems in
the context of folding the first problem
is that Merkel trees are not homomorphic
so if you want to do folding you cannot
you you you don't have the homomorphic
commitment right
away and since we are working on small
fields we cannot rely on elliptic curves
here and also depending on how you are
going to do folding even if Merc trees
were
homomorphic it might not be worth it in
the context of starks and I will explain
why now so let's look at the at let's
look at a cost breakdown of creating
star
proofs and yeah let's look first at how
a fry Bas tar works so yeah all the
proving proving systems I mentioned
before work as follows so first the pro
computes the trace or the circuit value
values the the values in the wires of
the circuit then it encodes the trace
using a Nar correcting code polom and
for this it interpolates The Columns of
the trace and then it evaluates the tra
the the polinomial on a larger domain
using inverse ffts and ffts this is
called Computing the low degree
extension of the trace then the prover
commits to this low degree extension
using a Merle tree and finally there's
some quotient the takes some quotients
and applies fry and so
on okay what's the cost of all the
what's the cost breakdown of all these
steps I'm citing El vason from a talk in
at SBC this summer so the tra generation
in the case of St costs 46% of the proof
of the total proof cost Computing the
low degree extension cost 28% Merkel
trees cost about 133% and the rest also
cost
of folding if we are thinking of using
folding it means that somehow we want to
use raron so we are probably not using
Merkel trees full of kets or uh Shad 256
or classic hashes we are probably using
Merkel trees that include some some type
of uh Algebra I hash in which case the
third step would be much more
expensive uh yeah so
here here's an important observation
even if the mercel trees were
homomorphic you don't want to to to do
the folding with the commitments to the
low degree extension of the trace
because you would at each folding step
you would perform this step this step
and this step and you would save this
this part in here and you would still
need to do folding so in the absolute
best case scenario you would save 13% of
the toal proof cost at each folding step
which is not a lot so what we are trying
to do here is to just commit to this
Trace in here we don't want to commit to
the low degree extension with merket r
we are just going to commit to the trace
in the most cheap uh way
possible uh yeah
so this is a key difference with
approaches like accumulation without
homomorphism or the arc protocol from
these researchers
uh from papers of this uh from this
year okay so let's recap what we want to
do we want we want to commit to the
trace instead of the low degree
extension we want the scheme to be
compatible with Starks and this means
that we have to work over a small field
we want the folded instance to be
provable in a reasonable manner with a
stark and yeah so in here since we want
an instance to to be provable with a St
here we think of instances as being
erors or plish instances and we look at
this as
ccss a CCs is basically an R1 CS
constraint um but generalized with more
terms okay so here is the general
framework of what we could try to do if
we want to fold Starks and afterward I
will talk about uh actual
instantiations so let's say we have two
instance witness pairs two two
SS the framework is as follows the pr
would commit to the trace not to the low
degree extension of the trace so the
trace the witness with a homomorphic
commitment
scheme okay so now we have these two
instance witness pair and then somehow
we would fold in a way that the folded
instance is in still in an error or
somewhat similar to an
eror and now say that we want to prove a
folded instance so we have done folding
and now we want to prove the instance
the folded instance winess pair so what
would the pro and the verifier do the pr
computes the low degree extension so so
we want to use Starks right to prove the
folded instance and for star in if you
are using star you have to encode the
witness because you are going to use
error correcting codes so the pr
computes the low degre extension of the
folded witness W3 and commits to it with
a Merkle tree like if as if it was just
using a St the star protocol then the
the prover proves that the commitment
from the folding scheme to the folded
witness is consistent with the mercal
tree commitment of the low degree
extension of the folded uh
witness and then once this is proved the
Prov can just finish the proof that the
FED instance witness pair is in the
relation with the his favorite
Stark Okay so we have to keep in mind
that we'll have to do this this steping
here when we want to prove a folded um
instance witness pair so this will
inform how we choose the commitment
scheme to not um make this this parting
here too
expensive okay so let's instantiate the
framework now we need a commitment
scheme that is
homomorphic that is compatible with a
stark field so it work it it somehow
works over small fields and the
candidate here is the itai commitment
scheme following in getting inspiration
from the ltis fault paper from B Chen
and Dan
Bonet and we need a folding scheme that
folds pairs of erir or blish instances
into roughly errors and blish instances
and the candidate approach here is if we
look at as I said if we look at eror
plish instances as ccss so let's say R1
CSS or relaxed R1 CSS then we can the
first thing that comes to mind is Nova
because Nova Falls relaxed R1 CS is into
relaxed R1 CSS so this is the our
candidate
Nova however there's no Nova type
folding scheme that works over laes
so there's when it when it comes to
folding over laes the only work
available right now is latis fold as far
as far as I know and ltis fold is a
hyper hyper nova analog that works over
latis but there 's no Nova analog over
laes so one of our main results is
designing such a such such a folding
scheme okay
so a bit on latices and and latis fold
so latis fold and many latis based
schemes work over so-called cyclotomic
Rings which are cyclotomic rings are
basically they look like field
extensions right you take a a ring of
polinomial over a a field a finite field
and quoti it by an ideal generated by a
polinomial however here the quotient
polinomial may not be
irreducible and in this Cas this means
that if the polinomial is not
irreducible it means that this ring
splits as a direct product or several
field extensions if f is irreducible
then here there's just one factor and
you have a g extension uh the standard
field extension but if f is not
irreducible then you have this direct
product but in any case these rings are
quite are quite nice because they are
just direct products of field extensions
so you could in principle and we show
that you can configure R in a nice way
and at the same time choosing F to be a
stark Prime field so we we can choose F
to be goldilux baby bear the big St
Stark Prime and probably M31 though this
is working progress
uh yeah and the commitment scheme works
on vectors of length M for elements of R
and the parameters of this commitment
scheme are as follows it's just a matrix
sampled uniformly at random from the
ring with with ring elements it commits
two vectors of length M from of ring
elements and the commitment is simply
the The Matrix Matrix Vector
multiplication a times the vector
so let's discuss the efficiency of this
commitment scheme first so say and this
is an example configuration we can deal
with we we can choose the base field to
be the goldilux field which has 64 bits
and we can configure R so that R splits
as eight um factors and each factor is a
degree 3 extension of the gold Delux
field here there's an important remark
on um how to work with catomic rings and
this is that because of this isomorphism
in here this is the number theoretic
transform because of this isomorphism
you can potentially
store eight Trace cells in a single ring
element so if you have if you want to
store eight eight Trace Elements which
are in the which and each element is in
the field you can put each element in
one of these
components and
then these eight
elements become just one ring element so
a vector of size to to the N with ring
elements can store 2 to the N plus Trace
cells and this is this is quite relevant
performance and this is a some some
benchmarks of our implementation of the
it commitment scheme using this
configuration so say we want to to
commit to a vector of size to6 fi uh
ring elements and this means 2 to the 19
fi elements so this costs 65
milliseconds this should be the
commitment time I don't know why it says
field and this is for
comparison what you would get if you
commit um if you do merry commitments to
the vectors so if you commit to to to to
the 16 field elements the with a Blake
function so classic classic has this is
but as I said this is just to the 16
field elements this is to the 19 field
elements also if you are using mer Tre
you probably have encoded the witness
which means that here you have an extra
one in the exponent which is not not uh
not giving you anything when you want to
encode the
witness maybe it's the the overhead is
even larger if the rate of the code is
less than 1
get similar performance and if we put
algebraic hases in the Merc trees which
you we Pro you we probably have to if we
are in the context of folding because it
means we are interested in using some
kind of recursion then the difference of
course is
dramatic how much time do I
have five minutes
okay so yeah we are almost there's one
or two slides
left so recall um and I take commitment
is just Matrix Vector multiplication of
ring elements there's a big issue with
this commitment scheme I I said what is
good about it and now what what's bad
about it this commitment scheme is only
binding when the vector you are
committing to has small norm and the the
norm of a vector Vector is the largest
coefficient of an entry of the vector
when you look at the elements of the
ring as
polinomial and yeah remember that the
the folded witness in our folding
schemes are a linear combination of the
two initial
Witnesses so there's two issues here
because of this caveat one is that even
if W1 and W2 have small
Norm because W3 is a random linear
combination of w 1 and W2 it is possible
that W3 has large
Norm in general W3 might have
arbitrarily large Norm in which case the
commitment to W3 with the it commitment
would not be
binding and there's another issue that
is even if one does not happen even if
W3 has low Norm for some reason when you
prove knowledge soundness of the folding
scheme you need to make sure that the
extractor gets
uh Witnesses of small
Norm because
we because because of this caveat we
only commit to Witnesses of small Norm
so we end up requiring that the pro
commits to Witnesses of small Norm so
when you prove knowledge soundness you
need the ex to show that the extractor
only gets Witnesses of small norm and
this is quite difficult to
enforce okay so since uh um there's 5
minutes less than I had planned for I
will skip how ltis fold and how we
address these two issues and just jump
to the Q&amp;A part thank
you yeah thank you very much so we have
one question so why am third one is uh
WIP and because of the two adicity or
yeah the thing is that there's a lot of
uh factors coming into play when
configuring these Rings we have to
configure them in a way
that when they split as field extensions
they have at least 128 bits to ensure
soundness during S
Check and at the same time we have to
ensure that there's a subset of small
Norm elements that is large enough for
the soundness in another part of the
protocol and this places a lot of
constraints on how you can choose the
cyclotomic um
polinomial yes but the the the
composition of P minus one is completely
different uh the the way you can choose
the the way you can configure the ring
is strict is is highly um constrained on
the factorization of P minus one on how
it
factors um do we have any other
questions um okay if there's no
questions then we're going to take a
five minute break so thank you Albert
again for a nice uh research I really
enjoy the talk
[Laughter]
spe
watch
very
is
so
oh
uh and we're going to continue uh our
session with two lightning talks so let
me introduce our next speaker who will
talk about how their knowledge and
blockchains will help help Humanity
survive please welcome Lisa akal
sword hello
everyone uh this is a lightning talk
meaning we don't really have any time
for jokes sorry for that we have to
start very being very serious from the
very beginning so the question I'm going
to talk about
today the problem is that we are very
small like as a blockchain industry I
mean on this picture you can see how the
rest of the world uh is trying to see
what is
blockchain if you want some more
specific numbers if we compare our
industry to other Tech verticals like
space Tech space Tech or biotech we are
something like 10 to 40 times smaller
Frankly Speaking we are like a small
dot but I think we need to be
large if we want to our industry to
prosper and take a meaningful place in
the
world and I think we need to learn from
mushrooms how to be
large what's the difference between
blockchain and
mushrooms blockchain is a three mushroom
Network and mushrooms are three trillion
mushroom
Network Three trillion mushroom network
is a really cool thing whenever someone
sees it they want to jump in because if
there are three trillion PE three
trillion mushrooms who joined it seems
to to be worth
it but three mushroom Network seems to
be a bit a doubtful activity so we need
to become
mushrooms that is to say it is on us as
a blockchain industry to find use cases
where blockchain and ZK are a perfect
fit for huge world's
problem and furthermore it's on us to
communicate it to right people in right
Industries and in right countries around
the world because I can guarantee you
they will not figure it out on their own
first because they don't think about
blockchain then because they don't know
about Z
knowledge so today I'm going to just an
as an example give you three real world
use cases that are crucial for Humanity
survival and I'm going to use the
formula of ZK for verifiable
computations and blockchain for
coordination think for think for example
about the space think for example about
satellite coordination there are many
countries operating in the space and
many of them are not friends but still
they have to coordinate their activity
in the space how can China prove the US
that their satellite won't clash into
some us space facility what they do
today they ask you promise yes I promise
but what if they use Z knowledge proofs
for proof of root or proof of heting the
specific coordinate instead of just
promising but how should they coordinate
these tons of zero knowledge proofs by
hundreds of parties for thousands of
satellites 24 to7 without disclosing any
sensitive information they can use
privacy preserving programmable
blockchain or think about
agriculture in many countries
agriculture is run by self-piloting
machines like computers with software
running on it
if tractors cultivators and bailers are
out of operation for the whole country
its economy stops and the country is in
deep economic crisis how can a small
human Force thousands of machines with
different programs running on top to
report them what's on their mind using
zero knowledge proofs but what about a
network of thousands of machines and
thousands humans transmitting zero
knowledge proofs in arbitrary directions
programmable blockchain I think about
nuclear missiles I know this is not the
favorite topic for most people but just
for 30 seconds if a country a has a
concern that a country B launched a
nuclear missile towards it his president
has several minutes less than five to
call their president and ask did you do
it but and if the president didn't
answer they must um launch their all
their missiles as a
prevention but can we prove that
something has not happened can one prove
that they have not launched the nuclear
missile or if they did can they prove
that this particular country is not a
destination I don't have 100% answer for
this one especially if we can prove that
something has not happened but I think
it might be doable and I think it's
worth thinking about
it so can zero knowledge help Humanity
survive yes
sure can blockchain help Humanity
survive this is a bit trickier but yes
but but it must be privacy preserving
programmable
blockchain no privacy no blockchain
adoption that's simple that's it thank
you uh thank you uh for interesting talk
um I also strong believer that
blockchains and their Pro knowledge will
help Humanity to reorganize in the
future and thank you again so if we have
any questions we have some
time uh okay uh then let's uh try to uh
kind of uh stay together because the
next sliding talk will be started in two
minutes thank
you may answer the fourth one yeah if
you want
yeah about proving to the partner that
someone is not cheating um if you a
computer I think and she is a computer I
think it is very
easy um if one of you is not a
computer it is tricky because when it
comes to uh bridging data from the
physical world uh into the digital world
from my perspective this is this is very
complex still very tricky thing and it
wasn't uh resolved so far there was um a
paper in 2013 um written by some
Princeton Princeton guys about like
utilizing zero knowledge proofs for
monitoring the state of nuclear
facility um and they assume that there
is some nice solution to um like an a
nice solution for a Oracle from physical
world to the digital world but up to now
there is no such solution as far as I
know and uh that why all the cases I
described they are digital and Native
from the very beginning so something
exists like a piece of coat from the
very beginning like self-piloting
machine or like
satellite thank you
[Applause]
yeah for
uh okay we're going to continue with our
lightning talks and next speaker will
talk about base rollups and precons so
please welcome Jason
ranik all right thanks for coming
everyone I know it's kind of early so
this is a lightning talk on based
Roll-Ups and pre-ms
and as you know these lightning talks
are extremely quick so this isn't going
to answer all of the questions it's
really going to try and lay the
foundation and motivation for why um
different teams are working on this so I
I would want to start with like what is
the big motivation here um and the big
goal of these based rollups really is to
help solve this fragmentation issue
we're starting to see in the L2 space
and to restore some value capture back
to the base layer so how did we get here
well ethereum is always in this tricky
position um the goal posts always move
gas was too expensive we created this
rollup Centric road map we suceed eded
in offloading all of this execution
things got cheaper TPS increased but eth
is dead so we really want to try and
address some of these problems headon
and the big focus of this talk is around
fragmentation So currently these l2s
aren't interoperable with each other
they fragment liquidity they fragment
users they also fragment developers you
have to pick a winning ecosystem to
deploy on or deploy across many which
starts to your resources and what we're
really seeing is this kind of
convergence on what I'm calling intraop
you have interoperability within your
ecosystem but not across these
ecosystems so how do we fix this
fragmentation problem well one easy
solution is that we just agree on one
entity to sequence all of these rollups
and that sounds pretty centralizing so
can we do this in a way that preserves a
lot of the values that we care about
so enter base rollups the idea here um
this is a quote from Justin's paper um
the tldr here is it's a based rollup
when it's sequenced by ethereum
validators so in this picture on the
left hand side here we have centralized
sequencing the idea is you have these
unordered transactions a centralized
sequencer job is to order them for the
rollup um these little squiggly things
are the Roll-Ups at the bottom here okay
as we move to the right we're increasing
in decentralization and we're unlocking
interoperability so with shared
sequencing you have multiple parties
that are all agreeing According to some
leader election mechanism on who has the
ability to sequence all of the
rollups and as we move all the way to
the right we enter this based sequencing
mode the idea is that the transactions
for these l2s will be sequenced directly
by ethereum
validators and how does this help how
does this unlock interoperability the
idea is that we have these right locks
over L2 State when an ethereum validator
is going to propose a block they have a
right lock over the entire L1 block and
all of the L2 blocks that are going to
be included and when we have a bunch of
rollups that are all agreeing to be
sequenced by this validator
it unlocks this ability for you to start
passing messages across these rollups we
don't need these Bridges we're able to
do these more
seamlessly so this has
limitations um one of the big issues
with based rollups is that they have um
really 12C block times a lot of users
want to come to l2s because they they
care about that Snappy ux those instant
transactions we can always reduce the L1
block times but that's a very long long
arduous process that has a lot of
unknowns and centralization vectors so
precums this is another one of these um
new terms that stands for
pre-confirmation a pre-con is a
commitment made by these validators um
to users about doing something related
to block proposals so this could mean
I'm giving a guarantee to a user that
I'll include their transaction when it's
my turn to propose the block or I can
even give a stronger guarantee like this
will be the state after executing your
transaction and if I break my promise as
the precc confer then I can get slashed
um on um various
means so to kind of wrap this up like
how does this all come together so the
user over here would be able to send
their rollup transactions to be
sequenced by an etherium validator they
in response give back this
pre-confirmation signature
um which is like this receipt for the
users guaranteeing that their
transaction will be included or it will
be executed um inside of the rollup and
if the validator does break this promise
they can be slashed by submitting
evidence to the slashing contract and
what does this enable well it solves a
lot of these ux problems and when we
start to enter this like execution
promps we we really make it to a place
where we can can actually outperform um
these alt l1s by giving these very
instant transactions back to users and
this all comes without modifications to
the base layer so hopefully this maybe
pequ people's interest on this topic um
but of course in a in a five minute
lightning talk that's uh there's still
many many things to be explored so thank
you all for joining
okay yeah we have a few questions
um right yes so the the first question
here how does this notion scale um if
they need to validate all of the L2
transactions so this is a great question
so I think there's kind of Two Two
Worlds here like one is sequencing
itself doesn't imply execution so it
doesn't have to take on all of the load
but realistically there's different
implementations of these um pre-com
protocols being built some of them
offload this duty to um these kind of
gateways is what they're called similar
to the PBS pipeline we see
today um second question
pre-confirmation Services seem to be the
biggest layer of complexity for me um
these pre-com networks will likely
require consensus is this the biggest
drawback so definitely over the past
year like it's been it started from this
like very dark Forest unknown and over
time we've started to untangle it and
some of the bigger questions are now
just around pricing but really you don't
need an actual consensus protocol to
build this um you're able to just
broadcast like these messages directly
to the users and if the user like
doesn't get their pre-confirmation
they're able to go and
slash okay maybe one last question why
is Spire better than puffer why is Spire
better than puffer well um we're all
here building based rollups so
um
yeah I I understand so everyone has
their own vision for the best approach
thank you very much so thank you please
give a round of applause to our speaker
w
okay we're going to continue with the
next lightning talk so our next speaker
will talk about practical approach to
unifying ethereum using Next Generation
based rollups please welcome M
team hello
Devon all right so we're going to talk
about next Generation base rollups today
there are some base rups that are Next
Generation there are some base rups that
are last generation you guys just
learned about some um I'm going to tell
you more about how you can become a Next
Generation Bas rollup kind of what the
definition is
and then a little bit more about how I
see the future of Bas rollups
evolving cool so this first section
we're just going to go through some of
the traditional base rollup research
talk about the the Bas rollups that have
been you know explored in the past some
of the designs that have been proposed
um and then we're going to understand
some of their flaws some of their
weaknesses so one of the very first
designs that is used by Tao today on
Main Nets is total Anarchy base
sequencing this is like kind of letter
of the law exactly what Justin Drake
proposed in last year right and it's
it's very simple very basic right it's
called total Anarchy because it uses a
uh election system that is
permissionless um and allows anyone
that's the Anarchy bet to propose block
so one key Point here is that the
sequencer Is Not Elected beforehand you
don't know who the sequencer will be
beforehand you might know the ethereum
proposer because you uh can look at the
ethereum look ahead be know 32 in
advance uh but the sequencer of the base
rollup might not be the proposer teo's
case it is TECO labs for the majority of
blocks um one other thing to note is
that layer two block proposing is
completely permissionless right there's
no permissions involved uh the way that
this ends up playing out in practice is
that we have this diagram up here uh we
have a bunch of sequencers proposers in
Tao's system that give their blocks to
the Builder to the me boost Builder that
would be Titan winter mute Etc um
and they would take these blocks order
them in the layer one block so you know
each block proposal is a layer one
transaction and then send this completed
block to the proposer through a relay
and through the me boost auction right
and then eventually the proposer would
propose this to ethereum once they
selected the block with the highest bid
so it's up to the proposer and and the
Builder to choose which block created by
these uh layer 2 sequencers or proposers
actually gets onto the chain
now one design that aims to solve a few
of the problems of the previous design
is vanilla based sequencing so lime
chain um George spasov put out this
excellent bit of research that explained
how we can actually solve a few of the
foundational problems with total Anarchy
basing right the Teo model so the the
first kind of thing that we we try with
vanilla Bas sequencing is a simple
sequencer election right that gives us
the ability to choose a sequencer based
on some rule we have a primary Rule and
then we have a fallback as well so the
fallback in vanilla based sequencing
case is just total Anarchy so there's
still some total Anarchy here U and the
primary sequencing is based on some
election mechanism that is not clearly
defined and kind of left implementation
in the initial research so the other
thing that vanilla Bas sequencing
includes is kind of very basic primitive
support for delegation which is allowing
the ethereum proposer to give the rights
to their base rollout block to an
external Builder with directly going
through Mev boost it's like external to
the Mev boost auction vanilla Bas
seening also included basic support for
pre-confirmation which gives the you
know we heard about it last talk but
gives the uh proposer the ability to
promise things about the block that they
will eventually propose um it does
require some sort of Delegation or some
um increased Hardware constraints on the
proposer and so the design for prec
confirmations has kind of wide reaching
implications for centralization vectors
for for stake and also for uh
pre-confirmation in real time now the
other thing that vanilla base sequencing
introduced that really caught my eye was
Revenue generation from a percent of
congestion fees and you you'll hear
Justin Dr talk about this all the time
you'll hear me talk about this base rups
can capture revenue from congestion
trivially right these base fees if
you're doing EIP 1559 evm right they are
represented on chain and are kind of
understandable from within the the evm
within the state transition function so
you can view things about the the fees
you can take these and um you can do
things with them right you can direct
them to a treasury you give some of them
to the proposer or you could return them
back to
users so kind of the the problems with
these that are actually really big
problems like Tao on mayet live is
extremely inefficient um all Forks of
Tao without major changes will continue
to be extremely inefficient um one other
problem with kind of total Anarchy and
vanilla base sequencing is that there's
kind of no built-in compos ability any
composability is on a layer above the
the sequencing and that's really
unfortunate because whenever you have to
build kind of another layer you
introduce complexity and centralization
vectors of some sort in the case of Base
rollups that's quite possibly around
pre-confirmation which means we could
have centralized ethereum stake which we
all want to avoid other thing is MV
Revenue so lots of people still have
this misconception that base rollups
leak meev revenue and that's true for
traditional base Roll-Ups because they
do not use um an auction of any sort to
kind of get an oracle into me so if we
look into layer one me research we'll
see things like execution tickets and
execution auctions um that are all
designed to get some Oracle price
essentially of the me in a block now the
other thing to note about bs like I
mentioned before is inefficiency so Tao
has a about a $10,000 a day cost to to
do their sequencing um before blobs they
had about $100,000 a day this is is a
lot of money clearly and the kind of
thing that you need a massive amount of
users and network effects to actually be
sustainable right and that's something
we we obviously want to
avoid but there is a solution for some
of these uh these Tao Forks we've been
looking at doing slower block time so
Tao now has a block time of 33 seconds
instead of 12 seconds um which is of
course ethereum block time that is you
know that has allowed their cost to come
down by about a third which is good for
them um but it's also really bad for
users you get a worse user experience so
the way we can patch over this is with
pre confirmations just throw some
pre-con on top uh the downside of that
is that without doing your
pre-confirmation designs in a clever way
you're going to end up with limited
benefits so your users are going to get
know very limited availability of
pre-confirmation um and of course a
limited composability so unless you're
using a a shared pre-confirmation
protocol you're not going to have
composability so we start breaking a lot
of things when we add PR confirmations
uh the other thing that that you know
specifically Taco's case you lose
composability with layer one because
pre- confirmations happen you know over
a course of a an entire Epoch perhaps
and during that time layer one state
could change a ton and so the kind of
current layer one proposer is very
different than who's actually sequencing
the roll up that's not sh sequencing
that's not
based but we can do better traditional
designs are not good enough we have over
the past two years we have new research
we have new teams we have a lot more
data about base rollups CU we have one
live and we have a lot better technology
so one of the big things that we'll be
talking about in their next section is
ZK um using snarks to save cost and
improve
efficiency so let's kind of stay take a
step back let's think from first
principles with all the data with all
the research um and with all the the the
teams that we have now kind of what are
the things that we really want to get
out of Bas sequencing the first thing is
in in my mind the most important which
is synchronous Atomic kubos ability and
you know this is a a buzz word for sure
what I think that means is atomic
cross-chain contract calls that are
sufficient enough for Flash loans and
the reason for that is because Flash
loans are a foundational tool for doing
Atomic Arbitrage between domains so once
you have cross train contract calls you
can do Arbitrage um you can do flash
loans for Arbitrage and this gives you
the ability to essentially Arbitrage
prices on different domains giving users
kind of the best prices uh across chains
you can also use that for doing like a
swap that uses multiple chains liquidity
if I'm on arbitrum I could directly use
ethereum layer one liquidity without
waiting for like a a service provider um
or you know some collateral now that's
pretty straightforward the other thing
to to look at is a a seamless user
experience and developer experience so
anyone who's ever tried making an
asynchronous application will know that
it's 10 times easier I'm not joking to
build a synchronous application if it's
asynchronous you have to deal with a
case where something goes wrong and uh
you have a dsync now the other thing is
of course Network effects right once we
have the the efficient synchronous
composability between chains we have the
ability to build Network effects on one
chain and use that on another and
because ethereum already has massive
Network effects that means space rups
can use that those Network effects those
liquidity users protocols Etc to um
directly improve the the user and
developer experience on their
rollup now the other thing that we want
of course all the time is faster things
and cheaper things so on the faster side
we're looking at good pre-confirmation
that don't break things um and that are
fulfilled 100% of the time frequent
block proposing the more we touch
ethereum the more we can compose with
ethereum custom front ends so this is
kind of changing the the unisoft style
swap interface to something that
actually you know represents what a
pre-confirmation might look like so
that's a green check mark um some
confetti of some sort it doesn't seem
like a lot technically but it's actually
really important to improving the the
user experience materially one thing is
like getting rid of improval and then
swaps we can get rid of that completely
with pre- confirmations uh another thing
is of course cheaper things which is
better execution so just writing your
smart contracts better and U not making
kind of the mistakes that we've made in
the past when we were rushing to get
code out aggregate everything there's a
slide on that so I'll wait um and of
course efficiency of of all shapes and
sizes now we want to do all of these
things and and both of these things I
guess without sacrificing
decentralization and censorship
resistance livess and sustainability so
this is where you know you can get
faster and cheaper if you go to all
layer one you can do it on a centralized
sequence or Layer Two what you can't do
is faster and cheaper with
decentralization sensorship resistance
livess and sustainability without some
form of Bas sequencing is my my
opinion so we know what we want it's not
that complicated we want fast things we
want cheap things and we want everything
to feel like one chain for developers
and for
users getting there next Generation base
sequencing this is the subject of these
three companies up here this is kind of
the the industry that we're in this rise
spy labs and Tao gwith um and we're
taking a very practical approach to
unifying ethereum so we're trying to
avoid the kind of discussions where we
get into the Ivory Tower semantics um
and actually build like tangible useful
products that are good for users and
Developers
so let's get into the specifics this is
a intermediate talk so we're going to
get a little bit technical here we're
going to share literally everything so
when it comes to um things we share like
if the answer is no then you're probably
lying we have deposits proposing blobs
proving Network effects assets contract
calls offchain INF security economies of
scale etc etc etc so share deposits
that's AG these are teams that are
working to reduce cost of you know
posting ZK proofs to main net by
aggregating ZK proofs also also has the
excellent benefit that you can do
interop between layer twos without ever
touching layer one so you save a lot of
costs with that as well shared proposing
saves a lot of costs and enables Atomic
composability again between base rollups
if we can share blobs so if you're a
base rollup and you're frequently
checkpointing or posting to ethereum
you're going to be purchasing a blob for
da in most cases and blobs are pretty
big and most base rollups do not use
so there's a lot of empty space um and
there's a whole bunch of teams spire's
kind of leading some of the research on
this side to figure out how we can have
multiple rollups use the same blob so we
build some cryptoeconomic system to make
everything a little more efficient and a
lot cheaper for base rollups we also
look at things like shared proving to to
save cost shared network effects so
using the layer one for Network effects
instead of the layer twos um and we kind
of logically centralize our network of X
for a better user and developer
experience and also of course shared
assets so we want the
canonical U ler of Last Resort for every
asset to be on layer one um we have one
fungibility between these follow-ups
that's something that we get with
shareed deposits but it's a big priority
in of itself contract calls of course so
we want to do contract calls uh we want
to batch those you know of infro that's
pretty obvious security that makes sense
and then of course economies of scale in
everything we do so one of these kind of
tools is pre-confirmation we have a we
over over here in number one we have a
centralized squencer that gives out pre-
confirmations this is what every layer 2
does today except for Tao um and number
two we have some proposed models for
based pre- confirmations where the layer
one proposer I mean like you know the
guy running on a rber pi with a dialup
is the sequencer and they're the one
directly giving out pre-confirmation and
directly interacting with the uh the
people who are requesting pre-
confirmations so obviously a pretty huge
of bandwidth and compute resources cost
um and number three is the design being
explored today which is some form of
Delegation that's that purple line uh to
a Gateway who actually gives out pre-
confirmations to users and then they you
know create a some Builder constraints
some set of rules that Builders must
build blocks that comply to right so the
the gayway is acting somewhat like a
relay in this case but with a little bit
more constraint around the builders so
we still have an auction taking place um
very similar to me boost and of course
the Builder gives the block to our
ethereum proposer who goes and gives
that out to layer
one now the other thing that we want to
do is MV retention um censorship
resistance uh you know being included
here and of course doing this all with
pre-com which turns out to be a really
difficult problem uh but we have some
excellent research from the ethereum
layer one about execution tickets so
we've kind of extended this to Layer Two
on base rollups we have these things um
that look very similar to execution
tickets we distribute these in an
auction and then you must burn a ticket
to propose a layer two block uh although
we do some of the the burning and um
kind of registration early in the epoch
and offchain optimistically so that
there not an expensive thing to do
onchain and of course with this we can
throw in some no delay forced inclusion
so every roll up today has a drift where
you can deposit make a deposit
transaction on layer one and then you
might wait a few layer one blocks before
that's included in Layer Two in a base
rollups case you you can pretty
straightforwardly build no delay Force
inclusion right into a uh a bass roll up
which gives you um you know cens
resistance equivalent to that of
ethereum now one other important thing
about next Generation based flops is
checkpointing so whenever we T CA is
proposing by the way but whenever we
want to kind of put our sequence onto
layer one we need to make a checkpoint
here and this is little red flag on my
diagrams but uh what we're actually
doing is making um kind of a a point of
atomicity right a layer one evm
transaction is atomic you can't revert
part of it um and because of this you
can do cross chain contract calls um
based on that atomicity you can also
checkpoint together that's this uh
bottom left diagram where we share lots
of checkpoints in one which saves a ton
of costs uh the other thing we can do of
course is other things while we
checkpoint so we can use layer one
liquidity during our checkpoint make
this available on layer twos we can also
um you know save the states of things on
layer one we could change the state of a
layer one contract to simulate um layer
one execution but actually doing the
execution on Layer
Two cool so one important kind of piece
of technology and probably the most
important for the base rollup teams uh
to compete on and be the first to is
validity proving and fast validity
proving and share deposits so there's a
whole bunch of ZK teams working on this
um cinct and Riso are two examples and
the goal is to take fastf D proofs for a
whole bunch of layer twos combine these
aggregate these into one fast CK proof
and then put this onto ethereum in a
share deposits Bridge contract that has
funds for lots and lots of rollups now
this has security kind of concerns you
have to trust your ZK so we probably
want multi-pro and it's also today
really slow so you know the the biggest
competitive advantage of Bas SCS in the
future will be how fast is you're
proving cool so this is kind of the the
magic of Base sequencing that we've been
working on at Spire to some extent of
course and that is using a Sensi
resistance committee to sacrifice
liveness for sensior resistance you can
read more about this in our light paper
um and then forward-based sequencing
which is using the uh a sequence posted
in um in a layer one slot to affect a
future layer one sequence this enables
you to do based sequencing and
traditional shared sequencing at the
same time which is obviously super
powerful so if anyone from espressos in
the room take a look at
this cool so after we've done all this
what do we get Harmony and more
specifically deconstructing economies of
scale to enable parallel Innovation
while maintaining Network effects I've
said this in all of my talks so far this
week and it's so important right we
don't want economies of scale to
introduce centralization risks and we
want to promote parallel Innovation as
much as possible the other thing one of
our important goals for user and
developer side is a monolithic
experience right not nothing monolithic
in practice um but we want to have the
ability for users and developers to feel
like they're on one chain um just to to
get that clearly better user experience
and of course doing all this while
establishing infinite expressivity
giving Builders the direct ability to
customize whatever they want about the
rollup including execution environments
gas fees
Etc infinite Gardens break
walls next Generation based robs
actually solve problems stay
based oh here's a quote from heraclius
Drake uh stay based for one man's
liquidity is another man's liquidity
thank
you okay thank you a lot uh so we have a
few questions um just
uh
so if you play cool so first question
what can Tao do to become a Next
Generation based rup uh will first of
all upgrade their Bridge contract so it
can share proposals and deposits and ZK
proofs with other rollups and then add
actually good pre-confirmation
um yeah they have a lot to
do
okay yeah second question as someone new
to the space I find it hard to factor
out the marketing how does your approach
compared to Espresso sounds similar at
least that's a good question so espresso
is building a shared sequencer um and
they're building a form of what they
call based espresso which is not
actually base sequencing um they just
call it that it's a marketing thing and
the goal of espresso is to unify layer
twos the goal of Next Generation based
rups is to unify ethereum and layer twos
so we're involving ethereum in the
equation um but to get there you can do
shared sequencing you can even involve
the layer one sequencer um but that
doesn't mean anything unless you do this
checkpointing unless you do this Atomic
synchronous composability so base
espresso will not allow you to do cross
Shain contract
calls okay thank you uh do you have any
other questions uh we still have time
okay sorry I could haven't figured out
to log into that thing um so you
mentioned that there is a no delay Force
inclusion uh I'm kind of curious how
that works with a chain reorg uh where
the chain State kind of change
after like if you force like a deposit
for example and a chain State changes
with a reor right so this is is
something that every base rollup must do
which is reorg with ethereum so in the
case of an ethereum reorg then your base
rollup must always reorg um doesn't have
to change anything but it will rework
and this is something that is very hard
to fix in protocol so we need an
ethereum upgrade to reduce the risk of
reor or um decrease time to finality but
there are a lot of outer protocol things
we can do so if you get lots of
proposers opted in in the look ahead you
can just ask them not to reorg have them
put up some collateral and you'll be
able to reduce the risk of re Orcs um
you can also like paste over it on the
user experience side you can have a a
solver or somebody take a duration risk
um the user never has to experience a
reor and then SP is also working on like
an RPC that's custom kind of retrofit to
deal with commonly no common reor one
thing I would add is that Bas trops will
reorg as much as ethereum does now so I
don't know how much you use ethereum but
if you do a lot of defi or trading you
still probably never experienced a
reorder that has affected your um your
life so I wouldn't expect that it's a
massive user experience problem yeah we
would have to rework okay thanks and
then sorry just another question um I
thought um cross chain contract calls
was very interesting uh but I still
can't imagine how it works like you know
across let's say like a bunch of
different chains that all operates at a
different speed right so could you have
maybe provide like some uh practical
examples with like a bit more details
yeah come talk to me afterwards because
that's a you know a longer discussion um
so all base rups have a batching time of
theoretically less right and this means
that the kind of composability you do
between them can only happen at batching
time because that's the only time when
you have atomicity and and synchronicity
right and so we can compose every 12
seconds we can do a cross train contract
call every 12 seconds um and then within
that kind of boundary we uh we can't do
any composability um that is enforced by
cryptography right we could still do
like Intense or you other kinds of um
interop
okay thank you please uh give a round of
applause to our
speaker okay I think next talk will
start in uh 7 minutes
he
you
uh okay and we're going to resume our
talks on layer twos so our next speaker
will talk about Beyond recours of
approving for starnet please welcome gon
cfer
everyone let's see if you can hear
me okay so uh
the goal of this presentation is to talk
about everything Beyond recursive
proving but I'm not going to assume you
know everything about proving or
recursive proving uh so I'll just begin
with the basics and uh you'll uh follow
me I
assume so uh let's talk about the basics
of a validity rollup what uh composes a
validity rollup you have
transactions uh sequencers select these
transactions Define their order and I'll
use the term sequencer also for
execution ution of these transactions so
if you're confused by base rollups where
they separate the sequencing from
execution here I'm going to combine them
um and they build the blocks uh once we
have a block uh the way a validity
rollup works is that it proves the
validity of the execution of these
blocks uh using a prover instance and
send this sends this proof per block to
verify our contract on ethereum on the
layer underlying layer one and once that
proof has has been
accepted uh a state contract tracking
the state of the rollup is updated with
a new State uh together with the state
update we also uh add what we call State
diff and uh we may include also
messaging between the layer two and
validity rollup and the underlying
Network State diff just to make sure you
understand what I mean when I talk about
State diff is basically the update to
the state of the rollup uh resulting
from the executed block uh validity
rollups do not need to transmit the
actual transactions that they sequenced
to the underlying layer there's no
context no uh uh such thing as fraud
proofs or anything of that kind we
positively prove everything happening on
a validity rollup and as a result we can
send much less much less data to the
underlying Network in order to be able
to reconstruct the full state of the too
so a state diff is basically just the
locations in the state that have changed
and their value so in this simple
example D has been changed into X so the
state diff of the transition from State
one to state two is just a single
element change location 3 to Value
x what does it mean to prove a block so
basically what we're doing is we're
using the context of uh of uh proof in
order to uh
um to prove the statement that we have
seen a valid execution from a given
State a resulting in a new state B and
the resulting stative between State a
and state B is such and such so the
statement is the transactions were
correctly sequenced and the input State
results in the output
State what are we doing on layer one for
the validity rollup in this simple uh
basic validity rollup we need to verify
a proof of a block which can be costly
in some cases we need to publish the
state diff typically using blobs on
ethereum and we need to update the state
which is typically some contract call of
the state contract tracking the state of
the role upon L one um as long as the
blocks are significantly
large this is all this is fine but if we
want just to have a few transactions per
block on Layer Two or quick finality
this can become quite costly so the
basic validity rollup is good if you
have either a very large blocks or you
have a lot of traffic and then you can
still have a short finality on Layer
Two or you have long finality then it
becomes less costly but it's less
effective because you have long
finality enter recursive
proving recursive proving intends to
reduce the overhead of of verifying the
proofs per
block so let's begin with what recursive
proving really is so on the left hand
side you can see the generic uh concept
of proving so basically you have some
statement and you want to prove that
given a a current uh given an input or a
witness if you like uh there is a
correct execution of the statement
resulting in a given output and what the
prover does it basically proves that the
statement was run correctly on the input
and that the actual output is the given
output uh the proof does not necessarily
need to divulge the input as we call it
zero knowledge proofs but if you like to
include some of the input in the output
you can just copy that within the
statement so how do we use this context
uh this concept to create recursive
proving basically we replace the
statement with a new statement that just
says I've verified two proofs and found
to be
correct uh so proof one with output one
and proof two with output two you use a
statement that performs verification
which is just an algorithm right so
there's no reason that you can't uh
build such a statement and the result is
the two outputs the original outputs you
just copy them from the input to the
output so when we prove this statement
exactly like on the left hand side the
result is a proof and the outputs that
we want to generate which in this case
are output one and output two what does
this mean we've basically combined two
proofs with two outputs into one proof
with two
outputs now we can use this construct in
order to combine various statements
possibly totally different statements
from different sources if you like we
can prove uh statements from multiple
rollups even uh into a single proof and
a series of outputs uh coming from the
original inputs or from the original
statements I I should say so in this
diagram you can see four different
statements there's no relationship
between them each of them has their own
input creates the own their own output
and uh using recursive proving twice in
this example we result with one proof
and four
outputs so what does a validity rollup
with recursive proving look like very
very similar to what we had before so
you have the transactions the
sequencers uh the Define the
sequence uh execute the transactions and
create blocks just like before in this
case let's say they accumulate four
blocks then we can use recursive proving
in order to prove these four blocks with
one proof as opposed to four proofs in
the previous example in the basic
validity roll up and this proof is sent
to the same verifier contract on layer
one then for every block a state update
takes place on layer one on the small
smart contract that tracks the state of
the rollup and the state diffs per block
are sent to layer one so using recursive
proving we've basically reduced the cost
of verifying proofs on layer one but we
still keep uh the concept of publishing
State diffs per block and State updates
per transition so from State I to State
I + one that takes place per
block it's less costly than before
because sometimes a significant cost is
on the verification of the proof uh
State updates are less costly but the
smaller the blocks get the more
significant the cost of these State
updates become so this allows us to
improve uh to reduce uh block times on
Layer Two on the rollup or if you like
uh reduces the need to perform large B
batching on the blocks on Layer Two but
still I would like to optimize this
further which brings me to Beyond
recursive proving which is the topic of
my
discussion uh we want to build something
which we call applicative
recursion so let's define applicative
recursion roughly in the following way
here you see again the same recursive
proving tree that we had
before uh we have four input statements
uh uh we combine them together into a
single proof with four
outputs with applicative recursion uh
the difference from regular uh recursive
proving is that here we're going to
assume that all the statements come from
a single application so they have some
kind of common
semantics uh for instance these are four
proofs of blocks coming from the same
rollup then what we do is we use the
same context the concept of proving but
now for basically squashing the outputs
together into a single
output uh so in this case we'll have a
new statement which basically says this
is in the red rectangle on the bottom
basically we verify the last proof so we
make sure that the outputs are valid by
using verification of this proof and we
perform a statement that is a valid
combination of the four outputs into a
single output so the result is uh single
proof
with a single output this time so let's
see what this output could contain okay
so for example if we're interested in
aggregating state diff uh here is an
example of three state transitions so
we're moving from State one to state two
to state three and eventually to State
four in each transition we generate
State diff so in the first transition
you can see that position number three
has changed from D into X in the second
transition we're touching positions five
and six and in the last transition the
fourth transition from the third
transition from state three to State
four uh we're changing position three
again and position six again so the
result is the
state called S4 on the bottom of the
slide but if you look at the resulting
stative between S1 and S4 there are only
three changes so there's no reason to
transmit three state diffs with six
changes as in this example so one of the
things that we can do in the squashing
proof this final step of applicative
recursion is joining the outputs
together into a single more concise
output now in reality for validity
rollups it happens quite a lot that the
same positions in the state are changed
multiple times even within a block and
certainly between blocks especially if
there are many many blocks or large
blocks so this kind of uh aggregation is
very very is very important to improve
efficiency of State div transmitted to
blockchain but also other things can be
done and I'll go into examples in a
moment so now a validity rollup looks
like this you have the transactions as
you know they're sequenced and
executed put into blocks for every set
of blocks we create a recursive proof
then we do the applicative recursion
because all these proofs relate to the
same application the same rollup in this
case so we can do that and this single
proof with the aggregated output a
single output is sent to the verifier on
layer one so we pay for verification
just like we paid for ver verification
in the previous example using simple
recursive proving but now instead of
doing a state update per block we can do
a state update per recursive cycle if
you like for multiple blocks together
simultaneously so what does uh this look
like so we have the recursive uh appc
applicative recursion
recursion per recursion we verify appr
proof and per recursion we publish the
aggregate State diff in one or more
blobs and update the state on this on
the contract that tracks the state of
the rollup with a single state update
that updates the state to the final
State we've reached after multiple
blocks and of course we can include
messaging as
before so the more blocks we have Pro
recursion the lower layer one cost will
be and this basically scals infinitely
uh depending on the latency you require
uh to layer one
um and uh this is actually what we are
doing currently on our rollup called
Stark
net what else can be done in this uh
applicative squashing or if you like in
applicative
recursion so the basic uh aggregation of
State diffs as I mentioned is just uh a
straightforward aggregation but you can
also do more sophisticated things for
instance if you want to represent your
state in a more efficient way so utilize
your blobs more efficiently you can
Implement for instance a compression
algorithm on this data uh just deflating
the data into much smaller form which
allows you to uh include more blocks on
your applicative recursion of course
eventually when all the blobs fill up uh
you may reach a state where blob prices
could go up or you have more blobs than
could fit in a single transaction and
things like that that is something you
want to avoid so that's a point where
you want to cut off the applicative
recursion so it's not really infinite as
I mentioned before in addition as I
mentioned you can uh remove the need to
do update States per block uh and if you
like you can generalize this into a con
into a concept of segmenting a very
large computation into multiple
segments so if you prove that you've uh
executed a program from some State a to
some State B and then you've executed
the same program or continuation of the
program from State B to State C Etc an
applicative recursion or the squashing
mechanism can ensure that you've
actually proven the complete execution
of this program from State a all the way
through State C or Zed or whatever uh so
this is the generalization of the
concept of applicative recursion and you
may have more ideas here and uh the more
creative you get the more interesting it
gets so basically if you think about it
uh the whole concept of recursive
proving applicative proving is are a few
examples of offchain proving so these
are proofs that are never submitted to a
verifier on layer one so basically
they're only submitted to a new
statement that verifies them off chain
completely and there are other examples
that are useful in in this context and
I'll talk about a few of these so one
example could be for instance for a
privacy preserving uh uh exchange for
example so let's say you have an
exchange on your rollup on the
blockchain itself typically exchanges
that are onchain they EXP the positions
of their
users uh some users are very sensitive
to this information because it divulges
trading strategies so what you can do is
basically have a user who knows uh their
own
position uh execute uh some order on
their
position while keeping the position
encrypted on the on the rollup itself or
on the blockchain if you like so in this
example if I go over the diagram you
keep you store encrypted positions on
the blockchain every user uh is involved
in the encryption of this of this
position by using their own key they can
read the encrypted position decrypt it
and then execute an order on their own
position and encrypt in resulting or the
resulting position now if they prove to
a contract that
executes um trades that this would be
the result of their encrypted position
if for instance they get a little more e
selling a little bit of
Bitcoin uh then a trading contract or if
you like an exchange can accept that
proof without actually knowing the
contents of the current position so of
course this does divulge some
information because uh we are telling
the exchange uh by how much how much we
are selling and how much we are buying
but anyone looking at the position of a
given uh user wouldn't be able to
decipher the current strategy of this
Trader so this is one example where
proofs can be combined into a blockchain
in order to create a more private
environment uh by using client side
proving in this example there are
variants of this concept uh where we
trust the exchange with our private
information and then all the positions
can be encrypted and decrypted by the
exchange as part of uh proving
uh but this is one interesting example
uh that can also be implemented on uh
rollups or blockchains as long as you
have a contract that can verify uh
proofs uh on Stark net we have contracts
verifying Stark proofs uh we also have a
contract verifying gross ex proofs so
you have a choice of building your
application on top of that on Stark net
today another example is for scaling
blockchains and this will be my final
slide so for everyone uh uh pressed for
time um this is a little bit more
sophisticated but the idea is let's say
I have a bottleneck in terms of the
capacity of sequencing and execution of
what's going on in the in the rollup I
want to Outsource sequencing to someone
else if you like or I want to Shard my
layer my uh validity roll up so that
different sequen C can run together in
parallel sequencing different parts of
the rollup or different contracts if you
like some segregation of
transactions so in this context you
basically what you see here is something
that looks like two rollups but they're
actually the same rollup so you have
multiple sequencers each executing part
of the sequencing for the rollup and
proving this sequencing is correct using
the validity concept where the output of
this proof is the state diff or the
changes to the state in the areas that
they're responsible for an underlying
sequencer that which is the validity
rollup sequencer can verify these proofs
completely remaining on the rollup
doesn't have these proofs don't need to
be sent to ethereum and by verifying
these proofs uh this centralized or this
rollup
sequencer can accept the state diffs
coming from these various shards or what
we call ZK threads and when we combine
the state of all the threads we result
in a single state of a single rollup
that can be as in the previous story
transmitted to ethereum with various
kinds of
proving uh resulting in a unified uh
rollup that has all the state computed
by multiple sequencers so here we
utilize uh validity
proofs uh in order to scale a
rollup that's it I think I have 3
seconds left
thank you we have now a few questions
could you
question so I think the first question
is how is aggregating State differ from
multiple blocks and is it better than
increasing the block time
itself um aggregating state is better
than multiple
blocks
uh no uh multiple blocks is better than
having a single aggregate block I'll put
it that way why because what users
really want is finality on Layer Two on
the validity rollup itself so response
times go down the smaller the block is
uh of course if we would wait for an
hour to aggregate lots of transactions
in a block then we would had hu we would
have huge blocks and the basic validity
rollup would work but finality on Layer
Two would be very
slow I also to answer of about about
proving
cost um it's a good question because uh
in the past people thought uh that
proving I remember back in 2017 or
that proving a statement was something
like four orders of magnitude uh less uh
performant and actually executing that
statement at starkware I think our
initial Prov reached about two orders of
magnitude H which is called the
stoneover and today we're talking about
Stover where execution of the statement
is almost the same as proving the
statement so the cost of proving has
gone down very very significantly well
it's not the same of course you still
have an overhead but to prove statements
today costs very very
little uh so all this recursive proving
for instance is done within seconds
every recursive step so you get a very
quick finality even of the recursive
proof and of course that doesn't cost
much okay um we have still time so um
what's the current transaction finality
on starnet if you uh can yes currently
on Stark net you get finality on Layer
Two within 2 seconds two seconds and
this two seconds will be preserved in a
decentralized environment where actually
block times will go down to 2 seconds
and we will continue to prove every
block so that's where we can go with
this
technology and maybe could this be used
for Crossroad lab Communications through
a
shared absolutely uh in fact in Stark
net to in starkware I should say today
we already have a shared prover it's
called sharp sharp for shared proving
and we use it for many systems together
so we use it for public Stark net we use
it for private Stark X instances which
are Layer Two platforms for exchanges we
use it for app chains of Stark net and
all of these com all of these proofs are
combined into single recursive proofs
some of them are applicative recursion
some of them are regular recursion and
all of this is submitted in a single
proof attesting to a huge number of
execution steps across multiple systems
so of course this could also be used for
messaging between different
rollups and the do we have any questions
from the audience no okay uh thank you
very much for your presentation Place
Applause
did you guys
h
s
okay uh we're going to continue with our
next
talk uh so let me announce our next
speaker who will talk about base per
confirmation with Mr mu boost so please
welcome
Lan okay hello everyone um today I'm
going to talk about basb confirmation
with Mr M boost I'm Leno Shani from
nethermind
research okay so most rollups let's talk
about most rollups today so most trups
today build their blocks using
centralized sequencer so users send
their transaction to centralized
sequencer the L2 transactions the
centralized sequencer will sequence the
L2 transactions eventually construct
these L2 blocks submit it to the L1
block building Pipeline and then the L1
block block will constru include these
L2
blocks and centralized sequencer are
nice they can provide pre-c
confirmations and pre- confirmations
what are pre- confirmations basically
users for example user transa submits
their transaction C to the centralized
sequencer the centralized sequencer will
return a precom which will say I will
promise to include your transaction C at
the third position of the L block after
transaction a and transaction B and then
some time passes and then the
centralizer will actually like submit
this L2 block but the thing here is that
prom will happen way ahead of time where
before before the L2 block is actually
submitted to L1 so it provides good ux
so Central sequence are nice they can
provide fact
ux we have few comps but however they're
centralized so big question here is how
do we
decentralize so one idea here is what if
we remove the SE sequencer Ro
entirely and this bring us to base base
rollups so base rollups idea is to use
the L1 block bling pipeline to sequence
not only the L1 transactions but also
the L2 transactions so the user submit
their transactions not only L1 but also
the L2 and then the L1 block willing
pipeline will sequence not only the L1
but also the L2
blocks so let's expand this L1 block BL
pipeline
part so this is like what the L1 block
Lo pipeline looks like right now the
user will submit their transaction and
then there will going to be Builders who
are going to collect these 01
transactions and then they're going to
construct blocks and then there's going
to be many Builders and then there're
going to be many blocks and then each
are going to submit a bid to the
proposer the proposer is going to select
the most profitable block and then
propose
it so the idea of Bas trups is that
let's use this same pipeline that was
used for the L1 which is used in blue
here also for the L2 transactions which
is using the red arrow
here and basees are great they inherit
the o1 sensorship resistance and
liveness because there is no like
external entity other than the and we
only have the L1 actors that we already
have right now
and it also enables L1 composability
because these L1 Builders they will have
full sequencing rights over the L1 and
the L2 so they can act basically as a
shared sequencer between the L1 and the
L2 providing composability
guarantees but there's a problem which
is base rollups are slow because there
is no pre-confirmation
here so to the address this problem
there's Bas pre
confirmations so B pre-confirmation the
idea is this let's let the L1 proposer
opt in to provide pre-confirmation
during their slot so like the user can
directly send their L2 transactions to
the L1 proposer the L1 proposer can
directly respond with a pre-confirmation
and then later on the L1 block building
pipeline runs and then the proposer will
ensure that these L2 blocks are included
in the L1 blocks that they
propose so one observation here is that
providing pre confirmation requires
sophistication because like the the
proposer here you have to have some API
or so some like RPC end point to provide
the confirmations and you also need to
run the L2 full nodes to actually like
sequence these L2
blocks so they would probably want to
delegate and the they will want to
delegate what we call
gateways so the idea of gateways is this
proposer can delegate the pre-con duties
to gateways ahead of their thought so
the proposer can say hey this is my
Gateway please send your pre-con request
not to me but to this Gateway and the
Gateway will be responsible for
responding with pre-confirmation and
then eventually the Gateway will
sequence all2 blocks submit to proposer
proposer will include it in their all
one
blocks so gateways are nice but they
have some problems which is first the
inherent of L1 censorship resistance and
liveness is
degraded because now you have this G
entity that didn't exist in the L1 block
building pipeline that is now sequencing
the L2 transactions and now L1
composability is also made more
complicated because you no longer have
an entity that's sequencing both L1 and
the L2 because the Gateway is sequencing
L2 the Builder is sequencing
Z1 so the question here is can we
introduce Bas pre confirmation while
retaining the good properties of Base
rollups and here comes our proposal
which is called Mr Mev boost so it's Ur
for multi-round me
boost and the idea is this so let's
split the slots into multiple Subs slots
AKA rounds and in each round let's run a
m boost auction to pre-confirmation
run it every 3 seconds for
example and and this uh pipeline is nice
because there is no additional entity
added to the pipeline so there is no
Gateway here and as a result we inherit
the L1 sensor resistance and liveness
much
better because there's no additional
choke point to the system and also en
enables L1 composability because the L1
Builder now is like sequencing both L1
and the L2 or they're like
pre-confirmation
yeah thank you a lot um so just a quick
reminder to the audience you can ask
questions by scanning the QR code and
uh do we have any questions from the
audience yeah I I was wondering myself
um if you can um explain you know how
long you've been working on this idea
and uh if you published any papers
already uh yes there's a e research post
um title of the same thing like based
pre-confirmation via multi round me
boost I think that was like two or three
months ago two three months ago so
people can find it on yes okay thank you
very much uh let's uh one more time give
a round of applause to our
speaker
for for
all right uh we're going to continue
with serious Topic in cyber economics so
let me introduce our next speaker who
will talk about not operator perspective
on pre confirmation transaction pipeline
please welcome our speaker Michael
Moser hi everybody um let me just
calibrate this yeah so I'm Michael I'm
head of research at course one we are
not operator with just about 3 billion
in stake uh some of you guys might know
us from some of our research papers
actually for example we've designed MV
mitigation on dyd xv4 uh which is a
system that's currently in production we
were also quite early to timing games we
started kind of experimenting with this
type of thing early last year and then
and then we think it's always important
to to strike a balance between rational
competition and ecosystem health so
we've published quite a bit about our
approach right and we took very
transparent angle to that and I think
philosophically this presentation is an
extension of that I just want to talk
about pre-confirmation from a proposal
perspective and maybe a more spicy way
of framing this presentation could have
been you know timing games in pre-
confirmations what do they look like and
then secondly what could an early
approach to pricing pre- confirmations
look like right I think first of all
it's important to note that it's very
early days I think there's just one
public pricing model for pre
confirmations and so what I'll describe
here is more of a general approach
rather than you know a specific model
because this will be very parameter
dependent and you know in the spirit of
rational competition we'll talk about
what it is that we do but we might not
have all the parameters public right
naturally um yeah so here's the agenda
I'll quickly walk through the types of
pre- confirmations that I'll talk about
the pre- confirmations pipeline from a
propos of POV uh game a is kind of like
a time in game right what that would
look like and then game B is pricing and
optimal inclusion so let's dive in um
yeah I think there's a lot of jargon
flying around and I think it's important
to just bring these things back to what
they actually are they're basically
inclusion pre-confirmation and then
they're execution pre- confirmations and
I think the key difference between those
you can really boil it down to the two
points I give at the top of the slide an
inclusion pre confirmation is just a
credible commitment that your
transaction will be present in a future
block uh but it's not a commitment of
the transaction actually executing right
the transaction may fail so what the
validator does is it tells you I commit
to putting your transaction in there but
then again you know if it touches
contentious State there's a chance that
it will fail an execution
pre-confirmation by contrast actually
commits to the transaction being one
present of course and then two subset
executed in the block therefore it
should not fail okay so what does this
mean in practice implication one
execution pre-confirmation can touch
contentious state right they also
require the block to be simulated
because otherwise you cannot commit to a
transaction actually Landing right you
need to simulate the block out as a
whole to understand whether this is a
commitment that can be credibly given
and then conclusion one from that is
execution pre confirmations are best
issued by Builder
and I think there's two really simple
reasons for that right if you just Dem
mystify it reason a is that Builders
have private flow um and you know as
like a proposer you don't see that
private flow so you a priority do not
have the option of simulating a block
out fully simply because not all
transactions are available to you and
then um and then B uh Builders also have
kind of sophisticated pricing right this
is something that they they they do in
terms of the it's part of their
Competitive Edge for a proposer it's
really more about uh about uh running
infrastructure really well okay I see
the I see the the light went out but
hopefully the the rest of my talk will
be enlightening right so maybe I'll do
my best um inclusion pre confirmations
on the reverse don't touch contentious
State because otherwise you know is not
something that that you you could you
could commit to without giving the
execution precon
which means they're typically best
issued by proposers and the reason for
that is just that the proposer is
certain to propose right with a builder
Builder a may win the auction but
Builder B may also win the auction with
the proposer you know for sure that the
proposer is going to propose the next
block and therefore you do not have to
probability gate it right if you get a
pre-confirmation from a builder you
always have to expect that that Builder
might not win the block or you know it
must solicit Downstream agreement from
the proposal but with the proposal there
is no such uncertainty right the
proposal is quite quite certain unless
something really terrible happens on the
infas side of things which is
unlikely um okay so let's zoom in on the
latter Point Let's zoom in on inclusion
quick confirmation transaction pipeline
for a
proposal um yeah it's kind of sketched
it out a little bit there um there's of
course a lot of nuance here but I think
to understand the general concept it's
enough to to understand the general
transaction flow and then I think we can
dive deeper into into uh more uh
granular detail um the generalized
proposal inclusion pre-confirmation
transaction pipeline you basically have
a transaction
originator would be you know maybe it's
a based rollup maybe it's a user and
that transaction originator would send
the transaction to some kind of
transaction aggregator right uh you do
not want transactions to be sent to the
validator directly because then what
what functionally happens is it can be
you know it opens up a Dos attack vector
and that would very badly reflect for
example on home stakers it also
generally wouldn't be the way that
people are are set up in if you're met
on Solana you proposers expect a certain
amount of traffic on a f that's really
not the case so there would need to be
some kind of proxy in the middle you can
conceptualize a little bit like a relay
and this proxy can do two further tasks
right either it just takes the
transactions and then forwards a set of
transactions to the proposer for the
proposer to choose pick and choose or it
does pricing itself and when it does
pricing itself you know frequently the
lingo that's being used is we are
talking about a a Gateway here um so
really that's kind of where the the path
diverges okay either this type of proxy
it does pricing or it doesn't do pricing
and then for the proposer if you want to
optimize you have to be opinionated
about two things first you must Source
transactions optimally this basically
how do you interface with the relay
Gateway proxy whatever you want to call
it in an optimal way and then B yeah
there's a there's another scenario or
this is like a subset of scenarios where
you can engage in pricing and then and
then three you know there's also maybe
another game where you can strategically
play inclusion and exclusion and we've
actually published about this right but
this is more relevant for pre for
execution precon so if you're interested
in that you can find it on E research uh
it's uh it's by Umberto who's a
colleague of mine and maybe I just want
to mention here this is a co-op with two
other team members Umberto and Beno
right are very um very active on uh this
type of of more quantitative
research um okay really let's take it
back right either transactions will be
sent to trans will be sent to a proxy or
transaction pricing can be delegated to
a third party um and then and then to
kind of close the slide I want to just
you like structure out these two
optimization axes optimal transaction
sourcing what that would mean in
practice there may be something like a
timing game but in actuality we would
argue that it's a reverse type timing
game and uh yeah and uh and then there's
a sub game where you know some
transaction types you might want to
strategically include or exclude but I
won't talk about this today and then
secondly for pricing yes if there's no
Gateway design and the validator does
pricing then you need to have an
in-house an in-house opinion on that
right I think in general it's important
to say that all of these things always
exist on a risk reverse axis for example
even in normal PBS timing games if you
push them really far what you do is you
simply you simply delay into a flat
curve and you actually you're actually
on a very bad point on the risk reverse
axis right so I think it's important to
always frame that in terms of expected
returns okay let's talk a little bit
about optimally sourcing
transactions yeah so this is a busy
slide um therefore I'll take it step by
step you see two two kind of axis of
graphs here there's two graphs at the
top and then there's two graphs at the
bottom and I think the the way to read
this best is the two graphs at the top
correspond to the first large point on
the slide and then the two graphs to the
bottom correspond to the second large
point on the slide I will explain um I
think the first thing to notice here to
set up kind of the timing game is that
gas use is dynamical right I mean it
varies a lot between blocks but then it
also varies a lot within blocks and if
you look at the the graph there at the
top right that's basically you know the
gas per transaction distribution and
it's of course extremely skewed and then
if you look at the gas usage versus
position which is on the top left here
you will notice that you know like the
the higher a transaction position is in
the block the more gas it consumes okay
so let's let's just keep that in mind
the earlier transaction is in the block
the more gas it tends to consume with
you know some edge cases around
background specifically and the gas SP
transaction is is distributed in a in a
manner which is which is super skewed um
and then I think and then the second
information we need to set up our case
here is that PBS timing Games capture
value by soliciting the block very late
right so you you send a get head a
request really late you give the Builder
a lot of time GA transactions to kind of
combine them right for Sixx Arbitrage to
come in and this is this is what you see
at the bottom here right this is the the
way it works in in PBS so the the bottom
the bottom left graph is the number of
transactions and you know kind of when
they come in and I think here the point
to take away is just the longer you wait
the more transactions are way aailable
so they can be aoral spaces higher and
then the the second the second graph at
the bottom which is on the right is uh
you know like the longer you wait the
higher the the ratio of the bit to the
max bit is right so uh basically the way
you would read this is simply the
expected value of a block goes up over
time okay uh and now and now let's let's
look at let's look at the game kind of
that we can deduce from these two
categories of information um so
conclusion one here is PBS timing games
benefit from expected transaction gas
use going up over slot time and PBS
timing games also profit from winning
over transactions with mland in the next
block right now for pre-confirmation I
would expect this to be to be quite
different and the reason for that is
because the the premium that you're
willing for to pay for pre-confirmation
it corresponds to the service level you
are getting right and let's say let's
say you can land anywhere between you
know like within a 12C time frame if you
land at like 11 seconds then you're
getting a certain service level but then
if you land at one second to the next
block do you really need a
pre-confirmation right so there's
definitely some like an effect here
where instead of instead of the expected
value going up over time you know it
might go down over time simply because
the service level that you provide where
pre-confirmation this is earlier this is
better the earlier in the block right
you're just doing more and and
and what the and what this would mean to
us is that the the pre okay so we can
say the pre-confirmation inclusion
premium scales with the expected weight
time right and what this what this would
mean to us is on the one hand we would
expect pre-confirmation value to Cluster
early okay so if you look at the PBS
graph here we wouldn't expect it to look
like that for pre confirmations in
actuality the highest expected value per
transaction that would happen that would
happen a lot earlier and then and then
you really probably wouldn't want to
wait super long instead what you want to
do is you want to you want to wrap the
pre-confirmation auction up and you want
to give the build a more optimization
time and then and then if you take it
really practical we think there is an
optimal early end to the auction that is
you know there a function of the the
transaction arrival and uh distribution
and and the and the price Decay right
and we we have some we have some very
specific thoughts on this but
unfortunately there's no time right so
we'll need to dive in to into the next
game and uh this is uh pricing and and
optimal inclusion so previously I
mentioned that either a Gateway can
price it or you know potentially a
validator can price it right um if you
ask me for hypothesis I would say it's
probably more likely for the gateway to
price it because I think node operators
on the whole as I mentioned earlier more
set up to run good infrastructure right
pricing is not is not something that
typically comes up um but yeah that
being said let's go ahead and and and
sketch sketch.
quick model right um I
think uh I think the the first thing to
consider here is earlier I mentioned
that the transaction the gas usage of a
transaction that varies depending on
where the transaction is in the block
okay and and so and let's let's approach
this realistically and say there are
kind of three tiers of transactions in
the block right there's like tier one
which is super early which is top of
block which is typically your sex tax
Arbitrage
there's tier 2 which is kind of you know
like mid block and then there's tier
three which is anywhere else in the
block right can say like mid block to
bottom of block and and then and then
okay so we have this sistic is it valid
well we ran the statistics on it and and
we you know like this P value which is
which is pretty pretty small if I if I
read that out now that would take the
end of my presentation time so these TI
are not are not you know the same in
terms of transaction usage right uh
sorry in terms of gas usage so it's a
heuristic which is kind of you know like
if you're
rigorously look at it from a statistical
POV it's fair and then and then one
conclusion we can draw from that is that
validators compete for tier 2 and tier
three transactions because tier one
transactions they are just super tight
to being at the top of the block right
the sex tax Arbitrage you know like
there's no there's no really real
discretion about maybe including it the
later point of time it has to happen at
that point in time because it is tied to
a certain to a certain price Delta
between a centralized centralized
exchange and the Dex okay um yeah uh
that being said uh again takeway one
there can be you know we can separate
our transactions in the block into three
tiers in a statistically valid manner uh
takeway to uh tier one transactions here
really aren't aren't you know as as
useful for our pricing model because we
are talking about inclusion pre
confirmations which don't really touch
contentious St in this way um that being
said let's let's sketch out the model
right um so the first statement that we
can make is well what what do we need to
build a model here right can we even do
that yeah I think we can do it right
because inclusion pre-confirmation do
not touch contentious State uh you can
you can build a model uh solely on on on
public flow okay so the model can be
built that's premise a um two um um how
how would the model look like if we if
we if we dig in a little bit deeper well
okay so we have a base Fe component and
we have a priority fee priority fee
estimation um let's let's look at kind
of some of the the attributes of these
two right um the base fee is easier to
estimate because it's discrete and then
the priority fee is a lot harder to
estimate because it it is it is
continuous right so just there's a
there's a much much larger space
um the base fee we can generally frame
as the the opportunity cost of
preconference transactions right because
if you if you do not
pre-converted base fee and and then the
priority fee can be seen as something
that's more akin to like a premium right
which it is in actuality if in a spot
Market the priority fee would basically
correspond correspond to to a premium
okay so how can we schedu a toy model
well first of all we need a way to
forecast the base fee which is which is
you know like something that can be
reasonably done and then and then we we
we uh finalize a distribution of the
priority fee over tier 2 and tier three
transactions because again t one
transactions not as relevant for
inclusion pre
confirmations um and then and then what
what we think is a good first way of
approaching it is you take the Bas fee
you take the Bas fee Baseline and then
you add a percenti of the priority feed
distribution as the pre-confirmation
premium to it and actually which
percentile you add to it I think this is
largely this largely a function of uh
you know it can kind of you can see it
as a confidence interval of how well you
understand uh transaction transaction
pricing in the future slot right um I
think this is a good way so a good way
of approaching it um we hope to to
publish a little bit more on it okay I
think for both the the last game with
timing and for this it's important to
look at things empirically uh for that
reason this is something that will
mature over time but in general I think
this is an approach that that is valid
you know for either an a operator
pre-confirmation protocol um or whoever
else is interested in that yeah so I
think I'm I think I'm ahead of time
thanks for thanks for attending and this
is it
yeah thank you a lot uh we have two
questions I will um give you a chance to
choose which one you want to answer
first sure sure so I'll answer the
question with uh with the one vote uh
first between besides based rollups and
MV Searchers who else might be using
pre- confirmations okay let's let's take
the taxonomy that I mentioned earlier in
the presentation between inclusion and
execution pre confirmations I think for
inclusion pre confirmations like it's
going to be two cases one is based
rollups and then the the second case
would be ux right okay so you can look
at that and you can say well you know
waiting 12 seconds is that really so bad
but then if you frame it differently and
you say you know speed that's comparable
to Solana then that actually that
actually sounds a lot better right so
for inclusion I think it's ux let's say
wallets and based wups and then for
execution pre confirmations I think
that's kind of where search has start
coming in right and uh and not only like
Atomic searches but then there's a point
where it gets relevant for sex Dex
Arbitrage as well um yeah okay thank you
uh we still have a bit time if you have
any questions we have microphones
available okay uh thank you a lot I
think U it was a very interesting talk I
also not operator myself I'm just a home
sticker okay thank you great thanks
d
uh hello again uh we're going to
continue with uh our lightning sessions
so our next speaker will talk about
search competition in blog building so
please welcome our next speaker akaki
mes hello everyone welcome to the
presentation so today I will talk about
Searcher competition in Block building
so this is the paper title and it was
coauthored with kristofh Schlegel and
Dani from flashs and Benny sudo from
eth and I'm a researcher at of chain
Labs so motivation was me and we we know
that there are many forms of me
extraction and I'm listing only the most
popular ones here so there is this sex
sex Arbitrage background sandwiches and
liquidation and in each form there are
also many different spe specializations
that you can take as a Searcher and here
the main point is that there are many
different types so Searchers are
different in their
specializations so it create some kind
of heterogeneity among Searchers so we
tried to model this uh with the tools of
Game Theory and for that we need to
identify who are the players and the
main player is validator or a proposer
that proposes the next blog and then
there are these specialized arbitragers
that in the ethereum setting are called
Searchers and in current market there
are also builders that aggregate
Searchers and also mol public manol
transactions but we are ignoring um it
for this uh simplified game because for
us the fundamental players are Searchers
and the proposer okay we denote the set
of Searchers by S that we can identify
by their addresses then Searchers submit
their bundles of transactions to include
uh in the block and typically now they
send it to um block Builder but in
principle they could have sent it to a
proposer then from these bundles there
are some uh in these bundles there are
some conflicts so you cannot be build
the block that is the union of all
bundles
so you can build many different blocks
for a build block Searcher generates
some value and the validator or the
proposer also generates a value so these
are the uh smallest building blocks of
our game so we are abstracting away from
all part particular mechanisms how they
interact and that includes Builders and
we only try to understand who will get
how much among these players depending
on their
bundles so for this we are using uh
tools from Cooperative game theory for
that we need to define a value of a
coalition and value of a coalition is
the best block that the Searchers in
this Coalition uh
build if uh there is no uh proposer in
the Coalition then the value is zero
so proposer or validator can uh block
any or veto any block so you need to
agree uh with the proposer the The
Searchers and this already gives a
coalitional transferable utility game
and in these games the most natural
solution we think is the
core and uh let me Define what is core
it's very simple and intuitive
uh the core solution gives uh uh payoffs
to all players so that no uh Coalition
of players prefer to deviate from the
allocation and create their own block
together because if if they can they
will and so we need to specify the
payments to all Searchers and the
validator of the global
game so there are nice properties that
core has first of all it's uh always
nonempty you always have one solution in
particular you can give all the value to
validator but of course there are this
would be very unfair to Searchers and
there are other core Solutions too often
but not always so for example there are
cores such that Searchers capture all
value and if we have uh additive value
over the bundles then we actually have
uh nice characterization of the
core so to make it more interesting we
look at the St stochastic setting where
we have a number of opportunities
denoted by m and number of Searchers
denoted by n and each Searcher generates
some value for each opportunity so we
have this Matrix and by P we the know
the probability that each Searcher finds
each opportunity okay then we have very
nice
um simple result that as soon as uh
probability slightly high so it's larger
than this to log n divided by n and
there there are not too many
opportunities so m is less than and then
with high probability the validator
captures everything and this can be in
particular uh empirically checked in in
the data so thank you for your attention
happy to answer your
questions yeah uh thank you very much so
um I posted one question uh I wonder I
wonder if you know how many search
providers are currently in ethereum
ecosystem So currently today I don't
know but uh it's in the order of
hundreds hundreds yes okay and we have
one more question how do you know that
the core is non empty and this is
usually requires strong
assumptions so we know because if you
give all the value to validator it
satisfies all these inequalities that
core
requires it's very easy to check and
strong assumption is that what you may
refer as strong assumption is that
validator validator can block any or
veto any
Coalition so that that has a veto power
and that's what that's why core is
nonempty and in particular we give exact
uh example of a
core uh okay uh thank you very much
please give a round of applause to our
speaker thank you so uh we're going to
have I think break and the next session
will start at uh 1:50 thank you
m oh
see
m
come
is up
what up
he for
all
hello yes much better hi everyone um we
are ready to start our afternoon session
hope You' all enjoyed your lunch it's
the last day of Devcon uh how are you
feeling Yes
W oh come on you can do better a little
bit more come on come on how are you
feeling all right all right I'll I'll
take it I'll take it yes yes thank you
so much all right um so just a couple of
housekeeping announcements before we
proceed with the talk feel free to take
pictures or videos if you would like to
just make sure that that the flash isn't
on so that you don't distract our
wonderful speaker and um there will be a
QR code for the session so that you can
ask questions during mircat you're
probably already familiar with it by now
it's the fourth day but yeah make sure
that you scan the QR code submit your
questions there and upvote those that
you find interesting at the end of the
talk we'll have a short Q&amp;A
session and uh yeah without further Ado
let's move on to our first speaker so
our first speaker is Shia a co-founder
of Perpetual protocol Shia is going to
be giving a talk called building a
cross-chain DEX with chain abstraction
and
intents and in this talk Shia will
explore leveraging intense and chain
abstraction to create a seamless
cross-chain trading experience let's
welcome to the stage Shia
hi good afternoon before the
presentation and uh I'm sha co-founder
of niod deex uh I've been building
things different things in eum uh since
friend don't know what I was working on
the thing we're building are just too
complicated to
explain but this time is different I
finally build something that even my
parents know how to use so uh today I'm
going to share the experience of
building a niod deex a product that uh
high production complexities away and am
to make defi accessible to
everyone so uh problem we all knew there
are so many usability issues gas C phas
Bridge tens of L
toes there are just so many things you
need to figure out before do a simple
transaction and most of us I believe are
offering different solutions from
different angle so like U Better login
another wallet or a faster chain but
even if we have some uh great solution
for part of the problem but if some
other place some other step are broken
then users still cannot get their jobs
done think um
for example um just like someone want to
buy her first coin let's assume they
have a perfect wallet and onboarding
experience is just perfect but it's very
likely that he will St when he need to
pick one CH from like 100 different
L2 or let's say now he has a um perfect
wallet and also a best Dex and now he
want to connect his wallet into her uh
uh the best deck but she might be mobile
and she don't know why just what I
connect sometimes just not connected and
nor the best wallet or the best Dex can
help them helping
her or um maybe she finally overcome all
problems now finally the the last step
she's going to buy the coin she want but
turns out it might be a fishing link
then he's buying the coin that actually
not the coin she think she's buying and
the worst scenario is she might lose
everything just because of this simple
mistake after spent so much
effort the risk and reward seem
asymmetric I think um there's no like
usable in crypto it either works or it
doesn't
so I think um we cannot make it usable
by just offering some partial Solutions
we need to have a holistic approach that
address end to end user
experience and users should not need to
learn like 10 different tools just for
solving one
problem you need to user just want to
deal with one product instead of like 10
different
tools so uh and from uh the entire
process we shouldn't mention any
technical terms those crypto Jun is
Irrelevant for the user normal user who
want to get things
done and when we are talking about chain
abstraction it's not about technology
it's all about user experience we need
to work start with user experience and
work backward to the
technology so it seems like a very
humble and simple request the ideal uh
flow for a normal user should be just
like for example like a biometric loging
just like most of other app and then
deposit some f and then you can start to
trade in second seamlessly in one app
but that's not the fact and after so
many years seems like there are not many
product offering this kind of experience
probably not even
one so our approach is to offer a UniFi
product combine several powerful
components and that only integrate some
trusted the
app with a native con user interface to
offer a simless user
experience um but then it's unlike
traditional wallet that will expose user
to unlimit the app which could break
your experience or maybe could be
unlimited potential attack vector and
it's also not un uh not like traditional
Decks that you always need another
wallet to
connect and I'll start to uh share like
like how the UN boarding experience
first can I play the
video
thanks oh great thanks so um user should
use uh
uh this uh should use a crypto like uh
normal F Tag app so in this case uh you
just use the pass key and create a
wallet and uh by the way there's a so
second Pass key is for creating a
session key but uh it's out of the scope
today but anyway now you have a self
custody wallet without managing the C
phras so uh behind the scene uh
um um after that process we'll deploy um
Smart Control wallet that of course
confirms the
contract wallet called kernel built by
Zod def uh W as a service
company uh so when we deploy this Kel
contract uh we also use this Pass Key
account as the main
signer there is one unique feature or
constraint of Pass key is exp binding to
a domain which means uh you cannot use
this Pass key in another
domain so it's nearly impossible to be
fishing but also there is another
downside that what if the site is down
so seems like a recovery mechanism is a
topic that we cannot skip but the
challenge is if users still need to
create another W for the
recovery but then it's probably they
still need to manage the SE race then
it's our failure
so uh we want to have a mechanism that
even user don't need to access the
private key or they don't even need to
manage that as long as they have address
that can receive the fund even it's like
a centralized exchange address or
someone they trust that still
works so our idea is just uh is very
simple so while user has the access to
the pass key so he can set up he can uh
enter the fallback address that he plan
to receive the fund when something goes
wrong and then he used the social login
to create another Guardian address and
then ask the colonel to Grant the
special permission to this
Guardian that the guardian can trigger
some recovery event that led Kel to
transfer all the fund to this fullback
address this is only possible because of
this is a smallart contract wallet at
least uh for
today and um this kernel contract also
Implement another modular smart account
um standard
ERC
extended with compatible permission so
uh for example like uh in our case this
permission would be like you only allow
Guardian to trigger uh to ask konel to
call a function uh that is transferred
and the receiver must be fullback
addressed so um now uh user has a
no reliable self conservative wallet
even when the site is down or even if
she lost the pass key so after the
onboarding experience we're going to
talk about how we combine uh leverage
the intent based cross chain Swap and
some account abstraction to offer a
simless chain abstraction
experience so uh first let's start with
a scenario that Alis want to buy some AR
with uh usdc let's say a usdc from U
optimism could you help to play the
video thank
you uh so atast she only focus on what
asset she's going to buy and don't need
to care about Chen and pick the asset
buy that's
it don't need to worry about any other
thing no gas no bridge and you can see
there are both optimism and ariton in
one place we should unify ethereum h of
ethereum layer to into feels like a one
ch
um but uh so how does it
works so we go through this cross chain
architecture step by step uh but should
be quick the concept is quite simple so
first in optimis chain and Alice
broadcast uh sender sign order and
procast this order to express her intent
so now Alice want to buy a minimum
amount of arish with uh
usdc and then uh relat pick this order
and then uh relate this order send
transaction to Smart contract the smart
contract will pull some usdc from Alis
to this smart contract butock the fund
as an
ESR he will relate uh he will repay the
usdc later to relay once the uh he he
ensure the relayer finish his
job so in the op ch ch this relayer um
since you know the intent the order and
then send the transaction to smart
contract and then smart contract was
transfer the Orit Chom to
alies and uh from Aly point of view the
cross chain transaction is done the
trade is done she already received the
AR CH she need and she already paid the
usdc she don't doesn't care it's in a
smallart count or another
relayer but uh for relayer she needs to
waigh uh the cross shair there there
must be some like cross shair messaging
under the hood and she she must to wait
the uh CR messaging to let optimism CH
know okay now relayer in ariton already
done his
job so um you can imagine this crossair
messaging is not that fast but from 's
point of view it's a lot faster because
once her trade is down she didn't touch
anything about
bridging so once optimism confirmed uh
okay Rel did his job in AR Chom then
smart contract will unlock the Fone and
just transfer the fun to
relay so um this is just an overview of
this architecture and now we're going to
zoom in a little bit on this smart
contract
component so actually there are several
layers so first um us uh niod deex as a
user facing product um has another
contract that confirms another cross in
standard UHC 7 6 8
work together to share uh infrastructure
like ERS and fer that can make this
system more
efficient uh under the hood the uh this
uh 76 A3 implementation interact with
another settlement layer in our case we
use a cross
protocol um then AC course protocol also
uh work with another Uma Oracle
optimistic Oracle to do the cross
messaging so
um as you can see relay seems like
taking a bit more risk but uh user is
still not risk free as many other um
smart contract user so there must be
some smart Contra R uh when using this
kind of complex architecture but uh I
think it's our job I mean the one who
build the user facing product we should
be accountable to deal with this
complexity not user for example like if
something goes wrong like okay Uma
Oracle um has a unexpected result which
may um make user loss her Fone but it's
impossible to ask Alis user to act as a
distributor during the challenge
period um if we really want to do this
kind of like chain abstraction thing I
think it's not only about make things
easier
but also about uh dealing with this risk
and complexity if we if we abstract this
away then it's our respon responsibility
to help users deal with
it so uh today uh We've shared approach
that to offer integrated experience that
make Divi useful just like a normal
thing Tag app and we El we show how we
can eliminate C phrase and what
extension
by adopting Pass Key and embedded wallet
and we also show how we can um abstract
gas away and design a fun recovery
mechanism thanks to modular mod account
and we also show how we can let user to
buy most of the aay in almost every evm
CH in one tab it feels like in one CH
without knowing anything about multi
chain and now user can use Defi and use
crypto in one app instead like 10
tools and we crypto native often think U
user should do your own research but I
think the truth is no I want to do
research and even um it's about dealing
with money most of the normal user they
still need someone to trust to be
accountable even what we offer is a
self- custody solution I think self
custody shouldn't be an excuse for us
that don't care about user experience
if we really want to unboard a building
user to crypto I think user facing
product like us should have the
encourage to manage the entire user
journey to on every step to make sure
our experience meet users
expectation uh I'm sha from niod deex um
everything I share is already living
production for like two months and I
really hope uh we can make Divi and
crypto accessible for everyone
thanks a lot Shia now we have a little
bit of time for questions and thanks a
lot for submitting a few I see only one
of them is upvoted so let's start with
that one and the question is are there
more security issues in using intense
chain abstraction versus fully onchain
Alternatives like Unis swap
our approach is actually not that much
difference compared to unof but I'm not
sure what kind of fully untr alternative
like Unis swap because if you trade if
want to trade like a a a cross chain
swap in Unis swap we're using basically
the same
mechanism unless you're talking about
like every doing everything in one chain
and then Bridge yourself to another
chain then
um but I think that's something that's
not compar
all right so let's move on to the next
um I don't know whether that one is
uh counts as as uh promoting I'm not
from across don't ask
me all right the next one is uh how can
the solver prove that it made the
correct work and are there any ways the
solver could take Alice's Tok tokens and
not do the swap but steal
them and take oh sorry where is the
problem so it's it's this one okay okay
thank you uh it's
gone anyway
uh uh I don't remember the problem it's
a bit long but uh I guess it's not able
to do that actually relay has more risk
than the trader
because um if
you it thank
you sver doesn't need to prove it made
the correct work it's the cross chain
messaging protocol need to prove the
sver uh did the work and server just
need to uh there's not much power from
the server solver just need to wait and
hope the culture messaging doesn't steal
his
money all right right um the next uh
question is what bridges are you using
behind the scenes to fulfill the
orders I don't uh we're us this we're
using across settlement but I don't
consider this as a bridge because we are
not using their
liquidity but it depends on how you
define the bridge we're just using that
for for doing the qu settlement that is
a bit different uh compared to bridge uh
at least that's what uh understand this
right the next one is is your solver
Network open to participate in who is
actually solving the user intents how do
you ensure users get the fastest and
most efficient path okay the easiest way
is we making permission so we provide
liquidity within a certain time period
to make sure we can always deliver uh
under our control but of course uh once
it's know uh maybe after some time of
Peri period period Then
everyone can to take this order and
because we actually try to uh know rely
on like the solver Network in across but
uh seems like because we offer too many
different kind of asset so there are
only a few major asset that's you know
some other field I want to
take all right all
right um the next question is how do you
manage liquidity providers is there a
separate interface for them we're right
now for spot trading we just using uh
we're more like a UI layer like a we
just uh use like act as aggregator to
use others liquidity from like Unis or
other
places all
right um Can a user approve spending
amount from the wallet when using the
wallet in another app connecting via
wallet connect assuming wallet connect
connection is
possible uh technically yes but uh but
now we don't think it's easier to
understand for normal user so uh at
least in our product it's it's not
supported but yeah it's technically
technically
doable all
right um what is the backend between
pasy and kernel
validator and as far as I remember now
it's in zero
Dev yes it is okay cool you just got a
confirmation lovely um why pwa over
native app it's just easier for us to to
to launch and and we just launch for two
months we don't want to wait for like
another month to do it for Native app
but that's also doable in the road
map cool and uh there are a couple more
questions but I'm afraid the time is up
uh for the Q&amp;A feel free to catch show
after this and ask all of your questions
and let's heared up for for show
all right all right so the next talk
will start at 2:20 it will be a workshop
so stay
tuned yeah
C
back back back
n
hello hello hello all right let's get
settled in for the last session at the
stage the the closing ceremony is is
going to be right after this hope you're
all excited
um our next speaker is anit
chiplunkar uh co-founder and head of
research at Frontier and one balance and
uh it's going to be a workshop called
speedrunning chain abstraction e eips or
ERC erc's and or
eips and so in this Workshop um we'll
look at different aips in the pipeline
across the cake stack and how they
relate to chain
abstraction so because it's a workshop
we're going to do the questions a little
bit more interactively so feel free to
ignore the mircat QR code that you see
just raise your hand when you have
questions and I'll get to you with a mic
and we'll do it this way all right um
without further Ado welcome to the stage
an chunar
hello hello
hello am I
audible
um this is this is supposed to be like a
speedrun it um the core uh objective of
of doing this Workshop is basically just
explaining the the Grand Vision of what
we mean when we say chain
abstraction uh um and then digging
deeper into more technicalities about
what are the different eips or erc's
across the stack uh that would help um
you accelerate or or or give the chain
abstraction Vision to your to your end
users uh one way how I describe chain
abstraction is if you are an app
developer then uh removing the word
Chain Bridge and gas from the user
Journey altogether is is the Final End
state of how how uh I see chain
abstraction and
so um if you're an app developer and the
user does not see those three words
anymore they just go to your app click a
button and get the execution they want
is the eventual end State uh that we
imagine as as the as uh the MC already
told uh I want this Workshop to be more
interactive uh feel free to just stop me
raise your hand uh we can have we can
have questions we can have like a Q&amp;A
session um uh there there are a bunch of
erc's that have their own like
historical context and more technical
depth I won't I won't go into like a lot
of historical context and Technical Dept
but the core idea is just to explain
like what it tries to achieve um and um
we won't get we won't get too much into
the nuances but like how it takes you
closer to to the desired end state is is
is uh the objective of the
workshop um okay so a few few things
this is like the outline U the first
thing is I just want to talk about the
blockchain cake or how we think like
what are the different actors or
different layers in the blockchain
ecosystem uh then like what are the
erc's that interact on the permission
layer what are the interact ercs that
basically are required between the DAP
and the permission layer so permission
layer is more like the wallet and so the
DAP and the wallet layer what are the
arcs that that you need to basically
communicate between these two entities
uh and then what are the ercs that are
needed to communicate between the
permission layer and the solver layer so
like the mempool layer and then what are
the erc's that you need to communicate
between like the solver layer and the
settlement layer we'll get deeper into
like what each of these terms mean but
this is just like the broader
context um and so like the first first
uh section is just about explaining like
what are what is the Grand Vision of
what we are trying to do uh this is
something that I call the United block
spaces of etherium uh if you think about
the last bull cycle uh everything was
amazing like you had the def summer you
just went to an app you clicked the
button you had the thing that you wanted
you you you went to yam Finance you
clicked the button you were able to
deposit into these defi ecosystems and
everything was super smooth the only
thing was you were paying $100 for for a
transaction and so after that this
rollup Centric road map L2 Centric road
map sort of emerged and um it was a
solution to this like block space is
becoming costly problem but it has
created a fragmentation problem problem
and so
um the L2 Centric road map has brought
us many block spaces some block spaces
are red in color some block spaces are
blue blue but um they all commit data to
the ethereum L1 but they don't feel like
they don't feel like United just too
much fragmentation uh if you just look
at like the ux that you are giving to
the user right now you have um you have
three different types of ethereum
if you if you open like your coinbase
wet you have three different types of
ethereum it just causes a lot of
friction to the user whenever you try to
change your network it just pops up and
says hey do you want to switch your
network and then the user like has to go
and and then click another button and
even if you want to transfer funds from
one chain to another it's like you go to
an aggregator and then you send those
funds to some other uh other location uh
you you like have these different
options where the user can choose
between time and cost and and it's it's
a very like buggy uh and uh friction
experience for the end State and this is
this is why it does not feel like uh
United block space like if you if you're
imagine if you're living in the United
States and every state had its own
version of US dollar and you had to
convert when you're moving to one state
to to another in its own version of US
dollar then it won't be as as smooth a
ux or when you were moving from one uh
state to another and you had to
basically get a Visa stamp whenever you
move move from one state to another it
was it would not have been uh as United
and so so this like if you solve these
problem then the ethereum ecosystem the
whole evm ecosystem will feel United
again um so that is I think the final
vision of of um um what chain
abstraction is all about a little bit
detour to just uh explain what we mean
by the uh blockchain kick um and so
there are we imagine like blockchain has
different layers uh and there are
different parties who are operating at
different parts of the stack but they
all these parties fall in like four
broad categories and they have their own
sort of tradeoffs that they are trying
to optimize for um the first is like the
application layer or the DAP layer these
are things like Unis swop or a a user
goes there this is like a ux interface
in front of the ux in front of the user
and then the user goes there clicks a
button gets the thing that they want um
the main thing that application lay does
is basically generate call data uh for
the user so um the user goes to the
website clicks a button it generates the
call data that needs to be or generates
some sort of instruction that needs to
be executed um signed by the permission
layer and then get then uh executed on
blockchain um so the thing that
application layer really tries to
optimize for is finding the application
that user want and then reducing as much
friction as possible um then there is a
permission layer which is which which
are things like wallets um and so there
are multiple parties who are doing
different things in the per Miss layer
but at the end of the day what they're
trying to do is convert this instruction
that is coming from the application
layer into some sort of signed
instruction that the blockchain
understands uh and is able to execute
and change State and so the application
layer is constructing some instruction
format and then the permission layer is
basically converting that into a
language that blockchain understands so
it can be a transaction it can be an
intent and then it gets executed uh on
chain and then the solver layer is
basically Al all your me pools so in in
in v0 you had me pools and then uh as
the me problem evolved you had like more
sophistication that was that that
developed on on the solver layer but at
the end of the day it's all about the
step between signing
and uh
finality everything that happens to your
transaction between signing and finality
is what uh is what the solver layer
cares about it cares about liquidity it
cares about sequencing it cares about
all the different types of auctions you
have there are maybe 100 different
companies are just operating on the
solver layer but this is like the core
tradeoff um that the solver um layer
tries to optimize and then the finally
the settlement layer these are your
blockchains and oracles where things get
finalized um and then that becomes your
root of root of trust um maybe just like
a just as a warm-up as a show of hands
uh can you can people just raise your
hands who is working on the application
layer in the
audience wow quite uh quite a few quite
a few people I did not expect so many
there's this joke running there's a
running joke in in crypto Twitter which
is no one is working on the apps
everyone is working on infra um um and
then uh there's the permission layer
like who's working on the permission
layer like the wallets and and uh
policies and intents um a nice good set
of audience over there as well who's
working on the
solvers
um quite a quite a few people and then
settlement layer like chains
oracles nice nice a little bit less
settlement people uh maybe they don't
like chain abstraction that much but
it's fine uh uh okay so let's let's look
at the core tradeoffs that each of these
layers are trying
to optimize for and basically where they
what decisions these players in these
layers of the cake make um you get like
different properties of your application
and so the the code rateof that the
permission layer is trying to decide on
is between between ux and user agency
and and so like you have one set of
users who just use like Hardware wallets
who verify the transaction hash that if
the transaction hash that they're
actually signing on the hardware wallet
matches the thing that they see on
metamask or or some other wallet and at
the other end of the spectrum you have
people who just use telegram Bots and
they just send their private keys to a
backend server and so but telegram Bots
still generate like 20 30% of the volume
and so there is this trade-off between
what great ux you want to give to the
end end user versus how much agency the
actual the user wants for them and um
this is like a tradeoff that that app
developers or dab developers or wallet
developers actually have to care about
and they lie some somewhere or the other
on the Spectrum another interesting
thing that that has sort of emerged um
is like if you guys have used these apps
or dabs which use Google SSO um all the
Google SSO verification or
authentication that happens cannot
happen onchain it happens in some
offchain compute system and so what what
the app that is doing Google SSO is
doing is is it checks if the oo token
that Google has given you actually
corresponds to the private key that they
store in some secure Enclave or secure
environment and then sign it and so U
even apps that are providing you Google
SSO are making this ux versus agency
tradeoff where users who actually ask
for Google SSO are U are letting go
their agency letting go of their um
censorship resistant properties for a
much better ux and so uh it was very
interesting for me to see like the rise
of these apps which uh like let go some
parts of the decentralization or
censorship resistance aspect for this
for this improved ux and it's coming
from like a user demand um the second
thing uh that you uh the second layer
basically the solware layer optimizes U
or trade trades off between finding the
optimal route
versus giving you like an execution
guarantee and so if you can imagine if
you imagine a world where are there
where there are multiple chains a user
is holding balances in three different
chains uh and says I want like a user is
holding $100 on three different chains
and says I want $100 at the end of the
day on chain four uh find me the best
route pull the funds give me the
liquidity um there is this trade-off on
the solver layer between like what is
the best price that you can give to the
user versus can you actually execute the
transaction or not and so that's that's
that's the trade-off that the solver
layer sort of struggles with and uh
finally on the settlement layer uh there
is uh this tradeoff between feast and
execution speed
so um like if you are trying to move
messages across two different chains
there are different ways in which you
can pass messages like you can either
rely on the L1 L2 Bridge which has like
secure way of transferring funds or you
can trust like some other Bridge
provider which has a multi and it will
give you just just things
instantaneously and so there is this
trade-off over there there are some
properties that obviously we don't like
but there's a breadth of options
available and that's what the settlement
layer sort of struggles uh between
basically giving you a better executions
feed versus like the the cost of time or
cost of of doing that
execution uh any questions till now this
was a little bit heavy or not heavy any
questions till
now no either I'm very good at it or or
no one is
listening but um okay so uh this is what
this is what I imagine the expected end
state to be from a perspective of a dab
so if like you're a dab developer this
is what the end state of chain
abstraction I think looks like which is
a user comes to your front end a user
comes to your daap they don't see these
three words anymore they don't see the
words gas chain and Bridge anymore it's
just abstracted away from their
experience the dab basically is deployed
on some chain it's deployed on some
settle environment L1 L2 L3 whatever is
their prefers be it ZK be be it evm be
maybe in even the new versions of VMS
that are popping up the DAP is deployed
over there the DAP requests either the
wallet or the solver layer what is the
effective balance of the user on this
particular domain on this part
particular environment and then knowing
that particular that effective balance
of the user on that environment can
generate the call data that that needs
to be executed on the environment and so
all the process of basically pulling the
funds from multiple domains into the
target domain into the target chain is
responsibility of everything Downstream
so like the W the permission layer the
solver layer the settlement layer the
DAP the only thing that the DAP cares
about is what is the effective balance
of my user over here and and then what
call data I should generate um or what
intent or whatever is the format I
should generate to basically execute
this uh and so like users can hold funds
like if if you if you if you if you get
back to this United block spaces of
ethereum vision then users can hold
funds on these multiple domains at the
same time like they can hold $10 on Main
net $50 on optimism $30 or $40 on
arbitrum and then the the wallet or the
solver figures out how to pull
everything over from all these three
domains and executes the call data on
base maybe the maybe the user wants to
buy some some mem coin on base user just
clicks a button gets the execution and
and uh that's what the DAP and the user
cares about
um uh any questions on the vision any
challenges things people don't
like I'm getting good at sales
apparently so um okay okay so let's
let's let's take a step back uh let's
only look at so in my opinion you need
erc's at these different interface
points between different layers and
those are the things that we should sort
of standardize there are some like erc's
that I think are interesting on the
permission layer which give which give
uh interesting permissioning or
interesting properties to the apps uh
and so we'll take a little bit detour
we'll just look at the permission layer
erc's and then
um then go then go
deeper um okay so first ERC is
so when ethereum
launched uh many years ago I don't
remember uh maybe draw knows but when
ethereum launched um everyone had eoa
wallets so
like uh um and your wallet basically is
is responsible for doing three things
it is responsible for uh giving you some
sort of a nonchain identity so like a
private key when it is uh converted into
some sort of a hash gives you an onchain
identity your wallet is responsible for
signing which is basically uh verifying
if the thing that you have you are
saying you want to do is actually coming
from you so it does o and then your your
eoa wallet is also responsible for
basically constructing this this
instruction set to the to the blockchain
um over time people sort of figured out
that this is very like restrictive and
this does not have the proper properties
you want for a very good ux um the thing
that was limiting there are a bunch of
things that were limiting with something
like this like one thing is you cannot
have modifiable
authentication and so like if you want
to do something like a multisig then you
would need to deploy a new smart
contract on chain which has its own its
own sort of authentication mechanisms
people also call them policies so you
can have more fine grain policies like
this app can only withdraw these many
funds or I can only with I can only
execute uh $1,000 worth of transactions
in in the next 24 hours stuff like that
so all all that is doable on chain um
all those like checks and balances are
doable on chain and then uh another
property that that uh basically dab
developers wanted was uh like uh
batching of transactions together um
basically
like the flash BS API just does this
like ensures batching of transactions
and so like you have a you have a big
entity just formed to to enable that
property to the transaction layer and
then uh also because you can do batching
you can do like gas sponsorship so the
you can you can give the user $100 and E
let them do the transaction and then
withdraw uh withdraw $100 of any other
token in uh in your solver and so like
these two properties is what people
wanted from a modern uh account which is
granular authentication and ability to
basically execute transaction on behalf
of the user so like gas abstraction is
also what people call it and so
into like all the all the details of
what are the different types of
instructions you can pass or enable but
but yeah these are the two properties
one thing one um one thing that uh I
think is pretty nice is 4337 is gaining
momentum and gaining adoption and so it
will be like the default way how people
deploy smart contract accounts on chain
um but for for a cross chain setting how
some Target chain and you want to
execute the a transaction on behalf of
the user but the user does not have any
funds on the target chain this message
sender message.
sender property is very
important for for every daab so
basically the way dap authenticates if a
request is actually coming from the user
it is by verifying if message.
sender is
the user or not um but be if the user
does not have any funds on the target
chain like the user cannot execute the
transaction and so uh how 4337 helps
is if your user has a 4337 account or if
your user has this batching property
which will be possible with 7702
whenever the 7702 hard for comes as well
the solver can just fund the user with
the money that they want on the target
chain and execute the transaction on
their behalf the user does not have to
basically ex the user does not need to
be responsible for the ex for executing
the transaction itself and
so um it has many other interesting
properties as well such as dos
resistance so like you always have a
mempool which is decentralized where
transactions you can just just leave
transactions and they will eventually be
executed on chain uh but I think in from
a point of view of the chain abstraction
Vision this message.
sender property is
is a is a pretty interesting
um the second one which is like we are
still in the permission layer we are
still in
how uh like what are the properties that
you give to your account basically
uh over time people sort of figured out
that we cannot create new accounts with
new properties every time we want to do
something new we wanted some way of
basically installing programs into your
account uh into your account so similar
to how if you have like a phone or if
you have your laptop you install
applications into these Hardware devices
you can basically install modules into
your account and get properties um like
the another clean thing about uh this
modular smart contract design is someone
can just B basically create one module
make it public get it audited and
everyone in the ecosystem can basically
just install it and and uh and get those
properties um any questions till
now no um so like there are three main
modules that are available one is the
validator module where you can basically
install uh you can install these
validator modules and the only thing
that the validator module does is
basically check
things before an execution happens the
second thing is the execution module
which actually uh changes state on chain
and then there are pre and post hooks
where you can you can do some
conditioning before and after uh an
execution module there are two different
versions of it like one is gaining more
momentum compared to other but both try
to solve the same problem which is how
do you create this communication layer
between an account and installable
installable um functions
um the second type of erc's are on
permissioning so imagine imagine you
have your Google account and you are
able to permission applications so
whenever you connect your Google account
via SSO let's talk only about web2 world
like whenever you connect your Google
account via SSO to another application
you are basically giving them
permissions to do something with your
Google account
permissioning standards or permissioning
erc's are similar like that where you
can basically give permissions of your
account to some other application and so
there are quite a few applications
already that are live which sort of uh
give session keys to the application so
if you if anyone has used hyper liquid
then the thing that they do is uh you go
over there they attach they attach some
session key uh maybe I think in the
browser context or in their back
and so you don't actually you just sign
once when you log in and after that you
don't sign anything you just click a
button and the session key behind that
who is responsible for executing or
generating call data and making sure
everything is valid um um executes or
generates the call data and sign stuff
for you so there's no there's no there's
no like there's no metamask popup like
the only only time there's a metamask
popup is when you when you log in and uh
after that there's a session key that
gets attached to the app and then um
then everything happens either on the
browser on the back end I'm not I'm not
exactly sure so there are these two
erc's that handle that um I don't know
which one will G gain uh momentum over
time but yeah there's this um these are
influx the good thing that the these
also touch upon this ux versus agency
tradeoff that I talked about earlier on
the on the permissioning layer so like
if you don't want the user to be
troubled by like a new popup every time
you want them to do something you can
and add a session key to their account
and then it will be just like a click
off a button and you can you can
generate uh multiple signatures or
multiple transactions just because they
have clicked something uh
once there is another one which I I sort
of like which is merized signatures it
is not a standard yet but so imagine a
world where again let's take the example
where you have funds on three different
chains and you you want to get the funds
on some Target chain the thing that
you'll have to do is basically sign four
transactions withdrawing funds from
those three different chains and
executing the call data on the fourth
chain if you have something like merized
transactions then uh you just sign once
like your metamask just pops up once and
all those for transactions are uh in
some in some sort of a hashed format and
you just sign once and it's like a
oneclick signature experience that
signature is valid across all the four
domains but it will only be executed at
the particular chain ID that that that
it has instruction on so you can really
give the user this one one click
experience uh without popping making
four different popups every time um for
every every different domain
um okay so that was all about permission
layer erc's let's let's look at like the
interface between between the DAP and
the permission layer um any questions
till
now yes
yeah it's not I think it's on B economy
docs it's not uh yeah yeah it's not uh
there's no ERC for it but it's just
something that I like so that because
like you can using that you can
basically do one click sign four
different transactions all those four
different transactions are just valid on
their particular domains and so you
carry that information on chain but the
execution only happens for that
particular that particular chain ID
um so in the in the permission layer
like just to recap on the permission
layer context we looked at four
different types of ercs that are in flux
that will smooth the that will smoothen
this ux versus agency trade-off one is
on 4337 it gives you this message.
sender property so that the user does
not need to have funds the user does not
need to execute the transaction on the
target chain the solver or some other
third party or even the DAP can do it
for them uh the second is is um how do
you modularize how you add more
properties to your account and once you
unlock that you can add like session
Keys you can add these uh merli
signature type things and you can you
don't even need to write any of these
anymore like people have uh written
these smart contracts and got them
audited and you just need to install
them in your uh in your account if it
follows uh the
standard um okay let's let's look at how
the DAP should communicate with the
permission
layer so this is another thing which is
in flux there's no ERC for it yet but
one end state if you want to have like
the United block spaces of ethereum
is you need like the transfer should as
the bridge should be as easy as a
transfer so right now it's like a very
very buggy experience I just showed you
how like when a user is trying to move
funds from one domain to another they
have 50 different options and they need
to choose between uh speed and cost but
um one thing that you can do and it
still uh I don't know the exact
specifics where it will land but at the
end of the day this is what an address
will look
like uh so it will have your normal
address hash and then some information
of the chain and then every chain would
have to register some sort of an enss
domain that domain will have all the
metadata that you need that the wallet
would need to basically uh unfurl where
I should send the funds and that is how
you would um you would be basically like
pasting pasting the desired address of
user um the other thing that that appap
needs to do is even just figure out what
is the user address in in cases where
you have Smart contract accounts or
different types of authentication
mechanism it is not very easy to figure
out what is the what is the address of
the user and so this is one way in which
uh the DB can communicate to the wallet
saying hey just give me the smart
contract address sometimes even on the
user might have different addresses on
different chain IDs and this is one way
to basically request um what uh what is
like what are the what are the available
addresses for for the user on all
different chain IDs and then construct
the call data according to
that
um another interesting thing that is
happening on this between this dap and
permission layer is there are these
session scoped um eips or ERC that are
being formed which is the DAP can
maintain a session with the wallet and
only request certain scoped properties
so it can maybe only request I can read
your balances it can only request I can
execute some transaction it can only
request I can change some some
properties on certain chain IDs and so
similar to how you have uh whenever you
basically authenticate bya whenever you
login via Google SSO or or Facebook SSO
you define some scope properties that
these apps can can unlock
um there are these four e there are
these four C IPS is what people call
like chain agnostic IPS that uh give
these session properties so you can
either create a session revoke a session
change a session or or even like if
there's a session that is active just
get a session very similar to how um
like a Dap in the web2 world will will
interact with your your Google or
Facebook uh backend
servers um another interesting ERC or
EIP uh is this one called badged calls
or badged transactions so it creates so
suppose in a multi-chain world or a
multi yeah multi-chain world what you
would want is to execute something on
the target chain you might want four
different things to happen one after the
other either four different user
operations four different transactions
um and this is the way how dap can tell
to the wallet that hey I want these four
or five different transactions can you
execute them in
batch uh
and instead of just sending one
particular transaction waiting for
execution and then sending the another
one you can just send a batch of
transactions to your wallet and if it is
a smart contract wallet the wallet can
execute it in in in in the same
transaction it will it will execute
those user Ops or even if it is
um uh like uh you can even send
instructions to execute multiple user
Ops or multiple transactions on
different chains and so this is how you
do like badged transactions in um
between U dap and wallet another
interesting uh property it has is this
get capabilities features so a lot of
the stuff that is driving these sort of
some some of these ercs between the DAP
and the permission layer is the idea
that you should have Smart wallets but
Dumber Dum dumb apps so the app should
only care about uh what call data I need
to execute what is like the Slick ux
that the user wants
but um but the wallet should care about
all the other intricacies of how how I
need to bring the amount or how do I
need to bring the assets to the to the
Final
Destination
um this one is this one is a combination
of the scope and the and the and the
call that you want to execute uh another
interesting one is so right now the daps
need to basically get a list have a
sense of what assets the user has and
then qu query them with their with their
uh note provider so like okay does the
user have usdc does the user have this
does the user have that and then just
query them um this basically gives the
responsibility to the wallet and so uh
uh dap can just basically
query uh okay for this address what are
the assets can you just give me all the
assets or can you give me these these
these assets and these these balances
and so all that job that the DAP was
doing to basically fetch balances is not
is is is offloaded to the wallet and
only the wallet is doing that job
um I think this is like because a lot of
this work is repeated across both daps
and wallets I think this is a pretty
powerful um ERC it
yeah uh I'm not sure I think only rc20
for now I I can get back to you but I
think only rc2 for
now
um any any other
questions no
yes can you use the mention that we
already have a execute badge function
right in the ERC 437 is it using uh EIP
execute user Ops one after the other in
the same transaction 4337 so it gives
the your account that property that it
can execute these things in the same
transaction 5792 is only about between
the DAP and wallet saying I want these
things to be H to happen and then the
wallet wallet needs to figure out if it
is a 4337 account then it can do it in
the same transaction or if it is anoa
account then it needs to do it one after
the other and
so and and what about like cross chains
like if I have let's say for example gas
fee I don't have a fund on a particular
chain yes but I want to do some
transaction then how do do do we have to
separately communicate between different
chains for this uh even that is like the
wallets responsibility the daap just
says these are the things you need to
execute please execute them there is
also like a flag where you can specify
if these things can happen in parallel
or they need to happen sequentially and
so that is how you can do some of the
some of the Cross chain thank
you um the next set of erc's are between
the permission layer and the solver
layer so how does how does your wallet
communicate to the mempo layer or the
solver layer that please do this uh um
so the wallet has
converted the instruction that is coming
from the DAP into some sort
of um signed message that the blockchain
should understand it can be like a
intent or it can be a user op it can be
a transaction uh like an eoa transaction
but yeah like by this point at the end
of the permission layer the wallet has
signed something for you one way I think
the distinction between applications and
and wallets is applications generate the
call data or instruction and then
wallets are responsible to sign them and
convert them into a language that the
blockchain can understand
um um yeah so one one thing which is uh
sort of popping up uh is this intent
framework um let me just take a sip of
water any any questions in between
cool
so when you are trying to communicate
between two chains you can either
communicate you can either send tokens
transfer balances or you can basically
send information or send messages across
and uh if you look at the things that
that an account has it either has
balances so things that are fungible
assets or things that are fungible and
then it has some sort of like
authentication Scopes that are attached
to it like a multisig address or a
session key or some some other property
or a policy and so when you are in a
cross-chain world when you are in a
world where there are different domains
you need to sort
of sync up that the sync up the
authentication scope all the time but
maybe send the balances at at exec time
do do you have a question no okay um so
this one is about moving assets across
chain one interesting property when
you're trying to move assets across
chain is because assets are fungible you
can basically pay a solver or pay a
sophisticated third party to uh just
move their those assets instantaneously
and so this is why you have these solver
or intent type of Frameworks that have
that have emerged where you have a
sophisticated third party who takes some
money
and gives you this PD this PD execution
um but when you're trying to move
messages around you cannot you cannot
have loss it cannot it cannot be lossy
when you're trying to move messages
around and you're trying to basically
maybe vote Yes in a governance vote you
cannot vote a maybe it it has to be it
has to be a yes and so when you're
trying to move assets there can be some
loss associated with it uh if the users
are happy with it but when you're trying
to move messages it has to be it has to
use the most secure pathway to to move
it around and so this is uh this is just
a standard to move assets
around uh and this is you can think of
it as like a cross-chain limit order
saying I want to give these these these
assets on the input side can you just
give me this asset on the output side
and then it's the responsibility of the
solver Network to figure out uh which
solver to use what fees to charge all
all the all the minute details but this
is how the wallet can communicate with
the solver layer
about this is the this is can you move
these assets for me and and get me these
assets at the at the um Target
chain um there's another thing that we
have sort we have been working on which
are resource locks um and so if you
think about a cross-chain transaction
there are three things that happen in a
cross chain transaction one is you need
to send a message on the origin
chain then the second step is someone on
the origin chain or someone on the
target chain is waiting for finality so
you send a message or send a transaction
On the Origin chain either to a bridge
contract either to a solver Network and
someone on the other side on the on the
on the target chain is just waiting for
finality or waiting for inclusion on
this first message and once they are
happy that they will get the money they
can execute they can execute the
transaction and so this is like this
three-step process very synchronous one
two and three that happens which causes
this like long delay
in in in moving things around and this
is also how like like centralized
exchanges work basically you send money
to their escrow they wait for certain
number of blocks and then they can debit
you the money this is what you need to
do to basically uh guarantee
equivocation protection between uh
between two
databases um we are working on this
thing called resource locks where you
can convert the synchronous process into
asynchronous process and so
if you are able to come tell to the
solver layer by whatever means you can
attach this lock on an account level you
can attach this lock on a token level if
you are able to communicate to the
solver layer that you will eventually
get paid don't worry about it just pay
the user right now you can convert this
three-step process into like a very
quick like instantaneous process for the
user and that's how you are able to move
um assets uh instantaneously uh across
chains it has like an initial bump of
actually users depositing funds into a
lock but once this lock is enabled you
can uh get instantaneous
execution uh I can show you a demo of
how this
works so the so the idea is that you
should be able to move funds cross chain
faster than you can move the funds on
the same chain even and so that is the
hopefully this demo Works uh whenever I
really want to make it work it does not
work but uh um so so just to give you
like a recap this is like the rapper
contract where user so similar to how
you have rapde you can have a rapper
version of the contract where users just
deposit funds and similar to how when
you deposit into W you can use it on all
the different uh daps like unisoft or a
uh something similar you when you
deposit into this rapper contract you
can instant mously move These funds
across across any domain so this is a
rapper
contract uh and this is my address on
arbitrum let's just let's just move so I
have already wrapped some some funds
let's just move a small amount of money
uh and what will happen
is uh it will pop up like a simple
permit to Signature message that I just
need to
sign and uh as soon as I've signed I
have Bas I have basically sending to the
solver the transaction so I was I moved
money from Main net to arbitrum and it
took uh like 2.9 seconds and if I
just um if you look the transaction on
the main net is still pending but the
transaction on arbitrum has already
happened I already got the money and
this is happening because you can do
this like asynchronous communication
between two chains and you basically get
this you if you unlock something like
this you basically get the speeds of
Solana across the whole evm block space
um this is live anyone can use it uh
just test it out uh but you can
yeah there's NOC yet there's NOC yet
just so how did you do uh we did not we
are writing an ERC but uh it's just like
a quick
demo the contracts are public uh it's
like a rapper contract which just so the
so the main question is can the user
revoke this transaction or not if the
user can revoke this transaction then
the user has double spent and the solver
has not received the money that they
paid
instantaneously um the way this works is
you when the user deposits into this
account or into this token they are
voluntarily opting into a Time logged
withdrawal so they can withdraw the
funds permissionless only after some
time lock period but uh but it's still
pending so it's not really I think it is
it should be finalized by now yeah it's
finalized now so the the solver has
received the
money but like when you say 2 second
that's even less than the The Source
chain confirmation time yes and who are
party like can anyone do it permission
LLY or are you do you have some so right
now it's it's being it's in a permission
setting like Peter from relay is sitting
over there who's doing it uh he was he
was waiting for the money he was waiting
for the money but he paed it up front uh
but eventually like you can also you can
also encode it uh permissionless but you
can you you just said you can cancel
right like because it's you cannot
cancel you cannot cancel you cannot
cancel even though it's pending yes
because you have uh you have locked the
the funds with that account or with that
token contract and the only way you can
cancel it is if you unwrap those
funds and relay is account sorry who put
the money the user the user voluntarily
put the money into before this happened
yes so before before user put some
amount of ease then they put the brid
instruction uh so let me let me take a
step
back so over here if you think about
what is happening
at transaction time user is paying this
this cost of finality or
inclusion but with the resource lock the
user Because by the act of depositing
has already paid that cost initially
when when so whenever the user
deposits we wait for certain number of
times to save ourselves for reorgs and
then uh we can say that there's no risk
to the solver if the user will like you
will eventually get the fund
but what happened to the brand new user
who just want to bridge something from a
to one it sounds like you have to do
some set up job to pre-allocate the one
so that when people do next time it's
faster but if it's a f time experience
it is not okay okay yeah so yeah you
need to top it up initially and only
then you get the the speed otherwise you
don't get the speed bump there's there's
another question at the back oh I was
going to say can you talk a little bit
about Capital efficiency okay and like
the reality is you've got to lock up the
assets first are you planning to put it
um you know the methods that you need
into say R teeth or something else so
that you don't have to hold you know one
balance eth or you know state teth that
kind of thing yeah that's a good
question so there are like there are
different places where you can put the
lock you can have a lock in this like in
a in a module so we we looked at some of
the valid like erc's where you can put a
lock uh where you can put where you can
codee different things in the mod itself
so you can either put the lock on your
account level and so whenever you
receive the funds the funds are logged
itself after some time or you can uh put
it on a token and so whenever so
whenever you wrap it you basically log
them um but yeah there is this initial
friction and so if if the user has not
logged it it will it will go through it
will go through this path if the user
has logged it it will go through this
part
yes first there and
then thank you uh so this sort of lock
is similar to how nois pay Works in a
way so that if I as a user want to move
money out I have to know wait a certain
time before so it's a two times
transaction I I say I want to do that
and then I can move money out yeah yeah
yeah so uh there are other things that
also like if you look at this there's
not something new this has been tried
before by different people they just
don't they just not named it but there
was gnosis P who was doing it so when
you are so you need to do something like
this when you need to put a card on your
onchain balance
because uh visar Master Card wants like
instantaneous uh guarantee but onchain
it might take some time or it might also
be reared and so you need to put some
locks in your account level so gnosis
has put some locks on the account level
to enable their uh their card feature
I'm sure any other wallet who has their
own card needs to put something like
this because uh because visa and
MasterCard won't wait for 12 seconds or
or some finality guarantees there are
there's also this thing by coinbase
called Magic spend where you have funds
in your where you have funds in your
like coinbase uh centralized exchange
and you want to execute them or use them
on chain at transaction time uh they
have a lock as well the lock is on the
centralized database so wherever is the
source chain whereever is the source
chain you need to have some to get like
the snappy uh 3 second and it took 3
seconds because it's a demo like the our
indexers are slow but it ideally it
should take you should just sign the
message and it should take the time of
the target chain the target chain block
time is is the only thing that that
should
determine um any questions
yes yeah
um do you provide the source code on
GitHub so we can dig a little more
in the one one if example it's not uh I
will make it public but the code is the
code is there in the the code is open
source so you can
just um so the smart contract but um I
assume on the UI there is a bit of uh
wrapping and
offchain oh yeah pack so I would like to
read into it as well got it there is I
maybe you have plans to publish it on
your GitHub there are some docs uh I'll
at the end of the slid I I'll share the
link to the docs but you can go to docs.
one balance.
I think and you should find
all the docs which docs
uh doc uh okay thanks a lot dos
one got it thank
you yes so these These are the documents
you can
just how do you handle reorgs on the
source or the ination chain so
because um the funds are logged even if
there's a reor you can just replay the
transaction and the solver will get the
funds can it cause a double spend in any
way uh I don't think so because like uh
whoever is providing there is there is
some like entity that is at the end of
the day what you're what you're trying
to do is solve for double spending
because you want the user to get the
money first and then give the money to
the bridge or the
solver um and so effectively whatever
this thing is doing is solving for
double spending and the way this solves
for double spending is make sure okay
this transaction goes first then this
transaction goes first then this transa
another way to look at it is it's like a
account level sequencer or a token level
sequencer
which is just trying to sequence
transactions one after the other so that
there's no double
spin yes but you execute transaction on
one chain and then on another reorg
might
invalidate one of them so the reorg
might invalid so suppose a user signs a
message like a 712 message send this
much money to this
address um first time transaction
happens then there's a reorg whoever is
the pay Mar Master can execute that
transaction again and give the solver
the money again because the funds are
logged uh because the resources are
logged the user cannot remove those
funds and so in the in the Locking
contract you need to be sure that there
is enough
time uh that even if there's a reor you
can the pay Master can replay the
transaction but uh yeah so the that is
the only thing that you need to make
sure otherwise uh the solver will always
get paid and how much time is this
uh I think in this demo it's 24 hours
but ideally it should be as long as you
are sure that you can get the
transaction included even if there is
some some sort of censorship or
reog thank
you yeah moral is the same uh question
sorry I have to reiterate so the input
transaction um uh the user is supposed
to to sub UT transaction On the Origin
chain right but at the same time uh you
send it to the solver assigned draw
transaction for the case that the input
transaction On the Origin chain gets
Reed so the solver can resubmit it any
time um herself but uh how do you deal
with nones for example you could
invalidate the the nons with another
transaction and then it doesn't help
that the funds are locked you cannot use
that sign transaction anymore that's uh
that's that's a good question so at
least on the token level uh since it's
just using permit to um the nons are not
uh sequential and even on the account
abstraction level in 4337 you can have
parallel nones so got it so so you
actually do not share the signed raw
transaction you share a signature um and
and that signature you can use in any
transaction submitted by anyone actually
yeah a user op or permit to or just
signed signatures anyone can bring them
on chain makes sense yeah and ideally
it's in the best interest for the solver
to bring the source chain transaction on
chain because they've already paid on
the target chain and even if there's a
gas Pike they they want they'll try to
get as much money as they can so even if
there's a gas Pike they'll keep on like
bumping up the gas and uh make sure that
that they get the money that uh that
they paid
for um any other questions yes
our solvers are permissionless so anyone
can become or our solvers are
permissionless anyone can become a
solver or they've at least it somehow uh
in the demo uh not yet but ideally yeah
you can you can have a permissionless
solver
okay um okay
so this was how you Comm how like the
wallet communicates with the solver l to
get some
properties uh either how you transfer
value or how you get this instantaneous
crossin
ux
um now once uh now once the solver has
done that stuff how do you validate or
how do you actually validate if
something has happened on the target
chain so suppose in the case of 7683 the
user has just signed a message saying I
want this much money the solver
pays the money but how do you make sure
that the solver actually gets paid or if
the solver does not pay the user on the
target chain how do you make sure that
the user gets back their funds uh this
is what this is what uh you sort of try
to do in in between these two layers of
kick there are two
standards one is just like a message
passing so if if you guys remember I
told you like there are two types of
messages or two types of things that you
need to move across chain one is tokens
or fungible assets and if you're moving
tokens the user can
basically take a price card take some LW
uh and get this faster speed or you are
trying to pass messages across and so
this is this is one standard to move
messages across like
bytes uh and then there is another one
to actually burn and mint uh tokens
across chains so
there are two different standards one is
by optimism super chain I think the 7802
is by optimism super chain and then 7281
is by a bunch of different like Bridge
providers it was called xcc2 before but
the the core concept is that a token can
assign a bridge to become uh a burn and
mint Bridge basically so we when we look
at the solver type of a transfer between
chains there can be some loss but in a
burn and mint Bridge um there is sort of
no loss you can you can just it's it's
as good as a transfer it's effectively
yeah it's if even if you look at the
code it looks like it's very it looks
very much like how the erc20 transfer um
gets is executed and the token basically
trusts uh burn and mint Bridge saying
that okay uh verify or validate that the
burn has happened just mint me the
equivalent amount of tokens on the
target chain so very uh uh Costless way
of moving assets that's all I have for
you guys this is some some Shameless
publication publicity for what we do but
uh we have two different products one is
like the chain abstraction tool kit so
if you're a Dap and you want to uh just
get all these properties of just you
just need to care about what is the
effective balance on the target chain
and this is the call data I want to
execute just make sure it happens then
that this is your this is the product
that you would want and then on the
second side we have another product that
will that is that we're working on which
is the resource locks as a service so if
you want this uh one token is just one
representation of it but then there'll
be more modules that we build on top of
it and so yeah that's
the uh that's the other product thanks a
lot any questions
there's one question
there there's one question over there at
the back or no
more none oh there is one just asking if
you could upload the slides cuz it was a
lot I got almost everything but not all
of them where should I send it sorry
Twitter I yeah I'll post it on Twitter
uh if uh I am anit chunar on Twitter and
telegram feel free to DM me if you need
anything thank you
there's another question somewhere there
right or or no maybe not um also I can
see that a few people did submit
questions through mircat the the one
that got an upload was how to support
Sal and
BTC
um I think effectively it's the same
thing you just don't have like ercs
there uh at least the good thing about
uh evm ecosystem is you can have the
same sort of language but a lot of the
stuff that we talked about will have to
be changed a little bit for these
ecosystems um but you can at least from
a like a resource lock perspective you
can put a lock over there as well and
you can instantaneously move you can
even instantaneously move Bitcoin from
just at at a click of a button to
another
chain but there's like a lot of
um other stuff that you need all the
different trcs that we talked about that
need to be talked with these different
ecosystems as well and I don't know who
is do doing it we are not doing it I
don't know if anyone else is doing
it another one is um is EIP 337 already
a standard for change specific addresses
like base ZX ABC blah blah what sax is
using uh yes it is uh but there's a
different one um there the the main
I think the main thing is like any any
chain can call itself base and so how do
you know what is the chain ID of the
base any chain can have the same CH
chain ID as well and so with with this
chain specific address like if you use
enss then
you there is like a way to actually hold
that metadata on yourself and the other
thing with that proposed ERC is it will
be permissionless so a wallet can
basically just run a light client and
and be able to get the metadata from
that from that ens
ID then we got a question how can a user
ignore the chain aren't different chains
uh with different security and
performance
properties
um there's a trade-off like some users
won't ignore chains some users will like
it happens right now as well like uh
some users are like I'll only hold
Bitcoin some users are like I'll only
hold eth some users want to trade meme
coins and this is
just like a ux makeup on top of
different properties that chains might
have some users will care about it some
users won't care about it and so if you
are a Dap that wants to Target the type
of users that don't care about it then
then then use this if you are a Dap that
um is very specific about no like the
user uh should have all the context uh
when they're trying to ex execute
something like this then then um the
normal path is also
available and the final question we have
here is how would wallets be deployed
into different chains for initial
setup
um there are different ways so um at
least on deployment I think one thing
one more interesting property that you
get with 4337 is you get this
deterministic address and you don't need
to deploy
uh you don't need to deploy your account
uh even when you're receiving funds on
any chain so you can just let the user
receive the funds and only when the user
is trying to transact something that you
can that you can deploy the code of the
account and then um do the so it it has
these nice like civil resistant
properties as well uh that is one way
there's another thing that if the user
changes their multisig on one uh chain
how do you sync up it's like it's a
different Rabbit Hole in itself there's
key store rollups there are l1s load
there's a bunch of other things we have
not even touched about that over here
but yeah that's a different Rabbit Hole
altogether all right that's all the
questions we've got through mircat are
there any final questions from the
audience just
spontaneously yes can can can you wait
for the mic so that everyone can hear
you um from the ux perspective how long
do you think it's going to take for us
to be at a point where users and normies
don't have to think about gas bridging
and chains like are we two years away
year away five
years uh you can use these two apps they
are already in uh that there is like
there are a bunch of apps that are
already in production users don't need
to care about gas
chains um bridging
anything okay so yeah at the end of the
slides there are two apps that I link
they just abstracted away and if you're
a dab developer today who wants to get
this like Snappy ux who wants to uh tap
into all the different um users who are
on all the different domains then then
then you can use these
things guess the answer is the future is
now yeah future yeah future was
yesterday cool thank you lovely anyone
else
if not let's give it up again for anit
for this lovely
Workshop thank
you and that my friends concludes the
program on the stage thank you so much
for being here hope you enjoy the
closing ceremony enjoy Bangkok enjoy
your life thank you so much bye
out there sh
back o
back back
