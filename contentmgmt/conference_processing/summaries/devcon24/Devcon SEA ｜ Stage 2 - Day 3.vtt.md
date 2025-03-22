[Music]
on
plan
good morning everyone I'm Kim so today
we are going to talk about uh what the E
instram Pary is
hello everyone good morning I'm
Kim so now we are going to talk about
what each insur pry
is shake shake shck hello everyone uh we
will talk about the insurance in game
like why itum isual policy is okay the
next slide yeah okay
sh check check one 1 2 3 4 5 6 78 19
check hello check two hey hey hey hey
hey
check check two hey hey check the club
hello everyone check taste one
two e
I
check check hello 1 2 3 4 5 6 7 8 9 10 1
five test check one 2 3 4 five 6 7 8 n
shake shake one 2 3 4 5 check one two
check
is
oh
e
m
see
SC
w
you I
St
m m
[Laughter]
yeah a
[Applause]
wish
oh oh
you
d
good morning everyone I'm really excited
to welcome our first Speaker we will
start with the session um the title is
called by ethereum's issuance policy is
redacted I have the pleasure to announce
Anar Dix as well as kashar Schwarz
Shilling they will talk this talk will
explore the status quo of staking
economics it drawbacks as we see them
and what the future of staking economics
could look like and a fun fact about
three of us we just discovered we all
German speaking so we my switch session
into German I both had the pleasure
meeting them on previous events in
Zurich and in Amsterdam but anyways we
speak in English since we're here at
Devcon in Bangkok I'm very happy both of
you can come on
stage thank you thanks for the info and
thank you for coming so early um I know
it's the first session um so yeah Ana
and I going to talk about why ethereum's
issuance policy is unsustainable in our
opinion um and for some of you who might
have been at Justin's talk um presenting
his idea of the beam chain um one of the
items that is part of that road map is
smarter issuance as he refers to it and
he put a little um spicy Emoji con next
to it and it didn't take long to
understand why
um this topic tends to be spicy um it
was the most upvoted question in the Q&amp;A
why are eth researchers obsessed with
lowering issuance and we're here to kind
of answer this question and argue for
why we think we need to change issuance
um so let's begin by just looking at the
current staking Trend um it's been a
relatively straight ofair up only um so
here you see basically the amount of
stake in the system and it's been yeah
trending upwards um at a fairly um
constant rate and um the question is
obviously where does this trend go will
it continue when will it stop what does
it look like in the long run um and to
kind of answer this question we're going
to have to argue a bit about kind of
staking supply and demand and to re to
be able to reason about what an
equilibrium looks like so in this
setting the demand curve is what we call
the issuance curve it's basically the
protocol's willingness to pay um
validators to secure the chain and that
function is very well defined we know
exactly at what point how much
validators um earn as yield if they
perform correctly of course and then the
supply is basically the willingness of
eth holders to do that work to do the
validation um for um different levels of
field and so um what we see here is
basically um the demand curve which is
the issuance curve um and to kind of
quickly run through this intuition here
why it's designed the way it's designed
um right now is that for what you see
here is that there's um a downwards
Trend as more and more ether Stak the
protocol pays validators less and less
yield um but at the same time one
property here that you can see is for
very low levels of staking the issuance
yield is very high basically the the
intuition here is the protocol really
needs to make sure that um we have a
minimum amount of security in the system
and so it pays a lot for that and as
more and more e um gets staked kind of
the urgency of um um needing to kind of
recruit more validators goes down um and
it goes down but it kind of flattens out
and so that leaves us in this awkward
spot that we don't really know where we
actually end up um in the long run um so
what happened so far is basically um
this upwards only Trend where more and
more people stake and what that means in
a supply and demand context is that the
supply curve has been shifting downwards
over time um and now the question is
where does this end up in the long run
and one reason of behind the fact that
kind of why we might end up in a sort of
High um percentage staked world is this
what we call the flattening effect and
the idea here is basically that um
for solo stakers to stake the kind of
costs are very heterogeneous and mostly
it's the fact that some people are very
good with computers some people not so
much and so to recruit the last person
on Earth or like the last eth holder on
Earth to sort of go through the pain of
setting up a server and like running
their own validating node is extremely
costly you would need to pay a lot
whereas with sort of delegated stake um
that cost is very homogeneous meaning
it's just a oneclick um solution for
everyone and so the kind of obviously
the Willing the preference is still
different so it is um an upward sloping
supply curve but it's basically uh
significantly flattened and again in the
supply and demand context what this
basically means is that with a flatter
supply curve you end up with more um
stake in the system in equilibrium given
a demand curve now um basically yeah the
question is where do we end up in the
long run and that's not um ex because we
don't know the supply curve we can only
observe it at any sort of point in time
we know that today x amount of stake is
in the system roughly 34 million so
roughly
the very least given the whole kind of
trend with lsts and liquid staking it is
very plausible that we over time um kind
of continue trending to the right in
terms of uh staking participation um and
because the demand curve so the issuance
curve is so kind of just relatively flat
towards the end and doesn't kind of
conclusively go to zero or anything like
that we don't really know where and you
can see that a very small change in
yield can have a dramatic impact on the
sort of um equilibrium um staking level
um and now I'm going to let Ana continue
yeah in the the second section um we
call that nominal vers real yield um so
we we've been giving like talks like
this over the past um half a year
basically at at a few conferences and
this is always the one section where in
the end when we talk to people people
are always just a little bit confused by
it and didn't really understand what we
were trying to say in that section so we
did it tried to um restructure it a
little bit
experimentally um uh and and we'll still
show like proper yield curves but I I
wanted to start with like a very simple
mental model first and specifically I
really think that there's two I call
them anomalies for proof of stake
accounting that mean that I think most
people's mental models for like how much
yield you earn in proof stake are just
fundamentally slightly off and to
explain that a little bit more again
simple model um so basically just let's
look first at a normal uh any real world
example where you have a large group of
people paying a small group of people
right everyone here takes some coins
gives them over to the other group um
very simple right and if you if run the
analysis like you could imagine I don't
know that's a retirement fund or
something a lot of people pay in few
people get get get uh get a pay out or
something H and you make the analysis
like who basically gained who lost or
like who paid who who received it's a
very simple analysis right everyone here
paid a little bit those two uh gain gain
quite a bit simple simple accounting
here um if you go to First proof of work
because that's where the first anomaly
shows up um it's a bit of a different
model right so we have these people they
now like see they say these are all eth
holders pre-merge right they all have
their own balance you have these miners
these miners need to incentivize for
their need to be incentivized for their
work so what we do is we give them coins
but this time those coins didn't come
from anywhere right we minted them and
so that's the first anomaly that's
basically that we in in uh in um uh
blockchain networks we often pay for
expenses by just minting new coins now
that's no magic right it's not magically
coming out of nowhere it's still a
payment
from those people to those people right
but it's an indirect payment basically
because you're now being paid by being
diluted right that that is accounting
Wise It's accounting wise the same thing
as if you just given coins over directly
but it basically instead takes this
indirect step and the way you can think
about it is right like the balances here
didn't change but because there's now
more coins in existence in general
everything shrinks a little bit right so
that's the way basically same thing
again it's just a different different
way of doing accounting but it does make
it a little bit harder to cheack what's
going on
now proof work that's still fine proof
of stake adds one other kind of weird
addition to that accounting model of
course wait that's yeah that's obvious
right like those people still paid a
little bit and then those people gained
so now proof of stake add a second uh
anomaly to this model and that is that
there are no miners anymore right and
that's great you know I think uh it's
great that we were able to do that um
but now who who actually is doing the
work who's being paid here right um and
it turns out that actually in impove St
of course the people that actually do
the work are some of the stakers some of
the the holers themselves right some of
the people with eth in this case I don't
know half of them of course right now we
are more like at a third or something
some of them actually are stakers are
are doing the the work and just to to
give a little bit more room let's
separate them out a little bit um and so
now same thing again right like they do
stake they they do they fulfill their
duties and they're getting paid right so
let's pay them okay so then again same
same thing same question what happened
here like who where where did this money
come from right same answer of course
dilution so let's shrink everything and
then we can run the analysis again and
we can run the analysis and we can say
well everyone here paid for the for the
security and then those those guys
actually got uh got extra money and and
and of course if you if you do the the
accounting like everyone lost a little
bit because they paid for the security
those two gain more so on balance you
still make a profit if you stake of
course right that that makes sense but
for example in this example we have four
new coins we have four people so
basically everyone got diluted by one
coin on average right so basically it's
I I chose this example just because
actually if you look at this here it's
very simple if you ask like how much did
you actually earn you didn't not like
you see two new new coins but the first
coin here offsets the dilution the
second coin is the earning so the actual
answer would be your staking yields in
this picture is one coin now there is
one annoying fact I don't know how many
of of you all have ever paid taxes for
staking but um if you're a solo Staker
you just pay taxes for the two coins
right because that is how much your
balance went up now in many countries
it's a bit better there are countries
where like you know the top tax rate on
income if that's tax income is around
lost the one coin that was your real
income just now you know so 50% staked
it's already getting quite uncomfortable
with kind of this this um this solution
effect and I I just wrote it down here
so the two the two in anomalies um that
they make it a little bit hard to to to
to talk about proof stake kind of the
the payment via new coins and then the
recipients are also paying um and so
what you see in terms of yield is not
what you get and actually I think you
know how a couple years ago when we
first had um icos people only looked at
like floating um Supply right and at
some point we all in the industry were
like wait that's not the right way of
doing accounting actually we need total
like fully diluted um uh volume of the
of the coins right and and that took a
while but by now that's the standard
metric and I would say we really need
the same thing with staking rewards as
well if someone tells you hey our
network is pays 7% staking yields but we
also have 70% staked you should actually
think ah so I'm getting 2% staking yelds
not 7% right that that actually makes a
big big big difference um now so far
that's not an argument for like any
anything about ethereum in particular
it's just like some annoying aspect
about how to you know do accounting for
proof of stake and actually if someone
tries to maybe convince the tax
authorities that actually they should
only pay taxes on one of those two coins
I think that would in principle be a
very sound argument but not not a tax
tax adviser um but like now let's go
back to actual yield curves you know and
like proper economics like this is again
this is the same curve from just now
like this show tells you depending on
how much total stake there's in the
system we have roughly 120 million eth
in total this tells you how much you
earn or how much you think you earn
right like this is the nominal that's
what we call it the nominal yield how
much the protocol how much your balance
goes up every year now we can just take
that and uh one one one point there is
that your incentive to to come in and
stake at any level right is is always
the difference between earning that
yield and earning zero right that's
that's pretty trivial so so now let's
let's adjust that for the real
yield and that shifts the curve down and
it should be relatively intuitive why it
shifts the curve down like towards the
left if B anyone Stakes right there's
barely any dilution so towards the left
those two curves are basically the same
if if we have 10% staked like the amount
your balance goes up that's roughly what
you actually earn in staking towards the
right if everyone Stakes that's not it's
not like the system breaks like if
everyone Stakes it still works but
everyone's balance goes up by the same
amount every year and that doesn't
actually create any value right so you
don't actually earn anything anymore at
that point basically staking is just a
duty for the entire network work um and
one one point I just wanted to make
there because sometimes people ask about
that that does not mean that the
security of the network is in any way
broken because your incentive to stake
is still always the difference between
staking and not staking and as you can
see I kind of plotted the real eth yield
here like so basically if you just hold
eth you know you're you you're getting
diluted every year so like basically the
the gap between those two curves still
stays the same as before so the
incentive to come in is still the same
like as you you you you you you would
have thought from the nominal graph but
it just means that it comes from a
different thing first it comes from the
potential to earn profit and then
towards the right side it comes just
from avoiding to be diluted and so
that's kind of the summary SL summary
slide here so basically we have a
spectrum of different paradigms of
staking you can have staking set up as
something that actually generates
profits potentially of course you know
for for stakers or you can set it up as
just a duty for the entire protocol both
of those work for the protocol so if we
just reason from what's best for
ethereum both of those work um but we
have to be aware and I personally think
talking to a lot of stakers that
actually once you kind of like try to
make that point people tend to really
prefer the world we actually staking as
a profitable
activity um and one side argument there
that we always make is like if we want
to go to the other world instead and we
want to just everyone participate in
staking we should design ethereum
explicitly with that in mind and then
the last point of course it's that it's
still all incentive compatible so yeah
sorry this was like a little bit I tried
again this now to to give you the
stickman um intuition hopefully that
helped a little bit better understand
what we mean when we talk about noral
real yield but that's basically our
first argument for like why if we do
nothing we'll keep sliding more and more
and change the character of staking from
profit driven to just an accounting
Mirage so if you
want right um oh wait wait wait wait
wait these are two because you know from
uh kaspa is our Mema and Chief and so he
always like comes up with these images
and I always forget about mentioning
them
so that's kind of supposed to illustrate
you know like this the staking mechanism
once we get to like almost everyone
Stakes right it becomes this like purely
cyclical thing where you think you know
coins come down the waterfall but then
it turns out that it's the same coins
that just went in right so basically
there like demonstrating that and then
um you know if you have to pay
taxes uh even worse so uh yeah and now
now over to you thank you Ana for
explaining my meme
um third um okay final section um so
what's the problem with all of this
right um ana basically just explained
the whole um
yeah why we should pay attention to
nominal versus real yield and how sort
of um staking becomes sort of a
profitable activity to kind of being
quasy forced Onto You economically by
basically if you don't want to be
diluted um it becomes this Duty actually
um and so so I'm going to as you see
there's a bunch of um reasons that we've
gone through in various iterations of
different talks um so if you're
interested in like different points you
can um talk to us after the talk or um
find it online but I'm going to focus on
um basically the network effects of
money and then we have a little bonus
one and um I think the network effects
of money are really crucial um and
so what do I mean when I talk about this
um so basic basically um money has
Network effects and that also applies to
um eth it applies to lsts and um in some
sense um basically
um one way to think about it is um what
makes an what makes money attractive it
makes money is attractive for example if
you can traded at good execution um sort
of this kind of mental model is
liquidity begets liquidity
so as you are a liquid asset people are
incentivized to come to your asset to
have that good execution and then some
sense eth and lsts are in competition in
the sense that they some somewhat
represent similar things lsts are a
derivative obviously there's like
slashing risk and sort of um
counterparty risk if you do it in in a
mediated way um but the whole point here
is that basically lsts have Network
effects and these Network effects kind
of lead to this Winner Takes most
dynamic where it's likely that in the in
in the long run that one LST will kind
of win as the money um on that um LST in
that LST Market um and what that then
implies is that if we end up in a world
where a lot of the eth is staked say 80%
um hypothetically um what does that mean
so you have 20% raw e that is still in
circulation and 80% is um mostly going
to be dominated by lsts because
unfortunately there's only so many um
solo stakers um and um basically then
what happens is that the dominant LST is
basically going to be the de facto money
of ethereum replacing raw eth and what
that means is that we kind of we're
adding a permanent trust layer to
ethereum so as an as an e holder you
come to ethereum and you kind of faced
with the question do I want to hold this
very expensive maximally trustless asset
that is eth or um am I going to kind of
not be the only silly one in town that
is getting diluted and hold an LST that
is actually at that point even more
liquid than eth because 80 like in a
market where 80% of um um is dominated
by lsts then um those lsts are going to
be the ones um more most liquid on
decentralized exchanges um it might
might even the the the nfts might be
denominated in that dominant LST etc etc
and so um it really becomes this
permanent trust layer that we're kind of
economically kind of obviously it's not
enforced onto anyone but it's kind of
economically quasi enforced and um yeah
you kind of sort of bullied into holding
the trusted asset um and we're losing
this maximally trusted um maximally
trustless raw eth as the main money of
ethereum and um I mean as a side point
also as for eth the asset this is also a
sort of huge concession in terms of uh
monetary premium giving up on that kind
of maximally trustless um uh Vision um
on that point we're actually going to
give a talk um next Saturday with a bit
more focus on on that topic at at the
bankler summit um
and
then since we're up with time let me
quickly talk about this um sort of
principal agent problem um
so basically at the very beginning
before um the be basically the initial
people that staked were almost kind of
crazy lunatics you didn't even know when
uh when the merch would happen people
still went ahead and um and staked they
were like basically um yeah crazy cool
and and then um the more more kind of
like sort of the less
risk friendly um solar stakers came in
and then um lsts kind of kicked in and
sort of the what I'm trying to get out
here is that there is a spectrum of sort
of who is actually running the software
uh who like the which of the stakers are
actually sort of running the software
themselves and as you kind of go on that
Spectrum um there's more and more
intermediation so lsts um are already
Des people staking with um rocket pool
or Lio for example on chain have are
pretty close to kind of the risk
tradeoff and are aware um and then
coinbase and centralized exchanges uh
it's it's gets it gets more and more
obstructed away it becomes this oneclick
thing you don't even know what's
actually happening it becomes less and
less a conscious decision and then one
reason why I kind of we added this as a
bonus was yesterday we there was the
news that um one of the ETFs just bought
a um staking service provider and
effectively um the the capital that is
being staked is less and less um sort of
close to the actual staking they don't
even know what happens in the in the in
the back end anymore um and so I mean
one obvious question here that the
elephant in the room is so what can we
do about all of this um
is um yeah basically changing the
issuance curve this is our tool of how
we can kind of control the um staking
ratio and with a high staking ratio as
we just discussed there's like a bunch
of uh negative externalities and so
there's different kind of approaches
there's a sort of progressive yield
reduction which one of our colleagues um
Anders is going to talk about I think in
maybe two hours or something um and then
there's also ideas of curves that
actually go to zero um to sort of
meaningfully um kind of constrain the
amount of stake that would um plausibly
enter the the the staking set um and
then we have the second sort of question
of um what kind of staking range do we
actually find desirable um I think
there's there's kind of arguments for
why a low range is uh preferable than
levels to similar today like 25% um or
sort of more closer to 50% obviously
there there is basically no um True
Value it's a tradeoff space and um it is
um it's it's a it's a big topic and
we're going to talk a lot about about
this in the coming sessions and future
talks um but yeah I think we we wanted
to really focus on why we think um we
need to change it and then um hopefully
will get to actually change it
eventually thank
you thank you so much um we have some
short minutes to answer um the most Ved
question and that would
be what should the ideal percentage of
State eth be for example if we are 20%
what ideal number do we want to equalize
it all right so that was a little bit on
the last slide it's It's tricky because
there's two qu two versions of the
question the one is like if we were to
design the system completely from
scratch before anyone starts staking
what number would we choose and there I
think as we as we said like initially
the system was designed with solar
stakers in mind with solar stakers only
we would never go about 5 10% of of each
stake maybe because just not so many
people are sophisticated enough to run
their own local setup um and that would
be exactly be these like five 10% of
like enthusiasts that really also care
about the network right those would be
exactly the people you would want in the
system the most
um it's it's unclear whether you know
from from the we now we're already at
actually get back down to that level in
a way that doesn't actually hurt
existing stakers too much or drives out
solo stakers then the next best thing
could be like maybe stay try to stay
equalized at at today's level um except
that for forever basically out of every
three coins you earn one of them will be
fake and just account for dilution um or
potentially you know if it takes us for
a long time to find a solution here or
the the process with the community like
of of All of Us coming to agreement
takes a lot of time we might have to try
to like basically just cut off S
basically blade in the process as as we
you know then find an agreement on which
might be closer to
an let me check what's the highest V
um will restake in wors in this issue um
we gave a talk about this I'm not sure
if it's online is it online uh yes it's
online there's also a website issuance
do what the where all resources on
the topic are listed and also that talk
and basically
reaking will is only yet another source
it's similar to me in a sense there's
different types of reaking some of them
don't really affect this at all the ones
that do are what we call basically
proposal specific reaking yield that's
things like pre-confirmation things
where basically your role in the
protocol is what gives you access to
that yield but those can be um addressed
we didn't talk about it in this talk but
there is this kind of upcoming proposal
for a feature called Mev burn more the
more precise term would actually be
propos a specific yield burn and that
would capture both the existing meev and
the re the relevant portion of the
reaking burn reaking yield so that
basically yes it worsen the problem a
little bit but it also we have already
the tools for for addressing it okay
then I think one last is an enshrined
LST
solution um yeah I mean I'm not sure if
I mentioned it but like basically the
the the the idea is here we just want to
be intentional and also like you know
the other question of like why didn't we
do it at the start of the the beacon
chain well because no one thought about
the kind of the the tail end of staking
everyone just thought about how do we
make sure there's at least 5% of each
Stak and so I think now the point is
okay we have a mature understanding of
proof of AK now we want to really design
for the end game or at least you know
like as close as we get to can get to
that and for that basically we just have
to make the intentional Choice hey do we
want low percent stake and it is
actually income you can earn do we want
to embrace you know 100% stake but then
let's redesign the system and enshrine
some sort of LST mechanism which by the
way would not mean that ligher or rocket
pool would go out of business you know
like you still need all of that on top
but basically the core mechanism we
could enshrine which would make that
part trustless so we would at least end
up with an LST that is a trustless LST
in the system um but then let's make
that choice and in that world of course
yes stakers no longer actually earn
money directly right it becomes a duty
for all eth holders if we if we like
that if we prefer that world over the
and properly design for it instead of
just being passively pushed into it
because when the beacon chain launched
we didn't anticipate we would go this
way thank you so much um I think our
time is up up so but you have a lot of
burning questions but I think you can
still um ask your questions later on
thank you so much Ana and thank you so
much KAS but this wonderful presentation
we'll be outside the door if you want to
come grab
us um you can stay for the next session
we just have like 5
minutes oh okay sorry there's no there's
no time left so um I think the next
speaker is is already
here let me
check um I'm have to pleasure to
announce the next speaker ready finding
rough consensus on
issuance um welcome Sasha on stage
I'm just testing the clicker
okay okay hi um can you hear me
okay okay I'm sasher I'm a researcher at
Lio um I just recently read the blur for
the talk and it's not at all what I
originally set out to do so I apologize
it's not as funny as I wanted it to be
and it's not as simple um so bear with
me what this talk is not
about this talk is not about making the
case for no issuance
change um this talk is about it you know
there are good reasons for that to do
with uh mainly
neutrality um and I think like a
pessimism towards attracting new solo
stakers but that's for another talk this
is really to try and find some sort of
consensus some sort of bridge between
what Casper Ansgar um and Anders are
doing and how
um I guess a subset of lighter
contributors think about
things so what this talk is
about an attempt to find a synthesis as
consensus that all sides can put up
with it does take as axiomatic that most
EF researchers have already made their
mines up um on an issuance cut although
there are disagreements on the detail
okay so what do we agree on
already I think we are all aligned that
issuance should concern itself with like
macro level risks to
aium um this is anders' framing if you
look at number two there are sort of
existential macro level risks and I
think that's within the scope of
issuance to try and anticipate and fix
um one you know one thing that I think
Casper and touched on is that the Crux
of this is having a viable social lay
that's uncorrupted by any staking
provider right that's ultimately what
matters the credible
neutrality okay so where do we
disagree we
disagree on three things I think right
the first is what the purpose of
issuance should be and this is kind of
we maybe
disagree the second is our confidence in
the shape of the longrun supply curve
and this is you know probably um
disagree and the third is the relative
chances of macro level risks under
different issuance rates and I think
this on this is what we definitely
disagree on right this is the Crux of
it so I'm going to present kind of one
side thesis the other side antithesis
and try and come to some sort of
synthesis um so kind of the you know one
side of the argument goes not touching
issuance this stage increases the
likelihood that an LST like Lido ends up
dominating e as the most liquid and
widely used currency within the
ecosystem this would make it much harder
for a FM to recover if that lstd were to
turn malicious at some point in the
future much harder to Fork something out
that most users depend
on um this is kind of like you know well
summarized by Anders here uh you know a
key reason for mvi is precisely because
of the fear that all e would be staked
when some Black Swan event takes place
and this is kind of sort of a story mode
in anders' Twitter which I think does a
good job of kind of articulating uh that
event okay what's the counter what
what's kind of the anti feis here um so
the other side here is that um cutting
issuance increases the likelihood that
decentralized exchange dominates staking
this could have dire consequences for
A's ability to remain censorship
resistance and hence E's
value a coinbase tail win is
increasingly likely given Trump's
election
win um there is now an increased
probability of staking
ETFs so why are we considering adding
fuel to the
fire but perhaps most importantly even
with less than 50% of each stake the
malicious coinbase could prove
impossible to socially slash
and to see this um kind small story kind
of inspired by Anders but kind of the
sort of the the other side consider the
following right
okay a significant instance cut is
implemented um let's say in you know 6
months two years time um maybe even
sooner um with margin compressed and E
staking ETFs given the green light stake
centralizes pretty quickly within a few
years over 50% of validators are run by
coinbase
um 2030 the Dems are back in power the
US government puts a tremendous amount
of pressure on coinbase to refuse to
process blocks that contain privacy
preserving transactions in them or
transactions from a continuously updated
government Blacklist that could in you
know include human rights activist
journalists uh whoever whoever is kind
of Public Enemy Number One at the
time by this time Brian is no longer CEO
he stepped down to focus on Long levity
research he's kind of burnt out of all
the politicking uh his replacement is
not as OG or aligned and caves in in
order to appease both the government and
shareholders um most of the FM crowd is
now on farcaster I don't know maybe they
already are already on for farcaster um
while farcaster has been you know great
for the ecosystem it strong ties to
coinbase make it especially difficult
for anti- coin based narratives to
spread across the social lay and that
kind of has to do with like how an
initial network is seated right if you
look at um I'm not going to go into this
now but it does uh you know if there's
momentum of initial follow
and uh in that's kind of hard to undo
later
on um okay major Basin forecast
influence argue that fking out coinbase
at this stage would be extremely unfair
to innocent users and you can think of
sort of I think Anar has mentioned
teachers with Pension funds Etc like
you're not going to just folk them out
and and and and stash their e
um so this leads to some sort of Crisis
right so you have on one side if your
OG's and researchers who are threatening
to leave the project if the sensorship
doesn't stop and on the other hand um
you have these kind of uh you know
coinbase aligned people that that have a
lot of social influence that that say
this is kind of uh a really bad idea for
aerum so the AUM Community splits into
two camps a contious for fork occurs and
circle surprise surprise sides with
coinbase so at this point you have two
sides in their own separate universes
with their own chains with no practical
way of coming back together um ethereum
a global Commissioners platform created
in part to be a refuge from Nations and
geopolitics instead ends up cleaved in
half by a large corporation that is
ultimately accountable to its
shareholders and
government so coming back down to earth
like what what the hell is the point of
all this the point of this anti fuses
here is to show that it's too simplistic
a view um it's too simplistic to to sort
of view the macro level risk through the
lens of solely the amount of e tied up
in
staking um which is you know a lot of
the which is the foundation for a lot of
um the issuance
discussion um one of the main reasons
given for cutting issuance so as we see
there are complex social dynamics at
play here that are very different very
difficult to untangle right um this is
one hypothetical scenario but you can
dream up you know millions of them it's
it's like uh it's not difficult
to so double clicking on on the coinbase
risk um today it's I mean this these
stats are slightly out of date but it's
the largest theerum node
operator um nearly 15% market share
could be over 15%
now um staking ETFs likely to happen
under Trump there's a good chance coin M
Will C on the market
here
um yeah there's you know us-based
custodians are more likely to be
whitelisted uh if you look at Bitcoin 8
out of 11 Bitcoin ETFs use coinbase as
the custodian this is a pattern that is
likely to repeat with e
the switching cost of moving capital on
chain is extremely low compared to the
switching cost of moving capital from an
ETF
sex um if staking which essentially
means if staking yield drops below a
certain point onchain Capital will leave
higher yields in in defi that's unlikely
to happen on an
exchange um in more sort of technical
language centralized custodians are
likely to have a much lower Supply
curved than decentralized
pools all this means that there's a real
possibility that state ETFs combined
with issuance Cuts think of this as an
accelerant uh leads to one custodian
controlling 51% of e staked a few years
down the
line uh if that happens you can probably
say goodbye to 's monetary
premium um and since this custodian has
a large if subtle influence over the
social layer it will be very difficult
if not impossible to Fork them out
should something go
wrong so before I come to some synthesis
right I presented one thesis short
because I think uh there's like Casper
Ansgar Anders have done a good job of
presenting that well I presented the
anti fees in a long way because I don't
think it's been presented before before
we come to a synthesis I want to do a
double click on how a strong LST adds
value to
ethereum the main I mean there are
multiple lenses through this but the one
I want to focus on is jurisdictional
dispersion so almost 20% of light owned
operate owned operators are um domiciled
in APAC countries that's sort of Kong
Singapore Australia South
Korea um and while Europe compromises
nearly 60% of the 60% of the total two3
of these are actually non-e right so
this includes countries like BVI Cayman
Islands
Etc so 60% in total we have 60% non-eu
and non- US nodes which is a pretty
resilient distribution especially
compared to an ethereum without
Lido if you look at sort of a
distribution of ethereum nodes you see
real concentration in the US and Europe
especially the
EU um sort of according to Ean nodes
like more than 66% of etherum nodes are
based in either the e or the EU so
that's significantly worse than Lio and
very prone to Gil political uh
censorship um I think if Li is doing
well but if it can get to 5 to 10%
representation from both laam and Africa
that would be perfect and I think we
should make that an objective
this is a picture from uh a couple days
ago from a Lio Community staking Meetup
these are kind of 11 leaders within the
ligher community stakers from 11
different countries all running their
own
noes okay so how do we find a synthesis
here I think we have to start by um
pushing back on the myopic focus of
solar stakers so I
mean um one way of looking at this is I
agree with Anders his point and his
point is um focusing on if solo stakers
might
solo uh might stop solo staking to a
higher degree than delegating stakers at
some specific yield is more important
than if they change
modality yes so stakers are
indispensable and we need more of them
but the overarching emphasis on this I
think is missing half the
story and one to reformulate this is we
need to if we care about using issuance
to improve geopolitical decentralization
of the underlying nodes we need to pay
just as much attention to whether or not
onchain delegating stakers might stop
staking to a higher degree than those
holding their e on exchanges at some
specific yield I know that's a mouthful
um bear with me in other words the
answer we're looking for really balls
down to the shape of the respective
Supply Supply curves of different types
of operators in question again technical
jargon but I'm kind of addressing two
audiences here
um this way of looking at things I think
was extremely well formulated by Barnaby
back in February so the sort of the way
he broke this down into the questions we
should be asking ourselves I think was
um was beautiful and and extremely on
point
um having said that I don't think anyone
has has quite answered uh these
questions and there are different groups
working on looking at the supply side
but none of them to my knowledge are
actually um specifically looking at
answering the way barnab has framed this
problem and I think without this sort of
analysis we can't really be sure whether
or not um enforcing an equilibrium
according to uh you know uh here I'm
Focus on anders' practical endgame we
can't really be sure whether this will
have a significant negative impact on
the composition of the staking
set okay so what's a possible path
forward I have six minutes
um barring enough confidence on the
shape of the supply Cur for different
types of operators one possible path
forward as I see it today is to build
off anders' latest practical endgame
proposal which I think is actually
semi-reasonable um very well
articulated um very beautiful read if
anyone has a spare week to uh to get
through the post um but very
inspirational for me um in terms of
seeing how how his mind works and how he
thinks this is kind of how uh what he
proposes okay this is an initial latest
proposal where you sort of you never
have a yearly issuance rate of more than
different curves that could satisfy this
sort of the three X's are on the B botom
are I think his his preferred curves and
then there's also like uh sort of a a a
curveball um solution he outlines well
okay we could just cap it at 0.5% sort
of that flat Gray Line and revisit it in
in a few years time when we have more uh
insights on orbit ssf and and and and me
burn um and as you notice sort of they
Peak around sort of 20 30 million e
staked um and then they kind of smoothly
descend down and they do follow the
current reward curve up to uh you know
let's say 10 to 15 million e uh stake
but then they uh they diverge uh Peak
earlier and then come
down and right yeah um okay so I think
the find of synthesis we can work with
something that is mostly aligned with
this
um modular the constraint that we need
to try to depart minimally from the
current reward
curve and this additional constraint
comes from three
things um one improving the geopolitical
distribution of known should be a
property of
issuance two the macro risk of a
dominant coinbase is at least as
important as the macro risk of a
dominant
LST three we don't have a good read on
what the long-term supply curve looks
like even if we agree the supply curve
still has some room to shift downwards
from
here concretely I think this means
finding a mathematically elegant curve
that one the parts minimally from the
current reward curve up until this point
two has a good chance of keeping total
leave State close to 50% so this kind of
you know again aligns um if we're going
to find consensus here I think one thing
that that uh is kind of axiomatic from
the other side is that there shouldn't
be another money that dominates uh uh
Eve um and so if you're trying to keep
if you're trying to adhere to that you
want to keep the total e State close to
significantly increases chances of
calization so that means like doesn't
taper too steeply and that has to do
with kind of the validat Set uh you know
deciding to censor new deposits because
um you know as new people uh come in uh
their um rewards their revenue as a
whole goes down so um so you don't want
this to sort of go too
sleeply this is kind of like a really uh
simplistic back of the envelope sketch
that has
no mathematical properties at all but it
sort of kind of gives you an idea of um
this is the brown line of kind of the
design space I'm I'm getting at here um
although there are mematic properties I
think the Brown Line sort of uh Peaks at
there are ways of doing this that are
not violating the mtic properties of of
of an isurance rate upper
limit okay
another possible path uh simple
pragmatic um I think a way to Fred the
needle here is to add uh a fail safe to
the current curve so in other words to
choose a reward curve that sticks to the
current reward curve for longer until we
get close to 40 to 45% of each Stak say
before dropping down this can be either
aggressively in the spirit of sort of
Anar um or more smoothly in the spirit
of Anders
um up for the bait the idea behind this
is it acts as a pragmatic break on Stak
Eve surpassing 50% of the E Supply
um so with the current churn rate limit
realistically it will take another four
or five years for the amount of e stake
to reach
allow us to gather more uh real world
information on what the equ equilibrium
is likely to be under the current curve
um more information on what the sort of
the long run Supply uh curve looks like
before making drastic changes which are
inevitably going to be based on um less
than complete information I think the
more time we have to sort of uh get real
M uh data on this the more confident we
can be to make the change um
okay and sorry I didn't have time to
sketch that curve this morning um but it
basically just something that follows
the current world curve for longer um
then sort of comes down uh at 45% stake
in terms of you know being uh a fail
safe to avoid worst case outcomes okay
three questions to think about I have 56
seconds one what are the set of reward
curves that could build off anders'
pragmatic endgame post while departing
minimally from the current reward curve
um two how steeply can the reward curve
fall without significantly increasing
the risk of calization attacks is this
something we need to be worried about
given that the social air can correct
for it um I don't know that's open
question three what are the set of
reward CS that could satisfy kind of the
simple SL pragmatic path uh what are the
downsides here again haven't you know
haven't really discussed this deeply
with the other side so we need to sort
of uh start a
conversation okay now I think you can
all throw tomatoes at me I'm pretty sure
everyone from the lighter side is
annoyed at me and everyone from the e
research side is annoyed at me but thank
you um yeah
can you hear
me thank you Sasha um now the stage is
open for
questions I think we just start with the
first one do you agree the issue is not
in the curve but the fact we don't have
a way to increase incentives to active
participants solo stakers and reduce
passive ones
M no I don't agree I mean I don't
disagree but I don't agree either it's
it's one
factor why don't you agree well the
curve matters a lot but so there's um
you know if you could find a way to
increase incentives to active I mean
what do you even mean by passive
participants I guess whose question is
it whose question is it maybe you want
to elaborate a little bit more on your
question is the person still here
well if not then we just go to the next
one why do you think 50% of e should be
Stak it seems a very high percentage so
first of all I don't think that 50% of
if should or should not be Stak I'm just
trying these are kind of not necessarily
my personal thoughts this this
presentation they're kind of trying to
find some sort of consensus I think like
the way you find some sort of consensus
is to say okay the most important factor
from one side is if should be the
dominant money the most important sort
of factor from the other side is hang on
we need to care about the geopolitical
diversity of nodes like how do you find
a synthesis um
dominate EA's money while still like
giving you the maximum room to to to uh
decentralize the validated set so
that's
all next one is there a technical
solution to identify solo Stakes for
example some on onchain Z zkp and
preference them in issuance I'm not an
expert on on the latest there so I don't
know okay then we move on to the next
what do you think will actually happen
with the EF decision well it's not an EF
decision it's a community decision
that's why we were here otherwise we
wouldn't be here the decision would have
already been made and ethereum would
probably be worth zero um not because of
this decision being made but because of
the EF if the EF is a SLE decision maker
ethereum is worth nothing so I have no
idea um what will happen but it's not
the F's decision to make it's all it's
all of
us I think we still have more time
um should we also think of changing the
entry Q to be closer and close to zero
instead of changing issuance
curve um I'm not sure I understand the
question sorry sorry with
um sorry oh stop letting in new valleys
I think that's that's kind of dangerous
because you have like then you cement
like a an OG class of of people that
just end up uh you know living off uh
yields forever and uh yeah I don't think
that's healthy for the system I think
you need it needs to be more
fluid I mean I think vitalic had an idea
if you were to cap right you could
randomly eject and randomly come in I
think that's interesting but I think you
do need some sort of fluid uh
movement um are there any more questions
from the audience which maybe you have
not found time to scan it and place it
online we still have more time
yeah the gentleman in the white shirt
has more
questions hey um the zkp question was me
the technology doesn't matter I guess
the question was like if one of the
goals is increase geopolitical
distribution um Andor just like solo
stakers if you are able to positively
identify Solo stakers in a non civil way
then you could design the protocol that
way so there are solutions I think to
this like choose your stack but there's
like some way to identify people so like
is that part of the conversation of you
know preferencing that goal by
identifying solar stakers I'm not sure
if necessarily identifying solar stakers
is part of the conversation but like I
think part of the conversation is how
optimistic are we that we can bring in
new solar stakers right and this is kind
of like a a higher level than that but
it touches on it and I think like I
would say I'm like Lio as a whole is
very optimistic that we can bring in a
lot more solar stakers right and I think
like maybe and I don't want to speak for
um you know Casper or or Anar but I
think like the vibe I get is they're
actually much more pessimistic about our
ability to bring in new solar stakers
right and so if you are more pessimistic
about enlarging this set of actors um
then you might be more prone towards
reducing issuance um than not but I mean
people can disagree on this right um
thank you so much time is up Sasha thank
you so much for the wonderful
presentation thank very much um we have
five minutes for our next speaker Aro so
if you want to stay here you're highly
welcome to stay here adwise you can use
the bathroom but 5 minutes back thank
m e
hi everyone I excited to announce the
our next speaker that uh talk about
maximum viable security mvs a new
issuance
framework um by arom he will talk about
study about diverse value data set and
ethereum's future defends on defend
defendability is a key factor for
issuance policy
evaluation and fun fact about
arum he knows a lot of questions so
maybe he will pay attention he will ask
you question instead of you asking him a
questions welcome on stage arum
all right uh hi everyone happy to be
here my name is uh AR kilki and I'm
going to be talking about this paper of
Maximum viable security and it's really
a framework for how to think about
etherum missions and it's a work in
collaboration with adcv Danny mcnut and
Sonia Kim from
Steakhouse maybe I'll give just a little
bit of background because I'm I'm kind
of newish to crypto research scene
um I have been mathematician for about
pure mathematics and yeah over like past
six years I've been slowly sort of
transitioning to crypto research and uh
I work at Cyber fund right and cyber
fund is an investing firm and it's
founder Le and the most important thing
about it is that we um we try to
accelerate transition of um our economy
to cyber economy and by cyber economy I
mean an open uh
efficient uh cyber economy where
everyone on the planet can collaborate
right um and the reason why we're so
focused on crypto is because crypto and
blockchains is a value substrate on top
of which this cyber economy can be
built quick disclaimer cyber fund holds
eth ldo and is investor in P2P so what
are we're trying to do in general uh
about ethereum issuance
policy um I think pretty much the call
is clear we want to develop a a stable
sustainable issuance policy um and I
wanted to take a step back a little bit
and and think okay what could that
really mean and I came up with this four
simple steps um and the first one is set
the North Star and have a guiding
framework second is collect the
necessary data third is analyze
scenarios individually and fourth is
analyze scenarios relative to each other
um and I I would argue that we largely
have been focused on number three um uh
research led by ethereum Foundation but
I think all other threes one two and
four are um also very very
important uh so let's and basically
those four step is is the plan for my
talk so let's start let's talk about
North Star and framework so first why do
we need a high level framework well the
first thing is that it's an incredibly
complex topic with many many factors
right so we need to kind of find find
our way through all these factors and
second it's very contentious so we need
to Rally people around uh a Direction so
um that's basically and it's in my mind
it's almost unavoidable if we want to
come to a rough consensus right we need
some sort of North staran framework
which will guide us and which will help
us agree on something next is how how uh
do we find this Northstar what to
optimize for this one is Big by the way
uh for me I think we need to spend like
a lot of time talking about this what to
optimize for there's three things I
think that are floating around one is
Network ethereum right um another is
asset eth and a third one stakers
interestingly right um and I would argue
that uh the framework and proposals that
have been suggested by ethereum
Foundation mvi State cap are largely
focused on the asset eth while our
framework maximum viable security
actually is more focused on network and
um this is this is basically the the the
starting point of our paper is that
actually the network is the most
important and it's not to say that eth
is not important or stakers are not
important but it's important to
understand that the
the value flows from Network to asset
primarily of course there is some value
from the asset to network as well but
primarily value from from Network to
asset and also uh am uh about the
stakers this one is uh like um you know
we we all really love stakers right um
and especially solo stakers because they
bring most decentralization but let's
think about why we live love stakers and
we are stakers by ourselves so we love
ourselves as well well it's the reason
is because they secure ethereum right
it's not just by default we love them
right so when arguing about ethereum
issues we cannot think about stakers
without thinking ethereum Network we
always need to have this in mind so we
cannot just build something that is good
for stakers because stakers are
providers of security for the network
and uh uh uh I I strongly feel that and
I strongly feel a little bit of um
confusion in the community that you know
we serve stakers we like all our
conversation about stakers but they are
about stakers because they give us
something right so we need to ground
ourselves in the root cause which is the
network and I'll come to that later of
course and so what should be the
framework well I would argue and I think
most of people agree actually that the
Network's uh highest value that it
brings to the table ethereum's highest
biggest value proposition is security
neutrality
um so yeah so now if we take security
and neutrality as a framework and I
think this there's largely there's a
large consensus that that's the network
biggest
differentiator what what should we think
about well we need to to think about
attacks and there's three types I you
know there's more but these are three
main types of attacks if if actor has
sign uh and this attack is is
interesting because it is seen by
protocol protocol can detect it and
there is automatic slashing there 51%
attacks are trickier because uh you can
do short re works you can also censor
and these attacks they are not seen by
the protocol and gradual Co coercion by
state actors is an attack that we didn't
really see but it's very possible we see
it and it is also not seen by the pro
protocol and I would argue that uh
ethereum's autonomy it's a concept that
Gabe Shapiro uh came up
with ability to resist this these
attacks that are not seen by the
protocol is a very important thing to
think about right because if we don't
defend against these attacks uh in some
other way not but not in protocol but
out of protocol we are vulnerable so
what are the defenses well as I said um
there's cryptographic SL for a there is
social slashing for A and B uh but it's
pretty politically messy to do uh and
also like if if you want to automate it
there are ways to do it to some extent
but it's very complicated and you cannot
do it fully right that's why protocol
doesn't see it and I would argue that
you know the core uh defense that
ethereum has against actually all these
attacks is the decentralization that
comes from this RB validator set um
ensuring that no single party controls
any of the big thresholds uh of network
and this defense is preventive it's
apparent it's ethereum's biggest
differentiator if you think about other
networks uh eum has the most diverse
value said by far and I would also
stress that it is key to neutrality okay
neutrality comes from this fact um so I
would argue we need to think about
intentionally about this defense
mechanism and so the upshot of framework
is that we we suggest this mvs framework
Maxim viable security and neutrality and
it largely comes from geographically
distributed and disconnected validators
and if I were to contrast this with the
framework of
MBI it mvs strives to maximize security
of course you cannot forget about asset
you cannot about forget about um stakers
so without compromising the rest for
example scarcity of e um and mvi is is
sort of diff is the opposite IT
minimizes issues prioritizes assets
without
compromising trying to with not
compromise security and and maybe a
slightly different way of to think about
is that MBS prioritize expansion of the
network and
sustainability right over efficiency and
mvi does the
opposite okay coming to the second point
um of of the plan is the data collection
right and this is what I wanted to focus
a little bit on uh because uh I you know
there's there's basically a whole stake
economy uh built around ethereum staking
and I wanted to uh maybe talk a little
bit in detail about it so first what
types of stakers uh there are well
obviously there are solar stakers and
they have actually about 10% of the
market give or take on chain Tech is so
these are people who are onchain and uh
um yeah basically on chain but without
really sort of big restriction big
regulatory restrictions or something
like that and then institutions they're
also on chain but they come with their
own sort of restrictions and preferences
there's retail and then there's ETFs
which are not yet not there yet but
they're coming and we saw yesterday the
that ETF ISU actually acquired a test a
tested so we know they're coming um so
now the next point and this is probably
the most important Point uh that I want
to con is that the majority of the
staking Market 90% Works through
delegation there's no way around it
that's the that's how the market works
and we we need to think about this
intentionally and we need to I feel like
we need to almost accept it because most
of the talk is about solo stakers and of
course we want to support them right but
we really need to think how ether
emissions will affect uh delegated stake
so what are the types of delegations so
first is centralized exchanges uh they
have 20% of of the market um and 15% by
the way is is is by coinbase and they
charge a
quarter different there are different
fees but roughly they charge actually
charge this High fee is because their uh
you their uh users are sticky right they
they don't want to go on chain and they
just want convenience okay and as a as a
result there's very big sort of network
effects there economies of scale and
it's a not compet it's a really not
competitive market and it is fairly
concentrated with in coinbase and
binance next come centralized staking
providers so these are FS like P2P Kil
figment and these are uh you know
interesting they are a little they are
really it's a different Market segment
from centralized exchanges
they serve institutions a lot they serve
onchain teas and they charge way less
fees one to 5% why it's a very
competitive market okay there's many
many of those and because it's a
competitive market it is decentralized
so these are two sort of let's say
straightforward way to delegate uh stake
right and then there's a there's one
which is uh trickier which we all know
is these uh decentralized pools uh
liquid Stak in uh token pools and liquid
raking token pools like Lio ethery
rocket pool Etc so these are it's
important to understand that these do
not really run node operators they do
not valid validate ethereum they are
middleware that take stake primarily
from onchain teas and they distribute
this stake into various validated nodes
so uh for example uh um yeah some some
distributed to solar stakers like rocket
pool or Lio with their uh Community
staking module but majority actually is
uh distributed into centralized staking
providers and the core point is this you
know I have these three arrows here
three arrows here is because it really
distributes it uniformly which actually
brings a lot of decentralization to
ethereum so and that's that's the that's
that's sort of uh one reason why exist
and the the other reason is because they
provide also liquidity so you you can
notice that they charge roughly 10%
there's different fees and the reason
why it's higher than centralized staking
providers is because uh people who stake
with LST and LT pools they get liquidity
right and so they can get um defi yield
on top so that's the market structure
right and uh pools have 40% centralized
taking PR 25 and centralized exchang is
okay um all right
so I want to stress one other thing
about this whole the these markets I'll
speed up a little bit that actually I
feel like the market the Stak in Market
is kind of subtle it's not
straightforward it is actually segmented
it is segmented into centralized
exchanges with very sticky customers who
are inelastic to yield essentially I'm
not sure I'm not even sure they know the
yield they just think that um they know
that they're staking and they're earning
something but they don't really care
like is is it two 2 and a half 1% or
something like that right and then on
chain segment with csps lsts and lrts
and solo stakers where we have
sophisticated um participants who
actually uh kind of go between each
other and I would you know a lot of uh
arguments in the research they sort of
at some point say well it's a
competitive market so the margins will
compress either way I personally don't
think so and I do not and I think we
need to try to let's say really segment
this Market the reason why is because if
the markets not segmented margins
compressed we do not have hope for
decentralization centralized uh
delegated St staking is way way cheaper
and Superior so if it's all hyper
competitive uh there's no chance to
decentralize the stake so we really need
to find a way how we're going to
distribute the stake among many
participants and this is I think one
natural way as it happens and the
natural way is that sticky customers who
are willing to pay
exchang they stay there and centralized
exchanges their optimal solution is to
not lower the fees not compete with
onchain segment their optimal solution
is to charge higher fees you can think
of this as Pension funds Pension funds
you know uh even though they seem to not
charge really high fees but in if you
dig if you dig down intend the mechanism
they actually do charge High fees it's
because their their users are extremely
sticky okay so I feel like some
important message of course I mean
there's there's a lot a lot of analysis
needs to be done here on the costs on
the fees on the um on the stake
elasticity and but that's how I feel
right now and we at Cyber fund uh have a
grants program MBI grants program where
various teams dig into all this and so
watch out for the announcements of
various reports that we're going to
publish okay so analysis uh of the
impact right so from what I told you
what do we think will happen if we cut
the
issues well as I
said the stakers are sophisticated with
LST LRT and csps and so as a result you
know that uh their yield will lowered
will be lowered and they will churn and
so the decentralized market segment
actually
decreases centralized exchange stakers
are inelastic and so they largely don't
turn and actually that results in
centralized exchanges gaining market
share and solo stakers will turn um and
you know as as Anar and uh cpar said
potentially at a lower rate right
because they have very diverse costs and
preferences however we also analyze in
our paper their cost structure and
actually they have really high cost High
fixed costs and they're very inflexible
so their supply curve is maybe steep
marginally but I think it's very low
kind of at the lower end of of yields so
at some point actually there will be a
big Cliff a big jump a big drop of Sol s
so we need to really be careful right
about solar stakers uh and by the way
the you know the the amount of solar
stakers will decrease and they will be
unhappy that's for sure maybe we can
argue that the percentage of solar
stakers marginally will will will
increase but will it Mar Will it
increase long term I don't believe so
and that that's what we show in our
paper and then on staking providers and
middleware this is the more subtle thing
what's the impact well um here lsts and
lrts they have high costs and the reason
why they have high costs is because they
distribute the stake among like 40 uh
node operators so some of those not
barriers will drop and so what the
result of this is will be just loss of
decentralization or or red reduction
decentralization centralized exchanges
preserve customers and maintain margins
because they just have really really low
cost and csps lose customers but they
actually maintain margins probably due
to flexible low cost so so they cut on
their expenses on their personnel and
Etc and we show in our paper that it is
possible so they will likely maintain
their
margins okay so what's the upshot well
uh caliz Exchange Market segment largely
untouched the decentralized market
segment of LRT LS LST and CSP feel the
pressure so the issuance cut hits this
Market segment and so that some stakers
and some csps leave uh and as a result
centralized exchange market share grows
and we end up with less decentralization
undermining
security and uh important thing is that
we actually try to model this scenario
in the paper and right now coinbase has
ETFs assets are coming coinbase is the
main custodian for most of the ETF
issuers and so with the insurance cut we
show that with all this information
combined there is a very real scenario
that of coinbase achieving 34% of the
network um in particular under 40
million State e cap right so these kind
of uh these alarm that I'm alarms that
I'm that I'm making that uh market share
can sorry decentralization can be lost
are very real um and yeah I encourage
everyone to look at our paper and read
the analysis um and yeah
so I also wanted to sort of uh try to
apply our framework this Maxim valuable
security framework to some of the
arguments that researchers have been
discussing so the first is real versus
nominal yield so one thing that you know
as a mathematician I really uh you know
appreciate the beauty of that
uh whole argument and construction but
from the Practical standpoint I feel
like it's uh concerns with stakers and
not the
network right because we're talking
about the stakers actually earning less
than nominal yield right the real yield
is is less and but in some sense network
doesn't really care about that Network
cares about how many of those stakers we
have so I feel like that
argument is is is a little bit not in
the root in the root goal of of what
we're doing right and then current
issurance is costly it's another
argument and we in our paper estimate
and actually Anders also in one of his
papers estimates that actually the safe
cost from cutting issuance are in single
billions right so it's about four but
give or take and if you think about the
market cap of eth the Vol the trading
volume of eth it's apparent that this
price is relatively low for security
assurance that you get from it so the
the saving on costs uh is like on
balance doesn't doesn't is is not as
valuable as the security and neutrality
that ethereum gets from issuance and so
the last one is boosting monetary
hardness of eth well there's several
points here so first is Bitcoin won that
market right there's a there's a growing
consensus Bitcoin is a store of value
it's very hard to uh sort of compete
with that but even more importantly in
my mind if
Mone doesn't really come from hardness
of its INF you know issuance rate it
actually may decrease if we change the
monetary policy because we uh undermine
The credibility the sustainability of
our um issurance policy and also
security losses like if security or
neutrality sentiment is uh is suffered
we you know e Mone will suffer for sure
because the network and eth are very
very
connected
um and then yeah and then I would I
would even argue that if we want to like
if we want to think about e and if we
want to think about ethereum
contributors and how we really around
coordinate and really the whole
Community right uh actually bolstering
the network might be the best way to go
yeah I know the time's up I I'll I'll
speed up in just one
minute um yeah and then there's an
attempt
like a really quickly on relative
analysis right here we didn't do uh
there's there's almost no analysis out
there I would say that you know there
are arguments uh Pro Cut there are
arguments against cut but uh on balance
it feels like agre aggregating stake e
on the transparent and smart contract
layer right that boost decentralization
is better than aggregated in on the
opaque uh tread file layer with
centralized exchanges that undermines
neutrality and I would say that this is
this is also a very important thing that
we we haven't really uh done too much
research on but the both arguments are m
security aligned right the LST dominance
argument and the centralization uh
centralized exchange State concentration
they're both very important under mvs
okay I'll speed up a little bit so we
have lots to do let's
collaborate um let's accelerate what we
want furiously it's an infinite game
there's no end game thank
you thank thank you so much
Aro people have questions let me start
with the first one solo stakers have
paid most cast upfront Hardware time to
set up Etc maintenance is very cheap but
then why do you think staking via sex
Central life exchanges is more
inelastic right so well first of all uh
I would say
that you know there's a misconception
that stakers have uh costs up front
right and their fixed costs they're
actually variable costs and they need to
upgrade their uh setup over time so one
needs to take this into account second
you know solo stakers are people who are
very engaged in the community right and
they are very engaged on chain they know
their options right and that's the
reason why they are more more elastic is
because centralized exchange users they
don't think about ethereum
they think about their life they think
about their Investments that's why
they're in elastic solar sers sure I
mean I I I I admit they have uh diverse
uh cost preferences so likely they their
you know their their supply C is is
rather steep at least marginally but if
you think about this fixed costs you
also realize that actually at some point
of the yield it it becomes
unsustainable so it's a very important
point to dig further and we did it in
our paper encourage everyone to
read thank you there one more time for
one question as more e is stake real
profit margins go down even if you doubl
issuance why do you think staking
margins will not compress either way
yeah so I answered this question on my
fourth or fifth slide is because the
market is segmented right that's
our uh let's say main hope that
decentralization ation there is a
decentral there is a we can sort
of pay this for decentralization is
because the other users other stakers
other Capital
allocators uh will be uh will not let's
say will be willing to pay higher price
with centralized exchange is the
segmentation of the market uh and it
really by the way it's a fact that it is
like that right now if just take a look
at the fees 25% fee with coinbase and
you know 1 to 10% % uh fees with uh
pools and csps so Market is segmented
right now question will it be segmented
in the long future I don't know I would
argue that there's a very good chance
that it will be segmented for example
investment the whole investment market
right there's Pension funds and then
there's professional investment firms
it's a segmented Market as
well thank you so much uh time is up
arum and thank you for the audience for
the questions if you have any further
questions are to miss around you can ask
the questions afterwards thank you so
much
for
for for
welcome back to our forth session I am
really happy to announce our next
speaker it's Anders elosone and his
topic is about practical end game on
policy thank you so
much welcome the stage is
yours thank you and welcome to this
presentation of a practical endgame on
isan policy which is also the title of
my recent e research
post and we begin in in a hypothetical
future scenario perhaps a decade from
now where the cost of staking has come
down and staking frictions have been
overcome now people still have different
perspectives of the cost of staking and
Stak under varing conditions so this
really no agreement on the exact yield
that is sufficient for
staking people have different
reservation yields that is the lowest
yield they find acceptable for staking
they are at this point indifferent to
staking or holding the
token let's plot the hypothe
hypothetical distribution of reservation
needs we see here we have Stak in yield
on the xaxis and we have amount of stake
on the
y-axis a few might be willing to stake
at the negative yield perhaps to attack
or defend etherum many more are willing
to stake as the yield becomes positive
and at 1% Sten yield perhaps a lot of
token holders rushing
in this hypothetical scenario at 2.5%
half the E is St and as the yield
reaches beond four 5 or
almost all eight is already
staked and we can explore this further
by Computing the cumulative stake here
in blue as it rises to
one the cumulative stake can be referred
to as the deposit Dru that is the
proportion of all steak that is
deposited for steaking
and we can also call it the deposit size
then we are referring to the quantity of
Stak the total reaching 120 million if
all e the
state now let's remove the negative part
of the yield and flip access and we have
now created from a distribution of
reservation yelds what we generally
refer to as the stake supply
curve so if you remember at a 2.5% yield
half the E gets St
we add also the demand curve specified
by the
protocol and let's add
also 200k of Mev each year we then reach
at the intersection of demand and Supply
what we refer to as the stake in
equilibrium at the black
square but currently we are here and
this blacker isn't exactly known to us
so that's the situation we have right
now we're now ready to discuss the
motivation for reduction
initials if you note that over half
circulating Supply could be staked in a
a plausible scenario but it's this
General agreement amongst researchers
that 30 million e is perfectly
sufficient for retaining security and
here we would be at more than twice of
that so in on this range here what's the
cost why don't we want to pay more for
security than what is strictly needed
well for one we can approach cost rather
generally speaking of you know the
hardware that you need to pay uh the
taxes you need to pay for you know you
you have a liquidity you need to finance
the upkeep of of your software Etc and
instead natural to approach the cost as
the reservation yield if you remember
that's the lowest yield at which you are
willing to
stti and then since the supply curve
captures the marginal reservation yields
as shown previously you can compute the
total cost for staking in aggate for the
protocol as the integral of the supply
curve and so in this scenario oh there's
a
pick can I remove this yeah and so in
scenario the the total cost of taking
becomes 820,000
e for this specific supply curve that's
$2.6
billion there's also a
surplus uh
above the supply Cod so the marginal
Staker with a low reservation Shield
will have a high Surplus and uh the Marg
St will have with with a high
reservation yield will have no no
Surplus at
all let's now reduce isance with the red
reward curve this then pushes down the
staking equilibrium down to the red
circle
here this gives us a cost reduction
benefiting all token holders uh so we're
removing essentially Hardware cost you
know taxes we're removing liquidity for
users and the risk premium and
benefiting all token holders in the form
of a lower amount of newly mined
eat and that's around $1.4 billion at
the current token price we would save in
this hypothetical scenario there's also
Ser shift from uh stakers to allil
Holders but this just shifts value run
from one set of jues to another another
the cost reduction that's the welfare
gain we're striving
for and it's a wonderful opportunity we
have here to reduce the cost of a uses
you know uh a a simple way to frame it
would be don't buy things you don't need
you know this is not a sustainable
model and we of course need to focus on
facilitating sustainable economic
activity then some people say well the
yield makes ethereum attractive in
Europe it's fun to
stti but we have to remember that all
eat that is issued will also dilute the
token holders so there's nothing gained
you know in aggregate we shouldn't try
to tricker uses into believing so we
need to focus on facilitating
sustainable economic
activity or some people say well we need
inflation otherwise people just hoard
tokens well that's not true first of all
consider the fact that if you issue a
high amount of token then you compel
users to lock up the token staking
instead of having them available on hand
you know for paying your
transactions furthermore consider the
fact that of course if you if
you if you focus on what we're trying to
do you know the the the need to transact
is universal it's not really
affected and if we ensure that ethereum
facilitates sustainable economic
activity and that e remains sound then
the best option of a producers is to be
on ethereum transacting using
eth and so that's what we have to strive
for and then some people say well apps
rely on the Yi you know framing the
yield as somehow productive it's not and
it's not our role unfortunately to
support applications that do not
facilitate sustainable economic
activity that's not our job and if we do
so you know a high agan will always over
time turn into perverse
subsidies there's also a macro
perspective to consider High s
participation puts pressure on the
consensus layer here we have the current
scenario around 35 million e sted but
imagine a scenario where almost all it
is sted and then something breaks say
there's a discouragement attack the
censorship or there's U some client BG
anything else in this scenario ethereum
relies on the social layer as a final
recourse but what happen happens if the
social layer is sort of wrapped up
everyone has stake in a game well in
this case the social layer sort of
becomes
overloaded and we have come to a point
you know where we can lead to very
aggregated failure modes we would then
very much prefer the bottom scenario
where we have a neutral social layer
available High St position also can lead
to of course higher attestation load and
furthermore it you know if uh it put
pressure on the app player when one or
or few lsds comes to dominate this
money ethereum then is deprived of a
trustless sound assets which is one of
the most important crucial features of a
decentral blockchain and and you can
imagine if if you have control of the
money you sort of can control uses and
apps in in various ways that we wouldn't
really like furthermore consider the
fact that if apps build on top of the
LSD and then apps build on top of the
apps building on top of the LSD and
you're creating this sort of mono and
then something breaks then you are sort
of threatening you know the whole the
whole system here which is something we
really would like to
avoid so in conclusion even though
nominally the protocol might seem
maximally secure if everyone is taking
it turns out that but it's actually a
bit insecure both at the consensus layer
and at the up layer and we would prefer
the bottom scenario
here however there are also potential
downsides for adduction initials for
example sud stakers do not have the
economic scales of large staking service
provider so it's perfectly possible that
a relatively fewer solar stakers might
be willing to stake in the scenario
where the is where the yield Falls very
low there are arguments in the other
directions as well but still let's
explore this a little bit so we go back
to the first plot of reservation
yields and let's split up this
reservation yields into two classes we
have delegating stakers and we have
solar stakers so loosely defined here
now there are more delegating stakers
and solar stakers so I'm just
normalizing these two plots as well so
one scenario is that if we lean on
economical scale is that the resolation
yield among delegated taken might have a
peak in the distribution a bit lower say
at 1% whereas the peak for solo stakers
is at 2% well in this case we would
indeed see that the proportion of solo
stakers at the lower e Shield will be
slightly
lower the argument in the other
direction is that at a very high State
parti position and LSD comes to
dominated money so there's you know no
lossing liquidity if you own
the big seconding surface providers also
get better economic of scale and you
know it may be perceived as that the
risk of staking with them Falls because
they become you know too big to fail
there's no social layer there anymore so
that's a counter argument and that could
happen at any Yi depending on the exact
shape and slope of the supply
curve M also becomes a much bigger
concern for us as low
ISS it increases solar Stak is relative
Yi
viability and you know because they
cannot effortly pull their rewards
furthermore it degrades the incentive to
attest properly since me will be the
only thing that
counts so there's a lack of incentives
to attest and we can then consider
various way how to resolve this you know
we can try to increase the attestation
penalties all right so now we increase
the attestation penalties but then if
you are a staking service provider and
you drop attestation of your competitors
then then you can you can sort force
them out so then we have to have
proposed penalties as well all right now
we added proposed penalties but then if
you're a soul ster and you make one bad
proposal you can get punish very hard
because we have low editions as well you
know and you might be in the red for
several
years all right and so then there are
ways to try to soften this but there's a
lot of things going on at the same time
here that we're working on and it also
further complicates the design of orbit
S A you know the single slot finality
design because then there's also so a
way for Stak is to avoid having to
attest as much as possible taking as low
risk as
possible and so the lack of incentive to
a test can then lead the sers to De
deconsolidate and then we need to raise
the consolidation incentives and this
can of course further raise fairness
concerns and what we would like to ship
is me bur because this reduces all these
three
issues so that's something that that is
really important for etherum but we will
don't have it and we have to deal with
the S we have we're now ready to discuss
a practical endgame on isan's
policy so here we have the current
reward curve with isans Rising all the
way up to 8 1.8 million e uh with the
curve here we have the redward curve
shown earlier it forms by taking the
equation for the current reward curve
and adding the cube deposit size to the
denominator and I refer to this as a
practical end game
it's practical because it's something we
can strive toward without murn it's
practical because we should be able to
guarantee s Stak is to not have to pay
for staking and it's practical because
it allows us to design consensus
incentives in an easy way and and it's
also practical and it's an end game
because it allows us to
probabilistically stop the grow in stake
so that's why I favor the red reward
cover or something close to it this
shaded range is approximately where I
would like to be that gives us room for
a higher or a lower worker depending on
you know how the design works out and
feedback from the community others might
prer differentes per focusing on
stopping the grow in stake or increasing
the yield for solar Stak and this can be
discussed but you know if we go too high
you can imagine if we say go to 110
million each state and provide anything
about the bare minimum to avoid solar
Stak is pay you know then this would
feel like a misbalance of these
different Traders we're trying to to to
balance and then there might be a
movement to further reduces chance and
we would like to make a One Singular
change to isan's policy and that's why I
find that this will be slightly above
where we want to
be and you note that none of the reward
cures nor the Shaded range goes above an
interest rate of
security to to ensure security and it's
a at the upper end of any tradeoff I
think we should ever consider so
regardless of the exact end game that we
choose we could safely commit to never
issuing more than
feels like a rather attractive
proposition you know tell your friends
shoose ethereum shoose e there will
never be more than 0.5% of the
circulating Supply issued each year and
a cap on isance it's perfectly viable or
Insurance security whereas a cap on the
circulating Supply is not regard lot of
you are in proof of stake or proof of
work and from my perspective we could
just ship you know 0.5% cap solidifying
it and then come back to this in a few
years but there seems to be from the
community aspect we want one single
change so that's not something I would
push
for there are other ways to construct a
reward curve I'm showing here other
other Alternatives in in the it research
post like sigo shapes for example uh
with the equation PR
there let's now look at the impact of an
insurance reduction on
stakers we have here the staking yield
and we see that we
are uh showing it with meev now we add
the supply curve and we are able to
reduce the equum from 60 million down to
around 40 million
state but of course we are here and so
given some reason we might end up in
this region
here we must also consider a very low
supply curve and what would happen in
this scenario and here we have that bad
situation for the M micr when all almost
all e is St and we could then bring it
down to around 65 million e with the red
reward C in this
scenario and of course shipping mean as
well we come down to almost 50 million
each
state and it might seem like a bad
scenario but it turns out that it's
actually better for SE to be at the red
Square there than at the black square
and that happens
because of this equation uh it's from my
post minimum vibration that sort of
started this whole conversation and it
captures the attainable change in the
proportion of the circulating
Supply so it's sort of like a
proportional yield or it's been referred
to as the real yield or the changing
ownership we have the yield that you
attain on top of the fraction line and
we have the inflation rate of at the
bottom of the the uh fraction line that
could be negative you know if there's a
if there's a high burn rate but
otherwise
positive and we can use this equation to
draw uh something I refer to as ISO
proportion lines and at these lines
across these lines the proportion of the
circulating Supply that you attain
remains constant so it doesn't matter if
you're at 1 1.5% yield 2.5% yield or 3.5
% from the perspective of the stakers
once you account for delusion effect if
everyone almost Stakes you get the same
proportion of the circuit in the supply
let's draw more of these lines it's like
a topographical map you know with
counter lines indicating equal
elevation so at this map you want as a
St to be as a high elevation as possible
this equum at the red uh area is not so
good even though the yield is high
because you're at low elevation
any equum above the dashed curve is at a
better higher elevation so the orange
area here is better for us a Staker even
though the yield is
lower and here we have the supply curve
from previously and we see that if you
start here at the black
Square you have 110 million each Stak
than a say a
good as a Staker but you follow this is
a proportion line all the way to the
other equum that's possible on the disip
curve and you see that you're equally
well off as a Staker at a you know
you are not suffering from
delusion and the optimal situation here
is actually at this at this red square
here where you at the highest elevation
is possible on the
map but this is your sharpless shifting
around you know it's not the for insance
the motivation is for insance reduction
the motivation is the cost reduction but
it's important to understand this as
well it's very important to emphasize
this and just as a concluding remark a
checklist on the Practical and what
needs to be done there needs to be a
theoretical uh foundation and we have
shipped it there's a cost reduction and
there's the micro perspective we need to
have curve parameterizations and they're
available in the post and
elsewhere uh we need to design orbit ssf
consolidation incentives and I I posted
yesterday a post on that so I would put
it as yellow because it's a draft post
but it's sort of outlines approximately
where we would like to be we also need
to redesign eum's consensus incentives a
bit if we push is down close to Z and we
have been working on this a bit but as
you noted the discussion about this
senses but there's a few things qu to
work out so I put it orange if we push
me Buton both of these becomes Greener
because you know then the issue isn't
that big
anymore I also working on a
probabilistic agon analysis that I will
post uh in the first quarter of next
year and that will uh I so I will put it
at Orange and that would be like a
foundation for my perspective of why we
can do it
uh from the perspective of you know
decentralization
and we also need to build community
support and I'll put it at
Yellow by turning the other check marks
green we can also build community
support better you know and we build
community support of course by striving
for an ethereum that facilitates
sustainable economic activity that is
what we're working on in all these
different parts of the roadm that is how
we strengthen e and ethereum and that is
a suitable North Star in my opinion
thank you
thank you so much end this now time for
questions first one what do you think
about reward corbs with Dynamic
parameters yes uh I I have written about
this actually there a fq uh and I talk
about the issue if if the question
relates to the issue of trying to know
dynamically I adjust the reward code the
point is that it's not a way to to
address the issues that we have in the
long term in the long term it doesn't
matter you know we need to focus on the
one reward curve because that's how we
prioritize this these different aspects
you know so I think that there's there's
the idea of you know having some Dynamic
solution there's there's there's a
threat in it that you think that you're
solving something but you're not solving
it you're not solving it in the run run
the only reason why we would like to
have a d damic curve is if we have if we
go back here oh I can yeah but if you
have an equilibrium where you have to
lower with seial so much in the
beginning then of course and I describe
it a bit in fq then of of course you
could consider a scenario where you have
like you tick down the reward curve
gradually over a year you know so that
you don't make people uh get to lose uh
the staking so quickly making like it
becomes like very bad effects on
everyone if you just shook it because
otherwise the assumption is of course
that some are going to leave so the G is
going to go up again but but if you
shook it down and then uh the year
becomes very low there's a risk that the
solar sters are going to live before the
comes up
again next one how does the beam chain
proposed road map affects progress on
issuance policy well so my
interpretation of uh how how it affects
is that is it's essentially um something
that is sort of part of the idea is that
we we try to ship isan's policy as one
of these gradual improvements it's not
it's not like part of the beam Fork it's
supposed to be done
earlier so I would say that it's sort of
part of the overall road map there
yeah thank
you what would what would you say is a
good governance process to agree on a
new issuance curve uh rough
consensus that was a quick
one
um why does MV burn affect our needs for
consolidation incentives in orbit S ssf
no it's not M burn that effect it's m so
if you design orbit s
like a Bas basic idea of how you can
design orbit ssf is that you push out
smaller stakers so that they don't
attest as
frequently while you at the same time
give them the same yield so that's it's
sort of fairness still but the situation
is such that if you push out them from a
testing you cannot at the same time push
them out from
proposing that's a a a lot of bigger
concern because if we still have me in
the situation then we cannot make it
fair if we push down the ISS and then
you still gain a lot of the value you
gain almost all the value from proposing
and attaining this me you know there's
no mer burn in place then everyone would
like to be deconsolidated to remove risk
but they still get to propose as often
as today and so that's an
issue great thank you so much the next
we still got more time is there yield
when you might expect institution to
lose interest in staking or might find
alternatives to generate
yield long question does it compete with
some traditional Financial yield
threshold I mean the beauty of having a
reward curve is that if there's a loss
in interest in staking in general the
yield goes up you know that's the whole
principle so I mean it's hard for me to
cons the the option would be here maybe
implic implied is that
that everyone wants to stake but no
institution other than one or a few are
still willing to provide services and I
find it a bit perhaps tricky to
contemplate that this would be the case
but of course we we have to allow
various institutions to compete you know
we we cannot avoid that there's going to
be a comp competition it's we would like
of course for for there to not be but
it's not something we can avoid you
should we go for the last one there's no
V but I think since it's already here
let's answer it there's already so much
Financial investment by influential VC
funded actors even at current levels do
you think it's possible to make a change
that drastically affects their bottom
line
yes okay do you can you a little bit
more about the yes why do you think well
I don't know I don't think that VC
funded actors is like the biggest issue
for us it's I mean the biggest issue of
course is if solo stakers would feel
like it's it's a disappointment for them
so Visa funed actors is the least of our
concerns I would say in
this great our time is up now thank you
so much andas if you have audience if
you have more questions Anders is around
we happy to answer you your other
questions thank you so much thank you
I think we have three more minutes for
change for our next uh speaker so stay
here we just continue
sh
h
hi hi
everyone Welcome to our next speak
speaking sessions it's all about about
account obstruction we will start with
UAV rise he will talk about exploring
the future of account obstruction
talking about the past how it was the
current state as well as um the future
outlook road map of account abstraction
I welcome stage you advice
hi
everyone so yeah today uh so I'm a
youris from the etherum foundation I'm a
researcher working on account
obstruction and today uh with today in
this talk and the next two afterwards
we're going to talk about the state of
account obstruction where we stand now
uh and uh where we
headed right so uh
first we're going to briefly look at
where it all
started so the prehistory it all started
in uh so it started at the same time
ethereum started actually so uh V when
vitalic wrote about ethereum before the
launch he already blogged about uh what
accounts should actually should
ultimately look like so this was the
first uh mention of account obstruction
and then uh in the year in the following
years until 2020 there was a lot of uh a
lot of research done on this a lot of
interesting proposals and idea kept
evolving then in uh
trying to get to a count obstruction and
start experimenting with the
counstruction models without protocol
changes which uh makes it much easier to
get started and uh this has led to ERC
obstruction uh without protocol changes
but also without compromising on
sensorship Resistance by relying on uh
by relying on a on centralized Rel
layers so that's uh that's what we've
been doing with LC
requires having a permissionless m pool
because otherwise someone could always
sensor you but it's a but it's a
challenge and the reason it's a
challenge is that uh full account
abstraction means also abstracting the
validation and when you abstract
validation U when you abstract the
validation um it means that it depends
the Val the validity of the transaction
now depends on mutable state so it can
so this enables a lot of Dos vectors A
lot of denal of service attack vectors
that need to be mitigated just to give a
quick example of such attack and why we
need to to uh why we need to solve for
this is uh let's imagine a an attacker
implementing an account H and this
account depends on a this account uh has
a dependency on a flag stored in a singl
tone smart contract so every account
using this implementation looks at the
same flag H in order to determine uh
transaction validity and also flips the
flag and now the attacker sends
thousands of such transactions on an
ongoing basis every time such
transaction gets H when a transaction
gets included it immediately invalidates
all the other ones so they can't be
included in in the chain and now they
have to be dropped and they have to be
dropped without paying for gas because
they're not valid so we can't charge
them but we but they still caused a lot
of validation work for every node in the
mol and this can easily escalate to a
point where the nodes cannot do any
useful work so we need to mitigate for
this kind of
attacks and uh the way to do it is to
separate between validation and
execution so that we can limit what can
be done by an account before execution
before it agrees to pay for the
gas now the question is what do we want
to uh what do we want to limit what kind
of restrictions could we apply the
easiest uh the easiest way the
no-brainer is let's not let's not let
the account access any state outside the
account until it it's until the
transaction is valid so it can only
access its own storage it cannot access
any other contracts and it cannot access
environment op codes such as a timestamp
or a block number so this solves the
denial of service problem but it also
limits usability quite a bit so for
example you cannot support popular use
cases such as H paying for gas using an
erc20 token because you cannot look or
modify the balances of that ec20 token
during the validation so it so over over
a couple of years we worked on a
developing a set of rules a set of
validation rules that support as many
use cases as possible while still
mitigating denal of service and this
enables use cases such as paying us with
the tokens and many others that wouldn't
have been possible
otherwise uh the me so the way it works
is H these rules are applied at the
mempo level
um the mempo will only propagate
transactions if two conditions are met
one the transaction must be valid and
two it must also comply with the rules
so a valid transaction in an account
that doesn't comply with the rule will
still not be
propagated now fast forward to the
present where are we
now so ERC 437 went live last year and
it gained quite quite a bit of quite a
bit of adaption there are now uh there
are now over 20 million accounts mainly
on different layer tools and a lot of
activity what's interesting is that uh
most of this transaction the vast
majority of the transactions actually
you also do gas abstraction using pay
masters which greatly improved the ux
for situations like onboarding we are
obstructing gas and this alone this
alone is a great Improvement
and over the so um over the past two
years we also saw a lot of great
projects a lot of awesome stuff being
built by the community some of it is H
things that we really couldn't imagine
before and uh I'm not going to dive deep
into this because uh one of the next two
Talks by Tom is is H precisely about the
diving into the numbers and interesting
use cases so be sure to stay for Tom's
talk another development is that the
public account obstruction mle just went
live so before uh uh so the idea with
the ERC 437 has always been to have
censorship resistance by having all the
bundlers connected in one peer-to-peer
Network one M poool where transactions
get propagated and this way you are
pretty much guaranteed that someone will
include your user operation but until
recently every bundler maintained its
own private mol and they were not really
connect Ed while we were still working
through the coordination of of this mol
and recently with a with an effort with
a coordination effort for the protocol H
three of the bundler imple three of The
bundler implementers Ether sport candid
selus um managed to uh finally bring the
to finally bring it up so now we have
this m poool and uh thanks I want to
thank these three teams and I should
also thank uh s of t a fast lane that
made it possible to uh to have the molon
polygon so uh thank you and uh this way
we have so now we have the mol running
on several chains and more are coming
soon I hear that also other bundler
implementations are going to join the
mle soon so we'll see it
growing now what does the future hold
where do we go from
here so one thing we saw is that uh many
uh so we started seeing layer twos
introducing native account abstraction
in order to have a better integration
more gas efficiency now the problem is
that they enshrined the modified
versions of ERC 437 which are not
standardized and this started calling
causing a wallet fragmentation so
suddenly we see wallets pretty nice
wallets that work only on one chain and
cannot be used on any other and that's
really not great for the ecosystem
system because uh if you found a great
wallet you like you should be able to
use it on every chain not only on one
chain and then look for another wallet
for something else so we realize that
this is actually not an account
obstruction specific problem but a
coordination problem that could cause
issues in other fields which led us to
start a rollup Improvement proposal also
known as roll call that's a coordination
effort with all the layer tools to
coordinate H standards that would
benefit the entire ecosystem after we
started this uh process and H both the
layer twos on board we started also we
working on RP
proposal native account obstruction
proposal for layer TOs and a layer two
that that uses this will get uh will get
a better better user experience and H
better gas
efficiency now what about layer one so I
said that r P 7560 is an RP it's for
layer twos but for for layer one we are
thinking more long term because we at
ethereum are notorious for taking our
time to uh taking our time and uh get to
get things right on layer one so this is
no exception we have a proposal called
EAP
account obstruction using e and the
dependency on eof means that it's not
going to happen very soon because eof is
not included in pectra but once it's
enabled it's going to enable a it's
going to enable interesting account
abstraction models and not limit us to
just one and it will enable things like
a improved sensorship resistance through
inclusion lists which are not uh which
are not uh possible to support otherwise
with something like
to and we're working on it um I'm not
going to dive H further into native
account suction but there's a the next
talk after mine is by Alex and this is
specifically about Native account AB
suction proposals so he's going to dive
much deeper into
this uh we also saw strong demand for H
for for supporting EAS to give EAS at
least some of the benefit of account
obstruction now it's not possible for an
EA to get the full benefit of account
obstruction because ultimately it's an e
eoa it still has single key single ecdsa
key that cannot be rotated but we can
still give it quite a lot of the
benefits and that's exactly what EAP 772
does it enables adding a code to adding
code to an EA without invalidating its
uh key so now the account is actually
both a smart account and an EA and this
works great with ERC 4337 because it
allows us to set the code to turn any
eoa into a into a 4337 account which
uses the 4337 M poool and this enables a
this automatically enables use cases
such as pay masters now you can have an
EA that uses 437 pay masters so you can
H for example pay gas with tokens or get
gas sponsorship for an EA
transaction and on this one uh there was
already a talk by light client that took
a deep dive into it so if you're
interested you should check out the
video for this
one now how does it all fit together we
have a so we talked about several
different account obstruction models
which would probably be confusing for a
h for someone looking into what to
implement so the answer is that the
account the the account model is
identical they all use the same kind of
Separation the account the same account
model same gas obstruction everything so
it's actually quite easy to uh build an
account that supports all of them so you
develop it once you can deploy it
everywhere on every chain whether it
whether it has some kind of native
account obstruction or not you can use
it uh you just use it use it everywhere
and once it's deployed it's a once it's
a deployed if a chain later if a chain
on which the account leaves switches to
a enables a native account obstruction
it will be able to benefit from uh from
the improvements
now the goal so this seems like moving a
bit beyond the count obstruction but
it's actually part of the same thing so
the goal with a c obstruction has always
been to go be to go beyond the
individual uh Beyond improving the ux
for the individual chain and to also
solve the cross chain problem and in a
minute you'll see why it makes sense to
use a count obstruction for this and
anyway now that we have the basis for it
it's time to start really solving uh
solving the chain obstruction problem
having great uh Coss chain
ux so the Cornerstone for this is that
the account obstruction enables
trustless bridging it's uh so with the
account obstruction you don't have to
trust a bridge operator you no longer
need these multi- Bridges and the reason
is that uh the operator is not in the
loop the operator is not a part of the
transaction in the sense that the
message sender is is never the operator
the message sender is always the user's
account as opposed to the eoa case where
a message Bridges have to sign the
message bridges are a part of the
transaction and are trusted in a sense
so with this the user can create a
transaction that actually operates on
several chains so we have one
transaction running on multiple chains
and the bridge operator can execute it
on all the chains on behalf of the user
and even transp apparently deploy deploy
the user's account on chains where it
doesn't exist yet but the operator
cannot change the account in any way the
account because the account self
validates its own deployment and this
means that now the account can validate
the transaction on on each of these
chains so once it validates the once it
validates transaction it means that the
bridge the bridge operator is not at
Liberty to mess with the transaction in
any way so because it cannot uh be
because it cannot uh mess with the
transaction we don't need to worry about
uh we don't need to worry about the
bridge operator so the brid which leads
us to lead us to um to bridging uh like
to trustless bridging and to
permissionless bridging so you don't
need a permissioned bridge operator
anyone can join and be the bridge
operator including the user uh including
the user or anyone else H as for the Gaz
with pay masters it means that uh you
can have the you can have the account
paying for the can have the account uh
paying for the gas using a pay Master on
each of the chain so the user only pays
on the source chain and uh the bridge
operator uses a pay Master deposit to
pay for it and and and then ends up
getting compensated from the user's
deposit on the source chain so that's
how we can solve
bridging and using a few more standards
some of which are being developed and
some will need to be developed we can
really solve the ux problem and make it
making it seem like using one chain the
idea is that uh the user will never have
to select a chain in the wallet and it
will feel like really using a single
chain some of these standards are so
among them are key stores with key
stores the idea is that you can uh run
any so with Kyo uh you can you manage
your credentials for your account on a
single chain whether it's layer one or
whether it's a designated ZK layer 2 you
can manage it in one place and know and
use the same credentials everywhere if
you rotate your keys they get rotated
automatically on can send a single
transaction that runs on multiple chains
and doesn't even doesn't even need to
hold the native coin of each of these
chains to pay for the gas so there so it
feels like using only the source chain
the wallet can also use a for use
something like intense solvers for more
complex operations so uh using in for
example performing a complex uh a
complex trade on multiple chains is
possible with in intense solvers but
unlike with the EA case here the account
can enforce the result and revert if it
uh if it doesn't like it which means
that uh the user doesn't have to take
risks when using
intents another thing is that addresses
uh that addresses will be come chain
specific addresses that's a standard
that is is nearly ready with chain
specific addresses the uh the address
includes the name of the chain the name
of the chain on which the address
resides and uh this chain is uh so and
uh it actually uses an ens name of that
layer to to give an example let's say we
have a user on yes we have a user on
polygon and uh that wants to send usdc
to a friend but the friend leaves on the
friend uses base so with this the friend
gives the gives the user an address that
looks like 0x12 three4 at uh at
base.
and the wallet knows how to deal
with it so the wallet uh the wallet can
look it up it knows how to bridge to
base and so the user pastes the address
the usdc gets sent and there's no need
to uh there's no need for the user to
even notice that they're actually not on
the same chain in order to to achieve
this um the ens name for each of the
layer TOS actually refers to a few
records that help with chain Discovery
the reason we need this is H we're going
to live in a world where there are many
layer tools and many more coming up like
every month so we don't we don't want to
configure the wallet to support it of
these chains we want we want automatic
Discovery so with ens we can get just
that we can have for example a we can
have a record for a standardized Bridge
so now the wallet can look at an address
and find out exactly how to bridge to a
how to bridge a assets to that chain it
can have a record for for RPC provider
so if the wallet needs to transact on
this H unknown chain it has an RPC to
the to use and then it also have a and
it doesn't even need to trust the RPC
because there's also going to be a light
client implementation a ccip based light
client implementation that can validate
the chain the chain State against its
layer one contract and this is also a
record so the wallet is able to
communicate with every chain and it can
communicate with with every chain
without previously knowing about it by
just looking at an address and then
resolving everything knowing how to
trustless transact on this chain from
the user's perspective It all becomes
chain so the so account OBS suction is
already here it's already thriving
native account obstruction is coming and
uh account obstruction is already
improving ux on many chains now but in
the future in the near future hopefully
it's also going to uh improve the ux
across different
chains and in the future it's going to
feel like we are using a single chain
rather than multiple chains but with the
scaling that comes from our Layer Two
strategy and all this without
sacrificing decentral ization and
censorship
resistance uh all right and I think we
passed our time so any
questions
yes thank you yeah thank you so much for
the wonderful session um we start the
first question how are we supposed to
develop a 433 4337 wallet in the in the
entry point contract keeps changing
yeah so the entry point contract will
not keep changing the last change the
last change was hopefully the last ABI
change ever unless some critical
security bug we're unaware of is
discovered and forces us to to change
something which can always happen but
unlikely at this point if not then maybe
there will be some minor bug fixes
inside entry point but not something
that would affect ABI and require
changing wallet implementations
do you think we will need l2b style risk
dashboards for different wallets to make
users aware of what these wallets
actually do definitely I think l2b is
doing a very important work on H on
layer TOs and we will need this for uh
for wallets it's actually not just for
wallet we need someone to verify that
the wallet does what we expect it to but
also when we transact across different
chains even though we want to make it
transparent to the user these not all
chains are equal and some actually are
riskier than others l2b does a great job
highlighting these differences and we'll
need uh and we need to also account for
that so
yes does 772 require the wallet provider
to be okay with upgrading the eoa to a
Smart count what happens with a wallet
provider after upgrade practical
practically H wait I'm not sure I
understand so you so uh maybe the person
who I mean I mean yeah they it does need
the I mean yes of of course uh you need
to add the code in order to use it so
you need to add 4337 code to the account
and then you can start using it as a
understand the last part of the question
maybe the person who raised the question
do you want to elaborate a little bit oh
maybe I mean maybe by saying wallet
provider they're talking about the
wallet as in this the part that runs off
chain on the users machine in which case
uh yes the wallet has to be uh the
wallet has to be aware of the
implementation but the wallet is the one
setting the implementation so now the
wallet the wallet will determine what
code gets set into the EA and will will
use whatever it can also
support great let's move on to the next
one what is the plan if there is a
critical vulner vulnerability on the
entry point it would be a Black Swan
that would compromise all wallets at the
same time and by definition it can't be
revoked in Mass yeah you could ask the
same question about uh about something
that doesn't use something like entry
point because because I mean what
happens if there's a critical protocol
vulnerability in ethereum and then we
also and also a lot of accounts get
compromised so hopefully we audited
things uh enough to prevent such such
occurrence and uh if it does happen if
it does happen then yes we will need to
H we'll need to deal with it at some
point where it's where it becomes such a
big thing on the network you have to fix
certain things by hard fult so let's say
EA was compromised somehow we would need
a hard Fork to uh to deal to deal with
it because we are not going to allow a
situation where every account on
ethereum gets compromised so it's quite
similar whether it's account obstruction
or
EA what's the main technical challenge
of key stores next one the main
technical challenge is being able to
access layer one state during validation
and the way to do it is by uh by having
an rip supported by all the layer TOS to
access layer one state and then you can
have a key store on layer one this is a
so there are currently two two such
proposals one doing a l1s load meaning
you're able to load a slot from a layer
one contract and there is also remote
statical that would let you perform a
statical on layer one either of these
proposals would enable H would enable
key stores efficiently because now the
validation will be able to actually use
that and this will become a part so a
part of the proof of the proof used by
the layer two will prove the correctness
of this
lookup okay the last question should we
adopt AA now considering future features
you mention might not be backwards
compatible I don't recall mentioning
features that are not Backward
Compatible and actually our goal is to
make it Backward Compatible it's uh so
if you develop a 43 have an account now
H you'll be able to easily make it work
with a future uh Native account
obstruction proposals and I think the
time to adapt it is definitely now
because otherwise you're not going to
get the benefits of H even things like
stuff thank you so much the time is up
you have thank you for the wonderful
presentation you led excellent
foundation for the next speaker thank
you thank you
um you can stay here like we continue in
roughly 4 minutes for the next speaker
thank you so much
hi everyone I am very excited to
announce the next speaker it's Alex he
will talk about the top title native
account obstruction imp Petra rups and
Beyond as Speaker before you have let
the foundation and now Alex will Deep
dive more a little bit about Native
account obstruction the stage is to
yours Alex
uh hello everyone my name is Alex I work
on account obstruction and today I will
follow you stock with a deep dive into
the future of native account obstruction
and our plans for it so for the purpose
of this talk I suggest like we all agree
that we want native account obstruction
the way to for count obstruction is to
enshrine it in layer tools and the uh
main net and we need to answer the
following questions before we go into it
uh first we need to know which part of
native account obstruction is already
happening the next ethereum hard Fork uh
we need to see why it is not enough and
what is still missing for us to achieve
the account obstruction endgame uh I
want to explain how we plan to achieve
it uh and also Explain how other
companies and teams can participate in
this effort and honestly look at the
possible alternatives to doing what we
are proposing so uh uh and a quick recap
of where we stand with account
obstruction right now if somebody was
not involved into it so the first
account obstruction proposal ERC 4337 is
solved account obstruction uh without
making consensus changes on eum protocol
it uh allowed us with purely out of
consensus to uh provide a account
abstraction solution and it did solve a
vast majority of cases and it has been
released more than a year ago the main
it and the mol have have been launched
so it's no longer a new project it uh
has been used for a year by a very
serious project EAP 7702 is a very
important proposal because it's the
first time uh mainnet is getting some
account obstruction features uh this EAP
allows uh as you know EOS to like role
play for a time in smart accounts and
this scheduled for the next hard Fork uh
you have mentioned RP 7560 this is our
proposal to enshrine the design of ERC
it has been implemented and there is a
devet ready implementation and now we
also proposing EAP
but it is trying to be less opinionated
using uh Le less of uh uh uh the
protocol Parts uh and it targets uh
ethereum layer one and it relies on eof
to do so it's in early draft stage and
we request everybody to provide their
feedback on it uh so a little bit like
more on 7702 uh this is how the account
looks for once you update it with uh
but you also have Smart contract code so
it changes the behavior of current e
allows them to have code as well and
this solves fully solves the execution
part of account obstruction your account
can do multiple operations in the same
time do int whatever uh it is it does
not however solve the security part of
account obstruction because you still
have a private key you still have an EA
you still have 12 words that can
override your smart contract wallet and
there also needs to be another EA that
creates a transaction to use your
authorization uh the upside of this is
that it works great with ERC 4337 and
such accounts can be part of account
obstruction ecosystem and get gas
abstraction and uh many other features
so one question you can ask is like
great so next we'll just wait for the
rest of account obstruction to be
enshrined in uh uh e in it well if you
look at the uh specs for the next three
hard Forks this is the list of eaps that
are considered or scheduled for
inclusion in the next uh three hard
Forks like this is a long list like
these changes will take quite a lot of
time and so if we were to just wait out
for to introduce a account obstruction
on layer
one this could take very long time and
also it it's a high hard to clear in
terms of uh production tested uh
specifications uh ful spec road map and
it requires an unanimous consense among
uh core ethereum developers uh to do
such a feature uh it doesn't mean that
we will just wait for these things to
happen we have a lot of uh activity we
can do on layer tools who are eager to
innovate with account obstruction right
now uh another like alternative is just
to keep using in ERC 4337 like forever
so can we keep using it well kind of yes
it's good enough in many cases but it's
very much not perfect like the main
downside is it still relies on EAS uh to
act as bundlers so you have an account
abstraction solution but you still need
EAS for that uh we also create a lot of
complexity by implementing a lot of like
parallel technical Stacks parallel mles
uh parall bundlers and modifications to
the node uh and as layer twos want to
innovate they start implementing their
own uh Native account obstruction
Solutions there are chains C did that
and it is it is a problem because then
it breaks the compatibility and also
there are still uh new eaps that
introduced new features to ethereum one
big example is inclusion lease uh you
have mentioned fossil uh and this eaps
like don't benefit account obstruction
users and account account Vice vers uh
so uh let's zoom into a flow of a single
uh user operation in ERC 437 so what
happens is the user signs and creates a
user operation and the user has to
provide it to a bundler server the
bundler server then collects and other
user operations and uh bundle them
together and provides uh it as a
transaction uh to the blog Builder and
it has to use this uh conditional API
meaning that it performs the validation
and he provides a condition for this
transaction uh to be valid and then the
block Builder can include this as a as a
call uh onchain with RP
structures that we had with the bundler
and conditional API and entry point
contract uh part of consensus protocol
so it very much simplifies and flattens
out the complexity and for the user they
uh signs transaction and they broadcast
it to the mle and the protocol takes
care of the rest uh and the complexity
becomes part of the protocol but again
it's uh
simplified uh so how it works is that
already now like all transactions that
we uh broadcast to meole and include on
chain they have a validation code
however this code is not a solidity evm
code it's a you probably go codes that
uh blog Builder have uh we validate
signatures non balances G limits uh base
fees and these checks are done uh in go
as part of consensus and then the
execution is done on the evm uh with
parts and the validation part is also
solidity code uh that also runs on chain
and uh but it's it's still a single uh
transaction that is split into
validation part and execution part and
error in validation part means that
transaction is not valid it's not
included on chain and reverted it just
cannot be included uh in a
block uh so if you're familiar with RC
for transaction to take is to have gas
sponsoring and uh to deploy a contract a
smart contract as part of the first
transaction interaction so these are all
execution pathes in account obstruction
and this is what it looks like in
transaction type we add a number of
fields uh and what what happens during
this transaction flow is uh First Step
user creates a transaction sends it to
the blog Builder as part of a
transaction uh it's uh smart contract
gets deployed uh pay Master gets queried
if it agrees to pay gas for this
transaction then the account is uh
quered to see if it accept this
transaction as valid check the signature
and not and everything then the
transaction gets actually executed and
reaches the Target contract and uh if
pay Master wanted to it gets also notifi
that pay transaction execution uh has
finished uh however uh what need to be
said RP 7560 is not meant to be included
in Layer Two in its current form and
like the RP process itself was started
for uh feature that are common between
various layer twos but not necessarily
Target layer one uh it provides a lot of
uh uh flexibility uh because we don't
need unanimous agreement of all core
developers uh it's an opt-in process
where rollups can decide to pick up
features and implement it on the uh
networks and uh uh it's very feasible
and like logical for some RPS who get
adopted to evolve into eaps so uh what
prevents 7560 approach to being part of
the main EAP well a huge part of it it
uh defines validation as solidity
methods like we Define solidity method
that say and we say that this method has
to return correctly then the transaction
is valid it is a little problematic
because evm is supposed to be language
agnostic and methods are just part of
solidity programming language it's not
such a big deal for layer tws because
almost all of them already have some
kind of pre-compiled that are defined
fully in solidity and they already do it
uh another thing is that eof ethereum uh
evm object format introduces the
deployment time code validation and
account substruction could greatly
benefit from code validation however
without uh UF definitions we would not
be able to do it uh with the um method
selector
and it it can be a problem that your
validation code is a part of your
contract that can be called by other
contracts in some scenarios that can
lead to
vulnerabilities so a reminder in UF uh
the contract is being split into parts
so Legacy uh contract they have the blob
that includes all the code and data of
uh your contract with eoff the contracts
are split into the header the code
section and the data section what we are
suggesting with the EAP 7701 is to also
split the code section into uh into
parts that have roles assigned to them
so the contract would have an EF
validation code execution code any other
code and uh uh we can verify the code of
uh the validation section uh before uh
deploying such contracts and uh we all
like uh
this code doesn't have to be observable
on chain from within eoff but it is
still executed as part of transaction
validation uh so if we look again on all
the flow the flow remains exactly the
same just instead of uh calling specific
functions uh the evm executes uh certain
uh predefined sections of your eoff
contract and uh this allows us to like
get away from this magic method
selectors into more minut uh level
solution so now uh it's time to talk
about challenges of account obstruction
like people have been talking about it
for 10 years it's still not on mainnet
uh this is because it's actually hard if
you see somebody talking about
validation scope on account abstraction
you immediately think about this picture
uh and the main problems for that what
uh account substruction creates is the
cross dependencies between transaction
and validations and the the complexity
it you you get in building blocks
efficiently and maintaining a
decentralized peer-to-peer M Pool
efficiently uh so let me try to uh
explain these problems uh so the cross
transactional dependencies look like
that uh you have transaction four it
modifies the state and it makes the
transaction five invalid so when you
received the transaction five
individually it seemed valid to you
because X was a was uh equal to zero but
now you started building a block you
include transaction four first and now a
equals 1 and it's not a valid
transaction uh and in order to work
around this issue in in general we we
just have to split the uh transaction
into two parts and have the validations
run separately from executions in their
separate place in in the book so these
are still three account abstraction
transactions but they validation parts
are separated from them and they run
before any execution code starts
running now you may ask but what if
validations invalidate each other what
if the validation code changes the state
that another validation uses and in
general it would be possible and in
order to prevent that we need to send
box the validation code to prevent it
from doing certain things that it should
not be allowed to do so what are those
things uh it's accessing other people's
storage and accessing environment of
codes so environment op codes are block
number time stamp base fee everything
that may change from validation and uh
execution or between uh phases and other
people's code is a code in other
contracts unless it is in a mapping uh
mapped to your address and on layer twos
it's also any stateful pre-compiled so
this uh doing this is illegal all other
things are allowed uh in validation and
it allows us to do many great things you
can use tokens you can transfer tokens
you can uh do all of that uh in
validation
functions uh like there are other small
complexities uh like
one example is you don't need to
invalidate a transaction to make it hard
to for a block Builder to build a block
with account obstruction like one good
example is uh unused gas and using
unused gas as a vector for example
you're building a block you include five
transaction you see that you still have
a lot of available space because
transaction four requested 10 million
gas limit but didn't use it so you start
adding another transaction to your block
and what happens is trans four saw that
change in the state and started using
more gas and now you are like you have
it recursive like chicken neck problem
because now the transaction six doesn't
fit your block and you need to exclude
it and you can get to um to square one
like we do solve it by introducing gas
charge on a used gas but I'm just saying
using it to showcase the kind of
problems we need to solve uh when
implementing account obstruction
natively uh and another thing is
maintaining an efficient uh mle uh to to
receive a huge number of transactions
simultaneously and validate them you
need to to parallelize their validation
so assuming like here's a block Builder
it has six uh CPU cores and it's
performing validation of six uh
transactions in in parallel so it runs
them uh uh individually meaning they
don't access each other state and if it
finds a transaction that is not valid
individually it gets included from uh
blog building and the next step for the
blog Builder is to validate all
transactions that uh that remain that
are remaining in a in a smamp pole and
build an valid block if uh we were not
able to uh separate uh the scope of uh
validation code in one of these
Transaction what could happen is we
could have a mass inv validation event
when one transaction uh changes some
State and makes all other transactions
in your block invalid and uh it provides
a huge d uh dos Vector for mle
participants and blog Builders because
we don't want them propagating uh in
valid
blocks uh now uh developers who are
interested especially if you're working
on layer TOS what can you do to make
Native account obstruction happen first
like do get in touch with us on any of
our channels Discord Telegram and let's
talk about Native account obstruction uh
do just read and get familiar with
either both RP 7560 and EAP
um and you can also go dive into the
code uh this is the link to our
reference implementation of RP
for the rip process I guess everybody
knows it just join it add RP 7560 to the
agenda and discuss it with other layers
too and let's uh let's start building it
so here are our websites and uh that's
uh that's it
for thank
Alex let me start with questions the
first one is if 4337 bundles bundlers
don't yet support the aggregation
portion of the spec how can we read how
can we be ready to make it part of the
protocol yeah so uh aggregation is a
part of 4337 it will be part of native
account obstruction uh eventually we
have a draft EAP for that uh however
it's a complex Topic in itself the
aggregated signatures are complex and
there has been little adoption of
aggregation yet uh it does provide
additional challenges in the context of
native account obstruction uh but I
think we will overcome them and again
our approach is to make all these
changes very very modular we don't want
to make one Mega account obstruction
spec and implement it in one fork we
want to make like basically as many eaps
as possible uh reasonably uh so that
chains can uh adopt them meaningfully
but uh uh one by one uh
okay next one how critical and how
centralized
is are the bundled like is is BU is the
bundled can can I
see how sorry how critical and how
centralized is the bundle yeah I guess
the bundler um so in Arc 467 bundler is
critical not very centralized if you use
it correctly so if you're using it with
a M Pool
uh that is not uh like you you don't
depend on any centralized bundler
uh with the uh
becomes more of an assistant to to the
block Builder and then it's as
decentralized in the underlying Network
there is no added centralization Vector
uh on on the bundlers uh if that make
sense uh yeah okay thank you next one we
have 4337
all play nicely with each other and how
can we avoid once again fragmentation
the space in this case with regard to AA
account abstraction Solutions um right
so 7702 does not pose any fragmentation
uh challenges whatsoever because this is
just a new feature of of the evm and I
assume it will get supported like pretty
widely and it's also like it's an
addition to uh account obstruction road
map with 467 and 7560 we keep the flow
the user flow uh so similar that it it
can have very minimal traction uh like
friction in terms of fragmentation
because if you have two accounts and
there differences are so minimal I
assume just most wallets would support
both and both of them will coexist
peacefully for a period between uh now
and when uh 7701 is implemented on Main
net and and so like they are all still
part of the same ecosystem so it's not
fragmented it's just different flavors
of of the same uh same thing that makes
sense what's your recommended root map
for metamask to achieve the end goal of
account
obstruction yeah so metamask and other
wallets uh UA wallets they would be like
it would be great if they started
looking into account abstraction like
they can start with uh
include some kind of code uh in their
EAS it can be like very simple like
recovery or gas sponsoring and
everything but crucially it will uh it
will get a production experience of
having uh and managing a fleet of smart
contract wallets because up until now
like most wallets have only been
managing like the private Keys part and
did not look at users wallets as smart
contracts and uh after that like there
is no reason the for metamask not to use
ERC 4337 wallets uh for people who who
are starting now like you you probably
don't need to steer them into using 7702
if they are newcomers you can just get
them to deploy an upgradeable proxy
smart contract wallet and uh as long as
long as it's an upgradable proxy they
can evolve together with
account obstruction like versioning and
uh and all that uh
right what do you mean by other code in
Brackets section at
slide I I can I don't have slides uh so
uh you can have an any number of code
sections in an eoff account uh so any
code that does not have a role assigned
to it as we described it is just an
external code so it can be called by
like some other contracts or other
addresses can just call into this code
and if the code is assigned a role you
cannot call into this code it has to be
executed as part of a EAP 771
transaction right it's uh so this is the
difference between like other code and a
code with an assigned purpose in terms
of account
obstruction now the last
question what's the point of separating
validation and execution in ethereum's
account obstruction if conflicts can
still arise during execution even after
validation under restricted rules yeah
great question like uh the problem is if
the execution conflicts uh with each
other you can get a state you didn't
initially want for example you can get
the transaction to revert but the
transaction is still valid and another
thing is execution is not limited not
sandbox it can be a 20 million G
operation and it can write all the
storage in the world uh validation is
limited and sandboxed so we extract uh
all the validations because we assume
they are small functions relatively like
I don't want to say pure but clean
functions that only access accounts own
storage and if they were to
Collide that would make block invalid
the difference between H reverted
transaction in block and invalid block
is the difference between a block
Builder being dosed and somebody having
to redo his action if in the event that
his execution was dependent on something
that changed during the block L uh so we
we we really need need the separation
for the Dos protection
thank you so much time is up thank you
so much Alex for the topic about Native
for cter Section now we have like 4
minutes break and before we will Deep
dive more into our count OB sertion by
team 4 minutes break
hi everyone I welcome you for our third
topic about account obstruction this
time Tom will talk about adoption
analyzis how account obstruction has
been adopted and what are the standards
Etc I would like to welcome on stage Tom
hey everyone my name is uh Tom tan from
the ethereum foundation I'm a product
manager for the constraction team so
we're going to be a little less
technical in this talk and we're going
to talk a little bit more product wise
what's been going on the past you know
almost two years since we launched the
entry point contract to mainnet so um
this happened back in March
entry point 0.67 that you have talked to
with some minor with some bug fixes but
in general like you said there's not
going to be anymore any any API breaking
changes and the one of the important
things from deploying the entry point
contract is that uh uh a concern that
you have when you're talking about uh
adoption is fragmentation and if we go
back to the early days like when we had
a you know just a couple of EA wallets
web 3GS was very beneficial in a sense
you feel like okay each wallet wants to
bring their own thing to the table but
on the other hand you do want to make
sure that as a wallet provider I don't
want each application to have to develop
a different interface just for me the it
it creates a problem for the users for
the daps even for the wallet themselves
so having this very um popular smart
contract wallet prevents fragmentation
so since a con abstraction brings so
much to the table in terms of the
functionality it created this effect
that preent that you know kind of
coalesced everyone around this standard
and that is a very valuable side benefit
that we've
seen um so keeping in line with the
ethereum foundation and the infinite
Garden kind of theme it wasn't just
enough to you know plant that seed of
releasing the entry point contract we
also have to continue watering this
garden and making sure that you know
when you're a developer you need to make
sure that there's developer tools ready
in place and things like block indexers
so when people start writing code they
can actually you know look at
transactions that are user Ops and and
read them and understand them we had to
make sure there's a couple of bundlers
and wallet and SDK is ready when we
launch so people can start building on
that and in addition besides just making
sure that developers have what they need
and can build on top we also want to
start exploring account abstraction so
we gave out grants to teams to look into
interesting ways to sign Keys uh look
into complimentary standards like model
or accounts stuff like RP 7212 which is
um allowing uh you know using your key
to sign transaction but that key can be
uh you know your fingerprint on your
phone or face ID things which are very
popular that are very expensive to do
with EAS well you can't even do them
with EAS actually but when you do it
with smart contract wallets it's still
expensive because that method of signing
the key the the the cryptographic
function is not pre-compiled in the node
so that's very expensive so we want to
have that and through rollups we can
experiment with that education and
obviously also work on the user up mle
we had to make sure that eventually will
come and as we all know that has been
launched we'll talk on that about that a
later um so ethereum is not the only one
that wants native that wants aom raction
we have all the l2s and rollups which we
very much love cuz they're helping us
reach the scale that we need but we
again we do not want fragmentation we
want them all rallying around the same
standards y have touched on this in his
talk about the fact that as a user if I
have a wallet that works on this rollup
doesn't work on that one and on ethereum
it's a whole different thing that is
also something that we want to avoid so
to do that we introduced rip which is
the roll up Improvement proposal that
allows all the different r s to kind of
rally around the same standards um in
addition it's very much worth mentioning
that to when you want to add so those RP
proposals are very nice but if they
don't get implemented somewhere doesn't
really help us and adding things to
death but it's not that easy for good
reason you know ethereum as you as as we
know doesn't doesn't move that fast for
good reason but RBS want to experiment
want to start adding things and
they each we don't want them each foring
gu by their own because then that
creates a lot of work for them they
don't move as fast and again we're
starting to create this fragmentation so
the EF is working officially with
nethermind to build rollup G which is uh
basically the there's going to be a core
Fork of G that all the rollups are going
to work on together and each one can
also Fork that adding their own very
specific things that they need but
they're going to have this core a very
much a roll up um um friendly uh get U
you know a client that they can all use
and save on you know development time
have that security benefits of all
everybody's using the same thing Etc so
we also wanted to make sure that all the
you know different uh rollups and letter
twos are also aligned and we're all
moving in the same direction and having
the same
standards So speaking of standards
there has been just like an abundance of
standard that came out some of them a
few of them with are kind of like a I
wouldn't say like blessing our support
but a lot of them are just teams in the
ecosystem that realize that they need to
have H standards to move forward you
know in a way that is much better and
faster and more secure so I'm not going
to go over all of them there's quite a
lot and just the mere fact that I can
say that I probably missed a if few just
kind of shows how many there are but mod
smart accounts is one of the very
interesting standards that have Arisen
we have two 6900 and 7579 always good to
have some sort of like a competition
always breeds more better results uh and
I'm going to touch on that a little bit
later but things like 7702 and 7212
which I mentioned which is the uh using
uh web aan to or more specifically secp
transactions and a lot of other ones
ways of EIP 5792 is also very
interesting which is um you know the
communication between AD dap and the
wallet is when it was in EA was fairly
simple but once you start having a lot
more functionality in terms of like
batching and pay
masters we need to start making a bit
more sense of the API between those two
entities so there are efforts to also
standardize that and just like I talked
about web 3 back then this becomes the
new kind of thing that you want to
have um this has been talked a lot in
the previous two talks so I just wanted
to kind of give it a slide to reference
this but we are not stopping at 4337
this is what has been going up until now
but we are growing into more uh into
into the future which is going to be
native Eon
abstraction a couple of things that
are really accelerating the growth in
the ecosystem that we've been seeing and
at the top top of the list is M accounts
and I'm going to go forward just a
second and come back to this this is if
you look at the Smart accounts that have
been deployed by provider and you see
that little Lego piece I put next to the
one the list on the right there those
are all model accounts okay if we're
talking about alchemy and zero Dev P
economy those are all using ERC cc900
beneficial to the growth of the
ecosystem for the
and the and top is safe well because
that safe but um they've been around for
so long but it's it's showing you the
benefit of it because other teams don't
have to build everything from scratch
they can build on the existing Security
on the existing adoption and and
everything around that and just add the
models that they want they have a
specific way to do account recovery they
can take zero deps kernel just take it
as is and build a model that does
recovery in the specific way that they
want to add something or some unique
interaction with their pay master or
anything like that but is it's driving
growth in a very very meaningful way um
there's other things here that have been
very very useful if it's zero knowledge
that we're seeing a lot of Novel
approaches ZK email has been given some
talks they're doing some really cool
stuff um pay masters are not just for uh
sponsoring the users gas fees we've seen
some Innovative uses where you can have
cross-chain asset transfers there's
magic spend Plus+ there's also so Magic
by zero Dev basically allowing you to
have that single balance anybody who's
developed a wallet and has to show users
their assets across different chains
even if though it's the same usdc it's a
terrible user experience this allows you
to actually allow they're doing things
like where you put some money and lock
it up and then you can use the cross
chains with pay masters it's really cool
but it gives the users an experience
which is very very
friendly interesting point about payment
so a year ago 98% of the user Ops that
we saw were using pay masters like gas
fees were like like sponsoring gas was a
big thing for for applications we even
saw cases where applications would allow
users to connect with metamask or any
other EA wallet as if it's just an eoa
account but behind the scene they would
deploy a smart contract wallet use the
EA is the signing key only so they can
actually give the user the that gas
sponsorship CU it's just improves ux so
much we actually saw it go down to 88% I
believe that the reason to do that is
just because we're seeing you know more
functionality that is you know that has
become important enough so it's it's not
the only reason to have a user up if
it's transaction batching on dexes if
it's simpler authentication methods or
account recovery those have become a lot
more sophisticated and a good enough
reason to actually use a account
abstraction not just gas and uh uh
sponsorship um as you have mentioned in
this talk as well we've launched the
user off mle that bears mentioning and
Want to Thank The Ether spot team for
taking the lead on on on promoting this
as well as candid and cilas for also
taking a huge role in this H and um also
fast lane which will thanks to their
work we can also have it on polygon
because they've really helped solve some
front running problem there that existed
so this is been this this has always
been on the road map and we really care
about censorship resistance the
centralization and we love user
experience that is good but we don't
want to compromise on that so it's a
very important Milestone that happened
two days ago so we're very excited about
that let's talk some numbers so these
are numbers that you sometimes see
everywhere you know close to 100 million
user Ops over 20 million uh users
and I want to focus a little bit on this
well you can't really see the laser but
the monthly active users now if you look
at the numbers on the left hand side
here on the y axis see 3 million monthly
active users
really well well no not really you I
mean I want to keep it well no not
really you I mean I want to keep well no
not you I mean I want to keep it well no
not really you I mean I want to keep it
well well no not really you I mean I
want to keep it well no not really you I
mean I want to keep it gas prices are
going down so we're seeing the number of
sponsored user opts going up so don't be
disillusioned by the fact that the gas
is kind of staying the same it's just
because the gas cost is going down which
is good so we're seeing more and more
sponsored user
operations I want to talk about several
applications out there that have been
using account abstraction uh I feel like
now that we are able to do stuff that is
I've always been when I was talking
about ethereum a lot of the time I was
talking about the fact that we were
waiting for this perfect storm of all
the Technologies being together like I
said maybe the killer da already was
available in 2019 but we just couldn't
pull it off because we didn't have the
infrastructure we didn't have all the
supporting standards I feel like we're
getting now to that perfect storm and I
want to show those case studies to just
kind of explain how we got there so
picnic is um is a deex that exists that
is based out out of Brazil and they make
use of execute to bash transactions and
they make a lot the the the ux is much
simpler and it's also in a way safer it
doesn't protect you completely from me
but it does help in a web when you have
all the diff you're not signaling what
you're going to be doing block by block
because you're doing all the
transactions in one block um it's the
leading safe wallet index volume and
they also received a grant from us to
build an open source their defi
transaction Batcher called Jam you might
want to check it out and they're one of
the leading you know in terms of volume
by cons indexes you know in terms that
they're doing pretty well H even the
toll balance that they have on their
wallets you can see very nice growth so
there is the the point of this graph is
to show that there is adoption of
wallets that are using 4337 it's the the
usefulness is very much there and people
are putting their money where their
mouth is a Mana Walt is also a very
interesting wallet that also receiv
received a grant from the
EF uh basically turning people uh people
in Japan get a government issued idea
that has a chip inside that can sign
transaction and they turn it into their
Hardware wall thanks to account
abstraction they can do this interesting
key signing mechanism so they've been
working closely with the government to
explore other use cases and it's just
like the the experience is super simple
people they did an experiment where they
brought a lot of people elderly people
people who are not not only not crypto
people but not technical people and they
were all able to just easily you know
people are used to doing that with their
Visa card doing that with your
government ID is just the same but
behind the scenes you have a smart
contract wallet where this is the
signing key and you can have all
interesting ways of recovery and stuff
like that
so this these are very interesting stuff
that we're starting to see happening
fers you might have known them as Doo
they're the official uh uh um
collaboration app for Devcon they're
using 4337 behind the scene and I find
it very interesting because this is a
non-financial use case so that's very
fun to see um you get all the benefits
of having like a web2 experience for you
know as a Google doc but everything is
on chain you uh you know your identity
is under your control the data is under
Euro control all the benefits that we
know from web 3 you can enforce access
permissions on chain that leads to a lot
of interoperability use cases that are
interesting we've even seen some
traditional Enterprise adoption over the
past two years which is a Visa you know
they're the OG pay master in the way and
they've been they released their own a
token pay master and verifying pay
master and released some articles on
that Toyota has looked at you know smart
contracts for the cars themselves and
this is all on our our there's links in
our Twitter so you can kind of scroll
back and you see the links to those
articles and Sony releasing sonum L2 you
all know they're very much working with
us about Native account
instraction uh to sum up you know
account instruction is here um there's a
lot of factors that have contributed to
that why we are seeing this amazing
growth and it seems like we can finally
offer deps you know that we don't have
to compromise user experience in
security and also with the release of
them me we don't also have to uh
compromise on
decentralization um that's it
questions thank you so much
Tom now time for Q&amp;A session I think the
first one is already
there let me read it how do you see
smart wallet moving towards cross chain
compat
compatibility um so that's an
interesting questions um I I'm trying to
answer what I mean exactly by moving
towards like uh how will it happen so I
think uh you have mentioned in this talk
some interesting things that can happen
once we have a abstraction natively and
that will allow a lot of cross chain ER
capabilities if it's the key there's a
lot of challenges when we're talking
about cross chain uh to name a few is
asset fragmentation it's the key
fragmentation and those are the things
that as we we have native account
abstraction um we're going to see
solutions that actually allow you know
for users to have that experience as if
they're using one chain but not behind
the scenes it's going to be coordinated
across those chains using the
technology I hope I answer that okay I
think so yes the next question how do
you think um AA wallets will surpass AO
a leaders like like metamask
Etc and what needs to be
done I think it's going to be about the
functionality my personal opinion is
that and this is kind of touching on
this is related to this so one of the
challenges that we have is that when you
have an AA wallet and we're seeing this
kind of issue happening is that each D
bring each dap onboards the user to
their own smart contract wallet so
there's this type of fragmentation my
personal belief is that one once we have
this really killer application something
that really takes off on just like email
because when email took off signing with
Google became the way that you sign into
other applications so I believe that
once we have that killer application
which going to have an AA wallet other
applications might say okay sign in with
that type of account and that's going to
just be something that suppresses metam
cuz it's going to well if they stay with
EA only I'm not talking mamas
specifically I'm talking EA wallet okay
um because the functionality that the
users are going to get through gas
abstraction through transaction batching
through a lot better Key Management
you're not going to be I don't see how
EA can win in the long term like we I'm
worried about using an eoa wallet on my
dayto day and I don't see how that can
continue on if we want to have
mainstream adoption so by definition I
think the functionality is going to win
out and that's got to happen I think
do you think in the future AA users know
what AO address they are
using well in the future how future if
we're talking about future native
account abstraction there there won't be
an EA address so they will not be using
an EA address uh for now also with
current account abstraction with 4337
they also don't have an EA um
so they right now they don't know if
they have they don't know the EA because
there isn't one like the bundler has any
way they know their their contract
address but you know that's not
something they're really going to see
too much they're it's going to be shared
behind the scenes and they're going to
have like an ens linked and there's
going to be some sort of like
userfriendly address that they're going
to be sharing with their friends just
like people are used to you know URLs
and they don't share
IPS okay what are some user of use cases
you are said about besides pay
masters um personally well if I had to
list the two more things I'm excited
about are pay masters and uh Key
Management I think the way user Ops
allows you to basically add whatever
signature you want it doesn't have to be
just an ERC ecda signature I feel like
that's that's a huge benefit
because take for instance clave wallet
uh another great uh 457 wallet out
there they right off the bat the way you
log in is just with your uh fingerprint
or face ID and that's all you know and I
think that's a terrific use case for the
average person so yes Key Management
that's the second thing besides by
Master
Okay um we still have more time for the
last one will native um account
obstruction be more or less profitable
for bondas SL blog Builders compared to
year C 4337
I think that's a question that we should
have asked yavo Alex actually I'm not I
don't want to give just an answer I I I
I believe it's I mean yeah it's I think
it's a weird yes because like they said
when we're talking about like the eof
situation the way bundlers are is a
little different so I don't know if
that's if I can answer that correctly
that question no worries then me go to
another one um will AA wallets gain
adoption mostly non-financial use cases
to avoid the risk of fund loss on new
tech I think the other way around and we
saw that with picnic more and more
people are saying that you know they're
willing to put their money into a smart
contract wallet because they realize
that if they lost their key somehow they
can recover their account in a in a way
which is still self- custodial which is
still decentralized so right now if I
want to use a wallet an EA
wallet it's either a hardware wallet and
it's super hard to use or it's something
that's on my phone then it's not secure
this way I can have something on my
phone from a day to day but if something
happens I lost my phone I'm worried I
can go to my Hardware wallet and recover
it so I'm gaining that everything is
with a hardware wallet smaller things
are with my eoa but with EA it's just
like all or nothing so I feel like I
should be more concerned about using
eoas I mean time is up but yeah I think
think you're still around so people want
to ask question but um thank you so much
Tom I think we end off um the morning
session with youf Alex and you I think
we had a very great insightful three
topics about the future the past and the
current state of our abstraction thank
you so much Tom for coming and it's time
for lunch now thank you for having us
it's
oh e
the e
welcome you for their s this afternoon I
am happy to introduce
stormy storm sorry who data it's a
lightning talk last 5 minutes I want to
encourage you to scan the QR code so you
can place your question questions we
will have after two or 3 minutes time
for um the stage is
yours just maximize the
window great hi everyone um today I want
to talk about the gas limit and how we
can get a be a better understanding of
it
so this question comes up all the time
should we raise the gas
limit lots of people have strong
opinions on this but the truth is nobody
really knows ethereum is a complex
system and downstream of the gas limit
there are hundreds of different
parameters and bottlenecks and metrics
that need to be
detailed but this is a really hard
problem so over the past year um I've
been trying to understand the gas limit
in a more data driven way and the most
interesting thing has been learning is
State growth the state grows too big and
this is somewhat true but it turns out
that other bottlenecks are more
significant like history growth and
bandwidth so this is a this is a graph
showing that history growth is a much
larger storage burden for note operators
um compared to State growth so I think
that the only way for us to gain Clarity
on SC scaling ethereum is doing this
type of datadriven analysis answer three
of the most important questions related
to the gas
limit so the first problem is how do we
price long-term storage storage is a lot
different than other Hardware resources
like uh CPU or bandwidth because storage
creates a long-term commitment a
long-term is we come up with a new
pricing scheme for storage such as
multi-dimensional gas or state expiry or
some ZK thing and then we do a
datadriven comparison the current
scheme and this can be extremely
detailed we can look at every single
transaction and block and protocol in
ethereum's history and we can rigorously
examine
um another gas limit problem is how do
we make the worst case closer to the
average case great example of this it
brings the worst case block size down
close closer to the average case uh
block size and you might ask yourself if
we can do this for Block size can we do
it for a bunch of other block metrics
like the number of times the block
building we can evaluate this solution
sort of using the same approach um that
I just described where we look at the
entire history of ethereum blocks we
these new constraints might affect um
all the different um things that we care
about the hard problem because ethereum
is a complex system with hundreds of
different parameters and bottlenecks and
metrics but it's not an impossible
problem we can model all of these
different bottlenecks and metrics as a
function of the gas limit and use data
to inform those models and I think
ultimately this is the endgame approach
for understanding the gas limit and
guiding our decision on what it should
be if you want to learn more about how
to actually dig into the crypto data um
come to my other longer talk in an hour
on stage three and thanks for
listening and maybe people are still
typing but i'm interested to know what
what was the motivation behind deep
diving into this topic more like what
what what like inspired you yeah so
right now e theum um it's sort of
notorious for being more expensive than
other blockchains and this is due to the
gas limit sort of uh clamping down on
the amount of transactions per second
that ethereum can handle and there are
really good reasons for doing this um if
you allow too many transactions that can
compromise Network Health
decentralization other things we care
about um but we at the same time we want
to make sure that we're in the right
sort of Sweet Spot um in that trade-off
space okay thank you this so read one
question you use to collect the date are
they or we need better
tools um at this point the tools are
they're getting really good um and I
actually go into detail um like I said
in this other talk um in an hour if you
can make it but the short answer is I
use cryo which is a tool I built to
extract a bunch of blockchain data sets
and then I use polers to analyze that
data um and slice it up in a bunch of
different ways and it's really efficient
and really
robust okay thank you and um this
popping in now in um which bottleneck do
you see as lower hanging fruit to fix so
uh probably history amount of space on
every full node and we actually have a
solution for this that node um keeping a
copy of the entire history we move
distribution scheme and then all of the
nodes will have a lot more runway for
either the state to grow big or just
make it I think he said there would be
long format of his talk maybe you can
follow there and then place your
questions there otherwise he's there for
answer questions after um after this
session thank you so much five more
minutes and then the next presentation
will come
she
then no take it
off in the picture of the current eum
Network thank the stage is
yours thank you uh thank you for being
here so I'm Leo from migal laabs um so I
want to start this talk with a quote
from one of my um favorite scientists uh
computer science uh dictra and he says
computer science is no more about
computers than astronomy is about
telescopes and I think this is a great
great example and talking about
astronomy um I want to show this picture
it's a picture of the center of the um
Galaxy and actually there two pictures
look completely different it's actually
exactly the same spot it's the center of
the Milky Way and this is how it looks
with two different types of telescopes
the one on the um that you see on the
left is taken by a radio telescope and
the other one is used by a normal kind
of telescope so this is what scientists
do they create tools to look at reality
with different uh from different
perspectives and this is the work what
we do uh uh IM Mavs so similarly in the
ethereum space you sometimes look at
data from different perspective and this
is an example that I want to show what
you see on the left side is um this CL
Distribution on the consensus layer that
we OB connecting with different Bon
nodes um on the right side uh you have a
similar picture that shows um how this
looks when you look at uh the creation
of blocks using a tool that is called
blog print which we actually try to
improve and and manage to improve the
accuracy using a different machine
learning uh technology we actually you
can discard the QR code if you look at
the P if you want to look at the paper
but what I want to show here is that if
you really look at the numbers there are
some differences between one and the
other because uh what really happens is
that sometimes we have many many more
validators in one Bon node and then when
you took of these two pictures you will
see different realities in the same way
you do when you see with two different
types of telescopes and this is what is
really important that you really
understand um what is going on looking
at reality from different perspectives
so here for example if you look at the
green te has like 12% of the Bitcoin
nodes but in reality is creating 23% of
the in this is because apparently they
are focusing or NOS with really har um
High number of of
validators uh if you look at the
execution layer diversity this is what
we can see doing some graffi analysis NE
mind if you look at the same picture one
year ago you will see a completely
different thing so we have evolved but
we still have to do some work here uh of
course not all the blocks in the system
have graffitis that can that allow us to
do this work only about 133% of this of
the of the blocks have a graffiti that
allow us to analyze this so uh this is
important actually I want to say for you
guys Improvement of of useful graffitis
for in the last six months uh so that's
good uh but for those that are running
noes please uh try to help on this so
that we scientists can look at the data
and and have an idea of how things are
evolving uh now if you look at uh if you
want to look at things like ISP
decentralization and entity
decentralization well we have a lot of
data also in our dashboard the QR code
is uh is a link to monitor edwi where we
publish all this data um the figure on
the right shows the different I mean the
different entities that are uh a stake
in ethereum uh those that are in blue
are entities that have less than 10,000
validators the ones in green have
between 10,000 to 50,000 validators in
yellow you see from 50,000 to 100,000
validators and in red you have coinbase
with over 120,000 validators okay so
what we want to see in this picture is
less red and more blue okay that's what
this message should be about and if you
look at uh the isps about 15% of the of
the nodes are running on Amazon Cloud
that home nodes is taken in the network
so this is that still work that um that
we have to
do now um this is the geographical
distribution of the ethereum nodes again
on more blue about 30% of the nodes are
running in the US and there are plenty
of data centers all around the world so
maybe if you are running nodes in clouds
maybe we can move those to other places
so that we have a much better
geographical distribution as well
anybody knows how many nodes run in
Thailand in theum network any 23 23
nodes running uh in Thailand in the in
the tum Network okay basically what I
wanted to show is that um we come to our
booth next to the classroom uh see and
or you can call me uh and and ask me
questions offline thank you so much
thank you Leo now time for kunun um as
the question not in I have a question
you mentioned that in Thailand there are
of the nodes been running in the United
States yes okay and second place and
second second place would be the US uh
sorry the US Germany Germany has about
France okay
interesting um that means there's room
for other countries to speed up on the
amount of
nodes um the first question how do you
get to this data again so we have uh
multiple tools uh one of the tools that
we have is a crowler that is connecting
to the etherum nodes in the consensus
layer and we are developing another
crowler that is connecting to the nodes
in the execution layer in addition to
that we use other tools like chatu which
is developed uh by the devop team the
team of the EF uh that is also getting a
lot of data that is actually uh one of
the tools that we have used to do this
analysis on on on um the bco uh sorry
the the noes the blocks and uh we also
have another tool that is uh is called
Ed poer which is actually to analyze the
this decentralization of said market
share but your data shows
we have seen uh what I what I show here
was just 133% of the blocks have a
useful graffiti so what I sh what I what
I show here the figure was about the
data that we collected from 13% of the
blocks that has that are stuck with a
graffiti that we can understand so that
means it's possible that they have 5%
and and at the same time they figure
that I show is
correct okay thank you so much Leo time
is up but I'm very insightful um talk I
think you're still around if people have
more questions um talk to Leo after
thank you so much Leo thank
you you can stay here our next we is
ready I think we have like roughly 3
minutes onto the next
to e
next Pier his name is Mikel he will talk
about insights from plog propagation in
the eum P2P Network I want to encourage
enourage you to scan the QR code while
he's talking already scan the QR code
place your questions because we only
have two minutes after his talk to and
um go through Q&amp;A Mikel the stage is
yours probab makes it like a really
essential key component of the of the
consensus uh spec because pretty much
like the chain finality depends on
whether these uh Duties are correctly
propagated to the network and on time uh
of course every node has to run it and
it's even more essential on the
scalability road map towards beer do and
full
do so um in prob laab we are pretty much
interested about metrics about uh
protocols with idea of trying to
optimize them and making sure that
everything is working as they should um
and what we know is that uh these kind
of uh Protocols are pretty much
interfering with some external vectors
like for example in terms of blow
propagation there are some some things
like time gamings that take a a big step
into when blocks are propagated like
some block proposers are waiting a
little more so that they can extract
more benefit from the network mbb um but
we know also that block sizes take a lot
of um they pretty much Define how fast
are these blocks propagating over the
network and of course like the topology
of the network has also like a big
impact on how much or how fast are these
blocks propagating so gosip app in this
sense is like an efficient and fast way
of propagating blogs uh this um and as I
mentioned this is pretty much what makes
it like a right solution towards things
like pias or
scaling to more or bigger blocks blocks
um so it's not only that there are
external limitations like gosip have
some minor soft liit topic like the new
channels to disseminate like different
messages um have many weird things it's
kind of expected that there are going to
be duplicates this is part of the
resilience that it brings to the network
uh the idea is that spam a little bit so
that you ensure that more people get the
message not only one person uh and of
course like these kind of uh duplicates
have a huge impact in Bank width which I
I I know that at the time like it's
pretty much the constraints that we have
to increase for example The Blob count
um so yeah this pretty much gets even
worse when we increase the blog size or
the message size um so yeah in problem
we've been pretty much over the last
months analyzing how gossip shop is
working uh which we've been monitoring
like how gossip have doing um streaming
all the events internally and we've
pretty much defined like U we were able
to identify how many duplicates are
there happening in the network and what
we saw is that for example for things
like a Blog propagation uh 55% of the
notes or the blocks are coming or the
mathematics but the worst thing is that
beyond that 55% line there are like some
Edy cases where we receive almost eight
times the same message um and this is
something that we believe should be
solvable and we pretty much also took
the time to see like how much time does
it take from the first time we see a
message to the second time we received
the same message like the first
duplicate how much time was it passing
by and what we Define is that it's
actually pretty good time to try to
reduce it as much as we can so that
pretty much also like um try to enforce
like some other control message example
being able to say others that I already
saw a message please don't send it to me
which yeah it's just still going on like
many um consensus clients still have to
implement it uh but so collaborated with
the the foundation and the uh e panda op
team uh we've put like um a website U
where we are streaming like when blogs
aring at each uh well at the centry noes
that they are having and we believe that
this is a core component like uh
monitoring is really essential Leo was
previously talking about like these
things seem to be not like pretty like
ah yeah it's cool we have a dashboard
but the idea is that by having these D
dashboards we cannot only see how they
predict or at least anticipate to when
things are going wrong or for example
when new version are rolling out we can
compare to previous versions and we
believe that this is a core component
that we should keep in the link to the
post that we wrote like U there are many
things in gosip shab and each of them
pretty much has its own blog post so
yeah won't take much time from from the
speakers so much
Mikel I will ask you when did you start
researching about this topic how long
have you been on this topic do you mean
me like personally or or in so yes you
personally okay yeah um so I actually
was working previously with Leo uh I did
my PhD with him so I pretty much got
into ethereum and the l2p layer with him
which was I think like four years ago um
so yeah it's been quite a while okay now
we already have the first one can you
expand about what you use to collect it
your own tool or something else right
good question uh I forgot have an open
source tool called Herms uh if anyone
wants to know more feel free to reach
out afterwards but it's pretty much like
a lip2p based event Tracer so we've
implemented a open connections with
ethereum nodes uh and can keep them
connected so that we can trace all the
internal logs and this is already open
source so yeah feel free to reach
out what do you dislike about liap
P2P I'm not sure how how much can I say
about this um we don't have to we can go
to the next one if you don't it's um
it's pretty cool in the sense that there
are many people working on it is quite
mature but of course like all these P2P
uh protocols or improving things so yeah
I think that the mod modularity
sometimes is is the right module to add
like that I would say that that's the
part that it's harder for me to to
follow okay um I think time is up y um
so thank you so much for your time if
people have questions he's around so you
can ask him questions again thank you so
much Mikel thank
you we have two more minutes and then
we'll go to the next
talk so he can see around
n
hi I'm excited to pronounce in hand
followed later by his colleague Fong and
S for the Q&amp;A session and the QR code
have 2 minutes quick uh quick uh intro
on fasting testing fing testing is a
software testing me more efficient than
Tradition Way like unit test and about
uh we do a review on the on some
vulnerabilities discovered by fing in uh
noting that most of our areas like
consensus mechanism and the evm and some
of is uh smart contract however there is
not no no TOS for P2P Network layer our
work FS this Gap uh let's meu what we do
uh first quick recap on ethereum D P2P
protocol the ethereum execution layer
use da P2P protocol while consensus
layer relies on Le P2P our works mainly
focus on that P2P that PTP is a modular
and the layer Network protocol for no
Discovery and the session management and
data transfer in our F in our fing
efforts we many Fus sub protocols such
as discover for discover F RPX and uh
wear and
snap uh so why we fing on p2v network uh
let's take a final message as an example
if we send uh pH final packet handshake
first and then results are correlated in
a time order the sequence of message
matters additionally each no State Chang
dynamically based on the previously
interaction so uh it's creating a huge
State space this complexities May works
Let's uh it compos in consists of five
main steps first we generate a package
ACR according to the WT specifications
and forting a baseline then we introduce
variations in this package to see the
how Target node handles then we send
this mutate package to the Target node
like gas or something and collect the
response packet and the no State then we
can the response to look for any unusual
behavior like errors or crashes and we
found a interesting response with flag
the packet and first analyzed then we
select the most promoting package for
the next round of fing yeah so we call
this a fasting uh loop and we can in
this Loop we can explore the more space
and vulnerabilities also we got a l
logic fla or difference in programming
language
singon R user and so on each client
propose the packet and produce output we
then use a compare to uh compose uh
outputs our fasting method is not limit
to any specific client it can be expand
bra research on our research if you want
to report yeah thank you
thank you so much Tim um I want to
welcome your two colleagues for the Q&amp;A
sessions yeah this is a good question
but are there any sorry the first
question are there any issues found with
fcet test in existing clients uh
actually we are ongoing this fing so no
no issues found right
now okay there are no other but I will
have a question since when do you do
this research when did you start how
many years uh not a not a long time
about three or four months ago we began
the fing and began our engineer and the
research on the fing yeah okay then it's
quite
new okay another question from audience
so fasing input is generated randomly or
you use some seed yeah there are some
strategy for uh generate the see because
there are some correlated and dis uh dis
uh dispense on the package so we need to
use seed to SM the search space yeah do
you guys plan to do liap P2P fuzzing
yeah that's our next step we first build
our method to check if our Strate
strategy is efficient and we will do Le
P2P about three months later maybe put
yeah let like first question we are in
our our way
yeah we still have more time in case
okay someone
questions s
there's uh how long it's um I think the
next one is comparison to automatic or
you manually check for
inconsistencies uh sorry
is comparison to automatic or you
manually check for
inconsistencies yeah it's automatically
uh because there are some feature on uh
inconsist inconsistence like crash or uh
disorder on sequence
yeah um our time is up but I mean the
three gentlemen they're here so in case
you have more questions you're more than
welcome to answer them off stage and for
me it's my it's the end of my mcing for
today it's a pleasure hosting you and um
I welcome my other MC to take over for
the evening session thank you so
much thank you very much abna let's give
our MC a big round of applause you know
all the MC's are volunteers and they
really really volunteer their time they
sacrifice their schedules to come here
so we really appreciate you thank you so
so very much my name is Ross of the
crowd before we get ready for for our
next session all right now let me just
check with our stage managers they'll
let me know when the session is ready to
begin they'll give me a thumbs up and
I'm going to introduce the intimate now
regarding the Q&amp;A you can scan and send
your questions in early but also very
important when you scan the QR code on
the screen you can collect a card it's
like a little NFD like a PO that's much
better all right let me quickly
introduce our topic and our speaker
who's going to be coming on stage run a
full node not a light node not an
archival note but a full note home of
course now things have become very very
expensive which is why the topic for
today is optimizing full node costs with
monitor tools yeah running a full Noe is
extremely challenging and expensive and
Technical but if we really want to
achieve decentralization we need to make
sure everybody can do it and so please
help me put our hands together and
welcome to the stage our next speaker
J hello everyone this is TS Visa and I
come from uh before this project I want
to introduce am group am group is a
leading digital finance company and the
way and in the meantime Amber group is
also holding Am AC uh which is launched
for the build quest web St Innovation
challenges and uh I'm the da leader of
the am Group web St security team and
besides of my system contributor and I
man also execution PL uh for gas rest
and elegant and here's a picture about
my uh contribution in uh over the past
six years and yeah I'm all I'm I'm
continually uh contributing and let's
continually cont yeah so uh today I will
uh I will introduce a small piece of uh
of our uh Fund in the is history which
is occurred in the execution CL gats um
before the uh before uh before we di
into the question what it is let me uh
show you what we found in the monum
panel uh you can see there's some
abnormal uh points in the picture and so
we just found maybe say something wrong
and so we need to find what's
wrong uh but we are lucky we found found
some a
project process set use webset to uh
connect with the guas node and pull some
data back um so we fin the process say
we just P it um this is a piece of the
per uh fir graph and then so we find
this maybe something
server so what's the
problem um uh what we just write some
simple code to reproduce this Pro to
reproduce the is is so in the picture
you can see we have two Str one is L
result and the other one is interface
result and L which is uses json.
law
messaging and other one uses uh
interface and we also uh Lo some
Benchmark uh functions to just Benchmark
it uh it is really simple you can just
reply it with systemical code in your
machine
and uh here's a result uh in the picture
we can see yeah let's uh first one this
is uses less CPU and in the meantime the
memory usage is also smaller than the LW
message so here's the question uh in the
sub St say uh store the data as Jon do
law messaging and they use it to mure
and unasal again and again but the way
um what way we want to improve is just
it as interface and on the uh on the end
we just return the interface and M it
into the J
messaging and uh so this is a uh p and
add some Test cast yeah thank you all
right let's give him a warm round of it
was Json uh Json file and you're saving
so if I understand correctly you're
using Json file to save on memory space
and that's how you save your costs is
that correct yeah okay good so I'm not
completely an idiot uh you know I don't
come from a tech background so it can be
quite challenging for me but
nevertheless let's quickly look at the
screen we got two questions for you JS
Visa so let's look at the first question
at the top what do you dislike about the
clients that you worked on get Aron R uh
actually I select the CL I like so I
like guas I like and I like R but in the
meantime for some some other CL like
Jawa a this okay all right I appreciate
honesty you select clients you like
fantastic how much of oh excuse me one
uh one got voted to the top what other
problems did you find in
gets P um I think maybe a lot of other
issues uh but uh in my in my point is uh
you need to it or you need to uh improve
it it is depends on your workload it
depends on your company's workload you
need to First measure it that you need
to monitor it and say you can find issue
you want to fix or you want to improve
or others yeah all right we got 30
seconds you think you can do one more
question let's try quick answer how much
of a performance Improvement do you get
after the
pr um actually uh let me say maybe 133%
pretty good but it is just for uh web
socket notify says IPC okay you got 20
seconds let's do one more how how come
interface is faster than raw message
unpassed
bytes uh how come interface I think I
I'm not I'm not really de into set one
but I think because in the Go Side they
want to uh Marshall and UNM because you
every time you m Mar it into better and
understand un Mar back this is the
problem what it is yeah all right ladies
and Gentlemen let's give our speaker
another big big round of applause JS
Visa thank you so much
yeah thank you thank you all right now
again these are the lightning sessions
so so that we can go through as many as
possible before time runs out now our
next session is not going to take too
long we're going to be starting almost
immediately let me introduce the title
of the session the session's title is
updating gas cost schedule based on
reproducible benchmarks now for a
non-tech person like me this seems very
complicated but I'm sure you guys are
inside the hall because you and enjoy
these kinds of topics but before I
welcome the speaker for those of you at
the back please it's so nice to see when
the first few rows are filled with
people and the speakers also appreciate
it so if you don't mind wow I see
someone getting up to come in front
thank you thank yes another person left
oh God does my hair look that scary
anyway ladies and gentlemen without
further Ado let me give you a quick
introduction about the topic now I'm
just going to read the description you
can also see it in your Devcon passport
sponsored by the ethereum foundation
this project that I'll speak speaker
will be talking about evaluates the real
cost of executing
opcodes and Pro compiles in EVMS across
diverse clients now our speaker is very
interesting he doesn't have just 5 years
not even 10 years not even 15 years but
Financial applications high volume
traffic websites and Big Data Solutions
now he was not born into the web tree
environment he actually came and he
joined the ethereum e system and we
welcome everyone in ethereum one of the
greatest things that I found while I've
been Ming the Devcon and this is my
first Devcon is how positive me feel
like as if I'm at home now ladies and
gentlemen are you ready for the next
session yes or
no all right I know I know it can be a
bit tiring especially after you guys
have had a heavy lunch I only ask for
one big favor please make sure you scan
the QR code the questions quickly
efficiently and Target the most popular
questions first all topic please put
your hands together welcome Miss jessic
Glenn hi my name is yek and I'm here to
present our project which uh looks at
the Gasco schedule and uh uh try to
answer the question uh how accurate are
actually the gas cost that we associated
with uh each of the up codes so uh what
we did we created some methodology which
evaluates each up code and uh more
importantly we want to share those tools
uh results and then at the end we of
course want to look at the existing gas
schedule and uh update updated so um
what we did uh for each of the
conditions and uh different number of
times we execute each up code so we can
see that by increasing the uh the time
times we execute each up code the total
time to execute uh in thesis as well and
then by using some statistical to tools
we can figure out for each up Cod more
or less what time it takes and as we can
see the results are pretty consistent
for each op Cod but the differences
between op codes which also indicates
differences between um gas that each op
Cod should be associated with now the
same plus this gives us a good view of a
single uh evm client the same process we
replicate for uh what we want to do is
to remove any and we can see differences
and how actually uh each of the op code
uh consume time and um uh efforts on the
on the executing uh machine now what we
do it's a huge data set what we do with
this uh data set we want to analyze it
and say where our existing Gus schedule
can be updated so we came up with two
options first option option is more
conservative we take the existing Gasco
schedule and we try to fit the data that
we got from our benchmarks into this
Gasco existing Gasco schedule and only
update what is necessary so in this case
we can see that the mo mode was
underpriced we need to increase the
price of it on the other hand xort
behave behaves much better and we can
lower the gas associated with exp uh uh
going forward uh we also measured the
pre compiles in this case EC recover as
uh many people points out is much more
expensive than the the current gas cost
so that's a conservative way of updating
uh the gas schedule um now the other way
of doing it is more radical when we
forget the current Gasco schedule and we
start from clean page so we take the
least expensive uh op code assign it
with gas cost one and then gradually we
increase gas cost as we go to the more
um expensive uh op codes which is an
interesting approach because it's
completely new uh gasos schedule it's a
massive change but there are some
benefits of doing it if we do it that
way we can um uh Lowel overall cost of
each up codes because we start from one
and we know that uh evm clients are
getting better the machines are getting
better so it does reflect the reality by
lowering everything and by keeping the
cost of State changes and the same level
and lowering the computational cost we
increase the gap which might in the
future promote more effective use of the
data in smart
contracts um but of course does require
a big change on uh evm clients um anyway
uh all our methodology the tools that we
use the Benchmark the decisions that we
took on the way it's all explained uh in
our uh repo um the EIP is coming with
the uh proposal to change the gas cost
schedule once I finalize it I will uh
link it in the repo as well so thank
you all right let's hear it from Mr
Glenn ladies and gentlemen thank you so
much sir appreciate it gas gas gas
always the biggest conversation in the
room how can we improve our gas how can
we make it more efficient now we are
waiting for questions to come in so if
you don't mind helping me scan the QR
code I don't want to block it in my hair
but you can scan it and ask some
questions now I do understand because
the format of this talk is lightning
it's just 5 minutes sometimes you need a
bit of time to digest the content from
the speaker and I I totally understand
Mr Glenn I want to ask a few people will
actually taking some pictures of your
slides because I think they want to go
home and they want to read it if they
come and meet you personally later would
you be able to give them a copy of the
slides is that okay with you maybe if
people want to understand a bit better
they can ask you more of course of
course of course that's what I want to
hear so I know a few people were taking
out their phones and snapping pictures
don't worry our speakers are here
because they want to share their
knowledge with you the format of this
talk is a bit short yes I do understand
and it can be a bit challenging but
don't worry if you have any questions or
you want a copy of the slides just check
with our speakers they're so friendly
we've got one question on the screen
thank you so much let's look at it
together did you find or recommend new
useful op code to reduce gas costs with
your
experience it's a it's a vast uh topic
uh whether we want to add some new up
codes or uh um not from the new up codes
that we already added uh the M Copy is
definitely a a winner but can come and
measure it correctly and uh sign it with
some gas cost in the
future o just as you answered first
question we've got a second one are the
proposed new gas costs or are they
manually chosen definitely not manually
chosen I I uh recommend you going to our
Deo and look all at all the uh
methodology and statistics that we used
is one of the best I'll wait another 10
seconds to see if anyone else has a
question they'd like to ask and remember
the only way to collect your card to to
show proof that you at the session is by
scanning the QR so you have to scan the
QR and then when you enter the Q&amp;A
choose collect card okay uh we've got a
few more seconds any questions now again
like I said earlier our speakers are
very generous they're here to share
their knowledge of course a format of 5
minutes is a bit tricky so please if you
have more technical questions you want a
copy of the slides you don't have to
take pictures just ask Mr Glenn he's
more than happy to send you a copy all
right with that L let's give Mr Glenn
another big big round of Applause thank
you sir appreciate your insight into gas
costs gas gas gas always one of the
biggest topics and how to reduce it now
our next topic is very very interesting
and I saw some people coming in if you
welcome you to sit in the front closer
to the front closer to my Afro H you get
good luck from my hair you know people
have been asking me a lot of questions
and you know I have been giving them a
lot of answers because the next topic is
about where I used to work right I used
to work in the security department of my
previous company if you saw on Twitter
you know what company it is but I won't
say it now wow that's a fantastic
hairstyle wow two two great hairstyles
on the stage I hope someone gets a
picture of us together now the next
topic is about web three security and
how embarrassing it can be how many of
you you don't have to admit but how many
of you have ever experienced a hack or
someone you know has been hacked before
raise your hands per of the room yeah
not only just uncovering some of the
embarrassing web3 security problems so
many people fall victim web3 is great
crypto is great but there is extremely I
want your fullest attention on the stage
please pay attention and most
importantly ask good questions all right
without further Ado let's welcome our
speaker to
the oh that's a great background so
far uh
yeah no pressure just have to have
slides on the
screen otherwise I'm going to do this
with out
slides also I was really hoping that
there was a different MC so that if I
had to do something like this at least I
had the hairstyle
also I have a quite a long session I'm
definitely
taking okay can we just display it from
the Google meet and
I'll and I'll take
click okay great hey slides here we go
um great you don't great time uh okay A
little disclaimer to start I love
security like I go to a lot of security
events I meet security people and they
always have things like oh they enjoy
cooking and mountain climbing and doing
croquet um I enjoy security right in my
free time I also do security I also love
drama uh obviously look at my hair I
work in crypto as well and I love
renting which you're about to find out
um so my name is Andrew mcferson the
Alias I usually use is Andrew Mohawk you
won't figure out
why uh it's cuz I'm very creative uh
previously I built something called
multigo at poova I did inent response at
bitm uh I set up IR at Robin Hood I was
the head of security at Unis Swap and uh
I recently moved to privy the embedded
wallet company uh also shout out to
privy an embedded wallet company that's
about to let me rant about wallets uh
that's very kind of
them um I'm also on uh seal for this is
a rant a should in four parts that's cuz
they don't give me a longer slot if you
give me a 2our slot I will talk about it
uh we're going to go through each of
these uh progressively as we get on with
it okay so the first slide web 3 is just
web 2 plus one great at maths as well if
you're wondering um basically we have
all the intricacies of web 2 except that
it's inherently more financial which
obviously is a higher return on
investment for attackers um we also have
direct user to like infrastructure or
user to chain in our case uh without any
intermediaries so if you think of like
web 2 um if you go to an ATM and you say
oh I want to you know withdraw all my
funds uh they'll say like hey you have
to go to the bank well we don't have
that right what's a digital so you can
do it 25 hours a day and irreversible
actions which are the things we like so
you know that's something so the first
part is we are just generally failing
our users we as security people if
you're not security people that's not
for you um you know if I if I look at
the statistics here this one is is
pretty depressing it is that
where is least is less profitable for
attackers than drainers like ransomware
is everywhere they ransomware like MGM
it's very upsetting that that we lose to
these people uh there's also 340 million
lost in the first half of this year
which is crazy amounts that's more than
yacht money uh drainers are also super
common and cheap so you can pay like a
couple hundred bucks you'll get a
drainer it works across all networks uh
you don't need to understand how crypto
Works they have automation they teach
you how to set up Cloud flare and do
hosting and register domain they also
have redundancy so every now and then we
get their accounts banned and then they
have thousands of other accounts that
they'll use and say hey everyone come to
these channels uh don't worry we have
backups it's a lot better than a lot of
web 3 companies uh which is surprising
then also like the app stores are filled
with uh fake apps so I think this really
like sealed the deal for me when I was
uh working at Unis swap is that there
was some fake Unis swap app in the store
and I was like okay well I've got some
free time so take the app I'll decrypt
it I have a look at what what's in it
and it's just a web View and at the top
it just says seed phrase and then
underneath it is just like an empty text
box and then a button that says submit
nothing no styling it wasn't pink it
didn't have the logo I was like how can
I lose possibly to these people they're
doing literally the least amount of work
I've ever seen um so that's why we're
here then also we have a lot of
dependency issues so we've seen a bunch
of supply chain attacks uh this one
recently and then obviously we had ler
connect we have some things with mpm
like you can't get audit logs um but
this is something that we don't see in
web too like when was the last time you
saw Robin Hood serve malware on their
front
page uh also I'm not going to go into
smart contracts there is lots of
attention there's lots of audits uh it's
outside the scope really of this talk um
and in Old security terms this is a
layer a talk I'm also really good at
graphic design as you can see I've
modified this slightly so that you can
follow what's going to happen okay so
we'll start with daps daps are basically
like the pivotal point between your
users and their wallets right and the
providers and the underlying crypto and
daps have a responsibility to users
which I find that often they you know
don't do effectively um but users are
putting their life savings into your app
and effectively you want your app to be
popular so you're expecting a lot of
users a lot of funds going to be in it
it is really important that you know you
look after that uh then also obviously
as your app gets more um popular you're
going to get more attention from
attackers like
dprk so the idea is that we're here to
help users right if you're building a
Dap you're there to help users for
starters web 2 before web 3 like you
don't have we don't have to speedrun
every web 2 security problem uh just cuz
we're in web 3 right and should be that
we help users make safer choices that
are easier for them and that they want
to make right so don't tell users like
hey every time you want to sign a
transaction go to the roof uh make sure
you've got those things that vibrate the
windows but it's ridiculous no one will
do it um in terms of things that are
effective Ubbi keys and P keys are super
nice people kind of understand them and
they provide like fishing resistant um
you know integration which is which is
really nice uh then also it's not just
external facing so a lot of daps you
know will will care a little bit about
the users but we don't see it internally
like if you a few Engineers please just
use a manager uh and UB keys or pass
Keys anything that's web bothin uh
you'll cut out like 80% of the of the
things that we soed right if you have
money for it get an udit of your front
of your uh front end of your interfaces
so we'll see companies or daps that have
like you know eight audits of the smart
contracts audits of the front end that
integrates with the smart contract that
if anything happens will just point to a
different smart contract uh so it's
really important to do that if you don't
have money you can follow this great
thing that uh seal is put out H that's
at Frameworks that QR code goes that
um but then the the one thing that I see
a lot of is that logging rarely counts
so I go to a lot of incidents because I
love drama um so I like to see what's
happening in there well get an incident
someone will be like okay well uh this
terrible thing has happened I'll be like
okay let's figure this out what happened
with the pipelines you know how do
people log in and you'll find out like
they don't have any logging and because
time only goes one way uh you can't turn
logging on afterwards so definitely
please turn on your logging um basic
scanning stuff is free you can scan for
secrets you can scan for dependencies um
and you can scan for uh you know your
code as well all these tools are free
they'll integrate with your GitHub
they'll integrate with however you uh
deploy uh then also like having a good
uh I guess security culture there's
something that someone in our company
says all engineering is security
engineering right doesn't matter what
someone is doing if they're building
something for the dab is running down so
we're going to start doing this
otherwise he's going to be verys said
that I've taken all this time securi and
arms race you can break into any time of
money there's nothing that's unhackable
right um effort because it's very
embarrassing to me to lose to register
domains or deploy stuff so we need to
demand that providers actually do
something about this right but it is
quite difficult because one being
registered at some regist then they lose
the money from that registration there
is one time of year that you're allowed
to make demands that might get actioned
um and that's during renewal season so
right when you're about to pay them if
you work at a company thing how are you
protecting our users so you do have the
options
there uh then as part of seal I help out
with the uh metamask block list it's
basically like we try and autoing
scamming sites and just putting them in
the block list ahead of time uh so we
have 226,000 entries uh block domains in
there right now there's about 173 that
still have who is or adap data and about
browse to them um I started trying to do
that self it's very quick to uh get rate
limited and all sorts of bad things
happen I once uh got our entire
apartment uh blocked from the internet
and I can tell you that my girlfriend
was very upset um luckily someone linked
me with uh who is XML and they did this
all for free which was super cool so
once I got the data I wrote some code to
do the data I mean obviously Claude
wrote some code and I ran it job
security uh and this is the data of all
the providers that we have
scam domains go through cloudly right
and someone was like well maybe cloudly
does most of the internet but actually
in their uh Q3 the internet but so
that's pretty disappointing uh they also
do 10% of the M then also there's a
slide that has statistics so I got to
use this template 68.2 and then I said
this is too much that's a quote for me
you can use that uh regist draws are
kind of the same I'm going to try speed
up a little bit so we get into it
Twitter expect that your account is
going to get taken away from you
unfortunately that's the State of
Affairs now you don't have options uh
because you know you're relying on a
third party provider uh but obviously do
follow the guidelines so it's not trally
easy for someone to do that AT&amp;T Verizon
like we get up still happen this is
crazy right uh the government forced
them to say like hey I I don't want my
account Sim swapped and basically
they'll go okay cool uh and that's it
they'll add a note says head it as a
note into your account and then when
someone is doing a Sim swap they should
go and ask you know what is that
password what is that account number
obviously that is no security whatsoever
if someone's getting paid like minimum
wage to be yelled at by people who hate
AT&amp;T and you go and offer them their
entire yearly salary they will
definitely do that right it would be an
insane choice not to uh if you are
worried about it I'd like to switch to
Google F and the Google account you can
protect with Hardware uh tokens make
sure it's safe okay okay wallets this is
my favorite part so wallets obviously
evolving rapidly and I'm mostly going to
be talking about extension wallets and
other things going on so make it easy to
address the underlying complexity of
crypto give away all your money the
wallet will be like great that's we're
having a great time let's give it all
way um so I was thinking about it and I
was like well what do wallets really
know and they know a bunch about us
right so wallets know where you are
right now they know like the IP address
you know they know your time zone things
like that they know where you're
connected to
now cuz you just click connect and they
know where you connect to before because
you click connect then they still know
that right they also know who youve sent
funds to so okay there is an asteris
there for the ec20 thing but if the
wallet is in the browser it knows that
you send funds to someone because you
clicked on the buttons you put in the
address uh everything like that um and
then they also know like usually what do
you do like after 5:00 p.m.
you go to
Pumped on fun and wreck yourself on
memes so the first one that I have that
really is bothering to me is these
lookalike addresses so lookalike
addresses are when the first you know
three or four five or whatever uh of the
address are the same and the last are
the same as the legitimate address so if
you set up so that when you go to send
again you accidentally click on those
ones and you get it but if you use one a
modern wallet it'll just say hey this is
a new account you sure you want to send
here um and actually you see that
dialogue a lot because everything you do
you're generally sending to you know new
addresses and things but actually the
odds of you hitting um a wallet that
you're intending to send to that has the
same four and last four is crazy it's
like one in 18 quadrillion I promise you
if you hit those odds I will buy you a
hat right I not that much uh not that
much money I want to spend on this but I
will buy you a hat um so why don't
Wallace just block it there's almost no
reason for you to to get into that
situation know the domain that you're
connected to they're in the browser they
have all the context of it so if you go
to like unich train.org and later on you
go to unichain dotop what is in the
wallet say
Hey you know basically like look at this
we can look at Levenstein distance to
say like okay how how close are they uh
we can have a list of known good we can
use an SSD Pat to say well the site we
originally went to and this one look
very similar so that seems quite
suspicious even the the age of the
domains surely should protect our users
better you can just block
stuff uh then wallets also expect users
to be Crypton native right I don't know
how anyone is expected to do this but if
anyone checks the call that it's equiv
approval flow my mom is never going to
understand this no matter how many times
I try to explain it to her um and if you
love your mom I love my mom and it would
drain all of her funds right wace don't
have the ability to go into a safe mode
where I can say okay here is a list of
all the domains I think that are fine
you know you can interact with those
anything else just don't interact with
it uh because really I'm okay with my
mom losing all her funds to mudang
coins but I'm not okay with her getting
drained because then she's going to be
like Andrew what doing security and I'm
going to be like well nothing I'm sorry
I'm a disappointment etc etc um so also
wallet don't warn users when unexpected
things happen like if you are uh if you
if you do drain someone you have to make
the wallet suddenly notices that hey
like all of your usdc just Yeet it out
of your wallet why doesn't it say like
well uh we didn't do that is that
something that you were expecting or
even better why doesn't it just move it
to a new wallet if I seed
phases uh this is terrible for me
because we suck at remembering passwords
that's why we password managers and
trying to get rid of passwords and then
we also sucker keeping things safe right
I definitely do I can't find most of my
things uh seed phrases are the you know
joining of two things we're really bad
at so we should just stop doing this
it's really difficult to manage it's
difficult to handle there are better
ways that we can secure these so there
are some Alternatives and look I put in
a slide from the company um we do this
we run an eded wallet so that's where
people can like sign in with like
different authentication methods things
they know they can use like Google or
they can use par keys in that way you
don't have to have a seed phrase that's
moving around the other one I really
like is the Unis swap extension um so if
you've loaded up the extension and you
have the mobile wallet you can scan the
QR code in the extension it will then
then you'll put in the code and it will
transfer the seed phrase right you
didn't have to copy it it wasn't in
memory at some stage like there's a lot
of good uh Alternatives
there okay so then the improvements that
I really like to see webo and py I'm
like a webo maxi if you don't agree with
me find me afterwards I will convince
you anytime you want uh allow listing or
what I like to call Mom mode like why
could I put the wallet in a safe mode
that says you can only interact with
stuff that is
pre-approved uh if you're a high net
worth
individual all the time we'll say things
like wow this person had a million
dollars in their wallet what a crazy
idea but if you are a high Networth
individual why doesn't the wallet say
okay well if you're going to interact
with a site I don't know I'm just going
to create you a new wallet let you
interact with the site and then I don't
have to risk all the other assets it
seems like things that we could do uh
emergency buttons why don't the wallets
have everything to be revoked I don't
want to have to go to revoke cash and
half the time get scammed because
there's also scamming revoke cash
sites um then also we should rethink the
approval flows like I think that ux
people Rock they're super good at
figuring out like how can we explain
something to a user how can we make them
feel comfortable we should let them
handle that uh and then of course clear
signing like I don't want to look at
called that's it's too difficult for
anyone reasonably to use the wallet uh
to understand and say like it's much
better if we have a a description of it
make this time the last thing that we'll
say is security folks need empathy um so
there's a lot of real people getting
scammed many times you'll see people
like just punching down being like wow
you suck you know you got scammed by
this they will feel less likely to
report it right they're already in a bad
place you don't need to do this um then
sometimes I'll see things like this
where someone's like you know what's sad
is someone uh sold their house for some
scam and then someone says well you know
what's more sad than that is that I won
the project I promise you it's not more
sad that you warned the project and they
did nothing than someone who lost their
house um security folks should dog food
so if you give out security advice you
should take it yourself right A lot of
people I see like giving out very
difficult to follow they saying like hey
I want a different email and telephone
number for every account that I have try
to do that it's pretty difficult to do
it's not easy to manage and as soon as
you run into those you can't use the
Devcon app it does not work in lockdown
mode um do you have 52 enabled on your
web orn like are you putting in a pin
every time you want to sign do you
authenticate before signing every
transaction so I think that you know
using these really like gives us a good
idea of like what is good and workable
because we will use
it then the last one security fol should
support so if you see good security work
say something be like hey that's awesome
we really like that you're doing that
that's a cool thing so you can find me
and tell me about your cool security
things any time you want I'm good with
that uh security people should share
their knowledge I find a lot of people
are like very nervous to share their
knowledge but is that you can like then
extend further uh and then lastly you
can submit a bug without getting paid a
million dollar Andre Mom that's me
thanks come come come let's get a selfie
together my God you know I very rarely
see a mohawk how many of you see a
mohawk these days my god let's um
because our speaker he had so much
content he decided to use his Q&amp;A time
to teach you guys a little bit more
about security but I think all of us
enjoyed it let's give him one more big
big round of applause and really really
scariest things I've seen in web 3 and
you might have seen this is when people
copy an address a crypto wallet address
but when they paste it to click Send the
address changes because there's actually
a malware that has infected the device
and it changes the address as you click
Send because some of us we don't really
check every address that we send to
right and so one of the thing be hiding
in your computer and your antivirus
doesn't see it your malware scan doesn't
see it but it could be changing your
address without without your knowledge
and I've seen it happen live I've seen
it happen so it really is now in terms
of security today's talks the rest of
the talks for the rest of the evening
are all going to be about security so if
you're interested in security stay here
those of them who are leaving they want
to get hacked right I'm just kidding I'm
just kidding I'm just kidding of course
I'm just kidding but please please do
stay let me tell you why I came from a
background where I saw people losing
money every day not just thousand six
Bitcoins I saw it in a it he's right the
speaker you know to onboard people right
we all want to onboard the next 100
million users uh but we forget that like
he said all engineering has to looks
nice nice uiux but when it comes to
security I think he highlighted some
really good tips that I hope any
developers here will employ now our next
topic let me talk a little bit about our
next topic ah yes our next topic is very
interesting it's going to be about a
little bit more about web 2 now many of
us in the space we know that web 3 yes
there's a lot of vulnerabilities we need
to settle but also importantly is the
web to front end how many of you have
seen a front end get hacked so many time
interact but if you're not if you're not
following you you wouldn't know right
and so Web Two security is equally as
important because web 3 we rely a lot on
web to as well right so our next speaker
and our next topic is going to be about
from web to security with love and our
speaker is going to be giving you an
insight into solving some of the
challenges especially if you still in
the hall can I just remind you later
when the speak speaker is speaking
you'll see a QR code right it's going to
be there the whole whole session and
please scan the QR so see an option
called collect card and last but not the
least speaker feedback right can you
please do all three so first of course
you join the Q&amp;A you submit your
questions and then you click collect
card it's like a little po app a little
NFD token to make sure that you remember
that you joined this event and very
importantly give the speakers some
feedback speakers can only improve if
you give us feedback right that's the
way that we want to improve by
supporting each other together all right
we're almost about ready to begin but I
just want again try my very very best to
welcome those of you who are sitting at
the back and coming in front we'd really
appreciate it I can tell you from a
speaker's perspective when we see the
front row full of people we we feel a
lot more happy and energetic but I know
of course some of you prefer and more
comfortable sitting at the back again
that's fine most importantly stay
engaged by asking questions that's the
best way that you can get the most value
out of these topics and one of the ways
that I protect my mother for example
from Hecks and scams is that I refuse to
install for her any banking applications
on her phone I refuse because she's
always on Facebook and she's always
clicking on scam links and then only
after she's clicked it she's asked me
Ross is this a scam I'm like yes please
stop clicking on it so whenever she
needs me to send her send money I'm the
one is very very scary especially for
older generations and if we really want
to make web 3 and web 2 inclusive we
have to be very careful with how we do
it now let me just check with the team
if the speakers ready for our next
session we're about ready we're about
ready yes I thumbs up all right we still
have a little bit of time so we're going
to give you guys some time to settle in
and you can actually staring your
questions right now right now right now
so if you want to ask now go to your
Devcon passport app click on the session
from web to security with love scroll to
the bottom click join Q&amp;A and then you
can join and you can ask your questions
it's actually it's a lot better if you
ask them in advance so that they'll be
on the screen and then we need you to up
vote so if you see a really good
question vote it vote it vote it and the
more votes that we get well then the
easier it will be for us to choose the
most popular questions I see some people
coming in from the back if you're just
joining us for the security talk please
come and have a seat in the front we'd
love to have you in the front with us
security again is my passion and I'm
really excited about it it's something
that's very important and something that
we should all take over right we should
all take ownership rather not take over
and when we sit down and uh we don't
realize we're not aware of our
surroundings and I just did this with
the person's who sat next to me Mario
I'm going to sorry Mario I'm going to
put you on the spot a little bit but uh
often times when you sit down and you're
using your phone some of us when we
unlock our phone with a pin number we
just type it in right and we don't
realize that people can be looking at
the left and looking at the right and a
true story I've seen this happen before
someone has stolen that phone and
they've just been watching over your
shoulder and they already have your PIN
number or in this case I saw his
Telegram and I add him on Telegram and
sent him a message said hello and he
didn't even realize he was looking like
how did you find you know I mean it can
happen right I just did an experiment
just just for the sake of case study
example so please be careful right these
are the small adjustments that we can
make in our life to make sure that we
keep ourselves safe all right now our
next speaker is very interesting he is a
threat intelligence Analyst at Mandan
now part of Google Cloud where he leads
effort to identify and track threat
actors using cryptocurrency and other
web three Tech forensics incident
response and intelligent analysis wow
this guy really knows what he's talking
about and again the sessions today
onwards all the way until 6:30 we're
going to be talking about security
security security and one of my favorite
sessions actually hacker groups in the
world I actually personally met someone
from my company previously who stands
warmly together and welcome Joe Robson
you have someone that infiltrated having
them infiltrate your
company so I'm I'm Joe Dobson and first
I want to thank Andrew if you saw the
the funny speaking guy with the uh the
Mohawk in the last talk he mentioned
that he doesn't want web 3 to repeat the
mistakes of web 2 he doesn't we
shouldn't have to speedrun I am Joe
Dobson you can call me dos and I've got
over 15 years of experience in cyber
security which is kind of crazy I didn't
have any gray in my beard when I started
in this industry but I'm pretty sure if
you just do it for a year you'll still
have gray and my job is threat
intelligence I track bad guys and that
means the infrastructure the malware
what they're doing day-to-day that is my
goal that's that's my role and
previously I did digital forensics
focused on uh extracting data from hard
drives thumb drives at an instant
response I've worked for a couple
startups I actually worked for mandant
twice now I'm at Google because Google
acquired
mandant now in traditional cyber
security there's a terrible thing called
fud fear uncertainty and doubt right one
is trying to sell you something and
they're doing it by saying oh the sky
falling if you have to run out you have
to buy something right now to solve all
the problems and that's not what I'm
here to do is to spread fud because the
security situation you heard Andrew it
should be and the solution isn't to run
out and buy things the solution is to
innovate we need to innovate our way
through the problems that we have in web
where we are in web 3 there is no web 3
without web 2 in 2024 that's just how it
is and you know what does that mean
that's going to be web to your social
media right if you're interacting with
your users on Twitter on telegram that's
going to be web too think about your
development pipeline right how are you
writing code your cic CD if you're using
AI models to enrich the code that you're
writing probably doing it all through
web too too and that all has an impact
because that's an attack surface is what
it is and thread actors are looking for
ways to infiltrate and attack that
surface this also means that web 3
security is about a lot more than just
smart contracts that's not to say that
smart contract security isn't important
I think the community has done a
fantastic job of focusing on that and
and and you know refining that but web 2
has made a lot of mistake three hard
truths about the what's going on in web
and then we're going to talk about
principles from web 2 that can be
applied to web 3 and make it a better
safer
ecosystem so first hard truth is
everyone is a Target in crypto if you're
developer if you're someone that's going
on pump that also means that you're the
front line of defense and we're going to
talk about that a little bit more later
but you have to first understand that
you are a
Target the second hard truth is that
you're out
um cyber conflict is asymmetric you have
nation states with what seems like
endless amounts of resources and they've
targeted
individuals how do you defend against
that how do you expect a user to defend
against that uh it takes about 35
seconds from the time that a a wallet
gets its first deposit 35 seconds until
it gets aird dropped a malicious token
that means Crypton noobs are getting
airdrop tokens before they know what a
token
is is it fair to to expect those same
noobs not to fall for the
fish that is a problem that we have in
web 3 and it's pretty bad um attackers
they're they're clever they're well
resourced you know there's a because
required to it's their job pack billions
of dollars have been siphoned out of the
ecosystem every time there's an attack
against you know anyone and they lose
funds that hurts everyone that hurts the
entire ecosystem social media accounts
are getting hijacked Dows have been
hacked right front ends get hacked and
you know bugs and vulnerabilities
they're going to be found the the ENT
attackers they have the element of
surprise so the other day uh Hudson
Jameson was giving a it was at like 4:00
so you have a crew that is jet lag the
middle of the night and that's when the
attack happens it's you have to be
prepared because it's it's like a car
accident right if you say that's that's
ridiculous and so it's the same thing in
security you have to be intentional
about security and to be intentional
about security there's a few key
principles that I think are really
important one of those is and this comes
from web 2 web 2 security has been here
before it's assume compromise you have
to expect that you're going to get
compromised you're going to get hacked
think about what that means for your key
management if you assume bad guys are
going to get a hold of your keys how
does that change how you're managing
your keys what what they can do be
prepared so that when you are
compromised you can actually do
something about it is your code supply
chain Bulletproof the SIM card in your
phone that you know you don't want to
get SIM
swapped all these things you cannot
expect not to get hacked right zero days
happen bad guys at some point they're
likely to get in and at this point you
might be asking well if I'm just going
to get wrecked anyway then what's what's
the point right why bother
well that's because it isn't just about
stopping hacks it's also about
minimizing the severity and the impact
of those
hacks one way to do that is through
defense and depth defense inth was first
deployed or applied to information
security by the the NSA in America
and what it does it means layered
defenses and layered defenses can be
applied to to ethereum especially but it
can be applied to uh to
cryptocurrency so here's some very
simple examples of Defense in depth and
practice and and really what it comes
down to is just having a well-planned
defensive posture right so let's say you
you work for a centralized crypto
exchange well your your customer
customer support they should be on a
separate Network segment than your you
know your actual operations folks uh
maybe you set up a trigger so that if uh
X percentage of the funds are moved out
at once then it it enacts a cool down
period and these are simple things but
if if more dexes and centralized
exchanges and bridges did these kinds of
things then we wouldn't see as much
theft as we do but you have to assume
that there's going to be a compromise
you have to expect at some point someone
is going to get access to those keys or
they're going to be able to sign the
transactions if you're a freelancer
developer right isolate your social
media ACC
put it in a VM make it a separate device
something throw a wallet on there that's
got a few bucks in it so if an
unsophisticated ATT attacker if they get
in there then they're not going to you
know you'll know it right because you'll
see the funds move but they're not going
to get access to anything more than your
social
media another thing is to have an
instant response plan right don't make
it easy on the attackers and that's what
so many organizations do I can't tell
you how many compromises we've seen from
web 3 organizations
and they they don't have logs their logs
don't exist right they people in web3
hate EDR in point uh detection and
response tools and so there there's no
centralized logging on the devices
they'll have something in their AWS
instance or gcp in the cloud somewhere
they'll have some logging there but a
lot of the compromises don't come from
the cloud they come attackers getting
access to the devices of the developers
the the people working on the project
you want to have a plan that helps
Defenders and costs attackers with
proper tooling you get earlier detection
earlier detection means you can actually
get the word out about the attack you
can share that information to the rest
of the community again it comes down to
how how do you make the ecosystem better
and early identification of the attacks
how those attacks are happening that
that would help significant
significantly you know unlocked homes
are easier to Rob so lock said I want to
talk a little bit about something called
attribut
right I know what you're thinking all
right but dos I I need to you know that
that's the mindset but really
attribution matters and when I say
attribution it's understanding who is
attacking you a deep dive in attribution
is for some future talk at some point
but protecting users and organizations
means we need to understand who's
attacking us script kitties cyber
criminals nation states who is it what
kind of resources do they have and fin
Financial theft that is just one
motivation that we've seen when it comes
to compromises in web
more excuse me stored on
chain that's using web 3 that impacts
everyone uh Commander control there's
been uh drainers like Angel drainer that
will actually use uh C2 those these
smart and storing information like that
that can't be taken down so that's you
know there's nation states out there
that are posting misinformation and
storing it somewhere like ipfs these are
different ways that web 3 Technologies
are being abused and understanding how
that's happening can help us understand
what we can do to mitigate attacks to uh
to identify and track the bad guys so
that we can protect the users and
protect the
ecosystem so on this slide I have a
is a North Korean threat group this
image comes from a uh a mandant Blog and
the reason why I have this here is so
that you can see that that's one threat
group using all all those different
families of
malware it's important to understand
attribution because then we can identify
who's using the malware how are they
using the malware when did they develop
of the malware how many people do they
have on their teams that are doing this
type of activity how sophisticated are
they with their malware what where does
it Beacon to what's the infrastructure
look like can you identify it offchain
or onchain and these questions also
apply to Smart contracts and onchain
activity when you're looking at
malicious smart contracts who wrote them
where were they first published were
they on a test net first or were they on
you know published in the main net does
it have code segment or portions of the
code that were used in other malicious
attacks before all these different
things can feed into attribution and and
help you understand who is the attacker
how did they get here and what are they
doing it comes down to the who what when
where why and
how and then there's dwell time right
dwell time is the time between
compromise and detection so if a bad guy
gets into a network
and they're there for a week two weeks
then the the uh the victim may not know
it and this comes down to detection
the earlier that they're detected the
less dwell time that they have the less
time they have to to actually deploy
their attacks um and ask yourself how
can the ecosystem prevent attacks uh
this is also a quote from uh mandant
mtr's report and it mentions that in
and 2022 16 days interesting statistic
if you ask
me but all that being said there there's
hope right again this is not Doom and
Gloom I'm not here to tell you the sky
is falling you need to to to to ditch
web 3 it's not the
case you don't have to go to loan the
industry is decentralized and so is
crypto security right you all are the
front line of defense remember it's
because everyone is a target that also
means that everyone is getting access to
the information of attacks share it out
let folks know there you can do it
through something like an ISAC there's
the seal ISAC there's a crypto ISAC you
can also you know there's tons of posts
on Twitter telegram areas where people
can go out and they can of what they're
experiencing and what they're seeing
because trusted sharing that is critical
to the health of the
ecosystem and think about the future
right the people in this room you're
building world changing technology all
right you don't have to accept security
the way that it's always been think
about how you want to change it what
should it look like what
responsibilities should or shouldn't
fall to the users what what information
should or shouldn't be out there and you
know you don't have to repeat the
mistakes of web 2 security web 3 is
Young it's Innovative that's the thing
that has astonished me going to Devcon
at other conferences is just how much
Innovation there is but you have to be
intentional about security you have to
think about it you have to actually
account for it from the get-go and web 3
security can also look a lot different
than web 2 security think about dows
dows they they should be investing in
security when it comes to developers
they should consider what are the the
different security practices that
developers should have but I really
encourage you to be Innovative consider
building something to support or enhance
thank you very much let's give him a
warm Round of Applause very very
inspiring as well um I think a wonderful
followup as well from our previous
session to this session they compliment
each other perfect remember as well that
if you want to you must scan the code
because there's a secret embedded in the
code yeah very secure M all right so
let's address our first question right
at the top we've got two votes right up
there um okay what is the biggest web to
Gap you see in terms of security amongst
web three products great question uh I
would say it's lack of preparation that
that's the biggest Gap lack of
preparation lack of preparation
preparation they expect to never get
compromised and so they don't set up
logging they they don't have an instant
response plan so when something bad does
happen they may not have a way to
contact their other Developers it may be
that they only talk to their developers
over telegram or signal and then that
get gets compromised and guess what you
you don't have a back Channel exactly I
think it's surprising when you said that
teams don't have logs that seems
unbelievable to me how can you not log
things these days it's awful awful and
and when I say logs I I also mean logs
on endpoint devices right so what
machine is a developer using to write
their code cuz so many projects they'll
they'll Outsource they'll hire someone
to do code development and then that
person is just shipping out the code
they get compromised there's no logs
from that developer box exactly I think
a great tip I believe all the developers
here have logs
right okay silence means they don't have
logs and they're going to have it now so
tonight let's go to the next question we
got four votes up there flip the
question a little bit what can web2
security learn from web 3 that's
interesting that's a that's a good
question it's a it's a tough one too
because I'd say that web 3 security
still sorry Jo could you hold the mic
yeah that's fine thank you I think web 3
security is still pretty young and
figuring out what it wants to look more
rivalry I think in web 2 than there is
in web 3 and I think the collabor that's
a wonderful learning point as well let's
look at the next question what do you as
front end for web 3
DMS I'm not I'm not touching that
question okay spicy question I'll the
stage let's go up again uh DIY Services
Consultants how much of security should
I do myself versus Outsource I love this
question this is great I I think that's
really up to the team but I I'll say
this much y if you're Outsourcing
anything I encourage you to do some
research on North Korean IT workers best
will they have been at infiltrating
companies because they're they're going
out there and they're freelance jobs
they'll go out there they get the job
they'll do a little bit of work but they
can also put in back doors they can
enable uh attacks right and North Korea
is a sanctioned country and it impacts
again it impacts everyone when they come
in and they're able you got to do your
due diligence on who you Outsource to
again let's go up to the top we got we
got still got time for some questions
let's do it uh how many attacks have
youve traced that was
State you got the they're in crypto they
doing they are right you would expect
you would expect crazy crazy it is a
crazy time to be alive all right how to
do asset inventory of web three assets I
don't have a good answer for that one
okay no worries not not my area I'm
sorry not your area that's fine what do
you think is one thing security posture
that's the solution I I understand the
question right if if a lot of folks you
know if you're not it's looking at the
content in your devices it's trying to
find something malicious and a lot of
folks don't like that idea because
they've got keys on their devices
they've got crypto their their device
might be dual you and I understand that
but with what's something else that they
could do Hardware wallets Hardware
wallets yeah yeah I mean it's it's an
old answer but y tried and true no I
I've sat next to a friend of mine and
his hot wall just got drained right next
to me and he's asking me for help cuz I
I come from a security background and I
what can I do it's not a hardware wallet
I can't do anything there's no backis in
crypto exactly right so that is
definitely some things to take note of
um let's see um they're really small
they don't have the money they don't
have the resources to do Audits and
stuff like that what what would you
advise them to do H sorry your
microphone just a little bit perfect
thank you with small teams often times
they don't even have a full-time it
person let alone having a full-time
security person so I would encourage you
talk to the folks like seal right um ma
is going to be up here talking here
shortly about seal security framework go
through that look at that that will get
aware communicate get on Twitter and it
amazes me that it's 2024 we're still
talking about how Twitter plays such a
incredible role in security but it does
and having that collaboration keeps you
up at night regarding the state of web
three we true security adapting FAS you
know you're people that are losing their
retirement funds they're they're lo you
know college kids that have invested all
their Savings in crypto and then it gets
wiped out because they don't know any
better really comes back to should the
burden be on the user or should the
burden be on the um the organizations
the Dows and wallets hand no spicy I
think I think I know what that is all
right answer I I love things like uh
like wreck news but I wish wck news
didn't have to exist right right right
of course yeah um let's do a few more we
got 30 seconds on the clock what's the
highest impact thing a user can do to
improve their personal security great
question I I think yeah uh the next
question is about dprk I believe that's
North Korean ttps ttps I'm not so
familiar yep dprk is uh that's North
Korea ttps that's t uh
T and and isacs yes like seal ISAC
ladies and gentlemen that comes to the
end of our Q&amp;A for security let's give
Joe a big big round of applause thank
you Joe the spicy too you know um and so
we're going to get ready for our next
session very very shortly don't go
anywhere stay in this Hall as you can
see the topics are really really
important right but security personal
security your computer security your
Hardware wallets I've seen people
drained right next to me my friend was
sitting next to me one day I think it
was a a Wi-Fi he connected to a public
wife but I managed to get a friend who
works with Arkham intelligence and we
actually tagged the wallet and we found
it actually ended up in a crypto
exchange and I gave him some some tips
about how to contact but these are the
things that we need to try and avoid as
much as we can we have a response to it
but the best prevention is cure excuse
me the best cure is preven oh no
prevention is better than cure you can
our next topic is security Frameworks by
Seal now seal very very a buzzword that
it will hear in security very important
for all of us to know um I'll just give
a quick as well to get you interested
comprised of dedicated security
Specialists seal aims to spread
awareness and educate the community
about web three security best practices
and pitfalls now again like I mentioned
a few of you have just come gets hacked
it's just a matter of when have I gotten
hacked before let me think I almost got
hacked once I almost accidentally
clicked on an NFD thingy and I almost
had my wallet drained but I I thank God
I had like Rabbi wallet if you use rabby
it gave me a notification like are you
sure and I looked at it I was like wait
a minute that doesn't look right and
thank God you know I was like oh my God
he uh refers to himself as a techno
hippie a security Nomad and the
co-founder and member at
the red Guild right and also very very
much so a proud seal member so when he
talks he knows what he's talking about I
think we don't have to uh spend any more
time let's H let's give him a big round
of
applause
yeah yeah I'm right here what up oh hey
you are oh hey man oh didn't know didn't
realize you were busy oh no worries how
you doing who are you good to see you
yeah pretty good pretty good pretty good
thank you um do you mind if I Twitter
accounts for war three
orgs um I think you mean the post that
Sam put up on Twitter a little while ago
I'm sorry Sam who Sam Sam C son you know
the guy who saved ethereum's ass like oh
I think I know that guy the guy with the
Anime Avatar on his SW
and I think I remember that post but no
clue where to find it yeah I'm just came
here it's a pain let me let me see if I
can dig it up for you
um yeah I don't know it's like all these
telegram group chats trying to find
information it's just so hot these days
um you know what now that you mentioned
telegram I think someone sent it to me
but I have to really it's going to be
really hard to find it there yeah wait
what did you need the Dr here uh yeah I
didn't realize you WR
um you remember that upset guide that
you mentioned yesterday did the one with
all these um Sim
protections and seam swapping
protections and fishing prevention
techniques do that ring a
bell I think you you're not mentioning
the officer C recollection ofice and
posts and you're not not talking about
the insights from the book How to
Disappear no no that's not something
super detailed like a stepbystep guide
giving you detailed instructions on how
to deal I was one of us um I was one of
us a little while ago wait I wrote
something that's on our our internal
notion which is like a transcription
from something I did when in
AI wait was it one or many guides
because also privacy has like a ton I
think it was one actual
guide wait Pascal Pascal shared one on
Twitter that's the one thank you thank
you thank you let me go back to his
Twitter page I'm G to have to scroll
over hundreds of tweets to find it but
we'll get there thank you thank I would
have find it without you do you have a
minute now that you're here would you be
so kind to share me some best practices
for developers oh dude there's like let
let me see if I can find that
didn't realize there were so many yeah
so tons these days man it's pretty crazy
yeah see wow
I was thinking I can't find it now no no
worries but if only there was a more
organized structural place where we can
all go and and see all this stuff you
know and you know what people say people
say that the security issues are not
because of lack of information but
rather because of ignorance that makes
sense that makes complete sense you mean
something like maybe a community owned
wey of Sal so we can all contribute and
point our um lovely users towards yeah
man I mean I'm tired of scraping the
entire internet looking through my
bookmarks and when I'm thinking about
this centralized thinging I'm not
thinking about notion or Kota or Cham so
please not I'm thinking of something
else yeah man that makes sense um yeah
it it it's crazy I spent so much time
all you know what I was also thinking
that even if the information is out
there but it lacks Readiness it's
outdated and you have to look for it
everywhere it's I mean what you going to
do right yeah well maybe we can help
maybe we can build that Central
repository single source of Truth when
it comes to security best practices you
mean like a
generic best practices thingy yeah like
security guidelines or security
SEC
Frameworks yeah man I I'll leave you to
it thank you oh didn't realize we were
here how are you so today I'm going to
be talking about the security Frameworks
which are high level best practices and
say in web three so I'm not I'm not
going to since it has already been
presented uh but the only thing I'm
going to say is
that we are working with a lot of
respectful people because I don't know
why they are on a triangle formation
that's some Illuminati right there
it suits them apparently P intended and
also with the SE if we fit into that
someone has to protect us too right so
back to the presentation we do many
things but my name is Mara I work at the
red Gill I am one of the founders the
other founder is there tincho and I'm
also leading the security Frameworks at
s
on the red Guild we work as a nonprofit
organization doing public goods for the
benefit and we're very much aligned with
SE that's where we're working together
so this is going to be like really
really really quick FAS because I don't
want to bore you and I just like talking
more than it's
necessary
so like the book John Dies at the End
instead of pitching something and
leaving the it straight at the beginning
so if you go there latest smallware just
kidding it will it will take you to one
of those links I forgot which one I
think it's the the main one so as you
can see here on the
links both are synced and are
deployments of those two
branches and I'm going to show you some
screenshots so you don't stare at the
phone and look at me or look at the
presentation so here as you can see it's
very basic the current state is like a
Wiki if you use gbook is something
really similar to it to navigate it it
all the Frameworks there of course write
the content and also there's a
disclaimer that reads this is a work in
progress not a release not a release
this is very important we are looking
for about on the on the on that icon it
will take you directly directly to edit
on GitHub and if you are on the doev
domain and you log in with Vel you will
be able to select any part of the
content are like really interested in
some of the Frameworks or the pages that
you have found you can book them
bookmark them so what we did in in on
top of this is we implemented a way to
navigate generic and there's room for
improvement but as you can see here
right next to the magnifying glass you
you see can search there and in this
case I'm showing Community
marketing and of course some of the
Community Management platforms that to
awareness so filtering TXS the TXS that
are outside the screenshots the are the
rest of the TX that have been
implemented recently and on the left I
have another example if you see it reads
security places and procedures
governance risk management compliance
with regulatory requirements metrics KP
kpis so it's right side you have HR and
if you pay attention to that it's mainly
related to onboarding and off
offboarding of employees and and members
of an organization so if you want to
look your bookmarks you just click on
bookmark and and that's it and now I'm
going to show you a a few classic
examples of in this case the category
operation for you to read at your home
with a family sharing a nice meal and
also here this is one of my favorites
say an incident happened and you don't
know how to organize your information
here you can use this template to assess
and act as fast as technical details
this is as you can see this is really
simple we have a an open repository
there it we we are using a set of kbook
mty
book and it Auto deploys with verel you
commit and you see the pr of the
deployment and right now only the dot
Dev is accepting comments so it's
basically markdown files and pure docks
I had to admit it but my mother was
right I did end up studying 15 years
just to write documents but what
what you're going to do so on General
details uh we have a currently Community
cor team I'm really fortunate to be
working with Freddy and medy and I have
them try to put minimum contents on
every page so you don't see some of the
Frameworks empty and so and you can jump
there and criticize what we have wrot
but a lot of work is really needed for
the first release so this is why I put
the disclaimer this is not release and
the next phase is currently right to
collaboration and we hope that making
everything public will inight for the
collaboration so what's the problem that
we want to tackle you seen that security
threat was saying if you paid attention
to H talk and something that's happening
is that
most RS let's say are not only aimed at
decentralized infrastru related to the
information if you remember the sketch
it's like really difficult to keep track
of all the stuff it even happens to us
at the at the guild we both you know how
it is it's like really difficult to keep
track and
it happens and they get updated of your
role in an organization to create best
practices mats and if we can do that
regardless of the specific technology
better what might difficult
process I mean if you come to DSS or
this track you know that the knowledge
is out there you're possibly something
in your head that I don't know and the
other way around so I just need to
understand how to get to each one of you
even proof reading is something that
helps and that's what I'm insisting
so then let's say that we created
something and it's useful we need to
convince people that they should follow
these practices so seeking adoption is
something real we have to make it at
least usable or easy to navigate
otherwise it would be like a painful
experience
so of course of course of course now
that we
create and another stuff that happening
is if you saw we have more generic
approaches but then you sell something
like Google s Discord Telegram and you
are going to say hey but that's like
really close to an implementation yeah
so the thing is that we don't want to go
too abstract in order is that we have to
understand better how
to see where it is needed to go further
deep on the implementation versus on
High level
practices right number I'm going to
drive you crazy about this so you can go
there log in with um with your create a
PR you can create an issue you can
create a discussion hop on on the
previous Rel created ones here I there
are 25 more than 25 so if you don't know
where to start there is even the label
good first collab and there are 15 of
them right now and I will start creating
more after Devon so why should you
collaborate I think that we need to
shift our perspectives stop negating the
human nature and like we're going to
make mistakes so if we use mechan of of
control trying to avoid people
committing mistakes is negating the
human nature right so what we should do
is just accept that we are going to make
mistakes as I said and build more more
important and of course we can do this
alone so since we can do this alone I am
also going to show you this
recent initiative that we're
participating along with secum and theum
Foundation from the red Guild I'm not
going to say much because you can find
anything everything there on E Rangers
but if you have participated in public
goods working in security for the past
year or past months then you may be
eligible for
participated in the past and you are
eligible and don't know what the
you should do we are going to give you
different initiatives where you can
support continuing your work which
because it's like it's really valuable
and of course security Frameworks fits
into one of the initiatives that you can
continue supporting so that's it I thank
you very much all for your time and I
hope you contribute to the security
Frameworks awesome let's give Mata a big
round of
applause can I just say I love his
outfit as well so colorful that's why he
calls himself a techno hippie yeah one
one with the stage one with the
environment and one with the security
now we haven't got any questions yet
maybe because I forgot to remind
everyone to please send in the questions
I know you're really interested by his
presentation of the Frameworks so let's
give everybody just maybe one or two
minutes quickly send in some questions
you can scan the QR code submit some
questions if you want to ask about the
seal Alliance about the security
Frameworks that you briefly mentioned in
fact I was just looking at the the um QR
code that he got on screen I scanned it
and I got it um if if you miss the QR
code it's uh frameworks.
security
alliance.
deev very very interesting
it's a resource a collection of best
practices written in abstract or general
fashion to be applicable regardless of
the specific technology right so it
doesn't matter whether they web through
whether your web 3 everybody can read it
is that right M absolutely everybody can
access completely free online I love the
fact that this is the kind of things
that we collaborate and we build
together speaking of building together I
see you guys building the questions on
the screen so let me look at some of the
questions and let's go right so we can
Target the most popular ones first one
on the top Mata why create oh excuse me
it moved okay they voted for this one
what's the highest impact action a web
three user can take to improve their
security oh it moved away but we'll go
to that one
highest impact that you can take to
improve your security what questions
really hard to to to reply to them so I
I'm going to try to be brief
sure I think this answer has to be more
it's more related to the relationship
everybody has beat war3 or two to the
Technologies I feel like we're using a
lot of technology and we don't
understand it it happens like on even on
household items you have a router you
have a portal computer that which is
capable of doing a lot of stuff and
people don't know like for example on
the iPhone you have a lockdown mode
which protects you for a lot of stuff
you can even disable I don't know a lot
of stuff that may pose you to other
threats
so I'd say that getting awareness and
understanding the technologies that you
use it's a more important stuff because
I've seen people say no you should use
this extension when you interact with
those things can be tricked and have
been tricked in the past and if you only
rely to that kind of Technologies to
protect you what happens when they don't
are you going to get wrecked so I'd say
use and the risk that they pose yeah
it's the most important stuff excellent
very good understanding the Technologies
we use right we use it every day but we
don't always take time to understand it
now three at the top why create a new
framework instead of adding to existing
ones from the web two companies I like
to see those I like to see those and
what happens at least to the ones that I
known things that I have seen from
organizations are like really jealous of
on like getting stunt I'm not saying
it's not valuable so it's like really
hard and for example if I want to
collaborate or others want to
collaborate it's like really difficult
so we we thought of doing something that
everybody could you can in Fork it and
start doing a new one if you think that
our our ways suck so this is an approach
I'm not saying it's the best one this is
an approach we have more ideas to
improve the the interface that will come
later this this year so we wanted to be
more to give the the community more
control over this stuff that it's really
important to us I completely agree it's
not always companies that are willing to
share companies are usually protect
their they don't want you to know their
security practices because otherwise you
might then take advantage right so but
this is collaborative what seal is doing
is to collaborate with everyone to build
a document together okay four votes at
the top Mata do share any memorable
incidents if you don't mind what can you
share something that happened that you
which made me get interested in security
like totally off topic because I mean we
can talk about like dpk or some other
stuff if you wanted I know know who wrot
this if you wanted something more like
that we can talk with
doing let me go back I started playing
online games like in 2000 there was a
very popular Argentinian game called
called arent online arine Arline yeah it
was the M the the first mm o orpg orpg
there so I met a friend there a female
okay nice nice and then we started
exchanging messages and back that the
day we used messenger for 4.0 wow yeah
and old yeah we were chatting and and
she she told me hey you can see this
emoticons not emojis so let me send you
this pack so I accepted the pack and
then my compa di was start the trade was
started open and closing and she said
thanks you thank you for your IP I was
like what the so I got locked off
and all my contacts were erased to
friends online I was like I feel like
violated
my you got hacked from MSN Messenger
yeah from an emoticon pack yeah Park
started wow I'm on my good one right now
now that is you can say I'm working for
two nonprofits I'm not good I'm not I'm
not thank you slip of the tongue there
wow that I've never heard of anyone
getting hacked on MSN of all things but
um thank you for sharing the story I I I
mean that was really memorable uh we got
a uh we got a few more minutes so let's
uh let's uh see the question at top two
simple things to enhance security
security the most so you mentioned
awareness and I think maybe if you want
to add one more thing that you think
would be a practical something practical
that everybody in the room can do well I
can tell you what I do uh for example I
have a Linux machine I have full dis
encryption and I also sometimes paint
the the the screws you paint the screws
with nail polish uh yeah in case I I get
a a made attack your room and then
unscrews your computer and puts a VOR on
it so if you oh I see you'll know if
someone has taken out the screws wow but
if you have full disc encryption it's
like it's okay yeah I mean it it depends
what's your thread model if you're like
a very high profile Target okay you may
be doomed but that is quite extreme what
I do what I do is for example uh I use a
firewall firewall uh in my case I use
open snitch but on Mac you can use
little snitch or Lulu I prefer Lulu
better and I have a virtual machine and
inside the virtual machine I run
containers and every project that I try
to run even the ones that we have
created around each one of them inside a
container because the container even
runs the extensions today's
Workshop there are even
misconfigurations that can leave you but
I think what you pointed out is
important not everyone has to do all of
these things right it's about your
Threat Level if you're dealing with
things which are dangerous then of
course you have to implement I don't
think I'm going to paint the screws on
my my MacBook at home but um but I mean
those are very interesting uh tips I've
not heard that one uh I got this tip
from Greg yeah hi Greg the um we're
using a giet G Net was it g g IET router
it's the it's called a VAR it's really
small yeah so what we do is we take it
for example to this conferences it comes
with a VPN inside y so we create a local
network and we connect all our devices
there even if you're on a plane and you
are only allowed one device it also
works like there like this so I
isolating yourself sharing those are
some very infol your work uh since we
work at two organizations mainly our
organization I mean our organization is
the red Guild you can go to the red.org
the red Guild okay yeah we have created
for Devon especially a
CTF on our platform which is called
direct direct games okay direct games
okay and so you have to play the role of
veran and then you have to help for
example theum Foundation to retrieve
some credit
has pushed and deleted on a file on on a
repository and then we have the fishing
yeah yeah they put you like a video the
fishing test yeah this is this is I I'm
really proud that we came up with this y
so fishing.
direct games.com there you
have for example it starts with an
interface of an email and you have to
understand if
you see some someone or Something Fishy
right and then it changes sceneries like
you sign in a transaction you're
watching ET scan trying to see if you
get spoofed but it's all fake even the
wallet you don't have to leave the the
entire platform it has been thought that
way so it's safe to play and and have
fun and then yeah we have I think like
monthly updates okay kind of like that
and on seal I I'd say join our community
we have a Discord where it's public
there's not much activity right now but
may if you come we can start talking
there and share
much all the way from the seal Alliance
ladies and
gentlemen these are the kinds of people
doing the good work of security and
collaboration to make our space a safer
one now we're going to take a quick very
very short break of 5 minutes as we set
up the stage for our next session we're
going to have two speakers coming up
next I'll just introduce the topic as
well so that you stay interested we've
got a lot of interesting topics and
after this we're going to see Lazarus uh
hacker group information later on that's
really interesting now the topic coming
up soon is deep dive into Fork Choice
compliance for ethereum clients so if
you're interested about ethereum forks
and understanding more about that please
stay tuned and then after that we'll be
hearing some more interesting security
talks as well we're going to take quick
make sure you're here for the next
session all right I'll pass it over to
the stage team thank you
EX
all right welcome back it's 5:00 p.m.
the dot good to see everybody if anyone
is just joining us for the first time
welcome to stage two please come and sit
in front those of you it's always can I
ask you to please the moment you see the
QR code appear here you start scanning
and you submit your questions okay now
you can submit throughout the entire
presentation but the earlier you submit
it is easier for us and please up vote
your most doing for today's session
right now at 5:00 p.m.
guys here are
devs who are interested to learning more
the two speakers are ethereum
researchers themselves C devs and I'm
sure they're going to have a great time
warmly and let's welcome Alex and fans
in the audience yeah hello cents and how
we approached it and to start let's
understand first why F chice compliance
is important uh the F chice rule is the
part of etherum protocol calls that that
decides on the head of the canonical
chain uh that is the chain that is the
chain that you use to confirm your
transactions that is the chain that will
be eventually finalized uh by the
protocol and uh a noncompliant with the
FTR pack implementation can cause uh
different security issues such as
confirming your transaction with the
chain that you local not to say that
this chain is canonical but the chain is
at the observation of the majority and
the network splits uh which can affect
validator voting uh particip validator
voting rate uh real world uh
every every implementation is formally
verified to be compliant with the for
expect this to happen because it is
quite challenging and costly and our
approach to the compliance is to
extensively test every implementation
against the folk Choice spec uh so now a
bit uh about
from the messages that are coming from
the network such as blogs votes and
others uh and the folk Choice rule
algorithm is executed over uh this state
in in the following three steps so at
the first step there is a filtering
function that uh selects blocks that are
candidate for head we call them viable
for head blocks at the Second
Step uh validator votes are used to
compute uh weights of sub trees uh which
contains those uh wable blocks and uh at
the last step uh the algorithm
recursively goes uh down to the found
and that LE block will be the head so
the algorithm doesn't look uh um quite
doesn't look complex it's Rel relatively
simple but uh the complexities here uh
coming from the different place uh there
are many many inter nodes interacting in
the network and they produce many
messages blocks and votes uh that
results in a huge variety of States over
which the folk Choice algorithm is
evaluated and every client
implementation in order to compute this
state fast and uh in order to uh run the
FTR rule so those makes those two things
makes the the FTR compliance incredibly
complicated uh and now over to Alex on
how do we fight those
complexities uh so our goal is to reveal
differences between Fork Choice
specification and implementations and we
need a lot of interesting test scenarios
but generating lots of really
interesting scenarios is a challenging
problem and so to overcome that we
developed a strategy which based on the
following principle differential testing
property based testing modelbased
testing and final ingredient fing and
randomization and okay about
differential proper for Choice spec is
executable so we can compare
implementation Behavior against
specification directly and this is why
differential testing station calculates
the head of canle chain correctly but it
does not mean that so if the check the
head is correct it doesn't mean that
protocol state is correct too and so we
can check additional
properties uh to reveal more buxs using
essentially the same test seed
and uh here is the example of how the
property checks can be really helpful uh
on the left side there is a buggy
implementation that for some reason just
missed one vote cases in case of
implementation and specification is the
Block C so this V this Miss vote Miss
did not affect uh the head computation
uh and if the test case would just uh
compare the head uh and uh the the
client this bug implementation uh
running this test gate
would pass it success comparing the
weight of Block C in this case uh would
help us to reveal bug much easier
because otherwise we would need to
create a test that uh in which run in
which this buy implementation would
would lead us to uh the different uh
block to be the head like for instance
Block B so it's just uh like L test can
can reveal more box that's uh the short
uh uh description of so so uh yeah what
we haven't yet mentioned is that our
compliance uh Tool uh leverages on the
already existing folk Choice testing
framework uh there is the consensus in
the consensus spec there is the fork
Choice testing uh format there are
manually written uh Fork Choice tests
and clients already run them those are
integrated uh and yeah the the clients
already uh check some of the properties
so the differential property based
testing is already is just add one more
property uh which is to check weights of
viable for head but just covering
various execution pass is not enough
because um they through executed on many
nodes and they're
interacting and building blocks using
the rule and so we actually what we want
is to capture this
interactions but we do not uh enumerate
all possible scenarios and so we use
model based
approach um our models basically allows
us to focus on the aspects that are
interesting abstract away from other
stuff and we have three models here FFG
checkpoint three shapes block three
shapes and also filter block three
predicates coverage model and each
models for example we have 10 blocks and
we have Vector for each of these three
shape and if we are able to do that then
we have 100% coverage of our model and
for our three models we currently uh
obtained a thousand of solutions but in
practice it can be arbitrarily larger so
it can be a million models no problem
yeah so to give you like G check points
model uh this model is parameterized by
two main parameters which are uh number
of EPO and number of Super majority
links and here is the example of a
couple of solutions that satisfy uh this
model with uh four EPO and two super
majority links and uh on the on the if
you look at the top uh deok number four
uh in this case will be finalized
according to FFG checkpoint to to to to
the finality Gadget rules and uh in the
SEC in the in the second case which is
on the will be finalized so basically uh
when we do the test generation we asked
the constraint solver to find all
possible uh combinations of Justified
and finaly checkpoints given the um some
certain model inputs and uh with 10 ooks
and four super majority links and so on
and this gives us a lot of uh a lot of
uh solutions to further work with uh in
our
generation okay so now we have uh many
model Solutions and everyone can be
turned in blocks but as a result we can
have the same
shape and and so we use randomization to
instantiate this model Solutions
basically flipping a
coin and uh after we have a test Suite
of test vectors we can additionally do
fing um it's important because our
models actually assume that all events
arve in time which is unrealistically
but we can easily overcome it by
shuffling uh duplication of messages and
dropping some messages and also by
mutating
messages we will also plan to implement
in future coverage guided fing of
implementations and this uh randomized
instantiation and fing allows us to
increase the number of tests in by
orders of
magnitude yeah here is the example of
how the randomization is used um as Alex
mentioned we have these model Solutions
and we use them to uh produce uh like
various test vectors and on the top
there is just a model uh which which
says that basically there is a block
that has two children the client has not
a real test Vector to make it we have to
make it a real blockchain that follows
the and uh we use consensus spec uh uh
for for doing this for making a these
blocks turn into uh making this uh block
dependency to turn it into real blocks
and real votes and in this case the
model does not answer you to many many
questions that the protocol need to you
know to to to create an instance of a
blockchain those questions such as like
uh which validators are voting for which
block every single slot uh where where
is the maybe there is an empty slot
between those blocks uh which is the
total number of validators participating
at Moment In Time whether the message is
like some message is invalid or not and
so forth and for every case for every
possible case here uh to answer such
questions to to decide on such uh things
we flip a coin so we have like a every
every test generator run there is a
combination of model solutions that we
use and a Randomness seed and running
the same combination of model Solutions
with different Randomness seed can yield
a different uh test Vector what matters
here is that this test Vector will be
completely different uh from the FK
Choice point of view so like in this uh
example there are the had TS a different
so but the model is the
same so we have implemented the initial
phase of the strategy and this work was
supported by Grand from from eum
foundation and but from consensus and so
we have a test generator we have a PR in
consensus specs repository we have gener
test Suite which contains about 13,000
of test which I believe is enough for
initial
phase yeah and so we did the as a
prototype we did the integration of this
tool in taku as I mentioned before uh
there there is already the FK choice
test and client was relatively
straightforward we added the new
property check that mentioned before uh
found some issues a couple of them are
related to optimizations I'll cover this
uh on the next slide and we found 4 H
case
uh four edge cases uh where te is not
kind of like compliant to this spec but
these edge cases are very very unlikely
to happen on any any test found those
edge cases uh shows us how powerful this
tool is with only 30 uh 100 100,000
tests or a million test and we're
looking forward to have this tool in to
have this uh suit integrated with other
uh consens layer clients to find issues
in them as well so we have uh test
groups inside test Suites for example
block three focuses on trees of various
shapes and block weight we try to
produce block walk trees where weights
are different distant from each other we
also have a shuffling group and test
group which focus on a test s invalid
messages and combinations of filter B
three predicates and overall we have
about 13,000 of tests right
now Advanced mutation are challenging to
implement for example if we change a
block we need to recate recalculate its
cash
and descendant blocks and attestations
should be recalculated to this uh takes
time so test generation is slow
currently it takes about 10 seconds per
second we have investigated the reasons
for that and okay one reason is that for
Choice Ru is expressed using python
which is an interpreted language and
it's low we but that's not the only
source of the problem because there are
also some slow spec components SL test
generation limits uh the Practical yeah
as I mentioned before there are some
optimizations that uh cause some test
fail uh and those optimizations are that
we have faced with are related to uh dos
protection so some arations some old
attestations that are not going to
affect the uh folk Choice decision are
discarded in TECO for instance and in
other clients as well and different
clients use different heris sixs to
discard such a problem uh is that the uh
the two the the CU cannot be designed to
uh to avoid all those uh failures and uh
diff and because of different clients
has different optimizations in different
her ristics there will be different
subset of tests that are failing and uh
we have like just 13,000 tests but
imagine if you have a million tests and
you have like uh I don't know thousand
of tests failing and you have to ensure
that the client developers
on and as the next step as the next low
step we want to integrate this test stud
into other consens clients here we
engage other client
developer and yeah yeah okay so one of
the most important things to do is to
speed up test generation and okay one
thing that we want to do is to transpile
specification to C or to n rust other
compile to Ang s and of course there a
problem that transpired code there can
be a bu into the translation but uh
since we are translating function to
function it's actually much easier to
test each function individually
individually and another approach uh
another important thing is that to
optimize all components we have already
experimented with faster implementation
so we as a result we
uh that our test should run uh test
should be generated at least 10 times
faster and also an important thing is to
implement coverage guided fast testing
of client implementation and for this
reason we it's critical to have fast
test
Generation Um so if you want to talk
about this topic reaches out description
of the Tes and methodology there is a
uh link to the pr to this spec which
introduces the test generator for this
suit and also there is the pr uh that uh
PR to Teo that integrates the Su into
Teo thank you very much thank you thank
you very much Alex and mik but I didn't
but I'm sure the audience did because
they're asking lots of questions I'm
very honest about it you know uh please
upvote your questions which are most
popular and we're going to look at the
screen and take a run through the
questions right at the top do you run
Fork Choice tests covering non
finalization with multiple Forks who'd
like to take this question I I I love
this question because I before this talk
an hour before this talk I was thinking
about having this test insed because if
you have if you've been at the dep lines
presentation who was presenting on the
non-f finality and how can it kill
ethereum this is very important for
clients to have this kind of testing
suit uh we haven't think thought about
this much but I think it is doable
discuss this um and try to make
something uh and try to make a suit that
would test nonf finality and let client
computer excellent from one one question
can change everything right uh now the
question at the top this test generator
rocks so another round of applause for
creating such a wonderful test
generator again if you want to give
feedback before you go into the Q&amp;A
there's a little box for speaker
feedback please go and write it there so
the speakers can take take a look at
that but well done to both of you let's
go to the next few questions do you plan
to set up a dashboard to show test
results from different CL clients like
Hive who wouldd like to take this um
I'll take this I we don't have such
dashboard for other CL tests we have a
plenty of Cl test that are uh run by
clients and yeah I haven't thought
thought about it we haven't thought
about it so probably not because yeah if
it will be useful we can but maybe not
okay all right let's go straight to the
next one what does it mean for the fork
Choice spec to be executable go ahead
yeah I'll take one okay so um it's
expressed as a python code so it's
basically a number of functions and some
functions prescribe how to react to
events or messages arriving from Network
it's on block on attestation on on a
tester session and some others so three
model is just one of the models uh and
there was just an example so with
randomization and uh we also have have
the FFG checkpoints model that gives the
all all possible uh combinations of
Justified and finalized checkpoints
given the model input so it was in the
presentation as well so we have a model
for that it is also this information
also used by the test generator all
right thank you for answering that I'm
going to mark it as answer separately
very good um I can expand on this we
have actually have three uh possible
cases for this one is that just in pure
onchain attestation the other one is uh
pure Network attestation that the
attestation that is not included in any
Block in any block and it is coming from
the network as well and this is all
decided by the randomization so we flip
a coin and decide which understand the
answer I don't but the audience I can
tell from the audience is nodding and
I'm just nodding along with them uh okay
we got uh one vter okay we got 51
seconds let's do it if the model is
written to test the spec implementation
how do you guarantee the model
correctness because we exe we use it
just to produce interest in test vectors
and yeah we are using spec code to
produce this test Vector um the python
spec and check that everything is okay
very good and I believe I can help you
answer do you execute the python spec do
ladies and Gentlemen let's give our two
speakers a wonderful Round of Applause
to Alex and mik thank you thank you
gentlemen thank you thank you very
much I love the fact that you got so
many long now you don't have to leave by
the way you don't have to leave our next
session is very very interesting it's
going to be talking about the Lazarus
group yeah now among all the hacker
groups in the world Lazarus is one of
the groups that have stolen I think
probably the most money in the
cryptocurrency world whether it's
Bitcoin or other cryptocurrencies a lot
of people believe that the Lazarus group
is a state funded hacker group now
whether that's true or not it's up for
you to decide I hope they don't watch
this live stream but they might be um
but now I'm not a hacker myself but
sometime Sometimes the best way to learn
about these kinds of things is time and
we we do have some minutes so what I'm
going to do is I'm going to give you
guys comfortable and I want you to just
enjoy the next session I had to run to
the toilet just now because we were
really right 5:30
at 5:30 so you got a few minutes if you
want to what you can do is the toilets
are located just outside the hall turn
to the right at the end of the corridor
that's where you find the toilets and I
also want to remind everybody please
sport app but need to scan the QR code
if you want to collect your card as part
of attending the session okay we're
going to give you a few minutes to
settle down those of you coming in from
the back thank you very much it's
wonderful to see you guys learning more
about security and how to defend
yourself we're going to take a very very
short break so don't go anywhere don't
go anywhere we'll be back here 5:30 p.m.
sharp and we're going to have a great
session learning about Lazarus
all right I'm back I hope you guys had a
quick is a very very important topic
something that's close to my heart as
well you know no matter how much you
tell people don't click on a fishing
link don't click on a fishing link don't
click on a fishing link people will
still click on the fishing link and get
scammed now Lazarus group is no
different they use the same attack
vectors all the time and guess what
companies still fall for it people still
fall for it we're only human and we do
make mistakes and that is why this
session is particularly in the crypto
world because Lazarus group has stolen a
lot of money in the crypto industry so
please be very careful and please pay
close attention our next speaker is
going to be sharing about the different
attack vectors they use in Lazarus and
how you can protect against them that's
the most important now again I always
encourage the audience please be engaged
as much as possible by participating in
the Q&amp;A the QR code come on the on the
slides on the screen scan it scroll to
the bottom join the Q&amp;A and start asking
lots and lots of good questions and
don't forget to ask vote the popular
questions so our speaker can address
them now our speaker is a blockchain uh
blockchain hacker and developer he's
very experienced and he's going to be
sharing his knowledge with us let's pay
him our fullest attention please put
your hands together and let's welcome
mudit
Gupta everyone uh thanks for coming um
it's going to be a fun talk uh so we
have slides up uh everything's ready so
so we'll just get started um so first of
all me uh if you don't know me I'm moabs
um I lead security and Engineering at
polygon today I'm going to talk about
Lazarus which is the biggest threat
actor in crypto if you ask me or if you
ask the and by far uh most of the other
large and we'll discuss about that I
have 20 minutes to discuss about 20
hours of content so we'll go a bit
fast uh so
first of all like Whois uh they are a
North Korean hacker group out in 2019
South Korea I mean that's how it starts
in North Korea um but then they realized
they can go Global so they started
attacking Banks and uh other big
companies from 2014 or so the Sony hack
was a big one where they were inside the
Sony systems for over one year Sony
realized oh someone's in here um
then they started focusing on crypto
exchanges in 2017 because they realized
oh these guys have lots of money and no
security so let's do it um but they hit
the defi lottery in 2022 with the 600
million Maxi hack 100 million Horizon
hack um source of revenue for North
Korea which we definitely should be
stopping so let's talk about the top
hacks from these thing uh in all of this
um let's see if you guys they do it just
give the answer it's like every single
hack that uh Lazarus does starts from
fishing or social engineering um so
estimates um and they have the expertise
in all the web to attack vectors uh they
have most of the operators are based in
North Korea but Intel suggests some of
them are in Thailand some in China uh
some in Cambodia and so on so um they
are getting Global
slowly um yes it was fishing all along
like it's a uh it's a bad thing um most
of the fish like fishing attacks as a
category falls under social engineering
um so it it's a big category that you
need to be careful about um I'll go over
really quickly some social engineering
techniques uh that they have uh
Incorporated and just imagine like how
many of those will you fall for so one
very common one right now is they get
hired at your company they'll do the
interview they'll do a great job at it
they'll do all of the homework you give
them and boom they are your employee now
and and uh if you are an employee it's
it's relatively easy to compromise your
company um Zach did some research lately
and he found at least 15 companies in
crypto that were employing North Korean
hackers there might be more that we
don't know about but this is definitely
a big one another big one I've seen
people Falls and this is one uho that
these guys have picked up they would
reach out to you and say hey we are this
big name VC or whatever we invest in you
or want to invest in you and start
chatting up with you now they can attack
you at various stages it can be uh at
the first stage where they say hey uh
join this uh video call and then uh the
video call wouldn't work and they'd say
oh run the script to fix it or let's use
this and job is done but I've also seen
them go through it at later stages and
get to like uh legal paper side and then
do it like we are getting this uh have
um they will act like hey I'm the senior
reporter at FBS or some fake video call
software and things like that uh fake
video call uh job listings this is a big
one this is what the axi fell for um
they would try to hire your employees
they would off and ask you hey come join
us work for us um and they would give
you like either a malicious exercise to
do uh you start writing code you execute
it to say it's working and you're
compromised or they give you malaci PDFs
you execute them and then you're done
for um so there a bunch of these things
like using they can get you and the
reality is like if they actually come
for you it's very hard to defend but
there are some things you can definitely
do and you should everyone thinks like
they won't get fish or they know better
but the reality is like the other side
is getting so Advanced that it's it's
important to keep up to dat just look at
the latest methods they are doing do
some trainings um if you have a security
team ask them to do fishing campaigns to
make sure everyone in your org is safe
um because even if you are are perfect
if the other guy in your or is stupid
you will still get wrecked imagine a
scenario where you're working on a
GitHub repo together uh you're following
all of the best practices but the other
guy guy gets compromised um they end up
pushing some malicious thing to your
GitHub repo uh you pull the code for
your latest work and boom you're You're
gone as well so it's very hard but the
only way to do it is um to have proper
training is to do it for any
communication uh then just ignore it if
it's important they'll reach out again
um can be messages emails letters
anything the other one is verify
identity independently it goes into like
the rule of multiple factors of
authentication everywhere uh where like
if someone does you to do something
critical over telegram for example make
sure to verify it over slack also or
verify over WhatsApp also to make sure
it's the right person you're talking to
um things like that if a new person
connects to you at this conference via
telegram hey I lead this thing at this
company blah blah blah maybe ask them to
send you an email from their cor another
attack uh some of the operatives might
be here with us learning how to get
better so we have to stay a step ahead
of them uh avoid clicking suspicious
things use strong passwords tofa keep
software updated um educate yourself um
and so on like I'm going really fast
because lots of content to go
through uh the thing
is if they really want to get you they
will get you there are so many attack
vectors that it is almost almost
impossible to defend against so what we
need is layers of security layers of
security is what's going to help you for
example um it should NE it you should
architect your things in a way that even
if you are compromised or even if one
person is compromised nothing is lost
this is why multisig are very handy if
properly done I'll come to that but
imagine a scenario where there is um
let's say even a 3x5 multis to
compromise a 3x5 multi-c you need to
compromise three people even if it's VI
fishing or social engineering
compromising three people at the same
time which might be using different uh
mechanisms or might be physically
located differently or will have
different ways to responding messages is
very hard versus just compromising one
person um so I can like if they want to
compromise any one person they will
reach out to you now you might get
compromised today or you might defend
against 100 attacks and you might get
compromised 2 years later but eventually
you will fall if they want to come after
you but if they have to go after three
people it is very hard even if one Falls
they will know and recover by the time
they can get the second one um so just
have more people in line layers of
security uh and that's the other thing
like yes social engineering is the
common thread here but actually it's
none of the attacks are just social
engineering social social engineering is
just a step inside the door uh it
doesn't give them anything if you
architect things properly and that's how
things should be um you avoid social
engineering at all costs you make it
hard and expensive for them to do it but
you architect your things in a way that
even if someone is social engineered
nothing really happens um and one of the
best things to do is is principle of
lease privilege uh but we'll get to it
first let's yeah delayers of security
first one I mentioned is principle of
lease privilege I really stand by it in
the sense like I see in a lot of
companies like the CEOs and everything
will say oh give me all the access like
I'm the most important person but the
reality is if you want a proper security
architecture the most public faces
should have the least uh Authority or
the least access if you look at polygon
like the founders have no access sandep
can't even open my calendar um so it's
just like even if they get tricked the
the attackers will get nothing even me
have I have less access than anyone
reporting up to me uh just because I am
a bigger Target it's natural people will
go after me um but yeah you come after
me you will get nothing so uh is not how
you secure things multiple factors of
authentication is very important um I
said like if someone sends you on
telegram verify it on WhatsApp and so on
MDM EDR is very underrated but a very
nice tool it's basically corporate
antivirus um and I I said it's all about
layers of security you will stop medr
will stop another 99% and um it's itive
in the sense like it's then you're
stopping 99.99% attacks like um so it's
better to have those layers um then uh
just architect things properly don't
have a 3x1 multi for example that's not
very safe uh don't have a one by two
multisig as well uh don't give access to
all of your keys of the multisig to one
hot wallet um it doesn't help that way
so um yeah just architect things
properly in a trust minimized uh setup
where you don't need to trust anything
the other big one is safe custody most
of the hacks that Lazarus has done if
those protocol were coding Keys safely
it wouldn't have happened the underlying
root cause really was just poor custody
of keys um and always use your Spider
Sense like if something smells wrong it
probably is wrong be be cautious about
that um and this is the big topic how do
you custody safely um so it I'll focus
on multix but um I'll start with the
caveat that consider using a
professional custodian um maybe even
service like fire blocks if you don't
know what you're doing um once you get
comfortable with it once you learn the
things then you can do it on your own
but there is no shame in using someone
better if you are not experienced in
something nobody can know all of the
things in the world so it's better to
not risk it and just use a professional
custodian if you're not comfortable but
if you are self coding then let's talk
about it one thing you need to do is use
Hardware wallets it doesn't matter if
it's $100 of crypto ,000 of crypto or if
it's just a multi key use Hardware
wallets like browser wallets are just
inherently not safe enough um the other
one the obvious one is do not share your
nimonic private key whatever with anyone
do not share it with metamask support do
not enter it out in a computer do not
copy paste it uh do not take a photo of
it and upload it on Google photos as a
backup there's so many ways but this is
the most common way that people fall for
it believe it or not so just keep your
private key safe and make sure it's
backed up don't lose access to that
wallet uh then I'll get on some more
dedicated tips one is if you're using
Hardware wallet always try to connect it
through rabby or metamask or other
browser wallets to uh websites is then
you can verify what's happening in your
browser wallet as well so you're
basically instead of completely just
trusting the website you're trusting
your browser wallet to um so yeah you're
connecting uh to nosis save connect your
ledger to your rabby and connect your
rabby to your nosis save so whatever
noses save sends for Signature you
verify on rabby you can consider using a
dedicated device for signing
significantly um then use multi6 it's uh
very basic Hardware wallets are totally
fine but definitely use multis before
that I will focus on one more Point uh
which is very Ledger wallets like I know
it's you only see hash sometimes but you
need to verify it um there is actually a
good script apps that that would take
your safe transaction convert the hash
and then you can verify that they hash
on your computer screen and your
Hardware wallet matches the reason for
uh doing that if computer is compromised
or the website is compromised and you
are seeing one thing you seeing okay I'm
transferring $100 to um which you don't
want to do but if you don't verify it on
your Ledger me the screen and the device
which can and your Ledger which can be
compromised which can change this so you
should verify always everything on your
Ledger device as
well uh when using multi6 the other
thing is ensure a is not secure it's not
the industry best practices as someone
some might claim um so just you have to
balance out risk and practicality with
security so I'm not saying do like 99 by
practical nobody is going to follow it
but create risk profiles and uh set
standards for what you are going to do
if it's very critical software then um I
I would say like use some ratios like uh
uh 8X 11 9x 12 something like that uh
very high ratio uh so people would have
to compromise like 8 nine people to uh
compromise what uh you are doing the
other thing is always segregate wallets
based on their act multis for all
purposes for operations and everything
like don't use your critical multi to do
$10 payments no like have a separate
operational multisig have a separate
treasury multisig have a separate one
frisks so and you can have different
thresholds then accordingly so your
operations are not blocked I'm expecting
nobody is doing upgrades every day so
that multis can be a lot more secure if
you're doing smart contracts every let's
have a talk something is wrong um but
yeah like ideally you should not be
upgrading things every day and I'm not
going to stop you from making $10
payments every day that one you can do
in a more practical
way uh then for uh signers try to use a
diverse set of signing devices um and
the reason for that is to compromise uh
like a Windows machine plus metamask is
a completely different risk profile than
compromising Android plus uh Ledger uh
nanox with Bluetooth and so on um so the
more diversed set of signing devices you
have the harder it's going to be to
execute an attack against you um it you
can argue that one stack is uh
theoretically safer than the other but
having the diversity gives you security
of both it gives you benefit of the Both
Worlds um and you can enforce you don't
really need to enforce it if you let
naturally people use what they want to
use you will have a diversified set but
if you somehow end up everyone with one
set you can ask them to move to another
the other big one I want to mention is
do not ignore failures when signing this
is how vazer X and other folks uh fell
for it
they signed a malicious transaction and
they saw a failure on the screen because
it wasn't the right one the app was
expecting and they was like H it's web 3
five failures one success it's normal
Let's uh let's try again uh but no if
you fail a critical if you have a
failure on your critical device figure
out why it failed before moving on to
more signatures um that is uh very
important so these are some of the
things you need to do to stay safe uh
once you have safe custody actually you
you would be in a very good situation
and when I say custody it's not just
crypto custody but any secret custody um
for example for axi their custody system
was their uh private keys for validators
signing keys for validators or the
bridge operators basically they had to
keep those secure but they weren't
that's where they got hacked three it's
Web Two compromise of a secret the
secret can be a private key it could be
something else it's at the end of the
day it's the same thing we have not seen
Lazarus execute a big smart contract
hack so far uh I'm not saying they don't
have the expertise I'm sure they are
building it up but in the current world
uh we need to be more worried about uh
these Basics instead of the smart
contract I think we have gotten a we
have made covered a lot of ground there
and we are very good at smart contract
security we just need to get better at
other
things and that's it for today uh thanks
for coming I will open it up to
questions awesome
thank you very much round Applause for
you all right uh first question on the
screen which I also had in mind do you
think there's anyone from Lazarus in
Defcon or even in this talk what do you
think mud most likely yes I mean most
likely yes when you were saying they're
in Thailand I was like so yeah I don't
know about like the likelihood is flip
someone in that's why like just be
careful with your security don't scan
random QR codes for questions maybe yes
yes but this one this one no wait this
is not random this is randomly generated
but it's not random it's purposeful
there's a secret inside you can get an
nft and it's 100% secure right right
mudit say yes yes yeah very good thank
you okay next question um did you say
that Lazarus has 25,000 operators I'm
not sure but was that what you said so
nobody knows the exact number uh but
this is the best estimates from that's
all right um P keys versus UB Keys what
do you think it doesn't need to be
versus it can be both they just have
multiple factors of Authentication I'm
not a big fan of just using passys as
your authentication mechanism because
again then you're relying on a single
medium and the way pass keys are
implemented it's a whole different topic
but I have so many complaints for
example like all of that would be if
you're using iPhone it would be bagged
in your iCloud if it's use if you're
using Google it would be withle factors
of authentication every time exactly I
think echoing what he said diversity in
your security all right do you think the
guy asking if laus members are here is
larus could be could be Double Double
Bluff technically they Lazarus tries to
stay under the hood they don't want the
Limelight so unlikely that the person
would ask unlikely but POS so I've been
pred to like since morning probably 10
fishing attempts um I don't know if it's
Lazarus I don't want to know if it's
Lazarus um and you should with the 10
fishing attempts if you don't mind
sharing a little bit so people are aware
yeah for sure I mean uh just telegram
messages uh Twitter messages uh emails
through those and all of the attack
vectors I mentioned um here this morning
and it it keeps happening the more
public visibility you have the more
people will go after you and the more
security not perhaps of Lazarus but have
you fallen victim to a fishing scam or
another type of scam
before um I we have detected at polygon
a few times when Lazarus tried to we
never even took their interviews but it
was obvious it's Lazarus uh on the infra
side they keep trying to get in with
scan Lazarus IPS that we block um and so
on so I know they are trying uh but so
far we have not detected any successful
attack I'm I'm very happy to hear I'm
sure the audience failed what is the
improve their personal
security uh just be cautious of things
don't trust I was wrong it was the
actual Kobe um so if he's watching this
I'm sorry um moving on to the next
question are you considered a local Dev
isolation as one of the security or do
you consider local death isolation as
one of the Security Solutions I mean I
mean I'm not sure what this question you
eliminate lots of attack vectors but
there are still a few which sneak in so
here concerns like the worldclass
policies which would make you
impenetrable but if you are practically
not able to follow those it means
nothing all right thank you for that
answer as well very comprehensive few
more Before Time runs out what what's
why it was obvious to you but how is it
obvious so the most obvious giveaway for
me has been fake job experience like um
I was leading R&amp;D at Sushi swap before
this the developers say they are the
lead developer at Sushi swap I'm like no
you are not um so verify the references
that's the biggest one and beyond that
like it's it's usually gets clear from
the resume if it looks fake it probably
is fake like even if you miss out on a
good candidate it's better to be safe
but once if you don't detect that at
that stage you got get in a call try to
get them to turn on their video and you
would see like the way they behave is
very like robotic kind of of um their
English is broken they would say I've
been living in America for 25 years and
then say speak broken things just don't
add up uh it could be anything but you
if you have that Spider Sense you'll
realize right very very good points as
well verify uh are you part of lrus I'm
going to answer that as uh leave it as
mystery um uh let's go to a few more we
got a 1 minute and a half fishing
campaigns are too basic and fishing done
by dprk is very sophisticated so why do
you think it's useful to do them good
question fishing campaigns are not basic
maybe the fishing campaigns you have
seen are basic U but I can construct
fishing campaigns that um so it's it's
it's just that yes by default the
default template fishing campaigns are
simple but some examples manager's name
and said please join this meeting
urgently Ross and I almost hovered over
it and I was like wait a second checked
with my manager and found out it was
fishing uh we got 30 seconds let's see
one or two
more yes some private Intel but this
number I think is on the internet as
well all right 10 seconds to answer this
um they have a big laundering Network um
they use uh you can learn about it a lot
more I don't want to detail how to
launder coins but uh there is ways there
are ways to do it a nice careful answer
ladies and Gentlemen let's give our
speaker all right now don't go anywhere
we've got one final session and we're
going to be learning about one of the
biggest scam techniques in the world now
as for someone like myself I've worked
in security before I've seen this happen
to people I've seen people lose their
life savings and so if you want to
protect yourself you want to protect
your life savings please stay tuned for
this next talk because this speaker is
going to be talking about something
known as the long con yeah there are
types of scams which is like you just
click a link and you get hacked right
there are other scams which can go over
for days for weeks for months I have
personal experience of handling a
customer and he was scammed for 2 years
sending money to a con Pig butchering
drainers and job scams yeah Pig
butchering is really really really
terrible it's it's called that way and
I'm sure our speaker will explain a
little bit more about how you gain the
trust of the victim and you feed them
information they want to hear when
they've trusted you and then you keep on
draining them of their funds right it's
really really quite terrible so please
don't go anywhere I know some of you may
want to go for another session but
personally I would say please please sit
down and listen to this session it's
really important not just for you but
people around you as well when you know
more you're able to help other people
understand ecosystem since 2017 holding
key roles such as managing editor of eth
news and project manager at my crypto
currently serving as the Director of
metamask security how many of you use
metamask say yes yes okay how many of
you protect your metamask with a
hardware wallet say yes okay I saw about
three hands okay okay the rest of you
you've just heard Hardware wallets are
good at the me from getting my nfts
drained I can attest to that personally
our next speaker is going to be teaching
you about these long con scams now else
is going to get it and we won't get it
but that's exactly why we have to be
more aware because we might right
everybody can be scammed I've seen it
happen a thousand times so please let's
put our hands together and welcome our
next speaker to the stage Luca big round
of applause for her all right
hello everybody Welcome to my talk thank
you for coming we're going to cover as
mentioned uh Pig butchering drainers and
job scams or as I like to call it the
most depressing talk at Devcon so buckle
up it's going to be fun um but before we
get into any of that we're going to have
to start with social engineering of
course because uh the vast majority or
you just started getting hit by social
engineering um some of you may have uh
seen the headlines a few months ago when
$243 Million worth of bitcoin was stolen
from a single person and that was
because of social engineering the
scammers were actually able to pose as
uh customer support from Google and
Gemini and they talked this this target
into giving up his Bitcoin uh thanks to
some investigative work by Zack xbt
shout out uh they were able to track
down um so there are some groups in the
space um there are others and if I
haven't mentioned you thank you for the
work that you're doing um but we're all
try before that is true and you are
about to interact with the URL that's on
one of the block lists and just so you
know it's getting a facelift so if you
see something different than what you're
expecting that never going to contact
you uh never trust links that are shared
on social media come from unsolicited
emails uh Discord telegram all that
stuff you're going to want to avoid and
if support does cont contact you about
something that you think might be
legitimate stop that conversation go to
where you know they to tell you what's
up for Builders make it really obvious
for your users we protect the users it
shouldn't be put the other way around
and the owners to be on the user the
owners to be on the
users but uh let's get into
drainers
uh the they are designed to maximize the
value out of theft the drainers as
services are they are complete with
their own advertising their own customer
support and as it turns out even mergers
Acquisitions uh getting back to the
account or to the social engineering
there's account takeovers are uh one of
the tactics that is usually employed to
get those risky clicks and these
scammers are bold enough to uh
compromise nft impersonator
impersonations fake airdrops and
giveaways and another Tac by access to
publish mic malicious versions of
packages that are then used by defi
ends uh spin up again you don't need any
kind of advanced expertise to use them
fighting them is like playing
whack-a-mole they are constantly
iterating they can Target many users
with a single campaign calculated just
one of these drainer Services uh which
this was an inferno has amassed over
$250 million from uh 250 18,000
victims and so if you see with just
these seven campaigns here there is a
combined reported loss of 75 over $75
million and there's what we're seeing a
lot is countless cases of individuals
who are losing smaller amounts at a time
so that really adds up but I do want you
to rest assured that so far there have
been no reports of theft by mudang
that's we're say some campaigns become
more successful uh the drainer vendor
are looking to acquire customers from
other other vendors who are retired
making a percentage off of each hit and
by acquiring Inferno Angel drainer has
now gained all of their Affiliates and
all of their drainer
strategies so don't get drained double
check URLs don't trust unsolicited
messages beware of giveaways uh read and
understand the transactions that you're
about to sign and you know just practice
General good wallet hygiene these are
the basics that we at all on one side of
it it's the the scammers are posing as
recruiter mentioned in the previous talk
um they could offer exciting job
opportunities competitive pay really
good benefits uh maybe this is a big
step up from your current position it's
enticing um but they're going to contact
you through social media or some kind of
me messaging app and then once they
Garner your interest they will have you
do a skills test and this is you know
very common for developers in our
industry but what the next step is is
they're going to ask you to clone a repo
or download some files and then that's
how they get you and if you notice on um
so really once they get you to do the
cloning and the downloading then they
can compromise your machine and do a
whole lot of dam come to you and ask you
to collaborate on a project or ask you
to help and I think especially in this
space it's kind of uh our nature to want
to lift up the builders around us too
how they get you because you kind of
need to always be aware of the stranger
danger when it comes to these sorts of
things and if you happen to be using uh
your company's laptop to help them out
then you've now compromised your company
server infrastructure and that's not
going to be good for
anyone don't run or build code from
strangers unless you're using repo uh
and again just practice really good
everyday crypto maintenance hygiene they
are targeting crypto projects from
startups to Big powerhouses in the space
and uh Zach xbt again using counterfeit
identification to get hired by a
startling number of crypto companies uh
one high-profile hack from March was
munchables who lost uh $63 Million worth
of eth and it turns out that that was
actually at the hands of one of their
own developers who allegedly had ties to
North
Korea besides the financial loss at
stake uh you know it's IL legal to
violate sanctions laws and most if
companies come forward they are seen as
victims themselves there might be a
Tipping Point where that is no longer
the case and it's no I'm if you are a
company who is hiring just always play
safe and if you suspect that you have
hired someone from a sanctioned country
then it's going to be in your best
interest to report it invest in really
thorough uh highlevel thorough
background checks um the these some of
these people are going to have verified
previous employment some of them have
it's going to be really hard to spot
some of them some of them are easy but
some of them are not and uh you know
some best practices again are the
principal least Authority don't the
access to sensitive materials to the
bare minimum number of people and look
out for suspicious behavior of new hires
uh what we have been seeing a lot of is
like one identity of a worker will
actually be passed between several
people behind the keyboard so keep an
eye out for big shifts in personel ity
big shifts in speech pattern all that
kind of thing yeah they they're usually
not going to be on camera
also um these are some of the top
Advance they're T but some of these dprk
workers don't even have to engage in
sabot sabotage all they have to do is
show up for their job you know do their
do the work collect the paycheck and
then funnel money back to the regime
because really at the end of the day
that's where all the money is going
anyway and it's being used to fund the
North Korean military and they have been
able to make significant advancements
over the past decade off of the uh un
estimates between 250 and $600 million
every year going to the
dprk um it's very possible that over
half of applicants in crypto are
dprk and uh just a little fact toid a
wage M make moodang very
Angy but don't worry it gets wor
course uh Pig butchering this is the fun
one uh this is where the scammer will
build up a relationship over time to
gain trust um sometimes it's through
social media sometimes it's through
dating apps and again they they're
they're building up the trust over weeks
months years and they eventually forms
uh and then they'll ask for more money
and eventually just drain the account
which is going in for the kill after
fattening them up so this tactic was ini
popularized in China uh before it spread
to other parts of Asia and now we're
seeing it actually in all sorts of
places all over the
world um and it'll start off usually
pretty innocuous uh either you know it's
a connection on a dating app or it's
some colleague that you kind of sort of
remember but don't from back in the day
reaching out to you uh and it'll never
start with them talking about crypto
again they're building they're laying
that Foundation of trust and then after
a long time time that they will uh
they'll clue you in on some investment
opportunity that they have for
you um and of course if a stranger
contacts you out of the blue it's really
and then and they're like oh invest in a
thing it's really easy to have those red
flags you're not going to you're not
going to engage with them but uh as more
and more of our social relationships are
happening online it's it's a little bit
it's getting a little bit trickier
because I'm I'm willing to bet that a
lot of people in this room have uh
friends and colleagues that they've
never actually met in real life and I'm
sure most of those people are not Pig
butcher but you know some of them very
well could be uh and it's once that
trust is formed once that you've uh
engaged that they've been playing you
this whole
time uh because these targets there
there sometimes who is who's uh
expressing affection for you and then
they're putting in hey there's like this
financial gain you can have on top of it
it all comes becomes very
enticing uh and you know sometimes these
people are uh have insecurities about
their financial future or the financial
future of their family so it's not
always just based in greed of getting
the gains uh I just wanted to point that
out so some of the major steps that we
see in most of these scams is first uh
the scammer will present themsel as very
successful wealthy put together
individual looking for a long-term
relationship
um they will send a lot of piics but not
uh doing video although with the rise of
AI and deep fakes we might see a shift
in that part of it but the the next part
is grooming they will move very quickly
to declare their love to the Target uh
they will chat daily again being very
affectionate and then eventually they
will introduce the target to some third
party uh dii app or website that is fake
and they will Coach them into to how to
buy crypto from an exchange and make the
transactions because most of these
targets are not crypto Savvy to begin
with uh will or a tax that you need to
pay it's any uh and that'll keep going
until either the money is gone or the
victim catches wise and at that point
the scammer will ghost them and that's
the end of
that um and this is just an example of
one of the fake platforms I don't know
if I'm standing in the way uh you can
see that it's very
realistic uh and that's where you are
watching your fake gains which uh are
pretty colors to look at but your
money's gone once you put it in there
syndicates and the scammers have been
specifically trained in order to gain
trust and get the most value out of
their victims they have quotas that they
have to
meet um and a lot of these uh activities
are taking place in on so the gangs are
able to run wild
there uh and it's going to get a little
bit darker now uh it's easy to see
everyone involved in these scams as just
evil but the truth is that a lot of them
are actually participating against their
will often they themselves have been
scammed into uh being abducted by these
groups so just put yourself in their
shoes for a moment you know they they
don't have a lot of money but they have
a promise of a really good job the
company has a fake online presence so
you look into it it looks legitimate you
show up to get the job they pick you up
in a really nice car
then they take you to another car that
has a different driver and then maybe
another vehicle and then you're on a
boat and then you're just gone and what
really happened that you you have been
trafficked across International borders
uh and they you're worth a lot of money
to the people who have just bought you
and the only way they're going to let
you go is if your family comes up with
uh at least as much as they paid for you
if not more and it's such an exorbitant
amount that there's no way your family
will ever be able to come up with that
money
um and then of course because of that
now you're being forced into labor of
conducting these scams against other
people in scam centers this is what one
of the compounds looks like that they
are taken to this one's in Cambodia um
they have hundreds of rooms for tens of
thousands of Internet victims and this
is where they are taught um all the
tactics to use against
people one of the largest if not the
largest uh comp uh they have made well
over $100 million just in
cont trips up that way however this is
how close we are to mudang and that
might be a lot more fun of an adventure
for you um I'm running out of time so
this shows money movement that goes
actually to some mainstream exchanges
that have not been named and um okay
trigger warning I'll go through this
part
fast they if the people don't meet their
quotas they are tortured beaten deprived
of be a little heavy for some
people um of course some people do get
out they are coming forward with their
stories they are sharing um but these
Escape attempts are Global Advanced
projects is a nonprofit they're
dedicated to uh exiting people from
places like Myanmar uh where these
things are happening and they actually
bring them back here to Thailand because
uh the the company is based in or the
organization is based in Australia but
they have a lot of people bring them
back to Thailand to get them safe I
don't have any affili with them but if
you're trying to throw money at
something this might be a really good
one and if you want to dig deeper into
what's going on with pig butchering they
have a really great documentary it's
short it's heavy but I would check it
out uh and we did it we got through the
most depressing talk at Devcon Pat
yourselves on the
back on let's give a big round of
applause I thought that was a very very
informative session thank you so much I
know you had to rush through a little
bit but we really really appreciate now
it really is important I've seen Victor
of these scams in person I know someone
who was actually trafficked across the
border and thrown into the back of a van
passport taken whipped it right into the
U the the like conentration cam it's not
even a room it's a concentration cam put
in front of a computer for 12 hours a
day he has to scam people thankfully his
family got him out but it is wild it is
wild anyway let's look at some of the
questions on the screen um who are at
most um I would acceptable to social
engineering and that's really the heart
of all of this yeah yeah um would you
say that there's any people who are more
at risk perhaps like older folks do you
find that older people usually get more
Pig butchering scams or yeah I would say
old older people do of putting it
everybody can be scammed so never take
it for granted all right uh okay oop
excuse me have you ever thank God thank
God for that all right next question is
it common to decline a skills test or
decline downloading a file in the
process of an interview do you think
employers should uphold the end of
protecting everyone in the process now
that's an that's a good question and I
do think that it should be uh on the the
companies to be educated themselves on
what risks are out there and file and
you know you could easily very easily be
compromised okay have you seen examples
of hackers was using AI to make their
scams more legit or for example using
facial editing technology to impersonate
others oh 100% And I didn't have it on
one of my I feel like we are going to
see a lot more of the deep fake
happening definitely as time goes on you
know what my family and I have done is
that we've come up with a secret word so
we told our mother especially my mom
because she tends to Yes um if someone
calls you and says I've been kidnapped
please send me money I have to say this
secret word afro sorry um um you know um
some other secret word perhaps not my
hair but um because I think that's
important because families really can
can fall victim to these scams and I
would highly recommend that you and your
family come up with a safe word uh sorry
secret word um oh my slight slip of the
tongue there sorry live streamers um all
right let's go at the top everybody's
voting voting voting okay keep the votes
on consensus what is your opinion on
Chrome security extensions that help
secure manam Mas example cbus fire
revoke cash an imposter of Faking to be
wallet guard just like do your homework
and make sure that you're using the
legitimate extensions and I would keep
them to a minimum exactly and I would
highly recommend Hardware wallets guys
Hardware okay in fishing attacks there
are many attacks by North Korea Lazarus
but are there any cases where you've
heard of Russia or China sorry moved out
Russia or China hackers what what's your
experience with all right I mean
basically anywhere in the world right
anywhere people want to make money they
will find ways to hack you what
in-person social engineering tactics are
you aware of what should be wary of when
traveling okay so this is in public
let's say I'm in a setting like a
conference what are some of the in area
of expertise but um doing things to
distract you um touching you um like any
way that they can pickpocket you or get
your phone anything like that that uh I
would watch out for yeah yeah the one
that I've seen is when people say oh
could you show me your telegram or
something and they open their pin number
and then you've got their pin number all
you need to take is their phone and you
can unlock everything so please be
careful yeah um we've got 20 seconds
let's do one last two or rather look
aware of from the go however they're
also saying that semi-autonomous AI
could be used to combat them by security
which is kind of exciting AI versus AI
yeah fantastic all right again I know
many of you had other final day at
Devcon it's coming almost to the end but
please we welcome you back to the stage
tomorrow's topics are going to be crypto
economics and I believe we have a
session on layer 2 as well
cryptoeconomics is a fascinating area
where you can learn more about
cryptography crypto economics and so
much more about layer 2 as well so
please come back to stage number two we
always happy to see you here and other
than that please enjoy yourselves we've
got lots and lots of other talks as well
wherever you feel best suited go and
enjoy my name is Ross Stevenson's been a
pleasure being your MC and host for the
end of stage two thank you guys so much
see you tomorrow
true
