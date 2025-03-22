[Music]
for
[Applause]
all
oh
I
B
o oh
o
hello everyone good morning how's it
going guys we have some few people here
this morning so how was the first
day yeah we had some packed days with a
lot of interesting talks so we're
starting
today uh with the first session which is
applied cryptography so I think we have
like five or four or five talks so I
will be the MC so my name is Yousef so I
work for Linea I was a speaker yesterday
at the very same stage today I'm a I'm
an ny life changed fast
right so yeah hope you're enjoying your
time so maybe we're going to start with
the first uh
talk so we have aush Gupta who's a ZK
Ste
steart uh and co-creator of
also uh plume signatures thec and then
we have also s
suami and they're going to talk about ZK
email so this is one of the
applications I'm most interested in like
for ZK for real lives and the stage is
yours thank you
enjoy
sweet today we'll mostly be talking
about ZK email new applications and
production ready account recovery I'm
aush I'm
Sora and most of this work was only made
possible because of this incredible team
of folks we have working with us so huge
shout out to
them so we'll start by mostly going over
the basics what is ZK email how does it
work then we'll dive a little bit into
how you can make proofs really easily
and we'll discuss a new registry in SDK
that lets you do that and we'll try to
expand the possibilities for how you
think zkl proofs can be used in
reality finally we'll talk about account
recovery and how you can generally have
email triggered trans actions on
chain and last we'll talk about Dev
tooling all the different ways that
we've put together tools for people to
build these kinds of proofs really
easily into existing
apps so to start with the basics what is
ZK email the idea is that emails are
signed according to the deim protocol an
RSA signature of the shot V6 of the
content of the email this is applied to
every single email sent to reive since
but we prove this inside of a ZK proof
and add selective disclosure and
parsing this means that we can get
proofs of emails where we can get
privacy as then we can hide or reveal
whatever we want we get Providence we
can verify the data from the web two
Services mail server directly and it's
portable we can verify it directly on
chain on any any chain that can verify
these
proofs you could imagine the simplest
intuition for this is something like
whistleblowing we take an email you've
already received and we redact different
parts of the email and then we prove
that the email was still valid or sent
by The
Source but you can do much more than
this for instance ZK PP builds
marketplaces on top of these emails one
example is a domain Marketplace the idea
is that you can take any name Che domain
that you own and you can list it on this
Marketplace and when you sell the domain
to somebody AK you transfer it to them
both of you receive a confirmation email
from Nam CH automatically if you prove
that confirmation email on chain you can
then unlock esro money directly to pay
for that domain this is quite compelling
and the idea that you can interoperate
these web 2 assets or things in the real
world with things on chain is extremely
compelling and how can we get more of
these so our idea was what if we made it
really really easy for somebody to
create new proofs and update those
proofs so we'll talk a little bit about
how this can be
applied uh to General proof
infrastructure in a couple of different
ways a registry that lets you reuse
proofs that other people have already
defined and Define new ones very easily
an SDK lets you use them very easily in
your application and finally some
inspiration around what are some apps
that people are actually building with
this so one of the main problems with ZK
development today is that an app
developer who's trying to build
something related to their emails should
not have to think about the nitty-gritty
details of which proof system they're
using and the different trade-offs and
different systems so the idea is you can
abstract this all the away
you just Define a sort of a blueprint
like oh I want to prove that I was
rejected from giving a Devcon talk for
instance and then if I Define this kind
of blueprint anybody can use it without
having to think of the proof system
that's happening in the
background how does this work the idea
is you can create new patterns very
easily for instance after naming your
pattern and uploading a sample email we
can automatically parse out the relevant
information from that email to help
Define this new kind of
pattern for instance we can take out the
center domain automatically or things
like the email length of the header or
the
body then we have this nice feature
where because we want to define a Rex to
extract specific information from within
that email we automatically they're an
AI on top of that raw email data and
Define that Rex for users we found that
historically this has been a bit of a
roadblock because having to adapt Rex's
to different kinds of email templates is
often not a very intuitive task but
we're hoping this makes it super easy
for anyone to define a new kind of proof
with no relevant ZK or necessarily even
parsing
experience and finally it'll give you a
configuration like this this is a decent
amount of text but the main thing to
take away from this is that it's only
about 20 or 25 lines this defines all of
your rexes where they occur and who the
email was sent from and other metadata
about it but this is a full
encapsulation and definition of your
proof then in the background we can
automatically compile this to all the
proof systems that we listed right now
we have circom and Noir incoming and
also z kvms um and once it's completed
the compilation is completed we
automatically will deploy an interface
that anybody can use to create this
proof we see this kind of like almost
like a bit of a versel you can sort of
create your proof and deploy it without
having to think about any of the
infrastructure behind the
scenes concretely for instance for the
proof of Devcon rejection you will
automatic Al get an interface for you
where you can automatically sign in with
your email and then it will fetch the
relevant emails that might possibly
satisfy this
proof we can filter those emails
entirely client size that our server
never sees those emails and then let the
user choose the proof they want to
select to make a proof of in this case
for instance for GitHub uh for Devcon
you can choose one of the specific
Devcon rejection emails or for a GitHub
you could choose for instance uh a
GitHub username email to let you prove
your GitHub username
finally the proof can happen in the
background and you can share that proof
out to whoever you want to share um and
we also show you the metadata very
clearly and even let you look at the raw
proof the idea is that once we have
these kinds of definitions we can expand
this even one step further we can also
kind of treat it like a bit of a GitHub
where each of these configurations can
be edited and Modified by other people
and you maintain a version history so
for instance you can imagine that each
of these patterns comes with versions
depending on email templates as they
change or users as they want to parse
different kinds of things and if you
decide hey I don't like this pattern I
want to replace it with a different one
say I want to take my Devcon rejection
email and instead I want to prove Devcon
acceptance I can just Fork it change
that value and recompile it and so we
see these kinds of flows that developers
are very used to also being useful for
General people to be able to create
these new kinds of
proofs you can try this out live if you
go to registry zk.
um we've put a QR
code up um these you can define a new
proof by logging in and then creating a
new pattern or trying any of the
existing ones within the interface um
note that there will probably be a
decent amount of load as all the folks
in the audience try this but we will
have a workshop tomorrow where we go
through detail uh step by step how
exactly to do
this now if you want to integrate this
into an actual application again you
don't need to read the code but just the
idea that this can just be three or four
lines someone can just Define this is
the kind of blueprint that I want to
prove within my app in this case the
Devcon rejection proof they can say they
want to be local or not and then they
can again you don't have to read the
code but they can just generate the
proof and verify it on chain if they
want without having to think about the
proof
system we've seen people build a lot of
really exciting stuff with just this
primitive for instance folks have built
proof of U sign or hello sign where you
prove you signed some document with some
title from somebody can prove you took a
flight to or from so and only reveal
where you took it from in the
destination someone created this proof
where you can prove your part of a slack
workspace you can now start seeing how
these things might start combining you
can build a system where you prove your
part of an organization on slack and
then you automatically get reimbursed
for your flights by proving you took
them and as people start realizing oh
you can bolt these things together you
can build actually interesting systems
on chain where you combine different
facets of ideas or identities or actions
we've taken in the real
world people have also proved for
instance you've exported your LinkedIn
data which they then sell to for
instance open AI to train on you can
then prove you orted all of your open ey
chat data and then sell it to for
instance
anthropic you can also prove you
automatically resolve the GitHub issue
and then automatically disperse
contributors for their
contributions John did this fund proof
where you can prove you ordered a pad
Tha in Thailand where you basically show
you have a grab receipt which has the
word pad Tha on it and a location that's
in
Thailand and of course you can prove
that your proposal was rejected from
Devcon so now that we have all of these
basic concepts around how you can make
proofs of emails that you've received in
your inbox one might imagine that you
can also make proofs directly on chain
so far we've just talked about of your
identity that already exists in web 2
but emails you can imagine are an
interesting interface to actually
interact with onchain apps
directly so concretely how might you get
this new kind of email triggered
transaction well the idea is that
instead of doing what we were doing
earlier where you log in with email for
and you select one to make a proof of
you instead send an email to trigger a
transaction on
chain this is quite interesting because
now you can have a smart contract that's
directly gated just by a sent email this
primitive is quite powerful you can
build things like account recovery for
instance where you add emails as wallet
Guardians directly on your existing
smart
accounts things like email signers where
you can add an email directly on your
multisig and have that approved
transactions for instance as a 2fa or
for f who don't have EA wallets to be
able to still approve
transactions you can log in with emails
this is something folks have wanted in
the system for a very long time but the
idea that you can interact with aage
application or crypto app just by
logging with your email and then using
that to authoriz an Emeral session
key or an email wallet where you can
receive assets directly to email
addresses even if they've never signed
up but
today um we'll mostly focus on I guess
to start with exactly how we can do
these kinds of smart contracts with
emails so for instance the flow here is
that users can receive some email asking
them to trigger some kind of transaction
and by replying to it they can initiate
that transaction on
chain They will receive an email kind of
like this we've moved the actual value
that's getting approved to the subject
so it's easy for you to read um but the
idea is that you would receive a command
kind of like recover account eth address
from Old owner eth address to new owner
eth address in reality users would just
see a simulation in their email not this
text but we've put it here so it's easy
to
read and the idea is that by replying to
this email they're effectively signing
this message which can then be used to
send
onchain flow here is that a user will
try to trigger some sort of transaction
a relayer will send them an email when
they reply to that email action is then
sent directly by the relayer on chain as
they make a ZK proof of that action
one of the cool properties of this is
the idea that we have this account code
for both privacy and
decentralization you can kind of see
again we've elevated it into the subject
here but normally this would just be
embedded into the body where the user
doesn't have to think about it but what
is the point of this long hex string
it's not really private key or something
we're necessarily exactly used to and
anyways it's abstracted away from the
user but it is nice because this value
gives us direct email address privacy on
chain we never reveal the email address
we only ever reveal a hash of the email
address and that
code we can also prove availability to
the user in this email that is
concretely we can ensure that the access
to the user's account cannot be withheld
by us going malicious because as long as
they have the account code they can
still transact with that email contract
and finally it allows for relayer
decentralization anyone can run this
kind of system can run email servers
that send out emails receive replies and
then trigger transactions on
chain you could imagine this can happen
via email replies as it does right now
or even directly via Google logins the
difference between these is mostly basic
security for instance on the left side
you can show concrete simulation data to
the user of what they're signing for
Google signin it's more like a blind
signin uh and a blind signature but the
idea is that applications can choose
whatever they want based on what is most
convenient for
them okay so from now our among the
products using email trigger
transactions U here we introduce the
details of the email account
recovery so in short using email account
recovery you can specify anywhere with
an email address as a guardian for your
wallet and when you lose access to your
private key this Guardian can help your
account or this Guardian can help
recover your account just by sending
emails and in this way this achieves a
similar ux as a a bank account or PayPal
such that user can reset password from
the email
account and we also believe the
combination of the email account
recovery with the pasy wallet is makes a
super easy wallet ux uh because pasy
allow users to sign transactions through
the F ID and so or and even and when
user lose a device or we you user can
use email account recovery to recover
your recover users account on the
an so from now we explain the details so
how email account details of how email
account Rec works with showing the UI of
the email account Rec feature in the C
wallet we are building now so in the
first step the user configures Rec
setting or such as Guardian guardian
information so in the cave Ur the user
just needed to specify the guardian
email address like this
one so in the Second Step the guardian
will accept this
request so the guardian will receive an
email like this one from the relayer and
if the guardian can approve this request
the guardian just need to reply to this
email and the guardian will finally
receive an confirmation email like this
one and in this process our Guardian
actually generates DK proof of the
guardian's email and send this email
proof on chain to register Guardians
address and once once the user loses
access to the private key we actually
start the recovery
process so in this process Guardian the
word user puts the email guardian's
email address again and the guardian
will receive an email from the rayer in
the same way and the guardian if the
guardian approves this recovery request
the guardian will reply to this email
and Rees the confirmation email and in
this process the the r similarly
generates D proof of the Guardians
email and in the first in the final
step in the final step or Guardian the
wallet user can complete this recovery
request once more than slh hold number
of the Guardians approves recovery
request however there's a time delay
before before completing this recovery
request and this improves the security
when the audience email account is
hacked because wallet user can cancel
Pro cancel recovery request or if the
email account is hacked so in this way
we can keep the security and
accessibility of the users account as
long is the the user can access to the
private key or emails the guardian's
email account is
honest sweet so we have those account
recovery deployment audited and live on
mainnet for both clave which we'll roll
out in the clave wallet over the next
week for pasy wallet and also in our
recovery UI for safes um but this can be
larger than just a couple of wallets the
idea is that any smart wallet can
integrate this into their wallet and so
we've created a bunch of Dev tooling to
make it really easy for anybody to use
these kinds of
proofs concretely for instance a
recovery module is a 7579 compatible
smart account standard this means any
wallet is really easy to integrate with
a uh this specific account recovery and
even if you're not 7579 compatible it's
still quite easy to add account recovery
to your
wallet we have a set of very simple apis
that users can call again you don't need
to read all the details here but to
trigger each of these requests you can
simply hit each of those apis and your
own wallet or your own application can
trigger any of these kinds of uh
transactions
directly and finally installing it to
any kind of wallet in a front end is
also very easy again you don't have to
read the exact code but it's the idea
that installation is just five lines in
for instance a permissionless JS uh
smart wallet creation interface you can
read more about it on our docs on the
right side we'll have more links the end
if you want to Define your own kinds of
proofs not account recovery but say any
of the other application ideas you can
Define your own kind of pattern in
solidity directly here we show that you
can say something like recover account
eth address to new owner eth address
once you've defined this kind of
solidity code you can then hit any API
that any relayer has deployed the API
request looks kind of like this again
the main thing here is it's just about
handle sending the emails for you
getting the response making the ZK proof
and sending it on
chain you can see again these docs for
how exactly to build with the dev
tooling over here and we'll have a
workshop tomorrow where we go over more
of it in
detail um so for instance uh you can
imagine this abstraction can be used to
build account recovery email signers
login and the email wallet primitively
talked about in the beginning but we're
excited for folks to explore with these
kind of email Tri trigger transactions
to build more different kinds of
things so just to quickly recap we went
over the very basics of how ZK email
works and simple kinds of proofs you can
make how to make new kinds of proofs
very easily and access them from a
shared registry then switching from
making proofs of received emails to
making proofs of sent emails we went
over how you can do email trigger
transac actions and then account
recovery and finally how we've made this
really easy for new folks to either
directly use or integrate directly into
their wallets or projects
Etc we're super excited to jam more with
folks if people want we'll have some
boots um specified on the left you can
catch us there after this talk and also
over the next two days and if you want
to learn more about how to specifically
use these tools in your applications
we'll have uh a concrete Workshop
tomorrow at 1:30 p.m.
where we go over
how to actually integrate each to these
things um directly with help from the
team who actually built
it sweet so if you want to read see or
hear more we recommend following our
Twitter on the left side looking at our
homepage in the middle on zk.
and if you
want to view an original copy of these
slides you can scan the QR code on the
rightmost side sweet thank you for
coming and we'll take some
questions sweet thank you shant that was
a very interesting talk by the way right
yeah I like to see zkps being used for
something else rather than Z ZK OLS
right and it mixes both web 2 and web 3
so we have some time for Q&amp;A so how
about we take um the first one so it
says what zkp framework you are using
and why yeah it's a good question so
we've used and benchmarked all of the
Frameworks that um we kind of listed in
the beginning we have versions in circom
and now Noir and also now in zkm like
sp1 and RIS zero um we generally so
because most of these things are
happening on for instance main Nets we
want to make sure that there's both high
security and extremely high speed So
currently we use circom on the service
side and also on the client side just
because it's kind of the main one that's
very main net ready right now and also
can prove extremely fast on the server
side and within like 5 to 10 seconds
usually for most of the proofs we're
talking about
um but we intend to work closer with
Noir to get those client side proofs
working in Noir and Clos with the zvm to
get much more extensible proofs on the
server side yeah that makes sense
actually by the way you can upvote the
question so that we can see those that
you up uploaded first here on the screen
so maybe or if we take the second one
would trusted setup ceremonies ever be
required if so when yeah so this sort of
depends on the exact proof system you're
using if you're using the circon proof
system we have in production right now
then yes you'll need to do a trusted
setup um however if you use the Noir
system on the client side we're moving
to or the zkm systems on the server side
that we also have um then you won't need
to do a trusted setup for that specific
circuit
um yeah so we have two
votes
uh yeah maybe this question so is there
any prerequirement for an email to be ZK
approved um not really any email you've
sent a receed can usually be ZK proved
because all emails require this DM
signature to go through spam filtration
um there are some restrictions like for
instance Hotmail is not exactly pursuant
to the standards so some things that you
can't access a two email within a
Hotmail email but in general almost
every email that you send or receive can
be approved okay
got I think we've still got time for
more questions
yeah um yeah maybe this one when we can
see the
I think we can see them also here I
guess the top one is there a key
rotation problem uh yeah so the public
keys that the Dum uh verification
actually happens with are rotated every
maybe six months to two years for some
folks never rotates um the nice thing
about this is that the smart contract
that holds those keys is publicly
auditable anybody can go in and say yep
those are the keys that my DNS is
fetching as well um but yes to relay
those keys on chain there has to be some
sort of uh a system of Oracles in our
case we use like a a specific multisig
in which all of the like a bunch of
autonomous computers are calculating
those and putting it on chain and you
can also doubly verify that with for
instance an ABS TLS notary or TLS
proxies to ensure that all those values
are correct the important thing here is
that you can use a single public value
that DNS value to verify private data
and that public value is auditable so
the idea is that if there was ever some
fault somebody pushed malicious keys
there are enough time locks built into
the system uh and also ways to to stop
it or ways to to uh override those key
Registries for each user that we think
this is not actually that big of a
problem in practice that makes sense
thank you for the detailed question uh
answer um yeah so maybe why if we take
this one since DK IM private key is for
the whole domain rather than the than
percenter presumably the security model
realize and we don't see the question
anymore yeah um so so I mean I'm just
repeating the question for the live
stream so that people uh yeah so the
origin MTA prev incenter proofing within
the domain yeah so the idea here is that
yes because you're only verifying the
signature from the domain you are
trusting that that specific domain is in
fact like disambiguating senders
correctly the nice thing here is that
most email providers that most people
use like Gmail Outlook iCloud Etc
definitely have this in by default
because it would be very bad if they
didn't but we have noticed that some
folks don't so for instance we just
disable um most doedu domains uh from
most of these models because often they
don't have very good uh parsing of this
kind of which sender exactly in the
domain sent that email um but in most
cases for instance that you received an
email from Twitter or Devcon or whatever
uh usually you can constrain exactly the
the email address I sent it and that's
usually good enough and they're usually
using something like Google workspace so
it's usually passible and in the context
of the email trigger transactions uh
while this depends on the earth private
key of the specific email or de de or
server like Gmail uh we believe this
achieves better threade off between the
ux and the
security thank you so I think we on time
uh please thank again aush and Sora and
please applaud him applaud them for for
their
talk and by the way for those who joined
us just recently so there is a QR code
at every beginning of the session if you
scan it it takes you to the Devon
passport and then there uh you will find
when you scroll down the Q&amp;A session you
just need your zoo pass and then you can
ask the questions up vote them and we
see them here so in five minutes we're
going to go to the next talk
back
hello
again so we have our next next speaker
uh Philip lafier so he works for polygon
in the miden team and he works on the
miden virtual machine so today he's
going to talk about lookup arguments so
you have may maybe you may have heard of
lookup arguments you're going to talk
about log up which is one of these
lookup argument and the lessons about
integrating lookup with GK in the mid VM
please welcome Philip
lafier St
hello um so I'm Phillip uh work on the
mining VM and um yeah today we're going
to talk about our lessons from
integrating log up gkr in the mind VM uh
it's going to be fairly high level so I
wrote a little hackmd book at bit.
leog
up- gkr where a lot of the details that
we don't cover here are in that
book so for context gkr is a uh
technique proposed by Shahar and olrick
around this time last year in their
paper improving logarithm derivative
lookups using
JKR so in this talk we're going to first
look at what log up is first of all and
then uh how log up is typically proved
with Starks and then we'll look at how
you do it with gkr which is the main the
main purpose of the talk then our
takeaway is from doing so
so really quickly log up is a protocol
to prove the equality of two multisets
uh multiset is a set where repetition is
allowed so they're super super useful in
Virtual machines uh they allow you to
have practically unlimited stack death
um do large number of range checks so
making sure that a given value in your
Trace is within some bounds
and uh they allow communication between
different parts of the trace so for
example in your main processor you could
have an exor and prove that xor
somewhere else in your trace the multi
set check is what you would use to
connect the two parts of the
trace so for example this is a uh
depiction of the uh M VM Trace so a 2d
grid of numbers effectively and in this
context a multi set check would check
that the multi set represented by the
green squares is equal to the multi set
represented by the blue ones so they're
they're basically multi sets on values
in your
Trace multi set
checks um so we'll jump straight into
the equation unfortunately we don't have
time to talk about why that makes sense
uh it's in the book but we'll take some
time and and analyze it together so uh
log up is there's four sets of variables
of interest um
the a AIG J and B J are the elements in
your multi set A and B correspond
respectively and then uh the m a and the
MB are the corresponding multiplicities
of those elements so for example if you
want an element to appear five times in
your multiset but it's only once in your
Trace you could set that M to be five
and it's going to be the exact same
effect so a a multi Set uh element is
the the expression is really its
multiplicity over Alpha a random value
minus AIG the the element
AIG so we have these two uh these two
terms per or actually K of them per row
where the I for the row goes from one to
n minus one the big takeaway from this
is log up is one big sum of fractions
that's the one main thing to get from
this slide and we're going to have to
prove
this so how do we do it with
Starks um so that's our equation at the
bottom and we'll just use an example so
we have a main trace of two columns A
and B and each column contains our one
of the two multi sets so column A
contains multi set a and column B
contains multi set B and we can visually
inspect that the two multi sets are
equal they're just a permutation of one
to the
next so the algorithm to actually do
that to implement the log up is to add
an extra column that we'll call P and we
say it's a running sum column uh so how
is it built it starts at zero and then
following our equation if we look at the
first element it's off by one compared
to the trace but we all the
multiplicities are one and so we have 1
over Alpha minus A1 which is the element
in the multi set a minus 1 over Alpha -
A2 the element in B and that again is
just from our
equation uh then for the next row we
initialize it with the the contents of
the previous row and that means we're
basically running an
accumulator and uh and then we add the
new elements so one minus Alpha minus A2
is added from the multi set a and we
remove one one over alus A3 from from B
uh same thing over again we we
initialize with the previous contents
add in the new elements and since this
is the last row uh it's going to all the
terms cancel out and it's equal to zero
so the boundary constraints on on this
colum are that it must start at zero and
end at zero if your multi if your
Columns of your multi sets are actually
equal but we also have to check that
each row is is correctly and that's what
we do in a transition constraint so
we're going to zoom in on that uh so we
have P here
um and uh
the the transition constraint is
basically what we just did in the
previous slide so Pi i+ one so the next
row is equal to pi plus the new
terms so when a is equal to one uh yeah
only two terms this is not quite right
because um the constraints must be pols
and fractions are not you can't have a
fraction in your polinomial so what we
need to do is simply multiply out the
Pol the the
denominators and so when K is equal to
one with only two terms uh per row uh we
get this expression which is a degree 3
polinomial because we're multiplying
three variables
together uh but that was when K was
equal to one uh when K is equal to two
uh we're going to have four terms in
that row so we're going to be
multiplying five elements here so degree
five so as K increases so the more terms
you have in your multi set per Row the
larger the degree the trick is in Starks
you typically have a bound on your uh on
your transition constraints on the
degree of your transition constraints
and so how we deal with this is we
simply make a new column if if only we
can only have let's say two elements
here we'll create a new column again a
running sum with whatever elements are
left over that we were not able to do
with the previous column and so on and
so forth it could go up to
hundreds so again the takeaway of when
we prove log up with Starks is that we
need a collection of running some
columns main
takeaway let's see how we do it with the
gkr uh gkr uh for context is a protocol
that uh proves the correct cor
evaluation of a layered
circuit uh so here we have a layered
circuit and yeah so effectively the
prover evaluates the circuit and then
uses gkr to convince the verifier that
this was done
correctly uh with log up we have a
specific circuit that encodes the log up
relationship so we're going to spend
some time thinking about how that
circuit looks like how it's designed
really uh if you recall log up is a sum
fractions and so uh over your entire
Trace so this is depicted by the the the
sum of fraction at the bottom here and
to get the the next layer we're going to
merge uh pairs of uh of these terms by
common denominator just like what you
did in high school so on and so forth
until we get just one uh one fraction
and really we're going to stop at two
but for for intuition we'll say that we
we get just one uh one
fraction um so that's not really a
circuit but it's a simple translation to
get a
circuit uh basically every node in your
circuit is going to have two numbers
corresponding to the numerator and the
denominator and then to merge two nodes
together we we apply the the the which
we Define as the sum over those pairs is
really the sum of fractions so the
denominator here if we look get uh a d
plus CB that's the denominator that we
got from those two fractions and then BD
is the sorry that was the numerator and
BD is the
denominator so then what do we do with
uh G on this circuit there's actually
slight modification through the gkr
protocol but we're we're not going to
have time to go through this again
that's all in the book uh so at a high
level theover evaluates the
circuit uh and then sends the output
layer to the verier so only two
fractions that represent the exact same
uh exact same sum that was in the input
layer but really at on with two
fractions so the verifier can easily
check uh that this is equal to zero and
we'll also check the denominators are
nonzero to make sure that they're proper
fractions and then Pro and verifier are
going to run gkr to convince the
verifier that uh the
the circuit was properly evaluated and
that translates to that the output layer
really comes from the input layer it's
basically the same sum but represented
in a different set of
fractions we're not done yet because
we've we know that the output layer is
equivalent to the input layer we don't
know yet that the input layer was
properly populated from elements of your
Trace uh to do that we're going to have
to do this in Starks and we're going to
have to add two columns to our
Trace we will not go into how we do that
unfortunately because it's like very
cool and like quite quite clever
honestly uh but the the the long story
short is that we need we really only
need two columns in uh in our in our
Trace so if we take a step
back um when we were proving log up with
uh with Starks
we ended up needing a collection of
running some
columns again that can go up to 100 or
more with gkr we needed only two columns
but with the overhead of gkr on top of
that so then the big question that we
asked before starting is which is best
and like anything in VMS there's no
simple answer uh it depends on a variety
of parameters uh so we just went on and
and did it and so uh there are takeaways
from uh from doing
this many many many different parameters
influence which technique is best in
what circumstance depending on what you
care about um we're going to focus on
three hash function speed the degree of
start constraints and the size of the
bus so hash function speed uh when in
Starks you have to choose your hash
function uh and by by slow or fast we
really mean on for the prover on on the
PR's machine how fast is it to to Hash
two numbers or whatever or how however
many so the reason why the hash function
speed matters in choosing one or the
other is that if you recall from log up
we were adding a bunch of columns and
each columns
adds hashing work to the prover and so
if that hashing work is expensive
because you have a slow hash function
it's going to it's going to cost a lot
to add these
columns uh so the green check marks
means favorable to gkr to to log up
gkr and the reason is uh log up in
Starks needed a bunch of columns gkr we
only need needed two and so if we go
from hundreds to two that's a lot less
work for the prover of course there's
overhead from gkr but from if we hone in
on that parameter it's very
good degree of star constraints uh same
idea
so uh if you recall from earlier the
degree bound on your star constraints is
what made us is what made us create new
columns because we were not able to pack
more uh we were not able to pack a bunch
of uh fractions in a single column so
the lower to degree the more columns
you'll need and then the same intuition
comes back uh the lower the degree the
more columns the more columns the more
the more work for the approver uh and so
removing all these columns when
switching to gkr is favorable to
gkr again if your degrees higher you're
removing fewer columns and so maybe the
gain is not as
good the last parameter is the size of
the bus uh by size of the bus we really
mean how many fractions per row are you
adding that K from the previous uh
uh K from the previous uh
equation
so here if you have a very large bus so
meaning you're adding a bunch of
fractions per row you're going to need a
lot more columns same intuition so a
large size uh a large bus is going to
mean a lot of columns when you're
proving in its stars and a lot let a lot
of Pro work that you're removing when
you're switching to
gkr so this is our mental model rough
model for uh when when to use log up gkr
and when not to use it so in the case of
MVM we the rollup uses a slow hash
function uh so that was that was good
that was quite favorable but the MVM
uses quite High a high degree of start
constraints we use nine uh three is uh
is quite popular five is also used so
we're we're pretty up up there so not
very good for log up J
also our bus was kind of small we only
had a few extra columns for log up so
basically we by optimizing gkr and gkr
is based on some check and there were a
lot of optimizations there get it down
to get log of gkr down to be equivalent
in time to uh Starks only but as soon as
we went back to a fast has function we
use Blake 3 uh log up gkr was still
slower and uh it seemed like
maybe it's it would maybe even never
reach uh like parody because our bus is
small and our degree is High
um we were not the only ones to
implement this starkware also did that
and um Andrew Milson was uh very nice
and shared with us uh the numbers that
they got so they have uh the they in
their experiments they used Blake 2 as a
hash function so quite fast but they
have degree 3 constraints so very nice
for log of gkr and a very large bus like
hundreds of columns and they were able
to get a 15% Improvement uh and they
will say that they're still not done
optimizing so they think they can get
that even higher but it just goes to
show that even though they have uh they
use a hash hash function that's fast
they were able to make log of gkr worth
it again this is all pro time one thing
that this slide doesn't talk about is uh
proof size and verifier time
maybe the the the big the big drawback
uh for log up gkr I'd say is proof size
so these extra columns that we're adding
and all the nodes that the the the
circuit nodes for log up gkr are um are
all the in the extension field so for
example at uh in the mine VM we use uh
goldilock so roughly 64-bit field
extension field is uh where we do any
any kind of Randomness is done in the
extension field and that's roughly 128
bits so every number is is larger and
proofs kind of at very large uh for
traces that are that we can expect in in
the rollup we were getting maybe 200
kilobyte size uh proofs just for gkr and
typically we're able to get it maybe at
kilobytes uh so it really blew up our
our proof sizes up and actually trying
to to decrease them so that uh so
ultimately
our our current um takeaway is that
we're not going to use it for the first
version of of the M VM but we're also
looking into uh making some pretty
drastic changes in the future and uh
yeah this is the Mind map we're going to
use uh when we when we do that and
whether or not we want to uh use log of
gkr But ultimately it was a a great
experience and uh like a very clever
idea by Shahar and
O so again like most of the details uh
we didn't talk about if you go to that
link uh most of them are there I I try
and make it approachable uh feel free to
ask questions on the hackmd directly uh
send me a DM on Twitter or just message
me uh whichever I'm happy to to have
more conversations about this and yeah
uh hopefully you're you learned
something thank
you thank you phip it was an insightful
talk so again I just remind you that
there is a q code if you want to ask
questions um but we have actually a few
so maybe why if we start with the first
one do we uh in practice mix J and stock
for different use cases other than Loca
IAS yeah that's a really good question
uh and something that we start to think
about more uh currently log up is the
only one that I'm aware of that is being
used or even tried um but uh it is on
our we are going to think about more
ways uh that we can do this because now
we we have a clear use case and or
rather a clear example of how it can
work and uh yeah but so far I I don't
think so so the reason is like just
implementation wise you need to try it
to see how it works so implementation
wise absolutely even just understanding
like the glue from from gkr to Starks
was non-trivial to understand at least
for me because you're going from a
multi-linear world to a uh univariant
world uh and there's some but I'm pretty
sure that some of the insights there can
be reused for other purposes that makes
sense um yeah what if we take the second
question is log up more gkr friendly
than other lookup
arguments yeah another good question uh
I do not know any other uses of there
might be but I do not know uh other
lookup Arguments for uh that use gkr so
uh I I don't
know and you were using like log UPS
before introducing JKR so we it was
stock friendly I guess right so we use
actually we use log up only when we need
multiplicities because uh as we saw it
makes the degree log up makes the degree
go uh go up pretty quickly because of
these denominators you have to multiply
out I mean a constraint degree sorry uh
for most of our lookup arguments in
Starks we use good old multi set checks
we I call them like vanilla multi set
checks they're based on they're not sums
of fractions they're really uh it's not
a running sum column it's a running
product and it's slightly different your
degree is slightly better so unless you
need to uncode multiplicities explicitly
we don't use log up but I don't know how
to do that other one with J okay cool
cool we have more questions so what has
function function you are using right so
the M VM does does not you can use
whichever one you want with the m VM uh
we use the MVM in the M rollup and for
that we use uh hash function RPO which
is a ZK friendly hash function and we
actually I think we're going to switch
soon to RPX so is it also it's like an
improvement on as I she's also stock
friendly also yeah
okay um then next question is how fast
slow is gkr verifier in
stocks uh yeah good question
um I it I think it's comparable to uh
from what I recall I was focusing Less
on GK fa fire so I'd have to go back uh
it was not drastically faster or slower
it was rough you were getting roughly
the same maybe a bit slower okay and
does it change like in terms of the size
of the lookup you're proven or yes but
in the numbers that we that we care
about so maybe traces of 2 to the 16 or
we typically around that uh you didn't
see many differences between uh it was
relatively constant okay cool
cool uh if we can just call down to see
more
questions yeah M and love yeah good one
it's a good
one and maybe last question any plans
for Hardware acceleration for the mid VM
yeah uh so we have uh GPU support that
is maybe even in our main branch yet or
at least soon to be uh but we have
active GPU work being done uh more
long-term we're also looking at uh using
ZK specific chips but that are not on
the market yet but it's already ax okay
yeah yeah right okay cool cool well or
if we give a round of applause of for
our speaker Philip thank you very much
thank
you
yeah about uh folding schemes so just
some uh house housekeeping reminders so
there's toilet on your left and you can
take pictures of um whenever you want
but just turn off the Flash and if you
see a sticker no photo so please just
don't take pictures of the speaker so uh
our next speakers are AR now and Pierre
and they're going to talk about uh
folding schemes
so uh ready for the next
session I think we've got some time
right
hello again and welcome for those who
just joined us so I'm Yousef your MC and
so we have the applied cryptography
session going on and this is the third
talk so uh the third talk is about the
folding scheme library and the speakers
are AR now from ZX Park and Pierre from
PSC please make some
noise hi um yes so I'm Pier uh working
at PC and this is a presentation done
jointly with ar now who is working at
zerx Park so we are going to walk you
through uh the library that we have been
working on with uh winda as well and
Carlos over the past
year so let me first introduce you a bit
to the concept of IVC which means
incrementally verifiable
computation so um the main entry point
to understanding what is incrementally
verifiable computation
is that um those are kind of
computations that are repetitive so um
for instance you see this little math
formula states that you can obtain the
result SN when you apply a function n
times on some initial state zero so to
give you some more concrete example you
can think of it as a machine learning
model which always does the same
inferences uh on uh some different data
points or maybe some virtual machine
with a fixed set of op codes which which
does some repetitive computations or a
rollup which always batch verifies
signatures again and again and again and
even the blockchain consensus U where
the same consensus algorithm is apply um
um again and
again so what are the benefits of IVC
schemes that use uh folding so uh this
is where the folding schemes thing comes
in uh so folding schemes are used to
basically realize incrementally
verifiable computation and you can see
on this diagram that the idea is that at
every step of the function you will get
a public input so the Z little Z and
sorry and um a witness so w the little W
thing and at every time the computation
is uh being uh done you will have a new
public States Z1 and maybe if you want
to redo another step of the computation
you will have a new witness W1 so what
you can see and that's interesting is
that the F function is applied
independently every time uh you do not
have like a big circuit where you do
some kind of loop and you say from uh
IAL 0 to IAL n apply the F function no
that's not how it works works here the F
function is really applied independently
every time so you get a prover that uh
whose memory is basically dependent on
the size of the function that you are
applying not on the number of time that
you are applying that the function so
that makes things very
interesting so uh you can use folding
schemes for recursion this is some form
of recursion that we have seen because
um we are just inputting the prev R
State into the next temp and uh folding
schemes um a folding scheme is a coin
that has been is a term that has been
coin in the Nova paper so it's something
different from what you can see in some
um in some stock protocols it's here
what we mean by folding is really just
basically taking random linear
combinations of uh Witnesses um and the
main intuition is that you can have a
folding scheme uh when um you are uh
taking this kind of combination between
Witnesses because you can show that if
you know two satisfying
Witnesses then if you take the linear
combination of those then you can obtain
another satisfying uh
witness um also um the main workflow
when you are using um folding schemes to
do IVC is that you will do your uh IVC
computation maybe for end steps you will
get an IVC proof and this proof is not
suent so you will want to um um you will
want to compress it basically using
something that is called decider and
it's basically a znar proof so we just
snarfy the IVC proof and obtain a more
sucin proof that you can then verify
wherever you want such as
onchain all right so let's just take a
step back and try to think a bit about
what folding schemes how folding schemes
look like so there is now what I call
the folding schemes Zoo so there are a
lot of different kind of folding schemes
because you have a lot of different
kinds of aromatizations you have a lot
of different kinds of use cases some use
case use lookups other don't some have a
uniform computation some have
non-uniform computations so you we end
up with really a bunch of different
folding schemes some are used for plish
circuits other use some specific kind of
aromatizations um uh thing that are
adapted to folding some do many to one
folding so not two to one but many to
one folding meaning uh instead of
folding two witnesses together you can
fold n of them together so it's very
efficient form of folding you have also
ltis bit folding more recently so that's
interesting for the postquantum
uh security properties of those kind of
things and so we really end up with some
kind of zoo um with many different
folding
schemes and even in terms of research
it's a very active area of research so
for instance just in April 2023 there
was like four different kind of folding
schemes proposal and way to do VMS with
folding scheme so it's a really active
um area of research um recently there
was some uh zero knowledge layer that
was proposed for IVC proofs so you can
generate your IVC proof on a client and
then make it ZK it's very efficient and
then for instance send that to a server
to have the server compress the proof
and send the proof on chain so those
have some really interesting um zero
knowledge properties um you we also have
latis fold which is postquantum ready
and is a pretty efficient form of um of
folding and um yeah so there is really a
bunch of stuff to to to talk about today
about what's going on in in the this
area of
research but let's talk a bit also about
applications because I I think that some
of you are interested to know what's
what's happening there um so for
instance um we did one experiment where
we were um uh building a Bitcoin light
client so the idea was just to prove uh
that the current blockage that we have
is um has been obtained after end blocks
and so we for instance run and uh a Nova
which is a folding scheme uh on the
proof of work um uh Bitcoin um algorithm
for 100k blocks and in total that costs
us uh $30 to verify on optimism uh for
running such a huge absolutely huge
computation that we wouldn't do using a
uh uh traditional ways of um of zik snar
proving libraries that we have
today we also have Z kvms today that use
folding so there is the Nexus team I
think that is you that is led by Yan gr
and Daniel Marin uh they use I think
hypernova for that there is also the
jolt team um uh they I they published an
update actually today uh stating that
they were interesting in interested in
folding and I think they are interested
for it regarding their memory checking
algorithm for their for their zvm there
is also ZK machine learning uh someone
Beed into Nova um a billion parameter I
think or yes something a billion
parameter at least there was it was a
um that they bed into Nova and for which
they generated the proof and I think it
amounted to something like a billion
parameters model uh so you have also ZK
machine learning yes so there is really
a bunch of projects that have been um
building on folding schemes lately so
yeah for that we have built Sono and
this is what Arno is going to talk
about hi so yeah so on you thanks uh on
you are interested into like uh being
able to use folding schemes for your
like uh recursive circuits um so we have
this uh Library it's a like a very
experimental um thing um intended for
research but we are starting to like now
polish things uh so the idea was to have
this modular Library where we are able
to add and Test new folding schemes uh
compare schemes like aples to aples and
also that allow researchers to easily
add their own schemes as happened with
the MOBA paper by nether uh they publish
the paper where they use sonov to test
their their like new design uh which
they implemented in on top of sonov and
now this is this was a request in sonov
so now this is mered so now like part of
it is in in in the library Al but also
the idea is to make it easy for for deps
to use folding like the idea is that uh
they should have a minimal code to to be
able to then fold the circuits this idea
of plaque and fault and but also allow
since we are building this on top of the
artworks set of Library um the IDE is
that that um it's easy to switch thanks
to artworks between different curves but
then uh in sonov and also switching
between different uh folding schemes uh
and also we have some experimental like
Z ciruit language kind of like um
interfaces where you can use like uh
other uh than artworks um um uh
languages to to define the circuit that
you want to fold and also like the third
kind of like pillar of son was to be
able to verify on chain um the the the
folding proof because this was something
that uh we we were not able to find in
any any of the other folding
implementations because of the theum
characteristics so so yeah uh as I
remarked this is like a very
experimental and research library and
for the moment it's
unoptimized
so yeah so that's the developer
experience of sonov this is like what
you already saw um this is like the the
the idea of of the folding schemes and
this is like how this maps to son uh
they it's very simple like the the dep
just needs to define the circuit that
wants to be fold uh select which folding
scheme to be used for example Nova plus
cycle fold but then you can swap uh and
with just changing one line of code into
using hypernova or Proto Galaxy then
also setting the final deider uh that
generates this um compressed snar proof
um and and then uh in the case that you
are using the onchain uh decider uh you
can then also generate the solidity uh
code like the template that you can then
deploy and you can use this to verify
the the proofs on
chain status of the library um so so far
what we have like uh fully implemented
is like Nova hyper nova and Proto Galaxy
folding schemes the three of them using
cycle fold uh techniques uh so um and
then also for for Nova we have like the
full solidity verifier there for
hypernova Proto Galaxy like we have the
the code in r that generates the the
proofs and so on but uh it's just a
matter of like putting time to doing the
Sol also then also we we started to
introduce this MOA an NOA these are just
like variant to the Nova scheme uh so
it's like with some tweaking and some
abstraction we can reuse most of the
already existing Nova code that we have
there um so it should be easy to fit
them in also and then for the front end
like how you can Define the circuit that
you want to fold um this is done through
some interface by default is artworks
but uh as experimental thing which is a
bit slower uh you can also use uh circum
Noah and no name but yeah so just to
give you a bit of like a sense Nova is
using this random linear combination for
the folding part which this is then need
this needs to be um checked inside a
circuit so then uh hypernova instead of
doing this randomly in combination uses
it linearizes the the instances and then
runs the S check uh to to prove the the
relation uh and then Proto Galaxy is
instead of random linear combination is
doing linear combinations with the
lrange bases uh in one of the settings
and in the other setting is also using
the S check but just to give you a bit
of sense of that different schemes use
different techniques so one of the goals
also here is like to be able to see in
in different use cases which one fits
better and and so on so having this
modularity then okay so this is how it
looks like the F circuit interface this
is like the the circuit that you want to
actually fold uh you just need to
implement this like the first three um
methods are just like very simple things
and then step native and generative step
constraints those are like the the the
logic that you want to do at each fault
step native is what you do in Ras like
outside the circuit and generate step
constraints is where you Define the
logic of the Circ that you want to fold
so this is like the constraint that you
are folding actually just by defining
this interface like if you implement it
then you can plug this into sonov and
then uh sonov takes care of like
wrapping this inside the augmented
function circuit um and and doing the
IBC folding and and and the rest of of
checks and so on so the idea is to have
this very simple interface that uh also
this is used so when you want to include
a new uh Zig language into being able to
use sonov just by implementing this for
for the language that you want to use uh
you you you already have it then this is
like the the the usual code that you
need uh using sonov to fold the circuit
so the main idea is that here you define
which folding schemes you want to use
and also like as you see this PS and G1
p and G2 so the G1 G2 those are like the
curves that you use we need a cycle of
Curves but you can pick uh most of the
cures that are available in artworks and
then the pon G1 p G2 this is like the
commitment scheme that we use in the
first curve and the secondary curve of
the curve cycle and and then the rest is
like more or less will be the same like
here we are doing 100 steps of this uh
proof step which is like the the actual
folding of the IBC and at the end you
can just verify the last one and so here
you are proving like that after 100
repetitions of this computation you
obtain this final step coming from the
first initial State um so so yeah so
that that's the main idea as you can see
I mean it's quite uh like simplified
and and easy to I mean easy to reason
isy easy to to have this working and so
on and then when you want to change
which folding scheme you are using it's
as simple as just taking this line and
then you can say Okay I want to use
still Nova but now I want to have uh in
the in the first curve I will use kg
commitments so that then I can use the
final uh decider uh that don't chain the
either that I can then uh send proofs to
ethereum and be verified or you can say
oh you know what I'm going to change to
hypernova so you don't need to throw
away your code you can just replace this
line and now you are using hypernova or
I'm I'm going to use Proto Galaxy so you
can then um doing this like easy line
one line change uh you should be able to
to have this um
then when it comes to to the decider so
we we we've been folding we have this
last IBC state with the last IBC proof
so now what we can do is is like we can
compress it with the deider so we have
the offchain decider and the onchain
decider so it's also like a similar
interface and then here is how do you
use it
um and the the one of the key things was
this unchain verification um so was one
of the goals because and and we've not
seen any other folding schemes libraries
having this on chain uh verification so
the idea is that in the original Nova
this decider this compressing of the IBC
proof is done through two Spartan proofs
one on each of the curves um in our case
in we are interested in to verifying
inside the evm uh the evm has some kind
of restrictions uh like we are limited
to a single cure the 254 and also
constrained by the gas costs so we had
to do a bit of gymnastics to fit this so
this is like a very high level idea so
we are using cycle fold we end up having
um some instances and what we do is we
combine some uh growth 16 circuit that
also contains some non-native arithmetic
stuff uh combined with the kg
commitments proof so at the end in
ethereum we just verify one growth 16
and two kg commitments for the case of
Nova for example um so this is very
suene and cheap in terms of gas costs um
and also yes so you can generate the
solidity code also from from the library
um so uh to to wrap up some preliminary
numbers uh just as a remark um until now
we've been focusing on implementing the
various folding schemes not on
optimizing so that's why now so now we
have the Nova hypernova Proto Galaxy all
of them using cycle fold um we've not
been focusing on optimization and
efficiency um but looks like the the
current numbers that we have when we run
some preliminary benchmarks they look
promising um and and the next steps will
be to start profiling optimizing and
adding benchmarks and like stopping
adding new papers that are appearing and
focus for few months to like optimizing
things and making them a bit more fast
and parallelizing and and so on and then
getting to a f release because until now
is just like commit after commit and the
interface might break so some
unoptimized preliminary numbers so each
folding step this is the recursive
iteration uh for a minimal circuit it
takes like 300 milliseconds um this is
there is this overhead of the the fixed
cost of the five 50,000 uh uh uh sorry
so it is this like about uh 300
milliseconds on a like uh today's laptop
then when you want to um prove off chain
the decider and qu takes less than one
minute it should be much less uh but
it's just that we are using pting based
snarks on both sides of the C cycle the
idea is that this should be using
Spartan at some point and the modified
version of Spartan that uses the relaxer
efficient um and then for the offchain
decider which is one of the main
contributions from sonov um we have this
big circuit at the end that does this
gymnastics and non-native arithmetic
stuff to fit into the ethereum uh curve
uh that it takes less than three minutes
in in a like in a in my ThinkPad uh and
the gas costs are 800k of gas mostly
from growth 16 proofs and kggg proof um
well one growth 16 and two k proof in
case of Nova uh the idea is that this
should be reduced to less than 500 with
some tricks of the hashing and of the
bound Le inputs and and of the um um
combinations of pings um yeah so just
just as a wrap up uh main takeaways that
you can get from from this t uh first of
all folding schemes are not a tool that
fits in all the use cases but when when
it fits into some use case that you have
a something that is like the same
structure of the circuit very repetitive
and and done uh a lot of times uh again
and again and again then folding
presents a big uh speed up compared to
full recursion of other approaches and
then uh well some of is experimental uh
the schemes that we have and we have the
onchain verification and preliminary
benchmarks look promising and the next
steps uh in the short term is to
optimize and and Benchmark well and um
do memory profiling and and so on and
that's
it cool
cool um yeah so I personally actually
use son and I can tell that it is quite
generic and also easy to use so if we
take some questions so the most upvoted
one is the first one so folding schemes
initially gained a lot of attention but
we haven't seen many advantages in
Practical implementation against stocks
can you compare them with stocks and
what are the advantages quite opiniated
question right yeah so who one of the
perspectives that we have on on folding
schemes in general is that is not this
tool that fits into all use cases like
the same Hammer that you can use on
everything uh it's very kind of specific
and like uh spe specifically in son we
have this IBC uh model so this you you
need to model your your use case to to
that so it will not fit all the use
cases but for the ones that it fits then
it's it's like it's sub substantially
faster than doing full recursion with
Starks uh but it's not as as like
flexible as as you would have with when
you are doing full recursion like uh
like for example taking a plony to
Circuit where inside you verify a
previous plony to proof this like full
recursion and so part of your circuit is
doing the full verification of the
previous St proof uh this is more
expensive this is a bit slower but it's
much more flexible and and easy to to
manage and from the engineering point of
view also with folding is more specific
so not for all the use cases but when
you have a use case that it fits well
it's it's like in 300 millisecs you you
can like do each one of the recursive
recursive steps makes sense maybe you
can also do folding with stocks which
takes us to the second question what's
the status of folding of for
stocks so our team didn't to re work on
that uh so U maybe you want to you have
something to so there there was um some
paper where they were showing how to do
folding of starks uh bonded to a certain
number of repetitions um and I think the
arc paper came last month or something
like this I think the one was like MOA
that does STS folding or something else
MOA is with is like a variant of Nova
okay there are being improvements and
and so but so far uh this library has
been focused focusing on IBC uh with
like Air1 CS or CCS surrounding things
not with with Starks the same for ltis
fault I see next question regarding to
ltis ltis also requires a different like
uh so you work over the uh rings of
polinomial and not on the like finite
fields that we use in in the traditional
snarks um so also it will require like
having first like some layer of of all
this like uh instead of the field
arithmetic the the ring stuff uh that
that it's not at least in in our
uh so so yeah and the folding Starks it
looks promising because Starks are
already fast uh if we can get to a state
where we can use the folding techniques
uh so the main idea is that with folding
uh without Starks we use these uh
homomorphic commitment schemes so that
you can uh combine commitments to some
vectors or polinomial and then uh this
result of the this linear combination of
them uh still holds some relations with
Starks since the commitments are not um
additively homomorphic um uh we are not
there yet but uh it looks like uh the
people in the Academia or in behind the
papers will bring some uh improvements
yeah I think Dan Bon is waiting for you
to implement that his
fault um so next question uh folding
papers work with different
arithmetization a1cs blish CCS now that
you did the implementation is it
efficient for anything other than a1s
another opinioned
question um is it efficient for anything
other than1
CS
uh well so there is basically L ltis
fold that is not using the R1 CS
optimization where you can use the idea
that are from the previous folding
papers uh for a different kind of
arithmetization
so uh there is also the question above
what's the status of folding for Stacks
you can reuse the ideas that were in
folding papers for another kind of AR I
guess the arithmetization
um so for a different kind of for an
arithmetization that is different from
R1 CS
um and uh so yeah I guess that that
answer the question if I understand I
think so yeah if we can just scroll down
to see the questions or maybe I can
check them on my phone
yeah so how does Sonic compare to Nexus
so um first of all lus is like a full uh
Company veed by VCS and their team is
amazing like it's a bunch of people from
Stanford and and so very good team so
now it's like a small team like we are
like three four people uh and and we've
been doing this but like uh uh in a more
experimental uh like not production uh
Focus but so far the benchmarks that we
run uh when you run the Benchmark in the
same machine for the now implementation
it's almost like the same like it's like
from 300 milliseconds in Nexus Nova to
the same hypernova in son is much slower
but because it's it's far from being
optimized and then uh we also have the
Proto Galaxy uh but in Nexus is not
there but so the thing is that both
libraries are based on artworks so like
the the the maximum speed uh should be
similar um and both are using cycle
fault which like the Microsoft Nova is
not using cycle fault it has a different
R so we have time for the Q&amp;A so why if
we thank again our speakers and give
them a round of applause thank you
you yeah so we have one more session
next so I'll be back like in a few
minutes
hello again and welcome to those who
just join us so we are running the
applied cryptography truck this morning
at stage three we had three wonderful
talks and we have more for you guys so
I'm excited to introduce the next
speaker because he's a colleague of mine
so uh he works on Gnar and L zkm so
please uh a round of applause for Evo
kuas thank
you hello good afternoon uh nice to be
here so today I'm going to talk about um
a bit about the optimization techniques
what we have done for making the proof
recursion uh in Linea and also in gar a
bit more efficient so so I work on Linea
and I mostly work on gark so gar is an
end to end Library written in Co for
writing uh circuits which can be which
can be proven using snark proof systems
so you can write circuits you can
compile it into uh constraint systems
for example R1 CS uh blanish um then you
can uh run the thrusted setup
particularly for the for the cross 16 uh
you can use knar for proving using a
different the rization engines so using
CPUs gpus finally you can use gar to
verify uh the proofs so we have the
verifiers written in example for the
native verifier for the mobile verifier
it's Al also possible to verify the
proofs recursively in in another snark
or we can also compile a solid verifier
so you can also verify snark proofs
chain on
etherum so let's uh set the stage uh
before we start so what we want to do
let's say we have some kind of statement
which can be a mathematical statement or
a computer program um and uh we have
some some inputs we have the secret
input and the public input so so the
secret input is something what only the
prover knows the public input is is
known to everyone so for like as an
example what can be a statement a
statement can be something very simple
for example I know the factorization of
uh RSA primes so I know two factors uh
which multiply together uh result in
some some uh some rme and so for example
I can prove that I know a solution to
this RSA factorization challenges and I
can I can uh obtain the the challenge
money but without uh without revealing
what are the particular inputs because
like if I would reveal it maybe like
someone will front run me and they would
um uh try to uh get money
themselves so what happens is that first
we take the the statement we possibly we
do like some kind of precomputation on
that so we we get some expanded
statement and then um the the the the pr
runs this program so for example the
gets some kind of uh execution
trace the pr uh proves using some
technique and we get uh we get the
proof and uh what we want to have
usually is that the proof is short what
what does uh what does it mean for the
proof to be short so the proof should be
short the sense of this expanded Trace
so the steps all the intermediate uh
results of the of the computations so
and if it is shorter uh then it means
that we have already won so we have some
like short proof of this computation and
we also want the verifier to be fast so
the verifier should run faster than
running the computation itself because
otherwise like what's the
point and uh like complexity wise maybe
we we wanted to proof and verifier work
like it is a let's say ASM totically f
faster maybe we want them to be let's
say logarithmic in the size of the
computation steps or maybe like a square
root or it will be very very nice if uh
it would be constant
size and optionally we we would like to
have zero knowledge sometimes but in a
lot of applications it's not necessary
so let's say some of uh some of the
proving schemes so there is the sum
check where essentially we if we
represent the statement as a multilinear
uh polinomial and the then the pro shows
that some let's say some property of
this multilinear polinomial holds and it
is it doesn't require like some very fun
mathematics it's like essentially we
just evaluate
pols uh the problem with the Su Che
based approach is that verifier needs to
do the the final EV so it means that
verifier needs to evaluate this Su Che
multilinear polinomial at some point
then we have gkr which is very similar
to S it's just layered it's
it's a bit more structured we have
Starks which are based on um on hash
functions so we can uh we can have some
kind of polinomial constraints between
like different steps and different
different
columns uh we have cross 16 which is one
of the first bearing based systems and
the nice thing about the cross 16 is
that the proof size is constant and also
the ver verifier workor is constant but
it requires a lot of pre computation it
requires per circuit uh trusted setup
and final blon blon is nicer in the
sense that it doesn't require par
circuit trusted setup so it can use the
universal trusted setup there are of
course a lot more but uh also like in
the big picture like these are like some
nice nice examples so the let's say the
the issue is that for the first three
schemes uh they are very fast and they
do not require like any particular kind
of assumptions they only do find field
arithmetic and hashing uh and no
assumptions at all so we just have to
choose the hash function but the proofs
are not that short so for the sum check
the proof size is logarithmic in the
number of uh let's say in the number of
steps uh for Starks I think it's uh it's
is square root so it is shorter but then
not but not very short so if the let's
say the if the statement input is is
huge in like hundred hundreds of
millions of uh of steps then the the the
proofs are still
big for the last two the issue is that
um the provs are slower because we use
the the fun mathematics called pairings
and kg commitments but the proofs are
very very short so the the proofs are
for example like constant number of uh
some group elements and the verifier
work is Al very short so like if we
measure it concretely on a na machine it
means that the the verifier work is for
example like milliseconds why we want
the verifier work to be efficient and
short is that when we go to L1 then uh
it concretely uh means that we pay for
less
gas so what should we do we have fast
provs we have fast verifiers we have
slow provs we have slow verifiers so we
can just combine like different
approaches let's
say we can uh combine the approaches
because like one of the statements what
we can prove is uh the verifier
implementation for the F program
so let's say if you have some very big
statement and we'll just use fast PR
first we get some proof which is which
is uh let's say not constant but still
smaller then we provide this as an input
to the slower prover but because the
input is already sufficiently small then
the slower appr is actually also
relatively fast so we can uh we can run
it nicely and in the end we get a very
small proof very very fast verifier and
we we can post this on on ethereum and
and we are done so we get both of the
best of the Both Worlds we have the fast
Brewer we have the fast verifier and we
we we we do not pay a lot of money we
don't pay a lot of money for verif
proofs we can use the like similar let's
say combination techniques uh CK
pipeline combination techniques to do uh
comput the proofs in parallel so let's
say we have uh in the context of rollup
we have a a lot of blocks so we can
prove actually the blocks in parallel
because even the fast Prov
uh they are slow so take they take
minutes so we can actually run let's say
up to like 400 uh proofs proof
generation in parallel and then we can
aggregate everything into into a single
aggregate proof and we post that we can
post that onum so this also gives us
some like some additional saving uh in
uh in posting the the proofs and in
finalizing the L2 on
ethereum so to summarize a bit uh what
different kind kinds of recur recursive
proving we have to do uh we have to do
the PN 254 long verification in pls2 377
it's for the pre- compiles and we verify
the fast uh fast proofs The Vortex
proofs in uh in PLS 12 77 PL then for
the proof aggregation we used the PLS
because ethereum only supports the BN
it back into into some other curve and
for that we need to use the the Final
Approach so what is the cost in uh or
what is the cost in verifying plun proof
so there are different steps so first we
need to need to do some hashing get the
the random
challenges uh we have some
exponentiations where the exponent can
be a variable or it can be an fixed
value we have scalar mul ications and
finally the the most complex part is is
Computing the pairing and pairing
consists of two parts so it consists of
Miller Loop and final exponentiation and
uh we today's talk we are focusing on
the Millar Loop and also final
exponentiation
so like what what can we optimize so
first uh we we work in elliptic like
elliptic curves so what does it mean so
we have some base field so we have
coordinates which are defined over a
base field what we can think about it
essentially they are like some integers
modu some some prime number and an
elliptic curve is all of the solutions
to some elliptic curve equation
u y like y^2 equal x x Cub plus a X plus
b and so the elliptic curve is a
solution to like this this equation so
we have a lot of
points uh and uh there is there's also
scalar field so let's say like if you
fix a point on on elliptic curve so like
all the let's say all the multiples of
it so
they if you have only a single let's say
a single group in the elliptic curve so
they they generate uh like it generates
um like all of the points and the
scholars they also uh they uh they
construct a finite field so we have two
fields we have the base field the points
and we have the scholar field for the
scholars in in the
elliptic it's really great if we have
some kind of match so right now we are
thinking that we are verifying
recursively so we are verifying a blon
proof inside a BL circuit so all the
arithmetic in a plun circuit happens on
the scalar field but we need to do
arithmetic in the base field in the
scalar field so like in in in in
different fields so we have some kind
some kind of mismatch it it would be
really nice if we have a match somewhere
so the scalar field uh corresponds to
the Bas field of some other curve uh and
uh there are like sometimes we have it
but most of the times we
don't so how how can we fix it we can
just use multiprecision arithmetic so we
can do it uh like naively as as for like
in library so we just split a big value
into into limbs so for example we split
it into like 64 bit lims so if we do it
like this then when we think about the
multiplication then we essentially we
have to use the school book
multiplication and the school book
multiplication the Astic cost of it it
is a quadratic in the number of Limbs so
it's it's not super beneficial or it's
not super efficient and also consider
that we are only doing the the integer
multiplication we also have to do the
model reduction so we have to do it
several times so a bit more clever
approach is actually uh to use um the
polinomial representation of this
multiprecision integers so it's the same
but uh we look at uh we look at the
polinomial where the co efficients are
the limbs of this multip integer and in
this
case uh because in a when we are
creating a blon proof then like actually
the pro can just hint some values the
pro can hint the result and also the
quotient and then like we can check that
this polinomial is is equivalent at some
random
point so when we compute the paing so
the computations in a paing happen in
different groups so they happen in the
in the group of the points but it also
happens in the in the extension fields
of the of the base field so we have the
G2 GT uh for the
bearing and uh so what are the extension
Fields so essentially extension fields
are a field of pols where the
coefficients are defined over the base
field and we also have to have like some
uh some let's say fixed fixed modulus
which is like some irreducible modulus
which essentially defines like how we
can reduce values uh when they go when
they are bigger than than the modules
it it's it's a it's a bit simpler to
look at the the the extension field
elements as vectors and then the
multiplication I'm sorry mul
multiplication inside the extension
field it's exactly as for the multi
Precision integers and we just do the
model reduction using the the the given
modules we have the same problems for
the extension multiplication is that the
complexity is quadratic so if we have
high like high extensions the 6 Dee or
like very complex to compute so what uh
for optimization we can actually use we
can use like towers of extensions so
like instead of going to the six
extension directly we first go to the
cubic extension then we go to the
quadratic extension and then the
multiplication becomes up somewhat
simpler so as a concrete examples let's
see like if we consider a quadratic
extension or over a cubic extension if
you do a multiplication then we first we
need to do one let's say uh one cubic
multiplication also for for computing
the result of the second uh second limb
in the in this six extension we have to
do two
multiplications uh
quad multiplications but before we we
before we mod reduce we can just add the
pols because like if you recall then if
you add pols then the degree of the
resulting po normal it doesn't increase
it may it may actually uh I'm sorry if
we add two Pol normals then decree
doesn't increase it may actually like
decrease if we if something cancels
out so there was a very nice result uh a
year ago by fter Prime and uh he he
actually showed that when we compute the
extension multiplication then we don't
have to do it uh like using the towers
we can do it directly and the idea is
very simple what we have for the
non-native multiplication is that
essentially we don't compute the value
but the approver provides the value
using a hint and also also the quo we
then the verifier provides some kind of
challenge using F usually and then we
just check that this direct extension
multiplication is
correct so this should be more efficient
and uh we like weed to figure it out so
we we
uh uh we found the direct extensions and
uh we started to to write out this these
equations and we started to to see like
how beneficial it is for that so the
previous result was only for p and 24 we
wanted to implement also for the other
CS for so for p P6 761 and P2
get something like this so it looks
something something simple but the issue
is right now that all of these
multiplications what we have right uh
right here they are non-native
multiplications
so like only for the left hand side like
we see that we have at least one so we
have like 10 or or 11 nonnative mul
multiplications and if we do the
non-native multiplication in this in
this way that we provide the result
using a hint then uh we have to do a lot
of range checking and uh this is not
like that
efficient so let's try to improve this
approach a bit and so
actually you can improve it like very
simply out say uh so when instead in
nonnative If instead of the
multiplication we want to evaluate
something more complex some like let's
say some multivariate evalation where
like instead of multiplication we have
some something let's say a * P plus C *
D plus EF and so on so we have some
something more complex then we we see
that actually we don't need to compute
all the intermediate results so we only
need to know what like what is the what
is the full result of the of the this
multivar evaluation
and the the complexity stays the same
regardless if we do non-native
multiplication only or if we do this
more complex multivariate evaluation and
if we implement it this way then
actually like evaluating these
extensions uh extension polinomial like
it becomes a lot more
easier so let's now write write it out
again uh like in full so we have the a b
c and then B so what we do at least in
gar is that we do not eval evaluate uh
non-native and extension multiplication
directly we just write it down that uh
we need to evaluate them later on and we
only provide the result using a
hint because this allows us to share
some of the computations so for example
if we instead of like Computing a fat
challenge for every check we computed uh
over all checks like if or we hash all
of the inputs then we can share this
random variable Z we can compute all of
the powers of
Z we evaluate uh the P of uh P at the at
this one place because it it shared over
all checks we evaluate A and
B and uh now we check so we replace this
a part the B part at the uh and also the
the the P part and uh now we have like
this one big thing what we need to
evaluate but this is this let's say
something what we can evaluate with the
nonnative operation which is which
corresponds to a single nonnative
multiplication and if you count count it
so on average let's say if we amortize
the the the P part then we actually only
have like non-native operations and this
is very efficient so for evaluating uh
the extension multiplication we only
need need three nonnative
operations and the main the cost here is
checking the the range checking the
hinted values so actually doing the
multiplications themselves it's cheap
but it's just like when we work in
when we look at the Benchmark results so
this is the number of constraints in in
in blanish so on average we were able to
to get 40%
reduction um but there there are like
still some uh some ideas what we have
for improving the performance so the
like one of the thing to to notice is
that we don't need to actually find
every quotient just need to like know
that there is a quo so if you look at
the random linear combination then uh
then uh can also provide the single
quo and we can apply it also for the
like different operations and we can
also apply the same technique for
curves thank you
uh thank you Evo for the presentation it
was nice are you ready for some Q&amp;A yes
so let's look at the
questions why do you need four different
combinations of plon and pl yeah it's a
it's a very good question uh I ask it
myself like many times so we need it
because uh we are uh like on one hand we
are restricted to what what we already
have so for example if we want to verify
a blun proof on ethereum then we can
only use p and 254 because this is the
only pre-compile which is provided by
ethereum and uh otherwise if you would
like compute a pairing using let's say
an imple assembly implementation it will
be just expensive uh for proof
aggregation uh we we will we would need
to have let's say a chain of uh chain of
uh or let's say two chain of Curves
where where like the scalar field of one
curve corresponds to the base field of
the other curve and the they come like
that often so we have to particularly
construct construct them and for example
because PN 254 is already given we
cannot construct a du chain for for that
um so we and we we also had like some
other like U other way because in linear
for example we have to we have to prove
uh also like pairings uh so let's say
like if if someone calls a pairing
precompile on linear then we have to
prove it that like it has we have
computed correctly so we have to we have
to show b54 precompile but the let's say
the the Cur we are working in is pls2
it's just is what it is makes sense uh
so next question can you show the
benchmarks again Yes actually we have
like a technical issue can only show the
questions at the end yeah but you can
take the questions offline with EVO
after his talk uh so the next question
does it work inside Nova folding
step it's a good question uh
unfortunately
I I cannot answer it
uh probably I think it probably would
but I I do not know the techniques
exactly to to answer it uh
concretely uh next question is how do
you generate Randomness in circuits okay
that's that's a very good question and
actually like this is one of the like
one of the uh nice improvements what we
have so for plon what we do is that we
we don't use vanilla blon we use uh like
a variation of blon where if we want to
let's say hash some variable inside the
blon circuit then we like copy this this
uh this variable into this uh another
let's say another column of like of blon
so we have a different um uh one more
column and then essentially we use the
commitment to that column as as the
value so we don't see the next question
but I can read it from the phone can you
use katuba for direct multiplication
instead of school book I think it's for
the extension maybe yeah yeah we can and
actually like this is uh this is how we
did things before uh and
yeah and I believe it's going to be some
more optimizations than compared to the
benchmarks yep
yep uh why if we take the next question
one more yeah can yeah can you use this
technique to anything that can be
expressed as polinomial I think you
explained it for multiplications yeah
yeah we can do it uh so we have a plan
to also use it for uh uh let's say
elliptic curve operations so for
additions doublings scalar
multiplications and uh we Al Al already
expect to for it to to give like a lot
of performance improvements
and we have one final question it says
can we use the same nonnative field
arithmetic mechanisms to prove secp 256
K1 operations in B and 254 Scala field
yes we can uh so actually so we Pro XP
in PLS 12 377 so on linear again we also
have to prove the ecdsa promiles and uh
so yeah we can we can do it we can do it
fairly efficiently I would say and uh
like for us because they all the all of
the methods or all of the techniques
what we use like they are very generic
so we can use the field what we emulate
and the field what we work in so
everything's gener generic and it would
work very well with respect to this
question it means it's already
implemented uh yes so it is implemented
you can just take it as
is okay so thank you again Evo and can
you join me applauding Evo again thank
you thank you um so we have one more uh
session uh for which I will be the MC
and then we're going to switch MC's so
I'm going to be back in 5 minutes to
introduce the next speaker thank you
and welcome back and please for those
who are just joining us have a seat so
I'm youf your MC this is my last session
then I will go probably get some food
uh so next talk is about Circle stocks
GPU implementation so this one is
implementation focused and it's going to
be presented by Daniel and Julian please
a round of applause for our
speakers all right uh hello I'm Daniel
from nethermind and this is uh Julian
from ER and we're here to present Circle
start GPU acceleration
so um what is a circle Stark we're going
to start pretty high overview um well
this is your classic uh proof system so
u a circle Stark is a proof system you
have two sides a prover and a verifier
and um the prover wants to send over
some proof uh usually some off fiscated
data of like uh private input and some
uh computation to the verifier and the
verifier you know sends back um either
accept or reject and uh does so in a
series of challenges and usually in
production we don't really use the
challenges um in these queries we
instead replace it with some hash
function and just going over the acronym
for those who are not um quite familiar
Ser knowledge just stands for the fact
that we hide um all the private input
and the computation away from the
verifier the scalable um stands for the
fact that as the computation increases
um in size the verifier and the um
prover run faster and faster and one of
the key things is that the verifier runs
much faster than the approver
transparence U transparent just uh
stands for uh the fact that we rely on
public Randomness so think hash
functions and one thing about the
difference between this and ZK snarks is
that ZK snarks use some trusted setup um
and usually there's some data remnants
that you need to take care of and if you
don't it might nullify the system
whereas for ZK Starks um we don't
actually have this and finally arguments
of knowledge just uh referencing the
soundness of the computations so this is
just um making sure that everything is
secure within the technology that we
have
today so let's talk about a matter of
efficiency for ZK snarks um we use field
sizes that are really large um these are
two to the power of 256 and uh they use
it because the elliptic curves that they
use underneath uh require this for the
actual security um whereas for Starks we
don't really need to use all of this
space uh because we are not actually
using elliptic curves we're instead um
uh working over uh just the field itself
and um the computation size that we're
usually using in production is around 2
to the^ of 28 so we have a lot of U like
um uh we have exactly two out of 228
like as the upper bound bits of unused
space and something to think about is
that uh about a 4X uh increase in the
actual field size and you can think of
field size as a like a prime number uh
is um equivalent to about a 9x increase
in the actual computation size so where
do we go from here we want to decrease
the field size uh while also keeping in
mind that the lower bound of this like 2
to the^ 28 so we need some field size
that is still greater than this but at
the same time we want to get um uh low
enough such that we keep in mind
computer architecture so 32-bit uh uh
CPU arithmetic operations are very very
efficient so we can if we can find
something in this area then that's very
ideal um so just looking into um uh
previous primes that were used we start
with Stark Stark field Prime which is uh
way down lower and lower and until we
finally get to the meren 31 prime which
is what we use actually in the circle
Stark um and one thing you'll notice is
that there is a plus one basically uh
for all the Primes before meren 31 and
this is on purpose this is um to unlock
basically one of the core features or
core functions that Starks use which is
a fast foror transform or uh if you're
again in terms of like finite Fields
it's a number theoretic transform and um
in order to actually use this it
requires as a generalization that the
field the prime minus one is really
easily divisible by two a large uh
number of times and with the mer M Prime
if you see um if you subtract one you
get 2 to^ 31 minus 2 and this isn't
really divisible by two uh other than a
single
time and so what what do we do uh
mathematicians actually um in said map
this field onto coordinates of the
circle and um by doing so we gain one
extra point and this one extra point is
what allows us to actually use the
mercen 31 and that's why it's called
Circle Stark because we're using the
circle as the uh kind of the group um in
order to unlock this fft that we're
using and so um the meren 301 is very
efficient on 32-bit architecture uh
there's um uh lots of optimizations that
you can do to really really um bring
this out and um as opposed to like baby
bear Prime which we saw in the previous
slide it's uh the next higher uh field
size it's um basically a 1.4x
performance
increase all right thanks Daniel so some
Basics on GPU
optimization um to be honest uh gpus are
used because they can handle many
simultaneous calculations but there are
also many uses for this so we will fall
in the first two categories which are
data intensive computations and alic
operations there's also the original
purpose for gpus which is point number
three um this comes with some problems
so uh gpus and CPUs have different
memory spaces uh one cannot access the
other's memory space and copying data
from one to the other is expensive this
means that we have to be efficient when
working with memory in these different
spaces there's also the fact that memory
accessing is not trivial so memory
accessing in GPU is best used coal East
which means um gpus benefit from the use
of consecutive memory accessing and
sometimes um our algorithms are made so
that memory access is
complicated this means that we have to
find a balance uh in which we uh play
around with our algorithms memory access
and the most efficient memory access
which is goal
East there's also benefit fits to this
we wouldn't be doing this if there
weren't uh when we launch threats to
processor data uh they will run
concurrently so they'll compete to uh
use the resources of the
GPU but the GPU can handle some threats
at the same time and this is what
benefits us so uh this will help our
calculations be parallelized and run
fast there's also the fact that some
architectures we'll talk about Cuda here
um bring you some particular uh
optimization uh heuristics or
optimization tools uh we won't talk
about them much here but here are some
of them consecutive memory access
operations andure registers are stuff
that are like um tools that are very
specialized but um yeah not much focus
on them for the
stock uh just putting some notes onto
the actual uh problems that we have so
uh one of the main things that um uh we
have for problems is uh the efficiency
of data transfers so from CPU to GPU and
back and forth and when we're working
with really really large um computation
sizes really think 2 to the^ of 28 um
copying back and forth anytime we want
to actually offload the functionality of
the prover onto the GPU comes at a very
very steep cost uh the solution is
really quite simple we keep most of the
data on the GPU to run throughout the pr
uh time and uh and uh yeah that's pretty
straightforward but let's look at a
different problem um we have a problem
of memory access so the way just gpus
work is um data that's uh close together
you can think about it um accesses um
are very very efficient but uh for
things that are really really far across
uh and lead to a lot of uh overhead and
lots of uh downtime and for at least for
um our use case when we're doing ffts we
have to access data uh from this really
really large set that's really really
far apart and this uh poses a problem of
all this extra overhead there's a few
solutions to this one is the fact that
we can kind of break down uh the uh data
sets into smaller chunks so that the
data access is a little bit more um uh
uh similar or uh nearby and the problem
with this though is that you uh
introduce a little bit of overhead for
actually reorganizing the data right
reorganizing and uh having um a copying
on the device itself well another
solution that we can have is uh breaking
down the functions into smaller and
smaller um uh uh kernels and uh by doing
so you introduce the overhead of of
calling these functions um but I think
more than anything uh the optimizations
that we're working on and uh that we're
continuing to improve on is a
combination of the three right we want
to minimize these data transfers we want
to have efficient memory access and we
want to reorganize um and break down
these functions uh uh as um few times as
possible and um one thing to note about
uh I guess other Hardware that's uh in
the uh ecosystem is uh one is uh fpgas
they also work similarly to to similarly
to gpus and that they work in parallel
uh the advantage is that they're a lot
low latency the um con however is that
um there is a high uh developer
complexity um right so there are a few
teams but I think as we get further down
the year we'll see more and more um
teams actually working on this and as
for A6 or any other ZK related Hardware
um we uh need to manufacture these and
design them way in advance so until we
actually have ZK systems kind of
converge to a single point and have mass
adoption then we'll kind of have to wait
and
see okay so for a real life case study
of this being applied we're going to
review first a sequential algorithm
which is uh component of the circle star
prover then we're going to make it
parallel and then we're going to compare
both of them to see uh how they affir in
terms of
performance so bat Chambers is the name
of the game uh it's a su component with
I this is a circle starover its purpose
is to calculate um the inversion for a
lot of numbers okay a lot of field
elements but since calculating the
inversion for a field element is an
expensive operation we use something
called Montgomery strick okay this
Montgomery strick is the sequential
algorithm we're talking about here so
let's start with four field elements uh
I CH chose four because it's simple to
explain we calculate the accumulated
products for each of these field
elements which means beta 1 beta 2 Beta
products up to A1 A2 A3 and A4
respectively um but this is inefficient
because if we calculate it this way uh
programmatically we can use that we can
see that we multiply a lot of them um
repeatedly so we can rewrite this as is
right we can rewrite this um by using
the previously calculated accumulated
product this is simple to see but it's
also
uh relevant and very important because
um when we want to parallelize this this
will be a limiting
factor then uh when when we're finished
we take the biggest accumulated product
and invert it using the extended uclean
algorithm which is this expensive
operation I was talking about and then
uh we see this ear trick to calculate uh
the inversion of the last the very last
element at first so intuitively because
there's no division in field operations
um we take uh beta 4 inverted as one
over the product of all the numbers this
is intuitive once again but it helps to
see how when we multiply it by the
previous accumulated product we cancel
out all the numbers that we don't want
and end up with 1 over A4 which is once
again intuitively uh the inversion of
A4 the same thing can be done to
calculate the inversion of the previous
accumulated product this way by
multiplying the the inversion of the
whole accumulated product by A4 and
getting uh one over the accumulated
product from A1 to
A3 and this helps us calculate the
inversion of every single number we have
in our list a four is calculated there a
three inverted is calculated there A2
invert is calculated there with the same
intuition with the same trick and there
and then A1 is an edge case so yeah it's
easier to
calculate now um this turns a potential
N Field inversions right so for for an
array of size 10 it replaces N Field
inversions with three n multiplications
and one inversion this is way cheaper
and and we like this tray
off now um as I mentioned monomer trick
cannot be parallelized as is because
calculating any accumulated product
means you need to have the previous one
uh and that means uh strictly
sequentially you need to calculate uh
each one and we'll adapt this algorithm
for it we'll pair ize it so we can
compare them
later this is the Adaptive trick to be
able to parallelize it in GPU uh we
start the same way with four field
elements but we'll make an assumption
that'll help us adapt it which is we'll
suppose the amount of field elements is
power of two
um we take those elements and multiply
them by pairs
okay multiply them by Pairs and we have
beta 1 to2 beta 3 to four as the
accumulated products by pairs
and beta 1 to4 as the whole accumulated
product now notice that this tree can be
paralyzed in the sense that one can
calculate each node of the same level of
the tree at the same
time okay this is useful because then we
will want to send those calculations to
run in parallel to the
GPU now we take the whole thing the
whole product and inverted with
expensive algorithm just like before and
we decompose it similar iation than
before right we can calculate beta 1 to2
with beta 1 to 4 inverted and beta 3 to4
this way okay um it's the same as before
just that the numbers in the numerator
change A3 and A4 and are in the
numerator and cancel out with A3 and A4
in the denominator and this is what we
get 1 over A1 * A2 which is intuitively
the inversion of beta 1
to2 so the tree is completed by doing
the same thing in the other side and
finally decomposing the accumulated
product for each of the elements that we
wanted to invert and we have all the
inversions here so once again this same
tree that I showed you here can be
parallelized the same way as the
previous
one now uh apart from parallelizing it
this way one can optimize it further
with CA specific or architecture
specific
optimizations but even even then you can
see the difference it's ridiculous um
this is compared against CPU using AVX
AVX is a a technology that lets you
handle single instructions with multiple
data in GP in CPU so that's even better
than CPU by itself and the difference is
still ridiculous this is for 2 to the 24
element to be inverted and this is how
it scales
uh bigger bigger
arrays so what did we learn GPU paration
is very powerful uh and a simple
heuristic goes a long way so a simple
parallelization can handle uh a lot of
data very
quickly this is a circle star prover and
we see how GPU makes the difference here
uh in accumulated time measurements so
this is a time uh that it takes to to um
run the prover up to that point so it's
accumulated and you see that uh the
difference the differences are abysmal
this is in the order of milliseconds
okay um so the GPU PR is way faster than
CPU using ABX
okay so summary like takeaways from the
talk what did we learn in the talk in
general first Circle Starks use smaller
fields to balance security and
efficiency uh harnessing GPU power is
vital and easier than you think for the
computation of cryptography Primitives
and of course we should keep an eye on
future Hardware acceleration Trends
because the future is in fpgas
um okay some due thanks uh we wanted to
thank the etherum foundation for
allowing us to be here um and organizing
Devcon uh from Erics we wanted to thank
nethermind for letting us work with them
uh that was amazing we appreciate it
very much and and yeah I think that's
all thank you very much um you have some
resources on Eric sqr and you have also
nethermind socials here I hope you
appreciated the talk I hope you you
learned something and yeah thank you so
very much
yeah thank you Daniel thank you Julian
it was a nice S I appreciated how you
kept it high level but also low level
was nice thank you so why we take some
questions um so the first one since
modern CPU are 64bit y 32bit field are
efficient so at least for the um
operations that are um uh
on that architecture um U I understand
that it's your concerned for like 64-bit
but a lot of the actual arithmetization
for the um underlying functions uh is
optimized for 32 uh bits so we can work
with 32 bits um very
efficiently okay so next question is is
this GPU Prov open source works with
meal good question yes this GPU Pro
Source uh you can find it I believe in
NE mind socials probably um um it's
separate from like the prover itself but
uh yeah the GP implementation has its
own repo and I don't know about Metal to
be honest I wouldn't be the one to
answer that question I'm
sorry so the last slide you had it has
the QR code so yeah oh sorry we cannot
go back but yeah last slide then we can
uh put it up later those QR codes can be
followed uh in any case at Eric's Coop
and at nethermind
F yeah and also the the talk you will
find the video on the dev Devone
passport so you can find oh yeah
definitely so next question comparing
M31 and baby beer which is more GPU
friendly and why uh so the M31 would be
um much faster just because it utilizes
that uh 32-bit um uh kind of space um
more efficiently and in the improvements
that you saw over just the baby bear you
get about 1.4x and it's just just um
because it's it comes down to a trick
that you can use with the meren prime
specifically the 2 to^ of 31 minus 1 um
I won't get into further details but if
you want to look it up online there uh
is a easy way to uh do modular
arithmetics on
cool um next question is how Erics and
nether mind involved on Circle stock and
stwo okay okay yeah uh so Eric and
nethermind work together in the St GPU
implementation um nethermind worked with
stet and er worked with nethermind to
develop the two Prov GPU implementation
and the two provs and the Stover uses
Circle STS that's how it's
related
okay um so if we can just scroll down or
maybe I can check it on my
phone yeah is anyone working on web gi2
acceleration of ZK generation
I honestly don't know uh that's an
interesting question uh we can talk
about that later and yeah we can take
this offline then I'm sorry um Can GPU
be used to speed up ZK olops
finality I believe it can uh I mean what
stet has achieved is impressive so I
believe most is
possible I think it keeps going yeah
yeah is it any better if we go to even
more smaller Fields example 16 bits so
the ones you presented were like 32 bits
yeah so um we still want to keep in mind
the actual size of the computation so in
production usually we use uh up to 2 to
the^ of 28 bits and so we don't want to
get anything lower than that and also at
the same time we want to really unlock
the 32 U arithmetics yeah and I think
for the next question you also talked
about it but how does GPU comp pass to
fpg and also he talks about ASX for
Circle Stars maybe specifically or yeah
at least there's no fpga for Circle
stars um that might be an interesting
Avenue to really uh look into and
research but um in theory the fpga um
should have lower latency than gpus so
it should perform marginally faster but
the since we don't really have anything
on that we can't really say for
sure uh so we have time for one more
question and I can I can read I remember
it um so the next questions was
regarding the Montgomery trick uh we
swept under the rug uh the fact that we
assumed um the elements we worked with
were a power of two well this is why
this is because um we can work with any
number of elements and then just add
elements until we reach the next part of
two do the optimized algorithm the
optimized adapted trick in GPU and then
discard the rest of the elements uh we
know how many we added it's easy it
doesn't matter it's a trivial thing to
adapt your your array to be a power of
two so it shouldn't really matter I
believe that's what we're they referring
to all right so that's it for the Q&amp;A if
you have more questions you can find
Julian and Daniel offline please some
Round of Applause for
them thank you very much very
much so this was my last uh session and
then I'm going to hand it over to Andy
who's going to be your next MC enjoy
Devon
welcome welcome afternoon
everyone glad you guys are here um want
to introduce myself I'm Andy I'll will
be your MC this afternoon I work and do
product and PSC but this afternoon uh
I'm going to join you here until the end
of the day I hope you enjoy all this
track and uh we have fantastic speakers
so I'm very excited before before we
start just want to yeah find some place
to sit uh for the ones who are standing
I also wanted to remind yourself uh you
guys that there's always a QR code here
on the right and that means that if you
scan it you can ask questions to the
speaker and that's great uh because at
the end we have five minutes to have
questions and I think those are uh one
of the most enjoyable parts of of each
talk so to get started with our first
Speaker uh his name is Ricard Bell and
he'll be talking about leveraging high
performance Computing for efficien
Starks especially an analyzing the
competitional aspects of starks
especially on the approver side and um
with that better reasoning please give a
big round of applause to rard
welcome okay uh hello everyone thank you
for being here I am Ricard b as he said
thank you for the presentation I work at
polygon um basically I work on on
develop and optimizing ZK technology and
yeah this presentation is about
leveraging high performance Computing
for efficient start
provs um the presentation is divided in
two parts first I will talk about the
present in terms of product which is the
ZK evbm and I will explain a little bit
the the Lessons Learned on the
development development of the ZK evbm
and then I will talk about the future uh
which is what we are working now which
is the the a ZK BM so a general propos
proving system uh based on STS as
well okay let's go for the ZK evm the ZK
evm was released two years ago ER and it
pro is based on a on a star method and
uh well we have an star and then we have
aggregation to uh so we have a recursion
process to aggregate proofs and then uh
from uh with a certain frequency we will
uh
send the proof to L1 okay the only thing
that we need to understand about an
Stark for this talk is that it basically
has two stages or two phases in the
first phase we will compute the
trace and then in the second phase we
will take the fry polinomial which is
kind of a summary of all the trays in a
single polinomial and we will prove uh
the proximity to a CL low degree
polinomial right uh the commit phase is
done in different stages uh this means
that the trace is is is filled in
different stages and this is because we
need Randomness for some of the stages
we need to we need some random numbers
to valate some of the polinomial of the
of the trace and this Randomness is
obtained from the previous stages so the
roots of of the of the of the of the
pooms evaluated in the previous stages
are committed to the transcript or are
added to the transcript and then we get
Randomness for the uh next stage that we
have to to evaluate okay uh in our
arithmetization of the zkm we have
the number of rows of the trace which is
something that we can fix uh it's it's a
parameter of the pro let's say it's uh 2
to the 25 so it's about 32
million this is quite a lot and it's it
ends up posing a a requirements of 800
GB of memory okay I will talk more about
this okay
um so why we use such a big number of of
of rows on our Trace basically because
we have a we have a monolitic approach
on the imization this means that we have
a static capacity so the our Trace uh
the capacity of our Trace is determined
by the number of rows and so we fix a
big number because basically um we want
to be able to handle any transaction
that comes to the network okay that's
why for the most heavy uh loaded
transactions that that the ones that
will will need more steps we we have to
uh we we need to have enough space to to
handle them okay this approach has some
disant has advantages but also some
disadvantages clear a clear one is that
okay uh when we have to close a batch
because we don't have more room for new
transactions uh because some of the St
Machines of the of the trades are filled
uh then there will be some spare um
cells on the trades that we have to
prove but are not they are not being uh
filled with with with real uh values
coming from the inputs okay so we have
some padding effects uh but also has
some advantages for instance that we
have a um like a constant workload that
we can optimize very well we can
allocate buffers on on Advance Etc so it
also has some uh Advantage related to
Performance now let's talk about timings
uh appr proof of these huge trads uh for
the ZM takes about 6 minutes
and the cost with the uh gcp instance
that supports ABX 512 it's only 0
$46 normaliz it by the number of
transactions ethereum transactions that
that we can fit within a batch uh it's
about 0.2
mil uh this would be the overhead per
per transaction okay so it's a very low
overhead which is negligible in terms of
the grand scheme of things in terms of
the cost that adds to the transaction
uh moreover uh okex has uh done a a very
um interesting job that it has ported
the appr to gpus and this has decreased
the latency to about 3 minutes okay so
uh and even decreasing the cost so this
is a a perfect situation where we
decrease the latency at the cost by
using gpus those are numbers given by
them and at the end we end up having 0.1
million dollars per added on on the cost
of the transaction okay so it's really
good
uh the speed up obtained from the CPU to
the GPU it's only uh if we if we
consider end the end to endend proof
from the beginning to the end it's 2x
here is is one of the limitations of the
Prov as we have such a huge Trace at the
end we will we will be transferring a
lot of data between the host and the
device during the execution of the
kernels okay we will and we will be
limited by the PCI
Express however still if we look at the
real cost What It's The End one matters
they are very low so it's not something
that it's very relevant in the in in the
current context if we go a a little bit
deeper and look into the kernels
distribution when we do aof it's a
perfect situation or a good situation
because we have that 95% of the time of
the time of the proof it's just uh
concentrated in four Kels especially in
two which are the entity and the
merization which take 70% of the time
and then we have Expressions that are
linear combination of polinomial and
then the executor which is the first
phase of the of the trace evaluation so
it's the part of the trace evaluation
that uh depends on the inputs okay this
is the the initial execution of the
inputs so basically we have to focus on
on these four kernel basically on two
and that's what we did a lot of work on
on this during on the past before
releasing the the ZK evm the first thing
you have to consider when you want to
optimize a code it's to understand which
where are the boundaries for the for
this code and
basically you have to do a roof line
analysis basically the roof line
analysis shows you where where is the
limit depending on the arithmetic
intensity of your kernel okay if your
kernel does a lot of operations per each
field element that you blow to uh the
gache of the CPU it means that you it
will be bounded by the CPU by the by by
by the Computing part of the process and
if you have a lower atic intensity you
are you are becoming bounded by the by
by the memory transfers from the from
the main memory to the cache of the CPU
in our case we are basically bounded by
the memory transfers for all the Kel
except the hash and this makes sense
because the hash does a lot of
arithmetic operations per each uh field
element involved in the hashing okay so
we focused a lot on optimizing the
optimizing the ntity uh we did um a lot
of uh basically the focus here was to
minimize the L3 misses we got uh well at
the at the end the result is the
performance that we get is to um perform
the entity on 100 polinomial of size 2
to 23 to 1.9 seconds this is more or
less the
reference and then the merization of
course is about uh in the CPU in the CPU
is another thing in the CPU it's about
vectorization vectorization so taking
advantage of the vector registers to do
in each clock to try to do four eight uh
operations at the same time and we go to
a performance with goldilux one not
goldilux 2 of 1 million hashes per
second okay so this is the summary of
what we did more less two years ago
before launching the zkm at some point
we arrived to the conclusion that
keeping improving the pr would not have
any relevant impact on the on the
performance of all the zkm because we
were not the pro was not a botel neck at
all okay so we were very happy with the
with the performance that we were
delivering to the to the application
okay that's a good situation we can
focus on other stuff uh and that's what
we are doing now the project in in which
we are involved is the the cisk zkm
which is a general propose uh
zkm uh basically uh as others that are
in the space we want to prove uh any
program that uh it's written in a high
level language like like rust CPP or
others okay uh the motivation of doing
this project or the the it's very
meaningful for us because we have
acquired a lot of experience a lot of
tooling a lot of uh knowledge on running
the ZK evbm which has been in many two
years and has been uh well we have uh
struggled a lot with performance ET so
we can take advantage of all these
things that we have learned to put them
for in the service of this new project
uh which is more General and and can be
more more impactful for for for in
general for the for the any user okay uh
it's you can you can check the GitHub
it's not fully fully it's not everything
complete to do a proof but uh it's
almost there so maybe in one two weeks
we will be able to prove any code that
comes written in
INR okay now the main difference with
this new um proving system so the
proving system that we are doing for for
zisk h it's differing in many ways but
the main difference comes from the
arithmetization or because now we don't
have anymore anast static capacity for
for the trace we will have a dynamic
capacity this means that we will shape
the trace uh depending on the input okay
and it will be uh divided in different
into different eight instances all this
will be explained in the next talk so I
don't I can skip the responsibility of
explaining this well but of course I I
encourage you to stay to to understand
all the all the implications of this
okay uh on the proving time basically
you will have to you will have to prove
uh all the instances that that you have
gener ated
onization we call them sub proof so we
have an array of sub proofs to to be
proven and then of course we will have
an aggregation phase on which on on
which we will aggregate all the all the
proofs resulting from for all the
instances that will result on a single
proof okay let's think about the
computational implications of all of
these uh in fact on the CPU efficiency
out of the box you don't get anything of
this you get worse time worse uh CPU
time why but basically the GPU I the the
the cost of one proof is proportional to
the area and this this uh stays through
even when you go to small small small
instances okay so you have proportional
cost you have divided the main Trace
into different sub traces but the area
is more or less the sum of the areas is
more or less the same of course we have
eliminated the padding effects that this
this is helpful but uh and it will
reduce a little bit the overall area but
it's not a big it's not a big difference
and of and we have added agregation cost
so at the end we are kind of making more
the proof a little bit more costly
however with this new
granularity there are a bunch of
opportunities and the most important one
is that we can take advantage of
accelerators um without having this
limitation of being to move data back
and forth from the host to the GPU okay
with this PCI Express limitation so this
is one very important Improvement here
we will be able to exploit gpus more
much more efficiently we have other
ideas that Vector like uh vectorizing
the execution of a Starks so we can kind
of run eight Starks at the same time
with trying to do every operation in a
vector register containing uh elements
of different Starks okay these some kind
of ideas that we are considering but the
most appealing idea for us uh it's going
to distributed computing basically the
idea of distributed computing is that
you want to R to run uh your proof using
uh not one single instance on on the
cloud but various instances and with
this try to strong scaling your your
your application okay you you want to
produce a latency which is one of the
main focus of of this project of this
project okay so let's talk about
distributed
Pro ah first of all um one of the we are
very happy or we have had an we have a
very important advantage on this project
is that we have access to a
supercomputer which is called selenius
it's part of of the CC Euro organization
with the in Netherlands okay it's part
of the erpc but the division in
Netherlands let's say and we were
granted uh of resources there to do our
proofs we kind of submitted the research
project where we want to find the limits
ofing a stark we want to see where can
we go where where how how how far can we
go on the reduction of the latency okay
this is our goal uh there is three L for
us we have hundreds of thousands of CPU
CES that we can link together in a proof
we won't go to at this level but
Hardware is there and we can we have
hundreds of gpus as well that we could
link to to run a proof okay um
nonetheless uh we want to we we want to
Target the highend performance available
but all that we are doing is can be
running on the cloud as well so we want
to reproduce at the lower scale we want
to reproduce the results on the cloud
and this is very important because the
production won't be done on on a
supercomputer will be done on a cloud
system like the ones that we are using
today
okay let's talk about the first part
filling the trace the wus computation
it's the part of filling the tray that
comes from the
inputs um how will we do this in a
distributed um
environment the most KN way to do this
would be okay I have um I have several
processes I talk about processes and
threats here one process two process
don't share memory so our process
distributed across the network and and
then the process Spa threads okay so you
can assign one process the master role
and say okay you will compute the trace
and then send distribute the result into
equal parts and then send to the others
okay this is a functional approach but
is not scalable at all so we will have
we are not parallelizing anything we
have a lot of memory requirements in the
master process and we are also at add a
high communication overhead so is not
approach uh serious approach now let's
try to get get rid of the communication
costs let's do the computation of the
winess uh redundant in every in every
process okay that's fine we have get rid
of the communication costs but we are
not accelerating because it's redundant
and we have um um we have high memory
requirements in all the processes
because all of them have to store all
the TRS so not not still there okay the
next strategy that we have been
developing is okay let's minimize the
Trad that we generate so we have divided
the tra generation in like kind of two
stages in the first stage we only
generate the minim what we call the
minimum Trace which is the information
that you require to uh then in a second
stage restart the evaluation of the
trace at any point okay so in a second
stage we can in parallel recompute the
trace
and divide this computation okay so we
have this first stage of computing the
minimum Trace which is very fast and
then uh we can from the information
generated in this process we can
distribute the tra between processes I
mean each process will have had run this
same Pro this same M the same this first
uh step of gener generating the minimum
Trace has been run by by all the
processes then all of them know which is
the actual la that have to be
distributed and then all of them um take
one part and then compute this part but
only this part okay this scale this will
scale much better okay let's look at the
results the test that I am using here
and in the next slid it's uh a program
that uh executes 10,000 sh 256 uh um uh
hash operations the medication that we
are generating is not complete okay
because well as I said this Pro these
project is under development at the
actual moment at that point we're
generating instances for the main and
the binaries and some some multiplicity
tables but it's enough to understand the
the the results and the potential of
this okay uh now if we consider as a
reference the emulation time which is
executing the program without generating
generating any Trace anything even not
the minimum Trace okay the time is 0.6
seconds for this program this means that
we are going about 80 MHz is our our
speed okay the overhead of generating
the traces ranges with one instance with
one compute node it's about 100% so we
are doubling this time down to
Computing nodes so we are going really
down the scalability is not very good
but because we are already very fast on
the execution of this of the trace after
uh because we are dividing it into
threads on a single note but at the
end really this overhead is not so it's
not it's very acceptable okay only 30
because I am running out of time uh then
let's talk about the distributed how we
manage the distribution of the of the
sub proofs so we have to solve the proof
for all these instances that have been
generated uh here we have uh um we just
need
to so here we have a synchronization
point because all these instances have a
common uh share the the transcript okay
this means that that this object to get
the randomness for the next stage is is
shared between all the instances and
this poses some synchronization between
the execution of all these instances
okay uh what we do is a communication
stage where we share the roots that have
we have to put to the transcript and
then we get the same Randomness in each
of the in each of the proofs let's see
the results scalability of this phase
generating the sub proofs it's 100%
efficiency okay we go from 70 seconds to
down to to 3.3 seconds okay uh it's a
little bit suspicious that we have even
super lineality so if you see the the
efficiency which is the line it goes
over 100% at some points so this is
something that is not let's say a little
bit suspicious
uh the problem here is that the
distributed appr even runs better in a
single note because you can fix better
theity of the threads that you are using
for the for the sub proofs then if we
compare the base point is the
distributed Pro itself on one single
compute node as a reference then we get
something that is more meaning
meaningful okay we are getting a
parallel efficiency of 80% that's good
let's go for the distribution the
distribution uh the the
sorry the recursion we have some
communication requirements when we
generate the tree because the sub proof
that we are aggregating can be hosted in
different uh processes and we have to
transfer to the process that will
generate the
agregation and if we look at the par
efficiency really it's not so appealing
right it's 44% okay but here we the
problem that we have is that um
um when we are going down to the three
there are at some point we have less
aggregations to do than processes okay
so there are some resources that are
being not used at all okay so if we if
we just release these processes to do
other things the real parallel
efficiency related to the hardware that
we are consuming is 88% so it's again a
very acceptable par performance now if
we look at the complete overall
situation for the all the proof
including including the winess
computation the sub proofs and
agregation the parallel efficiency is
seconds the recursion is taking most of
the time right now it's 65% of the proof
so this where we have to focus to
optimize the the performance to even
decrease more the latency and the most
important conclusion here is that as we
have a good parallel efficiency right uh
it's 70% by we can increase the latency
by 10x right we have increased the
latency of the proof by 10x while the
cost have only increased
to have because basically it means that
you can really decrease the latency uh
without additional costs so that's why
we and this can be reproduced in the
cloud because we are not uh we don't
rely in a very high high um performance
Network because the transferring of data
that we are doing is is really uh
minimal we are transferring uh proofs or
we we transferring Roots uh which is
minimal information
so just I am to very I'm closing with
this so we have we can decrease reduce
the latency at a very low uh cost
increase and as fter improvements we
will focus on the recursion on some
algorithms like a steel and multif Fry
of course here that is not the GPU in so
with the GPU we can even accelerate more
because uh our our performance now our
our architecture can uh support gpus
very well because the instances are
smaller we can even reduce the more the
performance with the gpus and also run
on the cloud infrastructure is our next
step okay sorry for extending a little
bit and I can take uh any
question thank you record yeah Round of
Applause so we'll have a few questions
reminder that great for everyone who
submitted the QR code is always uh in
the presentation and we and you can also
vote them so we're going to start if if
it's all right for you uh with the first
one could you give an how do you
generate a minimum Trace that can then
be used to restart the trace at any
point what's the data structure like
yeah uh then the minimum Trace only um
has is kind of evaluating The Columns
that you require to then be able to
extend the trace and this basically is
two columns for the main machine which
is the the ones that uh load the load
data from the memory it's kind of a a
and b register so it's only two columns
from that the rest of columns that
compose the main tray uh can be
generated from this information uh at a
given checkpoint okay so that's that's
basically it so it's evaluating just a
subset of two
columns great so the next one voted can
we say CIS VM basically trads more
aggregation cost with better concurrency
architecture
so basically um yeah um yeah that's is
one way to
uh although the agregation costs uh now
are huge and we have to pay for this
aggregation of course to have this
granularity that we are interested on H
but we want to reduce of as much as
possible the itat by improving the
algorithms for instance plony 2 has a
very fast aggregation we can do
something similar we have the a Ste
approach that reduces the number of
queries that you have to ver verify on
each agregation uh step so we had a
package of things that we can we can we
can do to to improve this part also we
have to really think which is the the
the ground reality that it's more suited
for for our Hardware so it's not maybe
we can generate less instances if we can
really exploit the hardware well and
then the recursion will have less levels
okay so a lot of Investigation uh it's
it's coming on this part because as you
saw it's the one that um it's more
relevant at this point okay great great
great the next one is can cisk run
programs written in lower level circuit
languages will they be faster than rust
will the Gap ever
disappear the the top
one well the purpose of this is is is
not this the purpose of this is
basically uh generate the the inputs
with with a high level language okay
basically rust C++ or any other language
so this is mainly design point of of of
this of course you may be able to
generate some arithmetization or some
and then use the prer as a component
that can be
um it can be self-contained and you may
be able to use it but uh the main
purpose is it's just you generate your
code with a high level language you
don't care about anything you will get
uh the proof of correctness of of the
execution of this of this of this
program from the inputs which will the
inputs of the proof would be the input
of the program the output of the program
and the elf uh of the compilation of the
program with risk five or any other uh
other architectures that we are also
considering like wmon or llbm or great
great great and I think we got chance
with one more quick uh just trying to be
futuristic can you give it insights on
what could probably be done in order to
improve the CK evm or VM prover in one
or two orders of
magnitude for me it's clear that we have
to go the the distribution Vector is a
path or a vector of improvement that we
have to take uh because because if you
rely on more specialized and and
complicated Hardware uh on a single but
relying on a single on a single instance
on a single
note you you won't we won't exelate but
we can take advantage of the more
sophisticated uh note available the more
sophisticated Hardware available and
compose it and take it two three four
whatever number can fit with a good
parallel efficiency because we are we
want to control all the time the com the
costs of the of the proof If you have
par efficiency it means the C don't grow
so that's that's the tradeoff that that
we really have to take into account
amazing please give a big rock of
Applause thanks so
much we start with the next talk in two
minutes next time
welcome welcome great great talk that we
had before and this next one is also uh
connected as it was told by rard and the
title of this talk is B Cup leveraging
start for tailor prooof generation and
just a brief reminder it allows to
achieve better cost efficiency by
focusing on the active parts of the
execution Trace um rather than just the
whole entire Trace so please uh give a
big rock of Applause to what welcome
Felicia Barcelo and Hector MIP Aron
welcome hello yeah
well hello everyone I'm MIP and he felo
we are from polygon labs and today we
are pleased to explain a little bit a
concept or better say I will say a set
of Concepts that we have been working on
during these months which we coin as
vops okay which stands for variable
degree composite proofs uh we will see
that this set of concept will allow any
prover specifically an prover to prove
any canic of mutation in a way that H he
can tailor the computation uh as it
wants okay let's start anyways with the
basics ER let's say that you are posed
with a problem of er proving any a
specific computation okay and you
normally see a computation
in two different views one view is the
evolution of this computation along the
time okay for example let's say that you
your your computation is composed of of
four variables you study the evolution
of the state of these variables along
the time okay and then and you record
these State Evolutions okay and this is
what we normally refer to in execu trace
this will be very relevant in order to
prove it correctness and then on the
other side you have what we referred to
as a transition function which is
basically a set of rules that these
computations has to OB for example you
can enforce that the computation on the
variable a has to start at one and B has
to start at seven okay you can also POS
restrictions on the very same state for
example you can say that a plus b is
equal to Tod along all the states you
can also say for example restrictions
along the continuous h States for
example that c has to be also has to be
always equal to to a of the previous
state okay and so on and so forth
basically ER linguistically speaking is
a set of rules that the developer think
of in order to compute a
computation okay then we have the
process of winess computation which is
basically trying to find a set of values
that satisfy such
rules F and finally and because uh
commutations can be described in in very
very different manners we have to find a
way a language to describe it in a in a
common way okay and this is normally
referred to as lization basically
finding the correct set of constraints
that describes the transation function
of the
computation okay now if we will go a
little bit beyond of this basic problem
let's say that we are posed with a
problem of trying to
artize thing like an evm
okay this is far from being something
trivial because in the evbm you have a
lot of components you have an storage
you have a memory you have Artic
operations you have memory operation you
have a lot of things and you have to try
to artize them all you have to find the
right set of of
constraints okay and the na solution of
this problem is okay let's try to do it
okay let's try to find a set of
constraints that enforces not only
arithmetic operations but also memory
operations but also uh input data
management and so on and so forth okay
and then we soon realized that trying to
do it as a whole is a very very complex
problem okay artiz in all these things
are far from something trivial okay so
we needed to find something else we need
to find a new tool in order to do
that and the tool the thing that
unlocked the on the of the evm was the
concept of of a Bas okay which basically
allows you to break down the
deratization
in different components okay so it's
very natural that if your computation or
if your component has arithmetic
operations you have a dedicated set of
constraints only ensuring the
correctness of the of the arithmetic
operations okay the same happens with
the memory with the storage and so on
and so forth okay then you have all the
components IND individually being proven
and then you need something to prove the
relationships between these components
okay and this is the vas okay with the
vas you basically
if you are for example in the main
component and you want to perform antic
operation you basically assume and you
have and you giving some inputs you
basically assume at the you basically
assume these inputs and you throw them
you throw this data to the Bas okay with
the expectation that at some point the
currect component if you have done so
for sure will take these inputs it will
compute the output and we'll check we'll
give you a proof that this computation
have been done correctly okay so from
one side you have components throwing
things to the bus this is what we
normally refer to as assuming a
computation from the other side you have
other components taking things from The
Bu okay taking things things from the
bus and trying to prove them this what
normally we refer to as proving
something to prove assume versus
proof okay this is very abstract so
let's see let's see an example let's see
the different ways that we have come up
in order to manage the bus or to throw
things to the bus for example you can
use the Bas to try to prove a
permutation between those two two
components because for example you want
to ensure that the memory operations
that you are doing in the main component
are exactly the same as the ones that
you are proving in the memory
component you can have lookups for
example because you may be are doing the
same arithmetic operations many times
and you want to prove it so you will
find it many repetition of this
operation in one site but you want only
to prove it
ones and there are a lot of more variety
of of ways to throw things to the bus
for example you have range checks you
have connections you have whatever you
basically okay but anyways with this we
were able to H divide the invation in
many components but the animation was
more or less easy I would say and then
you basically generate a proof of all
these things not only of the components
but also of the correctness of of the B
let's say okay and you generate this
proof and what you normally will expect
is that you have a lot of traces all of
them filled with meaningful values and
then you prove it and then basically
you're proving the state transition of
the evbm which is the original objective
but then then after after trying it with
very different inputs coming from
different kind of transactions we
realized that the reality was completely
different okay the reality was that we
had some components that were totally
meaningful were totally filled of
important values but then there were
other components that were not even
filled for example U because because the
size of the Tres has to be the same
because we are generating a proof of a
whole trace the
arithmetic the component was was not
even used H the in the average okay and
for example if you go to the extreme
case that you are designing a specializ
foron for special cases or specializ
operations for example when you want to
prove the cor of a pting then we
realized that this component was
totally Unos okay so we needed some way
of fixing this
problem and the way to fix it was the
introduction of B
cops okay now uh things will be
completely different okay we are we will
not be again trying to generate a proof
of the whole thing once and now the idea
is that you could adapt the armatization
to the size that you would like to to
have for example if you expect that for
the your use case you are not using
thetic too much but you still need it
you could design a imation that is lower
in size okay the same happens with other
different components and then the idea
is instead of generating a proof of
everything we generate a proof of all
the components
individually and for sure we also need
that this proof takes into account the
relationships between all these
components because the relation are
still there okay so from one side
agregation from the other side
consistency okay so let's let's go
through an example let's say that we
have the main component and the Artic
component different sizes specially for
our needs and we want to prove the
relationship between these
two okay so what we normally do is we
compute what we call an aili Trace
beyond the original trace the main and
arithmetic okay then when we do an
assume ER we accumulate this value along
these actually tray and the same holds
for the Artic okay and at the end we end
up with a with a value that we normally
refer to as an a grou
value and Beyond proving the correctness
of each component we will need to prove
that the resulting value is the same in
both sides okay achieving the fact that
they are related
correctly okay for example if you are if
you are with a problem of proving a
lookup and you're using for example the
Lo up protocol okay H we what we do is
we are going to be accumulating the
fractional sum of all these of of of the
both sides of theary Trace okay and at
the end I'm for sure you will have
constraints ensuring that this
accumulation Hub is done correctly and
this we at this still will be proven in
the let's say the basic proof and then
you will need to prove outside the
individual ones that the two values that
you end up with are completely are
basically the same okay achieving the
lookup H
check okay if we go a little bit on the
details of this aggregation and this and
these constraints and these proofs okay
this this is the in this diagram you you
see what is normally a circuit for
agregation aggregating to independent
proofs okay so the logic of this circuit
is basically a copy of the verifier
logic okay and you give it it expects
input for example public inputs dation
type the proof and so on and what you
expect that the the verification of this
two circuits is successful and then
generate a proof of this statement okay
this is a traditional independently
proven aration
circuit okay but now we are going to
enert is logic only to deal with the
dependence that this
proof have underneath okay we are going
to be giving it the Air Group values the
accumulated Air Group value until this
point then the circuit instead instead
of just saying if the proof is valid or
not they will also generate their a
group values their resulting sums that
doesn't matter if you lookups
permutation and so on the resulting sums
and then we are going to the SE itself
is going to aggregate these group values
and it going to be and then it going to
speed out as an output not only the
proof but the a group values okay and
then at the end of the at the end of the
aggregation the the last the last
aggregation circuit will ensure that
that the sum or the aration function
doesn't matter if it's a sum or not
matches okay as in the previous
example okay one one of the the things
that we need to to solve is the
scalability uh I was explaining before
scalability can be uh you can see this
in in two ways one is the high
scalability I
produce different um on different uh
machines specializ it that means that I
can solve the problem with a specific
machines okay um but but it's only one
type of scalability okay it in this
scalability I can use the different
number of the different the machines but
the problem is that I need to to add
something this is the this is the part
of the horizontal scalability the other
is related to the vertical scalability
that means if we analyze the different
type of the the state machine that we
have there are the typical single
machine that means that only one one
instance okay example the Rome that
would has the the the correct uh
instructions that can be uh exed another
another are the in uh the machines that
are s independently that have
independencies no have no constraints
between the differ SL that can I do I
can divide this in
horizontal I can put this in in in in
any place not have a problem because not
have relations uh between these machines
I I prove the different binary
operations okay but each proof is
independent of the other okay
but there are another that have some
relations between this or for example
the memory or the main because the trace
one row depends of the the previous row
okay something what can you do uh we put
some relation between the end of the
first the end of one stage uh of one
instance one segment to the other okay
and we need to link this in a correct
way
we use whereb who make this okay we we
use the same concept that Hector
explains before when you start a segment
you assume an an an initial state that
you put in the in the in the in the bus
and when you finish you prove that this
assuming this initial State you finish
with this state and you put this in
inside the bus
okay with this you you you can add any
uh instances any ex segments of the the
the main of the memory that you want
okay the only is the this relation okay
this have an uh thing that we need okay
what we R this start with one state and
finish with with this but we need to to
to broke this this relation because
really the initial state of the program
cannot be the the fin
Pro stage of the program for these
reasons there are a global constraints
uh that defines this relation using the
bass but in a point of view of the
global constraints that means that you
define with a global constraints what is
the the initial state for example what
is the PC now the boot address or what
is the the values of the register that
do you want okay and after you define
who needs to be finished this program in
correct way okay and this put inside the
bus this are a very a very useful uh
instrument because there are another
problem when you use um cycle machines
in the security problem that you can
repeat the cycle times and you got if I
close close this cycle that means that I
can add two different cycles and this is
not a correct execution of the program
how you put this in the in the global
constraint you only have produced One
Time the cycle because not have any
things in the bus to start a new a new
to allow to start a new cycle
okay okay uh as a summary uh the
continuations uh is something that
assumes an an an initial State okay and
and pro the next it's important that
this this continuations is different the
other continuations that use a big uh
numbers so use H one for uh for all the
machines this is individual for each
machines that means that I design a
machine i c that have relation ship
between the rows I don't have problem to
cut only do be use this this this um
discontinuations the initial and final
State I have full control about this
that means I can execute for example two
Mains with different program because I
can put in the in the in the the global
constraints the beginning and the end of
the different of the different uh
machines I have fully control of this
initial State and fin the other thing is
is we have an an an idea to produce an
an air value what is what is a value
when when when we think in the trace we
think in the rows okay but when we
thinking in the state of the instance
really don't have dimensions of rows
because not is the the the state at
initial or the state at the end no need
to to fill and row with these vales
because you not spend a lot of for put
this and this means that that we need
the air valal the AAL is something that
is only is common is inside the the the
the Hing stance for example what is the
beginning PC or what is the NPC what is
the segment ID something like that
okay and it's very cheaper because noce
something that applies all the rows
okay
uh okay uh how how these constraints
really this a Val you have an relation
to directly the specific row of the
constraint for example I say the PC P
say must match this a value related to
the beginning PC the first value that is
in the trace of the PC that this is the
relation who fix the vales or who
constrain the vales that have these air
vales
okay um this give to us an a tool to
Define to Define uh a trace that as we
want not not the limitations when we can
put put good good and put the different
the different things to the B using the
same performance BS not using anything
it's a like way to to to do this these
um continuations okay
and the same way that we use in the main
you can use for the memory okay and you
don't pay any cost for the other
machines for the conation because you
don't need okay or
Ms yeah well as you have seen uh there
were many Concepts that we try to fit in
within a 20 minute presentation we are
using all of these H to build the you
can check out the repository and see
that all of this is not only Theory but
it has been implemented in practice just
check it and try to understand it and
well epic phrase at the end uh yeah
thank you very
much thank you so much both for the
great presentation so um reminder to the
public that if you scan this code uh you
can uh visit the session in mcut and
that allows you to ask questions vote
for questions and also collect nft about
the session so yes uh I think right now
we only have one one vote so let's start
with that one if you were a time
traveler would you prefer better
architecture for evm to make it more CK
friendly and yeah maybe you can expand
that and me precise what what if
so yeah yeah yeah I mean if you see the
history the the the the people that
designed the evm at the
beginning reject or at least didn't
expect the world to be that g friendly
at the future and I'm sure they will
have designed some things differently at
the at the at the moment that they
design the ebn they will know the impact
of these things and the and the use
cases of GK and general okay just keep
in mind that when the when ethereum came
out there were not even papers that make
snar or GK in General ER pable and let's
say practical okay so yes for sure I
will make it more but I will say that no
one El at that time was able to predict
that that impact of GK in general one I
think is important to say that that all
the things that we have a lot of
improvement that we breaken some some
froners that we have Rel we make the zbm
and we found we alerted we have a lesson
learnet about about this is important
because we we see what what we need for
make more big things
that's the luxury of hindsight hindsight
right the next one thank you for the one
who asked what are the implications of
beam chain e 3.0 that was discussed
yesterday I don't know if you if if you
saw it or heard it as it relates to
CK yeah so I mean related to our talk
it's clear that at least we are using
all that we have described to build a
zvm and it was clear from Justin Justin
talk that gkbm will be used in many many
many places in three 3.0 in particular
in the consensus part so I mean I will
not say implications of the V chain to
GK but the other way around the
applications of the evolution of GK to
the vam
itself great please Round of Applause
thanks so
much and with that I want to remind
we're going to take a break for 1 hour
break so if you are into applied
cryptography please come back at 3 P.M
we'll be here we're going to have a
great uh set of panels and talks so yeah
have some good lunch food and hope you
enjoyed it thanks
e
is
for e
that
welcome everyone back hope you had good
lunch hope you have a good break so just
for this new block um just introducing
myself again I am Andy I work a product
at PSC I'll will be your master of
ceremony for this part until 6:30 so if
you like apply cryptography stayed here
we're going to have tons of great stuff
um so just to remind quick things uh
remember that when a a speaker is
talking there's always going to be a QR
codee on the left and that's where you
can submit your questions and you can
also claim an nft um that you have
attended this talk so I recommend that
you go in submit your questions also
like questions or vote if you want one
question to really be asked to the
speaker because that those are the
questions that are probably going to be
prioritized so for this next session we
have Don Beaver with an amazing great
title which is called the suprema ruler
of the world where we're going to go and
go into basic math we'll see uh to
understand better more about some Che
and succk so please uh join me in giving
a run of Applause and welcome Don
Beaver thank you so much thank you so
much for that nice introduction I I did
actually go all out to try to make this
the best title ever or if not it's at
least a tribute um what I want to talk
about today just to give a level set is
zero knowledge of course uh this appli
cryptography track um it's intended and
directed at people who have a little bit
of knowledge about uh cryptography a
little bit of knowledge about zeron
knowledge but are basically mostly uh
developers interested in finding out why
B doing this and what is actually going
on behind the scenes so uh without
further Ado um I'm going to talk a
little bit not too much metaphysical or
uh or mystical but more about how do you
get calculations done by powerful
entities and how do you trust that those
results are actually true uh when they
when they get hand something to you uh
this is really the realm of zero
knowledge it's actually a bit broader
zero knowledge and verifiable knowledge
there's a lot of different properties
that are important they're really
important to scaling things up on the
blockchain any kind of blockchain in
general and uh I'm sure many of you will
have seen a lot of Buzz around uh these
topics as well so what's the buzz about
how does this actually work uh what is
what is going on behind the scenes at
some reasonable level um in general I'll
do quick background so zero knowledge
proofs or interactive proofs are ways uh
uh for a computationally limited
verifier a client to actually ask for
the truth or or or falsity uh ask for a
a claim to be made and for somebody to
uh with a lot of power to give them a
proof that that claim is is true so for
example uh some of these problems might
be complicated like hey I know a Sudoku
solution and you know a 9 by9 is not a
big deal but n byn is actually an NP
complete problem to solve so these are
actually intensely uh uh complex
problems that people work on and and try
to demonstrate the truth of uh more
practically you might be looking at you
know consensus algorithms and saying hey
look I can tell you that I checked
out uh you don't need to bother so trust
me well in this setting we don't really
want to just trust people we want to
actually verify what's going on okay so
that's the that's the setting the the
the scalability argument here is that
one person is going to do the work and
everybody else can just sort of check
after that one person did the work okay
so for example what did the consensus
say I checked a bunch of signatures uh
you know did did they all pan out uh
what's the new state on maybe on my own
chain or on somebody else's chain uh
that's a lot of work to do if you try to
do that work inside of a contract it's
going to be very expensive uh if
somebody can do that work for you
outside of a contract and just prove it
to you in a contract that helps you
scale because it's a much cheaper thing
to check than it is to calcul calate and
so in general these things help us scale
with things like rollups with other
chains with uh with uh exchanges and so
forth anytime you have a a big
calculation that you want to uh land
just the result of on another chain uh
we'll use these kind of results so all
right there are two kind of very uh
closely connected problems here uh in
order to motivate it I mean really we're
going to talk about uh proving a
calculation here which is the middle one
uh it's we'll look at a couple tools one
is called sum check it's actually kind
of a very old play on words when you're
sending a message from A to B you do a
check sum to make sure it wasn't
actually munged in the middle uh some
check is a way of getting a calculation
from A to B and making sure the
calculation wasn't messed up that the
result that you get is really true um
related to this is something you know
I'm calling some Cal which is how do you
delegate a problem to somebody else and
get them to calculate it for you you're
a contract on chain you ask somebody
offchain to to do the calculation so
very uh very related very related math
behind it um uh you know and and then
we'll go into a little bit of the math
and see what helps us scale uh uh uh
these these different algorithms okay so
uh what's really happening here what is
the supreme ruler I'll get to it more in
a second uh it is basically a trick that
helps us look at very very large
calculations essentially exponential
siiz calculations and use like a
moderate amount of checking to see that
they're whether they're true or false
all right you can scale this down a
little bit you can say maybe I have a
human scale EP calculation and I have a
very very tiny verifier that uh that
only uses logarithmically many steps um
I won't get too far into the Weeds about
the complexity of the heory but but
really if you want to think about it
concretely you got a million step
calculation somewhere and it takes you
maybe 20 sort of questions of this
prover to actually make sure that the
prover is behaving and the claim is
actually a true claim all right so
that's where we're going to go we're
trying to get to this industrial
applications of ZK so we can scale up
things on blockchains all right so brief
in interlude uh from our sponsor this uh
talk is brought to you by the number two
okay so the number two is going to
appear a lot of different times today uh
let me just give a quick outline of of
many different things that we'll see
sort of a duality in we'll look at a
ruler we'll see where does that ruler
become a supreme ruler we'll look at
checking and delegating and they're very
related and the tools that work uh in
one will work in the other
we'll look at small scale and big scale
look at slow Computing like onchain
Swift Computing offchain what I just
said gas powered Computing versus CPU
Computing uh the aim of this talk just a
level set is to uh you know in the days
of like hey what was htps I want to know
what TLS is should I use it uh what's it
going to do to my performance Etc what's
all the buzz about that's the level here
I'm not diving too far into the crypto I
hope the crypto cryptography uh keep me
honest if I do uh this is a talk about
hey if you're a ZK VK verifiable
knowledge adopter what's a little bit of
the math that goes behind behind it what
is kind of the RSA flavor of that is it
not a talk about uh how to become a ZK
evm uh developer for example uh it's how
to use these tools and what what
actually uh gets us to the scaling uh
going to try to really hard to stick to
non-mood math I'm going to uh talk a
little bit about how you start with line
and turn them into something that is a
multi-linear this is the real essence of
the math behind most of this and I'll do
some geometry for that uh and take us
from an ancient kind of Jurassic age of
of of checking things into what the
Modern Age of really practically
checking things is and how that looks so
all right Jurassic as I said long time
ago 35 years ago U let's start okay with
sort of an everyday ruler now I am a I'm
also a dad and additional to being a
researcher so uh we're not talking about
rulers that command the universe uh
although the origin of this word is
pretty much the same rulers are things
that help us do uh do things like
command more of the world so if you have
a couple of points from second grade you
learn how to actually like draw a line
between them okay so you draw a line out
sorry for people in the back if you
can't see that but you can actually
extrapolate and get new points from it
so normal ruler does things like that
what else does a ruler do the second
thing ruler aligns things okay it's
really important you know if you want to
make sure that everybody is in line or
that all your data is in line that you
have a straight edge to actually line
things up so this is a tool that helps
you detect if something is out of line
This is actually the basic mathematical
idea behind most of the the or a lot of
the verifiable knowledge uh protocols is
actually just looking at lines and
seeing whether things that are claimed
actually line up so I'll get into more
of this in a minute that's just kind of
the geometric uh backing for all of this
for what's going on okay so we'll start
with a we start with kind of a basic
ruler and we're going to get to
something that is in larger Dimensions
kind of this sort of hyper cubeish
looking thing that is going I'm calling
a supreme ruler it is a larger scale
version of a
ruler okay so let's rewind a little just
to set the scene to remember kind of
high school math a little bit here if
you start with a table and you want to
draw a turn it into a line may make may
make a linear extension of entries in a
table here's where we go with it okay
this is just just a refresh memory okay
you have some inputs maybe a one bit
input it's either zero or it's one you
want to draw a line through it the the
GE geometry that we just saw uh a moment
ago so here's what you do you draw the
line okay it's nice if you have a
calculator to do it uh but the technical
part of this and and and we won't go too
far much too much deeper than this is
that the nice trick to doing this it's a
little bit of high school math as well
is we can use two really nice helper
functions is x equal to Z the is x equal
to Z function is just one - x on one bit
inputs okay I'll let that sit there for
a second 1 - x tells you yes or no is x0
and likewise you know this is this is
hopefully relatively simple high school
math at this point is x equal to 1 is
this equal to one function we're going
to use these okay in building up what
the extension is and there's a reason
I'm going through the basics we'll we'll
grow it out in just a second um if you
say this is basically a short program
here to say hey if x is zero output
three if x is one output seven okay so
these are kind of one hot functions
they're only they're only going to be uh
nonzero in certain cases and so this is
how you interpolate a line pretty
straightforward Okay add them up you get
a linear equation and that's you know
that's really what we just saw so that's
the algebra side of it okay so this part
hopefully is is straightforward I'm
going to jump into cryptographic
motivations for this uh kind of related
Pro problems that are related to zero
knowledge zero knowledge is a claim uh
that you want to prove there are also
things like delegation which is I start
with some input here 0110 and I want to
ask the cloud to actually help me
calculate some function of that okay
so all right the the the key thing here
is that the cloud is not supposed to
learn what you're trying to compute it
might be your tax return it might be
private inference that sort of thing so
it's a very related to zero knowledge
problem it has the same mathematical
solutions to it uh but it turns out to
be a little bit easier to to address uh
and to find where these tools work okay
so you send a message it's a little
garbled you get a message back from the
cloud and from that you're able to kind
of figure out what you were really
interested in in the first place okay
here's a sort of silly way of doing it
for like a line if your function was
like a line not not very complicated
function to compute but you can say hey
server tell me you know what was F of
five up here hey server tell me what
what what is like f of four and then
you'd go home and you say thank you and
you draw a line and then the server
would have no idea what you were really
interested in were you interested in
competing F of zero were you interested
in Computing F of one but the point here
is that you can actually do it okay so
that's a a trick with one
server now to some degree it's sort of
like why bother doing this it's it's a
lot of work for nothing at all you might
as well just done this uh at home in in
in the first place but we're going to
grow this uh and it turns out that if
you grow it in a certain way using this
multi-dimensional ruler you actually can
actually delegate uh delegate uh the the
query to a server privately uh and
likewise the same tool works for for ZK
as well okay so the shape of what we're
going to do is we're going to look at
things that are like hey points on a
line and you know uh if you actually uh
if you start with setting two of these
points on the line you will determine
the values of all the other points on
the line okay uh we'll expand to higher
Dimensions set four points on a Boolean
value square here 0 one Z Etc 0 01 one
Etc uh grow that from there and we'll go
to larger dimensions and it turns out
that at larger Dimensions we actually
get some payoff in this and that's where
the compression comes in that's where
scaling comes in the cost of going to
large dimensions actually uh there's a
trade-off that works really nicely there
okay so I said a little bit about going
back in time let me try to set the
motivation here a little bit to
generalize from like the one server case
to a multiple server case okay there was
some nice work in the 80s done on this
that said for one server you could
actually do calculations like this but
there were kind of very limited
calculations it got generalized a little
bit later on to saying what could you do
if I have a tax return and I want to ask
you know Amazon and and Microsoft and
Google to help me with it but I don't
want to reveal the tax return so you get
you get answers back from each of them
and you and then you're like okay I I
know what the the result of my tax
return is I I owe $5 or whatever in this
case okay so geometrically we take the
case that was like before um except now
we have different servers giving us
answers so in just a linear case might
go hey Alexa tell me what is uh you know
F of four hey Siri tell me what is f of
five and now having gotten those answers
back to some maybe some very complicated
uh calculations we can extrapolate
ourselves to the places that we're
really interested in which might be
something like if we are trying to find
F of one okay so you're going you're
asking for something on a line and
you're getting answers uh back for this
uh calculation and then you're able to
figure out what it is you wanted to
calculate okay so it's all drawing a
line like I said um I will take a very
brief detour here this is not that
important uh but it actually is part of
the trick if you want to look at this
later uh that's fine but there's a lot
of polinomial going into this so I don't
really want to uh spend too much time on
this but if you secretly share you can
actually go for those of you you know
who uh know multiparty computation and
secret sharing you can actually scale
this up to many many other parties and
then you're not just inter ating a line
you're interpolating something that is
of degree n to get your answer out uh
okay but that's as much as I want to say
on that because that's like maybe a
little too much into the Weeds on
polinomial okay here's the the core
trick this is what happens and gets
skilled up in zero knowledge it what
happens in in in delegation you actually
a go out and ask for uh these Cloud
servers to calculate a sum of a huge
number of things two to the end things
now the cloud is fine to do that for
some moderate end you as the client are
not bothering to do all that work uh
you'll get some answers back uh after
all that work is done in the cloud and
locally you don't really have to do very
much locally as the the the the the weak
client you're really just doing some
kind of like a drawing lines
interpolating a small polinomial over
here size n kind of calculation the
servers the the clouds are these guys
are doing two to the end calculations so
there's a big scale difference here
you're getting a lot of work from provs
lot of work from uh from delegates the
flavor of this the compression that
happens in all of this that that that
powers all of this is that the weak
person the one who has just gas on a on
a chain is doing a map reduce of size n
adding up N Things compared to work
that's being done offchain or or by
complicated servers that's on the order
of 2 to the N so here let's you know the
the the the kind of cool thing here was
uh is that you can delegate really com
licated answers uh and and using this
this this supreme ruler in a sense okay
so I will skip through a little bit of
the history in interest of time uh this
stuff got uh um discovered back well I
missed a punchline here this stuff got
discovered back in 1989 most of this and
it's now being implemented on chains uh
other kind of important things happen
there and it's kind of relevant um is
that this was the kind of the era of
Swift Computing if you like this is
where we we could speed things up by an
exponential factor sorry about that um
said dad jokes here um we are here now
doing things like sum check you'll see
things like uh hey I can do exponential
calculation offchain uh and and and and
get things checked in uh normal linear
time on chain uh that's really what's
going on here uh there's a kind of a
very very uh strong relationship between
the the the the delegation and the and
the and the cube okay I won't go into
the details of this this is a this is a
little bit uh it starts to look like uh
you know uh category of end funter kind
of explanation of the math that's in
here um instead you know I said no moon
math trying to be honest about that back
in the day this was the interesting
thing about this theoretical development
that you could take hyper cubes and then
squash them into like linear
calculations I'll say how in just one
second but uh kind of missed the mark
you know no wanted to do the moon math
in 1989 uh the New York Times said wow
there's a lot of research going on here
uh you know what's interesting well
we're not going to publish the moon
maath in the New York Times we'll just
say what's interesting about it so the
reason I'm talking about this here is
that well in 2024 it's kind of the same
thing you don't need to know all the
moon math necessarily but there's a lot
of hype around ZK and it's kind of nice
to and what I want to do in the next
couple of minutes is just go into the
details of that you know without that if
you the the really fascinating thing
that is not completely moon maath is
that hey with only 20 questions you can
pin down a calculation of a million
steps okay that's the magic okay so I'll
try to do the magic quickly it looks a
lot like the beginning where we had the
high school math we'll go from one bit
inputs to two bit inputs just to start
and so here's some random you know table
that you might want to compute this is
maybe a machine learning algorithm
output or something like that okay well
we do the same thing it's a program it's
a program that is a switch case
statement if XY is 0 0 output 5 if XY is
thing here is that well what do these e
equality uh Checkers look like well if
you want to check if x is zero and Y is
zero you use this function which is 1 -
x * 1 - y okay that's the one hot
function that is only going to appear
here in in my lookup uh once under this
condition and when you look at this this
is a term that has four this is a
function that has four terms in it uh
it's kind of exponential already it's
got four monomials uh but the is linear
in X there's no like x squared or
anything like that it's linear in y
there's no y squ or anything like that
the largest degree that you see here is
two kind of the XY that's in there so
it's very low degree all right
generalize this you can do this at home
it's you know you get a you get a
interpolated result here if you look at
the wall of of of latek you know this
actually expresses what really the
bottom line is is that when you try to
do this interpolation you get two to the
N monomials so you can actually Express
something that's really really
complicated but the maximum degree in
this is only a degree n so it actually
turns out to be easy to be for verifiers
to check because of that low degreen
you're only just kind of looking at that
low degree polinomial you're only
looking at lines but the servers or the
provs are doing intensely uh uh uh busy
calculations in this okay so picture uh
hopefully worth a few thousand words uh
starting with two values we looked at
two points on a line and these two
points actually really constrained all
the other values on the line and it
means if you do one of these shell games
let me pick a few of these points on the
line and see if they are consistent uh
you only need to ask for one or two
probes on this step the dimension up a
little bit and you've got four values
for two bit input two bit X and Y how
many probes do I need here I need kind
of maybe two or three probes okay this
is where the scaling actually happens
it's that when you try to encode a
function with eight values using this
multi-linear trick here I don't need to
do eight probes I don't need to do the
whole thing I need to do just maybe two
three or four probes to actually get
this to work okay that's kind of where
the math comes together it's what
happens in the zeron knowledge it's what
happens in the delegation in so forth
okay and in general you know we sorry
for the Universe I have to apologize
that we can't draw you know two to the
end values up here but when you're
trying to uh scale this up you get a
huge blowup in in in the power of the
checking and to be concrete again if you
have like two to the 20th values you now
only need to ask sort of two 20ish
questions it's it's a real explosion in
scale so that's the flavor of like the
basic trick that happens in a lot of
zero knowledge uh so that when you're
actually asking your you know asking to
verify something on chain this is why
you can get away with something that's
very very small okay so let me let me
just finish uh with this last slide or
two uh zkv Ms uh what are they doing in
general a typical pattern is you run a
program for a million steps you write
all the values of the trace of that
program on a hypercube that's you know
this this is a you know it's a it's a
computer easy for a computer to do uh
you've got your your million entry table
that says all of the steps of the
calculation and so the flavor of this is
to then build a proof around that and
because of this like Dimension
relationship here you only need to ask
like 20 Questions instead of ask asking
you know a million instead of inspecting
everything everywhere so that's that's
really the magic of it okay so if you
really want to do Z VMS there's a lot
more you know of moon maath here that
I'm skipping completely uh if you feel
nerd sniped feel free to go look at it
uh we're not getting into any of that
this the reason why these things are
hard is that there's more other more
stuff to to it than than just that trick
but this trick is the core of why the
compression works of why compressing
million steps down to a 20 step uh probe
is is is is is feasible at all okay so
that's it quick summary is history you
can look at this later if you want but
the real interesting things here is that
we started the area era of kind of Swift
sound computing 35 years ago if you like
uh we move forward now and we're finally
going from an era that was purely
theoretical to an Era where it's all
applied and we're now industrializing
this we're building programs that can
take a a million step calculation and
check to make sure that that that
actually is valid okay picture million
is what you get for the cost of 20 and
that's it thank you guys so
much thank thank you thank you Don
Beaver indeed a great presentation with
that jokes included and Hyper cubes and
multilinear and multi-dimension so
remember that we have uh this QR code
where you can input your questions and
the questions that were more voted are
more likely to be uh answered so to
start with the first one is there any
value to asking more than 20 questions
is said a high level higher level of
security uh or certainty yeah no this is
actually this is a perfect question I I
wish I had planted it there's there's a
really subtle Nuance in this um the 20
relates to the dimensionality and it is
not that asking one question or two
questions is is is worse or asking 40 is
better if you think about a line to
determine a line you need two questions
asking four questions on a line isn't
helping a lot so really what you want to
do here is to ask the 20 questions for a
another shot at it you might have a
chance of cheating the first time with
questions and we'll set the whole thing
up again so the the going from 1 to 20
uh you really need to get to at least
the 20 uh to to start off with great
question great question yeah thank you
awesome right any other
ones you can input if not please join me
thanks so much and uh yeah big round of
applause
amazing great thanks for the short break
hope you you're ared we have the next
speaker Alexander Belling he's going to
talk to us about uh wizard which is a
new framework in order to build newer
proven systems CK proven systems and
it's been used in Linea and it says like
we can build uh our own P IOP in less
than 15 minutes so we'll see if we are
able to see and do that in this talk so
welcome
Alexander some Applause
please um uh so hello everybody uh so
today I'm going to present to you uh the
tech we developed to develop the proof
system of linear linear actually use
many many different proof systems for
many different use cases it's it is a
complex system what I'm going to present
to you is uh the one the main one that
we use for proving the execution so
concretely proving evm
execution so uh I should present myself
I'm alexand uh I've been working in this
space for seven years now uh and being
focused on cryptography for 5 years now
uh I've been working on Linea since the
beginning even and doing research on
rollup even before that uh and so yeah
just to talk a little bit about
myself okay so uh uh I'd like to involve
the audience a little bit who knows uh
What uh zvk evm
is all right so that's a good half a
good third um so a VM layer is uh a
layer two
solution uh which is whose purpose is to
help ethereum scalability the idea is
instead of sending transactions on the
ethereum main net you send them to a
third party linear linear runs uh an
ethereum virtual machine will process
the transaction it will be processed
separately from the main net so the
contracts that are deployed on Main net
are not the same this isar really the
same as the one that are deployed on
linear the state are
separated uh but we can bridge between
the two I'm not going to describe much
more how we bridge between ethereum and
ler uh but what is uh important to
remember here is that we basically
bundle the execution of many transaction
and submit one proof at the end we give
you one number uh every finalization
finalizes on average 65,000 transaction
at once
uh and since uh we are using snack proof
systems meaning they have a very short
very time which is mostly independent
from how many transactions are executed
that's how we get
scalability verifying uh the final proof
which is a plun proof Tex a few
milliseconds but it's for 65,000
transaction so that's why it's much
cheaper and that how uh the kvms can
achieve much lower gas price
all right uh so maybe a few word uh on
um on zkp and SN zkps uh I mean usually
we say zkp but most of the time what we
use in production are ZK argument of
knowledge uh and in order to for a
protocol to be a ZK argument of
knowledge it needs three property you
need zero knowledge zero knowledge means
that the proof does not reveal more than
what it should reveal you need to have
completeness meaning that if you want to
prove something that is true you should
always be capable of generating the
proof meaning for instance if you want
to know that you prove the square root
of some number it should work for every
number and not just your favor just just
one number and the most important one is
uh argument is knowledge sess or
essentially computational knowledge sess
it is how you say that you know that you
prove that you know uh what you're
proving you
know um and so as I mentioned earlier uh
we are building a zvm but really the ZK
is not it's not about zero knowledge or
hiding things it's really about proving
that we know valid execution traces
we'll expend more on that later uh but
especially we need more properties we
want the verification to be suent to be
small and we want uh also uh the
verification the protocol to be non-
interactive it should be a single proof
a single message and from that we should
be capable of verifying uh
approve okay so let's apply all that to
uh the evm uh the etherum virtual
machine is a state
machine uh on which we can execute code
uh and a transaction in zvm is like an
instruction from the user
uh of that virtual machine uh it has a
lot it is specialized for running smart
contract it has a lot and a lot of
features and a lot that interact in a
complex way between each other and uh
and not every computation that are easy
to do on the evm are necessarily easy to
prove so for instance I'm thinking about
the kak crash function that a very smart
contract uses all the time like it's
free uh it's really not free to prove
um and and so if we want to solve that
problem uh so of course we need to deal
with the inent complexity of the evm but
we also need a proof system that is
flexible enough to solve all the problem
that we need to solve to execute the
evm
concretely um in order to prove the evm
we have traces of execution that are
instantiated by polinomial we call them
colon in our
framework uh and it could be summed up
as a collection of airs that communicate
with each other by sub argument and
there are many different sub argument
that are possible to use we can have
lookups we can have projection queries
uh we also support variant of lookups
that we call conditional lookup or
fractional
lookups um and so in order to make this
work we need a proof system that is
really flexible and can deal with all
the polymorphism that is inherent to
proving uh linear arithmetization
okay so in order to do that we designed
uh the without framework which is uh the
main uh um the main gateway between
describing the constraints repres evm
and actually proving
things uh it has a very neat
particularity is that in the wiard
framework you work you um write
protocols in an ideal model and you
don't have to worry about
how you're going to commit to things or
how which argument you're going to use
you you say what you want and then you
have a list of technique like a menu uh
which you apply to that uh protocol
statement and it will create for you uh
a proof system as complicated as you
need it to be and so that's perfect for
us it turns out that this is how in
Academia they describe uh complex
protocol like if you take for example uh
the grow 16 uh proof system uh if you
had a look at the paper before you would
see that they say okay so this is the
constraint system at the beginning then
we do something that is called qap and
then we do something that is called NP
and then uh in continues and at the end
you have a concrete proof system which
is a grow 16 proof system but that does
not translate into the implementation
people just take the final protocol at
the end that you apply after every step
of compilation of grow 16 H and there is
a Agro 16 implementation so what we do
is that we actually Implement every
possible step so that those step can be
Reus for other proof systems and we
don't have to really mentally work out
with the work the whole
protocol in the case of Lina it would
just be
impossible and on top of that we made it
in such a way that if anybody wants to
add uh their own compilers or do their
own tweak or add their own type of
constraints uh the framework will allow
that without changing the core of
it all right so as I mentioned earlier
the proof system uh the protocol that
you are going to construct uh you have
to describe it in an ideal model and
this ideal model involves what we call
the wizard Oracle the wiard Oracle is
from the point of view of the protocol
designer a trusted third party it knows
everything it remembers everything it
does computation for free it is always
honest it's like something you really uh
if we if it existed in reality we would
not need
cryptography uh so that does not mean
that uh what we build will not be secure
it just means that the Oracle will
concretely be instantiated by something
else in the future as we compile the
protocol so the protocol can also be
described in a multiun fashion I
mentioned at the beginning that we need
non interactivity the protocol s this
out using the fat Shamir uh the fet
Shamir
trick uh it put some limitation it means
that the verifier can only send random
challenges to the prover but that's a
common limitation that every protocol
have nowaday it's very uncommon to uh be
in a contrary situation and so
essentially the prover can use the
Oracle by sending big large message to
it and the orle will just remember and
notify the verifier that hey uh the Prov
did is part of the work you can ask
question uh to the verifier can ask
questions and the orle respond to the
question without needing to do any
computation it's like a Godlike
entity uh and it is always
honest so you don't have to worry about
him
lying so uh as I mentioned the prover
the verifier and the orle can send
messages to each other uh and here comes
the the first primitive of the framework
which is what we call colons so colons
can be of any sort we have what we call
commit committed colon committed colon
means it is sent to the
Oracle uh and basically being sent to
the the Oracle means uh that the prover
cannot change its mind about what was
sent to the Oracle you can only send
something once to the orle otherwise
you're
cheating uh and the protocol will always
ensur that
uh but on top of that we have what we
call pre-computed colums so pre-computed
colums are they can be of two types they
can be sent to the verifier or sent to
the Oracle and uh they are known
beforehand so that's something that is
part of the protocol description
actually they always have the same
values you can think of for instance the
plon uh circuit description which is
instantiated by several polinomial we're
going to see how we can Implement plun
in 10 minute uh so I'm just uh putting
myself forward a little bit uh you need
uh those colons to uh as part of the
proving keys and they describe the plum
circuits and on top of that you can send
proofs and proofs means a message that
is sent directly to the verifier and
there are other types actually we have
eight types of different variant of
colon type so col also have a predefined
size can be one it has b a power of two
it's it's due to a limitation uh aurent
limitation in the
framework uh and they have a r
assignment and the r uh number is
essentially describing at which round of
interaction the colon is sated by the
approver so that's for the main part um
and then as I said uh so for some col
that are sent to the orle or for some
groups of colons that are sent to the
Oracle the verifier can ask questions
about these colons to the Oracle so
that's what we call queries it's the
common term used in Academia uh if you
know about Fri they do uh random
position opening query so that's what
they mean when they mean query in
polinomial IOP protocol there would be
univariate openings in our framework we
query stands for at the same time
constraints uh that would be questions
that have a yes or no answer like is
this value the square of this other
value the answer can always be yes or no
most of the time it is s of as a
constraint uh and here we describe it as
a
query and and so we and we also have
open questions that are like polinomial
opening position opening uh and so this
have uh expect a response for from the
orle that is other than yes or no um so
we support many many different types of
query it can be lcaps it can be uh it
can be univariate evaluation it can be
uh inner product between several colons
so essentially uh most of the folklore
is there and because and we implemented
it because we needed it for the concrete
implementation of Vortex and linear
all right uh so as I said once you have
a protocol description uh the only thing
you need to do is to describe how you
want to go from this description in an
Ideal World with ideal Oracle into a
concrete protocol that is secure in the
standard model uh so here is the base uh
description that allow us to go from uh
with IOP to polinomial IOP at the end uh
but in practice this would not be
sufficient we would also need a
polinomial commitment to turn this into
a concrete protocol
uh so in this part of the code does not
describe how we do the pomal commitment
but how we go to this
point um okay so now let's get onto a
practical example uh so here is uh the
plun uh constraints um description so we
have a set of colums uh cues are
describing a plong circuit XA XB XC are
describing the witness uh and also
usually we add another colon on the
right that is for the public inputs and
that we are going to use on top of that
plunk has some copy constraint uh which
are can be instantiated by um a
permutation argument which I'm going to
show you how to do okay so let's
Implement
plun uh so as I mentioned we need to
Define our protocol then we can compile
it and after we can run run it so
running the pr and verifying it we can
also recurse automatically recurse it
but we're not going to cover that
today all
right okay so first of all defining the
protocol this is done by specifying a
function so the whole framework is in go
most of the pr stack of linear is using
Nar and the linear Pro is also
implemented in go as it is also relying
on gnar's
implementation so uh the defined
function uh has this simple um uh
signature and the is an object that is
going to store everything we said to
declare an entity in the protocol so
either queries colum or so on and we can
also specify checks to be done by the
verifier so let's go into
there okay so here are the colon uh
description uh so you can recognize uh
the plun colon that we saw at the
beginning uh so the CES colon are for
the circuit description they should be
the same no matter what we try to prove
so they go into
precomputed uh the XX bxc are commitment
they have to be sent to the Oracle and
Pi the public input uh is inserted as a
proof object because it has to be
revealed to the prover so it's a bit
cont inuitive that we call that proof
but proof means a message sent to the pr
Comm it is part of the proof even if
it's a nonsense from an Academia
perspective and also a number of public
inputs uh because the pi is po colon is
larger than the actual number of public
input is because every col should have
the same
size so and that's the value of the cues
should be known beforehand of course
because that's the circuit
description okay so now we can declare
the queries uh so on your right you have
the a global constraint which is an
arithmetic expression that has to vanish
uh on the all the rows of every colon
that is touching we can recognize the
equation of the pl gate constraint at
the beginning and we have a fixed
permutation uh which is instantiated by
some forc permutation that has uh to the
concatenation of XA XB XC uh invariant
and that's how PL proves uh the copy
constraints uh uh then finally uh we
need to add a verifier check this is to
ensure that the pi that is sent to the
verifier is well formed and that it
should be paded on the right with
zeros okay uh so now once we have that
we can compare that into an actual
protocol so here I added the part that
convert uh the piop into uh a concrete
protocol because I added the vortex.
compile Vortex being the pomal
commitment that we use and now uh we
just have to run
it uh so the only thing we need to
specify is how concretely uh we are
going to assign our colons because this
is the only thing that is unknown at
this stage after reading the protocol
description uh so yeah we just provide
it and we assign it it's four lines of
code uh and so yeah now so we have some
that allow us to write PL constraints
manually uh but WR I don't know if you
have tried writing a PL Circuit by hand
but this is really difficult uh and it
turns out that garx offers a very nice
front end to write circuit so let's just
write a wrapper of what we just wrot uh
using knar so that we can use AAR
description so I I did the
implementation it was a bit longer than
few automated
stuff okay okay so let's do a circuit so
let's use uh Fibonacci as a use case uh
so my circuit you have two values U U1
as input and you want to have the 50th
number of the Fibonacci sequence
generated by U and U1 U and U1 being
public
parameters uh so on your right you have
uh the circuit rating in KN so you can
say that it's fairly easy and much
simpler than writing a circuit by hand
and then we just have to run it and
that's it you
just create your proof function that is
explaining how to assign the colon you
run wizard.
proof and is going to
generate a proof for you using vertex of
the polinomial commitment and you can
verify that in one
line all right I have six seconds for
the uh future Improvement so we want to
add more queries and we think we can
also remove the necessity for runs in to
specify runs in the protocol as it
should be inferred
automatically right that's it you can
check out the carde
here
yeah amazing Alexandra thanks so much
for for the great introduction of wizard
so uh reminder that if you scan the Curr
code you will attend the session and you
can ask questions and you can also claim
an nft so and you can also vote so if
you have a question that you really want
it to be answered uh vote for them so
let's start with the top one uh does
support local tables and can it be used
to implement uh local tables based on
ckvm uh absolutely so uh the way you
would do it is for instance say um so
what you can do first of all if you want
to do Rand checks so that's a big use
case for lookup table you already have a
range query so you just take one colon
and you say I have this query that just
enforce the whole colon to be within
Bond and that's all you do uh a second
way if you want to do more complicated R
checks like exor for instance then you
would have to specify three colons for
your one colon for the left side the
hand uh the right side and one for the
result and in this colon you put all the
possible uh all the
possibilities uh so maybe say for eight
bits to 8 Bits you would have a color
you would have two to the 16 possibility
so you write down all of that in your
table and then you create a lookup
constraints between this table and a tri
plate of col for which you want to
enforce
exor uh uh constraint and you can also
add uh conditional lookups so you can
have a force colon that say that contain
zeros or one and that activate the the
exort constraints or
not great thanks for the answer the next
question is can you create different
custom Gates and at which instance do
you decide which row corresponds to each
kind of
gate um so when you generate a global
constraint is is essentially what is
your custom gate uh then it's going to
apply over everything um but the wizard
framework is more abstract than this uh
essentially there is a general technique
to do it uh which is to say that you add
a selectors colon that says which
constraint is going to apply uh for each
and you have a some product of your
constraint custom Gat expression
multiplied by uh an indicative that ask
whether this constraint is active here
or not and you would merge everything
into a single Global constraint in the
end so yes you could Implement custom
gauge actually that uh what they do all
the time uh when they specify the
evm great the next question is about
recursion so is recursion something that
would be implemented in Wizard or would
it be separately like the commitment uh
so there separate where you can do a
recursion uh so we do it inside of the
wizard at at the same time and
outside uh so the first way we have a
compilation step that is called self fre
that usually goes just after Vortex that
text a Vortex proof and reari matize it
and we can do proofs of that again and
we repeat and we can shring the proof
that's because Vortex uh as a single
polinomial commitment has a square root
verifier time but applying log Logan
application of self retion you get
constant size proof great and the last
question that we have in the queue at
least for now is uh that it's great that
you can define an ideal protocol
programmatically and it seems that that
does make it easy would would does that
make it easy or possible to support
automated formal verification or UC
proofs of
security um
so I'm not too sure uh what it would
entail exactly to uh formally verify so
we could formally verify uh like the
standard set of compilers that we have I
say this is at least necessity but then
there is a protocol description it
should be formally verified this I don't
know how how to do it I don't know and I
can't tell you how to make it easy but
it would be a great use case I agree
yeah it'll be great maybe after have
that conversation um and I think with
that we cover all the questions so thank
you alexand thank you for everyone for
the questions some Applause uh thanks so
much thank
you we'll back in four minutes with the
next talk so stay tuned
h
welcome back I have a seat cuz we have a
next great presentation so this next
presentation by Leo Jun we're going to
talk about CK evm uh approver
optimizations and we're going to go
through different techniques applied on
the Linea CVM and bottlenecks and
different Innovations Explorations so I
won't tell anymore I won't get ahead but
uh remember that there's a QR code you
can submit your questions while the
presentation is going and you can also
vote for the questions that you like the
most so please uh welcome Leo
hello um it's first time I wearing this
microphone I feel like I'm a k-pops St
now anyway yeah so really nice to meet
you um I'm a I'm Leo Jong i I'm a senior
research engineer at Linea and today I'm
going to talk about how to optimize ZK
EV improvers
so this is the the outline of today's
talk I will talk about the motivation
and also the introduction of this talk I
will share how to optimize zkv improvers
based on our uh one more than one year
of our optimization experience and then
we'll conclude the talk so first time um
so this is the initial Challenge and
problems we had so Linea launched our
main net last year August and we were so
happy so we are kind of dancing all the
time but but we realized that PR was
really slow so we were like what's going
on here uh and um we were spending a lot
of money for approvers so we thought
it's a huge problem and we decided to
optimize it so what we did is for uh
more than one year we spent a lot of
time and effort uh
optimizing PR in production so that
picture that's actually me uh fixing and
optimizing PR in re uh in production so
your production your priv is running
maget and you need to fix it uh that's
what I did but luckily we were able to
uh reduce the proval runtime by almost
um main content that I'm going to share
today first of all uh let's talk about
why it's important to optimize improver
uh the first thing is of course money
this is the one of the biggest the cost
of contributors in ZK rups and pro
optimization directly means you can
reduce the operatum operating cost of
your GK GK project so which is very
important the second the performance
impact so when you optimize z um
approver that means you have less run
time of your approver which also means
you have faster verification and final
finalization and that way you can
improve your TPS right
and you your users will be happy and
lastly you have you can also improve
your scalability by optimizing ZK Pro
because you can support more
transactions which means you can handle
more complex proofs as
well so let me share some common botle
legs here so most zkm provs and project
they have really high complex ability so
inheritant I mean ZK evm
are very um complex because we want to
simulate EVMS right and we want to
provide full compatibility so every
project has their own design um their
architecture so it's really hard to
optimize uh but all project project
there're something in common they have
high resource consumptions right so CPU
and memory they're using uh a lot of CPM
memory and also because to support larg
scale cryptographic calculations so we
have uh these things in common so the
common botle legs is you have CPU usage
and paration issues probably and then
you will have memory overhead a lot and
you will have iio blex because you are
dealing with a huge amount of
data so uh this talk I will uh I will
talk about what we will cover and what
will not be covered so first time we
will not cover linear specific optim
iations because you know if I share that
kind of information you can't apply that
to your project so H so I'm not going to
talk about detailed cryptographic theory
behind our project or ckvm and also will
not share about share uh how do we
accelerated optimizations and we'll
focus on CPU optimizations so here I
will cover some quiick wins and
strategies so you can just pick up and
uh apply to your project uh in in a week
or two weeks or sometimes maybe um on
the flight going back your home uh you
can actually apply that easily and then
I will share mostly on CPU and memory
optimizations without any significant
changes on your architecture or on your
code so that was the intro and we'll
share about the problems right now and
how to actually optimize it the first
thing you have to do is you know you
need to know um your your your code
right so there's a real really famous
and famous quote in this programming
World which is premature optimization is
really bad let's just don't do that
because you know uh sometimes you want
to optimize your code because you know
it it feels fun so you just optimize it
and because you think it's going to be
the bottle leg but most cases it's not
so before you actually start optimizing
your code you need to find out the
problems first and the most common way
or easy easiest way to do that is using
CPU and memory profiling so most
languages they have kind of builtin
profiling tools so that you can
visualize your CPU or memory usage and
you can understand your code there uh in
our case we are using goang we are based
in U so we used that kind of that tool
that profiling tool to visualize our
program so this uh is the CPU and memory
profiling we actually had this is the
whole life life CLE of our prover so I
know what you're thinking right now
you're like oh no I'm going to just
sleep for 20 minutes wake me up in 20
minutes but don't worry yeah we spent a
lot of time so and then we kind of
categorized them for you and we'll share
that uh quickly today so we here you can
see many uh holes or sparse areas which
is white white colored so here the green
color means you are using CPU very
extensively so you're good but the white
colors that that means something's wrong
so mostly it means CPU is underutilized
so you find out which part is not being
used fully and then you go into the code
and you look at the code and you can fix
it and on top of that we have memory
usage patterns and the the main goal of
memory usage or memory optimization is
to reduce the memory picks so first time
I will talk about CPU and then we'll
move to
memory so um you have many different CPU
issues but mostly it's going to be two
cases the first one is poor
parallelization and then the second one
is uh CPU underutilization the first
first panel when you look at this um
this graph here you have CPU number one
to maybe CPU number 100 and we are using
only five CPUs actively and the others
are just doing nothing so we realized
many cases we have these issues so we
had to uh add more parallelization to
improve that uh the second second one is
you are actually using 100 CPUs but
between uh between some run times you
are waiting for something so that means
you are underutilizing your
CPU the first thing so how to improve
parallelization uh this is common
methodology that you can apply to your
program so first thing is you just throw
your modules like like a graph on the
left and then you show you grab you also
draw your dependencies like that and
then on the right side you can have
those Lego blocks and then you can um
find out some better execution
scenarios for example in our case so
this was the issue right now right and
the this module actually was about
reading the setup for the Prov and the
especially proven key we were reading
this from the disk and origin Al on the
left side at V5 had issues of
paralyzation so we Chang this uh this
blocks on the left to the right so we
moved that V5 uh to the early stage of
of our approval life cycle so that the
total runtime of T2 became smaller than
T1 uh the other issue common issue is
CPU underutilization so this has
actually many uh many pro U many causes
so many root issues so the first one
could be poor penalization second one
synchronization issues and lock up
issues and most sometimes you have some
uh blocking IO operation operations when
you're using dis or network so in our
case uh we had this issue in fft and we
we had synchronization issue in our data
structure so we had to slightly change
our data structure so the CPUs are not
not waiting for other
data so after U with optimizing CPU so
we changed our CPU usage pattern from
left side to the right side so we got
one okay cat is happy so got one uh okay
cat for CPU optimization but we need one
more for memory optimization so let's
move to memory optimization actually
more than CPU uh memory optimization is
more important because in General in
most Cloud systems or cloud service
cloud services memory is more expensive
than CPU for example uh you can see that
we our Peak memory usage was 700 gab and
then so we have to use sub machine with
but when we can move from this one to
the other one with 380 gab we can save a
lot of money but we will also we can get
more ches so our plan was let to reduce
our CPU pick memory to maybe somewhere
between 308 uh so around 380 gab so the
goal is flatten memory usage and memory
pick that's the most important one when
you are working on memory
optimization so the first thing we we
did is using memory pulling so it means
sometimes you have many data stru
structures in your approver and some
data structures are being used tens
hundreds of times or thousands of times
and when you just allocate that data
structure every time when you need that
um you will allocate that memory and
also sometimes the garbage collector uh
will spend some some time to return that
memory to the system so instead of you
instead of doing that you just set up
this large memory pool for your data
structure and you just allocate
that and use it and when you don't use
it when you don't you're not you're not
using it anymore you just return it to
the pool and you keep doing this so you
only allocate once and you just use it
and you just return it only once so by
using this one we reduced our memory
pick to 450
GB but still not enough so we use this
mem limit both languages they support
this feature so it's a soft limit of
memory pick so the language for you they
trigger garbage collection when the
memory usage hits uh this memory limit
so in our case when you see here uh in
the inside right Circle we have many
many memory pics but that's exactly
around 307 gigabyte so your your
language or runtime will just run
garbage collection so it will not go up
above like 37 uh gigabyte here so
finally we were able to move to uh the
smaller machine and then but with more
course and cheaper machine but we found
out we are spending too much time in
these specific areas uh because of
garbage collection so we thought maybe
we need to do something more um so
garbage collection is something that
many in many garbage collected languages
they just do it for you right so it's a
very convenient but it's really hard to
predict when this will be uh in this
will and this will happen so what if it
happens during a very critical tasks or
areas of your code this this will be a
huge problem for example in our code
here so we are doing some fft inverse
function over there and it's very CPU
intensive and memory intensive so we
realize that every time when this part
is running the the run time language run
time try to actually run garbage
collection randomly and because this is
really critical in terms of CPU usage
and memory usage it slow down the pro
whole program a lot so so uh we realized
let's manually garbage collect before
entering that critical areas so we
decide to run manual garbage collection
before these critical tasks so that we
have less context switching overhead
inside or during these critical areas
and it actually reduce the runtime a lot
so uh if you have these kind of issues
you you can just manually run garbage
collection before those areas and will
you will get a lot of
improvement lastly um so we felt
everything's okay looks good but
sometimes when you have really large uh
input data um you you will see sometimes
out of memory issue right U and because
we have a very specific size of physical
memory it's not easy to solve that so
sometimes you need to move to larger
machine very expensive machine with
larger memory and then you have to learn
run that but we we we find out this
solution it's called zerm it's a
inmemory swap feature most Linux systems
have this feure and you can just turn it
on and turn it off we all know the swap
space in uh storage or dis right but
it's slow so in production it's almost
hard um it's impossible to use it but
this feature is inmemory swap so this
one if you don't have enough memory this
will compress your data inside your
memory and will just sort that within
your memory so for example over there
you have like we have like 74 740 gab of
memory physical memory but I set up like
actually have a lot more memory and that
fast swap space in your system so we are
actively using this for massive
integration test with terabytes of
memory
usage so finally we got two happy okay
cats uh and let's um I will share
quickly one more optimization things so
one thing is data compression so we
realized the transition data has really
high compression ratio so if you are IO
or network is the botle leg you can just
compress it and for example our case 40
gigabyte of Trad could be um 2 gigabyte
of trace and zero iation is a kind of
time you you spend on initializing your
data so because you we are dealing with
very large data set and very large data
structure sometimes time time taken for
uh initializing your data is a lot so
you you might need to auto
zero iation uh supported by your
language or use optimized library or
lowlevel libraries for zero
iation so let's conclude the talk um so
result we were so happy happy happy yeah
and then we reduced like okay we improve
a r Time by 75% which is good and we
saved a lot of operating cost cost not
only saving the operating C we
reinvented that reinvented that to uh
into our PR system so we increased the
final F finality speed and also higher
TPS and ironically we were able to und
understand what we did and what we built
and what we are doing which is I think
most important
one and some lessons we learned please
uh do not pre- optimize your code unless
you fully understand your code so I
strongly recommend that make
optimizations
only based on your measurement and
instead of doing this with a kind of a
local view uh you you need you need
someone to have a global view so that
you some uh you can set priorities for
optimizations our future work includes
distributed gkv improver so different
modules running on different machines
that means we can run some we can use
some smaller machines to save cost and
then we are thinking about also how do
we accelerate it
provs we think optimization is never a
one-time task so please measure analyze
optimize and repeat thank
see great great great presentation Leo
all right so remember you can always uh
ask more questions and vote for the
questions that you want it to be
answered so let's start with the first
one How could a f CH okay this this is
uh spicy How could a f challenge
Benchmark over same machines and input
be organ organized among uh CK l2s get
like yeah to Benchmark up against
systems um I think it's really hard yeah
I think because I I explained that um in
the maybe introduction because every
team or every project has different
architecture different models different
based on different cryptography so I
think this is just a good research area
I me has been solved yet so yeah it's
hard at least um maybe CPU based CPU
based or some specific cryptography
based that could be yeah benchmarked but
in general it's really hard yeah yeah
yeah agreed would you recommend on Prem
prare or Cloud
Pro um right now I think uh you can you
can I think you better start from the
cloudbased yeah
because especially on the early stage or
especially when you are a small project
MH makes sense if the memory compresses
well then couldn't you instead use more
efficient data structures in
linear sorry um is the top one if the
memory compresses well then couldn't you
instead use more efficient data
structures in Linea yeah actually yeah
that's true um we are trying to use
optimize our data structure as well uh
right now we are we don't actually imp
uh compress data structure in production
because uh to avoid some side effects
but uh after optimizing a lot and and we
have too too many transactions or too
much trans transactions I think yeah we
need to come up with better data
structure yeah as you say it never ends
right always optimizing I've read that
the finality of lenus around 8 to 32
hours will these improvements allow
these to be reduced and if so how low
can
go um actually um the finality time has
includes many different factors actually
not not only the prover itself but
number of transaction or uh service lay
uh service layer agreement or something
like that so it's not only it doesn't
depend on solely on the op appr
optimization actually it's more than
that so yeah agree have you had examp
and where an attempted optimization
actually backfire in an unpredictable
way yeah that's true um so I I think
that um M limit stuff is actually one of
them without M limit the soft memory
limit stuff because that automatically
triggering garbage collection for you we
didn't have any issues in global
constraints part but after applying that
we actually got a lot of garbage
collector collection calls within glev
constraints and maybe the runtime
increased a lot by that and uh that was
actually a huge issue and we finally
found out and I fixed it great great
great has Lena ckvm thought about
switching to ckvm to further improve
um I I have no idea on this to in this
question so yeah maybe I'll skip it yeah
yeah let's skip
it uh remember you can always find the
speaker after these these questions we
can discuss about discuss it and yeah
what are some tradeoffs that Lena made
in contrast with other CK
EVMS well let's say I I saw many Project
based on GPU or F fpga and how we
accelerated and uh we thought uh
starting with the simplest design and
architecture is the best one and
especially for uh so that any small
project or researchers they can just
simply run our product and then share
ideas uh to be more decentralized so for
for a while I we think uh we're going to
keep this um design choice and we'll uh
continuously work on optimization of
yeah CPU based and great and I think we
have one more time for one more besides
those techniques did line explored uh
Hardware acceleration oh yeah disc
question um we are still thinking about
it actually but uh in maybe in next
maybe at least for a while when every
before everything's until everything's
civilized enough researched enough uh we
will keep working on CPU
based great I think with that we finish
please give a round of applause thank
Le um we'll be back in a few minutes
there's more more talks and great
information so yeah stay tuned
all right all right we have a good break
we're coming to the next talk this
afternoon uh it's titled top up code
offenders in the ckvm and I think it's
very relevant especially as we're
thinking about all the changes that we
can add to layer one and basically how
that affects uh layer 2os in CK projects
so uh we have have Carlos Matana here
next he will be having this conversation
again remember you can scan the QR code
if you're just joining if you scan the
QR code you can join um the Q&amp;A you can
submit questions and you can also vote
for the questions that you like the most
so please with some Applause please
Carlos Scana work at UH polygon and
today I will be talking about the top
code offenders in the zvm in order to
explain that basically I will do at the
very beginning some introductions about
the what are the ZK counters what are
the types of the Z counters available
and how many Z counters do we have
available on the
zbm the second point will be in the
analysis of the offenders you will see
that there are some straightforward
offenders on the zbm so there is no
correlation between the gas consumed on
ethereum and the Z counters consumed on
zbm but I will go more into the details
there are some up codes that are quite
straightforward but uh when we analyze
uh in this case I will analyze a Unis
swap swap uh we will see which is the
worst the the worst codes that uh
performs very bad in terms of ratio
between gas and GK counters so for that
purpose I will analyze un SW Dr Trace
and in in the third point I will
basically explain it what are the next
steps um how I would say the the how we
can optimize those of codes in order to
have a better radio between the gas and
the S counters wasted and also I will
explain two different approaches um
about how those OP codes could be priced
on the zbm okay so let's start
what are the zik counters you can
imagine the Z counters if you can
imagine the gas on ethereum in order to
measure some computational cost
execution cost you can imagine the zik
counters exactly the same as the gas but
on the zbm okay basically in the zbm we
have in etherium we have a unit which is
a block in the zbm we have a unit of
proving which is a batch so there is
some relation over there and another
difference between ethereum and the zbm
it's like on ethereum we have
one single dimensional um resource which
is the gas but on the zbm side we have
the Z counters and we have multiple of
them okay so basically this uh this
table summarizes what I have just said
on ethereum we have a unit which is a
block this GM it's a batch the badge
consumes some gas it has some limitation
on the gas and the gas basically
reflects the EXE the the computational
resources that you are wasting when you
execute an OP code this veg has single
dimensional gas on the zbm side
we have a batch which is the our our
unit of proving we have the zik counters
we have several of them so it's kind of
multi-dimensional and basically they
reflect the the proof computational
cost okay well this is basically a piece
of code this is in CK assembly uh
basically this is the zik r we implement
the evm in the Z Assembly Language which
implements the the evm in a z assembly
uh language and basically those are all
the GK counters and all these values
quite difficult to read it so in order
to understand it better we have as I
mentioned in the in the CBM we have a
unit which is the the batch and this
batch has several Zig counters what are
those Zig counters basically we have the
steps you can imagine the steps sometime
I have heard about kind of the you can
you can change the word and instead of
St steps you can say kind of
Cycles H we have the arithmetic State
machine in order to do multiplications
and well also we use the state machine
in order to prove uh divisions by by
doing multiplications we have the binary
State machine in order to do additions
subtractions and bitwise operations
basically we have the memory align State
machine basically uh when you read an
slot on the CBM two different slots and
you want you want to join all the bites
together uh we use that steam machine we
have the kakam machine which is obvious
in order to do kak hashing we have the
padding PO on steam machine and the
posidon steam machine again quite
straightforward to do posidon hashing
and when we want to do a linear posidon
which is a concatenation of poons in
order to Hash a long array of bites we
need to use the padding poson Ste
machine and the very last one is the Sha
it is very important to say that each
state machine has its own capacity so as
you may see on on this slide H we have a
lot of steps because I would say the
computational cost of our step is quite
low it's just one I would say one hit
one row uh when we go through the
program through the GBM R but for
example on the kak you can see that
there are way less resources over there
why is that because basically it's more
complex so it uses more resources so it
has less capacity
basically one thing that is very
important also to mention is that nonone
in a batch we have all those zik
resources none of those Z zik resources
can be overflow if any of those Z
resources is is overflowed it means that
the proof will not could not be
generated basically the pro could not
generate that proof so we need to be
very aware of
that okay so let's do some kind of
analysis on the I would say top code
offenders on the zbm and as I mentioned
there are super straightforward op codes
that consumes ZK counters very directly
and clearly there are offenders on the
zbm what I mean when I say offenders it
means that those of codes consumes some
gas and this gas is basically not
reflected on the ZK counters that they
consume so there is a misalignment over
there the most straightforward one and
of course you may heard about in every
zvm if you do a loop of kxs then you are
wasting a lot of Z resources but you
pay quite cheap gas so for example the
the first code is the G the second code
is the code copy and code data copy uh
in this case um I would say that all of
codes that has some kind of um
dynamic dynamic gas pricing given that
uh given the memory expansion uh we need
to do some computations on the zbm that
of course it C some arithmetization
binary and steps and also when we do
some kind of copy between context one
context to another context it will
basically waste um a lot of steps as
well the third one also I think it's
very clear the example it's the external
Cod copy op code in this case we are
just I mean this op code basically just
go so copy some bytes of a bite code
into a memory region okay that's it what
you need to do inside the zbm you need
to provide the full bite code you need
to Hash it with the linear poon you need
to check that that hash matches the one
that that you need to read on the state
three so now you know that the full bite
code is correct and you need to go to
the exactly bite or number of bites that
you want to copy into your memory region
take that bite and then copy to the
memory region so there is a lot of
things to do on the zbm but the cost of
this code is not that
much and of course uh the clear
offenders are the pl on pilot smart
contracts uh you know there specific
functions on ethereum like is recover
pings uh modular exponentiation and so
on and there is a very huge misalignment
between the precompiled smart contract
gas pricing and the ZK counter
resourcing consuming the
zbm okay those of CES I would say that
are very clear that that are offenders
but I wanted to analyze deeper not the
clear codes but the standard up codes
standard transactions on the
evm in this case uh basically here this
table well before going to the table um
all these numbers belong I mean the some
assumptions the first assumption is that
here we are I'm showing data of a one
batch that has only one block and this
block
has end transactions okay and these
transactions are always the same type so
you can imagine a block in the zbm with
just ether transfers with just e to
transfers and just with un swap traps so
let's go for the first one theum
transfer we can fill up up to 2,000 more
or less of trans inside a batch and we
can see that the top GK counter the more
limiting GK counter is the
arithmetic why because we are basically
checking the signature inside the Cent
so we are doing a lot of is recover the
recover uses a lot of arithmetic State
machines if we go to the next two ones
thec the UNIS swap what we can see is
that okay we can fit less transactions
because you have you have some execution
do and we can see that the top of cod
counter offender are basically the steps
either also I mean either in the and the
Unis Swap Trap regarding the Unis Swap
Trap it gets even worse I mean you hit
the top uh the limit of steps and the
other state machines remain at Health
capacity even
less given those numbers uh we're going
to get into the details of what are the
op codes in a Unis swap swap Trace that
consumes more
steps okay so yes what are the up codes
that consume more States in a uni swap
swap so in a Unis if if you analyze a
trace of the Unis swap swap you will
find that
um push one push two M store pop and
push 20 are the most used to coders if
you join all the steps consumed by all
the appearance of that op coders on the
the book Trace you will find that the
push one op code uh will weighs around
uh 12,000 steps and it appears in the
unisoft TR it appears 658 times so same
for p two M store pop and P so basically
this is St these op codes are the ones
that consumes the most steps on a Unis
swap
shop but let's go again into the
details inside these op codes which are
the is the user paying the correct gas
price I mean is the user paying the
correct gas price in order because the
up code is consuming 2,000 um 12,000
steps so here's the question yes or no
so let's go to analyze a little bit and
here basically I what I did here is uh
comparing the gas of an not code versus
the steps that that code consumed on the
zbm so basically we can get some kind of
a Rao between gas and
steps here we can say
that by far the worst up code is the Cod
copy because it cost just 15 gas and
consumes 1,000 steps so the rtio is I
would say quite bad the second one is a
m store here I highlighted in in in
green because it also it's one of the op
codes that has more appearance also on a
Unis swap swap
Trace so clearly if we want to increase
the efficiency of a v in the zbm clearly
we need to optimize we need to get
better ratio in the MS store for example
example of
code third one is the call thata copy
then push 32 and then call that Lo we
want to get rid of those top op Cod
offenders what we should do is reprising
them or optimize them in order to get a
better ratio
basically on the other
side what are the best of codes what are
the ones that uh basically the user is
paying um I would say fairly about the
ZK counters that it consumes on the zvm
so here we have for example the to one
jump jump conditional St C size or log
three of course log three as a store and
this kind of op codes the ratio is very
very very very low because basically you
are paying that you are storage some
data on the rip three or on the state
three okay so now the question is how
to those OP coders according orderly
to the Z counters that they are
consuming basically okay and the most
straightforward approach which is the
one that we are following right now is
an static approach you can see from you
can imagine uh the batch as a monolitic
batch we have all the resources
available and think that regardless of
the transactions that are executed on
that batch that batch has a price that's
it in this case
the batches that it post to layer one
and the verifier when the verifier
verifies those uh batches that are poed
in the ler one it received the the fees
that's it super simple so the user I
would say that the user um does not care
about that only the sequencer and of
course this price is splitted among all
the transactions in a b
but then we can use uh the next
iteration I would say we can use kind of
a dynamic
approach the dynamic approach is very
similar to the gas limit on ethereum so
imagine that we introduce here A New
Concept which is kind of the ZK gas and
ZK gas limit so the sequencer does not
pay for a full badge but the badge is
dynamic so it means that basically the
pr can decide the amount of the state
machines that needs to prove basically H
we can achieve that via the the bat cops
and basically here the sequencer just
sets a z gas limit very very similar to
the gas limit which is the Z gas that
the sequencer is willing to pay for bat
and then when the verifier verifies the
proof it's substracting gas for the gas
limit and if it runs out it will be kind
of a out of gas but out of gas
limit so the batch is kind of uh
invalid then the next step is okay let's
analyze
properly in the in the in the language
in the compiler why those OP codes are
performing so bad and let's try to
optimize them let's try
to let's try to iterate uh let's try to
add more instructions in order for those
of cod to have a better Rao let's try to
improve the constraints the pill in
order for those of c those of codes to
have a better ratio and not to be
offended on the
zbm if you want to know more about that
uh tomorrow we will do a workshop at 3M
on classroom uh C it is called optimize
zbm throughput Series 2 we did one on
Brussels uh which one the serious one
was a lot of people over there so uh
we're going to explain um some
optimizations that we did on the Z
assembly site and on the compiler in
order to optimize those uh top upod
offenders okay thank
you amazing great talk Carlos much
gracias all right so remember you can
post your questions on the QR code we're
going to start to hit the first one the
top one um what happens if the sequencer
has a bug and it creates a batch that
overflows the counters and then it gets
committed to
ethereum yes inside the good question uh
inside the RM it can happen two things
so inside the RM if the sequencer has a
bu and commits a badge that overflows
the counter H we have a program as I
mentioned which is the ROM which is an
evm implementation but inside the Z the
ZM ROM we control the counters uh that
are wasted if you overflow the counters
then the prover can prove the batch but
it's an invalid batch when I say invalid
batch it means that the Old State root
is equal to the new state R so there is
no State transition function over there
the issue is when you have a bu the
sequencer and in the ROM then you end up
in a situation when you cannot prove the
watch Amazing thanks um the next one is
how much does ef help eliminate or
reduce the top offender up
codes
uh just read once the the
zip uh I mean I would say that uh we
need to analyze uh deeper um what will
be the top of offenders given the change
of the B code and EF basically it's very
difficult to answer yeah yeah no I I
agree it's coming but it's yeah it it
just requires a lot work and uh yeah
research do you still need counters if
your proving system supports
continuations you need counters but I
would say that those counters will not
overflow since you can continue the
proving execution into another batch so
this will mean that basically any
ethereum transaction will be provable
but still if you are just doing a loot a
loop of kick acts imagine that you're
looking a very large loop of kyats and
it consumes seven batches that ethereum
transaction needs to pay the seven
batches but we need to be aware on the
proving system that it's compute seven
batches I mean thanks to the
continuation we will be able to prove it
you need to pay for
it yep makes sense so uh next is around
gas cost would multi-dimensional EAP 50
useful I would say I I I was in some um
meetings discussing about this
multi-dimensional gas pricing and it
could be done but it's not easy to
modify the whole I mean adding kind of a
new transactions with new fields in
order to sign this gas that uh it does
not reflect the computation which is the
gas but gas layer to or ZK gas whatever
you want to call it that uh basically
reflects the um
counters or proving computation uh you
need to change libraries you need to
change um uxui metamask this is not easy
a chief a lot of work a lot of work all
right how do upcodes limit work with
Force transactions and would it be valid
reason to exclude
transactions I mean first transaction at
the very beginning is just a regular
transactions but you just bypass the
sequencer and it works exactly the same
that an standard transaction if a false
overflows the badge which can be and as
I mentioned before in the first question
the batch will be invalid and that's it
so at the very end you are kind of you
want to force your transactions but you
are not achieving to execute your
transactions because the batch is
invalid so and every time of course that
uh a user post um a force transaction
into layer one the user needs to pay for
it because you are bypassing the
sequence
right right uh the next one is are there
any steps that smart contract developers
can already take now to reduce the usage
of those offending up
Coast I would it's very difficult you
would need to go into a assembly code
otherwise solidity just put the op codes
most beneficial for execution not not to
take in account the proving system so I
would say it's very difficult yeah I
guess it would remind require like yeah
reactor architecting the compilers and
doing a whole bunch of like changes and
then yes again y yeah really deep
knowledge of that are there any this is
the last one are there any concerns with
the resulting Divergence with L1 fees in
terms of user
experience I mean we are achieving an
stage LLY that uh the difference I mean
this proving cost
are every time that are cheaper cheaper
cheaper cheaper and cheaper so H I would
not expect um a lot of Divergence
between layer one fees but still the zbm
has some mechanism in order to Port
layer one fees into Layer Two it's the
AAP 1559 in the base fees so it can
reflect the DAT availability cost on
layer one so yeah this some this is just
a technique but there are several ones
yeah but I guess like there's a lot of
improvements still in the back look to
keep improving layer twos instead of
like
yeah a lot of work uh and I think with
that we complete all the questions thank
you so much Carlos it's been a
pleasure
thank all right folks so we still have
three more sessions in this afternoon
evening um we'll be back in 7 minutes so
take a break come back stretch or yeah
they just stay here so we enjoy applied
cryptography thanks
hello hello so we're back for the next
talk grab some seat take a take a look
in what we're going to talk about now so
in this talk we're going to talk about
how the Birch is not going to break your
contracts and it's a look about what's
coming what's changing but also what's
remaining our speaker adran CA is going
to be our next speaker so give a big
round of applause
please thank you hello
everyone uh so yeah The Verge is not
going to break our contracts that's good
right so I work for open Zeppelin and at
open Zeppelin we provide all kind of of
services to the community that obviously
include the open- source smart contract
libraries but also Audits and so on and
we do that because we want to provide a
good a good context a good ground for
developers like maybe like you to build
a next trillion dollar economy that is
going to be poured by smart contract and
so in doing so we want to understand
what's the environment you'll be working
with how the evm works how the
blockchain works and share that
knowledge review through these talks and
also through the the best practices that
we apply to our
contract and yeah just a few days maybe
weeks ago I don't remember we deploy we
released the last version of the smart
contract Library the version 5.1 that's
been in the making for quite a while and
to me personally it's a big milestone
because it's the first time that we put
knowledge of upcoming blockchain change
like The Verge into the design of the
contract we adopt a proactive approach
that the contractor deployed today maybe
more efficient in a few months so what
is the Verge and how it's going to
affect Dev so I was told to not talk of
the merge too much but to rather mention
the transition to have more stateless
ethereum with stateless clients The
Verge being one of the approaches for
that transition and what the Verge does
and how it can achieve better
statelessness a stateless client is by
changing the storage layout to be more
friendly to to to to ZK proving so right
now what we have on etheria
is a storage layout where we have a
Patricia Mer tree that is divided in two
section and the top section is basically
the entire word of accounts and under
accounts some accounts don't have
storage and that's done but some
accounts do have storage and then you
have to go further down into do the ion
storage trck and that's how it works
when you want to prove some storage you
have to prove a miracle proof that goes
all the way from the bottom to the top
and that's that's kind of long that's
kind of expensive that's in Practical if
you want to build a stateless
client so what the Verge does is propos
to change this storage layout to use
veral tree that contains all the data of
all the accounts in a different pattern
and basically there are still somehow
two section there is a main tree that
are the first 32 by of this better hash
that is Computing using the address of
the account and the offset offset being
like the position in the storage that we
we already have
and then that gives you an extension and
an extension contain 256 values and and
then you use like the last as bite of of
of your position of your of your offset
to know where you're in the in the
extension that means that an extension
is owned by a single account uh but then
all these extension of all these
accounts are in the same same same veral
tree and this is a radical different
radically different vision from the
previous slide because in the previous
slide all slots were like identical slot
one and Slot 20 were were basically the
same object and warming oneup was
required when you wanted to agree or
write to it and the same was true for
for the other slot and all slots were
like identical in the sense that you
would have to warm them up individually
but with the Verge what you're warming
up uh and by warming up in the case of
the Verge we don't really what we mean
is put like in the in the in the proof
so in the in the commitment I don't
remember the name we come back uh but
what we do is we we put this this extens
complete extension and we prove it and
this completely changed the Paradigm
because if you want to access two
different slot if they are in the same
extension you only pay once so it's way
more efficient to access storage that is
close to one another which was not the
case before the vert which is not the
case today and so this is a rough
timeline we go from Denon that we passed
to pectra that is coming soon with a lot
of great feature you may have heard
about it during Defcon to hopefully the
ver this is changing the maybe faka
before uh I'm sorry for for that but
yeah I'm I'm really looking forward to
to this as I hope many of you also are
uh and this will impact our contract as
we see like it will impact them in the
sense that the gas cost will be measured
differently and that has an impact so
that's why I want to what I want to dive
into today and disclaimer this is work
in progress The Verge is not definitely
final and those are the best numbers I
could come up with with the help of Gom
from the from the guest team from the EF
but those are possibly not the final
number but it's still a good idea so
let's dive into this first graph there
are going to be a few of these so please
make sure we all understand what the
color means uh here we're representing
the gas prices of frequently done
operation on tokens such as erc20 725
and 1155 and we have two type of
operation there are the simple trans
that are in blue and there are a
transfer from so transferring someone
else's token using a permission that are
in green and in both cases you have like
a light blue a light green and a dark
blue a dark green the lighter colors are
the cost that apply today the darker
colors are the cost that apply after The
Verge and this color scheme will keep it
like lighter is now darker is after The
Verge and what we see here is that
basically for all classical transfer
operation on tokens it's going to be
more expensive that's that's the bottom
line but not but a by a lot so it will
still continue to work unless you're
crazy enough to hard Cod Gas Prices
somewhere in Europe but like it could
continue to work but like RC 721 is
going to be affected a lot the reason
it's more affected than the other is
like when you do a transfer from or
transfer in erc721 you are checking two
type of approval because you can approve
one token and you approve an oper can
approve an operator and those two checks
are two slots that are being warmed up
and they are not not in the same
location so there are two extension so
the price the over cost of of farming
and extension is significant
significantly more visible in the case
of ERC
contracts that are quite interesting
there are governance contract I love
governance and here we are looking at
open Zeppelin contract in blue and
compound Governor Bravo in green and
we're looking at the different operation
that are done in the life cycle of a of
a governor proposal which is you propose
you cast a vote you Quee and then you
execute here in the execute we execute
something small so that the actual cost
of the execution is hidden what we only
look is the cost of the of the governor
part one thing that is quite interesting
that we see is that for governor open
Zeppelin the price doesn't change that
radically the execute is a bit more
expensive but otherwise it stays pretty
similar and there is a good reason for
that is that in or Governor we don't use
storage that much to try to reduce it to
a minimum on the other hand Compound
uses a lot of storage because when you
propose you store the proposal to the
chain and then you refer to that
proposal stored on chain through its
identifier and what's good with compound
Bravo is that the the the proposal is
sted in a structure that is very
sequential so it turns out to be very
efficient in the context of The Verge
because like most of the of the proposal
will be in the same extension so you are
actually saving a lot of cost by by
warming up the enti extension what than
warming up many many slots and that's
what why the Verge is actually reducing
the cost of the execution on on compound
at least in the proposed part so the
idea that The Verge is going to make all
contract more expensive is is is wrong
some contracts can be made cheaper with
the Verge and it all comes down to how
the contracts are designed and what the
practices of the developers
are this is something I wanted to
measure it's the cost of trading tokens
on Unis swap so the x-axis is a number
of hubs like the very left most points
are just trading token a for token B and
the right most point it's trading token
a for token B for token C for token D
all the way to like token G or something
that and so I want so it's scal
basically linearly and in blue you have
compound V2 in green you have compound V
sorry Unis V2 in green you have Unis
swap V3 and what we see is that Unis V2
is a bit less expensive than unop V3
today because there is fewer logic less
logic with the the like the narrowed
down position and the and the capital
efficiency and that will greatly like
this additional storage will greatly be
visible in in Unis swab V3 so it's
likely that un need swap V3 is still the
better choice after the transition to to
veral because it's just way more Capital
efficient and the gas you pay will be uh
saved elsewhere because of like you will
have better prices on your token but
something that interest me a lot is unis
swap V4 because Unis swap V4 and
unfortunately I was not able to run it
in in veral we can go on that later on
but Unis web V4 doesn't use that much
storage at least not on the token side
because because of the singl ton design
there is no token transfer for the
intermediary token it's just like the
first token and the last token that are
being transferred and the rest is just
handled internally by by the single
turnon contract so I'm I'm curious I'm
sorry I could not get those number but
whenever I get them I'll make sure to
share them everywhere I can like on
social media because I want to see how
Unis before before those in veral I
expecting it to do pretty good maybe
I'll be proven wrong but maybe there is
a very strong case for unisab V4 here
and and again I think that using
transient storage and doing the way un
before does it is probably like the kind
of good design that we may want to do
right now because they are good but also
in the long run because they they will
be more vericle
friendly so small control design for
verium what you can do now so it's
pretty simple like you want to avoid
storage and you want to pack your
storage together and that's something I
did for my last to that was at atcc is
taking erc721 the token and try to put
stuff together in particular we discuss
the fact that there is a token approval
an operator approval an owner and a
balance and thing is that the owner and
the and the token approval are both
mappings that go from two unit 256 which
is a token ID to an address in both
cases
and rather than have two mapping let's
have a single mapping with a structure
and so when you load this structure you
are likely that it folds in the same
extension in some cases it will not
because of randomness of of CAS but but
usually it should and so these are
changes that you can apply today the
reason we don't do it is be in the main
contract is because it would break our
storage layout and that has an impact on
our upgradable contract but we could
technically do it today and like when
you run them on the test network of of
verle and again the slide will be
available online so the links here you
will be able to click on them to to look
at all the witnesses um but you can see
that on the left it's the traditional
erc721 and on the right it's the one
that is packed and you see that you have
two s loads that are significantly
cheaper those were pretty old numbers so
I'm not sure the gas prices would be
fully correct here but the the idea that
the weakness is smaller because of the
packing that that remains valid and so
this is measured with today's number you
have ERC 721 from the main repo on the
left and the packed version that is just
my edit on the right that we don't ship
yet and you see that the prices of
running this two version today on on
conun is basically the same like it's
marginally different that's that's
experimental error but after transition
to to the to a Verge node like you see
that the the ERC 721 PCT really greatly
reduces the overcost of of of the of of
like warming up the extension by about a
third like we move from three extension
to two extensions somehow so so that's
basically what what we expected so there
are design decision that you can make
today that may not impact the
optimization of your code right now but
that may have consequences in a few
months a few years uh if we do this
transition to The Verge for for having a
more stateless
ethereum so the conclusion is The Verge
is not going to break your contract your
safe it's at worse it will be a bit more
expensive but most system should be able
to work with that seamlessly but it will
have affect the cost and you can make
decent decision today to improve that
eventual future and the decision you
have to make are try to avoid storage
and that's a general set of rule like
avoid storage if you can and if you
cannot avoid storage try to use
continuous storage so use arrays instead
of mapping if you are writing a compiler
you can do a lot of work here like in
the arrays in solidity and and Viper the
length of her array are stored at the
pre-image of the array and then the
value are stored at the hash of that
that pre-image you could decide to put
the lens at the first St throt of like
the image and not store something at not
store anything at the pre-image you
would just shift your array by one and
put the lens at the same location as the
first item and it's likely that when you
access low item in your array like it's
one less extension you have to load so
that that may be an
optimization uh we I've discussed that
that at lens in my previous ethcc talk
so if you are able and you are
interested have a look at it again this
link to the slide will be at the end and
yeah like we we we do have some vertical
friendly design choices like in RC 7201
and hopefully like the compiler will
take care of all of that at some point
but for now it's not the case and it
will be breaking the storage pattern so
it's I'm not sure I mean something s has
never done before so yeah if you
inventing a new Lang which take take
that into
account okay thank you and link to the
slides and if you just type share.
Adrian kua.com then it index you can get
it from
here amazing great job Adrian all right
so we're going to get started with the
questions remember you can scan the QR
code you can send your questions thank
you for the person who just did you can
also vote for the questions so they I
know get answer first so thanks for the
great presentation so let's start with
the first one a little of off topic do
you you also evaluate contract designs
that optimize for
eof not yet but eof is certainly
something that is coming and likely
sooner than than than verle so we we
definitely we we care a lot about ver
about about e we want to make sure that
it's not going to break our contract we
hope that we are able to ship the same
contract that work with e uh it's
unclear whether we're going to be able
to do that or not maybe solidity will
have a major update anyway but like we
we worry about F I just don't have any
final result to give you
today great great great great question
yes keep sending the questions does open
Zepp has an array lip that stores the
length in the first slot no we don't
have that kind of lowlevel libraries uh
not yet at least uh so far we've tried
to always work with the solidity layout
and not modify it uh but other people
are doing it and maybe we'll do that in
the future why not that's a good idea we
we'll have to discuss it yeah I think
that you also mentioned a call to the
compiler teams to just like start
thinking about all these changes so if
there's anyone here to listen or set to
a friend I think that'll be useful when
do you expect that compilers oh very
relevant solidity and Viper optimized
for veral that's a very good question I
really don't know and I'm not very
optimistic uh one particular reason is
that solidity never broke their storage
representation uh and that would mean
breaking something they've never broken
since 2015 2016 so definitely not in
version
will probably be eof or something like
that uh my expectation is that solidity
is moving to a completely different
design of the compiler with standard
libraries and the compiler will be
smaller and maybe that's when like the
standard Library maybe open Zepp I mean
I'm counting that open zeppin build such
standard Library so
ever relies on them and that will be our
job to do this kind of optimization so
yeah great answer all right uh sorry let
me Mark that okay let me ask this
question does it make sense to implement
a set of addresses like 70 721 approvals
with an array instead of mapping maybe
for a funet or as a cache uh it really
really depend on the length of the
mapping and how you access it so it not
as a as a general rule no maybe in some
particular cases yes and that's what I
want to encourage you to measure and to
like maybe next year at devc connect you
give a talk about
that great how does code chunking cost
affect
deps I'm not sure I understand what code
shuning cost so maybe we can discuss
that after outside and you can me more
detailed because I I I cannot provide an
answer right now sorry yeah no no that's
that's fair uh it seems like 20% more
expensive transactions is a big deal
even if it's 10K in idea
why uh well I mean we're when you look
at small transaction yes plus 10K it's
mean it really depends on the gas prices
because like plus 20% if veral means
that like we have better stateless
client and we have a lot of crazy things
and we have better l2s and things like
that maybe having bit more cost on that
one is is acceptable um and any idea why
so why it's more expensive so why is
loading and extension so expensive I did
not explain why the reason loading and
extension is so expensive is because you
have to do a person hash of your account
address with the first 31 by of the
asset and a Pon hash is complicated to
compute way more complex than a kesak
and so the the the node have to account
for that complexity when they execute
the transaction that's why they're going
to make you pay a lot for that that's
also why we have extension we don't you
don't want we don't want you to pay I
mean the cordev don't want us to pay
this B and hash for each slot we access
so they give us 26 256 B bits I by slots
extensions great answer um I think
there's no more questions so Adrien
thank you so much please give him a
round of
applause great so our next talk is going
to be at 5:30 so we still have like 10
minutes so take a break come back we're
going to still have a lot of great stuff
on developer experience and and uh I'll
see you in a
bit e
afternoon afternoon everyone thank you
for staying with us and for the break
great so we're back developer experience
I think we're all uh thinking about what
could be be receiving and talking about
this next one so Chris Chris cash work
he's going to talk about about uh cheat
calls EAP and how this could be a good
way to standardize a bit how these
different implementations are done in
different systems remember there's a QR
code you can submit your questions there
and with that I L you with uh Chris
welcome hi I'm Chris CER and this is uh
cheit etherum Improvement proposal an
attempt to standardize uh an interface
of etherum development nodes so let me
Begin by painting a picture of a
landscape of etherum nodes so on one end
we have production nodes so this is your
GFF your ref your Aragon stuff like this
so these notes are all about strictly
hopefully strictly following consensus
rules of etherum uh they're about being
a good citizens in the you know between
different notes so you know mining blogs
verifying blocks uh gossiping blogs in
the PE peer-to-peer Network stuff like
this uh and they are totally not about
like you know giving developers any
control over the state because they need
to strictly follow consensus rules um on
the other hand uh on the other end we
have test environments these are not
really full nodes they're are more like
focused only on executing uh evm code
but they so this is Foundry this is hard
Hut and these Solutions are all about
giving control to the developers so um
here uh while you develop your smart
contract you can easily I don't know
deal erc20 tokens or ethereum uh or or
ethereum native currency you can warp
time uh you can uh you can do things
like this uh and this is very useful to
put I uh the uh put your smart contract
in a desired state so so you know you
can test complex uh scenarios and
somewhere in the middle we have the
development noes so um these are tools
like Anvil part of Foundry like hard Hut
node like tenderly or build bear so
these uh development nodes are um on one
hand they are like proper almost proper
eum nodes so you know you can ask them
about blocks about logs and so on and so
forth like that they Implement most of
the standard Json uh RPC interface but
on the other hand they also give
developers some uh control over their
state so they have these special Json
RPC methods that allow developers to
show
them so let's dive into these
development nodes because this is this
is what my presentation is focused on
and turns out they are very useful so
first of all they support forking so
instead of uh creating like you
know pure empty instance of a node
usually you Fork it from some other node
most likely a main net node maybe on a
particular block um another aspect is
that they can be both local or running
in the cloud so uh a good example uh so
basically development nodes Shine for
all sorts of uh uh integration testing
when you need to test both your smart
contracts and your offchain system so
for example in uh spark we simulate
every governance spell um we simulate it
on a uh tenderly Fork running in the
cloud and uh we paste a GitHub uh
comment on a PR with a spell um pointing
to the you know UI with this network
connected to so a reviewer of the spell
can easily visually inspect the the the
impact of the spell on the UI um also we
have like a lot of endtoend tests uh
written for our front end using uh uh
development nodes and also we have like
complex uh
systems um balancing liquidity between
multiple chains and guess what we're
also running like multiple uh instances
of um development development nodes
running together and acting as a like
you know layer one and layer
twos um and as I mentioned they
development nodes give developers
control uh over their state with these
Special Json RPC methods and let's let's
talk about them so um you know so
basically every more complex testing
scenarios uh scenario requires
developers to basically uh bypass
regular uh consensus rules so um one of
the methods so let me present some of
these special Json RPC calls so for
example evm set next block time stamp
allows uh developers to control the time
stamp of a next not yet mined block you
can imagine that this is pretty useful
when you need to assert that I don't
know some exact amount of interests were
was calculated correctly then we have
evm revert which enables us to revert to
previously created snapshot so it's like
a dump of a state at particular of a
state of the blockchain at a particular
moment uh then we have set ear to 20
token balance which does what you expect
it to do um or does it uh and there's
unveil mine for mining new blocks uh and
there are many other methods like uh
really God knows how many because they
are not documented properly and as you
can see like some of them have different
prefixes but the most important thing is
that all of these methods have
compatibility issues for example evm set
next block timestamp on some of the
implementation it will actually mine a
new block right away which makes writing
deterministic tests impossible evm
revert in some of the implementation it
allows you to revert to a snapshot only
once and then the snapshot is like
destroyed um tenderly set C20 token
balance only exists in like uh tenderly
and build bar so if you want to if you
relied on this Behavior to meant
arbitrary C20 tokens and you want to I
don't know switch to Anvil guess what
you you need to write your own
implementation somehow um Anvil mine uh
works great but uh only some of the
development nodes actually have like a
proper mle and some others uh just like
automatically mind transactions as they
come um so all of these
incompatibilities uh reduce the the
speed of development and make like
basically simple things hard um and this
is why I why we create cheat itm
Improvement proposal it's an up it's a
standard to be implemented by all these
development nodes by Anvil tenderly
build bear and hardat of course we're
talking with the team to make it to make
it happen uh but basic idea is that it's
like Foundry cheat codes but for Json
RPC so this is why it was uh named cheat
calls uh EIP um it's all about like
reducing lockin in a particular uh node
implementation and increasing the
interrup ability so imagine that you
develop a Dap and you don't develop a
Dap specifically for Alchemy or for uh I
don't know uh INF fur right like you can
switch rpcs without any issues guess
what when you're writing like uh this
testing scenarios like integration test
you develop it for part particular node
right now and you can think that this is
not a huge problem but turns out that it
is because often you want to uh switch
from local instance to a um instance
running in the cloud because I don't
know you want to have a sharable link
with something for everyone everybody or
you want to use a superior debugging
tools that are only available in one of
the environments right um and uh and
the the cheat C EIP is um is of course
like a list of cheat CES that we want
these nodes to implement but it's also a
testing uh suit uh to verify the
conformance to this spec um all of these
cheat codes share common prefix called
cheat uncore and uh just to give you a
little bit of taste like they they they
touch things like time manag agement
mining control snapshots impersonation
balance and storage management and some
other areas so now let me walk you
through some of the cheat cods so time
management um as I already mentioned
like this is very useful to be able to
calculate interests deterministically
and so on so we have two cheat codes
here cheat increase time which u mines a
new block with a particular time stamp
uh with with a time time stamp increased
by a particular number of seconds uh but
I think more useful is cheat set next
block Tim stamp which doesn't mine a new
block but once the new block is mined
it's going to have like an exact time
stamp um and guess what like this is
properly specified and we have proper
tests to catch all these mistakes that
uh happened in happened in some of the
implementations
uh then we have mining control so in
cheat calls we have a proper mle and uh
first of all you can just mine empty
blocks with cheat mine uh but I think
the more interesting is cheat mining
mode which enables you to set one of few
um mining modes like for example the
default is auto so basically as
transaction come the new blocks will be
mined but you can set it to manual uh to
uh basically stop block production and
you will be required to use cheat mine
to to B to mine new blocks and all the
transactions that are going to send are
going to be inserted into mempo uh and
there's also like interval mining so
something that we're used to when
dealing with mainnet um and speaking
about mle uh we can we have a control
how the block production chooses
transactions from the example it could
be random it could be like you know High
highest Fe first or first in first out
um and also we have control of uh
dropping the transactions from the mempo
so all of these methods allow you to
test complex block submission uh systems
where you can simulate rears you can
simulate Dro trans dropped transactions
from the mle and so on and so forth
um then we have bunch of cheat calls uh
regarding
snapshots uh so cheat snapshot creates a
snapshot and then we have cheat revert
snapshot which reverts to the to to the
previously created snapshot and of
course we make sure that you can revert
to a given snapshot multiple
times um impersonation is quite
important because often you want to
impersonate an account that you don't
hold a private key off so for example
imagine that we want to push a Oracle
update but obviously you won't have
private key to the of the Oracle so you
can impersonate an account uh of uh of
an owner of the Oracle and and push uh
an update and if you're familiar with
the previous implementation you were
able to either impersonate a single
account or imper and or sometimes
impersonate all of them at once so we
opt in into just impersonating every
account
automatically um so this is what cheat
impersonate all accounts does uh and you
have control either of either you use
impersonation or not because your client
Library if you provide a private key uh
they're going to automatically use if
send raw transaction so you send a sign
transaction to the node and if you don't
have a private key uh just just an
address the the libraries are going to
use if send transaction which contains
all the uh all the information about the
transaction and not uh actually like
Signs it or just pretends that that
signs that they are
signed um we also created a meta uh
cheat call for um inspecting the the
current state of the uh of the node so
by calling G info you get bunch of this
basic information about the state of
different treats like know what's the
mining mode what's the uh what's the
state of imperson impersonation and so
on and so forth and also it returns you
a cheat called spec version so this is
to Future proof uh this proposal when
there will be probably more proposal
proposals uh extending
it um now let's talk about balance and
storage management because this is one
one of the most important things that
you will likely do on development noes
so cheat set balance enables us to set a
balance of a native token but cheat set
erc20 token balance does the same for
arbitrary erc20 tokens and this is best
effort implementation because erc20
token standard doesn't talk about how to
mine tokens and so on uh so you cannot
do it in every single case but we can
actually come up with an approach that
works most of the times and I'm going to
talk about it in a second finally we
have cheat set storage at which enables
us to set a particular storage slot of a
particular account so how does this uh
how does setting a particular es20 token
balance could work
so uh with cheat set storage ad we can
tweak we can set arbitrary storage slot
the problem is that we don't know which
St slot holds a value uh holds the
balance of a particular account uh so
just a reminder evm storage is like a
huge u in 256 to U in 256 map scoped for
each contract um and solidity storage
layout says more or less that each
property gets an index and if the
property is a mapping then to find the
St slot you actually take an index and
you take the the the value of the key uh
I mean the key and you hash them and
this is your storage
slot so we can actually set arbitrary
storage uh arbitrary erc20 token
balances by tracing the balance of uh uh
balance of uh call of a for a particular
account first um and then we can
basically you know iterate over touched
uh St slots and change them until we
find the one that holds a proper balance
and this is actually how Forge uh uh
STD um deal uh cheat Cod cheat code
Works under the hood uh so this
implementation is pretty good it works
with most rc20 token balance token uh
implementations and if you're doing
something very custom you probably want
to come up with your own mock for a
given contract or something like this
so what's the state of this uh EIP so uh
it's in pre-draft State meaning that
it's submitted to etherum magicians uh
but uh it's uh it's not yet submitted to
the EIP repository uh there are three
contributors two contributors other than
me so special thanks for p and Emmanuel
anony for helping me with this proposal
and all the teams of developing the
notes are already familiar with the spec
and we're talking with them and even
today we had a we had a pretty good
discussion
um you know tweaking some some of the
behavior and here's a QR code for uh for
the to e magicians forum and you're all
invited to to contribute comment and so
on and also I'm more than aware that
pushing standards in the industry it's
not necessar easy thing to do and you
know there's this obligatory K KX CD
comic strip uh saying like oh there are
we need to create another one that is
universal and guess what there are 15
competing standards now so luckily in
this case we don't have any competing
standards it's just something that
wasn't standardized ever so I I hope
we'll have a better time uh doing that
but I'm also
I I'm also aware that it can take uh
some time uh for teams to implement it
and there's this alternative client side
approach where we can emulate and try to
uh you know smooth out some rough edges
on the client side so this would be best
effort implementation some of the things
won't work because uh there it's just
impossible to do it client side but we
can you know document actually uh what's
possible what's not uh we can warn user
uh warn users about
incompatibilities and actually one of
the more complex cheat codes like set
your C20 token balance actually it can
be implemented client side because you
can get you can trace uh any call uh
using uh access list so it's possible to
to implement such thing for example uh
client side and we actually have
internally a prototype of this approach
and uh you know it's something that that
that might help with transitioning for
the full uh full full
proposal and uh that would be it thank
you guys
and here's a QR code to the spec again
and uh as I said you're all invited to
contribute and I can't hear can't wait
to hear your comments and opinion
opinions thank
you Chris great job thank great
presentation thanks so much so with that
remember you can scan the QR code you
can submit your questions ah I see some
some hearts someone is loving the
questions and the presentation and you
can also vote for the the questions that
you'd like the most so let's start with
the top one when impersonating what does
EC recover do I'm thinking about use
case like permit
decided not to tackle yet this is a
known problem like it also does doesn't
work uh right now what my um suggestion
is is that if you need a signature most
likely the address of the account that
you need the signature of is somewhere
in the evm storage of the contract so
what you can do is you can overwrite the
storage slot with a address with a with
an address of a of a uh you know that
that you know the the private key off so
this way you just bypass this this
problem and you don't use impersonation
at all you just set start slot great uh
the next one is can we have a cheat
cheat mining mode where time stamps do
not increase automatically at
all um time stamps of the blocks right
uh yeah I think it might be a good idea
because actually it's a it's it's a
problem that uh they are picked
automatically and yeah I agree this
might be a good idea to just I don't
know crash instead of mine a new block
and then you would need to set the time
stamp of a block explicitly before so
yeah I definitely think it makes
definitely sense so thanks for this
comment and whoever did it or if you
guys have other ideas please find Chris
uh after the talk I think he will
appreciate that what about the get
storage range or even the get all
storage of a contract helpful to match
the State against an expected snapshot
after every AC uh Test action yes this
is uh this is great question because
iterating over storage slots is like a
particularly you know difficult problem
to deal with um so you know uh this is
like a first version of the of the spec
and I expect there will be more and
maybe this is one of the problems that
that you know can be tackled in the
future one of the uh like guiding
principles of writing eips is to keep
them focused so I
explicitly uh wanted not to you know
deal with too many problems at once but
I think like this would be an
interesting challenge to to tackle and
some of the nodes like Aron have some
special methods to iterate over the
storage slots great but yeah scope scope
 is a real a real issue on
