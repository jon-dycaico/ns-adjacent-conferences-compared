e
e e
[Music]
sh
oh
true
to
for
is
in
morning everyone okay okay it's my
pleasure to start the session today and
yeah my name is min and I'm from the
National University of Singapore and I'm
working on parallelizing on the stuff
and today I will introduce about our
work on parallelizing uh evm execution
so uh yeah let's
uh go into the details so this is a very
high level overview of what this talk is
about basically we have gbus are very
powerful accelerators invented decades
ago mainly for gaming but then it found
it use cases in all other uh domains as
well people have used it for general
purpose Computing uh scientific
Computing and recently AI pick up the
trend that's one make Nvidia become the
largest company in the world by market
cap so yeah on our um blockchain domain
we found a use case in uh Mining and you
have seen like people use it for mining
ethereum for a long time before the
merge but then after the much a lot of
comute power on on all of those gbus
like they some of them come back to uh
become AI training inference but some of
them finds that you new use case in GK
so you have seen quite a few talk and
this de gone about accelerating Pro
generating Pro faster using GPU but this
talk is about something different so we
want to find okay those gbus accelerator
power what can we use what else can we
use it for to help the ethereum
ecosystem so we think about one more use
case to um Beyond ZK to run the
transactions in parel so nowadays most
of the transaction you can see is not
just simple transfer from one account to
another
so the transactions now are more complex
smart contract executions and those are
quite comu intensive sometime that is
also the one of the reason for people to
set up like block limit and block scale
limits so that the computation is
bounded so you can uh verify run all the
transaction in Block time and
um so uh but we we don't intend to use
uh this work to like run your
transaction in Manet we found the use
case in fing to secure smart contract
the use case we found from our work when
we build our in-house fing tool to uh
find bucks in smart contract we got the
chance to uh run and test and also
compare with states of the art work in
Academia and also in industry and we
found that there's a very high demand to
run transaction and test and you get
some feedback you get some uh result so
you can finally the main goal is to find
the buck in smart contract to secure
your uh
application and GPU is just the main
like just the the the the best like uh
accelerator for you to run this kind of
thing in this use case because it has um
the massive parallel programming model
you can run like thousands of threats
and how about we map those thousands of
threats into thousands of evm instances
run in
parallel so running transactions in
parallel first we um focus on the niche
fing use case but then along the way
when we Implement our project we were
approached by different teams uh
startups they all building cool stuff
and some of them use some of other uh
sore to F out and have their own private
TR with their own amazing use case in
the ecosystem but this main this talk
will be mainly about fuzzing I will have
one slide about the other use case in
the
end so what is fing just a very simple
uh high level understanding uh so first
thing the main purpose is to find uh
buck in software is one of the popular
technique in software engineering and
recently there's a trend for people to
apply it to find buck in your smart
contracts as well so this is a very high
level depiction of gray box fing
basically you have a tool that generate
a lot of inputs those inputs have more
coverage and more complex than your unit
test usually you use so it's more
complex than they eventually it's a
iterative uh process you generate input
you execute it and then you get feedback
so those feedback can help the the
further to like generate better input
eventually you can find the input that
can trigger the buck in your smart
contract or in other subsquare so the
input are the so if you map it into um
ethereum transaction to test smart
contracts the inputs are the states and
transaction to interact with your DF
your smart contract and then the
feedback can be traces branching data or
the updated state after you run the
transaction and those are up to the uh
fing tool design and
implementation and yeah so one example
on the right is how they instrument the
evm to catch bux I just show very simple
example some of them are not uh like the
ad overflow is not very uh like it not
exist anymore after solidity eight
because they inject by C to check it
before they try to revert it before the
Overflow happen so for example if you
want to catch over flow you just
instrument the event to every time you
see upcut ad you check the upand if it's
like over uh the the two to the power 2
interesting up Cod is jum ey on of your
if else condition in your smart contract
or require statement it will be encoded
into this jum ey and those will be the
helpful hints for the fing tool to
further generate better input I'll show
one example of the Run uh after after
this so this is fing on a conventional
iterative process on your CBU then we
try to map it into GBU execution so you
see um our vers can generate thousands
of input instead of iteratively one by
one now you can generate a a bulk of
them like a batch of thousands of them
and then you can offload the execution
of thousand subd into GPU so this is the
main uh idea the main uh proposal in
that that uh our project trying to
achieve so so after we upload the
execution to GBU we can map one or few
threat in GBU to run this uh transaction
simulate the evm and then you get the
feedback back to the verser on the CBU
and try to update it internal stage
strategy generate better
input and yeah that's about it you have
to uh work you have to uh have some Comm
communication between uh the accelerator
and the CBU side and they all work
together to find bucks in your smart
contract okay so we offload the evm
execution to uh GBU and the AVM
execution basically you execute one uh
transaction and then you given the world
state so this is a very high level of
what is running inside so you see
nowadays like uh transaction interacting
with smart contracts are quite complex
they have Dynamic Behavior it's not just
one single evm call you run and you exit
it's actually uh every time you have a
con context and then each of them have
the volatile machine stat like stack
memory and they have their own size and
it's like evolve over like the running
at the run time we don't know beforehand
so this is also one of the challenge
when we try to implement on GPU we canot
just preallocate the for example you
know the stack size uh maximum stack
size and maximum col dep if you
reallocate everything is is gigabyte so
and we we don't need to do that uh at
the beginning so that is one of
challenge
and when you have call context and then
you can create a new call context or you
can rever back or exit and update the
parent State uh depending on the result
of the the child
call so these are the high level and
when we map to the GBU threats actually
we only consider each of the the current
call context uh so when you enter call
context you have your own St memory uh
volatile machine States and then it will
enter the execution Loop basically you
just give fetching uh new upcut and
increase program counter executing the
logic and then um eventually this Con
context either uh return back revert
exception or create a new con context
and it keep looping um and then we we
have the decision of how many uh G
threats that we can map to execute one
uh evm instance and imagine we have to
run thousands of them so the decision is
actually uh um dependent on one of the
library we use uh we use a cgpn library
from Nvidia lab to reduce the complexity
of development at the moment so they
have the limitation like how many
threads we can configure to compute one
U into physic um arithmetic operation so
imagine it's like some big in uh library
that you can use out there and um yeah
and also because they have some
limitations so we are currently have a
plan to develop our own uh library for
this they are developed for uh very
general kind of use cases you can
configure the bit width but then for our
use case you only need to use 256 uh you
in so yeah we can optimize a bit more on
this so this is how you map the evm to
threat and um after we Implement maing
using those library and you need to
ensure it's correct and uh for this one
uh when we develop this one we didn't
know much about the tools in the
ecosystem so thanks for the advice from
etherum Foundation we we actually need
to implement and compare with other EV
as well so uh we um we integrate with go
evm lab which is the uh the tool
developed by cor developers of ethereum
and then it's available there and we uh
make sure our traes are compatible with
other EV as well then we com compare
line by line so we use eiib uh 3155 make
sure it's outb correct and then um we
compare and then we uh use ad test to
compare and then uh currently we B on
the test and functional folders that the
important one and the one I highlighted
here are the one that are most time
consuming to us or recombine contracts
and general knowledge they are just a
few recombine contract but the logic and
the time we spend on them is quite a lot
so yeah uh evm of course is simpler than
this and some of the things we can use
open source but some of them we have to
develop on our own especially uh easy
bearing actually we copy from the bython
library from ethereum so we write it in
Cuda based on the logic there and um so
after the all the test so rare Corner
cases remain and mainly gas difference
uh so yeah so if your uh fing ju case is
not reliable the logic not reliant on
gas termination or some of the logic
then you can actually use it correctly
so we are still trying to uh fix on of
the remaining gas
difference so after we have satisfy with
the correctness then we think about
optimization uh so because time is
limited our developing time also the
time of this talk so I just uh bck one
of the optimization
that we did recently to show what what
we are doing so basically um some of
the we we try to optimize the normal uh
transaction that you usually uh see out
there in the real block and the real
Transaction what are the popular up
course what are the things that critical
to Performance what are the things that
you have to uh execute all the time so
we optimize them first so basically with
we check the statistics and then we
found okay it's it's quite intuitive
it's quite uh obvious that the stack
operations is almost everywhere you have
to optimize the stack the first and then
after that we also check
the the stats of the stack size what is
a normal stack size that usually
transaction use and what's the memory
size uh then the program counter it go
up to 5 8,000 so we found out okay we
cannot cat the program cter is too much
sorry catch the buy Cod 8,000 by is too
much but then stack side 20 something we
can allocate the fixed size uh stack on
Fast memory that's what we did so we
should alloc pre-allocate that one first
very fast uh uh stack on sh M and then
after if you your stack is bigger than
that you can use a slower memory as well
so most of the transaction you use this
you don't use a lot
uh you don't use large uh stack then it
will run very
fast H that's the one of the main uh
optimization that we're trying to do we
try to optimize for conventional common
transaction you can find out
there okay so current implementation we
are happy with one uh Beta release
currently so basically uh we support
Shanghai we started with Shanghai but we
couldn't catch up with new evm hardw
it's quite a lot of e implementations so
we stop at Shanghai first and then uh
executable we output the Jon trades and
then we have two versions CBU GBU and we
also have the share Library so you can
use it in two mods one is you use the
this share La Library it's open source
now and then you can use it to try on
Google collaborate uh collaboration the
Google collab you can use uh GPU there
so uh yeah you can use in two mods you
can write your python Cod to interact
with it and also you can use the
executable um yeah so performance is
still depending on the workload um so it
requires more comprehensive benchmarking
but yeah we compare with our own CPU
version is faster but one one thing is
that uh our CPU version is actually
slower than the current um evm
implementation out there so it's not
like directly up to up comparison and
yeah we are still improving the
performance
um yeah so this is one of the sample run
in fing and real uh like in action so
you can try on Google collab the link in
our GitHub reel and then uh one example
is a to example in smart contracts with
some of the very obvious Buck there and
some of the input guarding like if
condition so to make sure that you do
some real fing you make sure you get the
correct input you can run it and
eventually it will like output the line
the S SC line and the input that trigger
the the bug like you see input equal uh
inut 4 five 6 7 and Trigger the bug it
can show you the S SC the line bu this
one running the execution running in GBU
so besides the detecting bug we also
have feedback so this are feedback
raning feedback one example is this
function test Branch uh it's like
there's a condition for input to be uh 1
million and you see the current input
and the distance before you can break
that uh Branch those are the gray box
for the technique that we Implement in
here those are quite common in in uh
great BL fer uh uh fing tools out
there and our current relays the botton
neck is still remains in the way we uh
repair transaction and we get back the
serialized data to update the state of
our fing tool so it's stillo slow but we
have experiment experimental Branch
where we remove on of the complex logic
and of course this Branch does not
confirm with the yellow paper anymore
more but then it will reach very high
throughput it can reach like 60k uh
transaction per second and improving and
we saw some teams have rivate reel and
some of them uh clone a for from our
Rebel with with like private
implementation on optimization they can
reach th 100,000 of transaction per
seconds as well but we are offens source
and we're trying to make sure it's still
confirmed with the ethereum standard
and uh Beyond fing this is uh some of
the interesting use case where we talk
with other teams uh other team doing
cool stuff out there but they are doing
the layer two and also vering uh but the
main thing when we we were thinking
about bariz transactions for ethereum
execution client is it possible it
sounds cool but then it's not very
practical at the moment because you need
more transaction currently how many like
hundreds you need uh you need thousands
to have like to to um exploit that
parallelism in GBU and also the
transaction they are all
different they they are not very uh
similar so it's not easy to uh achieve
speed up on GBU and also to achieve this
kind of thing you need more client
support like
the GB memory you cannot just get that
terabyte of wor stat it's not possible
it's in the minute it's too big to run
and also because of memory concent and
also uh the client need to ensure it's
safe and correct to run those
transaction parallel which is not
because transaction you need to run
sequentially to one by one after the
other and eventually to get the final
State this one run in parallel there you
have to make sure that all the not
running it reach the same deterministic
output so they can reach consensus
otherwise it's it's not possible at all
so that's what we think at the moment so
we still can find all the use cases be
besides like trying to uh speed up
ethereum execution client uh we see
other layer two teams also can try to
have their own uh execution uh engine
also transaction simulation platform I
saw like people use it to simulate swap
for example and imagine you have a lot
of similar transaction testing
simulations and this one is a use Cas
for it
yeah you can simulate million of squab
in a short time serving a lot of
users
yeah okay so uh the last two slides I
want to talk about our team and
collaborators so yeah working with me uh
also uh we we have a small team of three
res Searchers and Engineers uh working
with me is Chan Le and we are from the
Singapore blockchain Innovation programs
uh n us also working with me was Dan and
uh we work in Singapore before and he
went back to Romania to become professor
and uh yeah we want to thank Fredick and
etherum foundation for the advises and
the grand support especially the advises
to make sure it's correct and how how to
use all of the new tools in the
ecosystem that we were not really
familiar with thank
you yeah so that that's that's all about
this one and you can find out on the
GitHub and um yeah just feel free to
create BR open issues discussions and
reach out to me uh I will try to
help thank you man and thank you for
this amazing presentation um so I have a
few questions let's go through them
let's take the first one how much work
would it take to integrate this in an
open source fer like a
kidna uh yeah you you can use it
currently we release the the uh the
share Library you can see it right away
but the thing is you need to modify your
further our our uh example toy fer we
have that bot neck to repair thousands
of transaction before you send to GPU
that one is quite a big Buton neck you
run in on GBU is fast but then you
prepare for it and you run you collect
the result is still quite bad so
currently need you we need time to like
improve the interaction between the
library and your fing tool so it works
but you need to work on piping yeah the
interaction yeah okay on Plumbing all
right can cute VM plug into sorry qvm
plug into a simulated node tool like
Anvil or if
tester yeah so in the end we need to
make sure it's uh it's possible but we
need to make sure it's compati for API
call so basically we provide that
Library if you have your own adapter
your requirements so you just send us
the state and the transaction you want
to run but should make sure the state is
not so big we can manageable like
transfer it to CBU and keep it there
sorry GBU memory and keep it there then
it's possible to transfer the state
transaction run and return it back to
result uh whatever result for matter you
want fantastic than thank you all right
third question would fuzzers have to
change to adapt your GPU acceleration it
seems like this is a version of the same
question let's mark it as answered all
right fourth question how does the GPU
Fred get the state from when executing s
load well that's
specific okay you want to take the next
one so we have the data structure that
reside on global memory so for the
states memor and memory we we have to
keep it in the slow memory we don't do
any caching and that one we keep the
structure pointing to the state and we
set through that so basically if the
state is Big so this is one
implementation detail we didn't
Implement very fast searching in the
states basically we have to go through
on the array of accounts so if the state
is so big currently it's quite slow but
yeah uh that's how it works so
everything on global memory we have to
set through them fantastic thank you all
right we still have test second 10
seconds so maybe a more playful question
have you considered calling it cute VM
rather
than but you know suggestions you know
yeah yeah we my CH to this time
wonderful I mean thank you for your time
and all the work you obviously put in
your uh in your slide and um looking
forward to your work yeah thank
you all right friends we'll be back in 5
minutes with our next speaker Valentine
from East Zurich stick around he has
plenty of really cool stuff to share
and we're back on all right people next
speaker is Valentine from eth Zurich e
Zurich is not an EIC organization it's a
leading uh it's a leading University in
Switzerland so Valentine is is to talk
to us about fuzzing infrastructure get
ready to get your mind blown and like
for the previous session scan the QR
code is going to appear here to ask your
questions and I'll make sure to ask the
best ones at the end of the session also
make sure to read the questions that
other people have asked because you can
up vote them and the questions that have
the most up votes will be treated first
all right Valentine please come in
welcome
good morning everyone so today I'll talk
about fuzzing for zero knowledge
infrastructure and this is Joint work
with my collaborators from the Technical
University of
Vienna so just to kind of make sure we
are all on the same page um let's have a
short definition of what I understand by
zero knowledge infrastructure so uh for
this talk I'll um Define zero knowledge
infrastructure as software components
that are used for compiling executing
proving and verifying ZK circuits so
examples would be the processing
pipelines that are commonly used by uh
dsls for describing ZK uh circuits or
maybe in the future we'll also look at
entire ZK
EVMS so um with this out of the way um
let's
um look at why this is an important
topic and why um more people should be
doing this well first zero knowledge
infrastructure is highly complex and
highly critical for instance it's used
in several L2 chains so kind of bugs
there uh could have a catastrophic
financial and
reputational uh impact and we should
really make sure these components are as
bulletproof as they can get
um while we haven't seen a really
catastrophic incident uh in this field
may maybe perhaps uh comparable to the
Dow hack in
have uh rigorous testing for these
components and we use um you know the
best engineering uh discipline that we
can um have right uh because these
components are really complex and
getting them right is is not
easy so what is fuzzing I don't think I
have to like explain this after the last
uh talk but fuzzing is widely used in
industry um for instance at Microsoft
Google meta uh they're fuzzing a lot of
their infrastructure uh to catch bucks
before um hackers can actually exploit
them in
practice so in this talk I'll give you
an overview of our fuzzer for um finding
critical bugs in processing pipelines
for zero knowledge circuits um the
fuzzer is called Circus and it already
supports four of these pipelines namely
uh circum cor uh Gnar and Noir and
there's you know like a a gazillion of
different dsls popping up it seems like
you walk around here and you see another
one in the corner
um and we've already found uh 16 bugs in
total for the four uh pipelines we
looked at um 15 have already been fixed
so that kind of shows that these bugs
are really uh taken seriously and um
developers sometimes respond within
hours to actually get them
fixed um you can also see a kind of uh
breakdown of the different uh bugs and
where we found them and as you can see
they're kind of very evenly spread
across the different uh Pipelines so
it's not like there's one pipeline
that's you know responsible for all the
bugs uh that we
found um now kind of to make sure that
everybody understands I mean like I yeah
I assume not all people are aware of
what these uh processing pipelines look
like look like uh here's a short kind of
summary um you can see in the sort of
yellow box um there is uh a circuit that
the user writes um that goes into the
compiler and then the compiler um hands
some output to the witness generator and
the witness generator can then take the
input so the you the user input uh to
the circuit and generate a witness uh
that can be then used by the prover and
then the prover generates a proof that
can then be verified to essentially
check that the circuit was actually
executed
so um now that we have a bit of an
understanding of how these pipelines
look like let's uh dive a bit uh deeper
to understand how we find these
bugs so first I want to be very clear um
we are not cryptographers this is not
our uh this is not my background my
background is in you know uh software
security uh program
analysis um and for this reason I can't
really you know try to understand the
the logic that's in the integrate log
logic in many of these
components um which is why we treat
these essentially as a blackbox so much
like what a typical user would do uh we
just view them as a
blackbox so how can we still find all
these bugs right well first we have a
lot of experience uh in testing uh
complex or software for complex domains
and building fuzzers for them so we've
done quite a bit of work on uh fuzzing
for smart contracts it's probably the
work that's most closely to the audience
that's here um and for instance we
created the Harvey fuzzer um many years
ago and we're still kind of maintaining
it um we also did some work on ML models
um and on on testing ml models and
testing program analysis tools um yeah
if you want to know more check out the
papers that are um
online um and the second reason why we
were able to find these bugs is that we
have a not so secret weapon which is
called metamorphic
testing so before um explaining in a bit
more detail what metamorphic testing is
let me just give you kind of a uh short
summary of how we got here how we got
into this uh interested in this topic um
so we were as I said we were um working
on fuzzing for smart contracts mainly
uh for many years and then at some point
um I guess maybe like a year ago roughly
um consensus they released the linear
blockchain um that is one of the first
ZK EVMS and we were like well this is
really complex uh we started looking
into it a bit um and we saw that there
are these components like the gnark
library and the cor uh language for U
processing zero knowledge circuits so we
were like oh what can we do to to you
know um test these what can we do to
make sure that there are no bugs in
these
components um and that's when we started
building um kind of a predecessor to
this fuzzer uh I'm presenting today uh
which was called
Rio um so the Rio is a fuzzer for thear
Library specifically and then
essentially this uh circus fuzzer I'm
presenting today is essentially an
evolution of this uh fuzzer that is a
bit more General and can Target multiple
um
dsls all right now uh back to
metamorphic testing so what is
metamorphic testing um I think the
shortest way to summarize it it's kind
of a way to define test oracles uh in a
pretty elegant and concise way so to
illustrate I've um I've uh collected a
few examples that um yeah explain this
uh try to um explain what metamorphic
testing is so so the first example is
how to actually test that the Sorting
function uh sort for an input let's say
an array of integers X actually does the
right thing well there's many ways to to
check this but here's uh a way to check
it um using metamorphic testing so you
take you sort um the input X and then
you also sort uh X but you Shuffle it
randomly right and these two um the
output of both of these in ations of the
function they should have the same
output right so pretty nice and concise
specification so let's look at another
example uh here um we want to test um
essentially some procedure for computing
the shortest path in uh graph G between
the nodes n and M so how can we do this
with metamorphic testing well one way to
do it is to say you know the shortest
path um between n and M uh in the graph
G is less than uh the shortest path
between n and n and n and M um in the
graph where we take G but we remove uh
some random Edge right because that edge
might have been on the the shortest path
and then the shortest path could become
longer
right so we can also do apply the same
kind of principle to more complex uh
components like a entire compiler right
so here's an example of how to do this
with metamorphic testing um when you
take a program p and you compile it and
then run it you should essentially see
the same behavior as when you take um
the program P but you add some dead code
somewhere randomly right and you compile
it and you run it shouldn't matter right
should give you the same output
essentially so with this um let's look
at how we can apply kind of the same
reasoning principle to uh zero knowledge
uh circuits so the fuzzer what it does
is uh it first generates a random
circuit uh C1 and then it applies a
random transformation to C1 to get a new
circuit C2 so now we have two circuits
that are essentially
syntactically perhaps completely
different um but semantically they
should have uh the same
behavior and now we the fuzzer generates
an input I
and um invokes the processing pipelines
for both of these circuits um and if
there's any difference in you know the
output or the behavior then that's a bug
somewhere in this processing
pipeline so for instance um the for one
circuit we might not be able to generate
a witness but for the other one we would
then there's probably a bug somewhere in
the compiler or in the witness
generator so um let's look at a few of
these Transformations uh to kind of
understand how the fuzzer does this um
so here's a very simple transformation
uh if you have somewhere in your circuit
an expression e uh you can always apply
um you can always multiply the
expression by one right that should not
change anything um or you can also
divide by one again shouldn't have any
effect on the
circuits um another transformation is to
basically negate the expression e
twice or you can also apply other
Transformations like um swapping um the
two operant of a
multiplication and then we also have um
um some Transformations that use
essentially new randomly generated
Expressions so here for instance we
replace an expression e with e minus
some random expression plus some random
expression right that should again not
have any effect uh
um and we have a small DSL for
describing these circuits so there's
many more of these
Transformations um So currently we
support roughly 90 uh such rules but you
can easily add more of them and think of
new ones if you want like
to so uh we also found a number of bugs
in um the different uh pipelines and
let's look at a few of them um just to
kind of give you the the idea and show
give you a concrete example um that you
can look at so here on the left uh we
see uh a small uh example circuit in in
the circuit circum um language uh you
can also look up the GitHub issue uh if
you if you'd like to um but this
essentially a minimized uh cleaned up um
version of the
circuit um and
as you can see there's a variable P um
in practice this is essentially just a
constant uh just didn't fit on the on
the slide so I um yeah put it at the
bottom um but think of P just as a
normal constant in your program and now
what the fuzzer does is it generates a
transformation of this circuit which is
the one that's shown on the right and
here it applies a number of um
metamorphic Transformations so for
instance it seems like the fuzzer first
um multiplied the expression P by one
then subtracted Zero from one and then
divided um that expression uh by one and
when we execute this um when we execute
these two circuits we can see that
um that the output out one and out two
actually are not the
same so this is bad and this is was a
bug that we found um seemed like there
was a bug in the witness generation
part um and here's another bug um that
we found in gnark um so at the top you
can again see the the original circuit
that the fer generated and then we can
also see the transform circuit um where
the fuzer essentially changed the
expression zero to just zero or zero
which should be equivalent right and
here um we observed that for C1 uh there
was no witness that was generated uh
whereas for C2 there was so this again
is um a bug somewhere in this uh
Pipeline and yeah now that you kind of
hopefully got an overview of the of the
tool and saw a bit how these bugs look
like in practice um I hope more people
will you know uh uh start looking into
this problem uh because I think it's a
it's a very important problem uh we need
to really make sure that these
components are uh bulletproof uh because
otherwise you know pretty bad things can
happen um it's better to do this before
the some you know attacker does it right
um and you don't need to be a
cryptographer to actually find these
bugs so you know that makes um gives
just a lot more um people that can
actually uh look into this um because I
think so far we only really scratch the
surface so there's more more things that
need to be done to to test these
components also there's components like
this popping up um uh every now and then
so we really need to um make sure
they're safe and we also should do um
continuous fuzzing of all these
components so for the gark team we
actually implemented a continuous
fuzzing setup where you know they when
they whenever they commit the latest
version to master uh we we start a new
fuzzing campaign uh we run for 24 hours
we tell them if something is wrong and
then the next day same thing happens um
we're also planning to do the same for
cor and if you're interested in um you
know us uh taking a look at your uh ZK
infrastructure uh please reach
out and if you want to know more about
uh what's going on in the fuzzer then
please just check out our paper uh you
can scan the QR code there um and if you
you know want to let take a
look um
yeah
fantastic thank you Val Valentine for
this presentation um let's get to the
question shall we yeah all right so I've
sorted the questions again you have a QR
code here you can ask your questions and
I'll ask the ones that are the most
voted so let's go to the first one when
you identify a bug can you just say hey
there's a bug or do you provide a path
to fix it like do you identify where the
bug exist within the circuit uh we don't
directly identify where the bug is but
when we generate the the test inputs
like the circuits uh we try to minimize
them so we try to keep them as small as
possible so the developers can really
hopefully quite easily identify where
things go wrong um and yeah so far I
think the complaint the the the
developers were very happy with the bugs
reported um and I think there was no
issues finding the the bug once they had
the the input makes sense thank you
second question do you fuzz logical
Expressions they're encoding in
circuits uh yeah we do I think yeah so
for instance we apply some you know some
common Transformations like applying the
Morgan's Rule and so on um so there's a
bunch of um these Transformations that
we that we use in the fer
wonderful
third where's the bug Nest where do bugs
usually reside in your historical fing
like from what you've seen um I think
it's it's hard to like can you really
derive U enough data from you found 17
yeah yeah I think it's yeah it's
probably too early to say but we did
observe that um the fuzzer found bugs
basically in um different components so
we found bugs in the compilers we found
bugs in the witness generator we found
bugs in the prover as well I don't think
we found bugs in the verifier it seems
like yeah that's kind of towards the end
of the pipeline uh and I think many
people are you know very concerned about
the you know getting the verifier right
so maybe that's also paying off uh here
um but we'll we'll keep trying
um we'll yeah we'll see nice um okay
when CYO
fuzzing um yeah we're I guess you insert
it in your slide if we're interested
people should talk to
you somebody from starkware wants to you
know uh us to look at more at CYO then
yeah please reach out um we're
interested um it's definitely a a good
idea to to do that yeah wonderful well
arud reach show um what do you think of
concolic testing of Z
circuits um I had to ask chat GPT what
concolic testing is okay and I still
don't understand it okay um yeah so
concolic testing um essentially I mean
for the audience maybe it's essentially
a way to you know generate um new inputs
by doing some kind of symbolic execution
uh but basically for some Expressions
that might be really complex like you
have non nonlinear expressions in these
circuits so there you might want to uh
concretize some inputs um and that's a
concolic part so it's like concrete and
symbolic um but yeah so the I think
that's that's an interesting area it's
not sort of what we focused on uh
because we we're not so much interested
in actually generating inputs for these
uh circuits um that's something you
would probably want to do if you want to
have a specific circuit that you want to
you know get right and you want to make
sure it h satisfies some properties then
you probably should think about you know
concolic testing for that circuit um
yeah perfect thank you how does it feel
to find a bug it like literally when you
find one is it is it scary is it
exciting I mean you're looking for those
so it's probably a bit exciting but it's
also scary there's probably money on the
line how does it till no it's definitely
I mean it's definitely exciting um and I
work a lot with uh students um
and you know it it really you know that
you can see they're they're excited when
they find a bark uh they're happy
they're making you know an impact um and
also the reactions from the developers
are a great motivation to find more bugs
because usually they're very um yeah
they have been very positive I don't
believe you there's no way you go to
people and say I broke your and
they're like oh yeah
amazing yeah I mean if if if you're sort
of yeah if you're
um yeah L2 and one bug like this can you
know wreck your system then yeah in some
sense your your job is also on the line
so you should you want to find those
bags I'm not saying you don't want to
it's just scary when I think about bugs
I think like yes I want to fix them the
first thing that comes to mind is like
oh yes no but you're right it's better
to be aware of okay we can actually take
the last oh one seconds left let's wrap
it up or do you want to are you using
property based testing for choosing the
input um we're I mean you can call it
property based testing but we're
generating the inputs right now uh
completely randomly so it's kind of
blackbox fuzzing that we're doing and
we're also considering to do more you
know feedback directed fuzzing like you
saw in the last talk um yeah fantastic
thank you thank you Valentine thank
[Applause]
you oops I'm not used to DMC yet all
right I see more people are joining in
welcome we still have a bunch of really
cool sessions coming up H we'll be back
in 5 minutes
n
hey
hey all right next section is starting
people um so for the next session again
don't forget there will be a QR code
here ask your question there up vote the
questions of your friend and we'll be
able to ask all of our questions to
Stefanos at the end of the of his uh of
his presentation stepanos is a PhD
student at Imperial College in London
he's also a part of ZK security doing
research in the zero knowledge field and
today he will talk about what we don't
know about ZK please welcome Stephanos
hello thanks for the introduction so
today I'm going to talk about uh
vulnerabilities mainly in the
implementation of uh uh snarks or ZK
snarks and also on what can go wrong
when we deploy snarks in production uh
this a joint work with collaborators
from du the ethereum foundation ZK
security the scroll foundation and also
imperior College London okay so let's
start um okay what is the state of zkp
applications today we have ZK rollups
that have become uh very popular in the
last two years they have more than 5
billion USD in uh tvl in them uh we have
Zas which is a payment system system it
was deployed I think the first version
around 2015 2016 we have many ZK
applications both for infrastructure
such as ZK Bridges
but also for private payments for um
using wallets without having to use Aid
phrases like ZK login we have private
programmable l1s and l2s like Mina Alo
azdc and also we have some of chain
applications and although all of those
systems have been deployed we haven't
seen any major exploits like uh the Dow
exploit we had in smart contracts
and although we haven't seen any exploit
there have been bugs in systems deployed
uh in production so zikas had the
vulnerability sorry for the pictures
might be a bit small but I will go
through through them so zikas had the
vulnerability for I think more than a
year in it um people from within the
zikas found it and uh patched it uh then
one of the most popular mixers had a
vulnerability that if someone exploited
uh it could have basically drained the
smart contracts of that
protocol one of the most popular Z
rollups had the major vulnerability that
someone could again potentially could
have exploited and get everything out of
that rollup and also I would say that uh
in audits in Z protocols even in topn
protocols if you compare it with top
notes uh smart contract protocols the
ratio of critical vulnerabilities it's
even higher so there are many
vulnerabilities and people for many
years suggested that zkps are very
difficult and very hard and not many
people uh actually understand them and
also they have suggested that to exploit
a ZK protocol it's much more difficult
to exploit for example a smart contract
uh vulnerability I would say the first
one is not true anymore right because if
you see the number of presentations in
ZK in Devcon this year and compared with
increase and also although it might be
true that some ZK vulnerabilities is
difficult to exploit I would say that
some of them are pretty simple and for
example here we have a circum circuit
it's uh a very old circuit but this
anyone who has written a circum circuit
could probably understand what's going
on here
and still there are such vulnerabilities
in Z protocols that I think are pretty
easy to exploit so there is a huge risk
uh if there are still vulnerabilities in
deployed protocols to be able to exploit
them at some
point okay so uh let's start with uh
explaining what are the properties of a
ZK protocol right we have knowledge
soundness which M basically means that a
dishonest Prov cannot convince a
verifier of an invalid statement except
with a negligible probability we have
perfect completeness which means that if
you have a valid statement and prover
will always be able to convince H an
honest verifier of the correctness of
that statement and also we have zero
knowledge which means that the proof Pi
that we produce with a zero knowledge
proof does not reveal anything about the
witness we are uh proving
so what is our thread model in uh uh ZK
uh word right we have three adversaries
we have the network adversary who
observe the system and its public values
but cannot interact with the system we
have the adversarial user which
basically is able to submit some inputs
for proof generation in a nonest and non
malicious prover and finally we have the
adversarial approver which is the most
common uh thread model and it's our
thread model when we actually need the
ZK property right but I would argue that
even if we don't need it if we want to
have a fully permissionless system then
that's the adversary we have and has the
ability to produce proofs and has the
ability basically to do everything to
try to trick the
verifier uh to give you an example of
what I mean with the second category
because it might be a bit confusing
consider ZK rollups at the moment right
where we have have a single centralized
trusted um L2 node that is both the
sequencer and the Prov so users can only
submit the transactions there and then
that centralized node will produce a
proof so in that case we have an
adversarial user
basically and what can be the impact of
a vulnerabilities so we might be able to
try to break sadness which means that
aover can convin a verifier of a false
statement and that could result in
basically for example in Zab to get all
the funds out of it we can break
completeness which means that a verifier
cannot verify proofs or basically that
theover might generate invalid proofs
right and for example such a
vulnerability uh could basically uh have
a high impact in uh the liveness of zq
rollups and we might also break zer
knowled which means we have some
information
leakage um okay so what we did is we
analyzed 141 uh bugs and vulnerabilities
from audit reports for from
vulnerability disclosures and from backt
trackers and our goal was to split those
vulnerabilities in layers and understand
what can go wrong in each layer and also
create a taxonomy of
vulnerabilities so let's start with that
figure so in the real work non snar work
we'll have a relation a specification
some idea that we want to actually
create uh zkp about it and we might have
some public and private inputs so the
first uh step is to manually and code
that specification that idea in a
circuit and get the circuit
implementation so we figure out that in
that level it's where most of
vulnerabilities happen and the the main
reason in our understanding is because
it's confusing for most developers to
write circuits because they have to be
to think both about computation and
talks about constraints and they might
do a very aggressive optimizations there
and they might try to apply some trigs
and that typically leads to
vulnerabilities so we identified three
main vulnerabilities under constraint
vulnerabilities which means that uh you
forgot some constraints or some of your
variables are partially constrained we
might have and that typically leads to
sadness vulnerabilities which is the
worst vulnerability can happen in Z in
the ZK system then we have over
constraint vulnerabilities which is the
exact opposite that most typically will
lead to completeness issues and we also
have computation or hintch errors which
is on just on the computation part and
accordingly you might have messed up
constraints but the root cause was in
the computation part
um so we did a complete root cause
analysis and I will share with you a a c
code for our paper to look into examples
and to look on how you can fix some of
those vulnerabilities Etc but very
briefly here we have categorized them in
three main root CA classes first is that
in When developing circuits we have a
different programming model and that
could lead to many vulnerabilities
secondly we observed that the root cause
of vulnerabilities were optimizations
and also having cryptography at the
outer layer and in very uh lowlevel dsls
that could introduce many
vulnerabilities and also common errors
like in any software uh like uh
specification issues or API M uses
Etc so the next layer is uh the front
end uh which is basically composed from
uh two components a compiler and a
witness generator the compiler will take
the circuit and will try to produce an
intermediate representation that it's on
what our proof system works on top for
example R1 Cs and then the witness gener
generator will take the circuit will
take the public and the private
variables we have and it will produce a
witness and the next one is a backend
the bent it's composed of three main
functions setup proving and uh
verification and things can go wrong in
all those functions so the
vulnerabilities we identified here in
the front end is incorrect constraint
compilation and errors in witness
generation and in the previous
presentation we saw how things can go
bad uh there and it's very critical to
actually trust and be able to have um
correct implementations of front ends
and in the back end the situation is
quite similar um we from our data we
found out that unsafe verifier it's a
very common issue and can lead to Major
vulnerabilities um and uh let's go to
the next one the next one and the last
one is the integration layer which is
basically you can think of it in the
blockchain space as the JavaScript that
is possible to run your approver client
side and create a proof and also the
smart contract that um consumes that uh
proof and calls the verifier you have
implemented or it was produced
automatically and try to do some things
and we had some very interesting
vulnerabilities in uh that layer I want
to focus in the first one which is
passing un checked data uh and what does
that mean
sometimes as already said we might try
to do some optimizations in the circuits
and for example one thing that it's
pretty common is for people to say okay
uh in that circuit let's have some
implicit assumptions that our inputs are
in a specific range and then delegate
that check to the actual code that will
call the verifier so in that example we
forgot we forgot to do H such a Che and
that could lead to Major vulnerabilities
then in our
infrastructure and uh in the last uh
year or so there has been a major change
in some architectures where instead of
circuits we have zvm circuits right so
the developers now only care about
writing some program typically in a high
level language like rust and then
compile that program and uh giving it as
an input to zv m still circuit bugs can
happen in the ZK VM itself and I would
say a sub new threat here is traditional
compilation errors that might happen to
the rust compiler for example that that
could lead to have invalid proofs so
that's something that people should take
into consideration when using uh Z KVM
sols so another way to see what we
currently uh described is in in a
hierarchal uh way and here I have an
example of all the stack uh when we use
uh the ccum programming languages and
snack Jes with growth 16 Azure proof
system I have two new layers here one is
fil arithmetic elliptic C which have
nothing to do with ZK but when we
construct and Implement um a proof
system we have to have such a very
efficient library and things can go
wrong there and those can go wrong in
the hardware in the operating system in
the blockchain we are using right so you
should always uh
be very
uh basically think about what you are
going to use and apply all traditional
best security practices we know from
other
fields and one last thing is that in the
proof system there could be errors there
there could be errors in the initial
description in the papers of proof
systems so if something goes wrong there
it doesn't matter if you have formally
verified circum circuits if you have the
best back end or front end it could be
exploitable and that basically it's true
for any layer so if your front end or
the back end it's uh vulnerable then
even if you have formally verify uh your
circuits they could be
exploitable okay uh so we did that
analysis and now I want to present some
of the results uh so we categorized the
bugs in uh all those layers and also
based on their impacts and we can see
that circuits was uh the number one uh
thread in the whole infrastructure of
using uh zkps and also most of the
vulnerabilities are uh uh res can result
in soundness
issues so what can we do uh fortunately
there has been like a lot of development
and a lot of research of uh creating uh
security tools for ZK circuits
for specifically for ZK VMS or ZK EVMS
and also in the last month two new
papers were published and tools circus
which was presented in the previous um
talk and also MTZ which is great because
such novel tools can detect
infrastructure bugs uh in circuits in uh
zkps but I would say there are still
still a lot of work that needs to be
done uh for example most of the circuit
tools they target a specific DSL and
also they typically Target a specific uh
vulnerability class and then we have uh
some tools like stattic analys tools
like circumspect which might have tons
of uh false positives and then we have
some really nice tools and very novel
tools like pus that try to formally
verify and find any under constraint
issues in the circuits but unfortunately
uh th those tools do not scale that well
uh so there's a lot of uh space to do to
have Innovation uh and try to build
better RS and here I have a list of um
security tools you can scan that QR code
and it's basically GitHub repository if
I don't have any of the tools that you
are know of please add them and yeah we
need to do a better job here and one
also major issue I see in the space is
that we don't have good uh tools for
writing tests and most of the uh
codebase that use your knowledge proof
are unfortunately not that good in
having like a complete test Sut and try
to to understand in the testing uh part
both uh soundness and completeness
issues okay so in conclusion why do we
have bugs one of the reasons is that
because zkps are not just mods there are
implementations and many things can go
wrong in those
implementations uh why else
H this is a quote from Ron riest in a
completely uh different context but I
really like it and I would say that in
the ZK space unfortunately we have give
to the poor developer uh enough rope
with which to hunt himself circuit
languages are typically very low level
so they don't have good obstructions for
developers to write um um safe code uh
we expose a lot of cryptography to the
out layers and also there is a lot of
complexity and a different uh threat
model than what uh developers are used
to and there is a lack of specification
throughout um the whole uh uh
infrastructure and the whole stock for
using zkps so we need to write more
specifications so what can we do
basically we have to negate everything
from the previous slide
we need more learning resources which I
think we are doing a great job in that
as a community uh we need to write
specifications and get used to write
specifications because uh if we have
complete specification then we know
exactly what checks we should put uh in
each uh layer and what vulnerabilities
can happen in each layer and that's how
we can help developers but also Auditors
into doing a better uh job been trying
to find vulnerabilities uh in those
systems we need easier and more secure
programming languages which I think it's
kind of where we are heading to uh for
example Noir is a is a great language
that it's much more safer than writing
uh circuits in circom or hello to but in
some cases people will still need to
write circuits in hello 2 or cicone
because they need to do some specific
optim izations or they need to deploy to
specific uh blockchains for example and
then we need better testing and security
tooling from simple Frameworks to write
unit test to do property based testing
to formal verification and not just
formal
verification uh so that's it I have
there a link with uh our paper where you
can find main examples and how to try to
avoid some of those speed Falls and we
also have a blog post that uh uh we uh
publish many blogs about uh ZK Security
general so thanks a
lot thank you stepanos this was
enlightening um all right people as
usual you can ask your questions here
we're going to go through them in order
and let's take the first one several
times in your slides you referred
Witnesses what are witnesses are those
private inputs uh so a witness I would
say it's composed from both the private
inputs the public inputs and all the
intermediate steps and the outputs for
our circuit so I will say it's a a trace
that then we create a proof about that
Trace thank you all right next next
question I've put a bunch of those so do
ask serious questions please we have a
bit of time what is your favorite bug
ever what is the most interesting bug
you've ever found h H that's a very good
question I think I can't pick one uh but
I would say typically the simple bugs
right uh for example the bug I have in
one of the first slids that could have
led to basically draining uh one of the
major mixers we have in the space um but
also bugs that have to do with using
cryptography in the circuits and
typically due to some optimizations or
some load errors in those circuits there
could be like pretty interesting
exploits that someone can do pretty cool
thank you all right the next one you're
doing research looking for bugs you're
paying your bills and buying your Foods
by finding bugs can we consider you have
a bug Bas
diet we can consider that yeah
definitely I hope that in some future
world there won't be that many bugs and
maybe I will have a better diet but
unfortunately at the moment we have tons
of bugs fantastic thank you what are
your thoughts on T okay that's the
question of Dev conl everyone asking
that question uh I would say it's a
different you have different security
assumptions when you use tees right it's
I think it can work along with zps but
they can't replace GPS H you have a much
weaker uh thread model when you are
working with the so yeah people should
use them when they have to use them but
also don't trust them like a black box
that will do everything for you and you
are secure if you use a te wonderful
thank you um what can we do to make more
secure languages like Noir faster
compared to circum particularly with
respect to gas cost how do we make more
how do we make it more efficient SO gas
C I have I will say that it's
independent kind of of uh what
programming language you you're using
it's more about like what proof system
you are using right and if that proof
system is has very efficient
verification that's the main factor but
also more General in the circuit uh
layer um I would say that indeed someone
if you don't like really use unsafe in
Noir which then breaks the whole purpose
of using Noir um you you can write more
optimized ciruits at that point in
circum but I would hope that we will
have uh uh major advances in compilers
for zkps and then we can have like
compiler optimizations that very strong
like in any other field and uh rely on
those optimizations to get like pretty
optimized uh circuits but if we do that
then we need very very solid uh testing
for our compilers to detect any issues
in those
optimizations thank you you mentioned in
your slide that you know sometimes we
give too much rope to the users to Ang
themselves with I think the design in ZK
circuits is diff difficult but also
using them is not very common place
right a lot of users are not used to
using this kind of systems and what goes
in what goes out what you can do with
them what can be what is safe Behavior
to do that you mentioned learning
resources do you think there's something
to do with users also to explain to them
what are the benefits and what should be
done or is it entirely on the app
developer yeah yeah that's a great
question I think as researchers it's our
responsibility uh to create uh learning
resources that are easy to follow by
almost everyone uh so I think we are
doing kind of a good job there uh for
example at zigi security we published a
book on hello to and basically many
teams in that space develop a pretty
nice learning resources and what I
really like is that they also have a
section about security vulnerabilities
and what you should look at when you use
a specific DSL so yeah I think we are
doing a great job on that and in the few
years it will be even better fantastic
stanos thank you we over time uh so
thank you for your talk thank you thanks
a lot
all right we'll be back in five minutes
with PR stick around it's going to be
interesting
m
oh for
t
hello everyone so I'm just here to
announce a small unfortunately we have
zero knowledge on the whereabouts of the
next speaker with the rain outside it's
possible that the street circuit was
overflowed I don't have a thir one um
we're waiting for him we'll be back we
we're going to wait for five more
minutes and um and hopefully you'll show
up and be able to present please wait a
little bit again
he
I
hey the next speaker is not available
unfortunately so the session is
cancelled the next session will happen
in 20 minute at 12 in the meanwhile stay
here grab a coffee enjoy the relaxing
mood and have a good time
a
w
oh m
you
no mic no mic
I can't people I'm sure people can you
wait oh wait you can hear me sorry hey
and we're back welcome everyone thank
you for showing up to this uh next
session the next session will be with
Richard so Richard didn't put a bio on
um the def connect on the Defcon website
so I can't tell you much about it but a
picture is worth a thousand word go look
up his picture he's with a deer so it's
funny um but Richard will talk to us
about the ejs API the iten gim and how
you can make the most of using this
specific Library so open your ears learn
a top of stuff and ask questions there's
going to be a QR code here uh you can
ask all the questions you want during
the presentation we'll cover them at the
end of the presentation and you can also
upvote the questions that you like to
make sure that they get covered by
Richard all right Richard welcome
okay
thanks um sorry I totally thought I had
a bio up but for those who don't know me
my name is Richard I work on ether's JS
um oh there's multiple red
X's which Red X
okay this one okay Sor um hi so uh I'm
Richard I work on ether's JS um I'll try
to face this one so I can talk to you
but I'll turn
around hello all um so ether JS is a
open source library for dealing with
ethereum um I'm guessing a lot of people
here probably use it if not uh welcome
and I hope you can try out some of these
new things that I feel are
like like when I tell people these
things the common phrase is I did not
know you could do that and then awesome
so uh I'll just start and
so uh there's different types of
providers so I'll go into a few things
first so first of all the multi call
provider for those that are familiar
with like multi call um this is based on
like kind of abusing how a knit
transactions work so there's actually no
contract on chain it works if you're
using hard hat on a pristine chain you
don't need anything deployed it just
works um I'll cover in a second how that
works but as you can yeah I'm going to
turn around ah sorry
anyways you can see so you have to pull
in the ex the ether's uh extension
package um you wrap your provider in a
multi call provider and this will make
sure that all the eth calls you send
kind of get wrapped up and like
sandwiched into this this weird compiled
solidity thing so that when you actually
make the calls they get sent off um in
parallel as one eth call and it gets
wrapped up in the multi call contract um
I'm assuming everyone is everyone here
familiar with multi calls I feel like
yes okay perfect um the one problem with
like mul calls in general is like if you
do a weight on each e call it can't
batch those together so you do have to
like kind of smush them all together in
this really annoying way in how
JavaScript deals with a weight async if
you'll have like a good solution to this
I'd love to hear that too um so one
thing to keep in mind with multi calls
that in this work this true for all
multi calls like message.
sender is
wrong um usually that doesn't matter in
a view function so uh and that's one
thing that's missing here is like there
should
view in there um it doesn't fit on the
slides and that's why it's not there so
uh yes um as so as a quick example of
like how you can like abuse the init um
this is very like like convoluted
example or very like I don't know like
quick example um but basically you have
your Constructor and in the last thing
you just put this like block of um
assembly and you're
basically returning the actual data you
want instead of the code that would be
deployed which is what a init
transaction usually does so you can
imagine the way you do this is you build
your bite code as if you were deploying
a transaction include no two address and
then you call the transaction as if it's
deployment and so yes please feel free
to come up to me afterwards and ask for
more information on anything in this
talk um but I'm excited about this
there's really cool things we can do
with this um anything that's a view is
that you don't need deployed to
contracts for is
wonderful um
so this is something I feel like
everyone really needs to understand
because it's so useful like people
always open issues saying such and such
isn't working and they're like I don't
know why and they don't give you any
meaningful information that you can like
work with so ethers has an event called
debug and if you do like provider.
on
debug it spits out a ton of data way too
much you definitely want like a filter
um but if you're doing ccip read it's a
great way to kind of like debug what is
going on with ccip read because it's
very complicated like back and forth all
over the place so it's nice to see oh
the URLs are coming back as not an array
or the URLs are are including something
that not supposed
to um or if there's a failure like it
tells you kind of like where in the CCP
stack things went arai so you can fix
your contract and continue on um same
thing for Jason
RPC there's a lot of times where Jason
RPC just returns wrong data and it's
kind of nice to be able to see why and
what data you're getting back from the
server um you can also just do normal
accounting um a huge example usually
when I I give this piece of because
people say sorry I'm talking so fast so
a lot of times people will say like um
you know I I'm sending a bajillion
request to the network I don't know why
they put this on and then they see that
there's a bunch of eth chain IDs being
sent to the network so then they realize
oh I need to put like a static static
Network true in the the Jon RPC provider
and then they literally just cut all
their requests in half by looking at the
debug for like 30 seconds they see
what's going on um and again like any
other analytics you desire like you can
really just examine what's going
on um so this is probably the big chunk
of the talk I want to cover which is
fetch hooking um so ethers has its own
like fetch Library called Fetch request
um and it's designed to be very flexible
because there's a lot of weird things we
can do in ethereum and but designed to
be hooked a lot and so the most common
hook that I recommend for a lot of
people is um this wherever it went maybe
it's on the next slide um it's called
get URL Funk and so you can give it an
alternate method of getting URL contents
um so for example now the defaults are
in browser it uses fetch in node.js it
uses the HTTP and https lib I mean it'll
be moving to the fetch in the near
future um but you can do things like if
you have a data URL There's no
distinction to the library whether
you're fetching a data URL or whether
you're fetching a like https URL or
whatever it is so this is useful for
example a lot of nfts have like a URL
like a property in the contract so if
you pass the result of that back into
this it doesn't matter whether they're
using data URLs or whether they're using
ipfs it'll just kind of get forwarded
and you get back whatever the
information you
wanted um you can also make your own
weird uh if you really want to do an
obscure scheme you want like weird weird
col SL SL does something you can use
this and you get an opportunity to kind
of like intercept that and now you can
Implement weird col SL slash to do
whatever you want it to do um it's
probably useful for like doing Android
apps or like Universal deep linking and
things like that it's just there for
people who want to do weird stuff so for
example like there's alternatives to
ipfs that I don't know about I don't
currently support for three lines of
JavaScript you can now add support for a
racket or SK Skynet Skynet that's the
one yes
umop um also so this is a great use of
it is hijacking for transparency now
this is a very toy example um but
basically this is hijacking the get URL
Funk so that every time a request is
made to the
internet the popup shows up to the user
saying are you sure you want to allow
inferior.
blah to execute and if they
hit no then the whole thing is just
killed um and you could imagine for
example having a checkbox in your thing
saying you know don't warn about this
domain again in which case inferior
keeps working why this is super
important and I think we need more
people to start adopting these type of
of protections for the ccip allows
reading a contract to send you to some
who knows what URL where they can like
attach your address to your uh IP add
like your ethereum address your IP
address and that sort of thing um and so
you can also Imagine like intentionally
blocking it if your app is is not meant
to show nfts and someone's kind of using
ccip reads to like mine this data you
don't even need to present this to the
user you can just like stop it right
then and there and say this contract is
like malicious or malicious adjacent um
and so please go into set like you know
whatever you want to however you want to
like process that sort of
problem um and you can either set it
globally so that you catch everything
from any fetch request across all the
ether's library or anything that uses
the fetch result or you can just attach
it to like one specific provider if that
provider is something you want to like
kind of gatekeep U because maybe you're
you're connecting to a chain you don't
trust or or that sort of thing
yes uh and for security again I have a
lot of like hijacking things because the
hijacking is so useful and I really feel
like there's so many cool things we can
do with it um so I mean I don't have an
actual example of how to connect a tour
up here but you could imagine like every
time you try sending a request to the
web it like gets a chance to B wrapped
up in Tour on and like comes back so if
you wanted to like build a more private
in uh like metamask if your metamask is
using this Library you can just send
everything through tour whether it's a
Json RPC request or whether it's a ccip
or whether it's uh looking up an avatar
if you use ens to look up an avatar that
returns a URL which points to a URL
which points to another thing it gives
you a chance to kind of like intercept
all those steps forward it to the person
you want it for to or or funnel it
through a socks five proxy or all those
good things um s one
second ah um and for example if you have
like be like JWT you could have one like
this bottom example every time a URL
goes out the last step you do before
hits the network is it gets signed you
put your your signature in there um and
the nice thing about this get URL Funk
is it gets called whether
it's like the the fetch result will
automatically handle things like 301
redirects for you or if there's a 429
throttle it'll retry so on every single
request to the network you get this
chance to like inject that like extra
data you want you can like keep the
knots going that sort of thing I think
there's one more example which is
mockery yes so I use a slot in ethers
myself for the tests but you can
basically make a URL Funk that lies to
the provider so in this case you can see
like uh you build a Json RPC provider
and it's always going to return block 42
when you call get block number um
because it kind of gets that to bypass
the entire network thing and just gives
you back that so for example the
fallback provider for those that are
familiar for those that aren't familiar
um it's a very complicated thing that
has a
nests uh requests okay let me stack back
for a it connects to multiple backends
simultaneously randomly issuing a given
request to a subset of those back ends
to look for uh coordination so for
example if you want to call ens and get
the the the address for rick.
eth it'll
call inere and Alchemy if they come back
with the same answer then you get that
answer if they differ it's going to like
knock off maybe anchor and it's going to
it's going to try finding like a
coordination between the back ends that
agrees so in the event that Anor was
hacked or in the event that infer is
down you get like a cohesive result at
the end that's kind of been vetted by by
other by by a quorum of back ends so as
you imagine testing this it's very to
test like well what happens if Alchemy
returns bad data and inferior returns
like correct data but this other thing
does really weird gibberish or there's
there's bad characters in the output
this makes it very easy to test what
happens to rider in these type of
situations you can use it for your own
stuff as well um for those that are
familiar with knock it lets you do a lot
of things that you can do with knock um
yes uh so almost done I'm trying to
leave extra time as well
questions um but so this is just a very
short thing I feel like a lot of people
don't realize the power of ether scan
ether scan has like verified contracts
we all know that it's awesome we all
love that like effort we go through to
verify a contract well it's nice that
once it's verified um you can just
provider.
getet contract give it the
contract address it'll fetch your ABI
and it will automatically connect you to
that contract and you're good to go um
after this you could imagine doing like
uh C.C connect to Aigner if you wanted
to get like right access to it
but yes I think we're getting close if
not the end yes ahha and so that is my
quick talk on some of the hidden things
I feel like are missing in a lot of not
even missing a lot of things I feel like
I want to see more people use so
yes thank you thank you Richard that was
much shorter than I expected but I also
finished at 8:00 a.m.
this morning so
all worry look I don't think I did a
proper job at introducing you oh sorry
sorry no that's fine so tell us what is
it you're doing um so I mean I've work
on a few projects so ether's JS
obviously is like my passion I've been
working on for ages oh nice how many
people work on E GS just me oh wow just
myself yeah um I'm trying to recruit
other help but I'm also a little bit of
a like it's I'm not a manager I don't
know how to delegate and so it's hard to
that sort thing but the other your baby
this is my baby yes exactly so uh and
the other project I'm working on is
Firefly for those that still haven't got
one come find me today um it's like a
hardware wall it's open source and all
that sort of thing so very cool all
right you have a QR code here smash that
question button and we'll get started
okay let me refresh top question wait
I'm not on the right position okay when
if simulate V1 support so I'm not even
familiar with what that with what that
is is if someone wants to like open an
issue and post like a link to either
like an EIP or like is it is it a GU
thing or you know what let's go to the
next question can you elaborate on using
static Network true ah okay excellent
that one I can definitely elaborate on
so um basically when you connect to a
network uh so if you're using for
example metamask uh the network can just
spontaneously change so ethers has to be
ready for the network to spontaneously
change if you get the kns for for
mainnet last thing you want to do is
start preparing a transaction with main
netns on sapoia things are going to fail
in horrible ways you can imagine much
worse things happening like sending
things to the wrong die address for
example um so ether's always like checks
but if you're connected to infira it's
never changing right there's never a
point in time where like
m.m.
will return to you sapoia data
outside of like catastrophic events um
and so you can basically specify in the
options that the network is static and
that you should not even bother trying
to check for it again once you get it
just use what you
have perfect thank you okay I have the
thing up and now we can go to the next
one can the ERS Canan contract retrival
also retrive from other contract
repository like sourcify so it cannot
now but it there's no reason it couldn't
if somebody points me to more data about
sourcify like where the repository is um
my guess is they don't run a back end so
you might need to specify the contract
address and provider to connect to but I
mean that's like five lines of code so I
mean I'm just not familiar with a lot of
these other services there's just so
much in the space to keep up with so um
for sure open an issue on GitHub or come
talk with you afterwards if you're a
sourcify person trying to push your
sourcify thing I fully endorse that and
I want you to come like bug me to get
added as well
um yes that makes sense the next
question is cut in half so we're going
to skip it can we can you tell us how
ERS is better than them so I feel like
this is I kind of expected a question
along these lines um I'm a big fan in
general of like diversity um so it's not
necessarily better I feel it's very
different
um the the big difference I see is VM is
very much designed around
functions um which is great for tree
shaking but I feel makes it things more
difficult for developers ethers is very
like object based um you can't tree
shake a class in a meaningful way so
that's kind of like you can only tree
shake at like kind the file or like the
object level at the end of the day I
don't really worry too much with that
like the thing is I wrote ethers for me
so it's what I use it's kind of using
the paradigms I care about um so I don't
really have a lot to say about that I I
mean I have not used VM other than like
looking at it I've talked to the guys
like it's yeah it is yeah I've got
nothing more to really to say about that
unless there something specific feel
free to be like nice so one of the
challenge for developers is to get
historical uh historical balances of e
and L2 chains what do you think could be
the best way in the future to get these
without an archival node in place I mean
I can totally imagine a place where
there's something like the graph but for
like historical data we really need some
sort of service probably to support that
um and like the economic incentives
around providing that data always mean
that you're basically going to need um
um like some sort of paid service like
an neir or whatever unless I mean if May
has brilliant ideas go for it um if
there's a service that ethers can use
for that please like tell me again I
feel like the moral the stories tell me
about it because I want to add these
things if they exist um but it's
definitely not something it's not a
service that I could write or host like
this is just pedabytes of data that
would be well it'd be gigabytes of data
with pedabytes of indexing into that
data so um it doesn't seem like the kind
of stuff you can shipping e but it's a
service people should be right and if
it's a service that exists like tenderly
I will totally provide an ethers like
like way into it nice thank you can you
elaborate on using static network is
this more than the last one yeah this
one is the one that was
voted okay I if you want to pick another
one go ahead which one do you like more
oh I mean I just I thought I answered
that one oh oh my okay sorry I didn't
mark it as sorry okay is there a way to
implement custom RP PC Cod some chains
have non-standard one absolutely so if
if you have a Json RPC provider you just
do do send you give the eth method and
then you give it whatever e method for
that network uh takes oh for sure like
this is the way you should be processing
a lot of um oh there's a thing I should
add to a slide it's too late I'll
remember for next time um but yes uh for
sure you can add like custom like it's
required like a lot of chains have their
own like exotic behaviors that are
really useful to be able to like access
okay we'll get you where you were a bit
early so I'm going to take another one I
was say 41 seconds left on there
everybody it's okay um so you showed
something about making requests over
tour why is it useful to make requests
over tour when you can't really run an
ethereum node over tour I mean these
serve different purposes right like if
your if your avatar is being served on
the internet off of some web server you
might want to protect your IP address
from being attached to that necessary
Avatar um I mean I understand the to the
question it would be awesome if we could
tfy like ethereum but there's still lots
of like privacy value in talking over
tour that's also like a toy example you
could imagine other weird transports
where you're you're basically trying to
send data over uh like a BL network over
top maybe you're inside a really busy um
venue like this and you could imagine
having a BL firecast style um
Communications protocol so you could
Implement that on top of that if you
wished um but I mean I'm still big fan
of tour I think
tour tour needs I don't know whether
funding is great word they need
something but tour is awesome um and so
there's lot of privacy focused things
where tour could could be useful still
Richard thank you for your talk thank
you for your work uh frog bump thank you
thank you oh frog aha I love it cool
thanks and to everyone we're going to
start the next session in five minutes
stick around it's going to be awesome
h
hello can you hear me nice okay get
ready for our next talk our next speaker
is anony he leads applier re applied
research at the noming foundation he's
going to talk to us about slang's query
API um and I guess you'll explain what
slang is better than I will don't forget
during the session you'll have a QR code
here and ask questions up votes the one
you want to see answered and then we'll
cover them um at the end of the talk all
right please welcome Anthony
okay good day my name is Tony I work at
the nomic foundation in applied
research uh I was previously a co-lead
on the slang project and it's in this
capacity that I'm going to speak to you
today uh I have a fantastic job working
with excellent people at nomic nomic is
a nonprofit and our number one core
value is kindness and we live this every
day and we are hiring there's meant to
be a QR code at the end of my slides but
I'm afraid it didn't make it uh and I
want to give heartfelt thanks to the
co-founders of nomic p and Fran for
creating and maintaining such an amazing
place to
work so today we're going to explore the
slang query API which is a new feature
which makes working with solidity code
surprisingly
straightforward now this is not a
tutorial so some of the details have
been emitted you can't copy and paste
any of the code that I'm going to be
providing it's just so that you can well
I'm hoping to inspire you so that you uh
go and find out some more details okay
so 20 minutes is a bit of a Sprint so
I'm going to speed up let's go
okay so what is slang so slang's our
solidity compiler Library it's uh
basically a developer tool that enables
you to write better tools it paes and
analyzes solidity code from version
city code that is
live our focus is on correctness and
convenience
uh we're about to release version one
which covers the typical front end
features of a compiler and our main
objective as I said is to enable you to
develop better
tools uh slang has a radical open uh
declarative met
architecture slang's a error correcting
compiler so it always produces output
even if you've got source code
errors uh a key feature of slang which
is what we're here to talk about is its
query API for code
analysis so compiler front ends fall
into two main categories there are those
that produce what's called concrete
syntax trees and then produce an
abstract syntax tree from that and there
are those that produce abstract syntax
trees
directly uh so what's the difference
between concrete syntax and Abstract
syntax well concrete syntax as you can
see on this slide is a complete
representation of the source code it
includes every character every bit of
white space every comment it's like
having as I say like having the full
book like a
PDF uh whereas an abstract syntax
tree is a simplified tree representation
so it doesn't include white space and
equal signs and and uh punctuation it's
just got the essential details it's like
if you were reading the the plot of a
book but you didn't actually have the
text
so here's an example of a contra of a
concrete syntax tree so we've got a
simple variable declaration here and
every single element of the original
source is represented nothing is removed
or
simplified now this is different from an
as which will eliminate some of these
details so if we look what we've got
here it's a simple variable declaration
now it consists of a type name which is
uint then some Whit space and identifier
some Whit space punctuation you equal
sign some whites space a number literal
one and then the
semicolon now what's crucial to
understand is that we're preserving
every single character in fact even if
there's an error in the source code
you'll find it in the concrete syntax
tree so why is this important well when
we're developing uh building developer
tools uh or transforming code we often
need the complete information so we can
round trip if if we were just concerned
with the meaning of the code then we'd
use an abstract syntax tree but for many
tools like formatters linters or
refactoring tools we often want the full
syntactic details you don't want to lose
comments when you're
refactoring and sometimes you want to
know if you've left two blank lines uh
and you want to preserve
that this level of detail is great but
it's also challenging it's quite
difficult to process this on the one
hand we have complete information but
working with detailed treat can be
complex and that's the challenge that
the query API solves so from now on I'll
admit trivia nodes and Whit space from
the examples they're still there but you
I don't need to show them so let's look
at a slightly more complex example this
definition shows how different elements
Nest within each
other uh and once again notice how
everything is preserved here we've got a
function definition we've got the the
keyword function the identifier we've
got a parameter list which in this case
is empty but we still preserve it and
then nested in that is a block and a
return statement and so
on now this level of detail allows us to
maintain complete Source Fidelity as I
said if we get a round trip we can track
precise C code locations so if you want
to do error
reporting uh it handles formatting
preservation and when you're Building
Development tools this detailed
structure is
essential for certain class of
development
tools so to emphasize this point and I
know I'm being repetitive here I really
want to make this point though why do we
need a concrete syntax tree well we
really want to in a lot of tools for
example in prettia uh which is now using
slang by the way using this technology
uh pretty a solidity we want to make
sure that we can preserve every single
character especially comments for
example you might have a tool that wants
to deal with comments wants to encode
validation information in a special
comment format not like the
documentation comment but your own
special comment format so you want to
preserve those
comments an on the other hand is
focusing on the essential structure
which is good for semantic processing
doesn't contain the formatting
information simplifies expressions
and it adits all comments in wh
space so now that we understand what a
CST is for let's look at how you might
traditionally process a CST so this is
the kind of code that you often see a
lot of you know what it's like to
Traverse a tree especially a very deep
and complex tree which is what you
typically get out of a
compiler uh and it's not pretty what
we're trying to do is actually quite
simple we just want to find all the
variable declarations in some solidity
code but look at what we have to
do so first of all we're writing a
recursive function we need recursion
because we don't know how deep in the
tree it is could be at the contract
inside a function inside a block
anywhere and then when we find each node
we've got to manually check its kind
we've got to search through the uh
children we've got to handle all the
edge cases and we've got to manage the
recursion stack especially if you're
threading State and this is a simple
example in real life code you'd have to
handle error cases deal with unexpected
node types which is what you can get if
you've got a source code error for
example manage your state during
traversal and if you've written a
visitor patn you know that it's a pain
in the ask to manage your
state you've got to handle parent
references and you've got to manage the
position in the source
code now the problems with this approach
are
numerous first it's incredibly verbose
the amount of code you need to write to
do even simple analysis is substantial
and the more code you write the more you
have to maintain and the more places
there are for bugs to
hide uh second it's Error prone uh not
only because of the volume of the code
but also it's quite tricky to write
these when you're dealing with
complicated trees for example in
solidity variable declarations can
appear in four loop initializers I don't
know if this code would handle
that it's a question for the reader it's
hard to maintain when the language
evolves and as you know solidity evolves
significantly uh in all sorts of
interesting ways like in one of the 0.5s
where the exponentiation operator Chang
associativity uh so when the language
evolves you need to update your
traversal code and that's because the
traversal code is mixed with the
analysis code so what you want to do for
analysis is mixed in with the mechanics
of
traversal to make changes you're often
going to break things finally and more
importantly this forces you to think
about what or how you want to do things
rather than what you want to do and the
intent of this code finding variable
declarations is buried in here you could
look at a big tra bit of traversal code
and you wouldn't know what it was meant
to be doing we need something
better so we'll have a look at some
specific challenges with manual
traversal so recursion management you've
got to handle deep nesting efficiently
avoiding stack Overflow you've got to
make sure you don't have any infinite
Loops you've got to maintain your
context State Management you got to know
when to stop recursing once again if you
use a visitor patent where you've got an
external visitor driving external code
driving your visitor you often want to
stop or you don't want to go into the
children of this node how do you do that
that means you end up with a more
complicated API State tracking is quite
complex you need to keep track of the
parent node when you're um uh walking a
tree you need to maintain scope
information in the case of a compiler
build up your composite results handle
cross node relationships I.E you want to
link this node which you visited you
know 30 minutes ago with this other node
which you're visiting
now now error handling just multiplies
complexity and edge cases keep appearing
for example parenthesized Expressions
nested structures optional elements and
language specific quirks of which there
are plenty in
solidity and finally you've got a big
maintenance budget now I know I'm
repeating this point but this is
significant as you'll see when we get
the queries which I think is the next
slide so this is where queries come in
so let's look at how we solve some of
those same problems
using queries so this is our first
example we want to find all the unit
variable uh all the uint variable
declarations it's as simple as saying
inv variable declarations where the type
name is uint and it's got an identifier
B that and return it no
traversal no edge cases hardly any
maintenance or efficiency problems so
the second example shows something a bit
more powerful in this case we want to
find immediately nested function
declarations I a function inside another
function so here we're saying in every
contract definition there are some
contract members in the contract members
there's a contract member for every
function definition in there find the
block and look for the a statement in
there that is a itself a function
definition call bind that to a variable
called nested and return
it so why is this so powerful well first
of all it's the Clara we're saying what
we want not how we want to do it makes
that code easier to understand and
maintain and when you look at this two
months later it's obvious what it's
doing whereas I'd suggest that you'd
have a couple of pages of code
traversing your tree if you were using
manual traversal and it wouldn't be
obvious what it was actually meant to
do so it's structure
aware so the query understands solidity
syntax structure it knows about scope
and it knows about nesting and it also
knows where type name for example in the
in the first case here appears in the
tree these patterns are composable so we
can build complex pattern matching from
simple pattern matching so if we wanted
to find uint variables Within These
nested function definitions it would be
as simple as putting that appending that
first query below the second query but
most
importantly this is focusing once again
on what we're trying to achieve we can
think about code patterns and structure
design without getting Bob bogged down
in the implementation
details so let's have a look at some
more advanced query
patterns this one for well this one
isn't that advanced but for example in
an unchecked block you want to find all
function calls as easy of that and it's
obvious what it does you could write
this on one
line the example is a bit more
complicated but here we're looking for
variable
declarations uh State variable
declarations that have a type that is
either map a mapping or an
array and think about what this would
take if you're doing manual traversal
you'd need scope tracking type checking
logic complex conditional logic and
you'd need to hand carefully handle the
nested structure here
so what are the use cases for this or
some use cases cuz I'm hoping that
people come up with far more use cases
than we know we want sort of emergent
benefits from this well if you wanted to
have custom coding standards you want to
enforce custom coding standards you've
got project specific restrictions that
you want to check or you want to do
version compatibility check so you want
to make sure that you don't use certain
features of
solidity uh style checking well if
you've got specific naming patterns you
want to enforce uh specific structural
conventions and you can have context
wear rules now you might be thinking
well can't I use a linter to do this
well yes but this is meant to write the
linter this is designed for writing
linters so that's why these are the use
cases this is not an end user tool this
is a tool for developers to write
tools uh so you can do patent detection
anti- patents for example uh
optimization OPP unities which may not
be immediately obvious if you've got a
big library of things uh detecting
complex structural patterns that you
might want to simplify or or Mark so
once again this is a kind of an es
linter uh
equivalent code transformation automated
refactoring refactoring is
Transformations that um preserve the
semantics uh code modernization it's
very easy to write um patterns that then
transform into uh more modern code
automated ifications I.E things that
aren't refactorings that actually change
the code and formatting and as I said uh
pretty solidity is already using uh
slang uh one important point I want to
make here is that uh we support wasm and
we support in spe specifically the
component spec and WID so for those who
know what that means this means that uh
all of this technology works in the
browser it's also available as a rust
API or as typescript which is our first
Target because most people uh are using
typescript so some more applications
code trans I've already done that
documentation generation uh it's easy to
generate automatic documents by
extracting function signatures doing
structure analysis um checking for
particular usage patterns and
documenting them and processing comments
as I mentioned before you might have
validation uh information in a certain
specialized Contex uh comment format now
you can also use this technology in
combination with AI tooling for example
to produce uh diagrams from your code
you can use this with uh by encoding uh
the slang API as a
rag so what are the key benefits well
structure aware queries your queries
naturally align with a structure of the
code that you trying to match you don't
have to think about trees and nodes and
and uh
traversal uh complete syntax
preservation you never lose
information perform Transformations
without losing the formatting and you
can round trip from a CST uh back to
Source efficient patent matching so we
can spend all the effort required to
make this efficient if you know anything
about the state-ofthe-art in terms of
tree pattern matching and in fact we're
not a a search engine we are a unifier
so we use a prolog SL datalog based uh
mechanism which returns you all the
potential matching results not just the
first one you can avoid unnecessary
traversals we can case results we can
index the syntax tree make it very
efficient it would take a lot of effort
to uh get the same uh result if you
doing it
yourself composable syntax rules you can
combine simple rules to make bigger ones
you can have a big Library of these uh
pattern and you can reuse them uh over
your code share queries between your
projects you've got maintainable
analysis code so the queries express
your intent not how you not what you
want to do uh how you want to do it but
what you want to do your code is shorter
it's easier to understand any changes to
the language we take care of that slang
takes care of that so you don't have to
less code means fewer bugs and these
benefits compound it's not one plus plus
greater than the sum of the
parts so what impact does this have on
your development well before using this
query API you spend significant time
writing and debugging the traversal code
you'd struggle with maintaining the
analysis logic and you'd face challenges
when adding new
features after it you end up with clear
Focus code it's easy to maintain you've
got a robust implementation and it's
highly
extensible and that is it any
questions fantastic thank you Anthony
all right let's get with the let's get
with the questions so folks remember you
can scan that QR code add questions to
that list smash that up vote button that
the most interesting question gets asked
let's go with the first one what are
advantages to using slang compared to
Sam GP uh well I must admit I'm not
familiar with uh Sam GP but I know the
general uh concept the specific thing
here that this is a programmatic tool
that you use to build other tools now of
course you can combine things like
semrep uh I imagine uh but I don't know
if that is something that you would
include in a tool for analyzing lots of
different versions of solidity that
makes sense thank you how does slang
differ from a fine-tuned llm could
slangs modularity allow to use llms in
the future oh this is I'm in applied
research and uh this is something that
is very actively under research uh I'm
not making any commitment uh but if
you've used fine-tuned llms uh and I've
used them a lot for example a lot of the
code that I write is actually written by
Claude uh a lot of this presentation was
written by Claude um amazing tool but
you always need a human in the loop so
yes you can do this uh using llms but
the thing with llms is that they are a
human augmentation tool whereas the
approach that we're talking about here
is exact and precise if you've used llms
to do this you know that you you spend a
lot of time on prompt engineering and
then you cross your fingers and
something comes back and it doesn't
quite work and you prompt it again and
so on and so forth so yes this is
certainly something that could be
included in the future there's a chance
but maybe not now I mean not immediately
certainly not now okay are the
limitations of an of a tree visitor
based approach not solved by using an
API with CFG and intermediate
representation like Slither
provides
uh well if if by CFG well you're either
meaning two things you're either meaning
the control flow graph uh which is
typically something you'd find in an
abstract syntax tree uh or if you mean
control flow as exposed by rust for
example uh and this is something where
you reify your control flow so you
return a token in your visitor which
says do you want to continue do you want
to go down uh the trees um now this Tree
Visitor uh these
um solution
these Slither May well um solve the same
kind of problem we have a different set
of constraints for example our query
language uh is intended to be extended
with semantic predicates and with the
ability to do arbitrary recursion by
skipping over arbitrary sub trees uh so
there's a lot that we want to do there
so I wouldn't say that that um in
slyther you can or cannot do that I'm
not familiar enough with slyther perfect
thank you is there a question you'd like
Mo in
there uh well with this work with
different evm versions yes it will
because we're dealing with Source where
well before evm slang is a compiler and
it'll produce bite code so that's a
question about the compiler not about
querying have we published the grammar
for slang yes we have uh slang is
actually a uh declarative meta project
so you can use it for any programming
language not just solidity and we have
um published that everything we do is
open source uh
nomic Foundation
on GitHub all of our development is in
the open you can reuse all of this
awesome uh how important well uh so how
important is it to maintain code with
different solidity versions why why not
just use one version because if you want
to be able to provide tools that analyze
a large number of contracts which may be
an earlier version of solidity than the
latest one for example 0411
there's a a contract on mainnet that is
you want to um provide analysis tools
for it that's why we want to support all
of these versions now we don't go back
to 001 or whatever the first version was
so we're pragmatic about it but these
are the versions that are live and our
goal is to support all the versions that
are live how do you determine the cut of
version uh what's analysis an analysis
of the of m all the contracts that are
live okay is it the number of contract
is it the value stored in those is it
the amount of transactions no the
earliest the the um I didn't do this
analysis so I must admit I don't know
what process we Ed to determine that but
it is the case that the earliest
contract in use apparently is 0411
fantastic thank you um what's the best
practice for using slang to analyze a
large number of program where should the
data be stored and in what format
imagine this is something you run
locally correct yes it is perfect thank
you all right what upd in solidity was
the artist to adapt for you mentioned
quirks and weird updates and solidity
which one was the hardest
or none of them was particularly hard uh
the volume of quirks is what is a
challenge I mean we've we've got
hundreds of edge cases we had to analyze
Soul C because that's the only
definition of the language uh and go
through the code and then test it and
then go to sanctuary fre and look at
massive uh numbers of
contracts uh run uh our compiler over
them or run our paer over them what
breaks what doesn't we've got extensive
uh test cases so that was the challenge
it's the number not the not any
particular difficulty fantastic thank
you do you dream in bite code uh no no I
don't dream I dream compilers actually
all right Anthony thank you a lot for
your time and all the best to you thank
you people our next session will start
in a few minutes I am off for today
thank you for those who spent a bit of
time with me this morning um and I'll
see you soon cheers
[Laughter]
GM GM I hope everybody's enjoying their
time my name is Robert a developer
Advocate at the starnet foundation and
I'm going to be your MC for the rest of
the day now uh I would like to introduce
the new the next speaker anesto Garcia
who is a smart contract engineer at open
Zeppelin contracts and he will be
discussing about how to bring your own
cryptographic identity to Smart accounts
please give him a round of
applause how's it going okay is it
working perfect uh how's it going you're
doing great perfect um okay so what
we're going to do today is talk a little
bit about smart accounts in the context
of open seing contracts this has been a
really requested feature that we had
been working on for quite a while and we
have a couple of things to discuss on
regarding this so let's get into it all
right so this is the agenda first we're
going to start with some a little bit of
background uh where are we starting from
this uh from this work also how to do
account abstraction like on a general
perspective just as a quick recap of
what account obstruction means then
we're going to custom signature
algorithms which is uh one of the main
topics and is the thing that is like the
most important about this this talk um
we're going to go over some technical
goals we have for an account
implementation in open spelling
contracts then we'll review a couple of
security considerations we we have to
understand to make better accounts and
finally I will guide you through a quick
way of how to build an account using
open sing contracts um I'll let you know
but like uh all of this code is already
on Alpha so we will be releasing over
the following weeks okay let's start
with uh some some background the first
thing you need to know is that we
recently received a grant from theum
Foundation to work on on account
abstraction right so this means that we
are going to make a a library that is
consumable for you developers so you can
use use open spelling contracts the the
same way you have been doing it before
and in this way you will have available
like a couple of variants for making
accounts uh extending accounts and also
having some Primitives that you can use
on your own accounts if you want right
um given this context we started start
doing some research and what we found
out is that there is number one already
a wide range of implementations right
like we already know a couple of
implementations out there some quite
popular like Alchemy safe bomy and some
others right so basically like all of
these development that has already been
made like we don't want to compete with
that but we we would like to provide a
way to also like create new accounts
innovate on on top of these ones and
also providing Primitives to also enable
developers to build on top of those um
second thing is that there are a couple
of emerging Securities challenges that
have come up because of the explosion of
creation of accounts so we want to
address those as well and having a clear
framework for you to move forward when
you're building an account the next
thing is that there is a lack of an
straightforward approach when you are
trying to build your own account you
basically have to research a lot of
different implementations if each one
has different modules or approaches to
bring your own functionality so the idea
is that you should be able to um have
more expressivity on the way to design
on an account and also you you should
have like a a straightforward path right
like the same way you use import erc20
and literally you use deploy it there
should be something similar to that
right so okay um our observations of
this sort of research uh is that we
would like to uh divide or layer the
account implementation into like
different layers um the first one should
be like a base layer for ERC 4337 the
thing with ERC 4337 is that it only
defines like a very simple and what do
you call it like yeah simple interface
right and a set of rules but on the
implementation things can get very
different so we would like to have like
a base layer for ERC 4237 account that
is super solid battle tested as
everything in open selling contracts is
then from there we go to the validation
layer which means um this is like the
the place where you put the logic to
validate a transaction right if you are
using a regular EA to sign a transaction
and putting into an account this is
where the logic for validating the
signature should go uh we think this
thin layer should be also kind of
customizable and you guys should be able
to bring your own uh functionality at
this layer right although there is
another layer which is the modularity
layer right here in which there are a
couple of competing eips or standards uh
we think there is a lot of innovation
coming on here and also happening right
now here um so yeah we want to provide
you like a way of using either a custom
validation mechanism on the previous
layer and also like a modularity
approach if you want to finally the idea
is that we have or we end up having a
similar to a wizard like experience who
has used wizard like open sping wizard
from here all right so for those who
don't have context open simping wizard
is like our tool to build smart
contracts in an opinionated way so you
can go to wizard.
opening.com uh and you
will see what I'm talking about so
basically we would like you to come to
uh wizard create your own account you
select a couple of options and you're
ready to go all right um talking about
Mass adoption I think we have been very
hyped about the fact that account
obstruction is bringing a lot of
opportunities to bring new people but
there are a couple of challenges we need
to address first so we'll we'll
eventually get there uh but there are a
couple things to do um in order to
understand what we need to do there are
a couple of related erc's and best
practices you need to understand and
follow the first one of course is ERC
and it has a couple of rules that are
quite interesting you know um all all
that is related to pay masters
aggregators all of that is quite complex
we'll event get there too but for now we
want to focus on the account side of
consideration is ERC
a storage validation well not storage uh
there are a couple of validation rules
for for 337 but the main or the most
important ones in my opinion are the
storage validation rules uh why is this
important because there are some um what
do you call it like setups in which you
can create an account and basically you
are violating some storage rules uh some
storage validation rules why is this
important because otherwise you wouldn't
be able to use the decentralized uh
peer-to-peer Network to process user
operations you can still use um a
private bundler that would be fine but
ideally we would like to have an
implementation that works out of the box
with um the decentralized network and
finally um ERC 7739 uh this is uh a
thing we stumbled upon uh when we were
implementing the account because
basically uh there there are a couple of
issues with replayability if two
accounts own are owned by the same key
I'll I'll get into that but this is a
cool RC to get to know more about like
how to um bind a signature to an
specific account implementation which is
pretty important to avoid replab ility
all right so let's get into how to do
account obstruction just for a quick
reminder uh remember that an smart
account is is way more than just the
validation mechanism right you can add
modules you can have like custom logic
all of that but ideally you will focus
only on the validation logic if you are
building your own account from scratch
uh from this we have seen a couple of in
amazing Innovations like CK email which
is using your email to send a
transaction from a smart account this is
pretty clever um also CK identity we
have seen a couple of options like using
passports and these kind of uh this kind
of things so this is why we think the
validation logic layer is like an
important part that should be extensible
for developers because a lot of
innovation is happening right here but
it's being brought up as modules which
is also a valid um a valid approach all
right so ideally this is what you should
do uh if you're you using open suppling
contracts this is not public yet we're
still working on that but this is like
what we are uh trying to achieve as you
can see it's only importing an account
ecd a in this case this is controlled by
an EA and there are a couple of things
to note here um let's get into that so
number one is this upgradeable um not
really the thing is that in order to
create an account you probably will need
a factory right and if you need a
factory you basically need some way of
initializing the account so upgradeable
contracts are perfect for initializing
right they are basically designed for
that and it doesn't mean that the
account is upgradeable it just means
that it's a clone that you deploy de
loyed and then you initialized uh second
thing is it is a draft uh well yes some
of these erc's are still a draft so we
have a couple of challenges there
because we guarantee backwards
compatibility for all of you so you
don't have to manage or deal with that
so based on this we wanted to uh or we
want to provide you with an
implementation but make it clear that it
is still a draft couple of things of
things may change and of course we will
keep uh working on this and we
appreciate the feedback um next thing is
is it clonable yes because as I
mentioned you need a factory and because
of of this you basically need some way
of cloning an account so that it is
pretty cheap to just create and generate
new instances of accounts right okay so
let's get into custom Uh custom
identities or custom signature
algorithms which is the main the main
thing we want to discuss here um so to
get into this um let's explore a little
bit on digital signatures right right
now the majority of implementations of
account already use some sort of
validation mechanism or they accept
something like ERC 1271 which is for
smart contract validating signature
validation so in this case then the most
naive approach to bring your own
cryptographic identity to an smart
account is just use an interface like
and then you're ready to go but in
reality uh digital signatures are more
more than that and we have seen that for
example a couple of traditional private
uh sorry public infrastructures like in
governments corporations Banks and these
kind of environments these are already
widely used it's just that is not used
in the context of an smart account so
this is why it is important to bring
your own cryptographic primitive because
it it be it makes it easier for players
in the industry let's say traditional
Finance to just come here use the same
key that you were probably using for
authorizing transactions within their
organization and they should be ready to
go um so they are widely adopted as well
and battle tested I'm adding a quote
here because well uh it's not the same
environment they have been around for
years but you know like in close
environments it's different to these um
to the crypto industry with where
everything is open source is pre barel
tested so yeah I think this is a cool um
it's a cool experiment but definitely we
we need to see how it behaves over time
all right um particularly with this
thing the wide adoption of some digital
signature schemes regularly means that
is cool for regulation right there's
some sort of Regulation around like
traditional finance using access control
mechanism so we can also leverage that
for real use
cases um right now in open seing
contracts for signatures we already have
three different signature algorithms
available the first one is the good old
uh ecdsa right the one that is
controlled by an EA this is already
there and has been there for a couple of
years we recently implemented a p256
implementation this is INS solidity and
the reason why we did it is because we
identifi that some change particularly
some l2s may not have already enabled
rip 7212 which is the one that uh
validates these kind of signatures so
because of that we came up with an
implementation that we think is uh
efficient enough and is welld designed
for you to use it but also if it detects
that the pre-compile is available it
will fall back to this pre-compile so
you can use use it out of the box
removing all of the considerations that
you should you should have as a
developer you use import it and use it
as everything in open sping contracts uh
also we are adding an RSA Library this
is because we have found a couple of uh
government public infrastructures that
depend on this particular algorithm so
it is there for consumption also is
pretty popular in some use cases like
for example DNS SEC uh ens uh probably
you have your ens but ens depends on
this algorithm for some DNS providers so
it's also a good primitive to have we
already have it in open spelling
contracts all right um for let let's um
like recap a little bit on what that
digital signature means just for you to
understand a couple of issues that are
coming so basically a cryptographic
signature is just a message that you
hash you generate like some piece of
data by 32 and then you use a private
key with a signature algorithm to
produce a signature right eventually
then you will use a public key and your
signature with the same digest to uh
pass it through a verification algorithm
and it will return true or false
depending on whether it was successful
or not so the thing with this is that we
can find out that there are two main
algorithms in this number one there is a
hashing algorithm and number two there
is a signature algorithm right so this
is important because um you as
developers you probably will be
constrained by whatever is an offchain
is is of chains signer right usually
people already have like a device uh a u
key some sort of uh software that
doesn't depend on you and is probably
using one of these custom hashing
algorithms we're Prett used to use um
kak 256 but in reality some signers like
op chain signers for example the one you
have on your iPhone The secur Enclave we
try to use chat 256 right so this this
is not really a problem like we can just
rehash it but we think this is too
opinionated and this is the sort of
thing that we would like to have um more
more contribution and opinions from you
um this is basically the idea uh because
some of the op chain um op chain signers
are constrained to specific algorithms
like we need to work around this right
and this will happen um depending on how
you compose your accounts uh it's
probably becoming a mess if we don't
take care of like standardizing this or
something
similar so another thing to take into
consideration is replab ility across
same key accounts this is let's say you
have account a account B and both are
controlled by the same key well then
there is the possibility in which if you
sign a transaction to send let's say one
ether to balik on one account that same
signature can be used on your other
account to transfer one it again to uh
vitalic right this is not ideal this is
an issue that was originally discovered
by curious Apple um there is a good
write up on the internet that you can
also search just look for replab on
Smart accounts you will find it so the
idea uh to solve this is that we need
some way of binding the signature to the
current domain in which it it is used
right so this is perfect to do um or
sorry EIP 712 is is perfect for doing
this uh are you familiar with EIP 712
okay I see a couple of hands for those
who don't have any context uh EIP 712 is
a way of constructing signatures with
types basically you can uh sign a
message that has an U into 256 type and
a couple of others it's like a struct
you can sign and what is special about
this struct is is that it also includes
the address of the current contract and
also the chain ID which makes it
um you cannot reply a signature because
it is B to the current implementation
that you're signing the message for
right this is actually what ERC 7739 is
proposing is like a way of rehashing a
hash so that it adds some context for
you to understand better what is going
on instead of just signing an opaque
signature an opaque hash sorry so all
right next thing is um another thing to
consider is that what if we want
accounts to be owned by accounts so in
theory this is possible like we have
seen multi signatory schemes in which
you have a single account owned by multi
multiple accounts but in this case if an
smart account wants to own another smart
account it comes with a lot of gchas uh
the first thing is like okay if B is
owner of a what should B sign like
should they just sign a message that is
for the domain of b or should should it
uh sign a message for the domain of a
what if there is another domain like
probably you're signing from B to
authorize on a an interaction with an
application C right so it it's starting
to become a mess in this way and it's
becoming a pack for whoever is signing
this on their user s okay uh second
issue like how how should we validate
from a that the signature is correct
from B right because this is this has to
do with um storage validation rules in
the validation phase which is literally
where use check signatures if you go to
another contract and check storage let's
say to uh record the public key then you
are violating some of these rules right
so these are some of the challenges that
come in when you want to like add
composability to accounts we we have we
have found this as an issue and we of
course want to work like to solve this
um just a quick quote uh this is a uh
this is a a popular joke in you know
computer science there are three not
really four things in computer science
and one of these is signatures in
account abstraction wallets right um but
yeah this is why we want your
collaboration um and this is how we're
doing it basically we have three main
goals with our implementation we want it
to be secure uh we want it to be layered
and we also want it to make it
extensible right we don't want you guys
to start you open open supping contracts
and then become vendor logged in to
whatever we have basically the idea is
that you can uh take any of the
components a user for your own
implementation so that we can foster a
barer um Innovation space and also a
more
expressive what do you call way of
creating
accounts um for these there are a couple
of security considerations like for
example we want some audited building
blocks for you to be safe whenever you
you're building your account uh also we
want to have a strong cryptography
Primitives this had been audited by the
research team are open Seine so shout
out to them they have been doing an
amazing job number three replab ility
issues as I mentioned number four we
would like to maintain user operation
reability we don't want the user to end
up signing something they don't
understand because this is super
dangerous and number five we want it to
be community-driven which means we we
really want your feedback on this and
try to C the development with the
community so this is how we build an
account um this is ideally the the sort
of steps you you should follow so number
one you pick a base account starting
from account base which has a virtual
function for validation right then you
add your 7739 signer and from this you
get immediate reability protection then
you just have to fill uh both virtual
functions that are there one of these is
the validate signature using ecdsa
recover and you don't have to worry this
already has the replayability protection
in in place so whatever you receive as a
hash is already bounded to the account
number four use deploy and that that's
it thank you so
much is there any
question thank you thank you so um now
we're going to the Q&amp;A section for those
who want to ask any questions we have
this uh QR code on the left scan it add
your question and up vote questions that
are very interesting thank you ano for
the uh talk now we're going to ask I
think we're going to start with the
popular question so the first one is why
not incorporate uh all or as many
popular algorithms so as to apply to as
many uh external opinions and
implementations right this is a great
question um the honest answer is that it
is really difficult to implement
cryptographic schemes especially in
solidity it comes with a couple of
challenges so it's it's a it's a tiring
process right we're open to receive
contributions on that it's just that it
is exhaustive it takes time and we also
have to audit those um also I forgot but
at the end of the presentation there was
a QR code for the community repository
everything that you want to add like on
the community side is welcome on that
repository we have less um we we have
more relaxed policies on that repository
so everything is welcome from your side
fantastic thank you very much now for
the next question is uh would you be
Implement uh you you would you be able
to implement your own custom functions
such as TFA or social recovery yeah the
short answer is yes the the long answer
is that we would like to understand
exactly what it means to have tofa right
because what if we want to be compatible
with like uh regular Web Two workflows
or do we want something completely new
that is EIP 712 base right these kind of
things are like worth discussing but we
eventually will get there fantastic um
how can we solve fragmentation problem
in ERC 4337
good question um I would say having like
a sort of what do you call like a a
straightforward framework like a set of
a steps that are pretty clear enough to
everyone we'll probably sort of solve it
but in reality we already have
implementation so I guess we we have to
work out and sorry work around them
which is like uh the usual what do you
call like way is the way things work
right we just like continue building on
top what is going on gotcha gotcha yeah
um okay so for the next question there
are few conflicting eips for plugins and
modules will open Zepplin uh take an
opinion on these or will leave that up
to the implementations also really good
question uh we would like to have an
opinion because we don't uh usually we
try not to provide you with two versions
of the same thing right but like we
definitely need to experiment with this
module uh modular standards to
understand for which cases are better so
probably our opinion will end up looking
something like okay for these use cases
you should use this ERC and for this
other you should use this other but
again uh we are implementing this on the
community repo of opening contract so
basically all of the ercs that are for
mod for for modularity are very welcome
to to be implemented in from
contributions from you okay and we have
one more question um if you want to ask
more feel free to do it is it possible
to create smart accounts that work with
iPhone security Enclave so I guess with
the uh different um signature yes uh
implemented is the one that is used by
the securing clave so yeah you just need
to create your account uh make sure uh
that you can select well make sure that
you're using the same hashing algorithm
as is as in The Enclave this is just
pretty easy just grab the the message or
the hash in another hash and that's it
but yeah the answer is is yes nice and I
think I have one question from me um
what's your favorite you think about
account abstraction what's what like
what you trying to solve overall for the
uh General users yeah I think I'm
excited about users bringing like
usually users already have some way of
authentication that they are familiar
with and I'm I think I'm pretty excited
of seeing all of these people bringing
these into their own account so we can
onboard people more easy fantastic
Ernesto thank you again for the
wonderful presentation on account um
smart accounts and account abstraction
please give him a round of Applause
thank you very
much okay and uh now uh I guess some of
you are a little bit hungry so we're
going to take a lunch break uh you can
grab some food uh the break is going to
be roughly about 70 minutes so we're
going to be back at 2:40 p.m.
uh with
the next session the evolution of ZK see
you in U 7 minutes
all e
spe
all
right
hello hello hello hello everyone um hope
you had a fantastic Devcon hope you had
a nice lunch break as well um we're very
happy to have this uh kind of like last
minute submission uh also to have this
announcement coming from uh Josh Davis
and nxo from um protocol support at the
ethereum foundation and so with no
further Ado I will welcome Josh and nxo
to jump on stage um so yeah warm warm
Applause please for n and
Josh hello hello
um yes it was a surprise announcement um
and you guys are the first to hear and
we just submitted it so we are super
excited to announce that we're doing a
the first ever open internship at the EF
open to anyone it's targeting um
University students PhD students and
that's University student undergraduate
students in like their third or fourth
year and really anyone who is looking to
change their career or or just has
exceptional talent and wants to work in
ethereum uh the teams that you will be
able to work with at the EF internship
our protocol security the rig group
portal testing eels gu account
abstraction and there's also a
generalist role if there's something um
that is very if you're very familiar
with ethereum and there's something very
general and very uh something very
specific that you generally want to work
with at ethereum um super excited these
are incredible teams to work with all
applicants will be paired with somebody
at one of these teams and they'll work
closely for three months next summer and
it'll depend on whatever the schedule of
the applicant is uh and it'll start in
June is
you've been following the ethereum layer
one development you know that we have a
few different sort of programs that
Target uh core developers uh this
program is not the protocol Fellowship
that has been going on for the past uh
few years this program is a little more
targeted and and uh guided through the
process uh with the EPF people who join
fellows are uh able to work on the
things that they want to work on it's a
lot more kind of free form and and open
whereas uh this internship program
you'll be directly mentored by a single
person who will kind kind of be giving
you tasks to do and and uh giving you a
slightly more hand holding through this
process uh in addition it is a shorter
uh duration so um yeah there's that uh
we are going to be opening the
applications tomorrow so if you are
interested in participating in this
program uh you can go to blog.
ethereum.org so the ethereum uh blog and
you can see the blog post post where
there will be more details about this
program as well as the link to the
application
form uh applications will be open until
December 10th but we will be uh parsing
through these applications as they come
in so uh again this is not yet public
knowledge outside of Devcon so you guys
are all the first to hear it if you're
interested in participating I would
suggest getting your applications
prepared ASAP because we will be looking
through them as they do come in uh and
then yeah just share it with people who
you feel like might be qualified if you
know about uh your local city or towns
like blockchain organization or meetup
group and there are people that are you
think think might be interested in layer
one uh development or getting into the
space and have some computer science
capabilities uh please do share this
announcement with
them uh yeah I think that's all thank
you so much much we're super excited to
on board the next uh cohort of
developers and researchers yep thank
you thank you very much make sure to
check them out and check all the
internship programs and thank you for uh
coming uh we'll be uh coming up with the
next session the evolution of ZK from uh
with us thank you
hi everyone so due to some unforeseen
events this session is cancelled so the
next topic uh that we'll have is on 3:10
p.m.
uh it's we're going to talk about
circum buses a New Journey so I'll see
you at 3:10 p.m.
me
h for
oh oh
welcome back everyone I hope you had a
great break and you're ready for the
next session um as always if you have
any questions for the next speaker we
will have a QR code on the ride you can
scan that ask your questions and also
interact with the questions by up voting
them so without further Ado I would like
to introduce the next speaker Albert
Rubio who has been leading the
development of circum for the past uh
five years and in his next session he
will be talking about circum bues a New
Journey please give him a big round of
applause and welcome him on the stage
hello uh welcome everybody I'm here to
present a new great feature of uh circum
called buses okay so just a little bit
of context of what is circum just in
case you don't know so circum is a DSL
uh where the programmer explicitly
provides the constraints defining the
circuit and also provides an efficient
way to compute the the witness um in
circum one of the nice features that we
have an a large uh library of circuits
that the programmers can reuse and in
fact this is uh really encouraged
because uh there is the best way to uh
program
easily good and safe uh new circuits uh
what the compiler does is uh from this
produces um constraint system in R1 Cs
on one hand and on the other hand you
you get uh the code that allow you to
allows you to execute uh the circuit and
compute the witness so probably one of
the draws of circum uh till today uh was
the fact that uh circum has a uh or had
uh two simple type system okay let's see
it in a in example assume that we want
just as a as a simple example we want to
to build a circuit comparing uh dates uh
and then what happened that when you
want to do that with
circum there was no way to express dates
you just could include uh signals and
then you need to express six signals for
day month and year of each of the inputs
okay so then you have something like
this which doesn't express any structure
of of of the of the data as as a date
okay so imagine that then you think okay
let's put it all together and then I use
an array but that's maybe even worse
somehow because you don't even have any
clue about what's the day what's the the
month what's the year so what do we
really need so what we need is doing it
properly okay and this is from now on
can be done with buses so with a bus you
can introduce this new type that says
well this is a
a a single structure that will have the
day the month and the year okay and then
from that point on you operate with this
and then you can see well I have two
inputs that are dates and then of course
you can access these uh these fields of
the of the bus using the standard Dot uh
operation okay so this looks much nicer
okay and uh so the point is that buses
are collection of signals like strs in
in other languages and of course we call
them buses because we work with uh with
circuits and then what's a collection of
signals of bus okay so this is the
reason for the name and not using stru
like in another languages uh a bus can
be defined in a in
a in a very general uh way without
restrictions so you can use signals
arrays and other buses okay all together
there is no restriction except for
recursive definitions but they will come
soon okay so then a bus defines a new
type
and the point is that now using these
types the compiler can prevent from
mixing uh data and that's very important
okay so now we we were able to to ensure
type safety and so on and and also this
will help us to define the library of
circuits in a circuits in a proper way
using all these data and and make it
this nicer so let's see a bit a bit of
this orthogonality in the definition of
the of the buses and then you see here I
have this date but then I can define a
new bus that uses this bus okay inside
an array no restriction at all so now we
have a a new BS definition which is made
of a signal and an array of dates okay
look that also we can use parameterized
uh buses as we can have parameterized
templates in in circum and this just to
make things fit well because you see
here I Define a template with a with a
parameter and this parameter is used
when defining a bus okay so then I have
this n for the for the template and this
n is again used to define the the the
bus uh that I'm using as input and look
then here I'm using an anonymous
component another feature of of of
circum then and you see I'm just using
as input the array of dates that that
was a field of the of this profile uh
bus okay so everything is is done
smoothly like in any other language okay
so all of a sudden you can see this code
and it is no longer can see that this
low level okay so it's it was something
that was always said about that was
low level is not level low level anymore
okay so look at this code doesn't look
low level so let's go a bit on what we
are providing with this so with uh now
we can combine buses with another
feature what was called tax and and the
combination of both things that you get
new types using buses and then you also
have some notion of subtyping using uh
the tax okay so know that now we can mix
both things the buses and tax and then
the tax can occur inside and outside the
bus so if they uh are inside the bus
they restrict any instance of this bus
so you attach this property to all
instances of the bus but if you use it
outside it's for the particular instance
you're using Let's uh and and adding tax
is also is very important because
somehow they show particular properties
on on the types Okay so this is a a very
nice combination that makes a
good still not so complex but a strong
and and and and useful type
system okay so all this will impact a
lot in the in the circum lip and let's
see it uh through a uh an example uh
coming from uh from the library which is
this uh circuits for the baby jabjab
elliptic curb and then the the point is
that in the original form you have
something like this you see you work
with points but what happens that you
have again the points are not there okay
so you have here two signals one for the
X one for the Y and and each for the two
points so there is no structure here and
then you also have the operations for
the Mongomery uh for the for the
Mongomery form and then we are using an
array of two uh signals instead of of
the two signals and then you see there
is kind of a is much but uh well who
cares and then you have also the
conversor as circuits and then you see
here we're using the the the the Edward
forms here as two signals and in the
other part as an array of two signals
okay so all together okay it's low
reability and error prone okay so what's
what's different now so look I will just
create a bus for El point and then I
have all the this so nicely written okay
I get an Point another point and produce
other point okay so from a point same
there okay I do this uh this there and I
get the same nice presentation and then
for the you see here I have this two
things and now for the conversal you see
everything looks nice then we have
readable code and type
sa okay so finally using buses I can
avoid using both
uh types of points because in fact they
are points but the thing is that they
are in one form or another then I use
tax to distinguish them you see here I
say I have a point but Edwards okay and
then in Montgomery say I have a point
but it's Montgomery okay and then with a
with a with a conversion it's clear that
I go from a point in Edwards to a point
in Montgomery okay and then the type
check will check everything okay good so
we have revised the the library we have
added buses stxs make it compatible with
different uh primes and uh we don't need
to a it again because we have formally
verified that that the that the the
constraints are the same it's simply
that they are nicely written okay so
conclusions uh circum is great but now
it's even better okay so now we we have
these buses to structure secrets and we
can secrets and we can Ensure type
safety and increase reability and
security and help audit all these uh uh
ZK projects and of course we will have
this uh new circum lip for the for the
for the for adapted to all this and just
this is for coming soon but uh well it's
just what is coming in the next uh few
months that uh will be useful for all
developers okay thank you very much
thank you thank you very much Albert uh
for your wonderful presentation now for
my favorite section we going to go to
the Q&amp;A uh we have the QR code on the
right make sure to scan it and we can
start with uh the first question I I saw
a few questions kind of like are similar
so um some people may be a bit confused
about why a bus is called a boss and uh
why not struct or
class as I said because this is uh
circuit we are programing circuits and
then buses is is the word I would say
it's not just uh uh there is I wouldn't
say well you can call it a stru but stru
are in in C like uh languages but then
why not a map or a dictionary or so so
we decide say okay we are doing circuits
or bosses got it thank you now for the
next question are there any educational
courses that can follow up to learn
Circle programming language oh there are
many there this uh yeah there is a lot
of of uh of of courses and tutorials and
and on the web for for uh for following
and learning circum I think that if you
just put the tutorials on you you
will get many of them available gotcha
so put tutorials and you'll find a lot
of resources and documentation on it
yeah okay next question is what are some
applications you're most excited about
that is possible with circum buses I
mean with buses the point is not that
you will be able to to design new
circuits the point is that you it will
be they will be defined in a nicer way
and they will be readable and uh it it
will be much more difficult to make
mistakes because the even the compiler
will check that all types uh match and
then you're not going to mix things that
are not meaning the same I think that
it's more about the security of the
circuits and the and and and of of the
way you program than the fact that you
can develop
new things or new project that you could
not do before it's Goa so it improves
the security but also offers a better ux
for the developers overall very nice uh
will uh circum become close to a high
level language like
python well in fact as you said I think
that it already uh got with this new uh
types and and and uh in the development
I think that this already can be
considered a high level language okay
maybe we don't have some of the features
but it's also because they are not
needed for our in our for our purpose I
would say I think that that providing a
good type system was the missing step
for for getting a high level language
all right uh we have a few more other
questions so people are very curious
about circum buses so uh maybe when is
it available to use it's already
available so the the release was uh kind
of a month ago and uh we have
just released uh circum 2.2.1 because we
are fixing uh we're improving some parts
but it's all available already and you
can download it and and use it uh in all
your your cets from now on okay the and
for the second lip it will be released
uh the new version with the buses will
be released in uh in few days okay
fantastic so you can already try it out
make sure to to check it out um is it
possible to add methods or Associated
function to a bus
um not not this way because this is not
intended to be like this I mean we are
not an object created language and uh
and the same as we don't have
inheritance or
or we just have this notion of subtyping
by means of tax but and we are not
considering that you have methods
Associated to templates I mean a
template itself does I mean it's a sub
circuit and it's not that think not that
that s that much sense to what methods
to do things on top of it I mean it's
the circuit describes uh what is
intended to do from the inputs to the
outputs but it makes so much sense to
add new operations on top of it got it
and I think this will be the last
questions because we running out of time
so TXS don't have to be declared ahead
of time seems like an easy way to make a
typo uh well there is so for types need
to be declared ahead so buses should be
declared ahead
uh and before using them but for tax is
not like this and well we maybe in the
near future maybe we will start at least
to have the possibility to describe them
and and and from the beginning associate
them to some buses uh in advance to
avoid mixing things or or just making
something that is not easy to
read Because you combine tax in on
different things okay fantastic well
thank you for answering these questions
and thank you for the audience for the
questions again a big round of applause
for Albert and thank you very
much okay um I hope you're ready for the
next session uh we're going to look at
uh the next session is C lookup
composite function based uh lookup
argument so we'll we will be in 5
minutes ready
cool welcome back I hope you are all
energized we still have two more
sessions left of this day so we're
almost done um I would like to introduce
the next speaker uh wo liim who will be
talking about uh see lookup um composite
function based
argument I believe I pronounced that
correctly right so he's been um U like
advocating for open-source fairness and
a cipher Punk OG so please give him a
big round of applause and welcome him on
stage uh hello every everyone uh thank
you so much for coming to my talk um
today I'm going
to uh have a talk about the SE lookup
the lookup argument based on uh
composite
function um actually this is the first
time uh that first time ever that we are
presenting our work uh so my name is
oneop Lim and researcher at
PSC this is a joint work with my
colleagues so I did this work with San
and dun
together and the summary is that uh
given that we have a uh n size of table
and a witness with size of
M then if uh
the size is much larger than the table
size we can accomplish a o of log squ M
time complexity to the the look of
argument
uh I'm going to explain more about uh
how we achieve
this uh first of all I would love to
introduce uh where we got The
Inspirations the first one was about the
gkr because uh we noticed that gkr is a
very a one unique um version of
function and the second was about hyper
plong P2 the permutation argument p iop2
uh it is also using kind of a composite
function it was very inspiring for me to
uh think about the local argument using
that uh and so using that we are using
some competent function just like in
gk's each layers actually in our case we
are using only one layer and we are
achieving the O of uh log squared and
time
complexity uh uh so first let's discuss
about the objective and let's understand
the current
situation that we have two
sets uh first one is about witness and
the second is about the element of the
given
table and our goal is is to prove that
for every element in uh W is also an
element of a
table in other words uh we are very ver
ifying that each witness element is
contained uh within the
table and this implies that the set of
witness W is a subset of the table
t uh okay and before we go uh Deep dive
into the lookup argument C lookup
argument protocol I would love to
introduce the main uh use case the
interesting use case uh if you have the
look
argument so what if we Define each
witness W as an encoding of function
along with its input and output
result and let T be a predefined
computations then we can formally verify
that f ofx equals to Y always holds true
uh provided that the witness is a subset
of the predefined
computations um this means we can ensure
that each computed value corresponds to
a valid function and input and produces
the correct output as specified in our
predefined table of
computations and it becomes a uh
Cornerstone for formally verifiable
computation so we can Implement some
like zkm which is also called the lookup
singular it which is also the uh jolt
and lour uh
approach um so I'm going to uh introduce
our approach the silico approach so
first we're going to define the relation
Sil up uh as the set of all Ts of public
instance X and the witness
W where the public instance X is a tuple
of Oracles of functions ft and
sigma and the witness is a function of
two is a tle functions T ft and
sigma um to be precisely f is a function
that maps all the witnesses defined on
the domain
XF uh with range
YF and T is a function that Maps table
element defined on the domain
XT with range
YT then if there exists a domain
transformation function
Sigma uh that maps elements from XF to
XT also which satisfies that f ofx
equals to T of Sigma of X for all the X
in the domain
XF then the range of f is a subset of
the range of
T and we say that the Tuple of uh public
inance and witness is in the cup
relation okay uh first I'm going to show
you the knife approach
version we consider a polom f and T and
sigma over a finite field and we're
going to use univariate polom
approach uh then we're going to map the
witness and element using the
corresponding root of
unity and the relation that F ofx always
equals to T of Sigma of X for all the
roots of unity holds true if and only if
there exists a quoti polinomial q such
that F ofx minus t of Sigma of x equals
to Z ofx * Q ofx for the vanishing
polinomial
Z actually here exists a caveat
that
um the degree explodes the degree
explodes if we have the univ polinomial
and if if we compute the composite
function the degree of the whole system
uh becomes a degree of T times degree of
the uh
Sigma so which means like n * m
but if we use multivari polinomial
approach it changes a
lot we will Define the domain uh on the
vector space uh for the witness we're
going to uh Define its domain as a bll
hyper Cube uh over a log M dimensional
space and for the table we're going to
define the domain uh over the log n uh
dimensional uh space
and then uh defining the domain
transformation function Sigma uh as a
tuple of all the domain transformation
functions then the relation that the F
ofx always T of Sigma of X holds true if
and only if there exists a auxiliary
polinomial H uh which satisfies some
zero Che Pol zero Check Pro P
protocol precisely here the r and RP
Prime and GMA are the randomly chosen uh
Vector from the
verifier and the auxiliary polom gives
you the Rel gives us the relation that
the there exist mapping correctly and
the domain transformation is actually
bound to uh the zero and one
correctly as a result uh we could
achieve the low squ of M against the
witness size or log of the table size
and complexity time
complexity if we think about the
protocol uh let's go through the
protocol quickly so let's assume we have
a witness F witness F witness Vector F
and the table Vector T 2 3 5 7 115 like
blah blah blah and the first step is
preparation so we're going to compute
the table polinomial but for a efficient
uh some parallelization we're going to
use the coefficient form but it doesn't
actually actually does not a big uh
thing because it's a pre-processing
period and then we interpolate the
witness so just say for your uh easier
uh understanding I just expressed this
in a coefficient form and then we also
need to find the domain transformation
functions this is just a mapping between
the uh table domain witness domain to
the table
domain so if you express that in a
coefficient form actually we are using
only the evaluation
form and then uh we use public coin
protocol to uh run some check only once
uh by patching every everything together
so we we choose uh the verifier choose
chooses is the r RP Prime and
Gamma and in this case let's say we
chose 3137 for R and five and 7even for
RP Prime and 9 and 11 13 for the
comma rerun some check the first run
will look like this and you can see here
uh the intermediate univ polinomial is
not a linear function it has some
degrees um and we run the following
rounds and as a
result uh we need to check the resulting
eval random evaluation from this Su
check equals to the thing uh that we can
quy from the
Oracle uh which was the one of the
public instance acts so we carry the
evaluations through the oracles and we
check this uh they are hold they the
relation holds true by checking this
condition and
consistency one important thing is that
the uh main advantage of this approach
is that it is very easy to decompose
into smaller tables so we have a t
polinomial here and we can uh decompose
it into two smaller pieces T1 and
T2 in T1 is just a t of 0 comma X2 comma
X3 and T2 is actually T of one comma X2
comma X3 so we can decompose a table
very
easily we can uh composite more smaller
pieces also we can utilize this uh
composite function approach with a a
some we can tweak a little
bit uh if if it to this a little bit
then we can also compute the two
intersection I mean size of two
intersection of two given
set and actually the result for the
computational results also uh shows the
same
result uh one of the key Theses we had
here is that if we uh use the composite
function using
multivariate uh setup then the C becomes
to uh
logarithmic and if we maximize the
parallelization uh we thought that okay
here's the composite function cost and
in Univar function it was the really
high because the degree was exploding
but in a multivariate setup we can
actually log Lo logarithmically change
that and the result is actually like
okay it depends on the number of rounds
Times uh the composite function cost
evaluation of the composite function
cost and once again composite function
is a very very generalized version of a
gkr is
approach um and to demonstrate our
thesis actually we implemented the Kura
based Su protocol price in this
repository so it'll a highly paralyzing
all the evaluations polinomial
evaluations using
GPU and then we utilize this Kura Su
check to see the results in this uh
click of repcal repository we just use
kjj just for easier implementation but
definitely you can change this
commitment scheme to
others uh and successfully we could see
our result appro shows the logarithmic
increase compared to the classical
approach actually the implementation and
Benchmark data is is still being fleshed
out so uh but we are pretty optimistic
for about the result that it's showing
the sub linear uh result not only
against the witness side but also
against the table
side uh
conclusion this approach is a very
simple to
understand uh comparing to other look of
approach and it supports table de
competition
gracefully and also it achieves sub
linear proving
time uh my toe was a little bit longer
than uh compared to the given time so I
cannot have some enough Q&amp;A time I'm
going to be out there so thank you so
much uh coming to my
talk thank you very much W for your
wonderful present ation and teaching us
about C lookup thank you and uh we're
going to start at 3:50 with the last
session so stay tuned we're going to
send in a few
minutes down
okay so we are ready for the next and
last session so I hope you're all
excited um without further Ado I would
just like to introduce the last speaker
for state age three freedam Basu who is
a cryptographic researcher at PSC and
for the next session he will talk about
Anon Adar I believe I pronounced that
correctly so it's Anon Adar protocol
using Noir 2 and hello 2 and Noir please
give him a big round of
applause hello everyone my name is Ram
Basu and I'm going to talking about Anon
another protocol using hello to an Noir
uh so uh without further Ado let's go
into the talk so here's a brief outline
of the talk I'll firstly introduce the
uh protocol was the Anon protocol and
then I'll go into the details of the
circuit and the features and how you
basically implement it and then uh I'll
go into the details of the
implementations like Hello to and Noir
and then I'll end with applications
so uh the Anon Adar is basically a zero
knowledge proof of identity protocol uh
with for Indian citizens uh which uh
basically preserves the privacy and
doesn't reveal the sensitive information
which are uh there in any social
security card so the Adar is basically a
social security card for Indians and it
also provides a set of tools uh for
generating an verifying proofs and uh it
authenticates users and also verifies
the proofs on chain
so uh there are a lot of problems with
the previous uh proof of identity
Solutions like in vanilla uh you know
kyc Solutions you need to reveal the
full identity and then uh if there's a
centralized database like the adhar
scheme uh so uh these database are
ideally uh vulnerable to um database
hacks and privacy leaks and there was a
lot of criticism for the Indian
government uh since the time it came out
and of course like if you put all this
information on Chen it's also really
bad so uh there are a lot of other ways
to do identity Solutions one is
Biometrics where you can basically uh do
like you know uh fingerprint scan or ID
scan uh for creating immutable records
uh also there's a concept of an
aggregation where you are basically
combining activity data from various
sources and you can basically uh provide
a comprehensive trust score uh in
including some social graph analysis and
then there's the third uh category of
leveraging document signatures uh and
this potentially uses some cryptographic
signatures to verify and authenticate
users on
chain so uh the Anon Adar protocol is in
uh the last category and uh in the
previous slide and basically uh how we
do it is basically we check both the uh
sha 256 hash and the RSA signature of
Adar identity and uh you know this
basically is was originally built um at
PSC with circom and uh you know there
were uh three libraries basically one uh
was the typescript SDK uh which is in
the core uh repo and then there's the
solidity library for the contracts and
also there's a react Library so uh
what's the problem statement so a
government potentially like uh will sign
and issue an identity uh to a user or a
citizen in this case and the citizen
basically Ally uh uh gives this uh uh
identity uh in the form of a scanner
we'll see in the next slide uh to
construct a proof uh uh in this case a
zero knowledge proof which will
basically hide all the sensitive
information and then there's a verifier
which verifies the proof of identity
from the uh approver so uh I think this
audience is fairly knowledgeable about
ZK snacks but I'll briefly go over it
for completeness so ZK snacks are
basically a way to prove the validity of
a statement without uh revealing the
witnesses or the private inputs and S is
the most important uh you know acronym
uh keyword in the acronym here so
succinctness which means that it offers
short proofs and short verification time
which is basically ideal for onchain
verification so uh and the two
properties correctness and uh soundness
uh which basically means that you know
the um like it ensures proof validity
and also prevents forgery so uh this is
a circuit so uh in this part uh
basically is the you know sha and the uh
uh RSA signature which I described in
the previous slide then there's the uh
extracting the fields from the sign data
uh so the photob bytes are uh extracted
and it's used to compute the nullifier
here so along with a nullifier seed
which is also uh uh you know obtained as
a public input uh here and then there's
the other part which is the uh
conversion of timestamp from IST
timestamp uh to the UTC Unix uh time
stamp universal time stamp and uh
there's an algorithm for it I'm not
going to go into the details of it and
then there's the third part which is the
signal hash so this is basically
preventing front Runing attacks uh so
There's a constraint which we apply on
the signal hash so in the circuit the
private inputs are only the signature
and the signed data uh these are all
public and then this part is the
conditional disclosure of secret so if
the uh these four parameters there's
four parameters in the Adar data like
age gender state and pin code you can
choose to reveal it so if you choose to
reveal it then only these will be
revealed at the end right so um yeah so
basically uh this is the uh Madar app
where you can download the uh any Indian
can download the uh um like AAR card or
there's a scanner and you it hides all
the sensitive information uh and like
this name gender and so on and uh you so
these are the features of the uh anadar
protocol like the user nullif this
basically prevents uh double spending
attacks uh Prime stamp this is acting as
a time was OTP system the public key has
it basically uh ensures that the signers
public key is same with the public key
generated by the uid which is the
authority and also the signal hash which
is used to prevent front running attacks
so uh I'll skip over the challenges and
caveat but mainly this says that there's
a lot of uh you know problem with uh
getting signed documents by the
government and what kind of data the
government chooses to sign uh so uh Halo
system and has a recursive proof support
so um this is some of the libraries that
I used for Halo 2 and I wrote each of
the separate circuits that I shown in
the circuit slide separately and
combined them into one circuit and
tested it with DL data so this is the uh
results uh for Halo 2 so most of the
stuff is very uh you know efficient in
milliseconds for proving and micros
seconds and milliseconds for
verification except the RSA part and uh
the onchain verification cost is also
pretty uh in efficient it's like 6.5
million gas for the Halo to gas cost and
for Noir uh you know it's one of the
foremost proving systems by Aztec and uh
it it basically we can write custom
circuits and prove back end using
barenberg CLI uh and same algorithm as
no like Halo 2 implementation elliptic
curves and uh b254 and the versions are
given here and these are the results for
Noir uh5 seconds uh roughly for proving
time under for all of the parts of the
circuit and 0.05 seconds roughly for the
verification time uh the gas cost is
like uh you know under 3 million for
each of them so the code is entirely
open source you can check it out uh and
in summary you know Noir is much much
faster than Halo 2 in terms of all three
parameters uh bottleneck in halo2 is RSA
and but circom however beats Noir and
hello2 for onchain verification cost if
you use nor Ultra honk back end it's
coming so it might be more efficient so
uh there are lots of applications I
won't go into the details of it like you
can check it out in the Anon AAR page so
there's PR ID SEMA 4 and Anon AAR
checkin and like uh you know quadratic
funding and lots of others so these are
some of the references and I'll end here
thank you so much for your attention and
I'll happy to take
questions well thank you very much for
uh presenting this uh we can probably
take one question from the audience so
um maybe let's see what are the plans to
make it work in a real world local
government office any ties up with the
Indian government plann yeah this is a
very good question I actually am in the
process of like you know independently
doing this work uh so you know there can
be lots of applications uh and other
government countries of course like
there are other projects like open
passport and like you know ZK passport
uh who are doing doing similar work and
I'm also uh in talks with them so there
is a plan to commercialize it in short
but uh like you know there's a lot of
bureaucracy involved particularly with
the Indian government if you talk about
it and with other governments we can
figure it out but it's a separate thing
from this because PC is uh you know
usually uh you know not for profit
organization but yeah I'll be happy to
take this question offline and you know
if somebody's interested in the audience
we would like to collaborate with them
sure you guys know how where to find him
so maybe we can take another question so
let's see uh did you do the comparison
between Noir and Haru for benchmarking
only or they were
complimentary uh so yeah I mean uh like
not for uh yeah we did it for
benchmarking uh with respect to circom
because the original library is in
circom and we implemented it because uh
like we wanted to understand if Halo to
or cir Noir would be better in some
aspects of course like you know Halo 2
had a steep learning curve but Noir was
uh really good I mean it's uh very easy
to you know implement it and also very
efficient and uh you know like it
depends on the details of implementation
but Noir is pretty good almost like
circum but circum still beats in terms
of the gas cost today maybe in future
who who knows Noir might beat it yeah
fantastic I think we're running out of
time so uh do you want to take another
one or sure sure sure yeah uh do you
prefer something yeah isn't the onchain
address pous only uh yeah I mean the
onchain address is definitely uh like
like like I don't know the question but
generally like we can hide using ZK
proves all the information uh so
definitely that's there fantastic well
we're running out of time so thank you
freom again for your wonderful
presentation please give him another
round of applause thank you very much
thank you so much so uh we're kindr of
doing a wrap up this was the last
session for this stage make sure to join
the closing ceremony at the main stage
it starts at 4 p.m.
thank you again for
listening to me my name is Robert codra
I'm a developer Advocate at the starna
foundation and I was the MC for today
thank you again and uh wishing you a
nice
day is as much a technological object as
it is a cultural object right it's not
just technology it's culture as
well and when you have something that
has multiple dimensions you can kind of
like make different things load bearings
at different times if you have something
that is purely technological and the
technology doesn't work then you have
failed in some sense you can kind of
promise that it will work better at some
point but there's there's a thing where
almost like a support network around you
means you can take more risks I think
that having an object that has multiple
Dimensions makes it more anti fragile in
some sense and so I find what I find
really interesting with the theorem
because system is that in general
there's a lot of energy for things that
on a surface level might look like
playful or silly or not going anywhere
but actually in many way I think this is
almost like an immune system for making
sure that um excess talent and excess
Capital gets distributed to a lot of
different kinds of experiments like one
sentence we use as ZB quite often is
when something is going in a strange
direction or not successful say that's
an experiment worth enabling not like
this is a failure or something like that
and I think uh the great thing with with
the Theos system is that it creates a
lot of experiments worth being enabled
and you both kind of like increase your
your rate of trying things but at the
same time you give a lot of space for
things to grow and one thing with
cryptography and and we see it when we
interface with academics or with the
industry Outside The Ether ecosystem is
that cryptography at this stage outside
what it can do very well and has been
doing for many decades it's almost like
going back to square one in Computing
and people don't want to go back to
square one because they're like I'm used
to all of this nice stuff like why would
I go back to square one and so in some
in some ways having an a place where
going back to square one actually has
been done in recent memory you know like
ethereum has gone back to square one
like a decade ago so because it started
at square one I think like this almost
like knowledge like it's still within
this generation that this has happened
does create a lot of space well going
back to square one reminds me again of
subtraction so not to just completely
hit this note again but I think there's
something important about being able to
let go of things too you know for um I
mean there's this there's this analogy
that sometimes I bust out with people
about ground Apes which are ground apes
are really good at grabbing stuff if a
ground ape grabbed me I'd be in trouble
