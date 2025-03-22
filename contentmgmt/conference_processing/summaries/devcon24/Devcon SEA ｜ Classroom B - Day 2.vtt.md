that
[Music]
oh
e
for
m
a m
w
oh e
a
EX
all right GM welcome back so uh
hopefully all of us are here for the
workshop this
morning this is going to be about
finding
bugs which is really what security is
all about finding and fixing bugs
hopefully and uh this is an interesting
format for a workshop we trying this out
um recently so this is going to have 42
tips from the four security researchers
that you see
here 42 why 42 42 is supposedly the
ultimate answer to all questions in the
Galaxy so why not finding bugs as
well and the four security researchers
here I let my smarter colleagues
introduce themselves first with
uran thank you um I am a security
researcher at consensus diligence where
I work mostly on tooling and automation
so you might have used a couple of my
tools uh but I am also a buck Bounty
Hunter so most of my tips today will uh
go into that part of security
research hi everyone I'm dcho um I work
for the red yield I'm a co-founder we do
security for the public benefit of
ethereum ecosystem um and in the past I
used to be a Le aitor open seing for
many years and before that I was a web
developer and
pester hey everyone I'm Nat I'm an
independent security researcher um I
spent four years at chera bits uh where
I did mainly Security reviews and before
that was a blockchain developer for
three years so yeah today my tips are
kind of going to be blockchain Dev
related and security researcher
related fantastic and I'm uh Rajiv so
I've been a security researcher uh
pretty much my whole life started with
ethereum security roughly about uh six
to8 years ago um early participant in
some of the leading audit contest
platforms um and then uh for the last
couple of years I've been a lead
security researcher with speit Cantina
um and in this context um started secum
about 3 years ago so
secum was um was was funded by an
ethereum Foundation Grant and
collaborating with some of the leading
projects in the space the goal was
really to scale ethereum security right
and by that we mean onboarding the next
hundreds and thousands of security
Auditors U to make ethereum safer so
secum is um is really an online
community known for its boot camp check
it out online has monthly quizzes
designed by uh many of the well all all
the people standing here and many many
others in the room as well uh check that
out and um secum also host trustex which
is uh one of the leading ethereum
security focused events so with that we
will kick it off right the first
question we really need to ask is why
right why why are we doing this Workshop
why are we trying to find bugs and as
you can see the whole not not just smart
contracts or OPC and other things right
the whole domain of blockchains right is
really about trust and in this
case finding and fixing bugs is really
one of the biggest um you know technical
risks not just in the base layer in the
layer ones and the layer twos in the
bridges and anything else in between but
also in all the daps right all the smart
contracts that really uh and and all the
glue that holds them to together right
we need to be finding and fixing
bugs why so why is that important I mean
it should be very obvious to many of the
folks many of the security researchers
here but just to sort of put it once
more if we would like ethereum to be the
world computer if we want to really
onboard millions and billions of people
onto the onchain economy and if you
really want eth to be ultrasound money
we need to make it Ultras safe right so
that's really the goal here so with that
um context we'll kick it
off and and this this really sort of
hopefully justifies it right I mean this
is from defi Lama as you can see and I
don't I mean this is probably
representative it really does not
capture all the other uh fishing and
many of the other things that are
draining millions and billions so this
is getting better I mean this graph sort
of gives us a warm fuzzy feeling that
hey we may be getting better but I think
we really have a you know long long path
ahead so with that we'll start with the
tips thank you and the
clicker awesome so all of you are
probably on Twitter uh if you're not
you're quite unique and if you've been
on Twitter and read any of the posts
around bounty hunting security research
uh you see a lot of gr set Focus post
and um I'm not saying hard work and
dedication isn't what's going like
required to be a good security
researcher but I honestly believe that
going into security research with the
mindset of ah I need to grind so hard
work 16 hours a day is the worst
possible approach um if you look at
other Industries like doctors um that
have a similar kind of mindset where
it's like oh I'm going to work so many
shifts uh I work hard if you look at the
amount of incidents that are caused by
people working multiple shifts it's
insane uh and the same thing happens for
security research like I'll be stuck on
a problem for four hours at the end of
the day and the next morning I'll solve
it in five minutes like staying stuck on
a problem just because you feel like you
need to work hard not a good
approach okay tip two scope coping out
targets and not just picking anyone at
random is a pretty good idea when you're
doing bounty hunting there's so many
programs and if you just pick one at
random well it can be a fun approach but
it's probably not that efficient so
probably the primary thing you should
focus on is the amount of time that you
have available closer okay uh probably
what you need to focus on is the amount
of time that you have available on these
Target so uh maybe don't go for like a
bridge
implementation or uh like a an L2 if you
just have a weekend um and of course
like if you're looking to make a living
out of this or a significant amount of
money then don't go for projects that
offer low bounties one thing I actually
look at a lot is not necessarily the
height of the main Bounty which is like
very high I look at the the the Bounty
that's off for the high vulnerability
because that's usually a really good
signal about how much a project actually
cares about security if they won't offer
anything for highs or if their high is
like 10K and their crit is 10 million um
this is just like random
um that's not a good sign that they
actually care about security uh they
just want to yeah prevent the main
things okay tip three try to sleep sort
up okay so this one actually happened to
me uh I was trying to sleep uh and then
well as as it happens my brain is like
oh you were working on this problem
here's the solution and so there I was
like in the middle of the night typing
up a bug report
um the idea here is not to try to work
while you're trying to sleep it's more
so um exploiting the idea that you have
like your brain is doing passive
processing on in while you're doing
random things like trying to sleep or
doing the dishes um and to really
leverage that it's important to not try
to do too many things at the same time
because so for example if you're bounty
hunting on a project don't switch to a
different project just keep doing this
one go for a walk let it process and
find some bugs um
and don't go like watch Netflix and fill
your head with different things because
then you can't like
Leverage this ability of your brain like
um I have a cool example from when I was
in university um was working really hard
on a problem uh like the we had these
days where you had to solve a a
challenge in a day uh kind of hackathon
um and I was like super stuck for like
the first four hours of the day um took
a walk to get lunch passive processing
happens solve the issue like right after
lunch so yeah till they are take some
breaks uh and leverage this passive
processing okay now some tips about how
to approach Buck Bounty
discussions if you're doing Buck
bounties eventually you'll have a
discussion with someone because projects
don't always agree with the impact or
what you found
um Everybody responds differently uh
there can be some emotions involved when
you tell someone their code is broken um
so one of the things that's really
useful is basically learning a little
bit of rhetorics and preparing for
fallacies um people will come up with
arguments that don't work addressing
them or strategies that basically derail
a discussion being prepared for them
will just make your life easier in the
end
another tip on Buck Bounty discussions
is kind of taking the mindset of working
with this project as a business partner
that you might want to do an audit with
uh later um this great to St
communication that's that's much more
productive and much less likely to
result in a situation where you're just
name calling like no your code is
and then they're saying no you can't
find bugs and everything sucks um so
this really uh helps things out there
and as an add benefit if you actually do
end up bu being business marter later uh
you have a much much better
relationship okay then um it's going to
be super useful if you diversify your SC
your skills so with defi there's all
these super useful uh resources like
secum uh um that can help you become
like a security researcher uh but it's
often uh easy to overlook the fact that
learning other things that aren't
necessarily directly related to um defy
or smart contract security is going to
be incredibly useful like learning
quantitative Finance is has been super
helpful for me like there's a couple
topics here uh like for example learning
how compilers work I think is an insane
thing like insanely useful thing to know
because you'll become so much more
familiar with how programming languages
work how solidity Works under the hood
you just get an intuitive sense of how
these things work and that in the end
will help you understand code better
find and find more bugs um it's
also just something that keeps things
interesting you know like after a while
maybe defi gets a little bit boring this
kind of switches it up uh so it's it's
also something uh to have some
fun
okay now some strategies that you can
actually apply uh in uh your buck
hunting
process I think one of the things that
works really well is uh finding a
paradigm and specializing in it so for
example in defi uh you have systems that
provide leverage so what you can do is
become super familiar with all the
things that you need to do to implement
leverage systems and what can go wrong
once you know all these things you can
just quickly go into all the programs
that have some type of Leverage see if
they do everything right and if they do
you just move on to the next project so
this is kind of like a an approach where
you go super BR um and it can be super
efficient what's important here is to
get pick a paradigm that is relatively
unknown or that you think nobody else is
specializing in because that way you
have some competitive Advantage um I um
so I guess leverage and concentrated
liquidity are a little bit old now uh
but I guess like various CK topics uh
can be something right now that there's
not that many security researchers that
specialize in these where uh there might
be uh some some good opportunities um
and I just pick something that you find
interesting to be honest uh because
that's the best way uh to to learn and
go about this
all that was the go broad strategy now
for the go deep strategy
um instead of just going for a bunch of
projects for one topic you can pick one
project and then go deep on that one
um this is an approach I usually take
because I have like I'm very time
constrained I do like weekends like
short weeks um and the approach I
basically take is I I pick a project and
then I take some time to explore it and
identify all the like the interesting
bits the risky bits uh the parts that I
think are going to be super difficult to
implement right if I were to implement
them myself and then I basically just go
have a look at those um and see if they
if they actually made the mistakes that
I think uh they would have um and that's
actually like a super time efficient uh
approach when you when you think about
it uh and this kind of exploits the fact
that as a bounty hunter you're not an
auditor as a bounty hunter you don't
care about finding all the bugs it
doesn't matter like it doesn't matter if
something is left after you go by as an
aitor that kind of sucks if that happens
but as a bounty hunter we just want to
find a bug as soon as possible and this
approach will allow us to do that we
we'll just have to look at like the
critical code the code that does
liquidations uh we don't have to look at
all the like boring bits like usually
you don't look at like the erc20
contracts where they do all the
interfacing right I mean you could but
that's not the the go deep
approach tip nine read the documentation
okay so design mistakes can be critical
people come up with interesting ideas
that fundamentally don't work or are
super hard to do right and from reading
the documentation uh this has happened
to me this has happened to other people
uh you can already notice some bugs and
then you just have to go into codes into
the code to
see whether like the bug you think is
there is going to be actually there
quick side note there documentation
usually out of date
uh fortunately unfortunately depends on
how you look at it um and uh there just
like there's going to be cases where you
find a bug in the design a bug that's
been there but they already like came up
with something that prevented it and
just didn't document it at
all even if you don't find anything
reading documentation will set you up
for Success because you'll have a good
General understanding of what the code
is doing um which is like the best
foundation to actually get started so if
you like when I do
the go deep approach I actually the
explore phase for me is reading the
documentation first um because with this
documentation in mind like actually
starting to read the code is going to be
super is more going to be more
productive because you have some some
context ual awareness of where
everything fits in the in the big
picture
then for my final tip uh this is kind of
a mental model I started applying myself
is when you are reading through a code
base you usually notice like a these
tricks or gadgets
where um it's not really a vulnerability
per se like even if you would sub
might be an informational or law but
it's these tricks that allow you to do
things in a system that are OD or
usually not supposed to happen and even
though these tricks are kind of useless
on their
own they are usually involved in um what
you would call a killchain so critical
vulnerabilities generally aren't
critical vulnerabilities not single bugs
but they are guilt chains and kill
chains are basically a sequence of stabs
or sequence of bugs that you string
together to achieve a critical impact
and
by keeping track of these little tricks
you find while reading the code base you
set yourself up for Success when you
find an actual bug that's maybe not
exploitable or easily exploitable
directly but when you apply your tricks
it suddenly becomes like a super easy
crit um
and just making a list or keeping a list
on a piece of paper or whatever note
taking up you prefer Apple notes could
be whatever uh just keeping like a
bullet pointed list hey I can trick the
system into doing this uh it's not a
security risk but it might be
helpful that's going to set you up for
success in building these skill chains
and basically escalating a vulnerability
from maybe medium or high to a critical
with a lot of impact all right with that
I'll give it over
to
[Applause]
Nat all right just a raise of hands how
many of you here are
developers okay a good chunk um all
right so my next few tips um as I
mentioned before I'm going to kind of
split between um develop ER based and
security researcher based just because
um I guess I've been a developer for
almost as long as I was a as I am a
security researcher um and it kind of
ties into even my current
roles all right so tip one is um
architect first code later um there's
nothing worse than a as a security
researcher or a developer than trying to
fix your bugs and then realizing that
one bug fix results in something else
happening which means you can't fix it
anymore and you have to Band-Aid patch
another thing and then that thing can't
be fixed because you have to Band-Aid
patch another thing um as a security
researcher that nothing is more
dangerous than this but also as a
developer it becomes really hard to
manipulate your code to add new features
um to add behavior um when you have new
code that you want to add um and at the
end of the day it makes your code much
harder to read um that means when you
bring new developers on board um that's
more time it takes for a developer to
understand your system um and more time
for security researchers in a review or
in a bug bounty to understand what
you're trying to do um I think this is
probably um one of the most uh
underrated techniques is just to really
think about your code um figure out how
do you what what do you want your system
to do um how do you want to build it um
identify you know the architecture of
your contracts of of whatever your um
system is supposed to do um and code it
later and I know that's hard because
even I tend to sit at a computer and
just write code um but I will say for a
project that go under goes continuous
development and continuous features um
following this kind of practice makes um
just reading that code much
easier this is kind of related to maybe
one of the previous tips um document
everything I think from a security
researcher point of view there's so many
issues that we try to uh find in code
bases and they're because they're either
wrong assumptions or invariants that
maybe aren't correct
um yeah sure the documentation might not
accurately reflect what the contract or
the co code is supposed to do um but as
a developer putting the actual um effort
into uh like documenting what you want
your system to do um how certain
functions work what the expectations are
um that can do a lot to actually helping
um other people understand your code I
think there's also been a lot of times
looking out certain functions um certain
code bases and then realizing that
everything all the documentation doesn't
actually match the implementation and
then for security researchers we have to
spend a lot of time trying to figure out
all right if that documentation or if
that line isn't correct what is it
actually doing um it can help save a lot
of time um in order to bring people on
board as
well all right this one I'm I'm sorry
for all your develop developers but
simultaneously test and code um yeah I
know tests aren't that fun to write and
I've been in that space I've been in
that mindset um but I will say that it
does help you think about your
invariance it does think help you or
forces you to think about how you want
your system to work um and it forces you
to like actually test the outputs of
your function which you wouldn't be
doing if you were just writing the
function um you wouldn't necessarily be
thinking about um how a function is
supposed to behave um if you weren't
actually writing the test with it this
can help with at the very least
extending your unit tests extending your
test cases um such that sure maybe your
test your test coverage may not be 100%
but it will be higher than if you were
coding and then testing
afterwards it also helps to use this
method to test for edge cases um because
if you're forcing yourself to say like
there's like a function with an if
statement that covers like different
Corner
cases having a test for that means that
you're also increasing your coverage
there and I think there's kind of a a
really useful use case for these unit
tests is essentially finding bugs before
your Security review or finding bugs
before your bug
Bounty all right um this one is uh kind
of related to what I'm saying before is
trying to automate as much as you can um
there's going to be a lot of bugs when
you write your code that that's already
a known Factor um the more time that you
put in your development process to um
documenting to testing um the more bugs
you'll find when like your code is going
undergoing development and also the
easier it is generally to fix those
issues such that hopefully when you get
to your Security review or your future
security practices um hopefully there's
less low hanging fruit so that the
security researchers can actually focus
on the really fun technical um
architectural maybe even like protocol
level um design concerns rather than we
found another re-entrancy here um
explodable here with this token because
is that something you could find with a
tool and it would save you it would
maximize how you use your Security
reviews um in in a better
way this last tip for developers is um
kind of higher level not necessarily in
the weeds um is proactively trying to
figure out how can you increase security
within your life cycle how do you what
are processes that you can use um in
order to find bugs during development um
such that your bugs that found that are
found future um in kind of the auditing
side or um the kind of further security
side um are are the the big ones
um generally the smaller the code the I
mean the the bugs have less impact
within the system to fix um and so the
more bugs that you find
while you're writing your code the
better for your
code all right this is kind of um
flip-flopping tracks because I am also
um or mainly a security researcher now
um so I guess raise of hands how many of
you are security researchers or
interested in heading that
direction okay um
then let's get started um this next tip
is preemptively ask questions and
preemptively identify all of the
assumptions that developers are making
and this ties kind of into the previous
recommendation for developers about
documenting your system nothing is
harder than trying to identify what did
you actually try to build in the first
place um a lot of the time I'll look at
a code base and then realize yeah that I
think that's what was intended I'm not
entirely sure um here's me looking at
the code base here's what I think it's
supposed to do but um it's really hard
to have that clarification and if you
make a wrong assumption during your code
review I mean you're you're you could be
missing a bunch of bugs um and and
issues within the actual code because
you misunderstood how it was supposed to
be used so for that I would
recommend collaborating with your
security team collaborating with the
developers um make sure that you take
the time and the effort to identify all
the assumptions that you're making in
your Security review um and make sure
that that's aligned with what how
developers intended to users to use
their
system all right this one is a bit of an
overlap as well um but essentially to as
a security re researcher build building
a mental model of the code base um is
incredibly important because um and and
this um graphic is from uh the most I
guess Sherlock Holmes where he kind of
references um thinking about like
different concepts in terms of a mine
castle and where he can um kind
of figure out how to um categorize
information into this um kind of
strategic uh model that he can kind of
be able to parse through information um
be able to understand things and then be
able to bounce
ideas as a security researcher this is
super important just because um once you
have this mental model of whatever code
base you're looking at now you can start
to understand okay this is how um you
know this particular flow Works um this
is how developers intended um this
certain flow to progress um and then you
can look for deviations and assumptions
where they can might they might go wrong
um a lot of the times this helps with um
kind of taking a break and then you can
be able to really understand like
different impacts um of like different
issues and and especially a kind of
higher higher level view of the system
um understanding just like how the code
base was built and how it works goes a
long
way all right this next tip is to learn
your tools as a security researcher
there's endless number of tools that you
can use um to verify whether developers
are doing things correctly um endless
number of um different like fuzzing
Integrations verification Integrations
that you can check things and I think
there's far too much conversation about
which is better I don't think that's a
productive discussion um instead I think
it's more important for um security
researchers to really sit down play with
each of these tools figure out when does
when do they come in handy when are they
most powerful um and really learn how to
use them um I think there's also endless
resources on how to use these um and at
least for me as a developer I just have
so much fun playing around with these I
think
um the more you play around with
different tooling and the more you play
around with um comparisons between like
use for example like um fuzzing a code
base um or like uh writing unit tests on
a code base I think the easier it will
be to test the code um and playing
around with um the code base with the
these tools that helps you in a
different way because with code then you
can test with test the code base you can
kind of see okay what are the different
branches within your function how do you
invoke certain um like if statements um
how do you you know Trigger or revert
and it really gives you a good idea of
how the system works so I guess the T
tldr of this is really just play around
with as many tools as you can and see
where they help you the
most as a security researcher I've
realized that um how developers intended
users to use their system never really
matches to how users intend to use it I
think that's just because um developers
have an assumption of you know this is
the one flow that users are going to use
and it's just this is this is it um and
users are always creative in terms of
arguments or just like the ways that
they call Smart contracts um any kind of
any potential deviation in these two
things can be um a fairly big bug um and
can result in like an impact in the
system um so it is one area to look
at my last tip is to lean on each
other's strengths I think um from a
security researcher side um I mean I I I
was kind of sitting in in both sides
before um but as a security researcher
they bring kind of understanding of you
know the security implications of in the
system um security kind of um tooling
and and knowledge there developers
usually understand how they want their
system to be used kind of the more um
Strate IC side and I think for a
security review you can really take
advantage of those two things um and
really collaborate with each other and
lean on each other's strength to
maximize or rather to shorten um the
amount of time it takes both parties to
understand a code base and then to
maximize the number of bugs you find
during your
review all right with that I'll pass it
off to
Tino hello hello hello hi everyone let's
put the
stopwatch thank you hi everyone nice to
see you here and thank you for coming I
know it's early some of you went
partying last night probably um
hopefully not too hard um yeah so the
idea is continuing talking about these
tips uh for security researchers for
developers um nice to see many
developers in the room next time perhaps
you can put like security researchers on
one side developers on the other and
like we throw each other stuff or
something like that just to get it
started uh but anyway yeah
let's let's be honest okay I don't think
many of us here I include myself we are
not going to invent the next new big
thing right uh it's probably the case
that we are iterating on something that
somebody else in the past built or that
somebody else in the past
found so it might make sense to learn
from history and to learn from what
somebody else found or what somebody
else built uh to try to secure the thing
that we are doing that we are reviewing
so for example you will find uh
particular in crypto that we are very
good at publishing things is not usual
in the rest of the security industry uh
to public audit reports you should take
advantage of that this is just one
example of Cypher solo it where you will
find a basically a database of issues
that has been that have been reported in
the past by many security researchers uh
across multiple platforms auditing
companies if you don't want to use this
you can go know trail of bits I think
publishes reports open sing publishes
consens D publes Sigma Prime does the
same and I could go on and on and on so
I'm not saying that you should read
other reports like you read a novel but
probably you should at least scheme
through them if you are building a new
protocol H that I know it's a defi Ling
stuff or some Dex or some whatever that
you're building next uh go see if
there's some similar project out there
that has done similar things to you that
probably the answer is yes and go read
the issues and probably you will find
good stuff um just to double check if
you're not missing out on something it's
sad when we see the out there in the
community the same and same and same
issues being repeated again so please I
don't know take a look this or many
other resources out
there we already talked about this uh
but I just want to reinforce the idea um
particularly for for people doing
security research out here it's very
difficult to understand to what extent
you should go deep to what extent you
should go white uh there's no clear
answer there's never a clear answer uh
my only tip here is uh whenever you are
very mat in depths of a code base be
careful okay um it's very easy to get
entangled in I know line 250 of that a
th000 line assembly code that you're
reviewing and you end up finding
something very cool that I know you can
do something very unexpected in that
function but is very hard to sum out uh
because you need to find the actual
attack Vector you need to understand
impact in the project and to understand
impact you should have context how many
times have you found something to then
realize that well yeah but nobody can
exploit this um if you're a little bit
evil you might end up reporting that
still to the developers just to fight
with them and they will end up telling
you that well it's not exploitable so zo
out have context understand where you
are standing understand the expected use
cases H an issue could be an issue for
you but if the system is not actually
expected to be used that way I don't
know if it's not expected to integrate
with that other protocol that you're
thinking about or is not respected to
use that token that you're thinking
about your issue won't make sense so so
uh have in mind these kind of
things di Mission returns uh are a I
know something that I struggle with and
actually I have questions I don't have
tips uh I will borrow tips from you if
you have some silar bullets to solve
this um I usually don't know to what
extent I should be chasing down backs I
mean it will depend on the kind of
Engagement that you're doing right so I
will talk about this later but auditing
is not back hunting and it's not doing
contest for example so so to what extent
you should be chasing out bags um to
what extent you should be going into
that rabit hole when should should you
stop probably experience will tell you
something about
it uh you will start growing some
intuitions little by little on to what
extent you should be yeah going down
certain paths and not choosing others
then when it comes to reporting doing
Prof Concepts is also a place where we
lose ourselves as security
people um how much detail should you put
in that how
many I know how much infrastructure
should you be setting up to test that
bag you found in that bridge with that
connects a thousand layer threes and
fours and whatever uh sometimes it's
very complicated and you might end up
losing too much time on that I've
been sometimes like a week trying to set
up a whole test n environment to try out
an exploit uh just to realize that then
when I reported perhaps it wasn't the
case or the proof of concept it's too
complicated to run or I end up debagging
the my own proof of concept instead of
deying the actual code that I need to
review so again just uh questions to
think about things to
consider and then the last one I'm not a
very big fan of uh this new security
contest but some people in the room
might be um you will find this
escalation Wars if you're not familiar
with it essentially uh in contest you
will find people like competing to
submit bags at some point in time there
I think this is true in all in many
platforms but they all do the similar
things but not exactly the same uh
people will start fighting each other
just to um escalate their issues and try
to make them more severe or to fight
back the judges or whatever and you will
see like endless threats of people
throwing at each other um and
spending precious time on that while
they could be doing something more
valuable for the ecosystem um but but
again I've been in some cases there and
I know the feeling and it's very hard to
to understand to what extent we should
be doing it uh but anyway dimin
returns okay diagrams yes I love this
part as a security researcher I'm
a visual thinker so that means that I
often times find myself like drawing
stuff just to think about the things
that I want to do I also write a lot and
I will told you right in then uh but
let's talk diagrams now I use diagrams
to understand systems and this I and I
do different kind of uh level of details
in diagrams this was me for example
trying to understand account obstruction
uh in the past uh and I ended up drawing
this as I was going through the code
through documentation and everything I
was just drawing stuff and trying to
understand what I was seeing in this
case it's more kind of an architectural
diagram I don't know I don't even think
about it I just write compon components
and I write names and and try to see
which are which are the actors how are
the relationships and this at least for
me is very useful uh perhaps for you too
so take a look at it and perhaps you you
will find something
valuable then I do some other things uh
in terms of tyam I could go into more
detail with them in this case this is
was me just thinking about the them
buneri this is kind of a set of security
challenges that I created this is one of
the solutions for one of them so I was
explaining this at DSS and I Ed a
diagram to explain the actual solution
so you will see me like doing function
calls and usually drawing where the
funds and where we should be putting the
funds and everything this just one
example in real a probably I will be
doing uh bigger things such as this h i
I do go in depth sometimes so this was
me back hunting in ler um so in this
case I was review main at contracts and
I need kind of to create a mental map of
how the contracts work and how they
interact with each other and where are
the addresses and then I would use like
uh yeah which are the EAS in this case
there's a multi in there and then I
would try to understand how fees are
distributed and I also use diagrams and
I they would try to understand uh
storage layout and I would also use
diagrams and so on and so forth right so
uh you might say that I'm spending too
much time drawing stuff and not looking
at code but this is just the way I think
uh often times and I find this valuable
uh in many cases
I ended up finding bags just by looking
at diagrams and trying to understand how
actors and contract relate to each other
and sometimes I end up kinding finding
kind of holes in my diagrams so I
realize that people can call things that
shouldn't be able to be
called so yeah and well you can use
whatever tool right so you can use
online tools your whiteboards in your
rooms in your offices whatever that you
that you feel like
um moving out of the comfort zone is
another good thing uh that we should be
all trying to do in many aspects of life
but let's just keep with security
research uh I just put that picture of
that book because I like it if you want
to read it and give it a try uh it has a
chapter about the comfort zone so um if
you're a security researcher uh
probably sometimes you will yeah you
will find yourself uh Growing Experience
in certain fields in certain C let's
call them of vulnerabilities or or even
protocols uh but sometimes it's good to
do something else earlier this year I
was um I mean I've been for most of my
career I've been auditing a solid smart
contracts uh so I don't have that much
experience Ting noes and infrastructure
for example but ear earlier this year uh
there was a contest I think it was on
Cantina for blast and I had the chance
to either go for the smart contracts I
mean I didn't have much time so I had to
choose smart contracts or go for the
note H which was written in goang it was
a fork of
gu and I decided to go for GU H for the
fork uh and I didn't look at the Smart
contracts I missed uh the all the fun
that people had with the smart
contracts um but I did have lots of fun
reviewing that um and I learned a lot
and I ended up finding issues and we did
quite well
but I wouldn't have I wouldn't have said
that I was a an auditor of Goan code uh
but I ended up finding things and that
only happened just because I I moved out
of the comfort zone and I started
letting go I had never written H
anything about
goang um so I learned about it I did a
few courses uh I prepared myself I went
in there and end up finding things and
even if you don't find things it might
be the case that you end up learning
which is always cool and the things that
you learn you can actually use in the
next contest that you do and little by
little you can specialize in that new
technology that you're
exploring um so I'm not saying you
should always be doing this otherwise
it's like you not specializing in
anything but every now and then see
where you can do something else uh if
you are a smart contract aitor see where
you can AIT a Noe or the the other way
around right um just give it a try and
see and then you can tell me about
it so writing I told you that I'm a
visual thinker but I also like writing a
lot uh two articles that I recommend
essays about the from from Paul Graham
that I recommend reading about writing
and importance of writing particularly
for thinking um I do very much agree
with the idea that you only know
something if you can write about it and
you can explain that to something to
someone someone else by writing it and
that's the only way I'm sure that I
understand something probably if you
follow me online H you know that I write
a lot and I publish articles on on on
the blog of the red Guild and that's the
way I think uh and I spend a lot of time
writing uh so when I do all I explain my
functions in writing I take down notes
and little line by line and explain
myself what the function is
doing and in that way I can find bags uh
because what I write sometimes doesn't
make
sense also when we exploring a new code
base it's the case that uh we explore
many different uh lines of
thoughts but you cannot be jamping
around uh many lines of thought right I
usually I'm single threaded so I can
only do one thing right uh so I write
down the other ideas I have and I don't
want to forget them so I write I write
them down and then I come back to them
later in the next day or whatever and to
communicate I always say
that secur doing security for me uh
particularly for Auditors 50% finding
bus and 50% communicating bus you might
be the best finding a bag but if you
cannot actually write a good report and
communicate that to someone else and
convince that someone else that you're
right about it it doesn't make any sense
so uh do Le to write is very very very
important and it's also somewhat fun uh
so I do recommend
that a particular strategy to find bugs
uh It's just sometimes going for what's
not
tested um what I sometimes do is
essentially jump into a test Suite see
which are the public functions in the
contract that are never called and start
exploring there it's usually the case
that whenever there's a public function
that is never call from the test it
could be yeah it's sometimes the case
that there might be something at least
at least to explore in that
sense then what I would do is that I
take advantage of the ex existing tests
I modify them I hook into them I rework
them I bring them WR I I do whatever I
want with the tests uh but just because
I don't want to be building tests from
scratch right so I want to reuse the
existing test Suite that's what what
that's why it's very important to always
uh take a look at them try to use them
run them and see if if it helps
you we could talk a little bit more
about this uh I don't want to extend
myself uh I do have some minutes left
according to Rajiv he told me I had some
extra time um so for me oing is not back
hunting back hunting is not contest and
contest are not auditing the skills the
mindset the experience the intuitions
the way that you play these games is
totally different and you might be the
best auditor out there I I consider
myself a good Auditor in the past and
then I moved to contest and I realized
that people play a different kind of
game in there uh and perhaps I wasn't
the best doing that and back country is
the same right uh in noting you will
find yourself doing client facing work
you will find yourself going deep and
going wide and going very detailed and
writing very detailed reports and
talking a lot with developers uh not
necessarily discussing but just thinking
along along with them just to to find
more vulnerabilities and backs and you
have access to to these developers often
times you also feel the responsibility
when you're an auditor particularly if
you're leading AIT you feel responsible
for what you're doing which might not be
H sometimes the case if you're just back
hunting right back hunting you're just
perhaps a solar back Hunter you are uh
um shitless in your home just doing
whatever you want and looking at some
code sometimes you look it more you look
less you you might not feel as
responsible as other
people um you can go as deep as you as
you want you can just get one win and
you're done Auditors might need to find
everything it's it's a very different
mindset and in contest well contest for
me are just like Madness um
some people find it fun uh sometimes I
do but uh again it's a different kind of
game you should be finding sometimes
specific BS that are more unique uh you
should be thinking differently about H
report some people even influence judges
some people throw at each other
just to escalate their bags I mean they
are a different mindset too so uh if
you're an aitor perhaps you're not a
back Hunter and perhaps you're not good
at contest or the other around but
choose your ground and know what you're
doing uh I about to wrap up
so whatever ground you choose H try to
be professional we see lots of people on
Twitter um not representing very well
the security community in many ways so I
always try to share with people these
ideas of being assertive without being
aggressive stand your ground but not
necessarily being aggressive with
developers being pathetic to them and
new developers with have security
research too we try we try to always be
as thought full as possible we take our
time uh to think about the things we
want to report the things I want to
explore the things that we share with
you um always putting as much attention
to detail as possible this is a big uh
thing to me uh paying attention to
details in
reports to the code when I'm when trying
to find uh
bags so very being very thorough being
sometimes slow and being thoughtful
about what I do and always trying to be
kind to each other I I this is the kind
of the hippie part but trying to be kind
to each other and respectful uh we all
have uh we are humans we have friends
family problems uh we can get very
adversarial sometimes uh but as long as
we are respectful to each other uh and
we don't each other publicly on
Twitter uh sometimes it could be
necessary a little bit um but please
avoid those report on Twitter
or you just public shaming somebody
somebody that is not answering your
report that you just submitted 15
minutes ago and it's ends up being an
informational or whatever uh so try to
be professional uh we TR to be
a big security Community
here wrapping up have patience
everything takes time particularly when
you're doing security becoming a
security researcher take time finding
backs takes time reporting triaging
judging escalations let's not even talk
about how payment sometime takes endless
time so yeah it's a game of patience
lots of people coming to me what should
I do how should I get started how should
I find this and this and that and what I
always do is be patient uh because uh we
are here for the long
run Rajiv you're up thank you
great good to see uh people sticking
around till the 30th tip so uh people
may be getting hungry but I would
request you to stick stick around for 12
more uh there is a fun quiz at the end
with rewards which may be
interesting all right so uh the next 10
tips more uh memes I would say um I
would like like us to zoom zoom out
right so we've had fantastic tips sort
of covering both the security researcher
mindset good to see developers as well
so covering that as well and by the way
on that we need we need more people in
security so if you're devs then do
consider not just securing your own code
base um and having that attacker mindset
security mindset but do consider looking
into security getting into more of
security as well so in this case the
first thing is really both as a Dev as
well as a security researcher is to zoom
out and sort of
assess the protocol that you're building
or reviewing right first thing is I mean
look at this so Billy somebody hands him
or her um money right but would like to
sort of take time to explain the
importance of smart contract security
but of course you know YOLO go and dgen
mode look at what the assets are put it
into the vending machine do some actions
and then you know make money or regret
right so this is I mean this may seem
like fun but it's all about the assets
right I mean that's that's why we here
all these assets are being put on the
blockchain in U various
forms what are those assets as a
protocol you obviously will have a very
clear view as a developer but as a
security researcher this is the first
thing you need to see what tokens right
where are they being
held where is it entering the system and
more importantly where is it exiting the
system because attackers are really
looking to exit out of the system with
these assets right so having this mental
model documentation of assets is really
critical and of course actors right I
mean these actors could be users of your
system could be abusers could be
attackers could be um developers
themselves in in the sense of you know
all the code that's gone in and
potential um
impacts negative impacts as well I'll
get into more more of that later it
could be even the governance right I
mean here we are talking about smart
contracts in general right so it could
be even the governance and how does that
how does governance as an
actor factor in to your threat model or
trust model so that has to be considered
and of course all the actions right so
what are what are the various actions uh
that can be taken by these actors when
are these actors uh when are these
actions happening when does it make
sense when doesn't it make sense right I
mean these these will be very clear to
the developers or the security
researchers once in the context of the
protocol but you really have to zoom out
and think about these very
consciously and how are these actions
impacting the assets how are they
impacting the factors and why does this
all make sense so that is at a 100,000
foot level I think that is really what
this is really what security is about so
if you go back I mean uh for for uh
those who are familiar with security
Theory this is really what an access
control matrixes you have the subjects
operating on the objects you have the
Matrix of permissions right so this is
fundamentally what we are looking
at all right the second meme so you may
see sort of repeating
repetitive um things in the tips that
we've we've been talking about but that
this is what we doing consciously to
drive these points home
right as a
developer you may have an expectation of
your ideal users right or the users of
your protocol but the reality is going
to be very different
and as a security researcher this is
something you have to pay you know great
attention to right again
users and
abusers how does this particular
protocol get normally um I mean how does
it function normally what's the normal
behavior but then that is that is fine
we need to build that model but what we
are looking at is the anomaly right how
can this go wrong now not all anomaly is
bad right I mean obviously there are so
many things U that we don't intend to
capture in the protocol which is fine
and not every anomaly is a security
issue right it's really a small subset
of that is what we call as bugs right
but really vulnerabilities that really
impact the system that affect the assets
that affect the actors drain it out and
and everything in between so this is
something that is
super critical that all the developers
should really be thinking about right
how is this going to be used how is this
going to be abused the reality is going
to be right more than one user I mean
the the monkeys on the keyboard sort of
an analogy right so really pay attention
to this and this is not just the users I
mean this could be again extending to
all the actors right it could be the
governance as well you've seen whole
bunch of governance attacks where um it
was wasn't within the attack the threat
model to really consider something like
that happening but that is really what
happens and for the users right I mean
this applies really to every scenario so
as as a user or a security researcher
one I mean we could expect uh on the
flip side a particular sort of a
behavior from the developers right but
of course we have scams we have Rock
pulls so even there the reality might
really not match what our expectation is
so for all the users developers and the
security researchers there's really a
message
here great so third one third
meme challenge assumptions I mean we are
saying this repeatedly in different you
know using different memes different
ways of saying it but this is really the
root of all
bugs right the assumptions made by the
developer about the user the assumptions
made by the security researcher about
the code base about the developer the
assumptions made by the developer and
the security researcher about the users
I mean all combinations right so this
is this is really the
root of anything that's wrong with
security right so question everything as
a developer
question question all possible scenarios
all the different ways that you know
maybe you have a design maybe you have a
spec from uh from your team but how can
this be used right how can this be
abused question everything every
scenario all that has to be captured
within your model and as a security
researcher again question everything
right I mean ask Nat mentioned uh Tino
as well about
questioning everything to yourself and
as much as you can to the protocol to
the developer team as well right because
if we do not understand as a security
researcher if you do not understand what
this is supposed to do how is this going
to be used we certainly cannot
understand how this is going to be
abused right so as much as possible
obviously practically there's obviously
a limit it's all time boxed so figure
out you know and this uh depends on the
model as well so if you're doing a
collaborative review you know you have
quite a bit of leeway in terms of asking
questions if you're doing a contest
maybe not as much if you're doing a bug
mounty again very limited ways of uh
sort of questioning the protocol about
every U knit and you know Nitty Gritty
detail that you may want to know about
right but try to get an idea of who
again actors actions assets who is it
what is it being done when and where
right so that is really critical
question
everything and security is nothing
without discovering the misuse scenarios
right again repeating myself use and
misuse critical
and abuse is really a subset of misuse
so figuring out just the various misuse
things is not going to um you know do
much as a security researcher you have
to figure out the abuse cases and the
abuse cases are really the
vulnerabilities we'll talk about the
impact in a bit and really to map out
what the attack surface is right so for
a developer in this case it is really to
reduce the attack
surface of your protocol of your Cod
good
base reduce it so that I mean one way to
reduce it is to reduce the complexity
right reduce the number of um actions
that can be done figure out what is
really critical there is a concept
called guarded launch you know maybe you
can do it in
steps various ways to uh reduce attack
surface because if you reduce it then
the potential for abuse is much lower
right so the probability goes
down and your actors and attackers I
mean we we are in the blockchain
environment right so in this case we
really looking at sort of um the worst
case scenarios from an adversarial um
mindset anything and everything can be
attacked and will be attacked and by
anyone who is a part of the system so we
really looking at a very uh High bar
right when it comes to to who that
attacker is unlike the web 2 or the web
one world we do not have an good idea of
who the Insiders are and who The
Outsiders are who what is a
characterization of uh the the normal
users of my system so it's a really
adversarial mindset um that should be
kept in mind when you're designing
coding and
reviewing great so um severity Tino
talked about this in the context of
bounties and and uh contest
this is probably more relevant for the
security researchers right if we do
determine and communicate like Tino said
what the impact is then it's of no use
right I mean it's probably going to be
like an informational finding maybe a
low severity one but not much but
quantifying that is super critical and
the way the sort of the rule of thumb is
to see
evaluate the assets are they being lost
are they being locked is it temporary
really objective in terms of how we
deter objective in terms of how we
determine
it but likelihood which is really the
probability or bounties right this is
again I mean if you're evaluating uh if
you're one of the judges or if you're on
the team looking at U any of these
contest results or Bounty submissions
this is something that you need to pay
attention to right and and it It's
Tricky but it is really
important great so for the star Star
Wars
fans it's really all about being
consistent for the developers it's about
being consistent with your
checks in different parts of your
codebase on the various assets on the
various actors and
actions if these checks are
inconsistent then it leads to
inconsistent trans transitions right in
your protocol and those result in
inconsistent
State and that is again the root of all
bucks right I mean these may seem very
obvious very
simplistic but at 100,000 foot level
that's what it really is right so if you
go back to the code that you're looking
at uh that you're developing or the or
you're reviewing look for these patterns
of checks anything that's done in one
place that is missing other places that
is uh you know it's a big red flag it's
a good starting
point
right so web
from web 2 right and it's I think I've
seen it used in the context of
dependencies where the the small uh
block that you see marked out as bug is
really a dependency for almost
everything that you run but it is small
nobody really knows about it nobody
really knows when it was developed and
whether it's being maintained and
breaking that right could really bring
down the entire space so in the case of
web 3 I think um it is very similar and
I think it is even worse because web web
many talks here that talk about the web
two aspect of security so we won't get
into that
but the bugs in web 3 can be anywhere
and really there everywhere at this
point so this may paint a very sort of
red nasty sort of uh uh picture uh very
pessimistic Outlook but I think we
getting better right I mean it's it's
worse it was worse it also sort of
signals the maturity of uh the entire
stack then space but these are getting
better right and as we do this we're
also adding a lot more um lot more
codebase lot of you know a lot of new
infra a lot of new tooling so it's sort
of um uh cat and mouse game right you
you fix these bugs but there are new
ones there's new code bases and there
are new bugs in
them so for for the developers I guess
the message here is that every line of
your code codebase m matters right so
just be very conscious about everything
that is getting into your code base try
to see if it is really required or not
and for the reviewers for the security
researchers read every line that's not
enough read between the lines as
well and what this means
is what it's it's relatively easier to
sort of find bugs in the code that you
see
but it's much harder to imagine things
to imagine bugs in the parts that you
don't
see right so do that and
uh and that even then it's not enough
right so it's uh it's almost um an
unreachable challenge for the security
researchers because you have to read
every line between the lines and Beyond
the Lines Beyond the Lines is really
about the dependencies that you see here
right it's not enough if you look at
what your code base is but all the other
code bases I mean we really building the
Legos of the future or the the the
financial uh D blocks the future
internet 3.0 piure term right if we want
to build that
then they have to work together and if
they have to work together we cannot
afford to have security issues in the
glue that is connecting them right so
that is that that is the real part here
so in the case of web3 smart contract
specifically you may be looking at
dependencies on oracles right I mean
dependencies on other protocols
dependencies on your web tooling all
those can have bugs and has to be within
uh your uh uh threat
model right so next meme for all the
Matrix fans here bugs are really
everywhere
right they're really there in every code
base it's it's pretty much a matter of
um what incentives are right for the
developers or the researchers to find
them so the message here is look at
what's there and what's
missing for all the developers think
like an attacker right the security
mindset how can it be broken so that is
really the sort of the repetitive
message here and for the researchers
obviously think like that but also act
like a white hat right uh we can get
into more of those stories later on I
think uh yuran had um had a talk earlier
on with uh talking about bounties
stories at the security
conference okay so this again is
invariance
Right a lot of security well lot of it
in the smart contract space in in your
codebase boils down to
invariance invariance is another term
properties what property should hold in
your code base what properties should
not hold good in this code base right
and these have to
be consciously thought about right I
mean this comes up in the context of uh
formal verification typically where
you'll have to specify the invariance
and then use a checker but then even
without
that as as a developer before you write
a line of code right think
about what should what invariant should
the satisfy what are the properties that
I'm actually coding for
and document it great if it can be a
formal specification fantastic right
because then we can use formal
verification
tools but let's even lower the bar right
write it in plain
English what is my code supposed to
do that is super critical for all the
researchers and reviewers who look at
your code base Nat talked about this as
well document
everything right put it in code comons
inline comments Communications is going
to be super critical in the space and
all of us are sort of repeating all this
over and over again because it's really
all these fundamental principles that
apply so read as a security researcher
read all this hopefully the devs have
written up all
this
ask ask questions be direct in asking
your uh protocol teams or your on your
favorite contest or Bounty platforms ask
you may not get the answer but it
doesn't
hurt and ultimately try to infer some of
these if you don't get the answers right
so that's that's possible as well
there's a fantastic area of research
where you can actually infer invariant
and a simple way of thinking about it is
inconsistent checks if there are some
checks if there are checks in some
places and not then it's either an
invariant or those missing checks are
sort of exceptional paths so try to
infer looking at clues in the code and
docs and so
on all right the the final tip is just
find it right I mean we tend to um
talk a lot think a lot but ultimately it
is really
about reading the code right and and the
good good part of the space is most of
these Protocols
are open- Source they have verified
sources so you can actually look at the
code base right and know that okay it's
hopefully the same one that was reviewed
was deployed look at the code there is
no buck free code it may not be the you
know critical criticals or the highs but
it may be the lows and the infos but
there are bugs right read the code find
the bugs and like all of us have said
both for devs and for
researchers I think success you know we
may think of overnight successes but we
don't see the sort of the we see the tip
of the iceberg but there is a lot of
preparation that people have done right
people have spent years decades in
different different ways practice and
then ultimately
patience so I have I have the pleasure
of U also sort of summarizing a lot of
all these
steps we'll do that in the next two um
next two slides and then we will have
time for questions we have 10 minutes
and then there's also a fun
contest so quickly right for devs before
you code
specify and design and after and during
you Code test right so this is not I
mean it it's it's written as sort of a
linear thing but it's really sort of a
cyclical thing it it happens it's a
helical model so do that repeatedly
think about assets actors and actions
actions think about where assets leave
your
system security mindset is critical in
this space both for devs and and the
security researchers
shift left which is a really well-known
thing in the space and all it means is
that let's not wait for you know uh test
in prod kind of a meme right think about
Security even before you start coding
for the
devs think about I mean that's that's
really what that's really the uh
environment we are in in in this case
right test properties t in variance use
your favorite tool it could be you know
the the the PRS we have some fantastic
ones from um uh the serator approver use
use fuzzing we have uh Medusa from um
from Trailer bits use simpler static
analysis tools we have so many of them
as an example
Slither and if if you're U more into bug
bounties you have various tools there as
well use Foundry
use solo D to as an example to look at
some of the P to learn from the past use
glider to look at things on the main net
there are so many of these
tools play around with them right I mean
some of them may
really work for you some of them not and
for the devs obviously the buck bounties
and you know the things may not may not
really matter uh for the devs but all
the various other tools right there are
so many plug for your Dev environments
use those to test it out there are
testing Frameworks there are various
extensions the key is to find your tools
and your techniques right and there are
we we I mean we lucky to have a good
choice think about the use and abuse
scenarios think about the adversarial
environment think about defense and
depth right because if there is any
place where we require defensive
programming this is it right do not
assume that I have you know I have an um
I have an array and it won't overflow
right or I have this code path nobody uh
it won't be executed or nobody will
um create a pool with this uh weird
erc20 token right do not make
assumptions right and for devs in this
case um yeah so won't repeat we're out
of time we want to save time for
questions as well
but all these things right and all these
slides will be available uh soon the
video I believe is being live streamed
but the bottom one I think is critical
right we tend to get
overwhelmed but take care of your code
as devs from a security perspective and
more importantly take care of yourself
well with that thank
you cool so so uh I think we have
questions we can take I don't know if
people in the room have questions or if
they have used the tool to put it up
here but maybe we'll start with
this hello hello hello yeah all right
the first one um what do you think
regarding an issue in erc20 standard
discovered in 2017 which caused 100 $5
million loss by ethereum
users which one is this I
what I don't recall that one I don't
know okay I don't have a formed opinion
about it thank you
okay while while that link is getting
posted I think we have one that went up
how do you say your process is unique
what do each of you do differently from
everyone else that's a good
one um I would lie if I'm I would say my
process is unique
um I don't think it's honestly I don't
think it's Unique I think uh well I
don't I haven't worked with these guys
side to side but um I do it to some
extent our process might look similar
sometimes I think we might defe
initiating to what extent we use tooling
for example that's one case in my case I
don't use tooling very much I'm very
much a manual
reviewer uh but perhaps not Raj or or
Jah might use some more tooling
sometimes I'll go first okay so um I was
very interested in the to in this topic
last year or sometime last year like
different methods of approaching
bounties Audits and there's a lot of
different ways of going about Audits and
security research but in the end they're
all not that dissimilar I think for J's
last slide is just read the Cod um in
the end that's kind of what everybody
ends up doing um Everybody builds this
like General mental framework that
they add information into as they read
codes um writing specifications running
tools they're all just methods of
thinking writing another meod of
thinking about the code but in the end
you're all just like mentally processing
uh and yeah so I don't think it's going
to be super
dissimilar yeah I would Echo that I
don't think it's that different um I
used to do a lot of my reviews with
invariant testing and fuzzing um but but
I don't think that's atypical um I think
if you put the time into really learning
how to use the tools um I think anyone
can really spin up like a fuzz test um
it's really just a matter of kind of how
complex um you want to get with
that there's too many
tools should we pick that one um I think
uh Nat had a slide on this um doesn't
matter which tool you use just use the
ones that work for you um I feel like
that's very true there's a couple V code
extensions that are super nice I
personally don't end up relying a lot on
this kind of tool I use Fe code
bookmarks super useful uh but that's not
really security researchable obviously
you're going to use some syntax
highlighting goto definition type
tooling um but beyond that is really
like what works well for you um and I
recommend you try out like all the
different things um in terms of
researchers to recommend these
guys the there are a whole bunch I mean
um just just go on Twitter um look
up and let let me look at the
publication right
um which publication so I would
definitely do a shout out to uh block
Threat by Peter from from coinbase so as
a publication so it's a I think a weekly
thing where all the threats in this
ecosystem are very neatly compiled so do
take a look at that if you're interested
and um if you're specifically interested
in smart contract bugs then the various
um reports from from contest from U
different project I mean different firms
like diligence they all have you
whatever publicly available reports on
their githubschool
right were there all their thoughts have
been captured so just go to those
YouTube channels or wherever they're
hosted take a look at it uh so that is
something I would uh definitely
recommend I found the link by the way
you can find it in this thread if you
scroll down the comments okay I don't
know how to scroll down um not in
this yeah maybe yeah we'll we'll hang
around so you can show it to us offline
as well can we yeah sorry I wanted to
add something about tooling um I
personally use Foundry a lot does it
count as a tool I don't know but uh I
write tests and I do fing with Foundry
uh that's mostly what I do and yeah
visual code Visual Studio code
extinctions and that kind of
things cool can can we go back to the
slide I I think there was just one slide
we needed to show for the
quiz so while it comes up so this is a a
short quiz it's really 15
minutes and you don't have to finish it
now just look at the QR code uh it's
eight multiple choice questions there's
a small contract which was designed by
uh and this was designed by tincho it
has uh you know for for the devs and for
the security researchers there are some
bugs in these uh contract Snippets so if
you go to that link and if you use this
password you'll be able to answer the
quiz and uh the top
two top two participants will get
tickets to DSS next year DSS is the defi
security Summit the security conference
that happened last week here in Bangkok
so hopefully it'll happen next year as
well so yeah if you get a chance do take
a look it's going to be open for about a
day and any further questions so yes
thank you for sticking along any further
questions uh we going to be hanging
around in oh there's one question in the
room thank you can I explain the history
of the issues that was asked regarding
the rc20
standard can I explain it and ask you
for your opinion oranization
I I'm sorry I don't understand your
question history of the erc20 attack the
erc20 uh problem that was asked in this
uh comments channel the erc20 standard
contains a security flaw that the Fabian
V the creator of ec20 standard confirmed
in
transaction handling so the ec20
standard is designed in such a way that
uh when you are trying to send tokens to
a Smart contract which is not designed
to receive Tokens The Tokens are lost
permanently for example if you would
send ethereum to some smart contract
which is not imp which does not
implement the receive function or if you
will send the nft token to such contract
that doesn't that does not Implement
their own earc
be lost but the ec20 token cannot be uh
uh handled on uh the contracts uh side
as a result uh if you send such tokens
to a Smart contract that cannot reject
them they will be permanently lost so in
were $6,000 of dollars lost because of
this issue at that time in the next year
there were 2 millions of dollars lost uh
in 2023 there were 60 millions of
dollars lost because of this issue
because it is still not patched and uh
on 1st November
lost and two days ago a user lost 25
millions of dollars because of this
exact
issue got it yeah I think uh we
understand it now so token sent to a
contract being lost right as opposed to
being sent uh accidentally to a contract
right
so I believe I mean it is it is how it
has been designed so users access excuse
me uh why is ethereum and nft designed
in another way and does not cause the
loss of money for users do we want to
say that the loss of money was designed
I I don't believe so this is very
specific to Smart contracts right and
it's not nothing to do with the ethereum
base layer and it also is about how your
smart contract works right so we can go
deeper into this I think there's a
misunderstanding here so we can uh talk
about this but time's up but we also
want to take the last question in this
room uh thank you uh just very curious
uh uh perhaps maybe the Tre you can uh
like describe how you approach a fresh
Cod code base where you studied and like
how do you map out and your workflow
like thank
you how do you look approach a fresh
code base so I already answered the
question I think before so me personally
I start with the documentation because
there's going to be problem sometimes
you already find bugs just reading
documentation I think I saw a Twitter
message like or the other day where
someone actually did the same thing
found a bug reading just documentation
and then usually like Global scanning of
the codebase and then for me I usually
take the go deep approach so I just like
spearhead for the parts that I think are
uh vulnerable but I think that is mostly
a bounty hunting approach doesn't work
for auditing or yeah a lot others speak
to that hey thanks for the question uh
so in my case um I was a documentation
first uh with a healthy dose of
disrespect for the documentation don't
trust everything that you read because
it might be a case that in the code
doesn't match the documentation so you
have fun with issues
there um and what I would also do is
just this is perhaps something personal
but I will just start with the little
Parts uh I wouldn't go first for the big
contracts where you have like all the
main interaction everything sometimes I
just start by the small libraries but
isolated things that I can then just
treat as black boxes in in the future in
the so I would start at the beginning
with those and then move up into
complexity yeah I would Echo
documentation I would also add um
starting to like find and identify
invariant from the beginning um so I
kind of start with that WID
documentation and then reading the code
finding some more invariance and kind of
iterating throughout that process um I
think over time the more you understand
about the code base the more invariance
you can find and very likely um the more
invariance you can
break thank you
lat
I
d
on
come
he
m e
is
sh
he e
SC
h for
for for
h
all
now
you
e e
here e
the
bu
B
o
y
true
is e
oh for
w for
n
t
G
e for
for e
h e
o o
also for
me okay welcome everyone to the this
Workshop about top hacks since last
Defcon last Defcon was a long time ago
actually so a lot of hacks have happened
since then we'll talk about what we
learn but first quick
introduction about myself um I'm one of
the founders at chain
security uh we are one of the old
Auditors in the space you can say uh
responsible for a lot of audits a lot of
things in the ethereum ecosystem I will
skip most of that but just so you know
who you're having in front of you I'm
more coordinating stuff seeing a lot of
the hacks of course working a lot on the
responses we also have our team here who
is actually doing the Audits and I'm
here together with mudit I'll let you
introduce yourself but many of you will
know
him hey folks U I'm modit I lead
security and uh engineering as well now
at polygon um and yeah like this is
going to be an interesting one like U
the aim is to go over all of the top
hacks that have happened uh since last
Devcon uh Matos and chain security have
done all of the hard work so I mean I'm
here as a guest speaker sort of I I'll
go over a few things a few nice things I
want to talk about especially about the
vazer xac and all of the other things
Lazarus is doing which I'm going to go
in more detail in my talk tomorrow but
it's going to be a good teaser today uh
and yeah let's
continue so the other participant is of
course you guys right this is a workshop
so the way I think we can best learn
from security incidents is by sharing
that knowledge of what happened what did
you learn from some of the things you
have seen what are your takeaways from
some of the hacks we'll go over in
addition to the ones um I compiled on
these
so we'll try something first on
this and that's one of the new web three
thingies to do documents right so try
this see if you can log in see if it
shows top hacks it's a document we can
all work on together to add um insights
too it's kind of empty it should show a
heading if this is not working there is
a Google Docs backup to do this
um but I'll I'll give you a second to
try yeah we going to have a bunch of
good learnings there and I'm going to
use them later because the vazer X act I
would reverse it like I would want you
guys to explain me how it happened I
have no idea how it happened so let's
focus on these and then we can together
figure out perhaps how the vazer X and
radiant hacks
happened so who has the document open
and sees something like top hacks just
quick raise of your
hands two three managed
four okay yeah some more I think we have
contenders yeah yeah yeah you know like
uh what is this uh five out of multis
here so good
enough okay now this is an ethereum
Conference of course and ethereum has
seen a lot of uh hacks because a lot of
building happens actually on ethereum
right but the biggest hack is not on
ethereum the biggest hack we have seen
since last Defcon was a compromise of
DMM
Bitcoins uh wallets
this I need to go into it a little bit
because uh the the Bitcoin world is a
little bit different right it did use a
two out of three
multis and this is natively supported on
bitcoin
right it is not known a lot about how
the attack has managed to gain access so
at least not to me perhaps some of you
have more insights in here um
all I know
is at some point this Exchange in
something resembling a cold wallet was
um splitting up like a lot of
transactions into 500 Bitcoin bunches
batches you can say right but they all
controlled by a single private key or a
multi6 so two out of three private keys
and um they were sitting there for quite
some time right right and it was being
used for some unspent and um yeah it it
was kind of active whenever they had to
to re uh fall back to it but then at one
point an attacker drained it but really
not completely they just used um I think
nine UNS spens the nine largest ones and
they had a few months to collect those
signatures in this
case who so yeah this this is roughly
what happened right
um
those uh the exchange was able to secure
the remaining amount roughly one hour
later to me it looks like a signature
attack once again not a compromise of
private keys because with a compromise
of private Keys we would have seen
everything drained right somehow they
managed to perhaps with an Insider
perhaps to fishing or whatever it's very
hard to say
that those uh signatures were created
and then were in the end used so this
was by far the largest TCH we have seen
yeah and the it it's very similar to
actually how vazer X got drained and
also radiant in the methodology which we
don't have 100% Clarity on we have
theories on how such an attack could
have happened and we definitely have
protections on how to prevent these um
regardless of what the method was which
we'll discuss but this it's one of those
brain teases you guys can while we go
over other hacks try to decipher how
something like this could have
happened so my my initial take on what
can we do to make such an attack harder
right is like you did see a very large
wallet holding significant fun
fs
and from a human perspective you know
like at the end someone had to sign
right but a signature here exposed a lot
of
funds so one way to reduce the risk is
splitting funds but that comes with its
whole own set of risks right and we
would have a later hack which shows this
whole set of risks there
um the other thing is what was special
about this haug which you are familiar
with here right but which I haven't seen
in other blockchains too much is
they choose the destination address
carefully it was an address which had
the same five initial characters in the
Bitcoin uh address and the last two this
points that someone did compare the
first five and the last two or those
were shown to them as a valid address
um and and I think we'll go over this
also even if it is kind of possible to
compare a hash because you have a
trusted source and you can compare the
whole hash laziness prevents us from
doing that often because we just start
with the first and the last and yeah
that's fine right we we kind of know
this is secure now it's the right
address but now on to you guys so who
has something to add to this first
hack the only one which is not on the
ethereum
echosystem yes can we have the
volunteers pass the
microphones also feel free to use the
document and add stuff there right this
is just
collaborative competitive
too it's just us farming our work out so
we don't have to do
it yes I have not so um what if to avoid
this laziness we would double has things
like it is hard to brute force that you
start and end with the same hex nibbles
and then that the hash of that itself
matches the first and last hex nibbles
would that help any way or would it over
complicate things
I can answer this one it doesn't matter
like it's same complexity um to create
that collision between a hash and a hash
of hash and a hash of hash of hash it's
still Brute Force so it's same
complexity
actually I can also repeat just chout
and I repeat that's perhaps
faster organically hit those those
numbers like there's almost no way that
you hit a
another account that has the same first
four and last four it's like one and 82
trillion whatever so why doesn't it just
get blocked at that
stage good point so the the point here
is like why didn't they have some
software in place which automatically
detects that there was something which
looks similar and just blocks everything
which looks similar right well
hindsite yeah this is a good idea but
but it's not something that's new it's
not new but that's the thing like we are
maybe 10 years behind from traditional
security when it comes to security
measures here I mean
are the epitome of security here is
seeing a random hash on Ledger before
signing it so we are far from where we
should be uh but yes 100% like um in an
Ideal World a wallet should protect you
with these scenarios and should warn you
hey this address is slightly different
from where you send are you sure you
want to send funds here uh
Banks do it with even names and things
like that even with email fishing and so
on like if someone sends you an email
with same name as someone you know it
shows you a warning like it's not that
same person and so on so yes these
protections exist and our wallets should
have it but our wallets are very
barebones the best we have gotten so far
is this tiny window on a browser uh
which you have to scroll down to see
details before you sign so lots of work
to be there to be done there and it will
happen we have made great strides but we
got to remain secure while that works
finishes okay question there one more
and then I go to the next heck
yeah so the um question here is what why
is this the standard that you have
centralized exchanges which do hold user
funds instead that is a standard that
you don't and people hold their own
funds um so I can answer this one as
well like because I'm a very practical
person like in reality yes I want every
one of you to do self custody and uh
keep your keys secure but the reality is
there was one bigger hack than this one
which was just user fishing like at
least around $2 billion were lost since
last Devcon to just users that are self
ceding being compromised and fished and
so on so like and these right now our
audience is very technical like anyone
who's self custody is a relatively much
more technical person than your average
Joe so if we want this technology to
have mass adoption we either need to
make it much simp simpler to self
custody or we need to make custodial
Services much safer um so in any case
there's lots of work needs to happen
there are tradeoffs but none is like
objectively better than the other choice
like imagine telling your grandmom how
to use metamask like it's just not going
to happen I would prefer she uses
coinbase
so okay let's go over to the next thing
and and if you have more to
right don't hesitate to put it in this
document so the next one was already
teased I'll let you cover it yeah
exactly it's um it's I guess the second
biggest one this was I think around $230
million or so um and the way this was
happened was very similar to the last
one um it all started by so vazer X had
a system of a cold wallet and a hot
wallet
so the hot wallet is was used to honor
all of the user withdrawals of funds and
so on and the cold wallet topped up the
hot wallet whenever it needed more funds
there were more withdrawals so the
hackers first thing they did was trigger
this movement or Force vx to move funds
from cold wallet to hot wallet by
continuously in a loop uh depositing
Gala token and withdrawing Gala token so
when you deposit to an exchange you get
a unique address and you deposit there
it doesn't go to the hot wallet directly
so what this meant was the hot wallet
ran out of funds um vazer still had all
of the tokens but in different wallets
it didn't have tokens to honor
withdrawals from the hot wallet so they
decided to move funds from their cold
wallet to hot wallet which is a routine
activity for them they do it every week
nothing suspicious although it should
have been suspicious like why there are
so many Gala deposits and withdrawals
suddenly happening but beyond that point
they started uh doing this deposit of
Gala uh in from cold wallet to hot
wallet uh initially the transactions
kept failing for them so they involved
the they were using linal as their self-
custody provider which as a product suit
in itself is hilarious like it's
basically a wrapper of unsafe on nosis
safe but they were using it so uh they
got them involved they started debugging
and everything but then it just started
working after like five failed attempts
it was working um so that's fine what
they didn't realize is those five failed
attempts could have been just them
signing malicious transactions and
obviously UI rejecting them so they
happily yeah press the button on Ledger
press the button on Ledger press the
button on Ledger all malicious
transaction signed all good um but yeah
at the end I won't go into details of
how the signatures were collected but
yes they had failed transactions which
they signed and just ignored because one
like
the ux in our space is so broken that
failures are normal like five times fail
six time success perfect it's nothing to
worry about um but that's yeah we come
to it how that's bad but yeah they just
signed these bad
transactions without realizing they
signing bad transactions the UI was
showing them the good details the
correct transaction but they were
signing something bad um how that
happened the UI showing them something
good and them something signing
something bad is an unknown with lots of
theories I have my own Theory uh but
what's your
theory uh my theory is that it's
something I would share later I I don't
want to poison others thoughts because I
want people to post their theories uh on
that thread or Channel or whatever um so
there are lots of POS posties I'll give
you some possibilities one possibility
is that lonel was compromised their uh
like service provider so the UI was
showing something else but sending bad
data for signing uh it is a plausible
Theory another theory is uh the wallet
they were signing was compromised so
they instead of installing metamask they
installed meta Fox I don't know and the
wallet was uh changing the transaction
another theory is those laptops they
were using chosing to sign were
compromised themselves could have been
like U they were at some point like in
the same infrastructure or something so
someone spread a virus on it or whatever
and the laptops themselves uh changed
the transactions up after the
transaction so once you compromise the
laptop you can modify the wallet you can
modify the uh interface between Ledger
and so on so you can do anything so one
theory is that the laptops were
compromised uh but those were three
different laptops MacBooks in three
different regions
so yes another theory is the ledgers
themselves were compromised and since
it's a single company single Hardware
device maybe they used the same vendor
to buy these Ledges and they got
compromised fake Ledges somehow another
theory is um the wires they bought were
compromised so this right signal left
the computer wrong signal left reach the
device and it just happened over longer
period so people didn't realize so there
bunch of theories you can theorize more
uh but try to theorize what is most
plausible here um but we'll ignore that
come to like how do you make yourself
safer so it doesn't matter what that the
theory is there there are some basic
things you can do to keep yourself safe
uh I have these is this is the basic
stuff right this is a teaser for your
talk yes it's a it's the teaser so I'll
go through these very briefly number one
is use Hardware w like don't trust
software wallets or browser wallets they
are much much much easier to attack than
a hardware wet the second one I have to
repeat this so many times but it it's
obvious like don't share your nemonic
key not to metamask support not to
coinbase support not to your grandma
nobody just just just never share it
never type it out on a computer never
copy and paste it anywhere just write it
down um you can write it down on
different pieces of paper split it down
whatever and just keep it safe um then
on just keep it safe that's all you need
to do it's a teaser it's a we we're
going a little FAS it's it's a very
loaded word and I can do a whole 1H hour
session on how to keep pneumonic safe
but I'm assuming most of the people who
are here have heard that a lot
already but yeah fair point then another
thing is like security is always about
layers even when you have a hardware
wallet if you're connecting to a Dap I
would recommend you to connect it
through rabby or metamask or some wallet
your Ledger instead of connecting Ledger
directly Through The Ledger kit to the
DAP because whatever wallet you connect
to Rabbi is good for this it would
decode the transaction for you and show
you what actually you're ass signing so
even if the website is compromised you
can catch it at the browser level if you
directly connect your ledger to the
website if the website is malicious what
you're seeing on Ledger is just
gibberish you're you're not going to
know what you're signing and you're
going to uh get wrecked so just keep
adding layers um verify what you're
signing on the browser wallet you can
potentially use dedicated air gaped
devices these don't need to be super
expensive can be like $300 $400
Chromebooks which you don't do anything
on except signing transactions on noses
safe so you can add a firewall to it
which only allows connection to the
noses website and nothing else so you
only open it sign it you close it there
is no other thing going in and out of
that don't do your regular work on it uh
another basic one is ensure secure
threshold for your multi6 like the
biggest hacks we have had were like 3x1
multisig 5x9 multisig uh 2x3 multisig
these are um and this one was I think 3x
say they were following the best
industry practices and they don't know
how to how they got hacked so it's like
if you are following the best practices
do actually follow the best practices
argue verify hashes on your Hardware
wallets this is a big one now uh Ledger
is working on making those more legible
which is super nice but in the meantime
we have some Community tools you can use
uh like uh PC has made the super nice
safe TX um hashes util which you can use
to basically it will fetch all of the
data from nosis API hash it so you
actually get a hash which you can verify
on Ledger like you then just compare two
things now you can be lazy and ignore
that but at least you have something to
compare uh before this if you were just
using the Ledger on nosis site nosis
will show you all of the d uh like dhash
things the actual data of what we are
signing and lger we show you an just an
hash so you can never verify like what
you are signing is actually what you are
seeing uh using these tools and I think
noses are adding this officially now you
can actually verify that you're signing
what you are seeing
uh
finally uh use a diverse set for your
signers don't make everyone use a
MacBook with Ledger with uh Chrome
browser and everything use a diverse it
and especially throw in mobile devices
there which because they have completely
different risk profile uh like hacking a
Windows device is much different than
hacking an Android device so just use a
different uh set of things and do not
ignore failures I know web3 ux sucks and
failure happens but figure out why that
failure happen especially when there are
critical funds at risk do not just
ignore a failure and move
on I so my proposal on this is we should
aim for this three star security
thing we have some experience with that
when really large funds are being
handled by centralized entities and it
really makes sense to try to force an
attacker to break three systems before
they get you right now we had cases
where you can say like if they got into
the UI of safe they got you if they got
into the Lial UI they got you right if
they control if they get https um
certificates for those websites you will
access them they get your red man in the
middle attacks were possible of course
these are State actors right we we do
face
here a different Threat Vector than we
usually face this is not about you
protecting your
own um Ledger or so right this is about
protecting funds which um larus groups
things are worthwhile to
attack
um there is a lot of things Unknown
about vazir and what happened here are
there things you want to add from what
we said ideas we already talked about it
theories what how how do you think they
have been
compromised um and then if you'd be the
ceso of that project what would you do
what would you learnings be out of that
what would you try
to do
differently I think we'll look at the
document later what ideas people
can we have a microphone
there uh didn't they have some logging
system
also logging yes but you can't really
trust logging and it doesn't help
because it's in this scenario because it
has already happened okay you logged and
realized oh I did a mistake that mistake
already happened so you need Beyond
logging you also need active monitoring
and aler in and actually taking action
on those um they had logging but it
didn't matter again like errors happen
they said errors are normal it's fine
let's move on yeah there were some
really after the fact things where you
can say like it was in the locks and it
was very suspicious right the problem is
the noise of locks I've been working in
this myself and they are very very noisy
and it is very hard to write before you
know exactly what the attack is what to
listen for in these noisy locks
yeah I think um around about the same
time there was a Microsoft threat
research article
on uh dprk using um Chrome zero days uh
um and it could have been a zero day and
um I think you've already covered that
mudit highly likely though if you look
at some of the compromises beforehand is
that it it was probably spear fishing
via browser extension side loaded BR
browser extension that that got them men
in the browser I think it was important
important for wiir to not have been
reading their email on the same machines
where they signed transactions so I
think um separate Chromebook or separate
iOS uh would have been a much better um
operation for them and also there was
probably time for them to add delay as
soon as they noticed the failures of the
two gala transactions they should have
probably realized that they were uh
being targeted potentially raised a
security incident started to go through
the transaction hashes and data hashes
um and I think lastly they had a really
high concentration of signers so if you
go and look at every signed transaction
for wiir X there was around about 1700
it it was basically uh three to four
signers so the the adversary knew
exactly who to go after um whereas they
should have have much more entropy in
sinum yeah in reality I mean humans are
the weakest link in security almost
always um VX had proceses in place or
policies in place but in practice those
procedures were never followed for
example the first question I also asked
them like why was your devic is not air
gabed and they're like it's our policy
to have air gap devices uh but we
installed Telegram and that on our to
communicate and like so they had all of
the policies none of them were followed
um and that actually sadly happens in
seen yeah on this a difference I've seen
in the more traditional industry is
really you have paid employees to do
this thing and they really care
versus they are deaths also paid
employees right but they are kind of
doing this because I have
to and you do it quickly so we we are
all lazy right so yeah I'll go to the
next hack we have one more
question um in my view they kind of
never fought deeply into their actual
like system they took a ledger connected
to like a four out of
six uh sign
multi but they gave Lial only one
signature so they could have easily just
bypassed linal if they wanted any
protection that may have been there
could have just didn't have need to do
it yeah for sure they could have but the
lonel was sort of like their signal
mechanism like if a lonel is signing
they would say okay it's good if they're
not signing it's bad but the thing is in
this scenario lonel signed so one of the
signatures were lials and lials firewall
or the security solution was like yes
perfect solution perfect transaction
let's goe so that that's why I was
saying like
it's I have no idea why they chose linal
as their custodial semi custodial
solution when they were using no say
safe because it ended up like weakening
their security instead of strong
strengthening as soon as lonel system
saw okay three people have signed it
signed the transaction so it became from
multis
um I prepared 20 hacks
no okay I'll skip over some anyway um
for like okay we take one more but write
your stuff otherwise in the
document so what what's the right
threshold for a safe like let's say for
example if the funds are huge like
couple of hundred million or like a
billion dollars what's the right
threshold to use and how many multi6 and
how to choose that yeah for sure it
always Bas is should be based on your
risk um because again like if I can if I
make the most strict policies in the
world nobody would follow them uh
security is always about risk management
and it's something you learn with
experience like you can create the best
policy but they're useless if nobody
follows them how how is it at polygon um
at polygon uh we have different levels
of multix so we have a threshold for
under a million dollars uh of exposure
we have a threshold for $1 to5 million
of uh exposure of 10 to 20 and above 20
above 20 is our like we have to keep the
secure kind of scenario and we almost
never use the above 20 multi6 because
all of the operations should happen from
the multi6 with lower uh exposure U
ultimately the the 20 plus how so um
ultimately like the ultimate multisig we
have are like for example the security
Council uh the protocol Council um they
are uh 9 by 12 I think right now or 9
by1 something along uh I think it's 9x
or 9x 12 uh for our protocol Council uh
and that's our like if you want the most
secure it this is that that's where we
settled not different phones the way we
enforce it is we don't enforce any
common Hardware so naturally you would
have a diversified set of signers but we
do collect like what sort of signing
devices people are using so if I see
okay like it's very Mac heavy or it's
very um this heavy then the next signer
I add on or replace would be on a
different set but I've honestly not had
to do it so far because just naturally
it has been very
Diversified do you know if they sent the
laptop of the developer to a forensic
company to try to investigate where the
issue could have come
from vazer X hired mandant and uh lonel
hired I don't remember someone to
investigate so they are working with
professionals but it it's very hard post
the hack because if the hackers are
state level actors like uh dprk in this
case they know how to erase their traces
like this is not web 3 this is web 2
stuff that they've been working on for
around 25,000 people in the lazerus
Lazarus or I don't know what's the right
word to call it but but yeah the thread
actor yeah yeah just just because we
can't find it after the fact makes it
really not a strong signal that there
wasn't
one um so yeah even though I wrote this
down here before like where where was it
no like no fishing was involved no sign
was
found this does not mean that it wasn't
like this
right okay let's continue uh um a
different case but still a key
compromise Gala games the third biggest
tck this was a very
likely I'm going out out of the way here
because it's not definitive but I'd say
very likely an
Insider um Gala was able to recover all
of these tokens and
um um somehow an old Minter address uh
was able to Mint a lot of Gala dump them
and and return them the next day uh
there were some internal conflicts at
the project uh key people
left um and and then this happened right
so coincidence or not hard to say right
um what did we learn here from my
perspective we had dormant access to
uh very powerful functionality in a
project
so um
likely yeah I mean this this happens all
the time right you forget to withdraw
access to people when they
leave um
you had here a a tricky case of trusted
employees which then turned into people
more adversarial to the company I think
in general you'd see a neglect of people
risk um in in this
case um of course you'd also saw on the
technical level that um EAS had very
high power in the system so that there
was no multiactor authentication or um
authorization for privileged actions or
high-risk
actions
um yeah um there there were no no checks
and balances in many on many of these um
places where they could have
happened yes so this another key
compromise but of a different nature a
common thing on Insider threats is
recovery of funds right people put on
pressure on these people very
effectively and usually the money gets
returned we will see other
cases any inputs from you guys on this
one I'm also interested in
how some of you manage the people risk
in your organizations or in
organizations you know where you'd say
look there was this worldwide W of web 3
what we kind of moved on by
now we do things differently what works
what doesn't work I know we take this
very serious at chain security
ourselves uh polygon takes it serious I
don't know how you do it would be very
interested in
this yeah how how to manage this people
risk uh um for a limited amount of time
for whatever the access is required but
kind of don't give permanent access to
security sensitive things yeah makes
sense and those are like the basic and
obvious one everyone should be doing
unfortunately people don't do it but
they should I I I'll make this
conversation hot and more interesting by
throwing a curveball in our space we
respect privacy a lot and we want Anon
contributors so how do you manage Anon
contributors and people risk that's the
biggest question how do you tell this
Anon is not
dprk anyone has any thoughts on that I I
can share the policy we have at polygon
because we are Anon friendly but still
safe I want to know if anyone else has
cracked the code or is working on
it
sorry I mean dprk can own all the anons
like they have more people than all of
the blockchain developers combined so
that strategy could work for first 3
months but then they will pick up and
yeah we had one more in the back uh yeah
how about just changing addresses so
authorization to the smart contracts
will rotate to another authorization
address or you know an exchanges just
move the money to another address after
key people leave yeah so having good
offboarding policies right um Eric
already mentioned this this is very
important like when someone leaves can
you really clean it and you need to know
you need to keep track of every
permission you give during the lifetime
this is hard honestly and then you need
to have efficient processes in place to
quickly withdraw them too but but it's
very worthwhile you need to do it anyway
right um yeah for sure and the reality
is like in practice from what I've seen
most of The Insider threads have
originated from people who are currently
employed by the org not the X people do
do you do background checks on employees
yes so I I can give some info about like
what we do as polygon in the Anon
friendly way so it's not 100% Anonymous
but we have two basic levels of security
there one for everyone basically we use
a third- party background uh company to
do background checks so they would have
all the actual details and everything
about the person which they would delete
in whatever the retention policy is I
don't remember the exact number of days
but uh they would get all the details
they would verify they will do police
background checks and uh everything but
they would not share any of that with us
so we will not know we will just get to
know okay this person cleared it or this
person has this this this issue um so
that is one thing the other is for
hiring Anon people we do have a few Anon
people uh in polygon um we require at
least one uh proof of recommendation
sort of so you must be recommended by at
least one person in our org who trusts
you and knows you um for a long time so
it basically like it's U we we trust our
org to know what's best or who which
andon is good or not you should not be
recommending anyone uh who you are not
comfortable with it's sort of like we
are trusting our employees are to be
good it's the philosophy of private
trackers if I don't know if how many of
you do tourance and all but it's
basically the invite tree um if you know
someone good you invite them if the
person who did you invited does bad you
also get kicked out so you you only
share these invites very carefully and
only when you really really really trust
this person and this process has worked
wonderfully for us we have not had a
single case where an internal employee
has recommended
an bad Anon like it has always been very
highly trusted good anons yes knock to
wood okay so this is for insiders there
is so much more of course which can be
done here but I'll keep it more
technical because I'm just more familiar
with the technical stuff please also add
stuff to your document do we have okay
one one really last one on this there
was one more on top of what you just
said uh if you want to uh to include
more unkown people is the use of uh
session keys or access controlled roles
where if you want them to do something
very specific give them access to some
address some function selector and some
other conditions to the call data and
the payload and then they can execute
the stuff it can be U time uh time gated
as well or not or can be removed with
refresh and um something that's been
actively worked actually a lot but
that's for this one time access it works
right but but this is mostly about the
people you trust for years or so you can
still Implement that for those people as
well yeah makes sense this also just
comes down to layer of security I would
do this not just for anons why I do it
for everyone like it's just a additional
layer of security which we should do for
everyone uh but then you have to again
balance like practicality versus uh
policy situation but yes it's it's a
good layer of security to
add
yes okay um I go
on this is a a case I want to talk about
too much
it's um an exchange was hacked because
someone got access to their Google cloud
and they had all the private keys in
there uh this is of course bad and we
don't need to say how bad this is on on
how many levels um this happens if you
hear you need to segregate wallets you
need to keep funds in different wallets
to be secure right but you don't really
know what you're doing
because yeah I
mean uh okay I'll quickly go through it
just so you know many are doing a lot of
things right right not everyone though
so in in this case uh like 15 million
were drained over a long time by an
actor uh who got access to those private
Keys just one by one draining all these
wallets right then the project didn't
even notice for really a long time
um and um I guess they got noticed
because someone told them look I can't
withdraw somehow it's not working uh on
next Monday right this was a
traditional Saturday morning Friday
attack something like
um yeah uh what did we learn um there's
obviously no use in uh segregating if
you lose access to all of these keys if
they are stored in a central place
that's kind of equivalent to not
segregating
wallets um relying on cloud
infrastructure so first off in this case
it was Google Cloud generally this is
more secure
than most of the things we can build in
reasonable amounts of time right this
this has to be said right but if you are
an exchange that's your business right
you can be a lot more secure and there
are dedicated system systems to allow
you to do that Hardware wallets and I'm
not talking about Ledger here right
proper Hardware hsms which manage this
stuff like that right there is really
this is the bread and butter of normal
Banks today too obviously they need to
sign a lot of things digitally too right
it's not only us um so yeah there's a
lot you can do this is really not how
you should approach
it yeah I quick like side thing
tangential attack Vector here because I
it just reminded me which I've seen
increase now a lot is people trusting AI
tools blindly when all of the AI tools
are just farming all of your data for
training so there are two attack vectors
here one if you use the public version
of it for example even if you buy the
chat GPT Plus for $20 whatever you enter
in there is going to be used to train
their model so for whatever reason if
you pass all of
your if you enter any secret obviously
it's gone but what people end up doing
is um I I've seen like they would upload
your whole they will upload their whole
code base and then ask for suggestions
or something so it chat gbt is good at
explaining code or uh doing things like
that so but the problem is if your code
base had Secrets any environment files
or whatever now chat gbt knows this and
it's actually going to add that to its
model and in future maybe someone would
uh type give me example of get a private
key and boom your private key is shown
to them so this is one one attack Vector
the second one is even if you buy an
Enterprise version of the software where
they claim private data and no training
on your on your data and whatnot the
thing is they they still log all of your
data and their support and Engineers are
able to look at this data for uh
training for their own like Improvement
purposes and so on so if um they if you
read their TNC you would see there like
um so if you enter any secret there any
of the openai employee support engineer
can still see it and drain you I've seen
this happen a lot with things like
Google photos like people would take a
photo of their pneumonic and upload it
on Google photos usually it's very safe
but in edge cases they still have access
to it um so not great uh and GitHub
co-pilot like how many of us added to
our repo where we have in like our
private secrets and environment
variables and everything just look at
their privacy policy one because I'm
actually not sure about the privacy
policy of gith up copilot but it's
definitely a risk Vector people should
explore uh so can you recommend
something uh so let's suppose in our
system like we are a bridge and we have
a private key that signs our transaction
I mean like 20 transaction per second so
where should how should we secure that
single private key like where should we
store what best practices should we have
I mean like like we can't have a air gab
device who is just signing transaction
this is a hot key just like someone
which needs to sign like automatically a
lot right so which technology should you
use to to enable that to secure that
private key like the securest way or
like the best practices I would say yeah
for any hot key there are two things you
need to secure one is the actual key
itself you can throw it in any HSM or
something and it's good enough for a
hotkey purposes you shouldn't it
shouldn't have billions of dollars on it
but the bigger attack vector and the how
most of the attacks happen to hotkeys is
the authentication mechanism if your HSM
just has a public API and uh it it has
SL poost data and it Returns the
signature it's worthless so it's a like
that is the actual mechanism you need to
secure that only people uh only the
right people should be able to request a
signature from there only the right
things should be able to request the
signature from there uh you need to
secure it through firewalls uh through
filters through everything but that's
the harder component you need to focus
on yeah
thanks you want to add
something uh but what if like the
dedicated HSM if you have like a gcp
admin and you can control the HSM if you
compromise JCP admin like what can you
do with dedicated hsms yeah that's the
thing like that's the access part once
the key is in HSM is secure like but if
you can access the HSM somehow and being
an admin is just one of those things it
is dangerous in gcp actually you can
have no admins uh in AWS as well nobody
has that permission um and only select
products have select permissions you
could have a system where nobody has uh
read permission to the HSM only signing
requests and so on but again then you
need to ensure people are not signing
the wrong things and so on so it's
permissioning thing but obviously you
need to ensure the people that are in
there are trusted and uh so you're
proposing having like a segregated like
also HSM infrastructure that oh yeah
like in your that that's again
traditional web to stuff like um in your
infrastructure it's not just hsms like
everything should be segregated and it
should be the least uh privilege of uh
like um I'm forgetting what the
principle is called but everyone should
only have access to things they need
nothing extra uh it shouldn't be like
okay I'm the CEO I I have admin access
no like it it's actually the opposite in
polygon like I lead security and I have
less access than all almost everyone
under me the simple reason is like I am
the bigger Target um and I don't do the
day-to-day activity that I need this
access every day like maybe I'll need it
once a week I'll create a ticket I'll
get access for 15 minutes I'll do my
thing I'll uh create a ticket remove my
access so it's just yeah like access
management is one of the biggest things
to like do it's the hardest thing to do
right uh and it's something nobody does
in our uh in our space but needs to be
done what but this is a good question
like is there someone here to say like I
want a shill and HSM right basically a
solution I am actually using and feeling
very comfortable with
you can actually use uh tees for this
you will answer but just ideally
something you can actually
use yeah oh look I think you could use
KMS or cloud hsms and and you can
restrict policies do just in time do you
know a good one yeah KMS is fine for
holding for for holding keys I think the
admin permission is the problem right is
so you just in time uh um um you know
just in time permissions using something
like lumos or other approval systems but
to tell you the truth um maybe just use
fire blocks I don't work for fire blocks
um but that's a a much better solution
um where it notifies multiple signers
you can build Chums so that's probably a
better solution
here
okay um okay one one more in the
back
and yeah we'll come to Smart contract
Tex too
uh so in terms of HSM capabilities you
have the cloud Solutions which is
obviously aws's Cloud HSM solution I
think is slightly better than gcps at
the moment sorry uh but I'm a I'm a dual
I'm a hybrid Cloud user so I don't judge
either way I just find the best solution
uh aws's Cloud HSM solution is a bit
more uh segmented and can allow for sort
of a bit more user granularity whereas
gcp and that's within the HSM construct
itself not just I am principles uh gcps
HSM is built into their Cloud CS system
and therefore you're a little bit more
dependent on just sort of the standard
identity access management within gcp
and I think that's your biggest risk
factor on both of these HSM Solutions um
as the previous uh person mentioned like
it's really less the HSM is fantastic
but it's going to do what you tell it to
do so unless you set up granularity
within the access control mechanisms
you're still going to have a similar
issue and that's why typically a lot of
people do move to fireblocks because
they've created that sort of multiactor
capability uh and authorization patterns
um again AWS you can do it a little bit
easier because you can dial into the HSM
console and and programmatically set up
some of these kind of multiactor
capabilities um otherwise on Prem um
Talis is a really good HSM solution if
you have unlimited money um if you've
minted unlimited money then you can go
for IBM Z series if you really want to
be fancy
um but really uh the best thing to do is
really making sure that your your access
controls um prevent your HSM from just
blindly signing anything that comes
through to it uh especially if you're
leveraging web application services that
are specifically signing on your behalf
yeah I I think this is a good thing to
repeat you need to think a step further
from my perspective if you think the HSM
is just holding your key securely that's
not enough it is really you need to
think of your hsmf the system which
validates if the if that transaction
should happen right and then then yeah
some good suggestions were
mentioned okay let's go
on this is one message I just want to
highlight right we we will and we are
smart contract Auditors right and so on
and we we really uh try to secure the
space from this perspective but key
compromises are the new big thing there
was a very good talk by Peter at DSS you
can see the recording highlighting this
fishing a type of key compromise right
and this these are the big hacks of
today so the big smart contract TX the
biggest one it's long time ago but
Defcon was longer this is why it's in
here we talked about this one a lot and
you might be familiar with it right um
there were great great great videos made
on this and I was planning to show the
video here the short part which explains
the hack it takes like three four
minutes um do you want
okay first some any some uh advertising
okay let me
see okay um I don't know the sound um
can you help me with the
sound you
cannot okay
subtitles language yes
let's
see I would try something crazy
but FL is a special type of loan anyone
can take as long as they the money in
the same transaction now that we have
$30 million let's deposit it into
Oiler then let's borrow 390
million start let going start the hack
drained six different tokens but they
all work in the same way let's look at
the first it starts by borrowing 30
million die through a flash loan from a
a flash loan is a special type of loan
anyone can take as long as they repay
the money in the same transaction now
that we have 30 million let's deposit it
into Oiler then let's borrow 390 million
and deposit it right back usually D has
a collateral and borrow factor that
leads to a maximum 75% loan to value
however Oiler has has a special
mechanism for self- collateralized loans
when your assets and debt are the same
token it bumps up your max loan value to
collateral we get a loan to value of 93%
and a health factor of 1.02 so
everything is still perfectly legal on
Oiler we just have a highly self-
leveraged die position now here is where
the vulnerability comes into play Oiler
has a donate function that allows users
to donate their collateral to the
protocol itself it was implemented
because sometimes if you have a very
small balance it can be cheaper to
donate the dust than withdraw it
yourself however this function lacks a
critical Security check it doesn't
require the user's Health factor to be
above one afterward and this is the bug
it allows a user to donate into
insolvency back to our leverage position
we now abuse this by donating 100
million now our health factor is
and liquidate the Violator earning the
maximum 20% penalty our deposits times
finally we repay the $ 30 million flash
loan to net a profit of 34 million
however Oiler doesn't have that much
money in its reserves so we walk away
with 8.9 million the hacker repeated
this five more times to drain a total of
$200
million news of Oilers hack spread like
wildfire with 200 million gone okay
okay
so I think there there are more uh
in-depth explanations more walkthroughs
there's a lot to learn from this
one but there is again there is a part
which is Technical and then very
interesting and there is a part which is
very human right and Michael did a
amazing write up here the War and Peace
uh write up at the end of this year I
heavily recommend it for everyone to
read it is a small book in itself takes
some time so I will not go over this
here what's
important so this hack
started with uh small change to the
code which the small Small Change was
also audited the small change was
actually to to protect against another
vulnerability which was missed in the
previous audits right but which was in
itself much less impactful than the
later hack would be and and then it was
a small change right so you ordered a
small change and if you ordered a small
change it is hard to say this will take
me three weeks while it's 10 lines of
code
right the problem obviously is that
small changes are very hard to uh audit
um and then we yeah we see this again
and again um also you don't want to AIT
re audit a protocol which has been
heavily audited too as an auditor you
don't like that right because you really
like to find bucks um So the lucky thing
of this story in the end the funds were
returned right um um they they lost 200
millions they got 240 Millions this is
because there's a time delay and uh also
an insurance
payout um
so what did we learn
here I already said it it's really hard
to audit
diffs but also security which which
Oiler took very ser serious and took to
the Extremes in the version We a lot of
you might have seen when you took part
in the crowd competition or as Auditors
and so on um really pays off on these
levels right because of the levels of
security of the things they had in place
they were able in the end to recover
those funds and I think it is a good
case
of what kind
of methods you can put up to recover
funds from The Human Side Right their
communication was really good and this
is a super super stressful scenario if
you read the war in piece you will see
like there were situations where it was
like blood tests and passing out on the
oiler team side of things um but if you
have some guidance some
plan and and it will not survive like
famously said right it will not survive
the incident but it will help you so
much
to to make the playing field a little
bit different to if you are well
prepared then you will still get hit by
the unknown but just because you're well
prepared you can really go ahead and and
kind of win in the end because the
attacker might not be so well prepared
and in this case this was a case right
it was a a single person who later went
to prison uh who was found and um
yeah so so in the end this this was one
of the few success
stories
um smart few smart contract TXS are like
that almost no key compromises are like
that I'd say key compromises our main
adversary today is Lazarus group yeah
that's true because um I'll jump in here
as well because like reality is it is
very hard to stay Anonymous when uh
first it's hard just when doing the hack
but it's even harder when you are
laundering the fund so you have done the
hack it's fine then what do you do with
it like you would naturally start
laundering and that's when people get
caught so most of the hackers actually
get caught at one stage or another uh
dprk also get caught but they don't care
so that's why they are a bigger threat
to us like you can't go arrest uh them
in North Korea um with this case in
particular couple of more things I want
to highlight is upgradability that's a
double EDG swad like I worked a lot on
Smart contract upgradability and made
The Primitives to make it happen in
why it's a double HED SW it it is I'm
seeing right now people upgrading
contracts like there's no tomorrow they
they had a new uh feature they upgraded
like any small feature and in this case
yes they were fixing a bug as well but
they might have just upgraded to add a
donate function you can donate to
protocol now $10 we'll have $10 more
Revenue let's upgrade the contracts so
they you have to be very careful about
upgrading contracts that you don't do it
just for small features either like it
should be security fixes or very large
features that you can't afford to launch
in a new contract so upgradability needs
to be taken seriously and this has
happened with more bigger protocols not
just Oiler another big one comes to mind
is compound Finance I don't remember if
it happened before last Defcon or after
but that was a more hilarious case
because they upgraded something people
noticed the bug and they ended up
minting like $250 Million worth of comp
or something extra in rewards than they
should have um and as soon as the
upgrade happened and they started
minting more people noticed oh something
is wrong at that point it was maybe like
what like the to upgrade it again they
had a time lock of seven days so the fix
took seven more days and by that time
they lost 2 250 260 million actually on
this we we have expert in the room on
the the compound like I'd be very
interested in the learnings compound
took after that uh if if those are fine
to share there there was a good talk at
DSS on this by
Michael
um there's so many Michaels in this
SP but yeah um if someone wants to add
something to those learnings that would
be
great
um Michael you need to look up from your
phone
yes from the compound case where were
learnings okay never
mind yeah but but watch the talk it was
good yeah for sure the basic learnings
are be careful with upgradability it's a
double H
SW okay so we got to the next we don't
have that many minutes left to be
honest
um I want to
skip it's another key compromise with
Insider involvement potentially who
knows little info little to be talked
about
here another
one little info key compromise hot
drained but here we are back to a Smart
contract actually one which uh is a
polygon using
polygon um in this case it's an oracle
manipulation and those used to be the
big hacks of last year not of this year
anymore because we really learned um in
this case how did it work
so you uh you might know in general
Oracle attacks they always work by
having a landing platform and
manipulating the prices this Landing
platform depends on to um first deposit
and then either get it back cheap or
like to to drain the um the lending
platform by pretending your assets are
really really worth uh worth a lot of
money right so this is also what
happened here the interesting part is
always how was the Oracle
manipulated uh in this case surprisingly
simp
simple teller is an oracle where uh it's
it's less permissioned than uh like
chain link for example and the way you
can uh the way they secure it is you
deposit um trb then you can post prices
and people should um go in and say no
this price is not correct and they slash
your deposit right so this naturally
takes time the buck a buck we see in
many Oracle attacks is you want to have
the latest time you don't want to wait
right so in this case also B Dow they
used that they used the latest price
which the attacker just by staking 10
trb could basically arbitrary set and at
this point the attack is easy right at
this point it simply
means uh lower the price deposit a
little for a lot of the other uh the
other value in this case Euro and um and
then increase the price and withdraw and
and off you go right so this is what
happened
um what did we learn here and this is
really an important part if you build on
stuff which is critical to your protocol
you need to understand it really well
and this is especially hard if you
change a little right you go out you
have an idea how to improve something
you change it a little but you don't
understand even if you read the code and
try really careful to do that but even
if you develop it from scratch and you
depend on libraries on Services outside
of what you developed you depend on them
honestly as as Auditors ourselves right
it's so hard
because we as an ecosystem some some of
very good at documentation some aren't
and in the end you need to read the code
of that large system you integrating
with to really understand what it's
doing because the documentation doesn't
give that
away um I was just yesterday talking to
one of the main devs um of uh the the
open Zeppelin libraries or the main Dev
um and an idea hopefully it
happens is do an underhand handed
contest for those libraries we all
depend on right we have an underhanded
solidity contest it was so so this year
was hard to find something apparently
but it's probably easier to find
underhanded stuff in libraries or uh
these kind of systems so it's really
important I'd say one of the main
learnings you need to understand your
stack to a degree which feels paranoid
at
times um yeah of course in this case
also there were some uh neglects on re
aiting the uh changes later and so on so
so this is also recurring
theme um yeah other other learnings like
what would make this easier use multiple
oracles and we'll have a hack where that
really fails um we we can put hard caps
in sometimes this works sometimes not
try to do holistic audits this really
helps uh but but it's really expensive
so I mean get it when you when it's hard
but of course in this system there was
really a lot at
stake um yeah and then on
oracles yeah it's it's very hard you you
really like I I applaud those it's a
centralized often a centralized piece of
infrastructure and and trying not to
have that is very important but you need
to understand the security caveats of
those and also oracles they should
really try very hard to push the
knowledge about this security caveats
down to users and then this is going
Beyond like I can say like just use
chain link right but that's not also
that means yeah you trust a multi signal
right so
um you need to know what you are into
yes there is a security flow in the year
C20 standard that was classified as a
lack of transaction handling in 2017 in
confirmed that this is a security issue
in 2023 there were 60 millions of dollar
lost because of this problem on 1st
November 2024 there were 90 Millions
lost two or three days ago another Us
lost 25 millions of dollars to this
issue which remained unpatched since
where a security issue that was
discovered 7 years ago cost 55 millions
of financial Dam to ethereum users
during this year and did chain security
report the security issue in any of your
C20 contract that you audited so
far the last part you need to repeat
what was the last did you report this
issue if you any of the is this about
approvals soorry what what's the issue
with I mean there are known caveats with
r
c20s you mean that we don't verify zero
address
transfers which which attack
exactly uh this is not the attack this
is the violation of security principle
of fail safe defaults when a user is
trying to deposit tokens uh to address
there is no way to verify if this is a
correct invocation or not and when a
user is trying to deposit funds to a
Smart contract this is 100% possible to
verify if this is a correct transaction
or it must not happen for example if you
are trying to deposit nft to a Smart
contract which is not designed to
receive nfts it will not be deposited if
you are trying to deposit e or erc223
token to a contract which is not
designed to handle these deposits it
will be automatically rejected and with
ec20 it doesn't happen as a result users
lost $15 millions of dollars yeah so
I'll answer that first of all like it's
not a issue in the standard itself
standards are meant to be generic if you
use web2 in fact Swift for example you
can use Swift to transfer money to
anyone who doesn't even know how to
handle it or what to do with it to a
bank which is malayas to a bank which is
under collateralized it it's just a way
to transfer money although I do agree
that there should be protection for
users to not transfer to things to
places which can't handle it but it
needs to happen at the wallet level not
at the standard level so the the the
general thing is here how hard as
developers as security people should we
it or how how hard should we try to
prevent user errors right we can always
say like these are cases where you say a
careful user will not have a problem but
the standard allows a user to make
errors clearly the code is much simpler
by allowing those it's harder to think
of all the
caveats this to this I'd say it is valid
it is important to explain that people
who use it know how this is done it's
not a fault of a standard to allow this
it's a fault of a standard plus the
community to not educate about this
problem right excuse me are you trying
to say that error handling is optional
and in some cases it is unnecessary to
handle software errors even if it causes
the loss of money for your users are you
saying that what the creator of ec20
standard is calling a security issue is
in fact not a security issue and uh are
you trying to say that if wallets failed
to solve it for seven years they will
magically solve it in the next years
what do you expect now again you're
confusing I'm not denying it's a
security issue I'm saying it's not the
standard where it should be fixed any
standards by definition should be very
generic to uh support any use case even
if you look at as a traditional Finance
you can send money to anyone it doesn't
matter uh using Swift using different
current company uh like uh countries
have different standards erc20 is a very
generic standard and it's not even just
for money where you have loss it erc20
token could be any representation of
anything it doesn't need to have any
value people could use it uh like you
could build functionality where you
intentionally send tokens to places
where they are not supported to increase
visibility of that token it just goes
there it stays there for example so
there are many use cases of erc20
standard this is a security issue that
needs to be fixed not at the standard
level at the wallet level or any place
where the user interacts with it um and
I agree with you like the wallets have
not 100% fixed it yet but a lot of
wallets now have added protection I
think metamask has it rabby has it and
so on if you try sending money to like
self address or zero address it will
give you a warning before moving it so
it's not that we have not done anything
but yes our industry as we discussed at
start it's not mature enough we have not
had the 50 years of progress that the
web2 has had to iron out these issues it
is an issue people are working on it
we'll get
there okay I'm skipping a few more
things here Atomic wallet it is a very
interesting hack to be
honest and I think some people know a
lot more about this hack than I
do um some stuff happened in here
but somehow like like a lot of people
got
drained they got drained at the same
time using Atomic wallet but it's
unknown
how
um this this simply is another private
key
compromise
um yeah so
um uh quick uh how how much more time do
have two
minutes the classic we can open the
document real quick see if there's
anything um yeah so so no then we'll
share the presentation afterwards it it
has like of course more more things in
there um a lot more hacks
um yes so so we'll use it for for final
final other
questions
um because yeah I will not explain a
hack in in a minute
okay then any final questions any other
questions comments
anything someone so of course feel free
to um is there one ah very good yeah
with uh egap machines how do you manage
software updates uh with What machines
uh let's say you have an airgap signing
machine how do you handle updates yeah
for sure so there can be different
levels of air gapping if you are just
purely using it for signing you don't
necessarily need to ever upgrade it like
it's just there it works if it's working
don't it's not broken you don't need to
fix it like even in fact ATMs for
example were running Windows XP for 10
years after it uh like security timeline
so if there is if it's air gapped the
security vulnerabilities are not really
applicable to it U but you can also um
just Whit list certain repositories
where you get updates from and just uh
in the firewall and get updates from
there um you don't necessarily need to
disconnect the machine completely from
the internet and it would be very hard
to actually do signing uh when it's
completely disconnected you can
technically but it would more be an HSM
then than an uh air gapped machine so
you it's just use a firewall good
connections whiteless base are okay
everything else blocked by
default I also made good experience with
um live CD style
systems so where where yeah you kind
of uh just have it for that transaction
and afterwards you you get rid of the
system again just by unplugging shutting
it down right and then it it uh this
works quite nice to uh not have
continuous
exposure okay thanks
everyone thanks you can if you have more
things to um if you want to ask more
stuff about other hacks um we we can't
be here in the front because there's the
next Workshop a very interesting one by
by the red Guild I can recommend it on
how not to get fished but um you can
catch us outside too of course thanks
folks
yes
