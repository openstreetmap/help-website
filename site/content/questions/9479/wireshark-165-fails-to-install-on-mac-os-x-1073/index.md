+++
type = "question"
title = "Wireshark 1.6.5 fails to install on Mac OS X 10.7.3"
description = '''I&#x27;m having trouble installing the 1.6.5 Wireshark on a MacBook Pro running OS X 10.7.3. The installer runs but very little is really done. No /Applications/Wireshark created, no /Library/Wireshark created. It did create the /Library/StartupItems/ChmodBPF and did create the BPF devices in /dev. The f...'''
date = "2012-03-11T19:22:00Z"
lastmod = "2012-07-19T21:03:00Z"
weight = 9479
keywords = [ "failure", "mac", "lion", "install" ]
aliases = [ "/questions/9479" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark 1.6.5 fails to install on Mac OS X 10.7.3](/questions/9479/wireshark-165-fails-to-install-on-mac-os-x-1073)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9479-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I'm having trouble installing the 1.6.5 Wireshark on a MacBook Pro running OS X 10.7.3. The installer runs but very little is really done. No /Applications/Wireshark created, no /Library/Wireshark created. It did create the /Library/StartupItems/ChmodBPF and did create the BPF devices in /dev. The following are all the messages (note the errors) that appeared in the console during the install process (by double-clicking on the "Wireshark 1.6.5 Intel 64.pkg" file from the mounted "dmg" file that I downloaded):</p><pre><code>==================Start of Messages===============================

