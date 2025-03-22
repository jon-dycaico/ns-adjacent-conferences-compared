w
[Music]
o
n
B
o oh
m
this
he
oo
m n
the
o o o
I'm
o o
you
oh oh
o back
a
GM GM GM
everyone um today is a day two of this
beautiful Devcon in the southeast Asia
my name is Eric um I'm from Africa my
state is Ghana um I've been working in
this ecosystem for the last few years
and I'm building the human layer on top
of ethereum so I know you guys are all
ceps it's going to be interesting and
this morning we' been going to look into
rethinking ethereum account model and
you could have had an amazing better
person to give us this interesting
conversation Dan well who happened to be
a former cev and author of account
abstraction
so everyone help me welcome our first
speaker
[Applause]
will cool hey what's up everyone how you
doing uh this should be a quick talk I
think it shows expert I'm actually not
going to go that deep um so I am a
actually go back okay so I think we
should uh rethink some concepts of the
ethereum account model and also the
account models that we're using on l2s
specifically to scale this for gotten
mechanism to scale I'll go into some
things here really quickly I think
deterministic State addresses and state
access is really important in order to
accomplish this um I think uh there has
been discussions of access lists in the
past that didn't necessarily get enough
traction um but this actually can uh
provide significant scaling indexing uh
improvements and security improvements
to ethereum as a whole um so with access
lists or countless um you know the state
ahead of time that you can touch this
allows for uh being able to uh do things
like uh execute concurrently um since
you know the different parts of a graph
of nodes that you are uh touching this
can be enforced by the runtime it
prevents any
overrides um for example if two swap
transactions are happening through the
same protocol um but the same token this
can actually happen concurrently so I I
sort of think of this as another
mechanism from Mex uh multiplexing
spawning parallel processors um another
way to think about it is um knowing your
IO ahead of time um and or having a uh
essentially a built-in mechanism for um
for sharding as well I think this also
works really well for multiple
concurrent uh uh proposers um this can
of go hands in hand it's really great um
again I I'll go into erc20 as an example
erc20 um sort of represents a massive
Global state that everyone can touch and
anytime anyone touches it this sort of
creates a global lock on the system um
and so uh you know I I sort of mentioned
this so um you know I'll go ahead and
skip this part um so this is like I got
this silly graph here but you can see
there's different parts that are being
touched um and in this case you could
split this up into three different
concurrent um uh processing um or
execution which um can actually make
things really interesting uh from the
security side this is really helpful as
well um I think security and the data
side like once we're indexing and once
we get things to scale and get really
really fast these are things we think
about we don't think about this a lot
currently um in the ethereum ecosystem I
I think there's maybe some exceptions
tjs here um but as as things scale
really big and we get to the point that
we're dealing with like hundreds of
thousands of transactions per second
across all the l2s um actually having
mechanisms that inher apparently provide
better indexing uh via the account model
can be extremely helpful um but again
approved pattern on erc20 is I'm just
giving specific concrete examples
obviously we all know it's a disaster um
you don't know ahead of time when you
look at the shape of a transaction um
you don't know what uh what accounts
will end up being touched you don't know
where the funds can end up being spent
um you don't have a deterministic way to
know what reads or writes are going to
happen if you know this ahead of time um
then this actually prevents a lot of
safeguards that you have to do on the
contract layer um and this is what I
call an account Centric model um I think
we've seen this in um some of the
concepts of like uh move ecosystem um I
think svm has has done this there's been
some experimentation with other models
as well um and varying parts of them are
are um are interesting so um this also
helps for things like memory Pro
programmatic ownership patterns memory
ownership patterns across different um
levels of the stack when we're calling
um when we're uh calling between
different contracts so um yeah so uh
also it's really fast pre-processing
level from security perspective um I
think what's going to happen is we're
going to have a lot of wallets that are
going to look at the fingerprint of a
transaction ahead of time and let you
know without processing on chain um or
simulating on chain um what are sort of
security uh aspects that that could be
vulnerabilities and so this actually
makes this really clean this is where
you can have like a easily readable
format of what your transactions about
to do um yeah that's uh that's sort of
the the thing I I'm all for State access
lists again um I'd love to see this come
back and have this as part of um
mechanisms to make things run
concurrently on ethereum and the LTS and
scale that um that's all any
questions okay
okay thank you well um do we have
questions okay I saw your hand
so that was good so yeah I have this
question like there was a paper
published maybe last year about uh like
access list by some people at U and the
outcome of the paper is essentially uh
the discount is not high enough many
people who are using access list are
misusing it many clients are
implementing it in correctly and so on
and so forth so what steps concretely we
should take to solve those problems
increasing discount or what yeah I I
think in general you need to enshrine
more into the actual consensus on rules
on how access lists can be used um
different different aspects like that
and then also from the security side
it's it's really important and then I I
also think um I I think that particular
study um looked at it comparing to what
the current patterns are on chain um I
think if you make the changes to have a
model like this um some of the
programmatic patterns will change and
therefore will lead to scaling uh
naturally but yeah next
question
okay beautiful so the eth research post
or discussion that was talking about
State access list way back in the day is
cited by Fuel and there's been some
extra thought on that and some
developments are there any differences
between your absolute dream like you
know Pie in the Sky perfect if you were
dictator model of State access and what
fuel is currently running I think what
fuel is doing is elegant um so I think
it it follows a more account Centric
model it's like sort of like in a utxo
model is the way that I see it and with
utxo style models um you have better
determinism around accounts and it's
much easier to see what you're going to
touch ahead of time and what you won't
um so I think with regard to ethereum um
it'll never go to that extreme um but I
think there's good balances to where we
can sort of keep some of the beauties of
the current account model but also have
additional speed and
security thanks last
question okay TJ
hello um can you just Define these lists
and then how do you calculate this list
prior to the transaction happen I never
understood that how do you oh okay um so
basically any state that you access you
can
deterministically write you can have a
hash that represents that state that
you're going to access for example um
and so uh anything that you touch any of
those um State locations would be
referenced via a list of hashes actually
um that's one mechanism to do it there's
there's a bunch of different but yeah
how do you know that without
running um so you have to how do you
sorry how do you get that without
running the transaction um yeah so the
user would run the transaction ahead of
time right um or may run the transaction
ahead of time uh before they form that
and then um it's then it's enforced um
in the consensus protocol if that makes
sense so that means people who are
listening for transactions that are
coming in wallets that are uh trying to
validate the security of a transaction
things like that um know that these are
the things that are going to be touched
and there's no like bit flip that might
happen that might suddenly have it touch
like 10 other accounts that could end up
siphoning funds or do some type of
bridge attack mechanism if that makes
sense okay thank you so much let's talk
later thank you so much guys let's give
a hand of Applause for
Wes and thank you for your amazing
questions like I said it's going to be
interesting this morning our next
speaker is Mark and Mark is going to
talk with us on
universal so encrypted meus a path to
ethereum L1 so help me welcome Mark to
stage uh hello my name is Mark and I
work as an ethereum core developer for
NE mind uh recently I've been working on
implementing the shutter encrypted mle
in the nethermind client uh today I'll
be giving a well- win tour of the
encrypted mle design space and sketching
a path towards enshrinement on ethereum
L1 uh let's start with how a transaction
normally ends up on chain without an
encrypted mle so the user gossips their
transaction in this case a swap from eth
to Donut tokens uh and eventually it
reaches the proposer or builder for this
slot who can decide to include it in
their block
um what's the problem with
this uh the first one is front running
so the proposer or someone else is able
to uh insert their own transactions
ahead of the users front running them um
they know that the swap will increase
the price of doughnut tokens so they can
buy up those tokens first and make a
profit while the user gets worse
execution on their trade um they can
then sell off the token afterwards uh to
make this a sandwich attack Um this can
also be a problem in other applications
such as in an onchain strategy game
imagine you can see your opponent's
moves um and front run them with your
own uh the other problem is censorship
uh this is when the proposer doesn't
include the user's transaction at all uh
encrypted mles are a solution to this so
the user posts their uh transaction
encrypted in a public constraint and the
proposer is required to include all
transactions from the public constraint
in the in a predefined order at the top
of their block um we need one extra
component for this known as The Keeper
whose job is to publish the public key
um and release the secret Keys just in
time for the proposer to decrypt and
include the
transactions um there's a spectrum of
possible keeper designs ranging from
trusted to trustless um in my opinion
only the most trustless of these will be
suitable for the high standards of L1 um
on one end we could have a trusted party
with access to the secret Keys um to
improve on this we could have the secret
Keys be stored inside a secure Enclave
such as Intel sgx this is what Suave
does um with a threshold encrypted mol
such as shutter we fragment the master
secret key between a decentralized
committee of Keepers requiring a
threshold of two-thirds of them to come
together to reconstruct the secret Keys
um finally we have delay encryption
where to reveal the secret Keys you have
to evaluate a sequential function which
will take a certain amount of time uh
this is a relatively weak security
assumption that every everyone is able
to evaluate this function at a similar
speed uh which can be achieved when
specialized Hardware is widely available
um and I think this approach will be
suitable for L1 enshrinement in the
future um now let's consider the design
of this public constraint so this
constraint should be available to
everyone to download and its uh
construction should be as permissionless
as possible so any user can add
encrypted transactions to this public
constraint uh one approach is users uh
posting their encrypted transactions to
cool data uh this is quite
permissionless but cool data can be
expensive uh another approach is users
sending their encrypted transactions to
the proposer who then constructs the
constraint and posts it to blobs uh but
this is more permissioned uh and there
are other approaches here so we could
imagine a uh a random subset of
validators constructing this public
commitment um and there's quite a lot of
overlap here with um inclusion list
designs unfortunately in the worst case
we can never be completely
permissionless uh whoever has power to
decide which transactions go into this
public constraint um could for example
demand demand proof of ofac compliance
um however assuming there is some legal
protection for using encryption and
encrypted mles become the default it's
unlikely this would be a
problem um so there are different
approaches to ordering I think priority
fee ordering seems like a reasonable
solution um in the future once the
cryptography is more matured we might be
able to do more advanced block building
strategies using homomorphic encryption
uh using this we can perform encryption
sorry perform ordering on the
transactions while they are still
encrypted replicating the functionality
of secure Enclave
designs um so how are we going to
enforce proposers to include a
transaction we want to make them choose
between including all of the
transactions in the correct order at the
top of the block or all of them being
invalidated so the proposer would lose
out on all of those tips um there are
two different approaches here we could
enshrine into the protocol so we tie the
block validity uh to correct inclusion
or we could have an out of protocol
solution so we check for correct
inclusion with a smart contract uh in
the long term uh enshrinement would be
preferable but until then we'll have out
of protocal solutions um we've proposed
EIP
change that will support these outer
protocol mles um to check for correct
inclusion this allows a smart contract
to tell where and the block is being
executed uh the final thing to consider
is hiding transaction uh metadata so
when the user broadcasts their
transaction um they can leak information
such as Tim stamp IP address and size we
don't have time to cover this but there
are various approaches that can be used
to hide this information um thank you
for
listening thank you Mark um thank you
for the session U do you have questions
for oh wow interested okay I saw your
hand
first uh um I have one question like um
do your approach going to add the
overhead to the process to include the
transaction into the block actually like
you have to do everything in the rank of
the block time to make sure
there yeah um I think there's there's
relatively minimal overhead so the user
encrypts their transactions um and I
guess it would add one slot of latency
so with shutter when we use cool data uh
we're going to have one transaction
where we post and there can also be an
overhead in terms of gas fees for this
post and then after that um then we just
have to uh decrypt and include that
transaction um and you mention like we
uh the the me uh is all about uh an
deterministic order of transaction uh
but then do you think like you the uh
encryp
pool is something like very overkill for
problem uh um I I don't think it's
Overkill really um I mean yeah we can't
necessarily eliminate meev entirely but
this does give us some uh front running
protection next question okay
yeah hey uh are there situations where
an out of protocol mol cannot protect
against front Runing for example if
there's a chain organization you have
the old block then you could front run
in the next block for the next block
right um so I mean yeah so these
uh I yeah I think um there are some
situations I me with our protocal
Solutions such as shutter like you the
validators have to register beforehand
so you know like which proposers are
signed up to use the out of protocol
solution and the keys would only be
released in in these cases um if the
proposer doesn't include the uh
transactions at all then there's a
chance they could be front run um in the
next one but that's why we need this um
we tie the block valid uh the validity
of the transactions to that slot so no
one can then later include these
transactions but you have potentially
leaked some information um about your
transactions with with shutter currently
proposal are trusted right yeah yeah at
the moment but um I'd say this is like
just a step towards um improving so you
kind of like remove these trust
assumptions
do you have one more question last
question okay last
question okay go
here yeah so around like the user
experience front front end user
experience point of view like how is um
this encrypted mour superior to the
flash BS like in terms of say avoiding
the sandwich attacks
yeah um I'd say from the user experience
perspective there's not really a
difference it just depends on your own
personal like trust model so they said
sort of flash bot protect for example is
like um I don't have the slides okay so
it was like the most trusted approach on
on my thing whereas like we can
progressively move to more trusted
Solutions so that you don't have to
trust FL uh flash Bots to uh do
this all right thanks so much Mark for
this session with you if you have more
questions please you can meet Mark and
then get to Deep dive um thank you so
much let's give a hand of Applause
for wow I'm learning I'm not a developer
but it's getting very intense now um the
next session is going to be um an
amazing man who is going to lead us into
a new session his name is Marcus and
Marcus is going to speak to us on
the universal ECC that is
elliptic curve cryptographic use cases
p256 pre compare in decentralized
Internet infrastructure woo that's even
the topic alone is confusing to me Mark
please engage your audience audience
let's welcome Marcus to the stage
whoa okay uh this is actually going to
be a pretty non-technical talk Believe
It or Not uh my name is Marcus I'm a
metag governance Steward at Yow and uh
today I'm going to try to convince you
that we should implement the p256
pre-compile in the L1 uh first of all I
just want to gauge the audience a little
bit how many of you have traveled over
hands okay hats off to you you guys are
the best okay how many of you guys have
an ens
name okay for those who don't you should
definitely get one today meet me at the
en booth and I'll help you out with that
and uh how many of you guys have more
than one
login across uh different platforms like
your bank accounts social media ET
Etc yeah I do too pretty much everyone
so basically what I'm trying to do today
is convince you that a single
login is much more effective and much
more useful than various ones obviously
right the problem is that um for those
of you that don't know uh there is there
might be a security concern with the
p256 pre-compile and I'm not going to
get into the technical details of that
today I'm just going to try to plant a
seed in your head and ask you to
consider implementing this in the evm if
you are a cordev if you meet up at the
ACD calls please take this into
consideration so let's begin so the
problem is digr what is
this this is a term coined by Douglas
rushkoff and essentially it's the
feeling of having your identity
fragmented across different platforms
and uh this kind of leads to a lot of
tension like internal tension a lot of
anxiety a lot of uh a lot of anger
depression and uh you know this is a
endemic to our terminally
online uh generation right uh so we
really want to find a way how to
alleviate it and I'm personally not of
the opinion that we should be taking
over uh you know drugs or anything like
that to do that there's a more Simple
Solution right um again uh when you have
your identity fragmented across
different platforms it leads to
serotonin and dopamine deficiencies
which leads to all these like really bad
things and uh you do really bad things
once you feel really bad right so uh
fragmented identities are bad for your
health and so uh what can we do do about
this right so what I'm proposing today
is an idea right a hypothesis for a
unified identity
framework and so what this means is to
have more sovereignty more control and
more self-empowerment over your identity
online across different platforms and
I'm not just talking about ethereum I'm
talking about the entire internet right
and uh ens serves as a bridge from web 3
to web 2 but there's a block
right um before we get to that I just
want to reiterate that having unified
identity across different platforms
would lessen the tension that we are all
experiencing experiencing today as a
terminally online generation right
so Universal logins with ens right uh
for those of you who are familiar you
probably connect your wallet and have
your ens set up and you can receive send
payments with your ens it makes it super
easy delightful user experience uh but I
personally would love to for example log
into my Chase account with uh an ens
name I'd love to pay my bills with my
ens name I'd love to apply to college
with my ens name I'd love to do
everything with my ens name and that's
not possible today because the p256
pre-compile is not currently implemented
in the evm and uh there was an EI EIP
that uh eventually became an a rollup
Improvement proposal and that's been
implemented across different
l2s um but essentially the path of 1
billion is actually much easier than we
are led to believe uh it's actually
already there we just need to uh make
this consideration of um integrating the
p256 pre-compile into the L1 um yeah so
that's pretty much it just a seed
something for you guys to think about
for the rest of your day uh here are
some prompts for the Q&amp;A if you guys
want to go ahead and ask and yeah that's
my talk
yeah thank you questions time we got a
question first one okay oh I'll try okay
okay hey what's your name hey my uh my
name is Lance I'm building a project
called Sur and we use uh p256
verification in our project twice one
for web offin and one for TLS notary I
love that we end up spending 600k gas uh
total on these transactions and I was
wondering why hasn't p256 been a
pre-compile since the beginning I mean
it makes sense yeah so that's a great
question um
so everyone here is familiar with uh
Edward Snowden and um I believe that in
uh he's disclosed that there's a
potential back door risk um it's a
pseudo random curve right so the
ethereum uh L1 is a uh it's a ctz curve
so it's determin
deterministically uh conceived whereas
p256 is a pseudo random curve so there's
this concern that the uh there might be
a back door that the NSA or some other
uh agency might have an ability to uh
take advantage of so that has not yet
been proven and there's um there is
evidence towards it not being a
conclusive thing um but I think a lot of
people here um I don't mean to offend
the audience but I think you guys might
be a little paranoid
sorry yeah next question next
question okay we got two
here I triy I tried I
tried hey what's your name hey uh my
name's Brian uh hey Bri I'm just Playing
devil's advocate here why can't we get
the rest of the world to adopt the
caker pardon uh why can't we get the
rest of the world to adopt uh 26 K1 like
the why can't we get the rest of the
world to adopt the p256 curve um or the
K curve oh okay like do the other way
around yes oh man so um essentially like
every uh every Enterprise business has
adopted this uh nisto curve and uh you
know I mean I guess we can like if we
all came together and just uh kind of
created a proposal to do that but I feel
like that would be like an uphill battle
in my opinion but I mean feel free to
argue against that last question guys
let's do this last
question okay I've got a question for
you okay sir um so I'm from Africa Ghana
and before l2s E was like no good area
for most of us I'm imagine paying $10 to
for just a gas fee what the future in
terms of making it easy for early deaths
who doesn't have so much to pay on on on
me gas to be able to use this
seamlessly um do do you mind asking your
question another way I I didn't I mean
how in terms of future for emerging
market like Africa for early deaths who
are not in your level to be able to
easily play with um this particular um
techn that you I me just discussing here
uh are you asking like what would be the
advantages of having this C implemented
for emerging markets yes um I think it's
just a universal thing right like so if
you if we're able to uh log to like
what's your bank account in in Ghana
what's the name of your bank account
well I high go to bank now I use crypto
I use exactly okay so like for example
if like you're able to log in with yours
to your bank account it might be more
easy to access okay versus uh just using
crypto awesome awesome thank you I mean
guys let's give it a hand of Applause
for Marcus thanks
um wow it's getting interesting we have
our next speaker coming up with
interesting topic again and his name is
suya
please how do I pronounce your name
please join me here I don't to M come
come your name how do I pronounce your
name help me pronounce your name please
Su right Su so Su is going to talk to us
about a mobile based light client
solution I love this topic so please
help me welcome Su on stage
hi good morning everyone and so glad to
be here and today I would like to share
about our current work named the Mobi a
mobile based client I'm s hun and
partner of the ABC Labs so ABC is not
just a ventures Capital we are always
make our hand dirty before we make the
investment so that's part of the
investment strategy so this work is
powered by ABC and cisc CC is another
company which are doing really good job
on ZK Hardware solution ation they will
help us to build more efficient status
like client so so the entire blockchain
Community is founded on One Core
principle don't trust verify this
principle served as a foundation P for
the architecture of the blockchain
networks so after the POS so the eum
officially posted their light client
works but fortunately several third
party teams are initially their own
implementations such as Nimbus based on
name and the ler based on the tab scrap
and Hiers based on the rust so however
none of those L CL Solutions cognitively
run on the most ubiquitous devices the
mobile phone right and so our goal is
quite simple we we are working on to
offer and or to e room Community a
alternative a light client can run any
mobile
devices so the motivation so why this is
is technically feasible so as
has advanced significantly we are
already seeing some developers running
local RM on your mobiles and running
light client on the mobiles only require
periodically network communication and
some storage so therefore running a eim
light client on the mobile is entirely
feasible so how to make it happen so our
goal is is not build something new and
we want to build
SDK for the native running L kind for
the mobile for the mobile platform
especially for the Androids so the whole
we don't want to build something uh
already happened so the the whole
architecture is about based on the very
efficient Library called halers created
by x6d and Hiers is based on R and what
we are doing here is to make a cing WP
and to make it as a library for the
Android so our secondary goal is after
achieving the compatible with the eim
midnight and is to make a h function
like to offer light client services for
E all e l to if they provided that kind
of
protocol and so because their time is
limited and we'll share some experience
to make this happened so as we know the
heers is codebase r in the rest so
they're containing a significant amount
of their a synchronized threat and but
Android is on the hand on that hand is a
build right build on their cing and
which running on the gvm so the rust do
not have their garbage collection
mechanisms whereas the gvm has the GC so
this happen a lot of times that results
in the synchronized threat has been
incorrectly garbage collected by the gvm
so it's really painful and more moreover
Android you have some unique permission
protection mechanisms includes the V
various permission Crosser arrows when
when directly invoking involve some
Hiers codebase and uh eventually we have
some long additions so apart from the
basic functionality we have further
expectation for the mobile light client
including but not limited to the
following two directions the first one
is functionality the core function of
the light client is verification right
right but however given the sto storage
performance of the modern devices we aim
to build something called light C plus
so beyond a simple verification we
intended to add some storage compability
for example users could selectively
store some State and histore data of
their s and then you can they can uh quy
them locally and additionally we want to
build some rpcs functionality for use
for other use l client knows this it's
kind of the portal Network and another
part is the entertainment or make it
more smart as we mentioned so in
addition to the light client so mobile
devices now have the ability to run
local RM inference so for for example
Android private local gini inference
apis and we want to explore where we can
combine the local node and local RM
together to conduct some uh something uh
interesting and so here is a demo and I
bring my phone here but due to their
tation if you got interesting I can show
you after after this talk and another
demo is called local RM and I bring the
lamas 3 three billion to the to to to to
the phones and I can show them after the
talk so that's all and about myself I'm
partner of the VC labs and fin year PDQ
and my us about their database AC apps
so thank you
thank you uh Su uh do we have questions
for a friend amazing speaker
here
okay he there thank you this is great
that you're working on like clients in
the the ecosystem yeah um how long does
it take for the client to be connected
to the network and then how quick can
you for example do an eth call and
validate that if you build a mobile
application on top and and how secure is
it at the end maybe you can talk to them
so actually is there is there in
protocol provided a a native function
called G proof and you can use this G
proof to verify the data from the other
client so the heers basically the heers
work as you can verify any data from
untrusted rpcs in a local way because
the protocol cannot be changed so that's
really how to guarantee the security
yeah no I um I understand that I've I'm
in the same boat as you but if you do an
eth call right which you want to do you
want to do a method call you don't know
if the VM that is on the remote site is
executing correctly so do you have a
local VM or like how do you solve that
problem wait I think the like Cent do
not have the local VM they just use
their just use the get proof to verify
their correctness of their mot
tree yeah but with the get proof you can
only prove the storage not the result of
a call yes yes oh that part is that we
want to you to to to introduce the AI
agent part like we use rmm to detect the
whether the core is malicious or not to
help because the light actually the
functionality of the light is very
limited so far so we want to extend
something new that's was this ini yeah
next
question um okay so since you are
working on mobile right there's another
constraint which is power So like um
have like how's the power consumption on
phones running on us
like battery life like how oh did you
optimize for it or so actually we are
working on a benchmark like how many um
C Bas can call on current mobile devices
yeah
okay um a followup to the previous
question about how e call
Works um I so the way how it works is
you have a local evm inside helos they
used the R evm RM yeah and it uses e get
proof to fetch the code yes you can get
the code from the state tree yes put it
in and whenever the evm needs some
storage that um it doesn't have
available locally it is another E get
proof like it's a lot of round trips
there is a lot of latency um there are
some uh efforts on the way to improve
that to make it more compact but if
because the Revan runs locally it means
that you can trust the local execution
and later on if you have seen
yesterday's talk from Justin Drake with
like the redacted title um in the future
once we have CK snarks that prove the
execution and the server can also do
that and we don't need the
local um guys thank you so much uh we
continue this conversation m s backstage
and let's have this conversation going
our time is up thank you please help me
applaud our
speaker uh the next person is going to
be Yanik and Yanik is going to take us
through from Nano seconds to
decades the time scale of ethereum wow
please help me welcome janic
good morning everyone thank you all uh
for coming for being here uh my name is
Yanik
and yeah so one way to think about
ethereum is as this very big machine
that consists of uh different gears uh
that connect to each other that drive
each other uh and that function together
to do what ethereum
does and these gears have different
sizes some of them are very small and
therefore they spin very fast and some
are very big and therefore they spin uh
spin slowly but therefore they um
they're all the more powerful and in the
talk for actually no particular reason
other than I think it's it could be fun
and interesting exercise I want to go
through a bunch of these gears these
processes that make ethereum run and
have a look at how fast they are very
quickly starting with the uh slot time
new slot every 12 seconds we get a new
Block in ethereum kind of the defining
time of of ethereum I would say and now
from there we can go lower um these
blocks need to be prop propagated
through the network that takes about 2
seconds another thing we propagate
through the network is transactions
they're smaller they're easier to verify
um so they propagate much faster takes
about 250 milliseconds to do
that now we reach a boundary 100
milliseconds is about the network ping
time two nodes talking to each other um
they will always have a latency of this
order of magnitude so if we go lower
than that then we're in this purely
local do domain of um um yeah that only
happens on uh on a single node
everything above that can be Network
wide 100 milliseconds is also the time
roughly it takes to execute a block of
course some blocks are bigger they take
longer some are shorter um some are
smaller they are quicker to
execute two orders of magnitude smaller
attestation validation takes about 1
millisecond attestations are these votes
that validat sent to agree on what the
state of the chain is and now we're
getting into a range of numbers that are
very difficult to imagine for humans 1
millisecond is not a very human time
scale so I would like to compare this to
length which might be easy to think
about if we uh if we go back to a slot
and imagine that this is the size of a
human then attestation valid validation
would be about the size or the thickness
of a human hair so quite small already
but we will go even
smaller 100 microc um rough time of an
average transaction to be
executed big part of that is the
signature check of course we want to
make sure that transactions cannot be
forged and that's why we have these
cryptographic signatures and they take a
long time compared to a transaction
execution to
check um but the most probably the most
important cryptographic function in
ethereum in blockchains is hashes we
hash all the time whenever we check a
signature whenever we change State
whenever we build a block we do a hash
and therefore these hashes have to be
very fast and they are 350
nond and lastly kind of the smallest we
can go a single unit of gas gas is the
unit of measure we uh we use to um
measure um um resources uh and one of
these resources is computational time
CPU time and one unit of gases
corresponds to 10 NCS um of CPU
time um 10 NCS again very small to
imagine if we go to um length scales
that's about the size of a glucose
molecule and the most important energy
carrier in biological systems such as
humans we can't go lower than this but
now we can go higher um starting again
nine orders of magnitude above um this
which each valid dator gets to submit
their vote on on the state of the
chain two EPO in a row 12.8 minutes
finality period and that's um in this
presentation at least the longest um
protocol um defined time scale above
that uh we're talking about humans we're
talking about human coordination human
humans are um are um slower so they need
more time uh to uh to coordinate the
fastet that I could think about it was
Emer emergency response times say ether
in breaks for some reason how quickly do
we get developers um online to their
machines to look into what's going on
and 30 minutes is um is kind of the
number I came up with based on a lot
little bit of data of course there not a
lot fortunately because nothing major
has happened so
far uh two days about the time it takes
to s a note hopefully we can get this
down um at some point maybe using light
cins as we saw before two weeks um the
time between uh the all C Des meetings
the meetings where um the core
developers talk about the state of the
chain and um the uh changes they want to
make to it uh to improve it
one year the time between hard Forks
when we actually Implement those changes
in in these
intervals two years the time to include
an EIP so the time between an Pro
proposal to implement the chain uh is uh
proposed and uh until it's included in
the hard for is about two years uh in
past two years also the time between
Defcon so may read again in uh
now and the most longterm features of
ethereum like proof of stake and
charting have been discussed since the
very beginning uh and these long-term
features can take 10 years to implement
and now I originally I wanted to stop
there but for for fun I just wanted to
add another number maybe 100 years maybe
that could be the lifetime of ethereum
if we think about if we compare to other
um protocols like email or social
systems then 100 is is kind of the time
scale we have to think about here and if
we look at these numbers we should uh be
very careful what what we actually
Implement here because it will hopefully
affect a lot of generations after us to
come so yeah maybe that's the only uh
outcome of this talk as well to maybe
make you think a little bit about these
longer time time scales thank you thank
you Yanik um we have questions for you
so guys do we have question for
Yanik oh okay cool
uh uh you mentioned that uh 10 nond for
unit of gas computation also the 12
seconds for a block I don't know if this
is a beginner question or a question but
I ask um when in the future the CPU
power uh becomes more powerful will do
you think will this uh 12 seconds change
to 6
second
um yes or no I think the 12 seconds are
um kind of constrained by um um Hardware
of of um computers but not necessary by
CPU time I think there's other resources
like Network latency that are more
important here but of course if Hardware
improves and physical capabilities of
computers improve then these 12 seconds
can go lower and also the amount of gas
we can spend in a single block can be
improved right now the target is I think
more powerful we can maybe increase this
uh but but also there's other resources
that are measured in gas and they also
have to be taken into account
yeah uh thanks for the talk it was
really cute um you you mentioned lots of
different metrics um I wonder which one
is the most important to be
optimized oh interesting
um uh I think not all of these are
metrics that should be optimized I think
some time scales are fine if they take
longer uh I think some time sces
probably can't be optimized a lot like
um for example I think um the all cord
meetings it would be very annoying if if
people would have to go to a meeting
every day or something like this so um
but in general I think the two years
Improvement proposal that sounds like a
a very long time um um on the other hand
if we compare it to the 100 Years of
lifetime of ethereum then maybe that's
not too big uh too bad so don't not
really have I don't have a clear answer
to that uh I guess the easiest answer
would be like the technical time scales
like inre uh
reducing um uh block propagation times
or things like this but um I think none
of these are very crucial to be
honest all right thank you so much Yan
for this amazing session thank you this
conversation has not ended you can meet
Yanik and have more technical
conversation on this particular team uh
our next speaker is Dr Dr
Leonardo and Dr Leonardo is going to
take us through another
interesting
Journey from not the longterm
decentralized storage for Bluffs Dr
leadoo is an interesting candidate to do
this and it's going to be EIP 444 so
help me welcome Dr Leonardo on stage
thank
you um so good morning everyone uh thank
you for being here I'm Leo I'm a
researcher uh with codex and also from
migal laabs and today um I'm going to
talk about the centralized stret for
blops actually it's very nice that we
have this this talk by janic uh taking
us through time and now I'm going to
take you through
space so um this is yeah the timeline of
uh theum history so we have the Genesis
block that occur in July 30 of 2015 then
we have the merge uh about 7 years later
happen in 2022 during that time we had
something in the order of 15.5 million
blocks uh and if you put all of those
togethers that takes about 427 gigabytes
of space um then in 2024 uh March 2024
we had the the blops the beginning of
the BL the E uh
had something in the order of uh 3 point
something million blocks and then uh
since March until now so about 7 months
ago uh we have been generating blocks
with with blobs all the time right and
in these last seven months we have
generated more data than in the first
seven years of ethereum so that's that's
quite a significant amount of data and
to restore the entire history of of
ethereum right now it takes about um one
terabyte so basically what I'm trying to
say today if there is something that
should remain in your head from this uh
talk is that storing the enre eum
history in every single note of the
network is kind of unsustainable and
there are several things that are being
developed so when if the portal network
but there is also other um ideas and I
want to show one of those um in this
talk so there are some uh files that
have been proposed that there are called
era files uh an era file is a is a file
that stores about no exactly one 8,192
blocks uh this State and also some index
data basically one ER file is about 27
hours and it takes between 500 and 600
megabytes of a space so this format has
been proposed by jask from the if and uh
the panda Ops Team in specifically party
uh took all that uh data from the Prem
merge so it's about 15.5 uh million
blocks and put it on on borrent so this
is the the size of the data during those
uh first seven years please notice that
we have have the blocks are between 5050
to 100 kilobytes toward the end of that
period now if you look between um what
happens after the merge uh the size of
the block starts increasing
significantly and we reach almost 200
kilobytes in um in average for for the
blocks so during that time we have about
almost four million blocks and if you
take all those block together that is
about 98 gabt of data and there has been
this proposal Again by the panda op team
um to create like a a
Bon chain checkpoint sync endpoint where
you can actually checkpoint uh sync your
client directly from of network sources
so you don't need to get all the blocks
from the peer-to-peer Network you get
all the blocks from uh a specific
offchain of network um source and now if
you look at the uh a look at the blocks
after the the the blobs basically uh
there is a new proposal now it's called
the Erb files which are specifically for
in blops and uh there is no no estate on
on those files but there is the kcg
commitments uh included as well and you
can see that during this time the size
of the blocks have uh decreased um sorry
because uh now we're going down to
almost 50 kilobytes in size and so this
is again a proposal by the nimus team uh
and and and I think this is a great idea
and what we are trying to do now in
codex is to store this history from uh
from ethereum in in codex so codex is a
decentralized storage uh that is
protected with the raal coding uh with
very reliable CK technology and we are
storing the entire uh history of
ethereum in in in codex so that's
basically all I wanted to to present
today and if you are interested you can
come to talk to us offline or in the
nimus booth as well thank you thank
you question time I love this part of
the session question time so who going
first oh wow no question for Dr
Leonardo oh wow you a good teacher are
you a professor sorry are you a
professor yeah I work at the University
yes oh no wonder so your students are
saying no question for you
[Laughter]
right oh one question who can I see
you who who is
good no question no question no question
okay so doctor it seems you gave such an
awesome presentation and what do you
tell Dr Leonardo doctor thank you help
me welcome and say thank you to Dr
ladoo yeah so we are going to have just
you can do some yoga exercises whatever
you want to do 5 minutes and we are back
with the only female in this session
amazing lady is going to share with us
something interesting so 5 minutes break
stretch your legs and let's come back to
continue
ah
oh yeah
oo B
see
welcome back and how do you
feel energize how do you feel awesome so
this next session we're going to engage
with an amazing Builder and she's
passionate about cryptography and she's
going to engage us with something that
I'm so interested because we believe
that etherum and blockchain is much more
needed in the frontier Market where I
come from so understand how thing is
going to help the world especially
market like Africa Latin America is
super important and cool so ladies and
gentlemen and everyone help me welcome
Teresa she's going to take us through
what you didn't know about contract
deployment sound very interesting right
so help me welcome Teresa on the team
deployment
hi everyone good morning my name is
Teresa I am a smart contract auditor at
chain
security uh and today I'll talk about
things you didn't know about contract
deployment so uh I suppose many of you
have deployed a smart contract at some
point and this session aims to take a
behind the scenes look at what happened
at this
process um so as a short recap these are
the three ways to to deploy uh to
initiate smart contract deployment on
ethereum so either via the creation
transaction or the create or create two
op codes um all of these will um trigger
the evm um to exe execute the init code
so will it will trigger um constructure
uh execution now the question becomes
what if we want to deploy
contract at an address of an already
existing account can we do that and for
that we must understand what it means
for a cont contract um for an account to
exist so let's um recap that every
account holds a state um we have a state
that contains four Fields uh the nons
the balance the storage route and the
code hash and for account existence
let's go all the way back back to EIP
execution of the init code uh the nons
is incremented by one so this means for
an address um of a non-zero nons we can
say an account exists at that address
all right but uh what what does this
mean what are the implications on
contract deployment can we deploy at an
address with um nonzero noner nonzero
code hash um well we can't there's e P
initiate creation on an at an address
with nonzero nons and non-zero code hash
um what about the storage do we need to
care about the storage route um
interesting interestingly yes there's
also a check on that and this has more
of a historic flavor there are still a
few contracts on mainnet that have um
zero nons zero code has but non zero
storage and these are from before e161
that I just mentioned on the previous
slides all right and what about the
balance um can we create at an address
with non-zero balance yes yes we can and
then um that number of way is just owned
by the address all right um now during
contract construction um there's quite a
specific behavior of the evm um so
usually when you um when you measure the
code size of a contract from within a
contract and externally it should give
you the same size the same bite length
um interestingly during deployment
during contract construction this does
not hold so measuring um the code size
from within and uh from externally will
give you different um values and this is
uh an important detail to
know um and one important aspect I would
also want to shed light on is the the
values xcode hash can take and this is
specifically important if you do eoa
checks using xcode hash you must know um
what states you can be in and what
values excode hash can take so for an
empty account uh so to recap xcode hash
returns um the code hash of the address
you query so for an empty account that
will be um the value on the top right
the Zero by string now if we deploy
successfully to an empty address this
will just take any value the hash of of
of the code deployed um all right now
how can we get from the zero address
from an empty account to the hash of the
empty string this is if you just send if
to a random address where no contract
lives um excode hash will return um the
hash of the empty string and also during
contract construction this will be
returned then from the from this value
you can of course then create on this
contract because the n n is still at
this account uh at this address sorry
because the non is still set to zero so
you can create on that now um I want to
finish off by asking if this is the
complete picture and in interest of time
I'm taking this away for you um well no
you can still still after Cancun this
still holds so you must not rely when
you do an EA check that um once you get
the results of Iran random a random by
string that this will hold because
within the same
transaction contract State can still be
deleted um yeah so don't let yourself be
deceived by the return value of xcode
hash um so in summary we've seen that
for account existence the LA is
incremented and this is done before
Constructor execution we learned that
you cannot create on existing accounts
or in UA and there exists still some
Legacy contracts with non-zero storage
but serer Nots and zero code and for the
xcode has transitions I really encourage
you to try it out yourself we set up
this remix
workspace and uh where you can measure
um the output of the op codes and um
yeah play around with that to really
understand um the transitions thank you
very much for your attention and if you
want to reach out to us I'm happy to
chat after this talk and you can also do
so via the platforms thank you thank you
TAA
question time the one I love the most
who is going first question for oh okay
ah I'll
try yeah so how would this uh eoa Che
transform after the EIP
and then EOS can also have EXT
code um
um not sure could you specify which EIP
uh the 7702 the aop code
EIP um where we can delegate uh EOS to
contract I see um I'm not entirely sure
about that but what is important for for
now during um after the Cancun upgrade
is that within the same
transaction um well you can have a
creation and you can have any function
execution and then still the
self-destruct and that is um I think uh
for right now what is often left out of
site is that um yeah it's still the same
transaction and self can still
occur last
question one more question no more
question oh okay Teresa thank you so
much please help thank Teresa for the
session you can still meet her behind
the scene and engage with her the next
speaker is Dominic and Dominic is going
to take us
through what is hot what's not hot
is not hot well I don't know which one
is hot and which not hot to help us
understand this Dominic will lead us
into it thank you please welcome Dominic
on
stage hello everyone good morning
welcome to this presentation we're going
to see some statistics about e evm
especially we're going to compare some
data um we collected data from 100,000
blocks before last day Devcon and
we're going to see what
changed I'm Dominic BRD one of the lead
Auditors and co-founders at chain
security so let's Dive Right In but
first um I have a question to you what
do you think is the most popular op code
used in the
evm it's push one it's mainly used to
push small constants onto the stack next
is push two um it's for larger constants
and this one is especially used to push
jump targets onto the
stack
um f uh third in row is Jump T this
marks jump test in evm code and you
might wonder why we don't see the jump
instruction itself being used heavily
and this is due to in the evm we have
two instructions to jump jump and jump
ey for conditional jumped and both
together roughly add up to the same
number as jump test overall between the
data sets of Devcon before the bot
before the Devcon bota and before this
Devcon we see no change in the most
popular op
codes moving on to the least popular op
codes um least popular op code is call
code this is basically a less helpful
variant of delegate call and it's used
really few times Only log zero just
emits log events with zero topics and
invalid op codes they basically simply
consume all the gas of the current
context when they are called now prior
to Dev con 7 this changed slightly
create made it onto the list it became
less
popular invalid is still on the list
this one is slightly interesting as this
is one of the op code that is dominant
ated by one single
contract the invalid op codes are almost
exclusively used by the usdt contract
and they have an assert in a Syma FY
they use which uh produces invalid op
code if
triggered now especially for the least
popular op code it may be dis
interesting to discuss some op codes
that do not appear on the list
particularly
self-destruct since the Cancun hard Fork
this op code has basically become
Obsolete and Let's ignore some special
conoc cases here it now simply transfers
all the EO of the account
onwards investigating this we were
surprised that the op code is still
used for in some cases and yeah um even
more interestingly we saw that it's
still there are still gas tokens
deploying new contracts we don't know
why this is still done uh we think it's
due to Legacy code still being triggered
by some contract
let's have a quick look at the new OP
codes introduced since last Devcon keep
in mind that all contracts deployed
before um these op Cod were introduced
um won't use them so all execution you
see here must be from Recently deployed
contracts push zero is already used for
new OP code is already used more than
for example call data load or MO
um you might wonder why T store is used
more than tload because in a typical
reentrancy patternn you have t store T
load T
store now what about
pre-compiled prior to defon 6 EC recover
was by far the most heavily used
pre-compile it was mainly used by open C
cport
contract for signature verification keep
in mind that we only have 11 million evm
transaction now day data set so 2
million users is quite a lot for sh
deposit contract and identity which is
mainly used in Viper for memory
operations now before theyve con7 we see
way less easy recover operation and the
far heaviest users now are permit 2 and
warm hole contract for sh 2256 the
heaviest users are the if to deposit
contract and igen
layer and we saw that Viper popularity
rose and we see this reflected in the
identity op code yeah the least popular
op code interesting here it's one single
contract that does all the Blake two
calls transaction complexity the numbers
of call per transaction went down while
the memory
consump
decrease yeah so super quick summary P
zero is super hot easy recover is US
less and there are more calls per
transaction and we've prepared a blog
post which is not fully ready yet but
will be published soon it will have full
description of the data more plots more
results thank
you thank you thank you Dominic for the
short presentation insightful one of
course um do you have questions for
Dominic oh okay let me try
yeah um it's interesting to see how
create was uh one of the least op codes
do you have a reason or Theses as to why
that is the
case I'm pretty sure because create two
became more common and then the
statistics are split right right yeah
okay cool thanks next question
okay um what can we do with all these
new
findings I think it's uh important for
the core deaths and the people
discussing the EIP stuff um especially
for the op codes
um it's really good for them to see
right at push two a new addition they
recently introduced is really used
heavily and has an impact and
may can have take a look at the
statistic and see what isn't used so
heavily but of course it's hard to
deprecate something right because we
still have contracts relying on them
you last
question okay thank you Dominic for the
session please give him a hand of
Applause oh wow it's interesting to be
within the technical guys I'm kind
of wow um the next
session yeah okay so we do a quick break
and come back at 11:20 so just 3 minute
break to stretch it's going to be more
intense um so 3 minutes break back 11:20
and we continue just stretch
o w
welcome back welcome back welcome back
guys
it's been interesting the next speaker
is going to take us through something
interesting and he call himself a
newcomer in itum and he's a mathematical
Ned I ran away first year in mathematic
class so I didn't do Mass I don't know
anything about mathematics and we have
an amazing person to walk us through
this important topic welcome earlier
he's going to take us through how copy
memory from evm how hard can that be you
could have gotten it an amazing person
than earlier who is a mathematical Ned
please help me welcome him on
stage everyone am I audible thanks again
um good to see you I'm Elan suani I also
work at chain security I can guarantee
this was not on purpose we didn't bribe
be organizers was so nice of them um my
top toic for today is arguably the best
fit for a for lagin because it turns out
it's not that hard to copy him in evm
especially since Cancun uh but yeah
we'll see exactly how much so um yeah
yeah the good the right way to think
about it in my opinion is before Cancun
and after Cancun because since Cancun we
have a new OP code that does exactly
that and it's arguably the best way to
do it but before then you had to
implement this some other way and the
were two main ways to do that to copy
from memory to memory in the evm so one
was to do an M load plus M store Loop so
you would do 32 bytes at a time you
would load 32 bytes from memory onto the
stack and store it back from the stack
to the destination in memory and this
used to be well quite heavy in terms of
code size because it's a full loop and
it also had quite a bad uh gas cost in
terms of um gas cost per memory word
copied uh the alternative was calling
the identity recompile that we just saw
with the last
presentation and while that has a little
less code size because it just a static
call that you can do to the to the
contract still the gas per memory word
is good enough it's only three gas per
memory word that you copy but uh the
overhead is quite big because you have
to do a call so it's at least I think
it's 180 yeah we'll see later anyway uh
since Cancun all our problems are solved
because we have a new OP code that does
exactly that has the least code size
because it's just one op code uh the
least amount of gas so now there's no
reason not to use it and as I'll tell
you it it's very much widespread now so
let's just go quickly over some
numbers uh one way to implement the
mload M store Loop is in software this
is done in a in a quite popular yet a
bit old solidity Library
and because it's done in high level
solidity rather than entirely in
assembly then you see you have two
checked additions a check subtraction
all this done for every memory word that
you copy which adds up to a gas cost of
around
copied which is quite
bad uh then we have the same concept by
implemented entirely in assembly which
is what the solidity compiler will
autogenerate for you it's so it's a
function if you inspect the IR it's
called copy memory to memory with
cleanup I think and yeah it's a tire to
Loop so it has less overhead so over
overall the cost per per memory word
copy is only a 67 yeah 67 gas and the
code size is also much smaller uh then
just to see an example on of how the
identity Rec compile would be used it's
used by C4 library and and also the it's
what Viper used you used to generate to
to copy memory to memory before
Cancun and yeah the cost per word is the
best it's just it's just three words
three gas but the the the overhead the
constant term as you can see is quite
big because you have to make a stattic
call that has also a fixed cost of5
inside and then you have to do some
checks so it's not ideal for for small
for small copies now keep in mind that
we're neglecting the memory expansion
cost because that'll be the same
whichever way you whichever method you
opt
for and and also we're doing this
comparison right now with these off Cod
pricing but keep in mind that those have
changed and will change again in the
future so whatever conclusion on which
method might be the most convenient now
maybe wasn't the same you you wouldn't
have come to the same conclusion five
years ago for
example uh but yeah to to just to be
sure about it now the M Copy op code is
used by by both solidity and Viper uh
for Cancun uh contracts and the gas cost
is the least the code size is the least
so everything is good future is
bright um I didn't have the time to add
the slides to this but from the same
analysis that uh that Dominic and the
other colleagues at t Security did it
turns out that already now uh the M Copy
op code is already used more than the
identity recompile even though it's it's
only new it's only quite new since canun
so it shows that I mean I don't know
exactly how to phrase it maybe there a
lot of new contracts deployed they
already outnumber the N the number of
guess solidity Viper contracts for
legacy so yeah it's it's quite popular
already then yeah I've prepared a remix
setup for you and also if you want to
shoot a message to our sales
representative to get an audit which is
never a bad idea feel free to do so uh
uh yeah I'll take any
questions thank you for the session
please do we have oh wow you have a lot
today I'll
try hello uh you said that the memory
expansion cost is the same in all three
cases yeah but my concern is that with
the loop option if the memory you are
copying is not a multiple of 32 m not
only you may copy memory you don't need
to copy so that's more expansion but
also you may override something that is
outside of your destination like just
after your destination yeah yeah so um
the memory expansion cost is actually
I'm only 87% sure about this but it's
only computed on the number of memory
words rounded up so even if you end up
writing at most 31 bytes you don't um
incur memory exion cost for another
word uh so it is the same if even if you
have write within the same word that
you've already paid
for um then what was your other
question ah for overlapping yeah uh if
in in some of some of those functions
are specified for cases where the
overlap is okay for example in in in the
the U one because I think that one is
only used uh to allocate at the tip of
the memory so there's nothing afterwards
but in cases where that's not okay for
example the library they do special
tricks like they they they round it up
with an M store that's aligned to the so
that to the last bite that you want to
write to and the rest they mask it with
the with the content that's already
there so you're basically writing back
what's already there on the P that
overlaps and on the just on the new part
say the 20 20 bytes you write the new
stuff one more question
ear okay no question I'm curious alas um
so as non- technical person yeah um
being among almost everybody's a
technical here how do you communicate to
a Nobis like me to be able to kind of
comprehend in simple language huh I
think I have an act for it like um
I it just comes natural to me like for
me I don't think I've understood
something until I can explain it to my
mom
so so I guess I guess all right thank
you so much guys let's give him a hand
Applause
wow staying with technical guys for like
five hours already my my blood is hot um
the next Pier is a researcher and a
developer and he's going to work out
through uh a team programmable
cryptography and smart contract
development everyone help me welcome
Shuki on stage thank
you hi everyone thank you for being here
so today I want talking about my current
research program cryptography and smart
contract so program cryptography is more
flexible than traditional cryptography
Styles like uh RC so this time I'm
talking about how to run smart contract
based on offchain execution by zkp and
secure
Computing at first let's talk about zkp
and smart
contract so it is easy to integrate with
smart contract because we have a
solier which en to uh produce a verifier
contract so we can verify the zkp on
chain and transfer asset to any other
appr or something like
that and so we can combine with zkp and
FH and NPC and produce a veriable
computation I will talking about this
later yeah so this section I been
talking about how to integrate with FH
and smart cont
the basic principle of fhe is encrypted
evaluation and only F can decrypt is
just
client so it is difficult to integrate
with smart contract by default if we
using smart contract we need to share
the encryp result and uh also decretion
Key by client side but it does not make
sense to achieve the secure Computing
right but somehow we have a solution to
combine with gkp or
NPC so verifiable FH is a kind of
technique to prove
the fh's evaluation and we can verify it
on chain as I mentioned before we can
use a
cier and m is a little bit different
concept it's SP the decretion key
and share it to the third party like a
smart contract
whatever both of two stuff is so cool
but somehow it is difficult to integrate
the smart contract on top of the proof
of time and the de
problem okay so next section is how to
integrate NPC and smart
contract the concept of MPC is uh
evaluate
collaboratory so each party share on
bits of uh confidential data and cabor
evaluate it and compose it to get the
result so in this time we don't
integrate with smart
contract however I think you can imagine
how to solve this problem you know we
can combine with zkp or FG like that so
verifyable NPC is similar concept of
verifiable fhe so we can prove the
execution of MPC and verify it uh by
smart contract using a b 3
verier and also collaborative snack is
similar to B NPC because we combine the
dkp and NPC but this is different from
you know uh in term of ctive snacks uh
this is just generate proof Cor lat so
user Ena to delegate the proving to
NPC okay so let's wrap up my
session uh I introduce how to run the
smart contract by uh offchain execution
of program cryptography and main idea is
using the Sol verifier and on
verification also we can combine with uh
each PR
to overcome the con or some
Primitives so program cryptography is so
cool and we can ower that isum and
blockchain Technology as well and I
think it is uh we need to more uh try to
some issue as I mentioned before like a
proving time or a datas problem yeah
that's it thank
you thank you shi for the session do we
have questions for our
speaker no question oh
good I sorry I forgot my volleyball
lessons uh yeah I wanted to understand
uh what other implementations are there
like any use cases or example there FH
yeah uh one of the B fh's this case is
kind of evaluation of uh stats like
offchain stats like a bank account or
GPA or something like that I
think next
okay next
question okay all right since there's no
more question I love to give some break
you know when the classroom is stands
like this you need to allow people to
have some time so please you can get up
stretch your legs do some little yoga
exercise just 2 minutes and we are
back at
exactly 11
t
back
I'll run run off to the
welcome back we have two more for this
morning session and the next speaker is
going to take us through an interesting
topic again help me welcome Rim who is
going to speak on verifier
Alliance inside of the contract
verification pipeline these are all
technical Jons right so ladies and
gentlemen everyone help me welcome rain
well hello everyone my name is R I'm a
software engineer at box Scout and uh
which is an open source box Explorer and
today I want to invite you to try to
verify a couple of contracts along with
me uh let's start with
with answering the question what the
contract verification is when you deploy
the contract uh onto the chain it is
represented as a number of bytes which
eum viral machine can understand and
execute and where is there are no
solidity of wiper sources stored inside
the blockchain so when indexers uh index
the contract data all we can see are
those two bite codee values which are
contract creation Cod code and
contractor and time deployed codes uh
but most of the people are not good in
understanding what the in understanding
the raw sequence of bites and what we
usually want to see uh what is
represented in the picture below so we
ask our developers to send those sources
to us and we recompile them and check
that those actually correspond to the
onchain code values and this is the
contract verification and today I want
to to verify a couple of contracts with
you so let's start with the simple one
uh represented by those two code values
here what do we need from the user to
verify the contract first of all we need
the source fil themselves of course and
let's assume that this tricky storage
contract uh is our potential candidate
uh it is tricky just because it has some
magic number before storing it inside
the storage that's it uh also we need
the compiler version which the contract
has been compiled with and the
compilation settings uh with all that
information our next first step is just
to combine all of that into the standard
Json input format uh which has all
information just in one file uh we
submit this Json to the compiler and
what it returns us back is the standard
Json output which is um uh quite big
usually but what is important here for
us is that it returns to bite code
values compiled creation and compiled
rtime code values so what we have to do
here is to just take those two bite
codes and compare them do we match yeah
play matches so that's it uh actually is
it always that easy to verify the
context well let's look at a little bit
more complex example here which is uh
where we used as external library for
making the addition operation and
external libraries as the contract codes
which are deployed once at some address
and when our contracts can link where
addresses
in inside themselves and reuse where
functions by delegate call up code so we
will do the same Transformations as
before and we'll get two up code two
bite codes as well but do we match well
we can see that there is a strange not
even a hex part inside the compiled
creation code which does not M
correspond to the onchain value
so why it happens actually this is the
place where the Library address should
be put at but uh as we haven't provided
it to the compiler during the
compilation it just don't know what to
put inside and uh uh placees some
placeholder instead so and our question
is how to verify such contracts luckily
for us there is a special section inside
the standard Json output which is named
link references and which for each UNL
Library contains
the some information how to where where
this Library address should be placed
inside
especially the first BTE where it should
be placed at and its length which is
always 20
bytes so what we need to do is just to
take the specified offset value uh when
take the next 20 bytes from the on chain
code and substitute it inside the
compiled code so do those two bite code
match now yes we do luy for us so here
we are just verify the second contact
today uh
in general such uh Replacements we name
them called Transformations and those
are some actions which may be applied to
the compiled code uh before or after
during the deployment process and which
changes its bite code a little bit but
which Remains the functionality the same
and there are currently five of soci
such Transformations we know about and
support uh and we talk about the
libraries but where are four more we
don't have time to talk about today but
if you are interested you might just
follow the QR link and uh
see some information about
so also I think the last slide my
presentation title was verifier Alliance
the first part of it and uh I don't I
haven't talked about that a lot but if
you are interested in that part as well
you may be you you're welcome to the
panel which will take place today at
Road scan the members of this verify
Alliance initiative will describe you
this a little bit more and talk about
verification as well thank you I think
that's
it thank you R do we have questions for
R oh
okay is this a mic too this is this is
pretty awesome
actually um why is it so difficult to
have decentralized contract verification
right we we use service walk Scout ether
scan but why after all these years is
the experience still so bad in
general uh
well I think uh it happens a lot because
you have to store this contact somewhere
first of all and we is sour fire which
tries to decentralize the storage
process itself and uh but
actually what is more important here
there are a lot of different formats uh
and uh all like different explorers use
their own format to store this data
inside uh Source uses its own data and
one of the with fire lines initiative's
idea was to develop the schema uh we in
which uh all contact should be started
and uh with that actually we are going
to have a just one database of all
verified contracts shared between
different verification
providers uh and I hope that will help
to increase the decentralization of this
data so we're going to share some Market
dams for that uh op access to the
database maybe and hopefully that will
work all right thank you shoot okay uh
in the verification part for
contracts that use Library looks like we
are using the reference by code from the
deploy BYOD is that
safe uh yes that is safe uh
because after the comparation we've seen
that uh this 20 bytes
the as that the Library address was
assumed to be put inside those 20 bytes
uh
by the contract code itself and uh this
address can be anything actually so we
just take uh the actual value so we
assume that the onchain code is Al
should also contain the Library address
at this place and take it
uh as uh as an well our address so it
it's it's actually safe just because
this offset was in
the standard Json output
section all right thank you so much for
this session please help me appreciate
our amazing speaker
R so too soon we are about to end my
session and the last speaker is going to
talk about something that I'm super
interested in and because I've had some
experience in the past so the next
speaker is Richard and Richard is going
to pick on Firefly build your own
Hardware wallets help me welcome
Richard hi High testing can you hear me
so um a lot of you probably know me from
my slides are excellent um most you
probably know me from ether's JS um but
today I'll be talking to you about
Firefly um our new exciting Hardware
wallet that we want to like get in the
hands of everyone um so keeping eye on
my time I see all the things okay so
what do we have so what is Firefly so
Firefly is an open source firmware open
Hardware Hardware wallet um it's going
to be cost effective hopefully everyone
will get them for free we have like 126
to give out today so feel free to drop
by after and grab one um and it's
customizable you can do whatever you
want with it if you want to like start
your own Firefly competitor and just
take our hardware and our software you
can run with it um if you can produce
this cheaper than us we want we welcome
you do the goal is to get security in
the hands of people everywhere no matter
what and so if you have a more cost
effective or a better way to disseminate
to a group people we can't reach we want
that um so again it's about making hard
worlds fun again um whether you want to
put a game on it whether you want it to
be like a a little animated gif thing
pong uh if you have a crypto Kitty you
really like and you just want like a
harder W that's just dedicated to that
crypto Kitty only forever um you can do
it
ah so assembly originally this was going
to be a like 2hour like assembly thing
so um if you want to build your own
you're starting your own Empire for
Firefly you're trying to take us out
first thing you need is a crew so uh my
parents and my wife over here uh we got
together and in an evening I mean it
took about an hour and a half and I
think we made 200
Firefly um so I mean my parents aren't
super technical and they can build these
things I actually have one here I was
going to build on stage but I think I
will forgo that just because I'm running
out of hands um
so um things you need you need basically
a pile system you need a pile of like
the panelized boards so six fireflies
come per board this is all in a script
in the repository if you want a single
PCB board you can do it and just have
one one Firefly per board if youve got
like a crazy manufacturing facility and
you want like a kilometer square of
these things you can just type those
numbers in and
I mean power to you um so you have a
pile for like your completed fireflies
your displays the
cases and that's really it it just like
Clips together um again it's designed to
be nice and simple we're trying to like
reduce costs to make it easier to do
what you want to
do um right so step one I just I just
cover this you D panel it it just snaps
off and there you go there's your
Firefly
um then you clip your little screen in
I'm not going to do that right now again
lack of hands and it snaps in it's like
a snap fit so it has a nice satisfying
click once it all works um okay so
that's assembling provisioning um so
this is where you might if you were
trying to like compete with us do your
own thing so we have a private key that
we use to sign each device um so the
device generates the private key for
attestation on the device it's never
been on any computer ever um it also is
why it takes like 2 minutes to to
provision device sometimes um RSA is
kind of crazy you basically pick a bunch
of random numbers do some rudimentary
math to make sure it's not obviously not
co-prime um and then you burn that to
the Chip And it well first it sends that
to a signing server which signs it it's
a bunch of like back and forth but at
the end of the day you get like proof on
the device sorry evidence on the device
that it can can use to prove that it's a
genuine device so if you're trying to if
you're trying to build your own uh
crypto Kitty Empire that each crypto
Kitty lives on a device now the device
can prove to the world I am a genuine
device issued by axom Zen
and uh I have not been tampered
with and cost breakdown just for those
that are curious um I mean the costs are
there you can take a look at the big
cost for us right now is the case which
is 3D printed I mean we're doing low
runs of like 500 at a time so uh that's
a huge cost right now but once we move
to injection molded you can imagine that
goes down to like 12 cents that's like
$2 off of the cost so we get down from
$9 to
so there's another like dollar we're
paying so anyways there's places to save
money and we're trying to keep the we're
trying to bring the cost down um yes and
huge thanks to to the ens public goods
working group um their funding helped us
the with the first 2,000 devices and so
we're like 650 out of those 2,000 um so
the next event we'll have another th000
and I that is my talk and I have 10
seconds left but I think there is time
allotted for questions so yes thank you
Rich we got our
first thank you hello
how can you Ure that uh each of the
devices are unique and no duplicates
have being made uh duplicat in what
sense uh in their baked in private key
so uh the private key is generated using
like thermal noise on the device during
the provisioning process we also jam it
full of extra entropy and so it mixes
the entropy we give it and it takes its
own entropy and smushes them together to
like make I mean we could produce
fraudulent devices but that a test
station key is more of a threat to us if
someone else gets it but there's a
digital signing peripheral on the device
that makes sure that private Keys
encryption key is all stored and the CPU
can't reach it like even if you write
your own firmware which you're more than
welcome to do you can't ever get that
private key off like we can't so thank
next okay
thank you this is this is amazing uh if
someone was to try to dedicate some time
to hack either the firmware or the
hardware stack um where should we start
please come see me um we will be I'm
hoping to get a bounty out for I exactly
want to pay people to try hacking it
awes I want you to like if you think you
found a way to like glitch the device or
undervolt it um the devices are
currently based on the esp32 C3 version
rev 0.4
so the glitching issue that affected the
previous esps is not currently known to
affect this but if you can do it I mean
a we would love it and B I'm sure
espressif would like love to talk to you
as well because
yeah um
s yes oh sorry I was just being reminded
off stage uh to check out the Twitter
because it's Firefly pocket um because
that will I should have put on the
slides um because that will be a good
place for you to kind of track all the
crazy things we're working on and if you
if we post a bounty that's where it'll
be sorry I cut someone off that was
asking oh yeah um I have the question
when it compares to other Hardware
wallets but like there seems to be a
dominant player called Ledger how do you
compare to them how would you sell how
would you help us sell Firefly to the
users of Ledger and makes them convinced
we should all use Firefly now so in that
regard I mean I feel like there's still
space for all these players out there
that we're not trying to conquer the
world the goal is not market share the
goal is just I mean providing that
competition that maybe makes them do a
different thing better or uh there's
there's definitely yeah we're we're not
trying to conquer the world um but one
huge Focus we are dedicated to is a
we're ethereum first basically ethereum
only I mean e ethereum adjacent only
obviously like your your arbitrum and
all that work but we don't focus on
bitcoin or those other things um and so
a huge part of ethereum is really
meaningful clear signing like we don't
want the word blind signing should never
occur in your device unless you're
calling a method in a contract called
Blind sign in which case it's a terrible
name don't call your your project than
so yes that's that's the big thing we're
aiming for is like yeah death to Blind
signing last
question okay yeah um not quite a
question I actually just want to say
thank you for ether's J JS you've like
made ethereum
accessible thanks thanks I'll be talking
about ethers on Friday if you're around
and want to hear some Hidden Gem for the
API but aming and then so to see you do
another project like this that makes you
know signing accessible and it's amazing
so thank you awesome
thanks last question okay all right
thank you guys and Richard thank you so
much for this let's give a hand of
Applause to
Richard wow too soon thank you very much
for being an amazing audience we are
coming back at exactly 1 10 my name is
Eric and I'm building the human layer as
developers you need to build with a
human being in front so let's talk about
the human layer we are building in
Africa for this ecosystem thank you see
you again
oh
you o
going
up
to
bu
he you
h
G
o oo
w oh
back oh
oo t
o up
he yeah
e
you w
come
Ole
uh good afternoon my name is Fred I will
be your host for the rest of the day um
I hope you had a a great lunch break um
so so this afternoon we're going to have
a very interesting um discussion the
we're going to cover mainly three tracks
the first one is going to be um um real
world ethereum so that will bring us to
uh 2:00 roughly and then we're going to
discuss uh crypto economics that will
bring us to um 5:00 p.m.
uh and we'll
finish the day with a a discussion
around uh Cipher Punk and privacy um so
uh this day will be comprised of
lightning talks so it will be very fast
um so so we won't be able to use the
mircat application that you've been
using in other rooms will just use the
uh time proven method of raising your
hands and uh talking once you have we
have the mind um so we we'll start
immediately with the the first speaking
speaker sorry uh this is uh Mrs Georgia
rusen she has a high expertise in the
world of web 3 ux and customer Discovery
uh she's previously worked with um the
big names like senen labs and Nia
foundations and she's now a senior staff
ux um senior staff ux researcher at
metamask um and she's now going to talk
about building for the next billion
product validation tactics please give a
warm welcome to Mrs George
erus hello
devcom hi it's a really uh it's awesome
to be here nice to see everybody so I'm
Georgia I'm a lead researcher at
metamask I'm also co-founder at open ux
and I'm here today to share some
Hands-On tactics on getting your product
widely
adopted um so throughout this
presentation I'm going to pretend that I
am a imaginary web3 product but the
story for this product is pretty common
let's imagine we're just some generic
defi protocol with some thousand or so
daily active users and we offer
reasonable in interest rates on stable
coins our core audience is already
adopted web 3 users but we haven't grown
substantially in the last Bull Run um so
we know that earning interest on saving
is like a universal use case but how do
we reach all those users who are not
already
adopted here's uh a typical adoption
curve you probably familiar this will be
familiar to you so you'll have heard the
term crossing the chasm uh why does a
Chasm exist at all uh because the
majority always has a different reason
for using your product compared to your
early adopters they use it in a
different way and they value different
things from it so to cross the chasm
from earli doctors to Major majority we
need to understand these folks and what
it's going to take for them to adopt my
product so the first thing I'm going to
do is look outside of our own Community
um and identify watering holes so these
are online places where people talk
about uh their problem and how they
solve it with other users so I put
myself in the Maj in the mind of the
majority user and I'm going to come up
with 10 to 15 Search terms that they
might use to solve the problem of
earning a decent uh interest rate on
their savings so here's a few I came up
with and I go online and I use these
Search terms I put myself in the shoes
of this user and follow the rabbit hole
so I go outside of the usual places to
find this information away from crypto
Twitter telegram Discord so the point is
finding new users not where they
currently where not there in your own
Community um so you I'm I'm looking all
around the web um these two screenshots
here are from um mountain climbing and
car enthusiast forums with users talking
about savings accounts and crypto so I'm
looking for the language they use
listening to their fears and pains how
they solve their problem in real life
what they value from different services
and coming away from this activity I now
know whether the problem is really big
enough to Warrant a solution and also
what novel marketing channels I could
utilize if I needed
to so um when it comes to pictures your
landing page is doing a lot of work
right my imaginary product has a landing
page already it might work for early
adopters but now I've learned something
about the majority user how they
describe their problems and pains I can
create a whole new experience for them
so I come up with lots of different
versions of our message but tailored
with this new information right not like
this it's going to look something like
this and I find people uh to talk to who
fit my ideal user profile but they don't
know what my product is and I test these
um these pictures right so I'm going to
try five or more vers
all very rough nothing fancy and I ask
them these questions on screen about
about each pitch right uh in your own
words what do you think this is uh what
already exists that does something like
this what might you be able to do
differently if you had this imagine you
tried it and it sucked what went wrong
um and after uh asking these questions
I'm listening for what questions they
have what excites them uh what turns
them off and coming away from this
activity I now know what value
proposition most resonates with the
majority user and what else I need to be
doing to allay their fears and
uncertainties so they'll try us
out my last tactic I'll share with you
in this very brief talk is about testing
the most important moments for users
that will signify whether they will
adopt your product or not so the two
most important factors for adoption are
the acquisition moment that's when a
user chooses to try your product over
others and the retention indicator
that's when the user derives value from
it it's the novel moment it's the wow
factor when they go I made a good choice
here right so I'm not going to rebuild
every part of my product experience and
then put it out into the world to find
that it's just not needed or wanted by
the majority I'm not even going to
prototype every part of the flow and
test it I'm just going to prototype
these two most important moments and
test them with real
users so I mock these up really um rough
in a figma flow right the acquisition
flow might look like a tweet or a blog
post going to a comparison site then my
landing page and from this I can learn
what I need to do to position my product
in a way that will mean that majority
users decide to choose it over the
competition and in my imaginary defi
product our wow moment might be when a
user sees how easy it is to deposit
funds or it might be uh when they
realize how much daily interest they can
earn um so I'll test these wow moments
right and I'm doing this really Scrappy
um if the user gets excited by this even
though I'm embarrassed to show them this
stuff then it means that I'm on to
something so coming away from this
activity I now know does the way we
position the product compel people to
try it out and does our core value
proposition our differentiator matter
enough for people to use it I might not
like the answer I get but much better to
know that now and I can uh iterate on
this and find where the real value
proposition is so lastly I'll just say
some of what I've shared today is humbly
appropriated from Tom kerwin's
Innovation tactics from pipex I
recommend you check it out I'm not paid
to plug this but I use it in my work and
it's really really useful so de
definitely check it out and come and
talk to myself and other researchers
designers and marketers at the adoption
Hub uh today uh so let's up our game
make tactical plays and uh think outside
the box thank
you thank you very much so now we'll
have time for a few questions so as I
said we're not going to use the app I'm
going to uh throw the the mic at you uh
raise your hand if you have any question
questions no nobody wants uh the the
mic no no no question
okay well thank you very much so give a
nice round of applause to Mrs
Geor H one question what I can't see oh
yeah in the
middle sorry
um when you were um testing on on a
bunch of users where did you get the
users you were testing on or the the
age-old where do you recruit users from
come and talk to us at the adoption Hub
there's loads of um routs for um finding
users definitely pitch your research as
user research not as sales um come and
talk to us at the adoption Hub we can
talk about that for
sure thank you very much um so yeah give
a round of applause to the speaker so
our next speaker is going to be uh James
V is the founder of fire eyes and
contractor engineer at open Zepp
contracts he also has experience with
infrastructure given his past experience
at open Zeppelin uh Defender and he's
going to talk about how to unboard 22
million users over overnight using
nonconventional
cryptography uh please welcome give a
warm welcome to Ernesto
Garcia all right everyone how's it going
are you enjoying Decon great so let's
get into it this is a quick presentation
so uh we better go quick let's start by
the agenda we're going to cover three
topics today the number one is a quick
refresher on web2 cryptography because
this is important for what we're going
to talk about number two the Mexican
case for digital signatures I'm Mexican
so I want to share more a bit uh about
this specific use case and number three
what is the status of this very similar
use case around the world in other
countries let's get into it and let's
start with this refresher on web Tre
web2 cryptography for understanding this
we're going to explore public
infrastructure who's familiar with this
topic okay I see some some hands perfect
let's go into it so basically uh public
infrastructure works by having a
certification Authority right this
certification Authority can certify that
a certain private key Either for
encryption or signature is belonging to
someone right for example we can use
this to issue a certificate for a
website if you have seen the green log
before that is basically what it's doing
it can also enable machines and of
course individuals but what is
interesting is that we can also enable
more certification authorities which at
the same time can enable more
certificates for again websites machines
and individuals all right so the most
common use case of this is basically
using the certificate for encrypting the
communication for a website if you are
putting a password on certain website
this is probably encrypted by using one
of these certificates all right now that
this is clear let's get into uh some
particular use case using uh government
certified credentials because most
countries already use some sort of
regulation for certifying uh private
keys for digital signatures so what can
we do about this and how can we use it
to board uh 22 million people let's take
a look for those who don't know uh
basically there is a model law published
by the United Nations in 2001 this is
for electronic Commerce and if you have
ever used your credit card on a certain
website is basically according to these
regulations in this one it is specified
that governments should
issue a certificate for a private key
for individuals so in reality even
before even Bitcoin was invented some
governments were already trying to
onboard people to use crypto for uh
digital Commerce all
right so the important thing is that the
call the talk is called how to unor 22
million peoples but in in reality on
this couple of months before I submitted
a presentation until today there has
been around 3 million more people
certified by The Mexican government
government to use a private key and
these certificates are tracked by some
public data that you can also find I
don't have the source here but I can
definitely share it with you so as you
can say see there are 24 million people
like individual people and around 2
million businesses who already have a
private key that is certified by the
government and already has kyc so we
don't have to ask them for a passport or
a digital ID or something like that they
literally have a private key we can use
and put into an account like using
account obstruction and on board people
immediately to that so the way this
works is in Mexico at least the bank of
Mexico which is the main Authority
certifies the taxes authorities right by
having this uh this structure of
intermediary um certification
authorities more private organizations
can issue digital signatures for
individuals like this literally all my
family and even my aunt understand how
to manage this private key so these
people already understood how to do
basic private Key Management revocation
and these kind of things like recovery
as we all do all right so this is the
interface to generate your private key
as you can see this is pretty familiar
uh this is basically telling you to move
the mouse who's familiar with that to
create entropy right this is run locally
so that means that the account is
completely self- Sovereign even that the
government is certifying it because you
only share the public key you have your
your P key for your own and you can use
this for any legal purpose in Mexico at
least so so just a quick meme um not
everyone is really happy with that
because you know uh there are some
privacy privacy issues related to this
uh but we we're definitely going getting
there at the end of the day people is
already certifying their own private
Keys sharing their passport or some
other way of identity so what's the
status for this around the world all of
these countries have some way of uh
public infrastructure that can be
already used for enable people to use
crypto and crypto Services most of this
is already regulated so if you were
looking for regulation there it is
guys uh some other cases like for
example if you're from from Spain in
Spain you have this this small ID with a
little chip on that that chip includes
another private key and the only issue
with the with this is that these are RSA
Keys which is not recommended anymore uh
but by the NSA on the following years
but we can definitely change that right
so aside from inside instead of this
sorry uh we have been scanning some of
these codes and making a CK proof and
adding some trust assumption to the
process so my call to action for you
guys is just use the cryptography it's
already there thank you so
much thank you for this interesting talk
yeah any question you have any question
okay
try um so whenever you generate a
private key and you use you know entropy
and then like a developer you are trying
to secure this SSH Keys how does it work
from the consumer endpoint in the
Mexican case how do you store and secure
those private Keys you store them
locally um usually if you go to the
office they ask you to have a USB which
is obviously not the best case but the
problem is that I think nobody has like
brought these questions up right so the
more we ask question about it the better
we get right now it's just an USB
so if you H if you happen to lose to
lose your USB you have to do the process
again okay yeah uh but you can do it
online you just need to uh basically
tell the authority to revoke the
certificate there is a mirle tree who
has like all of the all of the public
Keys enabled or disabled so you just put
it on a revocation list generate another
one certify it again you're good to
go next question is over there there is
a security issue in ec20 standard which
was classified as the lack of
transaction handling the issue cost $150
millions of dollars losses since 207 in
Fabian V confirmed that ec20 lack of
transaction handling is a security issue
this was reported to open Zeppelin three
times but you didn't apply any fixes to
your implementation of here2 token why
why is this issue not documented in your
jeub repository and causing Financial
damage to your user okay I think there
is an issue for that it's open so
everyone is pretty welcome to contribute
I think there is not much contribution
on that so that would be my answer
thanks okay any more
questions one over
there hey uh what would you say is the
main impact of the adoption of private
kids for everyone in Mexico I mean not
everyone but but so many people yeah I
guess the main impact is for tax
purposes is is that's what it's used for
and that's why people don't really like
them right but basically you can use it
for uh legal documents and there is some
regulation that specifies how to
transfer digital assets I mean it's not
called digital assets exactly there is
like a some some sort of legal framework
but basically you can put real world
assets fully compliantly using this
Keys thank you very much that was the
last question uh thank you very much
than
thanks
so so our next speaker is Mrs Karen
Karen Scaro um she's the executive
director at the Enterprise ethereum
Alliance as well as a senior technical
program manager at Microsoft and she's
uh trying to um Drive collaboration
between the industry and the ethereum
ecosystem and today she's going to talk
about um EA and the in in institutional
Infinity Garden uh please welcome Mrs
Karen
scalo great uh very happy to be here
everyone uh once again I'm Karen Scaro I
lead the Enterprise ethereum alliances
executive director right now and in my
day job I work for Microsoft so I have a
very uh good hand on how some of the
largest Enterprises are viewing ethereum
today and what can be done to uh
increase ethereum adoption and awareness
in the community so I definitely think
it's worth it to go over what exactly is
the Enterprise etherum Alliance and uh
if you haven't heard about us before we
were actually an organization started
way back in
use cases were going on private
blockchains there was a number of
standards and uh technical
specifications that needed to be
developed in the industry and ethereum
actually put together the largest
consortiums of uh companies to be able
to uh start acting on that activity so
we are a nonprofit membership based
organization that is advocating for the
adoption of ethereum in business and
ultimately our goal is to make it so
clear for business that whenever they
choose to do business in web 3 ethereum
and the layer 2 ecosystem is the very
clear choice that they choose to go with
for where they'd like to build uh invest
their time use cases Etc so core parts
of what we do uh we host uh events
throughout the year that's been one
thing that has uh been a a huge pickup
this year we want to be right alongside
the ethereum community so you'll see us
out at eth Denver
ethcc uh we had a major event here this
Monday with our EA industry day that
I'll talk about a little more uh token
on uh various digital communities as
well we also have technical
specification groups and interest groups
so a key group that we do have is our
defi risk assessment management and
accounting group that published a set of
risk guidelines for Enterprise this year
that's been looked at not only by
Enterprise but also governments around
the world and we had over 15 uh
Enterprise companies collaborating with
web 3 companies putting that together we
have our cross chain interoperability
group that also issued uh their
specification this year and has had uh
implementation as well among different
use cases and
Enterprise and to get into a little bit
about the renewed momentum that we have
because we started in 2017 but uh just
like a lot of blockchain projects going
through the trajectory of what's moved
from uh different Technologies over the
year we uh certainly had a lot of
interest in private blockchains in
based that is our recommendation and our
strong point of view to the Enterprise
ecosystem is to choose public ethereum
for where you want to build um we had
new leadership coming this year myself
Paul Brody from ernston Young that works
very intimately with the ethereum
community on the whole with the uh
Enterprise privacy solutions that ey is
building and at the beginning of the
year we set out to regain this momentum
that we had in 2017 and at the um
conclusion of this year at this event I
think we've largely achieved what we've
set out to do and uh include uh lots of
plans on what to do for the next year as
well so I mentioned some of the things
our groups have done the events we've
participated in and uh the number one
mission that we do have is fostering
this community to improve ethereum
adoption and Industry so why would uh
organizations want to be a part of EA
our membership rate is increasing at a
whole all-time high at this point we
have super high quality members um not
only uh the likes of Microsoft ey JP
Morgan s Tander on the web two side but
we also have uh Circle carpat Key
Gateway uh ens also join in as well from
the web 3 side if you're a web 3
engineering team that wants to come to
Enterprise join us because we're going
to give you the largest Spotlight
possible to connect you with the right
people um you'll see the pictures on the
side from our industry Day event this
year um which we highlighted a lot of
web 3 companies doing work with
Enterprise that um is very significant
and threw out a lot of different brand
names and you can see we brought out 300
people plus to that event with 75 Plus
speakers so it was a very well-attended
um heavy content event that we plan to
do more of in the coming years and we
have strongly articulated points of view
we are are not um coming in with well
maybe choose this ecosystem maybe choose
that we are ethereum based and want to
give Clarity to the Enterprise ecosystem
to join us in doing that so if you want
to learn more uh I have some QR codes up
here about our uh membership and our our
website um and thank you for the time
here thank you very much for your speech
uh we have time for a few
questions raise your hand if you have
any
question I can't see with the
lights one
here catch um thank you hello um working
for Microsoft um just um a question I
have is um what do you think their
intentions are with ethereum we see e
why launching products or trying to
build products in that space what is
your take on
Microsoft uh it's where we want to build
I'll I'll I'll put it that way it's the
strongest ecosystem to align with for
the future of the technology um also
surrounded by the largest ecosystem as
well um so a agnostic of any technology
we want to be aligned in that which is
being the most successful that which is
solving customer problems and aligned
with where the future is so um it and
more prolifically if you look at
Enterprise Cloud environments etherium
has always been the the basis of which
to build there and that's really
significant there there's not other l1s
that have the oneclick deployment for
Enterprise developers uh to build on and
um thankfully ethereum has that uh we
should have a lot more um the more that
you can meet Enterprises where they
build the the
better thank you we have another
question over there yeah I guess it's an
extension of the previous question um
with people like Microsoft and ey
building components in the space um like
Aztec is a privacy preserving layer too
and I know e is doing privacy things on
Main net ethereum um are they sort of on
equal footing or is there some advantage
to say ey being able to incorporate
things a little closer or recommend
things for Enterprise and I guess a
similar follow-up question is uh when
you say ethereum are you talking like
just main net ethereum or you talking
ethereum including layer to yeah um so
first tackle the second question here
the ethereum layer 2 ecosystem so we're
not uh directing people to main net
activities but building in in that which
um uh has ethereum as the settlement
layer of the internet uh and then in
terms of your other question on you know
how do we evaluate uh which companies to
go with a good qu
thought there is we we want to align
with projects that have sustainability
support and a a clear future road map so
um that is something to think about for
Enterprise because once something gets
in production which not a whole lot of
um Enterprise proof of con sets get to
at this point there's a a release team a
maintenance team there's a security team
that all have to be in place to make
sure that that product continues going
for Enterprise um and that's really
significant so the more that um ethereum
based web 3 ecosystem projects can
support that the better because a lot of
times um I would say you know Tech is is
very important The Innovation behind it
Etc but at the end of the day if you
can't support the longevity of a product
in an Enterprise environment um that's
going to be an Achilles heel
so thank you so we have one last
question over here
sorry um yeah uh I have a controversial
question here um so what Microsoft did
with open AI um taking open source
putting into close Source um do you
think it will align with the open source
ethos what ethereum is built upon and do
you think like they will start acquiring
startups building Cool Tech and making
them uh close Source well the way
ethereum in this community is structured
I don't think we could be successful
even if we wanted to um to to choose an
alternative Direction I think the entire
success of uh what ethereum is built and
cryptocurrency in general is reliant on
a open ecosystem so I I'm really
encouraged by that our open source
position is uh pretty strong there's uh
certainly different business models that
uh can be successful around around that
and uh we're keen to explore
that well thank you very much car Karen
uh please give a nice round of applause
to to
Karen so our next speaker is uh Mr Mike
silag he's the founder and CEO of e.
fi
um and prior to that he was the founder
and CEO of top hat um he's an active
angel investor and Mentor in the startup
commun community and today he's going to
discuss what defi founder can learn from
web 2 uh please welcome Mr Mike
sagad
hello uh all right so this is going to
be uh uh a quick one um uh so I I'll try
to go fast but hopefully keep it
comprehensible so yeah my name is Mike
sad founder and see of U ethery uh and
my lens on the uh the crypto space is
that I come from a web to background and
so one of the things that I want to talk
about is what are some of the lessons
that web 3 Founders can learn from uh
the web two
Universe uh so just to give you a little
bit about uh my background uh I got into
crypto super early bought some Bitcoin
back in uh 2011 that's like the actual
confirmation email uh it was about a
dollar per Bitcoin uh at that time there
weren't even exchanges I had to just
PayPal some money to a random guy on an
internet Forum uh which was fun uh then
around the same time I started a company
called Top Hat uh which was a web2 uh
company in B2B SAS so specifically we're
doing um uh education software for
universities so which is a very
challenging Market to be in uh spent
about 10 years uh growing that company
uh it ended up being pretty successful
we got it up to around 450 employees
about 65 million Revenue uh and then
sold in 2021 uh it was a great great
outcome uh and so then I decided to do
pretty much the exact opposite as far as
you can get from education software
which was my first Passion crypto and
started ethery around
well we've been humbled at at all our
success we the number four def5 protocol
uh by by tvl at least about 8 billion in
TBL given current e price um um and yeah
run 30 million Revenue in growing super
fast you know couldn't be more excited
about it uh one of the reasons I would
say that ethery has been successful is
because uh we've taken sort of the
discipline and mechanics of operation of
the business and brought it to the uh uh
the defi world and so what I want to do
is just talk about you know what what
are some of those lessons so you know
the curse of crypto is that there's way
too much money uh in the space uh you
know there's just a ton of gambling
money coming from the great uh you know
casinos in the sky
uh and that actually the effect that
ends up having is crowding out real
product development because it basically
eliminates the need in many cases for
getting product Market fit if you're
doing you know a web 2 more traditional
SAS type of business the the cycle of
that business looks roughly like this
you acquire a customer you get the
customer to give you dollars uh you then
keep that customer by you're providing a
good service then you reinvest that back
into R&amp;D and then the customer is happy
and there's a nice positive feedback
loop uh in web 3 it looks a little bit
of different uh usually you uh you know
you find a project that's really cool
maybe a nice decks uh you launch a token
uh you vest your tokens you cash out and
then you're done uh it's a great
business model super easy to uh make
really you know shocking amounts of
money uh doing it that way but when the
main business model is basically
printing casino chips uh and then taking
a rake uh you know this is why we can't
have nice things so uh so so what I'd
like to do is talk about like what are
some of the principles that you can use
uh to uh to construct uh projects that
actually have some
sustainability and the reason they're
important is because there's actually I
guess what I would say is almost a
science around this stuff uh um uh that
that goes into putting together these
businesses that are sustainable so that
you can answer this question you know is
your project a viable project does it
have some sustainability or is check
check uh or a uh
Ponzi uh okay so here's some quick
definitions so we're going to run
through this really fast CAC is cost of
customer acquisition or customer
acquisition cost arpu is average revenue
per user churn is basically how much you
retain uh you know one cohort of
customers to the next time period net
dollar retention is how many dollars you
retaining from one time period to
another LTV is lifetime value so these
are kind of like the key I mean 's
probably dozens of other metrics but
these are the key ones that you need to
remember and the main question is are
you even measuring these because if
you're not even measuring these things
uh you're you're probably more in the or
you're you're lending yourself more to
being in the Ponzi Camp uh okay so what
is that what is this look like well this
is the the fundamental kind of mechanic
of customer acquisition you spend a
bunch of money let's say you spend
$5,000 to acquire a customer and then
every month you get a little bit of
money from that customer maybe it's a
DEX you spend some money to acquire them
sales and marketing BD whatever and then
the user trades and that generates
revenue for the project over some period
of time until the customer churns at
some point and so at some point you know
you go from negative let's say you spend
$5,000 to acquire the customer and then
the customer pays pays themselves back
over time you go to you know cash flow
positive and then ideally if you at some
point pay back the cost of acquisition
the project actually makes sense so the
the rough Benchmark is that your LTV
divided by your CAC needs to be greater
than three why there's lots of reasons
for that but to be you know a top quti
kind of company you want to make sure
that your lifetime value of your
customer is worth more than 3x the cost
to acquire that customer and you want to
make sure that the payback period is
less than 12 months uh that matters
because it has a dramatic impact on the
growth of your business if your payback
period is like 24 months you're
basically never going to get out of the
trough you're basically the business
isn't going to isn't going to work
whereas otherwise you get a really nice
growth craft okay I'm over time um uh so
the other thing that matters is churn
you want to make sure that you're
growing uh your customer base the the
cohort of customers that you have is
growing in terms of their usage of the
product faster than the customers that
you're losing to the customers that are
churning out uh if you have high churn
you basically Plateau because the
cohorts all kind of compress and go to
zero if uh you have a negative churn
then uh you know it grows really nicely
okay so the first step I would say is in
summary uh you got to measure these
things if you don't know these numbers
then you you're you're going to have a
bad time uh and there's a real science
to this so I encourage you to go out
there and uh uh research about how this
science is put together so that you can
build more sustainable project that uh
have utility thank
you thank you Mike so we have time for a
few
questions y it's a bit
far can I over there behind
you thank you what's your most valuable
customer acquisition
channel uh I think for most projects uh
I mean it's it's X for Twitter um uh
that just you know that that tends to
drive uh most uh most customer
acquisition uh and then Word of Mouth uh
you know there's in in the SAS world uh
there's a parameter called the K Factor
how many customers does each customer
refer so I think in crypto it's pretty
much uh Twitter and and Word of
Mouth hey uh love the presentation thank
you for the pricing strategy 101
reminder that was great as a double
founder in web 2 and web 3 what's your
take on the fact that the majority of
the people in crypto come from like
successful company successful business
school we majority all know the this but
collectively we are not able to do the
basics to deliver insightful projects
I'd love to hear your take on that yeah
I mean I guess I just to uh so first of
all I would say the operating chops in
crypto are pretty low I mean the just
being honest the average founder that
you meet in crypto tends to uh not have
very strong operating chops huge amount
of money wasted um Without Really any
consideration for for Roi uh you know
companies just they're they're not run
super efficiently and so you see
projects that are even some of the
largest projects in crypto that should
be just absolutely printing money uh
that are instead just hemorrhaging money
incomprehensibly a complete lack of
financial literacy people that think you
know token emissions are revenue and
other Insanity um so uh so I don't know
I mean maybe maybe it's because it's
just so easy to make money by doing the
the Ponzi stuff versus doing the the
hard work um you know we're
okay I can talk more about that but I'll
stop
there thank you very much um so please
oh sorry we don't have more time for
questions um so thank you very much for
your time and for this interesting
talk um so our next speaker is Mark
Pascal is the founder of the well-being
protocol um and so he's been running the
first University course in the world on
Theo it's been founding blockchain Labs
it's been a part at met Venture and
today is going to discuss the well-being
protocol scaling localism uh please
welcome Mr Mark
Pascal hello hello can you hear me so my
name's Mark Pascal so for the last few
years we've been thinking about a
problem was really well described in
this book book called the third pillar
uh raguram was the ex head of the Indian
Reserve Bank ex-chief Economist at the
IMF and the way he describes the problem
is that Society is supported by three
pillars we've got the the free market
capitalism company pillar then we've got
the state government pillar and we've
got community pillar and what's happened
is we've had a few revolutions we've had
the agricultural industrial
technological Revolution and they have
fundamentally shifted the power they've
moved the power towards the big
corporates the company pillar the
government pillar and the community
community pillar has
suffered and he argues that this this
shift in power has fundamentally caused
some of the most systemic problems we've
got uh in society today so from the
environmental breakdown to loneliness to
inequality so what can we do to to to
correct this problem because it's really
hard to take away the power from the
people who've got it on the two s very
powerful pillars so what we can do is
Empower community and I guess we've been
reflecting for a little while and asking
ourselves the question could
decentralization help to bring back
Community is there a way to do
this we went down a whole lot of rabbit
holes over the last few years exploring
uh not only web 3 but whole whole lot of
other other tangential things and we
kind of emerged
uh in this point where we started to
imagine imagine if we could uh if a
small hyperlocal informal group in a
marginalized Community could spin up a
micro Collective micro Foundation a
micro Dow as easily as a Facebook group
and imagine if the if that user
experience the uh and the support
network around that made it super easy
for that group to make decisions about
money and imagine if we could scale that
times and imagine if we could also make
it super easy for funders to stream
money into those micro treasuries and
and by funders we mean anybody with a
kid with $10 through to multi-million
dollar
Dow could we cataliz this network of
decentralized Grassroots change makers
with this
mechanism so we got a really exciting
opportunity last year to uh to take a
first step towards that Vision we got
funding from the New Zealand government
to uh work with an indigenous Community
to actually start to reimagine the
community Grant system this community
was a mai Men's Health Group uh this is
a picture of some of the lads here
that's me and my co-founder and some of
the some of the ladies who represented
funders uh and really our brief was to
reimagine the grant funding system to to
create one that supported and empowered
the group the men to solve their own
problems long story short we uh got more
funding from three other government
agencies we built some software we ran a
trial went really well last year and
we're now running trials across New
Zealand Australia and the UK and we
picked up some pretty cool supporters
along the way so a was uh she personally
funded one of our trials in New Zealand
and has been a great support for the
project so what have we actually built
uh we uh we were really inspired by an
article by Jeff EMT who is maybe even
here he Ed yesterday so he's been a real
OG in this space and this article he
wrote a few years ago gave us a lot to
think about but what we decided to do
was to really try and take some of these
quite complex uh governance mechanisms
and to focus on the user experience how
do we turn this into something that real
people can use so what do we actually
build uh I'd love to spend half an hour
showing you the app it's an app you can
download from the App Stores uh and but
what we we and I haven't got time to
show it so here some of the key things
so we but we build in fund streaming
conviction voting quadratic voting
dyamic thresholds workflow delegated V
voting all sorts of cool stuff so uh
yeah so it's out and and we're running a
bunch of Trials across the world using
it so what next so I think the really
exciting thing is that once you've
solved a trust and engagement problem
you have a foundation to build some
really some other really exciting stuff
on top of that so uh micro endowments
volunte Co coordination tools savings
pools all that sort of stuff we get 100%
voter turnout we get 100% uh uh
engagement uh come join us uh we're
looking for funders we're looking for
partners to roll out more trials across
across the world uh and yeah if you want
to have a play afterwards uh just in the
top right hand corner download the app
search for hum hum Community request to
join the Ross Reserve community and you
can do some quadratic voting thank you
very much
you so are there any
questions
y
questions yeah over
there thank you any dpin projects has
been experimented on uh no
yeah hi hi um it was an enlighting S so
the thing what I would like to
understand is um you know when you have
certain of these ideologies um for
example like effective altruism which
could uh you know which is termed as
beneficial to all but over course of
time it get diluted and we see uh you
know bad things happening in the
ecosystems how do we make sure that you
know the essence of what uh we are
trying to achieve using protocol is not
eventually getting diluted and how do we
prevent the Bad actors getting into the
thing that's a difficult one uh I think
I mean what we've done is we've
experimented with uh building something
where we can yeah create a new mechanism
for to stream money the big picture is
we want to create our own Dow and embed
embed the values of the Dow into doing
good and ultimately decentralize our
governance to the communities that we're
supporting so yeah I think uh it being
taken over by Bad actors that's
something that's we are very conscious
of and uh will'll yeah do everything we
can to make sure that doesn't happen but
I think we're we're quite centralized at
the moment we're going to obviously
becoming a dow is a journey uh we're
early on that Journey
so yep so the question I had was that is
there a roll out plan for involving some
of the developing nations as well uh
yeah I mean we're we're sort of say on a
journey we've been talking to people in
Uganda uh Africa and yeah it's really
about building out that Network I guess
one key point I would like to make is
for the the marginalized communities
technology is just one small part of the
solution uh we need Partners on the
ground Partners to work with those
communities and there's there's their
organizations already out there there
are Community Development organizations
Charities so we partner with a bunch of
those in the UK and Australia already we
need to connect with th more of those in
developing nations so they can work with
the communities and effectively we we
support those organizations to run
trials and grow it out from there
yeah question over that
so what did your mayori users decide to
do with your
fund uh they did a whole bunch of things
uh again the interesting thing was so
the the the whole thing is held together
with con Constitution that's a document
that the community make that really
defines the purpose of the fund and what
they're going to do with it that's
pre-agreed and the funer agrees that
Constitution and essentially agrees to
keep streaming money in if the community
had holds that Constitution the the
first trial the M men Health Group T
order they uh they the funer agreed to a
more holistic view of health so in Mai
we have a think
called which is a more holistic view of
health and the funer agreed to that so
the guys they organized trips to the
beach they bought sports equipment they
paid for uh for for nutritionist to come
in they did a whole whole bunch of
things but it was very much their their
decision and yeah and they come with all
all sorts of ideas so yeah
okay uh sorry that was our last question
thank you very much for your
presentation uh please give a nice round
of applause to
Mark um so that was the last talk for
sorry uh so we're going to have a short
break and we're going to come back at
app
he h
o pap
t o
BL
it's o
oo o
oo oo
hello welcome back um so as mentioned
earlier we're going to uh touch the
second topic second track of the
afternoon which is going to be uh
cryptoeconomics um so this is the uh
biggest trunk of the afternoon and we're
going to start with the uh the the first
uh speaker
who is Lisa JY tan she's the founder
economics of Economics design and orus
she's an expert in toen economics and
Defi and a recognized author on the
topic and a guest lecturer at
universities all over the world uh she's
going to talk today about data driven
tokenomics analyzing incentive in action
please um welcome Mrs Dan
hi everyone good afternoon have you guys
had a good
lunch yeah okay fantastic we only have
five minutes and then we have two
minutes for questions so I'm going to go
really really fast going to pay a lot of
attention for five minutes so today
we're going to talk a lot about
understanding econom uh data and how
data impacts economics who here build
economics or who here deals with
economics okay who here are founders it
cares about economics and who here are
Builders great good wow a very very even
split so just a tldr of of economics and
data when people think about economics
people usually think about it in a zero
to one phase when I need to launch a
token when I need to launch my project I
need to think about tokens and how
tokens interact in the space and that's
why a lot of the focus has been which
rightly so things like your modeling
your your agent based simulations your
risk testing your risk scenario analysis
that's a very very big portion at the
same time today I want to I want you to
start thinking about how can we use data
to start understanding how the protocol
has been doing and use data to help
improve the health of the protocol in
every project there two key phases 0o to
one and one to 100 0o to one is when
you're brand new you're fresh is MVP
finding product Market fit going to
Market and there you use a lot of of
economics and to build it's all Theory
based to build out the economics on the
other hand when it's live in your 1 to
live data validated data that you could
stress the system and really understand
how users behave so the challenge I want
you guys to start thinking about is how
how can you how is the data giving us
information about how users are
interacting with the protocol the truth
is that as much as you're building the
the economy you're defining the economy
you're writing out the rules of how this
game works and people are just going to
game the system whether you like it or
not people are just going to game the
system they're going to find loopholes
they're going to find ways to extract
more apy more value and that's fine
that's normal in fact once you launch
the project things are just going to get
more and more chaotic if everything
follows the model and everything follows
the simulations that we built out all
the economists that I know they'll be
really really rich but they they really
economists are quite poor people so the
reality is that it's not like models
it's not like simulation so you need to
be able to balance that and one way to
start thinking about it is using a lot
of sess metric SS analytics things like
average average revenue per user user
acquisition user retention all these
data will will be very valuable and
insightful to understand how users are
behaving and interacting with the
protocol at the end of the day tokens
are just an incentive to to get people
to behave in a certain way so once we
have the data we can validate if users
are really reacting to these incentives
or not and it's fine if they're reacting
to it double down if they're not
reacting to it how do we change how do
we update the rules update the system so
that is the that's the general gist
happy to go into more case studies happy
to answer more questions and I think
there'll be time for
questions do you guys want to raise your
hand and see how far I can throw throw
this damn
thing okay I'm going to throw it and
then you try catching
okay hey good job all right go ahead um
hey everyone Robbie look the well
actually you can talk I talk in this oh
that is crazy did not I thought that was
just a fun exercise we were doing um
exercise got to keep
yes I love your videos I love just
everything that you do um from your
perspective what has been the most
like successful toonomic design in terms
of adoption from a data perspective um
so I know you know for context you see a
lot of um uh tokens you know or just
protocols use LP incentives right but
you know if you look at the data um that
you know Unis swap has put out they
typically aren't very sustaining even
though they might you know cause like
temporal um advancement in terms of what
you're trying to achieve and it seems as
though there are not too many sustaining
toonomic designs that actually drive you
know you know wanted Behavior over the
long term so just wanted to know your
thoughts on that yes very good question
and as an economist the answer is it
depends however there's context to this
it depends on two main factors your
business model and your Revenue stream
if your main goal is to get more
liquidity in there and then you you need
these incentives to bootstrap liquidity
versus you need incentives to keep
getting more people to to interact with
the protocol these are all different
kind of behaviors at the end of the day
the question you're asking is what is
the best incentive out there my question
to you then is what is the behavior
we're trying to incentivize are we
trying to incentivize user acquisition
or user retention take air drop for
example which is a very popular thing
which I'm not the biggest fan of but
it's a great distribution mechanism the
pro the pros of that let's start with
Pros huge user acquisition however the
cons of that is there is lack of user
retention people are there just for the
financial gains and as I said when when
you put the rules of the system out the
game the rules of the game people are
just here to exploit the system so which
is fine maybe you could start off with
with user user acquisition and some air
drops but it doesn't need to run for
such a long time take the data and
understand understand how users are are
reacting to it alternatively it's point
system where you've heard a lot about
and also how do you allocate reputation
to different kind of people so that they
can all and then we can start allocating
it correctly to the right kind of users
hi so uh thank you great talk and uh um
my question is more around the social
aspects of a platform right so H toomics
that it's easy to understand not easy
but I mean it's different to understand
uh rois and things that are more
financial and and like onedimensional
but on social like I'm from graa XYZ and
we're trying to optimize social
interactions and meaningful social
interactions I'm wondering you know some
examples of where this comes in and
where you saw like remarkable examples
of like toomics that work with the
social aspect that's a very good
question because everything that we have
been talking about so far is always the
quantitative because quantitative is
something that we can measure your apys
your tvls all these are some we can
measure and once you can measure that
you can always optimize for that and I
really love your perspective which is
social social is really hard to quantify
it's really hard to Define and one
example will be things like governance
or decision-making protocols so one
thing to to think about or one one
Avenue to start considering is how can
we tie in the the natural way that
people go inclined to which is financial
incentives tied with the social aspect
take poly market for example right the
biggest case study of of this year how
do you use Financial incentives as a way
to Signal preferences and from there you
can start building very very complex
models and very complex decision-making
mechanisms that takes into consider
consideration both the social aspects
and the qualitative aspects and the
quantitative aspects happy to go more
into details later
oh yeah we have another question over
there thank you thank you very much so I
wanted to follow up to the first
question because you said that different
type of activities require different
type of incentives which is uh I totally
agree with that so we have analyzed for
example uh LTI data from arbitrum uh
where arbitrum spent $15 million on
instant devising defis and apps and user
acquisition for them and the thing is
that most of those uh users basically
left uh DBS and Def after 3 months uh
either to move to another program for
example ZK sync ignite which is pretty
similar and is happening right now I
mean it's work in progress so basically
we call these users mercenary users so
what are your ideas and thoughts about
keeping the um renting this users
keeping their retention in the ecosystem
and fighting off also mercenary users
who basically move from program to
program to uh utilize it for their own
uh profit so I'll give you the short
answer first and happy to talk about the
long answer after the short answer is
that these things are something we
cannot control this is just natural
forces of how the market works when
there is green grass the Sheep will just
go there and eat the damn grass that's
just how reality works there's no point
controlling that it's not possible to
control what we can do is to understand
that it's going to exist and how do we
how do we channel the the funds or the
assets the resources to much better
highly better resources so reputation
building understanding like transaction
history are these people mercenary users
or are they actually value creators any
of the day you you are balancing two
things one is value extractor in the
short term and one is value Creator in
the long run and what are the different
nuances within your business within the
protocol within within the foundation
that help to channel towards the other
side of things so there is an aspect of
token there's also an aspect of business
model and Reven Revenue stream that you
have to balance quite a bit
that was the last question thank you
very much for your uh talk please give a
nice round of applause to
Lisa so our next speaker is going to be
Julian ma he's a research scientist at
the rig uh group so at the ethereum
foundation uh using tool from finance
and economics is U he aims to improve
the ethereum protocol and today's topic
is to start contributing to economic
protocol development uh please welcome
Mr Julian m
hi everyone thank you for the
introduction uh I'm Julian I'm a
research scientist at thean Foundation
but two years ago uh I was a volunteer
at Dev connect in Amsterdam so I'd like
to share something that's uh an insid
perspective on how to start contributing
to economic protocol research so first
of all what does protocol research mean
well it means contributing to ethereum's
Future what it is is via decent
calization efficiency or sensorship
resistance using tools from C crypto
economics um to help make decisions so I
think industry research very much is
about research as a tool for decision
making and here it means we need to find
what are the properties that we want for
ethereum so these are normative
questions and then answer these with uh
given these properties what economic
mechanisms are optimal and here you can
see a picture of the scourge which is
part of italic road map which is the
main part of cryptoeconomic research
that we're focusing on now
so where to start it might seem a bit
daunting uh to read the road map because
the road map is about all parts of the
uh ecosystem uh and then if you continue
and you read some other posts uh some of
them may to a bit maybe a bit too inbt I
think uh the best way to start is simply
by finding some researchers who work you
really really like uh and often in their
post they'll say something like these
are limitations of my research or there
is some opportunity for future uh
research here uh and then try to
identify some way how you can extend
upon their research and then very
importantly which is very um important
in crypto is just contact them with them
with your idea because everyone is open
to find new
people so when you're trying to find a
problem make sure to take into account
tractability and innovativeness so uh
tractability means how well can I answer
this question and innovativeness means
how Innovative Innovative is my uh
answer uh and tractability depends on
your skill set if if you've been a
programmer before perhaps something is
uh easier that's involves a lot of
development whereas if you're coming
from Academia maybe you're better at
answering questions of these are the
properties that we want and what is the
optimal mechanism uh to use but also um
find some some trade off there so let's
say that this is the uh optimal Frontier
find some problem that should impr
principle be ideal but
then be aware that uh this is actually
very difficult to do don't spend too
much time looking for the optimal
problem um just get your hands dirty get
familiar with how a Works um and do this
by finding some problem that's maybe not
on the frontier uh but that's at least
tracable to your skill set and has uh a
smart a small contribution as possible
it's important to get to know the
protocol before you start doing
something because the protocol is very
large and very complex um and getting to
know all of it first is simply too too
time time consuming
that being said I think uh ethereum very
much has a culture of just com in
everyone is very open and is actively
looking for active contributors who are
here for the long term and I think this
is this is our unique property as an
ecosystem we want to be decentralized we
want to be geographically decentralized
and decentralized in terms of who brings
which ideas so please just come in so
that was my pitch thank you very much if
you've heard Justin's talk yesterday
about beam chain this will need a lots
of new people looking at various
different sub subjects of the ethereum
protocol so if uh you feel you're
interested uh and you have some idea of
where you can contribute uh and your
idea is maybe not on the frontier but
it's trackable and it's Innovative then
email beam.
chain ethereum.org thank
you so now we have time for for some
questions do you want to okay I can are
there any
questions over there watch out for the
computer
well one very much appreciate your time
I just wanted to ask for the spelling of
that email real
quick um let me see if I can go back or
not no okay so it's just beam
beam.
chain ethereum.org beam doj beam.
chain any other
question no
we have a bit of time so over
there uh hello I'm a researcher from
University and uh in University there
are some ground
to uh ensure researcher can uh do their
jobs so if we want to work with someone
in eum ecosystem how this kind so how
how can we uh uh you know uh
uh make the ground works in the
University because I think the
traditional academic institution are not
accept the etherum F or something yeah
um okay yeah that's a great question so
um for how I can speak a bit to how
grander from etherum foundation and more
how they work in the the broader
ecosystem so first of all in the broader
ecosystem there are lots of places is
willing to give grants uh and I think
most of them are focused in like this
mindset of research for decision- making
um so there would be some specific
question that needs to be answered and
sometimes academic work is a very very
good way to answer this question uh
within the etherum foundation we give
out academic grants uh and they can be
structured as grants or as gifts um if
it's incompatible your with your
University I'm sure we can work um
something out um the the application
process is usually a bit different so uh
proposals don't have to as formal as
they are usually in Academia uh but
again they I think the most valuable
ones for us are clear like that you have
some understanding of how the protol
works for your question so it's clear
that the question is tracable and it's
clear what the contribution is so what
is the decision that you're trying to
motivates or what mechanism are you
proposing thank you uh there's another
question in the front thank you for the
talk um you use the term economic
protocol is is the same as talking econ
iomic design or is
different um I would say um the the
terms that I use in this slide are are
not set in stone uh so um we would be
open for uh research in various
directions um so yeah I wouldn't adhere
too much to what what's like the exact
words in the slide uh we be open to uh
any economic uh ideas that you have for
ethereum thank you we have time for one
more question
is there any any more
no okay well thank you very much for
your
talk yeah uh no still have one no this
one so yeah can um
have a 3 minute break and we're coming
back at uh 310
tle
and we're
back we're back so um the next speaker
is teron he's passionate about open
source and has been involved in the
ethereum protocol development since
he's focusing on epbs today's going to
talk uh about exploring auction
mechanisms in protocol design uh please
welcome
ter all right hello well first of all
thank you Julian for the wonderful talk
I think it's a nice segue to what I'm
going to talk about so um disclaimer I
am just an engineer I'm not an economist
I'm not an out theorist so this is based
on my intuition basically but yeah let's
see let's see how it
goes so I guess this was originally
supposed to be a 20 minutes talk but at
the end we shorten into five minutes so
I'm G to try to speed run it as fast as
possible but I guess the high level I
want to cover is that of the what how
and why of different um aen design in
protocol today and I want to make some
specific implication of like different
protocol within each option so so
basically we we'll do some case studies
so we so today we'll look at layer one
and then we'll look at Layer Two so for
layer one we'll look at MB boost we'll
look at EIP 7732 and then we'll look at
EA and ET ALR and then on the l two side
we'll look at first conf first serve
part uh PG and then time
boost so uh for each category we like we
will look at what is being exchange like
who is facilitating The Exchange and
then we'll look at who captures the
profit and then we'll look at when the
auction conclude and reveal right so for
M boost is what we known today right and
then if I'm Alice wants to um build a
block block through Bob the Builder I
have to go through the relayer and that
is aop political trust and this is what
we have today and then another thing is
that it doesn't scale long term because
of every one place timing game these
days because of that this creates
further friction for further updates
that P does and fossil and then moving
forwards that we have EIP 7 732 and then
this changes the trust assumption
therefore you only need to trust the
protocol the protocol guarantees
unconditional payment and it guarantees
Builder safety and then even within 7732
there are different designs such as
block auction and Slot auction and each
of them have like different tradeoff for
example like for Block auction you could
have like a DA problem because of the
hash gets committed first but then the
six Saturns gets revealed nothing gets
revealed you may have a cancellation
problem as well for example if the
Builder commits to something and then
the price goes over the water and just
doesn't reveal right and then slot
aution has its own problem slot
auction's problem such as that like you
have to try uh if you slot aution that
you may have an advantage by using the
relayer and then but then at the same
time there probably is less transaction
inclusion time so here are mostly trade
space that like between 7732 that like
it's probably worth thinking more on
like the comparison between slot auction
and and the block
auction then there is EA and ET so both
EIP 772 block aution and Slot aution
consists of like a timing game which is
possible but then the idea of EA is that
instead of like just in time for the
slot off you essentially uh do the ALR
that's further ahead of time this is to
reduce timing game and then for et
basically instead of proposer choosing
the Builder you have this protocol that
essentially issues the ticket and then
because of that you can enable like me
burn type of design but that also opens
like concerns about about like multislot
mbv so finally like let's jump from
layer one to layer two right so today
layer twoos there are even different
alra mechanism and then most of them are
conducted through a centralized
sequencer and that is easy in a way that
sequencer is trusted so you have this
private mut guarantee and then it's
straightforward to reason about and then
you can do do this very fast because
like users love the ux of like Fast
confirmation right and then who collects
The Profit typically it's the company
that's operating the sequencer or it's
the Dow depends on how like
decentralized that uh like basically
basically how decentralized the layer
two is and then within different like
option of layer two there are first
first serve there are PGA and there are
time boost and within and then basically
like within each auction there are imp
implications on how it affects
developers stabs and stuff like that and
ux so I guess like the takeaway here is
that like the ALR design is like such a
like fascinating space it's such a
profound space he he basically realiz
Engineers to work closely with mechanics
and designer with like G the
with with like with the economists and
many more so yeah if anyone is
interested in this type of design like
please talk to Rick please talk to like
people and yeah thank
you thank you very much um so now for a
few questions please raise your hand if
you have any
question no question
okay well thank you very
much um yeah so the the next talk has
been cancelled so we're going to be uh
n oh
o ooh
I oh
and welcome back um so the next lecture
is uh about well is um next speaker
sorry is Christopher Schlegel he's a
researcher at flashboot he's an expert
in Game Theory and mechanism design
and today he's going to talk um about
civil proof mechanism please welcome Mr
Christopher
Schlegel all right um here we go I
wanted to pitch my favorite theum of
that join work with our brilliant intern
flash Bots mingau and akaki over there
and I want to also tell you a bit about
how it relates to ethereum road map
stuff like PBS and so
on so here's a question have you ever
wondered can we have a decentralized
builder
Market um under any any mechanism that
we can use to to to select a proposer or
Builder and how can we make this
question more precise so how can we
think about it from first principles and
we wanted to turn it into a mechanism
design questions so we're wondering okay
could we have an allocation mechanism to
select a proposer that proposes blocks
and we operate in a per list system so
we worry a lot about cbls right and we
want to be distributed or decentralized
we don't always want to select the same
proposal okay that's minimal requirement
decentralization question is is there
any mechanism we're doing mechanism
design so we asking not any specific
mechanism can there be mechanism that do
that okay um Bitcoin has solved that
problem in some sense right so you do
proof proof of work is a mechanism
problem with that one is if you have
private value and in ethereum certainly
there's private value of proposing
blocks right we have even a secondary
markets for pro proposing blocks called
me boost if there's a secondary market
for proposal rights it means people have
different value otherwise there wouldn't
be a secondary Market okay so and that
value might be private information to
people right because there's things like
payments for order flow or there's
private order flow that people use to
produce blocks or they do searching the
builders and so on right so there Ample
Ample reasons for for private
information private value mechanism
design in in the end has one Insight if
you want to learn anything about
mechanism design that's that that thing
it all depends on private information we
want to elicit private information from
uh participants in the mechanism right
and so we turn turned ethereum roadmap
discussion into a mechanism design
problem okay and then we can ask
questions about it in a formal way can
there be any incentive compatible
mechanism that selects proposer classic
work from the 80s we know exactly what
are incentive compatible mechanisms for
the setup uh so-called monotonic
mechanisms me has told us about them
here are some examples we run an auction
we run a lottery we run a lottery
proportional to your value and so on Etc
PP it's huge space of possible
mechanisms that you can do but here's a
here's a Twist if we add this
requirement of permissionless of the Cil
proofness then basically only one
mechanism survives right and that's a
that's a punchline of the
paper there only one mechanism it's an
auction so we have to allocate through
an auction and it's super centralizing
right that's what we know about auctions
so in other words can we have a
decentralized builder mark Market
basically any Market structure with
significant private value will lead to
Builder centralization right so think
about the gazillion proposals that are
around there of restructuring the
Builder Market or restructuring PBS or
um doing a Testa proposal separation
theorem and principle applies to that if
there's significant private value
probably we run in a pretty centralized
Market
okay let me add some Reflections on on
this private value assumption and then
let's open it for discussion or
questions so why is a private value in
Block proposal and how does it link to
Market structure so that is that that is
a question you might ask um so private
value comes sort of from from private
orderflow and as I said Searcher
Searcher Builder integration in ethereum
so how would we deal uh so how would we
remove it from the market structure if
we cannot have a decentralized market
structure with private value maybe we
want to allocate rights in in advance so
that's one one class of proposals so
this execution tickets or U execution or
or even P POS you can think of such a
system or we could put constraints on
the proposal so things like inclusion
lists or like multiple concurrent
proposals they trying to go that route
okay first proposal um allocating rights
in advance I think there is sort of many
people have made this point that
probably one downside of that is that we
naturally have a secondary market so we
replicate the market structure in the
secondary Market which is super
centralized that's basically the status
quo so I think there's no way around
that that's my opinion a to take and
constraining the proposal I think some
of the proposals like inclusion list I
mean they make sort of the bad effects
centralization uh less bad but certainly
they don't remove centralization and
then we can think of other other
proposals like mCP where in principle
also our theorem applies so there we
would also expect Market concentration
unless maybe there's a very smart way of
constraining the Builder in these
proposals I'm running out of time
opinion to
conclusion ah centralization is the
thing we have to deal with it and maybe
one route out out of it that's the
flashboards proposal I guess is
modernizing decentralizing the Builder
Builder role the Builder stack always
think very very uh long and carefully
about other other designs
okay paper here scan it yeah sorry it's
gone
no it's on archive
okay well thank you very much so we
have we have time for a few questions
raise your okay
thought thanks for the talk um can you
repeat the name of the paper
it's called on simple proof mechanisms
thank you so much thank you for Shilling
paper any other
question please raise your hand if you
have any
question over
there what do you think of block
Building inside a
te did we hire you to chill these uh no
only
recently this wasn't planned I I'm very
bullish on on block Building inside of a
te obviously because that's one way of
so here's here's the thing right so if
you have this Market structure that will
naturally to to build a centralization
then we want to maybe constrain the
Builder the powers of the Builder and
one way of doing it is using cry
cryptographic tools or programmable
privacy tools and yeah definitely is one
of those
Solutions one over
there so uh if uh every mechanism
eventually ends up with a centralized
block Builder why when we look at other
chains like salana do we not see just
one big block
fer we see a few right is the answer so
we see a few so that's that's that's I
mean do you call Solana block building
decentralized I uh I'm the one asking
the questions
here so so is the idea that is the No
but but but I'm I'm I'm questioning sort
of you you you say a theory is rejected
I'm saying is it really rejected well I
think I think uh no one would uh agree
that salon's blocks are being built by a
single entity I also didn't make the
claim I just said we we have a
centralized uh centralized Market
outcome and when does a market become
centralized what is a when does it
qualify
centralized um few few um few Builders
building all of the
blocks thank you and the punchline of
the paper you know there's no clever
mechanism that that can solve that you
have to solve it so other
ways okay well thank you very much I
give a nice uh Round of Applause to
Kristoff so our next speaker is going to
be uh Dr aaki mamag he's a PhD in
computer science and a postdoc senior
researcher in
microeconomics um is currently working
on economic issue of blockchains rollups
and he's going to talk about latency
advantage in sex Dex Arbitrage uh please
welcome Dr
M so hello everyone welcome to the
presentation today I will talk about me
capture
Through Time Advantage Arbitrage so this
is the title of the paper that we wrote
together with at Fon Robin FR Maria
Silva and beniamin leitz and this is
different from the title in the of the
session so take your time to take a
picture or write it
down it will be gone I cannot go really
back so initially I submit it as a 20
minute uh presentation but it was
demoted to 5 minutes so the only thing I
can do is to motivate you to read the
paper and I hope I can do
that okay so main part motivation so we
tried to understand what time boost does
to me and to give you very quick
introduction in the time boost this is
uh selling fast lane license that allows
one player to have 200 millisecond
advantage over all other players and
this Advantage lasts only for one minute
and after 1 minute there will be another
auction then advantages of course assume
achieved by delaying all the other
transactions by other users and we want
to understand the Arbitrage uh between
Auto market makers and outside
markets so we have a lot of assumptions
in order to derive our few the
theoretical results and uh many
simulation results so we assume that the
uh in the outside markets uh fees are
very low or let's say zero and the price
Discovery happens on the external Market
on the IMM that is on the chain it's
only Arbitrage transactions of course
there are some noise transactions as
well but we assume that they can go into
into both directions so they cancel the
effects we also assume the efficient
market assumption which is that the
price depends only on the current so
price change doesn't depend on the
previous price changes so it's a pure
random
process which is of course not true in
reality and we even observed on the data
that it's not true uh so the model looks
like this we have this one player that
has this time Advantage during time T
there are two assets one risky asset and
the numer rare think of as ether risky
asset and numer rare USD or the other
way around the amm has a trading fee and
the risky assets price changes on the
outside market so initially we assume
initially of the simulation we assume
that they are the same the prices are
the same and then once the Arbitrage
report Unity arises on the outside
market so price moves then arbitrager
needs to decide when to capitalize on it
and we assume that it has only time
Advantage time so after this time passes
uh opportunity will be taken away by
other arbitragers and this is a
conservative assumption for the uh
Arbitrage
value so this reduces to an optimization
problem so we have time advantage
arbitrager and we have three parameters
that give a state what is the current
price difference relative time so price
difference how much time passed in this
millisecond and how much time passed in
the total period time and we need to
decide between trading so taking the
Arbitrage or
waiting and the punchline here is that
dynamic programming solves this
problem and with then dynamic
programming we simulated on the real
data so we took uh let's say ethereum
usdt Market on the binance and with step
size 10 millisecond we have Advantage
window 200 millisecond and total time 1
minute and we can calculate for each
point internal Point uh uh we can
calculate what is the optimal move and
also what is the uh um average gains
average Arbitrage value and we obtain
the observation that waiting till the
end of this uh Advantage time is mostly
optimal but not always so there are some
cases when it's not
optimal so I will not give you any
numbers uh because that's the only thing
that people remember in the end how much
uh money time boost makes with these
assumptions but it gives some upper
bound on this type of Arbitrage so
centralized exchange decentralized
exchange Arbitrage
uh uh additionally to this we also
looked into opportunity to let the pool
contract know about time boosted
transactions which allows them to price
such transactions differently and this
introduces some interesting game between
LPS and the time advantaged arbitrager
and then we can calculate what will be
the distribution of value between these
two and other arbitragers so thank you
for your attention happy to answer
questions about this and the time in
general thank you very
much so raise your hand if you have any
question y over there there first oops
sorry
sorry do you think it's a good idea to
use one minute uh allocations to arbitr
is is too long have you tried to do
short simulation times I ask for because
me multi Block M has been a problem we
don't stud very well so have you tried
to simulate
shorter so we in simulation of course
you can simulate and get results what
you get but um we thought that one
minute is not very long because um if
you make
it uh yeah if you make it longer it's
even worse from your perspective but if
you make it uh short then we need to
conduct this auction too frequently and
that also has some
cost so that was yeah this kind of
trade-off that we
analyzed there's another question over
there uh did you try this using real
money and uh did you find anything
interesting between Dr and the
simulation so we didn't try real money
but you are welcome to try uh we
analyzed the back testing so this was
data was taken in July but in principle
you can forward test that too once once
it's there but you can also forward
without time boost deployed on arbitrum
you can just assume that you have this
advantage and you can then see how much
you can make with the strategies that we
suggest so answer is it's very easy to
do but we didn't do it
hi um this is can and I'm not sure you
covered it but uh was any
differential gas uh price that uh was
taking into consideration in your
simulation so what differential I didn't
get uh gas like amount gas
fees or decentralized
exchange decentralization yeah the gas
fees
ah so gas Fe we assume to be um let's
say sub sent for the exchange so so we
took realistic C fees and subtract it
from the gains but they are very not
substantial for for the results I see
thank you uh there's one last question
over
there over there okay over there yeah
sorry yeah um what what kind of
inventory are is needed to actually pull
this off in a relatively profitable
manner I mean you need to have both
assets on the chain and on the external
exchange to like try this strategy yeah
but I guess I'm just looking from like a
like from a volume perspective of what
they actually need like in your
simulations was there a drop off point
where let's say if they only had 100 K
versus 500k it's no longer profitable
yeah actually sometimes you need very
large inventory to realize very large
price difference but we didn't go into
this we assume that you always have
enough but you are right that to take
this um Advantage you can check numbers
to take very large Advantage you need
very large inventory as
well so that was the last question thank
you very much for your talk uh please
give a nice round of applause to AI
um the next next speaker is going to be
Dr Theo diamandis he holds a PhD in
mathematical optimization at MIT he's a
research partner at Bane Capital crypto
where works on uh problems in crypto
economics and dii and today's uh talk is
going to be uh amm as managed customized
portfolio please welcome Dr diamandes
thank you for the introduction
um hi everyone my name is Theo um I do
research at B capital crypto and I'm
also going to talk about decentralized
exchanges um I want to kind of focus
this conversation around the liquidity
providers and this talk is really going
to be a call to action for some research
and then also product development that I
think would be quite
interesting um so let's look at the
value of an LP position in an amm I'm
going to say that we have two assets one
is a numer and the other is some asset
whatever you want with Price p valued in
terms of the numer ER so you can think
of maybe the first asset is ethereum the
second asset is uh some other uh some
other token and P is the price of that
other token in terms of ethereum and uh
this amm has a set of allowable States
so we can think about it as having some
set of reserves and it says I will let
the reserves change in particular ways
so what's the value of the liquidity
provider position well if we assume
there's one Arbitrage or at least one
Arbitrage or who's going to try to
extract as much value as possible from
the amm we get this minimization
function or sorry this minimization
problem which essentially says the value
of an LP position is the minimum value
uh among all the sets of allowable
reserves so for what's most common which
is the constant function market makers
that of allowable reserves is just going
to be essentially some invariant uh
evaluated the reserves that has to be
greater than or equal to some
constant so just to make this very
concrete with an example let's take a
constant product amm uh so things like
Unis swap V2 and for that we're going to
have the square root invariant if we
plug this in and kind of go through
everything we get the value of the
liquidity provider position at time T So
at t uh amount of time after this
position was opened is essentially
proportional to the square root of the
price plus a term that depends on the
fees so we look at this and there's a
few questions that one might ask or a
few kind of considerations uh first is
do I want this derivative uh do I want
this product second is what rebalancing
cost am I going to pay arbitrageur to
maintain this uh position's value for me
and then third is can I hedge the price
movement let's say I just want fees I
just want fees for providing my liqu
I don't want to be exposed to the price
movement how easy it is it to hedge this
so I'll review some of the current
research which is mostly on this first
question do I want this derivative and
there the question is okay well let's
say there's something I want so some
portfolio value V that I want how do I
get to an invariant for a constant
function Market maker that gives me said
value um we see some examples in
practice I'm using this Loosely but uh
things like zero CP on bonds at maturity
some of the yield token pools look kind
of like this uh we also see
things like weighted portfolios so
things like balancer pools geometric
mean market makers uh some of the
Perpetual exchange lending pools look
kind of like these weighted portfolios
uh we've seen covered calls on chain and
other people build options on top of
amms and then we've also seen recent
proposals uh for things like prediction
Market amms uh there's a recent blog
post from Dan and CMAC on that
the general theory for the static case
so for the case where the time T doesn't
matter uh from replicating market makers
papers in uh 2021 2023 says that if that
portfolio value function is some concave
homogeneous increasing function we could
figure out the cfmm that gives us said
function however this doesn't really
tell us why some of this stuff works in
practice some of the stuff doesn't seem
to have worked in practice
how do we do it in the dynamic case that
was only in the static case and there's
a few things that I think at least are
key factors
here for that uh I think the ease of
hedging the price movement essentially
if LPS desire some delta neutral
strategy so they're not taking uh risk
on the price of the underlying asset how
do they do that with an amm so they just
essentially want the exposure to the
trading
fees second is the amount extracted by
Arbitrage so if you've heard lever
thrown around or we can think of these
as rebalancing fees that you have to pay
to Arbitrage ORS how much is that and
like essentially how much leakage is
there from uh my portfolio value third
is just how useful is it to have one of
these custom portfolio value functions
like what are essentially derivatives
that I might want to have is the
portfolio value actually useful or
not so the reason that I think that
looking at this is exciting is there's
over 10 trillion dollars of assets in
ETFs there's there's a lot of passive
liquidity out there clearly people are
doing stuff in kind of the financial
world with this and I think there's a
lot of opportunity to bring this
liquidity on chain so if you're
interested in collaborating on these
types of questions on the research side
or on the Practical side please reach
out thank
you thank you so are there any
questions no questions raise your hand
so I can
send you the
mic
okay okay all
clear there's a question
yep uh you didn't talk uh uh you didn't
expand in detail but um um can you uh is
there um a brief uh introduction about
uh what are typical ways of
ping the directional move it it depends
on the actually I think this is kind of
a issue in a lot of amm because for
instance if you wanted to uh hedge like
say a like a constant product position
you have that square root uh function
that's your long exposure to the asset
and most places to get short exposure
are giving you a linear short exposure
and so what that means is the amount
that you need to be short that asset is
going to change as the price changes um
and that makes it very difficult because
you have to constantly be managing this
uh the short position the hedge of the
short position um which means that it's
like no no longer uh passively providing
liquidity and there's um there's a
number of blog posts if you um message
me I can send you from kind of a few
years ago that talk about this but in
terms of the question of like how do I
design a portfolio value that is easy to
hedge um I I I think this is a pretty
interesting area of research moving
forward especially the dynamic case
where the cfmm or the odd made Market
maker might be changing over
time there's another question over there
in the center how do you how do you
think about concentrated liquidity
provision in particularly regards to
hedging as you described so if I'm an LP
and I want to you know only provide
liquidity within certain bands you know
how do you think about that in regards
to the rest of the formula um those also
actually do fit in kind of the standard
constant function Market maker framework
even the constant liquidity pools um
there's a there's a paper that I wrote
with a number of colleagues called the
geometry of constant function market
makers that shows that connection um
essentially the the high level idea is
one way to think about all of these
things is there's like some set of
reserves that's allowable kind of that
first slide that I had and that set has
particular properties for let's say like
the things that you want to hold so even
say a con concentrated liquidity
position whether that's like the Unis
swap V3 hyperbolic type concentrated
liquidity or if it's a linear
concentrated liquidity you can even in
some ways think of an order book as
linear concentrated liquidity positions
uh because for whatever you're selling
it's just kind of a linear amount um so
this all falls into a similar framework
and actually I think that's one of the
things where kind of the more we can
bring this all into common framework we
can start to use more interesting
mathematics and then really push forward
uh our ability to like understand the
stuff and build end
products happy to talk more offline
thank you for the
question this time for one final
here what do you think is like the the
right way of thinking about these
portfolios for users because crypto is
quite quite a unique place you need to
put like these two tokens in in the AM
and Market making market makers are
looking for optimizing USD do you think
we are looking at maybe the WR metrics
when you are measuring this kind of
performances are should we build
portfolios for this two kind of tokens
what's your take on on um so sorry if I
understand the question correctly it's
like what types of portfolios should we
be what what kind of products are we
trying to design I I think that's a good
question I I think right now there's the
the first kind of step to answer
answering that question is to figure out
you know what might we care about and
then how do we design for those types of
uh for those metrics I I think there's a
question of to like what the metric
should even be and then after that we
can kind of you know look into what
actually how to actually construct those
portfolios um but that I think the
exciting part is the design space is
pretty wide open right now and of course
we can look to finance has a long
history that we can look for inspiration
to thank you
well thank you very much please have a
nice round of applause for
you um so our next speaker is going to
be uh nipun is a co-founder and core
contributor of infinite a previously
conf founded um Alpha Finance who was
the first to introduce leveraged yield
farming and today's talk is going to be
deep dive the lp pricing um please
welcome nipun
okay uh hello everyone uh so my name is
nipun from infinite uh def5 abstraction
Le so today I'm going to give a talk
about LP
pricing so uh before we start uh what is
LP uh everyone might be familiar uh it's
like a chair of the pool uh depending on
where you land where you deposit uh Unis
swap curve uh a balancer any kind of
cool and you get an LP token in return
in return it may be erc20 maybe
not uh so uh LP pricing uh why is it
important right it enables more use
cases uh it creates more composability
and capital efficiency where you can
reuse uh the end product the chairs uh
to be able to create more uh leverage uh
lending borrowing more usages right uh
LP value right uh Cy it's whatever is in
the pool divided by the shares right but
uh you know this is not true not so easy
life not so easy right uh many many
hacks in the past has occurred because
we're using spot price and sandwich
attack uh you can manipulate the price
or you can even inflate uh price per
share for the lp right so this talk is
going to be focusing on the high level
of what's important uh to compute robust
LP
pricing so so LP price uh depends on two
major things right uh one is what are
you going to use the LP for UC are you
using it for claro or using it for
borrowing uh second part
is what LP types are you using right it
depends are using uni V2 LP token which
is erc20 uni V3 which is uh ERC 721 or
V4 or even curve uh or other amm
variance right it
depends so so moving on to use cases so
this will determine like what kind of
pricing is needed for your use case so
for example if you're going to use LP as
collateral then you don't want to over
estimate your price your LP price why
because if you're using an as claro then
you don't want people to be borrowing
against your claro more than the value
that you should have right so if you use
calaro don't overestimate the price
second part is you don't want the price
to dump right you don't want to have
your collateral suddenly dump price by
your algorithm is is prone to
manipulation right so it can lead to bad
debt because uh the borrow the the B
borrow value stay the same LP collateral
value suddenly drops right you can
however under underestimate the price at
the cost of efficiency and at the cost
of liquidation risk for users
uh on the other hand if you if you're
going to use LP as for borrowing then
it's going to be counter uh uh
counterargument right uh you don't want
to underestimate the price because
otherwise you can borrow out more value
than than what you should have at the
same time you don't want pricey pump for
the borrowing tokens because suddenly
your your debt Sly can Skyrocket and
then cost bad debt in the system and
that can lead to attack vector
and at the same time you can
overestimate the price of the borrowing
tokens out but at the cost of capital
efficiency and also liquidation risk for
the users again so this is for LP use
cases LP types uh there are many kinds
of IB types but it'll it'll Define uh
what kind of pricing can be implemented
for example univ 2 univ 2 you can donate
money right if I transfer tokens and
then you call sync function
so that means price and pump uh at the
cost of uh money for the attackers so
you should not enable borrowing for for
uni V2 in V3 you can increase equility
again anyone can increase equility
increase the value price per share um so
you don't want to use this as as a
borrowing as a position as well so this
is uh some things that we need to keep
in
mind and example of LV types uh un2 un3
you can find exact formula uh balancer
uh generate uh unit V2 you can also find
exact formula using tailor approximation
uh curve stable swap you can use grade
in descent solidly Pendle GMX trer Joe
whatever and other forms uh you can
always find uh some form of exact and
some maybe some
approximation um so just a quick example
uh you derive Fair balance and then you
derive the fair pricing for the lp and
I'm not not going to go through the
exact formula but um this is the
the rough calculation of unit V2 in V3
is going to be slightly more complex uh
so you derive from the price and then
from Price reaction you derive back to
uh the fair fair pricing for for for the
lp So yeah thank
you thank you very
much thank you um so do we have any
questions please raise your
hand over there no
there what's the uh best place on chain
to um use Unis swap uh
nfts uh as
CER the question is uh what's the best
place to use uni swap on un swap in uh
V3 right uh yeah I suppose so um I am
not sure right now uh but there are many
uh protocols that are building on on top
of DV3 um allowing to lend and you
borrow out um also uh I think uh there
are leverage uh leverage U farming
protocols for sure um and there also I
think uh I'm not sure if a is allowing
uh univ V3 position as clar or not I
remember they they they did back in vv2
they allow they have like am markets uh
but they are not so much usage um yeah
thank you okay there's another question
in the
middle okay hello yeah I just want to
answer your question the best protocol
is
panoptic any other
question back there
hey I'm I'm curious to know
if there are no Oracle pricing for a
token in an LP po how could you still
get the fair value of the LP price if
there's no Oracle price right so so so
this is given context of if you have
Oracle price for the base asset right um
that's a good question uh and the answer
is going to be tricky um because if
there's no true price or the base for
the base assets then what do you treat
the asset what what's actually a correct
price right if it's if the asset is only
available in in in a DEX for example in
uh if you use like Pendle PT token
usually the pricing is derived from pts
pool itself um and I think uh you could
find other source of source of PT
pricing for example you can use twap at
the cost of um uh time uh and risk but
yeah so that's tradeoff because if
that's if that's the only place where
you can derive the the true price then
that is a true price right um so so in
LP pricing what you what you actually
want is a robust pricing where you don't
want to have like U manipulatable price
uh by flat flash loan flash swap
everything else so there should be a
reference where we we should find what
is the correct
price uh thank you that was the last
question thank you thank you very much
um give a round of applause to
nun so our next talk is going to uh our
next speakers sorry are going there are
to be two of them actually um that's
going to be Alan wo who a protocol
engineer at uniswap labs and Dr Brad
bashu um who is a researcher at Unis
swap Labs um and the topic is going to
be time is all you need optimizing Dutch
auctions on Abit
please welcome to Mr bashu and
Mr hi everyone my name is Allan I'm a
protocol engineer at Unis swap Labs hi
I'm Brad I'm a research scientist at
Unis swap labs and today we'll be
talking about optimizing Dutch auctions
arbitrum when we think about swapping
onchain we typically think about trading
against
amm but using amm and onchain liquidity
isn't always the best for every single
trade this is because of reasons like
liquidity fragmentation and me we want
to be able to expand the realm of
accessible onchain liquidity while also
opening the door for offchain
liquidity a pattern that's used to
achieve this is using intents where a
swapper assigns an intent to swap token
a to token B
and they don't care where the token B
comes from they just want it to come in
a reasonable amount of time and get a
good price for
it so thinking from this perspective
it's a simple problem that swappers want
two things good pricing and fast
execution today there are systems that
get us good pricing and fast execution
like RFQ systems but they often run into
problems around complexity and fairness
they're also relatively difficult to
analyze and
execute so today we'll be talking about
a simple approach which is using Dutch
auctions on
chain a Dutch auction is an auction
where the price starts high and it gets
lower and lower until the price is taken
this is called a price Decay so the
price starts high and it decays lower
and lower until Market competition fills
the order if you set the price too high
then the auction will take a while to
fill but if you set the starting price
too low then you'll just get a bad
price so we're left with a simple
question how do we set this Dutch
auction
optimally and the answer is time time is
all you
need so as Alan mentioned when you hold
an auction it takes some time for your
auction to get filled we can call this
wait time we can actually design a
system that depends on mainly this
output metric weit time to give the user
the best price
possible so in other words we can avoid
the problems of complexity fairness and
difficulty to evaluate without
compromising on execution quality for
user so to test this idea we made a
simulation and this simulation depends
on market prices amm prices um takes
into account price impact to create
reference prices and then we run
multiple Dutch auctions across this
price
background on your bottom left corner
you'll see um two output metrics fill
rate and weight time and we tell this
algorithm to aim for a weight time of 4
seconds on the right hand bottom right
hand side you'll see the parameters of
the Dutch auction tuning to try and
achieve this weight time of 4
seconds and in particular in the bottom
right um chart the xaxis is a parameter
that can give you an approximate value
of how much price Improvement you're
getting and this value is Meaningful
when it converges to roughly uh in this
case 4
seconds so what I've shown you is that
um oh and one thing is that the maximum
price Improvement that I injected in the
simulation was 25 basis points and as
you can see it converges to this 25
basis points so I've shown you that I
can only look at one simple metric and
give the user um best price possible
without com without um with the ability
to evaluate what that price Improvement
is so let me give you some intuition
behind what's going on here so um the
red dots here represent the auction
prices changing with different
parameterizations um your auction gets
filled when the market price goes above
the auction price when a user comes in
to swap for example at block 10 um we
can check the amm price generate a
reference price and use that to
parameterize on our
auction so what happens if you
parameterize your auction too low if you
start off too low you get filled
instantly this is bad because it means
you could have gotten a better price
what happens if you parameterize the
start of your auction too high you get
fill much later this isn't necessarily
bad but it makes your auction harder to
so if you get filled within the first or
second block or you know first couple
blocks then um that period tells you
that you parameterize your auction just
right and you give the user you still
give the user the best price
possible so using this strategy we can
compare it to other other strategies of
um parameterizing Dutch auctions you can
think about using sex prices if you use
sex prices then you run into the problem
of fairness um sorry you you are
guarantee fness but you can't
parameterize every token if you use RFQ
you kind of compromise on fness but you
can parameterize every token in all
cases you compromise on ability to
evaluate uh our strategy satisfies all
these
criteria so this is just the beginning
we're testing this out in arbitrum and
but this can work on any Dutch block
based blockchainbased Dutch auction and
we think this is a step towards testing
out nonlinear auctions in the future
future thank
you thank you guys so do we have any
questions over
here thank
sorry A B
short all right thanks so what does time
boost do to your
design so and time time boost you pay
extra to come in first right yes but
imagine so ignore that factor but there
is one player who has this 200
millisecond
Advantage uh I think the user gets
better price I don't um that user that
user yeah thanks no it's it's a they
what's important is the filler it's a
open market on the Dutch auction so it
doesn't really matter and
yeah don't think I understand then it's
open anyone can fill so yes but one
party has time Advantage like so you're
saying if the filler has time Advantage
yeah let's say filler or the other
um you yeah so if the filler has um
first move in that block then um in that
particular block where the price decays
to where the true market price is where
they would want to fill then yes they
would be able to snatch that before
other people
we have one question right here hi so if
I understood correctly it's you're
running this auction for each token
simultaneously or just one at a
time so whenever a user um makes an
intent to make a trade that trade itself
is a single auction that's going to run
on chain for people to fill but if there
are multiple uh auctions running par
there is a lot of Arbitrage opportunity
because the prices may not
agree uh um each auction for each trade
is unique right they have their own
unique parameters they have um outputs
that the users are expecting so they are
distinct so let's say if if if there is
a exchange between usdc and E going on
um that's priced at 300 and there's
somewhere else U the opposite trade is
happening at uh 1X 400 like there is a
Arbitrage opportunity across these two
if somebody can submit two bids and
profit yeah so um if the person who's
filling that auction there would be an
expectation if they're behaving
rationally that they must have um
sourced the liquidity somewhere else to
in order to fulfill that chain on
fulfill that trade on
chain I think you're I think I put in an
assumption in the simulation that you're
probably saying it's not necessarily the
market price that determines the fill um
and determines to fill is if some uh
whoever is willing to give the best
price and that's all we care
about the best price we can capture for
the user whoever decides to fill it so
not necessarily at the market
price we have one last question over
here hi uh how do you account for the
liquidity when you're doing the the
testing since if you if you only test
with like a small amount in your trade
and it gets buildt quickly but then when
you you adjust it and you want to trade
you want to swap more then you're going
to get hit by
liquidity you're going to get hit uh
mean you're going like the change yeah
the price um I think what I showed you
is a simple version where the price
impact is you take orders roughly the
same size and you run this algorithm um
you can either choose the bucket by
trade size and run this algorithm or
have a smarter algorithm I didn't really
talk too much about how the algorithm is
working just the intuition behind it
okay well thank you very much um thank
you Alan and Brad please give them a
nice round of
applause and now we're going to have the
uh uh last uh talk for the
cryptoeconomics uh track today uh so
we're we welcoming back the for his
second um Talk of the day um and is
going to talk about list uh inclusion
list inevitable trade-offs please
welcome back
ter hello hi I'm back thank you and yeah
so um this one is more again on
inclusion this and it's more on the
engineering side that as someone that
has been um focusing on inclusion this
over the last year and I also um started
looking at fossil more and more and this
is where my perspective in terms of
engineering challenge with regards to
inclusion this so today where we are
right so today we have ethereum slot and
each slot is 12 seconds and what are the
constraint within the slot so as a
proposer I want to propose a Blog and I
will hate to have my blog gets reor and
that's not nice so I want to propose uh
my blog on the strongest head that's
possible right and after I propose a
Blog everyone else on Network that's
running a Noe will verify the block and
compute what is the head and as aester
their job is to attest to the head of
the block so this is where the four
Choice follows if you use lmd ghost and
then as a aggregator as optional you
Aggregate attestations and then the
proposer essentially follows the votes
for the next slot and then it builds on
top of the head right and then because
of timing game you can see there is a
phenomenon that today the attested cut
up is at 4 seconds so basically
everything is pushed towards the 4
second Mark and that's kind of the
equilibrium right now that everything
happens between 3 to four seconds and
then between four to 12 seconds of
nothing typically happens unless you are
the net slot proposer you're lening
transactions and you're building block
so where does inclusion this fit in into
this picture so here I'm speaking in
terms of fossil so fossil is um a EIP um
don't know what fossil is so fossil is
probably the best inclusion this design
that I have seen so far that is mostly
bully proof in my opinion and then it
has the same slot property and then so
what F does essentially is that it
essentially allows uh secondary runs of
proposes that are allowed to send their
local block and then such that it
constrain the next slot proposal
essentially so where does that leave us
in the picture right so because of that
we have to essentially add this proposal
in the middle of the 12 slots that means
that as a proposer for the inclusion
this I have to essentially verify the
block beforehand such that I want to
essentially propose the best inclusion
this effort right and
then and then as a constraint the next
slot Builder or the proposer I have to
essentially pack the inclusion this into
the block and then if I miss inclusion
this then I may miss my block and uh and
also as a tester I want to make sure
that the block satisfi the inclusion
this so there are three more constraints
as a builder as a proposer as an tester
which I cover here so where are some
parameters that we can play in terms of
tradeoff so for example how big is the
size of it of how big is is the size of
an inclusion this right if the inclusion
this size is so small that it may not be
useful but the inclusion this size is
too big then you open up Network for do
concern what is the size of the
inclusion this committee because we want
commune size to be reasonable but then
but then if the size is too big again
you open up Network do concern and then
how much overlapping are there within
the inclusion this and then what is the
satisfactory rule right so as a proposal
for the next slot as a tester I'm
verifying the block like what like
basically like how much of the inclusion
this the proposal has to satisfy for the
block block to be validated so what are
the concerns so first concern I think is
the increase of bandwidth and Compu for
node like depends on how biger inclusion
this size is and then then again the
second concern is that proposer like how
much time do I have to build a Blog and
then as a tester how much time do I have
to verify the block so here are some
open questions for us to study if we're
interested in this inclusion space like
how compatible it this with the future
road map such as PR do such as such as
epbs how does inclusion this work with
account abstraction and then like how
can we add blob transactions into the
inclusion list such that it doesn't open
up those concerns and then how can we
better utilize local manoo for inclusion
this maybe we can just essentially send
the transaction hash instead of sending
the food transactions finally like will
there be a aop political market for
inclusion this and it's something that's
we need to study more so yeah if you're
interested to contribute definitely hit
up Julian and then hit up me and then
yeah definitely I'm I'm definitely very
excited about this inclusion this design
space thank
you thank you so now we have time for a
few Q&amp;A
please raise your hand if you have any
okay no questions okay it seems oh
there's a question
here um yeah super interesting I had a
so I don't know if you can answer this
but um in any capacity are you thinking
about doing fossil or inclusion list for
l2s like from or yeah and how is that
different from was in the EIP and what
could be on Main net right so their two
today is most of the layer two or all of
the layer two today they have just one
sequencer right so the sequencer
definitely have a lot of power say today
if you want to force your transactions
in there like if sequencer ignores you
there's nothing you can do but then
there's a lot of people say well you can
force transaction through layer one but
that's also not nice because you have to
wait like 24 hours right but then like
again I think like decentralized
sequencer can of sof set if you assume
honest majority so I would say the space
in terms of sensorship resistance on
Layer Two is is definitely very
different on layer one because on Layer
Two you can essentially having like one
million validators you could just have
like 10 sequencers and then trust like
honest majority and then as long as you
assume some of them are honest and they
will they like basically basically they
have to include your transactions
any other
question okay well thank you very much
for your talk uh please give some
Terence and that concludes uh the the
track crypto economics uh we're going to
have a break um and we're going to be
back at five um 10 5 uh to discuss
Cipher and privacy
Ro
this o
bu bu bu bu
got
t t
l
oh o
look
hello welcome back for the last track of
the day so we're going to have the
different topics to discuss uh Cipher
Punk and
privacy um so the first Speaker of the
day will be uh Frank um he's currently
leading the waku project he joined the
blockchain ecosystem for The Cypher
Cipher Punk values and the topic of the
day is going to to be bringing
peer-to-peer networks to all the PS
please are welcome Frank
all right thank you very much hi
everyone let's get started so bringing
P2P networks to all the peers what are
we talking
about so we are trying to create a
peer-to-peer model for un user devices
to be included in this model and by and
user devices I mean desktop app mobile
app web app in the browser and here more
specifically we are talking about leave
P2P goip sub based Network works so for
those who don't know goip sub is what is
used on the ethereum network for the Bon
chain as as a network
layer so the current status quo across
most peer-to-peer network is that we use
race apis web3 apis um and other web
getaways to allow users in the browser
mobile and desktop to access a
peer-to-peer
Network usually anyone could run such
API is have the resources but when
building applications whether web apps
or mobile apps um usually the users or
developer will select one API maybe or
maybe a
couple so this does create some problems
and and we're aware of that you know in
the eum ecosystem and initiative like
like client try to solve this problem
around trust data access and propagation
privacy and and censorship of this API
I'll go in more detail at the end for
that
so the first problem we had to want T to
use goip sub on again laptop um
potential mobile and browser is that it
has very unstable connections so if you
want to compare that to e node for
example when you're staking usually you
run your node on maybe r byp or dap node
or some on VPS U where connection is
quite stable but on the laptop we are
going to change Wi-Fi we going to go
offline the back online
and go sub doesn't have any mechanism to
help you with this specific scenario so
there's no acknowledgement um to know
whether your online is a bit hard you
can be have some timeout from TCP and
you can miss messages when you're on
when you're offline right because once
message goes through the network it's
gone so solution we we develop is uses
um goip sub and dv5 for desktop as well
as a smart contract and zero knowledge
based rate limit to ensure that you
don't have too much bandwidth too much
traffic going on the network so you can
support his Network on a household
bandwidth and we have a number of L P2P
request response protocol to enable uh
browser and mobile to query for for more
peers because this V5 can consume a bit
too much um bandwidth and and resources
and I was able to push messages and get
messages from the gohub network so you
still have a light weight to get U
messages but it's much
is still is more much more decentralized
than the rest API finally in ter of
Shing know if you start to put 10,000 or
Network um unlikely to work so we do
separate I would say the global Network
into smaller ghub network via
sharding so if you have a quick look at
how it could work um so we have service
nodes VPS that run in the cloud they
allow a mobile phone to go and query for
messages they missed
um mobile phone could subscribe to
desktop node and say hey can you please
forward messages that I'm interested in
um desktop node goes offline and then
back online can also quate messages to a
service node in the cloud and fin your
browser can push messages to service no
via websocket that we then get uh pushed
on the gy sub layer which we call ho in
our
case all right so we we did have to um
add resonancy right because have some
inbit uh bit in Rundy we had to add that
when for pushing messages we uh push to
a couple of uh of Nod and we also had to
add and to and relability protocol so
that in a context of a chat application
you know whether or you have some idea
whether your recipient other
participants in the group have seen your
message and the result is that now you
have some uh Rony and you can check
message presence using um
nod to access network instead of
thrusting one single rest API you do
have some improved privacy because
instead of having all your traffic going
through one rest TPI you can select
various peers and decide what traffic
you uh you ask from them or you push to
them and in ter of censorship as well it
means that you not rely you do not rely
on a single DNS single domain name for
example and single rest API uh which
could be censored or blocked but instead
you apply a peer to peer Discovery
strategy allowing you to access the
network via different
peers that's it for me five minute
presentation I think question for time
for questions thank you very much
so we're going to have a bit of time to
to ask some
questions so are there any questions
please raise your
hand um I think you mentioned status as
one of the users is are there any other
apps using this uh stack or approach you
highlighted yeah of course so yes so the
status chat app um use that and they
have a mobile app and laptop and desktop
app we have red gun red gun is a private
defi um systems where they have a Zer
contract and you can do defi without
revealing yourm address and they do use
waku on their mobile web and desktop app
where the wallet has Wu running um
inside with the l2p and um I can send
messages can send basically the
transaction the proof that they have a
note to broadcaster which are not in the
cloud which then takes the transaction
from the wallet and push it on
chain okay thanks and we also have other
project uh I mean reg gun and um status
are the most advanced one the most
mature ones
I think there's another question in the
middle no okay now go ahead uh hi so my
question was first is why rest and
second is why not grpc or
RPC why are we not using grpc yeah drvc
or
RPC so in in the case of so in ter of
lower lower protocol stack right um
we're using TCP and web socket I'm
guessing you're talking just above one
using grpc instead of lip2p I guess yes
so lip2p does come with a number of
useful tools so when we start to build
and starting to use gossip sub for
example um it means that we start to we
are introducing one technology stack
into into the system right so we use
thep GOP sub and when we want to look at
request respon protocol we could indeed
start to use grpc or rest API but this
mean introducing new technology stack
into the system which means that having
a heterogenous techology stack means you
know you may have more problem and so
it's just easier to continue using lip2p
and Define this request respon protocol
on top of lip2p and lip2p comes with
with good things such as um you know the
noise handshakes right so we have a
pointto point encryption with d2p out of
the box um so you can just use that out
of the
box good
question so we have time for one last
here could you share a few more words
about the sharding idea is it um if I
have an application that grows massively
would it start charting itself
automatically or that work awesome
awesome question
so the idea with charting first is that
you you know let's say you have a
billion user right um all the messages
they they generate will be too big to go
through one household band right so the
idea is to SP networks that you only
look at interesting
in the that's the rting layer we have a
Content topic which is metadata like
just a string that you can attach to
messages which allow you to further
filter messages you looking at so on
mobile you are going to only look at
specific content topic which will be a
subset of messages on The Shard so now
you have several options you can
either um come in and your application
use one content to pick and you're going
to just be part of one chard um and if
you grow up then you may want to look at
seeing if you can use more shards or you
can start in and have actually a big
application from the get-go and just try
to split over traffic from the get-go in
terms of you can start with one Shard
two shards three shards in ter of
growing to more shards is just a
consensus between operators so you can
say okay we need two more Shard on our
netor work and you can just tell youor
can we please support charge 10 and 11
now and they can start to support it and
you can start to diver traffic for it so
it's bit of manual process and we
haven't gone through this uh course pen
yet but it's um it's many operator
consensus
here thank you very much that was the
last question so give some Applause to
Frank so our next speaker is going to be
uh Sebastian Buel he works atosis SVP of
Technology he's a founder of opa and
previously founded two other Tech
startups he's an expert at building
Technical Solutions that empower the
individual and so the topic of the talk
is going to be Cypher Punk is low not
hyper financialized and unlike Twitter
uh please welcome Dr burel
yeah welcome and thanks for the kind
introduction um my name is Sebastian I
got introduced already um so yeah but
today actually I don't want to talk
about any individual projects because
I'm talking about a problem that I think
is bigger than any individual you know
project that we're seeing here and
before I get there I want to dive in how
we come here so a long long time ago you
know um in days so old that ethereum had
a vision a vision was stated on the
launch day website of ethereum.org July
ethereum is a decentralized platform
that runs smart contracts applications
that run exactly as programmed without
any possibility of downtime censorship
fraud or third party interference
ethereum is so the internet was supposed
to work
on a page you found how to for the very
first time in human history actually do
you know Fair
voting if you dig deeper you found out
how to launch your shitcoin without
running a network that was
neat somebody came up with a horrible
standard and called it ec20 and yet
people were building like really cool
interfaces on top of it the birth of
defi well the birth of defi in this Dex
had a bit of problem that you know if
you look in the order book only one
person can basically buy the top of book
right you wouldn't know who in the block
actually got that that's not great
luckily a young man came up with an idea
and another even younger man wrote A
Blog about it his blog can be summarized
in exactly five
characters x * y equals K I think the
most iconic equation of our times and
dexas were born right and and um Along
came a third young man who at the time
didn't even have a job or knew how to
code and coded up that
idea and called it
uniswap now if you use Unis swap you
might have seen the settings thing you
might have not seen it there's something
called slippage that fixes the issue I
talked about earlier of not you know
taking this exact order only fast
forward to last night there was some
fellow who was again trading a
token because that's what people do 15K
worth of coins for like 133.5k
worth of eth weird what's that
difference
slippage of course not right so that's a
sandwich attack that fellow got
sandwiched by sophisticated front run
and back run here how was that possible
well of course it's possible thanks to a
highly
sophisticated you know user screwing
infrastructure that's also called me it
was built to democratize access
and make things fairer for the user by
leveling the playing field and bringing
many players into the field so let's
zoom into that let's zoom into this
Builder section down here and let's see
how that democratization is
going well today we see that there's
exactly
two remaining right so um that's Titan
and beaver congrats on democratization
well and I think that it's broken right
that is broken that is not how ethereum
was supposed to work so an updated
version of what is ethereum
platform that runs Smart Financial
Casino contracts applications that
usually run exactly as paid without any
possibility of downtime and yes it
actually once set third-party
interference funny right ethereum is
Bernie mad's wet dream
and that is broken and that's why I'm
here to talk about and that's what I'm
standing up for because that is not the
ethereum that I came here
for it is about them versus us they on
faster blocks obviously right can trade
faster you can make more money quicker
we want resilience via privacy and
decentralization and is unfortunately at
odds why is that at odds well because
physics because it takes a few hundred
milliseconds to have a round trip of
ping across our you know not so tiny
planet and if you want privacy
infrastructure like mix Nets that we
build at Hopper or DVT that other people
build you have a bunch more of those
right so things are not as fast and
that's why that's an actual
problem now they invest in reaking rwa
and
rehypothecation we empower the
individual on the world computer these
two things have to share the same Ledger
and have to same infrastructure to share
they write checks Cipher PRS write
code they are here for the
profits we are here for positive human
interactions and experience in the
infinite Garden if you are here for
profits you are part of the problem you
are contributing to A system that is
corrupting the underpinnings of the
world computer that Cipher punks want to
build really great stuff on let's fix
that let's be conscious about that and
let's try to build an ethereum that goes
back to the roots of where it started in
order to bring us the infrastructure
that empowers the individual and not the
trader thank you so
much thank you so now is your
opportunity to ask some questions please
raise your hand if you have any
question about a censorship
resistance there are still mode
operators that make vanilla blocks so
how does that compare to what you said
so yeah I mean uh there are still some
not producers that produce blocks but
that's not enough 80% of the blocks that
are showed are subject to that right and
that's not great right so increasingly
even individuals are subscribing to the
big Builders and that corrupts the
infrastructure for example it's not just
the L1 with based rollups that directly
translates to corrupting the l2s
right so we need neutrality of the
L1 hi thanks for the talk so you showed
the website back in 2015 and 16 and I
think one of the big things that changed
was the DOW hard for and that split the
community uh to some extent but also
kind of filtered away some of the cipher
Punk
philosophy uh so why don't people just
the cipher punks why don't they just use
ethereum
classic sorry why don't they just choose
ethereum classic great um well I I think
we've seen the attack ability of that
right so Cypher Punk still deserve
security and Cypher Punk still deserve
security that they don't get on a chain
that could you know any time of the day
just get forked away under their feet
and that's not great so I think Cipher
punks deserve ultimate
resilience more so than the profit
maxers because they can still go to
binance if you want to make money
binance is great technology right please
do trade on binance
well actually that was the last question
thank you so much uh please give some
Sebastian so the next speaker is going
to be uh Evan McMillan he is the CEO and
co-founder of private idea having also
founded disco.
XYZ um and was a director with b hatway
and new
consensus um so the the topic of our
talk is going to to be Cipher bank for
centuries coordination and secrecy
across the ages please welcome
Evan all right what's good Devcon how
are you
feeling excellent thank you so much for
being here today my name is Evan
McMullen and I am CSO and co-founder of
provado ID along with a handful of other
honors throughout the ecosystem
throughout my
career how many of you would consider
yourselves to be cyber Cipher punks
seeing I'm seeing some hands here this
week there are a lot of brand new
members of our community who haven't yet
had the opportunity to identify with
that term Cipher Punk and I keep hearing
things in the hallways like privacy
doesn't matter so I think we need a
little refresher of the reason why we
come to Devcon the reason we build with
blockchains the reason this industry
exists at all the cipher Punk movement
originated in the late 80s as a response
to the growing threat of centralized
Powers invading individual privacy
however the origin of this ethos and
Associated Tech far precedes the era of
networked Computing so let's look at the
root of what got us here today around
BC the um the Mesopotamian Kings had
servants take a block of stone and carve
their names into it placing it in the
middle of the Town Square in a show of
force and Declaration of power then
after that King the next king had his
name carved on a giant block had his
servants come down to the town square
and put his block on top showing the
closure of one Epic and the opening of a
new window of time under his Reign this
stack a physical chain of command became
the first calendar and ancient
Mesopotamia a thriving ecosystem who
whose governance was anchored in a
protocol that measures time based on
blocks perhaps the first literal
blockchain in the Jo Dynasty people
started producing these metal pieces
shaped like Spades but too thin for
practical use instead they were monetary
instruments inscribed with characters
indicating denominations that
facilitated transactions providing
access to Services um representing a
assets but having no intrinsic physical
use in medieval gent not far from
Brussels there's a belf where the city
documents are stored inside of this
chest but this chest has three padlocks
each with separate Keys held by separate
parties the room that holds it is also
locked by three separate padlocks
requiring three separate people two
three of three multisig required to push
updates to the protocol during 1870s
Singapore there were secret societies
each with their own rituals practices
and and symbols these groups of people
self organ organized into cooperatives
to provide employment wellness and
address one another's social needs
secret society membership was only valid
if they were marked with seals on the
bottom the leaders of the secret
societies the signers had seals carved
in wooden blocks that they would stamp
in these documents secret society stamps
zero knowledge attestations only valid
with the right private key signature
Barcelona in Spain was and still is the
heart of the catalonian economy in the
tokens which contributed to their wealth
and Global Force the church saw this
practice and forked the protocol to
create their own tokens the design of
the tokens would change seasonally so
you'd get new season drops only if you
were locked in on the right day as
members of the congregation participated
in the Liturgy they could earn
additional tokens if they held for a
long time they would get more there were
withdrawal periods when they could swap
for Fiat and even greater rewards for
keeping those tokens sounds like an
incredible proof of work token with
season-based airdrops a robust incentive
and staking program and withdrawal
periods also in the 1500s the term
Privado was used to refer to a highly
trusted adviser of the Spanish Monarch
the provado was often a close Confidant
of the king and held significant
influence over Royal decisions sometimes
wielding even more power than the Kings
themselves or than other Royal ministers
themselves the provado was not an
official government position but rather
a personal one that usually involved
advising matters of State diplomacy and
even personal issues making the pado one
of the most powerful sources of security
in the Kingdom unlike the rest of our
examples today we actually don't see a
huge difference in implementation when I
comes to pado pado is still the most
powerful source of security and
discretion for decision-making based on
highly sensitive and contextual data
provado is the most powerful source of
security and discretion The Trusted
advisor to The Sovereign and certainly
to the cyer punks my name is Evan
McMullen I encourage all of you this
Devcon to hydrate be excellent to each
other and be Cipher punks thank you so
much for being here and I'll see all of
you on
chain thank you very
much now we'll have the chance to have a
Q&amp;A session any question did anyone in
here learn something new
today excellent
that was the goal I really appreciate
your guys attention I'm not going to
quiz you on medieval memes and
cryptography but if you want to talk
about that more my uh DMS are always
open okay thank you very
much
y okay come back okay we're going to
have a a short break um for five minutes
and then the next session is going to to
start at 5 40
w o
d
and welcome back um do not hesitate to
move uh towards the front to better
engage with the speaker during the Q&amp;A
session um so the next speaker is going
to be miros he's been in the crypto
webspace for five plus years he's an
expert in development product
organization and passionate about SSI
privacy social justice and education the
topic of this talk is going to be our
approach to self- Sovereign digital
identity does not work in real world uh
please welcome mirus
hello everyone and thank you for being
here I know it's like uh I know the
party is already started so and yeah I'm
looking at you Carlos uh so um thanks
again for being here my name is miros
thank you for the nice introduction um I
work in in Privado ID and I want to talk
a bit about why I think that uh that our
and I say our because I consider myself
to be part of the movement Cypher Punk
identity does not work so we have been
trying for years right to to to build uh
tools that will protect people and to
use all the cryptography and technology
that we have but how far have we
actually got um we are offering full
user control privacy decentralization
anonymity and business that is actually
building app ations for people to use
and I'm not talking about us right in a
web three bubble I'm talking about
people here on the street uh well these
businesses they want ux they want
integration they want compliance um what
are the key challenges well these right
first one is the usability talk about um
private Keys veriable credentials
concept multi-chain A lot of words that
are ununderstandable for a lot of people
right um
ease of integration if we are talking
about people that need to use our
technology or let's say businesses to
use our technology
decentralization most probably not going
to work or comes with a lot of hurdles
right and we need to work with Legacy
systems if we want billions of people
actually to benefit from all
this compliance uh sadly but we know
that the kyc AML and other stuff are
required right like it or
not so The Cypher Punk vision of total
privacy and anonymity is is an ideal
right and I'm not saying to kill that
right we need to keep the ideal there
and works toward that but
um we need to change some
stuff I call for an incremental approach
um I'm just going to take one example
here right an opportunity but there are
much more of these out there being the
European digital identity incentive so
they recognize the problem right that
the privacy of the regular people of the
common people is in danger um and their
solution is not ideal right uh they
offer selective disclosure data
minimization verifiable credentials it's
a good step forward but it's not it's
not Cipher Punk right but I think we
should join this we should hop on the
bandwagon because um we can influence
things we can try to change some stuff
and and actually this is why I'm here
right I would like that that this debate
happens here between all of us and all
of you that are out there on the
internet um so what we could win right
we could promote privacy for standards
we could encourage more adoption we can
actually have more private and
decentralized Alternatives um Jordi Bina
yesterday in his talk mentioned and I
agree with that although it's not ideal
right I would rather trust my um private
data with a government than with a
corporation again it's not ideal but it
is a step forward
right and no this does not mean that we
stop fighting right um I invite you all
to think critically about
building advocating or using right the
solutions that are both streaming
towards Cypher Punk right but
are adaptable and can be used in real
world right let's please try to balance
right um idealism with practical
constraints so we can
achieve more with what we have today
streaming towards the ideal world right
um there were a lot of talks and and I
like the the the the talk the that was
here the previous from in and and the
other one right
um and yesterday there were a lot of
also talks about um Cypher Park
movement um it is important all of you
need to join if you are not part of that
but again I advocate for an approach
that is incremental that we think not
only about ourselves but we think about
the people that are out there on the
street that doesn't mean that we do not
need tour that we do not need all the
tools for journalist for people that are
doing really important things that yes
but also yes
for the common people
right the struggle continues I MOS thank
much thank you so we will have some time
to ask a few
question oh raise your hand if you have
any question I I can throw the the the
red square at you oh you want to no I
mean I'm challenging oh
okay any
questions oh over there do do you want
to thr
no I don't want to he the the CSO of my
company maros obviously there are a lot
of examples that you've described of
ways in which things are
suboptimal now ourselves aside who else
is doing it right like are there
government leaders are there Enterprises
are there I you know I idealists or
leaders who we should look to in our
institutional structures as potential
Partners I think yes I mean you whoever
was on a bunch of all these talks that
happen yet and they are going some going
to happen tomorrow and the day after
there are people right that are trying
to do all this and of course it's I I
know our team best and and we are trying
the best that we can but I really like
for example that having the the
initiative coming from the European
Union that's 650 million people that
tomorrow can have privacy towards Amazon
yes where do I sign right but that's not
the end game so there are people there
are things that we can do and
and that's it right no you're right
absolutely that's a great call out
European union and also shout out to the
ethereum foundation for showing up this
week on this topic too
yes thank
you and that's a drop mic literally
any more
question okay no well thank you very
much please give a nice round of
applause
toas and so our next speaker is going to
be era um she runs her own design
practice she's an independent designer
specializing in branding and um visual
design strategy and the topic of our
call is going to be visual code of
Cypher Punk and lessons from subcultural
Aesthetics we should remember on the
road to mass adoption please welcome
era let's tune the wipe
so we all want Mass adoption for our
products and we want these products to
be loved and used by many and yet we
have one heavy anchor that will always
hold us back from Mass adoption a visual
language or cyer frun let me show you
what's happening visual language
consists of two core layers the symbols
they carry meaning and cultural baggage
and the styles styles evoke emotions
they always go together when when it
comes to how we respond to visual
messaging a positive style in a posit a
positive symbol in a positive style
evokes Joy a positive symbol in a
negative style makes rather negative
impact think about toys in the horror
movies a negative symbol in a positive
style can cause confusion but rather it
BR in am amusement and think about
Halloween and a negative symbol in a
negative style evokes not nothing like
fear and disgust people try to distance
themselves from everything that lives in
this quarter while adoption lives there
how do you think where cyber fun is
let's see the first symbol anonymity
mask traces back to guy folks who earned
a reputation of a failed terrorist and
actually never fought for
democracy while Alan Moore tried to
recover this image uh in the comics via
Vendetta making it a symbol of
vigilantism but later Hollywood
successfully shifted the message adding
a narrative with a fear creating
taglines and a lot of blood today it's a
symbol of Cypher funs now here you
already see a second symbol hoods that
was originally associated with monks the
knowledge Keepers which is good
beginning but later that became a symbol
of secret societies uh many of which
practice ritual murder and dark magic if
such a thing exists and recently hollyw
would dressed all the Assassin in hoods
adding a nice layer of death and blood
to the overall image today Hoots is a
symbol of cyer funs well here you
already see the next symbol which is a
common line romance which Again by
Hollywood in a form of digital rign
together together with the technor Style
presented technology as a global threat
to everyday life and the last style I
would like to mention is uh glitch
effect which was a way for early
internet artists to present to to
visualize a system vulnerability and the
beauty of breaking it but for normal
people the glitch effect evokes the same
feeling as breaking glass now how do you
think
where on this metrix Cipher funs
are well fortunately we have a century
of subcultural movements that can teach
us how to ease this tension between our
heritage and the past and the mass
adoption needs so here are three main
lessons I want cyer funs to hear first
choose joy as a strategy Cipher Frank
looked like it was designed for
postapocalypse but privacy should not
look like paranoia it should look like
Freedom just look how uh Pride movement
turned the protest into a celebration
they didn't promote a better hid in
spaces they promote they they made
visibility powerful and joyful itself
and you may say me rainbows but people
love rainbows ethereum love rainbows
so we already want this Joy uh next
lesson aim for Simplicity cyer visuals
require technical tools to reproduce
them but if your grandma and even you
cannot draw the symbol with anything
that you have in your hands right now it
will not
spread uh Extinction Rebellion teaches
us how to do they created a symbol which
a child could draw in seconds and every
human could reproduce with anything they
have around they later gave this symbol
to communities and communities style it
with their own wipes to represent their
emotions around the movement and the
movement went
Global and last example Embrace VAR
Embrace Evolution uh black panthers used
powerful yet very aggressive imagery
usually containing weapons because of
this aggression the movement didn't
achieve the reach they hope for but the
movement did not die the new generation
learned from the past and took over and
moved from displaying weapons to
displaying words from we protect
ourselves to we deserve to be here and
they reached millions and
more so if I were here I incarnation of
all the subcultural movements from the
past I would ask our eem to not not make
ethereum Cipher fun again but to make it
a new Cipher fun and maybe just maybe it
will also have a different name thank
much so we have a bit of time to ask a
question raise your hand if you have any
yes who's doing it right who can you
call out or are there any examples um
that you've seen this week of different
ways to evoke this um sentiment in our
ecosystem
visually I mean who is doing the right
Cipher fun style or who is doing the
right in
general we are here right now
so we have some more question over there
hello um thank you for the talk so my
question is from the kind of negative
examples that that you presented it
seems like a lot of them were kind of
you know serious tough masculinity
focused and crypto as an industry is
also quite masculine and in terms of
just people who tend to you know run the
companies uh if we gather up everyone
who works in crypto mostly it's men and
uh one of the positive examples that you
had was you know the pride flag for
example which is something that is quite
challenging to traditional masculinity
so how much do you think that plays into
the current branding issues that crypto
experiences thanks well I'm so glad you
ask this because because like maybe 20
minutes before the talk I just cut off
one slide because I needed to fit in
five minutes but after the glitch effect
what I wanted to say is The Cypher frun
imagery has a very heavy gender cording
and is all white male
narrative which is exactly what you tell
about
um well um all those movements that I
showed they actually showed the equality
of everyone and what I really love in
ethereum here right now in Devcon is we
have more of non-white people so it's
really good that white people are not
dominating
here um also if you study cyer Frank
movement itself uh there were a lot of
uh Regional um directions who actually
didn't go for this American uh White
narrative cyer fun and actually for the
original cyer fun movement Hollywood did
a lot of bad job for us because as much
as we were trying to narrate uh well
developers don't do a lot of good job
for the visual communication so they did
a lot of good stuff for like like vision
building uh but Hollywood knows how to
show masses what exactly the government
wants to see and if and in general
nothing goes on the screen which can
harm the government so even V for
Vendetta the author of we Vendetta
wasn't involved in the movies because he
didn't agree with the flatness and
bloodiness of the movie
creation the original Comics had a very
deep narrative that you actually need to
see where he comes
from did I answer
question thank you so there's a last
there okay if I may I would like to have
like a very small comment I absolutely
do agree with you that uh the imagery we
are using as holding us back and this is
like spot on and well job but job well
done but uh none of the images that you
showed are actually connected to the
original Cipher Punk movement because
they didn't have any image it was just a
mailing list uh very traditional mailing
list that didn't even allow to attach
any imagery the closest they they were
getting to having any visual identity is
when three of the people uh from the
original Cypher Punk movement were uh
featured on a covered of Wire magazine
and they were wearing masks but they
were very different mask they have
nothing to do with guy folks and it was
not their idea to wear the mask that's
one thing
uh second they used one pretty cool
image that became like really associated
with them but not with the movement but
one of the campaigns that they were
running like in early 90s there was this
danger that US Government will U impose
a surveillance mechanism on a
communication was like Clipper project
and what Cypher punks did was like
basically they hijacked Intel logo and
instead of in inside they put Clipper
inside and this was became like a
sticker that they were Distributing in
many many places and so this was like
quite successful but everything else
that you showed was had absolutely
nothing to do with cyber punks and and
one last thing cyper punks the name
itself it's not the that they created
they were not considered themselves to
be a cter cultural movement it was
basically a joke from someone uh who was
looking at them and and uh um commenting
how they are like approaching things but
they were not punkish at all absolutely
yes and that's how branding works it's
not what you say about you it's what
others say about you so I encourage you
open your laptop and Google hacker icon
and see what you have in the just Google
Cipher funs and see what Google gives
you and it's yeah that's the whole point
there the world world and we know which
powers are engineering the reputation of
cyer funs which is going to the minds
and hearts of people outside of Crypt
bubble and the call is not being passive
around this but actually do actions to
create the image that we want to have
not what happens because some other very
powerful media narrative is shaping how
people see us
thank you very
much so our next speaker is going to be
uh vvec he's a cryptographer and
designer at cursive working on
cryptography for human
connection and the topic of his talk is
going to be making defensive technology
offensive how to get Cipher Punk ideals
to the masses please welcome Vic
cool hi guys um so my talk is going to
be about
basically like focused on cryptography
as a defensive technology because that's
my area of expertise um how we can take
uh various cryptographic tools that are
super powerful and try to find ways to
communicate them uh offensively and
maybe maybe yeah just just to be clear
this is more like encryption signature
zaps this sort of thing obviously Under
the Umbrella of like DC and defensive
Technologies there's lots of other stuff
going on and I think how I would
personally Define cryptography is that
it's the art of making things hard to
break uh in this definition it is like
very inherently a defensive technology
you're literally trying to make tools
that is very difficult for adversaries
to forge or break into or otherwise uh
sort of damage the Integrity
of and I want to look at just a very
small set of examples here this is not
comprehensive at all but uh at one
really prominent use case of privacy
preserving Technologies in the wild
which is VPN um and vpns I think if any
of you guys have been to like New York
or Chicago or a couple other major
American cities you might have seen
these like mulad VPN ads everywhere uh
for Contex I personally use mulad um so
this is not really a dig at them but a
lot of their ads are very sort of like
intense Cipher Punk kind of vibe of like
you know like a bit of both like hopeful
but also kind of like fearmonger and I I
honestly am not sure how successful this
has been for them I definitely know for
myself like I got mulad before these ads
came on and like when I do see them in
in in like the subway in the train I'm
like I always think like is this like do
people want to see this sort of thing
and like one reference point in my mind
that I have is uh nordvpn a lot of these
other vpns this is not actually a ad
from them to be very clear but uh if
you're a big YouTube user you know that
like Nord and express these sort of VPN
companies are like major funders of like
every YouTuber and it's really
interesting to see how that marketing
has changed over the past years I feel
like initially it was very much focused
on like oh like this will protect you
from like you know your internet
provider seeing your history and often
that's still mentioned but actually most
of the time now the emphasis of the ad
reel is always on like you can watch
Netflix in other countries you can like
do this like new like you have this new
affordance from using this VPN uh and
that's always kind of like what they
like talk about for a little bit longer
and I feel like it is a very uh good
represent ation of the fact that like I
think users will generally respond to
things that are value ads um and not
purely sort of defensive measures
against like some sort of like threat um
and to be clear like I'm very much a
cipher Punk and I like deeply believe in
this technology but at the same time I
also believe that if we're not able to
do this sort of like communication work
uh we're not going to be able to get
users the defense and safety that they
deserve and so I want to talk through
just a few different kind of like
highlevel affordances that I think are
worth leaning into and talk about more
uh the first is idea that privacy is
really ownership um and I think
ownership is something that a lot of
people feel all more viscerally with
stuff like you know big social medias
like hosting all your photos you don't
own any songs anymore with Spotify and I
think there's a general sense of like
this is something that people like don't
have that they that they wish they did
and in general I think like one really
nice thing is that with cryptographic
tools um with signatures uh with like
sign data on all sorts of different
things you get to actually like own your
own data and and like have it be
verifiable but then if you want to
actually maintain privacy on top of this
like it Works hand inand with other
tools like ZK and really like if you own
something it is almost to some extent
like private to you like you should be
able to sort of like keep it to yourself
unless you want to share it and a lot of
cryptographic tools give you exactly
that another is the idea of user consent
and this comes up uh really interesting
way with something called multiparty
computation which is this cryptographic
tool where multiple parties get to sort
of do a computation on their private
data um there's actually a really nice
feature where if one of the parties like
leaves the protocol or otherwise just
decides to like um you know that they
don't want to be a part of it uh no
result is reached and I think this is
actually a very nice like positive
feature uh where it's usually viewed in
a lot of protocols as like a bug where
user consent is almost like
mathematically required um and I think
this is like an offensive useful thing
that people would be able to understand
know this idea of portability or
interoperability or verifiability like
they're all kind of the same thing and I
think um a bunch of really cool use
cases of this like one is like portable
social graphs um this is uh like an app
experience that I've been building with
my team where you're essentially tapping
different folks and building a private
social graph that also you can take with
you to other apps As You Wish um and I
think this is something that a lot of us
are feeling now when we're like locked
into sort of social medias that aren't
really working for us anymore another
really good example is just all personal
data stuff like ZK email enables you to
take things in your own email and
basically make proofs about them share
them with other people in a way that
means they don't need to just live in
one
service and finally I think an underated
one is efficiency um there's this new
idea that we've been exploring called
narrowcasting which essentially
basically if people do have their own
ownership and privacy over their own
data you can basically send messages in
a way that will only be read by the
people who like match this criteria and
so in a sense you can actually use
cryptography to more efficiently like
like disperse information uh in a way
that's priv is preserving uh really
quick uh where you can experience this
we have a booth um downstairs my team
cursive uh where we're showing an app
experience that has a bunch of these
different features baked in uh one thing
I'll call out is something called
private seter section which lets you see
what you have in common with other folks
and um yeah there's going to be some
more features added in this is where it
is in the booth and um yeah that's
that's the talk thank
you thank
you so we have time for a few
questions please raise your hand if you
much oh yeah uh we can have a quick
break uh and we'll be back at 6 uh 10 6
okay so welcome back the last oh no it's
not the last sorry next to last uh the
next speaker is going to be uh Max he's
a senior developer relations at n
Technologies um and the subject of the
of the talk is is going to be from pet
to privacy understanding and evolving
network security please welcome
Max cool hi everyone um yeah the talk
says Max Hamshire and M Mo it's just me
today
so yeah packet to privacy um I am Senior
devel at Nim we are a company that
builds mix Nets and and a decentralized
vpm product at the moment I'm going to
give you a bit of a tour of uh could of
a bit of a flash drive through how
packets move through networks just so
we're all on the same page how
inherently insecure they are and how we
can try and protect it so initially how
packets move through a network so we're
on all on the same page for the rest of
conversation data is sent between two
network devices in packet pet packets
are just chunks of data right so you
don't have a stream to whatever server
whatever rpcm Point you're actually
trying to connect to you send all the
data in chunks just so these things can
multitask and talk to multiple things at
once right packets themselves broadly
speaking contain a header which has a
bunch of information about the protocol
the type of content that's in this
packet the origin IP address and where
and the IP address that it's going to
right which corresponds to physical
space as well uh then you have the
payload which is your actual data
sometimes you have tailor as well which
have more information I'm not going to
go through this whole list you can take
a picture or come and talk to me
afterwards but this is the metadata the
data about the data that is exposed by
sending packets unprotected uh through a
network between two devices so where
it's coming from where it's going the
location when the type of packets higher
order patterns like the signature what
it kind of looks like um repeated
Communications maybe also like device
IDs accounts email addresses cookies
fingerprints all of this kind of fun
stuff and this is ultimately because
when the internet was made it wasn't
made with network privacy kind of in
mind and the situation at the moment is
that Network traffic is captured and
analyzed both by governments and
corporations kind of on mass they just
blanket capture everything and what they
essentially try and do is using machine
learning try and find patterns in this
data who's talking to who and when where
you're located what kind of traffic is
being sent and then relationships are
inferred from that why are you only
talking to you after midnight what's the
nature of your relationship all of these
kinds of things right so which can be
used to De anonymize you there's a lot
of different approaches that people take
so if we look at this diagram right at
the bottom we have your kind of
centralized VPN should we say all you're
doing is you're kicking the trust down
the road you're sending all of your
packets to a VPN provider their server
then forwards it on to wherever you want
to go right you're not able to defend
against anyone
who can uh see the size and the timing
of your packets and be able to infer
what you're doing maybe you're
downloading a video maybe you're kind of
getting your emails or something and
that is a centralized point of trust
that you're trusting that that vpm
provider will not sell your data and or
when they are subpoenaed give your
information Away tour does a bit better
um it doesn't have a single point of
failure in that regard but against
someone who can watch uh watch kind of
the whole internet which is kind of the
situation we're in now then they can
still be Deon
tour does not add noise to their
connection it doesn't pad the packet so
they're the same size you can still do
traffic timing attacks and all of this
kind of stuff mix Nets however fragment
your packets into um encrypted Spinx
packets all the same size they will look
exactly the same individual packets are
rooted differently through a
decentralized network of mix nodes that
delay the packets variably as well so
what you're doing is and we also have
cover traffic so there's kind of hiding
a signal in a noise idea right so what
you're doing is you're reducing ucing
the capacity for an observer to be able
to pull patterns out of looking at this
network traffic right to be able to De
anonymize
you and another technology we're working
on as well ZK Nims which are Anonymous
credentials for payments because non-
Anonymous payments are a problem I want
to pay for a privacy service that helps
me out even if I want to pay with mulvad
and I want to pay in zcash or use rail
gun or Monero um they're still
susceptible to network de anonymization
and generally we'll have a small
anonymity set of people who are using
that stuff to pay for a VPN however
privacy loves company you need to have
as big an anonymity set as possible the
possible sets of variations of actors to
uh basically make this patent finding
impossible therefore you need to be able
to construct a way where people can
actually pay in Fiat or pseudonymous
cryptocurrencies right but the usage is
cryptographically unlinkable to the
actual payment so I can basically say
yes I've paid for this in you know with
my credit C card however you can never
tell when how much they're using this
credential to access this privacy
service itself they're also selective
disclosure credentials which means that
you can prove certain things about
yourself maybe that you pass that you
have paid for something and in a
generalized sense you've gone through
you can pass kyc you've done another
payment you can vote in a da um it's
decentralized because it's uh generated
by our validators and it's a combination
of the coconut and offline e-cash
schemes finally Nim VPN is a the first
kind of um the first kind of product app
that's being built on the mixnet for
Network traffic protection so we are
using ZK Nims for private unlinkable
randomizable payments and access
credentials it has two modes the
anonymous mode where it goes into the
mixnet and you get the full um full
metadata protections of the mixnet and
it also has a two hop uh dual tunnel in
a tunnel wire guard which is using the
outside fringes of the mixet INF
structure if you want to we have an open
Beta right now um also come and talk to
me afterwards and I have um Flyers with
credential codes on them so you can try
it out I am also Devo if you want to
build with this because all of this that
I've just said also applies to you know
all crypto apps wallets everything uh
check out our Builder docs or come say
hi afterwards
thanks thank you Max um so do we have
any question no over that
thank you so if someone is using you
know there's the simple mode that's
faster and the more complicated node
yeah if someone is using the simple node
what can the government find out about
me okay so you still the the Speedy mode
where is you have tunnel in a tunnel
right you're still doing you're
disintermediating none of the
infrastructure that your traffic is
going through neither of the gateways
that it's passing through can have the
full picture of of either where your
traffic is going or where and where it's
coming from right so you're breaking
those two things apart Nim also has uh
Anonymous reply systems as well so you
can talk to a service and then you kind
of send let's say pre-addressed
envelopes along with that traffic so the
replies are all anonymized so the people
you're talking to don't know who you are
basically right so you never dock
yourself um we don't it doesn't have the
addition of the noise and the mixing so
there is that to be said one of the
things that we want to aim for with this
is split tunneling so then you kind of
get to a point where if you can capture
say all of your devices networking
traffic and then the stuff that is
essentially asynchronous messaging apps
email anything that's not like browsing
and streaming basically you can send
through the mixet mode and then for the
other stuff then it's still better than
the vast majority of other options out
there basically yeah yeah I started
using it yesterday
thanks do we have any other questions
over there and
there thank you for the talk um just a
question so if so you want to have a
decentralized VPN solution I
assume yeah that's that's what the
Speedy mode is essentially yes um so the
the exit nodes there the traffic is
basically internet traffic that comes
out at the end yeah um so how do you
protect those node operators from
malicious traffic so if if there would
be like illegal content being downloaded
from location where at we're relying on
using TOS toal list um so we're
basically like you know Tor and a bunch
of other people have had this problem
for a very long time so we're kind of
using a lot of the public resources they
have there in terms of the uh block
lists and everything that like they
maintain so we're starting off with that
but we're also working a lot with our
valid with our operators and uh yeah
kind of putting together making sure
that everyone's running in a particular
like legally okay way and that they have
protection as well but it is a thorn
it's a problem it's a constant problem
but yeah okay well thank you very much
unfortunately we we won't have time for
another question um thank you very much
for for your presentation uh and please
give some Applause to also anyone who
wants t-shirts I have a bunch in my bag
for questions and stuff afterwards so
come say
hi and so the next speaker is Manu aluru
founder of eth Barcelona and block
ravers and founding members of API 3.org
he also a partner at own.
fund and the
member of meta cartel an adviser to
multiple web three projects he going to
talk about solar Punk versus lunar Punk
the evolution and integration of these
movements please welcome Manuel Al
aluru hello everyone thanks for coming
to today today I'm going to talk a
little bit about the solar Punk versus
lunar Punk the evolution and integration
of these
movements so before we talk about solar
Punk and lunar Punk maybe we go a little
bit uh on History actually thanks to the
ne guys yesterday they did a sick
presentation about uh the punk movement
thank you for that shout out to them um
so yeah let's let's start very quickly
here so the punk mov me in the late in
the late 60s and the 1970s actually
started as a music movement um who knew
here that actually the punk movement was
a music
movement okay perfect there's a lot of
people that do know that which is really
good um what happened there is that the
there were people that were a little bit
depressed because or not depressed just
not happy with the state of the rock
scene The Rock scene became a very
commercialized thing so the punks they
were against this commercialization they
were against all this mainstream and
this anti-establishment they were like
basically anti-establishment so they
came up together and they started to
create their own environments they
started to create their own culture they
started to create their own way of
dressing up they started to create their
own ideals and so on
and uh the main ethos of the punk
movement was do it your own ethic um
valuing the self-expression the personal
responsib ability and the direct action
um then uh after that we had in the
early um 80s we had the Cyber Punk
movement and the Cyber Punk movement was
it started first like a Sci-Fi type of
thing so basically um someone um I don't
remember exactly the name wrote a novel
about cyber Punk and also cyber Punk was
start started to be mentioned more and
more in literature in the early uh
were being created um were basically
anti-authoritarianism and um kind of
like showing like a resistance against
the state or against like any form of um
coercion um and yeah um another another
that is another thing that is important
to mention about the Cyber Punk movement
was that this um this let's say um
movement was created thanks to uh a lot
of literature a lot of um movies like
Blade Runner and more more more um more
let's say films and different let's say
forms of media that was basically
showing to the world that we're going to
be living in a world where um where
there's going to be a lot of Oppression
and there's going to be a lot of um
control by the different um the
different organizations um not
necessarily the state but actually the
corporations
um then in the late 80s um there was
also again a new Sci-Fi um term that
came up which was the steampunk and the
steampunk was kind of weird because it
came after the Cyber Punk and the
steampunk um it came after the Cyber
Punk uh again the Cyber Punk was like
this idea this futuristic uh dystopian
um um distopian a scenario where you
know corporations were going to attack
uh the individuals and basically we
going to be surveilled and so on in the
steampunk they were imagining themselves
even though they happened in the 80s
they were imagining themselves that they
were in the Victorian era era and that
they were imagining in the future how uh
how let's say the steampunk type of
let's say culture would look like um the
steampunk uh for those that uh that are
not aware uh they usually use a lot of
Gears a lot of mechanical things if you
Google quickly steampunk you you
probably see that a lot of people um
have been like going to festivals with
this type of uh with this type of um um
let's say how would I call it
aesthetic then um the cipher Punk the
cipher Punk came the in the early 80s
and basically was um was with the idea
of uh creating more encryption and
creating this say more tools that we
allow people to um communicate directly
to each other end to end
um and yeah basically um the main ethos
is privacy Freedom uh through encryption
and digital autonomy then came up the
solar Punk movement and the solar Punk
movement was in the mid
movement was basically to have kind of
like a more optimistic view of the
future and how we can use technology for
the betterment of
humanity and then uh later on in 2020s
uh the lunar Punk movement came out
which was uh a movement which is a
movement that was basically uh around a
lot of mysticism uh when it comes to um
privacy and also um the balance between
the light and the dark or the Shadows or
what they call it the Dark
Forest and this movement emphasizes
cryptography and privacy tools um this
is the first video that actually
explained um a about the uh rise of the
lunar punk I'm not going to show you the
video because I don't have time uh but
afterwards you guys I'm going to share
with you the slide so you guys can see
but one of the things that they say in
the video is that solar Punk hackers are
creating transparent infrastructure for
funding public goods and that was kind
of like one of the things that they said
that is not necessarily good also that
the lunar Punk has been forced um to
break away from the solar P Legacy which
is basically all of these technology
with ethereum that is very transparent
and very open for everyone and yeah
basically I started tweeting to the
people that were that created this video
and say hey actually I find that I find
that you guys are kind of like being a
little bit populist and using like uh
using a narrative against the solar
punks um when in when in reality a lot
of the solar punks we do care about
privacy and actually um Rachel who is
the person that is behind the lunar Punk
movement she started replying to the
tweets and saying well uh the article is
merely is merely uh pointing out
authoritarian tendency within the solar
pong uh within the solar pong ecosystem
and and yeah basically she was saying
that proof of humanity and gitcoin they
are not necessarily really align with
values um here there's also a video that
talks lunar P versus solar solar Punk
versus lunar Punk uh with Kevin aukee
also we have it in the slides you guys
can check it afterwards um and yeah
basically what happened afterwards is
that when we started having this
conversation with rose we realize that a
lot of the things that the lunar punks
believe are very similar to the things
that the solar punks believe I myself I
was I was calling myself a solar pump
for a lot of years until uh until this
new let's say uh Narrative of the lunar
Punk came out when this new narrative
came out I stopped calling myself a
solar Punk because it was not really
clear what a solar Punk was and so on
and I'm saying all of this to you guys
is because it's important to understand
that we are creating the we are creating
these movements we are creating them
using language and using um using let's
say uh narratives
so that means that we need to be very
aware and very conscious of like the
language that we use when we're creating
these different type of um different
type of movements so as I said before we
we realize that that a lot of the values
that the solar that the lunar punks uh
said that they have and and the values
that I consider that I had as a solar
Punk uh are actually very similar but if
we extrapolate all of all of the all of
the things that the solar Punk or lunar
punks are saying one thing we have in
common is that the solar Punk Cipher
punks cyber punks or any of those punks
movement the only thing that they care
about was protecting their community and
having a better world for their
community and for their
Humanity so again if we
extrapolate all of the differences
between all of these different all of
these different movements the main
common de denominator is that word care
they care about their communities so the
what is the highest form of care to me
that's love and that's basically why I'm
calling myself a love Punk and that's it
for today if you guys want to learn more
about the presentation um there's
there's a a lot of videos there in very
informative videos check out the QR code
and connect with me and yeah let's let's
chat more about the New Movement love
punks thank you very much
um that that's a wrap for today
unfortunately there won't be a time left
for Q&amp;A uh but but perhaps you can ask
directly a question to man thanks again
for your presentation
um so as I said it's uh that's it for
for today but you can come back tomorrow
it will still be under the format of
lightning talk um so yeah have a good
evening and see you see you tomorrow bye
back I'm
here o
