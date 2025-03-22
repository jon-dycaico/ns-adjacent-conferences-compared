what to build on what makes them
different um and so I think probably the
first thing you've probably heard of is
optimistic versus ZK rollups right so I
think the thing to note specifically
again we talk about data availability
when we impose that back data back to
ethereum how do we prove it's true right
so there are two approaches optimistic
Roll-Ups came first what they do is
optimistically assume that data is valid
so they Implement something called fraud
proofs what this means actually is when
we do something called withdrawals so
withdra being bringing like eth from the
L2 back to the L1 they have to implement
something called a challenge period so a
challenge period is 7 Days basically
where it's locked up and gives the
community to opportunity to essentially
dispute the transaction and so what that
looks like is it say hey I want to
dispute that within the seven days and
then we will submit a fraud proof
validate that fraud proof and then if
it's good then we're good to go for bad
then oh no you know um the downsides of
this right is of few things right it
requires at least one honest node so
obviously there has to be a good person
I guess going through and doing the
fraud proofs the other thing is this
needs to post all the transaction data
back to the L1 right because what it
does needs to do is like recreate the
history of everything going on um so
that is something I will touch upon when
we talk about ZK rollups right so ZK
Roll-Ups was kind of the next phase of
rollup architecture um this is when we
think about okay rather than
optimistically assume let's actually
submit something called a validity proof
upon submission of that data back to
ethereum and so what this does is allows
us to like create mathematical
guarantees around validity um creating
safer trust assumption security
guarantees as well as when I talked
about finality before with the challenge
period you don't have to do that right
you can submit it and then it's verified
immediately um I think there are a few
things I want to note here that I get a
lot of misconcep itions about ZK which
we'll dive into a little bit later right
is very popularly known as something we
use in privacy with regards to rollup
specifically depending on the ZK rollup
privacy is not necessarily guaranteed so
the use case of ZK proofs in this
situation is posting that proof back to
ethereum is expensive right every time
we interact with ethereum that is
expensive so we want to bring the
smallest type of proof back and it just
so happens because ZK proofs have the
property of not having all the
information revealed as part of that is
kind of the most uh what do you call it
uh smallest proof that's not correct
English grammar but you get me right um
to be put back so the uh last thing
about that too right is like we only
need to post like transition state data
back to the L1 rather than everything as
compared to optimistic rollups um so
some examples you might know I put up
logos Scrolls EK sync you might know um
what's it called Linea polygon Z km um
lots of interesting players in the space
let's go a step deeper okay we've
covered the optimistic Roll-Ups we've
covered the ZK Roll-Ups but let's
actually differentiate within the ZK
rollup itself right how do we start
thinking in that design space uh so the
first thing I need to talk about is the
ZK evm so essentially what you can think
of a ZK evm as is like a magical
computer that allows us to execute evm
code so you can write solidity smart
contract
but also allows us to kind of translate
that into something that is provable
right because ZK proofs are math and how
do you turn code into math I'm not
entirely sure ask our researchers and
Engineers but that's um what a zkm
essentially allows you to do this is
incredibly difficult to do just based on
how the evm was built which has given
rise to four different types of ZK EVMS
so this is kind of where we start
talking about okay how did the ZK
rollups differentiate themselves from
each other so at a high level type four
is going to be something that we call
High language level equivalent but not
bite code equivalent so an example would
be like a stark net or a ZK sync what
this means for developers specifically
is you can write in solidity but your
tools will have to change to an extent
right because it's not to kind of
understand the information type three
I'm going to gloss over as sort of the
transitionary period to type two which
is kind of the next stage I put a frog
there because I like this one um but
anyways this is a highle language
equivalent so this the same thing you
can write in solidity you can write in
Viper Etc but it is bug in Viper that
caused a hack right and the problem was
not in the Viper code itself but
actually in the compiler right so if you
map that same Paradigm to ZK EVMS right
you can kind of audit all the smart
contract code but there's a lot stronger
at least in my opinion of a security
guarantee when at the lower level you
don't have that overhead of thinking how
it's different as well so that's type
two type one is kind of fully ethereum
equivalent so so again like I said uh
highle language equivalent ethereum
equivalent meaning um you can write in
solidity tools don't change um and
there's some little tweaks about like
data and hashing that makes it the same
but anyways the point of like also why
you would choose different ZK EVMS is
basically like I said in the beginning
EVMS or ZK EVMS are really hard to build
right so something like a stark net and
ZK sync took the I guess stance of like
you know evm is not perfect let's
actually change it a little bit um in
order to get certain vantages like maybe
it's faster maybe we have native account
abstraction built in versus maybe
protocols more like scroll or Linea
where we talk about no we want to
maintain faithfulness to the evm because
that's where the community is it just
smooth the developer experience things
like that um everyone's super cracked
and super smart so I'm not going to say
one is better than the other but I think
something to think about as devs when
you're comparing the landscape um other
things to think about because we love
numbers when we talk about rollups um is
the different stages so stages was
something that was defined by L2 beat um
if you guys aren't familiar l2b is a
really great resource to look up like I
guess rollup information that tells you
about like different security guarantees
um like their activity and stuff like
that um they Define three different
stages of rollup so again when you're
thinking about the layer 2 landscape
there's different um I guess what we
call training wheels that we have as the
technology progresses over time right so
stage zero is where I would say most of
the rollups operate right now um the
most important thing to think about
there is pretty much like the operators
are centralized um so operators being
like sequencers you might have you might
hear that phrase a lot centralized
sequencer right um the source code is
available for you to reconstruct State
stage one is kind of the next step right
how do we let go of those trading Wheels
a little bit more um so then that's when
we bring in smart contract governance
this is when we introduce something
called a security Council right so
Security Council is like a group of
people who are going to basically
arbitrate whether or not an upgrade
might be made things like that there are
specific requirements about like some of
the security Council people should be on
the team itself and some should be
external as well right and stage two is
like woohoo no we're completely training
wheels off it's fully managed my smart
contracts proof system is permissionless
Security Council is only there to
basically um handle like upgrades uh or
sorry not upgrades soundness areas so if
there's a bug like creating an uh Avenue
to basically say okay are we going to
upgrade this making sure we have an a a
a good amount of time for users to exit
if they don't want to be part of that
upgrade but also another kind of design
space to think about when you're looking
at the L2
landscape um and so to kind of summarize
everything that we've talked about
there's a lot of trade-offs that fit
everywhere here um at the at the highest
level I wrote as by highest level I mean
it's the first bullet point uh finality
is what I was talking about when you
think about challenge periods um in
optimistic versus ZK Roll-Ups that might
be something you think about when it
comes to liquidity fragmentation stuff
like that um I'm going to anticipate a
question uh in case somebody might ask
like oh wait when I when I withdraw from
like an optimism to ethereum it feels
instant I don't understand where's that
challenge period coming in um so just to
address that point specifically you
might think about bridges like third
party Bridges basically having separate
liquidity pools to allow you to give
that feeling um as we all know bridges
are the most like hacked space in the
kind of ecosystem right now but you know
I mean there's a lot of strong
guarantees that are happening that I'm
not a bridge builder so ask somebody
else about it but anyways last piece uh
second piece right like I said again
security guarantees and Trust
assumptions so whether or not you're
optimistically like waiting for a fraud
proof versus saying I'm going to submit
a proof on um submission yeah validity
proofs uh and to that extent thinking
about throughput cost again there's a
lot of different implementations that
have trade-offs maybe if you're building
a game you might want something that is
uh faster and cheaper with fewer
security guarantees than a different
type of app um developer experience so
this is a trade-off when I was talking
specifically about the different types
of ZK EVMS and what you're willing to
kind of um I guess appetize not what
what you have appetite for um
decentralization
soft Source software community so this
is kind of when you get into the ecos
side ecosystem side of things so how
much do you care about those parameters
um and like I said again Network effects
so that not only affects like how
connected are you to ethereum for
example but in your ecosystem itself if
you are a builder um what other builders
can you interact with like kind of
additive things so that is rollups at a
very high level I'm gonna scare you guys
a bit rollups are not the end game they
can still be very expensive um why so
like I said um oh I heard some Chuckles
let's look at this again uh but
anyways U let's let's let's dive into
maybe something that is a bit more of a
current event right so like I said when
I talked about data availability that's
putting data back on ethereum but what
do we remember about ethereum every time
you interact with it it is very
expensive so how do we get around that
right so this is something called EIP
sometime this year um which essentially
created something called blobs right so
blobs are a separate type of data
structure than what was traditionally
known as call data so before you would
post information to something called
call data and call data is permanent and
there forever right the thing about
rollup data right is you're really only
posting it there for like verification
so it doesn't need to be there forever
right so blobs are actually an ephemeral
type of data storage it will like go
away I think after 18 days um I'm not
the most current on that exact number
but essentially what that does is allow
us to use a different type of space the
other thing that is really cool about
this as well is it is a separate fee
market so when it comes to competing for
like I guess data on ethereum blobs are
completely separate space so what that
looks like or means for rollups is you
are not as exposed to the fluctuations
in the market on ethereum versus in call
data versus blob space so um I guess the
result is this is actually still not the
most perfect solution that's when you
might start hearing things about like
sharding dang sharding things in the
future of the theorum protocol but just
think of this as again a highle primer
on what you can expect for the rest of
Devcon um so other things that I just
want to kind of say uh to put words in
your head um is there are uh what do you
call other scaling solutions that have
kind of produced or cre been created so
you might hear something called a
validium so a validium is basically a
chain that does like offchain
computation proves via validity proofs
but they use offchain da so another kind
of buzzword to think about is now we're
talking about data availability layers I
don't work for these companies so I
can't go too deep into them but if you
want to investigate Igan da Celestia
Avail or kind of the new design space
you might think of there um and optimium
I forgot and I is basically optimistic
rollup plus offchain DM da and then the
last one is going to be called a
volition so volition is essentially the
marriage of a validium and a ZK rollup
where you can kind of switch between
whether or not you want to do onchain da
versus offchain um if you're looking for
specific examples again head to L2
beat.com it'll actually list a bunch of
different projects in the space and also
what they
are okay cool um I don't know how much
time I have left I figured I would be
talking for a long time so
ah ah okay my backpack is back there I
have swag for somebody who shouts out
the answer here what the okay which type
of zkm is bite code compatible
ABCD okay those are all numbers and not
letters I don't know the answer is H
everyone is right or not everyone is
right I guess but um okay this didn't
work out as well as I thought I I did
not think there would be this many
people here but thank you for for
participating okay let's move on let's
talk about zero knowledge okay so this
is some knowledge about zero knowledge
um basically at a high level right zero
knowledge proofs allow for a prover so a
person to prove to another person the
verifier that they know something
without revealing the information itself
right so what does that mean
specifically so when it comes to ZK
proofs there are three main properties
we think about completeness of the proof
so that means if the prover knows the
information they can convince the
verifier with their proof soundness
means if the prover doesn't know the
information they can't trick the
verifier and then zero knowledge is like
I guess pretty self-explanatory the
prover doesn't have to reveal any of the
actual information
itself so there are two types of ZK
proofs that we're going to get into
something called interactive proofs so
this is a type of proof that requires
back and forth between the verifier um a
an example that is pretty common you can
just Google
eli5 interactive proofs and this is a
picture you get from chain link
essentially what it is is this example
says okay I have um Bob and Alice and
there is a Magic Door in a cave the
magic door has a magic code that Alice
knows but Bob does not so Alice wants to
prove to Bob hey I know this code but
she doesn't want to tell him he knows
this code right so the process basically
looks like you have path a and path B
into a Magic Door that Bob can't see and
so Alice will randomly choose a path and
then Bob will say come back from path B
and then she'll come back from path B
and he's like come back from path a and
she'll come back from path a so what you
can think of this is if he asks her
enough times and she can consistently
come back in whatever direction that he
wants her to come that means she was
able to cross that magic door and
therefore she also knows what the secret
code is so that's interactive proofs
when we talk about non-interactive
proofs that's B basically saying the
prover can say hey I'm going to give you
one proof or like one piece of
information and the verifier says that's
all I need to know we don't need to
interact past that right so the example
here is about proving that anyone that I
have completed a Sudoku puzzle this is a
little bit more complicated so I'm going
to dive in into it deeper but this is
going to be what we think about when we
talk about ZK rollup space snarks
validity proofs Etc right so the way
this works is actually something called
hashing so hashing is a oneway
transformation of data so that means
like if I say oh I did 1 2 3 4 5 6 7 8 9
I can hash it and give you some like
long string of letters and you won't
know the actual letter but what you do
is you basically hash each cell's number
in the Sudoku puzzle you combine all of
those hashes and commitments for rows
columns grids um I guess I'm just
assuming everyone knows the how sidoku
is played um but maybe you don't so I'll
step back again and also explain how s U
is
played in case you don't know cuz we're
all about starting from the top
essentially sidoku is this grid and what
you need to do is be able to count one
through nine from the top to bottom one
through nine across the rows and one
through nine in each box and there's no
duplicates okay cool we all know what
sidoku is if you take anything away from
this talk I hope you remember that
specific piece um but essentially what
you can do is create all these like
commitments of the different forms of
all the ways you created a zudoku puzzle
and essentially the verifier is able to
use cryptographic algorithms to
understand hey yes everything you sent
me is every row you sent me fulfills the
requirement every column you sent me
fulfills the requirement etc etc but I
don't actually know what the solution is
right so that's how a non-interactive
proof works so now let's actually talk
about snarks versus Stark so maybe this
is also something you've kind of heard
and been like huh what okay um so we'll
we'll dive into it right so snarks are
succinct non-interactive arguments of
knowledge so these are ZK proofs that
are succinct so they're small in size
they're non-interactive so that means
they don't interact with each other like
the prover and verifier um these are
very compact proofs that allow for fast
verification thing to note is they do
require a trusted setup so a trusted
setup is a pre-processing phase that
allows basically creators to create a
public and secret key um for like I
guess the actual proving the secret key
needs to be thrown away so this is kind
of I guess a con of ZK snarks um which
we can talk about a little bit later in
the next slide how do we solve for this
so again another acronym that I heard
and I was like what is this and I'll
just explain it very quickly if you
heard MPC you might hear it later this
is called multi-party comp computation
this is allowing basically a more secure
way of creating those generating those
keys right so rather than just like a
single instance of like public key
private key uh MPC essentially allows
every participant to have a part of a
private key and then work together
without revealing their part of the
private key to create the full one right
so I mean there are trade-offs again
right this doesn't scale really well
when you have a lot of parties um it is
vulnerable to collusion if like there's
um I guess non- good non- good
participants um but I'll I'll give
another example so imagine all these
frogs are pirates and imagine all the
Pirates are looking for the secret
treasure map um so they want to complete
the treasure but they don't want to show
each other what piece of the map they
have so they actually do is they divide
each of their pieces into a bunch of
smaller pieces and give everybody one
part of their smaller piece so no one
knows your complete picture of what your
piece is but at the end of the day
everyone does have every piece necessary
to create the full map so that's NPC in
a nutshell with frogs and Pirates okay
moving on let's forget everything
actually don't forget everything but now
we're going to talk about snar Starks so
Starks stand for a scalable transparent
argument of knowledge so this is
transparent because you don't require a
trusted setup it's also
non-interactive um this is really good
for handling very large complex
computations however the problem with
them is they have larger proof sizes as
compared to snarks and so this is where
we thread again through data
availability right the size of that
proof is very important for when we post
it back to the L1 because if it's bigger
it's more expensive right um so I mean
again these are different kind of ways
that uh rollups have for move forward so
like a starkware handle ZK sharks um
however not All Is Lost um another
interesting design space that I'm just
telling you about that I learned right
is there I guess math is cool because
you can put math on top of math and so
what that looks like in some solutions
is you have a stark which is very good
for computing large complex computations
and then you wrap it you prove that it
was true in a snark which is really good
for making it smaller so an interesting
thing to think about um but anyways at a
glance you can kind of see uh snarks
have a trusted setups Starks doesn't I
put this here um postquantum means
Quantum resistant um basically snarks
right now quantum computers aren't there
yet so please sleep soundly but in the
case that Quantum Computing gets there
snarks aren't necessarily Quantum
resistant Starks will be like I said um
when it comes to developer tooling
Starks are less I guess adopted so there
might be less information in the space
um when we talk about I guess a a ZK or
a starkware for example they use Starks
they have to use a different VM they
have to use different I guess they write
in Cairo for example so super smart team
it is a little bit different if you're
like a solidity Dev moving in um and
then I'm going to move forward hello
yes are
notum uh no no so postquantum I should
have used like the layman's term so
postquantum means uh possibly Quantum
resistance
so what that means is quantum computers
are not at a stage that they can hack
stuff yet or hack snarks right but you
know maybe we get into a world where
that that is the way snarks are created
is something called elliptic curve blah
cryptography I'm not going to explain it
because I'm going to butcher it but
Starks use like random hashing and
basically hashing is going to be Quantum
resistant but uh electop curve
cryptography well that's a mouthful is
not but we're not at the stage yet where
we're thinking about it but yeah cool
good to know I will not write
postquantum anymore because it is
confusing thank you for that in the
front okay another quiz time I put
stretch sesh because I also expected
people would stand up and be like I'm
tired but I guess no one's tired uh oh
nice thank you okay um what does snark
stand
for oh perfect okay I don't have enough
swag for everyone who answered but if
you find me first you will get a
magnet okay moving on we have 30 minutes
left so hopefully we can get through
everything this is where we just get
into current events um things I see on
Twitter that people argue about that
probably don't really matter in real
life but whatever we're here talking
about
it so let's talk about Roll-Ups right I
went over optimistic Roll-Ups I went
over ZK rollups but did you know people
Define more types of rollups let me list
all of them for you that I saw on
Twitter recently Sovereign enshrined
based
modular yes okay cool so let's actually
just go through kind of I have like a
slide for each we're going to Define it
um and then you can find people who work
at those protocols to explain it to you
further but um before we start off we
have to start from just kind of the base
idea of modular blockchains right so
modular versus monolithic monolithic
blockchains do everything they do
consensus they do settlement they do da
and they do execution right so something
like a salon would be a mod monolithic
blockchain technically ethereum was a
monolithic blockchain until the rollup
architecture was introduced right so
modular blockchains do a subset of that
so they might only do execution they
might only do data availability they
might do a subset in multiple um and so
that's kind of when we get into all
these new definitions of sovereign
based enshrined I said something else I
don't remember but we'll get into it
okay cool so now we start with the
basics again right so so the what I
talked about before you know rollups you
might know today optimism scroll uh
Stark net zkc clenia polygon Z KVM I'm
sorry if I didn't name you and you work
on that protocol um I respect you I just
don't remember you right now um but
essentially what those are are going to
be what we call now smart contract
Roll-Ups right so those are controlled
by smart contract store on the L1 uh
what they do is again like I said before
store roll up state track deposits
withdrawals handle
verification key takeaway here is they
mainly handle the execution part of it
the other key takeaway here is something
we're going to get into when we talk
about enshrined rollups so enshrine
Roll-Ups are different from Smart
contract layer uh smart contract rollups
in the sense that they integrate with
the L1 at the consensus level so that
means something has happened at ethereum
core that they are now interacting with
what that means specifically is when we
talk about smart contract rollups right
we have an external party determining
what that smart contract looks like
right we need security councils multi
sigs you need a bridge for up L2
upgrades um for um so when we talk about
enshrined rollups you don't need all of
that right because it's enshrined within
ethereum itself um for a ZK evm
enshrined rollup like validators don't
have to reexecute everything because
everything's enshrined in ethereum um
the cons here are going to be VM and
flexibility right so in this case you're
married to whatever the L1 VM is uh the
cool thing that I will talk about at the
end of this presentation is about all
the new different types of VMS that are
coming about that's helping with scaling
right so you lose that um the other part
is like it's slower to upgrade you don't
move as fast um in terms of like
development it might be more complex um
but there are pros and cons like I said
and there is a space where actually both
of them live together um so we're all a
happy family uh cool moving on oh I put
a logo here this is tasos so tasus is an
L1 blockchain if you don't know them
they are doing enshrined rollups in some
capacity I don't know how but find a
tasos person and they will tell you um
that's that's my uh tip for Devcon week
uh the other piece you might have heard
of is base rollups so base rollups is I
guess not the traditional term of like
you find an urban dictionary um but this
is I guess the nerd sniping term for
people who are interested in Tao right
so base rollups basically use the L1 for
sequencing so if you remember when I
talked before about operators right
operators are a centralized sequencer
that kind of take everything together
um base Bas rollups basically use
ethereum for sequencing so what this
allows us to do is inherit the
decentralization of ethereum and
inherits the liveness of the L1 so if
ethereum goes down the sequencer goes
down like uh we are we are f u c k d
anyway versus like a centralized
sequencer going down that's a different
case right um and it is simpler when it
comes to like decentralization of the
sequencer um the con part of it right uh
is uh if you want to get into it we can
talk about it after I'm not going to go
over it here but there are different
performance improvements that rollups in
uh do by like fixing the way they
sequence stuff um that you obviously
won't get in this case um and the other
part uh uh maybe a good thing or a bad
thing depending on who you are me that
happens is going to be taken at the L1
level you no longer get like the
sequence or MV me from l2s right because
l1's are handling sequencing the last
piece we're going to talk about here is
Sovereign Roll-Ups so Sovereign Roll-Ups
are kind of like I choose everything
myself because I am Sovereign uh so what
that means is I choose my own execution
I choose my own settlement layers um the
pros here basically are again talking
about like that forced upgrade from
Smart contract rollups right so smart
contract rollup upgrades um if you want
to participate in the L1 or if you don't
want to participate in the L2 you just
have to you have to exit right because
the smart contract is upgraded soten
rollups are actually like Hey we're
going to choose our own settlement we're
going to choose our own execution we're
going to do everything our same it's
what you can think of is the nodes
control how they interact with each
other so what that looks like is in
order to upgrade a sovereign rollup you
have to actually Fork like a traditional
L1 um and so that allows us to basically
kind of maintain whatever state we had
before if you don't want to participate
in the upgrade um the interesting thing
here is right like this is a this is a
design space where you might be using
ethereum or Bitcoin as purely data
availability and then not care about
like um consensus settlement Etc maybe
with somebody else right I didn't put a
logo here but if you want to read more
about it Celestia is a project that is
working a lot on Sovereign rollups um
but yeah so section four is like other
Niche topics that aren't handled by
rollups I yeah I don't know how much
time I left but I think I have
yes this is what I read online so the
answer is yes as far as Google and a
article that I read is
correct um cool so let's dive into other
Hot Topic so something you might have
heard of recently is trusted execution
environments so trusted execution
environments is when we start talking
about Hardware with regards to privacy
and scaling right so a te is essentially
an area within a computer's processor
where you can run code but nobody else
can access it so like the OS actually
can't even access that space right um
what this means it is isolated so it
creat something called a secure Enclave
is something you might have heard of
within the main processor only
pre-authorized code can run here um it
has something not every te has this but
some of them do they have attestations
right so tees that you might use can
produce an attestation to prove to
others that the code is running is
genuine and
unmodified sorry I just
burped and the last piece is
confidentiality like I said because this
is a separate um part of the I guess the
hardware you get to do stuff that's
encrypted and inaccessible to the rest
of the system system so something that's
really important maybe for like privacy
Solutions in that new space right um
when we think about it further um actual
te providers you might have heard of or
now know because I am saying it right
now Intel sgx is something it's going to
be a hardware provider AWS Nitro is a te
provider but they're more of a virtual
machine um and like I said before this
supports use cases like privacy it
actually protects against me which is an
really interesting space um flash Bots
is doing stuffing and direction if you
want to Google Flash Bots te me um that
would be a good place to start there's a
question sorry
what oh yes yes there's arm and trusso
and I didn't list all of them there's a
few but I only put two I should have put
all of them thank you for that um but
moving on uh why we care about tees
right um it's a hardware secure
environment
um but to that point too it is going to
be vulnerable to whatever Hardware SEC
uh specific attacks there are you are
putting trust in a different party such
as an Intel such as an AWS which comes
with its own trade-offs um but these are
very battle tested widely used um
projects um it allows for fast
computation with Hardware acceleration I
think the con side is when we talk about
like participating in networks if you
require a te in order to run IE
specialized Hardware it might prevent
certain people from participating in the
network um and then Integrity guarantees
they have attestations um but again like
I said it does require trust in the
hardware manufacturers so whatever you
have appetite for um but actually this
is something interesting I want to dive
into when we talk about a particular use
case of tees when it comes to rollups so
the L2 design space right and I
mentioned before something called
multi-prover so this is a new buzzword
that you should keep in your mind so so
essentially if we look at systems today
we have a basically a single proof
system so if that is a if there's a bug
in that proof system that's a
vulnerability right so now there's a new
thing that uh scroll has done I believe
Tao has as well if somebody else is
doing please let me know um called
multi- proofers and what this
essentially says is we want multiple
proof implementations to basically reach
a consensus of Truth in order to like
strengthen the security guarantee right
um there's different ways to do multile
proofs right we have fraud proofs but
that will introduce I guess you could
say the challenge period so you have the
problem finality running in again
another way is just build a second zkm
because you're crazy um so do it if you
want that's I don't recommend it or
maybe recommend it I don't know um and
the third piece uh that scroll at least
is moving forward with is doing a
separate te right so we're doing the
transaction in a te as well generating
proofs there um and the way we're
actually doing it again when we think
about having multiple implantations um
we are doing via different types of
Hardware so if you see Intel sgx AMD AWS
things like that um I guess another cool
thing to think about when you're
considering the rollup space uh what
else do I have yes okay this is the last
piece and I have 50 minutes left wow I
talked for so long for so short of a
time sorry our ZK EVMS endgame so this
is probably the spiciest thing right
because I think you probably been
hearing a lot of rhetoric about like
ckvm fast finality like we want to
be um I guess on par with you know the
latest developments in ethereum but
there's something that's really
interesting in terms of the ZK VM space
so ZK VM you can kind of think of It's
relatively straightforward you just take
the ethereum out of it it basically
enables um like I said before
computation that is provable but this
time it's more General computation right
so you're not limited to whatever the
evm does um it's decided uh to support a
broad range of applications the cool
thing about ZK VM that has allowed um
developers to do um is actually build
circuits in languages that are more
mature right so if you're building
circuits right now you might build in
something called uh circum right when we
talk about zkm that are bu being built
right now we're writing custom circuits
which requires Custom Security auditing
which requires like I guess a very
specific skill set but with ckvm what it
allows you to do is actually do that
same thing but do it in Rust right you
have a bigger pool of developers um rust
has its own like really cool like Speedy
things that it does um and I guess
projects to look out for that are doing
ZK VMS is risk zero and succinct and
this is really cool actually like I
mentioned before of what this allows us
to do um is actually uh succinct built
something that allows optimistic rollups
to start implementing validity proofs
right it's it's very very new but this
is kind of the new space that ZK VMS
introduce right the other thing and like
what that allows us to do right is
accelerate ZK development in general so
when we think about blockers to privacy
use cases identity Etc it's all like you
you need a lot of I guess background
information but now you can do it stuff
like rust and like I said before the
auditing surface is easier um and so I
guess new things to look up research zth
and sp1 um ZK VMS are an interesting
design space to
follow okay so these are my sources that
I kind of was like looking through if
you want all of this information or want
to read more um I had a pretty wordy
slide because I feel like this is more
useful as a reference but um this is a
QR code to my beacon page which has a
link to the the slides themselves so
feel free to save it um if you want to
follow me on Twitter feel free I mostly
post about frogs so um I guess follow at
your own
Peril yeah I I think I have 47 minutes
left so I kind of screwed myself over
with 47 minutes of Q&amp;A but
uh that's
everything um I think that QR code is
supposed to allow you to ask questions
over chat but I'm also happy to just no
questions
yes
no write do I write about real frogs um
no I only post frog memes but I'll tell
you about my favorite real frog because
I have 47 minutes to talk about my
favorite real frog um and my favorite
real frog is the desert rain frog which
I have in a
slide yeah uh
[Music]
uh cool this is my favorite frog and the
cool thing about this is it never
becomes a tadpole because it lives in
the desert it just immediately becomes a
little
frog the
end okay cool have you seen the have I
seen the good place I've seen parts of
season one and then I fell
asleep okay cool thank
you if we're all good um you can also
find me I guess at the scroll Booth
where we'll have more swag for everybody
who enthusiastically answered the
questions so okay cool oh you have more
because
h
oh
e I
oh e
for for
for
okay than
you
a
I
your e
he
e
n
Ro
oo
back
[Applause]
all right hello
everyone welcome to this next Workshop
hopefully you can hear me
well I'm wondering how to share my
slides um maybe I just wait for a moment
for that all right here we
go okay how is everyone doing I hope all
of you hope all of you had a chance to
to get lunch uh you will need some brain
cells to to follow along uh although
overall it's going to be kind of a big
friendly uh Workshop we're going to do
kind of a presentation first and then
some solidity coding if you have some
basic experience with solidity with
smart contracts or if you're just uh you
know comfortable just reading code then
you should be able to follow
along um so yeah my name is Peter I'm a
protocol engineer at scroll and today I
won't talk about scroll per se but I
will talk about a new proposal uh that
we proposed called RP 7728 l1s load so
this is a new proposal that scroll kind
of U implemented in a Dev nut but we
hope that this will be adopted by
multiple at2s in the future so the hope
is that uh after this initial 20 minute
presentation you kind of get the idea
like what is l1s load what can you do
with it uh why should you care about it
and then for the remainder uh myself and
my friend RH will uh do like a solidity
kind of Workshop so we have a two
Hands-On examples and exercises for you
okay so now you can hear me
uh I haven't said anything important yet
so uh yeah let's kick off oh by the way
before we kick
off uh if you have any questions feel
free to interrupt me but also there is
this uh Q&amp;A function here in the app so
you can just click here I think most
people probably don't know don't know
about it I don't think it's widely used
feel free to submit any questions here
as well I will keep an eye on
this all right so l1s load is uh new
proposal for rollups uh for l2s it's a
pre-compile that allows developers to
build applications that read L1 state
from their L2 contracts we hope that
this is a new functionality it's uh not
groundbreaking this is something if
you're very technical or if you take on
the cost you can already do in your
depth uh but this proposal makes it much
much easier and we hope that this will
unlock a lot of new
applications so I want to talk about
what is Ion slot kind of show you the
interface how to use it where some of
the use cases that we found so far uh
then I want to get a bit more
philosophical like why do we want to
offer this service on the protocol level
and finally just some insights into kind
of the Procol engineering part and the
challenges of Designing such a such a
proposal uh there's going to be another
talk on Thursday where I will jump into
much more details about these Procol
level uh
considerations all right so what is L1 s
load so L1 SL load as I mentioned is a
pre-compiled if you're familiar with the
evm you know that there's the evm bite
code uh that you execute but there's
also special contracts called pre-
compil that uh Implement certain
functionality on ethereum on layer one
this is usually like heavy you know
expensive cryptographic operations that
would be very uh expensive to implement
in solidity but we can also use the same
mechanism to expose other
functionalities to to L2 smart contracts
so l1s Lo is a pre-compile and you can
call it from your contract just normal
solidity code and you can read States
directly from layer one which is
ethereum
um this is how it
looks how many of you are familiar with
solidity or has written
solidity okay so I think you should be
able to follow along uh basically this
is just a very intro example the way you
would interact with any pre-compile
including i1s load uh is basically you
can just issue a call to it like a smart
contract call uh here we use a low lower
level call called Static call and you
just encode uh the the payload and with
this proposal the payload is simply a
contract address an L1 contract address
and one two or more storage
Keys you can call it from your
contract um and then you can decode uh
the result so this is actually fetching
data not from the local blockchain that
you're running on which might be scroll
it might be optimism it might be
arbitrum any L2 that implements this
proposal uh
it's instead of that it's fetching data
from ethereum L1 under the
hood so this is defined in a in an rip
I'm not sure if any of you are familiar
with this so EIP etherum Improvement
proposals are used to uh you know
propose new features for the base layer
for ethereum and there's kind of a new
initiative this year called Rip which is
similar process for rollups so rollup
Improvement proposal it's uh optional so
we can create these proposals if you
guys find it useful then hopefully more
and more Ro will adopt
this yeah so just more details
here um why do we care about this why is
it useful uh this is kind of as you say
it's kind of low level just looking at
the previous slide code example it's
kind of hard to see what what it's used
for luckily we've already run a couple
of hackathons and hackers came up with
some great use case ideas in the past
few months and I think we have a similar
hackathon just after Devcon one of my
favorite use cas examples was a a cross
layer tornado cache Bridge so many of
you might be fam familiar with tornado
cache it's a shielded pool basically you
can uh deposit your assets and then
withdraw to another address and you
cannot correlate the depositor and and
RW address so it's a privacy preserving
mixing pool uh but you can only you
could only use it on L1 but you could
use the same technology to kind of
deposit on L1 and withdraw on L2 uh and
this could be built using l1s load
another use case is ens so ens is still
primarily used on layer one uh although
they are exploring you know supporting
more and more l2s or deploying on l2s
but if you're on a chain that doesn't
have ens then through l1s load you can
still resolve these domains uh just by
reading the register uh contents from
i1 there's also cross layer reputation
system incorporating data both from L1
and L2 chains uh there's bunch of defi
application use cases so for instance uh
you could borrow on L2 without Bridging
the collateral to L2 just using your
collateral on A1 that's an idea that
they explored uh you could also
Implement these hooks for UNIS swap to
make sure that the L2 uh pool has enough
liquidity and and not too high slippage
compared to the L1 pool so kind of give
more assurances to to you when you swap
and you can also use other you know
multi a wallet key store use cases with
this uh so these are just some
highlights and I linked all of them here
you can check the slides if you're
interested these are very interesting
project that we've seen at
hackathons all right so now you kind of
have a general idea of what is out1 lo
so uh let me jump into kind of why we
want to provide this function on the
protocol
level wanted to give a quick walk
through of rups but I think many of you
are here for the previous session by
Emily and I prepared two slides and
Emily did like 50 slides and she did a
great job kind of telling all of you
what rollups are so I'm just going to
keep it very short so a rollup is an
ethereum that's uh inheriting a lot of
security guarantees uh from L1 which is
ethereum in the case of rollups so
rollup create an L2 chain and then
package these L2 blocks into blobs post
it on ethereum and also post the
execution results which is the L2 State
rout and then there's different
mechanisms how you can verify the out2
state Roo uh towards a canonical Bridge
so you can use fraud proofs you can use
ZK proofs there's different uh pros and
cons so if you think about information
related between L1 and L2 uh when you
relay information from i1 uh you need
to uh usually use a deposit message or
some kind of other message on in the
canonical bridge and this message will
be relayed by the sequencer uh in a in a
verifiable way so uh usually the
sequencer would include these deposit
messages where you can encode additional
information but uh the sequencer could
also Implement other fun fun for
instance relaying the Alon block
hashes the other way around you usually
need to First submit a withdraw message
on the rollup and then once this is
finalized you need to claim it on the a
one side so uh slightly different ways
uh depending on which direction you want
to
go all right so if you're a dep
developer and you want to read some data
from L2 on L1 how do you do that well
you're lucky because you already have
the L2 State rot on L1 that's kind of an
inherent property of or rollups that the
L2 State root is posted to L1 so your
contract can just read the state rooot
and provide a mle proof and then you can
verifiably read any state from
L2 the other way is basically the same
thing but uh it's a bit trickier because
l2s usually don't have this notion of
the L1 State tro uh so we would have to
implement that first but there's ways
around this to implement it and then
it's the same thing you provide a mirle
proof to read from i1 so it is already
with without this proposal is possible
to do it but it's not very convenient
like how do you relay the album stage
Roo how do you verify it how do provide
this mer proof it's a lot of extra
complexity and overhead for the
developer as well as
cost so the the idea here is all of this
process the second part how to read L1
state from L2 is something that the
sequencer could provide you as a service
so hide all the complexity from the
developers and you just focus on your
application logic and just interact with
this uh contract
so I would say it's Miracle proofs as a
sequencer Service uh that's one way to
think about
it uh if you think about this how how
it's implanted by the sequencer
basically any call to this precompile is
translated to an RPC call to an L1 note
so if you're familiar with the uh Json
RPC of ethereum there's one called e get
storage at that's basically what this
precompact corresponds to uh and then
the tricky part is how do you verify it
so uh we also need to make sure either
in the fra proof or in the ZK
verification proof uh that you also
verify this that the sequencer didn't
cheat you the sequencer actually relayed
uh the correct
message as an as side many of you might
not know like why do why do we use a
pre-compile why don't we use an OP code
for instance uh it's mainly because of
compatibility so we want to maintain
compatibility with existing tooling with
the evm you know solidity compiler if
you had the new OP code then none of the
tooling knows about it but if you had
the new pre-compiled then most of the
tooling can interact with it as if it
were you know a normal solid solidity
contract so it's a much less invasive
way to add functionalities that ethereum
might not
have all right just a little bit more
details about kind of the implementation
um because as myself Procol Developers
for rollups and other rollups team rup
teams you need to think very hard about
how do you implement it what are the
possible attack reactors that this could
open up how do you verify the inclusion
Etc
so the interface of the contract uh that
you will also see in more detail in the
solidity example is we Tred to keep it
as simple as possible so basically you
just need to pass an address and then
one to up to five in the current spec uh
storage keys so you can read up to five
storage values from L1 in a single call
to this pre-compile and then the result
is also just standard storage slots if
you're familiar with storage layout then
you know what this means if you're not
then R will tell you all about it uh in
a couple of minutes uh it just return to
you and then you can decode
it uh implementation wise there's two
main prerequisites that might be a bit
controversial so first I briefly
mentioned that you need to have this
notion of what is the latest L2 L1 block
hash your L2 needs to have this notion
so uh either the sequencer needs to uh
relay this with a special system
transaction or you need to have some
other mechanism
but all the L2 NOS must agree on this
otherwise your execution would diverge
so I would call this feature trustless
L1 block hash relay some rollups already
have this others have designs for this
but not launched yet in scroll the way
it would work and this might be
different or similar to other rollups is
the sequencer optimistically relays this
information uh but any other note can
verify it at this point so if the
sequencer cheats then it's easy to
detect and when we finalize the batch
with the ZK proof that that's when we
verify that the sequencer actually
relates the correct block hash because
on L1 during finalization we have access
to this
information and the second prerequisite
is that for reading L1 State you have
you need to have access to an L1 node
right uh which is already true for
sequencer so sequencer has to process
these Bridge messages so they already
connect to an one node but currently for
some l2s you don't if you run a follower
node you don't need to connect to an L1
node now if you adopt l1s load proposal
then you must always connect to L1 node
so that might be an additional overhead
for some node operators but I would
argue that this is kind of
acceptable yeah so all add to nodes then
must connect to an one node so that they
can serve these requests about I one
state and then there two more notes
about implementation so we have a
reference implementation I have a link
to this uh in the slides if you're
interested in our go ethereum Fork but
basically what you need to do is pretty
simple so you need to modify the evm and
add this pre-compile so that when
there's a call to that address which is
specified in the rip then it triggers
execution of this special contract and
when this contract is called it simply
starts executing an RPC request against
the L1 node and waits for the result so
there's some complexity here that I
probably won't go into too much that
like what happens if the request time
times out or the request fails uh this
can be an issue and also this request
might affect throughputs but normally
when you run your L2 node on the same
machine let's say or in the same data
center as the L1 node this should be
fairly fast and and error
free and once the RPC returns you return
these results to to the evm and
execution continues as
before so that's the execution part and
the second part is verification
uh as I mentioned we need to keep
relaying these L1 block hashes to to L2
in a very viable way so in our case at
scroll for instance we have a solidity
contract on L2 the only thing that the
sequencer does is that it takes the L1
block headers and feeds them into this
L2 contract and the L2 contract actually
does the verification that it's a
correct chain of L1
blocks and then once you submit this to
L1 and verify it in ZK proof then we
read the the block has the correct block
has from the L1 you know evm context and
verify that this relay step was done
correctly and finally so this first and
second step is the uh trustless block
hash relay component but you also need
to verify each and every call to this
l1s load pre-compile so for any
pre-compile call we need to or the
sequencer or the prover depending on
your architecture it needs to fetch an
MPT proof and it needs to verify that as
part of the broader ZK proof so this is
something all of these steps are steps
that you would need to do as a developer
uh but now that this is part of the
protocol and it's a sequencer service
you don't need to care about this
anymore you can know that it's it's
working and
verified all right uh lot of details
just a few more uh notes about the next
steps so this RP is fairly new we just
published it in June this year uh
there's a call for the RP process called
roll call we presented it in July and
then as I mentioned since July until now
we had a bunch of hackathons where
hackers and and deaths could explore
this and play around with this
proposals and for now we just want to
continue this process and we'd love to
hear more feedback from developers from
uh Procol maintainers uh basically once
we can Converge on a spec that everyone
is happy with and L2 other L2 teams at
least two or three L2 teams uh have some
willingness to adopt it
then we can finalize a spec and and
start rolling rolling this out in
production I think it would be awesome
to get to that stage uh next
year all right there's a few additional
resources here for your
reference uh and I have again the slides
here if you want to save them but for
the remainder of the the talk or the
workshop we want to jump into more like
Hands-On
coding before we do that any
questions yeah
yeah so when you have a transaction that
calls i1s load then any node be it
sequencer or follower node will execute
an RPC call corresponding to this pre-
compi
call for the validation yeah so proving
it depends on your proving system but I
think we we can say that uh so the
question was how long does it take to
verify the whole thing uh a couple of
years ago this would have been
impractical because you couldn't have
proven you know an L1 MPT proof in ZK
the techn technology was not there yet
but now proving speeds have been
catching up and you have you know
general purpose ZK VM so in our
experience this would add maybe a couple
more minutes to the proving time uh but
it's not significant and it will go down
rapidly in the next few
years all right there's a question here
thanks for using uh the Q&amp;A form so
what's the adoption look like from other
i2s uh how do we help that's a that's a
great question so we presented it at Ro
call uh there's been some discussion on
eth magicians which is kind of the goto
place to discuss the proposal but we we
haven't received too much feedback the
only the main feedback we've received so
far is that Dev it you know it kind of
open UPS the design space to to depths
that you would not think about normally
so that's very good feedback but I'd
love to hear feedback from other2 teams
other rollups team teams if you can
point out issues or uh anything that
might break in the spec that we need to
fix the earlier the better and then we
can converge to a final
spec all
right so I just continue uh with the
next section so we have uh these code
examples basically three code examples
of increasing complexity although not
too complex setup if you want to either
follow along uh well if you follow on
you can just follow the the screen if
you want to reference this later then
you can uh take the code from GitHub it
has all the solutions so if you don't
want spoilers then don't open it yet or
don't don't open the files yet
all right so you can see the editor if
you know the text is too small or
anything then let me know and I can
adjust so I want to walk you through a
very simple kind of toy example just
kind of to get a feel of how l1s load
works from a developer P
perspective uh let me show you so for
this example we will use Foundry uh many
of you might have used you know remix
hard head Foundry I think more and more
people use Foundry that's what we're
going to use here but you can use any of
your developer tools that you're happy
with uh we're just going to do some fast
development and testing on Foundry and
then RH will show you how you can also
interact with a devet that we we
running so the simple toy example that I
want to talk about is uh a counter so
let's say we have this simple counter
contract on I one uh and it m maintains
two entries in storage so one is a
simple onside in
and the other one is a mapping so uh
nothing nothing fancy yet and then
there's only one function it which is to
increment this number and then to store
something in the mapping I guess counter
is a bit of a misnomer because there's
also this mapping but uh you get the
point we just want to have kind of some
State on L1 that we can interact with so
let's say you deploy this contract on L1
or someone has deployed it and you want
to reach from it how do you reach from
it from
outu so for that we will Define another
contract called counter reader uh and
the idea is that this is deployed on a
different blockchain this is deployed on
out2 so let's say counter is deployed on
ethereum counter reader is deployed on
on arbitrum or ZK sync or any any rollup
that adopts this uh
proposal so when we instantiate this
counter reader uh we definitely need to
have the address so I I have that
prefilled in here so we're going to
store the address of the i1 contract and
then the question is how do how do you
actually read from thean contract so I'm
going to show you first the lowlevel
interface and then we also have some
heler kind of utilities that make it
much much easier to to do
this so let's just go back to the slides
for a moment I had this slide previously
so um this is a recipe of what you what
you want to do uh you need to ABI incode
using Inc code packed the arguments to
this call static call and then decode
the result so let's try to do do this
and and see if it
happens so I'm just going to start by
defining the
payload and the payload is as I
mentioned it's an
address and we already have the address
here stored that would be counter I
could also call it L1 counter just to
make it clear and then it can be one two
or up to five story slots so let's keep
things simple and just focus on the
first variable for now
now who who knows what is the story slot
of uh of this
variable yeah zero uh this is quite easy
here but when the contract gets more
complex then it also gets more complex
like if you have inheritance Etc so one
thing you can do is I usually use Forge
inspect it's a kind of Handy command so
you can use Forge inspect storage layout
I believe this basically just calls into
the compiler and this will show the
storage layout of your contract so we
have number at slot zero and the mapping
is at slot one uh as
expected so I'm just going to go ahead
and read slot
zero and that's going to be our
payload so we have the payload next step
is to actually call the pre-compile so
to call the pre-compile you need to have
the address address here in this helper
I already have this
hardcoded uh this is subject to change
so uh as I mentioned the The Proposal is
still not final and also there's an
interesting discussion going on like
what address should uh these L2 pre-
compiles use should they continue at the
same address range that L1 pre- compiles
have or should they have like a
dedicated pre-compile address range I
think everyone is leaning toward the
second option but for now we just is
going to use the same address that we
have on our uh devnet that we are
maintaining so we're just going to use
this address and static call
payload and what this returns if you're
familiar with kind of lower level calls
inside evm is whether this call
succeeded and the the result of the
call all right so we are halfway there
um I'm going very slow because this is
kind of an intro example I think for
advanced developers this might be a bit
boring but just hang on for for a
moment so you got to make sure that this
call succeed
succeeded if it did not then of course
we cannot continue uh now it depends on
the final spec in the current
implementation there's no way that the1
load fails once the transaction is
included in a block that means that the
sequencer managed to fetch the storage
entries so it it should always succeed
but um unless of course you for instance
encoded the inputs incorrectly so you
got to make sure that you do that
right so it didn't succeed we just
revert and if it did succeed then we can
decode the
data so the data very developer friendly
again is just AI encoded so you can use
all the solity uh tooling or or syntax
to to decode it in our case for now this
is going to be a single unide
int so this is the number and I can get
to the number by just AI decoding uh
this return
value all right so we we got to a point
where we could read at least one of the
story slots uh now let's try to test it
and the test kind of also shows you
first of all how you can develop with an
S load and also how this uh Toy example
would work in
practice so I have a Foundry test
prepared here uh kind of the very
convenient thing about Foundry is that
you can use solidity for the whole
development process you don't need to
switch to another language uh to write
your tests so in this case we do run
this test in solidity but the problem is
that envil and Foundry all this tooling
is not aware of this l1s load
pre-compile so to make development
painless we created this uh this uh
class that you can use or this contract
test with1 load so this basically
injects uh fake L1 Lo that behaves the
same way as as the real one into your
test environment so whatever you test
with this should also work uh in the
actual L2
context and then the test itself is very
simple we just deploy the L1
contract um you can imagine that this
happens on i1 uh for now we're testing
it in a single EV
environment so deploy the L1 contract
and deploy the L2 contract with the
address and then you try to read the
contract originally we didn't initialize
the storage values so all of them to
should be zero then we call in increment
after this increment call uh when we
read from L2 you should see that the
state has been
updated let's see if that
works oops
all right so far so good so we ran the
test it passed and that means that
actually when we called this read
counter method what it did is it called
l1s load l1s load fetched this storage
from L1 and then it returned to the L2
context uh the only thing missing from
this example is the how do we read uh
the mapping because if I uncommon this
line since we didn't implement this the
test will fail as expected so so how do
we do
that um doesn't even know um so
basically what we want to do is read the
mapping value of this corresponding to
this key of 1 two three how do I get the
storage slot corresponding to this value
I wonder if anyone
knows hash of the message sender hash is
correct exactly so some way you need to
take the key you need to take the slot
which is one in this case hash them AI
en Cod and hash them together and that's
how solidity calculat these mapping keys
so it's a bit more complex but if you
know what you're doing then not not
super
complex so let's try to add
that I just move this to another
variable oops it's actually quite hard
to type standing here just hold on for a
sec so you need to ABI encode I believe
the first the first one is the key it's
something that you kind of got to
remember but RH will Enlighten you in a
couple of seconds in the about the
details so first is the storage key
second is the slot and then you just
take the
hash and let's let's see if that works
maybe I remember it incorrectly in which
case I can just fix it all right so now
instead of reading one slot I read two
slots uh the call otherwise happens the
same way I just need to add this
additional argument here and also when I
decode the results uh I need to decode
it as two unide in so this will
be first one is going to be let's say
value zero and the second is value
one and then just return
this so it's not fun Al different from
just uh reading one value or two
values okay let's see if that works so
now the test should
pass Yeah question
oh yeah
yeah so that's a good point I think the
the feedback is this is kind of low
level like who wants to deal with this
we could if we could just you know call
counter DOT number to read it this this
would be more convenient and you can
definitely do that I I think Ian asot is
just a a building block and it's very
easy to to build higher level
abstractions on top of that actually let
let me show you uh and then we can get
to the next question so just wanted to
show you this is how it works on a low
level but we do provide some uh
libraries a simple library in this uh
repo if you open it so instead of what
you can do is i1s load read
read inside in and just provide the the
address and the
slots so I still I still need to define
a slots but uh the rest of the code is
basically replaced by this single liner
so same thing actually just uh hidden in
a library uh so as a developer it's
probably much easier to interface with
this and also we have utilities for
onside in for byes for address Etc and
also this is still not as high level as
you suggested but using this it's very
easy to I can create a contract or
generate a contract that looks just like
this but is actually calling out one
EST that
question
yeah that's a that's a really good
question gu was can I specify which
block I want to read
from yeah so that that's a big challenge
for sure so in the first iteration of
the RP we designed the interface in a
way that you can also pass a block
number so you can read from arbitrary
height uh that's for some applications
that's a must have for many applications
this is not needed and it also requires
you to run an archive node because you
need to be able to always serve archive
uh data but basically one of the open
questions for the rip like do we need
this do developers need this if yes then
then we can add this uh but in terms of
reading stale data that's still a
challenge because uh there's a delay
between when the data is updated on L1
and when this information is related to
L2 so this delay can be reduced but it's
not
instantaneous exactly yeah uh someone
commented on eth magician exactly about
this if you have any input for that
discussion with love to hear or see your
comment any other
questions actually let me check the
Q&amp;A we can get back to the more general
questions a bit later so that kind of
wraps up the first example again a very
simple to example but kind of shows you
the power of Aon load and also shows you
how you can use this uh in your
application without too much added uh
complexity now for the next two sections
I want to hand it over to RH uh
hopefully I think many of you might be
dozing off you know my mellow voice and
also digesting the lunch so R is full of
energy and and he'll kind of shake you
up
so Peter's Too Tall I have to just like
adjust this a little bit so hey everyone
my name is Rh I am so happy that Peter
went first because mine is going to be
dialing it down a lot level lower u i
mean to the extent that because it's a
beginner Workshop we're going to be
tailoring it for beginners who probably
are not very familiar with Foundry as
well but they also just want to get
rapid prototyping accessibility by using
remix so we're going to be using remix a
lot shout out to the remix team and and
we're going to dive into the example
first okay while it's loading up here
I'm not too sure if I would be getting
like bandwidth or if the demo gods are
going to be with me so what I did over
here was that I pre-recorded this and we
could go through this it's probably
about 10 minutes and then I'm going to
be narrating over it as well so 10
minutes this is going to be like super
beginner friendly so for a lot of you
I'm seeing intermediate to advanced
level deps you're going to be bored out
of your mind and if you're bored out of
your mind hopefully I can sing you a l
by and then put you to bed for a little
while take a little nap and then be back
up for a bit more of the complex types
that we will be seeing uh so in this
section in part two just a quick
overview as well we have done three
hackathons so far which uses l1s load so
through those hackathons we have re
receive like multiple feedback on
implementation understanding how to
rapidly use it in different hackathon
environments so that you can quickly tap
into it and start building the
application that you're looking for so
that is sort of where I will be leading
this session more so for like the
implementation side of things all righty
so let's jump right into the remix Demo
First this is going to be covering some
setup in terms of like how do you want
to set up your injector provider
environment in metamask with with the
death net that Pier mentioned we're
going to be going through that and
you're all also in for some treat to
watch me do a bit of debugging and watch
my poor coding skills all on screen and
just before we dive into it I want to
give a quick shout out to ahed I see
Ahmed there in the crowd he was the one
who help us to also put this together so
a lot of the credits go to him okay so
without further Ado we're going to first
jump into remix so this is me writing
the L1 SL load demo.
soul is this like
how fast is this this seems like super
fast uh let's do fast okay all right now
I know that it's a little small because
even I can't see it from here so I've
unlodged this so in this L1 SLO demo I'm
going to do a quick demo on how you can
rapidly create an layer one contract and
a layer two contract just read L1 SLO
with less than 25 lines of code just to
see how simple it can get so for this
context over here we are creating an L1
contract so this would be on ethereum
Main net and in this case since we're
doing a prototyping version is going to
be on spolia we're going to be defining
the first variable over here which is
number of Type U in 256 and we're going
to be putting up a Setter function so
this set function over here is for us to
override this number variable and as we
can see number is equals to underscore
value and that's all that is required
for the L1 contract again this is a very
very simple example we're probably going
to be speed running through this because
Peter did a way cooler job with Foundry
but this is also to cater to developers
who are more accustomed to using remix
so now moving on to the layer to
contract yeah fun fact about remix we
can actually put layer one contract and
Layer Two contract also in the same file
I found that like pretty cool so the
layer two contract itself like what P
mentioned it could be an arbitrum or
whatever type of rollup in the future
that decides to adopt this piece of
technology so very quickly I I am
already defining the L1 SL pre-compile
address over here again I'll be sharing
all of the resources on where we can
find setting up for your defet it's all
here so I'm just like typing it out l1s
lo.
scroll.
systems if any of you are
bought right now I'm just putting it up
here also on the screen so you can also
be very handy with checking out the
resources that we have there's a
specific section here devet and it has a
table outlining every type of
information you need in order to get set
up with interacting with the defet and
there you can see that is the l1s load
pre-compile address and again over here
right now we're going to be building the
geta function for it and this getter
function will be the one where we call
the number from the L1 contract again
this is me trying to be as verbos as I
can but at some part not really I think
I do a pretty bad job so you can come
and provide me with constructive
feedback later on and we're going to be
creating two arguments over here we have
the L1 contract address because we have
to ultimately decide which is the
contract address that we're reading into
and we also have to define the storage
slot number and over here since it's a
geta function we're going to be
returning a u
showcasing some remix functionality
again we're diving into like what you
can also do in remix here so moving on
I've also written some comments on like
what I'm about to do next probably
should have done it in more like a to-do
fashion but anyways we're writing a call
function to L1 contract we're not really
defining the payload over here I'm just
trying to see what we can do with less
than 25 lines kind of code here so I try
to be creative not really and over here
we are destructuring already this lowle
call and we are going to be uh packing
the arguments which in this case it will
be the L1 contract address together with
the storage slot number and then
eventually the destructuring of this
process will return a Boolean of like
the success and also like the payload in
this case I'm defining it as U
data and very similar to Peter's example
over here we will be defining like for
Success if it's failing and it's going
to be reverting with an error message
over here okay I promise you we've
wrapped up really really soon now we
just have to convert the bytes we have
to type cast it from bytes to U 256 over
here so this would be the uh the syntax
in order for us to uh to typ cast it to
you in 256 so over here very quickly
just now you saw my wallet address and
it's already uh set up to be with sapoia
Network so we're going to deploy this
contract directly to sapoia
and yeah this is me being a lot more
verbos now we're deploying one contract
sapoia so really really beginner
friendly here like tapping on to like
the entire spectrum of even aspiring
developers here okay so now we've
deployed it
oops and after we've deployed it it's
probably a really good idea for us to
also copy the contract address which I
did not do but you can kind of see how
the terminal from remix would help us to
gather that information later later on
so I'm setting the number here to seven
just because we're at Defcon 7 ha found
that that was like pretty cool thought
process probably just myself so right
now number is set to seven on out on the
layer one contract itself so now we're
going to set up our custom Network for
defet we're going to go through this
process of how it can get set up over
here on the top left you should be able
to see like add a custom Network so over
here you just populate the information
of network name RPC URL everything you
can just copy and paste it from defnet
it's all set up for our
convenience there we go so this here
I've already preloaded the address for
seoa e now for developers who are
interested in trying this out the faet
the faucet is here definitely recommend
you to check out the faucet get 0.1
subol e for defet and it allows you like
Tinker with as much as you
want so over here now that I've already
added this custom Network we would then
be able to directly deploy it onto
defet so that's us switching to L2
contract and then we can directly
deploy over here I'm going to be
showcasing as well what were some of
those errors that I've encountered so
being very transparent as well notice
that there is the transaction failure
for not having enough gas I'll also just
be showcasing to some who are newer to
remix and also aspiring developers of
flight what you can do in order to get
this go through so then we just have to
bump up the gas so what I just did was I
just bump up to one very uh I would say
a simple way a smooth brain way of
treating this by bumping it one then we
are able to deploy the contract so right
now we already have this cont contract
on L2 so over here we're going to be
passing on those uh those to the
argument the input to the argument over
here we have the R1 contract address so
in retrospect in hindsight I should have
like copied the moment that the contract
was deployed on tooa but even if it's
not you have a record of the past
transactions in your terminal in remix
over here pretty handy you can see that
the contract address if this would go
away it's just directly uh tied to this
contract address key here so you can
just copy that and then you can just
pass that over to your L1 contract
address and storage slot number Peter
has done a great job already everyone
here is like Giga brain as well so you
already know that this is like storage
slot zero so I've also tried to be a bit
more verbal so that people know that
it's zero index for how evm treats story
slot and you can see that we have
successfully called seven as the number
as a response so we are able to get that
information from the L2 contract so
there was also one thing that was
lightly touched upon for the the L1 s
load technology itself so if let's say
if it is in production if I'm not wrong
it takes about 10 minutes in order for
us to retrieve the information on L2 but
if on defet that's actually an
artificial simulation so it's actually
relatively quicker in order for us to
get the information but over here you
can see that I'm trying to set a new
number to Showcase that it actually
takes some time before we're able to
read that data due to us simulating uh
the L2 uh the delay of the time that
we're getting the information from the
L1 storage slot itself so right now on
L1 you can see that the number has been
updated to 100 but when we're moving
back to the L2 contract it's going to
take a little bit of time in order for
us to get the latest information so as a
developer yourself when you're building
in hackthon if you come into this part
where hey why am I not getting this
information it's like better documented
inside the L1 sl.
systems as to
a bit of a delay for us when we are
getting this information but I can
assure you that I would say it's almost
about 20 30 seconds ago or around there
for the time of my testing this is me
just like repeatedly pressing it in a
way that I'm showing you that I'm
actively interacting with the UI here
and but eventually sometime about like
it will be updating itself to 100
so I think it should be
now this is also me going through the
different types of transaction that we
see yes so it takes just a little while
for it to update its information in
order to get the information from the L1
contract address uh so just like bear in
mind when you're also building using
Like Remix if let's say you encounter
this issue there's an L1 block input
delay time yeah it's better documented
here feel free to also like check out
the resource here so this is actually me
going through a very Elementary way of
what it's like interacting with the L1
SL load technology using
remix so maybe I can pause here a little
while to see if anyone has any
questions but I think like P done a
greater job and then he's covered like
all the possible questions so now what I
think we can do is I want to touch on
product refinement a little bit and what
I mean by product refinement is in the
previous hackathons we have different
developers also trying to use different
type of data types and different types
of structures which are a lot more
complex we're going to dive into it and
see how you can immediately implement it
inside your code in the upcoming hethon
or whatever hackathon that you're
looking at or even if you're looking to
just like build some cool right am
I allowed to say that I hope so but
anyways going into this hopefully this
is not too small let me enlarge
this okay so this is a pre-written
contract in order to like facilitate
this discussion what I've done over here
is I also have a couple of contract
addresses here and I'm just going to be
using them and load them in directly
into our L1 contract so over here we
have the first one we have F on
contract okay so for this demo over here
we will load this in directly into remix
we're going to pass that contract
address and this should be what you will
see now again all of this information I
want to highlight that it's already in
the QR code that Peter shared we have
all the information over here defon L1
Workshop if you head over to source and
if you head into part two of the
workshop you'll be able to get all of
the code here directly so at the same
time in a way you can actually be
interacting with this as I am going
through this demo with everyone over
here so very quickly while we're just
reading through this contract we can see
that we are defining you in 256 there's
a variable for it and then there's also
L1 text is what I've called it for
string and also by 32 which is for L1
bytes and some of them I have I have
left the Comon it's like storage slot at
position zero storage slot at location
one storage slot at location two but the
subsequent one we're going to try to
have a bit more of an interaction
together with the crowd here and you
guys let me know what you think of the
storage slot for the subsequent ones
we'll dive into them like later on so
we'll be also looking into fixed array
and also array with smaller data types
for example like a un 64 and then also
with Dynamic arrays and then we're going
to look at mapping Nest mapping and also
stru so these are some of the data types
and structures that we're using out
there definitely there's a lot more
complex on as well like what P mentioned
is also inheritance but for the sake of
time with pers the time that we have now
it's 2:50 okay we will be going through
this example that I have again it's a
accumulation of the past hackathons that
we try to refine the ideas upon and for
this Constructor very quickly running
through with everyone for L1 fix array
we have already instantiated a contract
with several input already so you can
see all of them inside here I want fix
array goes with like in the array of 3
six and 9 fix array 2 1020 0 and 30 and
so on and so forth and the following
ones these are just seta functions and
then also geta functions for us to kind
of play around if you're interested I
know that in hackathons it can get
pretty I would say stress so you just
want something quick and easy copy and
paste and start testing things out so
over here we're just going to take a
look at what it is like when we are
interacting with the contract already
there are some parameters that I have
already passed so I think the state it
right now it should be reflecting what
it is so for example when we're getting
retrieve number you can see that is it
too small I hope this is not too small
okay maybe this is better so u in 256
itself for for the variable of L1 number
it's already been instantiated with L
with 100 over here so there are a couple
more we're going to go through my
favorite which is retrieve string
retrieve string here this is interesting
I love Devcon I am super excited to be
here with all of you defon is going to
be the best time of our life all right
but it's very interesting as well
because for string type we're going to
see how we can actually access the
storage slot to concatenate all of the
string because as we know it's only a u
for what I have passed over here it's
definitely like way more than that it's
not able to like store all of it so how
do we actually concatenate everything
and then actually retrieve the string
that you want because there are some
hackthon use cases that I've heard of
developers wanting to also add maybe
like a URL to create like different
types of profiles and then like have it
live on like L1 so this is why we have
the example for retrieving string and
how do we like concatenate all of it and
if we don't what happens we're going to
be going through some visual illust
ations of that as well because the best
way to show is by yeah visual
representation and then for for the for
stru what we have set in place is that
we have let me quickly go through the
stru over here we have the name and we
have age and then some of some of the
information that we have already put in
place is like Alice is 20 years old Bob
is 21 Charlie's 22 and these are the
three pairs that we have and then very
quickly a quick run through as well if
we retrieve btes you can see that this
bite is not all zero Z you've got 1 2 3
and four 5 six for the sake of time I've
already SP run some of this information
I've already spit it in into this like
contract address over here so which is
why you can see that this information
they are not just zero if let's say it's
just instantiated you're going to just
be seeing zeros and if let's say we
retrieve like a dynamic array again we
have instantiated over here you can see
that it's 100 200 300 400 fix array 369
and also fixate to 1020 0 and 30 so we
can kind of see that I'm not lying this
is my proof of work that I've done my
homework everything here it is uh
correlating to this address which has
been instantiated okay so that is a high
level starting point to get everyone
accustomed to what this contract look
like when we're trying to call it like
using remix so now to the onward to the
fun part the fun part would be to look
at L2 contract how do we actually
interact with A1 contract and for this
example I have also deployed the
contract already because I feel like
demo gods are never always with me so I
just try to prepare myself as best as
possible to so everyone have a smooth
brain experience just like me okay so
for two of this contract here we have
the basic L2 contract.
so and this is
going to be touching on more of I would
say just three data types that we're
looking at we're going to have a
retrieve for L1 number which is the L1
number and then we also have the L1
string and then we also have the L1
bytes these are just the three data
types that we're looking at so I would
say this is probably the beginner
version before we move into the more
advanced type of manner of us calling
the different more complex data types
and data structures so for L2 contract
what we first going to do is we will
first change our Network and for Network
I have this s scroll l1s load and uh we
will also just copy the address which
has been deployed over here again we're
just working remix over here so
everything is whoops already set
up okay so for retrieving L1 number so
what we're going to do right now we are
going to be reading through the contract
together with everyone again there's
like multiple ways of us actually
setting this up we can even use the
contract that we're planning to read and
pass it on as an argument to the
function itself but for the purposes of
this demo in order to kind of like
speedrun this as well what we have done
is initiating this instantiating this
contract directly with the L1 absolute
contract address in this case which was
the L1 contract privacy that we' have
seen here so in this case when we call
retrieve L1 number retrieve L1 number
should return us 100 over here yes and
so when we take a look at Peter's demo
as representation uh basically I didn't
exactly Define the payload as a line by
itself that's the only difference but
everything else Remains the Same right
so a lot of the pattern this is me going
through the same patterns running
through in a recursive fashion so you
can kind of see that actually utilizing
this technology is not very difficult
even for aspiring developers this is
what I would like to try to instill to
everyone here in the audience I'll say
so we're retrieving L1 number public
view returns you into 256 over here the
you the slot number over here I have
defined it already in the local variable
as zero because in the L1 contract again
L1 number variable St uh Global variable
is at location zero and in order for us
to destructure this call here it's a
very standard uh standard syntax I would
say for us to destructure the
information we get the payload which is
data and then after that we typ cast it
to you in 256 in order to get the result
of 100 here which has been set in L1
contract now okay L1 string I'm going to
touch on that a little later I have
bytes underneath here first so we're
going to touch on bytes first very
similar also again the only difference
is that what we're returning right now
is then B memory and for the slot number
you in for the L1 slot number here it's
at location two I would say so this
would be what we would be efficiently
passing through to it and when we are
calling we making this lowlevel call
we're essentially calling this address
address here this l1s load address is
reading from here that we've defined in
the global variable and we can create
this lowlevel call and then we pack all
the information the contract address and
the slot number we concatenate both of
it and code pack and then we make this
call to effectively retrieve the data
which is in the form of bytes and when
we call it we can see that it is exactly
reading to what was the L1 contract
result like now for string type I find
that string is quite an interesting
piece of information I've heard some of
the audiences are already very familiar
with how to actually retrieving the
information so I feel like there are a
lot of like intermediate and advanced
level deps here already in the audience
so this is like fantastic also and what
we're going to do is just kind of like
rehash some of these Concepts that we
have seen and for string over here I
mentioned like test slots for example
because there's a limit for us to store
information in each of the storage slot
it goes up to like only uh uh you in 256
for example and so because of that
there's like limitation for each of
these storage slot what then happens is
that we actually have to add subsequent
we have to create a while loop in order
for us to concatenate all of the string
information together and then return
like what we have initially let pass at
the start of it so for example right now
string storage slot is located at
location number one but if we were to
pass on maybe the test slot of zero
because it's always going to be indexed
zero you can see that what is returning
is I love Devcon I am super but then it
stops over there but if let's say we
were to create a while loop for it so as
long as while it's true we are able to
concatenate all of the string data
together uh it should be able to help us
concatenate the entire string result
together and give us what we have passed
like I love Devcon I'm super excited to
be here with all of you you so that was
me like speed running it so let me dial
it back and then we kind of see step by
step of how we actually retrieve the L1
string so over here the L1 slot number
is still at location number one the slot
sequence here I've noted it as zero
because it all starts at zero but init
but eventually we're going to add the
sequence sequencing to just keep adding
it incrementally so that it can fully
concatenate itself we're going to be
defining string Ming string result as
empty at the start of it and while it's
true again we're going to be making a
lowlevel call over here and this is
where it gets a little bit more
interesting we have the l1s load
contract address but I've heard some
from from the audience mentioning that
we have to Hash it exactly that is
correct we're going to Hash it and then
we're going to type cast it to U 256 and
then we're going to add the slot
sequence to it so whenever that is true
we're going to incrementally increase
the slot sequence because we know that
there are still more information after
that slot and what it looks like is
because if us hashing this data
subsequently if let's say it returns
similar like
breaks as long as it stays true it's
just going to concatenate everything and
return the string result so this is like
a high level of how we can actually
concatenate everything and retrieve the
L1 string result
here okay okay so again all of this
information we have this code directly
available inside the L2 contract here so
for devs out there who are excited to
just get started with like tinkering
with this here's one for all of you okay
and then for the third piece third and
final one I know I'm putting everyone to
sleep right now we're going to try to
make it fun for the last one okay so for
the last one over here we have the al2
contract Advanced type here and we're
going to replace this with this contract
all right so for this year it will be a
lot more interesting because we'll say
that this is a bit more complex uh with
different ways of actually querying the
information but very similar similarly
as well we're still defining the L1 SL
pre-compile address up front over here
already and the L1 SL contract address
is because when we instantiating this
contract it's directly using the L1
contract address and and so that it
stays as a global variable here we're
also defining the L1 profile struct
already which means that we kind of need
to create the data type for L1 is an L1
profile stru take it in a way that we
are creating profiles for our people
this is a simulation and an example of
this so over here if let's say we were
to retrieve fix L1 array we're going to
be walking through the first information
uh first I would say retrieve function
step by step where passing the variable
storage slot in this case this variable
storage slot will be referencing L1
contract where this storage slot
location is and then afterwards
similarly because it's an array the way
to access it is that there is going to
be subsequent location that it is stored
in so what I've done is we just like
added in of course there like different
ways of approaching it but I felt like
it was a fun way to also get the
audiences like engage to see where
people think the storage slots are but
everyone is so smart so I think they're
G to get it so very quickly if I were to
just kind of get the audience to think
about where do we think is the L1 fix
rate storage slot
at this is storage
slot three dang that's good all right
three okay and maybe just a quick one
we're going to plug this information in
if we are going for retrieve fix array
element here and we say that the storage
slot is storage slot number three and
then array slot would be I'll say zero
because it's all zero index and we call
it you're going to get three because
three was already instantiated in the
contract here as position uh three as
well storage slot three but what about
for six and N where is the storage slot
for six and
N four and five I hear four and five
that's cool so let's give this a try we
can go to the contract
here and because what I've done is one
way to think about it is it's just going
to be added sequentially during the
contract instantiation so when we are
creating the contract already deploying
it there's like three six and nine so
three itself would be occupying one
story slot six would be occupying
another and nine would be occupying the
subsequent one so what I've done here is
that when 3 + one is essentially storage
slot number four and you're going to be
retrieving six as uh the return result
over here and the way to access this
information you're going to start seeing
very repetitive type of syntax it's also
encode uh using ABI in code pack where
we access the L1 contract address which
is from L1 contract and in this case
it's just a variable storage slot plus
array slot again we can always argue
that we don't need array slot the reason
I've added that in here is just to show
what it's what we're really thinking
about we just like adding the array slot
based off of the length of the array but
in this case actually for variable
storage slot we could have just
mentioned that this is variable storage
slot of four but the array slot let's
just say if it's zero we should still
just be getting six because technically
this is storage slot of four yes so we
still be getting
six subsequently if we look at Dynamic
array Dynamic array gets a little bit
more interesting because during contract
instantiation time it's more of the
length of the array that gets recorded
uh into the storage plot itself but the
data is itself is stored somewhere else
which we will need to access it
differently so if we look at this lowle
call over here it's actually ABI and
cack and then we have the R1 contract
address and then we are hashing this
variable storage slot and then we are
actually adding subsequent array index
on top of it in order to for us to get
this to retrieve the dynamic array
number so if we were to look at an
example over here for if we look at L1
contract so we jumped into like Dynamic
array over here yes we jumped over to
Dynamic array very quickly what do
people think is the L1 fixed array to
storage
slot
six is it six S 8 and N
though why is it not 6 Seven 8 and
N sorry
it comes up to you in 256 yes that's
correct so actually this occupies at one
storage slot by itself so just storage
slot six again I feel like the reference
from the visual representation visual
illustration from Peter using like
Foundry to check out this storage slot
that is like really helpful to also look
at it but this is also us going through
the example through the lenses Like
Remix and see what we can actually
identify so the storage slot here for L1
Dynamic array it is actually yes storage
slot seven then so for us to access the
storage slot seven over here it's going
to we're going to pass seven as the
input and then for array index here it's
going to be zero and then when we call
it we're going to be getting 100 and 100
matches with what we've instantiated
also as 100 over here but the way that
it is uh the way for us to actually
sequentially call the variable the in
the the information of in this this case
the U 256 information we're going to be
adding incrementally plus one because
that's how the information is packed in
the storage slot so it gets hashed and
then it gets type casted you in 256
every subsequent number that gets pushed
onto that array it will be occupying
that uh slot respectively for the value
so even though when we push new
information on top of dynamic array that
is we just have to add a subsequent new
uh increment plus one to array index and
we're able to access that information
and fetch it when it comes to decoding
this data it's really I would say um the
same type of syntax that we see for
retrieve L1 number Abid de code data and
UN in
mapping is a interesting one but because
this example here L1 address to mapping
this is fairly straightforward we have
the L1 address to number mapping which
Maps this contract which was
instantiated already the same address
will then give you a value of 100 so uh
with respect to time I think I only have
everyone will be able to like reference
this information over here I will skip
through retrieve L1 address to mapping
but instead we're going to go through a
cooler example which I think has seen a
lot of use case and a lot more uh
interest which is when we're trying to
retrieve and resolve ens handle there
was some feedback mentioning that there
were there are lot of um nested mapping
used inside of ens contract some of the
feedback that we've also gotten was that
it was relatively over engineered I I'm
not too sure but to some extent we would
use L1 SL load gives you the capability
to access and resolve your ESS handle at
L1 at the layer one itself right so for
this function when we call the retrieve
L1 nested mapping this will be a bit
more interesting in a sense that we have
mapping address as a variable and also
mapping string and where do both of
these uh arguments come from is that if
we look at nested mapping here where do
we go so for L1 nested mapping it's
essentially like an address that maps to
another mapping of string to then
finally resolve it to a u 256 so for us
to act to resolve to the final U 256
result there's like multiple ways that
we have to first hash the slot in order
for us to access that information so
because there is two levels of mapping
over here would say so we're going to
have to
first first hash the initial slot and in
this case would be like K 256 and then
similar syntax ab and cod pack we have
our U 256 here with the mapping address
mapping address this will be the address
that maps to this new mapping of string
to you in 256 and we're going to have to
like pass on the variable storage slot
now do note that in this context over
here you'll notice that this method of
concatenation is that the variable
storage slot comes later after the
mapping address so the way of hashing it
the way of accessing mapping is that we
first structure the input I would say to
the left and then the variable storage
slot like to the right over here and
then as you have multiple levels of
mapping you would add on uh additional
levels here so for example like buy stud
through initial slot and then maybe I'll
buy stud through like second initial
slot and so on and so
forth and then once we have the final
slot over here we're just passing the
final slot information into our lowle
call and then since it's a u 256 we're
then able to like decode this
information directly so let's give this
a try over here for L1 contract we
have initiated it with this address ABC
and also 1,000 and it should be
returning a value of 1,000 so this L1
contract it is over here and we have
retrieve L1 nested mapping here
we will pass
on address here first and again for L1
contract this is storage slot seven so
we'll pass on seven here and for string
what's for string
ABC let's do
ABC ah but when we call with ABC we're
getting a value of zero does anyone know
why okay I'm getting everyone like those
off so answer the question because we're
going to have to follow exactly more
like a check something I would say where
we have to follow exactly what was being
passed in this case it's supposed to be
like ABC uh let's see then we have this
call then we should be able to retrieve
this
information let's
see contract address whoops that is is
not storage slot of seven because for
nested mapping it goes to
n we call it there we go the value comes
up to 1,000 so for those of you who are
interested in understanding how to
access nested mapping this is a good
example for you to start diving deep
into for the last example I know I only
have like 17 minutes left I'm going to
like speedrun this so for the final
function here for retrieving stru this
is actually the same one we have seen
the same syntax like previously and this
actually goes back to mapping so when we
look at how
the mapping
for here we
go going
through here so for
mapping no not mapping my bad this is
with array index it's very similar
because the way that it is
yeah so for like Dynamic array number
the way that Dynamic array stores its
value the way that it accesses the
storage slots Dynamic array they're very
similar to stru actually exactly the
same so for example I'm going to
Showcase a quick example over here
for retrieving stru the variable storage
slot we're going to look into this again
we have seven here and then for address
to number we're going to say eight and
then here we're going to say nine but
for l one profile Str do we think that
this also occupies a storage
slot no the answer is no so I'll say no
and then over here it's actually storage
slot of 10 and finally over here if we
were to showcase the example of this
whoop so for retrieving struct here it's
going to be variable storage slot of 10
and if we pass in zero as the array
index we'll be able to get this value in
bytes but this is so interesting because
the payload that we Define it comes out
in bites so this could be like a
homework for everyone to kind of like
test it out because this contract is
already written you can see that how you
can access this information but I've
also created some utils over here for us
to convert for example like bytes to
string so if I pass the btes value that
we' pass in you can see that it returns
like Alice in this case so these are
basically just like a set of contracts
already written in solidity for us to
see what it is like implementing and
trying to extract information from L1
using uh two different types of data
types and two different types of data
structure so yeah this is all I have
does anyone have any questions or do we
want to like go through everything first
then take questions later yeah
yes using the gas cost I remember
reading that there were some but maybe
I'm going to like get get Peter to also
like but for like a general call usually
there's no guas calls
yeah but I do remember there was also a
topic on this but I will lean on to like
Peter to also like talk a little bit
about this that's a good question thank
you oh yes you
have yes
come again it
will yes
is it
okay yeah so we can probably spend the
rest of the time on questions uh there
are some interesting questions in the in
the form two so I I believe your
question maybe there were two questions
but the second one was why do we need to
have all this MPT verification
yeah so you as the L1 if you run an L1
validator you know exactly the state but
you as the L2 node or us as the L2
contract you don't so what that means is
the sequencer returns some value to you
to the contract Coler but the sequencer
could just make up a value uh we don't
want to allow that so that's why the
sequencer as part of the verification
could be fraud proof could be ZK proof
it must provide the proof saying that
hey I I gave you this value and this is
the actual value stored in our
one uh it's much stronger than an oracle
I guess so I would say the sequencer
optimistically relay this information at
this point you can view this as an
oracle but you also verify it eventually
so uh there's like a period where you
cannot trust the sequencer and then
eventually you verify it so the so
longterm canot
cheat so if you have two contracts let's
say on the same blockchain on
out2 uh if one of the contracts exposes
the storage let's say a view method then
you can read it if it doesn't then you
cannot so usually you would need to call
RPC uh so that that would be another
interesting proposal just let letting
you to read arbitrary slot from other
contracts maybe that's a bit too
invasive uh it's useful for as a
building block between R1 and R2 I
believe but for L2 to L2 applications or
L1 to L1 applications I'm not sure if
this is super
useful um yeah the proof of inclusion is
just a verification so that's kind of
the Second Step I think there's a
related question before we we go to
other questions someone asked Can can I
utilize L1 to call a view function on a
contract that's an excellent question
because there was an other proposal
that's called L1 call which is exactly
about that so you would call this also
pre-compile uh frame Al to contract but
instead of this very lowlevel access to
storage you would trigger a view
function which is much more powerful and
safe in a way the problem with that is
that it's much easier to verify it so
for instance scroll we have a type 2 zkm
ZK evm currently we have our own prover
and it works for scroll
but for L1 call you would need to spin
up like a whole different execution
environment a type 1 zkm and and create
a proof for that single call and
aggregate that proof together with your
original proof it's not impossible but I
don't think it's practical at this point
so a andot kind of fills the gap of
giving you something useful and
practical uh but it's not as convenient
as as a as a
call um I think we we had a question
somewhere there
if
not yeah
goe yeah so that's one of the
prerequisites that I said is that the L2
should have a notion of the latest L1
block and the way we would implement it
is that the sequencer of scroll relays
blocks from i1 now how recent these
blocks are is kind of a security
parameter of the system if you wait for
finalization that's the safest but then
you have to wait there's like a delay of
relaying information of like 10 to 15
minutes if the sequencer is waiting for
a couple of confirmations then there
must be a mechanism in the in the rollup
that reworks if i1 reworks so
the right so the the sequencer relays
the album block hash is to L2 so
basically you could also read directly
the L2 State root or the L2 L1 block
hash sorry L1 State root and L1 block
hash from L2 State and that's what kind
of L1 slot gets access to but it's a
very valid question actually uh that's
one of the open questions like the
sequencer could just stop relaying this
information uh currently there's no
mechanism to to force the hands of the
sequencer to keep relaying information
so it's possible that you read stale
information uh we need to do additional
work to support applications where this
could break break them but in most cases
you could assume that the data that you
read is maybe five 10 15 minutes ago
from
ethereum uh another
question right no worries uh just a few
I think we're about to wrap up I don't
want to take any time from the next
section
just uh you mean the road map like
moving on or
yeah so we we do have an implementation
and that's what I linked before so we do
have this devet but it's not production
ready yet so that's why it's only a
devet it's not part of our test net and
Main net uh there's still a few rough
edges that we need to figure out and
also we don't want to deploy it on Main
not until at least two rollups adopted
like this is only really useful if if
multiple at2 support it and to to say
say why I just want to mention that we
have a third example that we didn't uh
get to today if you open the repo then
you can see it and it's a key store the
idea of of the key store is that you you
you know we live in a multi-chain world
so you might have your wallet your AA
wallet some whatever you prefer on
multiple chains uh and you know it's
usually a multi so you can have uh
multiple assigners multiple Keys
associated with it now in this multi
chamber this becomes very um
inconvenient to maintain if you want to
add the key or remove a key you need to
do this again and again for all of the
chains and it can be you know five 10
different chains so the idea of the key
store is that let's say you have a key
store contract on L1 and it the whole
purpose is to to manage case you can add
them remove case and all your wallets
that are deployed on again optimism
scroll arbitrum they read which are the
authorized key from i1 and they just use
this so you can update it in one place
and it automatically updates with some
delay on all these other chains so um
that's kind of to show an example why
it's only useful if it's multiple
rollups that's supporting it because
these use cases are really unlocked by
feature yes so each each of the rollups
would need to implement it and because
rollups work differently there might be
so the specification and the inter
interface would be the same but the
details of how it works might be
different from rollup to rollup so
that's kind of an implementation detail
that that's left to the rollup team
uh apologies there's a bunch of
questions that we didn't have time to
answer uh if any of you are interested
either devs or Procol maintainers who
are interested in adopting this I'd love
to chat with you so find me anytime
after this session or or later and we
also have another session on Thursday
all for today thank
you for
e for
that for
AG
the I
be for
I for
see
almost
need is the battery
Avail I can't see
we have a
this will k
test test test uh
do test test
test
test test test test
okaying okay so please now all the team
member go to one pod take one pod
everyone all the team member take one
pod for yourself
m
uh
e e
so please please everyone if if you are
on a pod and you uh and you don't have
so if you on a pod please raise your
hand if you are the one who is leading
the Pod raise your hand if you are
leading the
Pod you are leading the Pod here what's
Happening
Here
what so you reading the Pod right so I
think here there is a bunch of people
here they don't have coins right if you
don't
which way here you don't have coin there
so if you are seated far away from the
token please stand up and go sit where
there are tokens if you are not near
tokens you not be able to participate so
all this side of the room over there is
going to be closed like all of that is
going to be empty please stand up and go
near where there are
tokens and I need the
wi
Wii I Wi-fi can youone know the
Wi-Fi can you give me a Wi-Fi I know if
mine oh can you give me a Wi-Fi I don't
know if mine is going to work I can try
but um no no there has been some
issue wa can we share the
Wi-Fi I will get
spot that the Wi-Fi of the confence yes
but what is it you have Garden what what
uh what
that the infinite
Garden not connecting
test test test so everyone so all the
people who are there in near
tokens oh okay so you have tokens here
you have tokens here do you have tokens
there well you are way too many here
they don't have cards they don't have
cards so this is going to close this is
closed please go get out of this find
some place where uh there are there are
people this is closed this this this one
this Ro is closed
okay
and are you seated in a are you SE in a
pod what is your pod there is someone
here oh you're taking
this okay
so can you take uh can you take this pod
take this
pod no you need to take a pod like take
your
POD mean do you have your
POD mean take the
Pod
okay so let's start so hi everyone so hi
everyone so today we're going to learn
about prediction market and you're going
to be able to to try your prediction
Market live so let's start so the goal
is to learn about prediction market and
outcome tokens and you go what the other
player have you don't want to have more
token than the other you just want to
get the highest amount of token for
yourself so prediction Market Basics so
what is a prediction Market prediction
Market is a way to make prediction about
the future uh using markets where people
can place order on what will happen so
for example who will win the US election
you can get tokens of trump you can get
token of Aris and if Trump wins well the
Trump token will redeem for some money
if Aris wins the Aris token will redeem
for some money and by looking at the
price of the token you can make
prediction about the
future so this can also allow you to get
more complex signal such as for example
what will be the price of Bitcoin if
Aris wins versus what will be the price
price of Bitcoin if Trump
wins and what do we need to make a
prediction market so you need a question
you need a list of
outcomes like who will win the election
for example you need an oracle you need
a way to report the outcome of this
market so for example reality or and
claros and I see the reality F there and
lot of claros Team there you need a time
where you can start uh to uh resolve the
market and obviously you need to get the
underlying token what you will earn if
your prediction is
successful so the basic of prediction
Market you will have one token that we
call the underlying token so here in my
side it's die where you are here uh is
going to be the coin that you have you
put it into this market and then you
will get one token of each of the
potential outcomes so here you put some
die and then you get some tokens for the
Democrats winning the election the
Republican winning the election or some
else winning the election and when you
look at the price of the tokens that
gives you some probability of this
particular event
happening so we're going to start our
first game so before that everyone take
for 500 worth of coin so pod leader give
pod 500 worths of coins to everyone in
your pod
oh we don't have any part leader
there who the P leader there is no P
leader there wait uh can you can you be
leader
there yeah this SP
what's happening the people at the back
are empty they need someone there or I
could ask ifone to get up and there is
no but leader over there do they have
they have the coin or not they have
coins
yeah uh maybe Mick Mick can you take
pod they have do they have cards no you
don't have cards there is nothing here I
don't know how you even got the coin so
if you want to play you have to go in
some other P this has to be empty
so now pod leaders take the first sheet
of mm which is C and dog and put a token
where it's in bold italan bold on both
of the markets put a token where it's in
bold everybody has 500 yeah you have to
take the sheet here and the cat and dog
the C cat and dog everyone take a cat
and
dog is there a poer here there is no
here uh
wait yeah you take it and you put a coin
I gave you a coin on the B stuff
so put the coins so put the
coins put the coins there you don't yeah
this small coins you put the small coin
for the amm you have
it you have
it you have it you have it okay this is
working there you have it you have
everything okay you have here okay
what need to repeat the first basics of
the am like just the first moment they
should be P leader everywhere and they
should be P leader everywhere like pod
leaders who should be able to uh ex
am so if any part has some issue and do
not have the dog the C dog paper raise
your hand
if anybody has an
issue okay so as the market maker sheet
okay so now what you can do you can buy
cat tokens if you think that it's a cat
or you can buy dog token if you think
that it's a dog and the price is given
to you on the am
sheet and what you can also do if you
wish you can give a 100 coins and get a
complete set of both so you have open uh
the Box a right you have all the Box a
okay so now you can start to trade on
with this amm buying or selling tokens
of cat and
dogs and if you have any question at any
point don't hesitate to raise your
hand yeah
how does m work so you have the you have
your coins no you don't have your coin
wait wait let me I will come back with
why it was here was they not have the
coins so you need to have the coin here
on your cat and dog so you have the
coins here okay
so this means that you can from the bank
you can buy token of cat at 50 and then
you move it up or you you can buy token
of dog at 50 and then you move it up
and yes and you have to open the box a
has everyone open the box a p leaders
have you opened the box
a yeah open the box a and you will see
the token no no that's that's the Box a
so here we need a p leader uh P can you
be P leader
there just take a seat here and uh take
a seat and Lead this
pod so what is here we don't have P
here where is the PO
leader are you leading a pole are you
leading a
pod uh so here so each chip uh each 100
uh they they get one that's the cat and
dog ones you have the cat and dog in box
a so here yourself bu you can buy at
this price and you can sell at the price
just above any amount or one by
one you can have like if multiple people
want to buy at the same time
yes can I shove on that or how what's my
what size can I bet before it moves the
you can do one by one so you
have how much size can I put in before
it moves it's already one by one so you
have to pay 50 you pay 50 50 okay that's
my Max size I can do at this price and
now it's moving yeah okay you put that
back into the bank
okay I'm
a you're going to be bag
holding you get the cat cat bag here is
going to um the catch thanks for the
exit
liquidity the dog price is too good
now so do we any way we can understand
what yeah because there should be a p
leader here why don't we have a p leader
here oh you are here right okay can you
leave this SP yeah yeah
yeah so it's
yeah do you have a PO oh yeah you have a
poer here
yes yeah you have the coin okay put it
and start to under your
P okay here well what here's the Reas
you have the P so oh thank you you are
starting here and every time you move
you are going to move the the
coin and what you can also do is you can
give 100 and get a complete set so both
a cat and a dog if you want to sell them
after
what cart and dogs are in the card set
in the pack a it's in the pack
a yeah open it it's inside
so CL can you take this p take the sh
the sh here and take this
SP
so so how uh if they give me 100 they
should get one if they give you 100 they
they get that and then the cat also okay
so for for example he's giving me a 100
yeah uh so so what what do I do what do
you want to do you want to buy cat or
you want to buy dog buy cat so you can
you can only give 50 you give 50 and you
will get one token of cat Okay 50 you
get the token of the small small one 100
one you just put it in the in the
bank have 60 for cat now now you have to
pay 60 for cat or what you can do if you
want you can pay 100 and you get a
complete set so you get both cat and
dogs you can use it to sell it but to
sell it you sell to the price above you
buy to the current price and you sell to
the price which is just
above
buy no you can either buy to the amm
here you either buy to the amm okay or
you are minting a complete set so you
give 100 and you get
both
yes if you put 200 you will get both of
those yeah you will get both sets you
get both sets if you put
you want to take a
position no no you can s it here to the
amm you can go and sell it there yeah uh
wait
here uh you need to be in the middle of
the Pod it's not going to work
otherwise go to the middle of the Pod
yeah can can you yeah move move one one
here can you both move one on the right
and and go
here so what's happening here are
you okay but still at
yeah understand so are you in a pod
where there is a pod
leader do you have a pod leader here or
no if you don't have a pod leader go to
a pod where there is a pod
leader oh you're the Pod leader okay so
yeah are you under the can you please
explain this so so we can we can we can
pay 100 the
market and one dog if you pay 100 you
get one cat and one dog right or you can
pay to the market maker the current
price but you will get only one side and
when you do that you're going to move
the
token okay if you buy one cat is going
to the next cat is going to cost 60
right do we have to buy sell you can
also sell but you sell to the price
which is above and also you move the
token yeah like the bank is going to
give you back the
money the bank can do the you have the
bank yes go here and you will give back
money so you what do you want to buy you
want to buy a cat or a
dog okay let's start you want to buy a
cat so you give
back and you want it to get a cat and
now it's move and now the next cat is
going to cost
the yeah the 100 cat
yeah this is the dog yeah and you can
buy it and it's
moved it's independent yeah
okay what so what what are you do what
are you here do you have a leer here you
don't have a p leader here right oh no
you the leader
right are you the P
leader so you have cat and
dogs we don't have the C we all
give okay so you have opened the box a
you gave the Box a
there no so you have the cat and dogs
over
there so what have what have you done
like you you split into how many pods
here are you many how many
pod yeah just do one pod uh no like we
should do two pod we had to
they have no
leader they have no none
of so can you do a can you do
there all three but different why do we
have three things here what is that why
is that this first this is not the
you should go down by how much what you
put in was effective possible to buy or
sale more than one no one by one one by
one yeah prediction
Market but it's going to be hard to get
if you are just arrive now like it's
already way more people than expected so
I can't get anyone in sorry
yeah does the price of one token
influence the other no
no so you what you can also do you can
give 100 and get a set of both
tokens
yeah so if you want you can give 100 to
the bank and get both cat and dogs that
can be useful if you want to sell them
because here the price of both are
increasing so you can get some profit by
giving UND getting both a cat and a dog
and selling both
yeah is that correct
yeah so here there is nothing right
I sell it at 7 right not at 0 yeah you
sell it to the price just up yeah and
you're moving the price
IAS you sell both yeah and so you pay
one so you got 40 of
profit so it's not buying it's a minting
so you are meaning complete sets
yeah for 100 you get
both no matter what the price yeah
so do you have the leader
here and that's the current uh okay and
it's it's back to 50/50 right it moved
up and down it's back to 5050
okay okay why is the price
t50 did you
do okay
okay okay so
what what do you want to buy cat or
dogs you want to buy dogs
right
so where are your
tokens where are
so and where are the cats where are the
cats uh over there why are the cats over
there like are you okay you got no one
oh I I got the one understand so the
here is the C is a cat and dog right yes
okay because this card is both like
there's a two category inside head and
the dog yeah so we didn't know this card
have to become to B it's by this
one so he going to like
Ju Just mer the Pod like just go all
around in the middle and Mer your pod do
only one pod you you only have like one
set of card do only it's only one pod
yeah okay
so everyone move toward the center to
make your
pod put this in the center so the you
need
a put this here okay need
this you have your cheap right yeah 500
so now you can buy cats and you can buy
dogs so have to separate out the
C so you have the bank right do you
think you can under the Pod huh you can
under the
Pod you can under the
Pod how so you are playing the bank
right okay so if you are there please go
closer if you are theree please go
closer this P does not exist this is a
p so I become
so you want to
buy uh cat Okay so if you want to buy
cat where are the cats
here
cat and then the price of the cat is
increible
okay everybody can do the same thing and
get tokens of cats or
dogs okay so right now if 60 if you want
to buy buy cat I have to pay 60 right no
you have to pay 60 to buy a cat then
going to 70 and it's going to go to 70
yes this doesn't move this doesn't move
no but what you can do at any time is
you can pay 100 to get a set of both
cats and
okay this is first round this is only
only one card no matter how much I buy
also one card how much what no matter
how much I bought also one one kind of
name you will get 100 if it's a
cat no uh if it's a cat you will get 100
okay so let's say he want to buy have to
buy 60 and then he will get one
card yeah now you bu 60 I get you get
one
cat and this is going
up okay
here a consensus yeah yeah that's okay
that that's
good we
have so what you can do is you can pay
this case you can make some profit
right oh no no actually it's okay yeah
no so if you pay 100 you will get both
and you can sell it back to the market
and you can no you can sell it only you
sell it to the app so you will sell it
only for 90 so it's not going to
work it's going to work but you're going
to lose money so for now the the prices
are
good yeah hey one question yeah can you
meet multiple times yes you can many
as many times so there's not
one show show me no no I
me the theual talk is
normal so what's happening in this
P if we if we sell if we sell a dog yeah
we we get 50 no you get the price up so
we will get 40 only I 40 you get 40 only
so sell one by one so you sell one dog
right so it's going to go here and you
get 40 ah
okay so you get
okay now now it's your
turn you can like as long as there is no
multiple people want to play at the same
time you can play whenever you want if
you multiple make a queue but uh do do
we need do we need that to to up 100
always no no no it doesn't need to S to
okay okay so oh you you this part is
working and you are you you stay at
yeah you can trade with other player if
you wish it's
okay meting does not move the price no
it's yeah it doesn't need to Su up
now it's a price
yeah okay so everyone
finish so please if you have any last
question tell me before we finish the
first uh
round
what what is it
okay any last
question is there any last
question all the are
working okay okay
so everyone we're going to now uh stop
the amm oh last order we're gonna stop
amm last order last
order do we have a last order
okay so every everything is done
perfect so please pod leader close the
am and so now we're going to uh first if
you if the price of the dog in your pod
yeah you the ammr closed it's not
possible to trade anymore is the price
of the dog is higher in your pod raise
the hand of the dog is higher raise your
hand
here's the dogs are higher the dogs are
higher here
okay the dogs are higher okay if the
cats are higher raise your hand if your
pod has cat price higher raise your hand
okay cat price cat
price so we see four pods with cats
being higher and three with dogs being
higher and so now you will get the
reveal and that was a cat
so now if you have dog tokens they are
worth
nothing and if you have cat tokens you
can redeem them for the amount of Point
return on
them 5050 oh okay okay
wely they are asking if they can keep
the card as a souvenir or yeah it's okay
they can keep the card it's okay
okay so did you all manage to redeem if
there is any question raise your
hand so no question and let's go to the
next
element so now we're going to open
another
market so this is going to be a market
about whether or not I'm going to say
the word there in the
mic if I'm going to say the word there
in the mic so if within 10 slide I say
world this specific token the token on
the left is redeem otherwise that will
be the other token which will
redeem so all all the Pod remove the cat
and dog amm this amm is over and take
the second
amm about this particular world that I
can't say or maybe I will say it we will
that are you trying to trick me
so if this world if I say the word if I
say the world you will get the token on
the left which will redeem if I don't
say it within 20 slide you will get the
token on the right which will
redeem and P P where is the
suitcase I need the suitcase because
there is your stuff inside I need the
suitcase where is the
suitcase you have to find that as soon
as possible because it disappeared it's
like under during the
workshop no you can keep the
C
yeah is the question is whether or not I
will say this word
someone is trying to trick
me
where's oh
what happened
where where is the content on my
suitcase yeah the content
disappeared like I have some content for
the workshop whicha
uh that's probably number four
five it's it's okay I it's okay I have
everything
so why
interesting so why interesting things
because I see a bunch of people trying
to make me say the
word so it's not necessarily the main
goal of prediction Market but you could
potentially use prediction Market to
incentivize some particular stakeholder
to do a particular thing
you you could see that so here we have a
participant uh we saying that it's a
something similar to assassination
Market I don't think Poli Market are
very suitable to make assassination
Market but they could inadvertently
become one and that's why you have to
make sure that your rule do not allow
that so for example in claros we have as
an arbitrator we have a set of rule on
what we can rule and what we cannot rule
on and Market which are antical are
going to be uh rule as invalid so they
will not resolve
normally and this for example happened a
couple of week ago where you had a
question about some amas leader being
removed like about some amas leader
being control of amas and obviously the
most likely way that he will not be in
control will be him being killed so here
the Oracle returned that it was the
invalid
Market
yeah
yeah so for us if the main source of
uncertainty is something which is
immoral we will refuse to arbitrate
if there is other sources of uncertainty
like for example if Trump was
assassinated before the election we'll
probably arbitrate because the main
uncertainty is not whether Trump will be
killed it's whether he will win the
election or not so the main source of
uncertainty is the vote of the American
people not a potential assassination so
there we would have ruled on this Market
well at least that's that for me I would
have ruled this Market valid as valid
yeah you you trade with in your pod only
with in your pod yeah
yeah sometimes they want to say in the A
and yeah if you if you sell you sell to
the price just above
so if you sell you sell to the price
above and you move it
yeah it doesn't need to be balanced the
market do not need to be balanced if the
market are unbalanced what you can do is
give a 100 coin and get a token of both
and you can make some
profit if you want you can give a 100
coin and get both
tokens and then you can sell
them you can always get both for
yeah if you want you can also you can
also give those back and get
you have to give a complete
set you get the price just
above okay just above yeah just above
no okay so sometime markets do not
resolve immediately so this Market is
going to stay on because for now it's
still undetermined we still don't know
if I'm going to say the word or not uh
and we're I go to another
market so another type of Market please
everyone everyone we're going to
explain please everyone silence a bit
thank you yeah so another type of Market
uh is scalar market so event but we can
also try to predict values so for
example here we will want to predict the
inflation in 2015 and to do that we set
up a range we can say from 0o to
and down token so if the inflation is
higher than
the inflation is lower or 0% the down
token is going to redeem but if the
inflation is actually within the range
so between 0o and
proportionally so if it's 8% the up
token is going to redeem for uh 80 cent
and the da token is going to redeem for
that's how you can estimate value and if
you saw at the start of the workshop I
was showing you the Bitcoin price market
and this was the scalar Market to
estimate the value of the Bitcoin
price so now we're going to go to this
Market about my age so you can go on the
age market and the goal is to find uh
all I am so if I'm like 40 for example
the up token will be redeem for 40 and
the done token will redeem for
Market the previous Market about the
world it's still open you can still
trade on it if you want at some
point so open the speaker age
market and in this
market you you obviously know I'm not a
negative age and I'm not 100 years old
so so the tokens are going to redeem not
completely both token are going to
redeem but you you don't know exactly
for how much so if I'm older the up
token is going to read more if I'm
younger the down token is going to read
more
yeah that's
E I know but I'm not going to reveal it
at least not yet
you have B you don't have B I can't give
you a
b don't have the speaker on we don't
have speakers
or
and so if you missing it I have a b is
candle B is
candle multile no there multiple in each
pack okay it's not only one thing so you
have it this is uh pack B so you have it
in the P also
we
don't Tok is that 70 the starting prices
for these so
starting there okay so what which token
you want to
buy so you want to buy okay so you pay
the no that's the weight that's not this
this is
the that was an a
so if you bu so so here you are not
necessarily betting on something in the
abstract
exactly so you should have your like for
yourself you should have some estimate
of what is my age you look at the market
is the market correct don't do
anything if the market you think is
incorrect you can either buy up or down
whether or not you think this Market is
too high or too low this Market
it says I'm 32 yeah here I say I'm 32
exactly this is the price of the da
token the da token is going to redeem
age
so so if you think that I am younger if
you think that I am younger than 30 you
can buy the da token
yeah you one minute I just yeah I just
came late so I going to end the session
so what is this game all about okay can
you pick up a pod pick up a pod and ask
the the Pod
leader you need an Oracle and I'm
walking at Clos which is Oracle
nice hi
speak let me see your
face gu okay I I saved two days ago
AIT
what the maximum is
my age the age Don token is redeeming
for 100 minus my
yeah this is one is younger here AG this
is age up no no no age down this one is
age down age
down
yeah you so here it's not about exact
just what you think it's about whether
you think the market is overvaluing or
under valuing so here you have 68
so if you think that I am uh younger
than no younger than
do 100 minus the price if you think that
I am younger than 32 you should buy and
if you think that I am older than 30 you
should buy the up token
okay think I get
it so how old do you think I am 34 or
yes you need
what
so here you are not making a bet in the
abstract but you are predicting whether
uh my age is is higher or lower than
what this Market is currently giving
currently the market is giving 30 so if
you think that I am older than 30 you
should buy the age up token if you think
that I am younger than uh how you how
much you have to pay for that then how
much do I to pay
for well it's here you can see
here so if you want to buy the age up
token it's uh
so if you think that my age is above 30
you will make some profit but if my age
is under if it's under 30 you will lose
some money so you are not making a
prediction in the abstract you are
predicting toward the value not just an
outcome to the value and for that you
have to look at market
prices the ede up is the one with the
old guy and the edge down is the guy
with one with a young guy
so I'm 34 here
okay I'm 36 here
yeah so if you think that I'm older than
to redeem for my age if you think that I
am younger you can buy age down okay
because so that's because a DA is going
to redeem for 100 minus my
age no just put this one this one is
just just like three this one is just
three of
this so don't don't bother with this one
just in case you had too many people
but this is the token you want to use
yeah yeah so here you have to look at
the market and if you think the market
is underestimating or overestimating my
age so here if you think that I am older
than 30 you should buy up if you think
that I am younger you should buy
down you done so it's you for now you
have to pay
age this one is 100 minus my age this
one is my
yeah yeah it's
sell the age down if you want to so to
Mint a complete set you give 100 and you
get
yeah much diverging that's a profitable
strategy to give her and get both
sometime you can make profit by doing
that Tove to your act to my age yeah
okay if you have any last question
before we close the
market okay so now we GNA we are closing
the age Market the World Market is still
there and I'm 32 so this means the up
token are going to redeem for 32 and the
down for for
to 36 so maybe on average maybe 33 so we
can see we had a pretty nice estimation
of my age with this
mechanism so you can redem your
token yeah if you have any question
don't hesitate to raise your hand and I
will come help
yeah from OG um claros is a let's say a
scalable version of ogre and also allows
different sort of use cases because we
have a a tree of quarts we have a tree
of
Courts yeah so Aur is just doing
prediction Market well well now he's not
doing much because it's more dead
uh but uh for claros you can have
prediction Market you can have anything
you can have curation
you can have some insurance and as a Jal
you're going to stti in a particular
court and you're going to be drawn in
only in the court that you are
specifically want to be participating in
and also contrary to um to Aur uh with
scaros you will um be randomly drawn you
don't Hall everyone to to stake on
anything it's only uh the draw which are
drawn so most of the time it takes only
a small amount of work from jals and
then
Aur is a bit similar butur also you
choose your own dispute why in Clos you
don't in Clos you choose your court but
not your only speed but both project
like both mechanism are pretty similar
uh because we are both taking we are
both taking this from trustcoin so
trustcoin was this Ching mechanism made
by po St except the guy was a maxi
Bitcoin Maxi so he never manag to itas
the it was Trust coin Trust coin set up
this mechanism initially uh but they
never release like the guy was wanted to
make it on bitcoin which was I think
invisible and uma uma is looking a bit
similar
mechanism um or it's a mix of both let's
say but it's you vot everyone vote on
everything but also keep in mind like
poly Market is using Uma uh but in
practice like they have some ad Min key
so it's not like a a real us
AG poly Market Oracle is working so is
making a call to Y um but also they have
some admin which can overrule Uma if
they want to and umaa is everyone V on
everything okay so now we have another
which is going to be a scalar Market the
weight market and uh here I have some
item that we can light to make smell uh
made by pon pon by the way uh and so
what you're going to do is you're going
to try to determine what is the weight
in gram of this
item someone still
trying so you have this item
what you have this item and you have to
try to determine the weight in gram of
this item so everyone take the weight
amm set up the weight amm you can still
keep the word amm the word amm is still
there and now you have the weight amm
where you want to
estimate the weight of this
item well if you are blind you should
probably not participate in the market
so if you want to see the
item I'm showing the
item no you cannot Fe it you can just
it yeah you can take a picture if you
want
to no you can touch but you cannot uh
it someone is trying to me again you
know
yeah that's the
item what is the weight in gram of this
item yes it is
only look only
look uh it's an item it's smelling nice
you can smell it you
know the
item it's uh to make some nice smell you
know you can smell it no don't don't
touch it because it will be unfair and I
don't have time
to it's done by my
girlfriend so the
item so you try to estimate how many
grams
n there is too many people so we will
not have time to get everyone to hey
someone is cheating someone is cheating
but you can take a picture if you want
to look at it a
lot it's just done by my girlfriend it's
not a brand like it's it's made in my
[Laughter]
kitchen uh this is the up token up
toen the wall thing it's the wall item
not just the wax the world item
so if the weight is above 40 gram you
can buy up if you think the weight is
below 50 gram you can buy the done token
only smell it
because it would be unfair I don't have
time to give it to everyone
so did you all manage to determine the
weight of this
candle keep in mind the markets are
still open the market are still
open
yes yeah the market are still open
the market are still open in
mind I it I'm the one who made it
what it's avilable I made
it want
to yeah they can by
yeah so keep in mind the
market still open
yeah this is still open you
can
yeah yeah that market was instantly
closed or no that's the point that's the
point I'm going to
make yeah it's still open yeah
yeah so keep in mind the market both
Market are still
open I can't un say it it's not possible
to UNS say it
yeah oh this one you can remove it's
finished
okay so now we're closing the CLE Market
the market of the CLE is
closed so everyone silence please
everyone silence please so here we had
this market and where I will say the
world
candle but the issue with this Market is
that we will not really know when we
will know because you will will not know
when I will say it and you will not know
when I will or you will not know when I
will go to slide 20 so for you it's good
you are Traders you can make some money
like you have something which is known
and you can get basically free money by
buying the token candle but for the
liquidity provider is very bad and so
for a lot of markets where we don't know
when we know it's extremely risky to put
liquidity because as soon as the answer
to the question is publicly known people
are going to jump on the amm and take
all the the token of the right answer so
here if you are here about the about the
candle immediately you're going to go to
a price of 100 and the amm is going to
sell some token which at this point it's
are publicly known to be worse 100 for
way less than 100 so that's why you see
most of the prediction Market will be
stuff like elections because election
you have a very uh cut of date where you
know when you know but if you are making
a market for example w the war in
Ukraine stop well you don't know when it
stop or it doesn't stop so for all those
markets it's tend to be extremely hard
to get liquidity so what you can do you
can sidiz the liquidity knowing that the
liqu provider will lose money but then
they should get more in the in the
liquidity
subsidies or we will need to have other
form of uh market makers which do not
allow you to just buy and sell at any
time so we are working also at with with
here on making some mix of am and
auction such that you have some one or
two hour to over beid other people who
are interacting with the market maker uh
specifically for Market where we don't
know when we know to make it way less
risky for liquidity providers so this
for now has not been implemented that
just like a research uh Direction but
it's a huge par for prediction Market uh
to provide liquidity uh the revolution
loss and so now on the weight of the
candle the
weight is 226
gam you
can but you can check here if you want
to if you don't try the orle you can
it's on the balance there if you want to
check so this means that the up token
are going to redeem for 100 and the Don
token redeem for zero
oh Market is done oh yeah the market
about the weight is uh
closed it's closed also yeah yeah so now
both Market are closed there is no open
market left and you can redeem the up
token on the price on the weight sorry
so e
okay so what do we what do you define
here uh we found a limitation of scalar
markets please everyone silence everyone
please so we found the limitation of
scalar markets in that you have to
specify
ranges and if your outcome is outside of
the range just using the market price is
not going to be very inform informative
um we even saw that on most pods the
price of the up was not even at 100 so
we see like here we have a huge Miss in
the prediction potential like if the
market was close to 100 you will have
gotten the information that the the
weight is probably 100 or more but here
it was not even
giving you uh scalar outcomes you need
to have initial range which are good and
it's only an estimator of the
value if this value Falls within the
range you have to make the assumption
that the value fall within the range if
there are some risk of the value falling
outside of the range you will end up
with a bias estimate of this value so
another limitation of of prediction
markets so now we're going to go to
scalar Market well multiscalar
market so what can we do we can estimate
we can estimate values but we can also
estimate proportions so for example we
can make a multiscalar market where we
want to estimate how many SE in the
Europe in the European Parliament with
each party will get so here you don't
take position on a particular value you
take a position on a particular share so
in the European Parliament well the
amount of of cities is fixed but here we
will see we will have a market where we
don't even know uh the the range the
potential range of of the value so let's
go to this
Market you can open uh the next two
boxes
and here we're going to try to estimate
how many participant do we have from
each continent so open take the
continent
amm in this room
yeah so the you want to estimate the
share of participant per continent in
room in this room yeah yeah I know at
the morning uh they gave give you the
global
amount or where we live or where we are
born so where you just were living
before coming
here oh no Let's do let's do where
you're born like where where are you
from like answer the question it's
subjective people may have different
answer to that the question is where
that I'm gonna ask is where are you
from e
you have to put one here
also oh okay as
what uh I can give you some you can come
pick some
here e
yeah in this room not the death gun in
this room
bet
with
take
that's the percentage not the amount
that's a
percentage and you may not even know
what is the total amount so here you are
estimating a percentage
both yeah so you're gonna need
to no it's gonna depend what people
answer so if they consider themselves
European or if they consider themselves
Asian
yeah okay so the market are
closing the market are closing and I'm
going to ask you
now so please everyone the market are
closing
do your last trade and the market are
closing okay can can you close the
market close the
market market are closed
everyone please silence silence everyone
please so if you are from Europe raise
your hand if you are from Europe 1 2 3 4
okay if you are from Asia raise your
hand one two three 4 5 6 7 8 9 10 11 12
if you are from North America raise your
hand one two
three four five five from North
America if you are from South America
raise your hand one 2 three four five
six
nine
nine oh in Europe I forgot to put myself
so that's
your hand one two two from
Africa and if you are from oania raise
your hand one one one one one okay
one so let's do the total
it's
okay so now you have the value that the
token will redeem the redeem for the
percentage not the absolute value the
redeem for the
percentage and what's interesting that
we can show that you really were good at
estimating that like I saw a bunch of
PODS where the price of Asia even went
to the max to the maximum amount of
value in the
amm so you can see that it's a very good
mechanism for doing estimation of the
future well here obviously I I can't
wait uh a week for a future event so I'm
showing you this event happening in a
couple of minutes but you can see that
here on this particular room the market
were very efficient in estimating
that so everyone you can redeem the
tokens yeah are
redeeming okay okay no no don't do the
mat it's already
written so you don't need to do the mat
I gave you the percentage on the in the
slide yes
yeah I gave you the percentage so they
each redeem for the
percentage
what it's based on the percentage I gave
token for each of your token you get 38
we have one last round after that no no
we have a bit more because they were
already late before I have the prompter
okay everyone
redeemed everyone
redeem so if you haven't redeeming your
pod raise your hand if you haven't
redeeming oh
okay wa
you redeem everything
redeemed okay so please everyone
everyone silence thank you please
everyone silence so for now we've been
using markets to make prediction about
future but the question is how can we
use those prediction to make a better
decision
so here in this example you will have a
market who will be the candidate of the
Democrat
Party and you will get a token of this
Market but then you can put this token
into another Market which will be which
party will win the election so here you
put some die you get some Biden token
you put the Biden token into another
market and now you get a token which
will redeem for die if Biden is a
candidate and the Democratic party win
election the other token they don't
trade for die they trade for the
underlying so here Biden so here you
have a Biden Democrat token that you
trade with Biden token and if this token
is worth 30 Biden token you have a
conditional probability that if Biden is
candidate the Democratic party would
have 30% chance of winning the
election so you can change the
market and what can you do with that
well we're going to start we're going to
start to show that so I need a volunteer
someone who is not vegan a non-vegan
volunteer
please non vegan
volunteer okay you can
come uh okay
so the volunteer will have the choice of
either trying a cricket snack or some
fried fish
skin and here we have two markets so one
market on what will he choose but after
trying it will give a a rating out of
that's going to be conditional Market
you will have a conditional Market on
what would be the rating given if he
picks the cricket or what would be the
rating given if he picks the
fishkin so you can open the
amm with uh crig or
fishkin and what is important is on the
first two token they are trading for
coins but then the other tokens they
don't trade for coins they trade for the
underlying
token so the first two tokens they trade
for coins the four last token they don't
trade for coins they trade for the
underlying token which is written on the
on the
sheet and if you have any question as
usual you can call
me uh you can participate in the market
yes but please don't tell
everyone and so keep in mind you can
always mint complete set if you want you
may not want to trade in the market of
what would be the snack chosen but you
may just want to trade on the
conditional Market on the rating
conditional on the particular snack
being
chosen I will be back I
just
oh minut okay okay
if you have any question raise your
yeah you have the token there can you
show the token yeah yeah you have F skin
but you have the smaller one you put the
smaller one here
to for some for the plums and for the
other things but not the
rating uh you don't have them here can
you check over there I think over there
and so here you have tokens of like 10
buying two token of 50 for example
for now you don't need to use a
paying you can get two token of 50 but
because this token you're going to you
can use it into those other
markets that's why we also give you
token of 10
and so here first you can get quicket
and fishkin and you you can open the
last box I think you will have in the
last box
yeah oh because they gave us as a
prompter with a timer here 520 520 was
the uh because like I have here like
it's giving like 17
minutes because the last team they
finish a bit later so I we don't have
the 10 minute to set up the the space
but it's going to be the last uh element
all do this one and after I finish
it
yeah and what will be the
rating if this is the particular snack
which is
chosen was the guy who was chosen no he
say he will come
back yeah
oh yeah he's back he's back
if you
think that's up up
what take what no is
there oh
yeah no 100 I have to receive four of
yeah two so you will get 100 of each so
that would be like two 50 or one of 50
and five of 10
oh yeah I saw I saw the GU there
yeah oh no no the rating is top 10
rating is a top 10
yeah and also they
for 400 so they can only for
that and five like that for example you
need you need to do 100 total so if you
mean to complete set or if you buy if
you buy here you will buy uh
well you can for 100 for 100 you will
get you will get that 100 of 100 of
and then if you want you can actually um
take some position on those Market white
be neutral on those you don't even need
to make a like a bet on this you can
make the prediction only on the
rating
yeah oh no no so you get 100 100 total
you have the 10 where are the 10 you
have some token of tens token token of
somewhere
here be some
somewhere 10 for the fish right fish can
how I just so here you have to buy with
the underlying token so here you have
your fish skin you can buy fishing up or
fishing
down you can me the set by giving this
and you will get a scent of fish up and
down yeah yeah yeah and you can meet a
set of fish up and down if you
wish 100 100 yeah
exactly okay last
trade last
trade where is overun here okay
so what we saw is that there are a lot
of PODS where bow stay around 50 but you
Al so have some pods where the cricket
stays at 50 but the fish the fish skin
goes to 70 so you can actually use this
as a tool to help your decision on what
do you want to to take because you can
see that the because you can see the
market believe you will get the higher
rating to the fish K than to the cricket
because lot of pods are 5050 and you
have some pod which are at 50 70 so here
you can use the market as a tool to make
a decision so which uh snack are you
going to choose I will choose the fish
and I do that from the
beginning so I I took r on fish
oh the fish is showan and what is
interesting here is because we had an
actor which could influence the market
well this actor took the token of what
he was going to
do
okay we let you finish
it so what is the rating out of 10 seven
so the rating is seven so you have the
fishkin token which redeemed and you
also have the fishkin up redeeming for
seven and the fish skin down redeeming
three oh no all the market are closed
all the market are closed and the
workshop is also closed that was the
last that was the last
element and uh so thanks everyone for
for coming to this
Workshop I hope it allowed you to
understand how prediction Market Works
how you can use those to predict the
future at least probably Cally to
evaluate potential future values and
also as a tool to help decision as we
saw with the fishkin and Cricket market
so thanks everyone for coming to the
workshop and if you could please help to
put back the coin in the boxes and the
card if you also put them in the boxes
that would be great also so thanks
everyone and if you can help us for
cleanup that will be great in order not
to delay uh anything so thanks everyone
for coming and uh hope you I got you
interested in prediction markets
yeah when can I get a set
of yeah where can I get a set of these
a you can just take a set by you have
spare you I
have
than for
t for
h a
w
oh o
