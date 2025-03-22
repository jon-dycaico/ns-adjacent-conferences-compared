[Music]
sh
for
e
where e
one one one hello hello oh
to
[Laughter]
uh hello everyone the session will
starts at 10 a.m.
so we just have 15 M
minutes time for people to come and we
start at 10: I am
I
spe
kep e
every
that
think
it's for
gu
be
sure
feel e
was
you
back
he
uh hello everyone uh welcome to Devcon
and thank you for joining us at security
track So today we're going to start our
day with the panel discussion on formal
verification in the ethereum protocol
and uh without further Ado let me uh
invite our panel so eager konov Julian
soand and zo p and the panel will be
moderated by David Pierce so please
stage is yours so a quick reminder
Devcon is using the Q&amp;A
app
okay okay just a quick reminder uh we
are using uh mcut app for Q&amp;A session so
please prepare it ahead of time and the
panel will be 45 minutes and we have a
Q&amp;A great thank you can
we awesome thanks uh everybody for being
here um so yeah we are going to be here
talking today about formal verification
which is a topic that uh I think all of
us love a lot the chat already before
has been intense so that's good um um so
yeah uh so we'll start I think just
start by introducing everybody so we'll
just go around and just everyone to give
us a bit of a a background of the you
know background and form of verification
and the kind of thing that they work on
um so yeah so maybe start with Julian
and we'll go around yeah so um my my
background is uh I actually did my
initial Focus was I did a PhD on formal
verification for concurrency I was
looking at termination so you know very
very uh different concerns from what we
mostly focus on in web 3 but uh after I
finished that I came to work at
nethermind and yeah it was sort of um
it's a it's a very interesting system
where um there is actually a lot at
stake while in some ways some parts of
the system are relatively tractable and
so can actually be verified and so I was
really excited to uh to be able to
contribute to that and in particular uh
apply trying and apply hard formal
methods to try and really get the
highest uh degree of certainty and
that's I guess what my uh what my team
focuses on and just just to clarify
the the tools that you use mostly in
your work uh yeah so we we primarily use
the uh lean proof assistant and uh and
easy Crypt so these are very should I
should I add a little bit about or we
wait till lat oh okay okay okay cool
cool cool yeah sorry go ahead um so
hello I am Zoe um I did my PD in uh
compiler
verification and for this part I mostly
used uh proof assistance in particular
cul and for the last couple of years
I've been working on building uh tools
for verifying smart contracts and for
that part um we use a combination of
proof assistant and smt solvers to um
automate verification
tasks um yeah and you're part of the
Argo Collective as well and I am part of
the Argo
Collective um the recently formed uh
Argo Collective um from former F
employees who are like building
languages and tooling for the ethereum
ecosystem and I'm also an assistant
professor at National Technical
University of Athens um where I like
specialize in programming languages and
verification
thanks hi I'm eor konov I'm an
independent researcher now previously I
worked in the cosmos echosystem for like
four years so I'm not new to blockchains
but I'm kind of new to ethereum actually
and my primary tools are model Checkers
I'm a model Checker guy using explicit
State model Checker checking symbolic
State model checking but also
simulations uh randomized stuff and and
and things like that so yeah I worked on
model checking of tenderman consensus
for instance checking some property
there uh checking agreement accountable
safety also worked on verification of
smart contracts but that's not like the
cool thing I have I guess I have done
and this year we actually had a project
with the serum foundation on checking
accountable safety of the new three slot
finality protocol yeah great thanks
Eagle Okay so we've got a few questions
that we're sort of going to go through
um and there will be a Q&amp;A session at
the end don't forget to post your
question you know if you have questions
post them to the QR code um and then
they will be read out at the end um okay
so yeah so the first question which is I
think possibly like my favorite question
um is about tooling and so I'm really
interested to know you know the tools
that you use um and in particular you
know what you think their strengths and
weaknesses are you know where are they
really do they work really well and
where what are the pain points that
you're really feeling um so I don't know
who would like to start that or we can
just go around yeah I'm happy to start
yeah so so as I mentioned we use a
combination of lean and easycrypt for
very different things easy Crypt is a
domain specific proof assistance which
we use primarily for um cryptography
verification and then lean is a general
purpose proof assistant which actually
well this is a bit debatable but I would
say that it has the largest
formalization of mathematics in in
existence Hall users will obviously be
screaming at me they're
wrong um for so the the reason that I
say that is that the hall library is not
very well organized they have a lot of
theories maybe it's the largest coherent
Library exactly the largest so Hall is
very disorganized lots of like lications
of theories with slight differences and
then proofs that say hey these theories
are equivalent so you can like cost
theorems between them and these sorts of
things but uh so so technically it has
more theorems but as you said not really
cohesive so there you go um so yeah so
so and lean so our goal with both of
these is basically to actually be able
to verify and you know I imagine egole
you'll talk about this more about
automated they improving and these sorts
of things of course but uh our goal
there is to verify I guess the really
complicated part of the ecosystem so we
look at verifying like complex safety
and liveness properties of protocols we
look at verifying cryptographic safety
safety property these sorts of things
which are things that um typically are
too complex for automated theor proving
to be EAS able to easily approach
without a significant amount of guidance
essentially so so where do you find
where are the pain points that you've
sort of hit excellent question so uh in
so easy Crypt has access to smt solvers
and these sorts of which which um
typically allow us to automate away
these sorts of like small detail things
of of like the Practical implementations
of programming languages like hey the
sum of these bit two bit vectors doesn't
overflow or something like that right
and and impr proof assistance typically
reasoning directly about these things
mostly because actually until recently
these this had formalizing these sorts
of things haven't been a big concern in
proof assistance so it it can be uh it
can be quite painful and in fact uh when
we were working with rzo we had one
engineer working for two months
continuously on formalizing a bunch of
theorems about bit vectors and most of
them were just like through Brute Force
unfolding and it was extremely painful
and a lot of these things can be done in
like minutes or hours with the right smt
solver and and then all of that broke
when lean the ma lean's math Li changed
the definition of a bit Vector so but
anyways they've since improved that
library and now we don't need to do that
anymore but that was a painful moment
yeah that sounds
that was unpleasant yes um yeah thanks
sorry um so uh I use a combination of um
proof assistant in particular Co and smt
solvers uh both are great in their own
ways uh the good with proof assistance
is that
whatever can be proved you can prove
like sky is a limit the user's ability
is a limit and smt solvers are great
because they can automate very t stats
that they would be very hard to be to
like um for the proofs to go through
otherwise and they can be used for like
symbolic execution for instance which is
very useful like to find like assertion
violations or um potential errors in the
code um this is extremely useful but
then if it doesn't
work then there is not much you can do
about it uh
so yeah so so comparing that then to the
interactive theem proof is like you know
what is the challenge that you find
there um in theorum provs or in smts no
interactive theor Prov inter the proes
are hard very hard it's the time that it
takes to actually get the proof yes it's
like it requires a lot of like expertise
to like carry out proofs and proof
assistance to encode problems to encode
specification problems in proof
assistance
so it's time consuming and yeah but it
it's also very rewarding um for a proof
to go through so yeah another
interesting difference is that um
improve assistance you build a proof the
proof is there forever you can take it
at any point smts will not in general
produce a proof that is takeable so you
need to rerun the smt every time you
want to uh prove something with can be
like uh time consuming in terms of uh
resources Computer Resources and also
like it can introduce some
non-determinism yeah I mean we've
certainly had experiences where
upgrading to the latest version of Z3
has meant now the proof doesn't go
through for examp exactly
yeah awesome thank you Eagle yeah I'm
using CH plus um as a as a specification
language that's temporal logical
factions by Les Lampert he invented it
like some decades ago and there are like
actually several tools there one is a
interactive theorem Pro called CS I
don't use it much I'm not the guy who
can write proofs for PR
basically um but there is also an
explicit State mod Checker which just
inate States and if it terminates it's
good right you have Prov the property if
it doesn't what do you do right and in
most cases if you dealing with something
like
consensus it never terminates right
because the states place is huge the
banan fults introduce a lot of new
States and everything and like there is
a third tool which I have been
developing for like since
symbolic mod Checker translates t plus
into smt but many of you guys I guess
imagine Quantified smt and everything
our translation is very stupid actually
remove Soul quantifi everything is like
ground that bounded right it it's
bounded M checken yeah there are only
constants uh and we we just analyze
executions up to like 20 steps or
something like that uh if you if you
smart you can use induction there to
reason about Unbound executions but
that's that's kind of hard because you
have to invent inductive invariance
which is as hard I guess as proven at
some point yeah and like the strengths
there that you can just run it right you
just throw out your spec you push the
button it runs the weakness that it can
run for days and you have no idea
whether it's going to terminate or
anything so basically you have to apply
a lot of tricks like introduce
additional abstractions if you see it
even doesn't work for simple things like
reaching interest in states have to
introduce abstractions make it faster uh
observe like which which of the
transitions take a lot of time in smt
and all that so so it feels like you you
do spend quite a lot of time sort of
trying to tweak those parameters to help
the proof go through yeah yeah
and I guess like the main benefit that
you're trying to like to find bugs as
fast as possible is tools so you really
start with very small input space to
like trigger you know interesting
behaviors to find problems and then when
you're convinced it kind of works you
start increasing the state space and see
what happens cool thank you okay so next
question so I think this is one uh that
you know maybe the audience might
appreciate as well um so what are the
challenges that we've you know that you
have faced and getting formal
verification to be adopted you know
within your organization I think that's
the first bit but also in a kind of
broader sense within the community you
know because I certainly feel that there
are a lot of challenges here
um yeah so I think in web 3 one of the
key issues is that uh the technology and
the space are moving so fast and
everything we do has a very high cost in
terms of tooling it takes a long time
before we can develop formalizations of
the new languages the new systems Etc so
that we can actually practically verify
things and that that's I think true
whether whether using interactive or
automated they improving to some extent
um and and so the thing is uh it
certainly feels like I'm playing a bit
of a guessing game sometimes as to what
is actually going to be useful next to
figure out where I should actually be
applying my team to actually develop new
tooling and it's happened a couple of
times uh I think I can think of two
instances where we have invested like
six months plus of work in a tool only
for it to be essentially deec the moment
it's released so I mean this happened
with a tool that we had that was called
Horus for CYO zero which was the first
darket language and literally I think a
week after it was released a stock stock
whereare announced that there was this
Kyo one language going to be released
and Kyo Z was going to be deprecated and
we spent six months developing that that
was pretty painful I can imagine that s
yeah very unfortunate yes yes so there's
that and then I think uh I mean this is
more true for the kind of techniques
that I use um where uh our techniques
are not necessarily so I mean we um we
were talking about you know the
difficulty in embedding things
interactive the improvers and there's
truth to that but also uh it's also true
that you know modern interactive theor
improvers you can embed all sorts of
automation into them and you know if you
find the right set of automation you can
make things a little bit more generic a
little bit more well much more robust in
theory um I mean there are examples of
for example uh the verification of Cairo
which is written in uh in lean actually
apparently it's I mean the details are
not all public but this has been
developed by Jeremy avad at CMU and the
proof generation is apparently almost
entirely automated uh inside the Le so
so uh so that that's uh so so there are
sort of some uh interesting things sorry
interesting things you can say that you
can do in that direction but the there
is a difficulty with robustness where
like if clients change implementation
significantly we have to redo a lot
presumably it's not just you know you
mentioned languages but presumably it's
not just languages so you know I know
that you work in the ZK quite a lot and
so it's actually new algorithms as well
that are coming along you know you got
plon you know turbo plon there's all
these different things coming out and so
it takes a lot of effort to understand
them to understand them and to
understand hey what are what are the
properties semantics they enforce Etc uh
and also because we're doing
verification on the cryptography side
like how what are the cryptographic
guarantees all of these sorts of things
so yeah I spend my life reading papers
on a variety of different things so
there you go yeah well things you could
be doing the worst jobs to have so cool
thanks Julian sorry so uh as Julian said
yeah it's very time consuming and there
is a step learning curve even within
experts to go from one tool to the other
so if there is a team working in
formally verifying something with a tool
then like abandoning the tool and going
to something else is going to take a lot
of time um so but there is also a lot of
Maintenance burden like it's hard you
build something then the code changes
then you have to adjust the
specification the verification
that can also be um very hard yeah sort
of like maintaining the proof alongside
the artifact itself exactly and uh
things change quite quickly in this
space so yeah that can be tough
um so
yeah do you feel like there are any
strategies to help kind of mitigate that
you know like to make it easier to
maintain as artifacts change
or so I think programmers should program
with verification in mind or at least
specification in mind like I think there
is a lot of value to writing
specifications even these are not going
to be formally verified they can be
tested I mean there is property based
testing we can test specifications and
that's actually quite useful and
productive in terms of code quality okay
thank you thank you uh eagle
yeah I mean when I started working at a
company like four five years ago you
know doing stuff for for Cosmos I I
talked to a lot of Engineers and
actually I expected them to complain
about performance and all these things
but it wasn't the case they complained
about usability was basic usability I
was sh them t plus and if you have seen
it it's kind of lat like Mazi syntax and
they all kind of questions like what
this thing looks like what is this
mountain doing here what this like kind
of strange questions but usability was
number one issue there you know like uh
what do I write how do I write it why do
I write it this way why don't I write a
loop you know all this stuff so I think
it's the number one issue there and at
some point we introduced a surface
Syntax for plus that looks like a
programming language and that changed a
lot people stopped complaining
immediately they were saying okay least
we understand that's fine oh that's T A
plus that's fine it's like very good so
really like focusing on usability I
think is number one thing so kind of
connecting to what people already know
makes a big difference yes exactly
exactly if people come if they have seen
like a simple functional language it's
much easier for them to connect to what
C+ is unless they have been rising
proofs in Mass you know which is very
unlikely if you're talking to Engineers
so that's one thing and another one like
what we already mentioned it's kind of
time to Value you know if you tell them
I spent like three weeks writing a
specification and then I check it they
will be super disappointed because at
some point maybe it doesn't check you
know nothing happens and it's very
important to give them results like on
day one basically you start writing the
spec you tell them look I can generate
an example I can show you an example
where where you know an algorithm
reaches some State and I super excited
about it because before that they were
drawing it on a whiteboard which is
super time consuming if you can generate
an example like 5 seconds and they can
read through it's amazing right know so
time to value is super important and
like randomized randomized exploration I
found it super useful before you try to
do any proofs just try to break to sort
of find that lwh hanging kind of FR
exactly exactly and do you like do you
feel um like you know there's a
challenge here in in getting people to
appreciate the value of formal
verification I mean I feel like that's
sort of what you're talking about there
that helping them see results quickly
will help them see the value yeah I
guess it's it's a bit more than that I
think it's kind of a problem of trust
because if you if you write a program
you kind of can run it and get your
confidence in that it does something
useful if you write a specification it's
just a piece of text and it's hard to
understand whe it makes any sense the
same for PRS I guess right unless you
prove something right and it's really
you have to give them a way to gain
trust in this artifact very quickly and
and whatever execution random simulation
helps a lot it's it's really because for
them it's kind of a detached right and
on a wall which is not running and
they're all Engineers because they're
used to running things so I think it's
it's kind of yeah okay thanks you know
um you don't mind me just interjecting
um the analogy that I've actually used
for it fairly often is that I I feel
like actually formal verification
suffers from a lot of the same problems
that vaccines do in genuinely genuinely
in the sense that as I said people don't
really understand them right and the
thing is if they if they work correctly
then nothing happens and no genuinely if
if we if we do our job right the point
is nothing bad happens and you never
feel like you needed to do it in the
first place then right yeah exactly
maybe maybe nothing bad would have
happened if I did nothing you know you
don't know
so yeah I I see where you're coming from
there
yeah okay okay um so this uh I feel like
this is yeah okay pretty similar or sort
of related question um so obviously
formal verification is often seen as
quite difficult and costly to apply I
think we've already kind of covered that
some of that but I guess the question
here really is you know as a community
what can we do about that going forward
how can we try to lower those costs you
know what are the things that we can do
um and I think Eagle already did touch a
little bit on that but but interested in
in more thoughts that you have um I
don't know who would like to go yeah so
we go yeah I can go so um as language
designers and implementers I think we
should build languages and tools with
verification in mind so once you have a
language that has like integrated
support with verification then things
will become much easier for programmers
to like get used to adopt trust even
like languages for instance with support
for but real world languages not just
like um very Niche languages that are
used in academic environments but like
real world languages with support for
writing preconditions post conditions
having Rich type systems like being able
to write in variants even if they are
not proved uh like automatically or
directly even if they are tested there
is a lot of value to it to like for
people to learn the discipline yeah so
so we were talking about this actually
yesterday in the formal ification
hangout um and in particular talking
about solidity and solidity has this
kind of extension called scribble where
you can write pre and post conditions as
comments so you know it seems to me you
know what you're suggesting there it
would be really nice to see that kind of
solidified and turned into part of the
language itself yes exactly and then and
then it will be easier to reach more
people it will be easier like for people
to think about it when they write code
which is extremely important to make
formal verification like viable
great yeah I actually completely agreee
with that I think you
know using some lightweight methods just
to help people get into it and to see
the value and to catch that low hanging
fruit I think that that definitely is a
win and I think um success story is R
which has like very rich types types is
verification basically and it's widely
adopted and like people love it and I
think it will be nice to have more
examples like that even for like
languages compiling to
evm cool um e yeah yeah I mean what I
wanted to say yeah I mean really
providing faster feedback loops that
what we could do you know to give value
to the to the users but also maybe maybe
the community could help us explain what
they do not understand because it's it's
also maybe people are a bit afraid of
saying it because it all looks
complicated PhD level stuff you know and
people should be just up front saying
like this I don't understand and this
doesn't work for me maybe you should
simplify it I had conversations like
that it's sometime sometimes it hurts
but it's very useful to to hear it
actually yeah I mean I definitely agree
you know academic papers in particular
can be very hard to read and understand
and even coming from me I've got that
background right you know so yeah
anything that can help bridging that Gap
but also having like open conversations
like we have now about what works and
what doesn't that's super useful
cool uh jul yeah yeah so sort of
following in the same vein I think yeah
accessibility is super important one of
the things that we've done actually is
writing um property testers that allow
us to extract well what do you call it
uh we we've written a property testing
extractor essentially from
specifications that we write in lean so
we can write specifications for a smart
contract and as long as they're
decidable we can automatically extract a
property tester from it um so like um
like input Val Val for example is that
what you mean yeah yeah so so basically
it uh gives you like a a generator for
input values and then a relationship a
decidable relationship between the input
and output States and then we just run
it on an execution client and and see
see if it's satisfied run the decide
function and and so yeah having this
sort of feedback uh being uh sort of you
know developing these specifications in
conjunction with the engineers to see
that for them to really see how you are
solidifying their intuition into
mathematics
uh and as you said Zoe may be
integrating more into the process but I
mean I I think that there well okay I
mean I maybe it's convenient for me to
put the blame on others but uh I do feel
like there's also a bit of resistance
from the developer community in a sense
on that because they feel that there's a
small cost to it and it slows down the
development and often we we've
experienced some degree of push back
sometimes so um yeah I mean I definitely
personally see the value of testing you
know straight away right and automated
testing saying you know if it's easy to
apply I think to me seems like a win
right for sure for sure and so so one
question I think of here is you know
like if I think about the developer
community and I think about lean you
know my experiences of lean lean you
know is very powerful but it is also
very challenging to use it and I'm
wondering you know how you would see
that Gap being
bridged yeah so uh I I I I don't see uh
an immediate future without so in domain
specific cases sometimes we've been able
to develop like enough uh automation
that plausibly with enough training
someone who isn't an expert in
interactive the improving could actually
prove some basic things so but but for
sort of general purpose tasks that's
probably not happening tomorrow
certainly but what I do think uh is nice
about lean and that makes it more
accessible than many other interactive
the improvers is that it has this uh
elaboration step where essentially so so
lean has lean compilation has multiple
steps and the first one is called the
elaboration where basically the
vernacular the high level language is
compiled down into a core syntax and the
thing is this elaborator is itself
arbitrarily meta programmable inside of
the language and so basically I can give
arbitrary strings of Unicode uh meaning
right and that means that uh mean you
can embed domain specific languages for
example yes yeah yeah and with with
arbitr Unicode and and so in particular
with like maths we can get uh you know
you can have a sum over a set and uh
with with some function and these sorts
of things and we can write it in a
notation where I can show my friends who
are you know mathematicians have never
touched a programming language in their
life the statement of a proposition and
they'll understand what it means they
won't understand word of the proof but
they will understand the statement
itself and I I think that in itself is
is a very is a good is a step in the
right direction okay um the other side
of it is that if you have genz
developers some of them will use emojis
as variable names and you know there's
nothing wrong with that uh hard
disagree cool I don't know if any if any
of you guys want to add anything more to
that about bridging that Gap um
like one can like build automation
inside theor improvers they someone
could like offload things from the theor
improver to an SMD solver things have
been done in this direction not very
like it's not very widely adopted but
there is stuff to do there another thing
that I've been thinking like for some
time now is like um like integrating AI
into the proof process because AI can
write pretty good damn code and there is
a very writing proofs so if AI can write
pretty good code they can write pretty
good proofs and you got the advantage of
course that that if it writes it you can
check it right yes exactly exactly you
don't have to trust it and you can you
don't even have to trust the code that
it writes if it writes a code it writes
a proof you check the proof if it works
happy times so I think there is stuff to
explore there but not not only in the
ethereum ecosystem or blockchains but in
general I think that's a very promising
direction for formal verification okay
thanks okay uh we'll get back onto the
script um so so yeah okay so focusing
now on the ethereum ecosystem itself and
you know so you've all applied formal
verification at different levels of the
stack in different areas ZK smart
contracts
consensus so I'm wondering you know
where do we feel like where can formal
verification have the most benefit in
the ethereum ecosystem how do we feel
like it where where is the where is that
kind of sweet spot where the cost value
benefit is best
thoughts for for me the answer is
obvious it's infrastructure level stuff
right so like ZK verifiers Checkers
these sorts things where there's going
to be a huge amount of uh the ecosystem
whose value will throw flow through that
and uh you know if that is exploitable
it's a sort of a um a single point of
failure where just everything will break
right and so cryptography uh obviously
Consensus These sorts of things right um
like uh like uh contracts that things
like wallets and these sorts of things
that mediate a lot of value flow I I
think that's really the place to focus
yeah um and of course these pieces of
infrastructure tend to uh change less
over time than say you know like some
defi smart contract or something that is
sort of in active development shall we
say yeah and I guess you would say that
that you know for example you know think
about ZK EVMS is just a good example in
this case um that it is possible to
verify at that level like it you know
some people may see it as as actually
something that couldn't be done yet but
actually it is possible to have success
there yeah yeah absolutely I mean um we
we haven't worked on zkm specifically
we've worked actually mostly on risk 5
uh uh ZK VMS but uh but yeah I mean we
we have actually I I would say pulled
off some fairly significant uh results
so as of yet because in lean there isn't
a full risk 5 spec yet so we haven't
done like a full stack verification yet
but like for risk zero we verified some
very important parts of the instruction
decoder making sure that that it matches
the formal spec we've uh verified some
important parts of the ALU these sorts
things and yeah it it can be done and I
think though are where I mean EF is
currently as everyone in this panel is
probably aware uh funding a fairly big
grant program to enable just this and I
think we're probably like at most a year
away from having fully fully verified R
infrastructure is a huge thing like to
have formal verified code because it's
easier like to have experts doing that
and it's very very important and it can
like Inspire others to do the same thing
for like user codes smart contracts then
it's like it's building some um
discipline that others can follow um for
me it's also verified compilers and
languages with well defined semantics
that can people like use to write code
that they understand well that's the
first step and then they can verify yeah
so for example the solidity would be an
example you know there certainly have
been a number of of you know significant
bugs in the compiler and trying to
eliminate that would be super helpful
yes yeah and also I guess um you know in
terms of smart contracts themselves um
there are a number of kind of
fundamental contracts like the deposit
contract and I know that there are a
number of contracts coming out for the
Petra upgrade for EIP 72 for example um
you know those kinds of things are high
value targets I guess yes and it would
be extremely good good to
have reference implementations at least
that are verified if not the actual
implementations that would be even and
it would be nice to to see you know like
in the EIP document itself for example
to see some reference to that to say yes
you know we have invested in formal
verification maybe maybe I don't know
some of the artifacts maybe some proofs
or I'm not sure but something to so it
was more visible yeah yeah yeah yeah
totally cool thank you
yeah I mean we have seen quite a bit of
success in smart contracts already I
guess so maybe we shouldn't invest that
much into them I don't know but the
smart contract people disagree I guess
right uh obviously consensus yes but
also I would say it's kind of whatever
you cannot write in code this should be
verified because there are a lot of
hidden assumptions usually about timing
about interaction of different
components and this is usually written
in English right you can write it in
code but it becomes tricky because there
is nondeterminism there are some kind of
external inputs which you cannot control
so this kind of stuff that is usually
written in English I think it really
requires some kind of if not complete
verification but at least specification
and an attempt to to understand whether
all these constraints that we have in
mind whe they make sense maybe they even
contradictory so so you're almost
describing a sort of a a mind shift away
from writing our specifications in
English sort of predominantly in English
towards you know making something that
can be mechanized even if you know the
individual doesn't do the mechanization
at least other people can then do it
right exactly exactly I mean there are a
lot of hidden assumptions in in many of
these protocols because we try to to
like go from English to to CL and you
uncover a lot of
things so in terms of consensus layer
Protocols are there any sort of
mechanized protocols for example
um I mean there was some proofs in in C
I guess uh raft was proven to be correct
in Coke as far as I know um pxo in proof
system it was proven correct and for the
rest I guess m checking you know what we
did at least showed some results for for
small parameters which is also an
achievement because it's hard to do it
for for the general case yeah okay cool
thank you okay so just now moving into
the sort of final part which is uh I
guess looking a bit more into the future
um see I guess how do we imagine the you
know the role of formal verification
evolving within the ethereum ecosystem
like where where are we going from here
you know what do you think how do you
how do you see it
going I guess it's me look like it yeah
I'm not going to lie I don't have well I
I as as I said in my previous answer
right I think it is absolutely because
like it seems that the ethereum
community their goal overall is to I
think at some point in the future be a
significant important part of mediating
the transfer value of our society as a
whole right uh and so if that is the
case and we have you know uh so many of
our interactions mediated through this
system um it can't go wrong like there
would be very serious societal
consequences if we got to that point and
things go wrong and so yeah I I uh I do
think that if that is really a goal for
the ethereum community that they should
continue pushing this and particularly
in the infrastructure I mean okay I'm
going to push back a little here
actually because I feel like you know
your answer is sort of idealistic in a
sense right completely I'm
interested I'm interested in like but
where do we you know are we actually on
that trajectory like is that the
direction that we're going in at the
moment do what do you think I I think
there a question more for the ethereum
community and less for me you know you
are part of the community I I am I am of
course but uh I work on something pretty
Niche and uh you know in terms of uh you
know there are people out there who are
looking at all sorts of governance
problems how these can these can
actually be used to in a decentralized
way actually manage real resources in
the real world and I'm I I'm not this
isn't a focus of mine to understand
these sorts of things right so so I I
wouldn't consider myself an expert but
as I said I do think that certainly if
uh I so I I do feel that this is from
things I've heard from people in the
community this is a significant goal of
the community and if that is to be the
case well we should really make sure
that it's actually correct and safe and
we're not going to suddenly wake up and
you know all of our what do you call it
accounting of value is completely lost
as a society right okay um I think
within the ethereum ecosystem um the
adoption of formal verification is quite
impressive compared to other like to the
industry in general so that's great
great um so that that's the thing that
attracted me to the um space at the
first place and I think going forward so
I mentioned this before but I think it
will be quite important to build
languages with verification in mind like
clean semantics like welldefined
semantics uh Rich type
systems uh support for verification for
writing specifications I think this will
be quite important going forward to like
people who have haven't heard about
formal verification before to start
adopting and like building a me a mental
model for it and being convinced that
it's something useful so so really you
know ethereum has actually made a really
good start so far that's what I'm
hearing totally and it's really about
you know as we move to that next level
you know really trying to push it
further into all of the languages and
systems that we're using yes yeah and I
know that they are for example
interested in in in looking at solidity
and and trying to think about what they
can do there so that seems like a really
good opportunity for yeah exactly that's
an amazing opportunity that we have in
front of us to like um make the adoption
even wider and it will be very important
for people who are not experts in the
field to start learning it so um
building the right tools the right
languages and also training people to
use
them cool thank you yeah I also have an
impression that ethereum is
probably the blockchain ecosystem that
has the most adoption of formal methods
that's like my impression and that's
really cool um yeah I think I would say
yes we should apply formal verification
everywhere but it's impossible right
it's just too much uh we should focus on
on the most critical things first right
that's obvious uh but maybe what is less
obvious we should also give small
examples of what works because what I
have seen in CLA plus people complained
that okay you have this huge
specifications of consensus it's so hard
to understand we don't understand what
consensus is can you give us a simple
example like a ding philosophers or like
this River Crossing puzzle you know and
show how to step by step so I think it's
also important you know to build this
bridge between the developers and users
and formal verification people to show
small examples yeah so that's about sort
of spreading the word about formal
verification and and kind of easily
understandable chunks rather than only
having these big examples that that are
very difficult to to get into exactly I
mean if you look at at Pro written in
all the serum progs you don't know where
to start right yeah yeah
yeah cool okay we've got a few minutes
before we go into the Q&amp;A um so I will
just dig into one more thing that
something that I've kind of heard on the
grap vine when I've been here in Devcon
so you know it seems at the moment uh
you know many people doing formal
verification related work are working uh
you know doing sort of auditing of um
you know system but contracts ZK systems
and so on um but it does seem like in
many cases uh you know people coming to
audits you know they they don't have
specifications for sure but they also
don't even for example have test cases
sometimes because you know they're
they're pushing it to the wire so much
and so it does feel to me like you know
if we're struggling to get people to
write like tests then we're going to be
struggling to get them to do formal
verification and what what can we do
about this how do we how do we address
this thoughts it's a difficult
question uh who wants to go first yeah
go on go they should absolutely write
specifications and test them it should
mandatory um yeah so building nice I
mean fuzzing property based testing like
this will be quite important and like
it's the first step towards like
formally verifying like formally
specifying testing the formal
specifications and then moving to formal
verification of the
specifications
is
a it's the right way to go I mean you
cannot start by formal verifying as spec
you have to convince yourself that it's
true and testing is a very good way to
do it's a key stepping stone really yeah
yeah yeah okay yeah I mean mybe can we
were also doing audits when I work to
the company now even right um and at
some point I was thinking like maybe we
should even require that if you don't
have an English document describing what
you're doing we don't do an AIT for you
if you don't have tests we don't we
don't do an AIT for you because it's an
absolute requirement if you don't have
tests it's just you cannot do anything
right it's most likely broken if you
don't have
tests very likely right I mean it's
obviously hard for companies in a
position where you know they want to
take on clients and so on like they are
I think at the moment sort of managing
that by adding test themselves or you
know reverse engineering the
specification in some cases um I mean in
some sense it raises the costs of the
audits as well you know like if that's
part of what you have to do before you
can even do any formal
verification um yeah okay thank you uh
Julian so yeah I mean I I'd like to Echo
what Zoe said if uh anyone in the
audience we were talking about you stop
it um um but yeah and and also as you
said yeah I mean we we have faced some
interesting situations with clients who
obviously in this situation will remain
less where they've told us hey here's
something we want you to verify and then
when we've asked them about it they've
said well we actually don't know how
this works anymore the people who wrote
this left and it's literally we've had
to reverse engineer fairly piece like
complex pieces of well I'm not going to
give too many details once again but we
we've had to reverse some fairly complex
pieces of software because just the
client themselves didn't know how this
thing worked anymore and uh yeah it's a
problem um but yeah the other thing that
I kind of wanted to to float with the
other panel members was one thing that
I've been thinking about recently is
that like modern proof assistants now
offer the ability to embed like very
fully feature dsls into them and one
thing I have really been thinking about
so particularly in the context of
consensus right is that um I it feels
like the lingua franer for a lot of like
consensus research and specification is
like a simple subset of python and i'
we've been thinking of like embedding
this into lean so as to be able to then
reason about safety and liveness
properties and that is a way that maybe
that we can we can create you know a
tighter feedback loop and a a closer
relationship with the developers through
the sort of things so just an idea I've
had don't know that resonate to you guys
at all yeah yeah totally okay so I think
that probably ends the formal part of
the panel and we'll now move to the Q&amp;A
part and um I guess with questions from
the floor cool um
thank you and please give a big round of
applause to our
panelists um as a PhD researcher myself
I also um kind of uh value when people
like uh make time in their schedule to
come out and talk with the community
about you know their experience and
expertise so we have quite a few
questions and I think the panelist
covered most of it but still you know
people in the audience are not convinced
like why should we go this and do this
extra step to implement formal
verification so the first question would
be please share the elevator pitch to
engineering teams to implement formal
verification as a hard gate that care
about velocity of shipping code and how
can we make this easy for engineering
teams to lean in and you know uh do this
method so if
anyone um so so writing code that is
correct and does not introduce
unexpected failures is like the elevator
Pizza I would say it's something very
valuable on its own
end
um and then again like I really believe
in writing spec and testing it before
anything else so if anything that that
we can do to convince engineering to
write better code is like specifying it
formally specifying it with like some
specification language and then testing
the specification and then that would be
a great step already towards having
better code in like a viable time frame
not like spending three years to verify
a piece of code uh well this happens a
lot um I think to all three of us at
least this this has happened or four of
us um yeah so I really believe in the
value of specification
um solidity
yes yes yes that would help immensely to
have native support from the language
that it's a language that people use and
like it's like um a common ground for
everyone to like yes it's not something
n it's not a weird tool that very few
people know and understand it should be
something that is widely adopted and has
support for writing specs and clear
formal
semantics okay uh next question is kind
of similar uh what metrics are used to
measure impact of formal verification on
the on the security and reliability of
ethereum if you can maybe give us more
information how can we measure the
impact of formal verification I think it
is what Julian said before like if it
works nothing good nothing happens right
so I mean you you can also uh so
certainly you know when we formly
verified things we have at times found
some fairly serious bugs uh and so
certainly you can want when you do find
these bugs you can uh sort of evaluate
the uh the impact in terms of hey what
would be the worst case scenario here
right and certainly uh you know uh we we
found uh bugs in CK proof systems we
found bugs in defi smart contracts which
would have potentially allowed them to
be completely drained or Frozen and
these sorts of things so there there
there's perhaps an economic value that
you can put to it but as you said once
again what we do is making sure that
things don't go wrong and so it's
difficult to quantify hypothetical
futures or hypothetical you know
parallel presence in which things went
very wrong yeah I mean one thing I have
seen in consensus which is very cute you
can actually just add a bit more folds
and in this case the algorith should
break and that's like very easy to show
people just have one more fault see what
happens it crashes all possible ways you
know and that's like an easy metric you
know but another metric like in code
verification is just how many bugs you
have found basically and and there is
like another metric which is saying how
fast you you have found this bug you
know okay thank you um we still have
time and uh uh also have still a lot of
questions and U the next question would
be have you had experience formally
verifying uh ZK proof systems and the
cons at constrainted polinomial level
and to what extent does lean have to be
modified to express theorems in that
context yeah yeah I think I'm the best
person to H this one so yes we have done
that uh how much does lean need to be
modified not at all it has uh Notions of
finite fields and polinomial built into
math Leb uh um now uh We've also
actually written some like uh custom
decision procedures for finite fields
and these sorts of things that do speed
up the uh verifications of these these
properties but yeah other than this it's
mostly actually just uh extracting from
whatever your ZK DSL is writing that
extractor from whatever your ZK DSL is
into a set of a polinomial constraint
system in lean but as I said there's
primitive support for that in the
standard Library the the one the one
issue that I think is a bit more
interesting and where we're hoping for
some more language support particularly
in plony 3 is that a lot of the ZK dsls
as they are now that tool chain is not
at all modular so it basically it goes
through a bunch of generation steps and
right at the end it just dumps you you
know thousands tens of thousands of
constraints sometimes in one big in one
big one Big Blob right and there's no
notion of oh this came from this chip
Etc and so one one thing that I think
will be uh good in terms of helping this
kind of verification scale better it's
more actually on the ZK DSL level is
actually having uh a more a better
notion of these sorts of modular
boundaries this is a chip these are how
these are wired together yeah sorry so
no no so just following on from that
because at the formal verification hang
out yesterday um you know there was
mention of uh it was called llz K which
is lowlevel ZK which is about bringing a
kind of Intermediate Language that all
of these dsls could compile down to and
then the verification work come off that
that's sort of what you're talking about
uh yeah yeah exactly exactly I think
this is actually a great idea the one
issue that I I would issue in quotes
that I would have with this is at this
point in time the proof systems are
evolving so quickly that it's unclear
that any DSL that we were right at this
point in time is really going to be able
to cap capture all of the constraint
systems going forward uh but uh from my
understanding this llz K or whatever it
seems like very honest like a very solid
attempt by very dice doing this for the
moment and I'll be very curious to see
their progress yeah
okay the next question is what is the
first baby step you and Tool you
recommend for engineering teams to start
on a journey uh with the formal
verification H well I mean uh most for
most developing teams are already using
formal verification to some extent in
the sense that often they use type
systems and that is a very simple form
of formal verification right um and I
think as Zoe pointed out rust is
becoming like more and more popular and
actually I mean linear type systems
certainly I think within smart contract
development has uh actually have a lot
of potential because I mean most smart
contracts are actually kind of like
about managing resources moving money
from A to B making sure that I haven't
uh you know I haven't double spent any
of that money I haven't not spent any of
that money right and so I think that
there's a lot of uh on the very low
level there's a lot of capacity for just
using basic type systems to enforc
properties are useful
um I think lightweight verification
tools is a great start um they should
use atvm to symbolically execute their
smart contracts um it's like easy on the
programmers end to like convert their
tests to symbolic execution like
assertions and then take them formally
with a symbolic execution so this is my
recommendation um yeah I also think like
simple tools and I mean
but you can check Quint that's like the
surface Syntax for plus it has a random
simulator like starting very easy I
would say but something like that in
general
yeah um and um one more question um
between wiper and solidity languages
which one is easier language to formally
verify is the last
question can the answer be
neither uh I mean neither these
languages have fully formal semantics
right and so this is this is a key issue
that we have is that typically uh you
have to go to Ule or the evm to really
have formal semantics so actually have
an actual fixed meaning of what the
language means otherwise for both of
these really the language semantics are
defined by well whatever the compiler
chooses they are and uh and and so the
answer at least for me is neither you
just have to compile them to some other
representation which does have a
somewhat fixed semantics and then reason
uh none I think uh but I think there is
a huge opportunity here to build
languages with formal
semantics and verification in mind I
think that's a huge step towards making
formal verification more widely adopted
in the
space uh thank you very much oh
sorry thank you very much and
uh U the next session will start at 11
sharp so we have 5 minutes uh for rest
so please
yes when MC
you so when you want to
take okay
oh
fin
w
B
uh hello everyone again um we about to
start the next session so now we're
going to have two lightning sessions
back to back so this is just a 7 minute
presentation and three minute uh Q&amp;A so
uh I'd like to uh welcome the tan High
Tran who will talk about the can we for
verify implementations of cryptographic
libraries like the CK libraries please
welcome thank you very much uh I am
tanan and uh I'm now going
to uh tell you whether we can formally
libraries like the ckg library this is a
CH work with between me the team and
Roberto
santin so we all know that RTO Ry plays
an important role in the ecosystem and
uh it has a lot of applications like
identification or sign nature uh however
the implementation is very challenging
you can see on the slide multiple attack
techniques on some common
libraries and uh we don't want similar B
things happen to the ecosystem the
ethereum
ecosystem and uh how can we do that a
typical approach is to use and uh formal
methods to formul reasoning about the
cryptographic algorithms in both the
design and implementation and this is
very active research area in the last
decades and uh many Frameworks have been
introduced uh for example we have crypto
of fosa and
others and now I'm going to show you a
running example the ckg library which is
uh used a lot in the EIP
specification but it implementation is
done in C so a natural question is that
how can we ensure that the
implementation correctly for the
specification and finding a solution is
very challenging because those languages
Python and C are not closed and the C
implementation has a lot of optimization
uh that is not included in the
specification so here is our solution we
uh apply a framework called
crypto and um first you you can see that
we manually translate the Bon
specification into the rpto
specification and then we generate a
test suit to check the equivalence
between them then we automatically
generate an lvm implementation for this
library and then uh finally we conduct a
form approve to show that the lvm
implementation correctly follows the
crypto specification
that is the general picture and I'm
going to show you more
details so uh we already finished right
specification for a function compute kg
proof and you can see that the syntax uh
of ripto is similar to programming
functional programming and uh is
readable uh we also
have test cases to show the equivalence
between the python specifications and
the scriptor functions for example that
the comput kcg proof and finally we
already formally conduct approv for some
C functions like bit reverse
permutation okay we are going to the end
so in this talk I have presented how we
apply formal verification to Reon about
rography and um
the QR code is about uh our GitHub
ratory on our work on the CK GG Library
so if you are interested I'm happy to
discuss more and uh you can find me on
telegram or Twitter my handle is there
is my name hyon and that's all thank you
listening uh thank you very much for
your talk and um I have a quick question
how did you start your journey in formal
verification how I question from me yeah
yeah how did you start you know journey
in formal
verification okay um how did you start
working on formal verification what is
your background ah okay my background
okay
um a few days ago I uh started my P into
youa and I develop a moch cheer for t
plus and then I uh join consensus to uh
apply mod verification technique to uh
blockchain protocols like DVT or like
the uh SEC Library yeah yeah thank you
very much and U do you have any other
questions no I think we're also running
out of time so we will take a short
break uh three three minutes and start
with the next lightning uh session thank
you yeah thank you please give a round
of applause to our
speaker thank you
this
how I pronounce it
Yan Yan
a
o
uh welcome back and we're going to
continue with our next lightning session
so I'm welcoming y uh y Han who yeah who
will speak about the proving liquidity
of amm please
welcome yeah I'm
and I'm formal verification researcher
as
Satora should I use this
one this one okay so um yeah and I want
to show you how to prove that your
contract Can't Get
Wrecked so uh let's remind ourself what
an amm is we want to prove uh a property
for a decentralized exchange namely that
uh yeah that has two major actors the
traders who want to sell or buy tokens
and there are liquidity providers who
provide the tokens to be sold on this
amm and the liquidity providers rely on
the correctness of the amm so the amm
smart contract holds all their funds in
custody and the tokens are automatically
traded and if there is a bug in the amm
then the liquidity providers don't get
their funds back and we want to avoid
so the desired property that we want to
show is that the money can always be
withdrawn from the contract even if
there's a bank run if everyone wants to
get their money back uh it can be
withdrawn and we need two properties
there is enough money in the contract
and uh that withdraws never
rever and we did this for the new
upcoming
uh version of Unis swop Unis swop V4 and
this is a contract that has a few scary
features namely it's permissionless
everyone can use it everyone can create
pools and all the tokens of all the
pools are kept in a single contract so
if there's a single pool that is uh
broken then it affects all other
pools and uh there's also a hook
mechanism so you can create your own
hook for your pool that
could affect this uh security of your
funds and we need to prove that this is
not the case so there are um some attack
vectors like malicious ac20 tokens and
FKS that we need to con
uhid what we did is now formal
verification and uh yeah what we do is
we take the bite code of the contract
and we take the specification and we
translate it with our tool to formula
that we that then run through various
smt solvers CVC 5 and
C3 and this will give us either a proof
that the contract satisfies a
specification or it will give us a
counter example or because this is the
logic is undecidable that we use it can
also time
out we have some assumptions for the
unknown codes so we support arbitrary
estic tokens but to prove liquidity we
need some assumptions on them so the
balance can only change by transfer and
burn um only the owner and approved uh
accounts can transfer there's no Central
author Authority that can steal our
tokens we need other assumption that uh
if you
transfer the only the amount is
transferred so if there are fees the
receiver pays
them and uh that transfer never
reverts thanks
um the transfer never uh reverts if
there is enough balance and for hooks we
need the assumption that there is no
withdraw hooks otherwise we can't prove
that you can
withdraw so what we do is um an
inductive invariant so we want to we
split our States into two kinds of
states where we have enough funds and
where we don't have enough funds and if
we look at all the transaction then we
look is there a transaction that goes
outside the circle and we found with our
tool that there is such a transaction
but it's actually a transaction that is
not reachable so we need to refine our
invariant we need to say um additional
things like that the contract also does
a consistency accounting of the
liquidity and if we do this then we get
the that all the transactions stay in
this inductive invariant
there were some problems with verifying
this uniop it was not as simple as I
just made it so we had some problems
with rounding errors break the
invariance and other things like sums
over ticks and
positions um we solved all these
problems I can't go into the details
because it's lighning
talk so to
summarize what we showed is enough funds
and consistent accounting is an
inductive
invariant yeah thank
you thank you it's a amazing uh research
and so we have one question and I'm also
very uh Curious how many human hours did
you guys spend to prove liquidity of uh
uniswap 4 and if there like maybe you
can uh put some price tag on it because
I think this is very interesting because
before like on the panel before we were
wondering about you know this kind of
yeah I I don't have the price tech I'm
not sure if even allowed to tell it um
but we spent several weeks with a small
team so several people on this contract
so I think it was something like six
weeks six weeks yeah W and uh how big
the team was like three people five um
more more like I think over five but
less than 10 okay okay interesting and
how many errors did you guys found one
one such case where this transaction can
lead to not enough liquidity right um we
didn't find the liquidity error so the
code was quite good there was mhm
slightly problems like you can't trade
to the minimum price and you can't reach
the minimum price but if you start there
it's possible to start with this price
so there was some inconsistency there
okay so we have one more question could
you briefly touch on how you approach
dealing with the rounding errors
in yeah so we use um we use a we use fix
Point arithmetic and we use a very high
Precision because we have unmounted
integer we can just use uh some
multiplier for fixed point that divides
every number and then we don't get
division uh roundings
okay thank you very much and for
interesting talk please give another
round of applause to our
speaker so now we're going to have a
three minutes break and we continue with
the next session
the
May presentation yeah uh no I'm doing
live coding yeah so if that's okay I
mean there is there's also U some slides
I'll be showing but
uh clear framework so the the first
thing is that so clear is a formal
verification framework and the first
question I want to answer here is well
what even is uh formal verification
formal methods all of these words what
what do they mean right and so uh
essentially formal methods are made up
primarily of well two one part which
we'll see in a second which is where we
have the language semantics part of it
which is studying actually the meaning
of programming languages what the
oh I need this oh I see it's not cap I
see okay sorry let me re redirect that
can everyone hear me now okay perfect
cool sorry about that so uh so the first
part of it is a sort of language
semantics so studying the actual meaning
of programming languages so that we can
reason about them and then there are
programming uh program Logics which are
allow us to actually then reason about
the semantics of individual programs
prove that they have certain properties
and these sorts of things um and yeah
you I mean some of these you guys will
be quite familiar with because actually
a very simple example of a a program
logic is actually type system so it
proves some very simple it actually
proves some very simple properties of
your program at uh compile time where
it's proving that hey this variable will
always have this structure because it's
of this type this sort of thing uh but
then there are more more advanced sort
of uh Logics properties and these sorts
of things so but but all of these all of
these Pro these program Logics typically
the proofs that we write in them are
quite complex and involved and so if we
want to have any sort of degree of
certainty that these uh the proofs that
we've written are actually correct we
actually want to also mechanize these
proofs so put them in a format where
they can actually be uh computer checked
right and so there are sort of schools
of thought primary schools of thought on
this one of them is the automated
theorem proving Direction uh which is
looking at sat Sol which I think most of
you would have heard of smt solvers TP
tptp there are a lot of complex
mathematical fact mathematical facts
come into the into reasoning about this
I'm seeing that the demo I wanted to
show a little bit later is uh currently
not compiling so I'm just going to
quickly rerun that it just needs to just
a lot faster requires a lot less uh
human interaction right but there are
some situations and there are there are
fundamental reasons in computer science
where there are some situations where
you are really are going to need the the
uh expressivity of interactive the
improving and uh in particular as I
mentioned in the panel earlier today I
do think that for certain important
parts of the um uh ZK protocols uh
consensus layers all of the all of these
sorts of things and so the the reason
for this sort of necessary tradeoff is
this thing called risis theorem
essentially uh it's a theorem about
about the uh
limitations of deciding whether the
specific if holds or not right and what
it says is so firstly we have some set
of programs right and we have a set of
states that these programs act on and we
have uh an evaluation function which
basically says given a program and
initial state it evaluates that program
in that state and it spits out the uh
the final state right and then finally
we have a predicate which basically
decides uh is is our specification right
and it tells us hey does this it's a set
of programs that satisfy ENT some
specification that we care about and
risis Theorem actually says this which
is if I have two programs F1 and five f
equal and the definition of that is at
the bottom it basically says that if
these two programs when run in the same
state will always give the same result
right then it is the case that uh
essentially that then we know that uh p
is on the sorry so if our our sorry if
our predicate doesn't essentially care
so if for two programs which are
extensionally equal this predicate will
always also hold or not right then P
must be undecidable and so essentially
what this mean so let me give you a
couple of examples of you know
extensional equality so a sort of
motivate this a little bit right so you
can think of like there might be
multiple ways of uh implementing like
addition right so you might have like a
primitive notion of addition in your CPU
you might do like piano stle Edition
where you just have a loop you want to
add a and b and you have a loop where
you add one to a b times right uh or you
might have something that where you add
B+ one to a and then you subtract one or
something like that right and all of
these all of these um uh all of these
programs are extensionally equal so they
have they're different implementations
but they have the same uh Behavior with
respect to what they return right and so
Rice's theorem says that essentially if
I have a predicate that only cares about
the behavior not the structure of the
program then it is necessarily on the
decid one right and so this basically
places a fundamental limitation on uh on
on what can sort of be proven entirely
automatically right and so of course we
can sort of uh we can stack heuristics
and these sorts of things to be able to
extend this as far as possible but uh at
least for the moment uh I I think
interactive the improving still has a
lot of place in the uh the verification
of some of the more P complex pieces of
infrastructure within particularly the
ethereum ecosystem but also more broadly
okay cool
um so now what actually is the uh the C
the sorry the clear framework it's a
framework for formally verifying smart
contracts written in languages that
compile to Ule so obviously for the
moment as far as I'm aware that's
basically solidity in vipers there not a
a massive set I put a dot dot dot there
I'm sure more coming but uh that's all
I'm aware of for the moment um and so
what does it do so it basically allows
users to write computer checked proofs
of the uh of the correctness of their uh
of their smart contracts right and in
particular all of this is done by
extracting the semantics so we have a
formal semantics and we go into this in
a little more detail shortly but we have
basically a formal semantics of of this
ual intermediate representation which is
used used by the cility compiler um in
in in the lean proof assistant and the
lean proof assistant has has this
Library called mathlib and mathlib is as
I said earlier debatably has the largest
formalization of uh of of mathematics in
proof assistance and existence right so
hey you need the Schwarz zipple Lema to
be able to prove the correctness of your
ZK ZK protocol well we've got you right
uh and andot and you know a lot of uh
other techniques wouldn't be able to
handle this it also has one thing that
is quite unique about uh about
particularly the lean proof assistance
is that has uh remarkably and and I'm
going to say almost uniquely uh
extensible automation system so if you
need new automation new proof
automations you come up with new her
istics to automate parts of your proof
and these sorts of things you can
actually just write that in lean right
so you can just integrate that into your
proof assistant you can write your new
decision procedure and then you can run
it whenever you want so this allows it
to be extensible to all sorts of domain
specific areas where you may need new uh
automation so for example my team has
embedded some like decision procedures
for finite Fields when we're reasoning
about like systems of um of poal
constraints and these sorts of things
and we we've embedded these new decision
procedures into lean and we're going to
see some very basic embedded decision
procedures today that deal with like
looking up variables and these sorts of
things so very basic stuff but
nonetheless all of this is done and lean
doesn't require and you know can can be
straightforwardly encoded into the
language and the final thing and this is
something that I find to be uh that I
really enjoy about the the lean proof
assistant in particular is the the it
has a very powerful notation engine so
um it's essentially and I I did say this
in my uh panel earlier but essentially
it allows it has a a pre-compilation
step where the um the the the the what
you call the programmer the lean
programmer can basically essentially
give arbitrary semantics that they
desire to an arbitrary string of Unicode
right and so essentially I can embed
pretty much any notation that you can
think of that is embeddable into Unicode
uh inen so that means that actually most
of most modern mathematical notation can
be embedded very straightforwardly into
lean and that means that unlike previous
proof assistance I can um I can write my
uh the theorems that I'm proving in a
format which is completely
understandable to mathematicians right
and and and can be made completely
understandable to uh to like people
programmers and these sorts of things
right so we can basically we're able to
uh expl explore exp this notation engine
to allow the specifications that we want
to write to be written in basically
whatever format the our target audience
is most familiar with right so if you're
a mathematician and you want to see you
know lots of uh and and you want to see
whatever notation that's fine but also
we can write specs as just like normal
tests and we want to prove that this
test can never fail for any sort of
inputs right both of these things are
fairly straightforwardly possible uh and
the other thing the other thing is that
uh proof is assistance are uh by by well
not by their nature but rather it is
fairly straightforward to make
verification inside of a proof assistant
modular right so what do we mean by and
what do we mean by modular so that means
that we can sort of split up a
complicated program that we have into
lots of small subprograms the functions
Etc and be able to reason about these
things independently write a
specification for my Loop my function
whatever and then be able to use this to
abstract that when reasoning about
things that use this function use this
Loop Etc and this this allows for
scalable reasoning this allows for proof
reuse right because obviously say the
solidity compiler generates a lot of uh
I'm going to say um a lot of sort of
generic functions so there are like
functions that check for uh arithmetic
overflow there are functions that
obviously compute your index into
storage memory when you're using a
storage array uh a storage map rather
right and all of these sorts of things
and uh the we can basically just
pre-write proofs for a lot of these
things and we've started on this um and
and and then basically these can be used
reused in whatever context by whoever
wants to then verify their smart
contract that happens to use these uh
these uh Primitives and then the other
the other sort of uh very interesting
thing is that also I think this is
becoming a lot more interesting and the
the the rollup contracts associated with
l2s are essentially interacting with a
like a a complex external system that
has complicated interactions and
semantics
and and typically actually we want to
reason about an interaction between
these complex and the actual uh L1
contract it's uh and the the the L1
contract itself and so in typical like
uh in sort of typical smart contract
reasoning Frameworks that exist out
there this ability to extend things to
be able to reason about what's outside
of this world what's outside of the evm
is uh I think uh very is very
powerful um and and then finally the
other thing is that unfortunately in
this tradeoff uh on the side that we are
I'm going to say that there's a a
relatively High entry barrier so
typically you want to have at least a
fairly strong background in functional
programming no bit of logic and all of
these sorts of things before you're able
to really seriously use these things now
we're hoping we're hoping to actually
introduce enough automation here so as
we said access to smt solvers tactics
and these sorts of things that it may
become feasible for humans for humans
I I am human I assure you so but uh for
for people who aren't e domain specific
experts if you will to uh to actually be
able to use these things and and I'm
hoping that uh that uh if if my demo
will starts working which I'm going to
have to look at in a few minutes uh I'll
I'll be able to actually show some of
this off today so yeah we'll we'll we'll
see how that goes perfect cool um okay
so then now what actually so what is the
clear framework actually made of so I
already mentioned that we actually have
a formal model of uh Ule so Ule is a
we're going to actually see a very short
like intro to U so U is just a very
simple imperative programming language
that in particular has a um uh has
basically has you know the control flow
that you would expect you have ifs you
have loops you have functions all of
these sorts of things switches uh as
well as being able to assign variables
to expressions and these expressions are
written in terms of constants variables
and uh and in fact the sort of the
subset of the Primitive operations of
the evm right and so essentially what
does it do it means that it abstracts
the use of the evm where you the human
being doesn't need to explicitly reason
like a stack machine when they're
reasoning about the control flow uh
while still being at a sort of a very
low level of abstraction and actually
having fixed semantics and this is
actually a very big uh issue overall
when reasoning about smart like EV M
smart contracts as a whole which is that
uh well most of the high level languages
don't have fixed semantics right so the
the formal semantics of solidity is
basically whatever the solidity compiler
says it is at that point in time uh and
that's obviously is is not ideal in
terms of reasoning um and so so here we
kind of to be able to have a a trust
base that we can actually have any
degree of uh confidence in we uh what do
you call it uh we basically need to
compile this down to a low level of
abstraction which is well we don't want
to compile down all all the way to the
evm because well we tried that and uh
humans are not and this time I really do
mean humans humans are not meant to
reason about stack machines it's uh you
know there's a a lot of cont contextual
information which is continuously
changing as you push and po pop things
off the stack off the stack and it's
just not practical so uul offers like a
good level of abstraction where it does
have fixed semantics while uh also being
at a high like abstracting enough of the
control flow that it's not you know I'm
not torturing my Engineers by making
them reason about these things so that's
always great um so okay so we have this
formal semantics of Ule and actually as
we said shares these primitive
operations with the evm and actually we
simultaneously have uh uh formal
semantics of the evm and in fact they
actually uh they actually share the
implementation of the prim Ops and why
why is that good uh well because
actually our evm model is uh modulo
certain details which we we sort of fill
in uh is actually executable and so I
can this is actually a formal model that
I can actually run against the
conformance test right and so by doing
this by actually running the evm model
against the conformance test I can have
a very high degree of certainty that my
uh my model of my evm Prim Ops are
really what uh the community and the
execution clients believe that they
should think that they should be right
and and so for actually for the moment
we have I think a around 90% of the
conformance tests passing on our evm
model which is not bad but obviously
we're hoping with this is ongoing work
and we're hoping over the coming weeks
to actually achieve 100% although it is
one of those like 8020 things where like
getting most of it is pretty easy but
squeezing out those last couple of
percent can be pretty tough so I I don't
want to guarantee any timelines there
but we're working on it essentially uh
and I think the key things certainly are
are probably uh correct uh at this point
in time which is good um and so yeah so
so essentially by by having this shared
model with the evm model being executed
we also then gain a very high degree of
certainty in our U model hopefully cool
uh and then the second thing that we
have as part of this is what we call a
verification condition generator right
and this is something that you can
basically you compile your smart
contract from solidity or Viper or
whatever into Ule uh and then what uh
what what happens you receive you have
your ual smart contract and you can then
point the clear VC at this ual smart
contract and what it does is it
automatically processes it in all sorts
of ways that we'll go more into detail
in in a second but it basically extracts
that Ule into the lean proof assistant
and automatically it cuts it up into
basic blocks for those of you who you
know know any things about compiler
Theory that's basically like a block of
code that contains no control flow right
so we like we cut up the ifs we cut cut
off up the while Loops Etc and we split
those up into separate abstracted blocks
uh and and then for each one of these we
sort of automatically derive a uh a
specification and this is done entirely
by the proof generator it's a basically
a a very
simple um it's basically just something
that uses the semant unfolds the
semantics of this and uh and and applies
a bunch of simplification tactics uh
which which is you know an ongoing work
to improve and perfect um but uh but
yeah so it essentially runs these uh
sort of uh these it uses these tactics
to basically give you a simple
relational spec so by relational spec we
mean basically a relation that uh
relates our abstraction of the uh what
do you call it uh relates our
abstraction of the uh of of the state of
the evm before and after the execution
of a given piece of code right and then
the last thing that uh clear that the
clear framework is made up of is
actually an like this is ongoing
development a library of theorems and
tactics which actually then facilitate
the Practical verification of uh of some
of these contracts so uh once again as I
was saying in my panel earlier like
we're developing like a lot of these
theor imprs tend to not have a lot of
facts about bit vectors Len is kind of
fixing this now but uh and then
certainly we have some facts about uh
how storage memory Works cack being
injective supposedly all of these sorts
of things which I'm not going to go into
too much detail with uh today
um okay so so yeah so the this actually
now this diagram shows us kind of the uh
the workflow of uh of of using uh of
using clear right so in particular you
take your solidity SLV do dot you run
salc you compile it to Ule uh in fact
actually our the clear framework doesn't
deal with totally totally generic Ule
and so actually you need to use a
specific set of compiler Flags uh which
I'm not once again not going to go into
too much detail about but you can look
uh on the uh read me for clear and find
them but essentially there are things
like uh the expressions in Ule can be
sort of nested where you call uh what
you call it you call some operation on
another on a sub expression which in
turn has a bunch of other operations
applied and Ule is not super happy with
that so we use one of the um uh what do
you call it one of the optimizations we
use is the expression splitter which
basically makes sure that your
Expressions have a sort of Maximum depth
of one and these sorts of things we
actually I think we're probably going to
fix this change this in the future we
thought it would be a good optimization
in practice it just makes the programs a
bit unwieldy so let's let's see if we
end up changing that then as I said we
have the proof generator which extracts
all of this into uh into lean you get
your Ule extraction and your
verification condition proof and then
the human all the all in quotes the
human being needs to do is to insert a
specification so this is a formalization
a mathematical formalization of the
intent of what they believe to be the
the intended behavior of this code and a
proof that the verification condition
this simplifi this proven simplified
specification of the code implies a
specification right and that me that
results in your uh your smart contract
being fully formally verified okay
excellent cool um ah yes yeah yes here
okay sorry one one more slide this is
just once again a very very quick
overview of the syntax of
uh and you'll actually be able to see
very shortly I think something that is a
very nice uh cool advantage of uh of the
clear appr approv system this embedding
of notation because well rather than
having to like embed the as well I mean
we do embed the as of ual into lean but
rather than actually having to
explicitly construct instances of this
actually we've just embedded the Ule
syntax into the lean compiler and so we
can just write Ule and lean and it just
automatically passes it for us and uh
and extracts it so actually the the you
know I I write this as an arrow there
the Ule extraction as if it's difficult
it's like literally copying and pasting
the code into into blocks right so that
that's that's not super hard the
difficult part was actually writing well
difficult it was actually very easy but
the in quotes difficult part was uh
writing the uh Ule the Ule passer into
lean um cool so yeah so as I mentioned
very quickly very quick overview of the
U syntax so the first thing is we only
have one type in so actually no this is
not entirely true so Ule is kind of a
parametric generic language when we're
talking about Ule here I mostly mean
what's known as the Ule evm dialect
which is a specific dialect of Ule where
the prim primitive operations are are
the evm prim Ops right um and uh yes and
and so essentially uh in the UL evm
dialect everything there's only one type
everything is UN 256 and then as I
mentioned we have assignments and and
these can actually be sort of um uh what
do you call it uh V sorry assign like a
higher arity assignment so it can be the
case that like a function or an
expression returns sort of multiple
values and we combine multiple values at
the same time so that's what this means
this means that x0 through xn are bound
to the result of the expression as we
pointed out the expression is built from
constants variables and the Primitive
operations of the evm we have ifs where
you have you
know condition on your if which is the
the B and conditionally on that uh that
evaluating the true we execute C we have
loops which are a little I mean they're
they're not unusual I guess but uh I'll
just go through the semantics here so we
have uh I which is the init block which
is run before so this can initialize
variables and these sorts of things
which are going to be used in the scope
of the of the loop uh we have uh a
condition a loop condition which is
checked obviously before each iteration
of the loop and we have a post which is
you know uh which is a little piece of
code which is executed after the uh the
body of the loop which is a c and this
post is you know used typically for
updating uh iterators and these sorts of
things right iterating variables and
these sorts of things um and these Loops
can contain break and Contin statements
and that's actually uh I mean we not we
might go into some an example with some
degree of uh showing of how we reason
about these but it's it's a bit more
complicated to reason about this in
totally generic way uh and then finally
of course we have have uh well we have
functions uh which are all
straightforward and finally we also have
and I ran out of space on the slide but
you can all imagine what it looks like
we have a switch statement which you
know takes some expression and depending
on the uh the Val the value that that
expression evaluates to it can sort of
uh go into multiple branches right so
all of that uh should be fairly
straightforward um okay so now uh I
wanted to run tutorial one let's
see if this actually works though okay
perfect um let's I I'm not going to
guarantee this is going to work because
of course uh as the genius that I am I
decided to make some changes to this to
try and perfect it this very morning and
so of course there would be consequences
so um but uh okay let me just switch
this over perfect okay
so so here we have clear right uh and in
particular we have some like simple
examples which we can see in the out
file I don't know why we call that file
out to be honest and let's actually look
at the very simple example that I want
to start out with which is the uh erc20
dole and so this is a very very simple
uh SM like this is a very very simple
smart contract and in particular it's
it's stateless right so this is
something that something like something
obviously it's incredibly simplified to
uh to allow to so that we can reason
about it in a very short period of time
but uh essentially uh th this is
stateless so typically obviously in the
rc20 we'd have some sort of storage map
that keeps track of uh the underlying
balances of all of the users and these
sorts of things we're kind of
abstracting that away because then we
have to start reasoning about Kack and
we have some automation there but it
just adds too much detail um and so
essentially we have a transfer function
which takes an amount and the balance of
account one and the balance of account
two and obviously the transfer is
happening from account one to account
two and we return two values which is
the balance afterwards
and we also don't actually deal with
overflow here so we're assuming that the
total supply for the sake of argument
that the total Supply is less than 2 to
the 256 and we know that as an
invariance so that this can't break
right as I said very simplified example
and so all that this does very basic Ule
that we've extracted here is it Compares
it makes sure that essentially count one
has a sufficient balance right and if it
does uh it uh what do you call it it uh
subtracts the amount from account one
and it adds amount to account two right
and and returns those values otherwise
it leaves them intact and obviously we
could do a revert there but once again
I'm trying to avoid here reasoning about
complex control flow we'll get to some
of that in in some uh some later
examples right okay cool so uh then if I
want to actually extract this into uh in
lean I have a VC which I can quickly
build make sure it's built up to date
apparently excellent and I can use this
to then basically I just need to point
it at a smart at the Smart contract that
we were looking at earlier which was
called erc20
Dole and Bob's your uncle in theory we
should now have yeah and it's all going
red of course so I I'll find out what's
going wrong here but we'll start
exploring it a little bit um okay it's
resorting the file perfect so what so uh
oh no I don't want to look at that I
want to look and let me close some of
these sorry should have had this a
little bit better
propar um but yeah so what what's
actually happened here is uh this is the
elc2 is being extracted into this file
here right and so you can see that we
have uh a file we have a file for this
transfer function right uh and we have a
uh well sorry we have three files for
this transfer function and we also have
this if thing here uh which we're going
to look at in what in in a second and so
essentially what's happened so we can
look at the generated uh oh great this
is this is amazing that was really not
what I wanted vs code to do let me just
click
here okay let me let me actually see
what this error is
sorry it's just telling me to rebuild it
let's see hopefully that will help
uh lucky me this was very smart of me
anyways um so so yeah so we can see
actually that this has uh that the Ule
here has been extracted into uh inine
and and this is pretty much the syntax
that you guys saw in the file right and
so lean actually because we just have
this embedding of Ule into lean uh lean
is just able to pass this I mean modul
is compiling which well let's find out
how that goes um so uh so yeah so so
soen automatically basically so sorry
the verification condition generator
automatically extracts this into uh into
lean and uh and then it also in
particular actually abstracted away this
if and that's what this extra if file is
about so if we look here we see that oh
it's actually split out this if for me
right and over here well you can see
okay this this all looks uh oh it's
compiled it wonderful oh okay it's
actually working always a good sign um
yeah so so actually uh so yeah so
actually then can we actually see this
yes awesome awesome so you can see that
as I said we've just written our Ule
here and actually what I what can I do I
can do eval and then
this uh one
second no it's not happy what's it
saying
no no no no that that is actually part
of this character here no no that is
actually part of that's a the limiter
for this um but okay maybe let me just
try and uh because actually yeah this is
not available let me just see if I can
just print this ah there you go okay
there you go this was what I wanted to
do so in in in lean I so basically uh I
can actually just print the underlying
term here that I get from passing all of
this U right and so this you can see
this is basically our as of Ule in um in
in like the the uh lean definition of
the Ule a that we have and we've just
been able to write the Ule directly into
lean and this just passed it out and it
now has sort of uh extracted that and I
can print it out all right and now you
can see this thing at the bottom which
was automatically generated uh which uh
you know is probably going to seem like
uh gibberish to you guys uh let me just
get rid of this quickly um but
essentially this is the automatically
generated uh uh
like specification this verification
condition generation right and actually
what are we doing here so actually this
me says that hey I have some C and C is
basically a predicate which relates a
state to a state and this is what we
call a proposition so this is like a
like a a logical proposition which can
be sort of provable or not essentially
right or true or false if you will I
mean that's not entirely true I know
that there are one or two constructive
mathematicians in the crow who sort of
frowning at me very heavily at this
point in time but most people don't W
won't care too much about the
differentiation um but yeah so
essentially we have uh this uh this uh
this predicate here which relates the
state it's meant to relate the state
before and after the execution of this
basic block right and this second thing
is basically a proof that we're
generating here and it's automatically
generated that says well for all states
initial State s0 and final State S9 if I
execute my piece of code here so this is
my if above right in the state s0 and I
then get S9 this implies that the c i
define here is a specification that
relates s0 to S9 essentially right so it
relates s0 S9 and we have this spec here
don't worry too much about it it's
because it deals with some with like
sweeping on the carpet reverts and
errors and a few other things uh that
that and it just makes it easier to not
have to explicitly reason about these
things and so basic basically what we
have now an automatically generated
proof that automatically writes somewhat
of a simplification of the piece of code
that I have above and we can sort of so
the nice thing about lean is it has what
we call this interactive mode where as
you go through a proof you've seen on
the right hand side it gives me
interactive information about what is
the context of my proof what's currently
happening all of this sorts of stuff
right and so I can sort of Step through
this and you can see the proof being
constructed on the right hand side as we
go along and we we I'm not going to go
through all the details but right here
this is where it ends and you can see
that here it's basically taken all of
the code into this H in the context it
simplified as much as possible and it's
saying hey this will be my spec
essentially right and so I can't
actually see it because of the angle so
I'm going to move over that to see what
the spec is for a second one
second yes okay
yes
so yeah so so essentially we have uh uh
uh an if in the ambient logic which says
well we look up in s0 underscore one we
check if its value is zero and if it is
zero then we basically we we uh do a
bunch of updates to uh s0 so in
particular we um what do you call it we
we compute the uh new value well you can
see we we update these the ac1 and ac2
values by and filling it we fill in the
the sort of arithmetic expressions for
them I I really can't see this very well
from this angle
sorry aside so we can see this a little
bit
better genius yes it is you're
completely right thank you thanks Dave
uh yeah this uh will make things a lot
easier excellent thank you so much um
perfect yeah so we can see what what
what actually happens here right so what
what it's saying so we're saying that S9
is equal to this and we're basically
saying well if uh s0 is equal to to to
uh sorry underscore one the variable
underscore one is equal to 0 and s0 then
this is the update that occurs otherwise
nothing happens and we just return s0
and so S9 is equal to s0 in this case
and that is the sematics of the loop
right and so here what do we say we say
that in s0 we update act1 right to equal
to equal essentially act1 minus the
amount and we update oh God sorry and we
update act two to equal uh the and yeah
this is after the update to equal
essentially the looked up version of Act
of this is because and we're going to
simplify this all away very simply in
one second is because well all of this
happens after the first initial update
and so this is the intermediate step the
intermediate state after the the first
uh the addition OCC sorry the
subtraction occurs right so so so but
we're going to simplify all of this away
using one single tactic in one second
and so all of this was automatically
generated so it wrote a simplifi like it
very
straightforwardly uh wrote a simplified
uh version of my specification for me
all
right essentially so it's it's for being
flattened into propositional form along
with a bunch of simplifications which uh
sort of and and actually uh the the
change that I was making this morning
that I just I literally reverted mid
speech which was very fun so I uh was
was actually to to already apply the
simplifications here to get rid of the
uh to make these lookups look simpler
right because essentially I should be
able to say when I'm looking up ac2 in
this well I haven't updated ac2 with
this update and so it's just the same
thing as looking up ac2 in s0 right and
so that simplification uh we have a
tactic that does this automatically I
was trying to inject this into the proof
generation it did not go particularly
well so uh yeah turns out modifying your
demo uh right before the uh the demo is
a bad idea who knew okay perfect so all
of that is the the user generated uh
side of things sorry the automatically
generated side of things now we can
actually get to the oh great and of
course vs code is being very helpful uh
now we can actually get to the user
input right so the user input here and
this is automatically generated but I
need to sort of fill it out so the inut
the user input here is well I need to
write a uh a specification right to like
I want to write the actual intent of my
uh if right and I'm actually going to in
this case my specification is literally
going to be my VC my verification
condition just simplify down a little
bit so I'm actually not going to write
it manually I'm just going to actually
use a simplifier one of clear
simplifiers to automatically get this
spec from the VC and then I'm just going
to copy and paste it hopefully um so
here so as we can see in lean we have uh
my goal on the right hand side so I want
to prove that the verification condition
implies the spec right except I don't
have uh a spec yet but what I can do is
I can already unfold this right to to
get the ver to see the verification
condition that the uh that that clear
gave me so I can write unfold this and
it now unfolds yeah I keep forgetting I
can just look ahead to see this sorry uh
and so this actually gives me this sort
of simple um what you call it this this
simplified VC that we already had right
and um here I can write is it clear VOR
uh did that simplify yes did
it s0o
amount well well actually there's an
easier way of seeing this I can just go
before I know okay so I need I think I
need to do s a clear V T
at uh and uh actually no no sorry let's
do this a little bit more cleanly so
let's do intros H so I introduce my
assumption so now I have a h in my
assumption which says Hey the um
specification for the verification
condition holds and I want to prove my
uh my specification right and so I've
I've introduced this and so now
hopefully if I do clear once again
VOR and I think I can do at
H was it h
comma okay there we go uh and yes okay
so now it has actually simplified some
of these things down all right so or has
it what's what's it actually saying here
oh yeah no actually it's not okay so the
the simplify isn't working super well in
this demo right now but okay so let
let's actually try and write the spec by
hand then to make it a little bit
simpler so what do we actually want to
prove here well we our specification
that we get the automatically generated
one is this and that's a bit too
complicated right let's actually make
this align this a little bit better to
be able to read it a bit
better um
okay this is now a little bit more
legible uh and where's my else Branch I
didn't copy and paste the else Branch
great one second so in the other cases
we say well it's just the case that S9
is equal to S Sub 0 there we go and we
just want to write
S9 equals oh that was not nine sorry one
second there we go
and okay still not fully happy with me
what's it saying
here ah okay so it's not entirely happy
with some of the updates for whatever
reason let me just try and like pass
these out a little bit better so that I
can read them so we have the update to
ac1 we have the update
ac2
um yeah this we can just forget this
just becomes so I'm just going to
simplify this
away this just becomes looking up ac2
right and this also becomes this looking
up amount because we haven't changed
amount
here and I think that should oh oh I see
I'm missing I see now what's wrong I
missed a bracket which was why lean was
unhappy with me yes okay now we have a
reasonable spec right uh and yeah not
entirely sure why the simplifier wasn't
working there but as I said I missed
messed around with this just before so
that probably did not help um but yeah
so we have so now we have this and now
actually we can also unfold our our goal
right so we can unfold this part of the
specification and we can run some
automation let's see what happens so
this is a quite a powerful simplifier
that will sort of go about uh um hm okay
so maybe maybe this is not actually the
cleanest way of going about it okay so
let me just go back to where we are here
let me introduce our H oh yeah we
already introduced the H and what we
want to do now is what what we're going
to want to do is basically case on this
to be able to prove this or this is
getting a bit messier than I was hoping
um so once again in N we can basically
break down on a case of whether
proposition is true or not do we oh we
don't even have an s0 in scope what's
happening here
sorry okay interesting why is it not
happy with
this it's not an inductive
type what am I eliminating
into uh okay well this is going I'm I'm
just going to sort to try and Brute
Forces to see where we go then um okay
so at least now we can continue the
proof so I I'm I'm going to
unfortunately have to because once again
I broke some of the automation this
morning it seems I'm going to have to
sort of break this proof down more than
I was hoping to uh it was meant to be
just be two sort of tactic applications
but it's not quite working out um but
essentially okay so uh we'll we'll
ignore one of the simple cases very
straightforwardly so I'll just quickly
get rid of
that okay that sort of goes away
here we have jump underscore and I'm
just going to sorry that out for the
moment and here we have okay evm and
sigma uh oh I'm missing another
underscore
here no this is
not ah oh it's checkpoint oh
God okay
so now I think we hopefully have
something a little bit cleaner so we can
sort of simplify down our goal and now
we just want to uh basically prove so
this this uh you might have noticed this
sort of outer fuel uh thing and this is
this is actually a bit uh annoying and I
was as I said this should have been
automated away but unfortunately the
automation isn't quite working this
outer fuel is basically because in uh
proof assistance there are reasons that
basically you want things to always uh
be able to terminate right and so the
reason is that actually termination we
we've talk like uh I've sort of been
alluding to this a little bit but
essentially lenix exploits this sort of
this what we call the Ki Howard
isomorphism so this is the fact that
basically actually at some level there's
a way of embedding high order the logic
into the type system of a dependently
typed programming language so if you're
if you're you have a a programming
language whose type system is expressive
enough eventually you can just basically
embed logic into it and just prove
things with it and this is basically
what lean does this in in a sense a
normal programming Lang functional
programming language where with a type
system on steroids essentially right but
the problem is that uh for proofs at
least having non-termination is kind of
an issue it's analogous to like circular
reasoning right so in in a a functional
programming language I can write like
def F and I can give it any type I want
and I can just say hey that's equal to F
and and it will just recurse at infin
item and it will never tell terminate
and that that's that's analogous to
Circular reasoning and so essentially
for these reasons we uh sort of need to
we need to only reason about terminating
traces and this is what this fuel is and
in fact in fact actually we can
obviously use gas to reason about this
because of course evm programs do
terminate because of this of gas but uh
but but but basically gas is a little
bit because some of the uh GA like some
of the gas computations are a little bit
complex and so proving that this is
monotonically decreasing is a little bit
more complicated right and we're working
on automation to be able to get rid of
this but this this outer fuel case is
basically saying hey you've reached a
situation where uh you've ran out of gas
if you will and therefore we cut if you
will and therefore we you know all sort
of all not all bets are off but it will
rever in in a case where it's not
terminating in this case it will just
have reverted by now right and so that's
what this outter fuel is dealing with
and so we're just sort of uh as I said
this actually should have been dealt
with the es sub spec tactic but is not
did not work right there I don't quite
know why but I'll look into that a
little bit later
uh well that's actually what we're doing
here right so actually inside of the
spec predicate we actually folded an
implication that says that uh if you're
not out of fuel and this is what this
question mark means if you're not out of
fuel then the specification has to hold
right and so this gives what we call
partial semantics to the program logic
of it says that hey only if you have
termination does this specification hold
right um and so so yeah so so
essentially we're we're continuously
filtering out these outter fuel cases
and as I said there is automation I
promise that does do this but it's not
working right now um because I was very
smart anyways so uh so yeah so we we
reach down to this state which is is uh
sort of we're approaching hopefully a
little bit more what we want um and what
we can now do is we can introduce the
fact and I'm going to call it not out of
fuel so now we have an extra assumption
which says well by the time S9
terminates I haven't run out of fuel
right and so that will allow me to
continue reasoning and now I'm going to
be able to unfold my specification the
specification I have here to be able to
uh actually uh start uh start proving
that my verification condition implies
this so let's try and do that so we're
going to unfold
spec at
H there we go and we know we know that
uh uh the initial state that we have we
we're considering the uh the okay case
the case where we're going to continue
so we can immediately simplify this down
so we do simplify only simp only at
H uh uh yes yes yes so we've we've uh
basically simplified down that
specification application now we've
extracted just a verification condition
and note that it requires us to be able
to use this verification condition we
need to actually uh apply know that we
terminate in a state that's not out of
fuel and this is uh and conveniently we
already know this so we're going to be
able to do this by actually specializing
H so we do specialize H at uh not out
no not not like that sorry uh not out of
fuel yeah thank you L there we go and so
now we we're getting closer and closer
to something uh where this verification
condition looks like a uh looks like our
goal right which is which is kind of
nice so we're now what I'm going to do
is basically like break down the proof
by uh uh cases on uh the on the value of
this if straightforwardly and once again
I mean this whole proof should have been
one single tactic but anyways uh so this
isn't quite showing off so okay so let's
do
case let's hope this works this
time
no inaccessible variables okay
interesting um okay well I guess what I
can do then is just split ifs I guess
that will do it that will do the trick
there we go okay well at least lean
wasn't too uh difficult with me there so
split ifs basically what it does is it
in your this is quite straightforward if
you have shockingly an if in your um in
in your goal in the goal that you want
to prove it splits it into multip it
splits all of the ifs adding the L the
if condition or its negation into your
context right and so basically split ifs
generates now two goals so I have the
goal the case where uh underscore 1 is
equal to Zer and I have the case where
underscore one is uh sorry is not equal
to zero right actually I think I need to
add some variables here so that is it
with uh okay yeah no so so now I've I've
bound this okay so I know this fact now
right uh and and so this is going to and
I should not have named it the same as
the previous H so let's call this uh
Hond
sorry uh okay and so now so now
basically I've split into the two cases
of whether I explor the loop the sorry
not the loop the if or not uh and uh
what do you call it um and and I'm going
to try and use this fact on my
verification condition so what I'm going
to do is I'm going to do simp using the
fact that I know the condition is true
at H oh
no that's going to automatically
simplify that down for me so so now
we've we're sort of we've eliminated
into the case where um where where sorry
the if is explored which makes things uh
fairly uh straightforward right and so
now I can actually rewrite with this
large expression here into my goal and
start trying to prove uh like try start
trying to straight forwardly prove
equality and hopefully some of my
automation will work otherwise this is
going to be a bit painful fingers
crossed uh so what I can do is basically
I rewrite backwards H into my
goal and so now I need to prove that
these two uh States these two final
states are equal and so hopefully
Constructor will help me
here nice it did good um or did it
actually no it did not okay huh great
um so okay let me just see what happens
if I try and simp this uh yeah okay um
um did that actually simplify anything
down I'm not sure uh okay well let's
just
try um maybe maybe this will actually be
helpful actually
here okay yeah so we broke down quite a
bit there but in particular I'm hoping
to use VAR
store uh clear VAR
store have the targets
and whoa I just eliminated one of my
goals so I've proven one of the cases uh
once again this whole thing should have
been one tactic so I'm not I'm not too
impressed with myself but anyways so
let's let's sort of indent that in uh
and actually I think I can probably
eliminate the seop I think just a clear
vastor will be able to do it so clear
vastor is basically a tactic which an
automation that thankfully worked unlike
some of the other automation but is is
an automation that is meant to
automatically deal with reasoning about
variable stores reassignments and these
sorts of things and so it
automatically uh deal with this sort of
jumble and figure out okay well if I'm
looking up account one in a state where
I've I've overwritten account two or
something like that since these two
things are not equal it's equivalent to
the original value of the variable these
sorts of things so it can automatically
discharge all of that and uh and handle
it and
then then we have the case where this
fails and once again well we're going to
just do this simplification
and you're going you you can probably
see that this is going to be really
straightforward by just sort of
rewriting backwards with h and and and
we're done there we go and so we have uh
and so on now what we've done is we've
proved that the verification oh and we
can now delete all of this mess at the
bottom and as I said really uh actually
there's this tactic called ESOP spec
which if you guys want to actually use
Clear uh this will work in the main of
the the repo this is just me breaking
things in the last moment so all of this
can be done with by doing these unfolds
and then just running ESOP spec which is
basically like a hammer automation that
just does like State like basically
massive State exploration and then
running clear vastor on the sort of
final States and that that clears out
this or would completely clear this out
automatically essentially so this should
have been done automatically it was not
apologies for that um so
so for for uh yeah so for ifs for fors
and for uh function bodies we will do uh
individual proofs essentially right um
so the the ifs is a little bit arbitrary
fours are of course required for like
this because Loop and variant are
generally undecidable so that requires
human interaction right the ifs are well
we found that there was a little bit
better scalability when we took this
approach practically speaking um and so
uh and and so yeah we would have to
write such a thing but obviously
typically speaking for uh such a simple
thing ESOP spec will deal with it in a
single go I promise you you can try it
on the repo um I just had to do this
manually because I as I said I was
messing with a lot of things this
morning and ended up breaking that so
yeah so now we've basically verified
that the verification condition implies
the spec right we can see that lean
tells us no goals here and then right at
the end lean has also generated this
other file that basically combines the
fact the proof that it's automatically
generated that the implementation
implies the verification condition and
and the human written proof that the
verification condition implies a spec to
be able to um to to be able to basically
it chains these proofs together to
basically show the implementation
implies a spec and Bob's your uncle
that's easy you've got a formally
verified smart contract right that's
kind of the idea uh once again as I said
there were some unexpected pain points
yeah and then basically you can sort of
bootstrap this up to the uh to to
transfer because this has taken a little
bit longer than expected because of the
broken automation so I'm actually going
to skip that part but what I do want to
emphasize is the uh the modularity a
little bit here right which is that so
I'm going to show you another example so
let me clear all of these things uh
clear no pun intended
um uh no well actually may as well save
that so I actually did some work there
um yeah why
not perfect so I'm going to show you
guys very quickly in my last 10 minutes
another example that I think really
emphas because this was like a
straightforward uh example to give you a
flavor of what's happening and as I said
it should have been a lot simpler um but
I want to show you an example of uh of
something of something that I think
maybe shows uh clears modularity a
little bit better right and it's it's a
Sim it's a s it's a simple I'm going to
say almost childish example example
but sorry but but it does emphasize this
point so here we have a broken proof for
whatever reason I'll Resort the file but
but the the yeah the proof itself
running once again doesn't doesn't
matter too much but we have here a very
we were talking about extensional
equality and we have here a very very
dumb implementation of the ad operation
in uh Ule right what it does is it wants
to add X to K and the way that it does
is it basically just Loops adding one to
K and subtracting one from K until K
hits zero right and the idea is at the
end of that you uh obviously you you
want to prove that um uh that you the
result Y is equal to X Plus K right and
this so this this is straightforward but
then I can write a function called uh
M right and M is a function that uh wait
no did it not oh great it opened it oh
God sorry one second
H this is working great okay so
m m is uh what you call it is is another
function which is defined in terms of
adk and it uses adk it repeatedly uses
adk to add uh uh so to well sorry to add
X to itself K times right so it adds it
starts off with some initial variable Y
and then it adds X to it k times and um
and and what and and the nice thing here
is that we have modularity so when I
actually want to reason about ad K I
don't need to unfold it and understand
hey what's the code here or have any
kind of model of it I I have this proof
that the implementation implies the
specification right and and clear
automatically knows this and can
automatically apply it there and so then
that massively simplifies the reasoning
about this call and then in turn MK can
be used to uh Implement an XK right
right an exponentiation operation which
once again sets some initial counter to
one and then multiplies it by XK times
using the m k function and once again I
can abstract that rather than having to
know its definition that it's a function
that calls another function in Loop uh I
I don't need any of that I just have the
spec right and it abstracts all of this
and so obviously these are very simple
examples but in complex software at
scale this uh massively helps formal
methods actually scale to being able to
verify complex properties over uh large
smart contracts and I mean the
particular applications that we have for
this is like verifying uh cryptography
like ZK verifiers and these sorts of
things where you actually need the
complicated facts that clear has access
to due to math lip to be able to verify
them okay cool so I I had another sort
of uh part to the tutorial which I'm
just going to completely skip but I will
quickly if I can find it yeah I'll
quickly go through yeah so I had the
running example um and yes so I'll
quickly talk to you in the the couple of
minutes I have left about well what is
uh what are the limitations and what's
the future work here right so obviously
one piece of future work is to unbreak
the changes I made this morning so
that's that's that's the number one
thing um the uh the the the sorry the IM
there are some immediate changes that
we're planning on making in the next
couple of weeks to make this more uh
easier these are what we call these
quality of life improvements because in
particular right now there are some
things which are sort of automatically
true in function specifications which we
don't derive and should be automatically
derived so for example when you call a
function you actually need to explicit
right now you need to explicitly write
and and clear that uh when I call that
function the only variables it
overwrites in the local scope are the
variables that are bound to the outputs
right and that should be completely
automatic and unfortunately that needs
to be written in the spec right now and
that's just a limitation well it's not a
limitation it's just it's it's not very
difficult to overcome I think will be
we'll be able to do it very quickly uh
there are also some um some some tactics
that we we're developing to being able
to De to deal with reasoning About
Storage right so storage is kind of a
complicated one because uh storage is
not actually storage maps are not
actually sound in reality right uh in
the sense that it it depends on uh the
catak map being injective and that's
true with very high probability but it's
not actually true true right and so to
be able to actually reason about these
things while injecting these assumptions
there is some like there is some like
reasoning about some what we call random
Oracle some random injective oracles
that needs to be done and so we're
writing some tactics to be able to do
that automatically because otherwise
right now reasoning About Storage uh
updates and these sorts of things is a
little bit painful but we're reducing it
to being a lot simpler and so well
hopefully just like earlier hopefully it
should be one tactic soon uh uh where as
I mentioned earlier we're trying to get
our evm model to uh pass 100% to get to
about 90% at this point in uh in time um
we're also we're also trying to and this
is something that sort of comes into the
whole
L2 uh sort of uh not well not only the
L2 thing but it it sort of is something
that I I most other solvers don't really
have an option for which is uh actually
we we can have this we want to add in a
most General client into this uh into
this model so this is a a way that we
can model external smart contract calls
that basically it just models an
arbitrary external smart contract as
some arbitrary contract that can call do
arbitrary calls back into my contract so
it's basically a a contract that can
make arbitrary random sequences of
finite sequences of calls back into my
contract and so that models all possible
re-entrancy attacks right and so we want
to be able to to to automatically to
have some integration of this model and
to be able to automatically then reason
about all possible re-entrancy attacks
which I think will be good uh the other
thing that we want to have is that well
lean has been working quite a bit
recently on um what do you call it on
integration with smt solvers which makes
things uh which makes some sort of
corner cases well makes a lot of
reasoning about like practical computer
implementation stuff like qualities of
bit vectors facts about bitwise
operations these sorts of things makes
it a lot easier right so in lean that
can be quite painful an smt solver can
just sort of hammer that away so we're
we're going to be integrating smt solver
using uh use to be able to make these
easier and then the the last thing is uh
is scaling because unfortunately so for
some fairly large arithmetic functions
that uh solidity will spit out we've
we're experiencing some sort of like um
time out issues with the proof
generation the verification condition
proof generation and so to actually get
around this we want to do basic what
we're calling chunking which is when we
have a very large function basically
just cutting it up automatically cutting
it up into smaller uh basic blocks and
reasoning about those and then composing
the the resulting verification
conditions automatically and that that
scales a lot better so that for to be
able to reason about sort of larger
amounts of Ule we want to do that uh
automatic and and there's also one thing
that is frustr okay I've got two minutes
left I think I'll manag to finish this
actually um one thing that's a bit
frustrating is that the saly Ule um what
do you call them optimizations are are
not the best and however much you want
to get it to eliminate the hundreds of
intermediate variables that it
introduces whatever you whatever set of
optimizations you use you won't fully
get it to do that and so what we also
want to do is introduce an extra step to
which which automatically applies a
bunch of simplifications to the code
like semantic preserving simplifications
that eliminate intermediate variables
and then automatically generate a proof
of equivalence between these two things
we've done this before not for solity
but we've done this for the Zur ml which
is an intermediate representation for ZK
circuits where there the compiler also
spits out a lot of intermediate uh
variables and these sorts of things and
we automatically eliminate them we also
do like lifetime analysis where we move
variables to the sort of the last point
at which they can be uh defined and all
of these sorts of things automatically
improve the equivalence to once again
simplify the resulting terms so yeah so
we've got all of these things in the
works coming in like the coming months
and uh so yeah so as you can see clear
is still quite uh experimental but I
think uh a few months from now we'll
have the evm model being completely con
conforming to the conformance tests and
we will have it scaling to sort of large
um large uh smart contracts and there
our primary goal at this point in time
is attacking a bunch of things for
actually like practical smart contract
uh developers that I think that
automated theorem proving can't really
uh attack which is essentially soady so
the soady library has so much uh
extremely optimized like inline assembly
Ule written into it and the thing is the
reason for the soundness of this these
operations although they're very
commonly used is not at all obvious it's
certainly not something that most
automated theorem provs seriously
approach and so we our goal will be
actually verifying some of these more
complex functions used by smart contract
developers to be able to I guess uh
provide some value to the community that
way great um okay so conclusions yeah I
mean I've basically gone through these
so clear powerful formal verification uh
formal verification framework for smart
contract ver like for for smart
contracts it allows you to M verify math
lip to have all of these complic ated
math facts at your fingertips uh so you
can verify ZK verifies complex numerical
estimators contract interactions rollups
Etc and clear is also powerfully
extensible I can write new automations
for it new uh new automations new um uh
like new predicates new theorems Etc to
be able to simplify its use and make it
easier for domain specific and general
purpose okay thank you so much for
listening
uh thank you julan for your work on uh
formal verification and uh developing
this framework so we have a few
questions from the audience and I'll
just quickly remind if you have more
questions please can and uh go to Mir
cut app for any questions so yeah uh
yeah so sorry is this is the oh sorry
you're going to read out go ahead go
ahead no no I'll let you okay okay so
the first question I'm guessing is can
you show us some example properties
you've proved in in the uh in your Ule
framework so I think so I I don't have
this immediately available but the most
complicated property that we've proven
is uh so uh many like like probably many
of you who are familiar with defi will
know about these sort of like
exponential estimators for like mapping
price ticks to prices right so you have
a tick which creates some spacing on a
price space right and you want to be
able to compute some based to the power
of this tick and you you want to
estimate an exponent like this
exponential curve except that's sort of
complicated in practice and so typically
this is done by basically breaking down
your tick doing a bit breakdown of your
tick and then multiplying together uh
the sort of the the sort of if you have
you know T like base to the power of t0
plus 2 * T1 that's the same thing as
doing like T to the power of T oh oh
base to the^ of t 0 times uh base squar
to the^ of T2 right and so essentially
you have uh uh what do you call it a
numerical estimator that uses this to
compute with very precisely an estimate
of this expon this exponential function
and we've actually formally verified
this and shown and and proven a formal
bound on the error um
okay uh next question how do you ensure
the correctness of the verification
condition generator that is how do you
guys ensure that the generation of the
Ule extraction plus VC proof from mule
does not miss any spec excellent
question so the so the the the obviously
the the Ule extraction itself is oh by
the way sorry I I have all of this time
to answer questions right or is this for
the next speaker okay okay okay it's all
for me okay good I was checking that I'm
not taking someone else's time um but
yeah so the uh so the the VC as we as we
saw basically clear has uh a Ule the Ule
syntax like embedded into it so checking
that it's actually fa F firstly I mean
it's literally copying a string but if
if you really don't check Trust that
part of it you can manually check hey is
this really copied and pasted from the
contract cool okay um and then actually
proving that the VC uh the verification
condition extracted well I I am certain
I'm as certain of this as I'm certain
that lean is sound because actually this
verification condition is is generated
by lean right so lean is the one that is
applying all of these simplification
tactics to generate this verification
condition so the VC itself doesn't
actually generate the verification
condition it just generates a proof that
then you gets lean that has a formal
model of of Ule that is checking this
against a formal model of of you all to
generate that verification condition for
me right and uh yeah okay cool can you
sh uh okay no uh that one I've already
answered are you able to use this now to
verify Enterprise grade evm contracts so
at this point in time the given the
scaling issues uh we wouldn't verify
like I I think it would be difficult to
verify a full complex def smart contract
end to end using this right uh and
actually what we're trying to do is we
we're looking at collaborations with
various other companies that do uh have
automated theorem proving based
techniques where actually we want to be
able to create Bridges with them um
where where essentially most of the
contract can be automatically verified
and then when you hit something
complicated like a numerical estimator
or something like that where automated
theorem proving is not really able to
reason about this to verify the
properties of this you can then extract
that out into clear and verify this
right so essentially the the way that we
see it at this point in time until until
we've gotten the scaling and the
simplification tactics uh to to be a bit
better uh at this point in time I think
it's more something that we would use to
verify the really complicated parts of a
smart contract right uh cool um II U I
don't know is that an acronym for
something that I'm not aware of
understand ah thank you if I understand
lean would allow you to reuse a state
value EGS Z as many times as you want
once it's introduced which isn't really
great are you able to use something like
linearity um okay that's I'm I'm not
entirely sure as to the motivation of
that question in that uh s0 here is a
symbol in the logic not a resource right
so the ReUse of it has no cost in a
sense right so if someone ask who asked
that question wants to clarify maybe a
bit more what they mean by
this I think you're getting a microphone
H was able to consume s0o to make a
claim about the resulting State and then
you if you try to do this again with
some other H in the same statement like
Ule isn't telling you that that some
stateful update it happened between that
it's kind of invalidated s0 is no longer
alive yeah so but s0 is the state at the
point in time it's never updated right
so s0 is always the state at the initial
moment in time it never changes so S9 is
the final State and then we introduce SS
Prime Etc if we want to reason about
intermediate right so there would be
never be a way in which another
function represented as a proposition
could take s0 as an argument I guess
that's what I mean is that yeah because
in my mind maybe s0 isn't alive anymore
like in the proceeding function call s0o
is now non-existent because it I I I see
what you mean in the sense that you want
to make sure that there is sort of
you're chaining the right states to get
right and this is this is done this is
sort of done by construction because
it's enforced by well hopefully the
semantics the ual semantics being
correct and changing the states around
correctly right but you're completely
right that it would be good to uh to be
able to make this clearer to the program
because I've certainly been like in the
middle of one of these proofs and being
like what the hell is s prime or S Prime
sub 2 you know or these sorts of things
so I think that that would be actually
pretty nice and in particular actually
um we're uh we're intending right now to
put on top of all of this uh something
called PRL so this is a probabilistic
relational logic which allows us to
verify cryptographic properties right
and in particular this actually has a
notion of a precondition and a
postcondition to this code rather than
just a relation and that precondition
can be updated over time time and then
you have basically you have rather your
notion of um uh you have a sort of a
temporal notion of state and you can
only refer to the state at the moment
before the piece of code you're
currently referring so so we are going
to be embedding a logic on top of this
to make this easy to make it clear or
what you're reasoning about and also be
able to reason about cryptography
probabilistically at the same time so
yeah uh but right now not so much yeah
uh cool
uh instead of writing the spec and the
proof and lean how about using some kind
of annotation for writing properties and
new solity in the matter in the manner
of liquid hascal yeah that's that's an
excellent an excellent idea and uh yeah
we we've actually been thinking about
this of basically creating a form of
like enriched okay I'm being told I have
very little time yeah two two minutes I
can answer yeah I'll finish this we have
a little more time so please just
five okay I have a little more time oh
okay okay well then uh you guys are
stock here sorry I'm I'm just going to
keep labing on um but uh yeah so we've
actually been thinking about this of
allowing basically a sort of like Rich
solidity where you can as you're um as
you're sort of developing your smart
contract you can insert function pre and
post conditions you can insert Loop
invariance and then then those are
automatically extracted by clear into
lean for us and then we can try and
prove them right uh and use our
automation to prove them and I I think
that actually this is a great idea
because at this point in time I feel
like developers and you know you guys
probably will know more about this than
me but I feel like developers uh feel
like you know formal verification is
this weird thing out there that they
know nothing about and at at best uh you
know they think oh maybe this will help
me out at worst they see it as a
hindrance to the sort of iterative
process of development right and I think
that actually by allowing by having a
sort of an an Rich solidity which has
these annotations actually we can make
this feedback loop with developers a lot
tighter and feel like they're integrated
into the process and understand a bit
better
what are the things that we're proving
rather than me just have it throwing
large equations at them and saying hey
this is totally the spec that you want
you know um so
yeah uh so uh so the okay so can lean
generate counter examples when the spec
isn't fored maybe via smt so at this
point in time so at this point in time
clear can't do this lean does actually
have this smt lean uh interface which
which I think does counter example
extraction and so in the future we we're
intending to integrate smt lean into
this to be able to deal with these side
cases and so I'm I'm hoping that in the
future we will also be able to extract
counter examples yes
um ah good that's a great question how
difficult would it be to use the evm
lean models to build cert verified
certified compilers for the evm great
question I love it um so we're actually
planning on bu because thing is part of
all part of the trust base and I didn't
mention this for all of clear is well
like clear is trusting that you're your
compiler actually compiles this down to
an evm smart contract correctly and
obviously there are typically a lot of
optimization steps Etc involved in that
process and a lot of things can go wrong
in that time right so oh by the way do
tell me when I'm out of time because
yeah um and a lot of things can go wrong
in that process and so uh I I do think
that uh you know I think it's important
to have a u TVM a verified U TVM
compiler this can be done in in lean I
think actually fairly straightforwardly
but there's a difference so there's a
difference between writing a Ule a u to
to evm compiler and lean that's verified
and a good uul to lean comp or an
optimizing U to evm compiler that's
verified right and so the form I think
will be very easy uh the and then we can
also put in sort of harnesses to add
optimization steps and then potentially
people can then prove those
optimizations correct in lean once again
um but but that that obviously having a
good set of optimizations and fully
understanding how they interact and that
each one of them are individually
semantics preserved and can be quite
complicated and can be quite
timeconsuming Tas but the first step of
having a compiler that's verified I
think will be relatively straightforward
right with respect to some notion of
like storage equality so when you
execute the Ule program versus the evm
program the uh in the same state the
resulting storage state will be the same
and return values will be the same
is that it okay thank you very much for
your talk
cheers so let's take a break and we're
going to resume our session at 1250
we're going to talk about the toolbox
for manuring the health of the ethereum
P2P
Network for
person
t
okay uh thank you everyone for joining
us uh today so next talk is about a
toolbox for monitoring the health of the
ethereum P2P Network and please give a
big Applause to our speaker
yanes hi everyone welcome uh I Janis I
represent the pro blob team and uh today
I'm going to talk about a set of tools
that we have built to monitor the health
of the ethereum peer-to-peer
network uh why we're doing this um
because we believe that things generally
might be working but not necessarily in
ways um in the way that we think they do
so we think that we should generally be
looking deeper into um how things are
working and we argue that the
peer-to-peer layer of the um of the web
received a lot less attention than it
should have there's a ton of onchain
metrics and dashboards but very little
has been done on the peer-to-peer layer
which is under everything uh under
everything else so we argue that if the
great stuff that people are building and
presenting is just going to come
crushing
down so um what if I had to say in one
sentence what we're doing is that we're
carrying out rigorous measurements on
the peer-to-peer protocol stock in order
to make the network layer better faster
and
safer uh and we think that's what is
needed in order to guarantee a robust
layer below um all of the other stuff
that is building on
top now over the years we have built a
set of tools uh starting from more uh
kind of high level topology and network
structure um items and going deeper into
critical components monitoring and um uh
uptime monitoring and so on and then
going deeper into more detailed and
sophisticated things like uh data
availability challenges that the
community is uh trying to overcome at
this point uh I'm obviously not going to
cover everything uh but just going to
focus on a few of those um tools to go
through and let you you know give you an
idea of what they are and the related uh
pointers so starting with network
topology you might have heard of or used
the nebula crawler which is a very
well-known crawler by at this uh by this
point uh it started off as uh a crawler
for the ipfs network but has now uh
expanded and supports many other lip2p
based networks but also dis V4 and dis
V5 networks such as the ethereum
consensus and execution layer uh the uh
one thing that makes uh nebula uh um you
know come apart is that it's not only
crawling the network it's also
monitoring the liveness of node so it's
going and you know um crawling networks
finding peers and then pinging them
every so often after a while um like
continuously and therefore we can find
things like uh pen and so
on so uh let's start with a quiz to see
what we can find out um from uh from
things like a simple crawler um and uh
all of the other things are built on top
so which one uh which ethereum consensus
layer client do you think is um least
dependent on centralized Cloud
infrastructure yeah
others okay that was correct actually
the last one Nimbus is the one um well
done to to the team so uh if we if we
see so at the top here it's not shown
very well but it's Lighthouse prism um
and load start and at the bottom is
Techo grandine and Nimbus so if you see
it in terms of percentages obviously
Nimbus is uh the least dependent but of
course it's not the most popular uh
client so it depends a little bit on how
you how you do it the the the blue line
here is the data center those that are
deployed in data centers and the orange
one is those that are um have got custom
deployments
um so you can find other things like
what's the most popular chain on uh
optimism any ideas
anyone sorry B
no this is a pretty recent result and we
found that is actually uni chain um by
far uh so yeah this is pretty recent if
you if you think um we're missing
something or or not we can uh come talk
to us we can we can argue and uh have
another look later uh to figure out if
we're correct or not um so yeah this is
uh these these are things that you can
uh figure out if you look a little bit
deeper into the network uh and that's
what we are uh we're actually doing so
carrying on again on the network
topology we have recently uh built a
tool called ants um which uh you know
like ants when you release them and when
they they are they're covering um a big
footprint so what we're doing is that we
want to release ants in um DHD
structures so that uh they can monitor
specific things specifically DHD client
requests um so we we spread ANS um on
every approximately every 20 DHT uh
server nodes and that way we're able to
gather information from all the requests
from the network the two is automat
automatically adjusting so if the
network size doubles then the number of
of ANS that are going to be out in the
network is also going to double and
we're currently uh supporting the
Celestia network but soon uh there they
going to be more so briefly how it works
is that you see uh we we can assume this
is the DHD key space uh these are reg
regular DHD server nodes uh the green
ones are uh the ons that we are putting
in the network uh as I said roughly
every 20 DHD server nodes and therefore
then what happens is that when a DHD
client comes in uh in order to do
several processes that he needs in the
network uh among others uh update its
routing table it's going to ask other
nodes around so we want to make sure
that one of these green nodes is among
the 20 um peers in the network where the
DHT request is going to end up through
so in that way we're kind of uh it's
hanot of sorts that is gathering
requests um now with this uh as I said
it was uh great to see how you know we
were able to figure out what's the light
node population in the Celestia Network
um we don't have results yet but it's
soon going to be on pro.
iO so if you
want to um know more about that that's
that's the the thing to monitor or you
can come talk to us afterwards um now
going into protocol performance um we
have recently built a tool called Herms
which is basically a gossip sub listen
listener and tracer
uh the measurement goals of building
that was to figure out metrics related
to message propagation latency number of
D um messages that a node is receiving
um the validator node bandwidth
consumption and several others so in
doing that we didn't want to run a full
ethereum node for several reasons what
we instead wanted to do is have a
lightweight lip P2P host which would
spin up uh establish connections stay
connected and then participate in the
network in this
way um it's tracing Herms is tracing all
of the events so from the lip2p host
events like connections and
disconnections to gossip sub Trace
events which were of particular interest
to us uh like grafts and prunes and like
in the off nodes in their local mesh
Network subscriptions I have and I want
messages for the gossiping function of
the protocol and then go deeper into
peer scoring and and things like that so
we were able to to gather all of these
data and uh this helped us look into
lots of um important metrics for the
network for uh a protocol for gossip sub
that is very critical right it's uh as
you might know it's transferring blocks
and messages um in the ethereum
blockchain and other blockchains as
well uh this is roughly what what the
architecture looks like but I'm not not
going to stay in in this slide because
uh that's just one way of of doing it
there might be several others and even
this might evolve over time but this is
what we used uh for the um for deploying
Herms on um on the ethereum
network now um briefly some results so
um we wanted to see the number of
duplicate messages and in this plot
there you see the number of duplicate
messages on the x-axis so it goes from 0
to 10 and the message ID the CDF uh of
messages on the y axis
so if you um if you look at the green
line it's representing the blocks topic
um sorry the blob topic and we see for
example that around
delivered to the same node four times or
less so on the one hand you know we like
seeing this result one might say four
times is is quite a lot uh on the other
hand you know we we should not expect
have you know zero duplicates because
this is not a client server architecture
here it's a p-to-p network and having
duplicates in many cases um helps in in
in case for example of an attack where
someone is trying to delay delivering
messages or eclipsing a node uh so it's
good to have some duplication but we're
seeing that as you know uh when we're
going to six or eight duplicates per
message that might be a little bit too
much so um we we figured out that things
are working well well but there is still
some space uh for
optimization um on another bandwidth
related um metric that we've seen this
is um on the on the x-axis of the uh
message types um and on the Y AIS is the
percentage in terms of um kilobytes from
the total and we we found out that I
have messages represent
uh which is quite a lot and there might
be again some of it is expected but um
there is clearly some space for
optimization um you'll find all of the
reports that we've done on E research uh
if you go it's uh all of these studies
you can scan them but also under the
networking category um they're pretty
recent the last few few months so you
can uh take the full picture of all the
things that we've uh managed to um to
find
um now moving on uh to another um to
another tool that we have uh recently
built it's called ukla Uh a network
bandwidth monitor uh we might have to
change the name but uh that's what we
have for now uh so the methodology is
that um we we as we run nebula and we
have a list of online peers we then
deploy Herms and try to connect to those
peers and keep uh stable connections and
then eventually we're trying to download
the carefully chosen volume of data from
each node so that on the one hand we do
not
overload um the node that has got other
things to do like these are main nodes
that are uh doing their thing and at the
same time we we are able to kind of
momentarily saturate the bandwidth of
the node so that we know how much
bandwidth uh they've got available um
we're seeing in this in this graph here
on the uh on the ex axis is the the slot
duration from 0 seconds to 12 and on the
Y AIS is the bandwidth in megabits per
second so interestingly we're seeing
that there are some uh like deeps in the
um bandwidth availability the Blue Line
especially for um the blue line which
represents Cloud nodes um whereas the
the orange one is for not non-cloud
nodes so seeing these dips there means
that there is a little bit of extra
bandwidth availability uh which could be
very interesting for engineering teams
if they want to for example push some
more data out during some particular you
know time within the slot then this
could be chosen um and this this I
believe it's going to become very
helpful as um you know as we're going
towards piras and the blob count
increase and all of those challenges
where you know it's not exactly clear
where bandwidth availability can come
from in order to to accommodate um quite
a few tools we've uh covered uh some of
them only and again we're going from um
networ a number of years now so we have
a kind of data warehouse of sorts which
we want um to make available to the
community so we're building an API um we
know that other um other teams are
interested to get the data and deploy
into their own models to do energy
sustainability metrics and risk modeling
and and things like that so this is
under active development right now uh we
want to integrate more networks um as
you know with some of them on the
pipeline already uh we want to repeat a
nut troversial study that we have done a
few years ago on Li P2P to uh figure out
the capability of the nut hole punching
component and then um more generally
focus on the challenges to deal with
date availability assembling on ethereum
and other networks so if you head to
pro.
you're going to find out weekly
reports for uh that the uh the networks
that we're currently monitoring uh
you're going to find other reports like
like blog propagation latency for the
ethereum network and then uh links from
there to our methodology and all of the
tooling um yeah and as I mentioned of
course some of the results St studies uh
results of the studies are on E research
um yeah and prob.
network has got some
more information about uh our team um
yeah and now thank you very much I'll
now pass it to on to Dennis to do uh a
little demo of one of the tools the the
bandwidth measurement monitoring tool to
see what band looks like uh on this uh
Wednesday
afternoon all right hi everyone my name
is Dennis I'm also from the pro blab
team okay
yeah all
right can you see my screen yeah there
we go
okay it's loading sorry ah here we go
cool so Jan's introduced you to ukla
already and to spice it up a little bit
I wanted to try uh a demo to show what
the data looks like that we gather um I
mean this data won't be representative
of cors because we're running it from
this uh Convention Center Wi-Fi um but
still I think it should be interesting
to you uh to see what data we We Gather
so if we run ukla uh this is our
bandwidth measurement tool as you have
heard uh you you can pass in a you um
command line parameters for example in
this case we query 10 peers from our
nebula database which are peers that are
online in the uh ethereum Network we
request from each of these 10 Piers two
blocks and if it fails we do three
retries and because we are running quite
a few of these um ukla runs every day um
you can also give it a tag from where
you have run it for example we are
currently running it from us East one
but you could Als in AWS but you can
also run it from different uh ge
locations for example and I just give it
a attack of lip oh of Defcon day Defcon
demo or let's leave it lip for now um so
right now okay of course the demo
demons it's always the same
sorry so we are running um a full prism
note in the uh on one of our in
instances in the cloud and Herms as you
have known is part of of ukla which is
running underneath um so which we build
upon it needs to connect to one of these
full notes uh so I'm just forwarding the
port here let's try it
again so it's launching the Herms note
and I want to emphasize Herms is um
quite modular so if you require for your
networks for example bandwidth
measurements Herms could be extended uh
to also work for your for your network
if you have bandwidth measurement
requirements so let's
see
okay so basically what it does I can
talk talk over it um it will yeah it
will basically just connect to the notes
download the blocks and maybe in the
meantime I have only two minutes left I
have run it earlier so we might take be
able to take a look
at okay it's all not working of
course so meantime just yeah I encourage
the audience to connect to Mir cut app
and you can ask questions
hang
on let's see
okay I hoped it would work on and I I
practiced a lot of course it's not
working let's let's try it again okay
may maybe you can ask questions and I
try to run it in the
meantime yeah
you will answer the questions yeah so um
ah here we go it's working so it's it's
it's connecting to notes downloading yes
thank you very
much so it's now connecting to notes
downloading blocks and um measuring the
bandwidth that these nodes have
available to get um a distribution of
what bandwidth is available in the
ethereum network which then would inform
protocol decisions around um for example
data availability samp or block sizes
that we could um increase to some
certain degree uh and so on um The Next
Step would have been that we look into
the database but it looks like my
computer's Frozen here so maybe you
should maybe that's already enough to
Showcase that it's working for now and
maybe go on with some
questions thank
you okay yeah we have a first question
and how many noes do you need to run
yourself to get a complete picture of
network uh okay I I don't know for uh uh
a complete picture of the network I
guess is that for the ANS if
uh complete picture of the for the for
which tool basically I don't that's why
I don't yeah if the person is in the
audience okay so can you pass the
micro thank you yeah I was just
wondering more in general terms for all
the tools everything to get all the data
you need like besides the crawler for
ANS or for anything like that how many
noes you run yourself in order to get
access to the network and data or can
you just use public nodes and connect to
that right so um it depends on the tools
like uh we we do have uh for example the
nebula CER is running 24/7 for from um
uh for several networks we have some
other tools like um to monitor the DHD
lookup time of the um ipfs DHD uh Amino
DHD and that is running from several
locations from Seven locations around
the globe I think again running
uh the question for for the ANS
architecture in particular for the
Celestia Network we're running something
between five and seven nodes I think it
doesn't it doesn't need more because it
can cover more space
yeah yeah that makes sense thank you
much yeah uh
let's let's let's go through a couple
more questions and then return to the
demo yeah cool so um can I run these
tools within crosis local networks I
guess the answer is yes
here depend so I'm not familiar with
kosis and the networking set that that
it's using um
uh hey uh yeah you can configure ketosis
so that it exposes the ports outside of
just the network that in Docker uh so it
essentially exposes it on the host yeah
uh and then yeah all of the stack will
work yeah I think another interesting
question is if these tools can be used
in a customly P2P Network the second
question yeah generally the answer is
yes uh it's not um as like most of the
tools that we're building are for lipit
be based networks uh so it's going to be
a lot easier than building a new tool
from scratch uh that being said uh some
things depend on like the the network
characteristics and how the whole um you
know protocol is uh is set up uh it's
not a matter of just changing one
parameter and adjusting to another
network but we have done I think a very
careful job of making it easy to
integrate more
networks okay and one more question what
stops someone from using Uka to grieve
network uh which one ah first one yeah
um the right now it's not open source I
think that's easiest answer that's how
we stop yeah U okay I think we don't
have much time uh left so let's just
transition back to the demo yeah I just
want to briefly
show the data that we it's a good
question though this one because we are
planning to make it up and source so
we'll think about Okay cool so you can
see database uh so as you've just seen
uh it has run and you can see that um
there are two studies now because I ran
it right before the talk and it was
working and uh so the second one here is
the second study that we just started
here you can see the tag that we gave uh
to it and then each connection to the to
an ethereum node
um results in a visit in the bandwidth
visits how how we call it here and um
yeah here you can see all the data that
we gather here so how um in which time
of the slot did we request the data so
you can imagine that in different times
of the slot the bandwidth might differ
because you have to to do other duties
here um if the connection was successful
which blocks we requested from that
other node um the um the compressed
number of bytes but also the
uncompressed number of bytes the bites
that that we sent over the wire so with
all the uh enveloping and so on and how
long it took and then the resulting
megabytes uh per second and and yeah the
round round time and how many retries we
needed and so this goes even Beyond just
the plain bandwidth me measurements um
yeah so there's even more data that we
can use to inform protocol decisions for
example which is one of our main goals
so thank you okay okay thank you and
yanis if you want to say some uh last
remarks uh uh no yeah okay thank you
thank you very much thank you danis and
yanis for amazing tool to analyze the pp
Network I think now is time for lunch
break and we're going to resume this uh
uh sessions at uh
sorry and we're going to discuss about
security of fire Shamir
commission thank you thank
you thank you everyone yeah so nice
I did take get there
d
a for
up
h
like this yeah
testing testing one
everybody my name is Marcus I'm a metag
governance Steward at Yow and I'm the
backup MC for today so uh today we're
going to be talking about
uh
interactive operations and transforming
that into non-interactive operations
using the uh Shamir
transformation I'm not a cryptographic
researcher by the way so I'm trying my
best thanks anyway um I'd like to
introduce our speaker today his name is
mial he's flown all the way from Poland
about a 17-hour trip so why don't you
give a round of applause to mial
[Applause]
how many P you have there's like
five does it work okay perfect yeah um
hello uh thanks for inviting me to
talking today uh so my talk is about the
security of fat Shamir transformation so
basically uh the security of the trans
information that allows you to use all
these snarks Starks on chain as non-
interactive proof instead of having them
like as a communication between prover
and verifier okay so uh before we dive
in uh let's talk very briefly about uh
zero knowledge proofs so in in zero
knowledge proofs we usually have this
these two parties prover and verifier
the the prover wants to convince the
verifier about veracity of some some
particular statement uh formally we we
want to say that particular statement
belongs to some predefined language but
we don't need to to go into such details
now um so in improver has like two two
uh two inputs one is the statement that
it wants to to prove and another is
witness so so for example
um like um when when you have have
uh the statement could be like a circuit
C uh executed on some input a evaluates
to B uh and witness could be like all
the the values from from this ciruit
from very bottom uh to the top and right
it should end with with b um so in zero
knowledge proofs we don't give the the
verifier the the full knowledge of of
this circuit we only give the the
statement uh the statement of of of the
prover this also comes from the fact
that usually we can write statements uh
in a much shorter way than uh than
Witnesses so uh from zero knowledge
proofs we require um basically three
properties the first one is completeness
so we want to say that if both prover
and verifier are honest then prover will
be able to to convince the the verifier
about the veracity of the statement uh
another uh which I claim is like
probably the most important one is
soundness so uh so here we want to say
that if the prover is is malicious and
the statement is incorrect then the
probability that the verifier will
accept such U such statement is is
negligible um the different flavor of
sound is knowledge soundness and this is
what we usually
use and this is like a stronger notion
of soundness so here if uh if verifier
accepts the proof then we know that the
prover knows the witness and finally we
have zero knowledge that we really don't
use in blockchain applications at least
now so so here we we say that protocol
is zero knowledge if if the verifier
learns nothing about
about the witness from from the uh from
this communication with the with the
prover okay so like let's talk about how
snarks are built so um sorry for for for
this like very theoretical slide there
will be few of them here um so Starks
and snarks start as a u interactive
proof uh between like this prover and
verifier uh so we design our snarks as
protocols where the prover send some
some polom to um to to to like some
imaginary party called called
oracles these
polinomial um for example represent like
very big computation so so these
polinomial are are
huge
um when these polinomial are sent the
verifier also replies with some some
challenges that also provides some
information to the prover how these
polinomial should be
built uh eventually the the verifier
asks this Oracle that got all these
polinomial to evaluate these pooms for
them so it picks some evaluation point
and gets the gets the
evaluations so finally the the proof is
like the set of all these pols sent by
by the prover uh along with all
challenges that the verifier sent
evaluation point and the evaluation at
the of the polinomial at evaluation
point so uh there are a few problems
with this approach uh Nam well like all
is like this imaginary party that really
doesn't exist in real life and like
since these polinomial represent all
this computation they are
huge so we don't want that so we need to
to make like a Next Step so for next
step we use something called polinomial
commitments which basically allowed the
theover to send like a short digest that
represents the polinomial instead the
polom and importantly the verifier can
Al can can also evaluate this this
polinomial by sending like the
evaluation point to the pr such that
this uh evaluation can be verified
so so now we can replace our Oracle just
by using the uh polinomial
commitments and that also makes our
proof uh much shorter right because
instead of full polinomial we send this
this very short digests so now the
communication looks like we have a
prover that sends some polinomial
commitments and verifier that replies
with with these random challenges
eventually replies with some evaluation
point and get evaluation of the pols
along with proofs that the
evaluations have been computed
correctly so now like uh okay this is
still U not great because uh we we have
this interaction between the prover and
the verifier so what we do is we
introduce a random
Oracle So Random Oracle is like another
imaginary entity that is is uh it's a
random function that on on input
provides some some random
answer so now this this function is used
to to compute all the challenges that
the verifier would compute
itself so um now the nice thing is that
uh the prover doesn't need to uh to talk
constantly with the verifier because it
will send something called like partial
transcript so so it uh it computes this
polinomial commitments send them to to
to the random Oracle gets a reply
includes the reply in the further
computation computes new polinomial new
polinomial commitments sends them back
to the random Oracle back and forth
finally it is able to to produce like a
single proof for that can be presented
to the
verifier and similarly the the verifier
itself self has access to this random
Oracle so can produce the um can produce
the the the challenges on on its
own so so now like the proof is like all
these polinomial commitments that that
the pro sent they are like included in
this proof along with with the
challenges from from the random Oracle
um evaluations of the polinomial and
proofs for for the evaluation
correctness yeah so so the problem with
random Oracle is that well it doesn't
exist so what we usually do is like we
say okay uh instead of random Oracle
let's use hush
function uh so now the question is like
how secure is is such such
protocol so now we are going to the
core um so the the think with
um the thing with uh using hush function
and like random Oracle as well is that
we change a bit the game that we are
playing with the with the approver so
like the verifier now is in a bit
different
situation uh than it was before why is
that because when we have like an
interaction between the prover and
verifier in the interactive proof and
the verifier realizes that uh that the
Prov is like incorrect like uh tries to
to to to claim something something
something wrong or like some of the
answers of the of the approver uh don't
make sense then it can always interrupt
the the
communication so we can think that the
communication goes as long as a prover
makes a mistake this malicious
prover
however um in the case when we have like
a Fatam transformation
the situation for malicious prover is
much better because now the prover since
it computes the uh it computes the
challenges that verifier sends on its
own he can uh predict like I mean by
doing computation he can see whether he
can answer these challenges or not and
if he uh sees like a challenge that he
cannot answer he can just rewind the
computation right to the very beginning
uh try to send like different polinomial
and can try locally computer proof that
that would fit
it uh so so here we have uh a notion of
of a lucky
set so basically we can say that some of
the challenges that um that the verifier
sense may be particularly good for a
malicious malicious Prov
um so maybe
for uh for for for those who are uh
interested in in
MAF um I can add that we usually want to
have some polinomial to be equal each
other so I I had an example like few
slides back let me go here here we have
this m1x * m2x = m3x
okay uh as I mention like this are huge
we don't want to S send
them on the other hand we can verify
this statement by evaluating the
polinomial at random
Point why is that because like the
probability that
the uh that this this
later later equation holds when the
first line doesn't is like really
negligible uh and it depends on the
degree of the polinomial and the the the
size of of the
field let me go back here yeah and and
here we have also like similar situation
right if the the malicious Prov is lucky
and it comes to to a challenge Z this
evaluation challenge Z such that well
even though these polinomial are not
equal each other uh but they are equal
on on
Z then uh then yeah that's that's a very
good situation for the
prover uh and with nonactive proofs the
the the the prover can just like try
multiple times right if we have like
interactive proof
then when well when if I would talk with
a verifier that constantly gives me like
a some bad answers I would just
interrupt connection
so how how to compare the the security
uh of of interactive and non-interactive
proofs so
now
um we need to to say okay so uh our
starting point is like saying what's the
probability that an interactive protocol
would be broken
and this is uh say some probability some
probability Alpha okay uh then uh we we
check like the probability that one of
the answers uh from from the ROM Oracle
from the hash function will be uh from
from this lucky set where where the
prover can provide a a good proof for
for a false
statement uh finally we need to include
the computational power of the of the
malicious prover right because if the
prover is like more powerful then it can
include like much more uh they can do
like much more
trials um not going into the formulas uh
but let me let me only say that that the
the security of uh the the security loss
of Fatam transformation is roughly like
this ITA time Q so so the the
probability uh that the adversary gets a
challenge from the lucky Set uh
times times the the power of the of the
adversary okay so um how how does it
affect
security so let's assume that our
starting point for the interactive
protocol is like uh 2 to the minus 100
right so so we calculated that uh an
adversary in the interactive protocol
who wants to to to break the
protocol has probability 2 to the minus
what is the realistic cue it's it
depends on the adversary right but if
you want to be uh
relatively uh pessimistic um I would say
okay let let's see like what's the
computational power of we have like
right now like uh here I looked at uh
Bitcoin network but it's like it's a bit
outdated data but like uh you know like
the computational power of world like uh
grows like immensely because of all the
uh of this AI related things uh also
like Bitcoin at $100,000 as well uh so
so the disc compal power is like pretty
pretty pretty
amazing and the result we have is that
we have like roughly like 2 to the 85
hashes per day that's how much we can
compute what does it mean it means
that um it means that the the the
probability that this network breaks the
uh breaks the security is is no longer
like the 2 to the minus 100 is 2 to
Theus 15 so um
if it's like big or or small I would say
it's like the probability is relatively
big especially that the compute grows
and you don't want to to change the
parameters of the proof system all the
time okay so one thing that is U often
used in modern snarks are small
Fields so in small fields
uh the challenges from the verifier come
from like very small uh set that also
makes uh
the uh that also makes the the the the
Prov uh much more capable of of guessing
the guessing the challenge or um being
Lucky in in having like a good challenge
and there are basically two ways of
dealing with this problem so first of
all what um I I I hope all Protocols are
doing is that they don't pull the
challenges from from these small Fields
but use some field
extensions but now I would like to talk
about uh parallel repetition because
this is also like technique that uh
works very nicely in interactive proofs
but is totally insecure in terms of
non-interactive
proofs so parallel repetition basically
says okay I'm as approver will uh so the
prover and verifier run two verification
protocols in parallel so there are like
two copies of the prover two copies of
the verifier for the prover to accept
the proof both uh both executions need
to be correct both executions needs to
be acceptable and when we have
interactive proof systems that gives us
like super nice property because like
the the probability uh here like denoted
by Epsilon 2 that that the verifier
breaks both uh both executions is like
yeah Epsilon squar so so it's like we
had like I don't know 2 to Theus 32
another 2 to Theus 32 it's 2us 64 but
for fat Shamir transformation this this
parallel repetition uh doesn't work at
all so so the thing is
that uh yeah I don't have time to to go
into details unfortunately so um but we
I'm very happy to talk about this uh
later um so so the the the main point is
that the the adversary can can partially
solve like one transcript and partially
solve like another transcript so the
more par repetitions we have then there
was this security loss it
becomes um okay so and there's more
about Fatam
transformation so uh it's easy to
implemented incorrectly so that many
attacks shows that uh so there's like
was a big uh big problem with uh uh with
plon uh because like some some some uh
teams didn't Implement that the final uh
final hushing uh that was discovered by
trail of
bits um and also uh yeah like it's very
important like when we have like a f
Shamir not to deviate from protocol
description so like the message I want
to say uh in this talk is that yeah we
need to use katamu
transformation but we need to be aware
uh that it comes with some security
losses and there is a cost um that that
we need to pay uh so we cannot be too uh
too aggressive on our par security
parameters that we pick and we need to
pick them wisely
thank you Mahal thank you so much you
can never be too careful you can never
be too
sure um everyone a round of applause for
mial
please that was a lot sir thank you very
much so uh we have a couple minutes for
questions now uh I'm going to point your
attention to the screen here at this QR
code so if you have questions for mial
uh just scan a QR code it'll uh open up
the mircat app app and you can start uh
plugging your questions in there
um the questions will appear on my
mobile and uh I will probably just read
the questions to Mahal if that's okay
with you and uh he'll feel happy to
answer
it yeah oh I see I see okay okay go for
it uh so why paral repetition fails um
so the thing is that
when we have like multiple uh copies of
protocol uh parallel repetition says
that we need to be successful in each of
them right when we have fat Shamu
transformation and we have this lucky
sets um so let me um repeat what lucky
set is like luy set is like
the it's a set of challenges such that
if the verifier gets a challenge for the
from that particular set then uh the
verifier is like of the hook so he can
compute the rest of the proof such that
it will be um it will be accepted by the
prover so the problem with that is that
the the the prover can in parallel
repetition can like focus on the first
transcript try to get into the lucky set
okay which it will come with some
probability because like as as we assume
that that the uh fields are small that
okay so that the prover knows that in
the in the first track it was successful
on other tracks on other uh executions
and do the same trick So like um so so
the thing is that uh when the the prover
is say successful in the first execution
he doesn't need to prove he doesn't need
to care about this execution anymore he
can go to the other um
uh and this uh this when when we analyze
that the probability of the adversary
successful in terms out that the the
security is like much much worse
when compared to this Epsilon squared
I'm happy to like discuss in more
details later uh which concrete property
should a concrete has function
satisfy
um so the thing is that uh as
cryptograph first Define has function um
you know like we need this U this the
Collision resistance this is basically
the the property however we know that
there are hash functions that have this
property of collision
resistance but uh but are insecure when
we try to instantiate like has function
with that so so the the thing is that um
and there is analysis but all these hash
functions that are insecure for fat
Shamir are like some um not natural
examples they are not like sha or ketak
or something they're like hash functions
that were designed to be like insecure
for fat Shamir uh I don't recall
correctly like what's the property uh of
of the hash function that it need to
have to to be um useful for fat Shamir
transformation um but if you take any
reasonable uh hush function it should be
good uh
very CH section on small Fields uh
pulling from extensions yes so uh so so
thing like uh I don't know meren Prime
field it has like roughly like two to
the 32 elements so this is like a very
small field um so instead of of using
this as a
challenge you you take a challenge being
a polinomial the of uh of degree one um
over like the say f squar like where the
f is the um with where f is this this
this meren Prime right so so you don't
take
uh you don't take like a single element
but you take like a pair of elements or
a triples of of
elements one more
question yeah uh one more uh no I think
I answered all I probably
not um
sorry maybe there's something like in
below but I don't see
it uh ah s Sigma
protocol
um I will need some time to process it I
think can me change you have a maybe a
minute okay so so sorry let let me take
is uh offline um maybe I will be able to
quickly answer the quantum security uh
fat like Quantum security and fat
Transformations are orthogonal problems
uh there's no reason for to to believe
that fat Shamir transformation is
insecure in the
quantum great okay awesome thank you m
appreciate it Round of Applause from M
everybody yes sir
great uh we'll resume the session in a
couple minutes feel free to hang out
speee
we Che picture
but yes with uh this one is for to the
I'll look at the okay cool I can
see be
more so we
nothing you
I don't even know
you guys talking
about Australia
I just wanted
okay we are back for those who are new
in the room I'd just like to reintroduce
myself my name is Marcus I'm a meta
governance Steward at ow and we have two
speakers today that are going to be
talking about ZK
passports um we have Theo from uh France
but he flew in from Lisbon 16-hour
flight whoa anyone flew more than that
more than 16 hours how much did you
fly wow dude dude congrats to you that's
amaz that's
crazy um so Theo you flew flew in from
Lisbon come on stage really
quickly okay give me a fun fact about
you just really quickly fun fact
yeah uh do I sound French actually when
I speak absolutely not there you go
that's the fun fact the fr the Frenchman
that does not sound that he's from
France okay awesome give it stay on
stage okay Round of Applause for Thea
everybody great and uh we have Michael
from Perth 5H hour trip you're lucky
yeah it was quite short for a change
usually it's like 20 plus hours like I'm
relate with this guy over here 30 hours
that's rough and a quick fun fact about
you sir yeah actually this a fun really
good fact um so black swans as a like
Black Swan event they're actually from
Perth Australia originally that's where
they they came from nice yeah perfect
okay beautiful all right everybody round
of applause for Theon Michael
go
it all
right all right there we go now it's uh
another Globe spinning very cool took me
hours to make that so I wanted to make
sure you guys saw it um yeah hey
everyone really great to be here I'm
excited to talk about what it is we're
building I'm Michael Elliot from yeah
and I'm d as introduced from obviously
we just got introduced so need for that
again um yeah we're looking forward to
to going through uh what is we're
building and uh the tech involved and
explaining you how we built it and also
uh why we built
it
so I'm pretty sure everyone in this room
is quite familiar uh with the fact that
online identity
sucks I think everyone here has had the
experience of um taking a photograph of
your past port and sending it off to
some service for for kyc
verification um you know that you get to
basically trust them to keep that data
safe uh hint they won't there's been you
know many many um hacks and data leaks
uh throughout recent years that just
demonstrates that it's you know very
difficult for companies to keep that
kind of data um
secure and this inevitably leads to yeah
theft and uh uh identity theft and fraud
and another downside of this is that you
can't bring it
onchain so another more recent kind of
um threat to this par this model is
generative AI um this is becoming
increasingly Advanced and uh easy to
access so this is an example of a a fake
ID generated by a service called only
fakes so it's it's currently possible to
pay like $15 and you can have a a really
genuine authentic looking government
issue document created so you know a
high school high school kid could do
this find a profile photo of someone on
like Twitter and then easily generate
something that would fool the KY of of
some services in fact the article that
um this is from originally um they tried
it out and they actually managed a kyc
on a crypto
exchange and I think it's just going to
get easier and easier for this to be the
case so this completely breaks the model
of um taking a photograph of your
documents and sending it
in so so what if instead of this what if
instead um you could reveal only what
you absolutely needed to reveal for a
particular service so for example if you
just needed to reveal uh your country
and nothing more then that's all that
you you you need to
disclose um and what if you could
generate uh unforgeable one-time proofs
so onetime in the sense that you can't
replay these so once they user consumed
by the service um they can't use it
again so unlike a photograph which could
obviously be you know if it's stolen it
could be
reused
um what if you could prove that you're a
person and and not an AI or a bot who
holds a valid passport and reveal
nothing else about
yourself um and what if you could use
this on
Shane I think we'd all agree in this
room that that would be pretty damn
cool and so uh okay Mike that's great
that sounds wonderful but like how do we
actually get
there great question Mike well let me
let me explain so most people might not
be aware of this although maybe you are
now um given uh the booth and there's
you know kind of more more awareness of
this but everybody in this room um on
your your passports your e passports
that were issued by your government on
the NFC chip there's your personal
information and your issuing government
has digitally signed over this
information essentially attesting to its
authenticity and creating like a
tamperproof seal
so we're able
to verify these
signatures um we leverage this existing
infrastructure um of essentially like a
government signatures and root
certificates um that are used by
airports around the world every day for
by by governments to protect their
borders that's a kind of level of
security we we take these signatures and
we can verify them um in zero
knowledge and then and then eventually
we can another circuit we can disclose
that um
selectively and this allows the creation
of these private and unforgeable proofs
of
identity and so you can actually
leverage this so we're going to show you
the app later but as a developer you can
easily integrate this can you just oh
yeah
sorry so we have built like a SDK which
is going to be usable easily to easy to
plug for any JavaScript or web
Developers whether it's in the context
of web two or web web three whatever
kind of web app so it's really friendly
strongly type typescript SDK it's
intuitive to use to choose which kind of
field you need from the passport what
kind of information you
want it's going to really unlock like a
lot of interesting use case we thought
about some uh but we really curious to
see what people can build with it maybe
they're going to come up with something
we didn't think about so that's
something very curious
about and this is fully nonprofit public
goods so it's like free to use there's
no restriction there's no payment
nothing you just plug it in and you're
free to go no API key
whatsoever so here's an example of how
it would look so as a first version of
our SDK typescript so you specify your
domain name the name the purpose of what
you're trying to do with what the PE the
visitors or users of your
website and you will get the URL which
encodes all the parameters you requested
all the fields you paramed and then you
can encode that into a QR code and that
the user scan it from the
app and then you will get the
information with uh proof in some of the
Callback like on prooof generated that
requested uh the next step is that we
going to build like a react SDK so it's
even easier to use we're going to take
care of all the UI in ux flow so you
don't have to take care of that so it's
really one button and everything will be
handled
cool and um yeah so this section we're
going to go go over uh kind of the
differences between custodial versus
self custodial and if it wasn't already
obvious by the colors that I chose um
one is good and one is bad and just to
kind of maybe like reinforce that uh
yeah this is the bad one and this is the
good
one okay so uh so for custodial identity
verification as kind of like a
conceptually this is how it currently
works so you're issuing government uh of
your passport or other government
document they'll they'll provide it to
you and then you'll be so also like
digitally signing over it in example of
a passport or a national ID card you'll
then uh take a photograph of it and then
you'll provide that to a kyc provider
who will then maybe do a bunch of
lookups in a private database and then
eventually they'll just kind of let the
service know um you know Yep this is
Michael no this is not um and the issue
with this model here is you have a like
it's not really end to end and so you
lose the trust
Providence uh along the route through
this counterparty so it's kind of like
it's wasted because the government's
attesting to it originally and then that
gets broken when you have this third
party that has to re attest to it uh
there's a Reliance on this this third
party another downside is is it's all or
nothing so you're taking you know a
whole photograph of the passport
um fraud is much easier with this
approach because like I mentioned before
generative AI you know that's coming
it's going to get better uh it's also
quite expensive so sometimes they need
to fall back to manual verification
which can can be costly for businesses
which doesn't scale very
well and I guess this is kind of like
the you know the big issue with it
really one of the ma major issues is
you've got to rely on them to keep your
data safe and they often don't which
really
sucks and so contrast
to that you've got self custodial
identity verification which is truly end
to end and so in this model the
government's you know digitally signing
over your documents or attesting to
these facts about you and providing it
to you and then you can use uh you can
use zero knowledge proofs here to uh
verify the signatures in zero knowledge
and then selectively reveal what it is
you want to and provide that proof
directly to the actual service and to
end there's no other uh you know
middleman that need to be involved in
this even us we just create the circuits
um that to facilitate this but we aren't
really the
middleman and another great way to kind
of think about this is who better to
attest to the attest to your identity
and your your personal information than
the same entity that issued you your
birth certificate so you know you change
your name or you get married who do you
go to right you go to your government
and it's also another way to think about
it it's kind of decentralized across the
whole world
in the sense that each government around
the world they're attesting to these
facts about their own citizens of their
country and so on just some some
interesting use cases here for Z
passport there's really a myriad of
different possibilities um but we'll
just go over a few that kind of popped
out to us is quite interesting and
compelling uh private and compliant
private tokens so we're currently
building out a wallet called obsidian
wallet on Aztec Network and we want to
have privacy as a default and be able to
have these stable coins like usdc on
ramp and then be used completely
privately so you can actually have um
this PTP you know private cash for for
using it for just normal everyday
transactions without worrying about
priority concerns and everyone seeing
your full transaction history and so uh
yeah in the future we hope to have this
um integrated into obsidium wallet so
we're going to have basically Zig
passport as this kind of first class
citizen a f first class uh citizen for
identity um as identity provider that
will be able to automatically generate
proofs uh whenever you know you're
transferring us usdc around and so some
maybe some examples here of the proofs
would be generated so you'd have like uh
compliance proofs which would prove
maybe that you're not an ofac SN list
you're not from a sanction country and
then another option here could be maybe
using this unique identifier that is the
same for every passport um but also
completely anonymous you could track
like transfers over time so you might
impose like a super generous limit of
maybe 100,000 usdc per month that's
enough for like 99.999% of people but
that's going to severely limit uh like
you know Bad actors from from laundering
lots of of money through this and
ultimately it's going to mean that you
can off-ramp onto an exchange and not
have to be worried about the exchange
you know Banning your account um because
you've used this this sort of this
private and compliant token
another use case could be proof of
personhood so you can have increased Cil
resistance so both in the context of web
two and three is quite important you
want to prevent spam and Bots for
example you can have a social media
platform that wants to really have one
person and one account so you can do
that much more easily with this solution
or like simply the use case we use now
day a capture you could replace that
with a proof of P passport that would be
much
stronger another one is uh being able to
prove you know your name is really what
you say it is on social media so you can
imagine like a ver you know a
decentralized kind of way to do this
with a verified name badge You just
prove your first and last name that was
attested by some recognized government
and then you could you could have that
on social media as a a proof of
name and another strong use case is
proof of age so there's some country
that's started to impose age gating on
some websit such adult content I know
that because France is actually the
country where I'm from is doing that
they impos this legally speaking so but
they want to do it privacy preserving
way they still care about privacy which
is nice to hear from the government so
that's one use case as
well um so here if you wanted to know
which country actually
support e passport electronic passport
this is all the country in blue so that
covers a PR big chunk of the world over
standard set out by the
iow um institution of the United Nation
so it's actually quite widely supported
you will notice that India is not part
of it it's like a big country that's not
actually part of it for that country you
would have solution like anadar which
actually supports that kind of like
alternative system uh but others like
passport is pretty good there's some
disparities in the signature algorithm
though so they don't always use the same
kind of signatur so we have to adapt to
that it's not fully standardized but
there's some flexibility to those
standards but it's already quite good
another thing I want to point out is
that National IDs especially in the EU
also support that standards sometimes
even residence permits so we can extend
to that and the EU is also pushing
generally for digital identity uh with
the EU digital identity wallet and the
general identity framework they're
pushing with
Eis and to give a bit of an overview
here of the um the hierarchy of how this
works it's very similar to pki with like
the current the current web and SSL
certificates you have this organization
called iow and uh and iow they they are
under the UN and uh they collect through
diplomatic channels these root
certificates from different
countries and then these root
certificates they then sign these
intermediate certificates called DSS or
document signing certificates and those
certificates they sign the actual e
passport data
itself so I'm going to go do a quick
overview this is this our secet work so
essentially we get most of our data from
what we call the data group one so it's
like visible on the passport so the two
bottom lines so it's like contain the
name the date of birth and other
information where you can derive a lot
of information that generally people
want and this is hashed into content
with the rest of the data which itself
is signed so this is what is interesting
because that signed data is then we can
verify it with the certificate mentioned
by Michael the root Trust chain go all
the way up to the res certificate that
way we sure that that data has been
issued inside by the state and from that
we can derive proof of country proof of
age while being sure that's coming from
a verifiable source without riveting
anything else about the information of
document um so cool great and uh so
rather than just talk about it let's
actually dive in and take a look at what
DK passport um looks like and how it
works so this is DK passport and is I'm
going to tap my um government issue
passport against the phone and it'll
read the passport data in by
NFC and then once that's done you'll see
it come up here so that's me loaded into
zikar passport and then the next step is
just to connect it with the who are from
Southeast Asia to prove they from one of
the countries from Southeast Asia um but
nothing else about themselves and then
they're able to get a discount voucher
applied to their purchase of their defon
ticket so to do that simply click uh on
the continue button here this will
generate a QR code which I'll then scan
with my
phone and then that will prompt that
will prompt me to um which it'll prompt
me to prove particular credentials that
are being asked of me from this service
in this case it's just my country um and
that's completely up to the developer
that's integrating this so I will hit uh
accept this will generate the zero
knowledge proof on my phone it'll then
be sent via the secure endtoend
encrypted websocket where it's then
verified um either on the back end or
even um on a smart
contract uh we uh we recently blessed by
uh from with a visit from uh father
vitalic at our booth just around the
corner outside so please feel free to
come by um we've got it for the rest of
the day and um we have a workshop on
tomorrow in classroom B at 12:00 p.m.
so
if you'd like to learn more about our
SDK and uh and how it works please come
by and yeah you can chat with us sick
and I guess lastly one one last QR code
uh we have a demo available it works
best on desktop it's the one we're using
at the booth um so yeah there's a QR
code if you want to try it out and
you'll be able to load your passport in
it supports both Android and iOS um yeah
but if you have any issues with that
please reach out to us and we can help
out all right round of
applause give it up give it up okay cool
so we
have a couple of minutes left maybe time
for two questions and let's just go with
the top two so um I think you guys could
just read that and answer it yeah yeah
that's go for it um so regarding Noir as
DSL that's the system so how did you
land on Noir as the DSL for circuit does
your system interact with a itself so
first question um Noir so why did we
choose that um we did choose it PR
stable but now it's pretty stable so
Noir I see it as a very um good language
if you want to do zds
you ttsl that's mainten toward the
future the Aztec team is pretty reliable
they're good team so you can rely on
them and it's a universal language which
means you can have like a single code
base and switch your back end for a
different one if you want a different
proving scheme so you can still just
improve uh with the whatever latest
Improvement has been done in ZK we still
maintaining the same Cod base so that I
found this pretty powerful as for
whether we interact with that St itself
so zik passport is is blockchain
agnostic like the protocol itself is
blockchain agnostic but as mentioned by
Michael we're building this wallet
called obsidian which yes that one going
to be interative with Aztec specifically
and going to integrate ZK passport for
compliance and privacy mixed with
identity at the wallet level on nastic
yeah there's no reason this can't be
used on other chains like Alo or even
like ethereum lay one um but it's more
suitable I suppose on privacy chains
where you can have these uh approv data
um more private yeah more privately um
how do you handle the ux problem of
convincing users that their passport
further remains client side that's a
great question I think this is going to
be a challenge and it's going to come
down to to Brand trust and basically
building that up over time so we've got
open source circuits and and open source
codebase I think that's going to be
that's going to help for sure uh and
just being like credibly neutral um you
know people can trust this as a as as a
brand that's going to respect privacy
it's one of our core values so that's
just going to take time I think and and
you know demonstrating it through our
actions
okay make sure to check them out later
at the booth give a round of
applause thank you the thank you Michael
appreciate your time thank you
cheers okay ladies and gentlemen we'll
be back in a couple of minutes feel free
to get your drinks outside of the booth
and come back thanks I
know oh yeah
thanks
okay thank you so much mate I appreciate
your help thank you
you e
don't see
me
okay but I
don't hi everyone our next talk will be
starting very soon so can I have
everyone just go back to their seat for
a little bit
okay hi
everyone can I get everyone seated for
our next speaker
please all right cool so next we do have
a very interesting talk uh the speaker
is Vivic uh he actually just told me a
really interesting fact about himself so
outside of cryptography he's also been a
singer for over 10 10 years right so he
will be giving a talk on MPC for human
connection and coordination um a little
housekeeping rule there's going to be a
QR code on the side so please scan the
QR code if you have any live questions
for Vivic and we will address them in
the very uh last five minutes of his
talk so now let's give a warm Round of
Applause to Vivic
we have time to talk for to hello okay
she hi uh I'm Vivic I'm going to be
talking about something that uh I've
been working on with my team cursive
called digital pheromones and the
overall kind of affordance here is using
MPC or multiparty computation uh for
human connection and
coordination so I want to start with
kind of trying to Define this as as you
know as we see it so far and for that I
want to introduce first what is
multi-party computation so this is
essentially where multiple parties can
come together they each have private
data that they keep to themselves and
they jointly compute the output of some
sort of function such that only the
output of the function is revealed and
no like nothing intermediary or nothing
about their like actual inputs
themselves um it's actually a fairly old
technique a lot of the stuff that people
are currently using is dates back to
like the ' 80s
faster and and and more performing in
the past few
decades I also want introduce like
biological pheromones if that's
unfamiliar for any folks um it's a
chemical sub substance produced by an
animal and it's generally used to
basically um get individuals of the same
species to coordinate or work together
in some sort of way and there's a bunch
of different option like bunch of
different ways this happens like for for
bees for example it's about like sort of
setting off a signal and bringing a
whole like swarm of bees to come
together in one place a lot of animals
like mark their territory using scents
uh and there's also a lot of like sexual
pheromones for different animals to Aid
in their
mating so digital pheromones kind of
comes from combining these two different
ideas and I think I would Define it in
three principles at least at least right
now as as we sort of played with it the
first is that um this pheromone is a
very lightweight and privacy preserving
signal um it's it shouldn't be very
heavy ideally it can just be transferred
across like something like Bluetooth or
some sort of like uh low energy Network
and we use it just to discover
connection and perform coordination very
similar to how this works
biologically another requirement or kind
of principle is that this stuff is fully
programmable and verifiable um you can
choose what conditions you want to
reveal and also like because we have
amazing Tech uh from from ZK land you
can basically ensure that a lot of
different stuff is actually verified so
that people aren't putting out like sort
of false pheromones and like essentially
getting connection when they shouldn't
be and I think a final requirement for
this to really feel like almost like a a
part of nature like as a as a biological
Fon is is that this stuff happens in
kind of a neutral peer-to-peer
cryptographic protocol um we don't want
this to be kind of within the ecosystem
of a single app it should be something
where you can use whatever front end and
app you want but there's sort of like
some sort of standard between them to be
able to communicate and
coordinate and ideally we don't need a
server for coordination if a server can
help in a way that's still privacy
preserving but can sort of make ux
better I think that's
fine and broadly I think we think
digital Fones can help in two types of
sort of like human connection uh
discoverability and improving depth of
connection so with discoverability a lot
of our current stuff is based on like AI
algorithms and advertising markets who
basically like have all of your personal
data from what you do on the app and
their objectives are to keep you on the
app for as long as possible and to
maximize the amount of money you're
spending with something like digital
phones and the suite of cryptographic
tools it's built on uh we get to a place
where we can have full ownership over
our own data using tools like signatures
and zkps and use stuff like NPC to have
these sort of like really safe
programmable controllable interfaces to
learn more about the people you're
interacting
with and in terms of depth of connection
um I think right now in the in the
current version of the web there's
basically no verifiability and a lot of
data you kind of just trust public
profiles as they are and as a result
like you know like there just isn't much
depth and the other kind of twist of
this is that often times these profiles
are very sort of like public sanitized
versions of who we are we're kind of
playing toward whatever game we think
the algorithm will like or what other
people will like with something like
digital phermones it opens up a world
where you can actually have all the
stuff be verified and provable and
because you are custody it privately you
have control over how it's used uh
ideally you can share more interesting
and deeper personal information and thus
facilitate better connection better
matches all that sort of stuff and yeah
using tools like NPC and this tool
called a private set inter section or
PSI that'll introduce um you can do this
in a very safe and um just sort of like
efficient
way cool cool so I want to just go
through like a bunch of different like
kind of use cases or general sort of
like features that we think this sort of
thing could enable some of which we've
built out some of which we're still
trying to figure out how we can make
efficient uh just needs more like
research and stuff so the first is idea
of narrow casting so narrow casting is
the opposite of a broadcast and the idea
here is that you can basically choose a
set of criteria uh that you want
information to be reached or sorry
choose a set of criteria for people that
you want this information to get to for
example if you're throwing like a really
exclusive party um you can basically
find people that are in your city and
find people that have certain other
connections and certain other stuff and
the cool thing about it is that this
information is just like encrypted
nonsense to people who don't match this
uh but for people who do they can
decrypt it and see this information and
the idea here is that this can basically
enable more efficient and also like you
know you can keep the sort of criteria
private to yourself so basically like a
a better interface to get information to
people versus just like depending on an
algorithm to do this for
you another one is this idea of
unbreakable consent so in in multiparty
computation there's a general sort of
like flaw or bug which is that in this
computation someone can always drop out
of the process and this can either like
break the whole computation or
potentially they can get the result of
the computation and leave before other
people do I think in the context of more
like human facing stuff and especially
for something like 2pc um this I think
actually is a feature uh basically you
need full consent across all the
different parties for anything to be
like verified or like revealed and so I
think basically you can build a system
in which consent is literally like
mathematically baked in instead of you
know just depending on the platform or
other things to to do that for
you another idea is idea of super
connectors so essentially the idea here
is that again like algorithms like stuff
like Tinder and hinge are being used to
basically sort of bring people together
match them on different criteria and
they're kind of this like Overlord that
works with whatever incentives they want
and we think this technology potentially
could have the benefit of letting humans
be those connectors for each other so
you can sort of receive like privacy
preserving like summaries of your
friends data in a way that's sort of
like still private but you can still do
computation over and then you can
basically just be like hey you two
should meet or you two like have a lot
in common uh in a way that's like
basically going through like a mutual
friend instead of through an algorithm
but still maintains
privacy couple other quick ones um I
think basically this generally an allows
for like more direct connection between
two different parties uh in particular
for businesses who are trying to you
know do something like ad uh this can
just happen this coordination can happen
directly instead of like someone like
Facebook custody all the data like
providing the market and sort of you
know taking a cut from
that this other feature that we're
hoping to build soon is basically
something like I'm feeling serendipitous
where you can just walk into a public
space you can like put out a bunch of
different sort of like privacy
preserving signals of the sort of people
you want to meet the sort of things you
want to do and like I guess the upshot
of this is that you can just sort of
like privately manifest like the kinds
of people the kinds of things that you
want to do in the moment in a physical
space and because it's all digital you
can just send this over the internet as
well through like encrypted
channels finally like another one that's
like a personal favorite of mine is like
because this stuff is peer-to-peer very
lightweight you can imagine just sort of
like putting this out these signals out
to your community to your like neighbors
and there's all sorts of like little
like small coordination stuff you could
do with your neighbors um that would be
super useful that maybe doesn't make
sense to All Join the same social app
and like you know put a bunch of
information up but on some sort of more
neutral protocol for example you could
do things like oh like someone else is
like looking for the same grocery or the
same like other item like I'll just pick
up some extras and then give it to them
um if you need help with certain like
house repairs or certain things like you
can just query like hey like who nearby
like you know how knows how to do this
thing and generally just like discover
fun overlaps and intersections with the
people who live close to you as a way it
more easily
connects cool so now this will progress
into sort of the more technical part of
this talk which is basically just what
sorts of actual cryptographic tools are
we using here to build this sort of
thing
um I'm going to go through some past
stuff and then some upcoming stuff as
well so the first one is something
called private St intersection this is a
really classic cryptographic technique
um and the overall kind of like
affordance here is that you can
basically discover commonalities in a
way that doesn't reveal anything else
and you can apply this to anything from
just like a ordered set to just like
arbitrary
data and so for example like people can
just attest a different interests and
then in a very very efficient
cryptographic interaction discover only
what they have in common and this this
can also basically expand from just two
parties to be a group of parties uh for
for coordination sort of things like for
example calendly is sort of some like
weak private like not cly I guess uh
like lettuce meat and these sorts of
things are kind of like a weak PSI where
you like manually enter your stuff and
you see everyone's
availability so I think some nice things
about PSI is that it is using privacy in
an offensive way which is that basically
you can put out a bunch of data about
yourself and the only things that are
going to be revealed are what you have
in common with other people and just in
general like I think the risk of sort of
negative side effects for something like
this are much lower because at the very
worst case even if it is something like
weird or personal it's like shared by
the other person and this this contrast
with tools like zero knowledge proofs
where actually the goal is to share as
minimally as possible you want to
basically only reveal what you need to
and then hide everything
else I think PSI is also very
conceptually easy to explain I think
like out of all the different
cryptography that I've worked on this is
the one that like a general person lay
person can pick up and understand the
fastest but at the same time it's a very
like rigid protocol it's like quite
simple uh it's not very expressive and
often in these sorts of like matching
and Discovery things you want to do more
complex
operations so that takes us to a second
tool that we've been working around with
which is multiparty fhe or fully
homomorphic encryption and I'd say the
general sort of improvement here is that
for especially consumer devices that are
involved in this process there's a much
like lower liveness and compute
necessary than for a lot of other types
NPC so the general kind of flow of how
this works is that I guess like a little
bit of a primer on fhe you essentially
can have like some sort of key that you
can encrypt data to you can do
operations on the encrypted data and
then if when you decrypt this it's as if
you did the same operations on like the
like plain Text data and so in this case
how we make that work in a multiparty
setting is that there's three phases the
first is that Alice and Bob or any sort
of group of people come together and
create a collective public key this is
done in a way that none of them know the
corresponding secret key so all of them
can encrypt data to this public key and
they know that no one else will be able
to decrypt it within their party so once
they've all sort of encrypted to the
same key you can now do operations
across it and so now you can take
different people's data and you can do
whatever operation it is uh like
literally anything you could Define and
get to some encrypted output and then
finally because no one actually knows
the secret key which you need to be able
to decrypt this you need to do like a
collective MPC to basically do this
decryption and like in this case this is
literally just building a PSI with um
this multiparty which is actually
something that we've done in the past uh
there's a really nice sort of like tool
kit called ring learning with errors
that essentially enables really
efficient private set intersections on
like an ordered set and so this is
something that we've built out in the
past uh works really
nicely however there's still a bunch of
rounds here in that the parties need to
come together on every single
computation to make this shared key at
the beginning and come together at the
end uh there's this new approach that
was pioneered by G Labs uh which
essentially can remove this sort of
first step of the process everyone
uploads just a public key and a server
handles the process of essentially
creating a shared uh like Collective key
and then everyone can encrypted that and
then you still have the sort of
collective decryption process at the end
but you can skip this first step which
is really really nice for a lot of
applications so one thing we built on
top of this was um at Frontiers uh
conference in SF we basically built this
sort of like private job matching setup
where essentially as a job candidate you
might want to have privacy over the fact
that you're looking for a job and like
what kind of salary you're looking for
especially if you're currently employed
somewhere you don't want to like mess up
really relationships but at the same
time you should be able to find the best
stuff that's out there and so what you
can do is you can essentially encrypt
your own job profile you can attach dkps
for verification all that stuff and if
other people also basically make
postings that are private which maybe
you want for like some sort of stealth
role or generally just like don't have
to put this data up publicly you can
basically discover overlap in this both
in terms of like the sorts of
characteristics of the job and what the
the candidate wants as well as like
salary which is a more private thing of
like the recruiter is willing to pay
this much um and Below whereas the
candidate is willing to work for like
this much and above and you can just
discover overlap in that without you
know revealing those numbers too early
on some really nice things about
multiparty f is that the actual
computation involved here can basically
just be fully offloaded to a server and
so as a result of that devices only need
to do uh generation of public keys and
uploading that and then doing encryption
of their data uh at least the latter is
a very cheap operation and the first one
is a onetime thing the importunate thing
is there's actually still quite a bit of
back and forth rounds involved in this
sort of thing where there is still this
kind of final decryption step which can
make for really weird both ux and devx
and finally unfortunately with a lot of
this stuff at least in its current state
the data blow up here is immense where
the public Keys you're using the
different encrypted data uh grows in
size a lot because essentially you're
adding a bunch of like sort of noise to
this data while still preserving its
structure and as a result of that
there's a really big blowup that can be
in the like tens to hundreds of
megabytes uh which just doesn't really
work on for most
applications cool so I want to talk
about um a new research result that's uh
was built in house uh called Trinity
which we think answers a lot of these
different questions uh in particular
it's it's a instance of a general form
of of computation called non-interactive
secure computation uh with an added
bonus that it's all verifiable at least
the the the inputs uh their properties
can be
verifiable it's a combination of it's
named this way because a combination of
three different schemes the first is
garble circuits uh which is very
classical technique uh casg witness
encryption which actually came out this
year uh really really beautiful paper uh
very simple results but very powerful
and finally uh good old plunk or any
sort of like kzg based CK snark that's
not gr 16 because gr 16 is like
weird so just a brief primer on each of
these things gar circuits basically
enable two different parties at least in
the classical setting to compute some
sort of function and there's this
initial sort of like phase where one
person sends over a garbling of the
circuit which is basically like a uh a
version of it that is sort of like
hidden and like encrypted in a way
and they sort of encrypt their own
inputs into this but then the other
person in this case Bob he needs to know
his own encrypted inputs and so these
two parties engage in what's called an
oblivious transfer which basically Alice
can send Bob's encrypted inputs without
learning what Bob's actual inputs are
and without Bob learning what the other
encrypted inputs would be and this
oblivious transfer technique
unfortunately has a bunch of back and
forth rounds so it gets us to about the
same place in terms of rounds as like
multiparty
FHA the nice thing is this very recent
result basically saves the day in that
you can essentially I'm not going to go
into the mathematical details but the
high level is that you can essentially
uh create a constant size commitment to
all of your different data and post it
once you can post it on the blockchain
because it's so tiny and other people
can essentially encrypt inputs to this
commitment and so as a result this is
all a bunch of like the math behind this
you can basically make the oblivious
transfer one round and so as a result
you can just send it with the garbling
and the upshot of this is that to do a
send them one message instead of having
a bunch of like back and
communication finally uh the really nice
thing is this commitment is a kg
commitment which means that you can use
other really really powerful tools like
plunk to basically verify different
properties of this and because so much
amazing engineering work and theoretical
work has gone into this this can be
really really efficient and so you get
basically both this sort of one round
computation but then all the inputs you
can basically have a proof that they
satisfy different
properties and yeah so as I mentioned
basically this's is one round of data
transfer and you have these like
succinct very ient validity proofs of
all these inputs and actually Alice's
inputs as well and so we think this can
basically enable a really simple devx
and ux for building consumer 2pc apps
and hopefully like more parties in that
as well with some more research um again
you can use sort of other verifiable
data and maybe the overall way to
describe this is that you can basically
just send like this is actually very
similar to like narrow casting it's like
kind of almost the same concept of you
basically send like one encrypted email
and the other person is only going to be
able to open it if they sort of match
whatever criteria or whatever like
function you set there and so there's
stuff from like hiring dating uh like
event promotion that we think could be
used could be built on this sort of
thing and be made a lot more like safe
efficient one Counterpoint I like to
make is that uh you might ask like why
are you doing all this fancy
cryptography like you can just use
secure Hardware which will do it way
easier and honestly that's pretty fair
but I think at least in the context of
this idea of digital phermones I think
secure Hardware is very not neutral and
it's also very not peer-to-peer and that
you have a like a server entity that is
basically posting this stuff for you and
you need to trust them that they're
doing the right thing and also like if
they are cut out of the process or they
censor you or they otherwise just like
are not accessible you're basically just
screwed and I think cryptography enables
something that is much more peer-to-peer
interoperable uh can be sort of like a
neutral Network very very akin to like
you know natural phermones
cool so where can you actually try this
stuff um so first off if you go
downstairs uh we cursive has a really
really nice Booth near the uh
registration desk like right right after
it next to the badge Creation Station
and you can try a couple of these
different things so first off is private
set intersection um you can basically uh
you get these little NFC chips and you
can create a profile around that and you
can start tapping and meeting other
people and building a little social
graph and then if you import other types
of data which includes like some
connections to GitHub or your Devcon
events or like different sort of like
forms you can fill out you can basically
do this private center section process
and discover commonalities and we're
hoping to add a few more data entries uh
over the course of this week uh so this
can be more
interesting um another nice thing we
just added recently is that basically uh
as you do more and more PSI and as you
learn more and more about different
people they're sort of this little
digital flower and the more and more you
have in common the more you discover
about each other this little guy grows
and so you can end the event with
basically this this Garden of
connections Each of which is basically
representing of yeah how much you sort
of have learned about each other or
otherwise
shared um you were promised a live demo
today I'm so sorry um it is so close to
being done and later in the week this
will actually just be uploaded into the
uh app and so there'll be this sort of
digital phones tab at the end of or like
in one of the like parts of the app
where you can essentially do this whole
process you can send out queries you can
receive them and you can also like you
know with this idea of unbreakable
consent no one is going to learn that
you matched with it until you basically
opt into it and so at the very least
we're going to try to just run back this
job matching stuff and ideally we can
add some more fun stuff over the
week uh a couple other the shoutouts so
this booth that I mentioned is actually
modeled in the form of a museum
exhibition called cryptographic
connections it's both a bunch of art
pieces and educational content about how
cryptography can connect us both with
present tools and also um with stuff
from the past and again it's right right
behind registration next to the badge
station and in addition uh over the next
few days we're going to be running this
cryptographic classroom we have a bunch
of like blackboards in the back of our
booth and I'm hoping to basically both
get to explain all this research in a
lot more detail to anyone who's
interested as well is just explain
classic cryptography constructions um I
really like teaching people about
cryptography it helps me understand it
better um right now it's this is going
to be running from Thursday and Friday
from 10:30 to 12: p.m.
uh we'll maybe do
more sessions if there's more interest
uh just come by the booth and express
that you want other times and we can
probably make it
happen a quick shout out for cursive uh
we're exploring all sorts of different
research and design work around
cryptography for human connection and
this is just sort of one of those
Explorations and come by our booth if
you want to learn about past stuff we've
built and finally
a really big shout out to privacy
scaling Explorations which is a sub team
of the ethereum foundation our team is
Grant funded by them and we've been able
to do a lot of really great research
exploratory work uh both on our own and
also with collaborating with other
researchers in the ecosystem and if you
want to learn more about cursive here
are some links for you to take thank you
listening thank you Vivic we have some
great questions rolling in
uh let's take the first one what
prevents Bad actors from interacting
over the host search space to recover
preference data that's a great question
um I think ZK proofs are the main tool
here so that basically like you can
require on the most important stuff that
you know the attributes that someone has
is actually ZK proven and so as a result
it's like much harder to basically like
just kind of like fish for information
the difficult thing here is a lot of
stuff is just self-attested and so
there's other sort of like outof band
things like rate limiting or maybe
ensuring that you only get queries from
like a friend or like a friend of a
friend to ensure that you aren't just
getting like spammed and kind of like
you know read in a
way all right and is there any SDK
Library I can use to build on MPC fhe
yes so um the main tool kit that we use
to build out the hiring flow and a bunch
of other experiments is called Phantom
Zone this is a uh multi-party FH toolkit
built by G Labs mostly a g
uh and some other collaborators from
within PSC um this is a really great
toolkit um I think it's performance uh
bandwidth all the sort of stuff is
getting improved but it's very great ter
NPC generally there's a lot of great
tooling coming from privacy scaling
Explorations um like a toolkit to
basically write circuits in typescript
called summon uh there's an M like a a
garble circuit Library called mpz which
is used by the TLs notary team um both
of these are going to be what Trinity is
built on in the the long term so that
it's very easy to maintain and improve
but um yeah those are my current wrecks
perfect and how do you reason about
incentives to report things honestly if
interest matching with PSI reporting
every possible interest yeah that's a
great question um I think for a lot of
stuff like there's sort of like a
humanistic layer to this where like you
don't really benefit from lying in a
sense like you might as well just put
what you are interested in and then you
will actually just genuinely get matched
with that
obviously there is sort of this still
attack where people can just like say
they're interested in everything and
then just be like wow we all we like the
exact same things so you know it's it's
difficult for a lot of the self-attested
stuff um and potentially there's other
ways of doing it where like you limit it
to just like your top three interests or
something um like on a on like a query
level but uh yeah all right I think we
have enough time to take two more
questions uh what is the operational
Bandit or footprint overhead
multiplicator for MPC FH
MPC right so
basically I'll talk about the
interactive setting because I guess
that's what this is asking um there's
this initial NPC which requires I think
like o of n squ uh different messages
being sent well actually yes I think
that's correct it's oven squared
messages being sent to set up this
Collective public key if you want to do
it in a peer-to-peer way um or it's like
I think you can have a server be
involved and then you can lower that to
maybe something closer to oven but
there's there's that initial NPC the FH
itself there's actually no as far as I
understand no huge performance increase
the fact that you're doing over multiple
parties because you're essentially just
doing like single key fhe once you
generate this Collective key and then
there's also also this MPC at the end
which I think is also o of N squared
messages so the more this expands the
worse uh with non-interactive this is a
lot better because the server can
generate this Collective public Key by
itself um and then you know can sort of
handle that first
phase awesome and how does the creation
of Collective public key works for more
than two people trying to share Fair
OS right um I think so again is this if
this is in the like interactive setting
you basically just engage in a like
multiparty computation between people
where essentially like you need to
generate some like auxiliary data
between each other to generate a
collective public key in a way that like
neither of you actually get to learn the
secret key uh there's some really
efficient ways to do this for certain
schemes um and then if it's more than
two parties you basically just expand
that uh with traditional NPC techniques
um to be able to generate this
Collective key all right cool thank you
uh our time is up so let's give another
round of applause to Vivic thank
you next speaker yeah but in five
minutes
hello hello okay this is good can I have
everyone seated
please all right so next we actually
have a series of lightning talks and we
have a very special speaker Simona pop
she's going to give us a talk on you
know what's going to get us from web 2
to web 3 therapy let's welcome
Simona hi hello hi um okay so this is a
super sped up version of the talk that I
gave at ECC this year with slight
improvements obviously cuz I wasn't
going to talk to you about the same
thing um these are my socials so we can
continue this conversation cuz this is
going to be a marathon I talk a lot so
we're going to go a little bit over
sorry um okay so what's going to get us
from with two to W3 it's clearly therapy
um here's the agenda like these are all
slides that you can take photos of and
then um read later because I'm going to
go real fast so I tweeted this um pretty
much a year and a bit ago
um because I very very uh deeply felt it
at the time uh this is after um I burnt
myself out and had to like the end of
me Simona what are you excited about
next year and I said nothing and so I
was like oh damn that's not good um and
so I realized and I used to like fool
myself and say oh yeah I was on the
brink of burnout no I was probably
burnout for like a year and a half um I
have been in this ecosystem for seven
years it is very intense as we know and
we kind of need to be mindful of how
we're treating the humans behind the
protocols and the humans behind the tech
I say this with personal interest in
mind because therapy has benefited me
greatly um we're in a space of all of
The Innovation and the thing is we have
all of the these ingredients where that
are prime for Innovation we're free to
think experiment and speculate however
the technology isn't the only thing
that's going to help us innovate we need
a shift in the values and the thinking
and the way we approach things and I
genuinely believe that we need that in
order to build better things or build
things differently why
because as maslo we know him he loves
pyramids he said you can continuously go
towards growth or fall back into safety
what keeps us into safety even when it
is very very bad for us our nervous
system is designed to keep us safe even
if it is again bad think of it from
bless you think of it from the
perspective of web two going into web 3
some people and a lot of people actually
would rather remain where they are
because they're afraid to grow let us
not be in that space and have and
facilitate within ourselves and within
our Collective the opportunity and the
way for us to continue towards growth
again not just technological but also in
terms of human
thriving because I firmly believe that
the societies and economies we build are
reflection of our conscious and
unconscious ious conditioning we have
been conditioned and bastardized into
intense scarcity mindsets
intense just combative and extractive
ways of Behaving and being that I
genuinely think if we are going to build
something different with this technology
because of this technology we need to
shift out of that and we need to be
aware enough to know what we are doing
in order to do that until you make the
unconscious conscious it will direct
your life and you will call it fate we
have the opportunity because of this
incredible technology that we're all
working on if we're aware enough we can
actually not just repeat the stuff that
we have built just over here we have the
ability and the opportunity to genuinely
change things and redesign things at
many many different levels that get to
benefit us personally that get to
benefit us as a collective
that get to benefit us hopefully for
generations to come lot of
responsibility um but what it also does
when you're self-aware and when and
we're leading into this oh my God I'm
going so slow okay uh you can access
like higher core needs right those take
a photo of that because those are
important when you're stressed you do
not think about those things you think
about how can I get mine how can I
satisfy my base base needs and you make
bad decisions when you're stressed you
make decisions out of survival now if we
think people are in charge of billions
of dollars and Building Technology that
can genuinely change lives we don't want
them making bad decisions because
they're stressed we don't want them
making bad decisions because they're not
aware that they have some sort of
childbase wound that makes them want to
extract money versus build something
that is better so this is important so
like yeah read it later um this was a um
this was a poll that I did for ACC where
it gives you some stats about where our
community is if you see most people are
feeling not great anxious me tired some
people are feeling good which is good um
but also these are some of the
challenges that are incredible stressors
for our nervous systems and these are
very very real elements of our ecosystem
like that that can put you into intense
stress and we need to be mindful of that
and we need to make sure that the people
building in this ecosystem have ways of
dealing with these things or we as an
ecosystem are dealing with those things
and are aware of those things um burnout
that was also me so um uh 70% said they
burn out at least once so that's not
good um anxiety is on the daily most of
the time so um again a very very
important factor especially when we want
this to be something that The Talented
humans are building in the SEO system
kind of do it more than a year or
two um you get the gist okay um sorry do
you want to take a photo I mean do it
quick um but you get it so um again this
was something that I did at ECC and this
would be the Practical thing that I'm
suggesting so a human protocol that's
puts the focus on the humans behind the
tech because I think there should be a
base protocol a base layer protocol that
focuses on the humans if we want all of
us here to continue being creative to
continue having energy to do this to
continue making decisions from a higher
Value Place we need to
have regulated nervous systems and we
need to be aware of what it is that
we're doing why we're driving certain
things why we're making certain
decisions how we're making those
decisions and I think this needs to be
implemented the same ways we talk about
tech protocols a human protocol is as
important as far as I'm concerned uh
these are the benefits and the purpose
and the vision obviously um and here
just because when you talk about therapy
you talk about anything like this it's
very scary I'm not saying that people
are crazy although a lot of us are but
these are kind of the stages you don't
get have to have Go full Ham on like get
everybody on the team therapy you can
start very small like a pilot and then
implement it and then grow from there in
stages which I think is again a very
very important thing to do something
gradual because again not everybody is
comfortable with a lot of things when it
comes to therapy when it comes to Stress
Management when it comes to um again
regulating a nervous system most people
don't know how to do that and it's an
important very important tool um to
have and then uh yeah this is a great
meme I made it um and then yeah thank
you how much over was I what did I do
was I good
oh thank you it's cuz I'm so
relaxed I think that was actually great
because we're right time um to draging
off the stage that was
perfect all right thank you Simona thank
you um next we have another talk at 4:
all right so it will be great to get
everyone seated um we have another
speaker coming up
uh let's welcome Spencer Graham giving
us a talk on trust zones why DS will be
the best organizations ever created um
let's just slowly get settled down there
will be a QR code on the right so please
scan the QR code if you have any live
questions for Spencer throughout his
talk thank you
okay everybody can hear me okay great
hello uh my name is Spencer uh I spend a
ton of my time thinking about
organizations what they are how they
work how they're structured how they
should be structured and how they
shouldn't be structured and today in
this tiny amount of time I'm going to
talk about a very or give a very very
strip down version of a framework that
I've been working on to better
understand all of those things and that
framework is called trust zones uh every
single slide that I'm going to show you
has like seven slides behind it that
I've stripped out so this is going to
feel a little bit fast and my hope is
that you just come up to me and talk to
me afterwards about anything that
doesn't make sense because a lot of it
is going to be very very
simple okay I am an agent that means I'm
an organization that means I'm a human
that might mean I I'm an AI agent I have
a goal I cannot do all of it by myself
so I delegate I delegate
responsibilities and resources to some
other agent this makes me a principal
what does that mean that means I now
have a principal agent problem a
principal can't be like me I can't be
sure that my agent will act in my best
interest I can't be sure that my agent
won't capture my resources won't fulfill
my the task that I gave
them in other words the principal agent
problem is that I don't trust my
agent 100% confidence in my agent means
that I have full in them that is
typically not the case but what
techniques do I have to incre prediction
that an agent will act in my best
interest so technique number one we can
constrain what the agent can do
constraints are proactive physical rules
restricting what agents can do they are
proactive they are physical you cannot
break them they are exactly what blockch
in smart contracts are really great at
but con constraints don't always work
creative work requires flexibility that
constraints intentionally limit agents
need agency to do their best work on
behalf of their principles and that's
often impossible to Define everything
what an agent will need to do
upfront but more flexibility for agents
means more risk for principles like me
so what do we do we can make additional
rules and we can enforce them
retroactively this is technique number
two accountability otherwise known as
retroactive enforcement and this is the
thing that this is the only tool that
traditional organizations have they
don't have any other
capabilities accountability always
requires something at
stake your freedom your reputation
access to Future opportunities Financial
assets Dow tokens compensation all of
these things can be put at stake to hold
you accountable later okay technique
number three we can create eligibility
criteria that filter out agents that
don't qualify eligibility criteria can
include skill sets credentials
reputation generally and also credible
commitments and this ties back into
accountability like I can stake
something such as Dow tokens that can be
slash later or my agent can stake
something and I can slash them later if
they're not doing a good job so what are
the techniques we have for increasing
trust one is we can play with the size
or limit the size of the resources that
we delegate to our agents we can create
constraints around what they can do with
a with those resources we can hold them
accountable and we can apply eligibility
criteria so imagine a
container in that container I if I want
to uh delegate responsibilities I can
put them into the Container same thing
with resources permissions access
controls Etc I can whoops I can create
constraints as a one of the ways that
the container is defined and I can
create a filter as an eligibility
criteria that changes or that let's see
if we do oh yes that um that uh allows
only certain agents into the container
and then I can also apply accountability
mechanisms uh or Define the container
with accountability mechanisms that can
revoke the agent and hold them
accountable if they're not meeting uh my
needs or uh conforming to what I need
inside the
container remember in the in the
container the agent has full agency they
can do whatever they want Within the
constraints and the resource size and
the uh everything that I've set up for
that container inside the container the
agent has my full
trust so I call these containers trust
zones trust zones are how principles
like me can confidently delegate to
agents to maximize their goals with
trust zones we can also optimize uh
delegation and operations within
organizations because all of our
techniques 0 1 2 3 4 are dials that we
can turn up and down
we can create the
same let's see uh we can create the same
level of trust with different
combinations of these properties with
different settings of these dials so for
example with stricter eligibility
criteria we can decrease the number of
constraints or the strength of the
constraints or with stronger
accountability mechanisms we can give
our agents more resources or in other
words we can give our agents more agency
within uh within the trust Zone within
the container we can hold trust constant
while optimizing for cost and other
scenario specific factors traditional
organizations cannot do this all they
can do is do things with accountability
retroactive enforcement Dows though Dows
can do everything we can program trust
zones with all of the with access to the
entire design space of all of these
techniques another word so this is what
I'm going to leave you with here I just
have one more minute another word for a
trust zone is a
role and when a principal delegates to
an agent they are assigning that agent
to a role when they're revoking that
role they are applying
accountability and finally when we
Define roles on chain with smart
contracts we can make the best
organizations that have ever been
created thank
you okay um we don't have any live
questions rolling in so I guess we can
pass around the mic in the audience if
any anyone has a
question okay so one uh issue that I
think uh impacts ability for um in mind
or one of these issues is um scope creep
you know like the both in a such a way
that um an agent's limited because more
things are expected of them or there's
you know things that are expected to
complete a task that ends up being
outside of a scope of um things that
they're authorized to do or um the not
having you know the bandwidth to perform
all the activities that are desired of
them because of scope creep I guess yeah
I would be curious to know how such a
kind of reg rigid but flexible onology
um like yeah optimizes against that
because it's one of the main issues
obviously in Dows and our types of
organizations I think it's a really big
big problem and especially in
traditional organizations where like
your boss has all of the Power and they
can just like throw more stuff at you
without you having much recourse and we
see a lot of that kind of in Dows but
that's less like because the principal
um is is like malicious and more just
like weird loose lack like strange um
lack of clarity what I think is really
important in in Dows and in lots of
organizations is that both the principal
and the agent be able to make credible
commitments to each other so the the
agent can hold a principal accountable
if the agent or if the principal is like
uh uh scope creeping on them or or like
adding too much and they can say no
ideally we're not there yet but we'll
get
there all right um our time is up thank
Spencer
uh so next we have uh Tanisha to give us
a talk on governance Innovation let's
welcome Tanisha on the stage
okay hello everyone um thank you so much
for taking the time to join in um in
this specific talk we're going to cover
about governance and it will assume that
you have a basic understanding of
governance already another thing that
this talk is going to do is drop a lot
of QR codes because there's quite a few
innovation I want to cover so you can go
apply it in your worlds and the QR codes
will help you dive deep into specific
topics that you want to dive deep into
um let's start with Innovation number
one and this is so often like overlooked
let's face it right be it grants be it
governance be it decision- making the
voter's perception is at the end of the
day your reality and the user experience
in governance is an area of innovation
that's not very much focused on um this
is where we have an interesting product
we just launched which um kind of shows
you how you can delegate in one of the
simplest user experiences possible uh
you can select uh the percentage that
you want to delegate you exactly know
what's your working power going to look
like and then you delegate and that's
simple and this is one area where we're
trying to make user experience as less
fragmented as possible um and if you
would like to read more about the
thinking the transparency the ethos the
onchain activities that went into
designing a governance Hub I highly
recommend um scanning the QR code and
jumping into it um now let's talk about
not just the user experience let's go a
little bit deeper right uh we did a
research on how exactly water Behavior
works out we took two vot escro systems
one we took pad do the other we took
curve both of them require you to lock
in your tokens and in return you get a
certain voting power that voting power
is deced over a period of time but
there's a there's one fundamental
difference curve has a financial
incentive mechanism to it every Thursday
you use your we curve tokens and um you
get apys uh based on how the treasury
allocates funds poka dot not necessarily
has Financial incentives attached to it
now you'll see some very interesting
insights so in curve 65% of curve is
logged as V curve and out of the 65%
that's loged an average of 38% is used
for voting what do you think that number
would look like for PKA do one that
doesn't have Financial
incentives well 54% is locked in
multiple PKA dot lockers and it's a you
know a shockingly low
see how finan fincial incentives play
out a huge role in in possibly this
disparity let's go let's go a bit deeper
into another data point in curve the
lock up period is 4 years 67% of them
actually do lock up for that long on an
average what do you think it's for PKA
dot a similar V escro system it's again
a shocking 4% locking up for a maximum
duration of 224
days what is the other sign you see is
that this this Behavior perhaps the
underlying assumption is the financial
incentives and how the whole incentive
governance mechanism is playing out
together we also went deeper we said who
are these voters that are locking in
longer are these whales are these large
token holders we found a very
interesting Insight both in curve and
Pad do where 93% of whales and 98% of
sharks tend to lock up for 14 days or
less they tend to enjoy a sense of
fluidity they tend to enjoy a sense of
like flexibility with their lock up
tokens we saw shrimps on the other hand
locking up much longer um and when you
design your governance system this is
going to play a key role who are your
token holders what's their demographics
how are you going to design your lockups
and who's likely going to lock up for
longer it's going to play a pretty huge
role in the way you design
that um for more on the governance
research paper it's full of insights you
have that QR code feel free to scan it
um this is one of my favorites good
governance is obvious but great
governance and is transparent so many
like over the last three years of being
in governance I've had multip multiple
people tell me I don't understand what
to vote and who's keeping track of what
to vote well we've introduced something
called as transparency reports where
every multi-c that's apparently taking
decision is supposed to put out their
rational behind it and so you can read a
transparency report it's designed for
even non-technical folks to really
understand what's happening and exit the
system if you choose that that upgrade
is not safe for you or one that you
don't like almost every governance team
I work in this is a mandatory
introduction and we made it very easy
for folks to generate a transparency
report my time's up but you can read
more about transparency reports as well
um what I'm going to do is I'm just
going to jump through the final one
which is the conditional voting power DK
so the concept's really simple your
voting power decays with time but based
on your participation and there's an
interesting research on that as well but
yes thank you so much everyone for
taking the time and I hope this
heads
okay all right uh
so okay so uh
okay uh do we have any questions for
Tanisha we can do maybe uh a round of
passing the mic if anyone has questions
yeah we do have one over
there we do have one question at the
yeah hello do you mention the difference
between paulot and curve and how curve
has like higher votes just because of
the Rewards or like uh incentives what
sort of incentives are at play in there
or what incentives you think might make
sense for more
STS that's a great question it depends
on what the Dow focuses on there isn't
like a one- siiz fit and like fit all
answer so if if it's like curve or any
da that's focusing on liquidity having
apy for staking that's combined with
governance where you you have like an
underlying staking mechanism with W
escrow and giving apis for that
cryptoeconomic guarantees makes a lot of
sense but for Dows that's not focusing
on staking and focusing on engagement
having very interesting ways of
Distributing funds based on the level of
Engagement like for a gaming Dow makes a
lot more sense than just vot as Crow or
taking so it's it's really what the Dow
is seeking at the end of the
day all right thank you and actually
Tanisha here's a Live question what do
you use to gather this dat
data um we it's mostly on chain in the
sense that a lot of these data points
are already there so when your curve and
PKA do already have it on chain so you
take all the wallet addresses we used
Arkham data to also Identify some of
these wallets and who they belong to to
to measure the level of centralization
but um I hope that answered your
question hi um my question is more maybe
on privacy and still managing engagement
do you see valuable like uh using ZK for
enhancing privacy in um managing the
proposal uh and still giving the
confidence of user that will not be
blackf fired maybe for an exposure yeah
that's a great question so maybe not in
proposal creation I think privacy is in
my opinion best suited to delegations so
I was talking about this to somebody
yesterday let's say that I delegate to
you and I want to UND delegate right but
it changes the social dynamic between
you and me and there's a very
interesting survey with ZK sing that
actually showed that 70% of delegates
have that social pressure of UND
delegating introducing privacy there
would be an amazing way to show that
it's verifiable UND delegation but
doesn't change the game theory and
social dynamics within the community so
I think privacy for me more than
proposal creation I think delegations is
a very interesting area to introduce
privacy
there that's it right all right uh thank
you Tanisha for giving us this amazing
talk thank
you should I
mess so floral and oler okay perfect
I'll talk to you guys later then
are you
ready are are you yes hi okay
okay so you can you can call at the
podium
hello
okay uh so may I have everyone to take a
seat please we have Adrien to give us
the next talk the next generation of
governance will be modular um I
encourage everyone to scan the QR code
on the right so if you have any
questions Adrian uh we'll address them
in the end all right let's give a round
of applause or hyrian
hello thank you for being here wait
let's do that yeah thank you for being
here everyone so very quickly uh
Governors are a big thing in ethereum uh
there is an estimation that there is
about $30 billion locked into different
forms of Dao Governor contracts that
kind of thing but I think that's just
the tip of the iceberg because most of
the value is also this Governor contract
control burning the upgrade of Z L2 and
all this kind of processes like like
Governor control compound and compound
holds a lot of assets and this is
governed by about 30 million people that
have wallets that contain whether they
know it or not tokens that allow them to
vote and that's a lot of people and and
you can go to Tali one of our partners
to have a look at all the governor that
exist there are a lot and maybe some of
them are not even here but like this is
a big part of the space yet users are
not that much involved into this process
most people don't vote in the Bas case a
delegate to someone else so the question
is what can we do here and what's
missing usually when you have an
application you start your application
by deploying it with like an EA and as
your application grow you update your
governance you go from an EA to a multi
in your early stage and once you have a
big enough user base with token
distributed you can go go to to having a
full-fledged Dao but like this Rush this
should not be rush you should take your
time doing it but you should be aware
that this is where you should be heading
at some point and prepare for that and
so usually the question that we get is
if I want to launch a governor which
governor should I use and the thing is
that there are many many option to
choose from uh and there are a lot of
questions that you need to ask yourself
when you are going to launch a governor
who is going to vote what's the model is
it like a multi with a small party of
people or is it like completely open
like like compound with a with a voting
token like what I'm I going to do with
my Governor am I going to manage some
funds that came in like for example the
funds that are raised by ens by selling
domain names or am I going to upgrade
the bridge for from mayet to m 2 and
what's going to be the life cycle of our
proposal and there are a lot of options
that you need to figure out and and
that's painful to figure out because you
need to figure that out ear
before you launch your
governor and so you can basically use
open dep contract we have a set of
contracts to building your governor and
hopefully you can choose from many
option and build a governor build a
governor that fits your need but
ultimately like this is not a silver
bullet because uh you still have some
limitation uh for example like maybe you
want to have different rules for
executing a proposal depending on the
details maybe like if it's just paying a
subcontractor some some multi would be
able to do it but if it's a bigger
upgrade you want the entire Community to
vote for it uh maybe you want to to have
a compliment like this of of the votes
of the user and the vote of Guardians
there are many things that you may want
to do you may have a dynamic approach to
voting whatever that may mean to you and
so you could have an
upgradeable
uh Governor that will have a new feature
at some point but upgradeability is not
ideal in particular because if you have
proposals that are in light when you
that are active when you do the upgrade
you might mess up with this proposal and
and and so we need something better and
my claim here is that we want to do
something that is more modular uh and by
modular you may understand a lot of
things from people may think like oh we
can make it modular by using like a
diamond proxy approach and and we can
add new feature and it's less monolithic
but I don't think that's the right
approach and my claim today is that I
think that you should be able to do that
transition from the multi phase to this
Doo phase very smoothly by having a
single core contract that is basically
the Vault of your governance and being
able to turn on and turn off different
modules like having a module that you
use early on so that it behaves like a
multisig and at some point this module
would go away opening the space to
another module that would allow people
voting with token and maybe those two
module can coexist with a system that
decide depending on what the propos Al
is and what the state of this proposal
is which module takes over so that was
what I could come up within 5 minutes uh
but I hope I got you interested in the
subject of Governor contract and
governance of application in general and
please stay in touch with with this if
this something that interests you we'll
definitely want user feedback on
whatever we build for for doing that
thank you
um we don't have live questions rolling
in so let's do uh let's pass around the
mic in the audience if anyone have
questions
for hi awesome and thanks for building
uh all the the good stuff you have there
for free and open source uh
so is any of these things that you've
mentioned already being built uh what's
the the state of the road map so the
governor contracts from open Zeppelin
that's built and that's modular in the
way that you can assemble module before
compilation and then it compiles to a
monolitic contract that may be
upgradeable so that's something we
already have and we have a big set of
modules and some some modules we design
on our own some design we design with
users like the ens foundation and we are
going to extend that with more modules
uh and you can build your own modules
but for like the endgame thing I'm
talking about like the the smart account
um honestly it's a very fresh idea that
came up during Defcon so those slides
are very very new we do have an effort
to building uh a framework for ERC 4237
smart account that uses ERC 7579 as a
plug-in system so this is something
we've been working on for a few months
it will very soon be available as a
public demo like sort of a of a back and
forth discussion space before it get
frozen into the main repository and
during this back and forth discussion
with the community that we're expecting
to have in the upcoming months we will
try to build modules to to test the the
feasibility of having a multi behave
like a governor or a smart account turn
into a governor so we don't have actual
code to show you today but we hope to
have it in the next few weeks and
hopefully next time this time next year
it will be already in production for
quite a while amazing thank you all
right so our time is up thank you Adrien
for this amazing talk
sorry I was at old
cont I'm going to encourage everyone to
SC the code and ask for live questions
is that okay for you okay perfect
perfect so I'm just going to say time
I'm not going to say this part I'm just
going to say
perf and I will speak for five minutes
and stop yeah
good all right hi can I get everyone
seated please let's get ready for our
next talk next we have not your handle
to give us a talk on protocol alignment
um I encourage everyone to scan the QR
code for any live questions uh not your
handle will actually be addressing them
in the end now let's give a round of of
Applause for not your
handle thank you
everyone perfect um I am not your handle
also known as Vaughn um going to be
talking about protocol alignment
governing like a protocol uh which
sounds really really strange but trust
me it will make sense in a second um
first of all I'm going to start out by
talking about why we need governance I
think most people think they understand
what governance is I'm pretty sure in
the context of crypto they don't um so
here's at least our picture of
governance so um thinking about
governing a piece of software is fairly
strange so what I like to think about is
governing something people kind of have
a good model for which is a vending
machine is actually an incredible
picture somewhere in Hokkaido uh has
done the rounds on Instagram I love it
um but you can think about blockchain
protocol as being kind of like a vending
machine it's fairly simple it defines
some rules you can interact with it and
it does something thing every single
time that you try and interact with it
and if you think about the the um box
the box is kind of like a set of rules
um and they just specify how anybody can
interact and the value prop at least
from my perspective is that Protocols
are great because they make the future
more predictable nobody can come to a
vending machine and do anything but put
money in and get products out at a at a
predetermined
price now governance the job of
governance is to extend this we need a
set of rules that specify how we can
also make changes to that protocol if we
could make any change we want that means
the protocol would no longer be able to
give us any certainty about the future
the future would become less
predictable the value prop is that
protocol governance also makes the
future more predictable if you have bad
governance then the future becomes less
predictable and there we have governance
failure if you think about a vending
machine a vending vending machine's job
is to give you exactly what you want and
if you go to a vending machine and no
one's been able to update it right as in
put more products in you'll find that
the vending machine no longer does the
job you expected to do the vending
machine slowly starts to lose its value
and again you no longer interact with
the vending machine or protocol so we
need protocol governance because
otherwise our protocols would no longer
get users you can think about the action
space of all the things you could do in
a protocol right or with a protocol or
in life and then you can think about a
set of actions being aligned with the
goal of a protocol right updating the
products in a vending machine is aligned
with the goal of the vending machine
machine punching a hole through the
front of vending machine not aligned so
you can think about governance as being
that ring it's the it's the rules you
put in place to govern the set of
aligned actions allowed to occur in a
protocol so governing like a protocol
from my perspective is really governing
four buckets of actions if you think
about a protocol is just being a set of
functions that you can call right one
for UNIS swap could be something like
swap or add liquidity and then another
function which is just how you update
those functions and that's what we call
the governance and the governance really
governs protocol upgrades making changes
to the code itself adding parameters or
changing parameters which is changing
parts or variables in the code um policy
update so anything that's like soft
governance any rules and processes we
have around the protocol itself and then
of course resource
allocation another way of thinking about
governance is it's a set of State
transitions between different versions
of the protocol so you can see
participants sending messages in they're
voting they're putting in proposals and
over time we're agreeing which versions
of the governance to change so upgrading
from V1 to V2 or indeed if we change a
function having the first version of Pro
school and changing it to the second the
third the fifth and so
on now what I wanted to do is very
quickly run through some ideas they're
going to be fairly rapid fire we can
tackle them in the questions if that's
interesting um we've at butter have been
looking at loads of different types of
governance systems now one of the ones
that we have already is token governance
we like to vote on proposals we use our
tokens to provide some information about
our preferences And We Gather those all
up and we make decisions great this is a
vote that took place very recently for
tally we all know tally we love tally
Tally wanted to put a proposal into Unis
swap that basically ask for like some
some resource to be allocated to them
and this passed so when this passes we
say like there's 3 38.8 million uni
voted for this we have to ask ourselves
what happened and one of the things I
want to get into your mind today is that
the way that we vote is based on our
preferences which is also based on our
incentives and most people in the world
are dangerously long themselves most
people are self-interested they care
about the maximum return to themselves
so if you think about those people
turning up to vote this is how you have
to think about them and as I said a
token holder vote is a token weighted
average of stakeholder interests so
that's what you're getting you're
getting this kind of as an average a
token weighted average some of other
mechanisms you could use include
auctions you could for example auction
off proposals I wouldn't encourage you
to read the text I put on the slide I
just put it there because I thought it
was interesting but if you look at that
I think most people understand how
auctions work you have a seller they're
selling something people are bidding for
it so imagine bidding for a proposal we
actually decided to design one of these
a proposal Market um and uh turns out
people didn't like the idea of bidding
on proposals but you can imagine the
idea that you're bidding to buy the
right to pass a proposal and you can
imagine all the ramifications of doing
that um and come and speak to me if
you'd like to Le more about how we did
that um another one is peer prediction
this is where you have lots of people
observe something and then decide
whether they think it's aligned or not
aligned with the goals um you could say
that token voting is kind of similar to
this but this could be any kind of
mechanism could design you can think
about Uber ratings being a peer
prediction mechanism and again we tried
to do one of these things we ran it for
element and it was uh it was interesting
again we have some good results which we
published online um and it's is all to
say there are loads of other ways of of
actually getting people to do this role
of deciding which which actions are
aligned with the goals of a protocol one
of the things that we've been really
excited about recently is futaki or
decision markets they're a mechanism
that leverages speculative markets to
make decisions I like to say you have to
think about it as this you have four
possible worlds in the future one where
you make decision a A B C or D what you
can have people do is speculate on the
value of you sorry speculate on the
probability that you achieve the outcome
you want in any of these worlds and you
can use the probability to determine
which world that you want to be in and
you can use that to actually make a
decision this works interestingly well
um it's something that we're trying out
we'll have some some trials actually
going live very very soon maybe in the
next couple of months um and um you
could imagine a market for making a
decision on who to hire as a uh as a
prediction market so you can predict who
would get the result you want which is
the amount of Engagement with a
particular proposal or with a particular
piece of work and then you can sell the
uh potential outcomes as tokens and
people can bid on them and they'll give
you the probability that each of these
events will happen and then you can use
that to actually make the decision on
who to
hire so a futak uh eli5 is if markets
believe an outcome given decision a is
more valuable than an outcome given
decision B choose decision a and ideally
decision a will be very aligned with the
goal so what we like to do in governance
is build a system where being long
yourself is the same as being long a
particular protocol that means you're
aligned and is the same as being long
with ideally an entire
ecosystem this is an example of the same
proposal which was the one that we put
through a vote with Tally but instead
we're now asking about how much each
project so we have tally versus other
potential places we could invest would
grow voter retention which is maybe the
metric we care about we have people bid
on these tokens and they produce either
the uh they they produce an a proposal
or sorry they produce a outcome that we
care about and then we can make a
decision uh I'm vaugh McKenzie from
butter and uh please come and speak to
us about futak and decision markets
thank
you thank you and let's take some
questions from the audience uh we can
pass around the mic anyone has a
question for the speaker
oh we do have a question over
here oh uh we do have a question here on
the the first
world hello uh my question is how I I
don't know if I is I'm going to say well
how futar works on on
Dows absolutely um so a DA could decide
that it cares about something such as
sequencer Revenue so for example and it
could then decide to ask a question um
you then decide to ask a question um
about whether a particular decision say
if they choose to invest in a particular
protocol or if they choose to um roll
out a particular program or make some
decision if that's more likely to
increase sequence of Revenue and then
you can compare the probabilities and
you can make a decision based on which
the markets believe is most likely to
produce the outcome that they care about
which is growth in sequence of Revenue
does that make sense yes it do thank you
okay no wor
is uh okay so I think that's all for the
questions uh let's give another round of
applause to not your handle thank you
all right so can I get everyone seated
let's get ready for our next
talk um we have lauro and Oliver to give
us a talk on why language is key to
decentralization Let's welcome them on
stage are we here yes I think we are
okay hi everyone I'm Laurel
internationalization project manager at
consensus working mostly on localizing
metamask and I'm Oliver I'm from
customer success also at consensus
awesome we're going to spend the next
five minutes remixing some old tired
cliches to explain why human languages
are essential for decentralization of
ethereum so don't put all your nodes on
two continents is our first one um what
we mean by this is that over uh 50% of
the uh no active nodes on the ethereum
network are in the United States um and
of the top five countries
America and Europe I think we have a
slide for that
right yes thank you thank
you and 99% of stable coins are pegged
to the US dollar again concentrating
defi within the influence the
traditional Financial system right now
the tech that we're building may be
stifled by the tech that already exists
and if our infrastructure mainly exists
between two or a few countries and our
stable coins are mainly tied to the Trad
econ systems of those countries
centralization is where we're headed
even if the rails look different but we
can avoid this all it takes is talking
to people and maybe not necessarily the
ones that are already in this room yeah
so so uh how do we get those people in
this room right uh our proposal is that
the users and the use cases are out
there um and we just need to get them in
here so let's take a look at the data um
uh this is from a16 Z's uh state of
crypto report that came out recently um
so until 2020 you can see over there um
even if there were people speaking
different languages and living in
different countries you couldn't see it
right you that it's imperceptible or
there's too much signal in the noise um
and then you can see like in 2018 this
big blue wedge thing that's like you
know we're we're bootstrapping we're
getting it off the ground and so we're
looking at mainly people from the USA
but then by the time a few years have
gone by here in 20121 we can see these
big Peaks coming out of Nigerian and
Indian and um Turkish users um that's
that blue wedge up there so at that
point we're starting to get we're
starting to be able to see um some
signal uh in the noise and this this
next data isn't up here but it's
something Laurel and I have seen at work
uh so since
and Indian readership of the metamask
support site support.
metam mask.
combined readership of those two
national user bases are greater than the
US reader base of that site so um there
is just a little complexity though to
that data that we found and we wanted to
pass that on to you when you look at
your own internationalization and Global
user based data which is um this space
has a non-negligible percentage of
paranoid an non Deens that are actively
avoiding various regulatory oversight
mechanisms in the impending police state
got any of those in the house huh no
okay okay thank you see you don't show
up in looker um so uh a lot of our users
come to us through vpns and that means
that it wasn't until we started
translating our content that we actually
saw how massively multilingual and
Global are user
so lesson being you need to figure out
who your users are and then meet them
where they
are yeah so the users are already here
um we need to build web 3 with
them and we're actively doing this in
our day jobs making sure that metamask
is also relevant for and usable by
people who live in Africa South America
and Asia the people who make up the
global majority and we think that
localization is especially important
when it comes to self- custody because
you can only exercise control over the
things that you understand and with
metamask we're finding success with a
combination of localization strategies
that we can't fit into five minutes but
find us afterwards and we'd love to talk
to you about them and translation is a
big part of these efforts uh so metamask
is actively maintained in 14 languages
and we've received Community submissions
in over 60 languages which indicates to
us that Builders are eager to adapt this
tool for their
communities so we did a test recently
and we translated the metamask homepage
and download page into nine languages
based on what little country level data
we have about our current
users uh which shows that our largest
user bases are across the continents I
mentioned before the African South
American and Asian
continents and in just two months of
serving a localized homepage for most of
the languages we served we saw a
dramatic increase in users who clicked
the call to action to download metamask
we had a lot of traffic from users with
their browsers set to these languages
before we localized um and the increase
in engagement signals to us that once we
localized people whose best languages
were perhaps not English could
understand the utility of a tool like
metamask better and then could make the
decision to use it so this is the core
of what we believe that people all over
the world are ready and willing and
wanting to participate in web 3 and it's
up to all of us in this room to
communicate what we're offering in a way
that's relevant to
them so uh moving quick here um no it's
fine it's fine um we do need to make
this better together right um and
there's uh a lot of arguments over what
words can mean and and how we get there
to a place where we can all work
together uh any times human any time
humans have had to work together U on a
project at some point they had to agree
on what words meant at least for the
scope of that project right this may
sound like a joke but if you speak in a
language other than English how would
you say dank sharding in that language
right um if you're building a thing with
other people you need to be able to
communicate it um and uh to the ef's
credit they held um a translate on this
last year and they made a really great
um uh glossery here um and uh uh so
that's a great resource um the field of
decentralized Technology though is a lot
bigger than ethereum hate to say it here
at Devcon um I work with education da
which is a um an effort that came from
the consensus Academy program if any of
you remember that and and um at
education da we want to cultivate and
maintain educational resources for
whatever bag you're holding if it's not
eth that's fine too so if you're looking
for a go-to place to have an acceptable
definition right like a multilingual
encyclopedia for web 3 um we're building
uh words of web 3 that's the GitHub repo
um that is an ipfs URL that we're trying
to make sure it works um uh so the the
website is up um at that URL but um you
know it's loading off of IP so it's fun
um and we'll be coming together with the
EF folks that we just mentioned um at
the red discussion Center sorry the red
discussion Corner Friday at 1:30 p.m so
if you want to continue this
conversation come see us there and we'll
leave you with just one thought uh a
cliche that we hope you can help us make
reality Gua Kiana head of crypto at uh
onaf freak recently said Africa doesn't
need crypto crypto needs Africa and we
think that's true so in that Spirit the
world doesn't need ather e ethereum
needs the world thank you everybody
you all
right thank you Lauren and Oliver for
the amazing talk we do have a little bit
over a minute for a question in our
audience so um anyone have a question
let's pass around the
mic we do have one in the
back uh Hey guys great subject matter I
love learning about about this how do we
offer support to these users in
different languages when they have a
question we want to make sure that we
have active support for them uh quickly
uh so how exactly do we offer support to
these guys in uh different foreign
languages um that's a great question and
uh may I just make the point that um
broadly in web 3 that's not a problem
we've solved okay um at metamask I feel
like the team does a a consensus in
general we do a pretty darn good job to
try to address this um it's something
that we're working on uh a best practice
that I want to offer you from uh the
Trad world is that if you can hire
multilingual people who are going to be
speaking to your customers specifically
maybe people who speak the languages
that your customers speak and then they
can provide support directly in the
customers's language that's a best pra
excuse me that's a best practice
obviously that isn't possible for all
the languages in all the world world and
uh you know I'm sure that the next
person to speak would say I think AI
solves for that um it probably doesn't
but it might get us
closer excellent love you guys all right
thank you guys so
much uh so for our next talk we have
Hudson Jameson to give us a talk on why
I hate on onchain token governance and
you should to Let's welcome Hudson on
the stage
let
black
come wa
why with look up PU
speaker
know
you for
introduce just me
of no just
give
sorry I mean should I say that if
there's no do do you want me to no I
literally will wake up a question you
literally will do that I will absolutely
do that cuz it's funny I think it's
funny I say j
it's good I can
sing don't step Don't Step on my okay
okay I'll sa it for
few minutes
the next next speaker so you
are you will have I
I'll
go hello welcome back everyone can I get
everyone seated for our next talk
please perfect so next we have Daniel to
give us a talk on unchain in index so uh
scan the QR code on this slide if you
have any questions for Daniel to address
in the end let's welcome Daniel on the
stage um it's actually Thomas
Rush um my name is Thomas rush I think
was I introduced as Thomas Rush sorry
about that yeah so um that is the
correct slide I don't have the
clicker um thanks for coming um my name
is Thomas rush I'm with a project called
true blocks I've been in the space for a
while I only have five minutes so I'm
going to try to go fairly quickly I want
to start with an experiment I was going
to ask you all to come forward so you
could hear me but I'm not going to do
that I'm going to raise my hand and when
I lower it I want you to sing the first
line of happy birthday in your own
native language I want to make a point
so help me out with this all
right and that's because today is my
birthday
ready stop stop stop stop stop wait in
your own in a non-english language if
you know if you only know English
hum don't speak
English okay that's good it's good it's
good it's good all right um
so I think coordination is every single
place you look in the world it's all
over the place that song I I thought it
would be much more uh combined the same
uh the same music but it wasn't really
but anyway let's just pretend like it
was all the same music the point I was
trying to make was someone wrote that
song in 1850 and within 20 years it had
percolated through the entire planet and
because it's a good way to wish someone
the happy birthday and I think that
coordination is everywhere you look does
anyone know what this thing is just say
the word what is this
English it's a bulletin board and EV I
think every person on the planet
understands this protocol this is a
protocol this is a standard and they're
everywhere you look so that's a bulletin
board what's
this this is a cave painting from 65,000
years a go I think it's actually a
bulletin board people think it's a
religious object I think it's a bulletin
board this guy here he's saying my cow
has too much milk please take the take
the milk this guy says camel races next
Friday at the at the rock this guy says
I need a ride to um Mesopotamia or
something like that so I think bulletin
boards are uh another example of people
coordinating and there's a very simple
protocol there's two participants a
producer and a consumer and the
producer's job is literally to pin an
announcement to the board that's the
entire job of the producer the consumers
is to read the announcement and
everybody knows how this works and it's
super effective as is indicated
by that there's thousand hundreds of
people in my town put up new things
every week in your town too probably
probably so I watch people build smart
contracts and talk about coordinating
with a blockchain and I think to myself
why is it so complicated it's not
complicated you can build the simplest
possible smart contract that lets you do
bulletin board by at the producer
produces the data the consumer consumes
data so this is an example of one of the
things that I'm pinning on my bulletin
board and I use the word pin on purpose
because I'm pinning it on ipfs and ipfs
to me is a bulletin board this contains
enough information that that hash at the
very top is a hash of the specification
of the data that I'm publishing it has
enough information for you to parse the
data and read
it and these hashes are the location on
ipfs where we're storing pieces of the
data that we want to share with people
the world and I published this to a
Smart contract called the Unchained
index and it's it's on the ethereum
mainnet at a known address anyone can
read it anyone can download the entire
index for the entire mainnet ethereum
chain and they can find a history of any
address on that chain and we do this for
five different chains and we're doing it
because I want to publish this data
because I want my users to be able to
access it and you want to read it
because it it's valuable information to
you because you can build software that
knows where to look for the history of
addresses on the
chain and it's a simple simple idea and
I think that um my goal here today is
to try to get us to look around a little
bit and say these things don't have to
be anywhere near as complicated as the
as they seem to
be so this is the um interface for the
contract it has one function and one
event the function is called publish and
the event is called something was
published and people can listen for us
publishing this this um piece of
data the thing about blockchain data
that's really interesting is that it's
reproducible and this is obviously true
because everyone could just start up at
blockchain and they can reproduce the
entire history of the chain and this
indexing data because it's built
directly from the um block data is
equally reproducible so anyone can
choose to Simply download this data and
use it same way as a blockchain or you
can download it and reproduce it
yourself if you don't believe that it's
true so we don't have any need to create
a mechanism to prove this data and
that's one of the examples where I think
people over complicate things as long as
the data is
reproducible uh you don't really need to
prove it because it's their
responsibility to prove it to themselves
if they
want so I think coordination is really
easy I think it and the other thing
about this is It's it costs $1,000 a
year for me to publish an index every
day for the entire year and it's
basically free which is exactly like a
bulletin board which ISE
free
um it's also a shelling point it's where
if people have something to say in a
community they they put it on a bulletin
board and people read it from a bulletin
board if you think about apis for a
minute there're also bulletin boards
someone saying I have information I want
to give it to you the the thing about
that that's different than what I'm
talking about is that they can refuse to
give it to you for free they can rate
limit you they can charge you for Access
they can spy on you as you're using
their API none of that is true if you're
reading directly from a smart
contract and I purposefully built this
as simple as poss as possibly could be
so that people could get the idea that
smart contracts do not have to be things
that need to be audited for millions of
dollars they can literally just be
simple things at
work I'm going to talk more about this
on uh Friday uh 2:00 in the uh
in the uh eth Staker Hub and I welcome
anyone to come there and I just wanted
to say one final thing
um there's supposed to be a clock there
but I don't know how much time I have
left
but as I said it's my birthday and I'm
another um another thing that the entire
world has agreed to is that the older
you get is directly proportional to how
wise you are so I want to just say I'm
very wise and you should listen to what
I'm trying to tell you so thank you all
right thank you uh Thomas for the for
the for the talk um yes so let's you can
you can move a little bit
to so uh we can take questions from the
audience or would you like to no no it's
okay okay okay let's let's take
questions from the from the audience
then
no okay all right oh here we have one
question oh no no hello I I have the
question for H you store in on chain you
store the has of the um Index right the
but in EFS what is the cost that has for
you to store all the information because
someone has to pin the thing right in
Professor we store a manifest it's
called a manifest and it uh contains
records of each additional new piece of
data so the first piece is the first
piece of data and the it just adds new
pieces of dat yeah so does this have a
cost for you or you have a server
running all the time pin in EFS the
information um the one nice thing about
this type of way of doing things is that
because people are downloading these
pieces of dat data to their own machine
presumably they can also pin the data on
their own bulletin board and they can
also be part of the solution to how do
we share this data because they will
also be serving it to other people and
that's the way ipfs works so we kind of
did that on purpose as well so there is
enough people serving the it's it's
unfortunately the case that you need
enough people it's a chicken and egg
problem but what I'm trying to say is
it's so simple they figured out birthday
songs in 10 years without computerss it
was all just people talking to each
other so it's a simple idea it
works and my time's up thank you all
right thank you
Thomas all right can I get everyone
seated for our next talk thank you thank
right okay so for our next talk we have
penj to give us a talk on indexing
entire 2.4 billion transaction on
ethereum in 10 hours Let's welcome Pang
J on the
stage thank
you oh okay thank
you hello everyone uh my name is pan so
I'm Tha so as a Tai uh welcome to
Bangkok and Devcon here in
Thailand all right so uh today I'm thank
you okay uh so today I'm going to talk
about uh indexing entire uh 2.4 billion
transaction on ethereum in 10 hours okay
um okay right now it may be like uh 2.7
billion right now but at the time it was
a 2.4 okay let's get started so when
talking about uh indexing on blockchain
uh this is the con conventional way to
do it so you have a database that tracks
uh the latest block that you have
processed and then you uh uh you you
call the blockchain node and then get
the data and then update the that block
and so on So You Loop this uh uh until
you get the latest block right this is a
conventional way to to work on the Lo
indexer but uh looking on the product
I'm working on is called Alat uh this
one uh we we have some special
requirements uh we want to index like uh
all address in on the ethereum since
Genesis and also we we want to get all
the erc20 token events and then get
those prices to get the what uh is
called pnl the profit and loss that's uh
that's what we want but how we do it we
cannot do it in in a conventional way
because it would take forever right uh
to to read uh those uh 2.4 billion
transactions and then uh loop uh one by
one
so we need to
uh think come up with a way uh to do the
indexer in large scale so let's get back
to the basic of the blockchain IND
actually it's just uh data processing
right we've got uh input we've got uh
then we put it into the process and then
we've got
output yeah so let's look into each
component what we need from the input to
be uh able to process it uh in at Large
Scale is that we want it to be Compact
structured so this is the solution
because uh bucket gives us like uh the
compression uh also we have type in
pcket as well c c pcket format is like
um CSV but better
CSV and we found this project this is a
very good open source project uh it read
data on the ethereum Node and then write
it into bucket file so that uh when we
want to process we just uh read uh the
file in in our file system that's is
very lightweight we we don't need to uh
call the node every time to get the
data okay let's talk about the process
how to do how to do the process in large
scale
so we have to do it in uh in a parallel
way right there are couples of uh
solution one is the Apache spark another
is Apache beam uh we choose Apache beam
because there is a man service on the
cloud
platform and then
output when we have process the data we
have to write it somewhere right so
uh that that uh destination that I have
to write uh need to be able to scale
horizontally meaning that uh if I want
to read a lot of and write a lot of data
I can just uh create new new instances
and then uh I can read and write uh
more there are a couple of solution to
do the uh distributed dat database uh as
you might guess that I selected the
Google big table because I don't have to
worry anything about infrastructure of
database all right now piece everything
together and do some coding this this uh
does not take uh 10 hours in I I mean
the coding uh it took me like uh two 3
weeks uh to work on all the components
and understand how Apache beam works and
actually write
it uh this is uh what the final pipeline
looks like so data comes from the top
and then uh tricker down and then uh get
the result
and we wait around 10
hours and it finish just like that yeah
uh so we I I I uh ran it and it took
like around 10 hours to index all the
ethereum transaction all the uh erc20
token
transfers and there's something more on
it because we only index uh the current
data right the big bat very very big
batch of data and how to make it real
time so uh I need to do it in a
conventional way uh to to uh update uh
to get the new uh blocks and then
because I I don't need it to do at last
scale anymore right I can just do it a
traditional way to make it real
time these are the numbers
um it cost me about uh $350
and the number of the row that is
written on the database in 10 hours uh
was the uh 7.1 billion records and I
scale the big table instance up to 20
instances the good thing about big table
is that when I finish uh writing the
data I can scale it down so after I
finish uh index those big data I scale
it down to just one to handle the normal
WID uh operation
yeah that's that's the good thing about
uh this whole
thing yep I think uh that's all for me
today thank you very
much all right uh so we can ask some
questions in the audience uh we can pass
around the mic if there's any questions
for p oh we do oh awesome we do have
some questions on screen so let's go
through the first one for eth node how
did you host that to handle large read
all right um for
the in this process is the uh is
the uh cryo right cryo reads from the
node not not our not my indexer right so
uh we use many service and that is a
dedicated uh server to to read all the
data yeah all right I guess we have one
minute to take one more question uh
where are you reading the archive data
from how does reading from the node
scale for you okay fortunate fortunately
for my for my uh case I don't need the
archive data I just need the transaction
data the locks yeah from from the
ethereum node that is just full note is
suffice all right um so I think that
concludes our talk for today thank you
so much I I see that there's a lot more
question so maybe uh we can discuss yeah
so if you have any questions for pen
feel free to discuss um in front of the
room okay in front of the room thank you
very much thank
you all right cool let's all get seated
for our next talk uh let's welcome
Daniel from xchain he's the co-founder
of xchain so let's welcome him on the
stage
right
so sorry
holy
 okay good evening you
