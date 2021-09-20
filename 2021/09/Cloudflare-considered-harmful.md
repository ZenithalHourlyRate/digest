# Cloudflare considered harmful

Websites should avoid using Cloudflare.

Cloudflare's HTTP fronting service incorporates some seriously questionable practices. As things stand, the extent of the number of websites which have come to use Cloudflare, multiplied by its issues, poses a hazard to the state of the web.

Cloudflare as advertised to site operators fails to identify these issues, and operators may even be unaware of them.

## The CAPTCHA absurdity

If a website uses Cloudflare, most likely and by default this will result in the website being rendered stochastically defective.

A website is an HTTP request processing service. Adoption of Cloudflare results in such services becoming unreliable, and causes denial-of-service conditions to occur for users, in an essentially random and unaccountable fashion.

Where such denial-of-service conditions occur, Cloudflare provides a bizarre “one more step” page inviting the visitor to complete a reCAPTCHA to access the site. Cloudflare claims that this is based on IP reputation, which constitutes a fallacious equivocation of IPs and users which has been found to be highly detrimental to Tor users in terms of the browseability of the web.

This doesn't even work if the user has cookies disabled, or if the user uses a browser which doesn't support iframes, such as lynx.

The HTTP status code for this page is 403 Forbidden. Essentially, Cloudflare by design randomly perpretrates denial of service attacks on users, yet at the same time Cloudflare paradoxically advertises itself as a service to mitigate DoS attacks.

Cloudflare claims that that these measures are necessary to counter abuse. This claim is dubious because it is a model of operation for a CDN which appears to have few if any imitators. In other words, other CDNs do not appear to have any issue implementing HTTP properly while providing anti-DDoS measures, without resorting to such practices as random demands that users complete CAPTCHAs.

Cloudflare's randomly occurring demand that users complete CAPTCHAs discriminates against users which are not humans, by design. This constitutes a hazard to the crawlability of the web. It is unclear what recourse is available to organizations spidering the web which find themselves impaired by Cloudflare's actions. Even if Cloudflare were to whitelist these organizations, this essentially makes Cloudflare an authority on the legitimacy of a search engine; which, given the magnitude of Cloudflare's user base, is deeply concerning.

There is no basis in the HTTP standard to demand that users or their user agents complete CAPTCHAs in order to load a page, and the CAPTCHA demands issued by Cloudflare are not communicated in any standard way. The '403 Forbidden' status code used for these pages could express arbitrary policy prohibitions, such as non-negotiable denial of access. Cloudflare demands not only a human user (but not consistently; only if it randomly decides to do so), but also does not unambiguously communicate where this is the case in a machine-readable manner, which is discriminatory to robots, many of which are legitimate.

Rather absurdly, if you want to provide an API over Cloudflare you have to exempt your API endpoints so that this doesn't happen, which raises the question of what the point is in the first place if you have to make holes in it, and basically proves the point.

Cloudflare's inexplicable inability to implement HTTP in a sane, transparent manner, despite this incapability being seemingly unshared by every other CDN service in existence, became even more ridiculous when Cloudflare reached out to the Tor project to request that they make changes to Tor to accommodate their own problematic practices.

In its liason with Tor, Cloudflare states that its reasoning for its CAPTCHAs is not DDoS mitigation, but the following:

They want to mitigate comment spam.
They think it's better UI to verify the user in a GET request than in a POST request when they're actually making the comment.
Moreover, if the comment system uses AJAX, intercepting the POST request won't work properly.
You would think that this last point might make Cloudflare realise that trying to stop comment spam at the CDN level is a futile idea and can only result in breaking HTTP, but no. What Cloudflare is trying to do here is a fundamentally broken practice (in fact, the whole premise of “web application firewalls” is fundamentally broken, see below) because Cloudflare is not in a position to understand the semantic meaning of HTTP traffic and is definitely not in a position to rearchitect a site operator's web application so that it understands why its own AJAX requests are randomly being denied.

In other words, since CAPTCHAs are discriminatory to robots as discussed above, Cloudflare's service is unwittingly discriminatory to the JavaScript of the very websites it serves, breaking them. Cloudflare's response to this appears to be to CAPTCHA the entire website up-front on the off chance someone might want to post a comment, though even this doesn't always work; I have definitely encountered websites which didn't do so and which had broken AJAX functionality due to the subsequent AJAX-triggered requests being denied by Cloudflare, a condition the JS code was not designed to handle (nor would there be any sane way for it to handle it anyway).

## “Abuse”, and the Web Application Firewall fallacy

Being a comment spam filtering service isn't the only thing Cloudflare is trying to do besides being a CDN. They also claim to use their CAPTCHAs to mitigate other “abusive” traffic, like “harvesting e. mail addresses”.

> **lunar**: [...] Could you tell use [sic] what qualifies as abuse?
>
> **jgrahamc**: Abuse: comment spamming, harvesting email addresses, attacking web applications (e.g. SQL injection), HTTP DoS (exploiting slow web servers/applications to knock them offline). I'm not interested in L3/L4 DoS and Tor as that's non-existent (unless then [sic] exit node is separately part of a botnet).

