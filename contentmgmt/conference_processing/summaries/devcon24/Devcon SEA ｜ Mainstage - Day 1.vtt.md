[Music]
h
hello hello
everybody hi welcome welcome why don't
you give yourselves a big round of
Applause for being here at Devcon the
biggest Devcon event ever and I think
the most diverse as well my name is Ross
I'm going to be your MC for the main
stage for the dur duration of the talks
this afternoon and evening great to see
you guys more people coming in so please
please come and find your seats I see
some seats in the front on the left and
the right come closer the closer you are
to the stage you get to see our speaker
up close and personal and my hair in
high definition as well I see many of
you wearing your little frog hat I saw
it it's so cute I just wish there was a
hat that I could wear sadly I cannot so
I had to give it to a friend but
nevertheless please feel free to wear
your swags be proud and be excited to be
here at Devcon now our topic for today
is very interesting it is a keynote
session executed inside of or on top of
cryptographic objects how many of you
did not understand that all right good
because this is a beginner level session
so this is the perfect place to be to
learn more about programmable
cryptography in essence what we want to
do with ethereum and programmable
cryptography is to create the internet
for the next 50 years how can we bring
the power of the entire Global Internet
onchain well programmable cryptography
might just be the solution are you guys
excited to find out
more all right well before I welcome the
speaker I've got a very important
reminder part of having a great session
part of having amazing session is
audience engagement through the Q&amp;A so
later throughout the session there's
going to be a QR code on the screen I'm
going to ask you to please scan it it
will open up your Devcon passport app
please scroll to the bottom of the app
and you'll see a variety of buttons
there Focus if you can please on the Q&amp;A
button and you can already start
submitting your questions all right so
scan it later submit your questions so
we can have a great time of Q&amp;A ladies
and gentlemen without further Ado let's
welcome our speaker for this morning now
he's the co excuse me he's the
co-founder of zerx Park as well as the
creator of the Dark Forest game please
put your hands together and let's warmly
welcome to the stage gup
sheep take it
away awesome it's great to see everyone
at Devcon um thank you all for coming
today I'm going to be talking about
programmable cryptography and ethereum
as a quick introduction I'm gub sheep
I'm one of the co-founders of zerox Park
we're an organization that emerged out
of the ethereum ecosystem about three
years ago and since we first coined the
term programmable cryptography in 2022
we've been working to accelerate the
development of the field from a
technical ecosystem and conceptual
perspective our goal is to take
programmable cryptography from research
to production and to harness its powers
for a new Digital
Universe a lot of this talk will Center
around the following question how do we
compute together specifically how do we
as in a group of multiple people perform
a computation or execute a program
together now to give some context on
this question I want to take us back
about 30 or 40 years to the earliest
days of the internet in the beginning
the internet was a peer-to-peer Network
for essentially transmitting bits
between equal peers this means that you
could do things like send a document to
another IP address using protocols like
like FTP or SMTP at this point there was
not yet any notion of you know web
servers as we traditionally think about
them today or the client server model
rather the internet instead of being an
answer to the question of how do we
compute together was more of a
peer-to-peer Network for communicating
together but Computing is something much
more than
that and pretty early on people started
to realize that it's useful to be able
to do more than just send data back and
forth it would be useful to be able to
run programs on this data that's being
passed around on the internet but with
the existing setup of the internet in
the early days there was a problem in
the days of the early internet the abil
the ability to compute was limited to
individual machines running programs
over their own data so you could only
run a program over data that lives
physically on your own device you know
that makes sense so most apps looked
like single player programs imagine
games like solitire you know a single
player game or something like Flappy
Bird um or tools like spreadsheets or
word processors or photo editing tools
or a calculator that just runs locally
on your own device but of course we
wanted to do more you know we wanted to
compute together and to have services
like marketplaces or rid sharing apps or
social networks or massively multiplayer
games or global payment systems or
dating apps or all sorts of
things and so we came up with a way of
sort of simulating this idea of
computing together while in reality we
were actually still sticking to the
single player compute model in that
first solution the strategy for the last
very important node like Dave over here
in the middle and to promote Dave such
that we all give Dave uh all of our data
and now Dave can basically run something
like the Facebook backend as if it was a
single player application running just
on Dave's machine so this has been the
status quo for many
decades and uh you know from this
example we can sort of see why servers
came to exist in the first place web
servers do several things that
individuals and pure peer-to-peer inter
uh pure peer-to-peer networks like the
early internet can't do alone web
servers allow us to coordinate on and
perform computations over multiple
people's state that state might be
private to some particular subset it
might be public um it allows us to
decide which state is canonical and web
servers also provide strong uptime and
liveness guarantees that don't
necessarily exist in a peer-to-peer
Network so um this has taken us pretty
far but uh you know one question is is
can we do better right there's been a
lot of problems that have Arisen as a
result of this being the fundamental
architecture and in fact these problems
are a big part of why many of us today
are in this room you can feel free to
choose the problems you care about
there's all sorts of things um and when
we return back to the question then of
how do we compute together we have to
ask is there a better way that we could
go about this right and one of the
really interesting discoveries of the
last decade is that blockchains
cryptoeconomics and ethereum have given
us new answers to this question for the
first time in decades right so now
ethereum allows us to run a single
computer collectively in a way that's
sort of very different than the
traditional model where we promote that
one single node Dave to be a very
important node that we give all of our
data to
to so ethereum has given us
extraordinary things you know many of
which we saw this morning because we
have the ability to have decentralized
consensus over global State we have
neutral and autonomous marketplaces
Financial derivatives prediction markets
we have payment systems that no single
Authority controls we have
permissionless identity Registries
spinning up we have interoperable and
composable
games um but we also can't do everything
that we want yet in fact nearly
everything that I showed on the previous
slide is still beyond the capabilities
of ethereum alone and not just as a
result of performance but as a result of
fundamental architecture and capability
limitations so enter programmable
cryptography programmable cryptography
is a technology that can give us many
more answers to the question of how do
we compute together and it can give us
these answers both independently and in
combination with
ethereum so what is programmable
cryptography
for those of you who aren't familiar
with the term programmable cryptography
refers to a second generation of
cryptographic Primitives that have
started to emerge and become viable in
the past two to five years these include
Technologies like general purpose zero
knowledge proofs multi-party computation
fully homomorphic encryption witness
encryption functional encryption
obfuscation and more these Advanced
Technologies are the ones in bold here
and one of the key features is that they
share sort of an underlying theoretical
common backbone and that they generalize
familiar generation one cryptographic
Technologies like signatures and
encryption so you can sort of see a lot
of these Technologies in the shape of a
tech tree where protocols higher up on
the stack generalize things lower down
on the
stack so programmable cryptography moves
us from a world where we have proofs for
specific functions you know in the world
of generation one or special purpose
cryptography to being able to perform
proofs of any function or any
computation we can go from being able to
verify specific claims to being able to
verify any claim and in general we move
from special purpose protocols to
general purpose cryptography compilers
to make a hardware analogy this is sort
of like the transition from special
purpose Hardware like an alarm clock or
a four function calculator to something
like a CPU which is generally
programmable what's changed in the last
couple of years to make this an area of
technology to focus on now well first
off there's been significant
technological advancements over the past
two to five years that have made
programmable cryptography more
approachable on the theoretical level
every item on that previous Tech tree
that we just showed up here is sound and
has a theoretical construction that is
believed to be secure in fact candidate
schemes even for the most expensive
protocols like obfuscation may even be
practical on the engineering level some
of the first branches of programmable
cryptography like general purpose zero
knowledge proofs uh have become
practical for developers today to start
using even developers who aren't
specialists in addition to the
technology advancements there have also
been significant conceptual advances
over the last one to two years we've
recognized programmable cryptography for
the first time as a unified set of
capabilities with a common foundation
and we've started to understand how we
can Leverage The Power of programmable
cryptography to build powerful systems
that were not possible before rather
than simply seeing things like ZK snarks
as a one-off way to perform a certain
kind of hack to be able to introduce a
specific kind of privacy feature onto a
specific kind of blockchain architecture
we sort of understand how to use the
general programmability of these tools
okay so let's return to our question of
how do we compute together um I want to
think about this phrase multi-party
programming you know the act of multiple
people coming together and trying to
perform some computation together again
this has been the strategy for the last
principles if you think about this idea
of multiple people coming together to
run a program you might abstractly want
something that looks like this so you
have some sort of network you have some
sort of participants in the network that
want to do some action and they you know
gather all their respective data that's
relevant to the computation and they
produce the results of the computation
and they want to be able to do so with
privacy Integrity interoperability
guarantees and for this to be
practically feasible so let's zoom in
and look at the anatomy of such a
program the general pattern here is
slightly more complex than this diagram
that we're zooming in on but not by
much essentially in one of these
multiparty programs there might be three
kinds of data that we would be
interested in running our program on
there's some sort of global public data
that everybody knows and then there's
data that might belong to or live on the
machines of specific participants in the
computation and then there might also be
data that only the program knows and
we'd like to be able to run some kind of
program over all three types of data to
produce an output now ethereum gets us
part of the way there ethereum allows us
to collectively run a world computer
that takes in some Global public State
and perform a verifiable computation
together on that but like other
peer-to-peer systems and blockchains
historically full multi-party
programming has not been possible with
this model being able to do this with
all of those different kinds of
state so everything I've been saying so
far has been a little bit abstract and I
want to dig into a specific
example lately there's been a lot of
interest in decentralized social media
in particular we've seen uh protocols
and applications like farcaster blue sky
Noster and Maston start to emerge and
communities to get built on top of these
um one thing that's really interesting
about this trend to me and one pattern
that I've observed is that people tend
to frame the problem of decentralized
social media or building a decentralized
social app in terms of building a
decentralized Twitter we always very
specifically use Twitter and my question
is why do we always talk about
decentralized Twitter why don't people
talk about you know one of the other
social medias out there like building
decentralized
Facebook you know there could be
cultural reasons behind this maybe
people interested in in decentralization
tend to have congregated on Twitter um
but I think that there's also a deeper
technical reason behind this as well and
the reason for that is that the state
topology of Facebook is much more
complicated than the simplified model of
Twitter you know in Twitter everyone can
see everything and everyone broadcasts
every post to everybody else so now you
sort of need to reduce this to some sort
of decentralized messaging protocol you
know in essence so the state topology of
Twitter might look something like this
you know it's a it's a very homogeneous
simple thing to reason about whereas the
state topology of Facebook is much more
complex right you might have things like
friends of friends can see my timeline
we might have private groups where
things happen you might have
personalized recommendations based off
of how your history intersects with
other people's history or apis that
behave differently depending on the
combination of multiple people's
settings um this person's a third degree
connection that influences my
recommendation somehow etc etc so the
state topology of Facebook looks much
more
complicated and in the general case
emulating those kinds of more complex
topologies or multi-party programs is
impossible to achieve empirically with
only generation one cryptography and
even some forms of
consensus another issue that really
shines a light on the fundamental
limitations of of our existing tool
Stacks is some applications have what we
might think of as private Global state
so this is State that's part of the
application that is computed on and is
necessary for the operation of the
system but which no user of the system
knows or owns so you can imagine having
a bit in this system that doesn't
actually physically live on anybody's
computer but is a necessary input to
some of the computations that are
running you know on a social media you
might have a list of all the user IDs
that have been reported at least three
times for bad behavior or something like
the naughty list and one of the issues
here is well if you try to emulate this
in a decentralized fashion and nobody
has that array stored locally but you
still want to be able to perform
computations on that well that seems
paradoxical another pretty clear example
of this is in some kinds of games um you
might have strategy games where there's
multiple players each player can see
some part of the world or the global map
but there's also stuff going on in the
fog of War that nobody has access to
maybe NPCs are moving around or some
processes are running and so these are
things that only the server knows but
because they can eventually interact
with a given player State you might need
to ensure that somehow this state is
still being updated and operated on in a
consistent way despite the fact that it
doesn't actually live
anywhere so in short you know why is it
hard to be to build something like a
decentralized Facebook well first off if
you have a transparent data layer
individuals can't really have their own
state
a lot of decentralized systems need
their state to be public so it can be
verified and the system itself might
also have some notion of global private
State and it seems almost paradoxical to
imagine a system made up of a bunch of
users that's performing a computation on
a variable that no single person owns or
can read or
has so enter programmable
has the ability to potentially start to
emulate some of these
capabilities if we break down
what we would need from our multi-party
programming model we can write down a
couple of things that we would need to
have happen in order to be able to
emulate these capabilities in their full
generality we would need verifiable
computation because you know rather than
one trusted actor running the program we
might have this world where programs can
be run across multiple different
computers or by someone who you don't
even know and you don't even have to
care about who's running the computation
we'll need execution on private State
because if that program is physically
running somewhere it has to be running
on state that might exist in some other
part of the network that the person
who's executing the code doesn't
actually have access to the internal
state of we want data interoperability
we want the ability for you know the
outputs of certain programs or certain
services to be usable in other ones we
want consensus so that everybody can
agree on the canonical program State or
the canonical state of a given
multiplayer service and we want non-
interactivity to be able to scale to
billions of
participants a lot of this mental model
is spiritually very similar to uh what
vitalic discussed in one of his recent
blog posts uh with the three Egyptian
God protocols looking forward to the far
future of
ethereum so let's take a a quick look at
each of these in succession let's look
at verifiable computation so we want to
live in a world where we can execute
programs over a network and these
programs might be running somewhere
untrusted they might be running in a
place that I can't determine in you know
in advance ahead of time um and we
somehow want to still know that that
prog is running correctly well this is
the sort of guarantee that general
purpose zkps like snarks and Starks give
us and we've seen phenomenal progress in
this domain over the past couple of
years with the ability to even run
virtual machines performant inside of
verifiable ZK snark
protocols in terms of programming on
private State well one of the Dual
problems to the world where we have
multiple actors who might be running the
program is that if those actors are
running the program they might be
running it on state that lives elsewhere
in the network and because of that they
need to be able to execute code on top
of state that they don't know or perhaps
nobody
knows so this is something that is at
least partially solved by Technologies
like fully homomorphic encryption and
we've started to see the first tool
Stacks like Phantom Zone or open F
become possible for developers to use in
fact we have a demonstration of a game
running inside of this sort of
hallucinated server downstairs if you
check Che out the Frog Community Hub
there's a game called frog Zone where
there's a backend that holds about 500
bits of game State that's running inside
of fully homomorphic encryption that you
can
play we want data interoperability we
want for the outputs from one service or
computation on this network to be usable
elsewhere this is one of the big
problems with the internet today and for
this we've seen various groups projects
and companies start to approach the idea
of proof carrying data the idea that I
can take data in that is
cryptographically verified I can perform
operations or run programs on it and I
can get an output that is just as
verifiable and Inter inherits the
interpretability and the verifiability
of the inputs to that transformation
process projects like ZK email TLS
notary zass and many other ZK ID
projects are starting to build up
towards a future where data is default
interoperable self-verifying and
self-describing we want want consensus
and data availability this is something
that actually no amount of cryptography
can give us but we want to make sure
that even if a program is being run
somewhere even if it's being run
correctly and with
confidentiality and it's producing some
sort of outputs we want everybody for be
we want for everybody to be able to
retrieve those outputs it's not enough
to just know that something was done
correctly sometimes there's actual
pieces of the state that you need to be
able to retrieve and this is what
blockchains give us this is what the big
innovation in cryptoeconomics and
consensus over the past decade DEC
decade and a half have
been and finally we want to be able to
do all of these things in a scalable way
many of our strategies today for
carrying out these functions rely on
these very interactive protocols where
everyone must be online at once so
imagine a world where we're all
emulating the execution of a social
media backend whether that's Twitter or
Facebook or whatever social media you
want we don't want to have to require
that all of a billion people or billions
of people are online all the time to do
decryptions or various kinds of
cryptographic interactions what we'd
like is for only the involved parties in
any given interaction to need to be
online to participate and this is what
the most advanced branches of the
programmable cryptography Tory like
obfuscation or functional encryption or
witness encryption give
us as of about three or four years ago
obfuscation and functional encryption
are known to actually be sound
um so while this is the furthest along
in the tech tree that we're working on
advancing we know that it is
possible so to
summarize there's a couple of questions
that we can look back on and ask one is
what can cryptography do that ethereum
alone cannot
do in short as we've seen cryptography
allows us to build Rich applications
with complex interoperable state it
allows us to answer questions like how
can domains that use different data
schemas proof systems semantics talk to
each other how can applications hold
state with complex predicates on who can
see it who can read it who can write to
it who can operate on it and how can an
application have state that nobody
knows conversely we can also ask what
can ethereum do that no amount of
cryptography can do and while we're just
starting to understand the limits and
the boundaries of these Technologies in
short we might say that blockchains give
us things like consensus data
availability and ordering a ZK proof
allows you to prove any that you want
about a hash or a hash pre-image or a
public key but how do we decide which
hashes and public keys are meaningful
how do we come to consensus on which of
these hashes actually reflect something
that we care about in the world how can
you prove that something didn't happen
you can't easily do this with
cryptography except in very special
purpose cases or how can you determine
which of two cryptographically sound
operations happen first or that data has
been made available or that participants
in a network are live or incentivized to
to be online again these are things that
pure mathematics and pure cryptography
alone cannot do but blockchains in
Synergy with these things can bring as
well those are some great questions gab
sheep and I'm sorry to cut you off a
little bit but because of time is it all
right if we can move on to the Q&amp;A
section so we can listen to a bit of the
questions from the audience for sure
yeah so to sum it all up um the one
challenge that I'll give to everybody is
to think about the question how do we
compute together how can we use these
Technologies to pull forward a future
where multi-party programming actually
reflects the natural first principles
model so thank you everybody and we'll
take some questions
now hello hello all right let's hear for
GB sheep straight away our first
question on the board what is the
coolest thing in ZK research right now
for fast client side
proving yeah so I'm extremely interested
in some of the projects that have
started to really take client side
proving seriously I think that because
of the economic incentives of things
like rollups and bridges we've seen a
lot of advances on making ZK proof
generation very efficient on big and
beefy servers you know things like
sequencers or or block producers or
things like that um because of the
increased focus on ZK identity by the
space in the last couple of years we're
starting to see the first projects from
groups like Iden 3 or psse experimenting
with using new proof systems in order to
build fast clients side mobile proving
libraries that actually run natively so
I think that there's a lot of lwh
hanging fruit here um and I think that
uh hopefully one of these teams is able
to uh start pulling out something where
someday we might be able to even run a
zkm on the phone efficiently I think
that would be huge for the space and um
lots of research needed definitely lots
of areas for experimenting and trying
new things let's go to the second
question which got the three highest
votes will this enable decentralized llm
into inference while preserving the
privacy of user prompts if so how far
away is it if not what tech do we still
need to enable this yeah this is a
really interesting question uh I think a
lot of folks are curious about what the
intersection between Technologies like
ZK or verif verifiability and AI is
going to look like in the near future um
in general I am I have two minds about
this I think that trying to plug in our
bleeding edge llms or bleeding edge
machine learning models into
programmable cryptography is likely
going to be something that takes uh a
lot more time than you know a lot of the
other use cases that we might have
around things like Identity or proof
carrying data largely because AI is
something that will eat up as much
compute as you're willing to give it and
if programmable cryptography causes you
to incur like a 1,000x overhead then
there's many use cases that it's just
really hard to to justify but I am very
interested in this idea that perhaps in
the future where a lot of the internet
is made up of different autonomous
agents or machines or Bond Bots they
might be speaking in cryptography to
each other so how Bots might make sense
of the semantic contents of what each
other is saying is they might be
speaking in proof carrying data sending
bits of cryptographically verifiable
things you know we could imagine these
things combating stuff like
misinformation or the lack of
interoperability between different
Services um personally I'm very
interested in that interesting let's go
on we' got time for maybe one or two
more questions why haven't traditional
companies invested in this area of
research why do you thing up sheep yeah
I think that one thing which I think
we'll probably also be discussing in the
panel following this is that um the
reality is that the economic incentive
over the last five years has driven
research and development largely towards
use cases that involve things like
server side proving and with a focus on
verifiability technology rather than
confidentiality technology in particular
because blockchains have created such a
phenomenal Financial incentive to
actually build out these businesses a
lot of the oxygen in the room gets
sucked in that direction so what we've
been trying to do at zerx Park and and
amongst a couple of our other partners
is start to direct attention towards
these other further out potentially more
speculative use cases use cases that
don't have as strong of an immediate
financial incentivization Loop um but I
think we're going to see this pattern
play out more and more as these use
cases start to become a reality
excellent that's all the time we have
for Q&amp;A let's give our speaker another
big big round of applause thank you very
much GB
all
right now I know I saw you guys voting
for a few more really fun questions
coming up as well don't worry gab is
going to come back later because we're
going to have a panel session on the
same topic right of programmable
cryptography it's a really big topic and
initially when I read it it said
beginner track because I'm not a tech
person so when I saw beginner track I
was like okay I should be able to
understand but no not really it is quite
complicated even for me but for those of
you in the audience if you do understand
and you find it exciting I tell you this
session was really good it was pin drop
silence everybody was paying full
attention and our speaker he was going
like a choo choo trainer I think he
barely took a breath speaking non-stop
for the past 20 minutes I think that's
wonderful because you guys are here to
get as much value and our speakers are
here to give you as much value now I
love the questions that were coming in
remember you don't just have to post a
question you also can vote for the
questions that you think are the most
interesting I'm going to choose the one
that get the highest votes and we're
going to to see them on the screen as
well all right now some of you are
leaving the auditorium that's fine if
you want to go for another session feel
free there are lots of sessions 450
talks but if you need to leave please do
so quickly and quietly right so that we
can continue with our panel session on
programmable crypto right if you need to
do it now if not sit down and hold your
peace okay all right a few more people
leaving so I see a majority of you are
staying are you guys excited about the
ethereum yeah that's what I like to hear
here you know um ethereum really is
quite life-changing and as he said
earlier the real question to be asking
is how can we compute together how can
we compute together that's just one
question we've got many questions and
our panel is going to be discussing some
interesting questions as well now the
topic is going to be the same
programmable cryptography and some of
the questions that the panel is going to
be asking themselves as well for the
audience to reflect on is why have we
not been able to do everything we've
wanted with ethereum what's in our way
and what kind of tools like programmable
cryptography can we apply to change the
future without further Ado let's kick
off our panel and let's invite our
speakers onto the stage Albert knee
Barry Whitehead GB sheep once more and
vitalic
buin let's give them a big round of
applause as we welcome them onto the
stage over here gentlemen thank you
jesting am I here awesome I'll give
everyone another 15 seconds or so to get
situated um and as folks are getting
situated I guess I'll just for say you
know welcome everybody to what I hope
will be one of the many highlights of
your Devcon experience my name is Albert
and I'm delighted to be the host
moderator and perhaps even provocator of
this panel joining me as has been said
is the one and only gub sheep Barry
White hat and a
vog three very low information names
taking this zero knowledge thing a bit
too seriously if you ask me though I
guess white hat is a positive piece of
information like you know how people in
the west they have these family names
like a like Taylor or Carpenter or Smith
or Shepherd you know maybe one day in
the digital realm it'll be full of white
hats but but I digress um today we're
going to discuss programmable
cryptography and ethereum this is
exciting for a bunch of
reasons one that stands out is that the
four of us convened at the last Devcon
in Bogata for a panel that we titled
what to know about zero knowledge now I
know most audience members didn't see
that simply because there's so many more
people at this Devcon than even the huge
number that was at Devcon
latam but as those who did see that
panel may recall I started that panel by
apologizing why because zero knowledge
is not just a misnomer it's usually an
objectively incorrect way to be thinking
about what is going on with modern
applied
cryptography and most of the time when
people do quote unquote ZK no part of
what they're doing is actually in zero
knowledge which we discussed at length
last time that's why it's cool to see
how the terminology has evolved in just
the last two years we used to call it ZK
because we didn't know what else to call
it now we call it programmable
cryptography or
PC perhaps because we don't know what
else to call
it now call me old fashioned but when I
see PC I still think personal computer
so I always do a double take when I read
a note by gub sheep or Barry that says
something something PC but you know what
hijacking words such as crypto and zero
knowledge uh to mean things that they
didn't mean before it's basically a
tradition at this point so more power to
you if PC actually starts to mean
programmable cryptography that might be
your most impressive feet yet so without
further Ado I I really have to start
here what are we going to be calling
this stuff in 2 years in 2026 or 2027
and I I don't mean like literally try to
predict the exact words because if you
if you knew then we would already be
calling things that but as gub sheep
alluded to in his talk and some of you
already saw the term programmable
cryptography actually predates even the
last Devcon uh in fact gub Barry and I
discussed programmable cryptography at
edcon a couple of months before the last
Devcon but we didn't discuss it in the
way that we are talking about it now it
was more Vibes and intuition than
realization and understanding so really
for any of you what jumps to mind for
what might be the Vibes and intuition of
how we are going to be talking about and
thinking about this in a couple years
anyone and I think uman we're going to
slowly stop talking about zero knowledge
proofs and sarcs and Starks and we'll
just start using the word proof and like
lots of mathematicians are going to get
upset but like that's like fine right
because like we made the economists
upset by just like abusing the hell out
of the word inflation so let's just do
it to mathematicians too so yay we'll
prove ethereum
blocks I I I think that the Advent of
things like fhe and IO is going to mean
that the way that people think about
programmable cryptography will be based
upon those Technologies more than zero
knowledge proofs so I think that we will
have things like faith and Destiny
become the kind of primary Vibes that
people need to face with
this I think I remember in hello in one
of our last conversations that was
particularly centered around zero
knowledge we discussed how the idea of
what people were calling ZK apps at the
time might not be a complete Outlook
actually on what is possible with this
technology you know the point of these
applications was not the fact that they
Ed zero knowledge but it was the fact
that they actually did something they
brought some new kind of capability that
wasn't possible before whether that's a
privacy capability or a verifiability
capability or something like that and I
think that you know to use a historical
example this is sort of like when we
when we talked about websites as Dooms
right there was some point in time where
we talked about the idea of like oh this
is a DOT company and well look how that
turned out eventually we started moving
to things like oh here's a browser based
game or here's like an e-commerce
storefront or something like that and
you know we similarly we don't call
things HTML apps or HTTP apps we've
started to move away from that in the ZK
world I hear ZK apps less and less these
days but I think we're going to also
face the same kind of problem with
programmable cryptography and
cryptography apps there's not really
applications of programmable
cryptography it's about what you do with
them so I don't know if it's going to be
something about like the nature of
programs that are collectively run by
multiple people or a capability or a
thing that happens as result um but
that's where I would think well
hopefully we'll have more chances to
chat about this in a couple of years and
Beyond and uh it'll be really
interesting to revisit it because I
think one thing we know for sure is that
we won't be talking about these things
the same way we are
now so programmable cryptography and
ethereum or maybe PC and eth uh I know
not everyone here saw the the talk that
gub sheep just gave but real quick in
that talk gub sheep did did a great job
teasing the first topic that I really
want to dig in with each of you here on
today which is quite simply how do we
think about PC and eth together how do
we think about programmable cryptography
and ethereum and I'll I'll start with an
even more direct prompt is ethereum a
form of programmable cryptography and
conversely or maybe
complimentarily is programmable
cryptography an extension or is it like
a spiritual descendant even of ethereum
um where does your mind jump to italic
I'll start with
you yeah I mean I think it's like a
similar type of thing but different it's
like kind of like uh how I think about
like Jus uh one shot signatures which
are this like primitive that Justin
Drake loves talking about but they
depend on everyone already having quot
of computers but like the reason why
that analogy comes to mind is basically
because I think blockchains are not
cryptog cryptographic algorithms in the
way that we think of cryptographic
algorithms but they achieve dat like
objectives that are similar to
cryptographic objectives right like they
give you guarantees that like some data
has been published at some point in time
they can create systems that can uh that
can have a guarantee that like someone
who wants to participate can participate
which is a really important property of
like voting systems but like really some
of like potentially everything they give
guarantees of like verifiability of the
whole execution uh process uh verif they
uh some like one cryptographic like
cryptography paper buzzword that
blockchains basically do is what they
call a bulletin board uh so blockchains
are like I would call them cryptography
adjacent because they do similar kinds
of things and in some ways they feel
like and work like a cryptography
primitive but they also have enough
differences from like things like sonars
and FH proofs and fhe and alisation like
that they're worth thinking about as
being their own
thing one thing I also wonder about is
is there some root node perhaps that
both programmable cryptography and
ethereum are specific facets of is there
maybe some more General way to describe
systems or the sorts of programs that we
might want to run where you might say
Okay so this property it's as an
implementation detail something like
ethereum or a programmable blockchain
can provide those guarantees and you
know this other property as an
implementation detail you can use
something like a ZK snark or some form
of program alisation to achieve that and
I think my answer for that is a
simulated trusted third parties uh so
this is the idea that you can take a
protocol and you first imagine your
protocol as running through a trusted
third party so everyone sends everything
to Zuck and everyone trusts Zuck and
Zuck gives everyone the answers and then
you figure out how to replace Zuck with
some kind of construction that has much
stronger trust properties meaning like
much less or no need to trust any any
specific actor and often parts of Z Zuck
can be replaced by cryptography but
there's but but often there are
situations where parts of zck can be
repl by
blockchains um so it seems to me that
like it's an like they're natural
extensions of each other that like uh
ethereum is an implementation of
programmable cryptography ideas right
that it's just based upon it's like it's
contained
within one thing that has shaped my
thinking is that having programmable
cryptography not necessarily as this
entirely distinct thing or an extension
but it seems to be and this sort of
Builds on what both gub sheep and
metallic were saying it seems to enable
us to in some situations think more
holistically about what it is we're
trying to do what properties we want
something to have and I mean two is
greater than one quite literally and
sometimes that additional flexibility I
think has really helped unlock how we
think about things even when it was
wasn't maybe strictly technically
necessary for that so I think some of
these second order effects which are
always harder to predict than even the
already very interesting like literally
what can like X versus y do or not do uh
is going to be a really big part of the
story as we continue to
explore one thing that's also become
abundantly clear at least to me and I
imagine others here would
agree is that programmable cryptography
or at least what we're calling that
right now and ethereum I'm pretty sure
we're going to keep calling it that at
least for a while those together the
whole is greater than the sum of the
parts these are very complimentary and
we're really going to see I think a
really beautiful Synergy or you know
choose your buzzword here uh in the
years to come but for this kind of next
section of this conversation what I'd
like to do here is put on this
provocator hat because if nothing else
it would be entertaining to me and
hopefully to some of the folks who are
here with us right now and and it's you
know as moderator it is my Devcon given
right to seek seek Amusement so what I
was thinking what's the best way for me
to provoke here um and let's start from
the basics if you want to provoke you
can be reductive and simplistic so I'm
going to be reductive and simplistic and
I'm going to say there's two buckets
here there's the uh programmable
cryptography bucket and there's the uh
ethereum bucket so I'm going to start
with vitalic as the I guess
representative of the ethereum bucket
metalic what would you like to see the
the quote unquote programmable
cryptography folks do differently like
maybe consider approaching or
prioritizing uh differently such as
potentially placing greater priority on
making things that people in the
ethereum ecosystem can use more
immediately I I think um you know in
ethereum this uh this year we've
definitely seen a big shift from like
just building demos to trying to build
applications that really work for
regular users and that work at scale and
we've seen like plenty of beautiful
examples of this right so you know we've
seen foraster and poly market and the
usual ones Doo you know decentralized uh
like um encrypted Google Docs
alternative uh you know we've seen uh
all kinds of different things and
blockchain's becoming much cheaper and
more performance has definitely been a
critical part of that right and so and I
think programmable cryptography has been
getting to the same transition right
where like deaf tooling around SARS has
gotten vastly uh better and just keeps
on improving every year um and I think
uh actually it is time to like really
have like at least some portion of uh
that Community like approach more more
problems with I guess a product mindset
right so like one example of this is uh
like a one you know we've seen this year
ZK email right and like basically
turning email addresses into ethereum
addresses where you if you have an email
address you can generate an ethereum
address that can only be controlled by
that email address like that's powerful
that's like a Web Two web 3 integration
that's like a bridge that allows um like
existing like web 2 users to start using
ethereum applications in this like very
direct way that allows you to then just
like swap the email address out with
anything else later and I think there's
like equivalence of that in zup pass
there's equivalence of that in the whole
like other like ZK identity rapper space
like basically like like really get into
that uh gear of like actually building
things that are like next year like
everyone here is going to use and like
use voluntarily and like not just
because uh the high priests told them
that that that this is like the aligned
thing to
use gab sheep I'm curious for your
thinking on this because you're
obviously not against the idea of
building things that people would find
useful and I also think it's been
fascinating to see how ethereum not just
technologically but well for lack of a
better way to describe it the values and
philosophy of ethereum have been very
influential and beneficial to you um so
when you hear things like what vitalic
was just saying what what else comes to
mind like why is it I'm going to be
again reductive deliberately here why is
it not as simple as figure out the thing
that a lot of people can use and go and
build that or or is that what you think
you are
doing yeah I think ultimately it has to
be the answer to this sort of thing has
to be a yes and um and I kind of favor
an approach that takes at least three
things into to in into some kind of
balance here so on the one hand we
absolutely need to be building things
that touch real users at the end of the
day that are going for adoption
maximization at the same time I think
that I've seen with myself and projects
in the zerox park orbit also fall into
the Trap of basically uh spending a lot
of time building one feature you know
maybe not even one product yet but but
one feature or you might see when the
technology is in really early stages
entire companies you know well-funded
companies emerge to build one circuit to
do one kind of identity transformation
or something like that and I think it's
worth taking a step back at times and we
do need to have that kind of feedback
loop out in the world but at the same
time balancing that with the approach of
well okay how can we always be thinking
about how to level up our capabilities
and generalize and and and not lock
ourselves in we've had a lot of
experiences where um we'll have
basically one neat thing that we want to
do U maybe it might be some kind of
proof between uh some sort of identity
source and some kind of application that
we could imagine using that identity
source as authentication and we might
put a couple of Engineers who might
spend a couple of weeks or even months
building the circuit that takes the
incoming data schema converting it you
know running it through a different
proof system and and getting some output
and then we might realize after
deploying that that actually you know
this is slightly different or this is
maybe even like completely
off from what people in the Target
domain actually want to see from the
data in the source so that's where a lot
of my thinking in the last couple of
months maybe year or two has started to
go around like well maybe we don't yet
have a complete mental model of what's
going on and before putting all of our
eggs into the basket of maximizing for a
particular kind of adoption if we can
build systems that allow us to flexibly
iterate and experiment then uh we can
sort of take a balanced approach and
then one thing I mean I'd love to hear
from bar as well is there's at least one
more kind of branch that we need to be
pursuing simultaneously which is well
what if it's not just the mental models
about existing technology that aren't
there yet but what if it's the existing
technology is completely wrong and
something like obfuscation or functional
encryption is actually going to solve a
bunch of problems that are uh you know
obstacles for programmable cryptography
even reaching any kind of adoption so um
some combination of these three
approaches in balance is is hopefully
the way to go I'd be curious to hear
from Barry
though uh so I spent a lot I spent some
time thinking about why the first
blockchain application was currency I
thought that there was like another
world where we could potentially have
had a reputation system become the first
major thing to use that technology but
since but I thought about it and I
thought that that was reasonable for a
while but now I don't think that that's
reasonable anymore because I think that
like currency is inherently Freer right
because you can just transfer currency
to other people and other people can
receive it from you there's no real
barrier to entry but if you had a
reputation system or identity system
it's it's it's harder to transfer
reputation the other major problem is
that like currency is able to like
interact with the rest of the world very
easily right because you can transfer
from one thing to another but like how
do you do reputation and identity
systems how do you use them well it ends
up being all about like going to places
or being allowed authenticating to do
something and I feel like this is not a
good like
a business to be in like this doesn't
seem like a good place to spend our
energy because it fundamentally makes
systems that are better at excluding
people or it's a more efficient way to
exclude people one thing that like I've
looked back on the last year and thought
like maybe that was a bad idea was the
focus on ZK around ticketing and things
like that because I feel like making
like there's these arguments that I've
heard before that like if you make it
easier to kyc people just people will
just get kyc more right or maybe kyc is
a bad example example if you make it
easy to check if someone's over 18 or
not then people will just have to prove
they're over 18 if they want to buy eggs
or something right so like this is my
general concern about like going in the
direction of like we should just go to
production right now and like this line
of thinking has made me feel less
excited about building things with Sy
knowledge proofs and more excited about
building things with with more uh like
an interactive technology like uh fhe
and IO and things like
that so that segue is nicely into I
wanted to dial up the provocator a bit
and uh I'll start with gub sheep I have
I have one for you as well vitalic for
gub sheep I
guess one
lens with how you zerox park and others
have been approaching PC that it could
be a bit of let's call it a skeptical
lens would be that it sort of kicks the
can down the road for figuring out the
thing which we certainly all is some
version of impacting people in a
positive way and I'll even get more
specific one thing that we've discussed
is there may even be these kind of
correct by construction is elements to
what's emerging in terms of how this
whole programmable cryptography thing
works there's some really interesting
stuff there and and actually if you ask
me I kind of believe that that's we're
going to feel like there's directionally
correct by construction things kind of
like how the theory of computation
was or even just like a turing machine
uh feels almost correct by construction
once you start to really appreciate it
even though it's not obvious at all at
first why you should have this tape and
these symbols and that that should be
like the way to think about pretty much
all computation or at least a very
remarkably effective way to think about
all computation and yet at the same time
it's a the turning machine isn't
actually a relevant concept A lot of the
time I say the vast majority of the time
you know I've been a professional
software engineer I think is very
interesting and yet it pretty much never
mattered you could say maybe that's cuz
we got multiple layers of abstraction
later other things I mean I think it's
somewhere in the middle there but yeah
that's kind of my I want to hear your
response to that sort of
prodding yeah so one thing that's been
really interesting for me to observe
over the past maybe five or six years um
that I've been building various things
with some of these Frontier Technologies
is this idea that it's been a process of
constant generalization and what
generalization gives us leverage um so
to give a couple of examples this one
actually comes from something you know
more adjacent to ethereum than than
programmable cryptography when I started
working on Dark Forest in 2019 at the
time the idea of building an onchain
game using zero knowledge seemed kind of
like this really interesting or clever
trick you know we were using ZK in this
one very particular way to achieve one
very particular kind of interaction
onchain and we built this application
using
uh some bespoke patterns because there
wasn't any you know model for this idea
of an onchain game or an autonomous
world and I remember thinking back then
you know one of our big Inspirations for
dark force actually was this game called
Eve online which was one of the oldest
and largest you know MMOs with sort of
the most interesting uh player activity
emergence longevity all of these things
and I was just thinking man you know it
would be so interesting if someday we
could we could get to a world where e on
line or something of that kind of
complexity was actually running on chain
so I ended up spending about two or
three years building Dark Forest and uh
continuing to just add to the specific
Dark Forest circuits optimizing the
specific Dark Forest smart contracts and
adding in all these features and at some
point I met you know my my co-founder at
Xerox Park um luden who what he did was
he took a look at how we were doing Dark
Forest and he basically built a mental
model for what was really going on so he
kind of built this mental model that was
expressed both in software and
abstractly conceptually for this idea of
Aon worlds and autonomous world's
infrastructure and they got to work
building lattice and mud and Redstone
and and all of these tools um and you
know suddenly it became possible to
build not only the next 10 Dark Forest
but also something like a dark force
that was actually a hundred times more
complex and interesting and actually had
a shot at getting to hundreds of
thousands millions of users and actually
today it's really interesting we've
closed the loop on this over five years
and Eve recently announced that they're
going to be building their new game on
ethereum base technology so when I think
about this sort of question I think not
necessarily like well how do we make the
perfect abstraction of something like
Lambda calculus but how can we build a
more General mental model that actually
gives us leverage where in five years
because we're thinking about this the
right way and we're building the right
abstractions we can actually access
those those you know millions of people
who might want to to use this
technology that leads nicely to the
proding that I want to throw your way
italic which
um my I guess strawman counter point to
the PC should be doing more for ethereum
people today it would probably be
something on the lines of um this is not
as generous to ethereum as I think it
should be but let's just say that
ethereum has made amazing strides but it
still feels a lot like this like magical
Island where the physics Works
differently um but it only works that
way on that island and and there are
bigger and better Bridges to get over
there but the island is still kind of
pretty far and the bridges are still
pretty narrow um it's almost like a
Bizarro burning man right down to the
traffic and and just how accessible it
is where it's like accessible but it's
not that accessible and ethereum does
already clearly have a very big
ecosystem folk with people doing amazing
work on all sorts of fronts and so
arguably what ethereum needs is efforts
that um kind of aren't just stacking on
top of those prodigious existing efforts
but taking this say complimentary
approach bringing like a phrase that
comes to mind is bringing Snippets of
ethereum physics back over to uh the
main continent um you know to accelerate
like how these these different worlds
can can synergize and synthesize um and
I'm curious for what jumps to mind when
you know you hear those kinds of
thoughts sorry I'm trying to like think
of
um you like ref ra the question again
yeah I think what I would boil it down
to is reductively you could say if
programmable
cryptography Works backward from what
ethereum needs it may be more marginal
in terms of how it can bring what
ethereum really cares about to the world
and that would be one lens that differs
at least slightly I think again the the
real answer is you can do both but I I
want to be reductive for the sake of
arguing
yeah I mean I think ultimately like it
makes perfect sense to like you know
have people that are developing the
algorithms and algorithms I think are
inherently a very general purpose thing
and uh like there are some sometimes
optimizations that you can make for some
use case but then like as we've seen
with proofs right everyone is just
moving to doing proof over risk 5 and
once you do that then it's like any
optimization is basically almost equally
valid for any use case right and I think
for fully homomorphic encryption and
offis cation like a lot of the
surrounding Primitives there's like a
big element to them which is just a
general purpose and uh it's inherently
something where you build infrastructure
that like either almost any use case or
at least very large classes of use cases
need right and there's like one group of
people that's very good and like very
naturally inclined to do that and then
there's like a somewhat different group
of people that are more applied um you
know applied programmable cryptography
yet in ethereum people um sorry I just
realized applied programmability in
ethereum spells ape it's
fun uh but you know so you have like the
applied programmable cryptography in
ethereum people and then like you might
realistically end up having like several
other applied programable cryptography
communities pop up that care about other
of problems and like to me that's a
natural kind of diffusion I mean just
like there's lots of eum communities
that like don't really think much about
programmable cryptography but then uh at
the like even those communities that's
like once the the general purpose stuff
gets good enough then they end up using
it whether they realize it or not right
like anything that's on top of a uh
validity rollup you know we're not
saying ZK rollup anymore they're
validity rollups uh the is uh a user of
programable cryptography but they just
like don't see it at all and so I expect
we'll see a lot of
that well for the final portion of this
talk which you guys both sort of hinted
at I want to dig into the future which
I'm sure everyone is interested in uh in
particular through the lens of
obfuscation um but before we do that and
I really only want to take like two
minutes for this because I do want to
make sure we have a chance to explore
that topic well I want to give everyone
like 90 seconds to one get another frog
because I know you guys want to do that
um and maybe even scan a neighbor's frog
if if you have if your neighbor happens
to to have one so everyone feel free to
take a moment to actually pull out your
phone search the swamp um and and while
we're doing that gub sheep I'd love to
hear some quick thoughts on what is this
whole frog crypto thing about anyway uh
we saw a glimpse of it at Dev connect in
Istanbul last year even just like why
frogs but you know what else is there to
it that you might want say while we have
everyone here yeah so some of you may
have noticed the Frog hats that have
been popping up kind of like mushrooms
uh around the conference um or some of
you might have swung by the programmable
cryptography Booth downstairs uh frog
crypto came out of uh being originally a
pun on one of the decentralized sort of
Dev connect events we ran last year in
Istanbul called Prague crypto and we
sort of realized I think at some point
someone either like typoed or or you
know some part of the pee on some
signage fell off and we're like oh frog
crypto yeah that maybe that could be
kind of like a mascot or something um so
the idea here is that you know these
frogs are almost a delivery mechanism
for some of the base uh sort of data of
programmable cryptography this year what
you can do with them is you can collect
them on zup pass so you can go to zup
pass press the little frog button and
start collecting a frog every 15 minutes
and what that frog is is it's basically
an EDSA signature that's really easy to
make ZK proofs about and various
developers have been building games on
top of this idea of making ZK proofs
about your frogs one of the new things
this year is that you can also scan
other people's frogs by you know holding
up your phone and scanning the QR code
and sending them a frog request this
allows you to add them as a friend in
frog social and what those frog requests
are are those are self-issued
attestations to other people who are
also participating in this so what we're
essentially doing here is we're building
this social graph actually of thousands
or actually I think of as of maybe a few
hours ago we might have crossed like
between different members of the
community that we're going to be able to
start making all these kinds of social
graph proofs on top of so you could
imagine being able to do these
reputation proofs we're already starting
to run into a lot of issues with Cil
attacks so you know it just goes to show
that cryptography preventing these sorts
of social attacks is definitely there's
both like a theory of it but also a
practice to that um but we're excited
for this to be a sort of sandbox for
people to experiment with the various
kinds of
functionalities cool cool well I I
recently got a an abusa toad which I was
very excited about um and speaking of
obod let's dig into obfuscation because
and and the reason for this
is I can't really articulate this well
but it feels a bit like the quote
unquote next thing and and what I mean
by that is it's a thing that we do
understand technically but I think we're
still figuring out how to think about
and reason about it and ways kind of
like how we technically understood ZK
long before we really started to have
some of these now seemingly basic
conceptual breakthroughs even like
single player versus multiplayer and
other things of that sort there's so
many different lenses here we can look
back at the Arc of how things are
developed and how your past predictions
have gone you can look forward you can
just share new insights and realizations
I'm going to start with you Barry
because this is something that I know
you have been diing into a lot and
you've been one of the primary sources
for me to begin to get this sense around
obfuscation um in the way that I'm
describing
here um yeah so I'm very excited about
the potentials of obfuscation and it's
like par of Me Okay so the way to think
about it is that you like vitalic was
saying earlier you can imagine that you
have this like trusted third party that
you can actually trust and that you can
just ask them to do something to help
you and with z knowledge proofs they can
help you to verify computation but they
can't do anything else and and with NPC
they can do like multiple people's
computation but they're not able they
have this interaction layer but with IO
you're able to have this like no
interaction required basically you put
the something in and you get the answer
out and this is really this seems to me
that like we're getting so close to what
like a an actual trusted third party
could do that it seems
that it seems that we might be getting
towards the end of cryptography that
like we're we're at the point where like
once we have this it's hard for me to
imagine like what else we could actually
have because if we could have something
else it would have to be something that
like an actual trusted human would not
be able to achieve uh like there is a
couple of things that IO can do like
data availability and uh onetime
signature kind of stuff they can they
can repeatedly you can force them to do
things repeatedly but like the it's
seems that we're getting to the end of
the land that like and I don't know what
we're going to do once we get
there I mean I think uh you know once uh
we like if we actually get to the uh end
of uh the line which uh I do think uh
alisation in some sense uh is in a
certain sense because we B it basically
does let you like simulate any third
trusted third party with the exception
of this
like you can't uh that you can't ensure
the nonreverting property and that you
can't Ure well you can't like do anti
anti- censorship uh but uh like once we
get the end of the line of like base
wire technology then I think that's the
beginning of the line for so many more
things that get built on top of it right
and I think this is uh something that we
see in lots of other fields right like
there's def lots of things that we've
seen that have basically approached some
kind of optimality like multiplication
you know we know how to do it in N log n
now and and uh okay fine you know the
algorithm that technically does it in N
Logan only actually becomes like
remotely efficient if you multiplying
like quadran digit numbers but like for
everything else we have n log log l and
like do you really care about the
difference right but then it's like when
you have like Fast these fast algorithms
that enables lots more stuff in higher
level fields to be built on top of it
right it's like if and like 4A or fast
an entire class of uh zero knowledge
proof algorithms that would just not be
possible and we will not even be talking
about this field in the same way today
right and then on top of that then you
figure out once we figure out how to
make any trusted third party trustless
and then once we get that down to uh
like there will be a period of like at
least a deade where we figure out how to
get everything down to the lowest
possible level of overhead right and
then once you get past that then you
know the question is like what are all
of like every time you make an
optimization what are the new things
that you can build on top and then I
think even after you're done the
optimizations you can keep on thinking
of new things to build on top like
that's I I don't think it
ends yeah one thing I think about as
well is this idea of right now one way
we can think about obfuscation is as a
as a dropin replacement for a trusted
third party and that might enable us to
give stronger you know security or
confidentiality or other kinds of
guarantees uh on top of things that we
use trusted third parties for today but
an interesting question for me is you
know in in the spirit of one prompt that
we've sometimes discussed is this idea
of like what if obfuscation is not the
end but it's really just the beginning
like what is it the beginning of I
suspect that you know similar to uh you
know I have a similar prediction on
things like ethereum and other kinds of
cryptography once obfuscation or these
kinds of Technologies become ubiquitous
enough we enter a totally different
state of what the internet looks like
and feels like it's not just the
internet that we have today but servers
are replaced by these more you know
trustable or verifiable or confidential
Services we actually go from like solid
to liquid or liquid to gas in terms of
what it even means to be interacting
digitally now I don't really know how to
think about that I feel like you know I
know Barry and vitalic have some ideas
on some of the the crazy stuff that
might happen there um but that's a
prompt that I at least think is
interesting to consider yeah I love that
I I'll build on that it's really hard
right now to imagine obfuscation being
like virtually free given that we've
barely begun to understand how to even
do it and then the overhead is
significant to say the least at the same
time you tell someone a 100 or
definitely 200 years ago that the cost
latency of sending a message and not
just a message like let's say HD video
halfway around the world would go to
basically zero um I think that would
have been even more unfathomable and so
we've seen that these things happen
slowly than quickly all the time and uh
while we've got a lot of heavy lifting
you know grunt work to do I do think
it's valid to take a moment and say what
jumps to mind as you start to imagine
the currently Pie in the Sky feeling hey
this is everywhere this is is the the
beginning you know intersections are
overlaps with other Technologies or
other aspects of society um I know this
is something you guys have mused about
at various points so curious to hear
what jumps to the top of the mind for
you
here uh so my prediction for the future
is that in 20 years there will be like
what we would call today a religion
that's based upon indistinguishable
obfuscation at the start of the panel I
talked about like Destiny and Fai
being the like Vibes of the future world
and that's my prediction I also predict
that one member of this panel will
become a member of that religion or that
like we won't call it a religion that ah
that that's a
secret um yeah like we won't call it a
religion in the future but like today
that's what we would see it
as yeah that's that's fine so it's like
how Beth Jos does his thing about
thermodynamics and we get to do our
thing about aisc yeah
yeah okay let's see yeah far future I
mean uh well get into oh get into bcis
and then you get trustless two-way
telepathy yeah you know you know do you
want to like upload your like your
thoughts to Facebook probably not right
but you know do you want to uh like have
deep communication that involves like
sharing uh thoughts directly with other
people for some specific other people
like sometimes possibly um so that's one
of those spaces where like if you don't
do it with cryptography it feels like
it's almost default dystopian but if you
do it with cryptography it feels fine
and uh like actually uh having
cryptography up to the highest possible
standard by of usability and just like
Drop in replace um replacement uh Power
once that stuff becomes available seems
like you would be really powerful right
like the level you want to get this
stuff too it's like uh I think for me
the analogy is how our like internet
bandwidth is at this point so good
people just like send pictures as a way
of saying things that they could have
said in like five words just because
sending the picture is faster and like
to someone in 1980 this would have
seemed like bad insane like no why
the hell are you like voluntarily
incurring like 100,000x inefficiency
right and like these days of course we
figured out how to cut the inefficiency
off of our like lower level bandwidth by
a factor of more than 100,000 and so
that's like doing that is like actually
totally fine right and so I think what
we want is we want to get the overhead
numbers low enough that the question
flips from like why programmable
cryptography to why not programmable
cryptography and we get more things
proven FH encrypted and offc as needed
by
default yeah one other thing that I
think is a really interesting feuture to
consider as well is this idea that
programmable cryptography or whatever
we'll call it in the future provides an
alternative lens on digital agents of
the future so I feel like a lot of the
dominant narrative today uh centers
around this idea of oh llms you know we
anthropomorphize them they speak to us
in natural language those are going to
be the the digital that's what the
digital agent of the future looks like
um but there's a very different concept
that you get if you take the idea of
something like a smart contract or what
we call a crypt Toma you could kind of
Imagine an OB fiscated program running
inside of a smart contract with one shot
signatures to its logical conclusion you
know this might be cryptography's dual
to something like AGI would be a
cryptomed um and what the cryptomed is
is rather than this sort of digital God
figure that's got its identity that's
bearing down on you it's almost like a
force of nature like a Gaia type thing
that pervades digital cyberspace where
wherever I am in digital cyberspace I
can kind of interact with this
underlying fabri style thing that just
permeates across digital reality so as
one example here I I sort of think of
DNS as a very very primitive version of
this kind of digital agent wherever I am
on the internet I can reach out to DNS
and it behaves in this very you know
well structured and useful way that
creates some sort of global context now
imagine taking that capability and
ramping it up a 100 thousand times
imagine imagine giving that intelligence
that's a very different concept from
something like GPT
so I feel like we're already getting a
snippet of this um but we have like a
minute and a half left and so I kind of
want to end where we began but instead
of what are we going what words we're
going to be using in two years what
words are we potentially going to be
vibing around in 20 or 50 um what
shotgun what jumps to
mind I mean I think like the words will
just become more basic right I think
it's like you know during the uh like
academic uh like the dance era um we you
know obfuscation is called um IO and
distinguishability obfuscation you put
the I lowercase but then of course that
like confuses the hell out of everyone
because that's input output and then uh
I'm expecting we'll just call it aisc um
and then I expect 10 years after that
we'll give up on that too and people
will just talk about encrypted programs
so I think we'll just like start talking
about every Concept in uh language that
just makes it feel like something much
more and more banal just like something
that's a part of
life yes one for me is as Barry and
vitalic has have been saying if IO gives
us all of the powers of a fully trusted
third party then that means that
anything further along this Trail would
have to give us more than what a trusted
party or an actual human could do so
there's probably some crazy sci-fi Tech
out there that goes far beyond what we
think of today as cryptography and
blockchain but as a natural descendant
um maybe we'll for the complexity
theorist in the room maybe we'll Ascend
the polinomial hierarchy or do some
crazy stuff with comput I think Quantum
is probably like the most immediate
thing that's in front of us but what's
after that I mean we don't
know I think that something will happen
similar to what happened when we
invented money that we invented all
these words like justice and like um so
so I I believe that those will become
the like default words that will be
using in the future like
honor
Justice all right gentlemen thank you so
much for that exciting panel session
let's give them all a big big round of
applause thank you now we're not done
yet we're not done yet we've got some
Q&amp;A coming up and we're going to show it
on the screen um ladies and Gentlemen
let's go well eight votes for the top
question two-party MPC could do
everything that fhe promises just much
cheaper now in the next 10 plus years
and likely ever are we victims of a VC
powered story takeover big question I'm
not sure who wants to answer it but
Albert I'll pass it over to you yeah
I'll start uh if there's a VC powered
story take over here that'd be very
interesting where's the I mean the whole
point of that is the money where where
is the money have you guys are you guys
not sharing something here with me and
what's going on
um um no like um 2bz is limited to two
parties though right and you want to
have like multiple parties uh so like
that's one of the reasons why FG is more
interesting like both are interesting
the other big problem with NPC is the
interactivity requirement that's also a
problem with FH and that's why IO seems
to be the most interesting I thing for
me right
now great all right anybody else if not
we can skip to the next question that's
good I also want to know where's the VC
money in programmable cryptography
hopefully coming soon ladies and
gentlemen next question has I believe
screen will the PC allow smart contracts
to have signing functionality similar to
eoa who'd like to take that
question anyone anyone
can yeah I mean I guess it depends what
you want out of signing functionality
right because if you want just like the
ability to express Authority then like
you don't even need any kind of
programable cryptography right you just
like use ethereum's built-in call
mechanism already right um and the one
the one thing that offis cation does
that is interesting is that it gives you
um a snark that where the algorithm for
verifying the snark just is verifying
any kind of signature scheme and like
that comes at the cost of requiring a
shusted setup but that does basically
mean that you have like zero knowledge
proofs that are extremely cheap and like
that that are only as expensive as uh
like just a a signature which is
extremely cheap in the current world and
then in the qu Quantum world like the
quantum resistant ones are somewhat more
expensive but it's uh I think still
interesting um the uh thinking about
like what like the other thing that you
could do like the thing that you
definitely kind of can do but with
difficulty is if you start talking about
not signing but like encrypting and
decrypting like what if you want a
program that has a secret that it
releases under smart contract conditions
and the challenge there is like the way
that you would do it is you would have
an offis skated program that releases it
if it provides a proof of blockchain
consensus um that like has like some
finalized route and then thei and the
finalized route like shows that some
particular condition was met and then
the program only then would just out
would actually output the secret the
challenge with this is uh like B
basically look one is vulnerability to
sakers come together they can privately
extract the secret without ever like
actually being slashed and one
mitigation to this would be to like add
a tiny amounts of proof of work in like
maybe like 1% proof of work and then
extracting any individual Seeker it
would cost like at least a few million
dollar um so there's some mitigations uh
there but like and so so it's like on
the B it's like possible but with uh
caveats which I think is uh interesting
thank you Vitali possible but we caveats
let's go on to the next question now
this one's fun I think gship just
mentioned this very briefly about Ai and
programmable crypto the question at the
top is how much autonomy should AI be
allowed to have to interact with
programmable crypto who'd like to take a
gup sh can I pass it to you yeah so one
idea that I think is very exciting to
revisit from the the last 20 years that
relates to this question is this idea of
the semantic web so for those who
weren't familiar this was the idea that
maybe we could have an internet wide
Mega project to take all of the data on
the internet and make as much of it
possible uh machine readable
semantically consistent with other data
um make it so that machines can talk to
each other in some set of data schemas
that are universally interoperable and I
think you know the semantic web didn't
work out for various reasons at the time
one was the verifiability of data uh is
something that we just you know we
didn't really have the technology to
have programat programmable
verifiability back then but now that we
have programmable cryptography we can
imagine a world where you know the
current version of autonomous digital
agents which is AIS and llms which are
an upgrade over the the bots of 20 years
ago can speak in programmable
cryptography to each other so
programmable cryptography almost becomes
like a language or communication stack
for these digital beings of the future
um so I'm I'm all for AI being able to
interact with programmable cryptography
I think there's like even Wilder uh
intersections here
but one thing I want to add here is
programmable cryptography is not like
entirely orthogonal to the idea of
autonomy but I think it's more in that
direction like the question of how much
autonomy what we call AI cuz honestly I
don't think we know it else to call it
right now that is sort largely in a
different sphere and what's interesting
about programmable cryptography is it's
sort of second order like depending on
the autonomy level of AI programmable
cryptography May really shape the
implications around it like like will
something decide that it wants a
semantic web or or those types of things
um but yeah the elephant in the room is
like will AI be very autonomous and will
have
you know very serious implications I
think that there some maybe interaction
with with what's going on here one could
say that it certainly has interactions
with with blockchains um but I just want
to highlight that programmable
cryptography at least at a simplistic
level I see as largely like something
that's complimentary to the to the
autonomy question um itself I'm curious
if anyone else wants to chime in on
that yes no no all right he shook his
head so I'll take that as a no but no
worries thank you for the answer is well
I think that's quite comprehensive
autonomous AI that's going to be quite
an interesting future to look forward to
let's turn our attention to the top
voter I think this is 12 votes the most
I have ever seen so far in any of the
sessions um if ethereum was built with
programmable cryptography in mind rather
than Bitcoin with smart contracts would
it have been built differently um I mean
yes with like a lot of tiny details
right it's like if AUM was built with
statelessness in mines the gas C
structure would have looked very
different the uh tree would have looked
very uh very different lots of things
would have been like designed around
stateless proving and for snarks it's
like basically similar like gas cost of
hashes would have been uh higher we
probably would have consider just like
using Poseidon right from the start I
think uh I mean when I started in
ethereum I was definitely like in a yoy
mood I probably would have just made
posid in the hash function um
the what like there's just a lot of like
little tiny decisions that would have
been different I think the core of like
being a platform that has accounts and
that has transactions and that has a VM
probably would have been the same all
right thank you very much Vitali
appreciate the Insight uh we got I think
one and a half minutes so let's try and
fit one or two more questions will devs
using prog crypto risk punishment like
tornado cash devs how to dance with
compliance a bit of a loaded question
would anyone care to try
well I'm curious what gub sheep thinks
because this is his problem not mine but
in in all seriousness I mean I think
that
uh look there is precedent like
cryptography in a very simplistic sense
was you know there were efforts to try
to ban it in the '90s something we
completely forget now it's like you
can't not use cryptography to surf the
web like no browser will basically let
you do that without a lot of pain and so
I think that the the financial aspect of
tornado cash was obviously a significant
part of that I think that what's
fascinating about programmable
cryptography is we literally have a
precedent that cryptography is
everywhere you all use it every single
day generation one cryptography in the
form of like https and other things like
that so I think there's a very broad
surface area there's always ways to do
things and ways that cause these effects
but I think the the key thing to keep in
mind is that the surface area here is
very very Broad and that's what makes it
exciting maybe yep maybe one quick one
quick sentence on it yeah yeah I I think
that one thing that I think about here
is it's about how we really sell the
capabilities of the technology for
example one thing that you can do if
you're talking with someone who might be
very skeptical is do you talk about
interoperability or do you talk about
subverting nation states and you can
talk about interoperability in that
conversation you know that's sort of
what what this kind of thing is all
about this is something where we are
testing the the powerful capabilities of
programmable cryptography um but uh you
know it it just depends on what we put
what foot we put forward first so all
right thank you very much as the music
bling that's our queue to say goodbye l
let's give our speakers another big big
round of applause to all four of them
for an absolutely fantastic panel
session on programmable
cryptography all
right are we here to work together are
we here to subvert nation states well
only time will tell um wow you don't
have to leave you know know ladies and
gentlemen there's going to be another
session as well let me quickly give you
the topic for the next session the next
session is eth or ethereum Plus+ a road
map to real decentralization now there
are many things that threaten the
decentralization of ethereum certain
things that are leading to a more
centralized blockchain but our next
speaker is going to be sharing about
what we can do today involving a
technology called
tees yeah so if you're interested in
that about how we can decentralize
ethereum keep it that way and achieve
the original Mission well stick around
but if you'd like to go to another
session you want to go and visit another
talk no worries I only ask you for one
big favor if you want to exit exit right
now do it as quietly and as quickly as
possible once again a big thank you to
all of you for asking these amazing
questions we really really appreciate it
and I must say it is quite amusing when
I see a question come in and then slowly
get voted voted voted voted all the way
to the top I feel like I'm running a dow
you know just collecting votes every
time um but do keep in mind that if you
ask any any uh unusual questions uh it
might get moderated away uh I did see
some funny questions just now about
frogs let's try and stay as much as we
can focused on the topics as well as the
speakers all right I still see a lot of
movement um and you know there's a bit
of noise while people are moving out
that's fine I completely understand
we've got over 450 talks across seven
stages multiple classroom and breakout
rooms so there's lots and lots to see I
often wish I could also split myself
into three people one to go eat one to
MC and one to go and enjoy some talks
but I can't do that so you've got to
make a decision where you want to focus
on I'll just wait another one minute for
everybody to exit the hall if you're
going somewhere else
yep those of you exiting the hall I've
just been informed by the volunteer team
if you could please exit on the left and
right and please enter to the middle so
that will help us a lot with the traffic
right if you can exit on the left and
right sides and you can enter from the
middle of the hall all right if you
could do you do me that big favor
that'll be so wonderful thank you all
right the rest of you if you're sitting
at the back hey there's some seats that
just opened up in front why not take
your stuff come and come closer to the
stage yeah it's always great to see a
nice full audience right in the front it
really helps the speakers as well
encourages them all right if you want to
move ahead go on and move ahead now I
also want to remind everybody you know
when you scan the QR codes and it opens
up your Devcon hi you want to take
picture hi oh hi Joe I didn't see you oh
hi guys it's nice to see friends all at
these conferences now I was saying as
you scan the QR codes and opens up your
Devcon passport and you click on the q&amp;
a you'll notice there are some extra um
functionalities there you can also
provide speaker feedback and you can
collect cards right you can collect
cards for every session that you attend
now each session has a unique QR code so
if you want to collect the card you
physically have to attend the session
scan the QR code and if you see the Q&amp;A
screen you can either ask questions
collect your card and also provide
speaker feedback yeah it's an important
part of the process even speakers want
to hear your feedback so that they can
continue to improve their sessions at
the Devcon or any other crypto
conference in the near future all right
I think we're settling down settling
down those of you who are exiting the
hall if I can ask you quickly exit the
hall as quietly as you can and as
swiftly as you can all right so that
those entering the hall can come in and
take their seats and we can enjoy our
session
together all right our next session
ladies and gentlemen e++ a road map to
real decentralization now the whole
mission of the block chain was to be
decentralized but there are some factors
that might be contributing to
centralization things like Ms Trends in
Block building well our next speaker is
going to be sharing about what we can do
and certain interesting Technologies
known as tees right that are going to
perhaps help us achieve back the mission
of decentralization so please put your
hands together and let's welcome our
next speaker Phillip to the stage ladies
and gentlemen a big round of applause
for Phillip
hello hello Devcon sea vitalic is is a
very rough act to follow so thank you
for everyone who stayed to talk about
decentralization today um so today we
are going to talk about deconstructing
the nation state which is how the last
kind of panel ended so that ends up
being perfect and in this talk we're
going to cover kind of a bunch of
different concepts at a at a pretty
rapid fire pace so we're going to start
with how does eth die how does eth go to
zero why are we actually on the Road for
some possible Futures in which this
blockchain and this system which we all
love just like doesn't do as well
anymore how can we save it what is the
formula for that what does this have to
do with E3 which I think is a meme
you're going to be hearing a lot about
in the next few months few years Etc
what are the Technologies we can use we
just heard about program uh programming
privacy and other things like that what
else can we do what can you the attendee
here at Devcon and in the space uh do to
help this
and then what am I doing about all of
this and where do Technologies like tees
come in so let's get right into it I'm
going to start a little bit funerary
today so I'm going to talk about what I
consider to be the two most disturbing
pictures in the ethereum news cycle the
ethereum space today at least to me and
to my dream of building a decentralized
system together with you all um so the
first one is from this paper called
regulating decentralized systems
evidence from sanctions on tornado cache
paper published by the New York Federal
Reserve observe authors listed below and
in this paper they go Fairly deep into
analyzing tornado cache and sanctions
enforcement on decentralized blockchains
um kind of enumerating various power
dynamics choke points and other levers
in the system uh and then studying how
effectively they can kind of manipulate
these levers of power to do things like
stop Technologies they don't like um
Technologies which for example many
people here uh may have different
feelings about so um actually let me go
back to that if I can figure out the
clicker um yeah so an interesting thing
about this picture is it shows the
approach that as the nation state game
escalates as we really go deep into this
mission of decentralization that various
kind of centralized parties take on
these things we build and it's very
simple it's about control it's about the
boxes of control and it's about how to
leverage them and make sure we put as
many X into these boxes that we see here
um as possible so that's the first
disturbing picture
the second one uh so this is a graphic
that you can go browse yourself online
the uh URL is up there uh I can't read
it from this distance but uh benj dd.com
AWS there we go and here you can go
through the various different AWS data
centers worldwide and kind of view
different uh AWS to AWS latency pictures
um in a very real world this is the
topology of the internet of the networks
on which we're building our Technologies
today uh so you can you can see on the
left there you have us east1 which is
the most popular AWS data center for
crypto deployments uh and the lighter
the color uh or sorry uh I guess they
changed the color scheme but I think the
blue lines are things that are like
approximately on the order of under 400
milliseconds uh the light blue line is
is kind of or maybe it's under 200 and
the light blue line is over 200 Etc um
but you can see there there these very
clear corridors of latency and power
that we've built why is that well
because that is where the data centers
are that is where the economic activity
is that is where in many cases the users
are that is where companies want to have
their servers and want to build their
infrastructure um that is where the
capital is and the investors and all of
these pieces of the puzzle and so we've
built a power overlay using the latency
structure of the internet on top of that
and this is what it looks like um so we
exist in a world where there are two
fundamental realities the first one is
that much of the world's power is
already centralized that includes
military power economic power
geopolitical power Social Power and more
um and on top of that the disturbing
trend is that centralization begets more
centralization so centralization is an
accelerationist Loop onto itself uh this
is present in markets through phenomena
like economies of scale or Winner Takes
all it's present in Zero Sum games such
as trading it's present in auctions Etc
so when you have one sort of
centralizing vector that tends to bring
all sorts of centralization into various
aspects of your system
something we really want to avoid if as
we said before deconstructing the nation
state is it all on the radar for this
project so what I would say that given
that we are in these situations we have
to stop yoloing uh protocol proposals
and upgrades uh in terms of this power
Dynamic and this topology on which we
exist and instead we have to start
treating distribution of power globally
as a first class goal for the next
chapter of eth how can we be intentional
about where we're pushing power in the
system this is much much more important
than the performance of the system fast
block times throughput latency anything
like that because if you have those
things without having distributed power
you've essentially just reinvented the
systems that we were trying to escape
this whole time those performance
systems already exist um otherwise we
come back to the reality where much of
the world is centralized and
centralization begets centralization so
instead of that let's stop yoloing
protocol proposals and treat
distribution of power globally as a
first class goal in E3 okay I'm going to
exit the infinite Loop and instead go to
the infinite Garden so this is an actual
picture of my grandmother growing her
own infinite Garden um and I think the
solution the exit to this this Loop is
planting our own Gardens building our
own systems so let us all together kind
of brainstorm this infinite Garden of
power distribution and think about very
intentionally carefully and together
about where we want power to go uh I'm
going to give you one troll idea and I'm
sure you're going to hear many more over
the next few weeks but this is going to
be E3 done my way uh this is the best
hatching GIF I could find that was free
Shout Out Wikipedia Foundation but it is
very cute um all right so in my opinion
these are the four pillars of e3 as I
see it and I say pillars because these
are actually non-negotiable properties
if either of these four things any of
these four things are compromised on we
will fail to achieve the goals of
cryptocurrency we will fail to achieve
the goals of ethereum
and as I said in the beginning of the
talk the price will obviously be zero
regardless how much institutional
interests or ETFs or Etc we're able to
create um so these four pillars as far
as I see them uh number one pillar is
permissionless and I'm going to explain
each of these in Greater depth uh number
two is distributed from a technical
perspective and a computational
perspective number three and this is the
most important property by far is
geoeconomic decentralized and we're
going to Define that very carefully
shortly and number four is neutral
Builder efficient um so what are these
pillars let's get into it well the first
one is permissionless this is something
we should all have at least a little bit
of context on in this space but
specifically um I slice it with thinking
about me and how me is expressed in the
protocol because that's what I work on
so for me what permissionless means is
that any actor is able to express their
value or preference into a block at any
point in in the block construction
process um and that value is able to
percolate to be expressed through the
process and into the system uh you might
note that this is actually the same as
many definitions of censorship
resistance essentially if you pay a fee
you get in is one slicing although
there's a lot of kind of details there
um okay other than permission lists we
must also make E3 distributed so this
one is pretty obvious too this means
taking computations that right now
require one big computer or one big
server and bring taking them down into
small pieces that we can then distribute
kind of all over the network and all
over the world um without doing this
it's hard to imagine how to decentralize
if you require a huge computer to do
everything in one central place that's
inherently not
decentralized um all right this property
as I said is the most important
geoeconomic decentralization I'll spend
a little longer on it um so this
specifically is a is a very specific
notion of geoeconomic decentralization
saying that col a in the protocol must
yield minimal additional profit so this
is not saying hey we have a note in
France and a note in the US it's not
saying hey we're on three of these AWS
topologies of power we're on three of
these links or five that is not
geoeconomic decentralization geoeconomic
decentralization is saying that there's
a Level Playing Field in your system for
people who are participating outside of
those existing corridors of power
outside of those existing latency links
outside of that game theory we've
created with with AWS and those people
must be able to participate as
profitably and as meaningfully as the
people who are sitting in New York as
the people who are sitting in Japan
collocated with binance and Etc if you
reduce the participation of those
systems in the network in the iterated
game as time passes your network
collapses to these Central points of
geography and power and then you lose
any hope at censorship resistance or any
of the other properties you want all
right so those properties sound great
can we actually build that well this is
my troll road map to uh get there uh
it's a little bit oversimplified but
hopefully it communicates the point so I
believe right now standing from today
there are two things or or or or kind of
two broad pushes I want to work on the
first is to teifi everything why teifi
well we're going to get more into that
in a second but basically tees allow us
to distribute the computation so
remember when we said before the one big
computer becomes many small computers
tees give you the trust apis to make
that possible with untrusted parties
operating these small computers and once
you have this distribution you don't
have decentralization yet but at least
you're able to start pushing pushing
this infrastructure and pushing the
power to the edges of your network and
outside of those lines of AWS those
lines of power that we have today so
after we teifi everything we have to
start in a cycle doing two things the
first is pushing this power to the edge
as we deconstruct the computation as we
modularize it we push and then the
second thing is also to reduce the power
of actually tees in our system so tees
are not a silver bullet they're not you
know a magical solution to everything
they give a lot of power in the system
to Intel they take it away from that
graph that I showed you earlier with AWS
and move the needle a little bit more
right now towards Intel and Nvidia and
AMD and other Hardware
manufacturers so while I would argue
that's better than only having kind of
trafi latency corridors determine the
evolution of our Network it's still not
perfect right and there's a lot we can
do using other cryptography including
what we've heard on the panel before uh
using using other alternative te
approaches open tees uh things like that
to sort of remove power from the te
itself as well so I think it's a
two-track approach once we have the
platform to distribute and push things
to the edges we then have to actually
start pushing things to those edges and
I'm going to cover how you all can help
with that shortly um but also start kind
of eroding that Core Power that we've
now built up in moving this needle to
this other party which is Intel um so
I'm going to ask for your help please uh
so please give me your arms or if you
don't have arms just your body give me
your soul sounded kind of dystopian so
I'm not going to ask for your soul uh
but please give me your help in this and
how can you all help with this well if
you're a Dap developer if you're an
infrastructure developer if you're a
user ask yourself how can we for our our
uses what we're doing what we're using
the protocol for how can we get power
off of these corridors of power that we
see here can we use endpoints that are
in different locations do they meet our
needs can we deploy our server somewhere
that geographically makes sense for the
change we're trying to create in the
world rather than defaulting to us east1
on AWS because it's the first thing that
happens when you click launch are we
able to make that change as a space I
think everyone needs to spend some time
thinking about what am I doing and is it
actually helping centralized power onto
these power corridors or is it actually
helping push power out to the edges uh
which is what actually underlies the
long-term value of decentralization and
cooperation and even the price yes um
okay so going back to this graph uh um
well one obvious thing you might just
say is oh we have many boxes why not
just have many of them just sign or have
some sort of list where the proposer is
forced to sign well the reason is very
simple because it doesn't actually solve
the power distribution problem it's not
meaningful solution to censorship in any
way right um if in your metag game you
collapse to a state where the system
itself is very centralized no form of
technical papier-mâché technical
decentralization Etc even though it
feels really good to us as technologists
it feels great to just say like hey we
can just do this and it solves the
problem does it I mean let's let's let's
think about it for a second um so
certainly on binance Smart chain it
would not and in general what I would
say is censorship and power dynamics and
the way our money works these are
political problems we're not going to
Tech Tree our way out of these problems
we need to have deeper conversations
about where the power is in our Network
where we're building power in our
Network and how we iterate that towards
the place that works better for us um
that being said that doesn't mean that
as technologists we can do nothing our
job is not to make it worse so please
also help me in that if you're
participating in this space do not
centralize power back to those corridors
um and remember today we already live in
a world where much of the world's power
is centralized and centralization begets
centralization so I think this is really
existential to eth we're at the point
where we have a choice as a community of
do we start pushing the power we've
built out outside of AWS or do we
concentrate it seeking ETF inflows
seeking Stock Exchange listings seeking
trafi participation and concentrate the
system to the very corridors of power
that we thought we were
disrupting um so to get actual
decentralization well the definition is
very simple it's how much have you
pushed this to the edges um and I wish
it was something that could be easily
Quantified but unfortunately it's not
and that's just something we have to
live with a few more things I have to
say so the first is um this is a little
bit spicy and a little trolly I think we
should reject the ethereum endgame so
the ethereum endgame for those who know
it specifically is a slightly older
probably like somewhat out ofd post so
I'm kind of attacking a strawman here
basically saying that like hey is it
really that bad if we have these big
centralized machines doing things
specifically for me but then we kind of
keep them honest with the rest of the
network we keep that lightweight and
everything I think that's defeatism
personally I think we can decentralize
all the things and I think as long as
you have a central Corridor of power a
central source of concentrated power any
sort of system on top is not going to be
able to meaningfully police or control
it uh so we need to actually
decentralize all the things that require
the big machines as well
um doing a deeper dive into how this
relates to censorship resistance um so
censorship resistance is a very
interesting topic traditionally in the
academic space it says that if you
create a transaction that assume you pay
the fees you'll be included within some
number of blocks that number is called
Delta it's called the censorship
resistance or synchrony parameter um so
one question I have for us as a protocol
is what Delta do we actually need and
how do we value various Deltas in the
protocol
against other properties we care about
like power distribution kind of uh
Geographic decentralization Etc uh
because as you push Delta to zero you
actually get Fair ordering out of the
the censorship resistance definition
right if you need to be included
immediately as soon as your transaction
is sent well what does that mean for the
person that's on the other side of the
world how does that stack up with them
what if your Delta is below the network
limit how does that then get resolved
into the protocol how do we weigh
collapsing these trade-offs against
other centralizing effects we can create
in the meev space that maybe help us
build this robust geopolitical base and
actually allow us to push power back
into the edges so I think the most
dangerous thing the space can do right
now is essentially fetishize and Chase
one block censorship resistance at the
expense of all of the core properties
that will actually provide geopolitical
robustness and censorship resistance in
the long term I think we haven't had a
conversation in the community about how
to weigh those two things together
together uh so let's do that please
before we start yoloing protocol updates
uh and let's do that in a way that
addresses this approach to to censoring
our
networks um so what we need for
decentralization is real Global
meaningful distribution of power that
sounds great Phil but we all know
there's certain things standing in the
way of that um so the first one is what
I call ux fenel this is a web 2
mentality that you need to make things
faster and more addictive for your users
if your users aren't addicted if they're
not running on your treadmill if they're
not generating returns you failed you're
a bad person you're a bad founder no
that's not the way we build web 3
applications I'm sorry uh right if you
chase ux fentanyl you chase the dragon
over and over and over again to the end
State well now you need 50 milliseconds
now you need 10 milliseconds now the
mind can perceive 5 milliseconds we've
gone down that path in web 2 and we've
ended up with users that can't
meaningfully interact with the
technology these zombies that just are
kind of fed these puts right how many
people like that here nobody likes it
right so let's stop that in web 3
please enough um yeah
seriously another one I want to talk
about and this is a little bit mean to
the EF so I feel a little bit bad
whenever I talk about this but napkin
research um and I tried to choose a
slightly fancier napkin this time
instead of like a like a dirty napkin or
something but I think we do a lot of our
research discussions very informally and
without even having deep conversations
about what are princip what does
censorship resistance mean to us what
does this protocol change mean how do
you define it I think we can do a lot
more I've written a blog post about a
few ideas I have but I'd love to talk to
people because I think the problem with
napkin research is when you have a room
this big the napkins become a flood and
it becomes too easy to Lobby too easy to
capture the process too easy to get kind
of YOLO protocol upgrades and bad ideas
shipped into the L1 we all care about so
let's kind of upgrade our napkin uh the
problem is if you combine napkin
research with ux fentanyl that's pretty
bad situation so uh that that I think is
how eth goes to zero it's the
combination of Na napkin research uh and
ux fenel eroding the decentralization
we've built so carefully um and leaving
US Open to capture to co-opting and to
rebuilding the systems we sought to
evade so in all of that the exit must be
globally distributed power there is no
alternative the alternative is z e say
it again and again and again please in
the mirror let's move beyond the napkin
um this is a table that I have from a
talk I gave at eth Denver I encourage
you to look it up it talks about all the
technologies that we have including as
we talked about kind of programmable
encryption and there are various
tradeoffs for deploying in these
contexts that we have in distributed
protocols including who would break them
including rent privileges including
Geographic decentralization which I
think is the most important row here uh
we need to jam more about this and fill
this table out more unfortunately I
don't have time to go deep today but
please check it out and let's discuss
more okay I'm going to leave you with
one sound bite y tees well they give us
the theoretical maximal performance for
taking all of these monolithic things we
have and distributing them so we can
push to the edges and at least for what
I care about which is the meev context
we can iterate the security there and
for your dap if you want to do this the
recipe is simple build demand distribute
the infra to where your demand exists
natively to it and then scale your
network from there as for what flash
Bots is doing we're doing so many
different things in terms of teying
everything pushing it to the edges
creating platforms for you all to push
things to the edges more there's a lot
that's going to be coming out in the
next few weeks so the only thing I can
ask is for you to stay tuned or find me
later and please don't forget that I
need your arms so that we can get out of
this power dystopia all right thank you
very much everyone all right Philly
well well
well napkin fenel and arms that's quite
a fascinating presentation but
nevertheless let's go right through our
Q&amp;A we got about 4 minutes left is there
any value to centralization at all or do
you believe everything in life should be
decentralized what do you think Philip
yeah I mean I think for example uh
government is fundamentally centralized
right and many people find that value in
many contexts I think you know like uh
for example my laptop is like a
centralized Computing hub for myself I
don't necessarily want to decentralize
that I think it really depends on the
application I think decentralization is
useful where you want cooperation across
differences and that's actually where
the power and censorship resistance
comes from the more different people
that are cooperating under the same tent
and the more each one walks away feeling
like yes that was fair that was a just
outcome the more robustness the more
censorship resistance you get for free
uh and so I think in those cases it's
it's it's not centralization is is
harmful but in other cases it totally
does make sense excellent thank you very
much all right I see people voting and
up voting the up voting the questions
right at the top with five votes te are
Peak centralization three us companies a
local device zk's viable alternative
take it away yeah so we can have a
deeper conversation about ZK zks don't
allow for the kind of like Interactive
group computation that you need to do in
a lot of consensus protocols or for
example me or transaction processing so
maybe like kind of at the edges of like
okay if I show you a proof maybe you can
run this more limited algorithm yes but
at the core it's not really the same
Tech or the same abstraction I think all
of the entries in that table ZK MPC fhe
tees Etc cryptoeconomics they can all
chisel away at the centralization so
it's all about using which one is
appropriate for your app maybe your app
is already centralized maybe it doesn't
need geod decentralization then why
would you use a te right um Etc so like
I think it's about putting as much as
possible off tees and making tees also
able to be kind of more trusted by
having open tees and things like that in
the future but yeah it is it is a
centralization risk for sure all right
excellent question excellent answer how
do you think centralization risk of
staking compares to the rest of your
pillars
I'm not sure what centralization risk of
staking means uh if it means like
basically the stake set becoming more
centralized or the fact that staking
exists centralizing the coin Supply I
think there's many like slices of
staking and
centralization um I think I think yes it
is kind of implied by the rest of my
pillars in my worldview like if we have
permissionless and distribution and
specifically geod decentralization where
it's fair for you to participate no
matter where you stake I think you get
less stake centralization so I would say
for me it's like Downstream of the
pillars if you want to slice it there I
think it is a totally valid thing to
have on the table say like we don't want
centralization into the stake set all
right we got one minute more let's try
one last question with six up votes te
solve every problem that was previously
described in the programmable
cryptography session why aren't more
people promoting them not only do they
solve all the problems but you can use
them together to give you defense and
depth to give you various optimizations
and things like that we're building like
a lot of stacks to help people do that
so I think a lot of people are promoting
them I think people are afraid I think
people in crypto and in life and in
general they love binaries either tees
are broken and they're useless they're
garbage we need to burn them down or
they're the best thing ever and like
they cast every opinion on te into one
of these two buckets the reality is much
more nuanced they make sense for a lot
of applications they don't for many
others um I think people are promoting
and using them and seeing success using
them actually basically everywhere they
make sense um so I do think you will see
more people promoting and using them
over time definitely in time to come
ladies and Gentlemen let's give our
speaker another big big round of
applause thank you very much
philli Sharing The Cutting Edge of tees
for the ethereum
ecosystem all right wow I must say just
one thing if you haven't done it already
just take a quick look around the hall
look at how crowded it is wow there is
not a single seat that's empty or maybe
just one or two so I've talked to my
volunteers and they've asked for some
help as you can see there are some
people standing at the side some people
sitting on the floor if there is an
empty seat in the middle of any of your
rows can you please fill it in fill it
in please so that people at the site can
quickly enter right now we want you to
get as intimate and as close to each
other as possible because obviously the
next session is very very popular our
volunteers are trying to find yeah
excellent thank you fill in the seats
fill in the seats our volunteers are
right here in the middle they're going
to be instructing you to fill in the
seats yeah because there's so many
people look at the queue outside there's
barely any space it's like a Taylor
Swift concert it's full yeah it's full
but just barely a few seats here and
there please again work with our
volunteers please listen to their
instruction now very important for those
of you outside the hall I know you can
hear me and I know you really want to
come in but for reasons of safety we
can't let everyone come in because
there's always got to be a part where
people can walk out in the event of
emergency unlikely but we need to have
one there's no seats on the
aisle no sitting in the aisle all
right okay again our volunteers are
going to be directing you guys so please
work with us work with us you need to
make sure there's at least a clear space
in between so that people can walk up
and down all right we can't have
everyone sitting in the aisle and
blocking it completely all right now
again for those of you if you can't make
it into the Hall don't worry we've got a
live stream of the session just open up
your Devcon passport open up your Devcon
passport scroll to the bottom of the
session and you'll see a live stream
together with translation tools as well
it's all through the Devcon app now
again try as much as possible make some
space at the side we need to have a
clear walkway on all three aisles okay
we can't block it completely I wish we
could had more people people inside and
I know you guys really want to hear the
next talk the next talk is even more
special because it says on my notes that
the title is redacted I had to go to
Twitter to our speaker profile just to
understand what on Earth the talk is
about well our next speaker has spent
months months and months researching and
trying to figure out what would ethereum
look like if he had to redesign it again
right so obviously it's a very exciting
session our next speaker obviously gared
lot of attention with his session even
though he has no title the hall is full
and again at the back there I do
apologize I know you guys really want to
come in but please just open your app
you can watch the live stream or if you
want to listen from the back that's fine
as well for the rest of you here thank
you so much for making space for others
as well ladies and gentlemen are you
excited for the
session that's what I want to hear
ladies and gentlemen put your hands
together and let's welcome our speaker
Mr Justin Drake
[Applause]
thank you and I do apologize for those
that are outside uh this is a main stage
for ants next time we'll do better so
the the weight is almost over the thing
that I've been working about on for
almost all of this year is called the
beam
chain so
so the beam chain is a proposed redesign
of the consensus layer that incorporates
all of the latest and greatest ideas
from the research road map and the goal
is to try and transition in a safe and
fast manner from the beacon chain that
we have today to this beam chain which
is much much closer to the final design
ethereum now before I share more
information I have two disclosers um
disclaimers disclaimer number one is
that this is just a proposal this is my
proposal and the proposal will only go
forward if there is rough consensus with
it going forward and the second
disclaimer is that there is no new token
there is no new network and we're
reusing the same ticker and vitalic was
very very clear as to what this ticker
is now I in in the rest of this talk I
want to take what may sound like a
totally crazy idea and convince you that
actually it maybe not so crazy that it
might be a reasonable proposal to put on
the table to completely redesign the
consensus layer and first I want to tell
you a little bit more about the beam
chain and what the big picture vision is
all about so the scope of the beam chain
is specifically the consensus layer and
I'm excluding the data layer with the
blobs and the execution layer with the
evm and the reason is that the blobs and
the evm are directly consumed by
applications and there is a need to be
forward compatible and so the the um the
opportunity to modify these two layers
is rather limited on the other hand the
consensus layer is not directly consumed
by applications and so there's a big
opportunity to shake things up a little
bit
there now why am I proposing now to do
this massive redesign of the consensus
layer and it basically Bulls down to the
fact that the beacon chain is kind of
old the the spec uh was frozen 5 years
ago and in those 5 years so much has
happened in particular we have a much
better understanding of me 5 years ago
we were extremely naive when it comes to
meev and since then we've seen the
market really blossom and and and and
and grow and we also have uh a much
better understanding of mechanisms that
can help us mitigate the the negative
externalities of me secondly from an
engineering standpoint we have this
wonderfully powerful technology called
snarks where there's been plenty of
breakthroughs in particular we've seen
snarks become orders of magnitude faster
over the last five years and we've seen
the Advent of ZK VMS ZK VMS are amazing
technology that allows any programmer in
the world to make use of this very
powerful technology without having to be
an expert in cryptography or in
SNS and then finally with the benefit of
the of hindsight we now know what the
mistakes we made with the beacon chain
and we have a bunch of technical debt
which is extremely sticky and tends to
Pyon over time and maybe now we have an
opportunity to clear this technical
Deb so I'm suggesting putting the
greatest and latest of the consensus
layer road map in the beam chain so I
guess it might be worth spending a
little bit of time looking at what
exactly is in the consensus layer road
map there's basically nine different
items and I've categorized them in three
different buckets block production
cryptography so the block production has
to do with me right now we have a lot of
centralization at the Builder and relay
level and one of the things that we want
to do is have inclusion lists that
dramatically improve censorship
resistance once we have censorship
resistance with inclusion list will'll
be in a position where we can cleanly
decouple the validators From the Block
production Pipeline and this is called a
tester proposer separation and there's
ideas like execution auctions
and then the final uh item here in the
block production bucket is faster slots
maybe we can take the 12C slots that we
have right now and Shrink them all while
preserving the invariant that if you are
on a home internet connection you can
participate as a validator as a first
class citizen even if you are in
Australia with a high latency internet
connection second bucket is staking
the researchers I think have come to
consensus broadly speaking that the
current issuance curve is kind of broken
and that there is an opportunity to
improve the health and long-term
outcomes of eum by changing it uh the
second uh item in the road map here
under the staking bucket is this idea of
dramatically reducing the total amount
of e to become a validator from 32 e
down to just one e and there's ideas
like orbit
that have that have been circulating
around recently and then finally this is
an idea that has happened that has been
talked about for many years is single
slot finality can we dramatically
accelerate the process of ethereum
gaining finality and then the final
bucket has two big ticket items number
one can we snakify the whole of the be
the the the the consensus layer in real
time using reasonable hardware and then
finally can we make the cryptography
that is securing ethereum sustainable
for the next decades and centuries and
make it postquantum
secure now the coloring here is meant to
suggest whether or not the item in the
road map can be done easily
incrementally or or or whatever it can't
so the five sorry the the the four green
items here in the top left corner are
items that I think can be done and
should be done in incremental Forks on
the beacon chain but then when we get
rid of those we we're left with big
ticket items the red items that I would
argue are best done in a more holistic
way so take chain SN ification for
example in order to achieve realtime
proving of the beacon chain with
reasonable Hardware we're going to need
to change the hash functions we're going
to need to change the signatures the way
that we serialize and meriz the state
and this is a massive change to the uh
to to to the beacon chain and so maybe
there's an opportunity while if if we
were to make such a change to change
other things at the same time and then
the similar thing can be said for the
bottom two red um boxes faster slots and
faster finality the truth is that 5
years ago our mindset was Security First
when we designed the the beacon chain
and performance was not really a main
consideration and with the benefit of
hindsite we found that there are designs
that preserve all of the security that
we want and at the same time pick some
of the lwh hanging fruit that is
available to us to improve
performance okay so this slide here is
trying to show the mapping from the
consensus laer road map that I showed
you and the talic broader road map we
have some items that are classified
under the merge some that are under the
scourge and then a couple that are under
the Verge and the splurge and the whole
point of this slide is to communicate
the fact that the beam chain is not
about changing the road map more so than
it is about identifying a specific
subset of that road map and accelerating
it and putting a mimetic wrapper around
it now one thing that is new uh in in in
the uh consensus layer road map here is
the fastest slots and the reason is that
the discussion around fastest slots has
happened this year in 2024 but the talic
road map diagram was only last updated
in
potentially accelerate these big ticket
items there's a lot ofch technical debt
that I mentioned that can be clear
cleared out if we have single SL
finality we no longer need EPO we can
just have slots um the the deposit
contract that we have right now is kind
of crazy and it's it's a remnant of of
the merge and things like the sync
committee is infrastructure that we
won't need going forward if we have real
time real time notification of the
beacon chain and the list goes on and on
and on and this is not as as I mentioned
to just clean it up all in one go and
you if you're interested in learning
more about some of these Beacon chain
mistakes last year I did a whole talk
where I I talked about 20 or so
different mistakes that we made in the
beacon chain
design okay so this is the big picture
view of how we have done upgrades to the
consensus layer since Genesis so in the
bottom left here you can see we did
Genesis in 2020 and since then it's been
an extremely regular pattern every
single year we've had a new fork and
every time we had a fork we made one
incremental change to the consensus
layer so in 2021 we added syn committees
in 2022 we did the merge in 2023 we
added withdrawals and then Proto U Proto
dang sharding and and soon in 2025 we're
going to increase
the the the max effect effective balance
now what I expect will happen is that
over the coming years we will continue
doing these incremental Forks um and we
will be picking up the low hanging fruit
um that that that was marked as green
bubbles in the in the road map in the
top left corner of the road map but then
we're going to kind of hit a wall and
the reason is that once we've picked all
of the low hanging fruit we'll be left
with all of the big ticket items that
are much more difficult to do in an
incremental fashion and this is where
the beam Fork happened the beam Fork is
an opportunity to have a Quantum Leap
Forward in terms of upgrading the
consensus layer all in one go and one
way to think about the the the beam Fork
is as a batching opportunity we're
batching multiple upgrades into one one
single fork and this has benefits both
technically and from a governance
standpoint and one way to think about
this baching opportunity is as oif
accelerationism this might sound like an
oxymoron but the basic idea is that we
want ethereum to go in maintenance mode
as soon as possible and right now
there's this tension because we know
that there's these big ticket items that
require a fundamental rearchitecturing
of of ethereum and the more we drag it
along the further ethereum will be in a
position where it can comfortably
aify okay part two I want to try and
highlight some of the technology that is
that is going into the the proposed beam
chain and the way that I would frame
this is basically in eras of ethereum
consensus initially we had the proof of
work error of airmed consensus and then
we moved to proof of stake and now we're
potentially entering this ZK era of
etherium
consensus and in this ZK era we would be
making heavy heavy use of SNS as a
technology so one place where we' be
making use of SNS is SN ifying the
entire beam chain the entire consensus
layer and this is where the ZK VMS
become extremely extremely handy so
imagine that you have implementations of
the the beam chain in various high level
languages in Rust in go for example what
you can do is compile these high level
languages down to bite code that the Z
kvms will understand and get SN
ification without having to worry about
the details of this notification
process now one thing that I do want to
highlight is that the only part that
needs to be snar ified is What's called
the state transition function which is
basically the crystalline core of what
it means to be a consensus client all of
the infrastructure surrounding the state
transition function for example the
networking or the syncing or you know
the the caching optimizations or the
fork Choice Rule n of that has to be
snfi and ultimately the state transition
function is a small subset of what it
takes to build a
client and what we've seen recently in
the last couple years is risk 5 become
the de facto industry standard for these
Z kvms so risk 5 is an instruction set
and basically you can take high level
code and compile it down to risk 5 and
we've seen seven different uh
companies provide these risk 5 zkv Ms
you may have heard of risk zero and sp1
and the list goes on and
on now one little side note here is that
this
exact technology which is extremely
powerful can also be used at the
execution layer for the evm but that is
a completely different story to the beam
chain story it's one which is extremely
exciting because it means that we can
dramatically increase the gas limit as
well as vertically scale aerum layer one
but this is going to have to be for a
different
talk the other place where we make heavy
use of snarks in the beam chain is with
uh aggregat signatures we want to have
postquantum aggregatable signatures and
the proposal here is to use hash
functions hash functions are postquantum
secure and you can use that as a basic
building block to build your
cryptography so we would have hash based
signatures that are produced by the
validators by the ATT testers and we
would also have hash based SNS where you
can take many many thousands of
signatures and compress them down to
just one proof and with these two
combined you get a hash-based
postquantum aggregatable scheme that
could be used for
ethereum and one little nice detail is
that this aggregatable scheme is
infinitely recursively agre aggregatable
so you can take Aggregates of Aggregates
of Aggregates which is something that we
can't really do today with BLS so it's
much more
flexible and the reason why I have this
proposal here today is because in the
last few months the progress in
performance of snar ifying hash
functions has gone through the absolute
roof so for those who are in the know
we're now able to prove on a laptop so
this Benchmark here was done on a laptop
CPU a MacBook Pro we're now able to
prove 2 million hashes per second which
is an astounding amount of hashes per
second and this means that this hash
based proposal has the potential of
being extremely performant for the beam
chain now in addition to the ZK the very
powerful Z kvms and snars that we would
be using I also want to highlight that
to a large extent we would also be
reusing existing infrastructure so the
networking libraries lip P2P the
serialization libraries simple serialize
all of that can be reused as is
today same thing for the p pyc is the
the the framework that we use to write
the formal
specification sorry the um the python
specification and and the unit test and
we can also reuse protocol Guild all of
which is infrastructure that didn't
really exist when we started with the
beacon chain and the same thing can be
said about teams when we started the
process of the beacon chain there was no
team there was no consensus client teams
so the five consensus client teams that
we have
today this is Manpower that could can be
reused and doesn't have to be rebuilt
and in addition to that we have
dedicated teams that will put in place
for the merge for example e panda Ops
which does devops and the security team
within the foundation and I also want to
give a shout out to the incentives team
and to the applied research Group which
are also teams that all of this
infrastructure didn't exist and we can
just reuse it for free
okay final part so here I want to try
and highlight some of the next steps and
how I see the the future so one possible
outcome here is that starting from
process so this would be something that
a small group of
researchers would would do uh and it
would take maybe a whole year and then
in 2026 the building process can happen
where clients would start writing
production grade code and then in 2027
would start an extremely thorough
testing process to make sure that this
is all production grade and safe to
deploy on
mainnet now the next step for me as a
researcher would be to start writing the
executable spec which I call the
executable road map and the idea is to
take the pixels that we have of the road
map combined with the the hundreds of
thousands of words that have been
written on E research and in academic
papers as well as all of the ideas that
lie in the the minds of researchers
combine all of this and extract The Core
Essence which would be this executable
spec and ultimately it would be a very
small document roughly 1,000 lines of
python
code now one exciting thing for me here
is that the chain assuming that there is
rough consensus to go in this new
direction would be a fantastic
onboarding opportunity to bring fresh
blood into the space especially for the
consensus clients so today we have
consensus clients in North America in
Europe in O Oceania and I'm very pleased
to be able to announce today that we
have already new consensus client teams
that are willing to build beam clients
so we have one which is based in India
which is called the Z team this is a
beam client written in Zig and then we
have Lambda class in South America that
has signaled an interest to also write a
client and so if you will also get
involved and we're going to need a lot
of excellent Talent we're going to need
speckers and networking experts and
coordinators and cryptographic experts
and and client devs please reach out at
this email address and beam up with us
on this new adventure thank you so
much right let's hear one more time come
on a bigger round of applause that was a
fantastic
presentation really really good really
appreciate it and I'm sure the audience
appreciated it as well now now is the
time to ask your questions or if you see
an interesting question please upvote it
now for those of you in the hall don't
leave yet okay just give us some time
because the volunteers need to clear a
bit of the space there are still a lot
of people outside so at the end of Q&amp;A
don't move stay where you are because
our volunteers need time to clear the
hall later okay so just stay where you
are and I'll instruct you at the end of
Q&amp;A all right Justin let's look at the
first question with the five votes right
on top deploying many changes at once is
risky in that if any one change gets
delayed or has a bug they all get stuck
or roll back how hard have you tried to
break them down in incremental
batches okay great question so there's
many things that I've tried to do to try
and drisk the beam chain the first one
is to encourage all of the incremental
upgrades remember the four green items
in the road map that could be done ahead
of time and by going through the process
of these incremental upgrades we're
going to go through a lot of the of the
lessons and a lot of the hard work and
discover the challenges there and then
um the other thing that I'll mention is
that the beam chain is really only about
changing the core of the client which is
the state transition function and a lot
of the the potential opportunity for
bugs whether it's a networking layer or
the merization
libraries or you know the fork Choice
rule a lot of that infrastru ructure can
to a large extent be reused another
thing that I want to do to drisk the
beam chain is make sure that all of the
existing clients are on board because
ultimately these are you know 50 men and
women that have many many years of
experience building consensus clients
and they know what a lot of these
pitfalls are and then another thing that
I would say in terms of drisking the
beam chain is that we would have an an
especially intensive testing period
which could last for example a couple
years this is what I had in the strawman
timeline and during that time we would
do many many rehearsals on dev Nets and
test Nets so that we could grow
confidence that there isn't a bug in
this big upgrade excellent thank you for
the answer indeed testing is very
essential when it comes to the
blockchain and updates now the question
that I've seen has gotten the most votes
of any of the rooms so far 20 is the
number to beat are you okay Justin with
people calling this ethereum 3.0 oh the
meme layer of ethereum wants to do this
okay great question so in my opinion the
moniker airm 3.0 is not appropriate and
the reason is that the beam chain is
only about the consensus layer it's not
about all of the firm layer one it's
just a consensus layer excludes the data
layer D sharding and it also excludes
the evm and there's lots of exciting
stuff happening at these layers of the
stack as well so this is why I've tried
to avoid the etherum 3.0 Monica all
right I mean it's a fair fair uh Fair
answer as well but people will do what
people do best and they'll call it
ethereum 3.0 and we'll get a few new
coins and people ask all the exchanges
will my ethereum change and all of that
um but let's go to the next highest
voted question which ZK VM will be used
for beam chain as there's no
standardization of ZK VMS okay fantastic
question so the amazing thing about the
proposed design and actually this is an
idea from vitalic is that the snar
ification would happen offchain and
would not be enshrined in consensus so
what that means is that every
independent validator can choose which
ZK VM they prefer so they can use any of
the seven risk 5 ZK VMS but they can
also use non-risk 5 Z kvms and
ultimately by having this offchain sfic
it means that if there's a bug in one of
them it's very easy to fix if there is a
performance optimization in one of them
you just update your client and you get
this this performance
optimization and also it means that we
don't have to pick winners and we don't
have to add a lot of complexity onchain
all of this is offchain complexity at
the social
layer all right thank you we got 30
seconds you want to take the last
question at the top any way to
accelerate that timeline oh we moved uh
okay okay okay well let's take the first
well okay they voted for 18 19 okay
let's do that one why are e researchers
obsessed with low issuance it's
all come on guys we need the Dow to
agree consus where is the consens okay
Justin take whichever question you want
okay I'm happy to answer all of the
questions later on outside that's fine
but um any way to accelerate that
timeline please email us at beam.
chain
f.org if you want to accelerate let's go
all right ladies and gentlemen one more
big round of applause for Justin
absolutely
fantastic fantastic
session once again I'm okay wait stop
don't move yet okay let my volunteers
clear the back area because it's really
crowded outside and we want to avoid a
traffic jam Bangkok already has a lot of
traffic we don't want to put traffic
here so please give my volunteers just
one to two minutes to clear the crowds
behind the hall don't worry you'll have
enough time to reach your other venues
if you want to change however I would I
would love to for all of you to stay
here because we've got another exciting
session that's going to be about the
history of history and philosophy of
Cipher Punk right so please stay tuned
for that now while you're in the hall
remember to go to your apps and when you
click on the Q Anda section in your
Devcon passport remember to claim your
card so if you click on it you'll see
the Q&amp;A session before you click join
Q&amp;A there's a collect card please
collect the cards for each session that
you attend all right okay I can see the
crowds have mostly cleared so slowly and
carefully make your way outside the hall
they've opened all three doors thank you
very much if you could please help us
slowly exit the hall and please make
space for others as well there's lots of
us here but as long as you all make
space together it should be fine all
right don't leave anything behind ladies
and gentlemen if you're taking your bags
with you just double check make sure you
haven't left anything behind if you have
any bottles of water or bags with you
please take them away as well yeah all
right appreciate it we're going to give
just a few moments uh for the auditorium
to clear and reset before we welcome our
next
speakers okay so if you could help me if
you see the doors open on the left and
the right please exit swiftly and
quietly thank you so much we really
really appreciate it and for those of
you staying for the cipher Punk session
and privacy session well make your way
forward come right to the front of the
stage as we learn about the history of
Cipher Punk taking down the nation state
privacy Freedom these are very important
Concepts in the world of cryptography
and in the world of the blockchain and
we're going to learn a lot about the
history and philosophy I don't know much
about it so I'm really curious for this
session as well
okay all right people still exiting the
hall that's absolutely fine slowly
slowly make your way outside on the left
and right you can go out as
well don't worry we'll give you guys
some time we'll give you guys some time
you want to make sure everybody goes out
smoothly and
safely all right while waiting ladies
and gentlemen those of you in the Hall
you can go to your Devcon passport app
and you can already start submitting
questions yeah you don't have to wait
till the session starts you can start
right now you can go to the app click on
the session the history and philosophy
of cyer Cipher Punk scroll right to the
bottom and then you'll have your live
stream you've got translations you've
got your collaborative notes and last
but not the least you've got your
Q&amp;A all right so you can submit your
questions already upvote your questions
as
well okay those of you at the back few
rows you can come in front come in front
and come and fill up the front as
well I know the session's about privacy
but let's also practice a little bit of
intimacy as we come closer to our
speakers it's always nice and I can tell
you it's a great encouragement to the
speakers to see the first few rows
filled with people all
right okay ladies and gentlemen while
the audience is still moving out I know
there's so many people we going give
them as much time as possible but we've
got to get our show on the road so if
you are exiting the hall if I could ask
you to just be a little bit quiet sh
just a little bit more quiet so we can
get our session started on the stage our
next two speakers are going to be
talking about the history and philosophy
of Cipher punk you know how we fight
against the nation state how we you know
we want to encourage human Freedom
through privacy and so that's a very big
topic a very important topic and we've
got two amazing speakers who are going
to be sharing about it together please
put your hands together and let's
welcome Harry and Max ladies and
gentlemen come on you can do better than
that let's give them a big round of
applause as we welcome them to the
center of the
stage hi
everyone okay so we are
here uh to basically bring back the
cipher Punk roots of blockchain
Technology I'm Harry Co of nim and I'm
Mark senior Dev Al for Nim so also if
you want to talk about building anything
with Nim uh come find me over the rest
of of the conference so I would just
like to begin this talk saying that I'm
actually very proud of vitalic in the
blog post where he decided he was not
going to bend the knee to Donald Trump
just because Donald Trump was going to
pump everyone's crypto bags Donald Trump
and authoritarian states are the
opposite of Cypher Punk it's the
opposite of our ethos the ethos of
cypherpunk is based on meritocracy
without
borders right not nationalism not
kicking out immigrants and all sorts of
other complete nonsense so I think it is
a good time to kind of go into the
history of how uh Cypher Punk came to be
and we're going to do it a little bit
differently I've seen a lot of talks
about you know Phil Zimmerman and Eric
Hughes and the original cypherpunk
movement but there's a lot of stuff left
out so that's what we're going to go
through I'd like to just give a a shout
out to the Father the inventor of the
term anarchism Pierre prone who had at
the dawn of the Industrial Revolution
many Core Concepts that now we are only
seeing come to fruition for example do
you know in 18 63 Pierre said we can
replace the monarchy with self-governing
communes and collectives and individuals
who will coordinate via
contracts and create their own
popular banking systems of course he was
uh taken out by marks and generally kind
of no one looks at them academically
anymore but there's really old roots and
then a lot of the questions that we are
facing today came forward in What's
called the Socialist calculation debate
where the question was how is it that we
can reorganize Society should we use
money or not should we plan in a
centralized way or not and most of
Austrian economics Hayek Ben Mees and
all these folks came from this debate as
a reaction against the Socialists from
Vienna like altoon nurth who claim that
money does not capture all the extern
externalities in the well-being of
population so there a really old history
that predates cryptography and the
invention of
computing about these topics should we
organize in a decentralized way
returning sovereignty and power to
individuals and to smaller communities
or should we centralize power if you're
interested in more tons of philosophy
work here but the general thesis is that
the spread of cryptographic techniques
which were originally the domain of the
nation state because the nation state is
based on hierarchies on the keeping of
Secrets keeping of Secrets around
agriculture keeping of Secrets around
military cryptography let this spread
into the general population and this has
been perhaps the most defining change in
sovereignty since like essentially
ancient Sumer
go for it Max all right so this section
of the talk we're going to go through a
couple of let's say the more basic like
um technological advances that have
happened and then I'm going to then
these these are things that we imagine
that kind of everyone here knows about
uh but we'll do a quick overview and
then we'll really jump into the more
like the social side of Cipher Punk and
how this is how it feeds back into the
technology it creates so in ' 67
Whitfield Diffy and Martin Helman they
kind of introduced public key
cryptography into the public domain
right so it's just the idea that you can
for the first time then you could create
a shared secret key with which you could
have like secret communication uh over a
non-confidential channel beforehand one
of the massive problems of actually like
setting up any kind of encrypted coms
with people was how do you initially
share this secret between both of you
right this is the public key
cryptography as well as being the basis
of like TLS SSL it's also obviously like
the basis of so much of the crypto that
we use today uh we do next
slide all right so then in
chasable electronic mail return
addresses and digital pseudonyms right
the tldr of this is how do you create an
anonymous untraceable communication
Network that protects the data of the
coms right as well as the metadata so
can you invis can you create something
wherein you can't tell who is talking to
who and when
next one sh it's the green there we go
and not too long afterwards he then came
out with another concept which is that
of anonymous credentials to defend
against a dossier Society so this first
line of this paper from
lot of stuff still sums it up today so
computerization is robbing individuals
of the ability to Monitor and control
the ways that information about them is
used so in 8 five charm was already
talking about the lack of agency that
people were having with regards to the
data that was about themselves and how
they communicate in the world and could
already see the kind of possible uh
dystopia on the horizon so finally we
had Diffy Helman they allowed people to
create to Envision stuff like misn which
allow you to communicate privately and
then also we have credentials which
allow you to transact privately these
two kind of key cornerstones of like
Cipher Punk Tech that then can be used
to Envision this kind of better society
that we're talking about
here so that was the stuff that I kind
of imagined everyone would already know
now we're going to the more fun stuff so
this was uh Resource One this was
resource one's project Community memory
this was the first computerized public
bulletin board system so the first
introduction that a lot of people would
have had to Computing in general uh it
was in the people's Computing Center in
San Francisco
and it was the yeah like I said the
first PBS so the first way that people
were able to like freely share and
spread information using computer
systems this is interesting because one
of the people who is criminally under
talked about in this space uh was also
key in not just Resource One but also
the creation of the people's Computing
Center and that's Jude milhon so
otherwise known as St Jude she was
actually the originator of the term
Cipher Punk itself so the title of this
Congress and everything else owed that
to her and as well as being a founding
member of the cipher Punk's mailing list
she was a civil rights activist so
actually this picture from the
Montgomery Police Department is after
she got arrested in Montgomery Alberta
on a Civil Rights march in '
and it was broad civil rights activism
throughout her entire life uh she was
also a senior editor at Mondo 2000 which
is now wired so you can see how both
Tech and culture is constantly
feedbacking the feedback is tight
basically
and a couple of choice quotes of hacking
as a martial art a way of Defending
against politically correct politicians
overly intrusive laws bigots and
narrow-minded people of all
Persuasions these are some of her uh
Publications take a picture um they're
all really fun and good but we don't
have that much time and a lot to get
through so another piece of culture
that fed back into the early Cipher Punk
movement and became part of it as well
it's true names by Verna vinger this is
a novel which actually has the original
use of the word Nim in terms of
pseudonym or hidden name and was even
though it was written in A1 thoroughly
predictive of government surveillance of
parallel online
spaces this then fed into one of the
kind of like the author of a series of
seminal texts within this right which is
Tim May so not only just true Nims and
crypto anak which was an essay that then
actually vinga enjoyed so much it was
invol it was included in the uh late
'90s
represses of true names he was a
founding member of the cipher Punk's
mailing list and his let's say
predictive power
to understand both the potential of this
Tech so providing the ability for
individuals and groups to communicate
and interact with each other in a
totally Anonymous manner um is something
to bring attention to finally a lesser
known let's say strain of thought that I
think is still foundational to a lot of
The Cypher Cypher Punk ethos that we
want to like push forward today is that
agorism so agorism until fairly recently
when it was like revitalized by the uh
agarist Journal so check that out
agorism
doxyz then this was a kind of a it was a
relatively little known strain of
political thought but still had a
massive impact on the cipher Punk
culture this is the idea of a counter
economy right so possibly a different
way of thinking about what we would
maybe call parallel Societies or these
kind of like
non-state um these non-state Market
structures right so his was very much
based in anti-statism and kind of went
all the way from black markets to gray
markets to just unregulated people
helping each other out and the novel
that's included here alongside night is
you could almost think of it as kind of
a a dramatized door experiment of a
Young Man who as Society is kind of
crumbling down um his kind of Journey
Through the agarist underworld of uh to
regain I suppose freedom in the way that
kin described it and I'll kick it back
to Harry
now so where things all started getting
real for the cipher punks it was
interesting Concepts and everyone here
is inheriting this tradition was
actually hilariously enough as the early
internet took off people leaked the
secret beliefs of the Church of
Scientology who you may know as a lot of
lawyers and they started trying to go
after some of the cyppher punks and
crypto Anarchist and this led to the
invention of what was called the cipher
Punk Anonymous remailer so you took
emails put them in pgp sent them in the
computer stripped off the header and
sent them out uh However unfortunately
those um those cypherpunk remailers were
attacked and this led to the first
implementation of mix Nets called
Mixmaster an anonymous remailer by Lance
Krell who I don't know what happened to
him I've heard various rumors and Lynn
Sassaman who people think was could have
been
Nakamoto uh and effectively you would
send your messages through a series of
computers and mix them up together and
that kind of unlined the messages and uh
this eventually led to tour by Roger
dingledine whose talk you should all see
I think on Thursday and they basically
said well you know Mix N are really slow
can we build something faster that does
web browsing but goes through multiple
peer-to-peer relays and that's the T
that's the anonomous solution that most
of us still use today and I remember
discussing with Roger once he was like
ah you know this hidden Services thing
what's it could it be good for and then
well it was good for Wikileaks right so
Wikileaks let uh Chelsea Manning who and
uh folks like Edward Snowden leak
documents securely ring the scope of the
mass NSA surveillance and the failure of
the Iraq War so forth and so on so
Wikileaks is effectively a Tor hidden
service and so it helped change the
world in the war in Iraq and the belief
of Julian S was by releasing information
into the world people could decide what
was true and what's false and this would
slowly eliminate the centralization of
power and the conspiracy between the
nation states to kind of maintain their
domination now the uh problem is of
course the nation states weren't very
happy with that they obviously put
Assange in jail I just want to give a
shout out to everyone who contributed to
Assange da I was good friends with
Julian and you know I said Julian don't
you have tons of Bitcoin he said I sold
it all the dollars like oh Jesus what a
stupid thing to do and then he was like
kind of unsure about this eth nft stuff
but then it raised 16 million if not
more to help him get out paid for his
legal bills and it's because of
donations from everyone particularly in
Asia that this happened uh so that's
absolutely wonderful and it's a real use
case of our technology after Wikileaks
was of course the rise of anonymous
which people may or may not remember
from 2011 the first people that
supported Arab Spring in Tunisia of
course also came together because of
Scientology and uh some of you may not
know this and he may not be happy that
I'm saying it but Mustafa from Celestia
back in the day his name was Tio and he
was the youngest member of one of the
kind of more prominent LC Anonymous
Crews and even uh vitalic himself was
work at the kind of before ethereum took
off he was living with Amir Taki and
other people in Spain working on dark
wallet the first private kind of Bitcoin
wallet because it slowly occurred to
people that Bitcoin wasn't private
Anonymous and we needed better
technology confidential transactions so
forth and so on they did what was sort
of the first not Ico but Bitcoin
fundraise and now uh dark wallet and all
the cool stuff before it like faircoin
and unst has evolved into dark F I just
want to give Rachel and Amir and
everyone here shout outs and definitely
come to Rachel's talk lunar Punk ingame
to know what the future we're talking
about the past but what the future of
Cypher Punk holds and it will be on
Wednesday H 4M on stage six and at the
same time as we're seeing this
resurgence the use of cryptography not
to centralize power in the state but
Empower individuals through Wikileaks
and so forth and so on uh anarchism
itself is resurgent uh there are now a
large amount of interesting and wildly
differential uh widely different
Anarchist books I'm going to recommend a
few here but effectively they kind of
argue that you know it's not just
domination is not just a nation state
but domination is how we think of the
world itself that the world is not just
something to be man manipulated and
controlled to satisfy our desires but
the world itself should be autonomous
and
free and this is there's also some newer
questions uh in this book I would
recommend there's the invisible
committee and the ton a French
Collective a book in 99 called the
cybernetic hypothesis and in this book
they said capitalism based on the
individual in the nation state is dying
but actually it's being replaced by
something worse a control Society where
computers are used to control and manip
manipulate our behaviors and to make us
completely transparent to various forms
of power in Domination but now the
domination is not centralized in the
palace centralized the king but spread
out and diffused through all
society and so I would just want to kind
of End by discussing a little bit we
covered a lot of history and hopefully
you got some cool screenshots of it but
what is actually the philosophy of
cypherpunk and I think it's actually a
descendant of the philosophy of
anarchism which remember happened at the
same time na the nation state itself
started forming and it's just the
critique of anarchism but given
technological power through cryptography
which is ultimately a nonviolent way to
redistribute power relationships away
from centralized power and two
individuals and smaller collectives
whatever they may be communes Dows so
forth and so on
so the decentralization of power is the
movement of sovereignity away from the
nation state into the individual and
importantly unlike all the rapid
nonsense going on in politics today it's
Universal to All Humans that we believe
that all humans should have the right to
use strong cryptography the right to
transact freely and to have freedom of
speech and that's like the fundamental
you can see how blockchain technology
enables that and also so it's important
that we you know we talk a lot about
Dows but the fundamental structure is
more deep voluntary Association that via
contracts and Market structures we can
create a society without domination and
exploitation by any form of ruling class
or other kind of terrible uh
self-inflicted domination and then
furthermore that information itself and
this is where cryptography comes in
quite useful should be based on strong
anonymity you should Anonymous first and
foremost and then you should as Eric
Hughes from the cyppher punk Manifesto
stated which we kind of skipped over but
it's excellent small text I recommend
reading it that the power that the real
power of cryptography comes from the
ability to selectively disclose yourself
to the world so you don't have a single
identity you can be a different person
in different social spaces at different
points in your life and amongst
different crowds and cryptography
enables that universally using the
internet and this gives us agency over
our flows of data which more and more
compose who we
are and the cypherpunk tech is still
under development again we have mix Nets
there's quite a few teams working on
them we at Nim are also working on one
electronic cash which uh you know of
course you have zcash and Monero but we
decentralized fast private ecash is
still not a solved problem and I think
this has been incredibly neglected we
need Anonymous credentials we need
ability to selectively disclose I think
ZK passport and some other teams and
raro whatever are working on this the
ability to selectively disclose
arbitrary characteristics about
ourselves but generalizable we're also
working on that a bit and I guess the
question we have is what are the
consequences for
ethereum right so we have again there
are two Paths of Technology as I think
Amir talking is head looking at Lewis
Mumford and one path we have this
centralization of Mega machinic
technology which sucks power away from
the individual and two centralized power
structures making us all slaves to the
machine and I think in the worst
possible World blockchain technology
would make this worse that we would be
completely enslaved in some sort of
libertarian nightmare where every our
movements and every we do and our
transactions are transparent to everyone
and recorded but the cyppher punk saying
is transparency for the powerful privacy
for the weak so we should have not
identities not soulbound tokens not
complete nonsense like dids or various
authoritarian technology claiming to be
self- Sovereign like The self- Sovereign
identity nonsense but we should instead
support zero knowledge proofs Anonymous
credentials that enable selective
disclosure okay
yeah I really wish people just not put
the words self- Sovereign in front of
fascist technology and be like oh it
makes it all better it's so stupid uh
privacy on chain is not s synness
Everyone in ethereum is obsessed with
gas fees and making things extinct but
reality is we need private smart
contracts which darkfy and Alo and other
folks are working on private
transactions Aztec and tornado cash and
again remember we have to support our
political prisoners Roman storm smof and
Alex so do support them
and I'll just try to I'm ending right
now but we also there's now discussion
of adding someone in the last session
said what when should we add privacy to
the network in ethereum I would say what
better time than now and what better
people than you all out there we have
mix Nets and MPC Solutions which can
help with network privacy and help with
inclusion list to make you know ethereum
not a censorship chain but a real chain
open to the whole world and we need to
defend validators from each other to
prevent DDS attacks and clients from
malicious RPC nodes and again let's not
forget another political prisoner who
was the only person to support mix Nets
when we started but now is in jail or
almost out Virgil Griffith so that's it
yeah that's it
who all
right you know if everyone had that
level of passion I think we could change
the world tomorrow uh but nevertheless
uh thank you thank you for that very
passionate speech and I believe you know
privacy is an important thing freedom is
an important thing but let's go over to
the Q&amp;A section and we've got some
interesting questions the top voted
question quite fun why does cipher Punk
sound so religious would a religious
fervor lead to Cipher Punk being not
that different from the future it
replaces very philosophical question
some deep ideas there how would you like
to address this well I would say
religions generally start as movements
against corruption and centralization
wow I mean they do and then what happens
is that they're then incorporated into
the nation state so for example I
Buddhism I I apologize I don't know too
much about but like with Christianity
you have you know Jesus throwing the
people out the temple and then all of
sudden BEC merging with the Roman Empire
right people do cyer Punk sounds
religious because it's fundamentally an
ethical and moral movement and on that
level is similar to religion but rather
than promising a pie in the sky a happy
afterlife we want to create a better
Society now and that will lead to
Passion I would rather have people be
passionate about building a better
Society now right now with the tools we
have than believe in something else well
said you want to add on yeah if I could
just add something as well I mean we've
also been talking about like Anarchy and
a lot of anarchist political philosophy
as well which truly I mean all of that
not solely relies on but is fully
undergirded by The Passion of believing
in each other as human beings as well so
there's a crossover there with let's say
like religious fervor as you said in the
question but I think you can still
distinguish those two things in a
meaningful enough way and it's still
positive so very much very much so thank
you for answering that now uh funny
question at the top Trump pumping our
bags is good for funding Cipher Punk's
Tech research Cipher Punk Cipher Punk
I'm just kidding um no I mean I would
argue look more Capital has been wasted
in the uh pumping of bags and I've seen
before and there's a double side to the
blockchain technology all the
interesting cretive Concepts come at
least from my perspective from the
cipher Punk movements blockchain smart
contracts digital cash Anonymous cash
and then you have all this kind of you
know other stuff coming from more
traditional financial institutions
taking Financial techniques and you know
I'm not against it letting them be more
widely accessible and I would argue that
what you're seeing now as you're seeing
the movement you know with particularly
with ETF is being slowly more and more
moving away from Cipher Punk ideals and
more towards just traditional Financial
pump and dump scams like whatever the
Trump is doing with defi World Liberty
blah blah and so it's true that some
percentage of that money is being spent
for Cipher Punk tooling but very little
almost none to project which has been
providing anomy for decades their
founder is here Roger dingledine but
they don't have enough money very few
people have donated ethereum so we have
some good uses like Assange but most
Cipher Punk Tech is incredibly
underfunded and now because of privacy
blah blah blah on turn no cash people
are afraid of touching it and funding it
I know I raised money from a16 and
whatnot some people throw down but it's
increasingly hard yeah also just be
realistic with what amount of uh
bandwidth you actually have when you're
building if you're optimizing for
something to pump a bag then you will
build something that pumps a bag that is
it so you also need to think about the
amount of uh you know Innovation tokens
you have to spend on any of these
projects even though in theory yeah you
could
uh have your bags pumped by a bad thing
happening and just quickly centralized
power in general does not Empower people
and cypherpunk is about empowering
people so that's why we push for
decentralization
voluntary associations do not
necessarily evolve into nation states
historically they actually destroy
Nation States from barbarians sacking
Rome onwards and I think that's not
necessary and I do recommend that people
just basically throw down as much as
they can on this Tech yeah this is
decentralization stage ladies and
gentlemen fight against the MC and the
MC State ladies and Gentlemen let's give
our two speakers a big big round of
applause for inspiring all of us to
fight for freedom
Freedom through decentralization Freedom
through privacy the first speaker to uh
go ahead and answer the Q&amp;A without my
queue so that was wonderful and very
funny to watch as well but nevertheless
that's the kind of passion that we need
right that's the kind of passion and
fervor that we need not just in one area
but in all areas of our life you can
really transform an entire room Inspire
an entire movement built on passion and
Charisma alone so that was wonderful to
witness really I think one of the most
energetic sessions that I I got the
honor to witness live on stage Now
ladies and gentlemen um some of you are
making your way out that's fine some of
you are staying here that's even better
now those of you who are staying there's
lots of places in the front here on the
left and the right hey come forward come
forward and make sure you get up close
and personal with our next session for
those of you the cipher Punk session
please remember to collect your card
what is a card when you go to your app
your Devcon passport app click on the
session click on the Q&amp;A button right at
the bottom when you scroll down and then
you'll see join Q&amp;A collect card please
collect the card yeah it's like a a
momento of of attending the event right
kind of like an nft so please collect it
and make sure you collect all the
sessions that you attend I'll just wait
another 30 seconds for people to come in
and sit down and settle down those of
you just making your way in there's lots
of places here in the front on the right
on the left we love to to see more
people coming and enjoying our sessions
and those of you exiting the hall thank
you very much please feel free to exit
quickly and quietly now the next topic
the title is called the shape of
protocols to come very nice title this
is going to be the final topic and the
final session for the main stage okay so
thank you for those of you who stayed
all the way till the end we really
appreciate it now ethereum ethereum
defies easy categorization
it Blends aspects of money Nations and
yet more and more and more but it
doesn't fit neatly into a single
category if you want to know how
confusing ethereum is just ask the SEC
they have no idea what it is till today
Now ladies and gentlemen our next
speaker he's going to be sharing a
little bit about this and explaining to
us how the shape of the protocol is to
come there's a lot of cutting ede
technology not just in this room but all
the stages all the classroom we are
discussing lots of things on the fringes
on the edge of Technology a lot of
things I don't fully understand some of
you might some of you might not but
that's why we're gathered here at Devcon
the biggest Devcon ever so that you guys
can get to enjoy and listen to these
speakers now I want to remind you that
you can already start submitting your
questions for this topic yeah you can
already start submitting your questions
hi thank you for coming please I'm so
happy to see people sitting in the front
make space for each other that's
wonderful please submit your questions
in advance and also vote for the
questions that you see so that our
speakers can choose from the list all
right let me just check with the team to
make sure our speaker is ready our
speaker is our speaker ready oh
fantastic she's giv me the okay sign
ladies and Gentlemen please put your
next speaker Tim
B let's give him a warm Round of
Applause
okay oh nice um thank you for making it
the real ethereum 3.0 talk um hi I'm Tim
makeo I work at the ethereum foundation
on core protocol coordination and as
part of this um I spent a lot of time
thinking about how we should Steward
ethereum like what are the things we
need to do or understand to make sure
that the protocol evolves in the right
direction and a few years ago I was
quite frustrated because I felt like we
didn't even have the right mental models
or the right Frameworks to think about
ethereum and the reason for this is like
ethereum is quite hard to describe right
like uh it's this complex thing and so
it leads us to use analogies to describe
it so to use one myself um oh nice I
have sweet to use an analogy myself um I
really like the parable blind man of the
elephant to think about this so when
different people look at ethereum
they'll see something different right
some people will look at it they'll see
that there's this asset in the middle
ether and think of it as money um other
people will see that oh there's like
this evm it runs computations it's like
this world computer and you can think of
it as a settlement layer for everything
to use as sort of This Global Ledger um
and even extending that something like
ethereum is a digital nation
state and all of these things are
partially true but there's there's ways
in which they sort of fall apart if you
look at them a bit more closely um
obviously ether is valuable it's like an
asset you can buy and sell it but it
functions very different than say Fiat
currencies similarly computation runs on
ethereum it's distributed but the
intuitions we have about scaling
ethereum are very different than how
you'd approach scaling like a normal
computer computer system um and then
when people start talking about ethereum
being a country or anything like that
you know ethereum doesn't have a border
doesn't have citizens doesn't have like
natural resources to
protect and so if we don't have actually
good mental models to think about
ethereum we risk sort of
misunderstanding what the thing is and
sort of doing a poor job of shaping it
in the future so a couple years ago I
set out to find better ways to go about
describing this ethereum
elephant and one intuition we had around
this is that maybe we should zoom out a
little bit and instead of looking into
like every part of ethereum and trying
to understand how it works could we find
something a bit broader and effectively
find like a higher level class which in
theorum would be just a single
instance one inspiration we had for this
was the idea of like chaos theory if you
look at Chaos Theory you have these
abstract formulas that allow you to
describe systems ranging from like
biological organisms to financial
markets or another example could be
something like economics people
obviously bought and sold things before
we had a formal field of Economics but
once we had the concepts like say Supply
and Dem demand and how markets work it
allowed us to reason about what was
happening in a much Clear
way and so in this case the framework we
landed on was
protocols after some initial discussions
a few of us within the EF and outside
had confidence that like protocols might
be a rich enough topic that if we
studied it as like a first class thing
we could derive some general insights
that we could then apply back to
ethereum helping us to guide its
stewardship
and so over the past two years we
effectively were inspired by this idea
of uh the blind man and the elephant and
decided to fund over 50 researchers to
study protocols from many different
angles and try to give us reports around
what they were seeing so that we could
see is there actually a common thing
there we funded people from with
backgrounds in architecture law
engineering uh Environmental Management
arts and way more and they each ort to
spend time collecting these findings and
you can think of this as like field
notes from touching the elephant in
different places and now I'd like to
share some of their findings you can
think of this as like a sketch of the
shape of
protocols so first off let's look at how
protocols get adopted protocols tend to
have like a pretty slow adoption curve
especially early on and the reason for
this is that they tend to require
consensus across many different people
in different institutions so this means
that at first you can feel like it's
it's it's almost like stagnant like
there's not a lot of energy there's not
a lot of process but then if the
conditions are right you can have very
rapid adoptions of protocols everyone
has like this common knowledge about
things and so it can involve very much
like a phase shift and because you have
this common knowledge once you've
actually adopted the protocols it feels
like it can get very entrenched actually
so it's like a new status quo in a way
so one way to sort of visualize this is
think of it as like a reverse Z curve
where early on you have like this
initial Wiggles of adoptions and then um
this sort of pH shift happens where the
protocol gets adopted and then it's a
new
equilibrium and the reason for this is
just again because there's like all this
common knowledge that's built up across
people around why uh you know this
protocol should be adopted and they've
coordinated on it so one concrete
example here is um how time zones got
adopted for decades there were
conversations around time zones as uh as
uh there were more and more trains and
rail worlds across at the US
specifically in Europe but it didn't
really go anywhere until one year there
was actually a conference which was sort
of the Tipping Point where at that point
in time people decided okay we're going
to do time zones within a year after
that 85% of the US had time zones
adopted so it sort of went through this
phases shift within the span of a year
and now if you think of time zones it's
effectively this protocol we take for
granted and even doing major changes
like trying to change daylight savings
time is this very complicated thing it's
super hard to move from the
equilibrium and one implication of this
is that once these protocols get adopted
they'll tend to fade into the background
as researchers were studying protocols
there was this one quote that came up
over and over uh different domains um
that everyone would sort of use as like
an anchor for how to think about
protocols it's a quote by a an Whitehead
that reads that Civilization advances by
extending the number of important
operation they can perform without
thinking of them and so we started
thinking of protocols as effectively
these tools to generate these Whitehead
advances to allow civilization to
perform more complex operations by
abstracting them in the background
one example of this is like GPS is this
very complex technological protocol um
that we've deployed across the world and
now we sort of take for granted that you
can just you know position yourself
between two points in space and not
really have to think about
it and to use an example a bit closer to
us you can think of Unis swap as another
uh as another one where prior to Unis
swap you know deploying markets between
assets was this long complicated process
whereas now we have like a simple
formula that we' protocolized and you
sort of take it for granted that when a
new coin appears there's like a
liquidity pool that's Pro that's powered
by the Unis
protocol um and one implication of this
is that almost like the better a
protocol is the less visible it becomes
over time think of something like HTTP
you can argue HTTP is like the greatest
digital protocol that's ever been
invented it Powers effectively the
entire internet but when I talk about it
I don't get like a strong emotional
reaction similar to how like when you
use a great product you know you notice
it or if you see like a beautiful work
of art or you walk into like a nice
space like the conference venue um HTTP
sort of false flat and you're like yeah
it's a good protocol but on the other
hand think of bad protocols uh one
obvious example is like air travel
protocols if you're traveling you know
internationally and I put these pictures
here you immediately have like a gut
reaction of what it feels like right to
take off your shoes you're scared to be
pulled aside um and maybe you know this
goes well you fly but then you're trying
to get a taxi to go back to your Airport
after you're jet lag and if the protocol
there is bad you know you immediately
feel it right you're studing there
outside uh it's warm and there's 100
people waiting for their grabs um and so
this was a really valuable Insight
because um it allows us to to sort of or
it sort of Illustrated the different
lens through which we could start
viewing
protocols one of the researchers
formalized this and called this the
Kafka index the idea being that it's
much easier to reason about a protocol
by imagining its worst version across
many different dimensions than to try
imagine the best possible version and
again this is very different than your
intuition when say Building Products if
you're building your product you're
trying to think like okay how do I build
the best version on across all these
Dimensions you know I go from like zero
to 10 Protocols are a bit like the
opposite it's more like you have all
these dimensions and you're trying to
get from minus 10 to
zero and when I was thinking about this
this week um it hit me that this is kind
of why the Bitcoin protocol I think is
is so elegant if you look at the Bitcoin
white paper um the second line or so uh
focuses on what is like the core thing
it's trying to address um so stosh's
claim is you know trusted third party
are like the worst things about online
payment system and the entire protocol
is focused on just trying to get around
that one thing if you look at the bottom
of the abstracts it sort of says look
there's all these other parts of the
protocol and they sort of kind of work
um but it's sort of less important than
the idea that on this one bad Dimension
we're trying to optimize to uh go from
minus 10 to
zero and flowing from this like if we're
trying to like protect these protocols
or get them to avoid these bad States
another way that's useful to think about
them is to to treat them as Commons in a
way Commons are these shared resources
that have a risk of like being captured
or overused um in in sort of outside of
crypto people will use this when talking
about things like Fisheries or P or
pastures basically natural resources um
and obviously in our context uh these
protocols tend to not have these like
physical boundaries um there's things
that have clear digital boundaries you
can think of ethereum itself as having
like clear digital artifacts or even if
you consider Linux to be a protocol you
know it's like a clear thing to point to
but there's also some more diffused
things for example think about like the
evolution of workplace safety protocols
it's clear that there's like a common
good here you know there's like this
sense of safety and injury and whatnot
but it's distributed across a whole
range of Institutions um without
necessarily having like a single
artifact but still I think it it points
at an important intuition that like if
you want to avoid the bad cases just
like for physical Commons we need to
have strong stewardship because we want
them you know we want to protect against
capture overuse and other
risks and the sort of risky capture led
us to one of the sort of final insights
around what's unique about
protocols at the very start of this we
spent a lot of time trying to Define
what even was a protocol and especially
how it was different than other things
you know like what's the difference
between a protocol and an API or a
standard or a
grammar and one thing that became clear
through this work is that protocols have
a notion of conflict embedded sort of
their core um and you know you can see
this very quickly in something like
ethereum right ethereum is effectively
this digital protocol we have nodes on
the network which have to come to
consensus about the state of things so
they have all these ways to resolve
conflict you know by peering or or un
peering from each other there's some
more um explicit parameters they get to
negotiate over like the block gas limit
um but beyond that we also have these
like Mela protocols around ethereum that
exist IM mediate conflict like how we
plan
upgrades and again outside of crypto you
could think of something like traffic
rules right the way that traffic is
organized and we're trying to mediate
different people going to different
places but going through the same roads
um is another way that like we have
these protocols that manage
conflict and this was like such a
central point that it allowed us to sort
of simplify our working definition of
protocols by about an order of
magnitude so in 2022 when we started
this Danny Ryan had the following
definition for a protocol which I'll
have to read um which is astrum of
qualified behavior that allows for the
construction of emergent or emergence of
complex coordinated behaviors at
adjacent loide and so this was broadly
right but it was quite verbose and then
through all of this work uh at the end
of this summer venat who runs the summer
protocols program was able to summarize
it in two words which is protocols or
engineered arguments and this is like a
really helpful working definition of a
protocol especially when contrasted yet
with things like standards apis and so
on and so to cap what we had so far you
effectively have like these five initial
properties of what the shape of
protocols starts to look like we have
this slow adoption and entrenched
persistence that we first covered sort
of reverse Zed curve then the idea that
protocols create these Whitehead
advances that they provide sort of this
invisible infrastructure that
Civilization can then build on top of um
we have this idea of a CFA index where
you can analyze a protocol by looking
through all of the worst versions of it
across different dimensions then
thinking of protocols as Commons which
have uh risk of being captured and
therefore require strong stewardship and
lastly treating protocols as engineered
arguments so realizing that they embed
conflict in many different
ways and this sort of validated the
initial thesis that there was a common
thing around protocol that applied
across different domains that we could
use to discuss um to discuss our
problems within ethereum and hopefully
learn from others as well and so now I'd
like to talk a bit about how protocols
May evolve in the future and
specifically how ethereum may help shape
and to do this it's useful to like zoom
into ethereum's distinguishing property
as a protocol uh which which I think is
hardness this is a term that Josh dark
coined a couple years ago um and defined
it as the capability to make the future
certain ethereum isn't the only source
of hardness in the world and in this
piece uh Josh puts out three categories
so atoms institutions and blockchains
and but ethereum's hardness is special
in three different ways first is that
it's globally homogeneous meaning that
no matter where you are in the world you
have the same degree of hardness when
you use ethereum and this is very much
not true of atoms and
institutions the second is that it's
independently auditable so anyone that
uses ethereum for hardness is able to
verify whether or not a certain thing
happened and then lastly it's
permissionless accessible so you don't
need sort of a high barrier to entry to
use
ethereum and so if we use this and
understand like ethereum has hardness as
its core um we we can start of see how
it can shape the future of protocols
the first is as an hardened foundation
for other things um this is kind of
obvious for anyone who's at Devcon here
but it's striking how special and unique
this is there's not many other things in
the world that exist to provide sort of
this strong source of persistence and
reliability to financial assets cultural
artifacts or even a whole set of
protocols built on top of it so um again
this it's it's kind of hard to overstate
this but like looking from all these
different domains it feels like
something truly unique that we should
not take for
granted but stemming from that there's
like a more subtle way in which uh we we
we have sort of hardness at our core and
it's as a hardened culture and here you
can look at hardness both in the way I
just defined it as like a giving you
better certainty about the future but
also in its like more traditional sense
as battle test did ethereum operates in
a pretty adversarial environment and
over time we've developed like norms and
practices to mitigate and respond to
attacks said both the protocol
application and infrastructure
layer but in parallel to this we also
have a culture of looking really far
into the future of trying to like plant
seeds for the ecosystem to grow to
become resilient and not dependent on a
single uh institution or set of people
and also have a technical road map
that's sound in the long
term and so by combining both like these
hard Foundation as a protocol and this
Sofer like cultural hardness um ethereum
effectively can impact the future
protocols Beyond just
crypto and one way one way I thought
about this is like ethereum is
effectively this tool that we can use
the Harden Commons um outside of the
space as well and this is because we
have this opland platform that's very
large and and and sort of very versatile
but that's also fairly sandbox from the
rest of the world this means we can run
experiments that would be probably too
risky to happen anywhere else but it can
still happen at sufficient scale on
ethereum and provide value to the rest
of the world
two examples here on this slide are
quadratic quadratic voting and
prediction markets both of these started
off as these theoretical ideas that
didn't quite have a place to sort of be
prototyped in the world eventually
ethereum became that place we were able
to run small experiments and learn from
those improving our understanding and
then you know leading to much more
significant outcomes most notably uh you
know prediction markets playing a major
role in a recent US presidential
election um and so I think going through
all this and coming back to the original
question I feel like we have like a
start of an answer to how we can best
Steward
ethereum so by understanding
um the the notes are wrong on this slide
but we'll run with it um but okay but
understanding anyways the shape of
protocols um we can better calibrate
effectively how we approach developing
ethereum in the future um you know we
should expect that things will take time
especially early on but we shouldn't be
too surprised if things gradually happen
as a sort of pH shift all at once we
should expect conflict and capture and
engineer systems that gracefully handle
them and instead of building for
hypothetical Utopias we should be honest
about everything and try to solve for
failure modes in the
protocol and by having this shared
language this shared framework of of
protocols we're able to learn from other
communities who otherwise wouldn't be
interested in our problems and at our
best we can also export our best
practices out to them so in other words
the understanding the shape of protocols
is the way ethereum community can
leverage its impact Beyond crypto thank
you thank you very much
Tim fantastic you win the record for the
first speaker that has finished Before
Time wow every other speaker pushed me
to come on stage a bit earlier than
expected but nevertheless that gives us
a little bit more time for some great
session of Q&amp;A I was going through the
questions some questions are not EX
exactly linked to the topic so if
possible we want to keep the topic and
uh as our Focus so please ask questions
regarding what team has shared about
protocols in theum um and feel free to
upvote as well right if you see a
question that looks really good please
upvote it so that our speaker can
address it let's go with the first one
on top how do we Converge on a
conception of protocols which will be
sufficiently specific to lead to useful
actionable in oh okay second one
oh they keep okay hold on uh I can't
scroll down can I scroll down I don't
know if the team can scroll down cuz I
yeah yeah the third one okay actionable
insights while keeping it
oh while keeping it okay I think I got
the question I'm happy to answer okay
let's go to number six do you think EF
ecosystem operation is a bad protocol
because we don't see any feedback
Channel that's a good question Tim how
do you think you'd like to address it
yeah I I guess I dispute the premise I
don't think that like there's no
feedback Channel I know I work at the EF
and I read all the tweets and I listen
to everything so I think um a lot of it
is not necessarily visible you know the
EF doesn't have a suggestion box but we
get a lot of unsolicited feedback so we
don't necessarily need to um and and
then I think back to what I said earlier
like um and you know back to is talk
this morning um getting the feedback
doesn't necessarily mean you have to act
on it right like I think one thing the
EF wants to optimize for is um leaving
the space for others to grow and and
sort of take ownership about Solutions
in the space and so if we just reacted
proactively and solved every single
thing um others would sort of feel like
they don't have the space to do that um
but yeah to the extent to which we have
or or we don't have good feedback
channels then yeah that would make it a
bad protocol that's a good answer and I
want to pick up on that because our
previous session with Justin a very big
crowd came in and he was sharing that if
you want to accelerate growth come and
email us and join the team don't just
watch from the sidelines you know giving
feedback is good but partic ipating I
think even better great question great
answer let's look at the next one um
okay what are the takeaways for ethereum
here rules of thumb for healthy protocol
Evolution past mistakes we should avoid
repeating yeah um one thing that felt
good about doing this research is
honestly a lot of the in instincts of
the ethereum community are are pretty
good like so um it's it's it's it's made
me a bit less concerned about this but
um you know like probably the biggest
one is like this idea of like solving
for the negative versions and um this is
maybe not as visible to to like people
who don't work on a protocol every day
um but the main thing that we talk about
when we discuss uh protocol changes for
ethereum is security right like everyone
comes in with a new idea for a new
feature for ethereum um it's always
great it provides a ton of value to user
but there's a security issue with it and
effectively not compromising on ethereum
security is more important in the
protocol development process than trying
to deliver as much feature or as much
value as possible through features um so
that's one of the takeaways we like it's
kind of nice that we were already sort
of doing it um I do think the adoption
bit is something we should think a bit
more about where a lot of the intuitions
we have around how ethereum will get
adopted we probably borrow from like the
technology sector and product
development um and we should probably be
looking more at things like yeah how
time zones got adopted or how GPS got
adopted them uh products y excellent
answer all right number four votes on
the top how does engineered argument
differ from logic defined by Wiki as the
study of correct
reasoning um yeah I'd say it's like
correct is uh correct is subjective
right like you know uh and and one of
the big things is just this idea that
protocols exist to effectively mediate
conflict um so everyone thinks their
version of the protocol or their viewing
the protocol is correct but a good
protocol will be able to uh to deal with
cases where yeah it's incorrect
all right thank you okay we back to our
earlier question which I couldn't finish
in time hopefully now it'll stay on the
board don't vote for anything else wait
hold on how do we Converge on a
or actionable insights while keeping it
open enough to facilitate input of
offchain
perspectives
um how do we Converge on you got 30 so I
this is like a low conf answer but I
think at this point it feels less like
there's a single core formula that we
can use that will be like perfectly
actionable rather than like these many
different lenses so I think um one thing
that's been useful in this summer
protocols research is having people from
different domains to be able to validate
like is this an ethereum thing or is
this like a broader phenomena and yeah I
I think just like gut checking against
other domains and yeah and I think maybe
just one more question the second one on
the list uh in casee anyone's interested
where was the research published in one
place and where was the research
published summer protocol.com all of the
research is there um yeah if there's one
place to go that would be it fantastic
and of course if you want to speak to
him later I'm sure he'll be around for a
little bit longer if you want to discuss
research let's give our speaker Tim
another big big round of applause thank
you thank you very much Tim appreciate
it all right ladies and gentlemen uh
we've come to the end of our session for
the main stage remember to also claim
your card yeah please collect your card
for every session that you attend and
we'll be happy to see you again here
tomorrow we're going to be kicking
things off in the morning all the way
until the evening again we've got so
many talks across many stages thank you
all so much for coming it's been an
absolute pleasure and honor seeing you
guys so excited about each and every
session I really really appreciate the
questions as well you guys did a great
job for now we welcome you to exit the
hall thank you so much our team needs to
clean up and reset and we'll see you
guys again tomorrow bright and early so
make sure you don't go out partying too
hard at the side events because we got
some great content starting early
tomorrow morning be here at 9:45 all
right thank you guys so much I'll see
you guys
tomorrow awesome
a
know
oh
B
t
o
e
m oh
for o
m
is
for e
SC