3/11/12 6:22:37.181 PM Installer: @(#)PROGRAM:Install  PROJECT:Install-686.3

3/11/12 6:22:37.181 PM Installer: @(#)PROGRAM:Installer  PROJECT:Installer-530

3/11/12 6:22:37.181 PM Installer: Hardware: MacBookPro4,1 @ 2.40 GHz (x 2), 6144 MB RAM

3/11/12 6:22:37.182 PM Installer: Running OS Build: Mac OS X 10.7.3 (11D50)

3/11/12 6:22:37.349 PM Installer: Wireshark 1.6.5 Intel 64  Installation Log

3/11/12 6:22:37.349 PM Installer: Opened from: /Volumes/Wireshark/Wireshark 1.6.5 Intel 64.pkg

3/11/12 6:22:48.301 PM Installer: InstallerStatusNotifications plugin loaded

3/11/12 6:23:34.704 PM Installer:
 ================================================================================

3/11/12 6:23:34.704 PM Installer: User picked Standard Install

3/11/12 6:23:34.704 PM Installer: Choices selected for installation:

3/11/12 6:23:34.704 PM Installer:   Install: &quot;Wireshark 1.6.5 Intel 64&quot;

3/11/12 6:23:34.704 PM Installer:   Install: &quot;Wireshark&quot;

3/11/12 6:23:34.704 PM Installer:   Install: &quot;Set capture permissions at startup&quot;

3/11/12 6:23:34.705 PM Installer:   Install: &quot;Command line utilities&quot;

3/11/12 6:23:34.705 PM Installer:  ================================================================================

3/11/12 6:23:35.039 PM Installer: Configuring volume &quot;Bob&#39;s MacBook&quot;

3/11/12 6:23:35.053 PM Installer: Free space on &quot;Bob&#39;s MacBook&quot;: 267.03 GB (267032055808 bytes).

3/11/12 6:23:35.053 PM Installer: Create temporary directory &quot;/var/folders/x0/390xwb6n07g0t1wcg7sw3_zr0000gn/T//Install.1065HvHBbv&quot;

3/11/12 6:23:35.059 PM Installer: IFPKInstallElement (3 packages)

3/11/12 6:23:35.118 PM authorizationhost: SFBuiltinEntitled: Installer.app is not entitled for system.install.apple-software

3/11/12 6:23:35.155 PM authorizationhost: SFBuiltinEntitled: Installer.app is not entitled for system.install.app-store-software

3/11/12 6:23:35.191 PM authorizationhost: SFBuiltinEntitled: Installer.app is not entitled for system.install.app-store-software

3/11/12 6:23:35.192 PM com.apple.SecurityServer: Failed to authorize right &#39;system.install.app-store-software&#39; by client &#39;/System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/Resources/installd&#39; [1076] for authorization created by &#39;/System/Library/CoreServices/Installer.app&#39; [1065]

3/11/12 6:23:35.200 PM installd: PackageKit: ----- Begin install -----

3/11/12 6:23:38.163 PM installd: Installed &quot;Wireshark 1.6.5 Intel 64&quot; ()

3/11/12 6:23:38.186 PM installd: PackageKit: ----- End install -----

3/11/12 6:23:38.206 PM Installer: Running install actions

3/11/12 6:23:38.209 PM Installer: Removing temporary directory &quot;/var/folders/x0/390xwb6n07g0t1wcg7sw3_zr0000gn/T//Install.1065HvHBbv&quot;

3/11/12 6:23:38.213 PM Installer: Finalize disk &quot;Bob&#39;s MacBook&quot;

3/11/12 6:23:38.214 PM Installer: Notifying system of updated components

3/11/12 6:23:38.214 PM Installer: **** Summary Information ****

3/11/12 6:23:38.214 PM Installer:   Operation      Elapsed time

3/11/12 6:23:38.214 PM Installer: -----------------------------

3/11/12 6:23:38.214 PM Installer:        disk      0.01 seconds

3/11/12 6:23:38.214 PM Installer:      script      0.00 seconds

3/11/12 6:23:38.214 PM Installer:        zero      0.03 seconds

3/11/12 6:23:38.214 PM Installer:     install      3.14 seconds

3/11/12 6:23:38.214 PM Installer:     -total-      3.19 seconds

3/11/12 6:23:38.391 PM Installer: IFDInstallController E34A4560 state = 5

3/11/12 6:23:38.391 PM Installer: Displaying &#39;Install Succeeded&#39; UI.

==================End of Messages===============================</code></pre><p>Several things caught my eye:</p><p>There are a few errors of note in the console log, even though the installer says the install succeeded. The errors that I noticed were:</p><p>3/11/12 6:23:35.118 PM authorizationhost: SFBuiltinEntitled: Installer.app is not entitled for system.install.apple-software</p><p>3/11/12 6:23:35.155 PM authorizationhost: SFBuiltinEntitled: Installer.app is not entitled for system.install.app-store-software</p><p>3/11/12 6:23:35.191 PM authorizationhost: SFBuiltinEntitled: Installer.app is not entitled for system.install.app-store-software</p><p>3/11/12 6:23:35.192 PM com.apple.SecurityServer: Failed to authorize right 'system.install.app-store-software' by client '/System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/Resources/installd' [1076] for authorization created by '/System/Library/CoreServices/Installer.app' [1065]</p><p>Why is the app-store even involved in this process (Installer.app is not entitled for system.install.app-store-software), as I downloaded the disk image file directly from <a href="http://wireshark.org">wireshark.org</a>???</p><p>I've had no other problems installing software like this, but have to admit not many are the "pkg" style of installs.</p><p>my looking around on this forum has not shown me anyone else having similar problems. I've even tried running the installer from the command line as "root" with no differences, ie it says it worked but nothing appears in the /Applications/Wireshark folder or the /Library/Wireshark folders. I even tried to create these folders before running the install and still no luck.</p><p>One thing I did notice from the output of another "installer" command to get a little more info about the package (this doesn't do anything other than look at some details of what is in the package and how it will get installed):</p><pre><code>===================Start of installer query command========================

bash-3.2$ installer -verbose -pkginfo -pkg /Volumes/Wireshark/Wireshark\\ 1.6.5\\ Intel\\ 64.pkg

Package information:

Package           : Wireshark 1.6.5 Intel 64
Status            : MetaPackage
Will Restart      : NO
Size              : 82928 KB
Must Authenticate : NO
Title             : Wireshark 1.6.5 Intel 64
Description       : 
Message           : MetaPackage information only, it is not installed

Package           : Wireshark
Status            : Warning
Will Restart      : NO
Size              : 82912 KB
Must Authenticate : YES
Title             : Wireshark
Description       : The main Wireshark application
Message           : The Wireshark network protocol analyzer

Package           : Set capture permissions at startup
Status            : Warning
Will Restart      : NO
Size              : 12 KB
Must Authenticate : YES
Title             : Set capture permissions at startup
Description       : This installs a startup item (ChmodBPF) that changes the group permissions of each BPF device to allow access for the &quot;access_bpf&quot; group. It creates the &quot;access_bpf&quot; group if it doesn&#39;t exist and adds the current user to the group.
Message           : Install the ChmodBPF startup item and add an access_bpf group

Package           : Command line utilities
Status            : Warning
Will Restart      : NO
Size              : 4 KB
Must Authenticate : YES
Title             : Command line utilities
Description       : Various utilities associated with Wireshark including TShark, dumpcap, mergecap, capinfos, and editcap.
Message           : Command line utilities associated with Wireshark

====================End of installer query command============================</code></pre><p>Notice that the "Must Authenticate" is set to "YES" for the "Wireshark" and "Set capture permissions at startup" and "Command line utilities" packages but not for the first "Wireshark 1.6.5 Intel 64" metapackage. I was asked to authenticate once at the start and assume that this one request is remembered for the 3 packages that need it, so not sure if this is pertinent. Also note that these same three components also have a "Warning" for the Status - I have no idea what that pertains to - any ideas?</p><p>Any suggestions on how to get things installed and what problem these errors are really trying to point out?</p><p>Thanks very much for your help...</p><p>-Bob</p></div><div id="question-tags" class="tags-container tags">failure mac lion install</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>11 Mar '12, 19:22</strong></p><img src="https://secure.gravatar.com/avatar/e06d78f803ce68425d2c377f6e4d8b5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="DeepYogurt&#39;s gravatar image" /><p>DeepYogurt<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="DeepYogurt has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Mar '12, 00:24</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-9479" class="comments-container"></div><div id="comment-tools-9479" class="comment-tools"></div><div class="clear"></div><div id="comment-9479-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="12874"></span>

<div id="answer-container-12874" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12874-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hmm. A user had an installation problem with another non-Apple program, with those warnings, as per <a href="http://www.dragonframe.com/forum/viewtopic.php?f=2&amp;t=639">this forum post</a>. Their problem was that the software kept asking for an activation key even though they entered it each time they tried running it.</p><p>The problem may have been that they'd somehow lost their admin privileges (i.e., "admin" was no longer in their default group set), and they fixed the problem this way:</p><pre><code>1) Opened up System Preferences -&gt; Users &amp; Groups
2) Created a new, temporary user account with administrator privileges
3) For the current, existing user, I unchecked the &quot;Allow user to administer this computer&quot; box
4) Restarted, &amp; logged in as the new administrator
5) System Preferences -&gt; Users &amp; Groups
6) For the real administrator account, re-checked the &quot;Allow user to administer this computer&quot; box
7) Logged out &amp; logged back in as the actual normal user/administrator
8) Deleted the temporary administrator account
9) Installed Dragonframe</code></pre><p>If your account is supposed to have administrative privileges, try going into System Preferences and seeing whether you still have them and, if not, try the above sequence (except with "Dragonframe" replaced by "Wireshark", obviously :-)). If your account <em>isn't</em> supposed to have administrative privileges, try installing Wireshark from an account with administrative privileges, and see whether that works.</p><p>In either case, add a comment indicating whether that worked or not.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '12, 20:51</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-12874" class="comments-container"></div><div id="comment-tools-12874" class="comment-tools"></div><div class="clear"></div><div id="comment-12874-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="12875"></span>