This is a fundamentally broken practice. Attempting to filter for SQL injection at the CDN level is an excercise in futility and security theatre. This is the “Web Application Firewall” idea, the absurd idea that grepping requests/responses for known-to-be-naughty patterns is an adequate cure for vulnerable web applications. In reality it isn't trustworthy or accurate because it can't be.

If I try to login on a website with the username ' OR 0=0 --, Cloudflare has no way of knowing whether this is a SQL injection attack or just a peculiar username which the website has decided to legitimately issue. Cloudflare has no way of knowing if the website even uses SQL for data storage.

If I post ' OR 0=0 -- in a comment, Cloudflare has no way of knowing whether this is an SQL injection attack, or whether it will actually work, or whether I'm actually posting a comment discussing SQL injection and including examples (at which point this actually becomes a form of censorship).

What using Cloudflare does mean is that Cloudflare will randomly cause DoS to users if it thinks they're trying to use a pattern of text to which Cloudflare is by design allergic. The circumstances in which these denials of service occur are, of course, ill defined and in no way exhaustively enumerated, so using Cloudflare presents an intense and unaccounted liability in terms of availability and content neutrality for any website. It is essentially a way to make your website unreliable and fail randomly.

The “web application firewall” concept is fundamentally flawed in all instances, because it falsely presupposes that a blind intermediate proxy can reliably assess the semantic meaning of data transmitted, which is in actual fact impossible. Since this kind of “service” is part of the Cloudflare value proposition and an attempt to add a profit-making value-add, Cloudflare has essentially built their entire business on doing something which is a bad idea and which cannot be reliably implemented.

## Arbitrary and poorly defined content mangulation

Continuing with the flawed “web application firewall” theme of an unknowing proxy trying to guess the semantic meaning of content transmitted through it, Cloudflare insists on being a CDN which does un-CDN-like things in yet other ways. Rather than being a neutral proxy of traffic, even when Cloudflare isn't stochastically DoSing its customers websites, Cloudflare insists on doing interesting things with response bodies.

For example, it mangles e. mail addresses and replaces them with some JavaScript convolution intended to complicate harvesting. Except that it doesn't mangle e. mail addresses... it mangles anything which looks vaguely like an e. mail address, even if it isn't.

This

```
# Welcome to example.com. To access the foobar API, use curl:
curl 'https://foo@example.com/foobar'
```

becomes

```
# Welcome to example.com. To access the foobar API, use curl:
curl 'https://[email protected]/foobar'
```

XMPP address? Filtered. SIP address? Filtered. OpenSSH algorithm identifier? Filtered. Kerberos principal? Filtered. Because this filtering is necessarily done without regard to the context, it suffers from the same issues inherent in trying to prevent SQL injection, and is a potent demonstration of how “Web Application Firewalls” are a fundamentally stupid idea. Cloudflare can't actually have the slightest clue whether something is an e. mail address or not, but filter away it will.

Since I browse the web with JavaScript disabled by default, it's a running facepalm for me to find things on websites which aren't even email addresses replaced with [email protected], even parts of source code listings.

Of course, this practice also discriminates against users with JavaScript disabled and against browsers that don't support JavaScript, preventing them from viewing email addresses (or anything that looks like one).

Cloudflare also takes other liberties. It rejiggers a webpage's JavaScript to optimize it. Essentially Cloudflare modifies responses to apply a variety of poorly-defined transformations it thinks appropriate. From a website operator's perspective, this should be seen as a liability.

## It is in actual fact an intelligence agency

No other CDN service offers a free service comparable to that of Cloudflare. Why does Cloudflare offer service for free?

It's because Cloudflare isn't a CDN, it's an intelligence project. Its entire purpose is to collect data. This isn't my inference, the founders of Cloudflare have happily gone on record and said it:

> Back in 2003, Lee Holloway and I started Project Honey Pot as an open-source project to track online fraud and abuse. The Project allowed anyone with a website to install a piece of code and track hackers and spammers. We ran it as a hobby and didn't think much about it until, in 2008, the Department of Homeland Security called and said, 'Do you have any idea how valuable the data you have is?' That started us thinking about how we could effectively deploy the data from Project Honey Pot, as well as other sources, in order to protect websites online. That turned into the initial impetus for CloudFlare.

Yes, Cloudflare was founded by the Project Honeypot people.

Cloudflare also has an extremely generous free tier, and probably most of the websites which use it do not pay. But as we've come to understand in this era of surveillance capitalism, if you aren't paying, you aren't the customer — you're the product.

**Threat to anonymity of Tor users.** Cloudflare doesn't just pointlessly inconvenience Tor users by making them solve CAPTCHAs to view websites; it also poses a vehicle for the deanonymisation of Tor users. Cloudflare is basically an ideal platform for attacking Tor because it is the closest anyone has ever come to building a Global Active Adversary (GAA) — an entity which can observe and modify traffic anywhere in the world. Compare this with the lesser category of the Global Passive Adversary (GPA), which can observe but not modify traffic anywhere in the world. Tor is not designed to offer effective security against either of these.

