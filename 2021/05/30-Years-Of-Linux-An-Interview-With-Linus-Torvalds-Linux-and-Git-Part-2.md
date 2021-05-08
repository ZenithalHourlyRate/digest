# 30 Years Of Linux An Interview With Linus Torvalds: Open Source And Beyond - Part 2

The Linux kernel is celebrating its thirtieth anniversary this year. In part two of our interview, we conclude our conversation with Linux creator Linus Torvalds. If you haven't already, check out part one to learn all about Linux kernel development and the creation of the Git version control system.

In this second part, Linus offers insight and perspective gained from managing a large open source project for three decades. He also talks about his employment at the Linux Foundation, and describes what he does with his spare time when he's not focused on kernel development.

As to what makes an open source project successful, Linus admits, "I don't really know what the key to success is. Yes, Linux has been very successful, and clearly Git too started on the right foot, but it's always very hard to really attribute that to some deeper cause. Maybe I've just been lucky?" He goes on to offer three practical recommendations he's followed himself: be there for other developers, be open, and be honest.

When he first started the project, Linus wrote every line of code. "I still remember the very early days, when people would send me patches, and I'd not actually apply them as patches, but I'd read them, figure out what people wanted to do, and then do that myself. Because that was how I had started the project, and that was how I felt more comfortable, and that way I knew the code better." He explained that it was important to learn to delegate, "I stopped doing it fairly quickly, because I'm just fundamentally lazy. I got really good at reading patches and understanding what they did, and then I'd just apply them."

Linus has also worked to stay impartial as Linux has grown and become more successful, "I very consciously didn't want to work for a Linux company, for example. I maintained Linux for the first decade without it being my job. That's not because I think commercial interests are wrong, but because I wanted to make sure that people saw me as a neutral party, and never felt like I was 'the competition'."

On the question of whether or not open source is sustainable, Linus replied, "Yes. I'm personally 100% convinced that not only is open source sustainable, but for complex technical issues you really need open source simply because the problem space ends up being too complex to manage inside one single company. Even a big and competent tech company."

Finally, as for how long he'll continue working on Linux, Linus said, "I do enjoy what I do, and as long as I feel I'm actually helping the project, I'll be around." Read on for the full interview.

## Managing Open Source Projects

**JA: We recently spoke with Drupal creator Dries Buytaert, and he credited you with much inspiration and the occasional mentorship and advice over the past twenty years that he's been maintaining the popular Drupal CMS. Do you frequently communicate with maintainers of other open source projects, either offering mentorship or just sharing notes? How often do other open source maintainers reach out to you looking for advice or help?**

LT: I don't know about others, but no, I don't personally tend to interact all that much with other open source projects, simply because I tend to be a pretty "one-track mind" person. I think that's why I still do kernel maintenance three decades later: some people flit from project to project, while others (like me), end up being fairly focused on one thing for longer time periods.

That said, there is often a fair amount of overlap in developers, with lots of developers working on more than one open source project. And different projects obviously affect each other, with all the common infrastructure. So you do have that kind of cross-pollination, and you end up having people meet at the same conferences (back when those happened) etc.

**JA: As the maintainer of an open source project, what are some of the key lessons you have learned that would help others manage their projects more successfully?**

LT: This is a hard one to answer, because I don't really know what the key to success is. Yes, Linux has been very successful, and clearly Git too started on the right foot, but it's always very hard to really attribute that to some deeper cause. Maybe I've just been lucky?

Because luck and timing, and being in "the right place at the right time" really is important. I think for both Linux and Git, the projects I started ended up being projects that a lot of people needed, even if they didn't necessarily even know they needed them. Was that just luck? Maybe. Or was it that of all that mass of people who needed those projects, I was the one who uniquely stepped up and did the work, and got the ball rolling?

My ego prefers the latter, but honesty forces me to say that you really do want luck too, and you do need to pick the right project. The one that people really need.

But if we ignore those kinds of "big questions", I do have a few practical and down-to-earth things that I personally think are important if you are an open source maintainer.

The big one is that you have to be there. You have to stay around, you have to be there for other developers, and you have to be there ALL THE TIME. You will hit technical problems, and it will be frustrating. You'll work with people who may have very different ideas of how to solve those technical problems. And the technical problems are in some ways the easy part, because they usually do have technical solutions, and you can often fairly objectively say "this is better/faster/simpler/whatever".