engineering okay wouldn't impersonate
all hide bugs about misuse of certain
private Keys yes so I don't think so in
my experience like it's very it's much
much useful to to to to use impersonate
all than you know worrying about oh did
I impersonate the particular uh account
or not um as I said like this should be
the dealt private uh client side right
like if you don't want to impersonate an
account you shouldn't you know have
private key of this account lying
somewhere in the client liary this is
this is my current view on this thing I
was also thinking about that maybe it's
a little bit too much but you know uh
talk to me I'm I'm open to any
suggestions and like etherum magicians
is like I guess the perfect place to to
leave such comments or you can talk to
me here yeah we need more more reviewers
more ideas all right can we have a cheat
restart node to clean up State and cheat
revert state to recover State yeah so
Anvil I think has something along these
lines um the problem that that I the
problem why it's not currently part of
the spec is that this spec is has to be
like Universal and has to work with the
uh R uh nodes running in the cloud uh as
well as like you know running locally
and this doesn't really make sense for
the ones running in the
cloud like I think Anvil cause it uh evm
or Anvil reset so it's possible to do
I'm just not sure if should it if it
should be part of the standard right
yeah I think that was the last one again
wanted to thank you great presentation
great questions and please give a round
of applause thank you Chris thank
you all right do not leave in six five
minutes six minutes we're going to have
our last presentation of the day
developer experience and that seems like
also very exciting hard hat 3 preview so
good evening welcome good to see you all
I'm glad you stayed for our last Talk of
the day uh which is about hard Hut 3
preview and Patricio Paladino Anda
talked with us about all the challenges
the changes the UPC coming uh features I
think it's going to be a great talk I
hope you stay put remember there's a QR
code on the screen on your right where
you can submit your questions and vote
for the questions that you wanted to be
answered the most so with that I will
leave you with Patricio please give a
big round of
applause okay these are the slides
uh hey everyone thanks for being
here uh my name is Patricio I am the
co-founder and CTO of nomic foundation
which is a nonprofit dedicated to
ethereum developers like you at nomic
what we do is Building open source
infrastructure and tooling for the th
community and the most wellknown that we
of our tools is
harat and during this presentation what
we are or I'm going to talk about is
harat B3 or harat 3 the new version of
harat which is still in development
because it's a whole overhaul of harat
with a tons of
changes uh but first let's take a look
at at harat at harat 2 for a for a
second especially its limitations and
why we decided to rewrite it the first
one and main one is that ethereum
changed Aton during the lifetime of
harad we started working on it almost s
years ago about
chain I think a way more simple
ecosystem there was main net and a few
test Nets those test Nets aren't even
live alive uh nowadays and the
applications were simpler right there
wasn't even uh stable coins back then
now applications are larger and ethereum
turned to be a single chain into a never
increasing ecosystem of different chains
each of them with a slightly different
Behavior another problem that we have in
harat 2 or
had is that we BR everything in
JavaScript including our Network
simulator and that had several
performance issues we also focus a ton
on on the NOS ecosystem because we
envision a building a platform for
others to be able to customize and
extend their own setups but that focus
on on JavaScript only also meant that
you could only write test in JavaScript
or Tes
script and the the final limitation is
that as when we designed Hara there was
only one chain main net we designed it
in a way where for every single harad
process there is a single chain a single
network connection you just import
hardat you have your network connected
there mostly most of the time it's going
to be simulated by us and all the boiler
plate all of your library Sol your
plugins get configured for you but it's
a single chain as soon as you want to
work with multiple chains you you hit
this limitation and you start making
work arounds we created rpcs for
switching the hard Forks or forking
other networks people use different
configurations and and things like that
so harat 3 we reot it from scratch to
circumvent these limitations and offer
more functionality and how does it look
well it looks a bit like this it's a bit
like hardcut it's still hardcut but
hardcut from the future or more tech
technical hardcut but at the end it's
just a hardcut right like it feels and
looks like
hardcut so as I mentioned it's a
complete reamp of the product the scope
is massive harad grew during this six
seven years it has tons and tons of
plings and functionality and I can't
cover everything here I'm only only
going to focus on this list of things
which are the network simulator that we
rewrote in Rust the solidity test
support support that it's added in
hardat 3 a our deployment
solution and how to ergonomically work
with multiple networks so that you don't
have to do those workarounds that I just
described and finally how we correctly
simulate upstack
chains the first thing as I mentioned is
that we rewrote
where simulator in Rust and we ship it
just as an mpm package nobody know or
some people notice this but in haat 2 we
are already running every simulation in
Rust and that led to significant
performance improvements for some people
that is even 10 times faster uh in real
war scenarios it's not just benchmarks
but they just got a new version of harad
and without noticing their test were 10
times faster 10 times f fter and you
just don't have to notice that the TS
interface is still the same it's just at
the at the core it's rust it's a project
that we call EDR from ethereum
development runtime and if you want to
learn more about that project someone
from our team is going to give a
presentation about it
tomorrow the other big change that comes
along with EDR is that now that our
runtime is written in Rust and we can
run things quickly we decided to add
support for solidity test if we did that
previously with our previous infra that
was probably going to be more
challenging and
slower so we added support thanks to EDR
it's also written in in Rust it's
foundly compatible which means that it's
mostly a droing replacement all of the
features that you would expect like
fasing invariant testing Forge STD
whatever you would normally use in
Foundry you can still use it in in
hardat 4 but under the hood it's going
to be run using
harut the other point that I want to
explain here is our solution for
deployment called harat
Ignition which is also available in
harat V2 if you want to try try it out
now and it's basically a declarative
deployment solution and by that I mean
that what you do in ha ignition is
describing your end goal how this system
should look like in production and
ignition will do everything it needs to
do to take your system there it looks a
bit like this instead of focusing on
transaction and execution of a of a
deployment you don't write a script but
rather Define a module you an ignition
module you can think of a module as a
JavaScript module Ras module python
module like a programming language
module where you define certain things
certain entities and you export some of
them the ones that are going to be
interested by other
modules in this case modules in ignition
are Futures are not transactions or
anything exec execution wise instead as
I mentioned they describe the intent of
the user to perform something on chain
in this case in this example we have two
uh contact deployment
Futures basically what we are telling
there using an API is to to ignition is
that it needs to deploy a contact called
parent with the first and single
argument p and a contact called child
with a c as its name I guess um and
finally there's an exra A different kind
of future that it's something like once
the parent is deployed please call at
child with the child address as it
single argument but this is as I
mentioned again or I will mention this
again once more this is just your
intention here when you do this there's
nothing being run there's no transaction
this those serves don't exist yet it's
ignition that we'll deploy them
later and given that it's just a static
description of what you want to do that
gives it ignition a ton of freedom to do
what whatever it does whatever it needs
to do to get there it will analyze the
graph of Futures that you define in your
modules and I automatically detect how
to or watch them and come up with a plan
so that they can be run in parallel as
long as they are safe to run in
parallel that leads to faster deployment
but that same feature or that same
capability of it being static and
ignition taking whole the whole control
of execution allows us to do things that
are much more I guess smarter or better
for you if you are running a a a
deployment a deployment script and it
fails for any reason let's say that your
network fails you forgot to find your
account or something like that ignition
can detect that and recover and how do
recover from those those kind of Errors
Well normally if you were writing a
script you would probably modify the
script maybe add an if or comment out
part of it just so that it only
continues running the things that are
missing in ignition is not like that you
just rerun it and ignition will
automatically compare its local state
with the network state it will validate
that they are in sync and decide how to
continue that allow us to handle a ton
of Errors just to name a few things like
gas gas price spikes we can bu
transactions if a transaction is is drop
from the main pool and disappear we just
resend it if there is a problem with
nons management we detect that those
kind of things we can do just because we
are giving control of the user to the
control of the execution to the user but
keep it to ignition and doing it
ourselves then while ignition has more
features the only other one that I will
uh talk about here is that modules like
the one I showed here can also be
evolved and iterated let's say that I
deploy this system everything goes right
I get traction maybe I need to add
another contact another child I guess
and that's common right successful
software always evolve always requires
changes maybe in smart contacts that
means adding a new smart contact or
running a a an upgrade if you're if your
system is
upgradable and you to do that in
ignition all you need to do is modify
your module rerun it again the same
module the same command and it will
detect if they are are compatible
complain if they aren't but if they are
it will diff the state and only run the
things that needs to be run to get it to
the new
version and finally the only big feature
of har3 that I harat 3 that I want to
touch is its new multi-chain
support which is a fairly complex one so
I'll explain it bit by bit there are
many things happening here I'll use
these two lines of of code to explain
them first as I mentioned in harat 2
when you just import hardat you get a
single connection to a single Network
right and that brings a ton of problems
in Hara 3 that's different we gave full
control to the user about network
connections and instead of exposing a
already uh I guess prepare connection
for you we instead give you access to a
what we call a network manager object
with has a Connect method and that
method takes a network config Name by
parameter and it allows you to connect
to whatever you want in this case main
net would be one of the networks that is
configur in our config but it could be
any other network right and it could
also be an EDR power Network you can
create many network connections to
simulating networks and create many
simulations and all of them are going to
be independent
then while you do that the pling system
that has been reot in carat 3 it's going
to initialize all the usual libraries
and helpers and things that kka does for
each of those networks so here this BM
is connected to the network connection
main net but not to any other one that
you create and you can doing that you
can create anything that you want and
avoid any kind of work around like
switching networks or having multiple
conf files or things that people used to
do in V2 at the same time we introduce a
new concept as you can see connect takes
a second param that concept we call it
chain type and as the name says it's the
type of chain that you are connecting to
I guess you could you could explain it
like if you were to take all the
different evbm networks some of them
will behave very similar to each other
like upstack Networks behave close to
each other maybe with some smaller par
param differences L2 behaves similar to
seia arb2 may have different deployments
and so on and so forth each of those we
call them chain types and what you do by
providing a chain type while you
connect is two things first you inform
the connection or or the pluging
mechanism that those libraries and
helpers that you are you you are using
and you install should be aware of that
chain type which can mean that they
include differences in the shason RPC
how they interact with the shason RPC or
they may even like in the case of of BM
here they may even install extensions to
their API if you use if you ever use BM
with OP stack you will you may know that
you can add special op specific actions
and that's this will be done
automatically both at at run time and at
type level so if you were to use OPN to
run an OP specific thing like estimating
L1
gas uh and you just switch the chain
type to L1 it will stop compiling it
will give you a type level error so that
it will lead to a very smooth developer
experience while at the same time
automatically initializing it for you
when you are doing the
when you're using the right chain type
now that's not the only thing that the
chain type does if the chain type if
you're connecting to an EDR Network and
you use a chain type you will also
inform EDR that it should be running on
a different mode EDR in harcat 2 only
supports only simulates mainnet but in
harka 3 it simulates different different
chain types right now we only simulate
three three different J types L1 which
is focused on Main it sepolia and
holeski uh or something like that uh we
have optimism mostly focus on upstack um
mostly right now uh mostly op mainnet
and opola and we have another one that
is called generic it's for every other
network that we haven't fully supported
yet H which is kind of a base common
denominator and and what dedr will do
when you provide a chain type is change
its Behavior to be to well to actually
behave as close as possible to the real
Network and what does that mean it means
a ton of things it depends on the
network right but it could mean shason
RPC change changes sometimes an object
has extra fields or some fields are
removed some chain types have extra Json
RPC methods um maybe some of them have
extra up codes optimism I think has one
or two up codes they have extra
pre-compiled pre- deepy contracts uh
different gas cost all of those things
we want EDR to be very precise at
simulating because otherwise what we end
up doing is just using L1 or or tooling
design for L1 testing against L1 and
deploying to different networks that we
have slightly different just hope for
the rest and that those things sometimes
go wrong that has already
happened so the idea here combining all
these features would lead to you being
able to handle multi-chain workflows
while very smoothly while also having
very precise simulation of those
chains uh finally uh the project status
I I want to mention how the project is
going as the title suest this is just a
preview this is not ready to be used
it's not in production we have an
internal
Alpha it's not really it's pretty rough
uh we are doing some demos with some
teams unfortunately we can do it with
everyone uh but if you're interested and
you see s you you meet us somewhere just
let us know or just get in touch through
the internet I guess uh but in a few
months we make that Alpha
public um finally if you want to know
more about what we do at nomic we have a
few extra presentations if you scan the
QR code on the left you can see a list
of our presentations tomorrow I'll give
a keynote explaining the high level
technical vision of nomic
foundation somebody else from our team
will give a presentation about how EDR
implements these chain types and
simulates different ta choice and on
Friday we have a presentation about um
slang our Sol compiler as as an API and
in particular some cool apis that it
offers to do code analysis for solidity
like imagine CSS for solidity code
something like that
um and well and if you enjoy what we do
and you would like to work with us scan
the other QR code and you will get info
about our show openings and that's it
thanks
everyone amazing Patricia I'm already
very excited great presentation and
great features thank you so all right
can send love there's already a lot of
like hearts and you can vote for the
questions that you want most I think
we're going to hopefully yeah I think we
can have there's a lot of questions so
let's start uh right now what's the
killer feature over Foundry yeah so I
think
um I think there are a ton of different
features I think developer experience
it's a topic because there is a ton of
uh smaller pain points that you need to
fix to have a a great a great
development experience and sometimes
there is not a single killer feature
well I do think that the multi
multi-chain support that I mentioned is
is great I think that's something fairly
unique I haven't enter into other more
advanced things that harat 3 does way
better over harat 2 uh but uh eventually
we'll release more information great how
does ignition handles proxy
upgrades yeah so proxy upgrades for
remission are just uh other Futures uh a
proxy upgrade is just a call so you can
encode the call uh you can
also um create reusable functions like
any any
function a module is just code so you
can create a function that would be run
this upgrade and it takes other Futures
and Returns the future or something like
that we have examples of of that on our
website great great answer next is VM
the future of hard heart or do you plan
to support both VM and ether JS equally
moving
forward
um both or yes I guess would be this
answer uh I think that the default
experience will be BM as we saw uh it's
more advanced especially for l2s uh it
it brings very support for certain l2s
that's great it's also way more advanced
with typescript but moving forward we
support both and we even support both um
we even provide a smooth transition for
people that use ethers in B2 to use
ethers in B in B3 and to use both in B3
yeah great next one is about deployed
State managed how how how is the
deployment state manage for example if
multiple deaths are working in the same
project but the state is local there may
be
conflicts yeah so the state is local uh
we think that it's just another artifact
that you should version and share and
just treat it as if it work up it's just
c yeah okay all right next one will
harad 3 provide full traces of failing
test like Foundry does uh yes and it
will also provide
other features that harad V2 does like
recognizing uh common error scenarios
like in harad V2 if you I don't know
send a transaction to a method that it's
with gas sorry with value to a method
that it's not payable and things like
that har the text them gives it a clear
err message saying hey you are sending
fans to a non payable thing and things
like that uh those will also be
supported in so test too oh maybe I
didn't mention this but the chain types
thing the ability of precisely
simulating a different chain that will
also be available in solidity test how
it will look like exactly we are still
exploring it it may look exactly the
same but just a flag at the command line
or it may be more present through the
solidity testing framework great great
answer so why not build in public since
the beginning of B3 I think people
really want to get their hands on it oh
it's on GitHub uh it's a branch called B
next it's just uh it's not ready for
production yeah just clone it build it
uh just don't complain if it breaks too
often it's still very helpful yeah
expected to all right ignition question
it doesn't let you pull the state of the
contract in the middle of the deployment
isn't it a great
limitation uh uh not sure if I
understand this question I guess uh if
it means if you can read a contract yes
uh you can read it it's just another
future I didn't show it here but just as
you do call which would be a right
operation you can have a future for a
read operation and it's it's just a
future right when launch of hardhead V3
time uh it will be early next year
exactly when uh we don't know
yeah great can ignition module be used
as a fixture in tests yes they can be
used as fixture in test both with BM and
ethers all right all right all right
will harad provide VAR debugging like
symbi symbolic by runtime verification
experience or better experience than
Foundry and how or how uh well we'll
focus very strongly on the baging after
our release uh how exactly
fairly complex we have 15 seconds uh but
we'll integrate the and our compiler to
be able to provide better the experience
and in that's part of what I will talk
in my keynot tomorrow so feel free to go
there don't miss it is multichain
support compatible with awesome plugins
that already exist like hard hard deploy
if not how hard is it to uh it's going
to be to be migrate
uh yeah so uh every
plugin if there is plugin authors here
you may hit me but every plugin we have
to go through a pre mechanical migration
plins are easier in my opinion to build
in harad V3 uh but it's not automatic uh
you have to migrate them right right uh
are you thinking about uh smart contract
mocking support yes so for solidity test
they are supported as I mentioned uh
solidity test is a
Jing replacement of Foundry sh we the at
at this score um and
for JavaScript test um we would like to
see smoke return but we'll have to I
guess chat with with the team and we see
in the future right does hardhead
ignition supports open sings upgrades
pluging no not yet uh it's something
that we' love to see happening uh and
I've been chatting a bit with some of
them uh that some of them may be here uh
but we'll eventually get there all right
there are seven more questions but we
are over time so let's take the maybe
two okay two more ignition is like
terraform for is is ignition like
terraform for
contracts I guess you could say yes or
somewhat it's a a biggest inspiration
nice nice and what is the difference in
supported chains like EDP op versus
General chain support what difference or
lack of features can we expect with the
generalized chains well the generalized
chain or generic chain uh doesn't have
any extension it's more like it's it's
the Bas common denominator of evbm uh
it's even less strict than mainnet uh
when you run on L1 mode we are strict
about simulating main it as closely as
possible with generic it would be close
closer to what harat 2 does and it's it
doesn't have any extension that any L2
has and it's a bit
more I guess
forgiving right there are more questions
but we're sadly run out of time so if
you want to catch patri later after the
talk I think he'll be available
otherwise online as well uh please give
a great run of Applause to Patricio
great talk we're all very
excited with that we complete the day
please remember to pick up uh any litter
or things to clean up after yourselves
we will start tomorrow uh at the same
time I think we have great applied
cryptography user experience uh
developer experience and core protocol
talks so please uh come back tomorrow
enjoy all these great knowledge and uh
see you soon so hope you have a good one
