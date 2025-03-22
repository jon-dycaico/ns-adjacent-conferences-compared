[Music]
[Applause]
for
that
e
good morning everyone it's great to have
you here so in this session we are going
to have presentations about evm and then
in the afternoon we will have
presentations about solidity and
developer tools for solidity uh so our F
speaker is Alex from Quan stamp and he's
going to talk about the evm object
format let's welcome
Alex hello everyone um thank you for the
intro and thank you for attending the
session this morning it's the first
session so I really appreciate everyone
um Coming uh yeah so I'm Alex from Quan
stamp and uh together with my colleague
valerian
uh we looked at how the bite code chaos
can be managed uh through introduction
of uh uh evm object format or
eof and uh yeah so what is EF and why uh
so there was actually a really nice talk
by uh Dano ferin uh on Tuesday uh which
Dives deeper into the motivation and I
highly recommend uh watching that when
you get a chance uh I'll just briefly
mention uh what the this is about so eof
is uh evm object format it's a new
format of the evm bite code uh that um
yeah and usually formats have special
magic markers right so in this case it's
uh ef0 0 so if the bite code starts with
those uh characters those bytes it means
that it's EF code uh it was originally
considered for the pectra upgrade and
that's when valerian and I firstly first
looked at it uh then it got postponed so
potentially it will be part of the one
of the upgrades after that uh but apart
from the technical Readiness are we
actually ready for this upgrade because
um yeah the questions to ask here is uh
are we do we understand it well enough
what does it do right is the tooling
ready what are the upside and downside
of of the of this new format and how's
the security side looking so all these
questions we were trying to uh to answer
in this in this
talk and uh why well uh currently any
bite code can be deployed as a smart
contract there is no predefined uh meta
structure no uh well defined version in
so it's basically uh maybe some
semantics can change over hard Forks or
new OP codes can appear uh with with a
new hard hard Forks of the evm uh but
uh there was no indication of the
version in uh that is actually part of
the bite code uh and there is no
thorough deploy time validation of the
code so which makes it which makes a lot
of other things tricky uh so yeah and
overall we have the following issues
right so it's difficult to add and
deprecate features as uh many of us have
experienced uh being the
devs uh and it's hard to analyze uh the
code and uh also it's a little bit
difficult for uh for the
compilers and also it's hard to fully
solve uh any longlasting uh I guess
omissions in the original evm uh because
uh as actually as that as Dan was
mentioning uh on the talk on Tuesday
it's either you have to just uh keep
making small tweaks or you have to just
break everything at once and just um
make it make it right uh and yeah the
solution there is we add structure
version in and evm is made better in
that new version while the Legacy uh
version would uh continue to to live
on and uh yeah so e EF is actually quite
a complex upgrade uh there is uh on the
right side you see uh quite a few uh
eips that are uh that go with it and my
colleague there try to draw a diagram of
how this is all keys together and with
some some uh some errow that signify
some of the interactions between eof and
Legacy we we do not have time to look at
all of them so I would just try to give
a bit of highlights of uh uh those um
items that I've that highlighted on the
slide and we'll give some uh code
examples as
well so let's move let's get to it well
uh on the left side you see uh basically
a toy example uh this is a very very
simplistic example because we just
wanted something simple to to go with to
just showcase the differences between
the Legacy VM and uh the new a format uh
on the solidity side we just have an
infinite Loop contract which pretty much
just Loops forever until it runs out of
gas uh and uh this is how the you know
below you see how it could be
represented as a bite code this is a
very rough manual translation there it's
a the actual bite code will will be much
larger because there will be additional
checks included by the
compiler uh yeah so what we have here is
um uh basically jump test instruction
which is
with 0x0 0 which is the location to jump
to and then the finally finally the
actual jump command so it's basically
you tell uh where the jump destination
is which is in this case just 0x0 0 and
then you push that value into the stack
and then you jump to that location so
it's pretty much the the infinite Loop
that's how uh it's um intended for this
example now let's look at
EF here we have uh a whole bunch of
other things uh we now see the structure
right there is the header and there is
the body in the header we have UF magic
which we've already seen on the previous
slide uh which is followed by the
version uh version one in this case then
uh it uh describes the sections uh in
this case we have the types section
types is indicated as 01 and the length
of that type section is four bytes
same with the code section uh we have
one code section which is also four
bytes long and finally there is the data
section and uh we will not dive deeper
into that we just kind of omitted that
completely so there is no data section
its length is zero that's as far as the
header goes so in the body uh there are
two subsections one is the types and
another one is code code so uh in the
type section what's described is the
number of inputs uh number of Stack
elements or in this case there is a
special uh character special bite
sequence just a 0x 80 if there are none
and the maximum stack height which is
two so the way I think of this type
section from my perspective it's almost
like the signature of a function but
applies to the whole contract in this
case
and finally then we have the body
section and that is where we would have
placed the bite code from the left hand
side that would would have been the the
correct place for it uh but as we see on
the next slide this bite code is
actually no longer valid in the EF
world so this is our like simple to
example that we uh we go with so what is
wrong about that uh bite code that is
highlighted in red
well the the thing is in EF static
relative jumps replace the
conventional Dynamic uh
jumps and uh yeah so in the Legacy evm
jumps are Dynamic which requires
so-called destination code
analysis since it is not clear
beforehand whether the code at the
destination is even executable or valid
code so that's why the analysis had to
be uh done
dynamically and to simplify that we had
to had to have this jump Des instruction
that we saw uh earlier to highlight that
this is one of the valid destinations
for the for the
jump so yeah as we see here in our toy
example uh that's how uh that's how the
to example will be translated from the
Legacy bite code into the eoff bite code
right so on the uh yeah in the middle
here we see uh jump test push one and
jump on the right side we replace that
absolute jump with a relative jump and
just for the purpose of this example we
say well how about we just jump to uh
minus one which is just going back so
that's that way we kind of get the
uh the infinite
Loop
okay uh how about uh deployment of smart
contracts well uh in the Legacy VM what
we already know uh we have to use the
create instructions and uh there is the
concept of init code which gets executed
just once uh and this will pretty much
uh place the the bite code onto the uh
permanent storage so uh here on the uh
left side you see the need code which
looks fairly standard it's basically
just um uh pretty much highlighting the
the sections of the memory where the
bite code is and store in it and then
there is the final uh return statement
at the end and the actual code is pretty
much uh at the end here so it's the same
bite code AS we've seen on the previous
slide
well now how about EF well uh
interestingly uh EF in need code is also
on itself um a UF uh smart contract so
youf bite code so what we have here is
uh we have the header and the body uh
but the interesting thing here is that
there is a so called the subc
container and the subc container is
pretty much the uh bite code that we've
seen on the previous slide of UF so you
see at the very very bottom there it
says subc container and it's exactly
like we had on the on the previous slide
so pretty much what you see on the right
side here that's that's what is at the
bottom of this slide and if we go over
this a little bit we have uh uh yeah
yeah also all these different sections
and uh in the header we see that there
is the definition of subc container
which is uh 03 and it's uh 22 bytes
long uh and by the way uh Foundry has
this uh nice command now called the cast
decode UF so if we run the bite code
through that command uh here is the
visualization that Foundry gives us it
is it is quite neat pretty much another
way of of looking visualizing the bite
code uh yeah and what about uh functions
well it turns out that functions can
also be self-contained and encapsulated
uh within UF um as uh different code
sections for example in this example we
have uh just a sub routine which doesn't
do anything just Returns the the input
back to the Coler and in the Legacy code
that's how we would probably Cote it by
hand and in the in the EF what we have
is we have the call F and read F uh
instructions now which um could allow us
to pretty much do the function calls
within the same UF structure just as uh
just using different code Sub sub
subsections here so we have code section
one and code section two here
uh yeah and uh the standard EIP 3670
defines how code validation uh is to be
done then uh yeah usually it involves
basically just validating whether all
the instructions are valid and uh for
example s destruct and all the Legacy
instructions will be uh
replicated and yeah so this jump Des
analysis is no longer necessary there
because all the jumps are replaced with
relative jumps so this should make
things easier uh and yeah I guess the
question is what about interactions
between the Legacy and UF contracts so
what which rules would apply
there well uh we just glance at it and
seems like some interactions are allowed
and some are not allowed for example
create uh create two will fail if uh you
deploy try to deploy a b um bite code
starting with
the evm as of as of now uh can um UF
contract deploy a legacy contract no so
this is this is not valid uh can an EF
contract call a legacy contract uh yes
if you use x call and xstatic call it is
allowed uh in case of delegate call well
I guess replacement of delegate call
this is this is not allowed
uh can Legacy can Legacy code um call an
EF contract yes it is possible and the
intention there is that the existing U
proxy contracts can be upgraded to use
the UF uh implementations and also note
there that UF must not be enabled on
chains where uh the EF 00 prefixed bite
codes are not valid um EF so that's but
that's already taken care
of uh another modification is uh call
instructions got uh revamped to remove
the so-called uh gas observability
because it has been an issue uh before
and uh as of uh the UF upgrade at least
in that um UF version uh the control
will hold the Coler will no longer have
control over the amount of gas that is
passed as a part of the of function call
so that that was like one of the not
notable updates uh and certain other
rules were Kept For example the 63 64th
Rule and also Max call depth even though
it was considered for for
removal and a few other modifications as
well well how about uh support and
implementation uh to our knowledge we
are not devs we just like pretty much uh
we looking at publicly available sources
so far it seems like it's still in the
works it's implemented in some of the
clients but in some other clients it is
not fully implemented including G and
SLC so we didn't try as much uh playing
around with with this with these tools
yet but I think that this will be a
different completely different story
later and uh while checking uh while
checking for um materials for the stock
we found a few interesting uh tools
which uh include the the fer include the
some codee performance Benchmark and
also bite code parsers you have bite
code
parsers and uh yeah and some other
useful sources there are no uh URLs here
but let me know if you're interested I
can just share the whole slide so is
code size an important concern and does
you help redu code size what about
performance uh yes so we personally did
not do the analys is on that front but
uh we saw other uh teams did that so for
example that uh slide that ahead with
build bear uh Labs that did this
analysis and they did see the reduction
in uh the code size and also uh
Improvement to Performance I think
performance is definitely one of one of
the aspects so yeah I think that this um
this this is uh looking promising on
that front but it will be clear as we
have have uh more um I guess more people
look into this
topic great uh so what's the Viper uh
progress towards UF is it going to be
supported uh to be honest I do not know
uh but maybe if somebody who actually
you know looks uh works on that uh would
be be
good okay so uh what's the reason for
relative jumps instead of directly
indexing of bites in the code
array uh yeah so relative jumps in my
understanding uh give have certain
benefits uh so uh because it allows you
to actually write the code that is more
or less self-contained and encap
encapsulated so uh you don't always have
maybe you don't always care the absolute
location of the code but uh you pretty
much can reference other sections of the
code and also the code within the code
section
uh in a in a relative manner so I think
that this this provides this type of
benefit in my opinion great so I guess
there is uh already a PR for death which
is good news uh I really like the next
question what are the arguments against
e well the main argument we've seen uh
uh when looked at uh this U talk is just
a complexity right because it's a very
complex upgrade there are so many things
it kind of makes sense because the from
uh from Doos talk on Tuesday it's
basically been pretty much an effort to
try to make many changes all at once
because you cannot just do all this U
kind of u p meing the of the the changes
you cannot just simply do it without
breaking other things so it makes sense
to kind of have one major complex
upgrade and if you have the version in
along with it then you can pretty much
have that um done uh in a non-breaking
manner while continuing to have the the
Legacy code supported so yeah I think
the complexity is uh probably like one
one
aspect MH uh so for RS which invoke
transactions with an arbitrary gas limit
will that param simply be ignored post
UF uh yes so my understanding is that uh
maybe it will not even be allowed to
pass it but uh I do not know the the
details of how it's going to look like
from the developers perspective but yes
definitely it seems like the concept of
gas observability is to be uh deprecated
so it will be probably not uh uh not
possible to have to work with this
lowlevel Concepts as
gas M uh so uh the next question is
about Legacy op codes and I guess if
they are going to remove from existing
AV implementations which yeah my
understanding is that all the Legacy B
codes would still continue to be
supported right so you cannot simply
just you know completely remove it in
the EF uh format if your bite code
starts with ef0 that's a different story
right so basically you would have uh you
have uh um we have better control over
which op codes will be part of that uh
new upgrade it's a different pretty much
format uh yes uh from what I Rec call
from my slides there will be some uh
Legacy op course that are completely
removed or replaced with the
counterparts for for the removal for
example self-destruct right so finally
you can actually just well I guess
removal here means just not including it
in UF
that's great and uh what happens because
we don't have that much time uh what
happens uh if uh there is a legacy op
code in UF it's going to be rejected or
it's going to be in a runtime error uh
yeah so there is uh basically uh yeah we
looked at some interactions of UF and
Legacy bite codes and some interactions
are simply not even allowed so for
example you cannot deploy uh eoff or you
cannot deploy a legacy contract from a
EF contract and and vice versa so it's
kind of like they they draw the line
somewhere where you you only can go in
One Direction and uh there is some
disjoint um sets of uh uh interactions
that that are possible great thank you
again it was an amazing presentation L
let's thank Alex one more time thank you
so
much so our next talk will be about uh
um e of uh stack validation and we will
start in uh 3 to four minutes
okay so our next talk it's going to be
on uh EF uh stack validation and it's
going to be a deep dive into it h by
Andre so let's welcome
Andre hello everyone who could wake up
thank you for
coming uh this talk is about us F uh we
had a very nice introduction thanks Alex
uh in the previous presentation so
hopefully you know by now this is a
series of
proposals that aims at redesigning and
improving evm in various ways and um I
will be talking about one part of it one
EIP 5450 stack
validation stack validation is in
general one part of a bigger code
validation procedure that happens before
code is being deployed on chain and one
of the leading principles and main goals
of it is uh to get rid of repeated
checks during executing the same code
and instead if we if we can do the check
once before code is being deployed then
we do that and then assume it is
satisfied during uh execution and
then basically we can Adit the same
checks uh uh at run time for St
validation in particular this means
ensuring the correctness of every
instruction in the code and and in evm
as we don't have uh types of the values
on stack this simply means making sure
that none of the instructions overflow
or underflow the
stack and given that we check this once
uh at validation then we can omit these
checks from The Interpreter Loop and one
important consideration to keep in mind
when designing stack validation is
keeping its complexity linear in the
size of the code uh this is important
because we cannot afford uh having some
Rust case bite codes exploding
validation time and enabling dos attacks
with
that very high level overview of how
stack validation would work we go
through control flow of the graph uh
control flow graph of the code uh
examine every instruction and see how
many values it pushes or Pops from the
stack and keep track of what is the
current stack height if it ever goes
below zero we detect detect underflow if
it ever goes above St limit we detect
overflow and reject this entire code AS
invalid and do not allow to for it to be
deployed uh this sounds pretty simple
and high level and you might wonder at
this point how is this even possible to
achieve without executing the code
because we are used to thinking about
underflows and overflows as depending on
the runtime uh value of the stack height
and uh depending on whatever runtime
conditions on call data storage or
whatever I will show you that in fact
this is possible given that we impose
one extra restriction on what is allowed
in the code uh so let's zoom in and
explore how this would work this was our
initial approach to this problem um and
let's discuss underflows first uh
overflows are handled quite differently
I will mention this later so every
section is validated independently one
section at a time uh we Traverse the
control flow graph of the uh code in a
bread res search or depth search manner
meaning we follow every jump uh if it's
a conditional jump we follow both
branches of the
jump uh we keep track of what is the
current stack height for every
instruction and record it uh if it goes
below zero we detect underflow and
reject this code AS
invalid and one extra restriction that
makes it all possible is the rule if we
ever uh encounter an instruction that
during out reversal that was already
visited before for uh it means that this
instruction may be reached via multiple
possible code paths during execution and
uh in this case we require that the
stack height at this instruction is
equal for all possible code paths
leading to it so this is something you
comparing to current evm so this U makes
some of the patterns that were possible
in current evm uh invalid now in EF uh
as a practical
example for if then else statement you
would be required to have equal stack
height at the end of the than and else
branches for example or for Loops for
example the loop body is not allowed to
grow or Shrink stack these are pretty
reasonable restrictions to have other
VMS also have similar rules like jvm and
web
assembly and uh thanks to this rule we
just when we get to the branch that we
have already seen we just check this
condition and do not revalidate the same
Branch so in the end every branch is
validated exactly once every instruction
is visited exactly once so complexity is
linear for this algorithm which is what
we desired so this is great and one uh
extra rule that we have uh if after the
traversal is finished some of the
instructions are not visited it means
they are never going to be reached in uh
execution and we do not allow this we do
not allow unreachable code to be
deployed and reject and entire bite code
AS
invalid I'll show an example now how
this would work
so here's the simple code uh we'll need
an array of Stack Heights for
instruction and work list here is a q
like data structure that keeps track of
which branches we have yet to validate
so we start with the first Branch at
offset zero uh push instruction would
add one uh value on the stack uh then
call data load doesn't change the stack
height then this conditional jump
instruction has two possible successors
at offsets 10 and five we add them both
into the work list and at this point we
also have to record the stack height uh
at both of the targets stack height is
zero after R jump I so we record that at
both offsets and continue then with the
next Branch from the work list we go to
offset zero there there's a push and
another push then as store checks
whether it has enough items not to under
underflow uh two is exactly enough for s
store so no underflow happens we are
good here and we continue uh this stop
then validates uh uh concludes
validation of this branch and we have
still one branch left to examine at
offset five we go there there's another
push and then another jump into the
Target that we have already visited
before at this point we have to check
whether current stack height is equal to
what we have recorded for this target
before it was one previously and stack
height is also one for this after this R
jump so 1 equals 1 and uh so this is
valid we do not revisit this Branch
anymore and then we do not have anything
else in the work list and this concludes
the validation this code is valid in the
end compare this to this invalid code it
is very similar but with one push
emitted uh so it goes through very
similar steps and ends up at this R jump
instruction uh and at this point stack
height is zero but we have seen stack
height one at the Target before and so
they are not equal and this means code
is invalid and
rejected so this uh exact restriction
that makes it all possible uh turned out
to be problematic in some important
cases so this code like on the slide uh
can be commonly generated by solidity
for example when you have a series of
required statements in solidity every
require is a check and revert in case
it's not uh satisfied and then uh
solidity Optimizer at some point
extracts these reverts into a common uh
code uh common code block and uh then
each requ require becomes this check and
the jump into this common code uh so the
problem here these uh requires and these
checks and jumps can be located at
arbitary points in the function code and
at arbitary stack Heights and this goes
specifically against our rule that stack
height must be equal at
every every jump into uh common
code uh compilers could deal with it
with some workarounds for example they
could insert some extra po instructions
before some jumps to equalize this stch
and make it equal for every jump into a
common code but this would mean
increased code size and increased gas
consumed so this entire optimization
might not be worth it in the end or
another workaround could be to take this
invert and make an uh separate code
section out of it and call it from here
this would also work but this also has
an overhead of um putting declaring this
extra code section in the UF header
putting its metadata into type section
so in the end code size also is
increased and we might have some
regressions comparing to current evm
this is something we really would like
to avoid uh and this is just one common
example it's not the only one in general
compilers are very much um uh in favor
of being able to jump into some common
uh helper code blocks from arbitrary
stack
Heights so we found a solution to this
and this is current spec 5450 and final
one uh so we have to modify our
algorithm somewhat in some important
ways uh uh we start with allowing
multiple possible stack Heights for
every instruction instead of uh
recording just one stack height value we
record uh the range of Stack Heights to
minimum and maximum for every
instruction we change the way we
Traverse the code instead of uh depth
for search or bread for search reversal
we just do a sequential pass through
through the code uh front to back just a
simple Loop we do not follow jumps when
they see them instead we handle jumps
differently depending whether it's a
forward jump or backwards jump uh so
depending on its relative offset and
this is known at validation time because
EF has static jumps instead of dynamic
jumps so we look at this offset if it's
a forward jump we always allow it and we
just record the stack height at the
Target uh
instruction if we have already visited
this uh we have already seen this target
instruction before we expand the stack
height range of the
Target and this specifically fixes our
problematic case
um we always allow these jumps into a
common code and thanks to sequential uh
traversal of The Code by the time we
reach the validation of this common
helper we have already seen all forward
jumps into it so we have seen already
all stack Heights at all of the jumps
into this common uh uh code and then we
validate it using this uh stack height
range that we have observed so this
fixes the problem and um as for backward
jumps uh we still keep the exactly same
restriction as before we require equal
stack height at the jump instruction and
at the target of a jump this means that
Loops that grow or Shrink stack are
still not allowed this is pretty
reasonable restriction to keep no
compilers generate such Loops anyway and
so they are fine with
it uh if this backward jump is in fact a
jump into a helper not a loop uh it um
this code always can be reordered in a
way that jumps into a helper is a
forward jump so this is kind of an
implicit requirement to put on the code
ordering for compilers to and this is
always can be done and so compilers are
fine with
this if we see a regular instruction
which is not a jump we just modify both
ends of the stack height range both
minimum and
maximum uh stack underflow is checked
viously using minimum end of the range
and one extra restriction on or one
change in how we Define unreachable code
this is very much related to backwards
jump rule that I have already mentioned
just now so we also uh expand a bit the
definition of what is unreachable code
if some code is reachable only via a
backwards jump we also consider it
unreachable now this is needed to make
this sequential traversal
possible and this is all also always uh
a achievable by compilers they need to
do some kind of topological sort
ordering of the basic blocks in the code
uh and uh it always can be done uh so
this restriction is fine some other VMS
also have similar
Rule and um also because uh we have this
simple Loop over all instructions every
instruction is visited exactly once so
we are still find complexity wise
complexity is still
linear I'll show an example how this
would work now uh so we'll need an array
of two arrays of minimum and maximum
stack height or array of
pairs uh note that we do not need a work
list here because it's just a simple
Loop uh over instructions so we start
with the first one push uh is a simple
instruction that modifies both minimum
and maximum so 0 to Zer becomes Z one to
one call data Lo doesn't change it then
this conditional jump uh it is a forward
jump so it is a load and we have just to
record the stack height at the Target it
is zero after jump so we record 0 to0 at
offset
X um uh then we continue with the next
instruction this is yeah another push
and push and C load and then another
conditional jump that targets the same
offset that we have already seen before
at this point uh stack height is one
after R jum pi and we have to at this
point expand the stack height range that
we have seen at the Target before so 0 0
becomes 01 then we have a stop with an
extra value on the stack this is allowed
and valid and then we get to this Branch
this is interesting Branch because it
has multiple possible St Heights it can
be either zero or one here then push
would modify both minimum and maximum so
it shifts the St height range uh 01
becomes one two and another push and
rever checks for possible
underflow uh uh using minimum and two is
exactly what revert needs so no
underflow happens this code is valid in
the end this concludes the validation uh
note that this code is very similar to
the problematic case uh that I showed a
couple of slides before this is like a
common helper that reverts and a couple
of jumps from different St Heights into
it uh so given this algorithm uh
concludes successfully uh we are
guaranteed that no underflows happen at
run time uh ever at all uh and we can
completely Amit them from the
interpreted Loop this is not the case
with overflow checks uh we cannot remove
them uh completely but we can minimize
how often we do them and not do them for
every instruction uh as current evm
does uh so to make this uh work we start
with the with what previous underflows
uh validation algorithm gave us we
recorded stack height at every
instruction in this algorithm and we can
just find maximum of these stack Heights
and this value value is going to mean
maximum stack height value of this
functions frame if this value is above
stack height limit it means execution of
this function May overflow and we reject
it immediately at validation we do not
allow it to be deployed uh if it is
within the limit we record this maximum
stack height value in this functions
metadata in the EF header and then this
value is used for validating the calls
into this section and also at execution
time when we execute call F or jump F
into this uh function so in the end we
only have to do runtime overflow checks
at two uh locations in the code for when
we execute call F or jump F we get the
current runtime stack height we add it
up with maximum stack height of the
col if this sum is above the stack
height limit we do not allow call f a
jump F we exceptionally abort at call F
or jump F otherwise U um execution could
overflow execution of this uh eof
function so this is how overflows are
handled and uh one final thing that I
wanted to mention is non- returning
functions and jump F these are defined
in their own EIP but they are closely
related to stack validation and
partially motivated by St validation I
would say so non- returning functions
are those that do not return control
back to a caller they do not execute red
f
instruction or you could think of them
as functions that and entire contract
execution with instructions like stop
return revert
Etc uh how is this relevant to stack
validation um so when we validate a call
to such a non-returning
function if there's some code
immediately following this call uh this
code is never going to be executed at
run time because this call is non-
returning this means that we do not need
and we should not validate this code
following the call to non
returning instead we should uh consider
it unreachable and reject it as we do
with other unreachable code uh so to
make this work stack validation has to
detect calls to non- return functions
somehow for that we have a special flag
in the EF header in the functions
metadata so when stack validation uh
detects a call when it sees a call it
checks this flag whether it's returning
or non- returning if it's a call to non-
returning function it considers this
call to be a terminated instruction and
then uh in the end then if there's some
code immediately following it it it may
be unreachable unless there was some
previously seen forward jump into it so
this is how it works what's important
here is that calls to ret return in and
non returning functions are validated
very differently so for calls to ret
return in functions you have to take
into account how many values were
returned put them on stack and continue
validation and calls to non- returning
adjust terminating instructions given
this difference I would say it uh a
separate instruction for call to return
is already Justified so this is exactly
what jump F instruction is if you need
to do a call to non return function you
uh use jump f for that call F to non
return is not allowed in
fact uh jump F also has different use
case it can be used with returning
functions but uh this does not fit this
presentation but you can read more
details in the EIP or some discussion at
this another
link and this is what all that I wanted
to say about this thank
you thanks a lot that was a very
interesting presentation so let's start
uh with uh the questions uh the most
popular one is um uh Cod stack
validation allow translation to a
register based instruction set
internally reducing dispatch overhead in
The Interpreter
loop I think definitely it
can any any translation is easier uh in
EF given that we have we do not have
Dynamic jumps that's the main reason
that we can do jittin we can compile to
whatever backand uh it's yeah there are
various ideas about what eoff can be
compiled to uh uh not
yeah interesting topic yeah okay the
next question is since STX size can vary
with recursion which is only known H at
trans time how can this method ensure St
stack Overflow is detected
statically good question so it is we
still uh uh require runtime checks for
overflow we just don't do them every
time at every
instruction so uh the recursive calls
will still do the Overflow check when
they do a call a call or jump off
instruction and in case uh this call May
overflow this call is not going to be
eded so overflow checks are not checked
completely statically that's that's the
answer great uh so the next question I
think uh in the beginning you mentioned
that uh some compiler optimizations
won't be worth it so I guess uh which
compilers optimizations might be worth
yeah so I refer to this one specific
case that uh was pretty common for our
uh initial idea of Stack validation uh
that where uh the optimization that I
meant was uh the application that
solidity compiler does when it sees uh a
similar code at at multiple uh points in
the bite code it gets them and extracts
them into a common Helper but like with
the first algorithm there was some
overhead and in the end this might not
be worth it and because code size in the
end may increase and gas also
increased MH uh so uh what does uh why
does this need needs to be part of eof
instead of just relying on the compiler
to H uh to handle stack access
efficiently
interesting
um well I would
say there is a value definitely some
value in ensuring stack correctness of
the bite code
itself uh because it can
it B code itself then can be audited or
can be formally verified can be
statically analyzed so like validation
and validation in general uh uh
simplifies these tasks and uh uh
immensely I would say so that's the
answer I think so if it wouldn't be
enforced on the protocol level
then high level uh the same only the
high LEL Lang language code would be
available to
uh to use these benefits I think
so makes sense uh so the next one is uh
if the code passes uh stock range
validation um is it possible that there
is a code path that uh under overflows
the
stock there is uh possibility of
overflows but not underflows that's the
answer yeah um underflows are completely
eliminated thanks to static validation
at at uh deployment time and overflows
still can happen but uh we do not need
to check them at every instruction as I
as I said MH uh and um the next question
is uh if a St validation makes uh ZK
cross compilation or ZK Trace
aromatization easier or
harder it definitely makes it easier if
in case this ZK compilation targets e
only eof and does not try to support
Legacy 2 in case it is ZK system that
tries to support both Legacy execution
and EF execution then it has to
basically support two different systems
that is big pain I guess so it's
generally much better idea to support EF
for them and uh
then thanks to uh code validation and
thanks to
uh deleting codee observability ZK
compilation becomes much easier that's
at least the theory and yeah we'll see
how this works
out okay and uh I guess last question uh
will gas fee reduce after this
optimization and if so how much so
there's no exact plans to reduce gas but
uh we definitely will see some uh
improvements in in in execution time and
this might lead to some optimization in
future uh there will be gas savings
thanks to better stack management this
is like not uh specifically related to
validation but rather to a better just
better instruction instructions to
handle values on stack uh we have now
Swap and d and exchange and all this uh
simplifies life for compilers and in the
end reduces gas consumed for entire
execution great how much can I
say uh let's thanks um one more time
speaker
and and we will be back shortly for the
next presentation which is going to be
about evm Max um that basically is an
extension built on top of EF that
enables fast modular arithmetic in evm
without the need of pre compiles
speaker name r
Rik Ric
think
hello again so if uh anyone just arrived
if you have any questions please can the
code that will be right there next to
the presentation so our next speaker is
Rod and he he's going to talk about evm
Max and extension on top of eof uh let's
welcome our
speaker welcome everybody I'm Ric from
from IPS research and development team
at ethereum foundation and today I want
to talk you about some uh some extension
we we're going to add to the to the
interium virtual machine uh in the near
future so the idea has a couple of years
already and it was initiated by some
cevs to uh to improve the way how the
cryptography is handled or cryptography
related functions are handled on the in
the in the evm the main reason was to
avoid adding or limit limit the need to
adding new pre
compiles yes so but before we get into
the details I would like to make some
simple introduction and explain the
reasoning behind evm
Max so what's the evm max so evm max
translates to EV interium virtual
machine modular arithmetic extension
it's a set of modular set of a new
modular arithmetic instructions which
support every sized C which is important
OD modules at the current spec we Define
uh addition subtractions subtractions
and multiplication we also consider
adding
exponentiation is a helpful uh for
calculation some more advanced uh
modular arithmetic functions like
modular inversion or square root one
every important thing uh uh which should
be noticed here is uh that in this
proposal that this proposal is built on
the top of the evm object format which
we had just a presentation of uh in a
minute and also there was one
presentation made by Dano uh on
Tuesday uh so um yeah so evm max makes a
usage of e e immediate arguments and the
validation of the immediate bite code
also and it makes uh it possible to
validate evm Max code before before the
deployment of the contract to the to the
chain um but I'm not going to get into
details of the of this validation
because it's not the the the the main
topic of this uh of this uh presentation
yeah but it's worth mentioning that uh
eof is a crucial dependency which makes
evm Max easier to implement in an
efficient way it doesn't mean that EV
eof is uh is a dependency which has to
be before it just makes the
implementation tvx much easier in an
efficient way so but uh where exactly
evm Max is located in the in the
cryptography related uh evm evm stack so
we have a basic operations in the
modular arithmetic on the on the bottom
level which are used to implement the
second level uh the elliptic curve
cryptography Primitives like Point
addition multiplication and sometime and
and more advanced like piring
verification and these Primitives are
used to implement ECC
uh algorith like signature verification
and ziker related functions but evm Max
implements only the bottom one level of
on this diagram the Epsilon team we also
uh use evm max to implement the second
level to make sure that the set of
instruction of VM Max is uh offer the
and the API offer uh right abstractions
right abstraction and
efficiency so so um
sorry too fast what is going on yeah
okay so we know uh we now know what evm
Max is in
general
um
some so one of the reason I already
mentioned at the beginning of the
presentation but there are a couple more
reasons I want to list so in aan
community there is a need to make the
implementation of the cryptography uh in
evm much easier and efficient
why it's
getting uh mus inefficient uh
so yeah so with VX we won't need to wait
for a specific uh promiles to be okay
thank
you to be delivered in a in a fork we
also would like evm Max to be a tool
which allows to avoid adding new
promiles in the future it will make the
cev's lives much easier because they
won't need to uh maintain the very
specialized cryptographic libraries in
the evm so they they will not have a
headache like uh what exactly this
function do I'm not the cryptographer
exactly or we don't have a specialized
cryptographer in the team so why do we
need to to to to maintain this
complicated libraries which we take
basically very often from some from some
external libraries which are already
implemented but um so evm max will
deliver a tool which should make
precompile specification also possible
in the evm max by code so we can imagine
if the promiles for some reason will be
still needed to to be implemented and to
use by the evm we can imagine that the
evm Max B code will will can define a
specification of the promiles how they
should be implemented
exactly
yeah so but let's get little bit deeper
into the evm max instruction details so
uh we can split it into three different
U three different parts so uh the first
part is uh just uh is responsible for
setting up the uh the evm max context
the second one is just the set of
modular arithmetic instruction I already
mentioned and the third one is uh
responsible for evm evm Max context is
communication so so let's get into DET
Tis of these three three three parts so
first uh set upex creates the evm max
context if it doesn't exist yet which
means it initialize modulus values and
allocates evm max value slots in the
dedicated for evm max memory only these
slots can be only accessed by the evm
max op of course and also initialize
some specific uh constant values like
for example R squ which must be which is
used for uh which is used by Montgomery
Montgomery form
in this context if the context is
already defined so the setup X just only
switch to this to this to this already
defined
context second part are the arithmetic
instructions so basically um they uh
perform the arithmetic operation
according to their names as you can see
so everybody who uh who know a little
bit about the the arithmetic modular
arithmetic should uh be able uh to know
what's what they exactly do but it's
worth noticing that they operate only on
uh indexes of the slots in the evm max
context and the indexes are static and
can be validated on the deployment uh uh
before before deployment of the contract
to the main net which allows to validate
them us exactly the same way as all the
uh all the immediate arguments in the
eof uh are validated
and the last but not least part uh is
there are are two instructions to up
codes responsible for loading soaring
values from and to uh evm Max context
they allow to initialize slots values uh
using evm evm memory and loads result
back to the evm evm memory because we
allow only uh we allow any size of the
modulus C of course but any size we
transfer Valu from and to evm memory
instead of uh instead of evm Stack so
this is this is the set of uh evm Max
instructions and uh but of course it can
be extended or changed as the proposal
is still in the design stage sorry I
need to take some
water yeah so we have uh we have a this
set of this five instructions which are
quite simple
um yeah so as I mentioned U earlier
about the promiles uh they have some
downsides I'm going to I'm going to to
to present also uh yeah but let me
explain what exactly I have in mind so
at first um they are all implemented by
many different libraries in in different
languages across all the execution
execution layer clients this means that
they are potentially Vector of attacks
on the client
and on the consensus of the chain
moreover the IPS proposing new pre
compiles cannot spec out the
implementation details details of them
because the implementations differs
differ the implementations differ
between the between the clients as a
result of this very often uh promise
implementation need to do some redundant
operations to make sure that the result
will be exactly the same for all
possible implementation
of the of the promiles so because if the
if the result will be different we can
have a basically if the result for the
same input will generate different the
for will be different it means that uh
that basically we we we have a consensus
problem yeah because we we get we get
different results for the same input for
the same promile on a different on a
different
clients uh and we have even uh recently
recently very intensive discussion about
uh about exactly this this problem when
when uh finalizing the spec of the of
the BLS promiles which is going to be
introduced in the in the in the upcoming
Fork yeah so um and let me show you one
example very simple example of the
precompile which already exists um it's
a it's a point addition on bn5 254
elliptic curve and I'm just going to
present you a simple formula which is
used to add two points on elliptic curve
not going into details because they they
it doesn't matter how they how the
addition is defined and why it it's this
way the formula is quite simple we've
got two points on elliptic
curve uh we first check that the x
coordinates are different of of them are
differ different and if they are not we
switch to the special case which I'm not
going to present because because it's
very similar and doesn't change anything
in what I wanted to focus on here
assuming that the points have a
different x coordinates we calculate the
slope of the line intersecting these two
points and based on this we calculate
third point where the line intersects
the the elliptic curve the point
addition definition tells that at the
last step we have to negate the
y-coordinate value to get the final
result this is the definition of of the
point addition on the on the elliptic
curve uh for this exact case when we
have a different x coordinates so uh
this is a simple formula very simple
formula and formula and uh let's focus
on what and how many operation we have
to do uh to calculate this so as we can
see we have a like six abstractions
substruction and two
multiplications uh which are basically
the operation which we already have uh
in a set of uh of the evm max
instructions but there is a one more
additional uh additional operation which
is the division and basically uh it's
it's marked with the with the red color
so but let's get deeper a little bit
deeper um what uh what the how how the
division uh can be calculated in modular
arithmetic so as you expected it's very
expensive
and it's uh it's very expensive and if
you uh if you use some well-known method
to calculate this using adchain for
example tool it requires about 300
multiplications so comparing to six we
have uh sorry two multiplications we
have on the previous slides it's
in the arithmetic uh in modular
arithmetic but the good thing is that in
real world we want to uh we want to add
more points to do
this sorry so but in real world when we
are adding more points so the sequence
of points uh we will we never uh make a
division every every addition we we do
so so like no so every two points we
don't do every division uh at at any
step because it can be it can be done in
different way which allows to make one
division at most if ever needed if if
any needed so so with VM Max we would be
able to implement the points addition in
the optimal way without redundant
operations and return the results in any
form needed for a specific case so yeah
so sorry let's get back to this slide
once again so the the the solution one
of possible solution is just to use in
different coordinate system like for
example projective for jaob coordinate
system but also there are uh algorithm
who which add a sequence of points uh in
aine coordinates and you can make a one
division in the
end so but what are the benefits of e
Max over promiles first of
all uh we improve efficiency because of
the reason that I already mentioned we
have also more flexibility uh because we
can implement the cryptographic algorith
according to the specific need needs we
also improve security as we mitigate
potential consensus risk the complexity
of the precompile implementation details
is moved from the evm to the smart
contract and last but not
least again project can and last but
sorry where was it okay and last but not
least project can deliver functionality
they need faster not waiting until the
specific promiles will be processed and
delivered to the
mine so as a summary I would like to
give you an update of what we did till
now so we prepared a bunch of aips and
more FPS are in progress we have an
experimental implementation of evm Max
instructions support in the evm one so
our project we um we develop from a very
long time and on top of this we
implemented a couple of promiles by
generating evm Max bite code and it
appeared that the implementation is
faster than implementation in libff
which is still being used by some of the
execution clients honestly Li is not the
the fast the fastest Library available
but but that it's still used to to
implement the existing pre compies
already by some some clients and thanks
to Jared from GF team we also recently
prepared a draft of of the specification
of the vectorized version of evm Max up
code which is a direction we wanted to
investigate in a as a potential
Improvement of efficiency of the
implementation of the posidon hash
function and smaller modulus
setup so what what we plan to do next we
need uh more use cases for sure to make
sure that uh that the spec is correct
and the API is convenient uh we plan
also to start supporting different
modulus which values which will which
will be the power of two some attention
also and research on SD s IMD
instructions is also uh sorry extension
it's also required to utilize uh this
extension if it gives measurable uh
measurable
benefits uh regarding the tooling uh we
work on supporting evm Max in higher
level languages like for example youu or
or half uh we haven't choosed yet which
one but now we are very close to very
close to to to start with fuel we plan
also to research the idea of using qvm
Max biteco as a spec language
as I mentioned already uh for the pre
compiles if they still will be needed
for any reason uh it should also result
in a tool to transpile this evm Max bite
code to higher level language so
opposite basically opposite way uh which
can be used as a precompile future
precompile implementation by the
execution
clients yeah so uh so regarding our
goals for the very near future uh uh we
plan basically the most uh the most
important is to finalize the evm max
spec then um then
uh
sorry yeah to finalize the evm max pack
then uh it when it's implemented it will
equip the evm in a cryptography friend
cryptography friendly tool chain and it
should minimize the need of adding new
pre compiles as I mentioned already and
uh make the evm more Z friendly we want
to be from the very beginning of the evm
existence almost and to introduce and we
plan to introduce this ideally after
Fork when the eoff will be will be
introduced so hopefully next year or
and and have more detailed questions and
we will not be able to ask it them now
uh this is the list of the people I'm
aware of who now work on uh on the on
the evm Max and this is ipsilon team I'm
a member of Jared from G and kevf from
RG ARG ARG team at
TF yeah so thank you for your attention
it's time for some question now if you
have
any thank you
thanks again for this very interesting
top uh talk uh so let's start with our
questions the first question is um is
there a chance that all these extensions
end end up being not enough uh what
about going in the opposite direction
and integrate something like wasm and
then implementing it uh at the contract
level yeah so uh it always can end up
with being not enough with there will be
some uh some use case which we uh
haven't covered uh when when uh when
designing the
instructions um but uh but yeah so
that's why we that's why we trying to do
all this all this use cases also the the
newest one ideas like Poseidon hash uh
like any others and uh regarding
quasm I think I'm not sure I fully
understand but uh but yeah so so the
wasm wasm idea to to to to use it to
replace evm evm was investigated like a
couple years ago by my by my friends
from ipsilon at uh I don't remember now
exactly the reasons but it was uh it
wasn't uh it wasn't finally appeared to
be a good uh to be a good
direction okay let's go to the next
so uh what the next one is the same one
so uh Eva Max is kind of another co-o
coprocessor why not just enable
restricted wasm kind of similar question
I guess H only signed the in sequence of
AD Mo store yeah yeah yeah that's that's
that's another so I okay now I remember
one one one one reason why wasm is not
uh uh not the best idea here first of
all uh while as far as I know uh but I
can be wrong doesn't operate on the on
the registers bigger than 64 bits and uh
and basically it makes the the
implementation of the of the of the
complicated that it can be done now in
the evm and uh and this also uh this
also means that
uh yeah so so basically this also means
that in the end when we when my friends
from Team were were trying to to use
wasm instead of evm it appears to be uh
basically less efficient than
evm great so is it a problem if uh
different implementations of a
precompile veryy in performance if so
how to avoid it so basically when we
have evm Max we will not have hopefully
we will not have uh new promiles anymore
anymore new pre compiles related to
elliptic car cryptography or uh or
basically to cryptography so we won't
have this kind of a problem but there is
a problem now with uh with with the
promi already and uh basically it means
that uh we when when when we uh when we
designing the gas schedule for the
precompile we just need to um we just
need to make it based on the less
efficient available implementation uh
available impation in the client
execution uh and layer execution
client okay so uh does adding new
instructions require a hard Fork a new e
version or both uh yeah it will require
hard for it will not require uh e
version bum bump mhm um are you
foreseeing any ways for uh anyone to
exploit uh these extensions in a non-
cryptography
way uh
actually I personally hadn't thought
about it but uh but probably
some some guys from ipsilon te will be
able to to to answer this question so we
are basically here so we can fight us
sorry because I I I don't I don't know
this
one can extensions like this be added
freely or is it bad to have H too many
extensions I guess something similar to
VM Max but for another Target uh
basically if if it will be needed it can
be add but you know the process the
process of adding new extensions is like
well know and straightforward you need
to propose it you need to fight for this
on a ACD calls and uh and maybe finally
it will be
introduced um so if implementing K Max
in another language I guess not see not
uh go or not uh
rust
um are there potential performance
differences
then uh yes definitely definitely it can
be it can be a per performance
differences in the implementation
between the clients uh like probably for
every other instructions which are
implemented in different languages
across the clients regarding that
yeah yeah so do you want to pick one
more yeah uh so regarding this this
question regarding SD uh it's it's a new
topic we haven't investigated it very
deeply but basically this extension we
plan to be used only for for smaller
modules like 64
bits which will probably make much more
sense
here okay um great thank you very much
and uh our next talk will be on rev yeah
let's thank our speaker one more
time so the next talk will be on revm
and we will start in about 5 minutes
our next speaker is dragon rakita from
the ithaka team uh he's working on our
evm and he's going to present what will
be the end game for uh that very
performant rust client let's welcome our
speaker uh hello everybody uh my name is
Dr rakita I got really good
introduction yeah uh in this talk I
would like to talk about endgame the
last step of uh Aran project it started
few years ago and I think I found the
solution that's going to last for a
while uh before that let's talk about
history uh and basic evolution of the
project it started in
basically go went to the seaside relaxed
a little bit and after I came back I uh
I did basically want to do some project
that's related to infrastructure wanted
to build something that use evm and I
started researching what's basically on
the market and there was like three
things open ethereum was the client that
I worked on before and it was GP license
so it was not suitable uh EV modm was
the new one it has some it's built by ex
colleague it has some experimental and
exotic rust night features and it was
like just interpreter so that sense it
was not enough for me SPN VM I was most
interested in it
and it was all the project all the evm
but it was not that maintained uh it was
hard to use it and if you want to do
inspection tracing you need to basically
build it in some different way and
that's very hard to
use so after making PR to the sputnic to
add some generics on the instruction
set uh basically after two weeks of no
response nothing and seeing the project
not moving anywhere I closed that PR and
made my own rvm in the month I had some
initial initial code that can be run is
PR if you want to look at
that but the end of 2021 I supported the
latest Forks uh state for test state
test for passing it supported the pre
compiles and the most important
interface for simple I wanted to have
for my experience open ethereum I want
to have evm where you set all the data
and say transact and then basically it
gives you the output of data execution
the database trait was the obstruction
that allows you runtime fing of account
storage environment was the way how you
set transaction block configuration
everything around it and inspector was
the good abstraction very powerful one
that allows you runtime inspection of
the your evm when you it it's
run G it's this PR it was optimized few
times but this PR was most impactful it
basically forx the the
performance uh it was no STD from the
start
uh IDE idea was to use it in
JavaScript or vas it was M MIT license
and by that year I basically jumped to
another project and RM became my
hobby first adopters came next year uh
fundry was the biggest one at the first
one uh the way how I met joio was he
tweeted if there is any EVMS out there
and I responded on the Tweet hey fresly
back if you're interested and he was in
the minutes my DMs that's Georgio he's
basically amazing in that
sense uh they started integrated a few
months I think the Oliver did the first
integration uh five months after the
start that was like March
last backand they published the this
year Builder surges was one of the big
uh users of the CL of the library and
they would the first one they sync from
the Genesis to the tip of the main net
and it was very nice to hear hey we are
sinking everything is
fine by the end of 2022 all Forks was
supported optimization was done RV MGS
was supported but removed by the end of
the year there is no traction a few more
optimization was done and most
importantly R the client started to be
made October 2022 at that point of time
I joined Paradigm to work on the client
I think I had H from the my open
etherium
times second year and R are mostly
basically focused on the client
implementation uh we needed to make
something stable and we did it very
fastly team was amazing I plan to stay
there just for a few months but I'm
still there now in itaka but did the
very same
team shanka and kakum were added and
time moved on this year red 01 was
released Big stability Improvement U it
was audited it was the the people like
it people wanted to use it it was it is
amazing RM on its own hit it own
Milestone it got audited uh it was
Community Driven by the six company and
it's buy gu gido basically the guy that
finds a lot of evm bugs uh there's blog
post if you want to hear more uh you
have got supported and start of the year
uh Z KVM become a
thing this year I could claim I feel
that's okay to claim that the rvm become
the be the most popular evm Library out
there and it's become the critical
component of of eum ecosystem there is
few types of the rvm users that I can
see they're basically clients and chain
R first Helo satellite client
TR uh as the execution clients there is
different chains Optimus scroll binance
polygon they all all interested to have
uh RM in their code or basically in this
sense red and in that connection rvm the
tooling both The Foundry hardhead are
basically using RM Builder cess they're
a little bit private but always in my
DMs are the big users of it and Z
KVM uh basically it became the standard
Library that's used in that field there
is even uh Grant by EF uh Foundation
that basically uh targets RM formal
verification with the usage of the risk
kvms this all affected the future of AR
even how I look at
it so the
problems first problem how to do AIP
testing how to do how to allow AIP
Champions to come to the code base
improve their thing implemented tested
in the fundry if needed and
basically do their own thing and do
their basically on their own time the
one of example is transient storage I
want just move on that bad uh in July 24
I got issue in GitHub hey can you
implement that that was one of the a
Champions that wanted this included in
Aran for him to test it in The
Foundry EP was not included in the any
hard Fork there is no even notion for it
to be included so that was mostly it few
months
after uh a got cied so it potentially
can be included in shangai but either
way there is not like strong
guarantee shangai happened y it was not
inside next har Fork Cancun July PR was
made for that AIP August it was merged
in March the AIP landed on minute
approximately four months before that
AIP should be made inside the clients
for the testing for the dam Nets and for
test Nets at the end
another example was
that Champions made were reasonable it
is from their point of view but the
question that I had is like should I
have started working on I right away
when I first request come it's a little
bit silly because I have different
priorities I cannot do
everything should I just merge PR when
it was made the question with that is
who is going to do maintenance who is
going to remove it if the AIP was not
included do I do it for every IP that
would be a lot of unary
code and in the end who is going to
maintain all of
that second problem with the maintenance
is uh how to add testing Dev uh
experimental features one of those I
always try to facilitate and enable uh
big project that depend of our evm to
give it support to give a to to make
Tech functionality happen sometimes that
there's like features U rust features
that basically enable those things as
configuration but sometimes if this is
only the evm project simple evm Project
R evmc r55 integration that require
different execution environment would
not be
possible and problem three is chain
support most of chains have small
difference and they're not like uh they
don't want to move away from evm a lot
they're most like new chains spec hards
new transaction types maybe few
aips but in general they're like small
difference from the main net main
TVM only way to do that previously it
was like to Fork the project and that
brings the maintainance issue and burden
of maintaining to
basically
repos so solution for all that is to
make evm framework I think that's the
the last stage of our evm and it's end
game what do you mean by that uh let's
make the code
extensible chain can use RM as the
library override the functionality that
they need uh add neutr section that they
need and just uses the library that
makes the core of the library same
across all the chains implementing newps
that are on the main net would become
easier and all the chains can just reuse
code uh tooling can create their own Uh
custom way to inspect maybe they need
more performance way maybe they need
rvnc needed new execution environment uh
new AP can be implemented and tested
separately uh and for example this is
the first look H have
basically I I'm not coming to the code a
little bit but yeah the main inspector
main Optimus inspector Optimus you will
have different types for your different
evm that you
need idea came uh initial idea came few
years ago I looked at TV and bomb and
they had like AR of functions and um
area of functions that was different by
Fork so my first idea was hey can we
introduce custom instruction and make it
like allow user to reimplement or add
their own custom instruction that idea
expanded so it's not just on instruction
but on full
logic and that full log function
overriding was the Handler from the last
year uh I think it was very great idea
but implementation wise it was like box
over pointer or function that was not uh
the greatest and more flexible
way uh I like the insights that I got
while I Implement that and the EV
framework uh it ruc two things it ruc
the generics on the data on transaction
block config and introduce it revor the
hand
in more trait like way so it's more
easier to
use few examples of that is basically
how how are basically of the optimism
that was the first uh that was first
chain that was included RM in sense of
the it was included as the feature it
was very like intrus intrusive with the
handlers it be I tried I succeed to
extract some functionality to handlers
but with EV framework uh that become
even easier currently it stands it's on
crate I still have work to do on EV
frameworking but it become possibility
another uh another chain is call that
did the similar thing on their own repo
just imagine like every evm chain doing
their own crates and having fundry red
or all the tooling support those ex
variants of
RM and all be tested all be done in
basically it eases the integration with
all the
stack the
split uh that was inside that the head
with Handler is there is split between
the data that currently context and the
Handler that is the logic part of RM
context contain transaction block usual
things it contains journaling state that
allows you to revert things when the
rever happen in the calls and it
contains database that fetch the runtime
data uh trans stor and Waring of the
account is all done in journaling uh
Handler on other hand he has four
parts uh valid dat that validates the
interaction between block transaction
and config config can config can have
chain ID that needs to be checked with
the transaction chain ID for example
prev validation do some warming do some
deduct the Coler balance do
um yeah
it it yeah change delegate quotes to the
state execution uh is little bit complex
it has two main Loops the frame is the
loop around the around the calls and
interpreter is loop around the bite code
basic
instructions and in the end we have post
execution that does refund of not spend
gas it reimburse the caller it basically
rewards the beneficiary and creates the
the outcome of the
execution in code uh as see context has
a lot of
generics and it allows you basically to
have it generalized there is some to do
to do spec needs to be made inside moved
inside configuration but in general this
is the the first view of the of the new
context in evm
framework validation Barre one of the
four stages in the Handler has basically
self contain it contains associate type
of the context and arrow a few factor
that needs to be
called uh other Handler types are in
similar fashion made and you can have
ethereum validation that basically does
the the ethereum specific
implementation many evm became become
just the context and the
Handler and to create your own evm this
is example of M evm it's still pending
and it's going to be changed in small or
maybe medium way uh you basically
specify everything you need for example
you have your context with some
predefined data the section and for
example are the structure inside rvm but
you can add your transaction liation on
it and you can specified the Handler
that has their own uh
functionality
execution uh AUM execu
has few field that are maybe
um they're interesting to people they
have pre compile provider and
instruction provider where you can
generate your basic list of pre compiles
and there is trade that you need to
implement for this to
happen uh on other hand this is example
of Inspector main evm is still work in
progress but idea is you will do your
create you create your own uh in
inspector types that Implement those
traits and you can just override it in
the end this inspector main uses the DB
and inspector
genics and this is how you use it there
probably going to be some helper
function that is allow a little bit more
um flexibility and utility but I want
show just example how this could look
it's
um yeah in the end uh I assume a lot of
users are going to come and Implement
their own evm or their own like
extensions and just use rvm in that
form uh I think that's it uh thank you
very much for H
me
and that's it
thank you Dragon it's really amazing
what you have man us to do uh all those
years with uh RM so let's start with our
questions uh the first question is about
testing so do you use any kind of
equivalent testing or basically
differential testing uh as part of of uh
your CI uh yeah on every PR state that
test around basically state test made by
thean Foundation the testing team and
it's like good first line of the defense
if everything is okay if everything
works other than that there is fuzzing
team fuzzing project that are running
the backgrounds by eum Foundation by I
think Martin R it from go evm lab from
go etherum but go lab I think is project
but yeah
it's there are few stages of the testing
done
mhm and this is based on every new PR or
yeah uh for fuzzing is done in
background not on every PR but the state
test uh running it in the on the web web
assembly some specific uh rust uh
Target uh running it on uh different uh
targets basically allows you to test all
those those things mhm so are there any
early architectural decisions that uh
you have
regret
uh yeah um think I didn't understand how
the calls and everything around that
works I still struggle with that I
didn't find a good fit on top of it the
frame and how the frame basically works
with other frames it seems it's nice but
the still need to land on the good
abstraction on top of it uh initially
the the calling a sub calling was behind
the basically you call your sub call and
stack became the problem so I needed to
move all that to the the loop so yeah
there are few of those
things the next question is uh if there
are any plans to natively support uh Z
kvms like sp1 because currently uh you
need to do some hicky but is to be able
to run them uh we should talk with them
basically EV framework is idea that
basically would allow and support
this great
um another question again related to zvm
so RM is now used on both CPUs and zvm
and these two environments have very
different performance profiles uh how
can you optimize for or the one or the
other or both in general everything is
Ras compiler so it what compiles
optimization of D basically on Ras
compal so the target is different Z kbm
use risk 5 while the CPUs has different
instruction set that are made more
performant in general I didn't I didn't
do the testing on on top of it so that
would be like good way to check those I
guess a followup here is and probably
you haven't check yourself and that's
more about the zg VMS but have have you
any intuitions that some uh llvm
optimizations might be better for zvm or
may be better to not use some
optimizations um compiler optimization
basically I'm not sure I didn't look at
it great uh so what is missing in our
evm to be more performant than evm 1 uh
I have some task in my backlog uh they
require basically testing every change
that happen on the performance side
needs to be tested measured then
validated that that assumption that I
made are correct so I need to look at
tail call optimization to check it I
need to look at the stack verification
if this extracted from the instruction
to before instruction the main Loop if
this is going to affect the
performance MH uh is it easy to add the
new new pre compiles yeah it was one of
the use cases that thought this say used
a lot and it was very easy it's one of
the biggest use cases of um how you can
extend easiest and biggest B to extend
rvm what uh the most interesting use
case that you have seen so
far
um Z kvms was really really
unexpected to be honest it just landed
it was like Hey it can be used in that
way I didn't expect that I made the nod
to use it in maybe front ends so that
JavaScript can be implemented on top of
it maybe it can be used in vasm as the
like some project that do that way but
zvm was like unexpected surprise and it
was amazing in general like thank again
our speakers Dragon for the excellent
presentation thank
you so the next talk will be on symbolic
execution for evm and it will be about H
evm basically uh it will start in a few
minutes thank you
is
n
h oh
hello so I can't reminder that if you
have any questions please use the QR
code that will be next to the slides of
the next presentation uh which is going
to be given by mate and he's going to
talk about hcvn
and how to start love symbolic execution
let's welcome our
speaker hi everyone uh I'm mat sa and
I'll be talking about hvm and symbolic
execution uh that we built together with
uh Lexi myself and Zoe uh we are part of
the uh Argo Collective uh that is a
recently spun out uh Collective from the
eor foundation um if you want a bit more
about the Argo Collective you can watch
our uh talk uh that was given
yesterday
so first of all what is this talk going
to look like so first I'm going to talk
a little bit about what it means to
symbolically execute then I'm going to
give a bit of an overview of hbm then
I'll explain how hvm can be used uh
within uh you know to to secure down
some of your um work that you have done
hopefully and then finally uh I'm going
to conclude this talk so uh first of all
what is symbolic execution so let's say
that your code looks like this um if you
try to do fuzzing on this code it will
likely not find the fault that is uh
marked by aert false which could be for
example something that drains your
contract or locks your funds or some
kind of negative event um so if you you
can keep fuzzing this forever
essentially and um nothing will happen
but if you U run symbolic execution on
this it will immediately hit the the
assert false and will give you the
solution the the the two indes that you
need to pass in to um to trigger the the
failure so this is a good sort of litmus
test of what uh symbolic execution can
do in comparison to to fuzzing of course
it can do more but this is a good
example where where fuzzing will will
not help you very much and syor
execution will definitely help you so
let's get a little bit more into the
details so here we have I used uh
traditional assembly I'm I'm I'm old
school uh I could have used evm assembly
but it's more or less the same so what
we're going to do here is uh I'm going
to Showcase a very simple uh straight
line program where we do a mo and and a
move and an ad uh with two registers so
here we have uh concrete execution on
the on the top and what you have is um
concrete values like one and two and
then the Mau will move the the value two
to um to to the a register and then it
will add uh four to this value and then
the final register state will be six and
two now um when it comes to symbolic
execution what it will do is uh it will
instead of initializing it with concrete
values like one and two it will
initialize it with a variable like V1
and V2 and then we'll try to execute
these instructions but over these
variables rather than the concrete
values and what that will do is that as
you can see step by step we um we have
the state evolve and eventually it will
end up with V2 plus 4 on the on the ax a
register and V2 on the on the B register
so of course if I substitute the the
concrete values into into that will end
up exactly where we were um with
concrete execution but what this means
is that I can um mathematically Express
uh what what is the state for any input
value right um and okay so that sounds
interesting where does this get hard
because this seems relatively
straightforward so it gets kind of hard
is when branching happens so here is um
a a program where we have a branch and
uh with concrete execution it's
relatively straightforward we have both
uh registers set as one then we're going
to check whether they are equal they are
happen to be equal and if they are true
then we're going to add five to the uh
to the register a and so the the the the
final U state is six and one right so
this is quite clear but when it comes to
U symbolic execution we we don't know of
course what the value of a and b is uh
we represent them as these symbolic
variables V1 and V2 and we need to check
for both potential uh execution paths in
this case when uh V1 is equal to V2 and
when V V1 is not equal to V2 and we'll
end up with two different states
potentially in this case we do actually
end up in two different symbolic States
in one case B1 uh has is incremented by
five and in in um in uh in the other
case B1 is incremented by four of course
again if I substitute the con concrete
values in then I'll get exactly the
concrete execution however what this
means is that now we Branch so now we
have two states and if if there's
another Branch then this can become of
course exponentially large number of um
exponentially number a large number of
of of potential end States um if there's
a loop of course that can be if it's
infinite Loop there it's not a bounded
Loop then you can have issues with this
thing never terminating because we don't
actually know you know if if ever the
loop uh condition is is reached and so
we can potentially Run
Forever um so I'm just going to talk a
little bit about what other uh symbol
execution uh systems are out there
before I jump into hvm um first of all
there's there's more or less two types
within this ecosystem as far as I
understand one of them is um you have a
static uh code analysis engine and now
you want to validate whether some of the
things that it spits out are uh
potentially false positives and in this
case if the symbolic execution engine is
not complete or doesn't understand
everything it's kind of fine because
what you'll do is you'll just simply uh
spit out the the the potential false
positive and let the user deal with it
um and that's fine but in our case we
actually don't use the static code
analysis engine as a as a as a precursor
to hm so we actually have to deal with
everything that uh the evm has to offer
um and uh so it's a bit more complicated
and it's also more complete of course uh
so these purely symbolic execution uh
framework based systems there is uh
there are number uh this seror approver
which is based on this uh backwards
exploration and and weakest PR condition
computation there's ebmc which is of
course as the name suggests abound in
mold Checker type system then there is
halmos U it's written in Python and then
there's a then there kevm which is based
on the K framework and allows you to
break out into into K in case uh you
need to prove some things for example
Loop termination or invariance and
things like
that um so just a bit of an overview of
hvm so it started a long time ago as
part of the DAP tools project
um it implements the evm semantics um
both concretely and symbolically and
actually idna fuzer if you know about it
it uses hvm underneath uh for the
concrete execution semantics um it uh it
is um possible to execute uh any any um
uh call from any potential state in the
the evm so it understands um a lot of
like all of the evm in terms of like for
example calling out for to an RPC to a
to an an archive node to fetch State uh
Etc um it runs it basically computes a a
query to an smt solver runs the smt uh
uh runs the smt solver to to get the the
response to the query and then
interprets this response and uh sends it
back to the displays it back to the user
in a in in a in a fashion that is um
more user friendly than some SM
uh output we'll we'll see that in a
moment um so there are two ways of using
hvm one of them is uh for counter
example generation and one of them is
equivalence checking so let's talk a
little bit about this uh counter example
generation for um um in this case and
and some kind of post condition that
typically is written for example in in
in Forge test case as a Forge test case
um so here we have solidity Viper
whatever language you prefer or even
just pure evm bite code and that gets
interpreted uh by the by the internal um
um symbolic execution engine inside uh
um symbolic interpreter inside uh hbm to
produce an intermediate representation
and then this intermediate
representation together with the post
condition that you put down uh gets
compiled into a logical formula that
gets sent out to the smt solver and smt
solver is what's called a sub Model T
solver so it understands for example bit
Vector arithmetic which is quite useful
because of course there's this 256bit
bit vectors or variables in in in evm
that evm operates on and then either it
proves the property U finds account for
example or times out of course that's
always a potential possibility um when
it comes to a ex um symbolic execution
for equivalence checking we do something
very similar but what we do uh
eventually is that um we try to compare
the two executions against each other so
you have bite code a and bite code B
let's say that bite code B is like a
refactored by code or something that is
gas optimized and you want to make sure
that it's doing the same thing as the
original one and now what this will do
is that it will try to act prove that it
is equivalent find the counter example
so some input or in state that where the
two contracts actually uh disagree or of
course there's always the potential for
timeout and um let's go a little bit
deeper into this kind of s execution
engine U inside inside hvm so it
operates on bite code which means that
we're not tied to any particular uh um
uh compiler we not even tied to
something like Ule for example um
understands all of the evm stack call
frame Stack Storage call data everything
um can as I mentioned it can actually
run at any point in the blockchain
history um and it is fast against the
concrete execution ICS of G in this case
um as mentioned like it has issues with
uh loops and recursions because of uh
this issue that unterminated Loops we
don't know when to stop um it has some
issues related to symbolic uh offsize
and memory copy this is purely due to
smt limitations and um doesn't currently
deal with symbolic gas so it basically
ignores gas when it comes to symbolic
execution um in concrete execution of
course it understands gas and we'll deal
with it and so Akida will be running
correctly in that
sense um so just a bit of the internals
maybe this is a little too small but
basically what it does is that it takes
in as an input the evm bite code then it
will um um Step by Step execute it and
Branch if necessary to build an
intermediate representation and then
this intermediate representation is
simplified in a generic way and there
are some specific simplifications
related to cat shck and arrays and maps
and things like that that are quite
specific when it comes to uh to how uh
the evm handles uh arrays and maps and
things like that so especially katak
which is very complicated to uh to put
to exactly represent in in smt and
eventually what happens is that this IR
gets compiled into a bunch of smt
queries and these smt queries get
dispatched to the SM smt solver or
solvers um and then we gather all the
all the results from the some solvers
and then get the counter examples
extract them and and and map them back
to the query that was originally
dispatched and see how how we can
display that to the user in a way that
they will be able to run this and and
and actually trigger the fault because
at the end of the day it's annoying to
get something like hey your problem is
faulty that's not going to help the user
but the user really wants some kind of
counter example so they can actually run
it and see how it is wrong and then of
course they can fix it or hopefully fix
it um so that's kind of the the high
level of the
internals um so let's talk a little bit
about this intermediate representation
I'm not going to go into the details but
that's kind of at the middle of this
whole uh box in the previous box that
you um that I showed so here's a simple
function right uh this will overflow uh
if if uh the variable that you push put
in is large enough in particular exactly
equal to 2^ of 256 minus 1 and uh B will
actually not be larger than a in this
particular case I'm sure you have uh
played around with this uh it's a very
trivial uh overflow issue and this gets
compiled into this intermediate
representation where we have a
proposition that a must be uh um smaller
than the A+ one right so I mean it's
very simplistic in this space but the
point was to make it kind of readable
and also human readable this can also be
compiled into a graph as you might
imagine um and uh it can be quite um
like understandable to a human how the
internal representation um Maps back to
the original code in this case it's
quite quite
clear um okay so I'm going to talk a
little bit about uh about uh how to
actually run this tool and what kind of
results you can expect so in this
particular case we have a forge standard
test that we're going to import
our contract is um is test and then we
add prove underscore in front of it you
will need Forge you will need uh Z3
which is one of the um smt solvers that
we we uh we support and you need uh hvm
binary that you can just download from
repository and uh you put down this test
and this test will of course fail again
due to overflow and the way you run it
is very very simple you just build with
uh the EST and uh run hvm test and it
will parse everything up and do its
magic and eventually give you a counter
example which is what you expect
so um this um is sort of the the base
way of using it um and it is as clean
and tidy as it looks on the on the on
the output I did not actually change
that or edit it or didn't even even the
the the spacing is is how it is so it's
quite visually uh representative of what
are you going to test and what are the
counter examples that come out if
there's more than common count example
there's going to be more than one listed
there so how does hvm equivalence work
uh here I'm just going to show a sort of
a a contracted uh thing uh it's a very
complicated uh code that was um someone
tried to uh use and here I just want to
show some of the edge cases but also
that we do power through the edge cases
as well so in this case there's uh two
codes and we want to know if they're
equivalent um uh you see that it it
makes a warning that we cannot actually
explore the whole thing in this
particular case due to a a call into
unknown code obviously we don't know
what's going to happen there uh like
what is going to get executed um but
beyond that it says okay well anyway I
power through like I'm going to ignore
these bits and pieces we have um 1.7
million end states that we need to check
for equivalence and then it says okay
well I try my very best there 93 of them
uh I couldn't do because of of uh this
memory uh that was a memory copy that is
that is symbolic I couldn't do two
because of timeout this actually had a
and eventually I couldn't find any
discrepancies given these warnings and
and and uh things that I couldn't
actually explore uh and if you have a
look this actually ran for like 34
minutes and 45,000 seconds so obviously
it was like uh a multi machine that did
this um so it doesn't like give up and
like error exit or something like that
it actually gives you a meaningful
output and of course this did actually
check 1.57 million end States so it
didn't uh it didn't do nothing even
though of course you can't completely
trust this because uh there are some
parts that were not explored as as
displayed
um right so I'm just going to give you a
bit of a references and and and pro tips
of how you might want to use uh hvm so
first of all of course there's the hvm
repository there's also a very extensive
user guide we have worked quite a bit on
it uh lately and uh it really does give
uh a rundown uh step by step how to um
the kind of outputs you can expect Etc
so it also explains for example some of
these warnings that here are of course
quite thirst because we don't want to
overwhelm the user in the in this with
output um just few Pro tips regarding
using hbm so I would uh recommend for
example using it for equivalence testing
the uh the the one that I showed you was
specifically done by one of the compiler
teams um who wanted to check if their
optimization or new idea uh actually
doesn't break uh the the the what the
contract is expected to do the compiled
contract is expected to do um so it's
quite useful in case you want to
refactor or if you want to do some gas
optimized codes can be useful um if you
write a lot of tests and eventually your
tests are going to be your specification
and that can be quite nice as a driver
for uh for maybe thinking about your
contract in terms of like what it's
supposed to do rather than what the code
says it's doing um and of course um I
encourage you to do uh test positive
tests negative tests and invariant tests
um um for example like a positive test
is what we expect for example somebody
types in I mean in a normal situation
not in a in a in in this one that
positive test would be you type in the
password uh and the password is correct
and you're logged in if you type in the
wrong password you're not logged in an
invariant pass an invariant in this case
would be for example in the space of a
blockchain would be that uh after
transfer the sum of balances is the same
right
um and even if EV just a note so even if
hbm test gives you warnings and and and
and shows you that some of the things it
couldn't do it doesn't mean that it's
useless in any way shape or form you're
not supposed to uh like complete
coverage is kind of a myth or something
we want to get to but it's very very
difficult and what you normally get is a
certain level of certainty and uh hvm
can help you improve this and and
Elevate uh your level of of assurance of
your contract correctness and at the end
of the day that's what we're aiming for
of course it'd be very nice to have it
all the way but this is
uh this I think is also very helpful um
especially because um it's more complete
than just a fast test so limitations I
think I've explained this before so
there's issues with loops there is
issues with recursion um and there are
some issues with complicated
mathematical expressions like
exponentiation modular division things
like that uh purely because it's
complicated on a 256-bit variable um for
future work we're planning to help uh
fix some of the hopefully fix some of
the issues regarding recursion and loops
with some form of CHC and um potentially
hopefully we'll help some some some
better uh jump desk handling but also
maybe EF will help with that um so in
case you want to there is of course the
the um the QR code and uh check it out
have a look see what you can do it
should just work out of the box with are
currently running
tests thank you that was an excellent
presentation can you come a bit forward
oh yeah sure okay so let's start with a
questions uh is uh hm better than other
tools such as CA or halmos in terms of
compatibility with Foundry easiness to
use Etc so I guess it's a more devx
question okay um I would not compare it
necessarily to Cur Cur has its own
verification language it's a
multimillion doll company um it's a
different ball game altogether um um I
would I mean but nevertheless actually
hbm does very well even though I would
say from the perspective of what it's
supposed to aim to do is slightly
different of course uh we don't have a
specific I mean not a specification
language per se we have these uh test
cases which eventually become your
specification
um regarding halmos I mean I really like
halmos uh so I I think um it's always
fun to have more than one uh tool
available for doing whatever you want to
do not only because you know if one of
them doesn't work you can try the other
but also because the two two two from a
development perspective of the tool
itself um of course it's nice to see
what halmos is doing and recopies
something from them and then they copy
something from us and that's a what's
called cross pollination and this this
is very normal in any field including
scientific Fields so compare I I I I
don't know I I'm not a big fan of this
kind of competition mindset I think it's
nice to coexist and and work together
and I'd like to do that with both Cur
and H yeah uh so the next question is uh
if we should avoid loping code or in
more General how can we write code in a
more verification friendly way yeah good
question uh yes no Loops please I mean
in in general not a good idea to have
unbounded loops because it can run
forever it will eat your gas um you can
hardly reason about it in in a you know
from from like what is it actually going
to do um so I think it's not a great
idea to have uh unbounded loops and you
should minimize the number of Loops you
have in general in your code um
I mean that also goes for recursion for
the same reasons um um yeah I mean you
can there are ways of K like K evm uh
can can break out and and you can try to
write some invariant and things like
that um hopefully we'll be able to do
something like that maybe with some with
uh including the loops into our ir and
and maybe we'll be able to do something
with that too that' be very fun and
interesting but in general you know
you're not only making our life harder
you're also making your own life harder
so perhaps avoiding it is the best way
to go the next question is uh how do you
deal with the path explosion
problem um we compile 1.7 million
queries and run them in 34
minutes that's I that's the best way I
can talk about it because enough in the
end of the day you know it will happen
but uh you power through it I mean
um how does c do it they have a a form
of server and then 1.7 million quers get
run in 5 minutes instead of 34 minutes I
mean you can also do that with hbm it's
not a big deal um at one point it's
going to be pretty cheap to do that
relative to how much money you're going
to lose by not having it MH I guess the
next questions can be maybe answered in
one go so oops uh is there any reason to
use Z3 over cvc4 CVC 5 do you use
multiple SMD solvers yes so actually I
don't know if it's publicly at but there
will be very interesting tooling
regarding you know what is best um from
the halmos team I'm very excited for
that um I personally of course am a big
fan of bwoods law and the team Behind
bwoods law I know them and I trust them
and I like them um um I also like Z3 if
you know Nikolai um it's he's he's a
very uh he's very good at what he's
doing so I have I I'm still on the side
of collaboration and and friendly
competition and so anything Works
anything as long as it works I'm happy
um so you can use actually any solver
you just do minus minus solver and uh do
your own thing you can also add your own
if you like um you can even add the
wrapper and then uh run any smt solver
instead of you can even write your own
like I think now even STP might work
like I used to write STP so um although
I was not very good at it but I did I
did I did also contribute to STP so I
last question how hard are your chak
constraints are on the solver um we use
an inter the the of an interpreted
functions to deal with katak that's the
best way I think to deal with this
particular issue um I'm not going to go
into details because we're running out
of time but basically KCK is a very
complicated function and and
representing it exactly is a very bad
idea so we and I think many others using
an interpreted the theory of
uninterpreted functions to deal with it
it has some downsides and it can be
problematic but if you do a lot of
rewrites on your maps and arrays uh
actually they can also completely go
away so with a good simplification
routine and um and
um the best potential way of of doing
this kind of uh use of uninterpreted
functions to deal with katak I think uh
we can get there it can be an issue but
I think um with some luck and and with
perhaps even better rewrite rules uh
it's not such a big issue great let's
thank mat one more
time so next we will have uh a few
lighting talks on eof and uh those will
start in uh two to three minutes
you oh
oh
hello again
uh our next uh speaker is pav and uh he
will uh discuss how uh a eof affects the
development of infrastructure and tools
for smart contracts and special evm uh
speaker hello everyone my name is PA I'm
from tend
I am working as a software engineer and
leading the virtual machine
team
so the idea behind this talk is to zero
in on the effect of eof the ethereum
object format on developer experience
developer tooling and to focus primarily
on
debugging hopefully by the end of this
talk I will convince you that eof will
make it possible for the web 3 debugging
experience to be Miles Ahead in
comparison to web
to uh currently um there are many
debugging issues in regards to solidity
everyone who's ever written a smart
contracts knows how hard it is to debug
it during
development and after it goes into
production broadly speaking uh issues
could be bucketed into two groups one of
them is the fact that we are lacking
appr debugging format and the other one
is the fact that you could
execute optimized and unoptimized
versions of the same contract and get
results these two issues are in a sense
intertwined so let's say that you'd like
to debug a program in traditional
programming SL
web2 uh you would need to debug it using
the debug
release if you would use the the release
executable you would have much less
debugging info therefore you would have
much less data about the state of the
program at the point that you were
trying to
debug so the issues are that in order to
the exact same amount of data when
you're debugging solidity you also need
to debug it using the debug release SL
executable which means that you would
need to debug the unoptimized bite code
since there are differences in execution
between the optimized and unoptimized
bite code effectively you could have a
debugging session that's been running
locally where you've executed a certain
code path and when you replay that input
in production or in a local session
using the optimized version of The Bite
code you could get entirely different
results the main culprit behind this is
the galop code which is being executed
every time there there is a call and
which can also be injected into the
execution VI an assembly
block let's say that we've got both the
optimized and unoptimized versions their
gas consumption is different therefore
the value that will be pushed in at the
stack when a guas op code executes will
also be different and if a control flow
consumes that value we will get
results therefore we cannot be assur
that when we are debugging using an
unoptimized version we are actually
looking at the things that we' like to
see and the lack of a proper debugging
format disallows us from having the
exact same data data granularity that we
would have while debugging in a
traditional programming
language um eof offers solutions to
these two
Problems by changing the structure of
the evm it will be much easier to define
a proper proper debugging format and to
extract the same kind of data that you
are able to extract in traditional
programming
languages uh but there is also one uh
extremely interesting development that
happens inside of the eof that allows us
to have semantically identical
executions between optimized and
unoptimized versions of the bite
code um gas op code is removed as well
as other op codes that
that whose output depends on the code
structure such as code hash code copy
external code cach external code
copy therefore when we get to a
debugging format that will allow us to
have to extract the same kind of data we
will be able to spin up uh debugging
session that will have the exact same
output with a with an optimized bite
code and an optim unoptimized bite code
and this is my final step towards
convincing you that web3 debugging
experience could indeed indeed be better
but I'm running out of time so I will be
quick um let's take a look at a single
request SL transaction
um let's make it an HTTP standard
request that lands on a server so every
program that executes has both has two
kinds of input a code and state when you
land on a specific server the state that
you're getting as input uh is fragmented
it's either either in radus it's either
a local variable it's either in pogress
but if you execute a transaction on the
blockchain the state is
localized therefore you can replay the
exact same input that you had in
production if a transaction let's say
failed in your local development
environment and if you are able to
extract the same kind of data via new
debugging format and have the same
execution in unoptimized bite code and
is and in as in optimized you basically
can replay every production request
locally with exact same environment as
in
production and that's it
thanks thank you very much for the
presentation uh so we don't have any
questions yet I I have one
uh is there any implementation of a
debugger that uses a so far or not yet
not as far as I know this is a thesis it
can be looked at it that way um some of
the clients have implemented the O but
some have not yet have not done it yet
okay let's go to that question H do you
have any insights on if uh e affect
source code
verification m
I'm trying to think off the top of my
head I do not have any insights as of
right now as I haven't thought about it
so source code
verification okay so
yes it does affect it um source code
will be verified on the protocol level
every time a contract is deployed there
will be no need for jump dust analysis
every time uh jump desktop code is
executed as it is removed from the
virtual machine alog together in EF
contracts uh and uh let's try to answer
one more question uh which difference
besides gas consumption can be between
optimized and non-optimized code so
optimized uh code depending on the
number of iterations that you optimize
it with
um so there's a flag that basically says
I want to this contract to be executed
optimally if it is executed x times and
you can say that it's a thousand times
so if it's executed a thousand times on
average it should have uh much less gas
consumption
than in in comparison to the
non-optimized bite code so optimized
bite code can uh throw out entire
sequences of the bite code it can also
merge sequences of bite code
and every time you change the buy code
you basically affect the G the gas
as
yeah great that's about it let's thank
our speaker one more time
thanks uh so the next presentation it's
going to be about testing the
implementations of uh uh compilers and
exec ution clients uh when they
Implement eof and our speaker will be
hubby uh let's welcome uh our
speaker yeah hello everyone it's my
distinct pleasure uh to today introduce
Emily which is our small contribution to
hopefully make uh EF uh safe so to make
sure everything in e works properly so
not just right before me but today
already multiple times UF has been
discussed so in case you just walked in
because you were especially interested
in Emily um I I'll give a short recap so
what is UF um so there there are some
two talks listed here by by Den Farin
and also from this morning which are
really good and and really summarize it
well but for the purpose of this talk
we're just going to say UF is a big
change in
evm so what is the problem with that
because with as in um with any big
change in evm a lot can go wrong so we
have a a lot of different smart
contracts right and we are using
different compilers I mean there's
solidity and there's Viper and they have
a bunch of different versions they have
different optimization features and so
on so we actually have quite a few
compilers that we're using and then out
of that we get lots of different bite
codes and these bite codes we execute on
different execution clients and uh on
these execution clients these new bite
codes interact with many different
existing contracts so we have a horribly
big search space to look for things that
can go wrong right and um experience
shows that things do go wrong and
unfortunately things go uh don't always
are detected during testing because we
had uh chain splits after certain hard
fors on chain so what do we think can go
wrong here so first of all um there has
been some discuss discussions on what
compilers should support so we can we
want to figure out what uh is actually
supported so that users can have a
seamless transition to EF in the bite
codes of course we can have incorrect
compilation we have a totally new um
features we might very well see
incorrect compilation and in the clients
we also have very new implementations
it's not implausible that we see
incorrect execution so all of these
would be horrible they they would lead
to to chain splits and then lastly we
might have incorrect interaction right
so you're calling an existing old
contract from your new EF contract maybe
that doesn't work the way you thought it
would work so now how can we fix all
that so that's why we're here um to to
improve stuff so first of all is this
news well no of course not so there is
already uh a lot of testing going on
right so there's the test testing team
and lots of tests are being written but
we think that Emily can improve the
situation because we in the past have
learned that what uh really helps is
real contracts with real data and real
interactions because that's in the end
what we want to be sure that works on
chain right because that's what might
cause the chain split so what does Emily
do so here we have an existing main
transaction which um yeah you are all
familiar with so now what does Emily do
exactly so we take contract a and we
recompile it to EF and we execute it
again so now we can compare these two
executions right because now we actually
have a really good idea of what
correctness should look like because we
have the execution above which is the
current execution and we can compare all
the parts so we can compare what does
contract a do what does it right to
storage how do all the call data and
return data look how is the output how
uh it's the success flx and so on so we
have a great uh correctness uh reference
here so Emily checks a bunch of things I
mentioned some of them already so
obviously Emily checks all the storage
changes Emily checks which events I
emitted Emily checks the call data Emily
checks the return data and the execution
status so um and lastly what we also
found quite interesting while developing
is that we um can monitor some of the
gas cost so we can see overall is euf
execution on average cheaper or more
expensive than the previous
execution and um with that I we can then
find all these things that we're really
concerned about right missing compiler
features incorrect compilation incorrect
execution incorrect interaction so all
these horrible things we want to avoid
we can hopefully find before they are
happening on chain so with that Emily
contributes to the security of EF of
course as is the usual case things are
not quite as simple so a bunch of things
can go wrong um I'm happy to discuss uh
them a little bit more during the
questions but uh one of the things that
can go wrong is um the as was previously
discussed the gas gas out code is
disappearing but currently it's still
there and it's causing a bunch of uh
problems as was just discussed in the
previous talk but yeah we have some
counter measures for that so I'm happy
to discuss this in the questions and
with that um I close and thank you for
your
attention thank you thank you so let's
start with the questions uh are there
instances where one may one may want to
rewrite their contracts for UF for
better performance or other reasons yeah
um I guess we're going to see I mean the
the I think the TR truth is that we
don't know exactly what the numbers are
going to be like because we haven't seen
the the latest compiler versions and we
haven't seen the full EF spec um but I
think there that's quite possible
because it's feasible that there might
be um contracts which are significantly
cheaper when when executed in EFS MH uh
so uh is there a compilation to EF done
from source code where do you get the
source code yeah excellent question so
we uh get the source code from ether
scan so and also other sources but yeah
one of the sources is ether scan so
obviously we don't have source code for
every contract but that's also not
necessary I mean we just want to test as
much as possible and it's actually good
that we don't have source code for
everything um because we as I said we
also want to uh test this interaction
with Legacy contracts so we don't want
to necessarily recompile everything but
yeah um we we uh recompile some and then
test the interaction mhm
um if Emily compiles Legacy bite code to
EF how does it cut compiler bugs from a
high level language to euf Yeah so
basically um we take the code and we we
previously ran it with the real data
right so for example uh let's consider a
transfer an an esc20 transfer and let's
let's say the esc20 transfer now works
incorrectly when compiled with with ef
now now what we would see is we would
for example see a a difference in the
storage and because we check how was the
storage changed originally and now we
check how is it changed now that we run
it based on EF we can detect those kind
of um correctness
issues uh great I guess uh that's it
thank you very much yep
thanks so the next presentation will
begin in around 5 minutes
can you
all right good afternoon everyone I'll
be taking over from Stephanos who has
been doing a great job mcing since the
morning my name is glce from Angel heck
or a death well marketing agency and I'm
thrilled to be with you and up next we
have a keynote titled the future of eof
layer one layer 2 and Beyond featuring
Danny faren a seasoned ethereum core
developer with a deep rooted passion for
the technology Danny has been focused on
the evolution of evm contributing
significantly to its ongoing development
and optimization and today he will show
how the structure of the EF container
may be adapted to support these
potential use cases
so let's give Danny a warm Round of
Applause as he takes the
stage it's great to be here we've been
talking a lot about what eof is today
but I think it's time we need to step
back and see what eof could be in the
future and what real power unlocks are
happening now I named this layer one
layer two and Beyond because a lot of
these features we're going to see is
going to get some differentiation in a
compatible way amongst layer twos and
other chain and other uses such as
offchain use but I'm going to focus
mostly about what I term as oh some so
I'm an independent contributor there was
a joke in there that I completely forgot
about and um you know that's that's kind
of a lame tieline who do I work for I
work for a company called numid LLC
which is a single person company so I
can be a freelancer and get tax and get
uh health insurance in in the US and I
can have any title I want I mean why
can't I just be a senior Consulting
principal staff engineer sounds great
better than that I could be the director
of execution verification and assessment
but I'm just going to stick with the
independent contributor so and so when I
when I think about the the future of eof
I like to think about what's in front of
us what's on the horizon and what's
going to be over the horizon and you can
think of that as what will happen on
mainnet what may happen on mainnet and
what might happen on mainnet because
it's kind of way out there there's a I'm
going to talk about a few things that
definitely are going to happen not in
the first eof Fork maybe in the first
eof Fork but on Forks afterwards and
then some things we'll probably see on
layer 2 first and then some things that
are going to be experimented with and if
they're really useful we'll see them
come into eof into the main
net so first let's talk about what will
happen and what's in front of us and
these are focused on things really to
make pre-compiled contracts a lot better
and a lot easier so we don't need to do
those anymore so pre-compiled can just
be just run the evm and you get all the
performance that you need um so what's
wrong with pre- compiles were they're
bad for client code bases they're bad
for security and they're bad for project
management they're just just really
difficult to to execute and deliver in a
uniform way it's much better to let
people write the code that they want in
the evm and execute it the way they
want the first piece is evm Max there
was a talk earlier today that went
really into depth what evm Max is about
what you can think about it is it's math
that lets you do uh stuff on
cryptographic elliptic curves a lot
easier a lot faster a lot more efficient
and it also lets you do things on curves
that are bigger than 256 bits because
that's what your typical security is um
it's got some new OP codes um it has a
separate memory space and it helps you
move stuff in and out of it and that's
just focusing on the modular but there's
another piece of math that we're
probably going to need in the future in
the next four or five years when Quantum
uh when Quantum algorithms actually
start impacting us and that is single
instruction multiple data operations and
this is for things like lab lus
encryption which uses kilobytes arrays
of numbers that are um stretched out and
calculated and and computed in large
fashion in vectors and it's inefficient
to do this individually so to really
support lattice encryption inside the
evm we're going to need a lot of
different instructions that do it on a
vector
basis and this these aren't going to be
really good for AI inference it uses a
lot of the same stuff but we're not
going to do AI on the Chain so there is
an EIP out there don't pay too much
attention to it I'm it's going to change
this is just a mapping of Intel AVX onto
what it might look like for the evm
there's a chance some of this might show
up in the evm max proposals but this is
something to keep an eye on in the next
four to five years because we will need
to get some sort of support for Vector
math to do large quantities of math
calculation on the chain and some of the
things that we can do in EO are to say
we're going to need kilobytes or
megabytes of memory in that in the
headers and we can propose to say how
we're going to solve
those the last thing that's going to
come on on to the onto the stage that is
definitely going to happen for us for
the evm is a legacy and eof parody right
now there are a few things that you
can't do in Legacy that um that you
can't do in eof that you can do in
Legacy um some key support for some
smart contract wallets uh the ability to
bring contracts in from your smart
contract wallet into an entry point and
bring it in right now that's fairly
difficult uh for eof but there are some
solutions that we're going to solve that
um and of course we could there might
just be uh Native account abstraction
that would be we supported in there um
but there's also some features like um
detecting if you have an EA that are
essential for libraries like open
Zeppelin another thing on the horizon
we're going to look at and this slide
speaks as though it's it's it's a given
but it's not necessarily a given is is
sunsetting um as much of Legacy as we
can perhaps making it impossible to
deploy new Legacy contracts maybe not
this is going to be a process where we
need to make sure that the eof is Legacy
for the things we want to preserve and
we want to keep that's the first step is
to get the parody and then we can start
looking at all the other contracts that
were deployed before and see what sort
of features they have in that are
dependent can these be brought into a
validated sense can these be brought in
and used within the context of what euf
allows or are they going to be doing
crazy things like like doing jump
locations from call Destination and is
it essential that we preserve those um
and also are they doing things like
polymorphic code addresses do we want to
support those or break those so those
are some of the things we need to look
for so the main takeaway from this slide
is in a couple years we either need to
have an in place plan for how we're
going to deprecate Legacy and not let
new Legacy code be deployed or we need
to have an answer of we can't do this
because of reasons X Y and Z and that's
okay and by that's okay meaning we can
still snark all of the main net
contracts just for these few cases it's
going to cost them a lot of money and
we're okay with
that so finally what are some of the
things on Horizon this is where things
get a lot more exciting and a lot more
uh leveraging some of the features
inside of eof
um and the key thing is we're enabling
better execution on mainnet and we're
going to prove some of these features
probably unroll it before they hit main
Nets and they're going to be hitting
things like account abstractions we're
going to try unbounding the code size
who wants to write a contract larger
than 24K that's going to be safe now in
eof and we're going to show you some of
the ways that it's some of the issues
that's going to be affected and another
thing to look out for the in the future
is concurrency not just parallelism but
concurrency being able to take these
operations um these contracts and split
them up and run them in isolation safely
um which is you know usually a step for
parallelism concurrency will feed into a
lot of the parallel efforts and make it
a lot
better so first let's look into a native
account abstraction um there's actually
a proposal out there and I was speaking
with some of the devs earlier this week
um at a at a conference we had in
offsite um EIP
within eof to make Native account
abstraction easier and the key thing is
adding into the eof Container the notion
of multiple entry points um typically
when you run an EF contract you have to
start at entry point zero but what
they're going to do is they're going to
put they propos putting definitions in
the header to say you know what you
could use section two Section 3 or
section 47 but each of these entry
points has a specific role and when you
execute that contract you're trying to
execute it with that role then you would
actually use that entry point instead of
entry point zero what's nice about this
is if you have a contract that is
validating or serving as a pay Master
with entry points you can be certain
that the evm is only calling those entry
points if they're coming in with the
role and you can be sure that it's being
used properly from within the system and
not just called externally by someone
hacking the system with some few random
solidity selector
addresses so there's proposed in there
right now five different roles um one
for deployment and two for validation
and execution of your smart contract
wallet and two optional pay Master
validations and the way that would work
is when you're doing a validation for
your contract we would call your
contract and keep the role and if it
sees the role has Center validation and
it has a separate entry point we would
use that to executed instead same with
validation execution and post
transactions this allows us to ensure
that these this code in these sections
only gets called when that role is
relevant next thing we're going to look
at coming up on the horizon is
unbounding the contract size um
currently the limit is 24 kytes and this
is a a a size that was set basically
during the Shanghai attacks and it
equates to 6 megabytes of gas in about
contract when the contract size was
first imposed but it was put in as a
safety measure in case that there was
some other exploit in contracts that
people didn't know about well there was
one and putting this contract size
limitation in place is actually quite
handy um there are some really nasty
jump dust attacks that you could do um
with Cate that could really consume a
lot of time and space and basically all
of the clients we fixed this in Shanghai
by charging every bite that we were
going to validate for a contract so this
is not a problem anymore but if between
Shanghai and the Shanghai attacks it's
kind of funny we fixed it in Shanghai um
if you would have done this jump Des
attack you would have really caused
damage to the
network now what's interesting though is
that eof validation gets rid of jump Des
validation the validation is performed
when you put the EF contract on the
Chain once that validation is done you
never need to do it again
so looking at this I mean it's like well
what's wrong with six with 24K can we
just increase it you why can we just
increase it to another larger value and
this goes along the argument of saying
well 640k ought to be enough for anybody
let's just pick a big number and we're
never going to hit that it's never going
to become relevant that's the sort of
comment that's going to come back and
bite us even though as you do research
on this you'll find out that Bill Gates
never actually said that comment even
though it's oftenly credited to often
credited to them so before we completely
Unbound it the limit is going to be
increased probably double it and maybe
double it again and even when we Unbound
it it's still going to be limited by the
amount of gas that you have a blocker
for your transaction so so if you're
going to deploy a gigabyte size contract
I hope you have a system that allows you
to use a trillion bytes of gas and in
some offchain systems that's exactly
what you're allowed to do um Peter cesi
from gu created a little burnt pixel
thing um where you can use the evm to to
create pictures and render them and and
it takes billions of gas it takes a
whole lot of gas more than you could
ever execute on chain so Unbound gas
seems to be something we need to be able
to handle um but more than likely we're
just going to be increasing the size to
more reasonable size to get rid of the
problems now in eof however looking
forward to this a truly unlimited size
does present some problems there are
some Natures of the way that eof has
written that you can only have code
sections 64 kilobytes in size um that
you can only have 1,24 sections um that
your jump destinations are limited to
plus or minus 32k from your location in
theory you could deploy a contract up to
sections and maximum subcontainers but
practically the maximum contract size
right now is
this probably in a few years when we get
to the point where this matters we'll
deploy something called variable length
quantities into some of the headers into
some of the op codes and make that as an
option that contract developers can use
if they need it um these headers instead
of being a fixed bite length would use
encoding in the bytes to have a variable
length so you can have truly arbitrarily
sized contracts what's interesting about
this is if you're using smaller values
the VQ is actually save btes and if
you're once you're outside of those it
costs a little bit of bites but the but
once you get past 64k it makes
impossibly large things possible um so
the downside is that the header must be
streamed now you can't check based on on
the sizes of op codes that might change
the way that we validate but something
like this is going to be needed to truly
un unlock the full size of all possible
contracts and and we'll get there uh
just as soon as we can increase the
contract size which is not the easiest
thing to get done on
ACD the final thing that's on the
horizon is that I'm personally
advocating for is we do a little bit
more attention of what we can put on the
evm to support concurrency a lot of
concurrency actually happens outside of
the evm cross-chain communications Sharp
in uh mailboxes semaphor and all that
but there are some things that we can
put in the evm that'll actually make
some of these concurrency things simpler
and allow us to use things like the
isolation um in the asset protocol to
make these transactions more isolatable
so if you have a bank from W if you have
a large bank account you can do all
sorts of withdrawals from it in sequence
and not lock up lock up everyone from
using that account until they process
all those transactions there's two main
ways we're going to look at supporting
concurrency Atomic operations and has
been proposed for deferred execution
whether we ship these or not remains to
be seen um I'm an advocate of at least
Atomic operations and there's been some
push back on the Deferred operations
we'll see what what happens there but I
wrote a proposal EIP 7519 that solves
the basic problems that are needed um
for uh Atomic storage is just have an
sedit and S debit op code where you can
take your storage memory and say add 100
subtract 100 now that seems really
simple and seems really boring when
you're looking at the evm level but the
implications are actually in the proof
level and in the vertical level because
you're no longer saying take a value
from one to two you're saying take the
value and just add one I don't care what
it is just add one figure out at the end
what it's going to be and from that we
can split things
apart and we also put in things like um
having the uh overflow and the underflow
detection in there to make sure that if
you're withdrawing money from an account
that the transaction is not going to
succeed unless there's actually money in
there this is truly like a bank credit
and a bank debit I mean this is
literally the sort of stuff that you
grab an undergraduate database book and
you look in the concurrency section and
it's like one of the first examples use
use relative and Delta values so we need
to put that into the evm so that can be
possible the next one um that's been
proposed is queuing stuff to the end of
the block uh is was was the proposal put
up by Micah but basically taking a
transaction have transactions spawn
other transactions um um there's been
some push back but there a sort of thing
that we need to look into and other
chains on l2s and l3s and offchain may
use this feature to have transactions
spawn other transactions in other ways
it provides interesting opportunities um
for out of sequence transaction
processing finally what are some of the
things over the horizon what are some of
the things that are not realistically
being planned what's some of the great
potential that we might be able to do in
eof a lot of this is adventures and
metad data the eof header has a rich
opportunity to put all sorts of random
information about things that may or may
not be relevant to the execution and
allow you to do all sorts of interesting
things with the values and that is not
something we could do before eof because
we didn't have a good place to put this
metadata and read it and understand it
and make it
safe so one example is we could so so in
order to support this we could even put
into the header to say hey we're using
experimental eips we could put in a list
of the eips we use maybe the version and
maybe some parameters like here's the op
codes where they mapped to so you can
create these experimental contracts and
you can use them in some EVMS in the
EVMS that don't support those
experimental features will be able to
read it and say hey hey hey I don't
support this sedit stuff I don't support
this sedit debit op code so I just plan
old won't won't use it and we can figure
out those things out when you're loading
the contract in on the create
transaction rather than when you build
an entire system and you're trying to
use the advanced feature and suddenly
you realize that push zero is supported
on this
VM so putting those sort of that sort of
information in the header is going to
make it really easy to support
experimentation in eips and in code
going
forward another thing we could do is we
could put alternate by code formats it
doesn't have to be evm in eof we could
put wasm in there we could put arm we
could put risk V it could be the primary
op code or even more exciting you could
put two versions of the op cord you
could put an evm version in there or you
could put a risk V version in there so
when you're running it on one system you
can run the evm version and when you're
running it in ZK systems you can run the
rkv version now it's going to be on the
compiler to make sure that those two
versions are equivalent and provide the
equivalent systems but it's a great way
to pre-compile and pre- optimize
operations on different chip instruction
architectures and when it comes to gas
golfing being able to hand tweak the op
codes in each of those systems is
key another thing to look forward to is
something called Progressive pre-
compiles this is a pitch that was raised
on uh ethereum magicians where they have
the idea of well let's just take instead
of having pre- compiles let's just take
all our fancy math and get a standard
evm implementation of this and then
let's feed it through the create to
create transaction that gives us an
address and that way we know that that
address is going to be where the op code
is and let's just make our pre-compile
code there do whatever the pre-compile
is the upside is if you don't have that
pre-compile in your system you can just
deploy the evm code and if you do have
the pre-compile while it's cheaper and
faster and more
efficient the problem comes in in that
how do you codify what the cheaper gas
is in the systems for the pre-compiled
when they are actual no local
pre-compiled and how do you deal with
systems that want to prove the evm
execution rather than using the
precompile logic and make sure they get
the right gas costs well in the evm we
could specify alternate entry points
like we did in 7701 instead of saying
that this is for validation we could say
that this is for the gas cost and based
on the input data here's what the gas is
so we can go from ancient systems of
measuring gas to fancy high-tech
versions of of predicting gas without
having to execute the contract and again
it's on the pre-compiled developer to
make sure that those numbers match up
properly and if systems don't want to
use this gas they can just reject that
field and use the evm
execution another thing we could do is
we could take the solidity dispatch and
we could wire this into the header in
the front of almost every single smart
contract is a bunch of SW switch code
where they're trying to figure out from
the first four bytes where to jump to to
execute your functions coming in we
could put this in the header and we
could just have this as a part of the
call dispatch and have it go to one of
the different entry points based on your
selector we could save a lot of gas and
do it really efficiently inside of the
EVMS and finally another thing we can do
and this is something that I thought of
after I wrote my slides came to the
conference and watched a panel about
contract verification we could put the
contract verification data in the
metadata in the header rather than just
having it as random code bytes at the
end of the data section this is an
actual live contract this is the Tron to
usdc Unis swap V2 contract and you can
see they put a lot of metadata at the
end that doesn't necessarily have to be
used at runtime and could be encoded to
say here's your debug symbols here's
here's the uh bzzr link to get the
source code and here's the version of
slid that we used to compile it and they
could put that in the header and you
could read that and uh you wouldn't have
to have that exposed and you could put a
lot more semantic meaning inside the eof
header and this would make people who do
validation much much more
excited so what will be what could be
and what might be the future um you know
there's what could be on mainnet one day
what will be on mainnet has to do with
with with with the eips that already
proposed things to watch for our account
abstraction Unbound contract size and
some concurrency initiatives that are
starting up and the things that might
come up is just random plays in in the
metadata there are some great
opportunities in
there so thanks uh nope that's not
me that's not me that's me thanks thank
you Den apparently you're a man of many
heads all right for our audience if you
just joined us um feel free to scan the
QR code on the screen to ask some
questions uh but we do have some already
on the mirat platform so we'll start
with the first one will the shift to eof
impact ethereum's security model um so
security means a lot of things in a lot
of different contexts um when you're
talking about the security of a compiled
bite code it's going to have huge
impacts because we can verify the stack
Heights you can be secure about your
code um but as far as the security of um
like am I authorized to transfer this
defi contract to the other thing um it's
going to have it's not going to make
anything better or worse on the
application layer of people using evm So
within the evm it's going to improve the
security standing and for people using
the evm not going to make things worse
but it's not going to make things better
all right and our second question any
chance for a 64bit
evm um there is a chance uh because
what's interesting right now to give
some context to that question the evm as
everyone in the audience is probably
aware of is a 256bit register VM machine
and that presents some ahead of time
compilation issues that you got to play
games with the types on the stack if we
dropped it down to 64 bits there's a lot
faster and better code that we could put
in um that's the sort of thing that you
could you know over the horizon encode
into um the evm header that says by the
way my register sizes are 64-bit and
everything in here operates in 64 bits I
mean that's that's an excellent
investigation that some l2s might want
to do yeah maybe in the near future all
right and our last question which of
these proposals would involve changing
the E version number that's an excellent
question so when you talk about uh
version numberings there's like major
number and minor versions and that's
kind of some of the the the heartache
that came with making eof is we had to
do a lot of breaking changes from the
initial evm things that that were
incompatible and that you couldn't
figure out were different so everything
that I proposed here is something that I
would call minor updates soft Forks so
if you imagine the world of all
contracts that are valid in E version
contracts in that first set are
invalidated but you grow the set of
valid things I would consider that to be
a minor upgrade grade and everything
that I proposed merely grows what is a
valid contract because of the validation
so we're not breaking anything that came
before we're increasing and adding new
features so I don't think anything I
proposed would require changing the
major version number of
eof all right I think that's all the
questions we have thank you so much
Daniel let's give him another round of
applause all
right and I think we'll have a quick
break before our next session but just a
reminder um you can actually start
sending in questions even before the
session begins the QR code will be on
the screen from the very start so yep
just a quick reminder on that and we'll
see you really shortly thank you
w h
o
good afternoon good afternoon for those
who just joined us hello I'm Glades from
Angel heck and a friendly reminder to
all of you that even before the session
begins you can start asking your
questions via the mirat platform you
just have to click into this session and
scroll all the way down to Q&amp;A and this
is a great segue to Hype up our next
speaker the next T the next keynote is
titled redis evm supercharging ethereum
calls with inmemory execution it
features Everton farga a software
engineer that worked for the ethereum
foundation on projects such as ethereum
Mist the first debt browser ethereum JS
libraries and ethereum grid today
Everton will share more about how the
reddest evm could reshape ethereum
execution environments enhancing
scalability and efficiency for deps so
without further Ado let's give a warm
welcome to
Everton hey what's up
everybody uh thank you all for coming
can everybody hear me even in the
back all right cool amazing so let's
talk about this unusual combo red is an
evm so for context I worked for the
ethum foundation before had the honor
and privilege to do so now I help
customers uh exclusively from the web 3
space to deplo and scale on AWS which uh
gives me visibility to some of the
problems that they face
right okay big one uh challenges on RPC
scaling that's uh super
fun so uh to begin with uh whenever you
have a consumer facing application let's
let's pick think about a um defi router
right uh you have to serve uh all those
RPC requests to millions of people uh it
is the traffic can be uh unpredictable
and you might have some huge surges in
traffic so some strategies that folks
typically do is horizontal scalability
of nodes super fair but it comes with uh
some challenges right so first of all is
reaction time the time it takes for you
to to deploy a new instance so take the
snapshot load it cop files and um load
the chain data and also synchronize the
difference uh from that
time second that's not a trivial
challenge though by the way second um
forecasting to understand you know your
user pattern and see oh uh on weekends I
have you know lower usage and then on
you know Tuesdays I might have um uh
more access and then you react uh
accordingly proactively but that is a
very specialized task right so the
caveat is of over provisioning which
happens a lot basically people paying
for more servers with idle capacity
that's not good for any
business final boss consistency right so
when you scale horizontally well you you
suffer from that you have potentially
notes that are behind the chain um you
have uh you know different states across
and people use typically the latest data
right so you do not uh scale
horizontally to serve archive data some
businesses they operate on only on
current data so consistency I would I
would say that is a final boss that
typically um makes people delegate the
task of managing these
RPC t uh RPC nodes management two
infrastructure providers some of you
know the ones that you know right but
they suffer from the same problem so
they they need to get really good at
forecasting reaction time and that's all
the perpetuating and putting lots of
pressure on those
players well typical uh strategy to deal
with with a lot of read um access is
caching some of those RPC methods are
pretty easy CH ID would never change
block by has one parameter get logs you
can offload uh the data to some U
database index and but the list goes on
and it becomes even harder eth call is
the main villain because it is typically
used for over 70% compared so if you
want to address this issue we should you
know first and foremost tackle the eth
call
problem word of the day
externalization so can we is there any
opportunity to externalize the
processing of evm op codes to a very
fast engine so I'm introducing today the
evm Lua project that it is technical
validation mode it is a micro evm
interpreted implemented in Lua and it
executes
inside redus with minimal storage read
latency and it is able to process
ultimately evm operations so e calls U
estimate as in the future of course uh
and and
others how it works you can actually
select what are the contracts you you
have there and then you load uh the
attributes that you that from that
contract so code balance on storage all
the storage keys there are scripts for
you to do that and and we have some
phases so R&amp;D stage this is where we're
at so loading the entire storage from
selected contracts keeping up with the
state diff processing evm code strips
Next Step evm compliance so implementing
all the op codes including transient
storage and adding evm metering SO gas
metering and and further steps include
deployment so benchmarks optimization
feedback loop and building for uh
catering to user specific features so
this is those are Baseline numbers from
Amazon elastic cache Benchmark using uh
of course that the simplest um the
simplest data structures this is not our
project yet but uh 1.2 million requests
per second uh for a single instance that
is a lot right and in a cluster you can
have over five million requests per
second and in if you scale those uh
radest nodes horizontally so here's the
project uh have fun please start it and
well thank you very
much thank you so much
Everton so now we'll move on to a quick
Q&amp;A so we have one question thus far
what are some potential security risks
of embedding an evm interpreter within
redis all right uh interesting question
so uh you can have uh several guard
rails uh for that uh but because you
control you have control of the up codes
that are being executed uh that would be
only for reads and how to write so uh uh
you can separate who writes and who
reads at a user level uh and have uh
several folks only reading from from
that uh inmemory
database does that answer the question
whoever
asked think so oh okay just on time we
have another question how large is the
Ram size needed that's another great
question so to begin with uh only um you
know just a couple megabytes uh and it
is already enough to start playing and
it depends on the contract storage you
want to load up there right so uh on AWS
the instances go up to 2 terab of memory
within a single instance so so the sky
can be really the limit here it could
fit the entire
State all right and I accidentally press
answered for one of the questions so
it's not showing up but I'll read it out
why don't we access State DB
remotely why do we access theb State
remotely great question uh I thought
about that too so we can create a
compute unit uh that is external to the
node and scale that out however they
will all be executing um Gat storage at
uh sequential
as you execute the evm instructions and
you will get the penalty of latency
right so the thesis here is to to get
together to put together both uh storage
and the the execution in an es scalable
way all right now we have a lot of
questions um next what happens if the
evm hits an unimplemented OP code it
breaks really
hard okay next one I'm assuming can this
run on reddis community absolutely yes
all right there even uh yeah so there
there are even uh novel uh engines there
one of them is called valky uh that is a
drop in replacement for red is uh should
be the same thing right and there's U
yeah you know there's a developing space
okay and our last question does it need
archive notes to feed the data is Redd
is sorting all archive data great
question so the project is uh currently
focused on current state uh you need uh
you don't need to have an archive note
to feed that in but uh your RPC uh uh uh
Source it needs to have uh some specific
debug methods available right so um
debug uh the way to export the entire
state of a contract is one of
them all right we'll just have one last
question when can we use this for full
block execution oh wow
I don't know soon please help
me all right I think unfortunately
that's all the time we have I know we
have one more question but I believe
Everton will be hanging around here so
yeah you can catch up with him after
this session uh thank you so much
Everton let's give him another round of
applause thank
you thanks everybody and now we actually
have a quick lunch break so I think
that's music to everyone's ears we'll
see you back here for the next session
at 2:30 p.m.
enjoy
I
you
n w
hello hello hello all right good
afternoon everyone welcome back I hope
you all had a good lunch thumbs up
thumbs down no good okay thank you so
much I hope there's no food coma
happening in the room here we have a
very exciting session lined up for you
so up next we have a panel session
titled changes to the L1 evm versus l2s
and our panelists will explore new
initiatives to implement evm upgrades
such as the eof on l2s before L1 and
discussing their pros and cons now
before I welcome them up on stage just a
gentle reminder that everyone has their
phones right so throughout the session
you'll see your QR code on the screen
you have if you have any burning
questions feel free to drop them in the
platform that will be you'll be directed
to that platform through the QR code if
not you can go to your Devcon passport
and there's actually a live Q&amp;A button
that you'll see at the when you scroll
down the screen so you can put your
questions there as well all right so
without further Ado please join me in
welcoming our panelists first we have
Mark we have Matt Daniel Alex and Eno
who will be our moderator for the
session let's give them all a warm Round
of Applause and ano the stage is
yours so this will be essentially um the
last one of today's um evm related
sessions that were um kind of structured
like an evm mini Summit here at Devcon
uh last year we had a full day um of evm
summit during Devcon act um and a lot of
aspects of today's topics were actually
um covered there but we will see um
what's new and um highlight some of the
um takeaways from last year's panels as
well so thank you for the panelist as
well for joining us um today and I would
like to first um ask you to beefly
briefly introduce yourselves and your
involvement with the topic and
evm let's start with
Alex yeah it works okay yeah my name is
Alex um I'm part of the ipsilon team
which you may have heard here a couple
of times today uh we do research um
focusing around the evm um and we also
did research on web assembly um and
obviously because we focus on trying to
improve the evm one of those big
proposals is EF the other one is evx I'm
definitely very bullish on getting those
out and uh you know we have been working
a lot on mainnet so obviously I'm in
favor of getting these improvements to
l1's as well not just L
twos all right my name is Daniel I've
been in the solidity team uh since 2018
have been the lead of solidity for I
don't even know how long few years now I
think uh and yeah uh so we are the ones
that actually need to generate code for
the evm so uh yeah we also would be
highly appreciative to have eof
everywhere because and including L ones
because uh yeah we will get into that
but uh but yeah uh we're in the ethereum
foundation right now we're spinning out
of that in the Argo Collective is
anybody in is interested in that there
is a recording of a talk the other day
but yeah that's
it hey guys I'm Matt I go by like
clients on the internet usually I work
on the go ethereum team and have been
working working on some of these evm
ideas for a while worked with Alex quite
a bit on Phase 2 for eth 2 back in the
day thinking about what new execution
environments in ethereum could look like
and also have just spent a lot of time
since this concept of the rollup Centric
road map was released thinking about
what the interplay between L1 and L2 uh
rollups would look
like hey my name is Mark and I am a
contributor to the optimism Collective
we maintain the op stack which Powers a
bunch of different you know L2 networks
our goal is to commoditize stage two
rollups so that anybody can you know use
our free software to deploy a stage two
rollup really easily I've written a
bunch of solidity and have worked a lot
on you know upgrading smart contracts
that are running in production that hold
lots of money have hit lots of different
you know edge cases with doing
upgrades um and yeah I I worked on EIP
Upstream that into gu so have some
experience working with um you know the
evm and yeah I'm interested in just
scaling ethereum
generally cool awesome thank you so much
so um I will address most of the
questions to one of you but if anyone
has any additional thoughts feel free to
to just jump in after so right so um the
evm has been targeted for improvements
pretty much since the early years of
ethereum um and there are several
related elements in the road map as well
but uh there were always some other
priorities in in previous hard workk so
there hasn't been too many significant
changes happened around the evm uh so
far um but there are a lot of progresses
made when it comes to R&amp;D um if you
listen to Doo's talk on Tuesday or even
today he gave a really good summary on
that um and there a bunch of very long
time also how do you see the future the
current road map elements how do they
build up on each other or how do they
interact with other road map elements um
and maybe also just touch a little bit
more Z friendly how much time do we have
for this question well try to give it
very brief um yeah I think some of these
questions were addressed has seemed like
different stages of development and
sometimes it had more Focus other times
less Focus um I think
generally maybe the first year after
ethereum launch there were more uh
quicker changes like uh reverts were
added um there was like you know quite
an important Improvement and maybe
shifts were added sometime
later uh but the most of the development
on evm has been more reactive uh
regarding State um so most changes were
gas related how do we deal with the
state how do we improve cost around the
state um or fixing something like the
Shanghai attacks um or making changes
around like the beacon chain integration
like the merge and focus was less so on
improving the evm itself um there have
been I think some initial l2s some were
more explorative um people were always
really curious at improving the evm um
but there was One Direction where people
spent most time on is a precompile um
they wanted these big features which you
couldn't achieve in the evm and so they
opted for like a maybe an easier way it
turned out to be not an easier way in
some sense it is other sense it isn't um
some of these pre compiles have a lot of
complexity they seem simple turn out
they have consensus bugs every year uh
some of them have taken more than four
years to get adoption like the BLS
precompile it's still still being
discussed um and so with all these in
mind we have been in epsilon we took
like a detour to to see like wasm would
that be an option we came back to VM
that evm is actually not that bad but it
does need a lot of uh help to make it
better and you know right now we have a
lot of adoption around evm so that's the
reason we we really want to improve the
evm um and to touch like on the road map
as I mentioned UF and evm Max um I think
is like a good um direction to go euf
gives you like a baseline to build up on
um but it also introduces you know a lot
of like improvements um if you look at
some benchmarks there are some
benchmarks regarding code size and gas
usage there are improvements to be seen
there um and there have been some other
benchmarks regarding
ZK um just to touch on it
quickly one issue in in ZK VMS is um
they may need to translate the the code
and if you translate the code you need
to keep access to the the code you
cannot only uh use the the new
translated version uh with UF you remove
like code inspection code introspection
so this problem goes away another big
issue is like the gas cost um the gas
costs are really tuned to like uh
regular computers and some of these um
things the evm has they would translate
really differently in terms of
computational cost on ZK removing gas
introspection in UF also removes this
problem um so we've seen some good
benchmarks um that the ZK application of
eof reduces proof Siz AG reduces uh
proof generation time as well um so all
of this seems to be positive but yeah of
course still a lot to to be done uh
going forward I'm not sure if anybody
has I I said a lot I'm not sure if you
have any like response to
these I mean we definitely introduced
bugs in our Bridge because of gas
introspection so um I'm a big fan of a
lot of the simplifications that are
coming with eof l2s also desperately
need um some sort of multi-dimensional
that um yeah I I think the one major
problem that we have is how do we
upgrade our existing deployments to
eof cool thanks so much um Daniel um
what changes do you want to see uh
happen um on layer 1 evm before
potentially o ifying it how could this
uh potentially um interact with um the
vision you have for solidity um I know
there will be a talk on solity later so
hopefully no spoilers here um and those
so maybe how could these changes impact
others in the ecosystem
positively okay I mean I would say don't
aify the layer one in
general uh but yeah if people want to
aify the uh the layer one 1M then uh
yeah I could enumerate a number of
things that are wrong with it that make
lives harder for any compiler developer
and any tooling uh uh person uh UF
solves a lot of the issues so EF is a
good basic block that would uh in bulk
uh yeah reduce the complexity of
compilers reduce the complexity of uh
tooling and formal verification on top
of it and yeah I mean you also touched
on quite a few points already so uh if
L1 is to be rified please at least give
us UF in it first uh Beyond UF memory
Pages even maybe give us some registers
or something like that but yeah at some
point okay I would understand if you
don't but EF at least
please but yeah I mean uh effects on
other people I mean uh I'm pretty sure
that a few people have picked up on for
example the uh solar initiative of
rewriting a a new compiler to solidity
in in Rust they want to Target EF
because they know that it actually is
much simpler to build a compiler in a
language in EF so I mean that goes for
every language that goes for every
language every tooling will be much
easier to implement for EF because it's
much easier to generate code for it so
uh but you mean they would like to only
target the UF if they can I mean we only
briefly talked with Georges yesterday
I'm not entirely sure what their plans
are and they only so far have a part so
I'm not
sure uh but yeah it sounded like very
foolish on having EF and targeting EF
but I can't speak for them for the that
and Mainline solidity when do you drop
Legacy
support I mean we would love as soon as
possible it's a mess to generate code
for the evm so I mean uh we do have for
quite a while I mean I spent quite some
effort from the shangai version of UF we
wanted it then I mean we have a delayed
road map already because it didn't get
in then uh we now are in the process of
finalizing production support for the
new eof but there has been prototypes
for ages that were usable uh thanks to
radic also shout out to him uh but uh
yeah I mean it would actually help us
extremely in our road map for the
backand side of the language to uh to
have e and as soon as EF was there we
would try to we would expect users to
move to it immediately because all the
advantages in gas cost and everything uh
and would like to drop Legacy support as
soon as possible at least so you would
you would ask l2s to adopt it quickly
too as soon as possible I mean yeah we
of course would need to have a
transition period I know that
uh all right cool how fast is soon I
mean Lu
um you know due to the design decisions
that we made with the op stack
architecture it's just easy to rebase
onto you know the latest G release or
the latest W release and get all of the
you know functionality into the L2
itself now when it comes to the smart
contracts for the op stack on L1 that's
going to be difficult to Mig the bridge
today and we would need to deploy a new
bridge and you know figure out a
migration pattern and realistically
there's just other things that we
consider higher priority than you know
migrating to eof for our L1
contracts this is the specification you
mentioned regarding the bridges which I
think we just need to understand a bit
more um so maybe we don't have an answer
for but I I do I'm I'm curious about
like a different question the many they
diverge from the op stack do they have
like some of their own changes or it's
like vanilla op stack always oh that's a
great question so it's free software
people are allowed to do whatever they
want with we there's um this idea of
just using the vanilla op stack and with
that you kind of inherit all the tooling
that everyone in the community is
building so uh my personal philosophy is
that you don't really need to make
changes to the evm there's so many lwh
hang fruits with user experience and go
to market and that's where the next leg
of growth will come from and it's not
the you know adding a new pre-compile or
something like that
so if that bridging problem would would
be solved then potentially all these op
Tech users would be sorted yeah I mean
the the bridging problem um is like the
Legacy you know bridge that we have
today that's written in preeo is good
enough um it's really like the making
the front end more usable and getting
people to adopt smart contract wallets
that's inhibiting more adoption
you want to I mean I was interested in
the argument of importing tooling uh
from the vanilla version of of the op
stack I mean I would say that's actually
a nice argument also for EF because EF
has nicer transpilation properties so I
mean it's much easier without the gas
introspection and whatever mess the evm
has to actually transpile you have to a
more modern system so I think it would
actually be smoother to have EF and then
actually build a more fancy version and
import the entire tooling stack built
for a plain EF version
by a transpilation process without
having to carry Legacy cost so I think
that's also for actually a future proof
system actually a very nice uh property
of f have to be a basis for something
like
that right so yeah there's been a lot of
talk on UF um today as well and some
other days um this panel is not
particularly focusing on that but it's
the next plan evm upgrade and it's
basically going to be the biggest change
um in evm history um so definitely want
to cover it a little
bit so since it's a core protocol
upgrade obviously it has to be well
tested and I think concerns around
security or even introducing some
complexity on the client level
maintaining both Legacy evm and UF evm I
think most people agree on these
concerns and they want to make sure that
this all happen the right way but I
think what's interesting is that even
though it's in the road map profile um
there seems to be a bit of a discrepancy
when it comes to its impact um
and I see two main perspectives here
basically that one saying is that um EF
won't result in um too much performance
Improvement um and the future art forks
and abis should focus on uh other road
map elements that would result in more
settlement Le performance improvements
and the other one is that basically EF
is not really about performance but it's
just an absolutely crucial step to to
make the EV to like a more mature vual
machine even maybe help introduce um
endgame features and make it more ZK
friendly so Matt maybe uh let's hear a
different perspective here you you used
to be um um you actually um published
about euf after the merge and uh listing
its benefits and um mentioning that it
hasn't be happened because of these
other priorities like the merge um that
they were more urgent um has your
perspective changed on on prioritizing
the E
implementation um
yeah I was really and am really excited
about eof overall I think what it
provides is the things that evm
developers have been hoping for for five
six seven eight years but placed it on
the priority list personally is the
thought
that is it something that ethereum needs
to have to succeed in the next 10 years
or 20 years and I have felt since that
Revelation which was a couple years ago
now at this point that there are things
that we're still trying to do today with
respect to the execution layer and the
consensus layer to me
seem much
more much closer more closely addressing
these existential risks of ethereum not
succeeding in the future and I'm not
saying that it's time to a ify the L1
evm but I do think that when we start
talking about implementing changes to
the evm that are very
complicated I have to ask like if we do
nothing if we don't do these things what
is the worst case scenario
and as we're moving towards this rollup
Centric road map to me it feels like
that is the natural place for the
evolution to be see the motivation for
making all of those
Chang is there anything that maybe for
the impact analyis is from the
ecosystem um
anyway I think the thing this is not a
satisfying answer but I think the thing
that would change my mind is if we
decide that the rooll of centric road
map is
wrong you're saying that L1 is a
sediment layer in my mind I feel that
the clients should be the most robust
pieces of that ecosystem that is the
thing that cannot fail
and we can probably probably be fine but
I just have to like ask the question
adds more prob more surface area for
attacks to happen for issues to occur
not just today but in the future
implementing new clients and I
understand it's something that make
compilers so much better then to me it's
almost like saying you're taking
compiler code compiler complexity and
putting into L1 clients and when I have
this thought I think I want L1 clients
to be as thin as possible as simple as
possible focused on providing one thing
and right now that one thing is
settlement layer for rollups can I say
something
spicy tens or hundreds thousand lines of
code and uh and optimize assembly and
all that and different clients use
different versions of
these I don't like pre- compiles that
much I would love to have evm Max I
think that to me I would rather have evm
Max in the next hard Fork than eof I
yeah I mean we can go deep on kind of
why it depends on EF technically it
doesn't depend on it you can do it
without but with UF you get a
significant performance improvements um
because you can remove a lot of the
checks runtime checks and move them to
um deployment time checks and in the end
it this means whether it becomes
competitive against promise or not and
you know without eoff it may not be
competitive and then it's kind of
pointless do you have a comparison
between E versus nonf evx or if Factor
like a order of magnitude is it within
the same order of
magnitude for some of them so the checks
you have to do I mean the bunch of
there's also like code size um increase
if you do it with ATF that may or may
not be significant uh but you do get uh
let's say like 30% code size Improvement
um increase on every like evm Max
instruction if you do it with ATF um you
cannot like do any kind of optimizations
for pre-allocation or anything like that
um but the key difference is the runtime
checks you have to do at each
instruction um which you wouldn't have
to do with UF I think there were some
measurements for some of the
instructions maybe it's negligible but
it's also implementation specific for
some instructions it isn't negligible um
but generally no I don't have a proper
number to tell right I I mean yeah I
think that even with the eof version of
evm Max there's been thoughts that it's
not it's never going to be as performant
as a precompile itself and so how much
closer it depends actually um rodex Talk
mentioned one case libff one of the
certain client client or clients it's
actually less performant than evx now I
don't think G uses it uh so there are
much more performance implementations
than libff but even now today uh with a
precompile different clients may have
different performance yet we have a
single gas cost for it right and you
know in some cases evx would be faster
but yeah if you look at like highly
optimized code just in the context of
the pre-compile highly optimized uh
pre-compile would be cheaper but there's
another factor that in many cases you
have to use the pre-compiled multiple
times to achieve something you have to
call like addition multiple times you
have to call multiplication different
times and PR compil use a different form
you have to you know translate back and
forth with DMX you can skip all of this
you can create highly specific
implementations for the use case and so
you may have better performance because
you skip all of those overheads as
well so would you say the biggest
argument like let's say the difference
between eof evm Max and non eoff evm Max
is fairly substantial you would say that
the most important reason to have eof on
Main net is allowing people to implement
whatever cryptographic Primitives they
want without being blocked on waiting
for pre-c compiles for
those like what is what types of things
are you hoping for E uh for I mean eof
is great but I'm thinking like why does
it need to be on L1 and like one thing
I'm hearing is that there are
pre-compiled and I agree with you we
don't want to put that many more
pre-compiled on L1 but then the question
is like how many more pre- compiles do
we need is there going to be one more
pre-compile that all of the zero
knowledge rollups will be able to use
probably not so then to me there always
more so then to me the argument that
makes more sense is that eof gives you
this ability to write any kind of
cryptographic primitive that your rollup
is going to need to verify it Zer all
this pre compiles I think it's also like
another aspect there were if you look at
when the were uh proposed there were
like a a Hotpot I think 2020 was a hot
spot where people were really 2019 2020
when they this other aspect that if you
open up the space face the ability to
prototype new curves and new use cases
there may be you know a lot more stuff
spawning up there as well and like
another thing which never has been I
think there may have been like
discussion of the pre-compile but Stark
verification that hasn't been covered
but this would be able to also uh help
in that um but generally evm Max span
out e span out of evm Max so the core
idea was uh still wasm trying to induce
remove the pre compiles and you know
these are Primitives you need for it um
and we had evm Max as like some kind of
a idea
specification uh and it needed something
like UF to be really performant so this
was actually the progression how it came
about uh but we ended up those
optimizations e provides which are
beneficial to vmx they also beneficial
to to contracts and gives like an
upgrade path one to mention is you know
uh address space extension which has
been an interesting idea in order to do
like State expiry uh eof would also be
providing a path forward like address
space extension even the current version
addresses it mostly um and that could
open the path to State expiry now of
course we always have this question of
legacy and you know it's like a big kind
of worms and I also find it always a bit
surprising to hear this kind of like if
L1 only is the settlement layer then why
does it need any more changes I mean the
settlement layer is very relevant the
performance on it is re relevant and
correctness of it is relevant and I mean
if people knew what compilers have to do
in comparison to non UF code they would
probably scream in fear and run away
from any anything like that so I mean
these things I mean of course for
settlement layers you have a few
contracts that need can be formally
verified with large efforts but I mean
still I mean all of that this becomes
easier that the settlement layer becomes
faster it becomes more robust and uh and
verifiable all the ways up the stack and
I mean this complexity that I mean it's
fair to argue that there it's good to
have not that much complexity in the
clients but I mean avoiding the in the
clients produces an enormous amount of
complexity up the stack the entire way
so I would at least be careful in
weighing
that now you might ask why doesn't an L2
just adopt
eof so one thing is you know the L2
space it's still really early a lot of
the projects are still kind of fighting
for and it's harder to make long-term
decisions when you're worried about just
being around for the next few years so I
think that we need to see more L2
ecosystems reach escape velocity before
they'll be able to you know think longer
term and do things like eof um there's
also the problems of you know there's
like barely any stage one rollups in
production today right like most rollups
they're stage zero still um it's really
really hard to even get to stage one it
was way harder than I done we're still
working to get towards stage two and we
need to make sure that all rollups can
eventually get to stage two and until
that point it's really difficult to
think about um you know pulling eof into
um you know an L2
client yeah and that perspective makes
me wonder if we are getting ahead of
ourselves and we're not letting the
ecosystem develop and we're trying to
force something that is going to happen
naturally on the l2s and sort of top
down dictate what it should look like by
pushing it onto the
L1 I mean anything that comes to L1 we
automatically inherit as l2s we learned
that yeah I mean you know thank you for
I mean another concern is um you know
it's way less likely that all of the
developer tooling will get built if one
L2 ecosystem adopts it so when L1 adopts
a change there's basically a guarantee
that all of the tooling will you know
accommodate that change so that's like
another risky reason as to why an L2
wouldn't want to adopt something before
L1 does I still feel like this is a very
near term focused thing like I think
that if you take a step back and you
think in five or 10 years I don't really
see a reason that everybody will still
be locked in on evm equivalent if we
have reached stages to and we're
comfortable like rups are going to want
to differentiate and they're going to
have more resources and they're going to
find applications that reach a 100
million users or a billion users and
once you get to that point then the
developers will come and you're going to
be able to create totally different
ecosystems I mean there's still the
argument that the transpilation
properties of euf compared to Legacy of
so I mean even if that eventually is the
goal
sorry what what type of transpilation
would you want to do in that I mean if
you want to bootstrap a new set set of
ecosystem for a new evm then euf can be
transpiled to that new version and
inherit all the tooling without building
it from scratch and then you can import
all the tooling and extend from there
with Legacy AVM that's much harder I
mean are we just not overly focused on
reusing things and not starting from
scratch I feel like we went I feel like
you went down this path with ewm you
know we were all having these ideas like
let's just reuse the tooling around
wasum and then we got turned out to be
yeah I mean turned out that you know the
time spent on that like how many years
three four years during that time evm
tooling caught up you know we had a um
what was it uh hot anyway you know we
had all these Frameworks we had
debuggers those were lacking um taking
maybe a step back to to where you
started the answer to I think yeah we
started this question a while ago and
you had a long answer you know what
changed your mind and I think that was a
reasonable answer and I do agree with a
lot of it uh I think it just misses one
point you know several reasons are are
there why this EOS system works and why
the RO La Centric road map works as of
today uh I think one important aspect
which we don't talk that much about is
really the developer experience and that
each of them have the same evm you write
a you know a project an application once
you can deploy it on any of them um you
can you know you can optimize for
whatever you're optimizing for whether
you're optimizing for the given user
based on a chain or you optimizing for
the cost for the speed um or you
optimize for the longevity and you go
for main net you know it's much more
expensive but you can deploy the same
thing uh not only the same smart
contract but everything around it you
know the RPC and everything is the same
you can write once deploy anywhere I
think that's very P powerful and if we
start you know diverging in each of
these because we hope that one of them
going to do like bigger
improvements um that can only
realistically happen if one of them
becomes
dominating uh or they have some other
incentives to get all of these
developers and and tools and everything
around it um do we want one of them to
dominate maybe we do but I think this is
going to really take some time before we
get there uh while at the same time
there's some maybe other l1s or other
change or other directions which focus
more on developer experience um and
there's certainly people you know
whatever you give to developer velers
they're going to work at the round right
there's nothing stopping them right so
the evm is not stopping developers they
they find the work round um but you know
if somebody comes around and they have a
much better developer experience you
know that can Kickstart some changes um
and I do think that we we really keep
forgetting about developer experience
and we are not unlocking potential
enough if he would give you know slight
improvements I think we would unlock a
lot more and we may be able to progress
more rapidly
all right so
um a bit to that suggestion to to move
um developer experience improvements to
layer twos and Mark you um kind of
answered the part of that question that
a lot of layer 2s and z kvms are
currently basically focusing on
performance improvements as well
optimization so developer experience is
is in the plans but it's not necessarily
in the near future um um I think in the
last couple of days there were a lot of
talks actually that um surprisingly um
they had a lot of plans um to to improve
uh developer experience as well um what
do you think the timeline is here um and
also could things like standardization
or or these kind of initiatives maybe
help with this to to speed this up
totally yeah I mean I think that gr of
the ecosystem as a
whole um
I think that at least um you know we're
we're really starting to get to a point
where the actual L2 software is becoming
stable enough and reliable enough and
there's still a long way to go um like I
said previously you know there's no
stage two rollups like that are actually
used a lot in production today and
getting there is the number one priority
um you know we do want to improve
developer experience along the way um
and I think um with regards to you know
the ZK EVMS and um the kind of like the
fault proof VMS those are definitely
getting hardened um you know I know that
there's a lot of great um Z kvms that
have come out that you can just take say
rust code and compile it and stick it in
the zkv and not need to implement the
evm changes uh by hand at like a really
lowlevel abstraction and interact more
closely to all the circuits and
everything like that so these uh as
these zkv Ms become you know more and
more optimized have been being told that
you know there's orders of magnitudes of
optimizations coming over the next few
years um where I think it'll be a lot
easier to just take um any arbitrary you
know L2 sof software and be able to
create ZK proofs for it um I think the
idea of you know ZK rollup and
optimistic Roll Up is kind of fake there
shouldn't be a distinction it's just a
rollup this idea of like optimistic or
ZK that's a property of the bridge and
that's not a property of the rollup
right the rollup is not the bridge
they're two different things I think
this is like a really big
misconception and I think that um you
know we we're going to get to a point
where all the Z kvms are good enough
that the stacks that are based on
optimistic rollups will be able to just
adopt
it okay cool so I would like to talk
about this layer to focused um evm
standardization initiative which is
actually an act actual practical step um
towards uh ler to standardization this
was launched last year um introducing
monthly roll call um roll calls and U
rips or rollup Improvement proposals
um and they've been happening every
month um and basically these are
optional standards for layer 2os um to
adopt if they want to um has your team
been involved in any of those totally
yeah we have um reviewed a bunch of them
and um I've personally attended a couple
of the calls and um we also adopted the
I think it was maybe rip
the RP process is really useful for kind
of
drisking frag more fragmentation between
all the different you know rollup
Frameworks um I do think though it is
still pretty early given that you know
all of the uh most there's no stage two
rollups so it's hard to focus onization
when everyone is still you know trying
to actually real rollup
software okay right so on a recent draw
call um there was also um something new
um introduced which is called I think
the layer twos to be equivalent with
each other but not necessarily with
layer one anymore um and also handling
together um future layer one evm changes
and make sure that are no conflicts um
with those changes um thenia what's your
take on these just generally on these um
coordinated layer to optimization
initiatives how could this
unfold yeah I mean that's great of
course I mean the only way that we could
ever accommodate anything on Layer Two
that's not layer one is if it's a
coordinated effort but I mean the
problem is that we're busy with working
around the issues of the layer 1 evm we
also still don't have the time to
actually really look into doing Layer
Two work specifically because the layer
one work is an extremely huge mess I
mean of course I mean layer 2
sanitization definitely a good thing and
and actually definitely necessary for
having anything uh any tooling support
for layer tws in common but yeah I still
would uh say that there is more space to
actually accommodate Layer Two changes
with a simple layer one at this point in
time right um sir we are running out of
time a little bit but if you would like
to learn more about this initiative and
Scar actually the um K of this
initiative we'll have a talk on this
later on today at 540 I believe on stage
one but make sure you check the schedule
um right so um maybe just one more thing
quickly um Matt have you heard of the
roll up get uh
initiative maybe just uh share a few
thoughts on that before we close yeah
they definitely heard of the roll of gu
initiative it's a it's very super
interesting project I think that what
they're trying to do is what needs to be
happening right now because we're not
going to be able to avoid l2s if there
isn't some kind of coordinated effort
and it feels like the best coordinated
effort is by making their lives easier
and For Better or Worse most l2s are
based off of L1 clients so finding them
an L1 client that is maintained by a
team focused on maintaining the
coordinated the accepted um proposals
and coordinating amongst the rollups to
figure out what proposals to accept and
for that team to implement those things
make a lot of sense I
I'm just very curious to see how it ends
up evolving over the next couple years
like Mark said you guys are super busy
getting to stage two and yes you can
just your Upstream to be a different
client but I think that the reality is
going to be a lot more complicated than
that as these things always are okay
yeah totally having um you know this
kind of neutral rollup gu is great but
it does add you know some governance
risk to the supply chain
so um I imagine that it will need to be
relatively conservative with what
actually ends up in it um and yeah like
I think that in an Ideal World nobody
needs to use a fork of gu and you can
just import gu as a library and kind of
you know decorate it with extra
functionality um this is like one thing
that is kind of interesting about like
the W project where W um is kind of
looking at l2s as um customers or users
and tries to like build abstractions
that make it easy for you know users to
or l2s to like build into ref but with G
it's important to be credibly neutral so
there's tradeoffs here all right cool so
um we have three more minutes actually
less um anything you guys would like to
highlight or any takeaways uh from this
finel um all of you maybe uh let's start
with Alex well I mean I have questions
on okay I I'm not sure if we have time
for those because we will have a bunch
of um yeah maybe we have the Q&amp;A as well
um maybe some of this is um I mean even
now the different l2s like they have uh
uh differences between them mostly on
the ZK level because they cannot support
like each of those or you know there's
gas
differences are you I'm not sure maybe
Mark you're the closest
um yeah how do you see like evm Common
Core what is the first goal of it and
maybe what is the medium-term goal of it
is it like making sure that even these
differences don't exist or it's like
introducing new stuff or it's just too
early to tell totally to be honest I
don't know a ton of information about
evm common core but at least what I
would like to see out of it is um
introducing new things as there's desire
to you know improve the evm then it's
about doing it in a consistent way right
like no L2 team um it's like we we used
to maintain a fork of the solidity
compiler very very difficult so like
having one set of tooling that works
across the whole ecosystem is really
really
nice anyone else any conclusions or
things to add quickly because we are
running out of time
no I like the first question oh okay
yeah questions are um coming soon um
Alex anything else I mean I could go on
forever but why don't we just look at
the questions and we can maybe I okay um
do you think that any of these uh Layer
Two standardization initiatives could
help with shipping um some of these
changes faster on layer one like maybe
some layer 2's um adop those and and it
works and then maybe the GU team says
like okay fine it works it didn't break
anything could this uh do you think it
could improve this I mean my fear with
this idea is that L1 teams love touch
the standards they love to leave their
little marks on them and modify them
just a bit to fit L1 perfectly and I
struggle to see how we're going to do
anything complex on the layer two first
and then bring it you know bring it
exactly as it is on the L2 on the L1
even just with the p256 pre-compile the
L1 Dev say maybe it's at the wrong
address maybe we should move it to a
different place BLS we're trying to
figure out like what are where what is
the exact parameters that are going to
go into these functions where are these
functions going to live like what are
the address of these pre- compiles doing
these things on the L2 is just going to
constrain what the L1 devs are going to
be able to do so you're seeing the level
of nitpicking is a bit uh bit more on L1
or it's extraordinarily High Yeah it
it's to be high quality but on the other
side do you think there's a different
need of like evm changes specifically
you think like l L1 has different need
of what evm should look like versus l2s
I think L1 has different needs than l2s
and I also think that incremental
changes are the best way to change the
protocol yeah but on evm do you think it
has different needs on L1 I think there
are different needs than L2 okay cool
thank you guys unfortunately we don't
have any more time but uh there will be
time to answer uh questions from the
audience so thank you so much uh for
joining us for today's panel don't we
have time for the questions yes the they
are coming up from yeah can and thank
you very much for our wonderful speakers
uh my name is Khan I will be your MC for
the next three hours for this stage um
let's move on to questions before taking
more time I will start with the topmost
one this question goes to Matt uh why do
you consider compiler bugs less scary
than execution client bugs I have
written both I written both andm
implementations they really really
wanted to ask this
question um so the way that I see it one
I'm a client developer I try to keep the
L1 safe that's my primary goal so I
don't want to like belittle the job of a
compiler developer it's thankless and
it's very difficult but similarly to
like keeping their codebase safe and
secure like I am trying to focus on
keeping my codebase safe and secure I
don't want to try and then you know have
blinders on and push all of the
complexity on the L1 into other places
but my perspective is what does the L1
provide what do blockchains provide that
no other facility in the world provide
and that's a platform for Unstoppable
trustless execution of code and to me
what you need to have happen is you need
to have a blockchain that works doesn't
have faults and if you need to write
applications on top of that yes it's
great to have a greater developer
experience it's great to have a great
compiler a safe compiler but we do know
ways of writing code that's safe
formally verified it's just extremely
painful so I know that in the absolute
worst case if we provide the L1 people
will develop applications on it maybe
those applications won't be as nice as
people want them to be or they won't be
developed as fast as they want to be but
I believe that if we give them the
platform to develop the applications
they will build applications that
actually use the platform in the way
that the platform is trying to provide
and why should they use the platform of
any other competitor that does have a
better layer one
instead sorry I see the first part no I
mean if you aif I mean who's to stop
starting a new layer one train that
actually has the better experience on
that level as well and then people
moving to that because it has the same
guarantees just only in a nicer way I
mean we'll have to see how these types
of things play out like you can already
see there is a bit of a there is a
comparison of ethereum and salana and
ethereum is as Josh said in his opening
speech the thing that does not go down
many of the eth competitors have the
meme of like going down salon goes down
Iota goes down these other chains are
not as resilient as ethereum and how do
we maintain this property it's by being
extremely thorough with the types of
things that we put on Main net that's
not to say that we should get stuck in
this mindset and totally aify but I
think that it's like something that we
have to balance very carefully and what
ends up happening is you have people who
are farther on my side who tend to think
that we should be more oied we have
people who are trying to accelerate
what's happening and we end up somewhere
in the middle it's just not a fun
process everybody on this panel is
extremely reasonable and pleasant to be
around but we just end up up here
arguing about what the ethereum evm
should look like
Fair um so the next question is around
in incompatibility around the VMS our um
attendee asks that they don't understand
why a bunch of a in bunch of
incompatible modifications to the same
VM across different L2 chains is
considered beneficial isn't it good to
have everyone on the same high quality
VM anyone wants to take
this the same VM I mean we all want the
same VM but um at the end of the day
it's a free market for you know scaling
ethereum that's kind of like what the L2
uh Centric road map is all about so you
know any project has the right to modify
the evm in any way um but you know the
reality is that there's a huge cost to
modifying the evm just because the
tooling is so
important I think this goes back to to
what you said earlier that
um if something uh maybe with the one
pre-compile now maybe that could be the
first occurrence um but this basically
you know this
question is if you do get it on on L1
the same high quality stuff we ensure
that everybody gets it um if some L2
adopt something maybe another one adopt
something else
uh it's unlikely to ever reach L1 so
there's going to be you know a lot more
diverse version of
FMS we have new questions coming in and
the leader board changing the next
question is what will be ipsilon Focus
after
E I guess I can take this it's evm
Max thank you the next one is in what
ways could alternative languages I move
or others bring new functional I mean I
guess I can try to take that but I mean
all the languages have the problems of
the evm as long as the evm is the Target
so I mean language there's only so much
that the language level can do I mean
you can try compilers to try to work
around the issues of the evm there can
be languages that are designed in a way
that are more in which that's easier but
uh but yeah I don't think that the
language level is the level to solve the
issues that the AVM currently
has adding an alt VM um you know at the
end of the day if we think about alt VMS
like one of the big bottlenecks in the
evm is you know like IO like reading and
writing and a new VM is not going to
solve that it's still going to be just
as expensive to read and write from disk
so like a like adding an ALT VM maybe
where um it's easier to you know build
like a emit native code that you know
Works off of you know 64 bits instead of
um that's like a way to like optimize
you know the execution but it's only
really useful for things that don't read
and write from
disk so the next one is around the evm
again the evm going to is evm going to
stay overall the same throughout the
next years or is there any possibility
radical changes to update to modern
architecture targeting smart contract
needs I guess there's one listen listen
to the panel yes I guess there's one
change
upcoming I hope at least
yeah right then the next one um
discussion here suggests the rollup
Centric road map reduces the complexity
in L1 yet with the diversity it means
compared compared to Native homogeneous
e two shards isn't the opposite
true whose complexity on L1 his not mine
at least
moving on with the next question are
going to innovate more than
L2 you know I think it really depends on
the particular L2 ecosystem um you know
some l2s like you know fuel um Stark net
like they're very very different so
anybody has the right to build tooling
that exists and you know maybe uh
contribute
improvements to the same tooling so that
L1 also gets the improvements so yeah I
think that the reality is that the
bottleneck for adoption today is based
on user experience and go to market and
not improvements to the
evm I also think in general like with
l2s you have the opportunity to try many
different flavors or have different
focuses whereas the L1 is the singular
thing you can't really be super fast
super decentralized you have to sort of
choose on the different axises that you
want to focus on whereas for an L l2s
you could have something that's you know
privacy focused only you can have
something that's extremely fast but
might go down something that is you know
has Central points of failure and I
think that the l2s like have the
opportunity to experiment on those
different axes that the L1 just doesn't
have I think like can el1 specifically
it's a bottleneck issue that uh you know
there's only as many people there uh
which are and they don't really have
time for some of these proposals even
including EF you know a couple of years
ago nobody had to have like a proper
discussion and and you know get any of
the opinions closer um I do think that
UF could have been like you know
couldn't shouldn't have been like this
big of a debate and this big of a change
and could have been done much earlier if
there would have been more Bandit um
that's ultimately what we are fighting
around um so we're running out of time
that that will be the all questions
we'll be answering but feel free to
catch our
speakers um our next session will be
starting in a few minutes feel free to
stretch and we'll be back soon
now
m e
on a project called sourcify at the
etherum foundation and now moving on to
the Argo Collective if you if you
catched that talk um but without further
Ado I want to introduce our next speaker
storm who is a researcher at Paradigm he
will be talking about Sovereign data
Sovereign data what why and how please
give a round of applause for
storm uh
great
um one sec the I need the uh display not
mirrored
yeah one moment
it's it's mirrored I need it not
mirrored yeah sorry one moment
uh okay I think I think this will fix it
great uh
yes cool oh let me
maximize
uh okay here we go hello everyone
uh and I want to start with a question
so let's say that you need to analyze
ethereum's
history and I don't just mean in a
simple way let's say that you need to
analyze every block or every transaction
or every state diff what resources do
you need to analyze these
things I'm here to tell you
that um you don't need very much you
don't need the cloud or any Clos Source
software you don't need a team of people
to maintain your infrastructure and you
don't even need a database the main
takeaway from this talk is that you can
analyze ethereum's complete history
locally on your
laptop and this is enabled by a lot of
recent advances in open source data
tooling that make this process really
easy and really fast and sometimes I
describe it as it's like having big
query on your laptop but it actually
goes beyond that in a lot of ways uh
because for many workloads this is
actually faster and easier than using
big query
this is all enabled by an approach that
I call data
sovereignty So the plan for this talk is
I'm going to start off by defining what
is data
sovereignty and then I'll explain why
this is
desirable and then finally I'll explain
how data sovereignty actually works and
show you some live
demos the overall mission here is to
convince you that data sovereignty is
easy and fast and
Powerful so in a nutshell uh data
sovereignty is just having full control
over the data Pipeline and this goes
further than just having an open data
set really special things happen when
the entire data pipeline is open source
it's modular using Open Standards and
it's available for you to run locally on
your own
machine even if you don't actually want
to run it on your own machine you can
still get many benefits just by being
adjacent to the tools and and the
ecosystems where these principles are
prioritized so what are the actual
benefits just like with the terms open-
Source software or decentralization
there's kind of two ways to answer that
question there's the ideological side
and there's the Practical side
ideologically data sovereignty is the
purest form of making data free and
open and your philosophy might be that
you want complete control over your data
data sovereignty is how you do
that on the other hand there's lots of
practical benefits uh this type of
workflow is often the easiest and
fastest way um to get the answers that
you're looking for and this is because
it's powered by a rich open source
ecosystem that is continually evolving
uh these day these days there are
hundreds of different tools you can use
to analyze crypto data and most of them
weren't built for crypto but we can use
them thanks to the power of Open
Standards and
modularity another benefit of data
sovereignty um is that it can give you
an extremely simple infrastructure with
low maintenance burden and this is
relevant because most crypto companies
don't have large data teams they just
have a single data person and this means
that we need systems that are easy for a
Solo solo operator to
use and as a final moot motivating point
I think that more data sovereignty will
improve the EIP process ethereum is a
really complex system so when somebody
proposes a change it's important for us
to evaluate that change using the
relevant data um so what are all the
downstream effects of this proposal is
this proposal actually addressing an
important problem sometimes these
questions can only be answered using
data and in the past it's been kind of
difficult uh to use ethereum data but my
hope is that as data tools become better
and better this will lead to the EIP
process uh becoming more data driven and
that'll lead us to better
eips so how do we actually do data
sovereignty we basically just take a lot
of the tools and best practices in data
engineering and we apply them to the
crypto world and people have been doing
this more and more the past couple years
so here's a flowchart of how I do most
of my
work you start with an e an evm archive
Noe and then you use an ETL tool like
cryo to extract data sets from the
node that data gets saved in files on
your computer um often in a modern
format like par and then finally you
query those files using an engine like
polers or duct
DB and that gives you results that you
can use in your eips or your dashboards
or whatever
else and one of the really nice things
about this workflow is that it's very
very modular you can run your own
archive node or you can use a thirdparty
RPC provider you can store these parket
files on your laptop or you could store
them in
S3 and you could uh query these files
from your laptop or you can run some
sort of cloud computing
engine and this highle of flexibility um
is a direct consequence of having a
modular ecosystem built on top of Open
Standards so let's zoom into the first
step in this pipeline which is data
extraction last year I built this tool
called cryo for collecting blockchain
data sets cryo can take any type of
information available over RPC and turn
it into a nice simple local data set
this can be simple stuff like blocks or
transactions or more obscure things like
op code traces JavaScript traces uh
really anything that's an RPC method so
a lot of this data can be really nested
and messy when it comes out raw out of
the RPC endpoint but cryo puts it into
simple flat tables that are easy to
consume and you can use it as a CLI tool
or as a python library with the syntax
shown
here so let me show you a demo of what
uh cryo actually looks like so let see
if this
works
okay
cool so
um the most basic usage is just
collecting a vanilla data set so let's
say we want to collect all the logs over
some block range uh we can do cryo logs
and then a block range like let's
collect from block 10 million um and
then 100,000 blocks after
that and if we do that it will collect
this data set and save the output to a
bunch of parket files that are now on my
laptop um which you can see here and
it's and all of this is happening only
on my laptop I'm running a base chain
node on the laptop as well using
ref and this interface is really simple
I could change to be a different data
set like blocks so instead of logs I do
cryo blocks and it would collect blocks
over the same
range um and you can see that it
collects 100,000 blocks in about 2
seconds um so if you want to list out
the different uh data sets that cryo can
collect we can do cryo help data
sets um it'll list out a bunch of things
there
um and is totally item potent so let's
say we want to collect a longer job like
collecting a million blocks instead of
um I can just kill the job in the middle
and it doesn't matter if I restart the
job it'll just pick up where it left off
um and there's no corrupted files
there's no things to worry about in that
regard and so it's done I'll kill it
again restart it and then finally uh
when the job is complete um you can see
all the collected data and if I try to
run it again pryo knows all the data has
been collected and it just exits
immediately and there's a lot of other
options as well um and just for the
purpose of time I will sort of return to
the presentation now
great so a lot of the magic of modern
data tools is just having really good
file formats par is the most common
format used by modern data tools outside
of um crypto and it's the out it's the
default output format of cryo as well
paret can be seen as an extreme
evolution of CSV most of you have
probably seen CSV files before they
store tables every line in the file is a
row in the table par stores tables as
well um except it does so in a much more
sophisticated way it breaks the rows and
the columns into separate chunks and it
compresses them and it indexes them so
you get a very compact representation
that can still be used for efficient
queries that only read the subsets of
the file that are relevant to you so
this leads to huge benefits in both
speed and storage
size and there's now a huge ecosystem of
tools that can create and read and
update parket
files here are some examples of common
data sets that you might collect using
cryo and the size of those data sets uh
when stored as
paret uh for example it takes about 100
GB to store the erc2 transfers from
throughout ethereum's complete history
and you'll need different data sets
depending on what you're investigating
if you don't have enough room on your
laptop you can also grab like a really
cheap multi-terabyte thumb drive um on
Amazon these
days so now I want to show a few demos
of actually using these data sets um and
I'm going to do this using entirely
local processing on my
laptop so let's return
to
endline and
okay so I've collected in this directory
blocks erc20 transfers contracts logs
and in each of these folders it's just a
directory full of files so if I do LS
logs it's just a bunch of files
and just to start off really simple um
one thing we might want to do is gather
all of the contract addresses maybe we
want to um label all of the contract
addresses on ethereum or maybe we want
to put them in a filter somewhere so I
have this script that just queries all
the addresses from the contracts data
set so if I if I go B demo
zero um it's the main Chunk in the
middle that matters here um
this contract equals thing and this is
using the polar's library to scan a glob
of files um and it also selects which
columns that you want to put into a data
frame right here it's just one column
contract address run this
script
using like
that oh we need to
go slash slash in
front yeah so it'll load all 67 million
addresses from ethereum um in about 1
second so if we time
it it's very fast 77
seconds and that that's loading all the
addresses into
memory so now let's say we want to run a
more useful query like let's check what
are the most common bite codes for these
sex for these 67 million addresses or
for the yeah for these 67 million
contracts so I wrote another script um
demo
one actually before I run it let me show
it so similar story um there's this
contracts query used by uh polar's
Library I'm selecting which columns I
want here just code cach and then I'm
adding this extra function value counts
that's uh going to count the frequency
of each by code so if I run it
it'll load those contracts again load
their bite codes and here you can see it
found almost 4 million unique bite codes
among these 67 million contracts and
it's also showing the frequency of each
bite code here are the top 10 and it was
able to do this in about 3
seconds oh yeah the screen's a bit small
so yeah can't quite
fit and then um another thing that we
can do is really efficient processing of
erc20 data so let's say we want to look
at wbtc and we want to load all of the
wbtc
transfers so here's another script uh
demo here it's still very simple we're
scanning a blob of files here I'm just
reformatting um the addresses as
hex but like let's let's run this script
and you can see very
quickly it loads about 8 million wbtc
transfers in about 1
second and it also loads all of the
relevant meta metadata about each
transfer like the transaction hash block
number sender receiver all
that and also note that this allows us
to process data sets that are much
larger than our memory size the the
erc20 transfers data set is 97 GB and
that's larger than the memory I have on
laptop and finally let's compute um all
of the WT wbtc balances of all
holders and so this final script is a
bit more
involved it's
finding you're not going to be able to
see much on this tiny little screen but
it's basically Computing the flows and
outflows to each address and aggregating
by
address so if we run
that we can see we basically compute all
of the holders of wbtc and here we're
displaying the top 10 and it it also
computed for 100,000 additional holders
and it does all that in about a second
and a half and this isn't this is not
specific to wbtc you can do this for the
majority of erc20 token tokens you can
get really fast data on the
distributions of those
tokens okay so let me return to the
slides uh but things can get a lot more
complicated in practice I want to finish
with a couple final thoughts uh first
thing is data sovereignty is not an All
or Nothing thing you can think of it as
a spectrum to decentralization there are
different levels to sovereignty
uh maybe something is closed Source but
it uses Open Standards or maybe it's
open source but you can't run it locally
and in the same way that you don't
always need 100% decentralization you
don't always need 100% sovereignty I use
plenty of tools that are not sovereign
all the time uh you should always be
using the right tool for the
job and the final thing I want to say is
that sovereignty is a uniquely ethereum
phenomenon ethereum's design philosophy
prioritizes introspection of what's
happening on chain and this has enabled
a rich ecosystem of tools that
collectively make the Sovereign workflow
possible this is the culmination of many
years of work by many idealistic people
um so I think we should all appreciate
that we're in a pretty awesome situation
with respect to data and I think it's
only going to get faster and easier and
more capable as time goes on
so that's everything I wanted to share
thanks for
listening thank you very much storm for
this insightful talk I guess everyone
who's new to data or who is already
familiar learned quite a lot today and
also you killed it with the live demo
the live demo Devils were away from us
today yeah it was a little
nerve-wracking right so I'll move on
with the questions um the first one from
the leaderboard word is is it suitable
as a subgraph replacement consumed by
end user front
ends um so the workflow that I'm showing
here is kind of more suited to
historical data analysis rather than
live data analysis um there are some
extensions um that could happen in the
future and it's something we've thought
about like for cryo and for other
related tools but the focus here is
really on historical data
analysis the next one is if the if you
can use cryo to serve my app which needs
near realtime data uh that's basically
the same question so same answer all
right um next up what does it take to
build similar tooling for L1 and L2 uh
the tooling is exactly the same so this
was actually technically an L2 demo uh
because I'm I'm running a base chain
node on this laptop and I was quering
all the data there um R Json RPC is kind
of like a common lingua franka of evm
nodes so anything that speaks Json RPC
you can do the same exact uh sort of
flow with cryo and then polers is even
more General it can process any parket
file you
want how hard is it to define a new data
set um it's it's actually not that hard
so in in cryo for example each data set
is just a single simple file um sort of
like finding the flow of like take the
RPC data manipulate it a bit a little
bit and then like output it as a row um
cryo already has a ton of different data
sets though so you probably don't need
to Define new data
sets uh what is the most common contract
eth uh I'm not I'm not sure I think it's
it's probably either a proxy or like a
unisa pool I think I can answer that uh
in Source 5 we have a data set as well
and I think it's gnosis safe proxy ah ah
nice that makes sense at least to our
data sets why Solana is not data
Sovereign well it's it's kind of the
reasons I listed so salana it it just
hasn't really been a priority um to make
introspection of what's happening on
chain really visible um the scale is
also an issue with salana um it it's
basic the salana data is basically too
big to fit on any local machine so
you're not going to be able to do local
processing there all right that's it
from our questions let's give a big
round of applause for
storm thank you very much for this
session and we'll be back in a few
minutes with our next session
hello
everyone uh welcome to the stage three
we will be continuing with our talks
today in day three of Deon um next talk
will be about the soli future and
present before for the talk I just want
to remind everyone to uh read the Q
session QR code which will be showed
here in a minute if you have any
questions you will be able to ask your
questions to the speaker um before
without further Ado I want to introduce
our dear Vish who will be giving the
talk today
wish here and thank you so much for
joining for my talk um this is actually
my first Devon so um really
excited what is a dog without some
hiccups
right oh that has skipped a little bit
let's go back all right so we're all set
uh hi I'm Vish um I'm a developer
Advocate at solidity um which is now a
project that's part of the newly formed
Argo formerly EF um I focus I've been
part of the more than a year now um I
mostly Focus currently on external
Communications helping the team um work
on and maintain
documentation um relaying in inter and
external important feedback to the
engineers so that they can focus on
shipping the right features for the
community and also some really cool
special projects like solidity Summit
and the annual solidity developer survey
Etc now that we have the boring
introduction out of the way uh let's
talk a little bit about my talk um as
the title suggests I will be talking
about how we started as solidity some of
the past highlights um the state of the
current language and um the recent
feature developments and where we are
going with
it so for how it started I wanted to
make a little call back to Devcon 3 um
from 2017 one of our team leads former
team lead now uh talked about um uh you
know like the initial goal for solidity
and the cost of moving fast with
features
um and then the path forward for a
language like solidity so I think when
we started um solidity as a language uh
the initial goals were something very
simple for a language like um a smart
contract language like solidity like we
wanted more people to write contracts
and not just write them but write them
correctly so unit tests and formal
proving Etc right and we also wanted
more and more developers to start start
writing smart contracts and solidity so
similarity to a language that they knew
like JavaScript was important so that
was one of the goals and type safety
blah blah blah when solidity was started
all these many years ago I think it was
like 9 10 years ago um the initial goal
the overall goal was also to make the
language generally usable for people um
as a high level language as fast as
possible which led to certain decisions
that in hindsight we would like to do
differently and that's also part of
something that I will be talking about
in this talk the language is now on a
path to make some important changes and
um we will be covering that in the final
section uh this is a really cool screen
grab that I got from that talk that I
mentioned um inside the compiler this is
how the code used to look like and then
when we introduced ulia which is now
called U the that's how it changed a
little bit from more convoluted code we
got to something that's a little more
readable um and I wouldn't want to go in
depth into this but this is to say that
the language has constantly been um
evolving a lot and I'd like to talk
about some really cool features that
we've um released recently but before we
move on to that I'd like for you folks
to meet the team so meet the solidity
team now we've also the team has also
evolved quite a bit on the development
side of things we have Alex Daniel our
team lead um Camille Matas Moritz who
has recently joined us Nicola and
Rodrigo
s um franzy and I work on community and
ecosystem uh we have Nick who leads the
eth debug the new debugging format um
smt cheer we have Martin uh Bava helps
us with fuzzing every now and then um
March and Rigo are have recently been
working very actively um with us on
language research and we've also been
collaborating with external teams like
fee and formal verification that are now
um part of the larger Argo Collective
with us um including other teams such as
sourcify all right so moving to the main
um juicy buits the recent features and
language developments
talking about new features uh Transit
storage has been one of the longest
awaited features on the evm level um
just as a quick definition Transit
storage is a new introduces a new data
location which behaves similarly to
storage but as a distinction it is not
permanent rather it um is only scoped to
the current
transaction um we saw a lot of interest
for support for Trans storage so um we
began rolling out this support for
Transit storage with the release of
solidity version 0.8.2 4 using two op
codes um in inline assembly um namely t-
store and t- load that you can use to
access the data stored in these
locations um over the course of
subsequent years uh sorry months we also
saw an influx of interest for support
for Trent storage on the um language
level uh the high level language support
so we introduced parsel support for
transends and storage variables in
types in
community uh the support for specifying
storage locations for storage variables
was one of the most discussed um issues
in the past few months that we got uh
it's it's an external issue that you can
see linked um in the first in proposal
to allow specifying storage locations
and this progress was triggered by the
EIP 7702 so if you know the EIP um it it
would be nicer if we have um if we allow
users to specify storage locations to
avoid
conflicts we shared a proposal for
explicit storage layout Syntax for
feedback because we saw really active
participation by the community to push
these discussions forward and then
further ected a candidate for
implementation so if you see the
proposal and I hope that these slides
will be shared with the audience somehow
um if you see the proposal there are a
couple variants and we selected variant
two um and you can read the rational and
specific uh the specification under the
original issue but this is how some of
the implementation uh of that could look
like another one of the most requested
features from our user Community was
require with custom errors um and we
rolled support for that in uh
efficient way of letting the users know
why an operation is failing right to
make it more intuitive and we do this by
introducing a new overload so what you
can do is you can um it actually lets
the user uh Define a custom error
message as um a second argument to the
requir function and that's a little
example of that of how you can use
it all right so one of the bigger chunks
of the talks um yir that was also a
major update that we made to the
compiler um how many of uh you people
here know about
yir that's a few people nice how many of
you have used it for compilations of
your cont contct s it's also a good
amount nice so for those of you who do
not know why all right it's a new
compilation Pipeline and solidity which
introduces um another intermediate step
um by first translating the solidity
code into an intermediate representation
in our case Ule instead of directly
compiling solidity code into evm bite
code um it is a more Modern Way of
compiler design design and it uh gives
us a couple of couple of advantages
we've been talking about yir for a while
now and we have limited time so I will
try to zip through um these advantages
but of course like if you are aware of
um how an intermediate representation
sort of helps compile a design it adds
this like layer that allows for powerful
optimizations um transparent and
auditable code Generation Um obviously
better gas efficiency and also
eliminating stack Tod beers which was
according to our solidity survey um one
of the main pain points over the past
few years so we're happy to be working
that it also gives us feasibility of
multiple backends and front ends um to
clarify a little bit um it is designed
the intermediate representation is
designed with the goal to serve as a
backend for multiple
compilers um a major example is the fee
language uh it also targets it's
multiple backends initially evm and ewm
and now EO eof ethereum object
format it is intended to be a backend
for experimental solidity well
experimental solidity is supposed to be
a thin layer of um type system over U so
it only makes sense that it is um the
backend the intended backend for
experimental
solidity all right recent performance
optimizations we are well aware that the
compilation um using the yir pipeline is
not the fastest right now but the team
is constantly working on making it
faster and more optimized um with every
release and I'd like to talk a little
bit about it um we to make the
compilation V faster we've been um
working on certain features the first
one was released in
update that uh es the U Optimizer step
sequence to make it newer and faster we
also started caching optimized IR to
make um the compilation times a bit
lower um and this was released in 0.8.2
of U ests only on demand to make memory
usage more efficient um and that was
released in
of other um smaller
optimizations but based on our
benchmarks and our data we've seen that
um we only started making significant
changes in the reduction of compilation
times and efficiency um in 0.8.2 one and
further yeah so this is a little uh plot
that we've U made to sort of represent
what it looks like what the changes look
like and The Improv M ments look like um
the three projects that we've used for
the benchmarks are open Zeppelin Unis
Swap and IG layer overall this has been
um uh the change in compilation time of
Benchmark projects across compiler
versions and this has been compared to
soulc version 0.8.1
compared to solidity version
reduced by 50% for
sein 69% for UNIS
Swap and 81% for igon
layer um now ongoing work on compilation
via IR um of course there is eth debug
and if you did not listen to Nick's talk
on eth debug and his current work around
it um it would be really cool if you
folks um checked out the live stream or
the talk when it's up later but it's
going to it's a new debugging format
that makes debugging better for the IR
pipeline
specifically we have also been working
with project Gray from University of
Madrid so huge shout out uh to project
gray members for helping us making um
Transformations for of the U IR um to
evm bite code Transformations improved
and more efficient they use ssfg
optimizations to speed up um compilation
time and to help us improve this so we
are still working with them to
investigate how this is going to make
our work around this
better all right what's next with
yir well we talked about um making yir
the default P default pipeline um back
in solidity Summit 2023 um so I'd like
to give a quick update uh that sorry uh
I'd like to give a quick update that
we've decided to tie that upgrade with e
for a few reasons two main reasons being
that eof has certain features that it um
like unlimited swaps and dupes that make
U to evm transformation significantly
simpler and more efficient and this will
help us um eliminate some of the
remaining stack to deep erors that is
one of the main goals for us to make yir
default um since the Y and EF upgrades
are both containing minor semantic
changes and the um uh update will
require it to be break a breaking change
combining combining the release will
make it um easier for us to reduce the
upgrade burden on the solidity solidity
ecosystem and the
community um we've had a full
implementation for eof for a while now
which has been on a branch but
unfortunately it hasn't been approved by
all civs for a merge in the H folk so we
really hope that um for instance since
the Epsilon team has been working on an
extension of eof which makes it um more
powerful and we hope that that can be
merged in um what is now scheduled for
the Osaka
upgrade we wrote an explan explainer
about Y and everything around it uh also
tying it to e so if you want to go check
that out that's up on our
blog and now one of the main um sections
which is where we are going and what is
the solidity
future before we jump into what is
planned for the future let's take a look
at what current solidity looks like and
what are the issues with
it as we learned in the beginning of the
talk solidity has sort of by um the
community and um all of these like
various features um that we've worked on
it hasn't been worked on in a much
logical manner
um this kind of compiler hardcoded
functionality can sort of increase the
complexity of the language the more and
more features that you add to
it the language is also not extensible
at the moment so that is also a major
issue and it makes adding newer future
features to it come at a high cost um
and at higher risks so we cannot move
faster with feature requests from the
community what what's missing generics
there is currently no concept of
generics in solidity which would be nice
to have it would also be nice to have
formally defined semantics that's
currently missing um and that that's the
reason for that is that because we have
so many features that poses special
cases that the um semantics cannot cover
or makes it difficult to do that um we
don't have formally defined semantics
that we'd like to have which would be
important for something like solidity as
a smart contract
language and all of these problems
combined mean that we also have a lack
of feature um lack of a set of features
that users actively request or need um
that the language cannot express at the
moment without taking major risks um and
compromising on
Simplicity um like immutables of
reference types and we've also currently
having the similar same concerns um for
support we Trends and storage especially
full language level support for
that um going forward there can be two
parts that we can take in designing a
language like solidity um the current
current path which is path a um that you
can do by extending the language with
compiler hardcoded functionality which
will further increase the complexity of
the language and make it um uh more um
higher in Risk so you can move faster in
short term with feed feuture development
but the risks are much higher and the
cost as
well path B um we've been evaluating if
this can be the path moving forward
where moving we move solidity to a types
to a standard
Library this would make it safely
extensible um and the extensibility can
become a first class priority of the
language this would also make um faster
implementation of important features
easier for the
team and this will be the path forward
that we are calling experimental
solidity um time is running out so I
will zip past the design goals that we
have for experimental experimental
solidity which is simplified core
language that is extensible allows for
formal semantics as we covered earlier
no hard-coded features in the core
language because we move it to a
standard Library um and one of the main
goals would be to maintain the look and
feel and the usability of the language
as the current
language the advantages of having
something like that would be that the
core language changes are rare and any
feature development will not drastically
change the core language and maintaining
a lean core language like that would
mean that auditing and formal
verification becomes easier further
meaning that the security
improves and then it makes moving faster
by delivering Community features easier
because we invite we are then able to
invite the community in this uh to be a
part of this process um and that is
important for everyone we will also
delegate Community stewardship over the
standard library and have a formal
process for changing the standard
Library this is also what current
timeline looks like for um experimental
solidity ongoing business has been
existing uh developing existing
prototypes that are able to reconstruct
simple
contracts um in the course of 20125 we
hope to work on a more complete Baseline
standard Library um and roll out fully
functional prototypes that we can test
and get more feedback on and also sort
of have initial syntactic sugar so that
we can reinstall the look and feel and
usability of the language as the current
language um in 202 26 we want to
stabilize the all of this process and
also um formalize a process for making
changes to the standard Library by
taking proposals from the
community and moving forward from prot
prototypes to production
capacity few quick resources before I
conclude if you want to know more about
any of the things that I spoke about the
features or want to dive deep into them
we have a lot of explainers and release
announcements on our our blog there's
obviously the official docs and if you
want to have deeper language uh design
discussions then you can reach out to us
on the Forum and leave questions there
and also engage with the rest of the
community on the Forum do follow us on
Twitter to stay updated and a quick plug
to the uh newly formed and announced
Argo Collective uh and you can see the
website and the blog there that's all
from me thank you so much for being here
thanks ton
thank you thank you wish for this
amazing talk I guess everyone in the
room and watching us live has a better
overview of where Sol is heading if not
feel free to uh give us your questions
through Marat uh we'll be answering them
one by one uh I'll be starting with the
topmost one are there plans to change
the storage layout spec for gas
optimization work state released um I'll
be giving the floor for to Daniel the
team lead of solity for the question I
guess
yeah yeah I'm here to answer technical
questions that's a tough one I'm
regretting it uh so yeah uh of course we
need to do something about veral tree
State um in an Ideal World we would have
experimental solidity and could adjust
onard library implementations of storage
layouts at the time that veral trees
would uh happen but yeah I mean the
timelines may not work out for that so
we will be working on
yeah seeing what we can do earlier than
that if
necessary next up what current feature
is considered hardcoded all of
them quick one um are there plans to
change the storage layout spec for gas
oh sorry this was already
asked when
standard library and it's small call
language is
stable um when um I'll be skipping the
next one because we talked about the
next features uh how does the Sol Duty
team collaborate with the F and formal
verification team um significantly I
would say I mean f is working on uh
language Frankin that have properties
that we want for experimental solidity
formal verification has a lot of uh
knowledge and expertise about The
Logical structure of that such an
English needs to be consistent and uh
formally verifiable Fe also has uh
working has been working with
experimental backends which we can use
uh which induces knowledge that we can
potentially use for making the V
pipeline uh faster so there is a lot of
synergy between the themes nice that's
great to hear um next up when moving
stuff from core language to a standard
Library will that be detrimental for to
compile times or make run time less gas
efficient we hope neither of that will
be a large problem uh currently the high
level language is not a concern in
performance it will take more time to do
parsing and type checking on the high
level language in the future we will see
when the prototypes are finished how bad
that will become but the most time spent
by far at the moment and the most
complex thing is optimization and uh and
code generation for the evm if we don't
have UF so we hope that it won't become
a major
issue if some functions move to standard
Library do we need to include that
Library code into Soul C
Json uh I would say no I mean each
compiler version ships with a version of
the and a library that can be referred
to by an internal yeah
mechanism um next one is I think
partially answered but I'll ask again in
EF the stack to deep error doesn't exist
exist anymore do you think y still makes
sense for
EF uh it doesn't exist anymore it's
maybe an overstatement it because it's
less likely because we have I mean we
don't technically have unlimited Swap
and du space we only have 250 six bit
access which is much better than 16 bit
uh avoiding stor deep errors is not the
only reason for vir it's also making the
compilation more simpler making the
compiler infrastructure simpler making
the results of the compilation interos
spectable by Auditors by as a target for
formal verification and so on and so the
biggest bottleneck in sheet contract
development is auditing is it a priority
to make formal verification easier or
automated yes I mean yeah we've talked
about that a lot experiment solidity
hopefully will help a lot uh
intermediate representations help with
that there is only so much we can do I
mean uh verification will remain hard
yeah we'll try to do as best as we can
with our collaboration with the formal
verification team as
well uh I guess this will be the last
question will experimental solidity have
in line assembly yes uh the idea is to
treat in an assembly in experimental
solidity to a similar degree to unsafe
blocks and rust such that actually the
sard library will encapsulate uh
implementations in assembly in a safe
abstraction that will then be usable but
it can be extended by still using in
assembly and providing new suchar
abstractions if
necessary all right is Fay also working
on a new back backend let's keep it
short uh I mean that's for them to
answer really but I mean yes atina which
is an uh is an SS closer to llvm uh uh
designed uh ssab based control flow
graph representation that's similar to
what we use to translate Ule to evm in
the future so there is yeah some similar
varities there but yes all right that
concludes our Q&amp;A session if you have
more sessions feel free to catch Daniel
or wish and let's give a big round of
applause for both of
them hello yeah which design discussions
come grab some stickers or some socks
thank you wish um next up we will be
continuing with our next session in 2
minutes in the meantime feel free to
grab a drink stretch a bit and we will
be continuing with other solidity topics
here thank you
m
hello everyone uh welcome to the stage
three of Devcon in day three We are
continuing with continuing our sessions
uh about solidity I guess we are having
a small scale solidity Summit here for
the rest of the day um if you have just
joined as a reminder you can you will be
able to scan the QR code of the sessions
and we'll be able to ask your questions
for the Q&amp;A session uh but without
further ado our next talk will be on
solidity inline assembly and how it was
used in Soul Lady by vctor eyes please
give a round of applause
for hello hello thanks for coming to my
talk you have 30 minutes because this is
a bit last minute okay so I'm vectorized
um in my free time I maintained this
Library call Soul lady which is a
solidity
library of various features written
mostly in inline
assembly so today I'm going to talk
about how we use inight assembly to make
things
simpler uh for users of the
library okay so to start off some time
ago I posted this tweet saying the
beginner use assembly to save gas
because that's the most obvious thing
the intermediate use assembly to avoid
the spirus dragon limit because SMB
makes your B code much smaller like even
without eof if you probably can see that
reduction then the advanced use assembly
to save time once you are so used to
writing inight assembly you just
straight away write the optimal U code
so inight assembly and you we can use it
interchange interchangeably in this
context okay so um today I'm going to
describe a bit of two and three the
second and third
Point wait okay so some examples to
start with the first one is safe
transfer leap I'm also going to talk
about the leap in so lady so in so lady
we have this Library uh for proxies and
our proxies are mostly I would say most
if not all our proxies are like directly
written in bite
code then we also describe like some
higher level features for example lip s
and how having uh init assembly can help
testing okay so for example St transfer
de we use
this uh let's say if you want to send
ether to someone in the auction contract
but what if the sender is some smart
contract that gu grief or does not
implement the receip
function so in so lady we have this
function called Force safe transfer if
which users self-destruct to force send
the at to the person so as a user you
don't need to care about all this
Integrity you just use the function and
you can be very safe that the Ator will
be actually for send to the person and
why is this
useful uh we know that rep if is like
not on the same address on every L2 so
so if you want to deploy your contract
to the same create two address and you
use rep if it's a bit Troublesome so
instead you can just use this function
and you can save your uh brain space and
time okay in lip clone we have this
function called uh deploy erc1 1967
which deploys a minimal bright code
proxy that is
upgradeable so it's based on this uh ERC
code 7760
so uh
this proxy has been written for more
than a year but recently we want to
consolidate all this into a ERC so that
block explorers can Implement Auto
verification
easily so because this ERC has been
around like the Proxes has been around
for some time it has also gained a bit
of adoption so on base chain uh it is
the proxy of choice used for the
coinbase M wallet and for polygon I
think they are using it for something
else also so they are like over
used around and the advantage is that is
fast is small and on uh some cases it
auto verifies so it save your time you
don't need to do some at scan API key he
just verifies it by
itself so lip also have some high level
functions uh can be useful for your
testing purpose like we have set
operations on sorted arrays you can use
it for your invent
test and then for test class uh we know
that if you def write your test in
Foundry you have to Define
your the random variables in in the
function arguments and there's limited
amount of space you can do that and you
have to think of like
nice names for the variables which I
find is very time consuming so instead I
use uh like a lot of black magic to
write this underscore random method
which allows you to
use uh to Generate random stream of
numbers anywhere in your code so you can
do something like guided fast
testing and if you want to uh know how
to integrate in into your project you
can follow the link
below okay so here are some other
example libraries you might want to
check
out uh one thing I find a bit
interesting is dyamic array lead for
example in solidity if you define a
array you know you can't do like a pen
or push back but whereas this Dynamic
array de has that
function okay so why inite assembly is
good for a Library writer like
me first it provides some techniques
like it helps me do some uh fine tuning
of the code so that users of the library
don't have to worry that my library caus
them to have a stack too deep you also
can enable some cool math that is not
accessible in normal
solidity and then uh if you know how to
push the compiler in the right direction
you can achieve some zeroc cost compile
time extractions
so for example avoiding stack too deep
uh we have this function called long
what in fix Point meth Le if you use it
on its own uh sometimes uh the compiler
tries to inline it and it causes causes
a stack too deep but if we rewrite the
function in inight assembly you can
somehow rearrange how the variables are
allocated on the stack and by
rearranging the
variables you help the compounder
compile in a way that avoid stack too
deep with or without IR so in uh so lady
we are very particular that it must work
in as many situations as possible so
whether you use V or whether you choose
not to use
V we want to make sure that it just
works you don't need to worry that our
library is the culprate of a stack to
deep that's why we are very particular
with all these tiny
details okay then inight as also allows
us to make some cool math you don't need
to understand what the math is about but
there are some op codes like the bik op
code and the branchless uh op codes that
allows us to make math faster for
example in this lock two
method and the advantage of having a
fully branchless function that is inline
uh that is possible with inline assembly
is that when you when the solidity
compiler try to optimize it will first
check what the function has any branches
if it has branches then the function uh
is likely not to be in line uh with the
V Pipeline and if you use the Legacy
pipeline it will definitely not be in
line so um by writing stuff in inmb we
help the compiler produce more efficient
back code by telling the compiler that
this function is
inable so using this trick we can also
achieve some other techniques like if
you want to compare a short string with
another short string traditionally you
will use some kind of Ky cut 256 but if
know uh in assembly you can do some kind
of black magic that will tell the
compiler that instead of doing useless
memory allocations just emit the optimal
op code so all these although it looks
like a lot of op codes but in the end
after you press compile it it somehow
simplify into just a few op codes and
this is only possible if the the entire
chunk of code is
branchless okay so the thing about
solidity is that it's a very beautiful
language you can write all the low level
things and users don't have to be
concerned about the details so all the
nitty-gritty black magic has been
extracted away from the users the users
need to just care about what are the
high level apis and what are the
tradeoff of all the different functions
so you can write clean and performance
readable high level solidity without
actually going deep into the inight
assemply rabbit
hole okay so
some cor goals like norstar Sol lady we
want to make sure uh that Sol is the
best smart contract Language by
providing a res set of Highly optimized
utilities that fits the solidity
compiler now and into the
future then uh okay so the idea is that
people say uh we want to write our
language in Ras because it has a
wider uh Library we want to write in C+
because there's a v library but in
solidity we have this uh exotic M
function called Lambert w01 which is
only available in Python maybe some math
language and solidity you can find it in
any other like major
languages so that is so ladies go if
it's touring complete if it's possible
within the touring completeness of evm
we will implement
it we also want to scale e ethereum to
show app layer
optimizations and also make the code
beautiful so quite a chore but I see the
importance of it in because eof code is
actually uh more optimal for stuff like
sp1
proving So eventually I think quite soon
so lady will have a
eof it won't be a breaking change so we
have a source directory and then we'll
have a EF directory so we can use either
one we won't like force you to use
either eof or the Legacy we'll give you
option okay so here are some links uh
you can visit so.org which is a shortcut
to show so lady or you can uh visit my
GitHub or my ex sometime I post like
small solid lessons on my
ex okay I think that's all for my
talk thank you thank you Rector eyes for
this talk I guess we have all now a
better idea of how to leverage assembly
inline assembly in our code um in the
meantime we have plenty of time for
questions so if you have any make sure
to please send them through this QR code
um I'll be the first one on the
leaderboard um did assembly ever bite
you in the butt where vanilla solitud
would have been more
safe okay um when I was starting up like
maybe two years ago I think the fix the
safe transfer leap forgot to clean some
upper bits because it was uh I directly
ped it from so but then uh someone
spotted that but so these days like I am
super paranoid paranoid about unclean
dirty upper bits so it becomes like a
second second nature so I think recently
it should be quite
safe all right next one when to use let
and when to use M
store okay let is a way of defining
variables in inl assembly
uh if like let's
say uh somehow you can't force the comp
po to reorganize a stack to avoid stack
too deep then you might have to use M
store to use the scratch space for
temporary variables but you Atmos can
only use two uh parts of the scratch
space like two slots because the other
slots are for for other purpose for
important
stuff um next one why do you prefer
solid inline assembly over other
lowlevel languages like h
okay so the thing about I I like half
but uh the benefit of solidity is that
it allows you to recycle your efforts
and also it allows you to generate more
compact bike code for example in half
the inline is really in line but where's
in solity if you have like 10 use if
your function is a giant chunk of bik
code and it's used like in 30 different
places you might not actually want to
inline it every single time
next one uh at l2's Cold data with call
data feedback function I guess from
libzip has greater gas versus
non-compressed Co data but has slightly
cheaper gas at L1 is that correct what
happens under the
hood okay um this depends on your out of
compressed core data to the users so if
you use CD forb back on optimism you
might not you will most probably not be
able to save any core data money if
you're Depo on op St just don't use
that when using assembly based libraries
is there a higher like assembly based
libraries is there a higher likelihood
that it is less compatible with future
solid versions I would say that is
actually less likelihood because for
example if you look at transient storage
solidly implement it on the asembly
level first then later it become like a
higher level thing so one thing you have
to worry about is that
um solidity might change in ways that
the high high level Parts interpret the
memory slightly differently so uh that
you have to keep up with the change
lock voriz also has a nice friend a nice
hat and a panda on his hat do you want
to show
everyone yeah I guess that helps you as
well en
coding um next one I guess uh how SOL
SOL these features saturated how many
more libraries and functions do you plan
add okay I think right now we have
mostly saturated uh we have a lot of
work to do to port to eof like is
especially the liap Clone is is going to
be but the solidity team has actually
much much a much
more stuff to do compared to
me another one About Soul ad will the
new solid compiler in R impact solidity
solid I think this new solid compiler
called solar they try to become like a
feature parity with uh the official
solidity compounder like for example in
C+ bu you have uh Clen you have GCC I
think we might go that route down the
road and if you just writing in a high
level language you don't need to care
whether you use Round of Applause for
Vector eyes
uh our next session will be in 10
minutes or stay here uh and see you all
in 10 minutes
hello everyone and welcome to the final
session of stage three from day three
from Devcon Bangkok um in this session
we will be hearing from Rob uh about
remix and what's coming up in remix uh
and I ask Rob what is a fun fact about
you and he says he likes with a black
bean sauce and a lot of chili you can
eat it we talk a lot of food stuff with
Rob but without further Ado do it's my
great pleasure to invite Rob to the
stage let's give a round of
applause yay
y uh okay I will begin with I might need
to because it's the last
session I think I might want to eat some
wasabi
peas oh look
amazing
ah
okay little spiciness will uh get this
going good
it ain't your grandma's
remix so we're going to go over a bunch
stuff I don't remember what it is
but I think the sessions will uh I mean
the slides will let me
know
so has anyone not used the plug-in
manager here wait not used wait has does
everyone has everyone tried remix here
anyone who hasn't
ah so and anyone not use a plug-in
manager wow that's interesting you just
go like use what's what's
default good
um so anyone use it regularly
remix I love you
guys so here's some of the little
updates because this talk is basically
what's the new
stuff so
um I just get to it
um has everyone seen the uh language
switcher it's been there actually for
maybe a few years or maybe a year
anyway we can make this uh as many
languages as we want we just need more
translators like it would be great to
have remix In tha and um I think I
should start organizing that so uh
anyway and once you switch
that oh another thing we added this year
was the right hand panel so when you
click that then when you uh click it it
bounces over to the other side of the
screen so we have this new right hand
panel which is super cool because like
we can have some instructions there wait
has everyone tried learni before know
what it is anyone not know what it
is it's a tutorial plugin so you have to
go to the plug-in manager or uh on the
Home tab there's often a promo for it so
you click that and it will load it up
and um well I'll go over that a little
bit later but you should try it because
it's um tutorials you can learn solidity
remix uh there's a lot of some bunch of
other ones that are very very
interesting and I wrote some of them uh
um anyway uh oh yeah so when you change
the language it'll change the language
inside of learne to which isn't so
surprising
but it's good to be able to do it I mean
if if it doesn't do it it's because we
haven't had the languages translated
which means uh we're going to get the
languages
translated oh so here's the uh learni
some the current selection or most of
them uh and then when you load them up
they there's some um solidity test so
you can it'll give you some tasks and
then you can um you know play with it
and then it'll check if your code is
right or not you can see some answers
and uh it's a good guide as well and
then you can you guys who are teachers
out there anyone teaching with
you can make your own learner tutorials
on your own repo and they'd be ready
immediately or you can then make a PR
and have them ready in remix uh as soon
as I look at them and decide they're
wonderful uh so now a lot there's a
bunch of AI updates and
remix so there's code
explanations code assistance did I
remember that yeah on request and code
completion while you type
and uh here we go oh yeah so the the C
uh explanations are initiated from the
robot icon the compiler errors and
clicking on some code a uh what you call
it contract
there the new uh AI assistant panel pops
up and it tells you what's going on in
contract and uh compiler errors like you
make an error and then you click that
button and then again it'll open up in
the AI
assistant and if you right click some
code you get this popup um menu on the
code and then what's going
on um for example inside a contract with
a triple slash you can ask it like write
a function that you know takes a
modifier and uh increments something and
what I don't know whatever so but anyway
you just it'll write it or at least
hopefully will write write it hopefully
it will write it well in fact uh when it
returns something it goes through um
Slither so it'll it should return
something safe but also if you don't
like it just ask it again and it'll give
you a different
answer so trying to figure out like how
well that will work for learning
solidity because
sometimes maybe it's going to take you
down the wrong pathway but it will give
you some code to try to understand
anyway which maybe is part of the
challenge of becoming a good
coder uh and then code assistance while
you type um you have to have the
switcher on on the top of the uh main
panel and then when you type something
uh they'll get a line will complete it's
only one line at a time but it will
complete it'll offer you some
suggestions about what should be on
there of course maybe that's annoying so
you just turn the thing off and you
don't get those
suggestions uh oh yeah so I put this
slide up is this is not new it's just
that I want everyone to make sure that
they're saving their work in a good way
because browser storage is not really a
good way you could lose your work and
that's you know frustrating so uh has
everyone at least know what remix D
is no one does except for
Sol it's a way to connect remix with uh
your file system so you have this little
uh script running called remix D and uh
it'll connect you specify the folder on
your computer so you get the script
running on your computer and then you
can uh just save work directly onto a
folder on your computer but you could
also use git and I'm reason I'm bringing
up git is because there's this new uh
git plugin and remix it's by default
active so you can do git login and clone
and
basically uh a lot of stuff so you can
log in and remix and then uh once you
log in you'll see the git icon in the
file explorer but it's going to do like
basic git operations you know Source
control commits
uh click click click pushes and pulls
and when when you first initi initialize
a repo the file in the file explorer the
codal is going to be the files are all
going to be green and then when you add
them and make the commit then they're
going to turn back to gray again um and
you can do uh diffs here uh so you click
on the on the commit and then you can
see how it's
different uh yeah I'm G to go on to the
next one oh yeah and the file explorer
you can see uh the which branch you're
on and also in the um New status bar at
the bottom of remix it'll tell you what
branch you're on and you can switch
branches in here when it when it pops up
but it well anyway that's a way to
initialize it too from the status
bar also if I'm talking too quick l or
if you uh want to ask a well no
questions will be at the end anyway you
could uh tell me to slow down or speed
up but there's no cherry picking and now
we've have this new panel for uh videos
so when you click that you get this big
remix guide and the cool thing is I I
have got uh uh smart contract programmer
videos here he's really great and he did
the great low-level videos so if you're
wondering like how to play with um some
low-level storage in uh solidity you can
go through his videos and soon it's
going to be those are going to be on the
right side the video with a place to
down to load his code into remix so that
you can be watching the video and coding
that's a upcoming thing and that's going
to be a great learning
tool um so that's where it plays right
now in the
middle uh and now we got this new
template uh Explorer so when you want to
make a new um template you click that
instead of this the old model it opens
here so there's a lot of space and we
have lots and lots of
templates and uh it has scripts in there
too so it's not just scripts it's not
just uh solidity files it's scripts and
then you can add them to the current
template that you're on so you don't
necessarily have to make a new workspace
CU a template is usually its own
workspace but in this case you can add
it to a current
workspace and we've done a bunch of
updates in deploy and
run um oh well first uh there's a
cookbook plugin which is kind of cool
for loading up some smart
contracts and there's some AI features
in that
plugin uh so I don't know if you all
know but there's that little plug icon
there actually has been around quite a
while it'll open chain list.org and if
you select the chain then when you it'll
configure your browser wallet to use
that chain so you don't have to go
hunting around for the specs of your the
chain you want to deploy
to and and we added pinning like as
anyone forgot what address they've
deployed the contract to even now like
it'll uh save for the virtual machine so
when you click that um it will save it
but also it will appear and on the same
workspace as what you originally were
deploying
from and uh yeah it's kind of saying the
same
thing uh and that's saying the same
thing and now we have this little
message signing I mean we that was
actually another one that's been around
a long time we just added the uh
functionality for EIP 721 I mean
uh yeah and so also now the share the
the state of the VM is stored in the
file Explorer so that means if you push
your your repo to GitHub and your
collaborator is working they can pull
down the state of the local blockchain
and uh so it should be good for
collaborations but also because it's
saving it when you refresh remix it's
you're not going to lose your work as
well and we have custom Forks so you can
go to uh whatever Fork of whatever chain
you want
to and sometimes s like this used to be
a really big
list but um then it got too long so in
remix there's a lot of like UI how to
was here oh yeah last this is um build
bear like it's a cool plugin and it'll
allow you to have a um private chain
where you can use your browser wallet to
that chain so it gives you keys and uh
it's kind of like it's a nice extension
to the private networks inside remix
and now one of my favorite
projects the uh contract verification
tool where you can
verify four services at
once and it's super cool because uh it
does that and it's
got a bunch of tabs one of the tabs is
you have to for chain for uh services
like uh ether scan you got to put in
your API key but for services like
sourcify you don't and it just works
and we also have this thing called quick
dap you ever like wanted to generate a
front end super
quickly it's good for hackathons this
only works on public networks so you got
to be on a public network then you open
up the deployed instance and you see
that funny little icon there if you
click
that then in the main panel you get
quick dap so you could have a logo you
can title your Dap You Can you have a
bunch of uh function shows all your
functions look at that when you open up
the daap there'll be a link to open up
remix with the uh verified contract
inside of it um but uh so you can order
your functions get rid of functions
explain your functions and then you can
quickly uh get a
URL that will uh here I'm going to go
here's a a simple dap so it's like great
you could just pass your dap around and
get some feedback
quick uh we also have remix desktop now
so it's a package of electron version of
remix but it gives you access to the
terminal and you can also work online by
downloading the solidity compilers uh
before you go
offline so each version each instance of
remix desktop is its own um each sorry
each workspace is it own instance of
remix
desktop and uh in this
case uh this is the file explorer uh and
it will bring up the previous
um uh workspace that you had open then
workspace is going to be a folder on
your hard
drive so it gives you access to the
terminal it gives you access to the
output typical remix output
panel as I said you can work offline see
that's
online first you got to download the
compilers now go offline go on your
airplane and uh get to
work uh so you can
yeah so you don't have to worry about
browser storage
anymore so here's remix like a bunch of
folders of remix open so it's a kind of
a
mess because you're having a just like
my computer screen is a Mash of
different windows open in this case it's
a mass of different folders each one
with a different uh instance of remix
desktop then you can also not use remix
remix for coding use vs code for coding
but used to use uh remix for uh the dev
the web 3 uh
tools know browser wallet you can use
hard hat and Foundry just like we can
this is all like normal stuff so this
has all been
there this is all just normal like using
hard hat and Foundry and
remix Has anyone used heart heighten
Foundry and
remix uh then you can deploy you can you
wow it's not for me I
think uh so we can now run soon be able
to run uh ZK projectorg
Hiers we've got a
Viper
compiler uh we've got arbitrum stylus
anyone want to play with that try it
out and we've got circom in
remix has anyone wanted to try running
some
circuits I mean they are a bit
complicated but I think remix is a grent
to start
playing so you can get them from the uh
workspace templates so you can load up
some and start playing around with them
too large and you want to uh do the your
proofs you can run them uh remotely via
syry there but to start playing with the
um proofs there's the uh circom compiler
uh icon
and here's a and it's step by step so
you're using the guey you're using
circom you click compile then you get
the next step which is doing the setup
and you can you should choose the right
number of uh what's it right number of
constraints so you get to learn the
terminology you get to run to the next
step which is uh running the setup you
get to see what the output in the
terminal you get to compute your
witness and then files are generated in
the file
explorer so you can see the uh witness
file in this case
simple and then you generate the proof
also it'll generate the solidity file so
you can get the proving done and then
you can deploy that somewhere and then
make you know use that to uh verify that
your proofs are the right
thing see that's the proof is valid
uh oh 7 seconds left so go play with
circum code and then of course you can
uh get a little bit more advanced in the
advanced configurations set your prime
number uh I think that's kind of about
it or you can add a syry
script and then now if anyone wants this
plugin over here that's always on and
then you can select ether 6 otherwise
select the uh default version for our
script Runner so you can run all these
other
scripts and it's coming soon account
abstraction hash generators more learn
tutorials and more
videos
ah I could have been looking down here
the whole
time thank you thank you rob for this
amazing talk uh we we have a couple of
questions to rob in the meantime if you
have any other questions quickly you can
just send them to us the first one does
the autoc code complete go through sler
well uh I don't think
so Stefan Stefan here no I don't I don't
believe it
does our um AI
genius has not deemed me high enough to
come to the talk today I guess that's
what being meant here yeah yeah
definitely yeah so if you're verified on
any of the verifiers like sourcify ether
SC BL Scout you can just enter the
contract address and get all the files
right correct
yes do you think gamix team could be
connected to other language ecosystems
that use different RPC VM and
language well we could be connected to
yeah I mean we were connecting to
different languages already yes you
already do right yeah I mean Viper and
stylus
and uh and it's possible for non evm
course more work to
configure paus welcome yeah um some say
five years more then 80% new code will
be AI generated what do you think about
making remix the AI first
tool already doing it yeah we are we're
already working on it and it's one of
goals especially in this era of hype we
have to have it but also it might be
like it might be a good learning
tool is U UPS smart contract easily
Deployable with remix IDE
definitely there's an interface when
you're uh in the I guess run and deploy
and you just uh click that it's a proxy
contract and it opens up this separate
interface and it deploys the the uh uh
one I mean the uh
implementation and the final one is it
possible to use a browser wallet with
remix desktop no remix desktop is not in
the browser
although there might be some workarounds
and maybe even a we're going to try to
get this going with a uh desktop
wallet what's the name of the mascot
that's the trivia question does anyone
know I love you it's
Remy so that was the last question thank
you very much Rob thank you big round of
applause for Rob
you want to whatab P thank you I need
because I'm hungry and this concludes
our day three in dcon stage three thanks
everyone for attending and see you
tomorrow in different talks