The harder part can be that you'll end up interacting with people who you don't like, or with people who don't like you, and there will be personality conflicts. Then you can't fall back on "show me the numbers" - people just don't always get along, and it's not a numbers game. You'll have bad days, and the people you work with will have bad days. And you'll have to work through it all.

That's not to say that you can't take a break. I do that all the time. If I get frustrated, I just leave the computer, and I will go read a book or something. Trying to force some productive work (or discussion) when you're frustrated and angry is not great. And I clearly have not always done great on this, and I've pissed people off and used too strong language. I think I'm doing better on that, but one way I'm doing better on that is by literally walking away more - trying to actively notice "I'm in a bad mood" and just stepping away from the computer.

So you don't have to be there "all the time" in the sense that it has to be constant. Taking the day off is fine. Taking a week off might mean that you need to let people know. Taking a month off? At that point you really have to have a maintenance plan, and in three decades that has happened exactly twice: once when kernel.org got broken into and people spent a lot of time making sure that everything was ok, and the second time when I took a break to try to make sure I had my behavior under control.

What I'm trying to say is that maintaining a big project is a fair amount of work, and it's something you need to keep on doing for a long time. It's not all fun. It's interesting. It's challenging in the best ways. I have not been bored being a kernel maintainer. But it's not all roses either. Not everybody wants to do that kind of thing.

The other big thing is that you have to be open. And I mean that in multiple ways. It's really easy to create some kind of "clique" of people, where you have an inner cabal that discusses things in private, and then you see really only the end result (or the fringe work) in the open, because all the important stuff happened inside a company or within a core group of people, and outsiders have a hard time breaking into that clique, and often have a hard time even seeing what is going on in that core group because it was so private and exclusive.

It's one of the reasons I really like open mailing lists. Not some "by invitation" list. Not something you even have to sign up to participate in. Really open. And pretty much all the development discussions should be there.

But "open" is important in another way too - be open to other people's solutions, and don't have this very clear and inflexible idea of how things should be done. I think one of the reasons Linux succeeded was exactly the fact that I actually did NOT have a big plan, and did not have high expectations of where things would go, and so when people started sending me patches, or sending me requests for features, to me that was all great, and I had no preconceived notion of what Linux should be. End result: all those individuals (and later big companies) that wanted to participate in Linux kernel development had a fairly easy time to do so, because I was quite open to Linux doing things that I personally had had no real interest in originally.

And finally, I think "open" is important in the sense of honesty. You don't want to play politics behind peoples back. Be open about your motivations, be open about why you do things and what you do. You don't have to like everybody you work with, and they don't have to like you, but if people are open about what they are aiming for and what they do, you don't necessarily have to always be best buddies - the most important thing is that you can trust each other.

Because trust matters. A lot.

**JA: Beyond what you’ve already mentioned regarding less coding, and more communication and leading, were there specific skills you needed to learn that you found difficult? For example, delegating, being a better writer, and other non-coding skills — and if so, how did you learn to do this? Was it hands on, from books, or from other people? Is this something taught in school?**

LT: So I'll just start off by saying that almost all of the process for me has been very much incremental and a learning experience. Three decades is a long time, and very few changes have been very sudden, and most of how we do things have grown in a very "organic" way.

In other words, it's very much not a result of planning ahead and reading management text-books etc. It has very much mostly happened on its own, and any structure we have now is not from some written-down org-chart, but from people simply "finding their places".

One skill that clearly some people find difficult is "letting go of control". I still remember the very early days, when people would send me patches, and I'd not actually apply them as patches, but I'd read them, figure out what people wanted to do, and then do that myself. Because that was how I had started the project, and that was how I felt more comfortable, and that way I knew the code better.

It turns out that for me, this was not a big deal in the end. I stopped doing it fairly quickly, because I'm just fundamentally lazy. I got really good at reading patches and understanding what they did, and then I'd just apply them. So my control freak days were fairly quickly over. I think I've been pretty good at finding people to trust, and then doing just that - trusting them and not micro-managing them overly much.

So delegating hasn't been a huge problem, but I know it has for other projects. Again, part of it is that whole thing where our maintainership model doesn't require some kind of absolute trust up-front, which really does make everything much easier.

