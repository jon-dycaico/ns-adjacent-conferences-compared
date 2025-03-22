[Music]
e
[Laughter]
for
sh
you
good to go awesome hey what's up
everybody how's it going oh I got to
close some stuff out here still have
some stuff open from the last
session yeah be a good client that's
cool okay so hi I'm Austin Griffith uh I
um helped create the uh build gild Dow
and we are focused on developer
education uh in particular we have this
stack scaffold eth and this curriculum
speedrun aum.com uh if you are
interested in learning how to build on
ethereum or you even have friends that
are interested in building on ethereum
tell them to go speedrun ethereum I see
some familiar faces that were at the
last sessions uh it's a lot of the same
similar content today we're just going
to start with scaffold eth and build
something simple and then I'm going to
hand it off to Kevin Jones and he's
going to do a uh like an extensions
build I think so we're going to kind of
try to wrap two sessions into one here
I'll do the intro to scaffold eth and
then uh he'll do that
extensions and I think maybe we'll even
have like a little Q&amp;A possibly in the
middle of them too while he's getting
ready so uh scaffold eth is our stack of
choice and uh it's great for prototyping
oh look at that we still got our nft up
I got to close stuff out here holy
cow sorry boop boop boop boop boop boop
boop boop boop boop okay here we go so
scaffold e you can find it at scaffold
eat.io it's uh it's a prototyping tool
but you can also push to production uh
it's good for tinkering and and we'll
get into it here so there's two ways to
do it you can kind of Clone the repo
that's kind of the old way to do it and
the new way to do it is with npx create
eth and uh npx create eth is sort of
like the step toward our extension
system so we'll be using that uh mostly
today and uh yeah I think just to level
set real quick we probably I probably
didn't introduce this very well uh we're
going to have like a whole day here I
think we're in this room like all day
today till like 6:30 tonight or 5:30 or
something like that so we're going to do
introductory content right now I'm just
going to quickly show you how to build
and ship an app uh then Kevin will do
the extensions then I think we'll take a
lunch break and we'll come back and
we'll build uh a few more things and
then we're going to have a CTF later
today so a capture the flag where you
actually have to like hack some
contracts and mint some Flags so it's
it's going to be a lot of fun if you're
more technical the afternoon will be
better if you're just getting started uh
the morning will be better I so sorry to
all the people that I keep seeing at all
these talks you you guys keep coming to
my talks and I keep doing the same
builds like I need to like innovate a
little bit here I try to do something a
little different every time just to make
it more interesting but thank you guys
for coming out and supporting okay let's
go let's get uh scaffold eth going here
so uh we're going to run MPX create eth
and it's going to be kind of like a
little uh Choose Your Own Adventure here
it's going to take us through let's see
this is Dev con app I'm going to call it
Devcon app 3 I think is where we're at
right now and uh this is kind of like
one of are more controversial things we
kind of still have defaulted to hard hat
it's taking us a while to like really
get Foundry the way we want in scaffold
e but you can choose between hard hat
and Foundry and Foundry is almost going
to be the default soon but uh it's up to
you you can choose either one both are
good uh Foundry you're going to spend
more time writing uh your tests in
solidity and so if you're building just
like a super complicated protocol like
Foundry is probably the option that you
should take because you're going to need
to write lots of tests
um and those tests run in solidity if
you choose hard hat it's a great option
still uh I think the deployments are a
little smoother and everything's in
typescript so I think hard hat leans a
little bit more toward like the app
Builders uh and they're doing a good job
at like speeding up too I think maybe
one of the concerns was that Foundry was
just a lot faster than hard hat and I
think they're they're improving a lot of
those things I just pick one randomly I
think I did hard hat for my Devcon app
number one and I think I did Foundry for
my Devcon app number two and I'm just
randomly back to hard hat for Devcon app
three but it doesn't matter whether you
choose Foundry or hard hat it's still
going to be the same commands we're
going to do a yarn chain to bring up a
chain yeah what's up you
sayt uh that's F uh hard hat hard hat is
all your tests will run in typescript so
like when you build out a test Bank in
typescript you know go query this amount
make sure it's that amount write to the
contract and make sure it wrote
correctly you're going to be writing
that in typescript and so that makes it
really nice if you're going to also be
building an app because you can get in
and kind of copy that code right into
your app so if you're an app builder
sometimes writing those tests in
typescript make sense but it seems like
the Giga brains are moving toward
solidity as a testing you know what I'm
saying
like I can tell that they're smarter
than me and they know what they're doing
but I don't know exactly why but they're
they they're they're on to something so
I think that like the The Foundry and
testing with solidity is like the future
and probably where we'll go uh but as an
app builder I feel like I can relate uh
with typescript and JavaScript
more and like I said like when you can
copy paste right into your app it's
really nice okay so once everything is
installed and shout out to the
organizers this is cool like I've been
to conferences before where I've done
demos and the internet was not good
enough to install this whole stack and
we just installed the whole stack just
now so shout out uh to Skyler and the
team and the Devcon team nton okay and
of course all of you guys that are doing
all the work behind the scenes okay here
we go we're going to spin up our local
blockchain so like I said whether you're
using hard hat or Foundry it's the same
command with scaffold e we kind of
abstract it away a little bit and just
give you the commands that you need that
command was yarn chain so I ran a yarn
chain and that basically spins up my
local blockchain and then I can do a
yarn deploy and that's going to deploy a
uh the kind of like the template smart
contract that comes with scaffold eth
and then we're going to do a yarn start
in another terminal here so it's kind of
like launching a rocket you got a few
you got a few uh a few things here it
feels it feels overly complicated but
once you figure out that this is kind of
like mixing two packages together and
you sort of have this back end that is
the the uh blockchain and then you have
the front end which is like your next JS
it starts to make sense how this works
and scaffold eth uh particularly does a
good job with taking your artifacts from
your smart contract and injecting them
into your front end and I'll show that
when we start writing the front end it's
really nice because it starts to give
you hints and it knows everything about
your contract
already Okay so let's get into the code
I'm going to use cursor or code whatever
if you guys use code you just do code
dot right but I like cursor even if I'm
not using the AI feature I just use it
as my IDE most of the time but it's
really nice because it has this tab over
here where you can pull it out and be
like yo build some buttons and GPT or
claw will just like inline write the
code for you so definitely if you
haven't checked out cursor go go grab it
it's a great uh code ID okay so if we
look at our packages we have hard hat
and then we have nextjs like I said
that's kind of like your back end and
your front end and if we get into hard
hat we can find the contracts scaffold e
starts with this kind of generic
contract that has a little bit of
everything just to get you started a lot
of times you might just like carve it
out right that's why we called it
scaffold e you kind of need the
scaffolding but then as you get the
thing built that you want you can kind
of tear down some of the scaffolding oh
I think my little mic is going weird
okay here we go so uh let's get into
this contract and look at it and let's
just Tinker around I think one of the
first things to show off with scaffold
eth is just this this kind of Dev Loop
you'll get
into and let's let's look at that okay
so we've got some let's look at this
smart contract is that big enough you
guys can see that
okay yeah yeah okay so uh you've kind of
got your primitive data types whether
you're tracking addresses or strings or
bus or numbers uh there's mappings
between these primitive data types like
for any given address you can keep track
of a number like a balance or something
uh events The Constructor even a
modifier here which is a little goofy
you you can kind of get the syntax uh I
would recommend solidity by example if
you uh are feeling like you need a
little bit more uh help figuring out the
syntax and just getting a little bit
better at just writing your your first
you know few smart contracts definitely
check out solidity by example and just
like go through each of these examples
and just copy paste them into scaffold e
and and they're they're really great
examples to learn from like for instance
like if we were going to go learn what a
mapping is all about we could get over
here and we could copy this mapping and
we could paste it into our smart
contract and then go dink around with it
right that's that's kind of like a good
Loop to get into let me specifically get
to this contract and Dink around with it
but I just wanted to show off solidity
by example as kind of a tangent here
whenever you're writing your smart
contract if you're writing it yourself
and not just prompting AI you probably
want to like go to solidity by example
and find some of these uh kind of nice
copy paste examples but I'm going to
close that out we're we're going to go
for memory here okay so uh I want to
look at this set greeting function it
looks like we pass in some greeting a
classic you know greeting contract this
guy's kind of waving around am I okay
here there we go uh classic greeter
contract we're going to set some string
uh but this is the the neat little code
block that I want to test basically it's
if you send money in when you set the
greeting it sets its little premium flag
to true and I think that's going to be
what what we'll do here in a second okay
so once we have our backend up and we
have our front end up let's go visit our
app here it is so scaffold e kind of
comes with you're you're going to write
some solidity and then you're going to
have this debug tab here let me make
this a little wider there we go see that
debug tab there we go this debug Tab and
this is going to give you this really
nice interface where you can kind of
just pointand click try things out you
can poke at your contract you can test
your assumptions so let's go look at
that greeting contract let's go set the
greeting right and that's going to teach
us about burner wallets and eth to way
couple of the initial Concepts uh let's
let's just try to set it it's going to
yell at us so if I say hello world and I
hit send it's going to say something
like you don't have any money and so
right up here there's a nice little uh
when you're on Local Host it recognizes
you're on Local Host and it gives you a
nice little faucet button but as soon as
you push this thing to a live Network
that faucet will disappear so I'm just
going to click that and that should give
me some eth right now we've got some
some money to work with now the second
thing I want to bring up is burner
wallets uh you'll notice there's a
wallet here and I could connect my
metamask if I wanted but but when we're
doing local development when we're doing
uh quick Dev I want to be able to just
like hit a button and send this
transaction I want to just be able to
click it and have it go right did you
see that like that was a transaction
there's a transaction that's a
transaction that's a transaction you get
a transaction you get a transaction so
it's just faster and it's a lot easier
to kind of test what you're doing to not
have metamask popping up and uh
switching the chain ID and a bunch of
other things that you'll run into but
this thing's all ready to go so by the
time we push this thing to a public
network work we'll be able to bring
metamask in and we'll be able to hide
those burner wallets but for now it
works really good for Dev and let me
just triple down on the burner wallet
thing real quick if I open up an
incognito window and I go to Local Host
see I get this account this sort of 1
a55 let me do that
again Local Host and it's a new account
right because it's in uh Incognito and
it's keeping the private key at local
storage you're getting a new one each
time you bring up that incognito window
which is super nice for testing and and
I'll show you that in a little bit but
basically you could say you have this
function that you only want the owner to
be able to call with this uh with these
burner wallets you can kind of bring up
the good guy burner wallet bring up the
bad guy burner wallet make sure the good
guy can do the thing make sure the bad
guy can't do the thing it's not like an
exhaustive test but it's a great way to
quickly test your
assumptions okay here we go let's go
hello world hello world 3 that's what
I'm oh whoops hello world 3 send it okay
so I want to get this premium flag see
over here these are all the like uh read
it's reading from our contract all these
different values and there's this
premium flag here that's still false so
what I want to do is send in some money
right the contract is still empty it
doesn't have any money what we're going
to do is we're going to send in
about building on blockchain is this
whole idea of eth verse way and again
solidity by example has a really good
ether verse way explainer here and
uh when you put a one so when I'm in a
smart contract and I put uh you know a
one right here that is one way right and
so if I wanted to send one E I need to
send one times oh get out of here one
* time 10 to the power of 18 right that
is 1 eth and the reason is the evm is a
super simple little computer it doesn't
want to mess around with floating Point
map so you don't do decimals in solidity
you have to basically do whole numbers
so sometimes when you need to do
something like uh take a thing and add
numerator denominator stuff uh but the
the thing is is right here we have this
little button and it does that for you
now only would a developer need this
like once you start building your front
end you need to do the eth to way
conversions all in the background and
the user should not know about it you
should just be like I want to spend 0.01
eth go and it goes right or even better
uh the USD value of that 0.01 eth and
then maybe the 0.01 eth underneath it or
something like that but if I if I try to
send this right now with a 0.01 it's
going to give me like a big int error it
just doesn't like that right developers
need to remember and this is why we put
it into scaffold eth you have to hit
this button and you have to take it
times 10 the 18 and then you hit send
and there we go we made a transaction
and what I wanted to show off was if we
send in money it should set this premium
flag to true and it did it's true now
right and if we zero that out and send
it again does it does it zero I don't
even know but we can test our
assumptions we can just try it and see
what it does yep so now premium goes
back to false okay so let's write a
quick little smart contract app and
specifically I want to show you the sort
of like core game Loop that you'll get
into with scaffold eth and that's
basically uh let's get out of here
you'll add some thing right like what do
we want to build do we want to build uh
let's do I like the the idea of the
beneficiary that one I I I've got this
like prediction like simple prediction
Market that I want to build but I
haven't like fully thought it out and I
don't think I should just figure it out
on stage so I think what I want to do is
do like a beneficiary and set it up so
the beneficiary receiv some money and we
have like a little front end where we
can update the beneficiary just set
something in a smart contract and that
whoever that beneficiary is will will
make the money okay so we're going to
have a public
address Ben oh look at that thank you
beneficiary okay and it's set to the
zero address right now if I were to
deploy deploy
this it's going to be the zero app that
is the beneficiary but we do have a
beneficiary now but it's the zero
address right so let's start that off
with I think I'm going to do uh let's go
to address vision atg I want to make
this guy the
beneficiary yeah that dude right there
okay and then I'm going to paste that
into the contract right
here there we go okay so now we have
this beneficiary and we're going to need
probably some function that lets us set
the
beneficiary and let's make
that we have this owner I don't know
we're just going to make this public so
this is another thing I do sometimes
when I do these demos is I make a very
insecure app and deploy it to production
and I think I'm probably going to do
that here basically I'm going to let
anyone set the beneficiary and then I
could I could delete all this stuff
probably but I'm mostly going to leave
it but there's this withdraw function
here and in this withdraw function only
the owner can withdraw the funds and I
don't want to do only owner actually I
want to kind of get rid of this idea of
the owner and I want to require
beneficiary there we go man co-pilot is
on point all right so and then I want
the beneficiary to get the
money okay and let's go test it out
right like I just made some changes to
the code and like this is a smart
contract that's going to be moving money
around and I want to be a little bit
more confident that I did the right
thing there so that's what this like
core Loop is about is like testing those
assumptions I've said that so many times
I need to come up with a new phrase uh
but let's go set or let's go set the
beneficiary to now watch this uh
scaffold eth has these components
components out of the box like this
address input field which are really
nice because they do ens uh resolution
ens avatars you got the blocky you have
the address but let's see what happens
there okay I was able to set vitalic as
the beneficiary and I think I can set
anybody right I can do at.
e and hit
send basically anyone can set anyone as
the beneficiary and then whoever is the
beneficiary let's set this dude to the
beneficiary for some
reason send now someone should be able
to hit withdraw and pull the money out
right so let's say a bunch of people
came in here and said hello world and
they paid
point1 and they hit the button and they
send it right and now the smart contract
actually has money in it right there's
$32 sitting in that smart contract now
and we just want the beneficiary to be
able to get in here and hit withdraw and
we want to make sure that money
disappears and shows up over here I
didn't watch very closely but I'm going
to assume uh no let's not assume let's
figure it out let's let's let's prove it
real quick uh let's set another greeting
send some more money in so we're at
withdraw I'm watching here what like
that decimal right there right we got to
make sure that yeah 99 okay good so this
is not an exhaustive test right you want
to build a whole test Bank to make sure
uh this thing does what it needs to do
and there aren't any weird edge cases
where you're going to lose money or get
money locked up but in terms of our
little smart contract I now am able to
like keep track of some beneficiary and
anyone in the world could set that
beneficiary and when they come in only
the beneficiary is able to withdraw the
money and it goes to
them it's a simple little app uh you you
guys are the solidity developers you'll
spend more time building things uh I'm
going to build a silly little example
but this you're deploying an an always
on app that will last forever Poss
longer than you and it's uh you know
nation state level hardness so don't get
thrown off by my silly little examples
like there's there's world changing Tech
here and uh sorry for my simple examples
but we're just going to build like this
little beneficiary system okay so it's
sort of working it does what we needed
to do I can set the
beneficiary uh there's some other
functions here that I'm just going to
leave the beneficiary can do the
withdraw what I want to do now is go
start working on the front end so just
to recap the the beginning of this is
about tinkering with your smart contract
and putting in some some solidity here
and then testing it out over here in
scaffold eth uh in this front end in the
de debug contracts Tab and you'll do
that for a lot longer than I did I'm
kind of like time boxed here to a short
window uh but you'll uh
you'll get in this mode of tinkering
with solidity and getting things things
right here and that will take longer of
course but once you've got it and let's
just pretend I do let's pretend that I
have built my whole app I've tested it
it works great it's very secure I'm
about to put it on a blockchain forever
uh and it's awesome I'm gonna actually
take this import out too I hate
deploying that on chain and paying for
it let me take that out here there's
there's some nice console log debugging
you can do with with hard hat and
that'll spit out over here whenever a
console log in your code you'll see it
over here in your blockchain and really
nice for debugging especially when
you're like why isn't this decimal
working I thought I thought I could do
that yeah okay I just wanted to take
that out and redeploy let's see if
everything's happy
here okay we're happy so you'll spend
more time on your smart contract I just
did a quick smart contract let's pretend
that it's all good to go now we're
thinking about our front end what do we
want we have this beneficiary and we can
set the benef benary and we can withdraw
I think I want some kind of front end
that lets me put in an address and set
the beneficiary and then another address
and then another button underneath that
that lets me like withdraw the money or
something like that so we're going to
read and write from the chain in our in
our front end and let's go let's go
start working on that so this is kind of
phase two you're starting to your
contract is pretty solid you may come
back to your contract and add some
events in maybe add some read functions
but generally the functionality is
working you're good to go uh so most of
the time now we're going to be over here
in react land and normally I would
definitely just prompt GPT I would not
be writing this code uh but I feel like
that's kind of like lazy like I don't
think it's I I it feels weird to be
prompting GPT in front of 30 40 50
people and be like bro please full full
files only like I feel like that uh that
is a weird experience to do in front of
a buch of people so it still makes sense
to for me to maybe just like Live code
this thing rather than ask GPT but if I
was at home and it was just me I would
be uh yelling at the GPT to get it to
work and not actually writing my
components myself but we're going to
write them oursel and we're not actually
going to write them oursel I'm going to
go to the docs and I'm going to copy
paste so scaffold e we go to the docs
there's this tab over here called
interacting with your contracts and
there's external contracts too but
interacting with your contracts is kind
of the first thing and here it is
there's here's how you read from your
contract and here's how you write to
your contract and this is using wagm so
you could always use wag me from VM and
look at their docs and go learn some
things uh We've wrapped it slightly
because scaffold eth handles some wallet
stuff and other things so it's it's
using the use read contract from wagy
but we called our own function use
scaffold read we just it takes a couple
less arguments and we fill those things
in for you it's a simple piece of
exraction but we we think it's the right
right move okay so what we want to do is
read from our contract we have this
smart contract that's keeping track of
this beneficiary and I want to display
the beneficiary on my page okay and so
far all we have is the connected address
oh shoot I got to go show the page so
we've all we've been on debug contracts
the whole time but if I hit home here
this is going to take me back to the
page and I've cleaned out all the stuff
that was here so now it's just down to
this and let's see what's
uh welcome
to this is going to be called uh I don't
know Devcon Devcon app 3 con app
three uh the Benny Benny fiary Benny
fiary oh man I didn't spell it right
come on help me a r y did I get it oh
there we go thank you okay and now that
should change over here there we go okay
and it's showing us our connected
address uh has that little blocky and
everything but now what we want to do is
read who the beneficiary is from the
smart contract and I've got that piece
of code copied already so I'm going to
bring it in right here and paste okay so
this is where I was talking about it's
really nice because scaffold eth knows
about your contracts so as soon as I hit
uh one of these buttons here uh let's
see I think I just open the quotes maybe
it's going to
start it's not which button is it
hm it should
autocomplete to whatever the value is in
the contract something is not right
let's see oh we need to import it here
we go let's try that is that what's
happening basically when I open this
quote it should give me there we go
that's what I want so this little list
is the stuff from my smart contract so
as I'm banging away on that solidity and
I write out my smart contract it knows
about all that stuff and it can set it
here so so instead of going to the smart
contract and being like what's that
variable I want to read I'm kind of in
line just like oh I'm going to your
contract and then I want the beneficiary
and I don't think there's any arguments
and let's hit save and then uh we want
to name it
beneficiary okay and it's yellow because
we're not using it yet but let's go down
here and put a div o what what was that
I like that yeah okay but I don't want
to use the address component yet I want
to show it off raw first and then it
will help us understand what we want to
do next okay so now we should be reading
from our smart contract whoever that
address is that is the beneficiary and
we should be displaying it right down
here let's go look and see how that
looks oo looks good right almost it it's
working it's displaying the beneficiary
but this is kind of a gross it's kind of
like a full address a full hex address
kind of ugly looking what you'd like to
do is do ens resolution and a lot of
things like that so what you do is
instead of just doing beneficiary like
this you wrap it in an address component
and this address component comes out of
the box with scaffold eth there's an
address and an address input and a few
others and I can show you in the docs
where to find those if you go to
components here there's all those uh
handy components and uh to extend that
we have an extension system that uses a
lot of other components like the like
onchain kit from Bas so if you wanted
like a swap component you could use the
extension system to bring in the onchain
kit and just add that in too so we have
like lowlevel components and then the
extension system will have like some
nicer level components and uh Kevin
Jones will show that off here in a
little bit when I get done speedr
running this okay so how is our front
end looking let's
go we have oh doesn't that look so much
nicer let's let's do that again so
whoops so this this is like at the eye
doctor you know number one or number two
number one number two doesn't that just
look gross and then when we do just this
quick change and we hit save and this
looks so much nicer I love it okay so we
are we're displaying who the beneficiary
is and we know who the connected address
is and then okay now we need to uh let's
see we want to write to the chain and I
think maybe we
could maybe let's just make a withdraw
button first I think that's the move
that's the move so let's go back to
scaffold eth docs so now we want to
write to our contract we're able to read
from our contract but now we want to
write to our contract so what you do is
you set up this like async contract
writer and that goes in with your
hooks there okay and that's going to
talk to our contract it's already named
your contract o we need to install
it okay and then write your contract
async Okay so we've got this object now
that we can write to so then here is a
button I'm going to copy that button
exactly and I'm just going to use it and
let's go down here maybe set up like
some
divs uh let's do a div first there we go
then the button then hit save okay so
what is this doing it's writing to the
contract and it's calling set greeting
so we don't want to do the greeting
though what do we want to do we want
to call what I don't even know what set
beneficiary set greeting withdraw I
think we want withdraw let's go with
withdraw okay
and then there's no arguments or value I
think I can Trash both of
those and let's see call this
withdraw and hit save and let's see if
we have a button in our app now whoa get
out of here yeah cool now we have a
withdraw button man my front ends are so
ugly scaffold e does as as good as it
can to like make this look nice but I
just tear it up and it looks terrible
okay uh can I hit withdraw here it can't
because I'm not the beneficiary right
right because Austin Griffith is a
beneficiary I need to set this dude as
the beneficiary and we'll make some
front end to do this but let's just go
do it in the debug tab real quick just
to test that this withdraw function
Works yep it does Okay cool so now we're
reading and writing from our block from
our smart contract right we kind of
tinkered around with our smart contract
in phase one and we kind of built the
app that we wanted to build in terms of
the solidity like I said you might come
back and add some events but you're
pretty much done there then we kind of
move over in the front end land and we
start tinkering with how we want our
front end to look we've read the
beneficiary from the smart contract
we've used wagy to tell us who the
connected address is and then we've
written to the the chain with this nice
withdraw button here so the last thing I
want to add here is a little address
input field that lets you put in a new
beneficiary and save them and I think
let's see how am I going to do this
maybe down here let's just make another
div down here it's kind of weird
uh let's see I will want no I want an
address I'm just going to go copy paste
it from the docs just go copy paste it
here we
go normally I would uh prompt the AI
with like examples and just have it
write it all for me but let's do it this
way I want address input okay so I want
to
grab this okay it looks like there's a
state oh yeah yep I want all that I want
that right there so you have some kind
of state over
here Boop and then you have your address
input right here on change it'll set the
address okay let's see how this looks do
I need to install this yes I think I do
let's see how we're looking let's see
what our app looks like
now uh oh uh oh Ed State we've got use
state is not defined we need to go to
that Ed state from react and make sure
we import
that
oh open Apple period there we go react
bring it in let's go let's go all right
how's our app looking now o there we go
okay there's a semicolon floating around
there I don't know what that is I'll go
get it in a second but now you should be
able to type in vitalic doeth and you
should get that nice ens preview you
should get boy I need some padding this
this this app looks
terrible uh how do I do that maybe some
like class
name yeah oh we might even Center the
div what does that
do oh wow yeah okay let's get rid of
that weird uh semicolon too I don't know
where that's coming from uh right here
we don't need that okay and I kind of
like this class right here I'm going to
bring that and I'm going to give that to
all these other divs just so this thing
starts looking a little bit better one
you one for oh maybe oh oh oh maybe we
do let's do a div here and do that class
name yeah and then close the div here oh
I think it tried to close it for
me the AI can just write code better
than I can I just I shouldn't be doing
this there we go doesn't that look nice
H we need a little padding but I'm going
to I'm going to go with it boy this is a
really ugly front end okay so we have
the withdraw that's working uh we have
the address input that's working it's
tracked in state I think what we need to
do is one more right function where we
uh set the beneficiary so we're going to
need one more right function I'm just
going to copy paste uh actually that's
all good I can just use that right async
so let's go get another button from the
docs oh here I have it right here I'll
just copy this button
here right this dude
okay H I'll take the whole
div okay and we're going to put another
button underneath this and this is going
to set the
benary and then for the function we
need set
beneficiary and there we go it wants to
give us some args that's what we want is
address the thing that we're keeping in
the state it is okay I think I think we
might be happy let's see what we have
here okay well it looks ugly but let's
see can we set vitalic as the
beneficiary boy a little padding would
go a long ways there yeah it worked
right now vitalic is the beneficiary all
right let's try that again
uh but if you're not let's go back and
do atg doeth again set him now if I hit
withdraw it should fail right because
I'm using the burner wallet yep not the
beneficiary okay
cool
um just want a little padding here it's
just driving me nuts let's see
p yeah there we
go there and
there how's that look yeah that's a
little better
it's still
ugly okay and and another thing we might
do is only display the withdraw button
if the uh connected address is the
beneficiary like we should probably only
show this withdraw button if these two
are the same address and here's a great
chance to just prompt the GPT to do this
but we could say something like uh
please only
show the withdraw button if uh let's see
what do we have if
beneficiary
is equal
to Connected address right there we go
let's
go yeah thank you and then it's just
going to give us the
code and we apply that and save and
let's go see now let's test it out okay
so it looks like that withdraw button is
gone now that's okay but if we set us to
beneficiary does the withdraw button
come back that's what we want to test
yes it does all right GPT you got on the
first try thanks bro all right awesome
so this is kind of we're we're nearing
the end of phase two basically we've in
phase one we worked on our smart
contract we tinkered with it we went
back and forth we got our solidity right
in phase two we did a lot more react
kind of getting our buttons things wired
up or reading and writing from our smart
contract phase three is now deploying we
want to put this thing out into the
world and to do that we'll have to
deploy both the smart contract and the
front end so to do that we're going to
need to yarn generate and yarn generate
will create a deployer account so you
don't you want to be very careful with
these deployer accounts you really don't
want to be like copy pasting private
Keys around they really should be like
living encrypted on your box uh so so so
when we generate this account this is
like a one-time use account basically
like I'm only this this account should
only ever have enough money in it for me
to deploy this contract once or twice so
there's my uh address then I'm going do
yarn account to show
it okay there we go and now I'm going to
send some money in there and we're going
to put this thing on a live blockchain
let's go okay let's see I'm going to use
a punk
wallet uh app built with uh scaffold eth
Let's see we had it on optimism
yesterday Bas let's see if I have any
bass in here I think I'm going to deploy
this to Bass okay so I just select base
I scan my QR
code and I'm going to
throw uh dollar at it right it should be
enough shouldn't be too expensive oh
time to retweet shutter block I got
you yeah let's
go re retweeting on stage okay so
hopefully I just sent some money here
actually yeah I did okay let's do yarn
account and it'll even like give us our
balances on the different accounts in
his base in there
somewhere Local Host arbitrum let's just
see we're hoping I have some base in
here
somewhere ah there's only oh there it is
yep we got some we have
one-time use deployer account we've put
a dollar in it and now I'm going to do a
yarn deploy just like I was before but
instead of yarn deploying locally I'm
now going to do the dash Das Network and
I'm going to go with base this time now
hopefully this works but let's see what
if it complains about
anything we may just put a smart
contract out on a live
Network that's looking pretty good y'all
Okay cool so our app though still says
hard hat up here we need to get in and
change our app over to Bas and what that
means is the whole app is going to
change networks so right now if I click
on this dude's address it's going to
take me to a local block Explorer which
is cool and nice for local debugging but
this is also really awesome as soon as I
set this thing to base then all of my
address components all throughout the
app will now link to the Bas scan block
Explorer let's do that real quick so I'm
going to hit open Apple p and find this
scaffold config and from the scaffold
config I'm going to change it right here
and you can even do like a comma
separated list here you can have
multiple networks like you could deploy
your smart contract to optimism and Bas
and let your users pick which one they
want to use even it's pretty nice uh but
we're just going to go with Bas now
watch this as soon as I hit save here
the whole app now switches over to Bass
and it doesn't let me use burner wallets
anymore and that uh faucet is gone right
by just setting that one thing from
Local Host to base your app now knows
that it's like oh we're you know it's
it's time to sit at the big kids table
we're going to go use like our real
wallets and real money here and let's do
that okay yes there we go okay so we are
now talking to our live contract on base
but we're still at Local Host so a
second step that we'll get to in just a
second will be to deploy that Li the app
live to forell uh but first let's just
Tinker around and make sure everything's
working uh on chain correctly uh so
let's see can we set vitalic to the V
beneficiary real quick just to prove
that we can and I'm actually going to
pay real money to do this right I'm
going to pay like you know a fraction of
a
penny no no more more like 32 cents
dang there we go but and now hopefully
will become the
beneficiary I'm going to hit reload I'm
impatient there we go cool and it's
working okay and our withdraw button
disappears too looks pretty good okay so
then let's I I don't know let's set me
back to the
beneficiary and then maybe let's put
some money in the contract and then
withdraw from it make sure everything's
pretty solid and then we'll ship our app
you know what actually I'm going to
start shipping the app now because it
takes some time so uh kind of the
commands if if we go through the whole
stack of commands here we did yarn
install yarn chain yarn start uh to get
your account we do yarn generate and
then yarn account uh and here we're
going to do yarn this is the best
command out of all of them versel YOLO
d-r like please do not check anything
just ship it and that's what we're going
to go with
yes got to do the Choose Your Own
Adventure here of like picking the and
the account and all that oo it's very
slow
no no Devcon
minutes to ship but now that it's
shipping it's nice because we can go
back and Tinker around with these these
few mechanics that we are worried about
here so can can I set me back to the
beneficiary take basically take control
back uh of the
contract and then uh let's maybe even
send some money into it right let's do a
greeting that says hello devc
con we nope I'm gonna do hearts hearts
hearts
classic hello Devcon hearts hearts
hearts and I'm gonna send in some money
and technically this money could be
stolen like anybody out there could go
to the smart contract set themselves at
the beneficiary and hit with withdraw I
don't think they'll do that but maybe
they will let's find out what
happens okay yeah $3 to be had if you
want to steal it you'd have to go find
the thing out on Bas scan or something
like that right like if we go look at
the contract here it's probably not even
verified yet but remember that contract
component all I have to do is click here
and it takes me right to the base scan
right the correct block Explorer for
whatever chain you're on and here is the
Smart contract but it is not verified
yet yep okay so I would need to verify
the contract before anybody is probably
going to attack it I don't think anybody
is going to figure out how to attack it
right now except for maybe you guys out
here which kind of have the alpha on it
so please come steal it like I I would
happily uh lose my $3 to anyone in here
who wants to steal it because that means
you guys are way ahead of the game and
really paying attention uh let's go here
uh Devcon hearts hearts hearts we got
money in here nope I need to S hit send
wait didn't I hit send there why isn't
there any money in here let's reload
this real
quick okay maybe I didn't hit send I
wasn't paying attention let's try one
more time Devcon no it's right there
it's right there hearts hearts hearts
premium is true oh man what if someone
already stole the money like it's not in
contract
what yeah someone did look at that look
at this address this is not my address
this is someone else's address someone
got in and got it right away wow that's
really impressive that's neat okay well
someone stole my
$3 all right all right that's that's
pretty awesome to be honest like I uh
that's really cool so that's like
probably like a a bot that's like
watching for contracts to get deployed
and looking at the bite code and man
that's really
cool ah I know don't even that's so cool
like I don't even I'm like thinking
about how like we could we could
definitely defend this right we could
set up a require statement here that
says only you know certain people could
set the beneficiary there is this idea
of this owner and we could say the owner
is the only one that can set the
beneficiary let's just do that let's
just do that all right so we learned a
lesson here about the Dark
Forest okay you know what I don't care
no we're shipping it this is this is
more fun like this let's just leave it
how it is the app is going everything is
good uh kudos to whoever's running that
bot and taking my $3 I'm probably going
to send them a couple more bucks here
for a little bit but check this out so
now our app is live and you can go to
versell and set up a domain on this
thing so within 30 minutes you can kind
of roughly crank out a smart contract
get a front end going and then deploy
the thing not just to base but also to
versel and there is a live URL so yeah
within 30 minutes we kind of built this
whole app and I'm going to go donate
another $3 to this uh attacker just cuz
uh I don't know that's that's pretty
cool let's see what are they doing let's
go look at this address real quick I'm a
little look at all those zeros oh this
is definitely a some
nerd they have how many is that that is
impressive yeah it's like an me bot that
has a bunch of leading zeros that is so
cool oh it's a contract we can know even
go dink around with it maybe
not okay anyways uh let's let's set the
beneficiary back to g.
e and let's see
if it like front runs me or what it
does that is so
cool uh oh here I have to I don't know
why I have to keep keep hitting this I
don't know if I need to like hardcode
the gas limit or something metamask is
just not happy with me with gas
okay and now hopefully I am the
beneficiary and it shouldn't it
shouldn't steal it right now right like
there's no Financial incentive for them
to set themselves as a benefici right
now what they want to do is wait until
there's money in the contract and then
almost like in a batch transaction set
themselves at the as the beneficiary and
sweep the money all in one transaction
atomically and basically like you only
do that if you wo Port man you only do
that if you uh like can make the money
right so the Meb bot is probably sitting
there like we're going to do all of
these transactions and we're only going
to execute them if it works and we make
money and if anything else goes wrong or
we don't make make any money don't do it
right so as soon as I put money in here
it's going to disappear again which is
pretty cool but not great but pretty
pretty neat uh let's see what man really
I feel like we could if a bot is that
sophisticated I might like start making
this as part of my like curriculum where
actually you like know that a bot is
going to handle something for you and
you can have them like be like rolling
the dice for you in some game or
something like that I'm going to think
about that okay here we go uh
uh oh please take my
money Mr all it could be Mrs too yeah
right right I'm GNA say miss m all
zeros all right
you right right it needs to be right
right so it's costing about 30 cents to
set the beneficiary right so then
another transaction maybe 60 cents like
it's got to be yeah within like a dollar
or something we did 0.00001 last time I
think and that was enough maybe we do 05
just to see let's see what this
does it would be really funny to like
calculate it just right and see like at
what point the bot takes
over but yeah here I go I'm going to
donate
another couple bucks to this bot
probably okay let's see there's the
transaction and does the money stay in
the contract or not let's see I'm
assuming it will be immediately swept
if Yep they're the beneficiary already
that is so cool oh man I'm going to use
this for something that is neat okay so
this is kind of the stack this is
scaffold eth this is how you can get
started building apps uh this is the way
you would go about tinkering with
solidity kind of in our first phase we
used solidity by example uh we wrote the
solidity how we thought we wanted it we
left it very very accessible and uh
attackable uh but you'll do a better job
of that when you're building real
contracts don't do what I do uh build a
good contract in phase one and then in
phase two we kind of built out the front
end and then in phase three we deployed
the whole thing so now uh I think I'm G
to hand it over to Kevin Jones to show
off extensions in a little bit but let
me just like pause here just to see if
there's any questions maybe we could do
like four minutes of Q why four minutes
four and no a couple minutes of Q&amp;A if
anybody has any quick questions and and
in the meantime I'll hand it over to
Kevin Jones and he can do the same thing
but he's going to use an extension
system probably graph or onchain graph
yeah that's what got got a sh got a
shell okay any quick questions yeah what
was
theoy the yarn command to deploy it was
yarn deploy Das D Network base oh the
versel oh yeah okay yeah and also this
is in the docs but it's versel it's yarn
versel colon YOLO space- dasr
and that's what uh shipped the app to
sale
yep yeah yeah yeah I did I'm pretty
impressed I like that means that someone
is watching base for contracts to get
deployed they're decompiling the bik
code and they're looking for attack
vectors where they can make money and
they're even doing this like batch
transa let's go see let's see if he
batched the transaction or not she it
could it could let's see where is
it yes you do so uh yeah so when you
deploy a smart contract to any live
Network the code isn't out there yet you
have to go to the block Explorer and
upload your code and then on their side
they compile it and make sure it
compiles to the same thing and then they
display the code so if I were to go look
at like
we what say one more time
explor the the block Explorer needs to
yeah so see how this contract has like
the green check and we can get in there
and actually like see the code for what
we how it
works yep yep so they have to verify
right because like they couldn't trust
you to do the verification you you send
you can send any code to them but it has
to compile down to the exact bite code
that's on chain for them to display that
code up here does that make sense
a free hosting service uh it's not free
I don't think it's it's just like a
really nice Cloud hosting service uh I
think it's probably less decentralized
we're a bunch of Cipher punks here and
versell is great for quick front ends
you can even like this code is all open
source and forkable so if anybody wanted
this code or to dink around with it they
could just deploy their own front end if
they wanted so like you could create
infinite copies of this front end so to
me it's like good enough decentralized
but also like you probably want to if
you're hardcore about this deploy your
site to ipfs also and have it live in
some kind of distributed storage that
people can access without even if
versell goes down you know you can have
that stuff pinned in ipfs but yes versel
is a hosting
service I think we pay for it build
Guild has a paid account but you can get
started probably pretty cheap lots of
lots of guys can answer that question
better than I can here too we'll have a
whole day of build Guild people here so
uh like come just come hang out and ask
ask him some more and we can show you
around for sure okay any last questions
before I hang it it off to Kevin
Jones I'll be up here again after lunch
and we're going to do speedrun ethereum
we'll go through your first five apps on
ethereum yeah what was your
question there is a verify command but I
think you have to have your API key and
I don't want to like go digging through
my credentials right now but if I do
yarn let me try it yarn
verify D- Network base let's just see
what happens here my guess is it's going
to say you need an API key yep I think
so there probably is some like Bas scan
API that I need to put into my config
but I don't want to go like digging
through that right now and expose like a
key in front of everyone uh
but I think yarn verify probably without
even anything on the
network I don't I yeah it's not going to
work yeah this is this is trying to do
it locally but yes yarn verify is the
command okay
how you guys feeling feeling good you
want to go let's go all right all right
thank you all I'll be back in a little
bit we'll be in this room all day today
this afternoon we're going to be playing
a CTF Capture the Flag it's going to be
awesome highly technical we're going to
give away prizes probably like thousands
of dollars thousand a thousand of
dollars we're going to also give away a
node we have a Precinct build Guild node
so if you go to client.
build.com we've
made our own build Guild client it
actually runs uh gu and Light house and
these exist kind of all around the world
and it's like this opt-in system where
you can become a distributed RPC for
build Guild uh but we're going to be
giving some of these away so you can get
a box from us and take it home and plug
it in and it's going to look like this
it's going to have W and Lighthouse
sinking automatically and lots of nerdy
desktop stuff okay thank you very much
we'll be here all day
thank you so much
oh hello welcome can you guys hear me
okay yeah seems a little low but that's
all right all right cool thank you guys
so much uh my name is Kevin Jones uh I
actually work in devell for the graph so
I work on the graph protocol uh which is
totally appropriate because I'm going to
show you guys the graph extension for a
eth and talk a little bit about the
extensions um I'm also core member of
the build Guild do a lot of workshops uh
with the rest of the crew here and uh
yeah so um if you that was an awesome
Workshop by uh Austin he covered really
all the basics of scaffold e so I won't
focus too much on that but we will talk
uh specifically about uh some stuff
that's on the on the actual doc site so
if we go to the docs uh there's a
section here for extensions so you can
come there uh it gives you some uh uh
basically like kind of overview of what
the extensions is you can have like a
GitHub repo with the extension
configuration and then you can just
execute it with this- e flag um and so
there's a lot of like Community
extensions if you go to I think it's the
build Guild website so if you go to
ble.com uh and you kind of scroll down a
little bit uh there's a section uh here
at least there used to be maybe it's on
the scaffold eth website actually let's
see yeah here it is so scaffold eth uh
there's a whole area here where are like
check out available extensions and we
did a hackathon I think not too long ago
so there's a lot of really cool ones
that have been built uh the very first
one was the subgraph one which is really
cool it's basically got a um you know
skaffold e one of the cool things about
it is it's this very local development
kind of environment where you're just
like able to hack away without pushing
anything to a test net and so the
subgraph extension uh is exactly that as
well we actually can spin up a virtual
um infrastructure of the graph on our
machine test our subgraph configurations
just all locally using hard hat so we're
going to show it off and so what it
looks like uh but there's a bunch in
here right there's one for Ponder if you
prefer that and then there's like erc20
as Austin said there's the onchain kit
which is cool it's got a swap extension
uh so yeah and you could write your own
we'd love for people to build on that um
if you go back to the docs and you go to
extensions there's a list of all the
available extensions that kind kind of
the we supported building uh that the
build Guild has supported but you can
also get the list from you know the
scaffold teth website and then here
there's an extion U an explanation of
how you create your own so I personally
have never created my own U it's
definitely on my to-do list but I think
it's pretty easy I think it's very
simpler to how you create a a package
with the npx command you can also do
that uh using this uh extension
development utility so you can come in
here you can either uh clone the
Repository or so you do need to clone
the repository which it's a special um
Branch here it's under the same scaffold
eth account but it's called Uh create
eth uh so you can clone that create eth
package install all the dependencies and
then run this kind of like build script
uh and then there's a CLI that allows
you to create new uh extensions so the
subgraph extens or the uh the extension
system is really cool um it really
allows you to kind of make these custom
reusable um uh environments all buil or
scaffold eth right so let's just take a
look at the the the graph one so it used
to be that we would have like a special
branch of scaffold eth but we're moving
away from that model right we're we're
moving to this extension model which was
designed by the core uh build Guild team
um and it's you know basically this
create eth uh extensions repository so
you can think of it this this way
there's the create eth package which is
the way that you install uh scaffold eth
with npx right uh um and then there's
the Crea extensions which is like if you
want to build your own supported
extension in the build Guild Community
you might do that so we have all of our
ones that we worked on here and uh you
know the very first one again was the
subgraph extension so if we come here
and go to the branch and and choose
subgraph there's this nice readme that
kind of explains it right uh this is
read me I wrote which kind of shows you
exactly how to set it up so anyone who
wants to follow along can do this but
I'm going to actually spin it up and
show you guys how it works
um show of hands here who is hacking at
hackathon few of you just a few huh um
okay so you know there is a graph Bounty
so one of the uh things I always tell
people is you could qualify for the
Bounty with this package um and use it
as kind of like a good starting point uh
who here has used the graph before who
who has used created a subgraph few of
you guys few of you who here knows what
the graph
does few of you some people from the
graph are here which is great um well
let me kind of preface it this way first
real quick because I think it makes
sense just to understand the context
this is not a talk about the graph but
it makes sense to why we would use this
graph extension scaffold e is like this
right it's got a front end it's got a
back end it's got all this cool
boilerplate code written it's got these
um you know all the proper packages you
need to build and create a a package um
or an app pretty rapidly um and it's
really the the quintessential uh way
that applications on ethereum have been
written pretty much uh since Inception
um but there is kind of like this like
missing Gap when it comes to reading
data from the blockchain now scaffold
eth is really good it has these really
cool like Hooks and uh be able to like
get the data that you need just if you
want to read it directly from the you
know uh RPC provider but if you want to
get like lots of data you know if you're
building a defi application or if you're
uh building something like an nft
platform with lots of users uh the more
users you have the more scalable your
data issue is so using something like
the graph is kind of like a a solution
to that problem so you can think of it
like this we're still going to use
scaffold eth but we're going to use
nextjs and hard hat and then in the
middle we're going to have this kind of
uh graph infrastructure so we're going
to like we're going to simulate this all
inside of Docker so the only difference
here is we're still using all the
packages that Austin used but we're we
have a a a layer that's going to run in
docker
so uh let's just spin it up so you guys
can see this is how you do it so you
just do MPX createe at latest and so we
do npx create D eth at
latest - e subgraph so same kind of
method we just use the MPX create eth
command asks us what we
want my internet connection Lo
did I do
something
uhhuh like like a
VPN oh tether oh I see what say I have a
tether yeah let's do this let's just try
VPN almost got disrupted right now that
was very scary I was like I've never
seen that error before Okay cool so it's
working now thankk you so much see build
Guild homies got my back all right so um
it's going to do the same thing it's
going to give you this kind of like
Choose Your Own Adventure method right
so we're going to do I don't know like
um uh Devcon sure uh hit enter and same
thing we get to choose a package we
support both uh I personally like hard
hat just because it's been around for a
while and I'm just so used to writing
the stuff in typescript but you might
choose Foundry like Austin said if you
want to write solidity tests it's the
way to go
uh or you might just not use the chain
at all maybe you just want to use the
graph for like doing some data stuff you
could do that as well um so it's going
to go through install the packages for
us um again it's going to scaffold out
an environment now Austin mentioned that
scaffold eth is this kind of like mono
repo right it's got the hard hat or The
Foundry and then it's got the nextjs
package well this is just going to give
us one additional package right it's
going to give us this additional folder
called subgraph right um and it's going
to lend that by going through and
basically using you know this uh where
is it right here using all the boiler
plate code that comes in here so if we
go to
extension and we go to
packages and we go under there you'll
see that there's this new subgraph
folder right so let's give it a second
on VPN is probably even a little bit
slower uh I'm using a cool tool called
t-mo just lets me split my screen up uh
this doesn't obviously need to be that
way um we can just do that in different
windows but let's do that so
Devcon CD Devcon okay cool and while
that's loading up let's just take a look
at the code because it should at least
be there for the most part okay so we
see this packages folder and then we see
there's an additional folder so in this
case we have this cool extension that we
can use uh called subgraph we can go in
there and we can start to see what's
available to us so it's the same exact
thing uh for scaffold eth we have the
contracts folder we have the same exact
sample contract and then on top of that
we have the nextjs folder with the same
exact code the difference is we also
have template in in some cool uh
additional code so an example would be
like in this case we wanted to have this
like subgraph uh route so uh scaffold E
uses um the app router functionality of
nextjs so we have this subgraph folder
and then inside of there we have this
dedicated folder uh or this dedicated
page with all the uh H the the the code
for the front end and I you'll see what
this looks like in a sec as soon as it's
done installing the packages uh it's a
little slow right now um and then let's
take a look at the graph so without
doing a full overview of the graph I
just want to kind of explain like within
a few words what a subgraph is a
subgraph is really just an API right
it's basically a uh an API layer for any
kind of blockchain data right it's this
middleware layer um and so we basically
want to create what are called subgraphs
to organize the data so just like we
have uh a contract here called your
contract and we have this concept of
updating the greeting which Austin
showed off right where you can like
update the greeting pay some gas pay
some value that greeting has an event
right so it has this basic event so that
event says who set the greeting what the
greeting was whether they paid some
value or not true or false and then what
that actual value was so this event is
kind of like what it's like a log on
ethereum right we want to keep track of
something and we probably want to
display that in our front end um so we
could just query that directly using
scaffold there's a there's a hook for
that if you go to scaffold E.O and you
go to interacting with your smart
contract there is a uh event history and
then there is also a watch contract
event so there's two two ways you can
get information lots of information or
if you want to just like watch all the
the events that come off you can also do
that so it's easy to get like small bits
of data but if you want to get like all
of the events that happened since you
deployed your dap maybe you want to get
thousands of events it's not effective
to use something like this because it's
going to be too slow right so uh we can
take this event data and as it gets
emitted off of the blockchain right here
right we can index it that's what the
graph is it's an index protocol right so
if we go to that subgraph folder and we
go to the subgraph configuration it it's
already pre predefined for us this
example comes with the network we care
about and the address of the smart
contract it also comes comes with the
concept of what are called entities and
again we're not going to go too far down
that rabbit hole but it's how we want to
store the data and then we have this
Handler and all of this stuff it's three
it's three files it's the configuration
file it's the uh SCH which is like how
we store the data and it's the Handler
which is like how we process the data
which is run runs an assembly script you
don't need to understand that stuff but
that's what a subgraph is it's those
three things created to process data so
if we want to write our own custom
subgraph we can um but we're just going
to use the one that comes with this
package for Simplicity we're not going
to change the contract at all we're just
going to show how everything works so
scaffold is done installing so let's go
up here let's go into the dev con folder
let's do yarn uh starts oh sorry yarn
chain sorry yarn chain yarn
start and yarn
deploy now the difference with uh this
package because we have a third um you
know package that we're using the
subgraph package we also want to have a
another window right so we still need
our chain we still need our front end we
want to do our deploys in this window
this last one is where we're going to
simulate the graph in Docker okay now
you don't need to know what Docker is
but uh Docker is basically a
virtualization layer that allows you to
Virtual run what are called containers
uh it's kind of like running virtual
machines but they're very very small uh
and so we're going to use the graph's
power or sorry the docker's power to do
that uh inside of what are called Docker
containers again you don't need to know
that but to do that all we need to do is
do yarn run-
so that's going to there's like a a file
that's on there called a Docker compos
file that has all the configuration
defined for creating a graph uh node on
your machines and all the infrastructure
you need so you need an ipfs node and
you need a uh database postgress
database so it's it's pretty much all
configured you don't need to change
anything so we're doing that now we're
spinning up everything inside of Docker
so you need to have Docker installed and
that's just one example of one of the
extension
I think it's the most relevant
especially if you're going to hack at a
hackathon and you want the graph Bounty
uh who who doesn't like bounties right
so use the graph graph one so you know
it's working um at least the graph uh
infrastructure is set up when it says
downloading latest blocks from ethereum
so we have right here so that basically
means that the graph node so graph node
is the the the thing that processes data
it's what all the indexers run it's a
rust based implementation of like data
indexing uh that is all running when
that says ready to download data's
blocks so so we have our chain we have
our front end we have the graph running
now we just need to uh deploy our
subgraph so we again we already have a
subgraph that's here and this subgraph
keeps track of all the events that come
off of the greeting and when those
events happen it takes in the data types
and it processes those over whatever
Network we want so this Local Host it
puts those uh data type ENT those as
objects or I should say values into a
database in a certain data type which
are these and it basically stores them
and makes them available via graphql so
that's the power of the graph is it
creates an API for event data which is
super
powerful uh and it does that using
assembly script mappings right and so if
you come into your this assembly script
we we see that nothing's actually uh
been generated yet so we need to
generate these types we use assembly
script with the graph which is a subset
of typescript so it's kind of like
typescript but it's a little bit more um
simple you can't do like Imports of just
standard typescript libraries needs to
be an assembly script library but it's
super powerful in the sense that you can
use the type safety of your Imports so
we need to generate these so let's go to
scaffold eth so if we go to scaffold eth
and let's go to the subgraph extension
by the way how much time do I
have any know no like 30 minutes 20
minutes something like that okay uh if I
need to stop just let me know all right
so this subgraph tab here is is this new
tab we get right because we're using
this new repo we've we've kind of
templated in uh some some code and so
now we can do some additional stuff so
you'll see on the bottom is I there's a
very basic me that shows you how to get
started so to spin up the the
environment you do yarn run node I
already did that to create a subgraph
you run yarn local create to deploy your
subgraph you do yarn local ship to build
out assets for your front end you run
yarn graph client build because we use
graph client and then to clean up the
database if you need to you can clean
the node clean node so it tells you
exactly what you need to type so let's
do that um we don't have any data in our
contracts maybe we make some uh let's do
some things real quick let's send some
greetings uh let's do uh yo
Devcon and send we don't have any funds
let's get some some value all right so
Kevin was here I'm just sending a couple
things so we have that thank
you cool so I've sent a couple things
but they're kind of like lost in the
ethos of like ethereum like how do I get
that data well we could use the hook
right to get that data but if there's
like thousands of of events that have
happened well it's going to be pretty
clunky right so let's use the graph cool
so the next thing we need to do is we
have the infrastructure set up to
simulate the graph we're going to do a
yarn local DC create like
this boom so that's going to uh create
like kind of like a a skeleton
environment for our subgraph that's just
like a very simple command you need to
type that once then we're going to
actually like generate the code build uh
the subgraph and then try to ship it uh
with a few commands so we do that by
doing yard local
ship so what this does is it generates
all the types for the subgraph it builds
the subgraph into a wasm module right
because we use wasm in the graph and
then it ships it to the uh graph node
instance and it puts all the stuff into
ipfs that it needs to and it creates a a
graphql API endpoint for you and it just
does everything uh using the graph
infrastructure and then it asks you what
what version you want to uh use as well
so just like you have versions in your
software your subgraph evolves over time
you add a new event to your subgraph
then you add a new version right so
let's do
enter it's going to check if there's any
errors in the code right if there was
like something missing that was not
properly generated then it's going to
give you an error but it deployed
successfully we can see here that the
graph is indexing data cool let's go
back so uh first of all we'll go to the
subgraph tab and there we go we get the
commands or the data here on the bottom
um I'm kind of surprised it actually has
the data already um if you make changes
to your subgraph you might have to
regenerate the types which is doing this
uh we use graph client which graph
client is like a front-end framework
it's it's similar to like Apollo uh or
um I forget the other one Urkle uh I
like graph client because it has it's
very simple you can do some interesting
things for like um um working with
graphql it's just a little bit more
optimized I think so we use graph client
so there's this additional command that
you might need to run to generate the
types but as you can see the data is
already there uh and so if we look at
that code real quick let's go to the ne
uh nextjs folder app subgraph there's
the main subgraph page and you'll see
here we create a table so we do this
greetings table which is down here at
the very bottom right here so we go to
greetings table and go to the components
of that greeting table here it is so we
use uh we're doing using some state
where we have this kind of uh query that
we do by calling a get creating document
which is probably somewhere in here here
it is it's just a graphql query so if
you're not familiar with graphql graphql
is like a query language that allows you
to query exactly what you want in a very
optimized way for front ends and so we
are using the graph for that and so um
we're using this kind of custom query
that gives us all of the data back in
one single HTTP query right instead of
calling the RPC over and over and over
and over and over again to get all the
events um we're just doing it in one
simple query and we're also getting uh
the greeting count and the address of
that uh of that person that sent the
greeting so we're getting a lot of
Advanced Data just with one query
right uh and so yeah so what else do I
want to show off real quick
so uh oh and also it's going to give you
this like URL uh which is right here so
let's grab that real quick real quick I
want to show that off uh so if we go
Boom time 12 minutes I have I have
enough time to actually probably go over
the subgraph config if anyone's really
interested or I can ask question answer
questions about extensions but let's
let's first of all show this off so this
is called graph iql graph iql is kind of
like this um way that you can like test
your graphql configuration so again the
graph uses graphql heavily right that's
that's what we rely on for people being
able to access the data in a in a
reliable way so if we click Explorer
here on the left and sorry this might be
hard to read but we can see that there's
these data objects that match what's in
our schema so these are kind of like
what's in the database basically so if
we look at this the graph graph qall
configuration for the subgraph and go to
the schema these are going to match so
in our case we have this greeter and so
we have greetings that happen and then
we have senders that send those
greetings and we kind of like build a
database for all that stuff and so all
this data is what we're storing in
postgress and exposing via graphql and
that's what you're going to see over
here is these these entities so if I
want to get all the greetings maybe I
want to get like the first I don't know
order them by the uh when they were
created and and I want to do it
descending and I want to skip over the
first 100 for some reason or maybe the
first thousand you know you have a lot
of flexibility here I want to know when
they were created what it was the ID and
I want to know who sent it what their
address was and how many they've sent
and then I can hit play and I can get
that data back that's not working oh
because I skipped over let's not skip
there we go so because I skipped the
first thousand there was no data but
here we go this is all my data so this
is a graphql query for uh that I'm that
I'm creating and this is the response
that I'm getting so what we're parsing
in our front on over here um sorry in in
here is the data that's coming back from
the Json response over
graphql
cool hopefully that wasn't too fast that
was good um so I can also talk a little
bit about the the graph C configuration
but why don't we like pause for a second
and see if anyone has questions first uh
about the extension system uh or about
the graph or anything that I uh talked
about right now so
far any
questions ber
ber no okay then let me let me talk
about the graph q a little bit uh the
subgraph configuration a little bit more
um definitely we we would love for
people to to build cool extensions so if
you're in the crowd and you are you know
working on a protocol that can take the
the scaffold eth and and create an
extension for it come talk to us we'd
love to hear what you want to build uh
and we can get it listed maybe on the on
the on the docs um but yeah please
please uh let us know if you think this
extension system is useful and like if
you would like to see any features or
any if you want to see a cool extension
built let me know uh but let me talk a
little bit more about the graph so
because I think it's probably the most
confusing thing of everything I just
talked about um but I want to cover this
part a little bit more because I didn't
really go too much into this assembly
script um one of the powerful things
about the graph is it allows you to uh
do some like interesting things like
during the time that an event happens so
the primary way we get data is events we
also have the ability to do what are
called substreams where we can get like
more block
data um but in this case uh the cool
thing about assembly script is again
it's a subset of typescript so it's
pretty easy to to to understand but
let's walk through it a little bit so
when we uh write our our contract just
like scaffold e generates the ABI right
to be able to interact with our uh
contract well the same thing goes for
the graph it needs uh the ABI as well so
we take the ABI and then we generate all
of the assembly script uh types that we
need and store them into these files so
in this case there's a generated folder
it has the name of the contract and then
has the schema types as well so how we
want to store the data so this is kind
of like how we want to read the data and
then this is how we want to write the
data right so these are the types this
other thing here is what we want to do
with the data so we use the graph TS
package to maybe we want to like um read
in addresses uh from the uh the thing
and store them a certain way uh in
typescript we need this like package
right so that's why in this case we're
using the big int package to do like
numbers uh to use big inss and so in
this case we only have one function that
the contract is uh sending and so we
have this ability to uh sorry one event
uh the greeting change event so we take
in the event here as part of the the
function right here greeting change and
then we create a a unique identifier for
the values of that actual uh string so
we do that by converting it to a hex
string then we try to load it in the
database so we try to see if it's
available if it's not available here uh
like it's like if it's the first person
Whoever has sent a greeting we just
create a new one right and then we
actually like set who that person that
that sent it is what the time stamp was
and then we do here this is where we use
the big int package to actually set the
value for the very first time as one
right so we do some interesting stuff
where we're actually storing the
greeting count off chain right we're not
storing it on chain so the graph is
really good for that because if you have
stuff you want to like process like defi
related uh metrics uh and you want to
like just store that in an easy to
access way that's where the graph is
very powerful and then if this person is
come in and send a greeting before well
they'll actually have a count of one
plus an additional one so it'll count
that and add that too right uh and then
the same thing goes for the greeting
like we do we create a an identifier for
the greeting create a new one using the
string the the hex string and then we
set all those variables for the greeting
the sender the premium the value the the
time stamp and the transaction hash and
then here is where all that data gets
saved so it's kind of simple um and the
cool thing about the graph actually if
you use the CLI it will generate all
this stuff for you so you don't need to
write this stuff but it's good to
understand how it works um cool all
right so uh I know it's that part's
probably a little complicated but at
least you guys get an idea of why you
would use the extension uh why you would
use the graph extension and yeah uh any
questions at
all there's got to be at least one
question come on no no
no
yes
person what is it that you most excites
you about this project and and the new
things that it enables scaffold e or the
graph the graph the graph the graph well
the graph is great because um you know
it really allows you to uh you know
improve the usability of the data from
the blockchain um and so you can build
some interesting stuff uh I think what
I'm most excited about is you know the
advancements that we're making in
indexing with like
substreams um and yeah just the the the
Network's getting the network is very
secure uh distributed decentralized and
we're like sticking very much to that
ethos right where we believe that
decentralized is super important uh and
so about I know was six months ago maybe
not that that long we used to have a
hosted service we've completely moved
away from that and everything is on the
decentralized network and we're we're
moving to continue that uh and and focus
on
decentralization so thank you yep thank
you cool we got four minutes any other
questions yep back there let's get your
mic uh back there green sweatshirt
okay so first one uh maybe it's because
I don't know the graph and so on but you
can run mutations like in graphql or
it's only for indexing data and fets
from uh the blockchain sorry I missed
the first part can you say it again yeah
in graphql you can do querium mutations
and here in the graph you are able to
run mutations in the same way or
computations yeah yes okay yeah yeah you
so you can essentially do like there I
mean I'm doing like a plus or I'm just
adding some stuff uh there's time series
data you can do with the graph where you
can like have like uh something happen
over a certain period of time and
aggregate um so there's some stuff you
can do automatically with some some base
stuff but yeah it's more yeah you can do
computation you just can't do like you
can't like it's not an oracle where you
could go out and like fetch some
information and get that back um it's
just stuff that you can do locally
inside of assembly script and process
and store okay and the second one uh how
much uh is autogenerated by the Avi is
only the the types from the schema or
also in the Handler we are
autogenerating on yeah so if you use so
that's a good question so the so the
thing is it won't generate the the T the
it won't generate all the assembly
script code for you it will just
generate the types but the CLI like the
graph CLI if you go to the gra.com and
install the CLI that will read in all of
the types and then build out a very
basic kind of uh one for you okay thank
you yeah good question
cool any other
questions no awesome cool thank you guys
so much for coming uh we're going to be
here uh we might take a small lunch
break I think soon and we will be back
here later so thank you so much guys
appreciate
you I think uh they do have a Q&amp;A here
where you can scan this QR code and ask
questions so if anybody wants to you can
scan this QR code and it's going to show
up right here on the screen so feel free
to ask more questions here but we're
here all day and if you find any of
these black shirts you can ask ask any
questions I think now we're going to
take a break though right it's a lunch
break time is that
right if the QA shows up we'll answer it
yep yep yep yep yep if questions show up
here we will answer them uh but yeah
don't feel too what stress to do that
the the key is we will leave this up for
and I think next after this is a lunch
break and then we'll be back and we're
going to going to do building your first
five apps on ethereum and then the CTF
will begin sometime around 2:30 I think
we're going to start the CTF and there's
thousands of dollars in prizes we're
giving out a node it's going to be
difficult though it's going to be a hard
challenge it's easy but then it gets
harder and we'll we'll explain more of
that this afternoon but uh yeah feel
free to ask questions we'll be here all
day go have some food come back in an
hour or so do we know when we start back
up again
be building your first five apps on
ethereum possibly maybe even Eda will do
a presentation yeah some of this oh
we've got a PO app here come come scan
this to get a PO app yeah but thank you
very much we'll we'll see you guys
around we're we're here all day thank
I
oh
e e
all
pap
he
yo what's up I'm Austin Griffith thank
you for coming to the afternoon session
I've done a bunch of uh morning sessions
we built a bunch of things already uh
we've done too many scaffolding sessions
already and this is going to be another
one we are definitely like wailing on
this uh beginner to intermediate content
if you are a builder uh go to speedrun
ethereum to learn how to build on
ethereum uh this will help you with your
first five apps and we're going to
speedrun the speedrun today I've uh
written a bunch of code this will
probably be a little less code writing
and more just like going through the
tutorials and talking about some of the
AHA moments you have along the way uh
just uh like Zoom all the way out we are
the build Guild uh we are focused on
developer education and tooling our main
tool of choice is scaffold eth and we
use that to build a bunch of things uh
but that is also the heart of speedrun
ethereum which is our curriculum and
we're going around the world teaching
people how to build on ethereum and
anybody can just go to speedrun ethereum
and get started today and we're going to
kind of just speedrun the speedrun today
I'm going to go through the challenges
and just kind of talk through the kind
of the AHA moments you'll have but
hopefully you can go home and spe
speedrun ethereum on your own time and
really kind of go through this at your
own pace but I'm going to go through it
quickly just to kind of cover like oh
here's you know here's the stuff to look
out for basically uh let's let's do just
real quick if you guys could give me a
show of hands how many of you have
deployed a contract on mainnet before oh
yeah we got five or six mainnet deploys
all right how many of you have deployed
on an
L2 actually less I think right less
people okay we're going to change that
today for sure we got to get you ready
for that scaffold I deployed one to base
earlier and someone attacked it stole my
money it was pretty
fun okay how many of you are software
developers okay those look at those I
would say that was almost all the hands
oh I just got goosebumps I'm excited
okay this is awesome so I'm G to just do
the speedrun probably 20 30 minutes I'm
going to speedrun the speedrun uh and
then I'm going to hand it off to Eda and
she's going to do I think like an nft
build right cool awesome okay so um just
just in case you've missed me shiing
scaffold eth I've been shiing it all
week but it's a really great tool for
prototyping but also deploying to
production it's really nice because you
can make small changes to your smart
contract and those changes are sort of
represented live in your front end so
you add like a new variable and boom it
shows up in your front end and then say
you uh set up a require statement that
says only the owner can get into this
function and then to go test that
instead of writing and eventually you
will write lots of tests but instead of
writing all of those tests up front what
you can do is just create a burner
wallet and try it as the good guy and
make sure it works and then try it as
the bad guy and make sure it doesn't
work scaffold e gives you that
opportunity to try it and it it lets you
tinker and test your
assumptions okay but today we're using
scaffold eth within speedrun ethereum
and let's just look we're just going to
look at each one of these quests and go
through these then I'll hand it off to
Eda then we'll do a Q&amp;A maybe we'll do a
quick set of questions before yeah I'm
going to do that I'm going to do like 20
minutes then we'll do five minutes of
questions then Eda will take over then
there's like this Q&amp;A thing where they
put up a QR code and you shoot it and
ask like anonymous questions or
something but we we might get to that
too at the end okay so building uh on
ethereum here we go the the very first
tutorial kind of points out that you
probably need to have some solidity
already uh if if you don't if you're a
coder I saw all those hands there's a
lot of coders in this room it's
basically everybody if you're a coder
you can go to solidity by example or
just go to the solidity docs and you're
going to pick up the language pretty
quickly you're going to pick up the
primitive data types you're going to
pick up the mappings and arrays but just
like go through this and kind of learn
these Concepts uh for instance ether
verse way is a thing that we'll talk
about today um there there's a few other
just kind of like aha moments you have
but you got to first get the syntax and
so you can get the syntax from the docs
or you can get it from solidity by
example or you can just prompt cursor to
write it for you too okay so uh that's
the basics um also there's a web two to
web 3 Series that can help you get your
wallet ready and do some of those you
know first beginner actions uh you know
what how many people have deployed to a
test Network so the main net was to okay
okay okay yeah that's like 50 60% of
people have deployed to a test Network
that's really great okay so with that in
mind I'm probably going to double
speedrun the speedrun and I don't want
to like bore you guys too much and we
can really get to to the heart of
building something with with Eda and
then after this let me make sure I Shi
this uh the live stream will actually
shut off and we're going to do a capture
the flag and knowing that there are so
many good devs in here already I would
recommend sticking around uh it's going
to start at 2:30 and it's going to go
till 5:30 there's going to be these 12
Flags in this nft contract that you'll
mint uh we're going to give away $1,000
in eth to the winner $500 second place
the prizes are here uh yeah there we go
but we're also going to give out we have
fully synced uh ethereum nodes we have
this thing called the build Guild client
where you can run a build Guild you can
run an ethereum node with a single line
and then we've been syncing nodes
ourselves and we bring them these events
so the winner will win a fully synced W
and Lighthouse node not not a Staker
like it doesn't have 32 eth sitting on
it but it is a node that you can like
run an indexer against or something like
that uh also also uh if you uh are
interested in running one of these nodes
we're looking for more node Runners uh
specifically in South America Africa and
Southeast Asia we only have a few of
them here and we're trying to get these
numbers up so come come talk to me after
if you might be interested in running
one of those you might just get a free
node that we send you we don't have that
many but we have a few that we synced
and we brought we'd love to get some
some more participants but that's for
the CTF that starts in a couple hours uh
about an hour and 10 minutes but first
let's speedrun the speedrun at speedrun
speeds so the the very first challenge
that you'll take on with scaffold eth is
just a simple nft contract you don't
even have to write any code it's more
about just getting your environment
calibrated you'll clone down this repo
you'll CDN you'll check out that first
Branch I'm going to uh bring this up
because I want to start looking at this
stuff in git I want to have that up but
it this one's super simple and it kind
of goes through some of the um basic
concepts that you get from scaffold eth
for instance burner wallets uh you've
probably heard me talking about burner
wallets if you've been to any other
session but they're really great for
local development if you're building
something locally and you need to make a
bunch of transactions it's way easier if
you have a local burner wallet and just
every time you hit a button it just
makes a transaction and you don't have
to like have the popup and have the
chain ID set with metamask and all that
stuff so burner wallets are another one
of our little secret superpowers built
into scaffold e and it has you you know
go to the faucet load up your burner
wallet and then I think it has you even
like send it around right in scaff E you
can open up multiple windows and since
that burner wallet has a private key in
local storage you can open up uh
incognito window and it's like a whole
new account so if you ever need like a
bad guy to try to see if he can you know
do something in the only only owner
block of your code you just bring up a
burner wallet fund it and then go try it
and then you go to your good guy and
have him run and make sure it it works
for them works for the good guy fails
for the bad guy right that's that's how
uh burner wallets are really handy built
into scaffold eth so I think what you do
is you get in here you uh go to the
faucet and you get some eth and then you
go ahead and mint these silly little uh
little animals and then it has you send
them around so you'll create another
account and you'll send one of the nfts
to the other one and you you just kind
of it's really nice it's like this it's
it's like a Goosebumps moment when you
like hit send and it disappears over
here and then a little Buffalo pops up
over on the other one it's a lot of fun
then it'll have you deploy it to I think
sapoia or maybe even Bas sapoia optimism
sepolia something like that Yep looks
like sapoia there yep and I think
there's even a second test net on this
so you don't have to use theoa I think
we have a second I think it's base theoa
but I don't know yeah I don't know and
there's some side quests here but that's
the the first Challenge and then what
you'll do is you'll hit submit challenge
you'll put in your site so you're going
to deploy a live site that lets people
mint nfts on sapoia and you can run
through this pretty quickly like a a
good Builder could run through this
first tutorial in like 20 minutes
probably so if if if you're a decent
Builder you can probably dive in and
actually like put an app out live with
within an hour so you'll put the app URL
there and then you'll put your smart
contract URL there and we have an autog
grader so the autog grader it it goes
and it I think it downloads your
contract and runs it or maybe it goes
and talks to your contract on sepolia
and makes sure everything works
correctly so each one of these
challenges are autog graded with like a
testing system so you can kind of like
level up as you go through each
challenge not really a whole lot of aha
moments here it's more like we're
building up the the base knowledge right
so let's go to the next challenge and
that would be the oh no NOP go to go to
challenge one and yesterday I went
through and built uh this one fully uh
during a video you could go look back at
that one from yesterday I think it was
maybe called the same thing as this uh
but yeah if you go to the Devcon
schedule search Austin it's going to be
like the second video there and I go
through the the staking app uh but let's
let's speed through it right now just
kind of looking at it so I think this is
probably the most uh this is the most
important challenge uh not I I would say
the decks is the most important
challenge but this is the the real like
heart of it this is the beginning of
like figuring out what kinds of things
you want to build on chain and and what
kind of things like belong on chain and
I think a real aha moment you know
you're you are deploying these apps that
live forever they have nation state
level hardness neutrality but it really
starts to make sense to me when I think
of an adversarial group of players
trying to coordinate they want to
coordinate maybe uh in this case what
we're going to do is we're going to get
everyone to pitch in like 0.1 eth and if
we get enough eth put together then
we'll be able to go do this second
action like go buy this thing or invest
in something right and what you need to
do is build the smart contract in a way
that they can't grief each other they
can't steal each other's money but if
they do choose to coordinate they can
coordinate and I think that's a really
powerful mechanism and so uh you'll
you'll write this Staker doou and you'll
build a stake function and you'll allow
people to stake money into your contract
and you'll need to keep track of each
person's balance because if they don't
end up coordinating correctly then
you'll have to refund everybody and you
need to allow everybody to be able to
withdraw from the smart contract so
that's kind of like starting to sink in
like what kinds of things you might be
putting on chain this is kind of like a
coordination mechanism with people that
don't totally trust each other it's
slightly Financial but doesn't have to
be uh but you have to write all these
rules and I think one of the first aha
moments for me is that none of this is
automatic it's when you think of
blockchain or Dows and autonomous agents
you just kind of think that there's like
this magic thing that is handling a
whole bunch of things in the background
and it certainly is a magic technology
but to make something happen on chain
someone has to make the transaction
happen it's it's not like the smart
contract is working in the background
and and and doing things right the smart
contract does what it's supposed to do
but someone's got to make a transaction
against the smart contract to get the
the the thing to work so in this uh
particular build you're kind of building
a state machine if we want to imagine uh
a a state of so there's this open Period
right and there's at this point anyone
can state anyone in the world can stake
in in this in this open Period and then
at some threshold or I'm sorry at some
uh time maybe timeout I don't know what
do we call it here let me make sure
deadline so at some deadline you need
basically the contract to be ready to go
into the next state so you sort of have
this open staking period and then at the
deadline you set up an execute function
that checks to make sure that the
deadline has passed and that no one else
has run execute yet and then in that
execute function we need to check and
see did we get enough money in the
contract so there's an open Period
people are yoloing in money we have some
threshold that we need to get to and
some deadline of time that we need to
hit and once that deadline of time is
hit someone's got to poke the thing and
if they hit the button or they make the
transaction and there's enough money in
the contract we move into kind of what
we'll call the Happy State where the
money actually gets invested wherever we
wanted to go in this case there's just
like an example contract and it moves
the money into the example contract and
calls a function on it but that contract
could be anything you're kind of just
imagining that that is something more
advanced maybe you're buying an nft or
something more fancy but so you're open
State you hit the threshold or you hit
the deadline you check to see if the
money is above the threshold and if it
is then you're in the Happy State you
move that money into the contract and
you trigger the next thing
but if you didn't get enough money
together then you need to kind of go
into the maybe the sad State or the
withdraw State you some people have
already YOLO money in and you didn't get
to the threshold so you need to
basically you have this open for
withdraw and the open for withdraw will
is is kind of another mode and that
means anybody who has put money in and
now that we didn't get to the threshold
and now it's withdraw time now they can
get in and withdraw their money back
basically and that's that's kind of how
these apps work right they need to kind
of think of it like a state machine you
need to make it so uh we're not sending
the money back to everybody they have to
get in and withdraw it right because
there's gas involved with that and we're
not going to run that system so that's
that's kind of the best the best like
quick first build in ethereum like this
this will be I guess if we call the nft
app your first build this will be your
second build and this build is really
going to start Illuminating the kinds of
things that you want to put on chain uh
I think you end up putting it out on
yeah sapoia and you basically deploy a
staking app and uh you learn learn along
the way so the next challenge is the
token vendor this will be your third app
and the token vendor uh really leans
into erc20 tokens uh if you uh have ever
Meed an erc20 token you know that
there's this transfer function but
there's also this approve function and
when you want to actually send a token
into a smart contract you don't just
send it and it does stuff you actually
do this really weird thing where you go
to the Token contract and you approve
the smart contract to take the money and
then you make a second transaction on
the smart contract that says hey I've
approved you to take my money please do
so and then do some other things and so
it's a kind of a complicated thing to
get your mind around at first but that's
what you'll do here you'll build you'll
deploy your own meme coin coin basically
and then you'll make a a vending machine
smart contract that lets people buy that
token at some exchange rate you'll say
maybe a 100 tokens per eth and then they
get in and YOLO some eth and then you
send them some tokens it sounds simple
but it's actually pretty tricky if you
think about the different transactions
that have to happen there and how these
different smart contracts are
interacting with each other let me see I
think the approved pattern is a big one
here contract to contract interaction is
a big one here just just this idea that
like let me I think it says it right
here like smart contracts are kind of
like always on vending machines that
anyone can access I think that's just
like a really cool way to think about
it's like a vending machine in the sky
that anybody can get to that's that's
pretty cool and not even like nation
states can sensor it that's really
powerful okay so uh those are your first
three builds your fourth build is going
to get uh a little gamly it's going to
be a dice game and so dice G the dice
game really shows you how Randomness on
a public deterministic blockchain is
kind of tricky uh you can't really get
Randomness in in the way that you might
think of when you just go to like hey
JavaScript give me a random number right
you can't get that from the evm it
doesn't do that uh but what you can do
and this is not a good idea you can use
the previous block hash so there's a lot
of entropy in the block hash because it
has to do with like proof of work Mining
and now it's you know validating and
different but it's it's basically a
random string of hex characters and so
you can use that previous block hash for
a very SE insecure form of Randomness
and there's really cool ways to do
Randomness on chain with oracles and uh
other ways that even like we have this
really cool way where you submit a
previous header and it uses the block
difficulty which is now randow so there
are like very good ways to do Randomness
uh this is not one of them this is a bad
this is a bad way to do Randomness
basically the way it works here is your
going to put in like 0.1 eth and it's
going to roll the dice basically just
looking back at the previous block hash
and doing a mod of that you know like
mod six and it's like a one die roll
right but if you win you'll win like
Sixx back if you lose your money stays
in the contract and you can play the app
and you could probably load it up with
some eth and it would play for a long
time but this thing is attackable you
can attack this by creating a second uh
attack contract I think it's called
rigged rooll is what we called it yeah
you build a rigged contract and the way
this works is the Smart contract knows
about the other smart contract and knows
how it's deciding it knows okay if we're
on block eight we know that this guy's
going to be looking at block seven and
doing a mod six on it or something like
that so you basically recreate that math
in your R rigged contract and then when
you go to roll you basically only roll
if it's a winner and so you can
basically drain the dice contract with
this rigged contract and and that'll be
your uh third or fourth build that'll be
your third build where are we at here
that'll be your fourth build all right
let me see if there's any other little
aha moments in here that I want to talk
about a really fun game though you get
to roll this die like you got all these
cool just scaffold LEF makes it look
cool and the build Guild team has done a
really good job designing this making it
look nice and making it flow really
smoothly some side quests in there looks
like you end up deploying IT contract
verification looks good go do this at
home you'll learn you'll learn a lot all
right the fifth app and I think the most
important uh and then I can hand it off
here in a little bit is a DEX and a DEX
is um a way to swap it's a decentralized
exchange it's a way to swap between some
token and eth or maybe token to token
but the way this worked before was like
an orderbook system if you wanted to
swap with someone someone would sign a
message that they they would be the
maker and then there would they would be
looking for a taker right and the maker
would say something like I have five of
these tokens and I would like one eth
and I've signed a message and that goes
into an order book and then someone else
could take that submit that message and
submit it on chain and send their tokens
in and get the eth back right so you
could swap but there's like this
centralized order book there and that
order book can get down go down that
order book could get regulated there's a
lot of reasons why the centralization
sort of falls apart you have this really
awesome decentralized blockchain and
then you're you know running this
centralized service on top of it so uh
the Dex brings this all on chain it
makes it uh fully decentralized and
really the the the trick here is to have
reserves of both loaded up in the
contract so what you do is you'll put in
a whole bunch of tokens and a whole
bunch of eth at the ratio of whatever
those tokens are worth and then when
people want to swap they'll swap much
smaller amounts between the two and it
there's a really nice kind of like
drawing in here you'll see the constant
product stuff uh what this thing right
here this thing right here so I'm going
to put in token a and get back token B
right and that curve is the price curve
and with each trade the sort of dot
moves up and down that curve and there's
a really nice visual uh uh uh curve here
it actually like plots this for you let
me see if I can find
it where is that thing yeah well here it
is but it's not there oh wait is that a
video no that would be cool uh you
you'll see this curve and you'll see it
move up and down and as you swap you
know if I put in a whole bunch of tokens
it's going to run down the line and if I
put in a whole bunch of eth it's going
to go up the curve and and the price is
wherever that dot is and the amount of
slippage is how far that kind of
triangle comes out it's you kind of have
to dink around with it but once you
start dinking around with it and saffle
E it's like it it becomes pretty obvious
how this works so your fifth app the
most important app is this Dex and what
you do is you build a smart contract and
you have to write the code you have to
figure out how to set up the Swap and
how to make it uh figure out based on
the reserves what the price is and uh
you have to
uh like really write the code and learn
and you'll have to get in here and do
this it takes a time it takes a little
bit of time by the way this Dex doesn't
have slipage protection don't deploy
this uh on you know on Main net or
something this is like a play Play De
you need to build more things into it to
make it secure to put uh
online on chain but it's it's good
enough for you to learn here yeah here's
how you calculate the price right
there's this constant product where you
figure out the the token to eth mixture
and then like there's the token to eth
on the way in and then the token to eth
on the way out and they have to
basically be equal okay so uh you
the there's the swap right you can go
from token to eth or eth to token but
there's also a couple more functions on
your decks and they're around putting
these reserves in you need to basically
load it up with tokens and load it up
with eth and when you do that you get
minted another token that represents
your claim on the reserves that you're
storing in that contract and this is a
really important concept because what's
going to happen here is that the
reserves are going to earn you money
money if you own eth in that contract
you have that token that represents that
money as people swap like Z3 or
something like that of that token gets
left behind each time so actually if you
look at a DEX with reserves in it if
someone swaps back and forth a bunch of
times the deck sort of slowly gains
value it actually earns fees so for you
as the liquidity provider you're earning
fees and this is what's called expansive
in in the term of hyper structures so I
want to hit you up with this one uh go
look up a hyper structure and spend some
time uh reading this this paper because
it's really inspiring and it helps uh
kind of lean you toward building on
chain and thinking about how you put
things on chain and what kinds of things
can be successful on chain uh it need to
be unstoppable free valuable expansive
that's what I was talking about about
the LPS why would someone want to lock
up all this like the more reserves you
have the better the swap is uh but
what's my incentive for doing so right
you have to incentivize folks uh it's
permissionless it's positive sum it's
credibly neutral check out check out a
hyper structure so yes you will create
the smart contract you'll be able to do
eth to tokens tokens to eth you'll be
able to put liquidity in you'll kind of
like learn all these intricate details
there there's the curve right there I
knew it was here somewhere and uh you'll
end up shipping this to a test net and
you can just get in there and swap you
can get in there and put liquidity in
pull liquidity out it's really like a
little sandbox Dex that's you know the
the starter kit for building something
like Unis swap okay so those are your
first five apps you want to go speedrun
these uh we are always in the telegram
channels there's a telegram channel for
each one we're in there answering
questions so if you have questions were
there and we can um yeah yeah help you
speedrun those if you have any questions
I think the last few challenges let's
just go look at those real quick just so
I can highlight those uh you you get to
join the build Guild once you complete
the decks and that's basically we have
like onboarding batches we do a small
grants program we basically prepare you
to go ship something in the space uh
State Channel application looking at
signatures looking at l2s looking at
offchain interactions a multisig wallet
would be having multiple signers that
could all transact or you need maybe
like two out of three signers to be able
to make a transaction happen so this is
really nice if you need like something
more secure uh a lot of good developers
in the room I've seen that if you're
holding eth in large amounts you want to
have it in a multisig right you don't
want to have it in uh like an app or a
hot wallet you want to have it in a
smart contract that has rules based on
you know if uh if if you want to move
money out of this smart contract I'm
going to need a signature from your
phone and I'm going to need a signature
from your laptop and I'm going to need
like a signature from your Hardware
wallet right you have to get all of
those together or maybe two out of three
of those together to make the
transaction happen and that's just much
safer it keeps the money safer locked up
in the smart contract wallet in the
multisig and then the last one is a fun
little just like SVG nft we started out
with that first nft and you'll get in
here and you'll learn about ipfs and
you'll realize that like the thing gets
deployed to ipfs the only thing that
goes on chain ends up being the link to
the ipfs so the thing that's on chain is
more like a little Json file that tells
you where the the stuff is you're not
actually putting the image on chain so
in this last challenge we actually have
you make an nft where the actual SVG nft
is rendered from the smart contract
which is probably more nerdy than
anything but it's just cool to do and
it'll be a good lesson to learn so that
was like a bonus basically your first
five apps go up to the decks and the
rest of these are kind of bonus uh
challenges but I would recommend you
take time to go through them when you
have some free time at home or maybe
just some free time uh around here but
you'll have to sit down and focus and
actually write code there there's a lot
of moments where you have to think for
yourself it'll say hey you need to do
you need to you know make this thing
happen but there's not going to be code
that you can copy paste you'll have to
write the code yourself it it gives you
lots of help but in the moment of
figuring it out like you have to figure
it out yourself and that's it's it's
going to help you learn like that's the
way to learn this okay so that's
speedrun ethereum uh I'm Austin Griffith
we're the build Guild uh we are going to
uh do the CTF after this but I think Eda
is going to come up and um do some nfts
next you gonna do an nft app awesome
okay and I don't want to close my laptop
but I'm good to go when you guys are
good yes thank
you thank you
I should have I should have done a
question session but we'll do a question
session after this we'll double the
questions
down okay is my microphone working okay
perfect hey J how are
you okay so hi guys now we're going to
do some NFD apps which Austin talked
about using scaffold e um and it's going
to be a quick session so I have 13
minutes and 45 seconds um so what we're
going to be doing is we're going to be
using scaffold e and it's similar to the
first challenge of the speedrun ethereum
where you build an nft application uh
and I'm just going to try to walk
through each step on how we can do it
how we can deploy the contract set up
our new contracts and kind of showcase
how it works uh so hopefully it will be
a nice preparation for the capture the
flag challenge this afternoon um and yes
let's directly get started because we
don't have a lot of time um so all I did
and I want to show you what I did um now
all I did was I went to scaffold e and I
just downloaded so then we can save on
time and make sure there's no error um
you're welcome to follow along if you
have Lo laptops opened um and yeah I
took MPX create e latest and I created
my own scap application I did nothing
else all the other steps will'll be
going through
together okay so where's my terminal
cool so I named it nft Workshop you can
see over here I have the project let's
kind of start our chain
uh I also didn't deploy the contracts
actually so like let's deploy what we
have just to see what's going on in our
app and then I'm going to do a yarn
start and I kind of went fast but I
basically have three terminals over here
one running my local chain uh I chose
Hound Foundry when I set up the sca lead
application but you're welcome to choose
hard hard if that's your preferred
development environment um and then I
deployed the first contract we have this
is like a basic smart contract um it's a
hello world smart contract we which
we'll just look into very shortly and
then I did a yarn start to start my
application and let's open where I have
too many browsers here so I'm going to
do like this I'm going to open my Local
Host here I actually want like an
incognito
window Okay Okay cool so this is what
you get with all the speedrun ethereum
challenges you use the same toolkit so
once you kind of go through do the first
one I think it makes you familiar so the
rest will come more easier uh and what I
have over here is this is like a sample
front end to get started with and then
debug contracts tab which makes it
really easy which Austin was talking
about as well um you know you can kind
of have this is the initial contract
which we just deployed it's a greeting
contract you can see the details like
the address the owner um all of like all
the functions available are displayed
here and what we're going to do is um I
want to add a new contract to our
application because you probably want to
have more than one contracts so this is
like a basic contract but what scaffold
makes you do is you can also have
multiple contracts in your same app so
this way you can kind of work through
them like have them send each other
messages or kind of link to each other
and that's what I'm going to Showcase
today it's going to be an Asic basic nft
contract and we're also going to be
building a small front end as much of as
my frontend skills allow no I I have it
ready too so no worries I think it will
work um okay so what I did and just to
show you my app as well uh this is what
we just downloaded I had it opened um
and I'm I have The Foundry folder but if
you choose choose hard hat when you do
the wizard which starts your application
you will see it as hard hat and um I
will basically have over here my this is
the your contract which we just saw and
is this good enough shall I
zoom it's
good
okay okay perfect so this is the your
cont contract which comes as the basic
you can see the details here and I'm
going to add a new contract and I'm
going to show you exactly how to do that
and one other thing so I'm walk I'm
talking about what I'm doing but the
docs are pretty uh clear and show you
all the step by step so um any questions
you have about scal Le you can basically
come to the docs what I basically just
did before like well just now as well
was to set it up using the CR latest and
then it tells you all the details it
tells you the details about the
extensions as well so so um you can
definitely go like default to the docs
if you have any questions they should
definitely have your answer and I'll be
going to the docs a lot during this
presentation Okay cool so let's get
started now as I said I want to have an
new nft contract and I'm going to go to
Foundry because I chose Foundry and I'll
basically be using the soulmate like I'm
going to create an nft with soulmates
all I am I'm at The Foundry docks and
they have like where is this exactly
okay they have the tutorials here so I'm
just going to like copy and follow the
tutorial to add the nft contract and
then that'll basically be my application
too and I come over here so um because
we're using Foundry I do need to install
like soulmates and I think we have the
open zeppin contracts but let's let's
make sure to install like what it
requires to create this NFD
contract Okay cool so this is I'm back
to my terminal let's just close this for
a bits um I'm actually not
sure I need to go to The Foundry folder
to install the
dependencies oh but yeah it doesn't
allow so I'll just do like a no
commit so this should be
fine oh and I actually didn't mention
that and I probably should have
mentioned it before I started too but
you can totally follow along what I'm
doing in GitHub I have over here a rep
repo to explain what we're going to be
doing now so you can totally follow this
along as well uh if you want to I think
it's fine like we'll go to the steps but
I'll provide this link but yeah Devcon
CLS so it has the steps which I'm going
to be running through
today um okay so I'm installing the
dependencies I need okay this was pretty
fast and I'm going to go back here I'm
going to do a yarn chain just so that we
have this running um all I did was I
went and installed The Foundry
dependencies um I'm just kind of
following this tutorial over here and I
want this contract so um this is like a
basic nft smart contract it has like a a
name a symbol and then the Min to and
token URI functions here and all I'm
doing is I'm going to take it and put it
in my scap
application so to do that now we have
over here the your contract I'm going to
create like a new uh file here let's
call this nft
contract okay um and I just copy pasted
the code we directly took uh because we
inst the dependencies we should be fine
so now all I did was I I added like a
new Contra like a new NFD smart contract
to our same application but this will
not automatically deploy I also need to
edit my deployment scripts because when
you do a yarn deploy it only deploys
your contract by default which is this
one over here so whenever you add a new
contract you need to update your
deployment scripts or like let's say you
know like you change the your contract
Constructor then you need to add that to
the deployment script details so then it
deploys all together and where did we
add that okay I think it's Scripts
okay so this is the deploy deploy your
contract this is the initial script
which deploys the your contract smart
contract I'm basically going to copy
this and create the same one for my NFD
smart
contract come on copy command B I'll
call
this uh
deploy okay I didn't do anything I just
copied it I'm going to change the your
details to
nft NF contract da da da
deploy it's also so cold in
here okay I think this is fine uh now
this is actually not enough you also
need to add it to the deploy script so I
created like a new deployment script for
my nft contract but I also needed to add
it to this main deployer script and you
can actually also add it here but this
makes it just a bit easier so then you
can like add change things without like
messing the structure a lot um so this
is like my new script which we just
created from zero called NFD contract.
like deploy NFD contract.
s.o and I'm
going to add this to the main deployer
so then it also actually deploys because
by default when I run like yarn deploy
it only like this is the folder which
gets run and um thank you to devs who
added the notes here um and I will copy
this and I will do a
deploy nft
contract okay I think I need to also
import this but
my uh my co-pilot should actually have
told me this
but okay so for some reason co-pilot was
slow but we got it so I think this
should basically deploy our new nft
contract and let's kind of see if that
works and if not we'll figure it out but
I think it should work so uh by the way
like when you deploy you like you um you
can gen like I generally do a yarn
deploy reset
to make sure that nothing gets
saved oh okay I remember so um I think
there's an issue with The Foundry like
the solidity version from our nft
contract this is like quite old so I
think if I do this 20 this should work
um this is an error of Visual Studio I
don't know why this keeps giving me like
import errors but I think this should
work like it was it was 8.10 but that's
pretty outdated so I think this should
work
now uh okay so this is fine I think this
is like
a this
is or I can just call the other one nft
I'll actually call this one uh so this
was called nft but I think it should be
called nft
contract I think this is better since we
named our file NFD
contract it's always hard to do online
demos but um I didn't edit the
Constructor so our Constructor is
probably empty so that's why it's giving
an error um so okay oh no it's on not
empty I need to give it a name and a
symbol so because I just copy pasted I
should have actually checked where my
what the Constructor takes and in my
deployment script I didn't add any of
the constructors so over here all I need
to do is I need to add my Constructors
so I'll just call my my token whatever
name and then I'll give it a symbol
right is it name symbol or symbol name
name and symbol and the name will be
like
edas I don't know if this creates like
legal problems but Eda because my name
is Eda um okay cool hope this should
work now right let's make sure that we
don't have any errors this at Line This
Is
Here we give the arguments
here I don't think there's any more
issues to be
honest do I have it wrong here
okay one second I'm going to like just
cheat over here I think we should add it
here though
Okay cool so I added my um Constructor
arguments at the wrong place uh but
basically the issue was I need to give
my um when I run the contract because my
Constructor takes two arguments the name
and the symbol I wasn't doing that
correctly um so now we basically
deployed like a new contract and let's
look at it on our application which I
think is the cool part so as I didn't
edit any front end all we were doing was
we added a new smart contract cont it
was a bit stressful but we managed so we
have like a new deployment script and we
have a new smart contract and then over
here it directly comes on our um on our
front end so as you can see now now
there's like two contracts the York
contract and the nft contract and I kind
of can play around with this without
making any other
changes um so this yeah I think this is
pretty cool like when I was like first
starting and I wanted to try like
multiple contracts I found it quite hard
like you need to like manage the
dependencies like all the new libraries
and stuff like that but by this like you
can just add like a new smart contract
you don't need to like um you can of
course like write the test and
everything but it automatically appears
on your front end before doing anything
else and let's let's see how this
works so um I I directly click this
button but what this does is it g me
gives me some funds from the faucets um
if I hadn't clicked it it would have
given me like a gas error it would say
like you have no money to pay for gas so
um I directly clicked it but let me let
me show you what happens if you don't
click click it
too oh this one I'll go to like my
browser over
here it's burner wallets so it generates
on new browsers so this one has like
zero e right now so I can go to the
debug contracts tab I can go to nfts
like let's say I want to like mint mint
this this
address and then the the Val like I
don't want to give any money right now I
send but it gives me gas
so that's why I had automatically click
that uh burn like that the the faucet
yeah grab funds from the faucet button
hopefully now it grabs funds um it's all
from my Anvil local chain so we're just
on Local Host right
now cool so as you can see I minted an
nft to this address and I can send it to
like this um this address the green
purple orange one as well and this is
kind of how it works and let's do this
again again on this
person um I'm not going to say any send
any money to it but you
can perfect so it's pretty easy to like
add a new contract and uh when you go
through the challenges you'll either
like modify the existence smart
contracts or you'll you'll be adding
like new smart contracts and this is
kind of like how you can work with
Foundry and add like new dependencies
and then create your new contract and
what I want to do is so we have this
inter like this web page but let's say
you built like an nft app like you don't
want to show this web page to your users
you want to have like something better
um that's why we kind of have the the
initial page to get you started as well
so I have like 15 minutes and 6 seconds
left so I'll try and like build a small
front end where you can automatically
mint nfts from that page instead of you
know sending this page to your users and
being like hey like go to debug contract
subab and then mint from
there okay time goes by much faster when
you're in a rush I
guess cool so yeah this the error is the
dependency error I think like uh Visual
Studio code or like my extension gives
it an error but it's actually like we
have the contracts in the lib folder I
don't know why I had the problem
earlier so what I'm going to do is now
I'm done with The Foundry folder we have
our smart contracts everything's working
if I want to add more I will add more
actually we will be adding more CU it
doesn't have like it doesn't set a
maximum Supply the default uh just like
you don't set a maximum Supply in the NF
contract so I kind of want to do that if
we have time so what I'm going to do is
I go to the nextjs the app and then I'm
going to create a new folder here and
I'll call it nft and then I'm just going
to copy this page.
TSX but this
is and then I'm just going to paste it
here or I'll just like remove everything
from
here what I'm doing is uh I want to
create a new page which we can go to
like localhost nft and this is kind of
the the way nextjs arranged it and I
just want to create that let's just call
NFD I think this should be
fine okay so I I'll be editing all this
but let's let's make sure that it
works cool so uh what we did was we uh
right now you only have the home and
debug contract I created like a new
folder in my um in my nextjs app and
then it goes to like by default the nft
extension because that was the name of
my folder and I have a page.
jsx there
which displays this uh but I don't want
to display this so let's just delete
this and let's just show
hello and let's actually like remove the
secondary background CU that's not nice
cool so um okay so we kind of have an
initial app we have like an initial web
page now what I want to do is I want to
pull the
pull the nft contract information here
so then it gives you a button to just
like you know you see the nft you click
it and you mint it and for that I'm
going to go to Daisy
UI uh scaffold uses daui so you don't
need to like work a lot on your front
ends like I I don't build many front
ends so this makes it very easier to
just like go and get the components and
have them be displayed on your app um
and I'm going to go over here to the
components and you can directly use any
one of them this uh I'm going to use the
card component the card is somewhere
oops I just take the card so this is
what it gives me let me just copy paste
this um you can use any components like
it has different like headers and you
know bubbles countdowns stuff like that
it makes it really easier like I highly
suggest it if you like it's if you have
any other framework you use that's
obviously fine but I'm just going to go
and paste this here
so this is the shoes
card uh I'm going to go to the nft toab
cool so all I did was I got let's open
it here actually all I did was I went
ahead and I got this Sho card component
and what I wanted to do is I I don't
want like a Nik advertisement but
instead I want to have my nft details
there and then it will show like nft and
then this button will be mint now and
then let's actually like Center that too
okay so the image image we should change
and
then nft
mint
here this is not a funny
joke and then you do a mint
here I think I can do item Center
okay I didn't manage this
but okay for now this is fine let's just
make it working and then we can like
send like do all the other details I'll
also remove this night picture because
it's kind
of Okay cool so nft meant here and then
the mint muton should be our nfts and
what we want is we actually should see
the NFD details right like what what's
the token name what's the how many nfts
are left Etc so I do really want to see
that information uh and to do that I
need to read from my smart contract so
um I'm going to go over back here to
scaffold heat talks to show kind of how
you do that but scaffold heat has
built-in hooks so you can directly use
the hooks which um kind of allow you to
interact with your smart contracts um by
the way I mention like it directly uses
wag me and wagm hooks so it's kind of
easier to use the scaffold e hooks when
you kind of work with it and daui
details you can kind of find over here
as well but I'm going to go over here uh
this gives you a shortcut like in like
recipes gives you a shortcut too but I'm
just going to show the read contract H
so um I'm just going to copy this what
this does is it allows like it directly
provides a hook for me to read my smart
data and then I'm going to add it here
dot dot dot and then I'm going to just
change it it's going to tell me I need
to import it let's just do
that and then it's going to be my nft
contract and then and I let's I don't
remember what we had on our nft contract
but over
here let's get
the the current token ID let's just show
that for
now there is no arguments I think I can
just delete
this and then I do the
token I also want to get my address
let's let's show like the connected
address and I I like everything is on
docks over here so it makes it very
easier to like get your connected
address as you can see we directly use
use wagm like use account from wagm um
but I also want to show the address when
we go to the like when we go to our nft
page and I'm going to do this address
this is going to import from rag
me and then let's let's add it here
um let's add like a H1
I I probably need to wrap the token ID
to uh an integer or something like that
but let's
see oh okay I need to do it's a client
side because I'm using client components
on my next JS app I do need that um okay
so cool it shows me my connected address
but uh instead of like showing it like
that uh I want to use directly the
scaffold address component it just makes
it look better like as you saw it was
doesn't look really nice you don't you
probably don't want to have this so um I
think there's directly an address or
account is this like Okay cool so I'm
going to delete this it will give me
like a blocky and an avatar automatic
ens resolution um this just perfect so
now okay so there's no ens resolution
because we're on like um Local Host but
as you can see it's kind of gives me
just a better view over here with my
connected
address and then the token ID I think I
need to like wrab this in like
something an integer
cool because uh it resolves like big
numbers so the big number format doesn't
match so can't you need to like convert
it to a like a a number format but Okay
cool so basically we directly use the
scav um address component we now have
this here and we want to have like the
mint button working because right now it
does nothing uh but what we what we were
able to do is we use like we added a new
smart contract now we have like a new
page which displays the details of that
smart contract it's token ID here NFD
mint here and then the mint M what it
should do it should mint an nftd and
then once it does like you'll
automatically see the ID increase and I
have five minutes left but that it
should be
okay um so I'm going to over here to the
scaold docs
again I have too many tabs
open and then interacting with your
smart contract uh I came back here
because we were using the read hook
before now we need a write hook because
basically we're going to make change
like we're going to to uh like mint a
new token um so we need to like interact
with our smart contract so a read is not
enough at that point um and it's it's
quite simple to like use the use
scaffold right contract hook I'm going
to directly copy like this is you need
to Define this up
here quite similar the way we did like
the use scaffold read contract it's just
going to be a use scaffold right
contract we need to import this let's do
that and then it's going to be like uh
nft contract because this is the new
contract which I'm working with um okay
so I basically pulled in like a right
hook and now I want my mint button and
uh all I do is it gives you like an
example usage over here so I'm going to
Tech copy this and then we'll just edit
it the mint button I think we can
just okay I'm going to delete this mint
button the function name is is it mint
two the function is called mint two and
it takes an address so I'm not going to
forget to add the address the function
name is mint 2 the args are going to be
the address and we don't we don't need
to pass any value but if you say you
know like mint for one e you can add
that probably want to add that to your
front end too uh but all I'm going to do
is I'm going to like for now like
actually just pass in the connected
address um and I can just do like
this this should be fine
oh I don't need these
maybe okay I think this should work so
basically what we did is we pulled the
right contract hook we added like a new
button and the button is called well not
set greeting but let's call this mint
here and then uh I
don't I don't want to at the
end and then uh yeah this should work
see so when you mint here basically it
should increment the token ID because we
minted a new token and then um you
should be able to see that transaction
completed so the token ID is now
incremented because we were able to Mint
an nft now of course you probably want
to show like a receipt over here of how
many nfts left but because I have only
two minutes left what I'm going to do is
I'm going to quickly modify a smart
contract to have like a total Supply and
display that on the web
page I think we should have enough time
that uint all I'm doing is like a new
uint like let's call this Max
Supply let's say 10 10 is enough and
then this should like have a new
require okay so I edited my smart
contract because by default it doesn't
have a Max cap right now and I want only
display this on my front end too um so
I'm going to do that but let's first
redeploy our smart contract to make sure
that or I think it's it's okay we didn't
do much changes but now we have a Max
Supply but I'll just redeploy because
then it will give me an error when I try
to add Max Supply is not
there okay so I quickly edited my smart
contract I now have a Max Supply and I
want to display that detail on my uh
front end so then you you can kind of
have like a counter which is a bit more
fun um I'm going to use the read hook
because it's just like a a value which
we read so we don't need the right one
and this is called Max
Supply and then I'm going to call this
Max
Supply and then what do we do over here
the token ID instead of we don't need
the token ID let's say
Supply I'll like left nfts
left well nfts left is Max Supply minus
the ones we've minted so uh I'm going to
do that
minus
um let me first display Max Supply and
then we'll do the subtraction
count do we do the max Supply wrong
but this is the max
apply oh thank you thank you I should
have this right the max Supply yeah
okay perfect 30 seconds left but this
should
work okay so now we have 10 and then we
mint well the max Supply is still 10 but
what we can do is we can quickly add
like a minus o
I'm not sure I can do the operation here
do I need to do like it
here okay my eyes are not working now
oh okay got
it I am finished okay okay it's working
woo
yeah we can show that too I have I
actually have 10 more seconds left you
did it it was great you want to hang out
up here oh yeah if you have any question
next is a Q&amp;A and you can shoot this QR
code and send questions to the board but
also like you can just Yeet them out and
we'll hear you and answer the questions
too also there's like 10 build gilders
all over here with these things on you
can just come talk to us and we can
answer a lot of questions for instance
if you're bringing up scaffold eth and
you have some like debugging error or
something just bring it over here to
these guys and they can help
out but yes if you have any open
questions there is a QR code also you'll
notice that if you go through through
speedrun ethereum within each one of the
challenges there's a telegram group and
in that telegram group we're sitting
there listening to you so if you have
any questions we're there and we can
help so questions maybe hands maybe you
hit shoot the QR very open here I think
we'll do like 10 minutes of questions
and then we will start the
CTF we can have question hearts hearts
uh any resources for python maximalist
so that's going to be different you're
probably going to want to use Viper
which is a different language solidity
is uh more like typescript right so if
you are a python maximalist I would go
look at Viper and I specifically look at
Patrick Collins work he does a lot of
Viper work and he's a really really good
teacher and a really good devil so look
up Patrick Collins and Viper if you are
a python maximalist
hi question yes sir where are you right
here oh there we go um so you use Daisy
UI on the front end how hard would it be
to use something else like Shad Cen
instead or would we lose some what would
we lose and what would we gain uh
nothing you could just bring in that
other it's sort of like we provide the
scaffolding and it's kind of a pretty
opinionated scaffolding but you can
carve out our stuff and put in your
stuff you can try different things what
what is can anybody over on the scaffold
e team do you guys know anything about
putting Shad CD in into scaffold eth has
that been something we've talked
about oh he's
busy do you know shiv if we're thinking
about putting Shad CDN into scaffold e
or how hard it would be to use Shad
CDN bring it yeah yeah like you could
actually it's compatible so like you
could install Shad CN and start using it
so yeah so it seems like a thing you
might have to carve out some Daisy and
put in some Shad but it seems like I me
both both Works directly yeah I think
the one what you should do is make an
extension that if you make a scaffold
eth extension that uses Shad CDN and
then we can cross promote it between the
two of us that could be cool that was
the next question was because looks like
some nerds are arriving for the CTF that
is a good thing to see I love to see
some nerds coming in with some backpacks
think about doing some hacking hell yeah
yeah so great question yeah they were
already um components like the account
display I would lose those I'd have to
rewrite those myself with so no those
aren't yeah you might have to rewrite
those for Shad CDN yeah yeah darn it
yeah cool but do that and make it open
source and let us uh cross promote it
with you so people who like Shad CDN
could go use those so what would you do
would you Fork it create a create a
branch and then contribute it there's a
really good video by Hunter I think he's
here somewhere on how to build
extensions I think the first thing I
would do is I would just Fork scaffold
eth and make it work and then i' take
the work that that I put into that and
uh put it into a scaffold eth extension
and there's a video that kind of takes
you through how to make an extension and
then you're kind of it stays
state-of-the-art so you could use
scaffold e plus whatever extension
you've added and we can kind of
cross-promote it and show it off to
people thank you cool thank
you we got a hand here oh you got him go
ahead y so uh we we have used hardit and
the fundry right so is there any
advantage or limitations between these
two yes so the two are different uh
they're great for you said hard hat and
Foundry right just to make sure okay so
uh hard hat is a little bit older uh
it's a little bit slower it's more
typescript tests but they're starting to
carve things out and uh act more like
Foundry Foundry is faster it's written
in Rust and I think the key thing there
is you're using solidity to write your
tests whereas with Foundry you were
using typescript to write your tests and
so as a solidity developer writing those
tests in Native solidity just makes a
lot more sense and a lot it's a lot
smoother however if you're an app
developer you want that typescript
because you want to copy and paste it
into your front end so having a hard hat
is also kind of good for the the front
end folks too so the the answer is
Foundry is the state-of-the-art best
tool hard hat is a really good tool and
before hard hat we had truffle and it
was awful sorry to the Truffle guys it
was fine it did what it needed to do uh
but uh also hard hat is catching up
they're starting to use revm which is
the technology the chain underneath
Foundry they're starting to rewrite some
stuff in Rust uh I would say that their
deployment process is a little smoother
but uh I kind of just randomly pick them
depending on like if I'm going to do a
lot of like yarn Forks I'll usually use
uh Foundry but kind of sometimes I
default back to hard hat just because
I'm used to it but the difference is
kind of this this the testing in
solidity versus testing in typescript I
think is the key thing and foundaries a
little FAS still got got it thank
you okay there's one over here somewhere
there we go
yeah uh what's up with the build gu
Guild ethereum node is it like a normal
node or yeah so you can go to client.
build guild.com or client.
bidle and
what it is is it's a process that runs
that spins up W and lighthouse in the
same node and then there's even like
this opt in that you can do where you
can opt into to our distributed RPC
Network and you start earning some
credits that have no value it's just
numbers in a database but you earn
credits for serving RPC requests to our
apps so we build a bunch of apps on
chain and we use the bill Guild RPC and
it's served by this sort of uh
distributed set of nodes and we pay them
back in credits but that's not a real
thing yet and it doesn't have any
Financial value yet right no no not ever
not ever but uh it's just an easy way
it's like a oneline command you can run
a oneline command and it brings up a
whole cool ethereum node but you'll need
like a couple terabytes of space right
Spencer is a man to talk to about that
he wrote that
software good question did that answer
your question I think it did right how
can I how can I run the notes uh just go
to client.
build.com and copy paste that
command into your terminal and it'll run
wait is that a Windows machine though
what is that Linux no it's a mac oh yeah
just copy just there's like a oneline
command copy the oneline command in your
terminal and you'll have a node running
the thing is it'll just take up a lot of
space okay I have one more question how
do you pronounce the name of the build
Guild build I just say build Guild but
definitely it is build gitt right it's
misspelled on purpose and it's like the
hotal meme right the hotal meme and then
the Biddle meme so yes it is B oh look
at these nerds coming in for the cpf yes
yes this is we're going to set this off
this is going to be great we might need
more
chairs uh yeah I just say build Guild
but it is spelled bidle gidle but I
don't
know uh oh do we have more questions
here do you guys have scaffolds for
other Frameworks like angular no it is
just react we are I think someone made a
spelt I think a bite at a time made
scaffold spelt if you go to build Guild
like bid.com you can go to the app and
you can look through all our builds and
within those builds you could search for
selt but I I don't think there's one for
angular nerds yes why is there not
enough what was that top one soccer oh
sockets where are there no oh no do we
like plugins back there is that what
you're talking about yeah we didn't
think we were going to have this many
people I think we'll we'll have to
figure something out uh maybe some other
people will clear out before the CTF
starts please don't please stay please
hack but if we need more Outlets we'll
have to figure it out we'll uh maybe
call them in or something but yeah there
are not a lot of power outlet in here
that might be tough not sure what we can
do about that but we'll talk to
them vuejs no uh it's it's all uh it's
all react how hardcore of a Dev do you
have to be to participate in the ETF
okay that's great we will answer that
question in just a second but the tldr
is uh even the worst Dev can figure out
the first couple levels but even the
best Dev in here is going to have a hard
time with the last couple levels so it's
you're going to have a very easy entry
into the CTF but it's going to get very
hard toward the end I
think building a multi-user
communication dap scaffold eth is easy
maybe I mean that sounds complicated but
maybe 35 seconds okay we got 30 seconds
and then we're going to switch to the
CTF which means I need to grab my
laptop uh can you can you do the CTF
without a laptop I think you're going to
need a laptop
yeah that might be a bit hard is this my
machine
okay
okay got 10 seconds left you want to
take that I got
it any last questions come on in get
ready for the
CTF there's also a PO app collect the PO
app if you are here collect
it okay oh my God if we could bring up
my screen here it
good oh that's not
me and I think we're actually shutting
off the live stream
right I don't think we're live anymore
or are we still
live we're still
live oh I hold it hold the mic or
hold oh oh oh this is being weird okay
okay oh hey here's my build Guild client
right here see it running so it's
sinking still but you can see dis
activity network activity CPU load you
can see uh the lighthouse
