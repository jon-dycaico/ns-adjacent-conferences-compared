when you start up the VPN you can choose
if you want to be fast which is no
mixing or you want to be anonymous which
is a mix net so we mix your packets up
and then you choose like where you want
to come in the nearest nodes I think
here are Singapore or where you want to
come out and then you cut and paste that
uh oop sorry you cut and paste that QR
code in and then it just works so that's
it we have a lot of cool stuff coming
please try it out it's free for a month
so we can defeat
authoritarians uh like Trump and all
these okay so yeah that's
it uh time for
Q&amp;A okay q&amp; time so in this stage we
will be throwing this microphone so
raise up your hand if you have a
question oh opportunity uh the Deep
State Democrats as well just just so you
know you're first okay catch it sorry
I'm not very good at
this um I just want to know what's the
main complaint of your current
users it's mostly crazy cryptocurrency
people doing beta testing so we have a
lot of people in countries which have
some form of censorship uh folks in
Russia China um we're still working on
some of the censorship prevention
techniques they get around like you know
certain kind of firewalls but mostly
it's just crypto people who are token
holders who just trying out and having
fun I think we have about five 6,000
people downloaded using it so but it
just started basically
but unlike a normal VPN the more people
that use it the more Anonymous you are
unlike tour or normal VPN so 5,000
people's a reasonable size in am many
set Yeah you mentioned earlier mysterium
and orid and they both are on the market
since a time and they both struggle
really to get any significant amount of
users like what what do you think what
do you think something we can do about
that to get more people to that
decentralized world yeah you got to on
board the normies like normies so the
problem was uh we looked at Orchid I
like 7 a cool dude uh but the problem is
that they said oh pay as you go so I
want to pay for a gigabyte or a megabyte
normal people don't do that and they
also required like some weird token
stuff to get the thing going and most
people have trouble buying tokens right
so what we do is we just have a normal
Fiat interface stripe do you like
Bitcoin my BTC pay and we take that um
payment in Fiat or whatever and then an
API converts that uh over to Nim token
and then and then we do Auto a atic buy
of nim tokens on the open market so it's
all invisible the token part and there
tokens that reward the nodes uh it's all
invisible to the enduser I think the key
is to make it look and act as much as
possible like a normal VPN but also
offer features that normal vpns don't
have so we have this Anonymous mode a
mixnet which no one else has for the
world's first decentralized actually
Anonymous mixnet you know support
Chelsea Manning works for me Julius s is
a big fan and that's something that no
normal VPN has
okay last
question I'm around afterwards grab me
afterwards run run run throw the
ball H why doesn't T just add noise uh T
has looked at it actually had dinner
with Roger last night you can ask him
this question they are considering uh
but Tor is not a mixnet so Tor optimized
for Speed which is reasonable for them
to do back in when they started their
code and they weren't like it's it's
complex you have to have like figure out
like you guys have to do some form of
traffic shaping and at the time this was
a harder thing to do mad's also looking
into adding noise I think they have it
working on iOS or one of their clients
it's actually really it's a large map
tricky machine learning so U mix Nets
particularly what we are called
continuous time mix Nets we actually do
a default what's called traffic shaping
to pan processes so you don't know when
you're packet R but you always know the
average time and that makes adding noise
much easier okay I think that's it I'm
sorry
next next I guess let's give a big
Applause to
Harry thanks for his Insight all
right okay next up we have jakomo he's a
cryptography engineer working for psse
in the ethereum foundation and today
he'll be telling us when to use ZK proof
FHA and NPC let's welcome Jomo
yeah it's
working okay cool so hello everyone uh
I'm joind I work as a software engineer
at PS team so as many of you know uh the
last few years have seen a huge
generational shift in cryptography we
passed from specialized to general
purpose cryptography and this has
brought exciting new opportunities for
everyone to make it more practical but
this comes at a cost the cost is that we
should navigate lots of jargon and
mathematic and to get the big picture
also for people that is experienced in
the field it's pretty hard like
navigating the protocols
Primitives languages tooling
Etc so today we'll try to do something
very difficult to give just an overview
but we will say a really high level
general purpose uh in order to
understand what the building blocks of
programmable cryptography can bring and
we will just focus on the programmable
part instead of the cryptography which
is how things work under the hood
because we do not have much time so
um yeah zero knowledge proof so a zero
knowledge proofs make one party the
prover able to prove uh to another party
the verifier that the statement is true
without revealing any information beyond
the mere fact of the statement's
validity so you can use this for example
to prove your age that is above some
sort of threshold without saying exactly
what your age
is um secure multiparty computation U is
a set of cryptographic protocols that
let multiple parties collaborate
together to compute a function providing
their inputs maintaining those inputs
for all the computation private this is
useful for use cases like voting when
you have to like vote on something and
you want to keep your vote private and
you do not want to trust on a third
party to count the votes then we have FH
fuel amorphic encryption set of
cryptographic tools that enables you to
do encrypted
computations what encrypted computation
mean is that once decrypted you get a
plain text and this plain text is the
same as you it performed the computation
on the decrypted data directly this
ideal for scenarios like AOS sourcing
computation like running machine
learning model without letting the model
owner learn about your data um each of
this block is pretty powerful by its own
um but they open up fascinating
possibilities by combining them in
particular
um uh on like trying to solve their own
like
drawbacks for example dqp can be seen
has an efficient up specific MPC but
combining them you can obtain um
verifying like the MPC computation like
able to prove that the multi party
computation was performed correctly
under some assumption in the key so
instead of just Computing you can also
prove from input to Output the
computation or you can Outsource the
computation so you can rely on other
people doing the computation for you
like they can be like uh more than one
people and this can enable complex
cryptography also in res constraint
deviced because you're not Computing by
yourself another combination and PCF
like one of the biggest challenges in F
is managing the decryption keys and
there are two main approaches the first
one um is with MPC Distributing the key
generation so you have multiple parties
and they can jointly and manage a single
F key where no single party has the
ownership of the key and the multi ke
every once has a key and they should
combine the key uh to perform the secure
computation and on the other hand since
FH is just addition multiplication of
cyppher text you can achieve sum of
product um the of encrypted values so
you can build generic
MPC with zp and F is the most
experimental and is basically trying to
tackle two questions the first one is
how can to trust that the encrypted
value was correct under some assumptions
like is a correct BF Cipher text or I
can trust that the computation was done
correctly and all three blocks
combined um is like you can combine them
it's technically feasible we can add Z
key to make verif verifiable npcf
combination you can add T's trusted
execution environment to do the Z key
and participate in the MPC FHA but um we
are still need to take into
consideration that many real world
problems can be solved with just one
vanilla block like just the key or MPC
and defining resources constraints and
unique needs of your problem can help
you navigate all the space of the
solutions and help you to make the right
choice um I'm running out of time so
thank
you okay we have three minutes Q&amp;A raise
your hand if you have a question that's
a little bit far I'm going to try
that's why I Outsource to
you maybe I should give it to you uh hi
uh what are the most interesting use
cases for every single one of the uh
technologies that you've seen um like zy
mpcf or the combination uh I mean is
there a combination application yet um
yeah there are some not applications
that like I cannot say that they are
production ready there are some
Explorations and
research uh so you have mainly like
tooling that can help you to distribute
the key of f in NPC or you have like
some sort of initial research in
verifiable FHA like proving that your
Cipher text is encrypted correctly so
there's still Lots going on and as I
said it's hard to keep up with
everything so maybe I'm not aware of
other stuff but in general yeah I think
the most exciting thing is trying to
make like advancement in the FG video Fe
ability because this can be really a
breakthrough and I don't know if I can
make another question but uh is there
any framework yet for uh F morphic
encryption with contracts like for Main
in solidity um when you speak about Main
and solidity uh I think that f is mainly
off stuff there are some teams that are
working on onchain FHA as well um but
yeah you can find like the
state-of-the-art in the tooling and
developer experience is not like as the
key one right now so there's still lots
of work to do in libraries tooling and
Frameworks right now there are good
libraries good Frameworks but mainly for
experimental research more than going to
production thank you thank you so much I
think I think we have time for one more
question thank you for thank you for the
presentation is f general purpose can we
use it for every for all computation all
kinds of computation um so I'm not 100%
sure but f is mostly additions and
multiplications so you can maybe emulate
everything with those operations and so
yeah you can have some sort of general
power po FHA going on but
um all the nuances about like the
constraints
on how efficient it is or how can be
applied on small devices or other stuff
is still depends on what kind of backand
you are going to use yeah I
think okay we have seconds let's give a
big hand to thank you so
much next up we have rosu rosu is a
software engineer he works for PSC
focusing on NPC research today he's
going to tell us about NPC tooling and
how to create NPC apps let's welcome
[Music]
rosu hi everyone uh my name is rasul I
work in MPC research team of privacy and
and scaling Explorations and today I
want to talk about NPC tooling or how we
can create NPC apps so what exactly I'm
going to go over is like first short
introduction what is MPC then I'm going
to talk about applications of NPC and
then I'm going to talk I'm going to
cover tools we work on in our team uh
that allow people to create NPC apps and
then short example interesting example
of using these
tools so what is NPC NPC is an active
protocol that allows parties to jointly
compute a function or their inputs while
keeping those inputs private so let's
imagine that we have a public function f
that takes two parameters X and Y uh and
let's say party one provides x uh X
parameter party two provides y parameter
and they will be able parties will be
able to compute the output of this
function uh while keeping their
individual inputs
private so there are two kinds of NPCs
first one is app specific and second one
is general purpose MPC so app specific
protocols MPC Protocols are designed to
uh represent one specific function so
let's say threshold signatures Shamir
secret sharing and PSI and many others
and general purpose to are designed to
represent any function including the all
the app specific protocols as
well so there are many applications of
NPC uh I'm going to like mention a few
examples so it's like privacy preserving
preserving machine learning uh costars
uh NPC stats is another great project
that pctm works on uh and
Etc so first tool I want to talk about
is called circum MPC uh C circum MPC is
basically a project project is a fork of
circom it's a famous ZK DSL but it
compiles to Universal NPC format called
Bristol fashion circuit uh that can
describe Bullen and arithmetic circuit
so why we chose circom is because many
zk/ cryptography devs already know
circom uh and it's easy will be easier
for them to create circuits in circom
and there's also a big number of
circuits written in circom already uh
for example circom Li Mel uh and they
can be reused without changing the code
and that's actually what we did in p as
well we just took circum liel Cathy's uh
library and we were able to run NPC uh
circuits NPC in uh ml sorry in
NPC another I want to talk about is
called summon uh summon is a language
for collaboratively summoning
computations uh and it's another tool
that my teammate mostly works on Andrew
Morris uh and summon is typescript like
DSL similar to circum NPC with a goal
for user friendliness it can be used
from uh or in typescript uh and
therefore it allows to build everything
end to end in typescript so if you know
cursive team uh they already use
summon tool as well uh in their
apps and the last tool I want to cover
is called circum MP speeds so first of
all MP speeds itself is a like big big
framework that people can use to create
MPC apps but it might be a bit uh a bit
uh hard for beginners to start with it
so what we do so circum AP speed is
basically a transpiler from Bristol
format that generated by someone
compiler by circum MPC and a transpiler
from Bristol format to MPC
representation that is required to run
the circuit in MPC uh M with MP speed's
backend uh and this project shows an
example of running circum Liam ml
machine learning circuits in mp speeds
and you can find uh benchmarks and
everything every every information about
this uh in the repo and uh yeah as I
said the same tool can be used to
transpile Circus generated by someone as
well not only by circum
MBC and the last thing I want to talk
about is an example of using these tools
specifically someon uh it's a matching
game for friends and lowers uh that
Barry White Hat was talking about last
year on defc connect Istanbul it's
called two PCS for lowers so basically
you can play with your friends or with
your lover and you can choose love uh
but if you choose love but the result is
friendship you only you will know about
your feelings uh even if your friend
knows Advanced cryptography yep uh and
you you can try it here yeah that's it
uh thanks for coming uh you can find me
uh by my username K
yep thank you
Ru any
questions oh there's one uh I probably
need some help no do you want to
try yeah let's
go uh we might here
there sorry sorry geie oh it was a good
direction so okay um I have a question
uh did you explore using MPC for
building interoperability or
Bridges uh no actually no I don't think
so I don't think so no uh do you have an
idea uh like for example opinion yeah I
mean building interoperability protocols
with NPC no we weren't doing this we
mostly were focusing with for I work
mostly on uh circum MPC uh so we were
focusing on privacy presing machine
learning like mostly and uh yeah not not
on that case yet yeah sure I mean we are
just exploring and and getting into it
so wanted to see like more opinions and
Builders around
that okay thanks uhu sorry sorry if I if
I didn't answer
we see a question over there yeah oh
this is a mic oh sorry I didn't know
this is the mic uh sirom is a usually
targets an R1 CS back end and so I'm
assuming all of these other tools also
and it's kind of I guess my question is
do you pay a price for that or there
other NPC arithmetization that um you
work with or is there something
inherently related to the serom tool
chain that you find useful here uh sorry
your question is do we have so my
question is that uh sorry oh okay sorry
I was not here when the dice was
introduced but my question is that R1 uh
sirom is typically targeting an R1 CS
backend and so I'm assuming all these
Frameworks and toolings are doing the
same but there are some pretty clever
other arithmetization and I'm wondering
if MPC is uh solely in this domain or
you can make use of other uh things like
plon or other artiz
yeah I think it's like uh as I mentioned
uh we like it's a fork of circom uh and
we don't Target our 1cs uh instead we
target uh Bristol format format Bristol
format is a universal NPC format that
can describe uh arithmetic and booing
circuit and uh yeah it's just like a
super simple format and from this format
you can already I don't know also
transpile it to whatever backand you
want so for example npz library is like
another library that PC works on you can
Target this Library uh you can uh Target
MP speed's Library yeah Etc
yep let's give a big Applause to Ru
thank you
[Applause]
Ru okay our next lightning talk will be
from enrio Enrico works for psse in
etherum Foundation today he's going to
tell us about multilateral cred Trade
Credit set off in MPC welcome
hi
guys oh sorry so my name is Enrico batti
and today I'm going to introduce you to
multilateral Trade Credit set of in MPC
which is an application of MPC and this
is a work joined with my colleagues and
fellow researcher Nam and masato which
are also part of the PS C team inside
the theum foundation so let's jump into
that first of all I want to introduce
you the concept of a payment Network so
as you can see here the payment Network
involves three firms each firm has a
balance and each arrow in this graph
represent an obligation like some amount
of money that a firm owes to another and
the problem of this payment network is
that they are kind of stock because each
firm given their balance they cannot pay
another firm so for example firm one one
cannot pay firm two because they are
waiting firm three to pays themselves
and the same goes for the other two
firms and apparently the only way to
solve this problem is to use uh external
liquidity which we know that is
expensive but actually there's another
solution to solve this problem which is
multilateral Trade Credit set off and we
can see how we apply that from the
figure on the left to the figure on the
right and you can also intuitively
understand this thinking about like if
you owe money to your friend Alice Alice
owes money to your friend Bob and Bob's
owes you money you don't need to make
free payments to settle everything you
can just remove the depth from the
system and another example that might
help people understanding it is how the
application split splitwise works so
what we achieved is a way to remove
obligation from a payment Network
without uh leveraging a expensive
external injection of
liquidity so this is uh an example of
multilateral Trade Credit set off on a
biggest scale apply on the network in uh
in Sardinia in Italy and the cool thing
that you can see is that the more are
the firms participating it the bigger
the higher the chance to detect these
cycles of credit and depbt and therefore
the greater are the liquidity savings
for the firms involved into the payment
Network
so this is actually something that
exists in the real world like the flag
that you see on the top right is the one
of Slovenia country in Europe and this
is how the process works so the firms
that decide to join the system will send
their Credit Data to this third party
agency managed by the government and
this agency will reconstruct the graph
perform this set off so remove these
cycles and return the updated data to
the firms while it works in practice
there's a very low participation rate
and this leads us to our research thesis
we believe that the limited
participation is due to the fact that
these firms have basically to give up
all the information The View on their
sensitive Trade Credit Data to this
government agency and we also believe
that if we could build this same system
with privacy embedded into that the
participation will be higher and this
will also yield as we said before
greater and um higher liquidity savings
for the firms involved in the system so
what do we mean by
privacy first of all we want to hide the
balances of the firms we want to hide
the amount of each obligation and we
also want to hide the topology of this
payment Network so in practice it means
that we also do not want to reveal the
fact that there's a specific specific
obligation between two firms in this
network and how does this work we
basically replace like um before you had
like the the government agency there now
this is replaced by a set of MPC servers
that are able to perform this operation
somehow
obliviously so unfortunately I don't
have time to go through like the details
of MPC and the algorithm that we
construct but I want just to to bring
the most significant results of our
research so we were able to
significantly reduce the asymptotic
complexity of this algorithm to be
performed in a MPC environment and we
did that mostly through two techniques
one is secure graph anonymization that
allows this servers this uh multiparty
nodes to anonymize the graph before
opening its shape and the second
contribution is the secure network
network Simplex which is a um Network
flow algorithm and we build its
corresponding and efficient version in
MPC so we're going to publish a paper
related to what I describ soon and you
can check my blog to be notified or also
follow me on Twitter to see the result
published thanks for your
attention thank you
enrio anyone has any questions raise
your hand and I can see you and I can
throw this to you
hopefully okay this one is
close all right uh my question is what
happens if party one has a higher
interest rate than party two is that
able to factor in interest rates yeah uh
we we we didn't get into this part
basically so we are just uh tling this
problem from a cryptographic perspective
not getting too much into the details of
the of the
process uh hey uh great use case um how
do you do the like can you touch a bit
the secure graph anonymization like are
you using something like an oblivious
Ram like what's the what's the actual
MPC technique to anonymize the
connections yes so basically we for that
we borrow a technique from this field in
Academia that is called graph
anonymization that is not related to
cryptography and this is mostly used by
like when a when a company for example
wants to open source some some graph but
they also want to hide the data uh
behind the graph what they do is they
use like this kind of obfuscation
or uh perturbation technique to the
graph and for example we use a technique
that is very simple it's called like
random add and eltion so you basically
just randomly add some Edge in the graph
and randomly delete some Edge in the
graph and what you get out of that is a
a new graph which basically like the
entropy generated by this uh by this
mechanism is high enough such that you
cannot infer information from that so I
I guess that it's also correct to
mention the trade of because since we
are also deleting Edge we are somehow
sacrificing some of the optimality in
the algorithm because basically some
obligation will disappear but I think
this is a trade-off that we are willing
uh to
accept we have one more question left
one
minute thank you um is there does it
relate to blockchain in some uh possible
applications uh no not
yet oh maybe one more
oh there's a question at the front is
the lady here oh sorry thank you yeah
thank you for the talk so basically it
creates an equivalent graph from the
initial graph and then what what happens
after that it's being reconstructed uh
and it looks like the algorithms that
you described is basically like AC
encryption where some rows being vated
and then switched with each other or
something like this so that are supposed
to be Key by which you can revert the
procedure and then do something with it
or yes yes so I have 7 Seconds like the
idea is that after the graph is
anonymized this parties of the MPC will
have an open version of the graph that
doesn't really conceive any meaningful
information and what they will do from
that they will perform this uh algorithm
which specifically is uh about like
solving the minimum cost flow problem
over this graph in a MPC like um linear
secret sharing way so it basically means
that all the values that are part of
this graph are split between parties so
every time they do I don't know an
addition a multiplication or a
comparison between secret Share value
they will also get as a result another
secret Share value and uh in order to
reconstruct this value in order to see
what's behind the real data basically
all this party need to collude and
recompose the value from the shares so
that's how we guarantee the Privacy
basically oh we have time for one more
question um so the results are some is a
chain of liquidations right uh so can
this result be used to reconstruct the
initial debts so for example if uh if I
get 100 uh liquidated and my friend also
gets 100 liquidated and another friend
gets 100 liquidated that means that
there were some relations between us and
people could just use this to
reconstruct the original de which want
to hide yes yes that's true I mean like
the one of the assumption that we make
in this um in this construction is that
the firm itself are not malicious so a
firm is interested in protecting their
own data and they're not trying to
collude with other firms to fetch like I
don't know some uh intermediary party in
this uh in this cycle and uh what I what
I would argue is that they could do this
anyway even without this uh this system
so it's not that we are trying to solve
the problem of u a FM not being able to
see if there's a some intermediary party
between uh between themselves so
probably I didn't explain it very well
but like in our um let's say threat
model we don't consider the firms as a
as a potential attacker we only consider
this uh NPC server a potential as a as a
potential attack attacker that tries to
fetch information from from this
graph okay thank you enrio for sharing
NPC
tooling our next lightening speaker is
saris saris will be showcasing some of
the work the psse members have done when
they were diving deep into FH MPC during
the second quarter of 2024 let's welcome
saris hello everyone um today it's going
to be another uh version of my like Pro
crypto style of talks which is we
speedrun absolutely about a lot of
Concepts uh try to get as much as
possible hold your seat and put your
belt on and let's go together so the
motivation and goals for this talk are
mainly see which are the basic common
questions that we have about FH what is
even FH which I will get shortly into
now see where we can apply it where we
have been able to apply it and see what
limitations and Alternatives and
conclusions about those uh we have so
fine found so FHA why how and what um
basically the easiest way to map that in
your brain is we are able to compute
among other privates uh other people's
private data and so the results are
always encrypted meaning whatever we get
out of of the computational uh result
only us can know the the answer to the
why this is useful uh I mean you can
sort of see this as like an untrusted te
somehow so imagine if instead of te is
being in Hardware they were just
uh an encrypted thing that we all work
and run on the top of math there's like
a lot less security assumptions that
then we need to have and how we do that
well we are based on lots of different
Primitives but I would say the most
important one is latices for example uh
but this is likely for other like more
advanced or mathematical talks so I'll
try to abstract basically everything
that is related to this cor
math what can we build so one of the
first
really small Explorations that we did uh
was can we actually make a Photoshop
which can be a software as a service but
run on an FH server so basically my
picture is private and the server
doesn't know anything about my picture
and I will tell the server I would I
want to do these edits the server will
perform those without knowing anything
about the image and will return me the
image encrypted later so only I can
decrypt it so far Server doesn't learn
anything doesn't know doesn't know
anything at all but I got my picture
edited and this is basically what we did
with Mario here um we can go like
further so we created some kind of frog
crypto shitty game I would say uh we
thought what if we could do more with
our frogs and so one of the things that
we decided is well let's make them fight
so now you have an arena uh which runs
on a server that is basically performing
all of the FHA stuff and so you can put
your frogs there they fight and you just
know what was the outcome of the fight
but you don't learn the strategy of the
rivals you don't learn absolutely
anything at all which can be fun can be
useless I'm not really sure but up for
you to
judge the two most important reasons we
learn is that uh it's a big pain to
write these things like the Photoshop
was okay because it was a negative of an
image then we got into the Pokemon kind
of thing and it was started to be like
it's taking me time to write this and
and the more you want to do like the
much harder it becomes so writing bu and
circuits by hand was not going to work
the second thing was we found a way to
actually crack this thing up uh which I
will go through in a
minute so in terms of speed and it being
uh terribly slow when you want to start
doing like Moab things there's a really
really really nice talk uh by NE imert
uh which you can fetch on YouTube in the
ingonyama channel uh he basically
cracked a way to do really really really
fast entities and summarizing it a lot
entities the core operation of FH which
is embedded into bootstrapping so the
general idea that I want you to get from
there is we can perform like 65 million
second so if we can adapt our problems
to look on this way well it looks
promising that we will get some
significant performance in order to do
more things
the second thing is what do we want to
build now and so forwarding that uh
there's some ideas that we have
discussed of course this is not like we
are committed to do that but this just
ideas that have flourished from this
exploration we can do private uh social
trust graphs meaning I can basically say
how much do I trust people uh in a
completely private graph that no one can
see and we can make queries to this
graph about any other person and we will
know how much we can trust them based on
how much we trust our peers no one
learns absolutely anything about our
relations but we get useful information
out of it the second one could be we do
private web search uh at civilization
scale so imagine we can do this private
information retal protocols and we get
Google's uh index database we perform an
encrypted search and we get encrypted
results out of it so we are just
bringing completely private no incognito
mode stuff uh web searching for anyone
to be
used questions and conclusions uh it was
really cool uh FH is is slow and it will
be like that maybe for some time but
it's really powerful one of the things
we wor is well there's maybe like
Primitives that are more powerful than
that and if if we know those exist
should we focus on FH because maybe we
can just focus on the next thing and
like get even more benefits and more
powerful Primitives
is MPC enough like are we overkilling uh
with the problems and the solutions that
we over engineered here and how much can
we optimize this how can we move forward
like I would say this is like the
classical type of stuff that that I
think we got some insights and that we
have further questions on so that was
the end of the speedrun i h you you are
still there uh so please if you have any
questions thank you questions raise your
hand
okay hi thanks uh just a question you
say that it's slow so what are the most
factors that make it that slow so so
there's a lot of uh tradeoffs that you
can take here basically but the main
idea is you're working over latices and
therefore you're accumulating some error
and the more operations you perform on a
cipher Tex the more you need to like
clean the error out such that it doesn't
eat up the useful information mainly
just to give you some kind of idea now
if you want to perform a bite addition
in consumer level Hardware we are at
around like 4 seconds maybe or something
like that so terribly slow for a lot of
things but there's a lot of subties and
details that you can definitely optimize
for to get the problem like much much
better so one question
there have you tried using 4080 super
for your computations because they have
the new chips yeah so I would say we
like of course Hardware Hardware will be
the bottleneck but we are at the point
that we need to make this a hardware
problem and not a purely theoretical
problem so that's why I showed basically
hair which is a an FH compiler made by
Google so one of the goals is we have
this bootstrapping operation right and
we want to have as less SE qual
bootstrapping operations as possible
because until don't I don't do one I
cannot do the next one so this is like
cool research topics and cool ways in
which we can try to optimize our
programs such that the final
representation that we get allows us to
just throw this thing into a ton of uh
like graphic cards let's say and get a
significant speed
boost
whoa any more question there
have you tried optimistic uh
bootstrapping so where you're where
you're so there's a I mean we have
checked them all so far uh following
this line the last thing that I've seen
that got my attention significantly it's
going back to Circuit bootstrapping
again mainly because they have figured
out a way to like see everything as a
graph problem and remove all of the
dependencies among the the graph so that
the bootstrapping like you can do all
bootstrapping in par essentially so you
can throw this to a GPU at the beginning
and you got it all solved this is the
theory then you need to implement it and
there's constants and they are massive
and you run into issues but I would say
we have looked at them all maybe this is
what personally I I'm the most
interested on but there's proposals
definitely on lots of different like
paths that you can take on that regard
yeah okay time's up thank you
saris our next lightning talk will be
given by Diego Kingston Diego is a
co-founder and also the head of research
at align today he'll be giving us an
introduction of the hash based proof
system here you
go thanks a lot for having me
here it's a huge pleasure to to be
presenting this it will be kind of a
speedrun because five minutes to explain
this so that you understand is to few
but um we'll try our best to get you
excited about this so why are hash based
proof systems important okay so they are
used right now by many projects and they
have helped developed performance CK VMS
that make developing provable
applications easier because now you have
to just write ordinary code and
something else is going to take the Gory
details of uh gener creating the proof
and all that so what are the properties
that hash based proof systems offer
first we can work over smaller fields
which reduces a lot the overhead that we
have in representing the variables then
another Advantage is we don't need any
kind of trusted
setups uh there are like minimal
security assumptions depending only on
um hash functions and uh it's easier to
generate recursive proof because we
don't need to do any kind of field
emulation or elliptic curve operations
which are uh very expensive operations
to to
perform okay so what are the main
ingredients for hash-based proof systems
first we need linear codes in general we
are going to use read Solomon codes
because there are efficient algorithms
for um performing the the codification
then we need a collision resistant hash
function for example ketak but you can
use uh others such as posidon 2 and the
idea is that we are going to commit to
these um code words and then we need an
arithmetization procedure for example an
algebraic intermediate representation so
the concrete choice of the linear code
the hash function and the
arithmetization will affect the
performance and efficiency determining
proof size whether it's easier to do
recursion Pro time verifier time
okay some examples of these proof
systems are Starks with fry Circle
Starks which have shown amazing
performance being able to prove over um
liero breakdown vus that works over
binary fields and can be an interesting
option to build new ckvm and fr
which also works over binary Fields but
has smaller proof
sizes so how do we use for example Rich
Solomon codes to build a polinomial
commitment scheme which is the main
ingredient of many of these proof
systems
so the idea is that at some point we
what we do is we compile the program we
want to prove to a set of polinomial
equations that have to be fulfilled okay
and everything boils down to uh showing
that this polinomial has zeros over some
set or it evaluates to some value at
some point said okay and how we can
commit to a polinomial what we can do is
we choose some some values a domain and
what we do is we evaluate that
polinomial over that uh setd and that is
what we call the read Solomon encoding
typically we choose a nice domain and to
show that we are not going to change the
those evaluations what we do is we build
a meracle tree to commit to those
evaluations and one thing that we need
to build this uh commitment schemes is
to have a way of showing that we
evaluated this polinomial correctly and
so here the main ingredient is a theorem
which is the remainder theorem that says
that if a polinomial evaluates to a
given value at a point then uh the
polinomial minus the value divided by x
minus Z should be a polinomial
okay and the idea is that we can commit
to this polinomial or this function by
evaluating over the domain and
committing to the marle tree and we
could show show that this is in fact a
polinomial just by giving the
coefficients but that wouldn't make
proof short we want logarithmically
short proofs so the idea is that we can
use the fry proximity test to do that
which has logarithmic size okay that is
something you'd like to to look when you
are trying to learn these proof
systems and uh well here is a basic idea
of fry but what you do basically is
divide the polinomial between even and
odd parts and then you do some random
folding to reduce the degree of the
polinomial by half this is the same
trick you use when you perform the
fft and uh here are the two phases of
fry you have a commitment where you
commit to the code words and then you
let the verifier choose some positions
where he wants to query and test whether
you are cheating or not okay and the
interesting thing is you get
logarithmically sized proofs and the
prover runs really really fast okay and
here there are like some cool things you
can do to have even faster things by
leveraging meren primes but you have to
move to a different construction which
is circle Starks okay it's more or less
the same as this but with some tricks uh
well and thank you for listening to
me happy to answer any
question thank you
Diego raise your hand if you have a
question and just to remind you this is
not just a throwboy it's a microphone as
well so please speak to it we can hear
you any hand
raised ah there's one uh you can
probably help me thanks
um oh there's a mic the microphone is
there all right fair fair enough um the
um the question is when you when you
actually do do these these hash based uh
uh proving systems and you do
aggregation because really it's it's
efficient you want to to keep your proes
really short but they're at the same
time you aggregate them up right or even
if you have different different improver
systems with different um commitment
schemes you still want to aggregate them
up to generate one proof right because
you don't want to shap around 10,000 or
way of these aggregation schemes like
lettuce FS that that you've encountered
well recently they released uh some
papers showing that you can use folding
schemes with Starks that could save you
the the work of having to do recursive
proof generation okay when you want to
link all these pieces of course with
performance cvms it should be easier to
perform recursion because you just use
the code written in Rust you execute it
on top of the VM and that way you handle
at least the first conversion to a stark
proof and then you can use uh Stark
recursion maybe using this idea of
folding and so I think that this will
greatly accelerate uh the development of
ckvm and the kind of things we can prove
using uh hash based uh proof
systems we see another question here
hi thanks Nikolai from terminal free
actually my question was very much
related but I'll still ask so these
folding systems in hash base proof
systems very much interested in that do
you know what's the concrete performance
of that now right now no because there
is no implementation this has been
released um a few weeks ago but I am
sure that uh either us or some teams
will start implementing because it can
offer some advantage in terms of uh
performance of course then uh we also
have to see whether these ideas can also
be easily extended to Binary fields and
that is also something really promising
because you can reduce a lot of the
overhead when you have to represent
variables okay the problem with CK is
that typically you have to represent
your native variables in in code like a
u32 or Boolean variables with finite
field elements and this in in general
are very very large compared to to the
variable you want to represent so that
adds some some overhead in memory and
performance we have time for a short
question okay thank you so much
thanks let's welcome our next speaker
Leo Leo is a member of the PSC he's been
working on a new language and ZK proof
compilers so today he will be talking
about a modern ZK proof kalalo let's
welcome
him hi so hi everyone so we are going to
talk about a project that we were
working on and and at at PSC that I mean
when we apply the when we apply for this
uh speaking about this the we were
working on this but now we have stopped
working on this so we are going to go
through what we were doing and the
reasons why we stopped working on this
so a little bit of of the retrospective
of a of a project let's
say uh so uh in I started working in
PSC was working on uh that was based on
H to kind of a plish arithmetization
and because it's is was very complicated
to to build something like that on top
of Hell 2 it's inevitable that you need
to abstract things so as a engineer I
found there like a a treasure trob of of
of really of really interesting
abstractions to be able to build the
ckvm on top of h 2 a lot of layers on
top of the hu to be able to to reason
about it and to kind of like yeah
abstract on it and and and build uh the
what we required and there like the
things like the stay machines no it it
seems like was like the right level of
abstraction to think about proving
computation on top of plish
arithmetization
and the the cell manager that was used
to kind of place things in a more
efficient way on the blish table and
also how to combine like composability
with something that was called the super
Circuit and Circ and this all this was
built when I started working here but I
started kind of learning uh learning
about it and I found like this idea that
these abstractions uh actually if they
are make in a accessible way uh could
make much more easy for the average
developer to to develop CK apps and that
something like this could help multiply
CK apps development and with that we
started
chikito first as a DSL in Rust then we
added a python frontend to make it even
simpler with the idea that developers
didn't need to even learn Ras they could
do it on Python and then after bringing
it to several hacker houses and working
with with Builders at experimental level
with with more information about how it
should be built we started kind of
creating our own front our own parer for
a language that kind of has a similar
syntax to circum but has State machines
and and more
things so in the end what we implemented
the steam machines that are the as the
kind of the definition like the
constrains of the transitions of State
machines are kind of the circuit and the
witness is the trace of a of a instance
of execution of these estate machines
and that's kind of like the main
abstraction at chikito and then with the
cell managers we abstract how that is
converted to the plish table and how the
the the witness is is arranged in
efficient way and can be is independent
so can be configured in different ways
to try different things then another
thing that we built is like arbitrary
Boolean Expressions compilation to
polinomial identities no so the the
constraints are expressed as polinomial
identities and and we build a system
that any Boolean expression as
complicated as necessary it will be
automatically compiled to to to this and
we kind of develop a a a mini theory
about how how to build this uh that can
be used in other languages like how to
compile any any Boolean expression into
polinomial identities then we also like
compilers has to optimize and through
optimization can get to better
performance that wow I'm going super
slow so yes we did more things and this
is how it looks the code and yeah you
can like for example here you can see
like arbitrary buen Expressions that are
compiled automatically to
constraints and we saw like it was super
easy and and users really quickly could
develop like complicated things like
Blake to Hash that in the ckvn we
couldn't Implement on top of h 2
normally with it and we we checked that
it has the same performance are manually
doing with h 2 and we found some things
that can be better and and then there
reasons to sunet it is basically ckvm
the race of ckvm make us reason that
that now we are in a kind of ckvm era
that the applications we want to build
now are probably better built by on CK
VMS and thank you for all the people
participating in different stages on on
Chito H PSC Engineers researchers and
and
grantees and yeah thank you very much
thanks Leo question time I have to I
have to accelerate a
lot any question oh there I'll go
closer I wanted to throw it you want to
throw you can do next okay it's okay hey
Lance yo what's up Leo um so question on
custom constraint systems I saw that
there was one of the um libraries that
you all use when it comes to ccs and ZK
VMS can you like are there any ZK VMS
that are implementing for that to go
from like plunk to
air but that would then be like a to go
from plunk to air that would be kind of
a easy translation I think like a not a
VM but uh from to be kind of easy
translation no because the difference
kind of how the rotations work in the
arithmetization so we we actually yeah
we we implemented the v as powder that
is kind of air so pow powder yeah one of
the yes the the ah I can show this like
yeah yeah yes so we impl back for powder
that is kind of air yes so yeah that's
is e plony and and and and and even CCS
we implemented the back in CCS
sonov um so yeah compiled to we we
didn't have time to check the the
performance on zob uh but but it it was
it was something that was compilable to
many different uh proven systems don't
really
cool I think there's a question here
yeah okay you want to
start who who this
oh hi thank you Nikolai from terminal 3
few questions actually first um can I um
verify your proof on chain like in B
verier now yeah and then you said you
made python but can I do r code and
compile it and because most of
cryptography is in Rust so rust is very
useful here and Let's do let's do these
two and then if you want okay okay so
you don't forget so the first question
on chain yes so we for for the CVM we
implemented a verifier in solidity for
the hell to proof so as long like it
depends on the proving system that you
use in the in the back end if it can be
verified on on because it's kind of
independent on the province system can
compile to different proving systems and
uh they generate different proofs so in
depend it depends on that and the second
question Ras is built on R chikito was
built on R and then we put like a par a
front end but yes you could interact and
connect it with other H hot to circuits
built on R and kind of actually
integrated together and another question
or okay we have one more question okay
there yeah better you throw it you want
to throw it again okay okay
last
opportunity too short so
bad uh so I actually not sure I
understand the difference between a ZK
VM and a ZK compiler like a ZK VM takes
your rust code transer like let's say
risk five instructions and proves that
okay yes so so so so the C so a ckvm is
one circuit
that it witness is the trace of the
execution of a instruction set so the
CBM is not a compiler it's a circuit
that takes as witness the the trace of
the execution and proves that you have
executed the the correctly the TR the
the program so so in that case you
compile Ras to this instruction
architecture and then H yeah you you
execute it and you get the trace and
that verify that compiler takes some
kind of
description of what your circuit that
and actually kind of outputs a circuit
itself so you could build a CVM on a DSL
in a
language I don't hear you
yeah so what what actually executes the
code like where what does the proof
proves if it doesn't prove correct
execution right with the compiler yeah
with a
compiler you generate a circuit that Pro
something about a witness so so a ckvm
is a type of circuit no is a is a is a
is a type of circuit that that proves
the execution of the trace of a specific
instruction
set but a circuit can prove any witness
like that follow certain properties
certain constraints in the case of the
ckvm the constraints are the correct
execution of the instruction
set happy I knew that question I knew
the
answer if they ask something
different I don't think we have time for
one more question but please feel free
to talk to Leo after his talk thank you
so much thank you
byebye next up we have uh pa pa is from
PSC as well he's a cryptography engineer
and uh he will give us an introduction
on postquantum um this is a bit tricky
postquantum signature scheme for
ethereum let's welcome
Pier
hi all right so a bit of context about
um why do we need postquantum signature
schemes for ethereum um so what canum
quantum computers do uh so you can think
about it as very good as quantum
computers at being very good at
exploring large search spaces which are
typically the kind of spaces in which
cryptography operates
in so there was a a researcher called
Peter Shaw that proposed one day an
algorithm that would uh solve the
discret log uh problem very
efficiently uh so the disc log problem
is one of the most fundamental problem
uh in the crypto in cryptography and he
showed a very efficient algorithm that
would break uh this kind of problem uh
very
efficiently um and um hashing however is
safe so there's there has quantum
computers can make some improvements at
it but we basically consider them to be
safe so it's really about
the ecdlp and things that use the ecdlp
and also pairings that will break
catastrophically so what does it mean
for ethereum and my goal here is just to
give you a bit of um an intuition of
what ethereum is faced with so here is a
bit the what it will look like for
ethereum in terms of constraints so the
consensus layer in ethereum uses some
aggregation scheme which um uh is BLS
signatures and what we would like to to
do for ethereum is basically to keep
some aggregation scheme uh because it
makes running a node um uh easy you
don't have too much Hardware
requirements so we would like to uh is
that does not require too much Hardware
from the node Runners and that will
still uh be post Quantum uh ready same
for the execution layer so so we would
like to have a postquantum scheme that
lets us keep the account based model
that we have on ethereum and yet
minimize the requirements that will be
made to wallet teams when we will uh
when we ask them uh when etherum will
ask them to to change to maybe change
the signature scheme that they
use so that's the that's the constraint
space that we have we want to to avoid
uh to have uh signature schemes that
impose too much of a load on nodes and
also we want some signature schemes that
make it possible to have a postquantum
secure execution layer where we can make
transactions um safely so what kind of
cryptographic objects do we have to do
that what what is the toolbox that is at
that is at our disposal to do
that so here what we want is we want a
cryptography that can run on our
everyday computers but can still remain
secure against adversaries that have
access to quantum computers basically
and so to do that we already have some
uh some answers so we have harh
functions as we saw before which are
safe we can say U we also have laes so
here laes are nice because they are
pretty fast when you want to generate
signatures but they generate pretty
large ones and we also have things like
isogenes which help us get small
signatures but are kind of slow are
getting faster and they don't have an
aggregation scheme yet but this is one
of the crypto some of the cryptography
tools that we can use to help make eum
postquantum safe and so I give some
examples here so there is the mod module
based um ltis signature scheme which is
a recent nist standard I think so here
you see it use laes you also have
winternet signatures which are hash
based and you have also you can also use
some stack based
aggregation technique uh with a post
postquantum resistance signature scheme
and you can see in all of those
proposals it's based on laes hashes
isogenes and you will see those things
come again and again and again in the
proposals that will be that will be made
for making for helping ethereum be
postquantum
secure so what's next uh so it's pretty
hard to predict when a quantum computer
is going to to come to come up and also
at what rate it's going to come up maybe
it's going to come up one day it's going
to pop up and we are going to be like oh
wow okay now we need to switch or maybe
it's going to come up um U slowly but
surely uh some think that quantum
computers are are not even physically
realizable recently there was a blog
post by Scott Aronson where he was
saying that basically would be very
surprised if quantum computers don't
come in the next 10 years and um this is
a probability density with pretty fat
tail so I think it's not it's not very
useful it's not very telling something
and there was a proposal by Justin Drake
that he was thinking about using Quantum
canaries so um um the idea of making a
puzzle that can only be broken by a
quantum computer so that if you break it
you get a lot of money but at least we
will know that when the puzal is broken
it will be the time to switch to some
postquantum uh schemes
you thank you
P question time do you want to throw it
yeah okay so I can I cannot do it with
my foot right I cannot I don't know can
I guess you can it's soft enough oh no
no I can't
okay thank you pretty good thr
um with nist approving just post Quantum
uh algorithms now for the first time do
you think that the NSA or the
governments in general know more already
about the state of uh quantum computers
available uh I have absolutely no
idea like there's there's no public
evidence of anything right that the
Chinese or the us or anyone would have I
would definitely lie on the paranoid
side but I have absolutely no idea yeah
okay next
question what makes lce is so well
suited to postquantum security I hear
them coming up a lot so
um it's it's just that they to you can
think of it as uh if you try to find the
key that you use in your scheme if if
you use lses uh quantum computers are
not at all efficient uh with this um so
the goal of cryptography in general is
to find very very hard problems and to
turn those problems into um schemes
basically and the problems that you have
with latices are uh very hard um and are
and at for which quantum computers are
not very good at so it's I think it's
it's hard to go into the mathematical
details first because I'm not very
familiar with them uh but also like in
in 10 seconds but basically um you can
think of it as a as a very hard problem
uh which is U still complex for quantum
computers to solve
yes and okay and what challenge is
ethereum current uh facing in adopting
the postc signature or what issues may
arise in this Pro
progress oh that's a good question uh
so so you have changes on the consensus
layer so for the clients that are that
are trying to reach the in the proof of
stake model that we have um you have
changes uh in terms also in the
execution layer so for all the
transaction approving logic um so I
think there will be uh engineering
challenges for instance does that mean
that we need to audit everything again
um do we need to make standards again um
so uh yeah yeah and also I think it
depends of of the timeline because if
one quantum computer pops up tomorrow
then uh the challenge to do it will be
much more pressing than than if we have
like a much larger timeline to think
about so it's it would also be an
engineering and human problem yes yeah
okay that's everything thank you
P our next speaker is Henry he is the
head of ecosystem from Star neck
Foundation today Henry is going to break
down star proof into simple blocks and
uh give you some high level ideas of how
they work welcome
Henry hello
hi everyone um welcome my name is Aro I
work at the star Foundation where I'm
the head of ecosystem and I'm going to
try to explain Stark proof like you're a
proof this is mine it's not perfect but
I hope you learn something so how I'm
going to go about it is the following
way I'm going to first explain quickly
what is proving what we're trying to
achieve I'm going to talk about
something that is called arithmetization
I'm going to talk about execution traces
and how they get used into proofs I'm
going to talk about error correction
code and I'm going to try to put
everything together so that you have a
clearer picture so first let's talk
about proving what is proving proving is
a person trying to execute a computer
code and trying to that person is called
the prover and he's trying to convince
the verifier that the execution happened
correctly without the verifier having to
reexecute
the computation now the kicker where
this gets interesting is that there's an
asymmetry between prover and verifier
and it's very efficient for the verifier
to verify rather than reexecute so we
Save A Lot on compute on the verifier
side that's what we're trying to do so
first now how do we do that we first use
one step that is called arithmetization
so arithmetization from a high level
perspective is the act of turning a
computation into
a set of pols that represent s
computation I'm not going to go too deep
into that but assume the following when
you use a computer you know that your
computer program can be turned into
logic that gets executed on transistors
and on zeros and ones you can get the
same result by having your competition
represented as polinomial and you when
you design a computer program that you
want to prove you have an expected
polinomial which is the polinomial where
every execution of your program will
have points falling on it okay now let's
talk about an execution Trace what is an
execution trace the execution Trace is
the equivalent of the stepbystep log of
you executing a program if you were
using a CPU for example it would be the
register of the list of all actions all
registers all CER all memory steps at
every single step of the execution of
your program so EX exting your program
is the sequence of all those specific
steps now what do we do with this
execution Trace when we run um when
you're trying to prove is we're turning
that execution Trace also into a
polinomial so you take all those data
points and you turn them into points and
you interpolate a polinomial that will
go through this execution Trace so now
you have two polinomial right you have
the expected polinomial the one that
defines the program trying to prove and
you have the executed polinomial which
represents the execution you just ran so
what do we do with that we apply
something on top of it that is called
error correction code error correction
code is something that is used in
telecommunication to transmit data and
verify its Integrity gives you two
property one you can detect error very
easily and two you can recover from
those errors but we're not trying to
recover from errors we're trying to
detect those so we're using those
techniques on those two pols to check if
the execution
polom is as close as possible or the
closest way possible to the expected
polinomial that's how error correction
code is used in Stark proof so now
wrapping it up what we're trying to do
is to convince the verifier that the
execution happened over the same
polinomial that the polinomial he was
expecting which was defining the
computer problem he was trying to solve
and with error correction code we're
just taking any tiny mistake that might
have happened somewhere and we're
amplifying it so instead of having to
check every point in the
execution the verifier can just take a
few points and then check using error
correction code whether there were there
was an error somewhere I hope that makes
sense and you learned something and
here's the actual explain
five explanation of Stark proofs Stark
proofs are 5 years old worst nightmare
when you're going to the swimming pool
and somebody tells you hey if you pee
it's going to turn red and everybody
will see it Stark proofs are the exact
same thing for computation if you try to
cheat at a single place it's going to
blow up everywhere and everybody will
see it and will know you're a cheater
and you're not going to be able to
convince the verifier that you U did
your computation correctly voila thank
you
you thank you Harry we should probably
invent something that makes your P turns
red in the pool right any
question ah there's one I'll do this
one um how do ER correcting codes and
polinomial commitment schemes
differ um I'm not entirely sure I can uh
answer this question I don't know enough
about it I'm
sorry oh I see another hand here this
lady by the way thank you so much for
the ei5 um want to really understand bit
more when you say you take a few points
out at the ECC stage you take a few
points and amplify it is that to WR to
understand it as a statistical
probability that it might have an error
that you cannot Det ATT because the
sampling wasn't done you know to capture
those points or is that just we should
feel comfortable believing that as long
as it passes it is error free I'm not
sure I understand your question but I
think what you're saying is is there uh
like sampling depending on how much
samples you're taking you have a
different level of certainty yes that's
actually the case when you're taking
samples you're going to see error with a
probability and the more sample you take
the lower the probability of you
catching a of not catching an error
is all
right any other questions for
Henry oh there's one
here uh Hey so do I understand properly
that this verifier need to have this
execution polinomial like
a like a sample that it needs to check
whether it's following the same steps
yes it does get a form of a it does get
some sample uh from the execution Trace
originally in proof there are like
protocols so that the verifier asks the
prover hey can I get this point can I
get this points and then he verifies a
few but using some fancy cry graphic
technique you can actually get away with
just giving the prover can get away with
giving a bunch of random points and
having the verifier just use them off
the bat
we take one more
question ah there's one
there uh if the approver can can select
the points to send to the verifier can
he select the points in such way that
the verifier won't be able to detect the
so the fancy cryptographic technique I
mentioned makes it so that he can't
select points that are comfortable for
him so um so then like he can't really
cheat
hopefully all right thank you everyone
uh I hope this was useful cheers thanks
Henry lots of inside from ZK proof well
sorry stock proof okay our next speaker
will be Alexandro he is a developer at
psse and he's going to tell us why
private voting is important and uh let's
Alexandra everyone um yeah let me just
see if this works cool it works yes so I
work at PC we do a lot of uh program py
uh cool stuff comes out to us we have a
boo there but yeah this is aming five
minutes and why priv what is
important uh just an agenda we'll talk
through what is Macy why do we need it
uh how it works and just look into the
future so Macy stands for minimal antic
collusion infrastructure and in a
nutshell is a protocol that allows to
run private on chain voting uh these are
some of the properties uh that we try to
push uh so collusion resistance uh is
increased because um there's only one
entity which can be certain of the
validity of the vote if that is trusted
then things get a little bit better than
other uh voting protocols uh you cannot
really prove how you vote it um because
um all the votes are encrypted you can
also um you can edit a vote by newly
find it but whatever is set on chain
must be processed and even if we talk
about this um trusted entity coordinator
even if they are malicious they cannot
really uh produce any false output of
the um votes so why do we need this
uh I mean I think you know boting is a
very uh sensible topic um briber in
collusions happens everywhere and I
think something that people a lot of
people find very close to and it's great
to work on this for that reason uh but
yeah like let's take an example like qu
funding or voting uh where more people
coming together can actually make a
difference but if it's easy to collude
then um the results can be gained and
also think like if you know how people
vote then you can also be conditioned
like there some people just don't want
to spend some time uh going through U
the candidates or whatever you're voting
for and you see like a famous person oh
cool I voted for this why don't I just
do it but if you don't really know they
cannot prove to you that that's actual
their valid vote then you could just
maybe think for yourself um and yeah and
then briber is reduced because it's hard
to prove and it's hard to collude and
our goal is to make um voting more
democra itic and
fair so in a Nell the architecture the
smart contracts that work on any EPM
chain uh there's some circum circuits
that can be used are used to prove that
all the votes sent are valid or invalid
and the tally circuit which T all the
vote so this around by's trusted entity
the coordinator and all the results supp
posted on change for everyone to verify
um yeah there's some sdks and tiet stuff
if people want to integrate it hopefully
you do and yeah how does it work as a
user flow you come and register into the
platform you register with your Macy key
which is not to be confused with your
ethereum key um you can just prove
you're human prove you on to pass ticket
and then you register into the system
then you can send encrypted votes the
only the coordinator is able to the
Crypt and you also sign them with this
AC private key so no one else can send
votes on your behalf and then as a user
after the coordinator process everything
you want to verify that everything was
done
correctly um the votes are encrypted
using a CDA so there say share key
between you and a coordinator it sign
and in the vote you specify um who
you're voting for whether it's like a
you know yes or no Vote or like you give
some sort of weight in contr voting and
yeah that's encrypted send on chain uh
fully encrypted and you also send a
public key that you used to generate a
share key so the coordinator can just
reverse the
process uh to finalize the coordinator
just takes all of the uh votes and just
all the events from these uh smart
contracts and then just generat uh the
CK proofs using the circus that we
talked about and they'll just post them
on chain uh they cannot censor any vote
they cannot uh prove something that is
not happen so that's some of the cool
stuff about it and yeah looking into the
future um
what we try to do is to make it easier
for people to use and actually get
someone to use it um some of the
research topics that we have plan is to
actually decentralize this coordinator
figure using NPC and try and make it
even more harder to collude um there
might be some um time to also look into
new voting mechanisms or like funding
mechanism they could be integrated and
maybe we'll also be thinking how to re
just reink the architecture and kind of
integrated with a lot of other PSC
protocol like sem4 RNR and
exia okay so we are running a Devcon QV
round there's like
so you can go and vote you can try Macy
you just need to prove your attendee by
um using zpas this is what it looks like
just try it out just be gentle cuz uh
yeah just be gentle with this up don't
break it please but yeah uh that's just
showcase how Macy work and um yeah
that's it five
minutes thank you
Alexandro
questions do you want to try this one
for me
thanks sorry
dude um you mentioned at one point that
uh there was a proof of humanity
required for the voting uh how do we
achieve that without relying on a
centralized entity and also how do you
protect against civil attacks in your
voting chain yeah that's a good question
so to prevent civil attacks we have this
concept of Gaye Keepers um so you need
to prove that's fully customizable so
whoever runs the vote will say hey I'm
only accepting someone that approves is
a death con so by scanning a ticket or
like own something uh like an nftd and
other other things so that's how you
protect against cbles so Mac is always
good as a Cil solution that you decide
to use and for the trusted assumption is
that this coordinated figure uh could be
remove with the NPC so you have uh like
a collaborative snark I mean I'm not
really going into this stuff so uh and a
high level just like instead of having
one coordinator you'd have multiple and
there might be some sort of con
consensus some sort of way of
um you say to make it hard for them to
also uh not post the results and not
collude between themselves but yeah
that's probably where we're going and
some smart people in PC that already
thought how MA will look with MPC so
hopefully we'll be able to implement
that very
soon I think we have a question at the
back
there in the beginning uh the ISAT I oh
uh receipt freeness of the vote yeah and
that it's impossible to show uh who you
voted for MH um but what if the user
would simply share their private keys
and then reveal everything that they did
they would still be able to prove the
vote in that situation yeah that's a
good point um so the thing is like when
you cast the vote you can NY it so you
know I show you hey I vot for this but
then you couldn't trust me that I
actually did unless the coordinator
colludes with this other entity and yeah
one of the uh other issues is if you
give out your key then they they will be
able to like post votes on your behalf
so like it's it's up to the user to not
sell the key um yeah that would you know
that would kind of mess up with the
system as well and hopefully we'll be
able to find some some good solution for
that um
yeah I think there's a system called
something something with bear vote like
the animal that has a property like uh
you need an additional salt to uh to
prove that it was actually you and if
you provide a wrong salt in the proving
process uh it's the result comes off of
somebody's else's
word okay I'm not familiar with this to
be honest but um yeah if you just hit me
up later and just describe this i' be
interesting to talk about
any other
questions yeah H I have some question
there there is any possibility you have
a credential for get quartin voting
about H your knowledge for example you
know computer science and there is a
proposal for some upgrade in the system
there is any possibility to do up this
so like to automate like some sort of
execution after the tal is prod use uh
yeah the proposal is made H you get a
vot and the calculation of what your
knowledge is to the quadratic voting and
then there some sort of action that
happens after like do we mean like in
let's say Dow governance or something
yeah yeah okay uh that's not something
we explore yet that governance actually
talk a lot of people about it today so
um yeah that that's still possible
because the tally is posted on chain so
they can be automated as a hook after
the tally is fully proved prooved on
chain as the data something can happen
that's totally doable yeah yeah thank
you okay thank you Alexandro let's give
him a big
Applause let's keep the energy going and
the next lightening talk will be from
Andy Andy is the product manager and
also project coordinator from PSC and
his Talk's topic is the blind men's
elephant let's find out what's going on
hey hey
hello so I know many people here uh work
multiplying matrices and like doing a
lot of polinomial day in day out uh but
I think my talk is going to be a little
higher level on like how programmable
cryptography can solve one of the I
would say most important use cases for
our space and and in general like uh
society which is like private identities
and this product Vision it will be more
like a high level overview about what
characteristics do we want and some sort
of approaches that we have been seeing
in the space um yeah trying to solve
these these issues so as we are in
Thailand I thought it was great to start
with an analogy of this blind man uh
elephant illustration because this is
the land of the white elephants um I
think with people who are inside the
identity space we kind of like see a lot
of acronyms throw everywhere like d a b
SSI um and those are these idea like
selfs serign identities verifiable
credential decentralized identities
those are all useful and have nuances
but at the end it has some core
properties which I want to like explore
in this
talk I'll say these are the properties
that we care um and probably we can grow
the list even more and we can even make
um security assumptions models to
understand how like in which sense these
properties we want to achieve want a
flexibility we want to verify a ility we
want privacy we want decentralization
self ownership transfers ship etc etc
etc but I would say if I were to sum it
up to like the core core properties that
we really want to key achieve with this
are um basically three actions that I
think we should uh pursue and target
with programmable cryptography in this
identity
space first H and and the ones bolded
are things that a user will typically do
in order to leverage private identities
one is the capacity to import all my
identities and data into something a
container um let's call it a wallet for
now the other one is to generate proofs
or generate an artifact that then I can
take and then uh prove an identity and
attribute something about myself so that
I can execute an action so my proof is
being useful elsewhere so if we were to
summarize like all the complexity that
we have in these three kind of like
steps and actions it turns out that it's
uh a bit easier to reason about like
like what type of like cryptography
systems and targets we want to achieve
with programmable cryptography in uh
identity so the first section is let's
import all let's import all my
identities my data uh and what does that
mean it means that for all the documents
and data that exists in the world in the
digital space anything that is signed we
should and want to Target it to bring it
to private identities um cryptography
use cases and that means VI things like
your National idid card your passport
there are great teams um in here
targeting that but also driver licenses
sign documents PDFs credit card
transactions maybe we can like Leverage
from WhatsApp telegram over reputation
social graphs Spotify history there's
all this signed data that I think we
need to hijack and literally start
adding into all of these containers that
it can be called it can have very
different names and we need to do that
permissionless that means without asking
the national government to allow us to
do that we need to do that privately
without them realizing that because
maybe you want to use it for things that
the government doesn't approve or the
Spotify or whoever and we want to make
that data
verifiable that's why CK and PCF and
other programmable cryptography
Technologies are so good and we need to
achieve like a web two user experience
in order for this to be useful and get
adoption and that means technically that
we have a lot of challenges that we need
to support a lot of hash mechanisms a
lot of signature schemes a lot of dat
structures uh standards uh that means
that we need to invent new things like
not only wrap things into CK but also
like 2pc and NPC a proxies and have like
wallet like experiences if we really
want to achieve this property the other
one is proof facts about them and if we
want to have a great user experience
then we need to generate proofs in
useful ways doing selective disclosure
in things like less than one second in
targets where our users are going to be
and that means browser in your laptop
but also browser in your phone and also
means native phone like apps um and that
means mobile s mo mobile side proven or
client side proven is extremely
important which not every programmable
cryptography project is is is targeting
and it needs to be very cheap or even
free it needs to be very easy for me as
a non-technical user to leverage my data
and import it and generate facts about
it whenever a website or a platform
queries and I respond to that the other
one yeah technically this mean Wason
mobile proving small Ram uh memory uh
Resort like low bandwidth environments
uh that means leveraging techniques like
proof aggregation recursion folding
different verification layers things
exploring things like Co sarks in order
to do delegate proving exploring things
like proof composition like I don't know
client side proving with with one
proving system like Spartan then
aggregating on a ckvm and then like
proving unchain with gr 16 those are
kind of like the solutions that were
seeing because we want to have cheap
fast composable proofs of our
data and lastly we want to basically do
very useful actions with that and the
most obvious candidates are voting
forums chats um Etc but there are things
that are popping up like yeah data
syndicates or data marketplaces where a
lot of people can just add up their data
and then make um charge basically to do
statistic analysis on that private
anonymized data we can do reimbursements
compliance stuff uh a lot of ux on web 3
like multi6 account recovery social
recovery are needed like need identity
so I think that's where our Solutions in
this space are going to be extremely
important humanitarian cases anti-il
Etc so yeah basically we need to be able
to do useful actions and one of the
biggest I'll say challenges is like
nullifiers and the nullifiers is like a
strong problem I just listed um
different approaches and levels of LOL
fires where the government basically no
nul fire that's the worst case and best
case is like yeah not even the
government trying to collude will be
able to you know see that you sign up
for a really controversial uh
service so yeah for last things uh in
this needs to be secure post Quantum is
like a must have now because like in
five years you're doing voting and it
gets like uh captured the data and then
uh decrypted later it could be a problem
for you it needs to be interoperable no
Bender lock in it needs to be movable
from wallet to wallet it needs to
support key rotations live checks etc
etc so these are some properties that we
want to achieve and I think we all in
this space are trying to actively work
on so to finalize I think the three key
messages that I want you to take is like
first let's hijack everything let's take
all the data of identity sources and dty
sources and try to Bing um to our use
case onchain or offchain let's try to
discover novel use cases like different
interactions that we can unlock with
this new data Providence um things and
now let's build uh new Lego blocks to
build a better future
thanks thank you
Andy there's a question
there oh I did pretty well thank you
good throw
yeah um so question um great great to
see the product perspective for once and
I really like the threee fre stage
components and um product deals with
human nature right so
human nature usually runs on incentives
so if I give an example for the
government the government gives you the
right to drive a car so you have to get
a driver license therefore you have to
get an identity yes so it usually goes
backwards right from 3 to one so I was
wondering what are the cases that you've
seen that the incentive is so big that
you would then go and find an identity
Source um because if you want to use
this as a as an actual identity that
people use they usually don't start with
wow this is so private and has like
encrypted proof and hashes and
everything yeah so I was wondering what
what do you see that uh that has kind of
grass roots in in in reality when can it
can really brings the masses back to the
to the platform to platforms like this
okay I think that's a great question
what I understood is like what are
places where we will search for
identities or data where people are
already there I would say like yeah I
start with where are people there like
it's very hard for us to request
everyone to sign up to a system but it
will be way better if we just say like
yeah all people are interested in
driving a car in these locations let's
just use that as a like source of
starting point to bring their identity
on chain and to do actions onchain and
to do like voting and etc etc
um so yeah like I don't know like
anything that that you sign up that has
a digital signature I think it would be
great to just hijack it and the more
people use it the more common they are
are the more used to they are like face
ID Touch ID all the the secure enclaves
I think they're great to to to start to
do
that just just to follow on that
um like the way I approach it just uh
just to say it in a couple words we we
have a company called Grappa and um we
use reputation basically so we're saying
you want to prove your reputation going
to say that you did something in life
you want to have some kind of a um
attestation from somebody else that you
are not worthy in something that usually
a start for an identity that usually I
want to prove this to the world I start
with that that starts to be kind of the
seed of my identity and then I cannot
forgo that yeah right yeah no great use
case
right so one question there okay I saw
on your slide uh verifiable oblivious
pseudo random functions yes uh what the
uh what where do you see it fitting in
yes that's a technique that a couple of
teams in the identity space are
exploring I think it's great that they
didn't get to all the technical details
but we basically a network like MPC of
nodes and basically how it does is like
it calculates the salt with this like in
an MPC fashion that is deterministic but
no any no node by themselves can
calculate that Sal for you so I think
this solves two really important
problems one is like using your private
data and this Soul generation process
which is deterministic you can recover
your account or you can recover your
identity even if you lose your phone or
like your cash data the other one is
that
um yeah just like way way better user
experience and oh the other one was that
no government can calculate that unless
yeah they tap into that these these
process type uh like private data so and
we can make these like very Uh custom so
like yeah you can choose like private
data that only you know in your head
plus like private data that I don't know
it's very filed in a credential so yeah
in short very strong for for nullifiers
and uh yeah anti-is Discovery
mechanisms any more questions for
Andy okay thank you so much thank
you our next lightening talk will be
given by two speakers so the first one
Kevin he is from psse he's a software
engineer and the second speaker is uh
John I believe he's a computer science
alumni from Columbia University and
today they're going to talk about a
framework called MPC stats so it allows
users to query statistical computations
without leaking any privacy let's
them yeah
hello everyone so um we're NPC stat team
at PSC so today we'll introduce our
project and it's currently work on by
Jour by Jour and I and
kazum yeah so the goal of our project is
to build a framework that allows users
to quer statistical computation across
different data providers well guarant
the data Prov privacy and also the
correctness of the
result with implemented um common
statistical operations using MP speeds
which is a well welln NPC
framework we've supported 12 statis
statistical operations and also some
common table join and array conc
concatenation and filtering
so um users can Define computation like
this and we also integrated TRS notary
so that the inputs to MPC are
authenticated from some well-known
websites so that we can prevent garbage
in garbage out
situation all right thank you Kevin so
basically right now we are talking about
NPC right so intuitive approach for NPC
is that having all parties data
providers data consumers to join as a
computation parties right the bad things
the I mean the good thing for us let's
say is that it's really verifiability
because everyone is in the same like
computation set right so they know like
what computation is done right I request
mean I know that this guy just compute
mean for me right the bad thing is that
the data providers consumers everyone
need to be online at the same time and
it's really hard right for many numbers
of data providers especially when the
number of data providers grows the
computations grow Skyrocket so badly so
how how to solve that right we use
another approach called client interface
which basically means that the data
providers and data consumers are not in
the computation parties so there's three
phase the first phase is that data
provider secret share the data through
some delivery thingss they can lock in
share data and log out and then another
set of computation parties compute data
and once it's ready data consumer just
loog in to get it out so this is good
because they now the data provider and
consumer doesn't need to be online at
the same time which makes sense and it
also doesn't grow with the number of
data provider because the cost of the
MPC computation is actually from the
number of the parties in the computation
parties the bad thing is that the data
providers and consumer now need to trust
the parties right it depends on our
setup is it malicious we need to trust
at least one of the party is right and
again because we are not joining in the
MPC competition party itself we have no
idea like what is the function that they
calculate is actually the one we want
but again the trust Asam is the same
that if you trust that at least one for
the Malaysia sitting right the
computation parties honest we can be
sure that they just run the computation
that we want like mean or median or
anything we want so use case we are
thinking about cross departments data
sharing government verifiable salary
data any survey research for policy
planning and yeah many more let us know
so demo time so this is C up and running
we still under maintenance the final
optimization because it's pretty big so
we will notify soon but it's pretty
interesting to explore e balance INE
equality at Defcon so what it means like
you guys can use your binance to share
it privately we won't know your binance
balance but then we will be able to
calculate the interesting stat we will
show later but you guys should join this
group first so we will notify by today
or tomorrow once the docker file is
smaller so that it can make sense to run
in this like internet in Defcon so the C
right because we want to be up front so
we will only allow you to share share
like privately the free eat in your spot
balance of bance and again the parties
who still learn a number of digits
although this is comes from the the
limitation of the the is not itself that
the Pary still know like the number of
digits of your binance balance but again
we won't know actually the number and
again this is the trust assumption that
we trust that our three party doesn't
collude right and yeah please please
join this telegram group we will get up
soon and anyone who join will get a
chance to win an nft and win a lottery
as a actual cash so yeah so this is just
to Quick go through it will already be
in our read me in our demo so get
binance API key just go your binance API
key everyone know how to do that get the
API key and secret key make sure it's
read only and then yes so noes this is
only our script that you need to run you
just get clone and you run and make sure
that your Docker is opening and running
on your laptop and then yeah you just
run this again this is just one line and
each address is just address for
receiving the price this is not not the
address for the binance this is just for
to send the price if you want one and
yeah this is the website so we are
having Max E balance of Devcon mean
median number and Genie Co to make sure
of the inequality so yeah Joy us thank
you so
much thank you Kevin
John any
questions oh that's too far okay you got
it uh hey uh great talk um it's not
clear to me are you guys trying to
collect like aggregate statistics from
like multiple parties and if that's the
case and that's use case um did you
explore something like a prio like M
like system you know using like function
secret sharing uh I don't think MP speed
support that so I'm kind of curious it
should be much much more
efficient yeah thank you so much for
suggestion yeah I think we look at
through some of it but this limitation
mostly is through the number of data
providers so right now again like f
multi key functional encryption secret
trying uh yeah we look through some of
them and we're thinking of using some
but again the limitation right now is
that the state of are MPC of a huge
number of data provider it still matters
and we think again because we make sure
right that we don't want the competition
to just grow indefinitely with the
number of data provider so we still
choose this but thank you so much for
for yeah yeah yeah so just look at
function secret sharing I think it would
really really boost your result thank
thank you I appreciate function secret
sharing
note do we have any other
questions oh there's one
hi I was trying to scan the the TG um QR
code that you showed just now and it
says link expired for me uh is it just
t.me MPC stats that's a link uh yes yes
okay sorry about this so t.
me/ mppc
stats any other
question can I ask a question um I know
that the the Federated rate um Federated
learning is similar to you know
preserving privacy and then the
medical hospitals they're having a lot
of um you know confidential data of the
patients so they use Federated learning
I just wonder what you're presenting how
different it it is from Federated
learning Yeah so basically Federated
learning is like you trains offline
right like they T do that and then you
send the update on the gradient descent
or anything to your machine learning up
in the air right so basically you train
everything up there but now MPC it means
that you train you gather data from
different parties and compute at the
same time so for Federate ring so it can
use actually it depends on what types of
thing you use but it can also use MPC
itself so but yeah when it comes to F
running people still consider like not
too many parties or advance but when we
thinking about stats we thinking about
like population so we wish to make it
more scalable in term of like number of
data providers itself but but yes I
think a lot of Federate learning
techniques to use MPC but we just want
to make sure that MPC framework that
really scalable to a huge number of data
providers yes okay thank
you okay uh thank you very much Kevin
John our next talk is from viven Vivien
is a computer scientist from psse she'll
be talking about privacy preserving
group let's welcome her
hello everyone my name is Vian Placencia
and I'm a software engineer in the
privacy and scale expirations team at
the the foundation and today I will be
talking about privacy preserving groups
privacy preserving groups are groups H
where the
Identity or the actions of the members
is private there are a lot of use cases
for this type of groups and one of them
is everything related to Anonymous
interactions like Anonymous feedback
Anonymous voting there is also an
interesting use case related to Pro H to
proof that you own a credential so there
are a lot of credentials that take time
to H prove and verify so something that
you can do is to H ask people to verify
the credential ones and then add them to
a group and then they can just every
time they want to prove the cred they
just have to prove that they are member
of that group and that's a cool use case
of these type of groups because you can
keep
privacy H we cannot talk about groups
without talking about anti-il mechanisms
so there are a lot of ways to use
anti-il mechanisms for your groups and
an anti-il mechanism is a method to
prevent fake or duplicate identities in
your group and something interesting
that you can do for to have a stronger
civil mechanism is to combine H many
anti civil mechanisms using logical
operators so that H is you have like a
stronger anti-il for your for your
group there are a lot of examples of
anti-il mechanism so one of I will
mention a a few one of them can be like
invite codes you can send people an
invite code and they can join a group
and another can be like social media
information like GitHub follower
or personal stars and also a spec number
of comments on a specific repository
also twiter followers H or if you follow
a specific user those can be anti-il
mechanisms uh from web too and there are
also anti mechanism that we can get from
blockchain information like your account
balance the number of transactions
and the identity Protocols are also a
nice way to have anti-il mechanism for
your groups example of this is a an Anar
and also open passport there are a lot
of other protocols that are really cool
H anti-il mechanism like e attestation
service TL notary and pop so some
projects can be can work can be useful
for privacy preserving groups and also
for anti civil mechanisms one one of
these is semaphor H this is for groups
Anonymous interaction but it's
useful
for if you are part of a group then you
can be added to another group just if
you are part of another different group
so also supas which is a project that we
are using here it has groups and also
can be used as an anti civil mechanism
and bandala which is an infrastructure
to manage privacy preserving groups and
it also have a lot of credentials and
and C kit which is a a set of libraries
and and algorithms so that's also has
groups and can be used for anti-il too
so the three main ideas H from this
presentation that I would like you to
remember are like privacy preserving
groups can be used H to verify
credentials H to have a better user
experience in your applications also
that you can combine a different anti-il
mechanisms to have a stronger one H
that's H very important is maybe it's
not not your case but H for your
application but it can be the case for
some other applications and some
projects can
also H be used as anti civil mechanism
they were not created for that but they
are really useful as an anti civil
mechanism so that's the third point so
thank you very much and yeah I will be
around feel free to ask me any questions
about this topics thank you thank you
Vivian we have some time for question
hi hi Vivian I've used bandada before um
I I just find it difficult to understand
like uh this works in with IDs right uh
you get a group ID and uh users IDs so
how do I use this group IDs or or what
what happens after I get one of these
groups set up yes h
bandal is compatible with semor so you
can use the SEMA for identity package uh
to have the SEMA for identities and you
can add this the commitment to a bandala
group and then you can work with that
group and it's also since it's
compatible with semaphor you can do
Anonymous H things with yeah the members
in your
group any other
questions it's over there
I see some people wearing the miror cat
hat but unfortunately we're doing the
rolling the ball of
throwing yeah please so quick question
so are there any like practical way to
forcefully remove someone from a group
so I understand that like it's kind of
easy to verify someone and try to add a
group right but I mean as the group have
run and there might be a reason to
remove someone forcefully then any
practical way to do that yeah yeah there
is a if you want to do it with code
there are functions for that if you want
to use it if in case of H application
for example bandala you can use do it
directly the dashboard yeah there is a
way an easy way if you are using Code or
not yeah uh can you explain the mechanic
behind like how can you like maintain
privacy everyone and also kind of can
specifically remove
someone yeah ER in the group you will
have identity commitments which is like
the it's like a public key like a your
account that is public and you you have
a private value so the commitment can be
public and commitment are not attached
to to to the identity of the real person
so so H you can I mean the the person
it's a commitment so people don't know
like who is that commitment okay thank
do we have other questions for Vian
there's one question
here um a lot of these privacy groups
are opt-in privacy group uh privacy
groups is there any opt out privacy
groups as well that you guys have looked
into that you mean like if you can be
you can if you want to be out of the
group you can do it but yeah like by
default everybody there admin and the
admin can H remove people so
yeah I don't have any
question
okay thank you
Vivian thank
you our next talk is also going to be
about uh s Sam 4 V4 so let's welcome our
next speaker sidu he's going to show us
some new features of s for V4 and some
of the importance um of the ZK
technology let's welcome
him
hi so hi folks uh I will start start
introducing myself and then I'll present
uh some news regarding semop for and our
future
plans so I'm Cedar I work as a software
engineer with the PC team and in the
past years I have mainly focused on
improving the developer experience of
some PSU
projects I'm talking um about what semop
for is sem for V so some news and then
our road map
so first of all semor as as far as I
know is one of the simplest client side
zeron protocols so the core cirquit only
contains 22 lines of code without
documentation and like empty lines
generating approv only takes less than
one second on browsers and veryify a f
chain only consumes less than
around 5 cents on
arbit but what is it so semop for is a
zero knowledge protocol that allow users
to prove their membership in a group and
send messages such as votes or feedback
without revealing their
identity in addition it also provides an
alfier mechanism to prevent user from
reusing existing proofs so sema4 is
basically a general parpose protocol so
you can use it for any use case where
you need a layer of
privacy we have been working on semop
for for a few years now and we have
mainly focused on on developer
experience until V3 but with the latest
version V4 we also focused on
interoperability and efficiency and
onchain costs in particular we um have
made two important Chang we have a new
identity schema which uses eddsa D EDSA
keare and we have optimized the data
structure for
grips so let's go a little bit deeper
replace the hold identity schema um with
an eddsa keeper EDSA is one of the most
efficient public key cryptography
algorithms using Zer circuits and it
makes the new version of spa for much
more compatible with other existing
protocols which use
EDSA in the old schema the public
commitment which is like the public
identifier of the semur identity was a
posidon hash of a secret in the new
schema the public commit commitment is
the posidon hash of the EDSA publicy
and in addition um it also allows user
to sign messages and verify signatures
inside and outside ziky proofs or
Secrets which has been and will be
hopefully pretty useful for some
applications like Zupas which uses sem 4
before so then we optimized the old data
structure the incremental Miracle Tre
and we created a new data structure
which is based on the old one the lean
incremental mirle Tre um so just small
improvements that that made it much more
efficient especially when the tree
doesn't have many leaves so for small
groups the key improvements are two zero
ashes are no longer required and the
tree grows dynamically
now so zero hashes um I just want to
show like the difference between these
two threes uh in the old implementation
if the parent node as one child it will
be calculated as the hash of that child
node and the zero hash in the new
implementation on the right um the
parent node can actually equal the no
the child node itself so no need to
calculate any H in those
cases the second important change is
about the dynamic depth in the old
implementation the tree has a static dep
each insertion needs to update a number
of nodes which equals the static dep of
the tree and in the new implementation
the tree um the three depth grows with
the number of leaves which means each
insect
would only require updating a number of
nodes proportional to the current number
of
leaves so this is quite complex so
please if you want to know more about
this data structure uh go to the um
paper we published a few months ago in
the zikit repository
below finally uh what we would like to
to do in the next months we will like to
have a new Explorer which people can use
to see on chain groups and um we which
admins can use to create and manage
groups we would like to work on a new
version of rln uh which is pretty
similar to semaphor they share the same
code but Ern Works um with an additional
layer to prevent spam we would like to
add additional tutorials to the
documentation and possibly uh have like
specifications for SEMA for before
something that people asked us a lot of
times uh we will also explore and
consider new improving systems of course
and try to keep ourselves updated on the
latest
um Technologies to improve the key
requirements of the
protocol so some links you can use to
connect and ask us any questions um yeah
thank you very
much thank you
sidor any questions oh there's one there
do you want to give it a go it's on your
side
hello test thank you for your speech it
was good I'm just curious to know more
about semi for's business model the teex
sounds amazing but I'm curious is there
a way to generate a profit from this no
I mean we are funded by the TM
foundation and um we are not thinking
about any way to make profit okay thank
you I think we're also not allowed to
speak about profits just from what I
heard okay thank you
okay hi uh I was
wondering to upgrade or migrate from
previous version does that mean like
preexisting project need to generate new
identities yes yeah you need to generate
a new identity and one way is to derive
the secret for of the new identity of
like the semor V before from the
identity of sem for with3 so using the
same secret and deriving the private key
from the previous Secret
I have a question for the how the
protocol Works do all the notes need to
be online at the same time where are you
I oh sorry okay hi do do all the notes
who want to take part in this protocol
need need to be online at the same time
or is it possible to establish the group
without um all the participants seeing
the other participant at any point in
time
can you repeat your question sorry about
it's about the liveness of the
participants yeah so can we establish a
semap for based communication for
example um even if some of the notes are
only online for a certain short period
of time or do they all have to be online
at the same time to calculate these
secrets uh yes they have to be online
yes on chain at the same time okay thank
questions oh we have one at the front
row
here hi what are the advantages of using
the the lean IMT um now data structure
for like um Dynamic the depth of the
tree uh I think one advantage Advantage
is that with the old static um with the
old incremental Merle Tre with sted dep
um we had a range of redep supported
reeps from 16 to 32 and even if the
group is small like with 10 members you
had to use um a Merle 3 with a static
dep which was like 16 so bigger storage
then yes for storage and like the the
generation of the grou as well needs
more time because the circuits has more
constraints okay thank you
yeah okay we still have some time for
questions if you have
any no okay thank you sidor thanks for
sharing with us SE for
V4 and coming up next will be our last
lightening Talk of the first part we
have three parts remember I I talked
about it at the beginning so the last of
the first part will uh we will have two
speakers uh we will have yaan and moven
from psse and they will be talking about
mpro uh and they will tell you how to
use mopo to develop your ZK proof on
mobile and make mobile development
easier let's welcome them
hi Sika I'm yawan or Vivian and his
moving and we are going to talk about M
Pro to make U mobile cide proving
easy so without that there are more and
more mobile users than uh compared to
desktop users because because of the
accessibility and portability of mobile
and then there are many powerful
features in Native mobile for example
the performance is better than browser
and it can access to uh hardare devices
like camera
GPS biometric and also the uh offline
functionality and push notifications are
also interesting features in Native
mobile and last but not least the mobile
development lacks infrastructure for ZK
applications so our goal of mpro is to
improve the mobile developer experience
so we provide ffi CLI and provide
templates and documentations and we want
to improve the native mobile performance
to generate like ZK proof and
cryptography
proofs and also we want to build a
mobile development ecosystem as complete
as the web app ecosystem so we want to
build packages for mobile developers and
also build good communities for those
who want to build mobile
apps yeah so our role map is to adapt uh
in integrate as more as adapters as
possible for example ZK and hu and
folding system and pcfg in the future
and we will generate the bindings for
different platforms not only iOS Android
but also for website and gamings and
also your
desktops yeah so we can look on
look detail in this structure we are now
in the middleware of the m in the
middleware but we we we need to
coordinate the back end the proving
system GPU acceleration and the front
end is the like SDK for different
protocols yeah so how to use M Pro we uh
provide a CLI for developers to easily
use m innit m mop create to create a iOS
or Android templates and then you can
easily getting started with the the app
so The Benchmark on mobile it can be uh
speed out up to like six times faster
than sjs on the Mac but the disadvantage
of mobile is that the memory is uh is a
short is is really uh few so we need to
solve this problems and this uh The
Benchmark of CPU and we will introduce
the GPU research results okay um so
we've been researching on uh GPU
acceleration on client side proving for
a while and what we found is that uh
client side proving is a completely
different story from server side GPU so
we want to highlight two things the
first is uh scalability so if you look
at the right hand side table uh you can
see that although there is like uh 9x
capacity of serers side GPU
uh it seems not that much but uh the
point is it can be cluster thousand
hundreds of thousands of GPU to do
extremely fast computations so on the
other hand the uh mobile GPU is just the
one sit on your phone so it's relatively
limited and the second thing we want to
say is that the ecosystem support of the
shading language which is where we do
programming on GPU is uh really
different so uh Cuda is what one of the
most mature uh GPU shading e ecosystem
right now so if you want to do
development on Cuda it's much more
easier than metal which is one we do uh
GPU acceleration on your iPhone yeah so
uh we target MSM to accelerate because
it incompass 70% of the proving time in
like gr 16 so uh the first thing is that
we found that a current CPU
implementation is much more faster than
GPU one in the Z prise 2023 winners and
the second thing is that uh although the
GPU is uh much more slow uh slower in
this case but when the inant size grows
uh the uh GPU has the potential to shine
in larger instance size yeah so f
takeway is that we still have so many
things to under exploration so a better
El library or making much more memory
efficient for mobile
and we want to also want to leverage all
of the Computing resource on mobile
device and make sure the GPU and CP uh
CPU synchronize in a way that maximize
the computation speed yeah so like GPU
is a totally different story and we want
to explore
more yeah so here's the link to the
mopro resources and it includes a Google
form that you can we want to collect
feedback from uh ZK uh projects what
what you need for no mpro and there's
also a like giab link and telegram link
yeah feel free to scan this QR
code yeah so cop
cop thank you m and
yaan any
questions oh there's one over there you
guys want to give a
go
really I don't think I can
oh thank you
hello okay uh so I saw your uh
benchmarks so are the benchmarks
comparing the snark J on a browser or
against rapid snarks on like mobile
device like what's your performance
versus rapid snugs on mobile and gar on
mobile yeah so the snars on Mac is uh in
with CLI so I use like MPX snar fullprof
proof to generate the the proof and then
the Mac is uh M1 M1 Pro Max and the my
iPhone is the native app so it is uh
iPhone
or rap no no no no with with more Pro so
it's the native bitings okay yeah yeah
like the uh uh yeah so we use Rost and
then generate the bindings uh binaries
for
iOS and then we uh calculate the proof
with the
binaries so uh do you need any specific
DSL that you have to write your proofs
or like circums or like you are going to
integrate other dsls as well so the uh
actually we use the circum uh results
the Z key and Wason and then you can use
the these two key uh two two things in
uh M proo and then it will generate the
native Bings for you to generate the
proofs and then you can use it in the
native app native
app and then the for for example the the
iOS and then you will create also ffi
for Swift so I I can call like generate
second proof in Swift to generate this
proof thank you
questions oh there one over
there ah oh sounds
nice I just wonder about any like attemp
or um um um CH challenge for building
like AVX specified instructions because
when it comes to like looking at um um
the vector databases in in in add Fields
they're trying
to uh the for for fa its calculation by
implementing those uh the uh some
Transformer uh calculation you to embed
it into the CPU with using AVS
instructions um is there any like
attempt to doing a similar approaches
when it comes to doing um electric curve
acceleration for uh ZK stuff or kind of
things uh okay so can you say again uh
okay so I just know about um there's
some attempt to accelerate some um um do
product calculation or like Matrix
calculation to using on when it comes to
using a Transformer architecture for
accelerating each calculation using AVX
instructions which is to accelerate on
the CPU compiler of which is compatible
with x86 um architecture so uh some
backr databases try to use those like a
instructions to to to make sure to
optimize those instructions so when when
I just trying to looking at those
approaches I think um it could be
applied to accelerate on the calculation
for electric curve because we can just
uh unloop those
um uh duplicate calculations into a
compil level this that's my um kind of
imagination but have you ever tried
those tempor kind of things that's my
question yeah it sounds interesting but
we haven't try that like uh
implementation that and we are yeah we
account maybe you can create an issue in
our giab or we can contact contact each
other and then know the much more
details about your uh suggestions yeah
you oh we have two
questions oh maybe the
F hi uh
here um is um is your research
concerning also storage on mobile or it
is it has nothing to do yeah yeah yeah
yeah also also the the storage and
memory also uh really Fu in in Mobile
okay so and and yes uh with this are you
using like a different Keys generation
for every time um every time I want to
prove something or A Change Is Made
because I think that um this um adds
more to the phone storage right I heard
from the folks of nor that uh they have
like a the different uh back end that
only needs one one key to generate and
store yeah so now we uh when we explore
the cir Pro and then there's a really
large Z key if your circuit is really
big so yeah it's sometimes takes like
several G gigabytes to store in the
storage and it yeah it's crey pretty big
but yeah like the no example it has
really uh smaller zik key and it's uh
better for CLI side proving so maybe in
the future we can integrate more proving
systems that is better for clii proving
yeah thank you thank you for your
suggestion and also on the GPU size
we're trying to use uh much more
efficient way to encode the uh elic
curve points and scalers to make sure it
is much more you know efficient for the
storage in on the mobile
device thank
hello okay uh nice to meet you I want to
ask a question about the device uh
device memory limit uh some more detail
about your benchmarker uh as we know uh
the more larger your circuit or app
worse then the more device memory yet
may take on the GPU or your mobile
memory uh so for example uh I you have
show that you can do kiak or sha has on
uh on your circuit to generate the proof
but I want to know uh for your uh device
Benchmark uh 8 GB memory how large uh
you can do in sha or
kak so for uh for for example for
example uh uh you use snack ja and your
R banding do uh proof on your mobile use
matter and the app do Shahi about 1 KB
or 1 million
byte date as the pr image but like shot
shot or kop it doesn't take like that
much memory to generate proof in Mobile
so I would say like maybe less than 1
Gigabyte but I forget the uh exact
number okay yeah
yeah okay I got it just uh want want to
know the limit yeah but but yeah like
RSA is more more uh much more than like
K or shot
okay oh there one more question there
see everybody's interested in mobile
application um when you say mobile is
not clusterable like it has to be
standard I'm just curious um have you
like look into like there was like boing
or like there's like um I mean I guess a
few software or like a few Frameworks
that can actually uh facilitate cluster
Computing or even like building a uh I
guess what they call like a cluster
distribut cluster just with mobile
devices have you considered like looking
to those and um so that to just like get
around the U like memory limit or like
storage limit of a single device
things um yeah I I think that would be a
a way we want to explore but we want to
start much start from much more simple
stuff which is doing the proving on your
own device and then we uh do the the
method you propose like leveraging many
others like consumer device to do so
yeah but it it still cannot be compared
to the the the serers side GPU when like
like the one data center it's like
hundreds of them inside uh it's really a
really big difference so when you look
at the Benchmark of GPU acceleration you
might you you need to be mindful about
like uh which device they use to
Benchmark it's really
different okay thank you everyone let's
give a big warm Applause for aan and
Movin and that wraps up the end of the
first part of our lightening talks and
we will come back at 3:30 sharp and
we'll have another group of six
different speakers uh lasting for one
hour for the second part so hopefully
see you soon
o
up
he
to
bu
B
BL
sh
I'm I'm
n
oh
w o
o oh
oo
pap
a
o hi welcome back everyone hopefully you
had a nice break had some snacks and
freshen up because we have another hour
of excit exting lightning talks today
we'll have six speakers in the next 1
hour and they'll be covering three
tracks the developer experience layer 2
and also real world
ethereum so let's get started anyone
who's at the door please come forward
and uh we'll keep the previous um
throwball game whenever you have a
question please raise your hand I will
throw the board to you and remember it's
also a microphone so please speak
towards uh the black the black circle on
top of the square okay we have next our
lightening talk speaker Guan Guan is a
tech geek from Stark neck
foundation and she's going to share her
own experience about how to build a
vibrant developer Community let's
welcome her
hi everyone uh thank you so much for
coming uh my name is Gan and I'm based
in Bangalore India I'm a developer
Advocate with the starnet foundation and
I've also co-founded uh one of the most
popular developer communities if I can
uh called The Phoenix Guild we are um
heavily populated India and also have
branches across the globe um today I
have uh you know a short agenda of uh uh
what are some of the things that you
need to keep in mind or what could be a
potential successful uh process to build
a developer Community uh be it Regional
uh be it Global or um just uh for a
particular domain right so I'm going to
talk about um first two things I want to
highlight because they're extremely
extremely important and if you have
cracked that then uh the next three
things are pretty much um a lot of um
you know empathy collaboration and just
your uh willingness to kind of make this
Comm Community better right so how do
you start where do you start uh when you
are thinking about building communities
or building developer Focus communities
right um the first thing is and the most
important as you can see important stuff
that comes in your email right find your
persona right who is your main developer
Persona uh we have different types of
developers uh at different learning
stages we may have freshers who are just
out of college right they are complete
beginners they have no development or
domain experience in that case you're
offering them knowledge uh in bridging
that gap of getting into development and
then being able to get them into the
domain that you're building your
community for um your audience could
also be people with basic development
experience uh but may not have domain
experience so for example web 3 is one
of the domains where if you're
interested in building a developer
Community then you want your audience to
already have some basic programming
experience right it would help them
become much better web three developers
if they already know how you know if Lo
if and loops and all of those things
work or maybe you want to build
something which is much uh at a higher
level so they have some domain
understanding uh but want to build stuff
so maybe your community is just for
Builders right people who want to build
interesting projects interesting
businesses um or maybe you have a niche
domain which is just for experts or uh
based on diversity Etc once you identify
this Persona half of your work is done
but make sure to be very very
straightforward in terms of who are the
people that your community is catering
to if you want to cater to everyone it
will be a huge problem right and it will
be a very hard path to build anything
viable the second is that the Persona
that you have chosen write down a
journey that will work for that Persona
how will these people learn from your
community and make sure that the journey
includes closing the loop right I I say
this to everyone who's planning to build
communities or trying to work on
building communities that you need to
figure out what will be the end goal for
that developer who comes into the
community will they get jobs from your
community will they get support to
become entrepreneurs will they get
funding what will be their goal right
this is the second thing that you have
to crack and you have to really sit and
crack this right are you offering
education are you offering
entrepreneurship support are you
offering networking what is going to be
a journey of that developer who enters
your community and they exit by exit I
mean they have found something valuable
from your community and then they are
the ones who are going to give back to
your community so for example I just put
up an example of maybe a community that
is catering to builders on ethereum so
their ideal Journey would be getting
educated about ethereum which is what
you could potentially offer or build
their portfolio by working on Project
within your community uh maybe a
research Focus Community right uh or a
builder Focus Community where you have
opportunities for people to build
businesses or um you know you're you're
a community that is focused on
fundraising supporting entrepreneurs
right so if a mixture of one and two is
what you have to crack first everything
else that everything else that comes
after is just a bunch of slides with not
much wordings right so you need to
collaborate right um You may not be able
to offer everything so collaborate with
other communities who may offer parts of
that cycle for your community members so
their success will also be attributed to
your community success right um and how
will you sustain long-term a lot of
communities are springing up every day
saying that our mission is this our
vision is this but have you thought
long-term how are you going to pay the
people who are working in your community
how are you going to incentivize the
volunteers what is it going to be for
them is it going to be um a sort of
incentive that I'm satisfied after
volunteering for this community so you
need to really think about what that
long-term sustainability for your
community will look like and last but
not the Le least Community is all about
people so be empathetic and make sure
that you're starting small on a small
scale talking to builders talking to
people who who are your ideal Community
Persona and build from there so you can
focus on quality over quantity which
should be your final aim in terms of
community building and yeah that's me
Gan and if you have any questions around
Community Building web3 Community
Building or just developer Community
Building feel free to reach out to me
over my email that's both my Telegram
and Twitter at Gan lakmi um and yeah I'm
super excited that uh you are all here
to listen if you have any questions
happy to take that thank you
again any question for
Gan okay
I love
this always hit the wrong
person uh yes just one question uh okay
building the community what metrix are
you using typically to understand like
what's happening okay I didn't know okay
uh what metrics are you using to
understand like how it's going what's
processes like uh like and like what
like maybe maybe like what issues and
like sorry could you please speak to the
black C I got the question but I believe
you got me yeah okay yeah so I think at
the beginning I would say that don't
Focus too much on hard metrics like
especially metrics like how many people
are coming to your meetups or how many
people are joining your online sessions
these are all rubbish metrics honestly a
lot of times what matters is that what
is how many people are achieving the end
goal that you set out to achieve so if
you are a community that wants people to
build applications on ethereum your hard
metric should should be how many teams
are actually build building sustainable
long-term applications on ethereum right
and that's the metric that actually
matters to understand how to get to this
metrics of course you do a lot of
feedback loop in terms of like hey uh
you know you attended this particular
online session how did you like it so
maybe you track a little bit of you know
when do people drop off your online
sessions or you know when people come to
your meetups um in the when they come to
the next Meetup do you see the same
people coming again so are they getting
value out of your meetups or every
Meetup do you see different people
coming in if yes then maybe there is a
problem right so I would say that don't
focus a lot on uh metric like temporary
metrics but focus on what your final end
goal is like if you want Builders
building businesses then that's your
final metric so you have five teams
maybe that successfully came to a
hackathon from your community
representing your community and they are
talking about your community that's a
good metric for you to have right so uh
I would say that and I'm happy to also
chat about you know more after of
course okay sorry we don't have time for
one more question but please talk to Gan
afterwards yeah have any questions yeah
thanks everyone yeah have a good
Devcon next up we have Bianca and Bianca
is the lead Dev r at chronical Labs
she's going to tell us how to build a
developer EMP Empire let's welcome
her GM Devon this session is about
building a developer Empire my name is
Bianca buza I'm lead Deval at Chronicle
protocol and also the founder of Deval
uni one of the perks of the startup life
is about building building a tight KN
team along the way I remember when I
first started my very first startup our
office was someone's apartment and to be
honest I think we spend more time
playing Mario Kart than actually
building the
product but then one day it happened we
found product Market fit
unfortunately now if you think that Pro
finding product Market f it's difficult
that's because it is a lot of the teams
struggle finding that but then after you
find product Market fit the next big
challenge is about building a great
developer
experience every developer interaction
with your product is a gift so you need
to make that worth it make their Journey
seamless and
enjoyable you already build so far so
don't become complacent
now there are around around 26,000
developers in our
ecosystem what that means is that it's
not enough to have a great product you
also need a great developer
experience how many of you have run mpm
install on a freshly cloned repel only
to discover that it doesn't work raise
your
hands okay me too we've been there done
that that's the developer equivalent of
I'm going to deal with this tomorrow
we've all exper exp erience that
frustration we're going from one error
to the other nothing seems to
work and yet we try to move forward
sometimes it doesn't work and that's
when developer need the most our support
developer relations is about supporting
developers every step of their journey I
like to think of it just like compound
investment every resolve bug every clear
piece of documentation every positive
outcome those are all wins but then just
like compound investment losing feels
worse than winning feels good and loses
have lasting effects and they make it
harder for developers to re-engage with
product now there is a common
misconception that motivation is all
about money perks and praise and while
those are true the true driver I believe
is the constant feeling of progress
developer experience should align with
Community use cases ideally you want to
anticipate the needs and the challenges
of your developers you need to be deeply
invested I would even add borderline
obsessed with understanding and
supporting your developer
community and here are some examples
when I joined Chronicle we discovered
that uh some of the developers struggle
changing the addresses of the self
kisser the self kisser is a smart
contract that basically allows you to uh
authorize yourself to wiely yourself to
read from the oracles on testet networks
but as you can see in the image it has
different addresses for different testet
networks so what we did we introduced
this a table in all the guides where the
self kisser was mentioned making it
extremely hard for developers to miss
the fact that they need to change the
address while this small change uh might
seem like very trivial to you yet it had
a very big imp imp developers were able
to progress right
away another example is about hackaton
Workshops the challenge with hackaton
workshops is that they cover many
protocols and they are very tight uh in
terms of time all the workshops need to
run back to back however when developers
first interact with your protocol
they're going to have
answers and questions to ask so the
solutions that we came from uh was was
to have preh hackaton workshops those
were virtual more time relaxed
developers can come and build along and
they could get any questions
answered this not only that enhanced
engagement but also drove better
hackaton
results so far I share with you uh the
positive examples but the truth is we
don't always get it right and that's
okay a big part of devil is listening to
feedback even the tough stuff for
example we heard from developers that
they needed more time before updates and
they wanted to be notified so we
acknowledge that and we introduce
processes to make sure that developers
have enough time and we notify them on
time not only that this remove the
friction but only it strengthened their
relationship with the community
developers felt
heard now Deval is more than just code
and documentation it's about making
developers feel seen heard and
empowered by using small consistent WIS
and by cultivating trust and support
we're building relationships that keep
developers coming back Deval in my
opinion is creating lasting
relationships that go beyond technology
making developers feel that they're part
of something bigger and this is exactly
what motivates them to come
back thank you
much any questions for
Bianca Community Building very
interesting okay thank you bianka let's
welcome our oh is there a question
somewhere did I miss no okay sorry thank
come
back come back okay because uh some
unforeseen uh situations our next
speaker is not here so we will have a
break and we'll come back at what
we're looking for the speaker from base
if you are here please come to us
see
welcome back everyone we finally have
will from base here and he will be
sharing his experience building Bas
Community with us and in general how to
build a more scalable ethereum Community
let's welcome will
hey
everybody can everybody hear me okay
pretty good all right thank you so much
for coming here and being here today so
um Hello friends my name's will bin I
also go by W bins they smashing my name
together I communities at base I'm also
a full stack developer a base we're one
and a halfy old Layer Two on top of
ethereum
our objective is to build a global open
economy that spreads equality
opportunity and freedom around the
world we just processed our 1 billionth
transaction this past
week it's still it's still day
one across Discord farcaster GitHub and
X there's millions of people that are
part of our
communities I said Hello friends but we
don't know each other there we're
different genders different skin colors
we come from different
countries there's all kinds of things
that make us different here that
fracture us that drive us apart that
lead to a lot of the conflict that we
see in this world right now but we're
here we're here to
together all of us here left something
behind that really wasn't working so
well in some
way to look towards something better for
us for our friends for our families for
our loved
ones and that I think is something that
all of us can build a friendship on and
I think that's in the context of this
lightning talk high level our
future is the the most important part
focusing on that in building a scalable
Community an open economy that anybody
can be part of being able to work from
wherever you want being able to live
where you
want equality all those things I talked
about all those things that make us
different all those things that don't
matter
transparency verifiability on
chain not having to take each other's
word for
things
freedom and
hopefully
in what we see these days in the future
more peace in the
world but how do we do
that we have to make space for
everyone Builder ERS creators lurkers
people that are just curious speculators
gamers even scammers and
spammers there should
be direct paths for all of these
people and in order to do that we have
to create opportunities for
everyone I just said scammers and
spammers and I think one of the most
important parts of creating opportunity
for scammers and
spammers is being
empathetic there's people that are born
just by the lottery of
life in some part of the world where
they can't even leave their town they
wish that they could get on a plane to
come somewhere like this to sit next to
us today but they can't do
that the opportunities in front of
them LED them to that path it's up to us
as Community
Builders to build something
better to help people discover new apps
new opportunities new jobs learn educate
them for some people it's just to make
friends new
friends in a real world where they don't
have
any and in all that all of
us are better
life in order to do that we have to
focus on the fact that these problems in
the world these problems that we have
with each other across this evm even
these things that make us different
these subcommunities
that split us apart that we see
disagreements in those problems are what
unite us they're not what should drive
us
apart this evm is ethereum is what
connects us
together and so you as Builders building
Community people building apps across
the evm across
onchain an app is just something people
download but a community is something
that you come back
for so what do we
do we have to realize and admit our
mistakes when we have them we have to
realize we're not kings and queens we're
not
royalty being in this space is a gift
from the
universe but it's also a
challenge what am I what are we what are
you going to do with this gift to be
here today to be able to fly here to
Thailand to be part of this community
when others can't leave their
own to build something
better and there's a quote that's often
cliche but but it's so
true
alone we go fast but together we can go
far and so in that vein um I set up just
a telegram group so anybody here there's
no difference in networks we're all part
of this ethereum
community if you'd like to be part of
this
telegram I'm an open book people in our
based Community are open books we're
trying to build a better world together
let's share our knowledge let's build a
brain tust people watching this
recording later come to this group let's
work together let's go through the
things that we can't talk about in a
lightning talk how do we build safe
secure communities how do we scale
communities how do we make sure that
everybody has their space so thank you
all for sharing your time to be here
today thank you so much
will any questions
please raise your hand I will throw this
Cube to
you oh there's one there um please help
me uh it's not a question but a word of
gratitude thank you for your talk uh we
for your highly need this kind of speech
in the in the space like I just went out
from a very different conversation thank
yeah thank
you uh I see another question over
there hi Will I to meet you in
person how do you see communities like b
latan b India it's
Africa impact those
communities I think that
um thinking about like how all
communities start they start small and
in time they grow some succeed some fail
but if we think of things like on a
cellular level how human life imitates
itself in the form of how we build
communities the ones that continue to
get bigger and bigger and bigger they
divide and become their own communities
taking Costa Rica as an example here
there's many builders in Costa Rica but
in that there's also many people with
differences there's people that want to
build on chain that just want to play
games they just want to trade they just
want to work on infra and a lot of those
people they don't want to have anything
to do with each other that doesn't mean
they don't like each other they're just
not interested so for us as Community
Builders it's important that within the
first 10 15 seconds when they come into
our community we're helping them get to
the right place and so in the context of
this question for based latam which
we're referring to here which is based
communities in Latin America it's
continuing to build more and more
smaller and smaller and smaller
communities till eventually we reach the
Grassroots so that's my answer to the
question thank you well thank you so
much for your talk I actually have a
question but I'll ask you later it's
about Web Two user to web 3 I'm
interested in how you bridge the web two
users thank you but thank you will we
will welcome our next speaker uh nine
he's the founder at
Symmetry and he will be talking about
ecosystem development best practices and
he will tell us why you should start
with the builder
first stage is yours
hi good afternoon guys so my name is
nine I'm the K found of symmetry and I'm
also a fellow Tha here so it's a
pleasure for us to welcome you to my
home country in my hometown which is
Bangkok so really excited to be here so
yeah straight into my talk so as you can
see from the talk title it's about
ecosystem development so what I do at
symmetry is basically we help chains onb
more Builders and users from time so I
figured this would be a good topic to
touch on given
Devcon so what exactly is ecosystem
building so ecosystem building is
basically a two marketplace right so
side Marketplace so you when you're
building chains you need both Builders
and users and you need both add really
strategic timings a chain cannot
function with one or another so it's
basically a chicken and egg
problem but actually
if you actually look at the data if you
actually go down and dig into the
history and how each ecosystems came
about whether it's ethereum align or not
out EMS whatever that may be what's
actually the key is Builders not users
and what I mean by that is if you think
about your typical user Journey right
when you try out new Shan why do you
actually go to that new particulation
why do you actually go to opum why would
you actually go to optimism base
whatever that may be
because you have maybe you went there to
try a new flagship app a net new
application that you would like to use
which wasn't present anywhere else in
another
chain these applications would then
therefore Define the Shain identity so
if you think about optimism obviously
the word public goods pop into mind if
you think about arbitrum probably defi
if you think about base probably
consumer but how do we actually onboard
these great app
Builders so we need to think about what
what Builders actually want what do
Builders want right so they want to
onboard more users at lower customer
acquisition cost of CKC and how can
chains help them do that so there's two
ways you either help builders on board
users directly or you give Builder more
resources so that they can do more
within that chain which and effectively
lower CAC from
them so how do we actually do that we
actually see two successful approaches
are the chains that we work with
first you own what new net new users all
the directly to the shange itself a
great example of this is mantle so what
mantle did instead of going circle
jerking around and onboarding the same
set of users and liqu what they did is
they partner up with a firm called an
alpha and they help on board idle BTC
vity on Chain by creating Structured
Products around them such as fbtc which
is quite interesting and I think this is
a good way to onboard net new liquidity
into the chain which is more helpful for
Builders
another way is to do directed campaigns
so if you think about like a new change
launching out you have all these new
applications you can try on right what's
best and optimal for both the chain
itself and also the the builders
building on that chain is to help direct
user activity onto these applications so
a good example might be linear park or
even blast
C but if you go into that like there's
also a couple of different Frameworks on
how a Shan can actually support builders
in a more Hands-On Manner and you you
often see this sort of dilemma play out
into different ecosystems that you see
out there especially the al2s there's
the curation approach and the education
approach for curation you're just
working with select number of Builders
I'll select teams and just doubling down
them and then on the other end of the
spectrum you have all these chains who
are focusing on education giving
workshops doing things across the globe
and the truth be told is there's no
right or wrong answer
it's more of a dynamic answer to this
particular question and it's important
for a Shan to double down on certain
teams and Builders to build those first
set of great applications and once you
do that then you transition out and then
you onboard more Builders you be become
more inclusive so you need to transition
when your equos system
matures some creative tactics I'd like
to highlight to here so there's the
Scout program similar to AWS if you're
familiar so you have other people giving
out grants from on your your behalf
which helps provide reach you have
tricker down incentives like big blast
big Bank competition to tricker down
incentives on the Shan level down to
apps you also have retroactive programs
like optimism retr pgf or circuit buil
to earn to provide retroactive rewards
for build cating activity on
Shan but what if my Shan is ptge how do
I fund these apps what you can do is you
can partner up with VCS to set up token
lest ecosystem fund structure structure
or you can curate deals help your
projects fundraise you might not need a
token you might need to help them to
find resources find their Network and
get and put these ecosystem projects out
there and to wrap it up what about
southeast Asia how do we actually
penetrate this region I would say three
key things localization is key because
you need to be aware about languages
cultures and Val differences you need to
have continuation Builder mind share is
always is filled with these noise from
other ecosystems chains out there trying
to onboard more Builders so how do you
actually maintain that Spotlight in a
continuous manner you have to have
consistency and lastly you need to
allocate time to do proper division with
like the people that you're working with
in the local partners that you have
because you have asymmetry information
in language and whatnot so that's also
another thing but all in all the Dil is
in the detail because ecosystem building
is a multidisciplinary challenge with
death ra marketing ecosystem and all
that stuff to need c functional teams
who constantly iterate so yeah that's
say basically it to the end of my talk
so just to wrap it all up just want to
say thank you for your time for
listening hope you learn a lot from it
and also as a fellow Tire welcome to
Bangkok C
cup thank you very much nine any
question for nine
any interesting question about Community
Building okay thank you very much nine
thank you let's give a big
Applause uh next coming up we have Yen
ho and he has spent the last six years
running the technical direction for
runtime
verification and today he will be
sharing the challenges of building and
Main maining the open-source web 3
software please welcome
okay good afternoon everyone I'm y from
De learning yeah
it's fantastic to be here to share our
journey of building de learning and hope
our three years building exper could
offer you some inspiration to build your
local usering community yeah is
pensioning with limited or even no
startup
fonts my presentation will cover three
airs the learning introduction and its
main
components then and we are work through
our our community governance the rules
that keep us organized and
collaborative finally and we show how we
get grants in web stre ecosystem and how
we allocate our funds to support our
community
groups since the last Devcon in po I
have introduced de learning in detail so
this time I just quick recap the
introduction on the left side is our
community relevant data we are designed
for developers to step into blockchain
dep development where they can learn
Define ND doll and crypto projects we
help we could not only give
Junior developers a feasible and easy to
use dep learning road map but also
present Advanced developers with a PL
for for communication communication and
cooperation yeah this is our version our
community is built on four components
GitHub OS
you translation team and website
team let's start with our GitHub our
initial idea was just to create a GitHub
report to record our learning Trace in
of dep depth development in 2021 to our
surprise is it was more popular than we
expected there currently there are 80
basic tests that help you to learn dep
development step by step along with
advanced task like nft do crypto yeah
Etc now we have GED more than 5,000
stars and nearly 200 contributors have
submitted their Pro request to our repo
what's more exciting our report
frequently appears on the air drop list
of many web3
projects next next we call it the
learning open source University as many
Community member can schedule a session
to share web stream
knowledge as long as his presentation
talk is reviewed and approved by our
core contributor reward we we reward
each session with 160 D through ouru we
have produced a wide range of courses
including a comprehensive Define
learning road map and a DK introduction
course
uh next is translation team yeah the
world of blockchain is full of over
source of Temptation and scans so it's
essential for newcomers to study
structur course from famous university
yeah so our team have translated MIT
open course blockchain and money we also
translated many white paper and research
reports into Chinese 2 as a local eering
community we try our best to make high
quality content from English word
accessible to our core
members next is our do governance
governance are important to attract
developers to build Community Trust and
build a Community Trust yeah uh there
are three rules interesting rules of our
community they are working well rule one
anyone who has submitted PR three times
or has shared at least one time can join
our developer group it has a s selling
of and 20 people we also build a
community group for free communication
too yeah if you want to make a
advertisement in our group you should
share first
yeah the last part is our grant and the
is Grant and our fund allocation as a
nonprofit organization our funding
primarily comes from Grant and donations
like ESP Grant and gitcoin Grant in the
middle term we also get support from
many outstanding projects te such as
optimism scroll starnet C syn Etc this
year air drop from web three projects
are also a big source of revenue for
us yeah the financial modu enable us
remain a techology neutral stance yeah
we only focusing on eering and is Lay to
develop mment without any commercial
bioses yeah the slide shows a support
from okay sorry yeah this is our fun
allocation you can
see yeah we set up Community grants and
web three use grants to help developers
transist from Web Two to web
three uh this is
our rec con from the industry yeah the
slide shows the support from l two
projects lastly let me show our sponsors
yeah thanks for their support for our
community okay thanks for your attention
and I open to any question you may
have feel free if you wanted to join us
uh we have a question here do you want
to throw
it good
catch okay uh yeah thanks for your
sharing and uh I think we all know uh
building and maintaining the community
is not easy and uh that planning
definitely is a phenomenal success and
could you tell me or share your
experience about what's the biggest
problem or
challenge um during these years I mean
in terms of Education or the management
yeah um that's a really good question
yeah let me think for a while I think
that the most
challenging is the same as the most
developer uh K crass 2 is the DK
technology yeah as you know we have
produced a course of Define learning
road map I think is a good material for
developers to learn Define but we find
it hard for developers to learn DK or
make CK easy to understand for New
Commerce so we still try our best to
make easy accessible to everyone okay
okay okay thanks thank
you any other
questions I actually have a question for
you so for your users I guess they're
all geographically distributed in
different places do you think um there
are specific designs that is more
attractive to certain group either age
group or Geographic locations do you
find them um tend to use you know the
the app learning in different
ways actually same uh our users mostly
from Chinese speaking AOS the most of
the Chinese yeah uh uh they are the most
of them are developers yeah
uh because our content is more technical
you see technical right I see yeah so
yeah we try our best to make it
accessible to non developers too but
yeah that's okay thank
you thank you thanks
yeah okay we'll take three minute break
and we come back at 4:20 for the next
speaker
t
back welcome back um so we will be
having our last speaker for the middle
session today and uh we will have aage
from runtime verification he spent the
past six years uh leading the technical
Direction in runtime verifications
development tooling and today he'll be
sharing his knowledge
on some challenges he face in developing
open source soft software for web 3
welcome hi uh I'm ever henbrandt as was
introduced and I'm the CEO of runtime
verification and I'm here to talk to you
about the challenges is of developing
open source software and maintaining it
sustainably not necessarily in web 3 it
doesn't really matter web 3 web 2 I mean
there's some different challenges in web
same um so uh why are we qualified to
talk about this at all uh we have you
know a huge GitHub presence 170 public
repositories depending on how you count
given time it's spanning 15 different
programming languages lots of external
collaborators obviously the internal
developers at the team as well um you
know we have dependency chains within
that software that runs six deep uh in
some cases and we have different teams
that range in size from 1 to 10 we've
grown teams we've shrank teams we've you
know done all sorts of different
projects over the course of the last six
years as I've been working at runtime
verification and we have super active
and super awesome uh autom
with C
CD so what are the challenges I'm going
to start from the easiest challenge to
solve which is the technical one and a
lot of people probably think oh this is
the only challenge the technical one and
you know with the the technical
challenge with managing open source
software is automation you need to
automate everything uh so you want to
enforce as much as possible we use
GitHub for that you can use gitlab or
whatever other version control um and
publishing software you want to use we
use CI for testing so every you know
releases tested that just keeps our you
know Keeps Us sane basically automated
releases and updates and so we actually
have it you know that when we have those
six dependency chains going on we six
deep dependency chains if there's an
update to one of our pieces of software
it automatically pushes down the chain
to the next piece of software for us um
and one of the kind of challenges that
you might notice is you know that
software goes through different life
cycles right there's when you first
start developing a piece of software
you're in Rapid development mode you're
prototyping you're trying to move as
quickly as possible you don't want to be
slowed down um and that looks a lot
different than when you're in kind of
the the later stages of a project where
you're just evolving the software over
time and you have a lot more tests there
to guide you so you you need to accept
that there are different life cycles to
software development and for example
keep GitHub enforcement turned off at
the beginning of the development and
then you know a couple months in or a
couple weeks in turn on that GitHub
enforcement the Second Challenge is
person and this maybe it even deserves
to be the third challenge um because
this is you know the medium difficulty
challenge but what I like to tell new
hires at runtime verification is that
learning to program is easy learning to
program in a group is hard right and the
key thing to remember is that you have
to be respectful of other people's time
right and uh you know one thing to keep
in mind is it's always harder to read
code than to write code and so you're
submitting code changes or something
like that and it was easy for you to
read it because you have the intent in
your mind and you translated it into
codee it's much harder to go from that
code and translate it back into the
intent as the pr reviewer so as a person
who's authoring code you need to make
sure that your code is you know small
changes isolated changes easy to read
well tested so that the pr reviewer has
an easy time pressing the approve button
um you know remote remote work obviously
makes this a lot harder you know when
you're all in the same office together
you just turn around hey like what do
you think of this change and you work on
the same screen but now we're talking
about different time zones and there's
delays is associated with that so you
have to keep all that in mind and
actually keep it in your mental model
for your development um and so here
process is key example at runtime
verification I let everyone know you
know beginning of your day you clear
your slack messages first then you do
your poll request reviews and then you
do bulk code development on new code and
then you open new poll requests at the
end of the day you do your poll request
reviews first because that's blocking
someone right that is causing a
synchronization point between you and
someone else they might be on the other
side of the world and suddenly if you
don't do that PO request review you're
delaying them by a day and then that
maybe delays You by a day and so
suddenly you know some small change gets
delayed two days maybe three days if
we're talking about an 8-week project
and you have a handful of delays like
that you've lost two weeks on that
anyway uh next Slide the third challenge
is money and you know if you know how to
solve this please let me know uh the
solution I found is to beg and the you
know the the problem with begging is
that everyone starts begging and you
need to have like a begging process and
have a little structure to it and so you
have like grants and retr funding and
side quests where you get people to fund
one thing but then you develop another
thing as well um and the problem with
structured begging is that it becomes a
game and big players are better at games
than small players and so then the small
players Resort back to unstructured
begging and so I don't know we're back
at square one so anyway that's my talk
uh you know solve the technical
challenges first prioritize those that's
the easiest part make sure as you on
board people that you make them aware of
the Personnel challenges and then come
let me know when you figure out the
money thing thanks thank
you any
here great presentation I just want to
know more about runtime verification I
just check in the website um and but
it's much better for you to like
introduce what you do and why are you
working on open source yeah so we do we
do mostly formal verification and formal
verification tooling so we have this
project called the K framework that's
kind of our biggest project that is a
tool that enables us to do formal
verification for any programming
language basically um and so we have
formal verification tools for solidity
for web assembly for rust we also have
for some other blockchain like cardano
and tesos and stuff like that so that
require that's a big formal verification
is hard software to develop and it's
used in a bunch of other contexts as
well and so we just end up having a lot
of different repositories targeting
different ecosystems and different
programming languages that we do for and
most of that is done for security audits
basically so thank
you there's a question over
there thanks hi um cuz you you already
mentioned uh the workflow especially the
GitHub pull requests so I had a question
about that um do you have any advice in
terms of leading the team and
structuring the pr reviews uh because in
my opinion when there is an update or is
a bug fix it's quite straightforward it
doesn't really matter the number of
commits because you look at the change
you look at the description you know
kind of what's happening but perhaps uh
you have an advice on how to structure
the commits when it comes to a new
change and when you said about like the
m like it's hard to construct the intent
by looking at the changes so perhaps
having more commits and uh following
them one by one would help with that or
you know what I'm asking perhaps have it
up there uh I mean it's challenging and
it's challenging not because it's a
non-s solved problem it's challenging
because people just don't do it right
but uh I mean have good commit hygiene
try to make it so I try to make it so
every commit builds if not passing tests
it might be that you're going through
refactoring and tests have to be failing
in the middle there but every commit
should build in my opinion and so that
should make it so every commit you can
review in isolation if that's necessary
which is not the ideal way to do it
because that takes a little longer to
review but then the second piece of
advice I'd give on that is as a PO
request reviewer just be really picky
you know if someone sends you a poll
request that is changing four different
things and it's hard to review the whole
thing and keep it all in your head don't
bother reviewing it just send it back to
them and said hey you weren't respectful
of my time break this into four poll
requests and I'll review each one
independently because ideally as a poll
request reviewer it's easy for you to
look at a poll request and say this is a
good change I'm going to hit approve and
move on right but if if the if you can't
do that and you have to now dissect what
is this change doing you're not the
expert on it you didn't write that code
it's much easier for the person who
authored the poll request to go and
split that up into multiple different
poll requests than it is for you to
dissect what they meant right so don't
you as a poll request reviewer don't be
shy just be like look be more respectful
of my time please go break this up into
multiple PO requests so I can review
each independently that's my opinion on
it all right thank you very much thanks
thanks for the tips for PR reviews I
think we can all benefit from that um
that's everything for this session let's
um give another Applause to Everett from
runtime verification so we will take a
we'll have nine speakers uh giving the
last part of the lightning talk so we'll
be back at 5: and the day ends at 6:30
so hopefully you have some break and
we'll see you soon at 5:00
m
bu bu bu
got
you he
G
w
you n
bu w
session of the lightning talk so we will
have one and a half hour with 9 speakers
giving different talks um so let's keep
the energy going and uh let's kick off
with our first Speaker Pablo welcome
Pablo hey how are you guys how's
everything well today I I had a workshop
but they but they told me okay you don't
have an hour you have five minutes so
I'll make it brief and I'll go to the
conclusions well I'm Pablo SAA I do web
three operational security H at OBC
where we train and audit companies for
everything that is not on Smart contract
and I am a contributor of C 911 where we
do incident response for
blockchain so what are we going to talk
about today simple things that we can do
to enhance our upsc right so one thing
that is very important to know is that
it's not so important if I use Windows
or Mac Android or iPhone Chrome or
Safari or whatever the important thing
is how we configure the tools that we
use right so first thing I want to check
about very fast two Factor
authentication things that you not have
to do do it with SMS and we cannot do it
anymore with top apps like go like
Google Authenticator or AI those kind of
tfas can be fished and they're being
fished every day we need to use UV keys
right but not the UV key with the normal
OTP mode UV key with F to that cannot be
fished this is happening a lot in the
ecosystem next soja engineering we have
to be very very very careful for this
like professionals hack people not
systems right today is much cheaper to
attack someone and much easier than to
attack a system so be very careful with
suppose recruiters busy fanss investor
and journalist that want to invite you
to some call or something never download
anything be very careful with PDFs that
you open they are usually in infected
and if someone looks if something looks
like strange it's probably it's probably
in scam right and everything is an scam
until proven otherwise
everything next eventually all of us
will get hacked that will happen it's
not a matter of it will happen or not
it's just a matter of time so we need to
be able to contain the damage so that
you know when someone in your team has
been hacked the damage will be contained
even the founders even the ciso even the
CTO so everyone use an antivirus and a
firewall people think that no I use a
Mac I don't need an antivirus use an
antivirus MacBook is not uh good with
barers alone there's a good foundation
called Objective C that has many tools
for security in Mac one more thing the
attack will come from a trusted Source
right for example we saw how they were
hacking the even brights of the events
at delcon one hour before the event and
they send the the message from the real
account to everyone hey you have to Mint
this nft you mint it your wallet is
drained
completely uh you receive an email that
says that it's from Tresor and it's
really from Tresor from the official
system but it has been hacked they send
you a drainer you are
done one more thing use a password
manager and never never ever reuse a
password right but let's use password
managers and we have to have to have
them configured very securely but never
ever ever and this is very important
very important never put a seed phrase
in a password manager right for sure
many of you have done it yeah and you
say oh we did it but it's okay my
password my password manager is secure
no it's not if you have ever put a SE
phrase in a password manager you cannot
use that wallet anymore you have to move
to a new one use Hardware wallets
hardare wallets are
important many will think okay this
things that this guy are telling us are
very basic this basic stuff is the
reason why today 85% of lost of lost
funds uh are are lost every day right in
blockchain is not anymore due to Smart
contracts we have gotten very very good
at security with with smart contracts uh
and money is be being stolen like this
so you have to be really really careful
well I hope you you liked it I will be
here if you want to talk more about this
like this was a very very very small uh
resume but um operational
security is important is the number one
reason H how uh we are being attacked by
very sophisticated third actors
something that is happening is that in
the industry we have one of the worst
obss in all the industries worldwide
because we don't have regulations so any
company does whatever they think that
it's okay and it's not and on the other
side we have very very sophisticated
threat actors from nation states that
are doing these kind of attacks and they
know what they are doing so be extra
extra careful I hope you liked
it thank you
Pablo any questions for Pablo
yep oh there do you want to give a go
cuz it's on your side do you want to
throw I had to throw it there okay
oh sorry you're much better than
me um so what would you recommend to
people to store their seed phrases
securely because I think the challenge
is I mean I'm a CTO as well uh you you
either have to make it secure or if you
you you want to prevent people writing
it down on a post right so what I think
that writing down SE phrases is one of
the best ways to store them one Hack
That that you can use that is very very
simple was told to me by one of the guys
from the red Guild is buying
anti-tampering bags the ones that
eCommerce use so you write it there and
wherever it is that you you save it you
save it with that so with that you are
sure that it has never been seen by
anyone if sometime it was seen by
someone they have to break that so
that's another very good way and I
really like Shamir like having your your
seed phrase and cutting it in places in
three lists but you only you need two of
those releas that gives you
confidentiality and availability so I
think that's pretty good thank
you do we see any other questions oh
over there there was one question
y all right I actually wrote down my
question uh how do you choose a product
for Secrets like SSH Keys o tokens Etc
management across multiple Cloud
providers so a product for what sorry a
product for Secrets management like SSH
Keys o tokens across multiple Cloud
providers uh I don't have a good answer
for that so I'm not uh I'm not sure what
would I
use
um the guys that are really because I
only talk about stuff I'm really really
good at right and the guys from the
redil had a very good guide on on on
that so they will be maybe able to ask
that question far for rather thank you
than me no thank
okay uh what do you think what is the
most secure multi wallet or Hardware
wallet no I think that safe is good and
regarding Hardware wallets I consider
that all of them are also very good
treas or Ledger safe palal the think is
how you use them right
but I I think that all of them are are
very good and I think that safe is also
very very
good yeah there's a question over
there right uh you covered a lot of
stuff there but uh is there any uh
advice you give on browsers or how you
deal with browsers and that's generally
where a lot of Steelers are sitting or
what yeah yeah browsers be very very
careful with the extensions you download
like we have to be very very careful
with extensions there are lots of
malicious extensions and the other good
practice is to have more than one
session for example you use Chrome you
have five sessions one for work one one
for Def One for personal staff one for
this for that for that and you also can
have an our browsers right uh or even
better than that is having an hour
session in a BBN right so you have it h
sorry in a virtual machine so we have
another virtual machine with another
browser if you want to keep it like
really separate and that's also pretty
good okay thank you
Pablo our next lightning talk will be
from Jason Jason will be showing us how
to secure your secrets with micro do
let's welcome
her hi guys
w just joking welcome to
Thailand um okay um for my talk I'm
going to talk about micro dots so what
exactly are micro dots so I'll be talk
talking about how do you like why micro
dots and how do you can how you can
actually make them and I have some
samples so after the talk you can you
can check it
out so I guess there's a lot of
questions about obac and how can you
hide seed phrases and so a lot of the
process are all digital but what if
there are physical processes if you can
obus skate
stuff and so key custody remains like a
huge problem and so they like secret
sharing social recovering social
recovery practices but I know a lot of
crypto people in sales of hiari so like
social recovery might be
hard so look at this graph we have the
Hess epidemic that happening right now
so yeah key custody and like like social
recovery is going to be a huge
problem so what if there are physical
approaches of upus skating information
and so this is one of a stenography
technique and it's you and it's called
micro dots and so the reason why I'm
showing out is Ana forer today because
this has historically been used in espon
and spies um and so the goal is to
essentially heighten messages in plain
sight so how do you do this um so
apparently all the documentation around
this is so limited so you you try asking
Claud is like saying sorry guys no info
for you so I I was like trying to
reverse engineer this information myself
and basically the slides are going to
document everything I won't be able to
cover everything but I'll cover through
some interesting
details uh so we are going to revive
analog photography for this use case so
why we want analog processors there's
basically no chance for someone to hack
like a analog camera unless he steals
the camera from
you uh and there a lot of Gess so uh I I
kind of screwed up so much and I I can't
talk everything in details but um I I'll
I'll I'll create a GitHub re for
documenting the
processes um so one of the main issues
with analog photography is this thing C
ISO so on your cameras like this is not
a huge deal you can adjust it but ISO is
a function of like the film greens and
so this becomes a problem of how how
much you can Mize in the image so the
smaller the is the smaller the greens in
general and so this is like the few
processes that you need to do first you
need to take a photo and then you have
to develop the photo and then fix it and
that's like the first phase and so we
we'll we'll be talking about two phases
so the second phase is instead of
expanding the image we want to do the
opposite okay this are all the things
that you need to
use oh yeah so this is kind of
interesting so I I have like two
processors one of them uses ammonium D
chromate so I call this cancer orange so
I probably need to go for cancer
screening after this because I think I
might have Ren some dust from
this uh yeah and then there's like
cellophan so this like dialysis tubing
so I was like going to a medical St I
don't have diabetes by the way but no I
don't have kidney failure diabetes but
uh you need this to kind of as a
substrate okay bunch of optic stuff so
this is how how how you do it you write
your seat phrase so normally a methas
you ask you write a seat phrase but then
um where do you put the seat phrase so
this is one way you can you can start
the seat phrase you take a photo of the
seat phrase uh role in the film develop
film oh and also one interesting thing
apparently this all heavy metals because
they're silver metals like you shouldn't
put in your toilet so I P some in my
toilet so I might have committed some
offenses around here um yeah it will
probably corrup my pipes in the worst
case but I might have caused some like
environmental
hazards yeah so the next process you
take the photo again and then Tada you
have this tiny little boy over here and
so this process where you retake the
photo against called the British process
the next other process which I want to
do was like a dichromated process and
this is how you can get like microscopic
modifications like 1,000x and so the
goal is to find a chemical substrate for
this uh and so this is where the
Forbidden orange juice comes in and it's
uh very toxic to not refin or use this
chemical um so I I'll try to find like a
better chemical for this but most of the
photosensitive chemicals are toxic as
hell um yeah and this is like the
process
so I I did spill some of it and so I
almost
died uh yeah and so this is how it works
you project the image and then you get
this tiny little thing dots on this
piece of
paper uh and that's it uh for this
presentation I'll sh my details on the
GitHub refo if you guys are
interested thank you
Jason very cute ha any
questions okay I'll do the easy
one um how do you do this whole process
without getting on the FBI list uh I'm
probably on the list right now so uh I
guess you need fake IDs
or got it okay another question did you
consider anything else oh I didn't
consider like other stenography
techniques but I I think things like
micro dots uh uh have historically been
used but I somehow do not see them
around in practice today so it could be
the case that it's all classified so I'm
like maybe leaking classify information
right now
so well I guess my follow-up question to
that is there were other methods used
for Espionage throughout the world wars
that might have been easier to do
yeah it might be classified so um yeah I
couldn't find information much
information about this unfortunately so
I was just reverse engineering the
chemistry yeah in s of code is not
chemistry I think we have a question at
the back
there so why why are we not using photo
lithography for
it photo photography oh yeah it's
basically a similar technique so uh but
not everyone has a clean room in their
home so the goals to find processes that
you can do in a home environment uh so
it is kind of similar to
photolithography techniques so some of
like the techniques are applicable U uh
yeah but also like Photo lithography
also some processes are patented so you
can actually like use them in in
practice cool any other
questions ah this there one over there
can we
throw uh is is it in the middle
there oh no sorry you raised your hand
and I thought you want to catch up the
okay there's another question
there uh how small are the micro dots uh
I I can show it show it to you Le it's
quite small that's all I can see it's
like small so so you definitely need a
microscope uh the one using the British
process you can see if you with a naked
eye but the other one uh it's kind of
really damn tiny so I'm not even sure
whether it's it's like a actual image or
not yeah I need a microscope for
great ah you do have a question um and
and how long I and um how long does it
stay is there like a half lifee uh half
life this is not radioactive I know but
what I mean is like does it U Can you
see it after like 20 years for instance
uh we'll find out in 20
years okay one more question over
there hello have you reverse the process
meaning you encoded have you flowed up
the picture to see if you recover it I I
think you could uh you probably need
some kind of optical setup so
essentially you're trying to project an
image okay we're running out of time
that's the last question thank you very
much
Jason uh if you guys want to see stuff
I'll I'll be somewhere around here you
can see some of the samples thank you
for your time
guys thank
you on next next speaker is Peter Peter
is the CEO and co-founder of L2 beat and
today he's going to show us some new
feature of L2 beat which will allow you
to see the protocol risk you are exposed
to as a user let's welcome
Peter let me tell you a
story and you're probably familiar with
it you might have even lived this story
yourself a young guy like you or me
decides to bridge their
tokens they take out their Hardware
wallet connect it to the computer go to
the Bridge website and now they start
sweating right they're bridging they
they don't know what's going to happen
they they they they make a transaction
and the coins don't appear on the other
side what's going to happen what's going
to happen 10 seconds pass the coins are
on the other side the guy's saved
right but actually not right and that's
that's the funny thing we we think that
the only risks that we are exposed to
are during the bridging and then we
don't really think about the tokens that
we get on the other side and so for
example for bridges that lock and mint
tokens
the tokens can still be stolen on the
original chain and for bridges that are
liquidity networks well they still have
to give you a token on the other side so
this token still might be stolen
and you know we were sitting half a year
ago in
Budapest at an offsite for L2 beat and
we were looking at our website and
thinking you know those risks that we
show
they are really nice but they aren't
really connecting with some people
because they see what uh what we show
they can see oh arbitrum this optimism
this they can they can go dig deeper but
it's not personal for them right they
they don't have an ability to to see the
actual things that they are exposed
to and and when we thought about how to
solve this problem how to how to make
something that will actually allow users
to see the risks they were exposed to we
we actually figured out that this thing
would have to be for a different Target
user and it would have to look
completely different than l2b today so
what I have for you today is a thing
called
insight and what Insight is is currently
a demo that you can see on our
boo but what it is also it is a way to
see the risks for your specific wallet
so if you were to input your ens address
or your ethereum sorry your ens name or
your ethereum address there you would
see a list of your tokens that you hold
on different
chains with the associated risks so now
you no longer have to go to the to beat
main page and figure out oh is this
chain where I actually have my tokens is
this bridge the one that I have used all
this information is compiled for you and
what we also show right on on the inside
is the path that the token has taken
through the different blockchains so you
can actually see that the wbtc you're
holding on arbitrum one has been bridged
from ethereum but before it to ethereum
it has been locked on bitcoin and there
is a multisig on ethereum that some
permission custodians manage that
actually takes care of those tokens and
we hope this is this is an experiment
that we're doing but we hope that maybe
this will allow users to feel that the
risks are actually affecting them see
what risks they're actually exposed to
and we're also thinking maybe we can
suggest some mitigations one one example
would be uh you that you might be
familiar with would be the usdc E and
usdc tokens where the usdc E token is
the one that was bridged from ethereum
while the usdc token is the one that's
Bridge through
CCP or ccip the the the bridge from
Circle itself so one has an additional
trans assumption the other
doesn't and I encourage you very much to
go to our booth check out the demo play
with it and thank
you thank you very much
Peter any questions for
Peter out2
beat I actually have a question because
I use L2 beat a lot are you going to
include uh me data on L2 on l2b oh
that's a very interesting question we
haven't been exploring that site very
much I think um it very much depends on
the progress that the chains are going
to make because the more progress the
chain makes right for example right now
we most of the rollups are stage zero
there are a few that they are stage one
and at those stages the thing that
actually matters is the fact that the
owners of those rollups can just upgrade
it under you and just take all the money
so the me is like a detail but it
matters way less if we start seeing uh a
future where rollups are more and more
decentralized then those topics would
become more and more important because
we can stop focusing on the trivial
stuff and I think this will be a good
point to start looking into this I see
you a question
hello are you planning to incorporate
any um notification of uh scams after
they happen in real time for specific
Bridges that's a very good question I
think I think this is something that uh
that we would like to do right uh it's
uh very hard to detect this because you
never know what exactly is going to
happen we we have a monitoring
infrastructure but it's still I guess
run every other hour so it's not in real
time uh maybe in the future our internal
tooling would be sophisticated enough
that we can you know detect those things
in real time and then we would maybe
send notifications that would be really
fun do we have another oh there's
another question there oh there sorry uh
so right now you are only uh detecting
famous dexes or like any Dex that will
just pop up and someone brid through
it in terms of what we show from the
risks right at L2 beat we analyze the
l2s uh not all of them are just dexes uh
some of them are just general l2s
meaning they can execute any evm code
and for the tokens uh we we actually
look at uh other risks for examp example
the bridge risk so it's it's more than
just
dexes okay one last question at the back
the gentleman there yeah I think of this
similar to tools like revoke cash where
you would manage your allowances so
what's the original goal uh what was the
original intention behind building this
like what risks are you mitigating yeah
the the main intention is is to make
things personal right when when you go
to the L2 beat website the the things
you see are very technical and also very
specific to the projects right and and
with this demo you can see the actual
things that affect you without without
seeing all the rest right so so the
intention was to Carter to a different
type of user uh that you know doesn't
feel the connection with the main
website that we
have okay thank you so much Peter thank
you so much good to know these new
features from O2 beat our next speaker
is Pina Pina is a researcher from
runtime verification and she'll be
showing us a Playbook of secure smart
contract development let's welcome
Pina hi everyone uh I'm Pina from
runtime verification and today I'm going
to present our comprehensive approach to
security that we have at RV because I
believe believe that it's it can
significantly improve the security
stance of projects and even make it more
sustainable for them um I'd like to
represent this project as a pyramid
where lower layers uh enable or at least
make it easier to get the higher lay
layers right and currently the standard
is to implement the code and just hand
it over to some external auditor or a
contest for a oneof audit or code review
and while it is a pretty good Baseline
it also doesn't do much in terms of
continuous security assurance and that
is very important especially for
protocols under active
development um if the team has resources
or feels like it uh some projects also
have some documentation outlining what
the code um is actually supposed to do
or even use some tooling um to do unit
testing or fuzzing and while the
completeness of those is very much
hindered by the constraints in um devel
the development process um having more
complete documentation and some tests
actually makes helps make sure uh that
the audit is actually going to go well
because it adds an additional Dimension
to it since the auditor can not only
check for some common vulnerabilities
but also uh for the adherence of the
code to the business logic uh that
they're supposed to
implement um and having test obviously
is good too uh a more comprehensive
approach however uh add some more layers
and maybe counterintuitively we actually
think that it makes the security model
more sustainable and uh one of the steps
that is often overlooked is the design
review view that's where some person an
auditor looks through the design
understands what the project is actually
supposed to do and um how does the
architecture looks like and sees if it
actually makes sense because if the
design doesn't um then none of that
matters actually because the protocol
can still be compromised and the good
byproduct of that is that it also allows
you to write Better Properties and
specification outlining what the code is
should or should not do and once
formalized in the forms of tests or
proofs we that actually enables uh the
application of more advanced tooling we
can have more complete fuzzing test SS
we can do formal verification for even
better security guarantees and the best
part of that is that we can also run
them on CI and I generally believe that
having automated security processes um
is good adding more automation is better
because it makes it harder to just skip
through certain steps it ensures that
the the security protocol is actually
followed consistently and also CI in
that sense works as sort of an automated
audit that is going to be run on every
PR or every commit uh and um well that's
less expensive than having a human looks
through it over and over again so as an
example of
something um that as an example of how
it is important to follow through this
whole process I have this well example
that may or may not be based on a recent
hack and that happened to the protocol
that uh helped users convert their BDC
into an equivalent amount of rep BDC
that we call Defcon BDC
and it was running on BTC chains so it
was supposed to work with Native tokens
but it was also running on other
networks which had ethereum as a native
token and there was a change that
actually made it possible for users to
Mint uh an equivalent amount of Devcon
BDC for eer and iser is like 20 times
cheaper so the hacker actually just Meed
a lot of free money basically and the
thing is there was a property that just
hasn't been enforced or maybe hasn't
been formulated that the user should
also not be able to convert non bbtc
tokens into uh well the rupt version of
BDC and this property could actually
have been enforced with something as
simple as a unit test or this fuzzing
test that you can see on the slide um
that just checks that if um the protocol
is running on ethereum Main net then
whenever someone tries to Mint tokens
using ether um this transaction fails uh
so that is a Foundry test uh has it been
running on CI it maybe it could have
caught um the issue as soon as this code
was pushed but before the deployment
uh so to summarize the points I want to
make here is that security is
complicated I think everyone knows it
there are a lot of steps in this process
it's very important to get all of them
right um automation is very useful
because it helps ensure uh that the
process the security process is followed
um consistently and is enforced and in
addition CI also provides a very
efficient and a very coste effective um
way to ensure that new updates don't
break anything uh one last thing that
has been missing so far is this Baseline
layer which I haven't really touched in
detail that is uh OBC because
unfortunately there have been a lot of
private key compromises um in the past
year and if the private key is
compromised then unfortunately even a
very secure smart contract code uh can
also be
exploited and and there are lot of
resources about how to get it right on
the internet so I encourage all of you
um to look through it and yeah thank you
much thanks
Pina any questions for pina
I guess my one question would be around
maybe fatigue in terms of continuing to
be diligent about making sure that the
basics are in place and I'm curious for
you what has helped to maintain those
habits over
time thank you yeah we try to follow
this processes religiously uh at RV
automation helps a lot because uh you
don't have to you know go over the same
things uh over and over again instead
you write some properties that you
specify some properties and then you
formalize them in the forms of tests or
proofs with a lot of formal verification
so that's that's what we try to set up
and then as whenever code changes that
actually handles it for us uh for a
large to a large degree um I think it
actually the having the process makes it
easier cool next uh yeah question on
like uh blockchain security the where
you have Smart contracts which is
immutable versus let's say on web 2
where you can update your code if you
discover a security um problem after the
fact so how does that factor
in Oh you mean upgradeability uh not
necessarily but like let's say you don't
have upgradeability then how would you
modify your security practices such that
that doesn't uh like so that you
mitigate that I guess right got it thank
you um well I guess that's why you try
to get it right the first time before
deployment that's why we advocate for a
very comprehensive security analysis
that you perform before deployment uh to
make sure that you go through all the
stages that the team you know writes
proper documentation helps us formulate
the properties and invariance that
should hold that they can that can later
be monitored um we advocate for like
formal verification to ensure that there
are like the bus security guarantees I
guess there are some there there is a fi
that that deals with like some posst
hack things or recoveries um but I guess
that's um that's that's a different
story we just we just suggest that
people should get it right and I think
you know I think we're getting
better cool is this something like the
oasp Zed attack proxy equivalent in
smart contracts or blockchain Frameworks
that you'd
recommend sorry can you please repeat
once again the O the open web
applications standards project The Zed
attack proxy that they have we used to
use it in our CI Tooling in like web 2
sort of development to test for the top
vulnerabilities right yeah I haven't
been aware of that but it's it sounds
pretty useful I'm all up for using any
tooling that helps and having it on CI I
guess anything would help static
analyzers are great uh as the first step
especially um having unit tests is also
extremely helpful and very efficient um
fing can enover a lot of vulnerabilities
so uh yeah thanks for letting me know
about
that okay one more
question thanks um you mentioned like a
design review as a precursor to the
actual code review is your like hope or
expectation from an audit point of view
that a team comes to you with the design
before they even write the code or were
you just talking about that as a
separate specific phase of the audit
that is perfect but that almost never
happens so sooner we introduce
security and you know some testing any
of that uh into the process of
development the easier it becomes for
everyone uh that's something that we
have found out ourselves uh but it
almost never happens so we at least try
to allocate some time for design review
first before we dive into the code
itself to make sure that we also
understand what it's supposed to do um
but I mean having the team providing us
the design first is ideal and we can
also like help us help help out with the
stages uh but it's pretty rare because
of the resource constraints I guess
great
thanks okay we can take one more
question if there is
any oh this one
day thank you uh I would like to know if
uh if there
are some security best practices
for smart contract based on artificial
intelligence thank
you Bas on artificial intelligence right
yes right um I am aware of a few tools
that do it um I think you can also ask J
to generate you some security practices
uh and it will be pretty helpful when it
comes to like common vulnerabilities I
guess the current common problem with
all this AA based tooling is that it it
is good at pattern matching right so it
can definitely help you find some common
issues that are known for a long time
but it probably has bigger issues with
like business logic or design review
Parts um so I guess it's it's pretty
helpful at least when it comes to the
the the first
part thank
you okay that's everything thank you
Pina let's give it up to
Pina our next lineup is Jack Jack is the
co-founder and CEO of Sherlock and he's
going to share with us what's the most
common vulnerabilities found in audit
contest stage is
yours hey everybody great to see you all
here thanks for coming out I'm Jack
Sanford I'm the CEO and co-founder of
Sherlock Sherlock is one of the largest
audit contest providers ERS in the space
and today we're going to talk a little
bit about the most common bugs found in
audit contests so if you're a protocol
developer or if you want to become a
protocol developer one day you are going
to be ahead of 90% of other protocol
developers just by being aware of these
bugs so just a quick intro on aut
contest and why you should care um Auto
contests have become and are becoming
one of the most popular ways to secure
smart contract code before deploying a
protocol to mainnet uh there's been 625
audit contests run uh the most have
happened this year of any year so it's
really taking off 36,000 vulnerabilities
found 36 million in prizes have been
paid out to thousands tens of thousands
of Security Experts people who are
learning to be Security Experts all from
finding bugs in these audit contests and
as you can see the biggest teams in the
space are using audit contest all these
teams have done an audit contest this
year in order to secure their
code so what is an audit contest
essentially the goal is to find bugs and
code usually critical bugs bugs that are
going to cause losses for users on
mainnet you start with a pot of money
you say hey here's 100K or in some cases
here's a million dollars and we're going
to pay people based on the bugs that
they find and anybody can participate so
it's a really great way to onboard to
crypto really great way to onboard to
web 3 security participating in audit
contests and
depending on the severity of the bugs
you find so if they're critical severity
you're going to get paid more for them
if they're super unique and other people
don't find them you're going to get paid
more for that and if you find you know
three of the four bugs that are in that
protocol during that audit contest
you're going to get paid a lot of money
for that so really cool thing and we're
going to rip through super quickly the
top 10 vulnerabilities that are found in
audit contest these
days so number one first depositor
inflation attack in ERC 4626 volts this
is a super famous attack really annoying
because anytime you deploy a new Vault
um on a blockchain you're essentially uh
exposed to this attack um because the
person who puts in the first deposit can
essentially put in such a tiny deposit
that it causes sort of a rounding issue
and then all the deposits after that are
a little bit messed up and the first
depositor can steal funds that way and
kind of Dos the the vault
second one using transfer instead of
safe transfer so just using the transfer
function in solidity doesn't actually
check the success or failure of a
transfer and it can also allow for
really bad things like re-entrancy with
non-standard tokens such as
usdt number three missing validation and
admin checks so let's say you only want
the owner of a contract to call a
function or someone on a white list to
call a function
a lot of times there's so many functions
you just forget you just forget one
essentially or you forget to check for
something that you meant to check for
and that's what Auditors are here for
and they're really good at finding that
stuff um so this happens more often than
think okay missing check for active L2
sequencer so essentially if you are
deploying a protocol on top of an L2
like arbitrum or optimism um sometimes
the sequencer goes down not very often
but it could happen in the future and it
could happen for long periods of time
and if you're a derivatives protocol or
something where real-time information is
super important malicious actors can
take advantage of stale prices because
of the sequencer being
down number five the classic re-entrancy
very first major vulnerability ever in
ethereum the Dow hack um basically there
are certain functions where essentially
you can continue the execution outside
of the function and call that very same
function again and this can cause all
kinds of problems there's a bunch of
different like surface area for what
these um vulnerabilities can do but I'm
sure a lot of you have heard of
re-entrancy
already feon transfer rebasing tokens so
if you want your protocol to be able to
handle any token out there um or even a
pretty General set of tokens a lot of
them are non-standard a lot of them
don't conform to you know things that
you would think that they conform to and
so smart contracts can get completely do
or or um funds can be lost because of
these tokens um having non-standard
behavior with your
functions so rounding Precision loss
issues this one has become really famous
in the last 12 months even if something
is off by a couple of way or you know to
the 18th 17th decimal place you can have
major issues because of the way that
solidity essentially or the evm
essentially doesn't have floating Point
arithmetic so it truncates things it it
rounds things a little bit and that can
cause a lot of issues um hitting the
last three really quickly here using
spot price uh instead of twap and Unis
swap so this is something that I think
we've all seen price manipulation
attacks where someone um basically
inflates the value of a certain currency
in a Unis swap pool for even one block
and then does some attack using a flash
loan and then it goes back down so that
one is really common uh less common
these days thankfully incorrect
implementation of upgradeability so
essentially you want you want your
contracts to be able to be upgraded and
it turns out you hardcoded something in
an initializer you hard-coded something
in the Constructor and you can't
actually upgrade your contracts and you
only find that out later so that's kind
of annoying but not too big of a deal
unless it's uh unless the initial
deployment of your contracts is super
critical last one no slippage check in
custom vaults and pools so ERC ERC 4626
is great use you know standards whenever
you can uh when you're developing in
solidity um because if you have
non-standard pools you can actually have
um your user sign up to get a trade done
at one price and then at the very next
block or the very next execution um that
price is completely different and it can
be off by a massive amount of percentage
points so your users can get really into
trouble if you don't have slippage
checks on your functions there so that's
the whole talk if you're looking to
become a protocol developer check on
these 10 things before you send your
protocol to Audits and you'll be ahead
of 90% of the other developers out
there thank you Jack I see a question
over
there right um when when would you do an
audit contest would it be like after
you've done an audit or before you do
your first audit like or instead of a
regular audit what what's the goal there
yeah it's a great question if you can
can do multiple audits I would normally
say do the audit contest last because
you get 300 people it's a little bit um
there's there's more operational um
complexity with it because you have to
deal with 300 people you know Sherlock
and others will D duplicate the issues
for you um so if you can do a
traditional audit or two before that
that's even better because you get to
have kind of consultation with somebody
and really fix a lot of the things early
on and then when you're like hey I think
this thing's ready to go to mainnet do
an audit contest and you'll find all the
other stuff essentially that's the
goal all right um are there any standard
protocols or platforms for holding these
contests that you can recommend yeah so
I'm the CEO co-founder of Sherlock
Sherlock is one of the the main ones so
I'm obviously very biased um but
Sherlock there's Cod arena there is
immuni does them as well now there's a
platform called Cantina code Hawks hats
so there's a few platforms out there
you any other questions oh we have one
here thank you a this is very
expensive so what is uh your suggestion
small uh dab with the very tie boxes
thank you yeah um if you're if you have
a tight budget uh I would say just try
to keep your contracts as simple as
possible every line of code is going to
cost you money uh when it comes to the
auditing phase and you really want to
pay per line of code like essentially
you need to pay for the best people
because those are the people who know
how to hack contracts and those people
exist on the black hat side like the bad
guys so you need to make sure you're
paying for the best good guys as well to
ensure that you find those
vulnerabilities before you go to mainnet
so if you're kind of bootstrapping just
try to keep your code as small as
possible as simple as possible use other
code that's already been audited if
possible um and when you actually do do
an audit don't go for the cheapest
provider because you really want to get
that top talent even if you have a small
code
base okay that's it thank you very much
Jack thanks a lot
everyone our next speaker is om sha and
he is the co-founder of wallet guard
he's going to show us a history and the
evolution of scams and showing us new
techniques to combat them let's welcome
hi everybody my name is m i was
previously one of the co-founders of
wallard now I do security R&amp;D at
metamask today we're going to talk about
the evolution of scams uh throughout the
crypto space specifically pertaining to
end
users so let's start with some of the OG
scams in web
phase here scams your typical seed phase
Steelers when you end up on a fishing
website you also have those send your
money here and we'll double it I'm sure
everybody has seen this across Twitter
or some of these other platforms and
then you also have some of these other
types of scam methodologies where people
reply to tweets and uh link this way to
uh earn yield um by using this Arbitrage
bot now talking about some of the more
interesting scams in the space that
we've seen over the last couple of years
are drainer
kits a lot of drainer kits actually
started um around May of 2022 uh with
monkey drainer being one of the first uh
drainer kits that kind of originated now
what's really interesting about monkey
drainer and uh the origins of drainer
kits is that it kind of replicates a
business model that you see throughout
the traditional cyber security space for
like Mau as a service but now
introducing it in a different aspect as
drainers as a service so how this
actually works often times is by
approval farming so when the early days
of monkey drainer came about they kind
of uh were very targeted towards the nft
space so what they did was they
leveraged your open approvals that you
already had on assets uh you've listed
in the past on openc or other platforms
and they essentially leverag those
approvals to essentially create a zero e
listing to themselves effectively
draining you of your
assets now throughout his notoriety he
stole around 16 million USD um before
shutting down his
operations and from then uh you had the
rise of Inferno drainer and Angel
drainer which which are some of the
other more prevalent kits in the space
Inferno drainer has stolen roughly
around 80 million in assets employing a
lot of the similar tactics that monkey
drainer had used in the past but also
leveraging newer techniques by using
things like uh potentially over
engineering of certain protocols like
Unis swap for example has a uh
functionality where you can actually
swap to another wallet address um and
the intention behind this feature was so
that you could swap directly into a cold
wallet but now from an attacker's
perspective you can swap directly into
their wallet so by leveraging things
like this you can see um what the pop-up
might look like on wallet guard um this
was an actual uh transaction that was
blocked and the idea was just swapping
directly into the um attacker's wallet
Now angel drainer is another really
prevalent kit um now what they really
employ that's a little bit different
about them is their multi-chain draining
strategy as of recently through efforts
of metamask and the security Alliance uh
Inferno drainer has uh kind of shut down
and starting to work with Angel drainer
um so there have been a lot of changes
and Evolutions in the draining industry
as a whole um but it's a constantly
evolving field and that's constantly
affecting end users given the um idea
that a lot of people sign transactions
without really thinking about them and
what we're really trying to do nowadays
um through transaction simulation that a
lot of wallets use um is trying to
portray to end users what exactly
happens when you are actually committing
a transaction on chain
now Pig butchering and dating scams are
also a massive massive massive plague on
the industry you see you know hits from
like $55,000 to like hundreds of
thousands of dollars so these are very
targeted attacks they typically start on
dating sites like Tinder or whatever
else and the idea is it can be as simple
as a hey message and then lead to
somebody um asking to invest on some
investment platform um often times it
acts kind of like a Ponzi scheme in the
beginning where you uh put money on
there you start earning and then you
trust it and you start investing even
more money um often times they that's
why they call it Pig butchering because
they fatten it up before they actually
take the big hit and take every every
asset you have there now this is also
the um out of all the scam methodologies
this has the highest um amount of return
for the attacker per
hit now security is an Ever evolving cat
and mouse game um but be assured that
there are you know companies like
metamask security Alliance blockade and
many other security vendors that exist
out there that are constantly working on
mitigating these threats and that's all
I have for you today but I'm happy to
take any
questions thank you
questions please raise your hand we're
getting more crowded oh there U do you
want to give it a try I don't think I
can make that
F thanks this might be
embarrassing uh so question about the
future of uh all those sophisticated
techniques and drainers basically um we
discuss the current uh state of them
from your experience and just looking at
you know all the different smart
contracts um that are malicious what is
the future of that like operation um
that malicious octar are performing
where is it all going right now yeah
it's an interesting one because it's an
Ever evolving field like metamask has
released some features as of recently to
do a lot more on
the uh client side detection feature uh
feature sets and it's actually mitigated
attackers very much so to the point
where Inferno drainer has Consolidated
into Angel drainer um and other drainers
have completely shut down and we've made
the barrier to entry for draining
significantly harder than it's ever been
um so it's a constant c mouse game where
when we take out or disrupt one piece of
infrastructure they're going to migrate
to another piece of infrastructure um
you know typically right now we see a
lot of infrastructure being leveraged
like Cloud flare um so some of the
bottlenecks that exist in the industry
for example is you know people like
Cloud flare who aren't taking as active
measures to mitigate these threats um so
it it constantly evolves though so like
if cloud were to do something they're
going to migrate to something else and
uh that's why I called it a cat Mouse
game uh there's a question at the front
lady oh there's one at the back first
okay please um so I have a question what
are the the techniques to for detection
for these malicious transactions for
example what differentiates a malicious
approval from a non-malicious one yeah
so that's a good question question um so
in the case of like Inferno drainer or
monkey drainer or some of these past
draining kits it's actually
leveraging legitimate approvals so like
if you leave an open approval um on your
let's say you have you were on Unis Swap
and you left an approval open for your
uh for an asset you're going to swap um
and you never revoke that approval
afterwards um that approval could be
leveraged to steal your assets in the
future so this is why like having good
hygiene on your wallets by like revoking
things that you don't need um is like a
really important tactic um so like back
at wallgard we released a product called
like our security dashboard and it would
run a whole scan of your wallet to check
like all the different assets you might
have and the open approvals you have so
the idea was that lingering approvals
are not a good thing and if you're not
using that approval you should have it
closed
out um I think the microphone is not
working oh yeah okay there it goes um my
question is essentially it might be a
little bit more philosophical but uh I
feel like there's a lot of creativity
applied on the other side with black
hats how do you feel we can be more
creative from our side in terms of
protecting our assets and being
proactive about preventing um hacks you
know I think a lot of those
responsibilities um security is actually
falling on the wallets themselves um
more and more like one of the reasons
that we were so Keen to do the
acquisition was metamask was because I
truly fundamentally believe that
security should be built at the wallet
level um and it allows like by having
security built at a wallet level you get
to impact transactions at a different
level um back in the days when we were
um operating as wallet guard we were
essentially a browser extension that
would be kind of a companion to your
wallet and as good as it was it wasn't
the level of the stack we wanted to be
at and I think that's why like security
really should be built at the wallet
level um where the transactions actually
being controlled controlled um so taking
control of that transaction life cycle
is the most important thing we can do as
um on The Blue Team side thank you thank
you so much gim let's give it up to Gim
sorry to
oh right we're coming up to the last
half an hour and we only have three
speakers left next coming up is the CTO
of Ledger gim sorry I just pre-announced
his name just now can't get more excited
so he's going to change your mind about
blind signing and he's going to tell you
why defi can't move forward without
clear signing let's welcome
him GM everyone uh I'm Charles G I'm CTO
at lger um and today I'm going to talk
about clear signing and why it's it's
important if you care about security uh
you must have a ledger device uh raise
your hand if you own a ledger
device okay most most of the people in
the room uh own a ler device but would
you sign the transaction raise your
hand you wouldn't but most of you have
already signed the transaction and it's
a big problem because signing a hash is
uh completely insecure because you can't
distinguish a legitimate transaction
from uh malicious payload and um you
might sign away your asset so this is
something we need to fight against this
is what we called Blind signing and
blind signing is simply equivalent to uh
signing a blank check so maybe you are
signing the transaction you want it to
sign but maybe you are s signing away
your assets and unfortunately um getting
scam isn't Fun and this is very real a
couple of months ago W Rex was hacked
signed transaction uh giving away uh
their uh assets only two weeks ago rant
act Capital got hacked same story they
got a malware on their computer they
thought they were signing a transaction
on safe while the malware was replacing
the transaction by a malicious
transaction they blind signed the
transaction and they got hacked so the
attack the attacks are aren't
theoretical at all they are U they are
very real are part of our reality and we
really need to fight against this attack
and the idea for us is to provide the
user with all the information to take a
decision to sign a transaction or not so
the idea is to have something very
transparent completely uh human friendly
and to empower user again Ledger won't
decide for you we just give you the
information and then you decide if you
want to sign the transaction or not and
in this case you will swap your uh your
Matic to usdg everything is uh is clear
and you don't have to uh to guess if the
ash is dangerous or
not the key component for the clear
signing initiative is are quite simple
we have created a standard that is based
on a Jon file so we are asking DBS to
create a very simple Jon file that
explain how to interact with their ABI
and to give like the uh human friendly
name for the different method and uh
parameters we also provide an editing
tool to uh to make this as easy as
possible then there metadata file will
be stored on some public register
registry and for wallets then it's a
matter of um trusting this metad data
file or not Ledger is one of the
trusting Authority for Des metadata file
we sign this metadata file and as soon
as you uh will sign a transaction the
whole transaction payload will come
along with this uh gon metadata file
that allows the hardware wallet to
understand how to pass the transaction
this is how how it works and from if you
are a wallet from an integration
standpoint it's pretty easy uh you just
have to integrate our last version of
the device SDK so to summarize from from
a DB standpoint you just have to fill
this metadata file with uh the tools
that we are providing and for wallets
you simply have to integrate the L last
version of the uh device management kit
and then the clear signing comes for
free um the device management kit is
pretty uh pretty easy to use uh it
allows to discover devices to connect to
the device to exchange data to the
device uh there is also some State
Management that allows the wallet to
know where the hardware wallet is and
and several OS command the visualization
tool is also pretty convenient for dab
developer if you are a dab developer and
you have written your uh smart contract
you will you won't need more than 10
minutes to um to fill the metadata file
and with this tool you can see what will
be displayed on Ledger
devices you should care um we this is
not like a ledger problem it's an
industrywide problem that needs to be
solved we need to fight against the
those attacks we need to rebuild uh
trust in the ecosystem uh we see more
and more sophisticated attacks and that
won't stop here with more Stakes
attackers got get more sophisticated and
we will see more and more um people who
are who are drained and so on so we we
really need uh to solve this problem and
we won't be able to solve this problem
alone so we need your help as developer
dab developer or wallet developer to
make uh this
reality uh here a couple of useful links
so you have the developer portal
you have the clear signing on page uh
you have the GitHub repository and a
blog post explaining how to uh interact
with the clear signing initiative thank
you for your attention and happy to
answer to your
question thank
question okay I have a small question
it's a little bit of topic can I ask you
about after the section sorry uh can I
ask one question when you will leave
it's a little bit interesting for me but
a little bit of topic for now okay okay
thanks okay we have a question
behind um has like open Zepplin
implemented that for like all the
regular stuff like for vaults for
example so we don't have to do it yeah
very good question uh not yet to to my
knowledge we have created the open
standard recently we asked for we
implemented some RFC in order to get
feedback from the community and so
and now we are in the phase where we are
asking different dab to fill the Json
file and the generic parer at the device
level will be available in like a couple
of weeks like in one month something
like this so it will come but to my
knowledge they didn't do that already so
for now it's on H dap to yeah each dap
needs to fill this uh this gon file
again it's it it takes 10 minutes but it
needs to be done by tabs because they
know how to interact with their smart
contract yeah thanks thank you
yeah here um I wanted to ask if this is
if here okay yeah if this is for any
kind of signature not only so signatures
or transactions and if you do some
validation on the shason that the
developer propos or is a totally like
decentralized or something like that
okay very good question so for now we
focused on evm mostly uh so all of this
is valid for evm we will continue the
the work on other chain next year but
for now it's only on evm we are
supporting already uh like uh the
approvals permit permit to EIP 712 and
for the metadata file that needs to be
done by DBS like we have created a a
public repository so anyone can
contribute but when it comes to uh
trusting the metadata file each wallet
is responsible to signing or not Des
metadata file and and Ledger is a trust
like um a certification Authority for
Des metadata file the the the the
transaction that you will sign on your
device if they are clear signed that
means that we have reviewed uh the uh
the metadata file and then we think it's
legitimate thank you any other question
if we have still time for one question I
think there's one there how how do you
sorry how do you ensure the uh integ of
those Json data files so they they they
are simply signed uh by by so they they
can't be
modified I think we have a question
there yeah hello um I'm probably missing
something but what's the difference
between this and npec because I thought
natspec was supposed to solve this
problem which spec Nat spec n spec to be
honest I I'm not aware of nat spec we
have created this specification at the
beginning of the year and we have
discussed with the different people in
the ecosystem ask for for feedback and
so on and U and I to be honest I I don't
know this this specific spec so that
spec is where you embed the intent
within the source code using special
like comment format and uh then that
stuff can get tracked in a decentralized
manner is it does it uh does it enable
to explain how the transaction is
actually uh implemented yeah in order to
pass it yeah it's about three or four
years old I think okay but what what we
have created is a standard that U that
also gives like some form formalism on
how the desent file must be done so that
the device understands it so maybe the
the the differ between what we did and
NP is one this the specification of the
gon file
thanks thank you thank you very much
let's give it up to g c
flro okay our next talk will be um from
Kim Kim is the CTO and co-founder of
blowfish he will be sharing his
experience for simulating user
transactions in the in the last two
years The Good The Bad and The Ugly
all right hello everyone uh so my name
is Kim um I'm the CTO and co-founder of
blish uh for the past two and a half
years uh we've been doing Security
Services for wallets
essentially um simulating and doing
security metrics on transactions before
the users signs them and in this talk
I'll give you a very abbreviated version
of some of my learnings or as I Like To
Call It The Good the Bad and the Ugly of
transaction
simulations uh so starting out with the
bad uh a naive approach to simulation uh
simulating a transaction seems super
easy you do a debug Trace call you can
look at the transfer uh event submitted
you can look at the storage you're good
you can see this transaction transfer 10
usdc you're all good unfortunately this
is not the case because we are in an
adversarial environment and as we heard
in the previous talks there's a lot of
money to be made by circumventing
security tools um so you have to deal
with a bunch of things like malicious
malform tokens contracts admitting fake
transfer events and one interesting
thing uh red pill attacks which is
essentially an attack Vector where a
malicious contract tries to inspect its
environment to determine am I running
inside of simulation or am I running
onchain if I'm running in a
simulation I'll show an outcome that's
great for the user you're getting a
bunch of tokens for free looks great
while onchain when it's executing it's
actually stealing a bunch of tokens from
the user um and the important thing here
is that bad simulation can actually be
worse than no simulation at all uh so
that brings us over to the the ugly uh
which is uh the current state of
simulation that we have in production um
so what we're doing at blowfish is we
have a fully custom evm execution
environment we try to mirror uh the
onchain environment as closely as
possible to eliminate these red pill
attacks uh we look at the actual State
changes we don't look at the events
because that gives greater accuracy the
problem with this approach is that
multi-chain becomes quite difficult we
have a plethora of different chains and
they're all evm similar but not exactly
the same that opens up to a bunch of
problems and red pill scenarios that are
difficult to deal with but does this
actually solve the problem uh
unfortunately it does not because as we
upgrade the tech the scammers also
upgrade their Tech so one thing that
we've been seeing uh in the past year or
so is um a rise in bit flip attacks what
a bit flip attack is is that the
malicious actor the user signs a
transaction then the malicious actor
submits another transaction to front run
the user's transaction
to change some state in the smart
contract which Alters the outcome so
when the transaction was simulated
looked great for the user they signed a
submit it gets front run something
changes the user loses all their funds
and this is one of the most common
attacks that we see in the salana
ecosystem today and it's uh probably
going to get more prevalent in evm as
well as simulation sort of gets more and
more common place in wallets another can
we prevent this with a using a private
men pool not really it makes it a little
bit more difficult for the attacker they
can not look at the public men poool but
if they own the UI they can probably
figure out roughly when they need to
send their transaction to sort of front
run the user in the next block and we've
also seen that they're having quite
success quite a lot of success with this
uh in production uh so what we've been
working on is uh trying to enforce the
simulation results on chain and this is
quite interesting because then we um if
the exec ution on chain significantly
deviates from what we simulated the
transaction will revert so the user will
not lose any funds this is something we
put into production and experimented
with on salana and it's showing a great
potential and it's actually stopping
quite a bit of scammers from stealing
user
funds uh but when you look at it a
little bit closer so when you're
enforcing the simulation results um we
start to think about what does the user
want to achieve that is the simulation
results what they want to achieve and
and that is uh basically an intent
basically a different way of doing
intents so that brings us to the good um
simulating user outcomes instead of
transactions and inputs so intense may
be the way forward to save onchain
transactions but the question is how do
we get there and just like uh the
previous speaker was talking about it's
very important that we have standardized
framework for translating these intent
messages into something a normal human
being can understand so this is a great
opport Unity to show uh what you see is
what you get experience directly in the
wallet where all the user cares about is
I'm swapping one e for
$5,000 and it's going to happen within
one hour or it's not going to happen at
all and I think that this could
significantly um decrease the number of
scams that we're seeing because the
problem today is that users are signing
transactions without a full
understanding of what will happen and
that was a very abbreviated version of
some learnings from the past two years
thank you all thank you
Kim any
questions uh we have one at the
back okay I think we have one there okay
hey I'm Titus from Civic um um who's
responsible ultimately for the
transaction simul simulation is the
protocol the wallet the third party that
like is blocking the transaction who
ultimately is dealing with all this like
in your opinion just so currently how it
works in ourf flow is that the wallet
receives the transaction from the dab
they send it off to us we run the
simulation and we return back the
simulation results uh with all security
warnings if any and then the wallet can
show that to the user before they press
the the sign button so essentially it is
within the wallet's responsibility but a
wallet needs to do a lot of things so
maybe this is something that they do
want to Outsource to
professionals oh so we have a no
okay any more question oh there's one
back there Hi um I tried writing a red
pill bot I didn't know there was a name
for it but um one of the things that uh
I kind of assumed that people would be
aware of upfront is that if I tried to
execute some code which uh depended on
not code which was environment dependent
like the chain ID for example then uh
some uh uh I I I guess would that not be
filtered out by like sensitive
transactions does that does that make
sense um I think so yeah so yes you
could look at sort of what is being
called uh as part of the transaction and
you could have heuristics for this to
try to filter this out that is a valid
approach however then you need to sort
of catch all of them right and there are
some maybe valid use cases to be looking
at the gas price or the uh the base fee
or something so you might have some
false positives so we try to go the
other route and try to make our
environment as production like as
possible instead right thank you
okay thank you Kim thank you thank you
so
much now we are going to have have our
last Talk of the day from chisu he's a
security engineer from fand he's going
to show us the attack and defense game
in the me world let's welcome him
hello
everyone um my name is shei and I'm a
security engineer at Fen and uh for the
for the past year we have been digging
into them world so we have some uh
insights to share to bring some new
methodologies into this world and uh the
topic is how to fund run transaction in
the future so in 2023 we have seen a lot
of fundr Runners has rescued millions of
dollars in the hacking incidents for
example like conf they rescued uh 5.4
million and also bloack and also in the
kyos SW incident they rescued 5.7
million and return those funds to the
protocols these are like white hat
hackers but we are seeing a decline
declining trend for this uh in 2024 and
there are main some some reasons for
that so before that let me go over
around uh about the background of MV and
for running so this is how a
transactions life cycle so on the top
you can see when the user wants to send
the transaction he want to send it to
the Builder first then the validator
then the validator will propose a block
and commit it to the chain but if there
is a font Runner uh when the user sends
a transaction to the Builder the fundr
runner will see this transaction and uh
he when he detects this transaction is
profitable he'll replace the beneficiary
to himself and then add a little bit
more gas on to that so the Builder will
place his transaction in front of the
normal transaction so the you um usess
transaction will be reverted so the
front runner will gain profit from
this so then the role of private M Pool
came they say we will keep transaction
private uh and this is beneficiary for
most parties first Arbitrage are fair
like m boss they want to balance the
pools they find the a better swap path
when and also user they don't need to
suffer from um sandwiches and also the
side effect of this is that hackers
transactions they are protected by the
pr and pool as well uh for example in
the previous examples uh those fun
Runners are not able to Fun Run with a
private
transaction and is fun running de and we
found the re uh answer to this question
is no not on the Block Level let me
explain that so we have seen a lot of
patterns like this it's called a
two-phase style attack so first uh if if
a hacker wants to hack something he will
first deploy a assistant contract and do
some preparation and finally he'll send
another transaction to trigger the
vulnerable function of the victim so to
exploit it um all a mbot or a fundr
runner needs to do is to extract all the
functions of a contract uh by using the
function signatures and call every
function and if it happens to be the
trigger function uh aont runner will be
able to like for run this transaction
that that has not never been sent to the
Builder before
and so it becomes a uh catam Mouse game
between the MV Bots and hackers and
there are like hackers they are they
thought of some like better strategies
to protect their contracts for example
here we have a address verification but
it's easy to buypass all it B need to do
is to add some hints and also if it has
a authentication uh like here you you
have a hash of some uh address uh if
it's compared it's compared to a fixed
hash but all a bot needs to do is to
change that equal sign to a not equal
sign and also then hackers thought of
some more sophisticated uh methods for
example they hide the parameter to uh to
the vulnerable function directly in the
parameter in the function and we found
that the goal is really to find the
input to trigger a profitable path in
the contract because it's already in
contract and fuzzing is a good tool to
do that so what is fuzzing it's
basically generate a random input this
random is not really random uh and then
it execute the program observe and
analyze the execution collect
interesting information and if it's a
profitable path we will exit otherwise
we repeat using the collected
information and there are different
purposes for fuzzing in web two it might
be corrupting corrupting some memory in
web three audio space it might be
breaking some invariance and here we are
really to find a um profitable
path so the the effects really depends
on the input generation here are some
heris uh functions uh or generation
methods we uh want to offer you and the
important thing is about the heris
functions uh these are the that makes
the fuzzing
different and there are some pros and
cons to fuzing for example it's fast
accurate and easy to build a prototype
and also for the cons uh it can be time
consuming uh especially in some chains
that have a very low block time interval
and what we want to um promote is that I
think we should bring more Web Two
methodologist into web 3 for example we
haven't seen sta analis something like
that and we're bringing fuzing also
adding added some ttin analysis and
symbolic execution into our engine and
yeah we're hoping to see more of this
and that's the end of my talk I'm ready
to take any questions thank you so much
T any questions the last chance to ask
questions before the end of today
anyone wants to give a
go no questions okay thank you chi and
that wraps up the day of lightning talks
what an incredible series we had today
and uh thanks you thanks for all
attending and all our speakers and
tomorrow we'll continue so hopefully see
you tomorrow
w oh