To put this in perspective, in 2013 the NSA had given up on ever achieving GPA status (and therefore on ever being able to reliably deanonymise Tor traffic), let alone GAA. Cloudflare is effectively inviting people to help it become a GAA.

**Tracking cookies.** By the way, Cloudflare delivers a tracking cookie for any website which uses it. Even if the website is completely static and stateless, you still get a tracking cookie. (Since Cloudflare definitely has assets in the EU — it has to, it's a CDN — it's also pretty egregiously violating EU law here.

## It is probably a US Government-attached intelligence agency

Cloudflare is known for providing its services to a variety of websites, including notorious piracy websites such as The Pirate Bay. It is also a US company.

Since the US is known for taking down even companies that appear to be legal on paper, such as Megaupload, when they are associated with copyright infringement, this situation is peculiar.

**Probable liability.** 17 USC 512 provides for exemptions from liability for copyright infringement for various types of entity. 17 USC 512(c) provides for the takedown of “information residing on systems or networks at direction of users”; this is the well-known “DMCA notice” provision. However it also contains a provision 17 USC 512(b) which relates to caching proxies (i.e., Cloudflare).

This clause provides several conditions for this exemption from liability being valid:

* that the material is transmitted by the caching proxy without modification; and
* that the proxy handle takedown notices for material on a site if a court has ordered that the material be removed from the original site; amongst other things.

In other words, if a US court were to order that The Pirate Bay take down certain pages of their site, Cloudflare would be obliged to comply with notices asking them to give effect to that takedown in the absence of compliance by The Pirate Bay itself — and in any case, it seems likely that a US court could also just order Cloudflare directly to disable access to it.

But even this is moot because Cloudflare modifies the material it passes. Therefore, it cannot claim 17 USC 512(b) exemption at all. Moreover, since 47 USC 230 (the Communications Decency Act) explicitly exempts copyright from the immunity from liability it grants intermediaries, without an applicable 17 USC 512 exemption it is likely to be liable. Despite this, there has been an absence of even attempted attack by the US on Cloudflare's activities providing services to notorious piracy websites.

**My conclusions.** It appears likely that the US government could adversely affect Cloudflare's business via legal action if they wished. The fact that they have not is therefore unusual. However, it is well known that US federal law enforcement is happy to avoid shutting down illegal activities if they believe that they can obtain more intelligence by not doing so.

From previous programmes like PRISM, it is well demonstrated that most large tech companies are perfectly happy to comply with requests for total access by intelligence and law enforcement agencies. Moreover, given that Cloudflare is now used by an absurdly large number of websites, this means that Cloudflare is essentially the world's premier global MitM agency. This is a level of access and visibility that signals intelligence agencies could ordinarily only dream of, especially since it breaks TLS. To put it frankly, the intercept data available to Cloudflare is so tantalising to intelligence agencies, it seems almost beyond plausibility that they haven't gone after it, especially when considering the possibility of effectively blackmailing Cloudflare over the legality of their activities and, for that matter, the known historical contact of their founders with DHS. (Though even this assumes a default reluctance to assist extrajudicial surveillance on the part of tech companies, which is known to frequently not be the case in favour of indifference or outright enthusiasm.)

In other words, on the balance of probabilities, I believe that Cloudflare's continued lack of aggression from the US government and simple consideration of the standard MO of both intelligence agencies and tech companies makes it overwhelmingly likely that Cloudflare is an effective element of US signals intelligence.

This is not, of course, evidence or proof. However, the probabilities are adequate that assuming it is not the case would be, frankly, imprudent. Although the use of Cloudflare as a wiretap alone would be alarming in itself, the prospect of the fusion of Cloudflare's partial GAA and the NSA's partial GPA capabilities would be formidable in the extreme. An abundance of caution — and a distrust of companies essentially trying to put themselves in a position to MitM all web traffic, even if they claim benevolence — is wholly advisable.

After all, the mere possibility of this threatens to undermine the “crypto renaissance”, to undermine everything which the public cryptographic community has worked for since 2013 — and cryptography is all about mitigating mere possibilities in the first place.

## Conclusions

* Cloudflare's product is based on fundamentally flawed ideas such as “web application firewalling” which simply cannot work properly.
* Using Cloudflare is a way of stochastically DoSing and subtly breaking your own website.
* Using Cloudflare discriminates against Tor users, and for that matter some non-Tor users.
* Cloudflare is the world's leading global MitM agency, rivalling the power of any signals intelligence agency. They are in a position to monitor, surveil, deanonymise and modify an alarmingly large and growing percentage of web traffic because of its widespread usage and the fact that it terminates TLS sessions2. Even if you were to trust Cloudflare, putting this level of trust in one entity is extremely unwise.
* It is extremely hard to imagine this intercept data not ending up in the hands of intelligence agencies.

## Original Post

<https://www.devever.net/~hl/cloudflare>