<div id="answer-container-12875" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-12875-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Wait, I stand corrected, I didn't read it properly.</p><p>3/11/12 6:23:35.118 PM authorizationhost: SFBuiltinEntitled: Installer.app is not entitled for system.install.apple-software</p><p>'/System/Library/PrivateFrameworks/PackageKit.framework/Versions/A/Resources/installd' [1076] for authorization created by '/System/Library/CoreServices/Installer.app' [1065]</p><p>I have read a few articles on this after a few searches. Feel like I owe it to you for my knee-jerk response. There are two recurring suggestions, user accounts and permissions and security signing. Security signing makes sense as it could well be installer.app self checking to make sure it hasn't been tampered with (a potential way to circumvent a large amount of software protection I guess), but this error is borne of the installer, whether through wireshark (unlikely because as I said I've seen it before when installing Logic) or installer.app itself.</p><p>I suggest repairing permissions, then removing your Admin rights, restarting then and reinstating them.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>19 Jul '12, 21:03</strong></p><img src="https://secure.gravatar.com/avatar/f419a609126e558ee3f528b6264638b1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="GenZ&#39;s gravatar image" /><p>GenZ<br />
<span class="score" title="0 reputation points">0</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="GenZ has no accepted answers">0%</span></p></div></div><div id="comments-container-12875" class="comments-container"></div><div id="comment-tools-12875" class="comment-tools"></div><div class="clear"></div><div id="comment-12875-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

