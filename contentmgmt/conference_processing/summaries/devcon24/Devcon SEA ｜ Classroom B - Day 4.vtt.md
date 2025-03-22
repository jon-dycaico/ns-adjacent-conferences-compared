[Music]
t
o
back e
for
e
that
you
m
oh
sh
I
hey guys hope you guys can hear me okay
now but uh welcome to Defcon at Devcon a
tabletop experience today we're going to
go through the harrowing experience alog
together of what happens when your
protocol gets wrecked now today uh my
name is Heidi and I'm joined here by
Peter my colleague we both work at
coinbase on the unit zerox team now
let's set the stage a little bit over
been stolen this year from almost 300
different projects the average time to
steal funds is only 15 minutes but the
average time to react is usually at
least an
hour now there have been about 27 or so
instances which were great where white
hats were able to rescue about $150
million and you too can also save
millions of dollars by practicing
incident response in a very safe and
controll environment today here with us
so I'm going to go and hand off the
discussion to Peter where he's going to
be talking about the tabletop
setup cool thanks Heidi
so one thing that we found that really
helps folks to deal with incidents is to
practice practice not just you know when
you have a real live one when you're
freaking out and waking up at 2: in the
morning but in a control safe
environment where you can actually take
lessons and build things um without
wrecking your whole protocol so what we
do at coinbase is we run tabletop
exercises all the time where we think of
a really scary scenario and we practice
that scenario in a very controlled
simulated environment so
tabletops um so the goals for today one
we want to practice incident response
handling how many of you have
participated on a live or maybe
simulated incident
response uh
exercise not all of you that's a good
thing that means you didn't have to go
through the worst of the worst thing
that your protocol can go through but I
encourage you to take notes what we
about to do today and bring it back home
and do the same thing again and again
with your project um the other thing
that we want to do today is we want to
educate you we want to educate you about
some of the threats and exploitation
tactics which are most like this I don't
want to give you any spoilers but the
scenario that we picked out for you
today the thing that we're going to
practice is something that will most
likely hit your protocol and most likely
be damaging enough to pose an
existential risk to
you um and you know like the way that we
designed it is something which is very
portable you know we we're not bringing
like large infrastructure or things you
can literally just after you come back
home schedule some time with your teams
and say hey let's let's uh you know
Heidi and Peter they taught us how to do
those things let's run a quick thing
like this is what worries me the most
like we upgraded a contract or we
deployed a new DB or we have some cool
Cloud thing that we just sign up for
let's let's practice what happens if
that gets
hacked participation is not only
encouraged it's required so we're going
to use slido we're going to give you
questions you know things to discuss you
can team up if you want to um but we're
looking for your live responses we'll
give you time so you can you know
brainstorm how you would respond to
different things that we're going to
throw at you we're going to throw a lot
at you uh suspension of disbelief you
know we're practicing this is all
simulated so we may give you like
certain scenarios which may think like
oh that would never happen to me in me
real life well most likely it will but
but you know suspend your disbelief
sometimes
uh it won't be perfect but the key is we
will learn and the key thing I want you
to bring home this like feeling of um if
something really nasty happens to me at
least I kind of played with it once so
I'm going to breathe in and do what
needs to be
done okay so terms injects artifacts
discussion so injects are things that we
will provide so you know we we'll inject
something some event that just happened
throughout each inject you may ask us
questions those are the artifacts so we
can you can ask me like hey uh Heidi you
know if I was to look at that EA address
do I see any interesting labels on ether
scan you know or if I talk to person X
we can even do like a real roleplay
maybe we can you can talk to one of your
devs so we can we can play those games
together so you can ask for facts and we
will provide those facts to you and at
last discussion so this is where the
slido comes in we will go back and forth
based on what what questions you insert
through slido and we'll discuss them
together okay so Logistics so we are the
facilitators we will provide the
injections and if we see that within
your slido answers you kind of going
down the Deep Rabbit Hole like is this
like something really outrageous we will
you know call it out and redirect you to
something more more
reasonable um we'll give you a break you
know it's uh 10:00 so we'll give you
around 11: we'll give you a 5 minute
break um and then after the exercise is
complete we're going to sit down and
talk through what actually happen and
you know all the all the things all the
lessons that how we would approach it
and how we would we would love for you
to what takeways we would like for you
to take go there um one more thing which
is pretty cool for every inject that we
provide we will also give you a case
study everything that we're giving you
today is based on a real life compr
so we will give you an inject something
happened and then we're going to give
you a project which was hacked in this
exact way and then we're going to
compare and contrast how this project
reacted and how you reacted and then how
we would react so we'll learn
together um before we jump in make sure
that you can scan this QR
code and you can or go to sl.com or go
to slid
and just type in that meeting number and
you will see that there's a drop down of
various different injects if you don't
feel comfortable scanning QR
codes yeah we'll give you a minute or
two to make sure that you're all loed in
to be clear that QR code you see on the
side there for mirat we are not going to
be using today so make sure you use
slido the reason being is that a slido
is a slightly more interactive um and B
we also wanted encourage remote
participation so if there anybody if
anyone's watching this live stream right
now you too can join the SLO link uh and
uh start asking questions or making
statements how's everyone looking you're
able to log
in all right cool okay well let's begin
then so there's this really cool project
out there it's called founder mode down
and unsurprisingly it actually was
launched on the mode L2 chain it's got
over 100 million tvl right now in fact
actually it's got almost two million 200
million tvl at the moment and what's
interesting um about this project it is
that it involves the fumo token which is
the governance token for the project now
what this project does is it invests in
various native nent D5 projects and
requires them to create a token pairing
with fumo so unsurprisingly about 80% of
all projects on the mode chain hold fumo
or some derivative
thereof and
you are trying to look for to join a new
project and guess what you just were
hired by this project you're very
excited uh one of your contacts from
Devcon back in Boga in 2022 reaches out
and is like hey we'd really love you to
participate with us and you are
psyched the team is fully remote um and
it consists of only five people but you
guys are ready to go and what's really
nice about this project is you kind of
know everyone you everyone uses their
real name everyone's very chatty and
conversational and you're really excited
you're at youru computer you just
finished like day five of getting
onboarded and you're reading some of the
developer docs making sure you fully
understand what's going on within the
project when
suddenly you wake up at 3:00 a.m.
in the
morning your phone is blowing up
telegram signal Discord X all your
friends are messaging you that your
project just got wrecked your team is
panicking and begging you to sign off on
a quick real quick protocol upgrade what
do you do so if you could pull up your
slido and if you have
questions put those in the slido feed
what would you
investigate I mean and look at those
questions right there that we have to
kind of prompt you um but yeah you've
got two minutes we'll give you two
minutes time to think of questions
responses and then we'll talk through
them
so I'm already seeing a lot of responses
here and unfortunately we're not going
to be able to share the slido here
directly with you guys I guess I can
plug my laptop in maybe we want to do
that um but I'm seeing lots of questions
come in and I'm sure when you're on your
phones you see them as well um some
people are asking and it looks like it's
being quite upvoted right now is what
happened here I don't know Peter do you
know what happened
here well the key thing is that the
contract had a A Fault in that contract
and it
appears that the funds are flowing out
of those
vaults someone also said I'm gonna call
my mom and apologize to her for getting
into crypto I totally get
that it seems that as as folks are
investigating a little bit more it looks
like the main contract holding all the
volts was recently upgraded
keep putting in your question I'm seeing
start a war
room my question for that person is is
how would you go about doing that who
would you start a war room
with your team who's all asleep at 3:00
a.m.
is there pause free function in the
protocol there used to be but now that
the protocol is upgraded there is some
unknown contract which is sitting in its
place with no source
code someone's already asked has the
upgrade been
audited the response here is uh no we
don't have time for that it's 3:00
the upgrade does not be appears to
be expected in any
way you can update the resume that's
fine yeah we have some people rapidly
trying to just get out of the space Fair
let's try to share the screen I think it
would be fun can we share can we do um
can we do a screen share a screen share
yeah can we plug in the can we plug in
our laptops again sorry sorry I think
it'll be fun to see the
puts but someone asked war room and I
know that I prompted them like saying
well with
who your team um I think uh just to
provide some artifacts you reach out to
seal 911 um which is a part of the
security Alliance consists of various
different people many of whom are
actually in the room uh that are willing
to help um and they're starting to look
into it but
you don't want to yet spin up a
full-blown uh investigation
quite so what does the protocol consist
of so the artifact to inject is that it
appears to be an unknown contract which
is being called by an attacker and after
every single call a new vault is being
drained
you're
good we've got a bit of a delay but now
we're going to be able to
share no signal that's
good okay there you go
they drained the volts could you could
you please repeat the last
response yes
so uh following the upgrade you're
observing onchain a whole series of
transactions and after every transaction
appears to be large amounts of funds are
being drained from The Vault previously
controlled by that
contract someone also said roll back
first analyze after what do you mean by
roll back roll back the
chain roll back the contract okay but
funds are already
drained you're not recouping those
funds is there does have an emergency
pause there used to be an emergency
pause in the original contract but since
it was upgraded there's no it's unclear
what functionality is in the cont
contract how would you approach
that oh let's get a mic so you need a
mic
we I'm I'm actually a little bit
confused about the the cause of the hack
are you saying that it was the protocol
was upgraded to an implementation and
there's no source code correct and who
perform that upgrade was it the prot
that's a good question how would you
figure that out oh okay so it wasn't the
team that performed that up upgrade and
caused it themselves want to ask let's
let's figure this out that's a good
question let's let's follow this uh
Chain of Thought like what what
questions and who would you ask is there
a
CTO no everyone's the
CTO yeah there are five people there's a
CTO did the upgrade happen at 3:00 a.m.
and then the hacks happened right
afterwards it appears that the upgrade
happened shortly before the the drainage
started train started um so we could ask
everyone on the team in the war room if
anyone knows anything about the
upgrade
first and then check the onchain
transactions to see like what kind of
governance system implemented that
upgrade if any if there's like a multi-
we could start looking into
that so interestingly enough the upgrade
was performed by a private key that was
used by the original
deployer okay and the team members all
deny perform this upgrade themselves
there are only four team members on this
war room call right okay so we can
assume that the deployer key got
compromised by
hacker potentially possibly possibly
okay I think we
should
yeah so you're you try to get five
people on the call and so far you have 4
it's a It's let's say it's 4:00 a.m.
you're still trying to reach out to
people this other Dev is a little flaky
so you don't know a little
flaky yeah right now we don't know a lot
the Seal team is is investigating that
along with the uh the project team in
the War Room at the
moment I think um we're going to pause
this conversation here to actually go
over some real world case
studies and I think since I'm sharing my
screen it's going to be pretty nice oh
yeah okay so before we dive into next
steps we just want to step back and look
at just real world recent very recent
real world scenario we're talking about
end of September of how similar
protocols react to that kind of 3: a.m.
phone call so the case study we're going
to use is
shezmu so the sorry let me uh so the
initial detection that someone reached
out to the protocol saying that well how
the protocol even found out there is an
issue was the classic Tweet someone
tweeted them saying that there's an
issue so this is at uh 8:00 p.m.
8:30
p.m.
it took the
protocol just 20 something minutes to
make an announcement to triage
this so before that like the actual Hack
That was happening so this is the
killchain the hack itself happened at
out there to detect that there was an
issue and reach out to the
protocol um the exploit itself was
deployed 1918 1921 the exploit was
deployed the first transaction started
happening at 7:30
and five minutes later the attacker
already started swapping funds so this
is a typical
timeline when we when you get the
initial call like that every single
minute counts so when we're we
eventually arrived like oh like the
right question was asked like hey like
who made that upgrade where is that
coming from can we upgrade the protocol
again to save it like those type of
things need to be in your playbook they
need to be in your kind of like you
known things to do ahead of time so you
can shave off those minutes so those
five minutes before the attacker so the
two exploit transactions that were
executed usually attackers don't drain
everything all in the same go so you
have just a little bit of time literal
minutes that you can minimize the losses
so it's just a one case study
um so in terms of response for for this
hack in
particular um an hour later someone
detected it half an hour later there was
an announcement and then a day
later the pools were paused so someone
asked like can we pause the pools right
away rief I think it was you that
question was asked and responded to
almost a day later
so just just a just some some things to
absorb know what you need to do
including mitigating actions like
pausing pools or doing an emergency
upgrade or something like that ahead of
time now one of you guys also already
mentioned this but there are some online
sluth out there we're already starting
to look into the actual exploit
transactions and an online sleuth Zach
actually points out that one of the
funding addresses of the attacker has an
ens name with the same telegram handle
as a recently hired contractor the
project now what are immediate security
concerns here how should we investigate
this situation now and how can we
respond internally or externally now
that we know that there might be some
Insider things going down I'm going to
give you guys two minutes um to write
your questions in slido um and the way
you're going to go about doing that um
within uh slido is actually go up to the
top and just flip over to inject to and
start writing uh any kind of questions
you have we'll try to answer them real
time
but someone's asked what access
permissions the contractor had can we
revoke those yes we can to an extent
unfortunately mode uh to founder mode uh
we let everyone set up uh their
their environments using their personal
laptops so we can only revoke access
keys that we know about in the cloud
otherwise though we can't really revoke
much
access what's the contractor's role
someone asked um the contractor's role
was as a developer um they were testing
out upgrading some of the pool contracts
um so that you know we could um have uh
better better and more rap transactions
flow that was one of your
devs has that Dev ever said anything
negative about Kim Jong-un
no no he hasn't but you know what we
didn't apply the test of like hey can
you please say that our dear fist leader
is terrible no we we uh we didn't do
that here in the project team
unfortunately um I mean you can try to
contact them and that's actually what
you do you're like hey I want you to
write me on slack immediately [&nbsp;__&nbsp;] Kim
Jong-un he does not respond though he
has not by the way responded to any
messages that's on telegram on X on his
phone nowhere he's like Gone
Gone does this contractor have access to
other protocol contracts interestingly
enough this contractor was involved
initially with the development of
founder mode he just did didn't think he
could commit full-time to the
project is he dead I don't know
someone's got to check on
him so in terms of actions um so feel
free to ask for artifacts like what's
going on but what are your steps what
what are you working on right now as an
incident
responder and let's flip back to those
questions to kind of help guide us right
what are immediate security concerns
some of you guys ask like hey does this
guy still have access to any kind of
privileged roles yes he did um and let's
say you start revoking them all
immediately there's another question
here of how can we respond internally
and externally we'll let you guys sit
with that one especially
externally it's one that project teams
think less about but but is
critical yep rotating deployer account
quickly so that's one action so on the
proxy contract you are trying to rotate
to new keys okay that's a great
idea where are the exploited funds going
well currently the exploited funds are
just sitting in an eoa belonging to the
exploiter but that's a good question
we're concerned about about them moving
along what piece of code does he
actually inject into the protocol so
when you go to Ether scale and you try
to see like what is the code it just
looks like a large binary blob that's
that's all the data that you have like
what's any like what would you do with
that what would you guys do with that
there's no there's no nice solidity code
uploaded to Ether scan attacker was um
not nice enough to do
that someone asked where's the
onboarding guide use that guide for
Access revocation I'm sorry this project
just spun up a couple of weeks ago yeah
sure it's taking over mode but we don't
have an onboarding guide here we are the
onboarding guide as the
team higher Hitman okay
it's good way to thought he was dead
someone decided he need we needed to
hire a hitman he's getting a little wild
here have we tried decompiling that's a
great idea thank you so uh you try to
decompile the contract and the one
function it's all kind of scrambled but
the one function that stands out was the
one that was used to drain volts it
appears to be very simple um token
transfer uh functionality that links to
the attacker's address there's a proper
access controls in place so only the
attacker can call it and all it does it
takes the token address that the
attacker wants to transfer and just
simply drains whatever is in the
contract so it's very
simple you're also seeing other you're
also seeing other um I guess functions
within that decompiled piece of code so
when you you can also specify it looks
like the token address to drain and the
amount and also the token uh the token
address the some kind of like owner
address and also the amount so you have
two functions in there which appear to
be
non-standards some people said uh take
down any external sites where users
might add funds to pools and issue a
warning not to interact with any
contracts that's a great idea um
hopefully the team is talking about this
in the war room and is issuing tweets
and reaching out immediately to these
websites because as you guys remember
this project um sure it has a high tvl
but it impacts all most other projects
on the mode chain so
effectively we're this this whole
incident could make mode chain entirely
toxic which is not what anyone
wants so that's something that we
haven't heard the room do and often
times we see projects also forgetting
that they're so busy with handling the
incident they forget to do the coms and
it's very important to tell users tell
other projects what is going on what is
the impact and potentially if it's a
systemic issue to give them a heads up
like maybe we're dealing with yet
another compiler bug right where not
just your project is affected but
everyone is affected or there's like a
Mass fishing campaign where not only
project your project was said but others
so it's very important for the sake of
the ecosystem to communicate there's an
issue someone else said uh pause the
protocol is a safety measure tweet about
it assuring user funds are safe
investigations ongoing this is exactly
to Peter's Point messaging out to users
upfront even though you don't exactly
know what's going on is critical it
provides that trust for users to
potentially still come back to you even
if you do end up being wrecked time and
time again a lot of Protocols are not
exactly explicit and forthright about
what exactly is going on and that
destroys trust within you and your
users what you might do in this sense
and it's worth asking is what funds are
not safe here are there still treasury
funds and if there're are treasury funds
then you can say hey we have treasury
funds funds are safu in one way or
another we can help reestablish so that
would be one way to do
it another person said contact exchanges
Bridges to see if we can stop the funds
from being withdrawn that's a really
good question um especially because
we're right now the funds haven't get
moved from this one EA but once they do
start moving they're going to
immediately attempt to flow out of mode
chain why as I just mentioned that
entire chain is going to become very
toxic soon mainly this attacker has
withdrawn mode related tokens right and
so these mode tokens aren't useful on
any other chain you want to get out of
there if you're an attacker as soon as
humanly possible and so you're going to
bridge over those funds so bridges are
most risk as well as any centralized
entity that is interacting with the
specific founder mode token
I think uh we're going to move on to a
case study actually just because in in
uh the essence of time because we have a
lot of different injects to talk about
here today but um well if it loads we're
going to talk about a very recent case
study in fact actually this slide is way
out of date because as many of you guys
know um Delta Prime was not just hacked
on September 15th but also just a couple
of days ago again um and on September
compromised admin key we don't have to
go into all the different details of it
but it was because the admin key was
compromised and interestingly enough
there are quite a number of concerns my
bad there are quite a number of concerns
about Delta Prime and how they were
managing their contractor base in
particular if you do a little bit of
onchain slothing as many people have
already done you can find that there are
relations to several unsavory actors out
there whove been paid directly by the
treasury to do some contract testing um
for the protocol and these guys have
been involved in lots of other really
interesting exploits in the past which
date back all the way even to like the
yam Finance exploit and defi summer of
contractors that these these guys hired
so I'm not going to go into all the
details on that one but having a chat
offline um about the Delta Prime
situation but various different unsavory
character have been involved there and
they've been alerted of this in the past
if you are a protocol and you do get
alerted of this make sure you take it
seriously dig in assess whether or not
you think the risk is worth the
potential reward of having hired this
contractor yeah and uh uh oh there's
another
exploit just as you were thinking that
You' made the comms looks like the
attacker done just holding all the funds
at this point they drained the entire
protocol now you get another alert users
are users on the mode chain are reaching
out saying that their wallets are now
being drained so not the funds stored in
the vulnerable protocol itself but the
money is moving from their very own
wallets and as you start interviewing
all those users which were compromised
or sorry are losing funds the only
common thing is that at one point
another they interacted with the founder
mode
contract what could be causing
these wallet drains how should we
respond to protect users and what is the
overall impact to the protocol
ecosystem we're going to give you two
minutes to ask
questions yes so for those of you that
didn't didn't hear this revoke approvals
immediately how do you do that across a
decentralized community of individuals
sorry I'll go
back awesome um I'm gonna start uh
reading some questions here so it looks
like someone also said infinite
approvals can we easily revoke all
approvals uh that would be really scary
if we could I'd be concerned about there
being additional attack vectors if that
were the case so that is no no we
cannot should we try to upgrade the
contract to a null address uh something
like null
code okay so we upgrade the contract to
basically overwrite yeah attackers
whatever malicious code okay that's one
approach if that's possible yeah I just
have a general question like before this
even happens we communicated externally
in this situation would you recommend
preemptively for users to revoke all
their approvals against the protocol as
part of that almost like a standard
action I
mean there there are multiple stages of
the intive response like one one stage
is the triage and then the root cause
analysis so it's very critical to
perform root cause analysis before
jumping into like mitigations and comms
and all that to understand what happened
what's affected and how big is a blast
radius so you may accidentally advise
users to take actions if if it's just
for safety that's fine what I'm more
worried about you you you force people
to do actions which may be more damaging
because you don't have a chance to fully
understand what is the root cause I'm
trying to think of a scenario so if
there is a compromise and they start
interacting with a token or protocol
revoking approvals and by making that
approval they somehow are triggering the
code they shouldn't M we could have a
mass I attackers don't listen to this
but point is if the approval itself is
getting back doored and all the users
are calling it on the compromised token
now you're poning the whole
ecosystem um that's a good point extreme
example but the point is root cause
analysis and understanding is is very
important there's also like the Panic
thing like what what we're seeing is was
actually IM unify recently published an
article about like what is the true
impact of a token compromise and we
usually focus on like hey pro project
tax was compromised and they stole $5
million or whatever but the secondary
effects are often times 10x if not more
the initial impact so we have token
prices which are dropping to zero the
value is dropping then you have
secondary ecosystem the like the people
are getting wrecked if they're loaning
something getting liquidated so very
important to be very careful what is it
that we advis to users and externally
after we fully understand what what
exactly
happened actually on that note Peter I
was just thinking about I forgot if it
was in 2022 or 2023 but wasn't revoke
cash overtaken uh at one point or
another and so if you're tweeting out
hey use revoke docash to revoke all
approvals if an exploer has taken over a
website like that you're dunzo right now
your users will never trust you again um
and that would actually be one of my
bigger concerns as opposed to some you
know little smart contract thing but um
someone wrote on here why don't you
tweet to revoke all token approvals with
the fumo contracts that's one thing you
could do but as Peter mentioned again
understanding the landscape is extremely
important but messaging to users is also
important so we don't want to forget to
message to them saying that we're
looking into it we're
investigating um but you might not want
to say hey revoke all token approvals
until you've actually done
analysis yeah so so far we got a couple
good points if the attacker was nice
enough not to change the administrative
account and the proxy upgrade it to
something non malicious
comms revoke revoke approvals anything
else that you would you folks would jump
in
on okay which token got uh
drained ERC 20s doesn't matter
oh so if it is like uh propriety token
of the fumu contract then we can just
like uh remove the liquidity from all
the decks and like we will tell all the
centralized exchange like this is a
blacklisted token so at least that
hacker or the T actor can't uh get out
it fun we can do that for fumo but the
problem is because there were so many
pairs right you know how we talked about
how the fumo governance token works you
can maybe do it for fumo but all the
other tokens out there are screwed right
all the other users that hold those um
someone asked here what wallets did they
use they used all sorts of different
wallets metamask coinbase wallet privy
doesn't matter Unfortunately they all
got wrecked so unfor this is not a
situation of like a slope wallet uh here
but good
question and someone asked here what
does a sample transaction drain looks
like well they're calling to a contract
and you can see here suddenly there are
a whole bunch of transfers then looks
like over 100 transfers take place in
one transaction alone all just
transferring ER c20s from whatever uh
whatever person whatever EA it was that
had done the approval to the particular
exploiter remember when you were
decompiling and there was this unusual
method which was taking a token address
amount and also and an I guess an owner
EA address it looks like the attacker is
calling just that so they were not only
greedy enough to steal money from the
Protocol no they came after users as
well so someone has the cool idea kind
of like you where it was snapshot the
balance before attack and try to migrate
the fumo token or fumo contract token
into a new one great idea but only good
for poor fumo and not everything else
and unfortunately as we know fumo is an
ecosystem token if the ecosystems
wrecked it doesn't matter if fumo exists
or not
someone also asked hey can we get Waller
providers to show warnings about
approval revocation yes that's possible
so you're in the seal 911 team uh who
can hook you up with metamask and with a
couple other wallet providers and
they're happy to help um and they're
happy to provide sort of that warning
sign um but as you see on chain you see
at least 10 of these transactions going
down as you're trying to reach out and
get contact with
metamask and that's something I someone
mentioned it here but we should continue
pushing on the ecosystem if you recall
this is the ecosystem wide token we
should be in the war room talking to all
the other projects right now pausing
their protocols because it's not enough
that we are compromised the the fumo
token is compromised all these other
liquidity provider Pairs and they're
about to get wrecked as well they're
about to get drained because someone is
has these Mass amounts of uh fumo token
and they will use it because they need
liquidity to get out of the
chain a lot of other questions uh
there's one question about did Ledger
and VM package get compromised again I
don't know do you want do we want to
research that maybe we get a researcher
in Seal 91 to take a look at it um and
they find HM no I don't think this is
The Ledger mpm package it doesn't look
like it this does not look like
like that particular compromise at all
that developer the fourth developer
sorry the fifth developer is still not
online by the way you still can reach
them yeah we're not sure dead Hitman
what were the other ideas that happened
to this guy food poisoning I don't
know someone asked can white hats
recover funds from uh from the user
using this approv related method are
there legal concerns with this
well unfortunately the attacker was
nasty enough to change the admin owner
of the original compromise contract so
you cannot just upgrade it as
easily so white hat action is not
possible but what action would you take
like uh is there anything that if
there's a chain wide hack like what any
other creative things that you could
take so we're already messaging out to
wallets and asking wallets can you
please please please throw up a warning
sign revoke approvals we're already
sending out tweets saying hey revoke
approvals not using a revoke docash link
or anything like that because we're too
paranoid is there anything else we can
do uh was that fifth employee working
remote or where can you repeat that so
the one guy is still missing on the call
right yeah so we can uh talk to the
local police uh to their uh living area
yes and of course you know this person's
true name right and the previous inject
we also learned about his ens handle we
can do a little bit more due diligence
on that front in steal 911 you also have
some online SLU that are trying to
figure out where he lives however our
project is entirely decentralized we
love that we pay everyone in fumo right
we don't know exactly where this dude
lives unfortunately we do have his logs
though and unfortunately his logs point
to him using mulvad VP n and so we're
not exactly sure of his location and
mulad uh is a little notorious for not
necessarily providing us the details we
want um but we can do a little bit more
digging again we're a startup with five
people okay I'm seeing a note heart Fork
the
chain here we
go who whoever H asked that question if
could you get a mic please and let's
discuss this a little
bit or they might be remote or they
might be remote well on a high level so
we've
seen I'm trying to count the number of
times that full chains halted or hard
Fork so we have the blast that comes to
mind we have Linea we have the good old
BSC when the the bridge got BC token
token Hub was hacked a few years ago so
it's not an unheard of thing to do to
hold the entire chain when a major
protocol is hacked so what what how
would that even look like just just to
just to um you know we're what we're
doing this here is like we're simulating
scenarios so if you are arriving at a
point where you know as Heidi mentioned
this is half half of tvl of a given over
half okay half over half of tvl of a
given chain L2 chain got compromised is
it unheard of to reach out to the chain
owner like provider and start a
discussion to Halt
it or may be like what are What are the
in between actions
like would we call mode into the war
room and beg them and tell them your
Project's dead in the water your chain
is effectively toxic I want to say
Phantom had that problem right Phantom
hasn't really come back from the grave
since the multi-chain exploit it's
effectively become a toxic chain right
so maybe you could dangle that and say
hey Mo you don't want to become another
Phantom you know please come help us but
is there any other precedent for that I
don't know but we can certainly talk to
them and maybe try to get some lawyers
in the room again we're a bunch of devs
we're only four people now we don't have
lawyers yet but we're still talking to
seal 911 and uh trying to work that
through with
them so one thing to keep in mind when
you even talking about like you know
nuclear options this is a nuclear option
it's a because it breaks the
fundamental Assumption of
decentralization for what is it that we
do here if a single entity can decide to
make AC take actions like that that's um
that's uh you better you know I mean
we're ethereum like this is ethereum
conference like we've been through this
before
so the question you need to answer is
where and how exactly you going to take
do that so you have a variety of points
you can you can uh like the linear
approach or blast approach you can you
know block list malicious addresses on
the sequencer side you can approach it
on the bridge side on the mainnet side
you can potentially start looking for
outbounds and start you know paying
attention maybe block them there where
else would you would you put some kind
of stoppage or like what are your
thoughts
like go ahead Maybe can get a mic
or could we ask for a recap of what's
worked so far because we've thrown a
whole bunch of
things on the wall what's what we were
we actually able to accomplish in the
last 40 minutes so so far in this last
scenario the vaults are
drained before we had a chance to war
room and get everyone in attackers as I
showed you with the uh one a sample
exploit attackers need five minutes to
do their thing so attackers currently
holding all the funds in their eoa the
funds are not moving yet following that
internal investigation showed that it's
potentially someone who has access to
private Keys the deployer private keys
and the last piece the attacker is
currently actively draining all the
users that ever interacted with this
protocol and collecting those funds as
well so funds are still not moving out
of that EA but we are still in the war
room kind of like deciding what are what
are we doing next we've unable to pause
cont we were unable to pause the
contract because the core functionality
of the contract changed it's now a a
contract which is fully controlled by
the attacker so that ship has
sailed there's one other fact too that
uh your fifth Dev you're unable to reach
out to them right and we know that they
may or may not be associated with other
elicit
activity let's actually take a quick
pause here and let's do a quick case
study I'm sure many of you um already
kind of assume some of these case
studies coming up here
sure okay so the case study that we're
basing this on is radium Capital so
radium Capital if you look at the
attacker right now on chain so the
initial hack was $53 million and you
know pretty fascinating attack all by
itself the the three key signers of the
protocol
were not NE let's say tricked they were
tricked by substituting a transaction
that was on the way to their Hardware
wallets to make them sign something they
did not intend to sign which is an
upgrade of a
contract here's what's more interesting
in this not only did the attackers
perform this upgrade to drain all the
volts they did add the functionality
just like how attacker to also drain the
users I have not seen this level of
greed and also sophistication at the
same time that it's not enough for you
to be $53 million richer no you continue
the attack and I'm I looked at the the
attacker just a few days ago they
continue draining users even as we speak
right now so the second someone put some
money in their wallet drained so they
have a script running which is just
moning those wallets that are approved
to that contract and they continue
getting themselves more and more
assets so just a case study so this is
again every single inject is based on
something that unfortunately happened in
the real world you should be prepared
for so the takeaway here is just because
your protocol just got compromised it
doesn't
mean you're
done not only not only is your protocol
now lost funds you have to start
thinking okay what is you know we
discuss like you need to do the root
cause analysis to fully understand the
problem you do need to quickly decompile
the contract look at what other
interesting functionality there may be
sometimes you get surprised attackers
don't put uh some kind of access
controls so you can wi hat it so you can
take all those funds back um that
happened before or at the same time you
need to immediately start warning your
users and reaching out to your partner
protocol saying the first wave of the
attack is done we are about to get hit
by the second wave which is going to
Target our users as opposed to the
protocol itself so just another lesson
learned so the tldr of that is you
shouldn't just be worried about your
treasury your pools you also need to be
worried about your users right your core
users are the reason why you even have
your project to begin
with cool so we are now at halftime
basically and I think it's a good time
to go ahead and take a five minute break
because it's been a lot um and we're
going to come back in five minutes time
um to uh continue maybe we can give him
like so it's 10:51 right now let's come
back at
more there going to be
resolution there will be a
resolution not necessarily happy
this is not this is not Hollywood so the
story does not always end with with us
walking in the
sunset we're going to try
though
e e
not on uh on here okay I think we're
ready to begin after our lovely
break so does anyone to try their hand
did a quick recap of what we talked
about in the last hour all the
injects anyone that's okay if you don't
the long and short of it is is you're
running founder mode your project right
it involves the fumo token and your
project as well as others with the
derivative token make up 80% of Supply
on the mode
chain it seems like your project got
wrecked all of the funds were withdrawn
from various different pools um for your
token uh due to a malicious contract
upgrade um you no longer have access so
it's not like like you can try to take
it back um and you know that one of your
project team members is not responding
to any emails slacks phone calls Etc
they've just fully gone
Mia you also know that this
particular employee or
contractor they seem a little bit
suspect and
finally you thought the worst of it was
done it wasn't because suddenly users
who had approved their tokens to all the
pools that were drained are suddenly
getting drained themselves
so you spray the sigh of relief to an
extent all the pools are fully drained
at this point all the users appear to
have been drained sure some users can
still send funds to their eoas and those
can get drained again but you know
you've messaged out you've done all the
comms that you can you've like talked
with C 911 you've set up a war room
you're in conversation with local law
enforcement you're in conversations with
various different exchanges through seal
the incident you I think that you can
wind down the War Room at this point but
unfortunately this is usually when the
real fund begins
because as we mentioned last time the
attacker was mainly just sending funds
to one eoa
alone but in the middle of the night
they start swapping and moving funds
over to various evm
chains so there are a couple questions
we have here can devs do something what
actions can we take who can help us stop
this and how do we warn everyone so I'm
going to go back to slido here and we're
g to Pivot over to inject four where
we're going to start that
discussion and now some of you one of
you guys actually asked earlier like how
is it that we would maybe reach out to a
centralized exchange to maybe stop flow
of funds um and I wanted to leave it
actually to this point uh so we could
talk about like how do we even reach out
to centralized exchanges my advice would
actually be if you are already in a war
room with seal 911 they can usually get
you in
touch so someone right immediately on
here stop Bridges so there are two
different type of bridges here there are
bridges right like a canonical Bridge
which usually has a 7-Day lockup period
um of funds so yeah you could prenti
you know stop those Bridge funds from
moving over but various different third
party Bridges right um those are going
to be a little bit more tricky to stop
now some of you mentioned Way Way Back
like hey we should already be reaching
out to Bridges let's say you reach out
to a couple of them and only one
responds and is blocking the funds
that's great you've only blocked though
$20 million 20 million is great but as
we mentioned before we have $100 million
at stake here
plus someone says Blacklist the address
on token contracts like usdc that's a
great idea unfortunately though usdc
here on the mode chain is not native
meaning that uh we have we're dealing
with usdc here which is a bridged asset
there is no blacklister
ability same with
tether but that's a great idea on chains
where you can potentially have funds
blacklisted like usdc and usdt that is
indeed possible however I would not rely
on that these the process for getting
funds blacklisted is usually slow and
arduous and you have to already have a
contact with law enforcement established
and I would say that nine times out of
those tokens immediately into tokens
that cannot be blacklisted so I wouldn't
even bother
necessarily someone says prey pre Zack
xpt finds the person behind this
account well what would you look I mean
it's great to rely on third parties but
like what would your approach be to like
to figure out like who's what is the
identity like do we know who is the
attacker at this
point someone said uh why don't we warn
the Mia contractor right remember
remember we had that contractor that was
our fifth Dev that isn't responding to
us that everyone is a suspect at this
point and there will be legal
implications if laundering doesn't stop
immediately that is possible but they're
not responding to anything right they're
not opening any of their messages it
doesn't even look like they've been on
Telegram in the last two days since this
incident some say why don't we reach out
to the Tacker and uh have and say that
uh we won't pursue any legal
action if uh if they give us some of the
funds back we're going to hold on that
it seems like the teams back and forth
as to whether or not we should indeed
you know reach out to them we don't
really feel comfortable we've been
talking a little bit with law
enforcement even though some people on
seal want to do that we're just not
exactly comfortable at this front uh
doing that but that's an interesting
idea
well going back to laundry like what
what are we doing to to see well one to
identify where we going where the funds
moving and then potentially stopping or
freezing them so we had some token
freezes exchange out reach anything else
that we should be doing right
now is there anyone else you maybe want
to reach out
to some of you guys mentioned and uh
Zach xbt is a person to reach out to
there are a couple different uh online
slth that you might want to reach out to
your team at this point is going to be
extremely tired if you're up for X
number of hours trying to solve this in
a war room you're not going to have the
ability to tra track down all funds and
you guys might be sitting there thinking
well why do we even have to do that
funds are gone well law enforcement's
not going to be capable enough to do
that when you reach out to them no
matter if you reach out to them today or
tomorrow they're not going to be capable
of doing that so it's going to be in
your best interest to understand where
the funds are so you can best explain
how to potentially get them back if
indeed that's even possible there are a
couple of different companies you could
be reaching out to at this point um zero
Shadow is one of them that tracks funds
and gets alerts another thing though too
is you can start tracking the funds
there are several different Services out
there that are free like metas sluth
that you can actually set up alerts on
various different addresses uh so that
you can see for example like with
attacker right let's say he sent funds
only to one eoa you could s alert on
that EA if it ever sends funds out right
boom then you're going to be aware um so
there are a couple different services
like that that you can already just out
of the box get uh without having to sign
any crazy contracts or doing anything
self-reliance is key like it's
definitely great to reach out to third
parties and ask for help but you know
the reason why we're doing this exercise
is to identify your gaps so if you today
if you're sitting in the room and you're
saying like well if I had to trace funds
I don't I don't know if I'm capable of
doing that well why don't you go it's a
it's a free it's a free uh project that
you can use today go to metas sluth it's
free of charge pick up any exploit I
think we have a case study coming up so
you can take out the case study any of
the case studies that we at we're we're
discussing today and just see if you can
just trace the funds like where where's
the money flowing like what exchanges
does it hit what project what Bridges
what swap they perform spend half an
hour on that so that that 30 minutes
that you're going to spend will mean the
world if you have to do this under much
more stressful scenarios where you have
to like do this live like okay where
where the money go at least you know the
tools you know how to use them and just
it will give you some guidance of like
what who to reach out for help someone
has this cute comment in here why don't
you interact with an ofac tainted smart
contract or wallet so that all of the
addresses for founder mode get blocked
so they can't drain money anymore that's
cute but uh uh I don't think I don't
advise anyone doing that if they are
working or interacting with um uh users
um or uh platforms that are based within
the us or Europe generally speaking I I
don't think that's a good idea it's cute
though a security research company that
sh remain unnamed did do this for the
sake of the experiment is it's not a
good idea to do this let's let's stay
there there's certain ethical things as
a Defender that you can and cannot do so
one of the things and it's well
established in traditional security and
applies to our side as well you can't do
things like hacking back a protocol or
targeting you know you know interacting
with something that you're not supposed
to like ofac uh addresses and so on so
on so it's a don't stay on the right
side of the law actually on the hacking
back aspect someone mentioned here you
know why don't we get founder mode to
sign with the seal Safe Harbor um yeah
certainly that can happen but I mean
seal Safe Harbor is great you know
signing that beforehand would have been
nice maybe there could have been some
more prevention that could have happened
uh but that's potential and for those of
you that don't know what the Safe Harbor
is effectively your project signs uh a a
legal release so to speak saying that
hey if I get hacked and and in this
particular instance where a white hat
sees the hack going down they can
actually hack those funds back and
return them to this particular address
that I have designated now seal safe
Harper is fantastic but it works in very
very specific legal instances so it's
just one thing to keep in mind here and
maybe now that you are thinking about
you know what happens if my protocol
gets compromised this will be the push
that you need to sign up for something
like that so if we if we go back to the
case study we we covered earlier the
shezmu the shzu hack right it was
actually a success story because the
majority of funds were
returned um immed well first of all the
the initial attack of returned the funds
for for the a bounty what's called let's
call it a bounty Ransom Bounty um but
something amazing happened the same
protocol also had a weakness of
vulnerability which was even more
damaging than the original hack and a
white hat explicitly white hat found it
reached out that they performed a white
hat attack returned all of the funds so
engaging the community signing up for
something like Safe Harbor ahead of time
so that people don't have like this
moral dilemma like do I save all that
money or do I risk going to jail if for
some reason I don't have permission to
maybe you can short circuit this this
thought process and sign up for the Safe
Harbor so that if someone does want to
help you they they're not afraid for
their own safety and their legal
repercussions of that there's some
pretty funny comments in here I just
read one saying SWAT the contractor's
address gez like we're going wild here
some people said to hire a hitman some
people said check if the contractor's
dead there's a lot of stuff going on
here I would say the the top comment
here is secure all access logs like
Discord um so that we can use it for
future analysis I highly recommend that
um there are a couple other things you
can do as well and in the essence of
time uh because we do want to kind of do
a mo postmortem of this attack I'm going
to kind of move on with a particular
case study that I kind of want to talk
to you guys about um with regard to
laundering to help you guys think
through it now generally when funds are
stolen nine times out of 10 on an evm
chain what they attackers will do is
they'll use some mix of mixers Bridges
coin swap services and also sexes in
order to launder funds and interestingly
enough tapioca Finance which got hacked
what was it last month um they the
attack here instead of using a mixing
service they primarily actually used
bridges for opusc purposes so as many of
you guys know tornado cash used to be
the main stay for attackers to just mix
funds and for any Anonymous developer to
actually you know anonymize their source
of funds or destination of funds or
whatever right unfortunately now that
it's been oaed though it's basically
Persona on grata and a lot of exploiters
actually tend to use it so you're
effectively mixing dirty money with
dirty money and you're going to be
getting dirty money out and that's not
great if you're an attacker so they're
trying to evolve a little bit here so
I'm going to go very very quickly
through the general flow of a theft so
usually adap will have whatever their
native currency stolen so in this case
it's the fumo token right that fumo
token though right let's be real here
it's worthless to us because in theory
if mode finally reaches Z out to us
right as the as the the uh as the
founders of the company maybe they'll P
the chain right maybe there's something
we can do here right so I want to get
out of fumo as fast as possible because
if I dump that token it's valueless so
usually those funds are bridged over to
an evm chain from there they're usually
mixed through a mixer and then it's one
or the other they either go through a
coin Swap and Bridge and usually this
will happen a couple times over but
eventually those funds will go into
Bitcoin for whatever reason I don't know
I think it's because in Bitcoin there's
common spend while it's look a little
bit more scary researchers decide to
quit tracking through that and so
because of that they send through mixers
and then they go back bridge over to evm
chains and they cash out at otcs and
Sexes I see this happen all the damn
time it's really annoying because
Bitcoin basically Chas like it basically
halts a lot of people from tracing funds
down the line even though I would highly
suggest spending some time in the
Bitcoin ecosystem and you'll see how
easy it is to sometimes break break some
of these mixers now um sometimes they'll
rinse and repeat some of this stuff to
make it a little bit more complicated
but this is the long and short of it now
unfortunately as I mentioned before
right here at the beginning part tornado
cach is no longer super trust like we
don't want to use tornado cach because
it's full of dirty money there also
aren't many privacy protocols even rail
gun doesn't have the liquidity enough to
off you skate a lot of times attacker
funds so what exactly are they doing now
in tapioca instance what happened was is
they stole a whole bunch of money some
USD usdc um on arbitrum and what these
guys did was they used a series of
different Bridges and just started
bridging tether over through all of
these different Bridges and chain
hopping and interestingly enough some of
these bridges are easier to trace
through than others so what these guys
are doing is I mean you use a mixing
service right you use a mixing service
to off youate the source and destination
of funds you don't keep the money there
as like a savings account right to like
keep your dirty money forever that is
not the point and especially if you're
an attacker you don't trust any service
right so all these guys are doing is
trying to buy time so that you as the
protocol cannot Trace through where the
funds are so you can't stop them so this
is how they buy themselves time and
eventually of course they get into
Bitcoin and these attackers their new
way of doing it is through one chain new
way it's actually we've seen this a
couple of times and from Wan chain they
go to Wasabi wallet which is a mixing
service and from there they go back to
evm and the whole song and dance again
the same thing we see with usdc right
and this is just to kind of just give
you guys a flavor of what you guys might
see out in the wild if indeed you ever
see a protocol getting wrecked or your
own protocol getting
wrecked okay so yeah so the the name of
the game is to stay just far ahead of
researchers and investigators that they
can move the funds safely to a
centralized exchange so they can cash
out so whatever aisc techniques they can
come up with and it's like especially
like moving through Bridges or swapping
and all of that the reason why they do
this is that standard analytical
analytics tools they they don't have
like proper parsers in place to very
quickly identify okay the funds are you
have to look at the full like
transaction call data figure out like
where are they sending them funds and
then for every single protocol you have
to look up like oh it's a the chain X
means they're moving money
to I don't know polygon or Avalanche or
whatever so it's it's massive pain in
the ass to like go through the docks
figure out where the money is Flowing go
to the other blockchain Explorer catch
it on the other side and you have to do
this for every single protocol so if you
have a an idea for a brand new killer
analytics product is is is uh build
something that would have modules for
every major protocol for every major
Exchange and so on that traces through
those things actually there are a couple
of bridges out there right now some of
which that I mentioned in tapioca like
um Stargate for example uses layer zero
so you can go look up the transaction
the bridge transaction on layer scan um
dln has that as well across does not but
you know what would be a really killer
app is bridging all of these different
scans Bridge scans effectively together
to make one big I don't know cros
hopping chain scan out there um yeah
effectively though you as a protocol
need to be on top of what's possible and
what's not um attackers obviously like
to you know be the first adopters for a
reason um because some of these things
are very difficult to understand if you
only have two minutes to really Trace
through to figure out where the hell
funds are going especially if you're
very hopeful that since these funds are
in both usdc and usdt that eventually
they will hit ethereum and that's when
The Blacklist function can potentially
be invoked well you got to trace through
that very rapidly because otherwise
they're going to dump those funds and
you know you're one chance is
gone okay
yeah yes so centralized
entity yeah so uh what one person here
said was uh centralized enti act a lot
like like mixers from The Outsiders
perspective if you're working with a
company or with Cal 911 you can
potentially collaborate with these
centralized entities that will help you
trace the funds on further one thing I
highly recommend too is when you're
working with law enforcement they can
also more quickly get that information
from whatever the centralized entity is
so that you can continue tracing them on
now there are ways to break these
centralized entities especially coin
swap Services now for those of you that
don't know what when I talking about
when I Mak a coin swap service it's a
service there are a ton of them on best
change.
Ru that effectively allow you to
swap like Bitcoin for E without
providing any kyc details whatsoever so
it's very quick fix float is one of them
change now as you probably know change
Le um there are a bunch of them um but
yeah those are the ones that um yeah
that you can also reach out to as well
in that in that
instance yeah the time is not on your
side and then the attackers when well
depending how sophisticated is the
attacker they they know exactly what
they're doing and they're moving funds
like every few minutes like boom boom
boom one after another so not only do
you have to know how to trace through
those things you have to be fast to go
through through all those different hubs
but again depends on how sophisticated
is the attacker like a lot of times if
we're dealing with the you know kind of
like if you've seen my talk the lone
wolves the you know the crypto natives
who are not like fullon criminals that
you know lering is their second nature
they will fumble those things because
they don't they don't know we're we're
preparing you for a professional money
launderer who's been doing this for many
many years and just to prepare you for
the speed of tracing that you will need
to perform and one other thing that I
want to make clear here is they
partition out funds into increments of
full amount that was stolen they usually
don't um a lot of times attackers are
quite lazy when they launder initially
through tornado C passion they just like
throw it all through and then they
basically just withdraw using the exact
same tactics over and over and over
again so it's very easy to
detect what percent would you
professional like this and what percent
is
like oh sorry I'll ask it again what
percentage of attackers would you say
are professionals versus fumblers like
yeah half and half from what I've seen
okay so it still makes sense 50% chance
that you're going to hit a professional
it also depends on the root
cause yeah I would also say though in
terms if we though translate this into
volume the professionals are getting in
ton of volume but the professionals that
that conduct the attack initially the
professionals who conduct the attack are
not usually the launderers though in
that case and the launders will screw up
all the damn time like they'll mix F
through tornado and then withdraw from
tornado to like an address they already
used like I mean the amount of things
that I've seen like that happen on both
Bitcoin and ethereum is wild but yeah
they're not very great they're
contractors usually cool and you said it
depends on the type of the attack so is
it going to be the like the nation
states right if you're dealing with
nation states you're dealing with Pros
if you're dealing with criminal gangs
you are dealing with Pros if you're
dealing with like the early example I
used was the Shmo the there was a lot of
fumbling there was like a lot of doxing
there was a eoa account that was used
and reused many many times you can find
all sorts of data if you want to dig
more hence why it was so easy to reach
out to the attacker and negotiate a
return Co thank you yeah I would say
nation states it depends though whether
or not they fumble the laundering
process laundering looks very different
in a lot of nation states dprk in
particular fumbles laundering because
they hire various different contractors
out to conduct the laundering and
basically follow a flow right and
sometimes the contractors screw up and
you can basically see that then the
manager's like no you're done here like
just send me the money and then you're
like yeah I see what happened here cool
well
uh okay speaking of dealing with
attackers and and the next steps a
common tactic that we're seeing that
happens post the compromise is projects
reaching out and talking to attackers
saying hey uh you know can we uh can we
negotiate and such is the case with your
team as as the uh as your all of your
friends and colleagues they're
increasingly getting
panicked and there's no way to get the
funds back they start begging you to
reach out to the attacker so the
question for for the room is how would
you do that what would your message read
and what are you negotiating for what
what are you hoping to get
back so feel free
to throw
answers and some of you guys already
asked that question like hey why don't
we just negotiate with the attacker so
this question is let's
negotiate I love these responses uh
that's that's the Sting the the the
Hitman yep we have some aggressive
participants here today I do not want to
get on your bad
side call it aggro Dow
instead some people are saying hey we're
going to offer a bounty maybe five to
it five or 10 you kind of want to be
precise about those things have you guys
ever taken a negotiation course
yeah only one of you guys uh highly
recommend um if you're a Dev and you're
concerned about this ever take a
negotiations course it will help you
figure out exactly what you are willing
to negotiate on because it's not just
the funds that you're NE necessarily
going to be negotiating on right um You
might be negotiating on getting access
back to your contracts um they could
have other things that you might want
the ownership of your company
director
role yeah you get to be the director
again
director inside joke which we'll reveal
in a second yeah um ask them if they
need a nap first yep exactly naps are
important before starting negotiations
again this is actual case study it's not
a joke that actually happened someone do
like 5.88% I have no idea where you got
that from but you know seems like an
interesting anchoring number to use yep
um someone wrote threatening will not
work for them exactly yeah so that's why
you want to negotiate right um offer 5%
expect them to accept for 10 to 20% and
call it a lucky day someone has
definitely dealt with negotiations
before this sometimes and this
oftentimes actually happens uh but you
don't know to necessarily lowball them
either because then they'll get offended
um and then they might not even respond
with
you well it would be great to see like
full text if you want to if you want to
throw it in the chat like what would you
actually send on chain and then the
Assumption I'm not seeing this mentioned
but the assumption is normally
negotiations start onchain where you put
a literal asky text in a call data and
you set a transaction to the attacker
with a message so bad actors usually
expect that to come through sooner or
later or sometimes they will reach out
to you and say like hey let's uh let's
talk let's talk this has not happened in
this case not in this case
yeah um someone actually mentioned get
get a hold of the techer and reach out
to law enforcement at the same time this
is a really interesting one actually
because usually it's we're assuming this
year but usually the negotiation is hey
you give me Bounty I won't reach out to
law enforcement or pursue anything you
do not have control of law enforcement I
don't care what you say you have no
control over law enforcement so don't
even bother I would say negotiating on
that angle well you should say because
it's not eally binding you can sorry you
should you should say cuz it's not
legally binding you can tell them that
you won't press any charges and then
press as many charges as you
want there's that there so interesting
case study is the mango markets with the
AI Eisenberg right so there was everyone
familiar mango markets you know a very
profitable transaction you know
following that very profitable
transaction there was negotiation where
you know there's a little back and forth
where a agreed to return the funds in
exchange I what the exact terms are I
think they were they wanted to cover
whatever the loan was that that he
manipulated and not pressing charges and
not pressing charges which was
immediately followed a few months later
by the uh manga Market's pressing
charges a very detailed and interesting
um uh I guess uh case and an indictment
by doj which fully understood exactly
what happened so to Heidi's Point not
only can law enforcement well not only
can you say later on that you sign an
agreement under duress so on the
attacker side like this this kind of
like verbal agreement that I'm not going
to I'm not going to um reach out to law
enforcement means nothing really um yeah
I'm not sure that's I don't think it's
legally enforcable in any way for sure
and then on top of that law enforcement
may get involved regardless of this
negotiation if there was any like let's
say there was a single Us customer that
was harmed by this compromise they can
swoop in it doesn't matter if the
project wants it or the attacker did
something else they can just swop in on
the case and take over it it's just a
matter of finding someone interested
enough try to introduce the fear we'll
see how that works in a
second yep so we've got Intel that may
identify them interestingly enough don't
forget we still have contractor or Dev
number five
that we still haven't heard anything
from so we're assuming that Dev number
five is our guy and we have a bunch of
different information on him we had his
ens address we have all the other
addresses connected to that ens address
as well as other social media handles so
we can definitely pull that uh pull on
those strings a little bit more to do
some analysis so we've certainly seen in
those initial messages where people
outline um basically like this is what
we know about you you just so happen to
interact with the centralized exchange
and you
know use that as kind of a leverage so
the more data that you know this is why
the investigation side is so important
the more data you can collect on the
attacker even if you do or do not reveal
it at the time of negotiation this is
your leverage that you can use to get
the money back in one of the case
studies that we actually have coming up
interestingly the um negotiators started
the conversation with the exploiter in
China
specifically to
intimidate someone's
asking should we even be negotiating
Oiler was intentional in starving
information that's a great question can
you elaborate on that one
more sorry yeah sorry so if you read the
blog post um I think the founder it's
it's really a really great story
of but I remember like the founder said
that he was very intentional in um not
wanting to publish anything not like
tweeting um so it's kind of like it's to
make the attacker feel like hey what's
going on you know like um and it would
kind of like cause him to make mistakes
I suppose so so that was the angle that
they were going
for yeah that's a great Point that's one
one possibility so would you still reach
out though or would you not even bother
reaching
out I'm not sure to be honest um if you
can have
a yeah I I I don't know I guess it
depends on the information that you
collect uh about the attacker if you can
kind of uh get a feel for his
personality on what might work um yeah
then maybe that would give you a better
Direction on what approach to take
well Oiler case was really interesting
right because for Oiler attacker it
wasn't just the the oiler that reached
out it was also like the entire security
Community kind of like reaching out to
the to to the person
um basically saying like what are the
consequences like advising them to
return the funds so there's a lot of
back and forth that you
can watch on chain to encourage the
return of funds
there are lots of people talking in here
about offering bounties I think Andrew
here has said that uh yeah tell them to
well we'll give them 10% they transfer
money back to us then immediately go for
the kill and press charg us for those
other 10% sounds
like I mean it this the the whole
negotiation thing is tricky like if we
call it for what it is this is this is
the web 3 version of ransomware know you
get attacked in the traditional security
your machine is attacked your data is
held at Ransom and then you pay a ransom
here your money is is held and there's
no reason for the attacker to return
those assets they just for for just kind
of like this warm fuzzy feeling that the
project promises not to press charges
that that's seems naive um but again I I
think one thing to and we can jump into
the case study I think but one thing to
just remember
when you do the negotiation think of who
is the attacker if the attacker is
someone that you know and is fully dxed
right if it's a let's say if it's a
malicious
Insider then you have enough on the
person to like offer kind of like hey we
can soften the impact of what's going to
happen by just like let's let's let's
walk away from from this so no one gets
hurt too much if it's a loan in it's a
you know a crypto native not a criminal
just just some person who is very clever
very smart got overly excited and you
negotiated with that person this great
likelihood they they don't know how to
La their funds or they're not proficient
at it and they understand what their
capabilities are they're very good at
hacking smart contracts but not they're
not criminals they may not necessarily
be as proficient in laundering and
opening up fake kyc identities and
exchanges seems like a hassle this uh 5
but uh seems like good enough a pretty
good life-changing amount of uh money to
come out of this if you're dealing with
a nation state good luck that's not
going to happen if you're also dealing
with a professional criminal group also
good luck that's that negotiation is not
going to really go anywhere so it's very
important you know how we did the root
cause analysis now you have to do the
kind of like personality analysis like
kind of get into the psychology of who
are you dealing with and craft you
message appropriately yeah are you
dealing with a person or group of
persons I know in the oiler case it
worked to their advantage that there
were actually three participants who
were the attackers and one attacker was
like I don't want to negotiate I want to
keep all the funds and then there were
the other guys who were like no no no no
no I want to be done with this I'm out
I'm out and of course that worked really
in their favor right if you have a small
team now I'm curious actually here we
all know stories of funds being returned
but for all the stories of funds being
returned what do you guys think the
percentages of fund of stories of funds
were not returned from
negotiations just
curious I think it's
we're all talking about negotiation here
even though it seems like many of us
think that there's an over 50% chance
that ain't going to happen so it's
something just to keep in mind
exactly um and the key like we wanted to
share just a few case studies like one a
success story and one not a success
story so one is a success story so
that's the recent socket compromise for
$3.3
million that was another infinite
approval one too infinite approval yeah
as always and then uh we can show the
negotiation that took place so this is
this is the one that Heidi mentioned
where the Outreach was immediately you
know they were they they were thinking
they're using the native language of the
attacker based on the information they
provided this is this is the translation
uh look at the tone and the language
used we understand you're responsible
for the socket attack we would like to
discuss a bounty with you and return
most of the funds to affected users
contact us to blog scam chat you have 12
hours so couple things to note here very
neutral you're not accusing anyone like
pure business transaction very calm like
acknowledging the fact like this
happened
some people go slightly On The Other
Extreme like they
say good job on hey white hat good job
on
attacking sorry uh you're you're very
good attacker like your skills are good
or
whatever sorry
so another thing to point out is the um
the blog
scan sorry losing
voice okay yeah the other thing that we
can point out here is the block scan
chat so that's one way that you can
start having that discussion without the
public seeing um and another thing to
point out as well is the time limit
sometimes um when negotiating it helps
to put a timer out there to be like hey
attacker you need to respond to me in 12
hours now there are pros and cons to
that because as someone mentioned in the
chat earlier sometimes they also need a
nap and setting that 12-hour time limit
it it seems kind of pointless if you're
going to go over anyways and you're
still going to negotiate with them it
seems like an empty threat if
anything Peter are you back
okay getting
cold sorry getting some cold here but um
so the other thing is they took this off
off platform they got it on
emails and finally acknowledging that
the funds were returned so that's a
standard flow so let's look at another
example so this is the kyber swap so a
few of you mentioned it already that was
the the
director that was a massive 48 million
compromise
and the negotiation there was much more
forceful so reached out to law
enforcement we have Footprints so very
threatening the way that it worked out
beyond that is it was a complete
breakdown so the attacker came back and
basically on the next slide demanded
everything like hey I want full
ownership of your company I want to be a
director I want full records and
everything else
so this is this is the example like a
lesson learned from this put your egos
in check this is a business
transaction it sucks the fact that you
even have to negotiate for this but it
is what it is so be smart be understand
who you're dealing with but
attackers they not only want to show
that they can steal that money from you
they also want to show that they're the
smarter person in the room so play to
their
egos you know validate their skill set
validate their uh control over your
assets and focus on your users that you
need to get the money back that's that's
the real win how you get there it
doesn't matter
yeah I think this case is really
interesting because it not just only bro
it broke down but I don't know how used
kyber swap is anymore after this so
clearly you know they didn't relinquish
full control over kyber but of course
this attacker the kyber swap director
has all the funds of kyber effectively
right and it destroys legitimacy
entirely in the protocol now um let's
move on to our second inject let's say
we decide to write the attacker saying
hey let's negotiate maybe over email
contact us here by the way this is what
um the I think the oiler team might have
done the reason why you wouldn't want to
post that on chain is then you get a ton
of different people reaching out to that
one particular email that's why we
recommend you know having a chat via
block scan so that not as many people
can actually read your message um and
therefore you're not going to get a nund
data by a bunch of spam so in this case
let's say we reached out and we
initially hadn't heard anything back uh
to our message we just said hey we'd
like to negotiate um and that's all we
left on Shan the attacker actually
responds with an encrypted message this
is on Shan right in the call data and it
links to a downloadable library on
GitHub for an encrypted chat and you can
see here what do you guys think this is
are there any risks with this should we
respond and who do we think the attacker
is here and you guys can check out that
GitHub repo I don't know if I would uh
download anything from it
though do not click the link
yes do not click the link I would agree
with you be very careful with
downloading that software it may be
malicious exactly so you might want to
do you might want to reach out to some
people who might be able to reverse
engineer it to understand exactly what's
going on there absolutely do not decrypt
using the GitHub link provided this may
be malicious code which may cause
further attack yes do not use that do
not Point like all the money is gone you
guys are paranoid enough this is
great or maybe we scared you enough by
now um it looks like um uh oh someone
has a great question any thoughts about
an attacker who might actually be
attending this conference like this and
learning these tactics as well there
might be a potential future attacker in
the room absolutely we've considered
this that's all I'll
say but yeah that's one thing to always
be paranoid about right um You may
invite people to your project in fact
that's one reason why with our founder
mode now um we even said hey you know
wait a second we all know one another we
all use our real real quote unquote
names someone can introduce themselves
as whoever right um You don't know if
that's necessarily true you want to
verify all of that um and even if you do
verify all of it be skeptical be
skeptical in this
space yeah all the money is going click
link
yellow yep be careful about the
software so someone said why don't you
click the link in a in a virtual machine
right money's gone anyways who
cares uh there's a lot of other things
that could be happening here um so I
think actually if I go to this um case
study example I'm going to talk through
the case study and we'll go back to the
questions because this is one's really
nice so of course course we know about
the oiler Finance hack um Oiler oh well
so it looks like my laptop went off okay
so the oiler Finance attackers were I
don't know what where they were in their
minds but they decided to donate um 100
e to the Ronin Bridge exploiter address
why well because they wanted to make it
look like they were like dprk so sorry
bro funds are gone like nothing to see
here nothing new um these were kids in
reality and they thought that they could
then get away with it because everyone
be like oh it's dprk whatever um well
funny enough 3 days
later that address decides to respond
and that
address posts this lovely message saying
hey why don't you decrypt your um your
address um uh with using or sorry why
don't you decrypt this message using a
private key belonging to this address
like it's so obvious what's going to
happen here by the way this attacker
this is where all the funds were sitting
so dprk was like sweet bro like we
didn't do the attack but we'll take your
money um well it's a win-win even if it
was a legit message what would they do
like come come visit us in North Korea
one way ticket oneway
ticket or or we just take all your money
so I regardless of the message of being
malicious or not like this is a win for
tprk good PR good PR and by the way like
when we were we were Heidi and I were
watching this hack live and when we saw
that those funds flowing to to a dprc to
a Lazarus account it's like you're not
we know exactly what you're doing you're
not you're not L we know how they
operate and you're not that like no
matter how much you try to misdirect we
saw right through that that's how you
know that's not a pro by the way like I
immediately was like oh this is kids
kids it could be one Lone Wolf kid or it
could be multiple kids but it's
kids so some people are saying analyze a
software to look for Clues on who the
attackers might be that's true that's
absolutely worth worth your time in this
case we kind of know who the attackers
are in that case study but yes you might
want to be doing that and that's the key
when you do this kind of analysis you
start building up profiles on the
attacker like what exchanges like to
interact with how do they swap what what
what are interesting components even we
even sometimes dive into the exploit
contracts themselves to look at like H
like I wonder like do they prefer to put
access controls in such a way or at what
point they like to put access controls
or how they exactly they interact with
all the different like exchangers or and
so on so every little bit that the
attacker does on chain is a signature on
them and once enough signatures are
built up you will start seeing patterns
evolved so we that's how we classify and
cluster together attackers laundering
tactics exploitation tactics like all of
that starts kind of creating a profile
we got some great troll questions in
here well now they know you're
communicating send them malware instead
um yeah I don't know if that's in the
steel Safe Harbor yet but uh talk to
them about that
that's a tricky one again there's
there's a line that we cannot cross so
we cannot hack back like
that's I guess depending what
jurisdiction you're in but from where
we're standing like we're we we just
can't do the same stuff that the the bad
guys can do unfortunately or fortunately
like that's that's the distinction
between us yeah and a lot of you guys
are saying well why don't you open up
you know um why don't you open this up
in some virtual environment or you know
gapped computer certainly you can do
that that's that's one possibility
there's one question I do want to
address here is how do we know that the
attacker wouldn't do anything else after
the agreement right and we don't and
that's why you're negotiating basically
on your back foot from the get-go when
you even bother to open up these
negotiations right like you've already
lost everything why should they even
talk to you and that should you should
kind of be going into it with that
expectation and I think one thing that
we usually find is that and it's kind of
what we kind of came up on here earlier
is that nine times out of 10
negotiations do not work out and they
actually are a waste of your time
because you could have been spending
that time trying to track the funds and
trying to stop the flow of funds so you
can actually get them back because as we
know at least in this case study we only
reached out to the attacker after they
started laundering all over the damn
place right the funds are effectively
gone and it's going to be really
annoying to try to get them back and the
attacker is not going to want to spend
the time to do that unless we have some
leverage on them be patient like we've
seeing that after the initial Outreach
to the attacker it sometimes takes a day
or days for them to reach back out to
you maybe they realized maybe they had
like a some kind of like ethical
Awakening or who knows um but regardless
like be patient that just because they
don't reply immediately they may reply
in a day or
so in the essence of time I think we
should move on
um this is the end of all of the index
congratulations the protocol of founder
mode is it still exists on chain it's
unfortunately been wrecked um and
there's still a lot of cleanup to do and
we didn't have time to really talk
through the cleanup yet but we should
probably have a postmortem regarding
the past six injects that have happened
so the actual EXP exploit right
exfiltration of funds laundering and
where we currently
stand sure um so just on the high level
what what is it that happened what
happened was and a lot of you were
digging that directions like hey like
where's that other worker why is he
disappeared in fact it was a dprk it
worker it was a malicious Insider who
performed an unauthorized upgrade they
already had all the keys it's just at
some point something flipped
they made the upgrade and started
trading all the locked funds after the
initial attack they also implemented
additional functionality into the
contract to also Target the users hence
why you you saw there was like an alert
that came shortly after the drainage
that hey now all the users are being
drained as well all the user
wallets yep the attacker then started
swapping stolen funds and bridging them
everywhere until until then they were
laed through a Bitcoin mix and we didn't
even get to that part because we didn't
even ask where the funds were we were
just like let's stop them let's stop
them that is such a great I loveed your
guys's reaction there because just
trying to stop the funds as fast as
humanly possible is usually best because
once they start splitting them out and
partitioning them it's hell on Earth
Track so the sooner you stop the flow of
funds at the beginning the better it is
now the team obviously then attempted to
negotiate with a bad actor but instead
they received a link from
malware so let's have a quick postmortem
what went well here what could be
improved what's left for us to do and I
know we only have 7 minutes left here
but uh let's go back to slido and go
into that postmortem section and start
typing out some responses things you
think went well what didn't go so
well to have a bit of a discussion
here but congrats for staying with us
for 2 hours through this harrowing
experience
yep someone's already written having
private key being able to perform this
upgrade shouldn't have been possible yes
if you have been to any security
discussion I think this Devon one thing
people say is multisig multisig multi
sigs and try to have like a multi- where
it would have been four out of five
individuals so in that case even if we
did have that one malicious Dev that
they wouldn't have been able to deploy
the upgrade unless they had three other
people that they had pulled the wool
over their eyes
of right it's hard to do when your your
entire team is five people but even with
five people you cannot have a single
point of failure you can't have a single
person that either mistakenly or like
don't even think about malicious inside
of just just think that someone may have
gotten compromised on your team a single
compromised Dev box should not result in
your entire protocol getting
trained people say rip fumo that's a big
one actually so the entirety of mode
chain is basically toxic now right no
one's on it anymore there are no more
projects building on there basically
that entire ecosystem is wrecked based
on you know what our project was right
it's something to really consider your
position right and the risk that your
protocol has on the space as well as
other protocols have maybe on you and
your
protocol don't hire Anonymous
contractors like even the contractor was
actually not Anonymous right we
mentioned that all five people in the
very beginning all five people have
their names it's just
that what are your practices to verify
what what kind of background checks do
you actually do to verify that the
person saying who they are really is
that person like for smaller teams it's
very hard to do like we don't have the
same capability well we have to build
quickly and you know we meet a person at
Defcon at conference and like hey let's
let's build something together we get
all excited but you know either they
were an intentional plant with fake
Identity or it could be that someone
just goes Rogue because something
happened I would say because of that
again you want to partition out
ownership you never want one person to
be the owner of for example everything
in your AWS Cloud you do not want that
you want there to be multiple people who
have access to things right you want to
partition out Keys as best as possible
that's one way to prevent this kind of
stuff sure it slows you down from
deploying things upgrading things but at
the same time it will prevent any sort
of instance like this from happening at
least you'll have one check check in
place I'm seeing a lot of yeah I'm
seeing a lot of stuff about pre- exploit
like just like the top question like
ability to upgrade what I'm not seeing
is I guess what I'm not seeing are
thoughts about what happens after the
hack the incident response process the
sleuthing and chain tracing there's a
lot of stuff like hacks can happen to
anyone it's what we do after the hack
happens how quickly we react to it
knowing like like one thing we could
point out I wish we knew exactly what
levers we can pull in the protocol so
someone said can we pause like that's
that was a perfect example like knowing
what are those levers that we can pull
to quickly start moving funds which may
be a risk quickly that's that's the
matter of are you losing just a few
million dollars or you're wrecking your
whole protocol so preparation in terms
of incident response when the incident
does happen preparation in terms of fast
reaction how to start a war room with
who and what are the participants and
who what are the responsibilities in the
War Room shaving up those minutes means
a completely different outcome for how
the hack is going to go some people were
also saying like we need to actually
have done more online sleuthing and I
highly agree with this a lot of times
when you're in a war room the sleuthing
is mainly happening on the smart
contract right seeing how exactly the
exploit occurred and trying to patch it
at the same time though you need to also
have people looking into who actually
deployed this contract what were they
previously doing did they leave any
other interesting tidbits behind there's
a lot of information you can actually
glean out of that you can see if they
also might have deployed other cont
similar contracts on mayet or other l2s
um and we could we also had the internal
information too about this Dev not
responding to anything but of course we
had their quote unquote real name right
we had their email we had all of their
different handles we could have been
doing a lot with that so don't let that
ENT information scare you use that to
your advantage and just I mean all of
you guys know how to look up things on
the internet I'm not concerned about
that here just use that to your
advantage and start
digging the stats on malicious I guess
the stats on funds recovery for
malicious Insider actually good knowing
who who actually perpetrated it and
leveraging that against them to be able
to return funds that's that's a
reasonable approach towards things
so someone said required North Kore
Korean attestation prior to hiring it's
funny um uh for those of you that
attended the defi security Summit I
think a lot of us have talked about that
um the problem is is the concern here is
that eventually even dprk is going to be
like yeah I hate Kim jugun right like
they're just going to say it um there
are a lot of other ways of getting
around this like even if you turn on the
cameras even if you you know require
real names there are lots of ways dprk
will get around this right they can hire
body doubles so to speak um they can do
all sorts of stuff like have fake kyc
documents prepared instead again
partition out key access that's your the
main way that you are going to protect
yourself don't trust anyone basically
even if they're your BFF
online cool it looks like our time's up
here today we want to do a Q&amp;A but um
hope you guys had a lot of fun and chat
with us in the hallway and most
importantly
take take these lessons home today and
start thinking what is it that you will
change in your product in your protocol
to respond to the things that we covered
today that's that's the biggest
takeaway that's your homework that's it
easy
should I
start okay so hi everyone um so I
prepared a presentation on uh mainly uh
using very ious tools for
auditing um so let's
begin you all see
my okay
perfect so let's maybe switch this
off hopefully that will
be okay um so let's begin at the top you
mind yeah yeah let's do
that okay so uh a little bit about me so
I organized PCO meetups in 2013 um I
worked on the nois Dutch X and the safe
uh around 7 years
ago and I've been doing the last around
five years I've been
doing uh security
audits um so I have yeah long trace of
uh various
bugs uh but to be fair a lot of the I I
felt my audit process I always felt like
my audit process wasn't really
sustainable um the the bugs required
extremely high effort and so two to
three years ago I embarked on a journey
to make the process more efficient and
uh here I'd like to present the results
yeah yeah
okay
uhhuh maybe I can just move move it
would would this be better
okay um
so I found myself working at TR bits I
got an offer from a check company called
Aki and so why did I leave so they
wanted to invest in
tooling and um and so that's where I
went and that's where we developed a
tool called wake which is also one of
the things I'll be presenting today um
so why why did I feel that was a good
idea so I I felt that there were things
in trail bits tooling that warranted
rewriting from scratch so I have four
things listed
here um so in particular
um this so for example slyther uses
Library called critic compile which
tries to figure out which framework
you're using and compile your project uh
but the issue is that it doesn't really
have control over the compilation so if
you want to for example build a language
server which will also be showing uh
then um you're at the mercy of the
underlying framework right so one thing
that you might want to do when you're
building a language server is you might
want to try to minimize the size of each
compilation unit so that when the user
makes a change in their editor like in
vs code uh the recompilation is very
fast yeah so all the other tools uh they
try to um they try to minimize the
number of compilation units so they try
to minimize the time for first
compilation whereas maybe you want to
try to maximize the number of
compilation units um so that you you
optimize for rec
compilation um so that's that's one
thing that I'll be I'll be showing today
uh by the way if you guys have any
questions then feel free to jump in um I
can
answer uh on the
go um so I think fuzzing in our industry
we call it fuzzing but that immediately
evokes it's something that has to run
very fast and um actually the way we do
fuzzing is not by just sending random
data uh because the reality is most of
it would fail right so you try to be a
little bit more intelligent and you just
send uh like um the appropriate
functions so the appropriate ABI
encoding uh but even that is mostly
going to fail because if you try to
transfer token without sending an
approval first it will always fail so
the way we actually do fuzzing is we
it's more like modeling uh so we uh
design flows or uh or rules as they're
called in various
Frameworks um and so when you think
about it like that when you think about
it as modeling the system uh then it's
much more uh better to write it in a
language where you can write it really
fast right so my favorite language for
modeling stuff um is python so I felt
that it was a good idea to uh have a
framework where you can model uh
economic U and financial blockchain
systems in in that
language um on the static analysis side
so um I felt that for example sther
doesn't merge compilation units so this
is really really tricky because
you might have like this diamond pattern
right where some Library can be compiled
with multiple solidity versions so it
has the appropriate
pragma uh but then it's used in two
different contracts that pin that
solidity version and so as a result you
have a valid project you'll just have
two different compilation
units and so this is kind of a problem
because the way solity works is it gives
you this huge Json and it just numbers
the nodes one by one
and so even if it's the same file let's
call it lib um it's going to have
different IDs in two different
compilation units and the reason for
that is solidity doesn't go file by file
it just goes node by node so they're
going to end up uh as different
indices and so this is actually kind of
a big problem so if you want to create
the illusion of a single compilation
unit of a single unified thing for the
user you have to merge all of these
compilation
units um and slitter doesn't currently
do that so um that's something that I
think should be
done um and then struct member
references I'm not 100% sure about this
but uh I was unable to find a way to uh
find references to struct members only
struct like
variables there's no there's no model
for the a so it's all just dictionary
access whereas um if you create an
actual model for example with the
library like like pantic uh then you can
catch your assumptions about the model
faster and then obviously I wanted to
use a lot of cool new libraries like
rich and click and networkx Etc I think
networkx is used in
instead um after about a year after that
I uh started researching tooling
full-time and so I'm going to talk about
both things General tooling and wake um
so disclaimer oh yeah I was actually
messaged uh by somebody TR bits um in my
talk it says that I was a lead auditor
um so I was a lead at audits uh but they
actually turns out have a role called
lead auditor so just wanted to make that
clear um so uh you guys can join
groups um so the thing is uh not
everything here is done in fact almost
nothing is done um and so I plan to uh
update you guys right and so the best
way to do that I think is with a uh with
a telegram group because I don't want to
like take anyone's emails stuff like
that so I'll post to this link um you
know as I as I start publishing these
things so if something you like here um
you can find it out
later and also I'm as a freelancer
looking for Audits and other engagement
like uh building tools but mainly my
specialization is yeah Audits and and uh
security and developer
tooling um a lot of things I'll be
presenting here involve a lot of
external software so be very careful
with that um so be very paranoid so
before you download anything um you know
make sure to check on the on the uh on
the the developers um me listing it here
does not mean it's safe um but that said
I do try to keep in touch a little bit
um so most security companies will tell
you that you need to keep all your
software up to date all the time uh
that's true for things like operating
system and stuff like that but I found
that with some of these tools that I'll
be showing today since they're Indie
Developers
actually the opposite is true you want
to uh pin your version and then ideally
check on the developer make sure they're
still active before you update it
unfortunately what happens is and I uh
it's even in this in this talk we'll see
it um tools get bought by uh Shady
people right and then you don't know
what happens okay so let's actually get
into it um so yeah uh the the plan is
talk about mainly two things uh wake and
general tooling I personally really like
when people talk about their config so
this is sort of my
uh my uh contribution here okay so um
let's talk about keyboard layout first
so um I tried several uh keyboards I
ended up uh using one called The Glove
at um so the thing about these things is
they're
ortholinear um they're split and they're
programmable um that said I found
that uh you don't want to presumably get
as much of the programming into the uh
keyboard itself because then it won't
work when you're using the laptop
separately so you want to get as much of
the programming on the on the OS level
which we'll discuss um soon as well
presumably um so for the keyboard layout
um I use a a layout called vorac um and
that's the thing I didn't know about any
of these things just a few years ago um
and so as I sort of started diving into
it
um so this is how it looks um so the
idea obviously is to minimize travel of
your of your
keys
um
yeah um so some of the things I learned
along the way oh yeah and then the third
thing is um what for example Apple calls
human interface modifications um and so
for that you can use a tool called uh
Carabiner so let's actually see it in
action right here um so the way it works
is is it creates a Json or you create a
Json and it reads from that Json to for
modifications uh and Json are pretty
hard to create and so you have a tool
called Goku where you can write it in a
in a more suent language called um edn
and so you can use
that uh so some of the things I learned
along the way uh don't have too many
layers for example for the programmable
keyboard um it's nice to have the same
key on different sides of of the
keyboard uh redundancy is fine it's
easier to learn something where the keys
are closer together than before than if
they're like really
far um so the main the main two uh
layouts that people have apart
from uh Cordy is dorak and KAC so the
reason I didn't go for KAC is JK which
is a very popular key combination
obviously um and so as a pure pure
chance in vorak they're next to each
other which is just I guess pure chance
um whereas in colak they're not so if
you want to you know uh be able to use
uh those two keys uh very efficiently
then then uh that's something to
consider uh one thing that's really cool
which I guess I didn't know is that it
works on pretty much every single uh
various
device um I wouldn't I would say don't
make your own modifications
because then you have to make them
across all the devices which can be
pretty
tricky uh dorak does come with a
completely different punctuation so I I
do remap it to to regular ones and then
this one is was fairly important for me
is um I remapped all of the command plus
key and Control Plus key uh to their
original uh
values yeah
cap yeah to escape yeah yeah yeah yeah
uh remap caps loog to escape it's way
easier to go to normal mode MIM instead
of like moving my pinky to the end of
the key yeah it's feel nice yes yes
absolutely agree in fact I have the same
exact thing yeah so I have the same
exact thing um so is vim fine yes in
fact for some reason I think Vim gets
even better uh with with these uh
combinations just one more point on this
if your Mac OS user Mac OS does have um
uh a key layout where for command and
control it goes to query but actually
it's a buggy layout um so I wouldn't
recommend that so I would recommend to
do this remapping either on the level of
the programmable keyboard or on the
level of uh the cbin or the hid
modifications it took a very long time
for me to learn uh very long time uh
whether it's worth it or not um you know
there's obviously massive advantages uh
because yeah typing is something we do
very very often um so I think it was
worth
it um so Carabiner is the the main thing
for uh creating these modifications on
Mac OS so you can create a hyper
layer uh for
example and
um yeah I think um I think we can kind
of move
on um so for examp so what's a hyper
layer so it's when you hold one of the
keys and you can access a whole another
layer with like arrows and stuff so you
can have like a systemwide uh Vim setup
basically which is pretty
cool um don't spend too much time on
this obviously once you learn it use it
I haven't touched my config for many
months now which I'm very proud of um so
one thing I didn't know also uh which I
might have just considered if I was
starting again is there's also there
already uh some existing
layouts um so you might want to check
into that before you you go into I'm
planning to publish my layout dig well
um So
currently uh I have caps lock bound to
uh escape and when you hold it you get
the hyper
layer um and then therefore I don't need
Escape itself um so that switches to the
last app which is really really
cool um
yeah let's move
on so actually all of this started in a
tool called Alfred originally where uh
it was all worked with command um then I
moved to the keyboard then mov it to the
alt or option modifier but really you
want to use a custom layer so that you
don't block obviously the um the keys
with the with the modifications okay
cool so let's so that was around the the
keyboard so let's talk about some other
apps um so vimium is a Chrome extension
I in particular use the one called
vimium
c um so what does that do so it allows
to let's find something I don't know
like here allows you to scroll it allows
you to to search right open your uh and
then allows you to also uh like use your
keyboard to open links uh go back and
you can like uh configure all of this in
the in the extension unfortunately you
can't configure it with a text file
which would honestly be the
best um so if you're on if you're on and
this one is for any operating system
obviously since it's um you just need a
chromey browser if you're on Mac there's
a app called home row which does the
same thing but on the operating system
level so this is how it looks I just and
then you can you can press anything from
there
um there's also one called shortcut but
I personally like home R better it
doesn't always work for electron apps um
scrolling you can also do with hom roll
so you can scroll anything very very
useful
stuff so many people use trackpad for
gestures um so with an app called magc
gesture you can actually have gestures
uh on your mouse so I have a lot of
these for example uh dragging to the
right will will dim the screen I don't
want to do it right now so I'm not going
to do it
um so this is the one that you want to
be careful about so um you can so this
is an app that does several things so it
allows you to minimize your menu bar and
then you can search it uh you can search
it like this and you see all the items
here uh but this is one of the issues
right is um actually recently it was
acquired so before updating you might
want to uh check the uh the current
status um to be fair yeah so there is
there is a one an open source tool that
um that I want to migrate to
soon um
okay uh
so yeah um let's let's let's move
on okay so let's talk about Hammer spoon
um so if you're a Mac User this is a
very very useful thing um so the idea of
this is they expose uh for example
Objective
C uh Mac OS apis um in a scripting
language in particular in
Lua um so this is also used in neovim
yatsi
MPV um if you don't like Lua you can
also use uh teal which is meant to be a
typed version of Lua or fennel which is
meant to
be um like a closure or list
uh
syntax um I found that with teal people
don't really use it uh because instead
the most popular Lua language server has
support for types um so people uh use
that for example in the in the neim
community um and then other obviously
honorary mentions are uh keyboard
Maestro rcast and
Alfred um so uh window Management on Mac
OS is very very hard
uh but I'm pretty happy with the
solution so far so I can show
you so what I do is I take the function
layer and I bound it to open
apps now that sounds great but you also
want to like retain the for example the
volume keys
right so you can do this all with
crainers you can say some keys will uh
open apps and others will remain the uh
the media keys um so yeah I just have
browser chat GPT and terminal most the
apps I use the most by
far um
yeah and you can go really crazy with
this um so in case anyone's interested
um my current setup so you can combine
the F keys with various modifiers right
um so I have the following combination
so uh if I press control then it sort of
switches to a different app app so for
example Arc or Chrome YouTube music or
Spotify so that's all done with control
then shift as a
modifier uh forces it to be on the
current screen the current
monitor um and then command and command
does a different monitor next monitor it
loops around and uh shift command does
uh does previous
monitor um so what I call Window
Transformations I launched that with
command M and that allows me to do stuff
like this and if I have multiple
monitors obviously move the window
around or even focus various monitors uh
all of this stuff is either public or
will be public soon so um if anyone
wants to use that they
may um okay and then I also have this uh
launcher at command control a
uh which is basically like meant to be
the best way for me to uh enter into all
of these commands so once you start you
know writing all these commands you
don't want to keybind everything some of
it you want to
keybind uh but maybe some of it you want
to uh you want to keep as um as like a
command like a searchable command so
some examples of what I have there I
don't know if I have some examples here
oh yeah I do okay so for example
inserting unic code keys so for some
reason uh keyboards don't have an m M
Dash and so if you want to insert an M
Dash you kind of have to do it yourself
and in view ofm it's it's uh shown with
a monospace font obviously but if I use
another app like telegram it will be an
actual
mdh um I also have some really cool
clipboard Transformations so most people
would use their text editor uh like to
write a you know script in ym or
something but if you do it on the OS
level it means you don't have to you
know you can use it in any app so I can
like um I can
um um I can select some text and let's
let's copy it and then I can say like um
I can um here I can add or remove four
spaces which is I guess the initation I
use for uh for most things but you could
obviously add anything else uh for
example another one is if you have like
if you have some if you have some text
here and you want to copy it then you
want to get rid of the everything before
the pipe right so I also have a I call
that one remove pipe charart right and
then everything else beill the pipe as
well um let's
continue okay um so where were we again
so we
were okay and then um some things I want
to add to the launcher is uh controlling
timers um so we'll we'll talk about uh
two timer use cases in a second so
timers are
um hammer spoon's way
of like do right so this is like Hammer
spoon's way of being able to schedule
stuff so this is an app called Dash
allows you to get like documentation um
for various things so I use it for like
python documentation L documentation
hmer spoon
documentation so it's offline and it's
you don't have to go to the
browser okay so brightness so this thing
is very important for me because I have
a thing called tunnel vision where I
just focus like so much on one thing um
and so what brightness does is every 20
seconds it dims the screen for one
second so this was actually very
important for me to uh get rid of that
uh that status
um okay so for
notes for notes um I used to use an app
called log
seek um and I stopped using it in favor
of as you guys can see actually in the
screen right over here uh just neovim so
it's an asky doc based
setup and it actually works really
really well uh so yeah it's a custom
custom Newen plugin and it works really
well so what do I need for my notes so
you guys can see the highlights that's
pretty cool so uh whichever whichever uh
bullet point you're on currently it
highlights those stars all the previous
stars and then sometimes it even and it
also highlights all the parents yeah so
very very easy to to see like the entire
path all the way to the
top um and then obviously the other
thing you need is you need to bind uh
stuff like when I press o which in Vim
normally creates a new line you want it
to create the you want it to create the
Stars at the same time right now when I
press tab you want it to indent right
and then shift tab so like basic stuff
but turns out like that's all you need
for a really really good note system and
if I ever wanted to publish this online
asky do obviously has a HTML conversion
so uh that's very easy to do as
well um so this one this one um I
haven't published yet uh but yeah we'll
be publishing um soon um so it's based
on aski do um so that's the name of the
the format I'm using and then also the
the tool that can generate the HTML uh
export anyone else have any other
questions so
far how are we doing on time okay W
already 30
minutes okay okay let's move
on yeah so one thing I learned about the
notes is uh it's very important to have
fast access to them uh and so people you
know talk about all these systems like
zedel Casen and that kind of stuff so
for zle Casen in particular I feel it's
a little bit outdated um I get a most of
my knowledge these days from Chad GPT um
and in fact it's much faster than than
um than like maintaining notes so um but
still Fast Access is very important um
so when I was using Loy got this thing
where I could search all the notes so
command control n now I can uh search
all the notes and then it would open it
uh in the program uh just by hitting
enter it also shows me how many lines
words and characters are um so this is
just a shell script that uh outputs the
the data in the in this like Hammer
spoon
launcher okay um HP also gives you
access to uh programmatic access of your
a of your menu bar
and so I mainly use that for three
things one sec I'll take a little
break some
so the first one is for showing me the
layer of the programmatic keyboard um So
currently we're in normal
mode and um so this is really really
cool how the keyboard if you change the
layer of the keyboard so the way I do
that is it sends a private key I cat it
in uh
cabiner and I use that to call
hammerspoon a particular hammerspoon URL
and that changes the uh the menu bar so
I can see very visually on my screen
always the the layer of the keyboard
you're currently
in um and then number of windows on each
screen um So currently I have 23 windows
I can actually even click on it to see
all the windows although Arc is kind of
misbehaving it looks like right now and
then something I did actually quite
recently which is pretty cool so if I uh
let me see if this actually works uh
because I haven't tried it uh just on my
uh personal like laptop just by itself
uh but um so toggle uh for me is the
best tool for like counting
time and yeah so it's it's worked really
well right now so when I press command
control and then the pause button or the
play
button it resumes the last
session so the last session is called
the last project is called Defcon the
last thing I was doing was preparing
this
presentation and it does actually uh two
more things it also shows me the current
uh the current time today and the
current time in the last seven days um
so this is a visual representation to
make sure I'm always counting the
correct project that I'm working on and
also kind of a motivational thing um you
know I always want to be obviously above
like 20 or 30 hours uh in terms of work
done in the last seven
days and like daily I want to get to you
know like whatever like uh five six
seven hours
whatever um and then obviously if you uh
I can also launch the app right um to
see like all the details and all the
projects and stuff like that I can show
you guys how it looks if you're
interested so you can see like the
calendar here yeah and the list and all
that stuff so that's for me the the best
one um so should we keep the time
counting now or should we stop it keep
it counting just to get more more hours
okay so obviously hours are not
important um the output is important but
uh from personal perspective uh it might
motivate
okay um yeah so that was the menu bar
okay so let's talk about let's talk
about terminal emulator yeah so to be
clear I went from a person who mainly
used vs code to somebody
who terminal emulator so is it better um
um like I think it is obviously uh but
there's kind of a learning curve right
so there's there's a lot of stuff these
these programs they're they're pretty
simple and how they work it just bites
in and bites
out uh but they're also not so Advanced
so even to this day the most modern T
like for example Kitty cannot actually
handle well uh multi Cod Point
graphes yeah
um or and and and the the editor uh
can't either um so for example if you
want to use
emojis yeah let's let's see some emojis
um let's for example go to wake um and
then let's like open some random
file okay so this is something I'll be
showing in not
long um so this is how I read code uh
these
days um and so it's it's based around
emojis um to a large
degree um so they allow me much faster
to see the uses of a particular
identifier because every identifier has
a unique
emoji and then the colors are also uh
every identifier also has its own
color um so like yeah I mean I was going
to talk about this later but might as
well talk about it
now um so in syntax highlighting we do
the opposite of what we want we
highlight useless words like class def
try and four and we don't highlight the
important stuff which is uh which is the
identifiers and their uses um so this
flips it
around um and I think I can also try to
decrease to increase the contrast so
let's try to do that let's see if it
works um H and then let's
okay so it's yeah this is pretty
experimental it's only like implemented
in a few days so it doesn't work right
now the increasing of the contract which
is fine um so basically you can also
fiddle around with the contrast
obviously if you have higher
contrast uh then uh you can see the uses
of your identifiers much better um by
the way it's a it's a pretty
uh uh it's a pretty small screen right
so we can also like split it like this
and bind it
together
um but then if you have very high
contrast it's also like visually
striking so it's not that great so I
have like pretty low contrast uh which
makes it very very pleasant uh to
read yeah so um I I and then I'll we'll
have another example where we see uh
where we see emojis in practice um and
the thing is you have to pick among only
the ones that are single code point so
they can be multiple bytes they just
have to be single code Point um and so
there's there's a lot that you can't use
for example you can't use flag and other
ones um so I have it in fact I have a
whole list of all of the all of the ones
that are single single
uh code
Point yeah whereas vs code can handle
anything
so uh this actually is not meant I'm not
at this point meant to talk about Kitty
here the terminal emulator I'm using
that actually comes
later um so at this in this section I
was actually meant to talk about uh the
hammer spoon uses of Kitty uh but let's
talk about that a little later I'll just
scroll through everything right
now uh yeah I mean
um like just last thing I'll say like
context if you want a a better version
for command tab then check out this
app yeah and I think that's that's
that's enough I spent too much time on
window Management in the last uh few
years so uh what I learned using
hammerspoon so as with any other thing
you want to have a very fast iteration
process so for me instead of reloading
the entire thing every single time by
clicking reload config or even like
having a key binding I find it much
better to just reload one single
module um and so the way the way you can
do that yeah I mean that's it's pretty
obvious um you can interact with a CLI
or like with a with a uh with a prompt
thingy instead of with
this uh but it does not support readline
so readline is a very popular C library
uh that is used in many various
prompts um to to handle text essentially
so for example it's used in if you just
type in
Python um that actually uses read
line unfortunately yeah so this actually
uses so you can very quickly jump
between the
words um so Lua by itself or HS does not
unfortunately use read line yeah so you
can't quickly jump between words um
which kind of
sucks and
you can't really embed it you can't
really embed Hammer spoon in an external
low program uh which is unfortunate
because then you could use Lua P which
is the uh reline version of the Lua
console um and then interact with
hammerspoon that way but unfortunately
there's not really a way to do that
because the binary itself is like um
crosslinked with u with Mac software so
that's pretty unfortunate right
now cool
okay okay so let's talk about termal
ulator so um I'm a big fan of this one
called Kitty um so it's written go and
Python and C uh by a guy called covid
Goyle goyal he's also the author of
caliber in case you know that uh that
program um so my view on things I write
it right here is system software versus
user
software so if you're writing system
software like ZK or an operating system
or whatever you want to use something
like rust um when you want a fast
iteration
language or you want to write like
scripts or modeling then um something
like uh Gore python is great um
so yeah um it has things like you can
uh launch a console you can uh for
example if I have some output let's say
uh where was my let's say we uh for
example have some some file
here so what does ef and CF do that I've
been using uh recently so they they um
they look up uh they use fzf to look up
that particular file and they either
edit it or CAD it
um so CF let's do server so it's going
to it's going to C it except uh it's
going to use bat for that which also
gives me syntax
highlighting um and then and then uh if
I want to just use this particular
scroll back and like scroll through it I
pipe it into less I can also do that
with h so this is this is all supported
out of the Hood um I didn't do any
modifications for this one so um you
know don't read invent the wheel uh if
you know don't don't allow users to like
search the scroll back like create a
whole new UI when you can just pipe it
into less and have them search it uh you
know with uh with less and then you know
you can search with with less that way
you can also modify less um
so um so you can uh do that with
something called less
key yeah so you can
also you can also uh you can also uh
modify the the user shortcuts um in
terms of a pager like a lot of people
are working on a a pager right now but
they're not done yet so there's a lot of
things that uh Les doesn't have that we
might want from it uh but it's it's what
we use um right
now but the the really coolest things
are for example the keyboard protocol so
the idea here is uh we're all um
using uh like this is the way the
terminal communicates with the app that
you're running for example your shell or
your editor or whatever um so we're
using standards from like a monitor in
they for example can distinguish between
Tab and control
I yeah so uh some of you might have
encountered this in the past
but uh the way that alt and control were
traditionally handled by uh terminal
emulators between modern before modern
standards Like the Kitty uh keyboard
protocol is the following so when you
pressed alt or
option um it sent an escape and then it
sent uh the key and if you pressed
control and a key it actually just
subtracted
like 128 from it I
think and so tab which is right over
here um was actually the same exact
thing as control I um so a lot of
there's a lot of questions on the
internet like how come I can't bind
control I to Something in Vim or how
come it's doing the same thing as tab so
this is the
reason um and so let me show you the
yeah so this is
it so it's called the kitty keyboard uh
protocol and so the idea among other
things is to distinguish between those
things okay so it has uh it has uh it
sends a particular bite sequence when
you uh when you press a button when you
release it and it sends you the exact
information so as an app devop it's very
easy for you to to handle that and it's
currently supported in actually many
many places not all of them have full
support uh so for example NE ofm is is
getting support but doesn't like have uh
full
support just
yet um the only thing that that I feel
it's missing so there might be like a
distinguish between left modifiers and
right
modifiers so that's that's a bit
unfortunate you know but um it is what
it is so left control is the same thing
as right control right now there's no
distinction and so if you want to see an
example of
the of uh the the protocol uh let's see
if I can I can do
yeah so we want
to okay this one perfect sorry not
except not unit code input but I think
it's called
showkey yeah perfect okay so here you
can experiment with this for example
when I press a it sends right the bite
sequence corresponding to a if I press
command a it sends this is escape and
then these are the uh these are the the
uh the bytes that uh you can also figure
out over
here so this is very very useful uh
because I use this uh to create
something which is really really cool
and that is uh having full Mac OS key
bindings in basically every single shell
app that I use so what do I mean by Mac
Keem binding so um on your computer
you're used to that if you do option
left it jumps back
award and um and like
command uh
a like command Left Right Command right
command backspace like you're used to
these things you probably use them um
and especially if you have a hyper layer
right like we talked about earlier then
they just become much closer and you
just end up using them all the time
right but you don't want to have this
distinction obviously in vimi can always
go to or even in your shell you can
always go to normal mode that's true but
sometimes you end up pressing it because
you're not aware that you're in a shell
app right you think you're still in the
browser or something so ideally you want
these key combinations to work and shell
applications as well and so that's a
little tricky so how do we do that so
the reason It's Tricky is um K is
actually very intelligent and it
actually figures out which app you're
using and whether it's going to support
the uh the protocol and if it doesn't it
reverts back to the old
standards and so what you want to do is
you want to force it to use the new
standard and while we're at it we might
as well just uh pick like random keys
that we're going to send okay this is
not necessarily I could probably get rid
of it but it works and so I'm not
changing it so what I do is I send f27
F28 f29 f30 all the way to like
F35 and then you can catch it on the
layer of the app and handle it there
yeah so you can do this
in currently in so this currently Works
in everywhere that read line Works in
which we talked about so for example
bash or the python console this works in
zsh and uh let me also should say
because it's not it's not obvious which
of these required Uh custom handling and
which of them didn't so readline
required custom handling so that one is
uh is interacted with with
um uh with with a file called input
RC there we go and so this is how it
looks if you want to if you want to get
it to work in bash or in the python
console it's just this uh let's look at
how to do the same thing in
zsh so that one is a little little
different um so let's see if we can find
it uh how should we do this ah here here
it is so this is how you do it in in zsh
yeah and I mean the other ones are
similar as well uh so readline which is
uh new Shell's a version of read line so
in Rust it actually supports it out of
the hood and so this is available there
out of the hood
um and so if you use New Shell you
can yeah uh okay so it doesn't work
right now um oh yeah because okay okay
it doesn't work right now actually I had
a pull request to NOA which got merged a
few days ago so I guess I'm not on my
version I'm on their version right now
because it's not working uh but uh this
stuff was merged into New Shell as well
a few days ago um so this this also
works in New shell uh same with IPython
created a PL request recently that was
also merged um so let's see how it works
IPython um so let's for example go
somewhere here and let's get rid of
everything let's go back
to yeah so you can type some text and
then you can yeah so this is this was
very important for me because it was
extremely
frustrating um when I'm used to this
working in most places and then I'm you
know doing my happy
uh you know interaction with wake and
IPython you know stuff like that and
then you press one of these keys and
sometimes what you get is it clears the
entire input yeah so this is very very
frustrating so I spend a lot of
time making sure this works everywhere
and yeah as I said uh two of my PRS have
been merged recently so now it works
also in New Shell and in IPython um and
for a long time now I've added work in
new of them insert mode and command line
mode so let's look at uh command line
um so it works perfectly in command line
mode and I can also do backspace
obviously right and then in insert mode
it works as well there's a little bit of
a Flash and I think I know why the flash
happens but it's just not a super high
priority to fix it right
now okay
so um I think we're in the foundation
section in terms of like um in terms of
like you know everything I learned
regarding the
terminal
um wait did we accidentally I think we
skipped some some
stuff um okay so yeah keyboard protocol
so that's where we were so uh supporting
a lot of apps including New Shell NE
stuff like that image protocol also
really cool um so this is also supported
in for example natively for example in
so um so you can so you can have a file
manager like this and it prev
previews uh it previews the images uh
for you inside from emulator uh
automatically this required zero zero uh
effort from my part it just does this uh
does this under the hood because it
supports the the keyboard protocol uh
the image protocol uh the app signals to
to kitty that it supports it and so it
can ask for an image and kitty can give
it that
image uh has a text based config uh it
has a remote control which is really
really
cool um and uh allows you to write
python based plugins um for example one
thing I wrote recently is this tab bar
customization which I really like so the
second letter always shows me the uh the
app basically that I'm using but like I
limit it to just a few so for example n
is neovim L is less Y is yatsi and then
the first character is the first
character of the current
directory um and while we're talking
about this let me show
you um this thing I built a few weeks
ago I call it uh kills Kitty
LS um so this I really really like so
this shows me all my uh terminal window
Windows let's Zoom it up a
bit it shows me the current running
program shows me the current
directory um I'm using a tool called
macup for syncing all the dot files
through Dropbox across all the devices
and then it shows this is very important
if you're doing some like uh like kitty
work it's always really frustrating to
like not know the IDS of things and
stuff like this um so uh what I do is I
give the full full Json it's scrollable
also the full tab also scrollable full
OS window also
scrollable um and then obviously I give
the name so they're all called DC which
is the current project I'm working on
Defcon and they all have an ID uh tab ID
and then uh obviously uh OS sorry uh
window ID and then this is the ID on the
OS window level so if you want to do
things like maximize the window and
stuff like this you also need the uh the
sort of Mac OS ID so that's the that's
sort of the Mac
ID okay so uh where were we
um we're kind of uh jumping up and down
but I think um I think I'm doing a
fairly good job like uh giving structure
and stuff so let's just
continue um so we might come back but
let's let's talk a little bit about
command line tools so one thing that you
might want to check out is this link
right here you can also yeah
um you can also open it in the
browser yeah so the idea is like there's
a lot of advantages right to trying out
uh new stuff and uh this is the best
article for like uh doing that that I
have
seen okay so currently I'm using Zell
but I plan to migrate to Newell so
Newell is really really cool so let me
tell you two main advantages
um you don't so in traditional Styles
like all types are strings right and
that's kind of annoying because you
might want to have a dictionary or a
list and it's very very painful to keep
on decoding and encoding everything as
like strings and so new shell is like
you don't have to do that you can use
your strings if you want uh but you can
also uh use more High
types um so you can call functions just
as you would external programs but now
you can also pass in uh things like
dictionaries and
stuff uh but the honestly the main
advantage I personally would say is it
makes it very easy to create shill
programs that's that's for me personally
the the largest
Advantage um so for me like using it
first as a scripting
language uh um and then migrating it uh
to use it also like interactively is I
think the the best approach and while I
was using it I
um I made a a shortcut called
n which just runs
the uh just runs the command in New
Shell so I can very easily interact with
it uh from from zsh so that's something
that helped uh me a lot I don't have to
go to the interactive session and the
way the function works and you can ask
Chad GPT for this to work it's possible
is it works both like if it's if you
pass in a string and if you pass in a
list of positional arguments it works in
like both
cases
um let's where should we go let's let's
jump here for just a
second uh
so for listing director I used to use a
tool called
LSD uh the issue with that is that it's
it's a little bit nicer and
EXA um the issue with that is that uh
Mac also has a a thing for last modified
for files and for example if you want to
sort it by last modified lesd
unfortunately doesn't give you access to
the last modified thing um so I had to
migrate away from LSD and So currently
I'm I'm using a tool called
EXA um and yeah I mean you see it when I
do L you can also see it when I do F
that's that's a tribbie and
moreover um this stuff is
also uh also available as a CD hook um
so you can do this in D you can run C
any program on on a CD so if I CD it
automatically lists and so um for
example um I can with Z oxide I can jump
to a directory and I can have it give me
the tribut and if it has a read me it
also shows me the read me really really
nice okay so where were we over here
um yeah yeah we talked about all this zo
oxide um allows you to jump between
directories um super
quickly um let's get rid of some some
tabs here just to make it everything a
lot simpler there we go two
tabs um so where were we again
uh oh yeah yeah so this and then you can
also use zi um and it it it pipes it
into fzf and you can see all of your uh
solutions that way um so you can and
then obviously if you if you press enter
I pressed contrl C but if you press
enter Then you can uh CD into that uh
directory okay I feel like we went a
little quite far with this so let's
maybe back up and see if we missed
something from above let's split
it um okay so we talked about Kitty
right so let's let's talk about Kitty
and hammerspoon integration so normally
the way I work is I have my laptop and I
have two
monitors and um the convention that's
worked for me is I name all of these
Kitty Windows as position and project so
for example there will be L Scratch R
scratch L Defcon R Defcon and I have a
shell command called Kos to rename right
to name the the OS window
essentially um and so and then you can
bind command control tab to switch
between Windows of the same
project very very useful um and as we
already said command plus an F button
goes to the next window of the current
APP and there's also command tab which
does context remember the context app we
mentioned earlier but just for this
current APP so all in all I have three
ways to navigate to Windows of the same
app very very useful it sounds trivial
but it's actually very useful um so and
let's let's so let's write them out over
here so command F3 to go to um to go to
next then we had command control tab
next window of same project so this is
next monitor yeah I mean this stuff is
meant to be as an inspiration so it's
like not really important that we get it
uh exactly correct and then obviously
there's also like command tab which is
just uh just
contexts uh switch Yeah okay um and so
that allows like really really high
level handling of all the windows so for
example command control e uh shows me
three things it shows me all of the
projects I'm running right now uh we
created a new window recently so let's
let's give it a name let's call it also
let's call it RDC or like let's call it
also DC just like this or maybe like 2dc
or something right and so now let's
press uh command control e so now we
just have one project in the first
window I have two kitty windows and in
the second one I have one kitty window
um the second thing that allows me to do
is to create a new project
interactively um I hope this will work
I'll show it in a second um it's fairly
recent Edition and then to open any of
my safe projects so let's try to create
a new project
interactively um I can also get there by
doing command control shift n so let's
do it that way command control shift
then so what this is going to do so the
idea of this is the following once you
start to think of your windows as
projects let's say you want to start an
audit you don't want to have to go into
one of your existing Windows to get
clone it right you want to you want to
create a you want to sort of do it both
at the same time you want to get clone
it and create the uh the window so the
way I do that is the following so first
the first thing that
happens is it creates a new window
called new project and it gives me two
tabs there so here I can do my good
cloning okay so here I can
do uh you know whatever I can do my G
clone and
then um
it uh creates this this toml
file and as soon as I close it it's
listening to the
process and as soon as I close it it's
going to open the the windows to work on
yeah so this solves the problem that you
can both do your cloning and you can
launch the uh the windows so let's see
it in practice so three two one close
it and Bam so what did it do currently
the way it's configured is it opens one
window called LR and then R PR and
obviously this is customizable we call
our project P so that's what we get as a
result but we could have called it
something else so um
yeah okay um so where were we oh yeah um
convention names Windows usually by
position project working setup to
monitor
Okay blah blah blah blah blah blah here
shows both running projects and then
obviously if we also save the project uh
oops I accidentally did the new thing so
it's going to launch it again three two
one bam so let's close it all
again um then we would also if we also
saved it then we would also see it here
in the save projects okay let's just
jump through this because I want to move
on so let's see uh this one we talked
about create new project uh
um uh and then and then this one we also
talked about so uh this is the one that
has the web server and it gives you the
view and it allows you to uh just by
clicking it now it's going to focus it
hopefully it's going to work let's try
it it might not 3 two 1 it worked okay
so it focused it let's try with the OS
window 3 two one okay it focused it so
it works um also you can also actually
close it uh that is not implemented yet
yeah it's it's not hard it's just a few
lines of cod just haven't been done yet
so if you close this um then right now
nothing happens okay it's not hard I
just haven't done it
yet
cool
um yeah so I wrote all of this Kitty
integration with hammerspoon all of this
stuff is written in hammerspoon
Lua um while some of it was probably a
good idea I should have considered the
python based plugins much more
seriously um for example for window
opening you don't get a call
back so you do get a call back when the
process ends that's how we're able to
remember the when I said let me close VI
and it's going to launch the window so
you do get a call back when the process
ends but you don't get a call back when
you launch a window to it actually being
available which is kind of fortunate so
it means I have to do this like yeah
hack where you wait 100 milliseconds and
then you interact with the window it is
what it is it works it's never not
worked uh but
um I'm not particularly proud of it um
and generally sometimes I find myself
asking what language do I want to use do
I want to use Python uh which obviously
I'm like super productive with and with
like libraries like rich and stuff um Lu
which would then allow me to integrate
it directly into into
hammerspoon or Newell right so I'm like
um kind of
undecided window management is really
really good uh in in this termal
emulator um there's some really cool
built-in plugins like for example
Unicode so this allows you to search for
any unic code character it's a built-in
the plugins are called kittens this a
built-in kitten as you just search for
particular uni code character uh hints
um so that
is uh where for example if you had a
link uh or actually I could show hints
probably like this let's see if that
works
um uh well okay so I recently rebounded
but you can for example this might
work um okay let's just give me like 10
more seconds to try it out so let's see
if we have for examp
Le Echo
High there we
go okay so what just happened there I
mean nothing nothing fancy um it's a
kitten that I'm bounding
to a particular sequence I can even show
you I can maybe show you in a different
Tab and um yeah I mean honestly I don't
think I need to to show it it's not that
interesting
um but since I'm already here I'll do it
so uh
hints is right here so map kitty mod
which is command control uh command
control uh plus p and then l so let's
try it out in practice command
control uh p and then it says shift l so
let me press shift L okay press shift L
and so what happened there so it ran a
kitten called hints
Das Das typ
line dash dash program the current
scroll back D- multiple so now I can
press one and it copies it to my
clipboard I can press seven copies it to
my clipboard um I have a feature request
on GitHub to also support ranges it
doesn't currently do that uh but it is
what it is and then I press escape and
now I have it in my clipboard yeah so
this is kind of cool um I think most
terminal emulators don't have that most
people do that like with vim and stuff
but this is very useful if you have some
output so like you don't have to use the
mouse right the idea here is I
completely eliminated the
Mouse um it also shars with nerd font so
these are these are kind of important
so uh a lot of CLI tools like LSD and
EXA they show you these
icons and you need you need like a
what's called a nerd
font um and so you can either download
it online but Kitty ships with the Nerf
font so it's going to work it should
work out of the box uh without having to
uh download
anything um and then tab bar recent
Edition we already talked about that um
you can customize obviously how your tab
bar tab looks let's
continue
yeah um so would you guys
prefer I show you wake or I finish
this what would you prefer I show you I
show you wake because we don't have so
much time left unfortunately
so I'm going to show you wake but I also
want to talk a little bit about this so
let's see if we can do both at the same
time okay so who here has heard of wake
start like that not a single person oh
okay one person I can't see you do I
know you personally or not no okay
that's cool wow how have you heard of it
or online yeah
okay um so what is it
so okay so there's quite a lot of
explaining to do so let's let's let's do
it quickly
okay there we go
so alt is a little shell script that
just toggles between underscored and not
but it's actually really useful
okay so
uh two more very quick things so um SEC
is a tool that allows you to count lines
of code
code and I have a version called sccd
that does the same thing but for
directories um and then I have a thing
which will probably be called Prague p r
a for practical git but is currently
called uh I think it's called git python
or something um so let's run both of
tools and
now um if we launch Ranger which is a
file manager uh we can see two really
interesting outputs so the first one is
the recursive line
count of every directory and the second
one is G
history so this is the first age it was
edited um 63 months ago this is the last
age it was edited and these are the top
months that it was edited in um so I
just wanted to show that because this is
how I start any exploration of any
directory is by running these two tools
so here we are oh and by the way I also
integrated the same thing in for example
neovim yatsi and all the other tools I
use okay so here we are so let's maybe
start at the very beginning so in the
past lity worked by specifying a number
of files and it compiled it then they
added a thing called standard Json which
allows you to interact with the compiler
through standard input in particular
adjon and to specify the files that
way the issue with that is people want
to have
dependencies and they don't want to
specify the remappings they want to say
just import at open
Zeppelin and uh they want it to work
they don't want to say import node
modules at open zeppin
Etc so what they added is think called
include paths that allows you to specify
okay include paths node modules and now
everything that uh for example if we do
import at open Zeppelin if it doesn't
find it it's going to look in node
modules so there's a typ ER
okay so we see that actually I was part
of this uh audit many years ago um so
there's a typ
eror and uh there's something going on
but we don't really care about this
directory it's an audit directory so we
want to exclude it so how do we do that
so let's start by running wake in it
config by the way if you want to see the
the help just very quickly this is how
it looks in fact we can even get it in
color this
way uh we have to rerun it there we go
so let's run wake in it config it's
going to try to create intelligently the
current config file um so it detects
that the contract size is over the limit
so it has to enable the
optimizer does
that um and it still gets the same
errors right so now we need to tell it
how to compile
it so comp compiler do soulc include
paths this is a compiler
thing whereas exclude paths that's for
the tool and it's going to tell the tool
which directories shouldn't be primary
compilation targets they might still get
compiled if they are imported from
elsewhere but they will not be primary
targets okay so let's just add audits
here is it called audit or
audits audits
let's try to switch it
around there we
go
oops and now we can compile
it and this is a clean
uh G clone and we were able to compile
it so the idea of this tool is it
started as a static analysis tool you
can also use it as a framework as a
fuzzer um as a lot of other things that
I'll uh be
showing uh but uh the the main thing is
it tries to work with all the other
Frameworks out of the box
ideally um and as you can see it did
work out of the box this was kind of a
well except if we excluded the audits
this was kind of an easy example because
they actually don't have any
dependencies there's no dependencies so
it was fairly easy but uh even if there
were node modules by default uh node
modules are actually in the include path
by default for the tool so if you come
to a hard hat or truffle project uh it
will uh it will work out of the
box um the it will not work out of the
box with
Foundry it will but but listen so the
reason
is uh Foundry kind of uh screws up the
entire import system so it doesn't just
uh work with include paths like we've
been uh using for years it actually
strips out uh the
SRC uh from every uh dependency which
they have like as G sub modules and so
it actually screws up the entire thing
um luckily we have a special adapter for
especially for Foundry as well um and so
uh it will read the remappings
txt and if it fails to read those it
will run uh the remappings command right
is I believe this is what it's called
this what it's called I believe this is
what it's called something like that um
and um and then it will it will put that
into the the config for the compiler in
particular compiler doc.
remappings it
would put it right here compiler dos c.
remappings in fact we can even see um so
recently somebody asked me how do I
compile this using wake so I'm going to
show that um so the the project that
they asked me to do it on was this code
Arena
project so let's try to copy the
link Let's uh try
to let's see how should we do this let's
just do
gcdp single depth single
branch that should hopefully get us
where we want to
be oops
wake up and wake in it or synonymous
okay so this is a little tricky because
there are a lot of solidity uh files um
here and um yeah so this one is going to
be a little a little tricky and I don't
think we have the time for that because
we're out of
time um so instead let me show you what
you can do once you compile
it so one of the things is we give you
really really easy access to the a so
for example let's create a new
thing
um okay so let's let's hope this
works I haven't tried this stuff before
the presentation okay it worked
right so anytime you know something can
go wrong and then it requires maybe five
minutes of focus which I don't want to
do right here but
um so this in
particular uh we have a inheritance
graph um this in particular is a
reference
graph okay so this is a reference graph
so let's try to click on one of these in
fact let's have just
okay so this is uh references of the
functions
um this I built one year ago and I
haven't published it yet it's on some
pull requests but nothing merged yet but
I plan to publish it soon a lot of
people are like people ask me like for
this even though it's like not really uh
public yet um but the thing is it's not
done like there's so much more we can do
right it's really just the just the base
um so you can annotate these functions
with various things like whether or not
they have for Loops whether or not they
have external calls um you can add
emojis um you can add probably much much
better um like focusing like if I click
on one of these uh functions it should
probably highlight all of the all of the
edges but already it is extremely useful
especially if you have multiple monitors
especially if you have a big wide
monitor that as you're auditing to see
all the references so for some reason uh
for some reason it starts on the on the
right I'm not sure why honestly the docs
say that it should start at the top but
whatever it is what it is um so this is
the first function and yeah so we have
check ticks um so I do call it a
reference graph but the arrows are more
in the direction of a call graph so this
function um calls this
function um right this function calls
this function and so on um and same with
inheritance graph so this is like this
is in my opinion better than anything
that's currently available um I
personally have not found anything even
close to uh to these tools that I built
for myself but I think they might be
also useful for other people
in fact um just by typing in uh wake
init uh printer DG you can create any
printer you want um
so so it creates this file um we can go
there um one thing you want to do is you
want to say export python path and you
want to add the
Wake side packages so that once you
start importing stuff from wake it can
see it okay so I started aring after
quite a long time of doing tooling
research around one month ago I was on
the I was doing the um unisoft
V4 uh code Arena thing and I ended up
actually just writing massive amounts of
printers um and they are really cool uh
so let me show you some of them so let's
for example try write functions um in
fact right now it's pretty ugly code
actually but I'm in the process of
structuring it so before each printer
was a separate file now I'm in the
process of uh putting it all into lib
and just having like the entry points uh
so let's for example
do see if this works I call all of them
like U dash for like user so I know that
they're not like the built-in ones you
can also see all the printers by typing
list let's do it again now it has a
wider
terminal available printers
so uh loaded from so this is the package
so wake comes with this package called
wake undor printers um so it comes built
in with a bunch of uh printers so let's
try at least one of them so that we can
see it let's try for example C3
linearization
let's see if we get
uh tab complete we don't because it
would be too probably imp performant to
Loop okay so this is like similar stuff
to what you have in existing tools the
difference
is um all the stuff I've been mentioning
like you have the
unified uh
Vision into the entire code base so when
you write printer it's going to work on
all the all the symbols there at
once um
so uh yeah so these are the ones we have
now and let's
see uh okay let's try to run for example
one let's see if this one works maybe we
need to add a
u did it
work okay so this is something that I
wrote for myself so it's called Write
functions so this is really
interesting um so it takes all of the
contracts in your in your project it
puts them all here it sorts them by
the number of
statements but it is C3 resolved so for
example if this was a very small file if
this was the most
derived file it would still be last so
it resolves the C3 inheritance and then
it counts the uh the the statements and
for each of the
contracts it goes back in the C3
linearization and for each
ancestor it shows you the uh all the
storage changes of all the
functions it shows you the full storage
layout there's nothing in this
particular
contract and then it shows each of the
functions so you can actually just audit
it it's much
faster to uh to navigate all of the
different uh different
functions um let me show you one one
more thing so let's do for example I
mean I have this one called types which
is pretty
cool oops I think I in the wrong
directory okay so what types does it
uses the same exact ordering yeah so
that's where it's important to put this
logic into a lib so that you can reuse
it in all your printers so it has the
same exact
ordering now for each contract it shows
you the number of statements C3
resolved and then the types one is meant
to be for like uh peripheral things um
like uh stru types enum types I don't
think it shows events uh but it does
show um it I think it does show storage
variables and it definitely shows
constants um so that way you can you can
read the types all the structs and stuff
and what they mean uh before you uh even
begin and the final one I want to show
is the reference graph or the call graph
uh but inside of a terminal um so I
actually don't remember the name so
let's see how I call this um contract
call graph I believe
um um how are we going to do
this should I try
to okay one sec I have to find this
first emojis create not so this is meant
to create an outline of notes for all
the contracts and all the functions so
that I can very easily take notes on
everything also very cool this
one
um um actually
okay let's try
to let's try this
one yeah it
worked so what is this so this is the
full call graph so when you're reading a
function you can uh let's say you're
reading TIG bitmap position then you can
see the entire
depth of the entire uh color
graph and since it's easier to see color
and symbols than
text um I also assign
emojis
yeah
um I think we might end it
here um so just for the record
stuff I didn't get through so I haven't
even touched upon our language
server it used to work in neovim as well
um right now for some reason it
doesn't um so you know how the existing
solidity
extensions when you click go to
definition it jumps to a different
symbol then is actually the definition
so the reason is they don't use the
compiler
information um so we built is a language
server that actually communicates with
compiler um to resolves all of the
references and uh even actually gives
you all the references here as uh like
these little buttons that you can click
on and it even works for struct
members and it even works for uh
function parameters and function return
values take lower has three references
take upper has three references this
return value has zero references so this
return value is never assigned and we
can be 100% sure that these return
values are never assigned and the reason
for that is that there's a direct return
so what we haven't got into is the
fuzzing um so I guess next year or next
time some other time um and let's see
what I have not been able to do in terms
of uh the other stuff yeah everything
around neovim like the Emojis and the
percentages that I
showed
um and some of the stuff I'm I'm working
on uh right now for example one of my
goals is what I call one
click uh which is a printer that you run
and it will export all of this
information into a HTML
file so that you can open it for example
on your phone or on your tablet and you
can audit on the go while having this
like uh really Advanced uh information
about your code base so that's it guys
thanks a lot for coming and yeah thanks
does anyone have any questions questions
h
h all
[Applause]
w
m m
and
ch
oh oh
all
n oh
[Laughter]
oh e
n
to o
B
he
perfect hi everyone um glad to be here
and nice to see that even so it's the
last day last session uh before the
closing ceremony there's still some
people around interested in agent-based
simulation of execution tickets so
before we wrap it off we go deep again
um yeah um happy to be here for everyone
coming in feel free to join in also
because we are more of an intimate crowd
if you have questions feel free to raise
your hand anytime um feel free to yeah
let me know if something is unclear you
can also ask questions via the Q QR code
um feel free to scan it um I try to have
an eye on the Q&amp;A as well if something
comes in um otherwise I would say we
start right off on um yeah the general
structure um is going to be half an hour
of theory a bit of background on this
yeah execution tickets quick uh wrap up
what's execution tickets again then some
research insights what did we find in
the agent based
simulation um and then the second part
is kind of a let's say open-ended part
about uh running the simulation running
the code on your own machine um I
provide their some information um how
you can set it up how you can run it um
and I'll be around to answer questions
um and then it's basically you can run
it as long as you want try different
settings run different settings um yeah
with this I would Dive Right In um maybe
just as a quick recap why do we care so
much about me why is that a topic that
everyone talks about um um me Boost
payments since um the merge 1.7 billion
US dollar that's what um yeah has been
paid out via MEF boost so that's quite a
big number that's $2 million us per day
on me per average so I think what
concludes from that at least for for me
um means we should be very deliberate
how we distribute me how we go about
yeah distri Distributing it um what
incentives it creates um $2 million per
day it's quite a lot of money people go
a long way to go around the protocol do
other stuff so it's important to design
a mechanism that really works that is a
bulletproof and one of the ideas to do
this is execution tickets um the idea
was first introduced by Justin late 2023
as a Testa proposal separation with the
idea of separating the beaing the
consensus chain from the execution chain
um thereby kind of um yeah um splitting
off the consensus part trying to isolate
the consensus part and having then the
execution part that could be um yeah
somehow differently allocated and the
idea to allocate it was is basically the
execution tickets u meaning the protocol
itself auctions off or sells the tickets
uh which are then kind of lottery
tickets to be chosen as the next
execution block proposer um so as a
builder for example if you want to
propose a block you buy an execution
ticket you get into the lottery and if
you're lucky you get chosen to propose
the next
block the idea of the randomization is
to prevent multiblock meev and liveness
issues if we would just auction off the
block for example execution auctions we
have the problem that there could be
multiblock M strategies where someone in
advance by a lot of blocks and then runs
this me strategy covering multiple
blocks in a
row quick recap again how is the process
um basically without going too much into
detail the idea is that first the beacon
chain runs um for the beacon chain um
the selected proposer proposes the
beacon prop um very similar to how it
works right now um a testers um yeah
vote on it um probably some form of
inclusion list will be involved as well
to ensure censorship resistance and then
in the second round um the execution
block is proposed by the holder of the
chosen execution ticket and then um this
proposer can propose the block and this
is also then um from the testers
validated to ensure timeliness and
validity of the
block so when we look at execution
tickets at this mechanism how how to
sell the block space the execution block
space that contains all the me what are
things to focus on so in our research we
came up with four guiding research
questions in this process one of them
was basically The Meta question what's
the objective what do we want to achieve
what's the goal of all of this um the
second one going along is how do we
measure it um if we have a goal and we
can't measure it it's hard to optimize
for um based on this was then the
followup Point what are the possible
mechanism Des design choices that we
have what is the what's our option space
what's our design space and then the
last one is if we run the simulation and
do this yeah as a simulation based um
what are actually the outcomes um how
the different configurations score on
this um when yeah looking into the first
part first question what our
optimization objectives um we split it
into on the one side optimization
parameters then price behavior of the
tickets um with the most important part
being the yeah three objectives that we
categorized as one decentralization it's
for one decentralization of the um
consensus layer Beacon chain which is
very important but also of the execution
layer for certain reasons we don't want
to sell all the tickets to one ticket
holder
um we want to have at least a certain
degree of
decentralization the second point is me
capture the idea of selling the tickets
is to also capture the MV at protocol
level so we should optimize the
mechanism for a design that actually
captures the me at protocol level and
the last one is more coming from
economic theory block producer incentive
compati ability it means we have to
incentivize block producers that yeah
propose the block to participate in the
protocol in the first place because no
one can be forced to do something we
have to incentivize people to join in um
so we have to find a mechanism where
yeah people that participate profit from
um joining into the
mechanism um on the price Behavior side
um yeah we focus on on price
predictability price smothness price
accuracy and then defined couple of
measurement metrics where I won't go too
much into the details um there will be a
paper coming out soon on it where we
more go in depth how we Define the
metrics but I think that goes a bit
beyond the scope of Friday
afternoon
um then the next step was to lay out the
design space um when laying out the
design space we had um different
parameters that we looked at um it was
for one um the amount of tickets how
many tickets execution tickets do we
want to sell is it a fixed amount is it
a flexible amount what's the target
amount of tickets um the second part is
should tickets expire so when giving out
a ticket is it indefinitely running or
does it expire at a certain point um
third part is about refundability and
related to resell ability if can I give
my ticket back to the protocol or not
and also can I sell my ticket um we
looked at it more from an um yeah
theoretical perspective on a technical
perspective it might be hard to restrict
a secondary Market um but on a
theoretical perspective uh you can also
divide between allocated and unallocated
tickets um but it's uh in our yeah
simulation what we saw it has quite a
big of an impact if a secondary Market
is allowed or not and then also look
ahead period currently we have 64 slots
look Ahad should that be changed or not
and then also pretty relevant the
pricing mechanism what kind of pricing
mechanism do we use um in our setting we
looked at four different pricing
mechanisms two auction formats first
price auction and second price auction
and two quoted price formats um an
adapted version of an amm and uh similar
to EAP 1559 style mechanism um and use
this in the simulation to see how the
market
behaves um yeah then the next step was
we ran the simulations um I didn't go
through all the six um yeah specified
configurations that we have um just I
think that goes a bit beyond the scope
but basically what we did is yeah we set
up a first price auction and the
different other um formats
configurations um where we mixed and
matched together kind of the attributes
that we can have and tested it some of
them are pretty close to the current
setup for example the Justus in time
second price auction slot auction um
some of them as the yeah later ones are
more experimental the idea was to see a
bit what's the impact what's the yeah
impact of each of these um parameters on
the outcome of the simulation what's the
impact on um our metric if we run it um
yeah in theory there are more than 500
combinations to be run so we could go on
for a long time running different ones
um so yeah we choose a bit some of them
more as yeah examples uh then trying to
run a holistic um yeah simulation of all
of the possible
configurations um yeah in the solution
then or running it um what we saw is um
on the different metrics um I hope you
can read it but the summary what we can
see is that on the decentral
decentralization metrics um it's pretty
hard to get to a um good result um what
we see is we have a pretty strong focus
on centralization in this market
however on the other metrics depending
on the configurations we see that a lot
of them yeah score pretty good there's
some outliers um we go a bit deeper into
in a second um but uh there are
configurations that have a very high M
capture have a high price predictability
and so on um yeah to go there one step
deeper or actually as just mentioned um
decent ization as one of the goals so
decentralization to be precise here of
the execution chain is pretty hard um
remains hard um we tried a lot of
different
configurations um however the problem
that we have it's also consistent with
yeah the theoretical literature that
you're doing in xun pricing so you're
basically pricing your execution ticket
on an expected value in the future um
you expect what the value will be in a
day in seven days uh which means you're
kind of yeah using the mean you using
the mean or your expected value um and
this leads to one ticket holder one
block Builder who has on average the
highest intrinsic value has on average
the highest uh bidding value to win most
if not all of the auctions um so what
happens is that kind of the
specialization effects that you have
right now where in certain time periods
certain Builders are more specialized on
high or low volatility environments this
is kind of smoothed out due to working
with expected values um which leads to
this strong
centralization um which yeah also um in
the meantime a lot of theoretic papers
have shown that this most probably is
the case um however what we saw in the
simulation which is pretty interesting
is that the secondary Market reduces
this effect because what happens is that
the um ticket holder the buyer with the
highest average expectation buys the
ticket however then sells it on the just
in time secondary Market um and on the
yeah just in time secondary Market there
might be other builders or other yeah
participants that have an higher value
just for this specific slot it can be
due to propietary overflow it can be due
to volatility effects it can be due to
different other factors um but um there
we saw that actually the secondary
Market leads at least in the Redemption
of the tickets to a lower
centralization on the second main
objective capturing me at a protocol
level um we actually saw that uh in a
lot of simulation uh we get two quite
promising results um we get two to Value
somewhere between 70 to 90% of the
theoretical me that exists um captured
at a protocol level um we can see here
one exampl chart um where we see yeah
there's a certain level of theoretical
me part of it is captured by the ticket
holders and then um quite a high part is
captured at protocol level as well um on
the on the pricing formats what we saw
also quite interesting is that actually
auction based formats worked pretty well
um so and more specifically we tested
sealed bit first price auction and
sealed bit second price auctions um
which both got similarly well results
there was slight differences but overall
pretty similar and also the amm sty
pricing worked pretty well um however
was with a bit of a lack because it
always adapt kind of afterwards but
adapts pretty fast uh while the 1559
style pricing um had significantly lower
Meb capture I go also a bit into
problems of this uh yeah in in a second
um so overall summing it up on the two
say main objectives decentralization is
difficult MV capture works well with the
mechanism in different configuration
different designs
um yeah just a bit of a deep dive on the
E IP 1559 star pricing so basically how
we set it up in the simulation very
similar to the yeah standard EIP 1559
pricing is that after each slot it was
looked at how many tickets have been
sold if a lot of tickets have been sold
the price increases if uh no ticket has
been sold the price decreases um which
has from the mechanism the problem the
inherent problem that you're only yeah
looking at it after the fact and you
kind of have a fast changing demand as M
me in general doesn't if you look at the
data it doesn't have faces of high and
low meev but there's this fast reversion
to the mean and so you're pricing it too
late in a way to when you want to price
it which leads to oscilating pricing
effect so actually the price starts to
fluctuate strong stronger and stronger
um to a point where it first overshoots
then it unders shoots and then it
overshoots even stronger um because it
always kind of has this um yeah too high
latency so this from our perspective um
we tried it with the 12.5% adjustment
Factor but even if we go there to 50% or
the price stabilizes um it works but it
really depends on the attributes of the
ticket holders um which uh makes it not
very stable which makes it pretty yeah
fragile um so at least in all the
implementation settings that we found um
it is not a good pricing mechanism for
execution tickets um so that was quite
interesting because also in yeah a lot
of the theoretical discussions it was
frequently mentioned as one of the yeah
useful pricing mechanisms but um I think
from what we saw so far auction auction
based pricing or kind of an amm style uh
or adapted amm style pricing makes more
sense for execution
tickets um a few more findings on the
other attributes I talked about fixed
versus variable amount of tickets um
what we saw is there it depends a lot on
the mechanis as well for amm or 159 star
pricing you of course need to have a
flexible amount of tickets um for other
formats it could make sense to have a
more
fixed uh amount of tickets expiring
tickets um there it was actually
interesting when on the agent side
implementing their optimal bidding
strategy if you have expiring tickets
makes things a lot more complicated
because you have to take into amount
when does each ticket um um when does
each each ticket expire how many tickets
are in the pool how many slots are
allocated already what's the look ahead
um so it makes pricing a lot more
complicated without having a lot of
benefits um so our preliminary
conclusion was that it doesn't really
make sense to have it um similar for
refundability um we saw that it adds
complexity without adding too much value
to the mechanism design um because it's
yeah depending where you set it either
you create Arbitrage opportunities for
Ticket buyers or it's just an in kind of
inferior secondary Market um and on the
secondary Market we saw that actually
yeah allowing the secondary Market um
helped a lot more with yeah creating um
decentralization uh due to the fact that
in the just in time secondary Market
specialized ticket holders can buy
tickets and uh so even though it has
some disadvantages um I think it makes
sense
to plan for a design where a secondary
Market exists and also the second part
about it is um from a technical side
it's really hard to prevent a secondary
Market because yeah it's decentralized
it's Anonymous people can create a lot
of different IDs um so there's almost no
way to avoid void um yeah ticket holders
to sell the tickets
anyway or sell the slots I mean it could
be that the ticket holder runs kind of a
me boost auction um just for the slot um
that he get assign to Via execution
tickets good that was um the theory part
um there's a lot more to say I didn't go
too much into the all of the economic
properties of execution tickets but that
could be covered as well um but um I
wanted to leave enough um time also for
the workshop part um I put in the
question do we need a break but I think
um I would not do a break right now only
if someone says hey I need a I need a
pause um otherwise I would go straight
into the workshop part maybe just the
quick question are there questions right
now any questions on the um on the
theory so far on execution tickets on
our
results I know you said it's out of
scope but um what prevents uh
centralization from occurring in the
secondary
Market um I think it happens to a
certain degree but what we saw in our um
yeah simulations um that you have for
some um um specific environments you
have certain very you have builders that
are very specialized for example on sex
STX Arbitrage in high volatile
environments and they might not be the
most competitive Builder on average but
they are competitive in certain um slots
in certain environments um so what we
saw is you still have centralization um
but it's a bit less it's basically it's
like the market now let's put it that
way you still have kind of
oligopoly um but it doesn't worse to the
worsen to the market that we have right
now hi good summary um have has there
been uh any work done on how um
exclusive order flow is uh going to be
uh I guess a winning Advantage for some
people in the execution tickets
environment and do you have thoughts on
exclusive water flow in this
setting yes I think um we didn't in the
simulation we didn't model exclusive
order flow explicitly but I think um as
in the market right now it would be one
of the winning factors um having
exclusive autoflow gives you an
advantage in bidding for the tickets it
allows you to bid for yeah at a higher
price on average I think you would still
have the fact that um um if a secondary
Market is enabled and someone else also
has exclusive order flow for them the
pressure builds up to bit um so we did
some yeah multi-lot analysis and what
you see there is that over time prices
go up and one of the theories that we
haven't proven yet is um that uh for
let's say you have one winning bidder
who has the highest value but you have a
second bidder that also has exclusive
private orderflow um that needs to place
their block at some point point in time
so there is an incentive of kind of a as
long as the exclusive orderflow doesn't
only go to the one monopolist um it
creates a pressure for having different
block Builders uh for um yeah for for
row of
slots um and I think that is pretty
pretty pretty similar for execution
tickets um that um each Builder that t
exclusive waterflow needs to um buy a
certain amount of tickets to ensure
inclusion of the orderflow um however if
you have one Builder ticket holder that
has the best autoflow they will probably
still dominate The Market at least to a
certain
degree any more
questions I think we are
good perfect thank you very much then um
yeah I quickly go to through the
workshop setup um as said um it's pretty
open so the general idea is I just run
through it I run through how it works
and then everyone can um yeah
self-guided set it up um I have uh also
online a setup guide um that explains a
bit how everything works um yeah first
step download and run the simulation so
make sure that it works on your machine
should be pretty simple I tested it with
some people
um but yeah it's the first step second
step is design another
configuration mix and match the
parameters and then run it test test it
and if you want I have set up a noce
dock where you can share results you
don't have to um just if people feel
like they found a very good simulation
or simulation configuration that they
want to share with the
group um on the simulation um here on
the right you can see the general
setup of the code I used a red cut
simulation framework in Python um the
high level logic is in the first step it
updates the market metadata so such
stuff as um slot number me the slot
which is randomly generated based on
historical
distributions um in the Second Step um
ticket holders can buy tickets um
depending on what mechanism is chosen
there are different ways to buy the
tickets if a secondary Market is enabled
um that runs in the third step and the
last step is redemption of tickets where
the ticket that get allocated to the
slot is redeemed the ticket holder gets
the me of the slot and the ticket is
burned in a way um just very quickly on
the file structure um there's one major
um python notebook where most of the
logic runs in um I've set it up in
Google collab so it's pretty easy to
share and run um there few Support
classes the models uh the data models
purchase functions on buying the tickets
and some yeah support functions util
statistics and there's also results
folder where all results are stored um
they're just a quick primer if you run
it on a large setting results can get
pretty large because Red Cat stores a
lot of very granular
results um yeah other than that on the
agent ticket holders they are modeled
after the current uh block Builder
Market you have top Builders medium and
tail Builders um that get randomly
allocated different um capabilities such
as me capturing abilities aggressiveness
uh initial funds and um their discount
Factor however that's used
less um yeah where can you or what can
you adjust um there's a CIS perams file
where all the information is in um
that's in the second cell if you go into
the notebook um could be should be easy
to find other than that the time steps
how many rounds you want to simulate how
many runs you want to do in parallel in
the beginning I would recommend to do
one run otherwise it can take a while um
so there main message is sis perms is
the place to adjust the parameters of
the simulation if you want to
go um if you want to go really deep um
then uh you can also adjust the bit
mechanisms how ticket holders buy buy
tickets and um yeah much more in terms
of how the auction runs and so on but
for the beginning I would just adjust
the sis perams and yeah with this
basically link to the notion dooru where
you can find the setup guide um uh there
yeah I think the main important info is
to yeah access to Google collab notebook
which you can find the link in the
notion doku to copy it um it's pretty
easy you go to yeah file save a copy in
my drive you store the copy of the
notebook in your drive and then the
second part is to download the rest of
the code from the Google repo um it's
ea/ simulation on GitHub um you download
the code you move the code to the Google
my drive root folder that is important
because the notebook needs to access the
Support classes and then you should be
able to run the simulation via runtime
run all um hopefully pretty forward
straightforward and then you can adjust
and run the simulation adjust a lot more
code and um I hope it Mak sense and then
you can yeah design your own um
configurations run your own setup on
execution tickets and see what results
come out um I leave this here so you
have the links and feel free to ask me
any questions on it feel free to yeah
ping me also now or afterwards also for
the people in the live stream that's
better to ping me afterwards um also if
people run it later um my yeah contact
details are in the end um so um I'll
share all of this with you you and um
you can use I think the best is to use
the notion and go through it to set it
up
awesome then any questions for
now any questions
guys yeah we are
good thank
you I think that real trouble starts
when they download the reer and try to
install it the real trouble starts with
reer probably you you should head
started like good guys and
solid yeah maybe next time that's a
first step then everyone has half an
hour to to download it and run it but um
I hope yeah it it should be pretty
straightforward for
yes is it on yeah I think I'll turn off
the microphone for now and if people
have questions just let me know I come
around
d
let
h oh
