# Adding a "duress" password with PAM Duress

By Jake Edge
August 24, 2021

Users often store a lot of sensitive information on their computers—from credentials to banned texts to family photos—that they might normally expect to be protected by the login password of their account. Under some circumstances, though, users can be required to log into their system so that some third party (e.g. government agent) can examine and potentially copy said data. A new project, PAM Duress, provides a way to add other passwords to an account, each with its own behavior, which might be a way to avoid granting full access to the system, though the legality is in question.

As its name would imply, PAM Duress is a pluggable authentication module (PAM), which is the mechanism used on Linux and other Unix operating systems to easily allow adding different kinds of authentication methods. PAM is not exactly standardized, however, so there are multiple implementations of it, including Linux PAM that is used by Linux distributions. The Duress module allows administrators to configure the system to check for one or more extra passwords if the normal password associated with the user account does not match what is provided.

The project page gives a few examples of the kind of actions that could be triggered by an alternate password:

This functionality could be used to allow someone pressed to give a password under [coercion] to provide a password that grants access but in the background runs scripts to clean up sensitive data, close connections to other networks to limit lateral movement, and/or to send off a [notification] or alert (potentially one with detailed information like location, visible wifi hotspots, a picture from the camera, a link to a stream from the microphone, etc). You could even spawn a process to remove the pam_duress module so the threat actor won't be able to see if the duress module was available.
Scripts or binaries that are meant to be used when duress passwords are entered (i.e. duress programs) can be placed in either /etc/duress.d, for global duress actions, or ~/.duress for those specific to a particular user. In either case, the duress_sign script is used to process a file into something that PAM Duress can use. The script will prompt for a password, which it hashes with SHA-256, using the SHA-256 hash of the file's contents as the salt; the resulting hash value is written to duress-script-name.sha256. That stored hash protects against changes to the script and securely "stores" the password within a single hash value.

In order to use PAM Duress, the system's PAM authentication file (e.g. /etc/pam.d/common-auth) needs to be set up to try the user's password first (with the normal pam_unix.so module); if that fails, it should be configured to invoke pam_duress.so to check for any matching duress passwords. As shown in the documentation, that might look like the following:

    # Example /etc/pam.d/common-auth
    auth    [success=2 default=ignore]      pam_unix.so
    auth    [success=1 default=ignore]      pam_duress.so

    auth    requisite                       pam_deny.so
When invoked, PAM Duress will look at each file in the two duress program directories, hashing the provided password using the hash of the file's contents as salt, then comparing it to the value in the corresponding .sha256 file; if there is a match, the duress program gets invoked. If any file matches, success will be returned to PAM, which will result in access being granted and the user's login shell being invoked after the duress programs are run.

A simple example to demonstrate the module is provided in the repository. The pushover.sh script uses the API of the Pushover service to send a message reporting that the duress password has been used. The message includes the username of who logged in along with the local and external IP addresses of the system.

On the page describing the example, the script is signed with a password that is meant to be given to each person when it gets installed on their system. The example points out that the password should be changed if someone who knows it leaves the organization, but other strategies could be used (e.g. individual passwords). The integrity hash on the scripts seems to mostly be aimed at preventing inadvertent changes, since an attacker with access to the filesystem has lots of other ways to compromise the system. The demonstration script uses a configuration file for API keys that has no hash protection so it could be changed without detection—not that it really matters in the grand scheme of things.

Sending a message when the duress password has been used seems relatively innocuous from a legal perspective, but some of the other possible uses may not be. In a lengthy Hacker News discussion about PAM Duress, multiple commenters pointed out that deleting files in the background when requested to log in at a border crossing may well be an offense—if it is detected. It is, as with everything regarding security, a question of the type of threats being protected against. As "jeroenhd" put it:

If you're held under gunpoint, that script that wipes your entire hard drive will only make your day worse.
AFAIK if you actually get detained and questioned at airports, your drive will already get imaged before any password is even tried. You may be able to get away with this on a mobile device where this feature isn't generally expected (because who uses Linux on a smartphone in the first place).

I always wonder at what scenarios like these are supposed to be about. If saying no is not an option, pissing off your captors by giving them fake info probably isn't either.

I don't know what law enforcement would be looking for on my work drive, but if saying no is no longer an option, my encryption password isn't worth getting shot over.

"Spooky23" said that the idea of handling the situation with a technical means like PAM Duress is "silly nerd porn". Someone who has data that the authorities want access to should not be crossing a border with it on their device: "The only way to win is not to play." But others pointed out that the intent of a duress password is to "give the appearance of compliance" as "dredmorbius" said, which may be enough to satisfy the investigator and head off further inquiry.

No discussion of this sort ever happens without a reference to the xkcd pipe wrench scenario. Technical means to avert the often arbitrary and capricious nature of border searches and the like are certainly attractive to those of a technical bent. But providing plausible deniability by way of hidden encrypted disk partitions, filesystems that look like gibberish, or other schemes of that nature can all fall prey to the wrench scenario. If the authorities (or criminals, though it is sometimes hard to tell the difference these days) want to access the data badly enough, they are going to find a—quite possibly non-technical—means to do so.

As might be guessed, there were suggestions of other ideas for technical measures, such as a mechanism to "nuke" an encrypted disk if a duress password is entered. There was also a pointer to an earlier project, pam_duress, which has much the same focus as its nearly identical name would imply. In addition, there were suggestions of storing the sensitive data elsewhere (e.g. encrypted in the cloud) for restoration once the destination has been reached.

In the final analysis, having no sensitive data when crossing a border or otherwise being in a situation where there is a potential for duress being applied is the safest solution. Storing said data "elsewhere" has its own set of risks, of course—the cloud is hardly beyond the reach of nation-state actors. Dangerous-to-possess data, which is often defined quite differently in various parts of the world, is difficult to handle; technical means can certainly help but they are no panacea.

## Original

https://lwn.net/Articles/867158/