Communication skills very much are important. I actually come from a family of journalists (both my parents were journalists, my uncle was one, my paternal grandfather was a poet and a journalist), so I grew up in a household where reading and writing was pretty much taken for granted from a very young age. And while English is my third language, it was a pretty strong language for me already by the time I started Linux, and communication wasn't a huge problem. But I realize that it very much can be a big issue, both for personal (perhaps personality) reasons and for language barrier reasons.

But in general, mostly I did learn by doing. Again, remember - none of Linux happened overnight. The project it was thirty years ago is very different from the project it is today.

**JA: While open source has been hugely successful, many of the biggest users, for example corporations, do nothing or little to support or contribute back to the very open source projects they rely on. Even developers of surprisingly large and successful projects (if measured by number of users) can be lucky to earn enough to buy coffee for the week. Do you think this is something that can be solved? Is the open source model sustainable?**

LT: I really don't have an answer to this, and for some reason the kernel has always avoided the problem. Yes, there are companies that are pure "users" of Linux, but they still end up wanting support, so they then rely on contractors or Linux distributions, and those obviously then end up as one of the big sources of kernel developer jobs.

And a fair number of big tech companies that use the kernel end up actively participating in the development process. Sometimes they end up doing a lot of internal work and not being great at feeding things back upstream (I won't name names, and some of them really are trying to do better), but it's actually very encouraging how many big companies are very openly involved with upstream kernel development, and are major parts of the community.

So for some reason, the kernel development community has been pretty successful about integrating with all the commercial interests. Of course, some of that has been very much conscious: Linux has very much always been open to commercial users, and I very consciously avoided the whole anti-corporate mindset that you can most definitely find in some of the "Free Software" groups. I think the GPLv2 is a great license, but at the same time I've been very much against some of the more extreme forms of "Free Software", and I - and Linux - was very much part of the whole rebranding to use "Open Source".

Because frankly, some of the almost religious overtones of rms and the FSF were just nutty, and a certain portion of the community was actively driving commercial use away.

And I say that as somebody who has always been wary of being too tainted by commercial interests. I very consciously didn't want to work for a Linux company, for example. I maintained Linux for the first decade without it being my job. That's not because I think commercial interests are wrong, but because I wanted to make sure that people saw me as a neutral party, and never felt like I was "the competition".

But I do think that some projects may have shot themselves in the foot by being a bit too anti-commercial, and made it really hard for companies to participate.

And no, it's not always easy working with companies. We have several kernel maintainers that have been very active in trying to help teach companies how to work with open source: it's one of the things the Linux Foundation does (not just on the technical side: there's teaching about the legal issues etc), and apart from being one of the main kernel maintainers, Greg KH is very active on that front. So it does take some effort.

But is it sustainable? Yes. I'm personally 100% convinced that not only is open source sustainable, but for complex technical issues you really need open source simply because the problem space ends up being too complex to manage inside one single company. Even a big and competent tech company.

But it does require a certain openness on both sides. Not all companies will be good partners, and some developers don't necessarily want to work with big companies.

**JA: A common theme we've found in talking to long-term open source maintainers is burn out, in part due to the constant pressures of maintaining projects so publicly, and constant demands from users as if you owe them something. Have you experienced this? How do you deal with this, and avoid burnout? Have you ever considered walking away from kernel development?**

LT: Well, I kind of alluded to this issue earlier in your "key lessons" question.

Because yes, it's a pressure. And yes, I've been fed up too at times.

At the same time, at least for me personally, my bouts of "Ok, that's enough" have generally been very much "That's enough for TODAY". I get stressed out, I get annoyed. I've obviously exploded at people at times, and it's not pretty when it happens (and I really have been actively trying to make sure it doesn't happen again). And you obviously don't see the cases where I just walk away pissed off about something or somebody.

But.

I go off, read a book, maybe drive around a bit if it's nice outside, take a break. And I get over it. And I'm back the next day, because in the end, I really enjoy what I do. I'd be bored to tears without kernel development.

So even when I take a vacation (I try to go scuba diving a couple of times a year, although the pandemic obviously means that that hasn't happened the last year), I take a laptop with me so that I can keep up. I let people know that I'm not as available as usual, but particularly when I can time it to the end of the development window, it's usually not a big deal. I'm very seldom entirely off the grid, although that has happened a couple of times too (again - scuba diving sometimes means "exotic location without internet" even these days), so I've been entirely incommunicado for a week due to that a couple of times.

And I do love being on a liveaboard, doing five dives a day for a week, and literally not even able to read email. I've managed that three times in the last five years, I think. It's lovely.

But then I get back, and I'm really happy to be back too.

**JA: 30 years is a long time, and while I understand it's impossible to predict the future, I'd still like to ask: Where do you see Linux in another 30 years? And what do you envision as your roll at that time?**

LT: So this is a question that I can't answer, and it's not because I'm trying to weasel out of it, but simply because it's not how I work, and not how I think about the project.

I don't have a "30-year plan". I don't even have a 5-year plan. In fact, I don't plan ahead more than a release or two (which is obviously just a few months).

As an engineer, I have this strongly held opinion that "details matter". Details are almost the only thing that matters. If you get the details right, the rest will follow.

That may sound a bit odd, considering that I did already talk about "good taste", and I'm certainly very much on the record as saying that the unix philosophy ("everything is a file" being one of the core pillars) is the right one.

And in Git, I very much wanted to have some overall "design" too, and there's very much a couple of overarching big concepts in Git too ("everything is an immutable object" is perhaps the Git equivalent of the Unix one).

But those kinds of "high level design" things are great mainly to give you a kind of cohesive end result, and give the community a kind of "design compass". They aren't really the most important thing in the end. Reality is complex and often ugly, and the high-level big design cannot stand in the way of details, and all the special cases that you actually need in reality.

So I just like to say that I'm a "plodding engineer". I look at what's going on right now, I look at the problems we have now, and I don't really plan for the future outside of just knowing that "I have to maintain the end result", so I do want to make sure that the work we do today won't be a huge problem tomorrow.

That kind of answers the last part of your question: I do see myself as being around. Not for another 30 years, but I do enjoy what I do, and as long as I feel I'm actually helping the project, I'll be around.

**JA: Do you have any advice for open-source developers that are looking to raise money to support their open source development efforts?**

LT: This is the first question that I really don't have any answer to at all.

I started out thinking of Linux purely as a hobby for the longest time, and never thought it would actually be my job. My first industry job (outside of academia, where the first few years happened) was non-Linux-related, and I made my contract explicitly say that my Linux work was not company work (Transmeta did use Linux, but that wasn't really my job, even if I ended up also working on some Linux issues that Transmeta had internally - mainly early SMP problems).

In fact, to me Linux was so much non-work that I was planning to take an unpaid year off from Transmeta to get the Linux 2.6 release out (ok, to be honest, now I'm unsure what the exact version was, it's a long time ago. I think it was when there was some stress during the 2.5.x days, and I felt I needed to concentrate full-time to get to 2.6). That's when OSDL came in ("Open Source Development Labs" - later to become Linux Foundation), so that I could actually get paid to do Linux without working for a commercial Linux company.

So for me, the first decade of Linux I never felt like raising money was an issue - I did it on the side. And ten years into it, when I felt I had to work on it more full-time, it had become big enough that it "just happened".

But I realize this is really really unusual, and I simply do not have an answer to your question in general.

Unless the answer is then exactly "plan on it being a hobby for a decade, and if it grows so big that it cannot be a hobby any more, you've likely already solved the funding problem".

NOTE! This is the point where I would like to just say how lucky I was to grow up in Finland. With an education system that is completely free, and one of the best in the world, I simply came from a background where it was entirely sensible to treat Linux as a hobby, and just know that I can make money as a commercial software developer. I came out of 8 years of world-class university studies with something like $7k of student debt - not exactly worth worrying about in the world of high tech.

I very much realize that a lot of people in the US don't really understand the kind of freedom that gives you in life. You really can choose to just do what you love to do, because you can afford to.

## The Linux Foundation
**JA: How involved were you in the creation of the Linux Foundation? What is your role? Has the Foundation impacted the kernel beyond allowing you to get paid without working for a commercial Linux company?**

LT: I have had nothing at all to do with creating OSDL (and then the Linux Foundation). I'm literally just an employee, although a high-profile one with the title of "fellow".

OSDL started out as a non-profit industry consortium for companies to do things together - particularly collaborate on enterprise capabilities - and with an original emphasis on having a machine farm that was available to developers (eg the kind of hardware that developers wouldn't have otherwise had access to). This all started before I was employed by them, and entirely independently of that.

It then became the Linux Foundation when OSDL merged with another non-profit industry consortium: the Free Standards Group. The hardware lab side part fell to the wayside, and the "industry collaboration" part became the main thing. Again, while I was by then employed by them, this was not something that I was personally part of: I have very consciously stayed very much focused on just the technical kernel development side.

LF does a lot of other things than just support a few key developers like me and Greg KH. In fact, it does so much that you really are better off looking up the LF web site (or the Wikipedia one). LF ends up doing a lot of infrastructure of various kinds: some technical (like kernel.org), but a lot of it other "support" - organizing conferences, having lots of working groups for industry partners, things like that.

So LF is basically support infrastructure and a lot of different projects for various things around Linux. And I'm just an employee with a fairly unusual employment contract that basically says that everything I do has to be open source, and that LF can't tell me what to do with Linux. I'm happy, and it turns out that the member companies seem to be happy too, because they all know that I'm entirely outside all of the company politics.

## Other Interests
**JA: What brought you to the US? Do you miss, and have you considered returning to Finland, or elsewhere?**

LT: So I moved to the US in '97, and part of that was that I was fairly young, and I got an offer from a startup that did very interesting things in an area that I was very familiar with (ie the somewhat odd 80386 architecture - exploring it was why Linux got started in the first place).

And Finland at the time was very much about high tech, but it was dominated by cellphone technology (Nokia is Finnish, and at the time was the biggest cellphone company in the world, and the biggest company in Finland by quite a big margin).

I wasn't interested in phones (this was before they grew up and became small computers - people actually used those things to talk to each other, if you can believe it). And the US seemed interesting, and I moved here with my wife and our (at the time) 10-week old daughter.

Moving to another country when you just had your first child, and you have no other family around to support you may not be the smartest thing to do. But hey, we were young, we took a "let's try it" approach to things, and it all worked out. I still remember how we moved in February, and it was cold (about -20°C, so about 0 F) in Helsinki when we left, and we walked off the plane and it was sunny and a nice balmy 70°F when we arrived at SFO.

It's been interesting. The US is home these days, and yes, I miss some parts of Finland. The US education system is a disaster. You have to move to the right area to get a good grade school or highschool, and you have to pay insane amounts of money for a good college. It's a disgrace. So is the healthcare system. And the political climate in the US has gone from "slightly strange" to downright scary. In Finland? Things mostly JustWork(tm).

But hey, there are advantages too, and it's not just the weather (yes, we then moved up to Portland, OR, and the weather here isn't as nice as it is in the Bay Area, but trust me - the weather is still a lot better than Finland). And we've been here so long that our kids don't speak Finnish (both me and my wife are from the Swedish-speaking minority group in Finland, so we speak Swedish at home), and we have friends and social ties here in the US. And you can largely ignore the failings of US society as long as you have a good job.

Did we consider moving back? Several times. First when the kids started school. Then when the kids started highschool. Then college. See a pattern? And then when it looked possible that Trump might get re-elected.

**JA: Much of the world was carefully watching that election, and worried about what it would mean. And even yet, knowing that some 70 million Americans supported his re-election, there’s foreboding for the future. How do you handle conversations with people who supported Trump’s re-election?**

LT: The US political system in general worries me, and the American exceptionalism and nationalism is sad and scary. Particularly when it is often by people who literally have no idea what they are talking about and have never lived outside the country.

The US is a lovely country in many ways, and it's also a very varied country with lots of different cultures and people (and nature), and I like that. In fact that would probably be the hardest part for me if I were to move back to Finland - Finland is a very nice, sane, and safe country, but it's also a very small one and very homogenous.

But the uneducated "Rah rah, America #1!" thing can be very annoying too. You see these huge trucks with American flags, and you just face-palm occasionally.

And sometimes it's even educated people. Before Trump was elected, I was talking to this perfectly nice medical doctor, who was absolutely convinced that the US health care system was the best in the world. He based this on having never lived anywhere else, and couldn't possibly admit that other countries actually have better healthcare - even when discussing it with somebody who actually has literally seen that better health care first hand. This is a highly educated person who went through many years of medical school, and still has that "America, f\*ck yeah!" mentality.

And yes, he was a Trump supporter.

Don't get me wrong - nationalism exists everywhere, including Europe. Including even Finland. But the US version of it does seem to be pretty toxic.

And honestly, it's one of the reasons I live on the West coast. Oregon is mostly very liberal, at least in any population center (Eastern Oregon is very much different, but hardly anybody actually lives there - large in area, very small in population). So the area I live in, you certainly don't see the confederate flag (or the Trump flag) very often, although you do see that occasional big truck person who drove in from elsewhere.

That said, I do think the US is changing. We've lived here almost 25 years by now, and it feels like it has changed even during just that time. Religiosity is way down, although it's obviously still very much an issue about where you live. And in many ways the US has obviously shed a lot of socially repressive policies (ie the whole legalization of gay marriage, effectively the end of the war on drugs etc). So on the whole I'm fairly optimistic, and I do think that the Trump phenomenon is possibly (hopefully) just the result of those overall positive changes. Classic reactionary conservatism.

**JA: What are your interests and hobbies outside of the Linux kernel? What do you do when you're not focused on kernel development?**

LT: I've already mentioned the main two a couple of times: I end up reading a lot (nothing serious, it tends to be random fantasy or sci-fi off my kindle), and when I get to travel I try to do scuba diving as much as possible.

And I actually have a fairly normal family life. I've got three daughters, but they are older and have mostly flown away. The youngest is still in college and will come home for summer, the middle one is doing some graduate work and won't be home for summer, and the oldest is working on the other side of the country. We still try to do family vacations (but only the middle one ever got scuba certified - I tried with all of them, but it is what it is), but last year really was not great.

So these days, it's mainly me, my wife, our two dogs, and a cat. I've gotten my first vaccine dose, and am looking forward to trying to go back to a slightly more normal life in a couple of months.

**JA: As an avid sci-fi reader always looking for new books, I'd be curious to know if there are any authors or series you've enjoyed above others? Are there any good books worth mentioning that you still think about from time to time?**

LT: Honestly, I'm a "read-it-and-forget-it" kind of person - I read mostly very forgettable random stuff, definitely not things you think about afterwards. Things like the Miles Vorkosigan series by Lois McMaster Bujold are high-brow by my standards - I think I spent a year reading the free or 99¢ kindle scsi and fantasy novels by random unknown authors with editing problems. Probably mostly fantasy, largely because it's easier to find (and I find bad scifi much more annoying than bad fantasy).

On the "not trash" side of fantasy, I think Brandon Sanderson and maybe Robin Hobb stand out. But for every Sanderson, there's probably fifty forgettable random sword-and-sorcery coming-of-age stories.

There are a couple of things I come back to, and I think I've re-read the Dune saga about once per decade. It's one of (very few) things that have stood the test of time and actually aged well. I remember loving Heinlein as a teenager, and now I just cringe at it.

So no, don't take reading cues from me. To me, reading is something I do to relax, and is never high-brow or very serious.

**JA: I found this earlier interview an interesting read, offering a lot of background into your diving. Do you still use and contribute to Subsurface, the divelog program you started?**

LT: I still use it, although for obvious reasons I haven't used it in the last year. Subsurface is a bit like 'Git' in that it's not something I wanted to write, but that I wrote because I needed it. And like Git, I found a maintainer for it, and Dirk Hohndel has been maintaining it for a long time now and taken it to be something much more than it was for me (with support for Windows, MacOS, iOS and Android, not just my original Linux support).

And without any diving, I haven't been motivated to work much on it, although I've helped fix a few reported problems over the last year.

My second vaccine dose is a couple of weeks away, and I'll go diving again in a couple of months. So that might make me fix a few more issues.

**JA: Thank you. My entire career has grown out of your “hobby”, both directly through usage of Linux, and indirectly through countless other projects that exist because of Linux and Git. I’m grateful to know that through all of this you’re still enjoying what you’re doing. I’m glad that you’re on your way to being fully vaccinated. And I’m sincerely appreciative that you’ve shared so much of your time to thoroughly and insightfully answer all of these questions! Again, thank you!**

## Original Post

<https://www.tag1consulting.com/blog/interview-linus-torvalds-open-source-and-beyond-part-2>