all first of all I would like to thank
the Devcon Organization for letting us
Host this talk together and I shall
start so my name is Daniel I am a
co-founder of chain chain it's a it's a
company that we decided to do a Blog
Explorer as we call as we can all see a
bunch of new blockchains are being
spawned every day
and this number is not slowing but the
the but the currently offer for blog
explorers is rather
limited uh we believe the community
needs new actors so that's why we
decided to go for
it as for today we are live on the
ethereum ethereum mainnet and and
testnet and on the polygon zbm and
Cardona that it's it's testet we support
all the basic things that a user or a
developer can can possibly uh uh need
such as uh data from the transactions
interacting with verified smart
contracts or verifying smart
so as you may know uh running a block
spur is not as easy as it seems it's not
just connecting to an RPC and showing
the data on a beautiful UI it actually
involves a lot of interdisciplinary
Technologies such as the Big Data uh
being the part like the the guy before
me said that he indexed the whole
blockchain on 10
hours being being having that available
on a on a just a few clicks and on and
on a couple of seconds it's very
hard that being said let me you let me
give you a quick overview of our of our
infrastructure what makes us different
so what we pursue is the onboarding of
any newer blockchain evm compatible
blockchains and as S as simly and as
easy as possible
for that what we what we have done is
that we have extracted all the e all the
evm compatible
um core the the stuff like the blocks
the transactions the internal
transactions all of this we have
extracted on our core module and then we
inherit from that and then we we build
uh the The Primitives that are needed to
index for example for the for the eum
block we inherit from the base block the
base evm compatible block and then we
top it up with specifics for the for the
chain in ethereum would be all the
consensus info the blobs Etc so that we
have it that makes us able to index any
newer evm compatible chain in no
time this level of flexibility what we
is what we believe what gives us an
advantage here because we will uh sorry
the level this level of flexibility is
what we believe is necessary for
creating the tools that will help to on
board new new new users to the
blockchain we envision that the solution
is to is to develop purpose build
explorers more than one fital solutions
that it's what we have right now
different blockchains have different
needs and different users therefore
their explorers should be
different now this is what we currently
have now let's talk about the future we
are exploring the idea of decentralizing
the block
Explorer as you may know blockchain
technology is is all about
decentralization and
trustless yet the irony is that most
users get into the into this space using
centralized
explorers this creates a significant
contradiction if we believe in the power
of of blockchain and decentralization
our tools should align with this
centralized explorers are single points
failure someone could tamper with data
in introduce bias and even Sense on
transactions what would happen if a main
Explorer gets gets hacked and change the
Avi of a of a really user smart
contract this Reliance this Reliance on
centralized party undermines the very
values we stand for the blockchain in
the blockchain
community if our infrastructure is built
on trustless then our our tools should
reflect
that we think the future lies in a
decentralized open source and trustless
data fits much like how chain link
functions as a decentralized data
Oracle imagine block Express that
aggregate information from this from
validators it would be like as as as as
chaining does with with some or with all
the oracles to come up with a price we
envision that the solution is to grab
data from different data sources and
aggregate it on a on a one
proof remember several races Rose by
orle manipulation it hasn't happened yet
that we had this data manipulation but
it's something that can happen and we
better be safe than sorry and I would
and I will conclude now with my final
statement that to truly embrace the
blockchain revolution we need to align
our tools with its
principles together we can build a
future where the Explorers are
decentralized transparent and open to
all ensuring blockchain data remains a
public good for everyone
much all right so let's see we can take
questions from the audience do we have
any hands raised
up no anybody oh we do have a Live
question coming in do you have
differentiators from ether scan block
Scout yeah as I said at the beginning uh
our our infrastructure and our vision
it's what it's different we we believe
that the that the future are the are all
the chains that are spawning up and
being able to respond quickly to their
needs is what differentiate that I mean
we have a level of of personalization
and a level of of
um of giving the the the the layout that
they that they that they want that our
competitors doesn't
have all right cool um any more
questions all right cool all right thank
you so much for the amazing talk let's
give another round of
applause okay
uh so we do have a three minute break
until our next talk so feel free to
install the the dependencies
and while this is running this takes a
couple seconds while this is running I'm
going to quickly explain you what mud is
so mud is a fully onchain uh well mud is
a fullstack framework for building fully
onchain games or really any onchain app
that you want to build and now that the
um dependencies have been installed we
can start the local def Runner which
will start a uh client Dev Runner and it
will also start a contract death Runner
and it will also start a local node and
it will also start the local World
Explorer all right the first thing we're
going to have a look at is our
client our
client need the video to
start there you go all right so the
first thing we're going to have a look
at is our client
that we're going to open the URL that's
printed here and mud has onboarding and
smart accounts built in so we could
connect uh our external wallet here or
we can just create a fresh wallet that's
pasy controlled here um and then create
a local uh session account that receives
some delegations from the main wallet um
so that now we can move our little color
blop here in this in this world um
without having to hit approve every time
again all right let let's have a look at
the Explorer
next um for that we'll click this little
button here on the bottom in mud all the
state is stored in tables and the state
the onchain state is automatically
synchronized with the client and also
with the Explorer here so we as we move
around our little color blob um we can
see the state on the bottom in our
Explorer update and we can also explore
all the other state that's in this app
and then another very useful feature
that the Explorer gives us is um the
interact tab where it basically
automatically synchronizes the entire
ABI of the world dynamically um and then
we can use the interact functionality
here to interact with the world directly
um for stuff that doesn't have UI yet
for example so in this case we're going
to move another we're going to spawn
another color blob and uh move it around
by calling the functions directly on the
Explorer and
then now it's time to add some game
mechanics to add some functionality
for that we're going to open our
favorite code editor and we're going to
open in this case the move system
systems are what mud uses to implement
the logic of the game so the move system
here for example implements the logic to
move a player and this is where we're
going to add um one more game mechanic
which is the ability to teleport a
player um in this case we can uh we we
just receive two input variables and
then we're going to write them to the
onchain table um and then as we write
that it's going to be synchronized to
the client again and then once we save
once we hit save here after we're done
implementing this function the def
Runner is going to pick up the change
here um in the contract and it's going
to redep redeploy upgrade it's actually
not going to redeploy the world but it's
going to upgrade the system um so we
still see our state here and now
immediately the new ABI has been
synchronized and we can now interact
with this uh with this new function that
we've just built the teleport function
all right I think this is pretty good so
far so it's time to deploy to a chain
and for that we're going to run the
deploy command and this in this case
we're going to deploy to the r rol light
chain and we didn't have to fund our
deployer account here because it's
actually going to use Smart accounts
again and the deployments are going to
be sponsored um so now we have deployed
to real chain and we can now um run the
client again against this version that
we've just deployed um and then we can
open our browser again
and connect our wallet again this time
to real chain um and then yeah we're in
and we can again move around um in our
little world if you want to try out this
game I won't promise it's fun but you
can go on workshop.
mdef and and try it
out try the onboarding flow and
everything and if this made you a little
bit curious um you should scan this C
code because there's a much better like
longer version of this Workshop that's
going to be held tomorrow at Mud day and
this QR code is going to bring you right
there um Frolic from our team is going
to hold that and he he's going to go
into much more detail um and with that
we're
done all right thank you let's take some
live questions uh what is the tech stack
you're building on so um this is M so m
is the framework the the main piece um
and then mod is evm compatible so you
can literally deploy to any evm chain
there's no um yeah any any chain that
can run evm bite code is is basically
that and yeah we're using a bunch of
like I mean we're using all the all the
libraries that everybody is using um VM
permissionless and so on so perfect so
I'm going to mark that as answered do
you have differentiators from either
scan SL blocks that's probably a
question for the previous talk so what's
Roto light uh Roto light is just our
test net that we're running um it's the
the test net that belongs to Redstone um
rolite is a type of redstone if you're
curious um that's why it's called like
that but yeah it's just a test net
perfect um so we actually do have a one
minute for any questions from the
audience no all right cool oh we do have
one over
that's that's a great question um is
it's you could you could technically
represent them as mappings it's it's
very similar to mappings like you just
have the keys um that are the keys in
the mapping and then you have the data
that's the value in the mapping um we're
not actually doing it as mappings
because we we do some custom stuff to
make it more efficiently uh more
efficient but you could Implement them
as mappings yeah so not like I mean I I
have 10 seconds left so I I don't I
can't go into detail but you can check
out the code it's open source um but
yeah it's it's like we're just using
like asem to basically pack the data as
efficiently as possible um and then ride
to storage very similar to a mapping in
the end all right so our time is up
thank you so much alvarius for your
all right can I get everyone seated for
please perfect so next we have drew Mill
to give us a talk on ethereum's Ultimate
Gift will be birthing digital matter um
there will be a QR code on the right
side of the screen so please scan the QR
code if you have any live questions for
drw Mill now let's welcome drw
hello okay uh so funny enough the last
talk was about like building uh a game
with mud in 5 minutes this talk is going
to be about a game built with mud in
like 5 months so the much more extended
version of it and I think I think it the
last talk you probably found to be
useful and Technical and like you can do
something with in your life this talk
will be really really weird um and you
might find it useful but you'll you
should at least find it really weird uh
ethereum's Ultimate Gift will be uh
birthing digital matter so basically
we'll start off by saying that one lends
to view ethereum is as a more efficient
open Global Financial system and this is
a valid lens to view it as um and if you
if you view from this lens there's a
particular set of things you care about
you care about stable coins you care
care about rwas you care about onchain
treasuries you care about secure wallets
and private
payments but this talk is going to be
really weird right so it's going to be
about an entirely different lens to view
ethereum through a lens that is not
really about moving our existing World
on chain to make it more fair and more
Global and efficient new and weird world
uh which is quite different from we have
today and and the future that's like
super weird and interesting but
something we can enable with
ethereum we're going to talk quote
ethereum as a way to make people treat
digital objects as if they were
real if if you think the if you think of
the prompt that Bitcoin was able to
birth digital coins that people treat
like a real valuable coin The Prompt
today is going to be can we use ethereum
to 100x this and birth digital planets
that people treat like real valuable
planets and to to sort of draw an
analogy that we can play with if we
think Bitcoin has scarse coins we can
think a Planet might have scarse crops
scarse wood scarse ores scarse land if
we think Bitcoin has tamperproof IUS you
may think a digital planet has
tamperproof
physics just like having a lots of
scarse Bitcoin grants you power in
bitcoin's World controlling lots of the
scarse matter grants you power on a
digital Planet if you sort of just
visualize it imagine that if you want to
go somewhere far you know because you
want to mine a valuable resource there
you're going to need a lot of food so
you can sort of you know re-energize
yourself and get there so if someone is
going to farm crops and you have scarse
crops that's valuable and you can create
markets with
it and if we do another thought exercise
just to get really weird here if you
think that Bitcoin on AWS It could only
be worth so much right but if you put
Bitcoin with true scarcity and temper
proof rules cuz you use blockchains it
can be worth a trillion dollarss uh so
likewise if you have sort of digital
wood on AWS it can be worth you know
nothing but if you have digital wood
with true scarcity and temper proof
rules I don't know can you have digital
wood that's worth a million dollars um
and there's already like there's a bit
of a meme about this sort of in the
community we're from about digital sakur
that takes a year to grow and you can
build really cool things with it being
like super
valuable and to make things concrete and
not as sort of abstract as they are
we're going to use biomes as a case
study
um on the surface biomes is basically
just Minecraft with everything on chain
um this is possible for the first time
ever because of recent advances and sort
of scaling this means everything is on
chain all the items are on chain the
players are on chain every action the
puller takes like that like building and
jumping and you know moving all of it is
on
chain and recently biomes has started to
see a lot of traction um funny enough
there's sort of the the chain that sort
of you know that that was being talked
about in the last talk uh that chain is
sometimes in you know top five in roll
up.
WTF which is the chain biomes runs
on one of the community members has said
biomes feels like ethereum but more
playful there's there's people who spend
hours and hours a day building stuff in
biomes people who spend you know 8 hours
plus hours a day sort of mining stuff so
biomes has really been you know getting
a life of its own recently and we're
going to ask and we're going to deep on
why this is happening and why people are
excited about
biomes think of it like biomes is a
digital Planet the same way big coin and
you have provably scarse matter there's
only so much coal there's only so much
ores there's only so many crops only so
much wood and you have temper proof
physics similar to how folks use Smart
contracts to build on top of ethereum
folks use Smart items to build real
economies on top of biomes smart items
are just items
with functionality in the world that you
can program with a smart contract so
imagine you have a chest in a chest you
can put stuff inside you can take stuff
out imagine I put a smart contract
inside of the chest and I program it
with you know Unis swap so every time
someone mines you know an ore and puts
the ore inside of the chest they get
some amount of token or I can put the
token inside and get some amount of the
ore and all the prices are set by amm
pricing just a way they would be in a D5
protocol and you can sort of imagine
this for a ton of things you could
imagine a door inside of the world that
is a literal token gate the door checks
if you have a token and if you do it let
you open it and get through right so
you're you're taking ethereum and you're
giving it the Homer Simpson treatment if
you told like some random person what is
a token gate this is what they would
think it is it's a gate that you need a
token to open you have a force field
that can protect lands and and you can
program with a smart contract to who's
allowed to build and mine
inside so yeah smart items are just like
physical smart
contracts and already a lot of really
cool things have been built inside
biomes with this stuff um the bizaar is
basically our version of Unis swap it's
a it's a large mall with chess shops for
all types of objects and it prices
everything according to the uniswap uh
amm
formula and there's a there's another
group of players who right beside our
building created this thing called w
Swap and basically it's the sushi swap
of biomes right they're trying to vamper
attack the bazaar with like different
pricing so you can kind of see the same
kind of like emergence you see in defi
happening inside of this virtual world
you have the Sakura Temple so Sakura
wood is a wood is wood that takes a year
to grow and it's a bit of a meme in the
community so you have you have a group
of players who have built this big
Temple where programmed a chest such
that if you donate Sakura to it it gives
you a membership nft and they're
probably going to gate all of their
future meme community events with this
nft and they're going to use all of the
donated Sakura to build the largest
sakura tree in the world you have the
Castle Hotel and Sakura Inn which are
hotels with beds inside and they're
going to make it so you can keep your
Piller safe and not be griefed when
you're logged out um and of course you
got to you know you got to you got to
pay rent to to stay in these hotels the
pyramid Arena will host a bunch of duels
in the future
have a bunch of betting markets around
all these duels and price pools the
parkour challenge it's this really hard
challenge where if you complete it at
the very top you can sort of mint an nft
and this nft will grant you access to
more difficult parkour challenges in the
future so you can already see how smart
items are literally the smart contracts
of biomes and people are building
physical daps inside of the
world so with scarse matter tamperproof
physics and smart items a crazy new
asset class and economy is now being
burn inside
biomes imagine a force field protected
gold Reserve imagine you have a chest
where you go around this you know
Minecraft world and you and you mine for
you mine for gold and gold or is scars
and hard to find you get this gold and
you put it in the chest and the chest
means you a coin if you put the coin
back it burns the coin and gives you
gold ore right so now you have a coin
that is backed one to one with the scarc
gold ores in the world and every time
you do this it takes a small fee and
gives it to players that reinforce the
force field that is protecting sort of
this chest from being stolen and broken
into in this case what you see is if
this coin rises in price let's say this
coin like it's enough mind share and
enough excitement and enough utility in
the world that it re it reaches even the
and viscerally obvious why you need the
gold scarcity to be provable because if
I as the dev of the world can
arbitrarily mint myself more gold ores I
can just go to the chest and mint myself
more coins right and then that just
breaks the breaks all of the
functionality of the coin it also makes
it super clear why the physics needs to
be temper proof because if I change the
physics I can make the force fields
really easy to break and then I as a Dev
can can just go to this bank reserve and
just break the force field steal all the
gold doors and that token is going to go
zero so as soon as you have these this
new asset class that's extremely weird
an asset class that's born in the
physics of a virtual world as as soon as
you have that asset class take off it
sort of just carries the virtual world
forward you know why all the ores need
to be scars all the physics need to be
temper proof um and it's it's just a
massive narrative violation where the
virtual world now just instant ly become
super
significant um to to sort of give
another example you can think of like an
old asset class which was uh I don't
know if anyone's aware of like the
entire nft metaverse land movement that
happened a couple years ago that's kind
of you know that's really failed but
basically in that movement you could own
and trade land nfts and if you had one
of these nfts you would have total
forever ownership of that land and this
was really good for a specific crowd of
people the crowd of people that were
into
hyper Ral Financial speculation right I
can buy this real estate because I think
it's going to be worth more in the
future and you have like Snoop Dog
buying land um but in this new asset
class it looks very different if you
want to sort of protect land you have to
build a military now this military can
tokenize a land they're protecting and
sell it to people and like Oh Come build
in this land and we'll make sure only
you can access it but that token is only
worth anything as long as a military
still act
if I come back in 8 months and that
military has been broken down the token
they sold is can't really do anything
right so this is a very different type
of economy where players have to
actually grow and maintain a digital
military to maintain the value of the
assets they've just sold and anytime you
have a like a thing you kind of seen
this in crypto all the time with whether
it's been defi or nfts or meme coins
when you when you have a different asset
class with a completely different set of
rules it it invites a different type of
participation and you start to appeal to
a different set of
users so yeah we think a crazy new asset
class which is enabled by digital matter
and smart items is slowly unlocking
biomes and soon we think these sort of
concepts are what will unlock autonomous
World worlds broadly the crazy new asset
class enabled by digital matter and
smart items this is this is the
statement um now you know we have some
time because they I think they allocated
too much time to me for this talk so
we're going to go a bit crazy and we're
just going to zoom out from this biomes
case study and sort of put our you know
heads back in the sky for a second we're
seeing here how ethereum can eventually
birth worlds that we don't physically
inhabit and we never can but we still
treat as tremendously real and valuable
consequential um in these worlds unlike
Bitcoins scar digital coins and
tamperproof IO use these worlds have
scarse digital matter and temper proof
physics and inside of these worlds
inhabitants use Smart items which are
tangible forms of smart contracts to
grow digital economies with unimaginably
large
gdps um so I think I think the thing
that's interesting about this slide is
you're kind of just seeing how in a way
this has already happened right like the
idea of of scarse digital Resources with
tamperproof rules has already been
proven by Bitcoin and all you're doing
is you're taking that same concept and
you're making it very physical you're
saying that instead of scarse digital
coins now we're going to have scarse
digital matter instead of tamper proof
Financial rules you're going to have
tamper proof physics rules and just like
smart contracts have already created
this crazy onchain economy with a bunch
of emergent defi protocols we're seeing
how smart items takes that and brings it
to Virtual Worlds and you see a bunch of
crazy emergent econom inside of a
physical world so the same way we
unlocked crypto I think is how we're
going to unlock autonomous world but
this time it'll just be way cooler
because way more people like Minecraft
than like EXL
spreadsheets and okay if we if we just
you know take another step back if these
autonomous worlds grow like billion
dollar gdps right or even like a
trillion why not you know we can make up
numbers here let's say it goes a
trillion dollar GDP and you start
somehow having autonomous agents living
inside then it becomes really funny
because if if if these agents live
inside these worlds they're going to
Value the scarse digital matter inside
of the world that they live in much more
than they value coins from our world
which they don't live in you know if you
give an agent
like five diamond ores from inside of
the world they can take those ores and
turn it into a weapon and like cause
havoc in the world so it's obviously
useful to them but if you give them
like5 us like what are they going to do
with that they can't like buy like a
McDonald's burger right they can't eat
that it's a software so like if the if
the if the GDP grows to a couple billion
dollars and you have a tonomous AI
inside you're going to have a super
weird World um agis only accept Sakura
for payment they don't believe in coins
um in 2027 biomes is our only
Communication channel to AGI agents and
when we seek wise counsel we travel into
biomes and journey to the lands and
homes of these AI agents and we bring
them gifts like glowstone in exchange
for books containing the rean hypothesis
solution I don't know if anybody's seen
like doctor strange but there was this
like thing at the end where to save the
world Doctor Strange had to uh like
bargain with doramu like doramu give me
the solution so it'll be the same thing
you're going to go and bargain with the
AGI inside of biomes and be like here
AGI here are all these redstone blocks
and the AGI would be like oh wow I value
these because the GDP is so high in
return here's the solution to climate
change right so yeah and Skyler you got
to trust Skyler Skyler is very credible
Skyler is the Devcon head right so he's
trustworthy and here's what he has to
say about biomes he thinks uh first this
is Unstoppable Minecraft but next it is
a Unstoppable lifelike simulation with
with unalterable digital physics you
know roamed by AI cryptomed who believe
they're as sentence as we believe we are
so even if this looks like Minecraft you
need to take it very very seriously this
is very
important um go to b.
APW to see all of
unfold you can come to Mud day tomorrow
the the the thing the QR code that was
here in the last presentation um and
there'll be much more of all the
stuff uh thank you and we have time for
a Q&amp;A
H um tell me more about the Sakura meme
okay basically I I honestly don't know
how this got started I think it's
because like there was a video that
could released in Twitter about how I
was talking about how coins are kind of
useless but digital wood is very
valuable because you can build a house
with it and Sakura is just a type of
wood in biomes that looks really pretty
and it's really hard to grow and it
became a bit of a meme so people just
want that Sakura is the Bitcoin of wood
people really want
it I think that's it yes uh do we want
to take any questions from our audience
any of I have a
question okay thank
you all right thank you for the amazing
talk
if there's no one questions we'll just
take some questions from the crowd
hello can I get everyone seated for our
next talk
uh next our very last Talk of the day uh
we have housei to give us a talk on
Civil Tech M St let's welcome
housei hello
guys thank you for coming to my session
uh I'm very honored to be here for
sharing our story about Civic Tech by
the way so before starting the uh please
raise your hand how many of the people
know the ter from Civic
tech oh very few good uh so I'm founder
of code for Japan and running Civic Tech
Community in Japan and Civic Tech is a
global movement transforming government
transforming government Sten
relationships through technology and
Community the we have both two phases
the one phas is for the collaborate with
the government uh to for open government
initiatives like promoting open data or
open source software or or or doing
hackathon with them and to to know that
the to understand what kind of Civic
Innovation is enabled and also we
have we facilitate citizen Le projects
like uh citizen participation for uh
change for improving the society or
cities uh
often uh organize uh the kind of the the
participatory uh experimental projects
with citizens it called living loves and
also uh provide some participatory
policymaking platform or something and
also uh encourage we encourage students
to start new projects for solving local
issues uh organizing haathon or or uh we
have specific projects for solving
social issues like gender equality or
anti- disinformation and so on so the
key point is that we use the digital
public goods for or infrastructure for
uh for enabling this post side
Communications and uh so so digital
public goods is created by the
communities and also created by the
government we utilize th those of the
ideas to facilitate Civic Innovation and
in Japan there are four types of
stakeholders like a central government
or private sectors or local governments
Academia so uh for the central
government uh we work with them uh
through the Outsource uh sometimes we do
outsourced work from the government or
we sent some uh Tech uh developers or
technologist to the
become a member of the government
committees and also there are private
sector it is important uh and there are
big tech companies or social startups or
G Tech startups or non nonprofit
organizations so we ask funding uh
simply for to this big tech companies
and also we work with the social
startups or nonprofit organizations and
and also also we promote open source
software or open data to these private
sectors and the local government is
really important for us uh because Civic
Tech literally the citizens can do
something with the local government so
we facilitate to build the local
communities or uh become uh some
sometimes the the the uh uh
technologists become fellows to the
Civic uh local government and
as a Academia uh we we provide kind
opportunities for of the students in
intership or use Civic engagement
processes and and so on so we have those
kind of stakeholders and uh code for
Japan's role is uh uh facilitate Civic
Tech in Japan and my our vision is Sy
together create together and we have
three pillar class of activities mainly
one uh we Foster uh digital democracy
and we build uh digital public goods and
also we facilitate C that project and
those three PS uh under those PS we have
many projects uh and right now we have
more than 8,000 members on our slack
workspace and also we have uh more than
we have n 19 plus brigades brigades mean
the local code for Community like a code
for saporo or code for Osaka and we have
Grassroots communities and connect those
uh for uh facilitate the uh to start new
things uh I started Cod for Japan uh 11
years ago and we or we have been
organizing the uh more than 65 times
monthly hackathons and we have multiple
government
Partnerships let me show some examples
from the uh digital public goods part
and this is a DDM the software uh open
source software for the citizen
participation processes the uh this is
created by the originally created built
by the uh Barcelona city government that
this is open source so that we
translated this software into Japanese
and also provide the those instances to
the local government uh like City
kakogawa cities or k isi City and the
the in Japan citizen engagement tools
are beginning to be used in a wide range
of fields both of the public and private
sectors so right now Cod of Japan is
providing such uh uh for uh providing
those software for cities to encourage
uh citizens to participate the policy
making
processes and also we have as I said uh
uh we have 19 plus Regional Civic Tech
communities uh each communities have the
different uh format of activities they
organize hackathon with the local
government or local just local Comm
communities or have some experimental
project with them so we connect those
those communities and and and try to uh
create create the digital INF digital
public goods
infrastructures and one of Key
activities of us is a social hack day
this is the monthly haakon just one day
haon and and we everyone can join not
including non- tech people
uh the in in the beginning of the event
the the uh project owners uh will pitch
their ideas or existing project and ask
help uh for the to by the participants
so each participant can choose which
project they you want to join and and
after join uh forming the teams uh that
team will work together and and at at
the end of the event uh they will uh
share what uh what what Improvement has
done on the event and this is the
regular regular hon so that people don't
need to build the new new new projects
every time they just they can bring
their existing project and people join
and help to improve this is uh this
hackathon is not a competitive hackathon
that collaborative hackathon and from
that activities there we have so many
projects uh this is part of the project
list our project list and I on this
stage I I don't have time to explain
details but uh uh uh some of the
projects are very active but some of the
projects are already quiet and some of
the some some of the projects have been
released uh publicly so uh so this uh
from this uh so from the hackathon event
we uh citizens create projects and some
projects uh uh actively developed and
but still we have uh many challenges as
a uh Civic Tech Community uh
sustainability is issue or and also
impact and adapt adaption is also issues
and and also technical social issues
like uh yeah we have uh funding model is
very difficult uh currently the in Japan
uh there is not much uh Foundation
helping the this kind of the uh new uh
form of activities so that so we earn
revenue from the government and spend
those revenues to the community decide
and so creating sustainable Civic Tech
EOS system
is very important challenge to solve and
also growth management is difficult uh
maintaining quality with scale uh it's
very uh difficult for to manage by the
voluntary just the voluntary groups so
we need some kind of solution for uh GL
managing managing grows and also impact
side the the government integration we
is still uh still difficult uh
bureaucratic resistance to open source
is strong in Japan and the procurment
system is not does not fit with this uh
kind of uh open source software and
Civic engagement and we there are
digital literacy gaps between
Generations or sector
and Technical problem is uh technical
challenges also we have uh yeah recently
technology evolution is quite rapid so
we have to catch up to uh to understand
the new uh new uh challenges like AI
governances or privacy protection so and
also social Innovation side we have to
uh we need to uh have a way to measure
real social impact this is very
important to uh to expand uh our
community to the other
stakeholders but and also we have uh we
we can see the future Trend and
opportunities uh for example uh AI can
be used for uh making better policy
discussions and the right side images uh
from the uh recent election in Japan and
the some uh
researchers uh Illustrated visualized
and clustered opinions from the uh
citizens and all so that this kind of
software is widely used in Japan uh not
wiely used started by started you uh
yeah uh this uh for example talk to the
city or police is the software uh that
we used and also uh we maybe we can
enhance the policy participatory
platform like this and so second one is
the perfect perfectly match with this
conference so we want we have been
building the digital public goods so
maybe uh connecting to web3 ecosystem we
can build some some of sustainable
funding models or com how we can enhance
communties work by uh creating incentive
mechanisms and also we can uh find we
want to expand the Civic Tech uh close
border collaboration so maybe from this
uh conference maybe we can uh have new
uh projects together let me show some
examples of our project
and we uh organized a matching donation
syst project using simple Grant this is
the open source software uh for uh doing
the uh quad quadratic funding uh
donation so uh we we selected the 18
Civic Tech projects from community and
listed uh this those projects and asked
funding from the to to uh the publicly
and the result uh we uh we prepare
uh $615 us as a matching pool and and we
collected uh ,200 us from uh around a
still small amount of the donation but
we uh we understand how the quadratic
funding Works uh and and Next Step would
be uh we can we will run more rounds and
we want to expand
stakeholders like uh government people
and and also uh we uh we accept we want
to merge the the this mechanism with the
token donation the simple grants is the
uh using the credit credit card donation
so uh we want to expand this more
and last uh project I want to share is
toang
uh this is uh the kind of the Dow tool
simplest way for contribution recording
and re distribution and key challenges
from our activities from da Dao daish
Civic Tech communities uh we have three
main programs like uh TR tracking our
works it's annoying actually uh track
so Civic Tech Community is a Civic Tech
project is U mostly the uh open open
source uh Community like uh work so uh
contribution measurement is bit
difficult uh if it is only the
development side uh maybe the we can
track record by the uh GitHub commit
report uh commit record but uh Civic
Tech Community Civic Tech project
requires many tasks other than the
development so uh and also we often
forget to report completed work and also
uh reward for long-term contribution uh
is uh important for making sustainable
Community uh which makes people to
motivate uh to be motivated and but uh
it's hard to secure funding if the
project is on the early stage uh and
also CH go unnoticed there are so much
unvisible work and how can we reward
those
efforts it is uh that is one one point I
want to we want to solve and also on
boing rather is uh also ke key and so
many people can join easily because it's
it's open but actually it's difficult to
join without help understanding the
community uh understanding the community
is uh takes time so uh we need to uh
create uh we need to have a better uh on
boarding processes and yeah so uh that
why we started toban toban is a role
based reward system so uh
the those features toan has this kind of
features uh it offer offers effective Ro
management this is not a task based
system Ro based uh project owners can
assign and manage
responsibil effect efficiently and also
track contributions from the uh
contributors use P2P token transfers to
even small
contributions and and we said toban can
uh be uh used by to set fair Riv
determine rivs based on role and time
engaged and also quick distribution toan
can distribute Rivers swiftly uh to
large groups we use the we are using the
hats protocol uh like this and so uh the
uh role
can be distributed to some people uh and
also that people can that assigned uh
the people can assign their role to the
this to
subgroups so that uh the role will be
distributed to the contributors and
after getting some rewards uh like a
treasury or or revenues from the uh
project uh the project owners can
distribute that the uh rewards to the uh
contributors so uh this this can be used
not only for the Civic Tech communities
we we for example the uh so uh maybe
toban can be used for The Residency
program housekeeping or essential
workers additional bonuses so uh yeah uh
but this is is just beginning
uh if you are interested in please join
us uh there we have the GitHub report
and and we started TG group and there is
a read developer so please talk to us
and yeah that's all mainly but we have
many use cases let's solve real world
problems with us thank you very
much all right uh do we have any
questions for hell uh in the
audience we do have some time to take a
few
questions you have any
question you can use Mic you guys
okay we do have one how you tackle the
crossborder payment oh it's good
question so uh I think this is for the
uh simple grants program uh we accept
right now current uh currently we just
accept credit credit card uh donation so
but uh maybe we we can expand our
program to the Token donation so so that
to crossb
uh donation uh to to enable crossborder
donation and also uh we uh want to uh
yeah uh we actually we uh participated
uh to the gitcoin round and maybe we can
mix that kind of the
solutions all right uh we do have one
question
here hi um this is matali I actually
wanted to ask you how one of the
challenges you mentioned was
MH and say especially in countries that
have authoritarian governments how how
do you propose um one can like navigate
through these
challenges good question thank you very
much so we
H yeah we have been uh convincing them
that government people to use open
source software uh but the we need to
explain the the value uh about uh using
open source software not only the
technical side but also the uh why uh
they have to care about this so and one
of the reason they uh accepted is the
the efficiency cost cost efficiency
because in Japan there are uh
each city is built the uh their Solution
by scratch it takes so much cost but
it's happening in Japan so I explained
uh and demonstrated to build the
software as a uh some uh to uh we we
actually we built a covid-19 dashboard
for Tokyo Metropolitan government and we
published that source code on the on
GitHub and accept the uh issues and pro
requests after that many people
contributed to uh the improving the soft
to improve software uh and and also
other prefectures uh uh used the
software and same software and using
their data uh to visualize the covid-19
situation so so such kind of
demonstration was really uh useful to
explain why government have to uh choose
open source
license all right I think we can take
these two questions are there any
advices or hard learned lessons you want
to share to people who want to establish
this kind of initiative
oh so hard learn lessons could
be people
uh it's very very difficult to keep uh
long contributions from everyone uh
people have no time to uh keep
contributing to the uh Civic Tech
Community actually uh I'm a founder of
cod for Japan but no
one still working with me uh as a
initial uh member so we have many
generations
uh to continuously so maybe the from
lessons from that is that we you if you
start this convers uh this community you
need to encourage to to to join new to
to encourage people to join and people
leaving is normal but the uh so such
kind of the uh so inviting new people is
is really really important to sustain
the community all right uh so you
partially answered this uh how do you
sustain the momentum of the
decentralized community right so it's
important to share the information what
happening in the community and and also
clear guideline is needed if you want to
start something uh for example we
prepare we have a month three haason so
that you can just come here and Pitch
your ideas or find to find the project
you want to join and also we have slack
workspace to uh communicate with uh yeah
so yeah clear guideline is another piece
of uh that all right cool so our time is
up uh last round of applause for hell
thank you very much so yeah this
concludes our very last talk for day
thank you everyone for coming
ah w
