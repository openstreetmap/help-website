+++
type = "question"
title = "[1.10.0] trying to run on OSX10.5.8 but crashes on load."
description = '''Hey, Every time I launch WS it crashes with the following report... The interesting line is the last one. Does this need to be filed as a bug? Process: Wireshark [770] Path: /Software/Security/Wireshark.app/Contents/MacOS/Wireshark Identifier: org.wireshark.Wireshark Version: ??? (???) Code Type: X8...'''
date = "2013-06-15T00:00:00Z"
lastmod = "2013-07-29T14:27:00Z"
weight = 22081
keywords = [ "mac" ]
aliases = [ "/questions/22081" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [\[1.10.0\] trying to run on OSX10.5.8 but crashes on load.](/questions/22081/1100-trying-to-run-on-osx1058-but-crashes-on-load)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-22081-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-22081-score" class="post-score" title="current number of votes">0</div><span id="post-22081-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hey,</p><p>Every time I launch WS it crashes with the following report... The interesting line is the last one. Does this need to be filed as a bug?</p><p>Process: Wireshark [770] Path: /Software/Security/Wireshark.app/Contents/MacOS/Wireshark Identifier: org.wireshark.Wireshark Version: ??? (???) Code Type: X86 (Native) Parent Process: launchd [99]</p><p>Date/Time: 2013-06-15 07:41:54.920 +0100 OS Version: Mac OS X 10.5.8 (9L31a) Report Version: 6 Anonymous UUID: 5DCB56D2-C51F-44C6-9413-40CBF6383CE7</p><p>Exception Type: EXC_BREAKPOINT (SIGTRAP) Exception Codes: 0x0000000000000002, 0x0000000000000000 Crashed Thread: 0</p><p>Dyld Error Message: unknown required load command 0x80000022</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-mac" rel="tag" title="see questions tagged &#39;mac&#39;">mac</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 Jun '13, 00:00</strong></p><img src="https://secure.gravatar.com/avatar/bb0dd8c140ac683baf24b6438c825c87?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ASGR&#39;s gravatar image" /><p><span>ASGR</span><br />
<span class="score" title="20 reputation points">20</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ASGR has no accepted answers">0%</span></p></div></div><div id="comments-container-22081" class="comments-container"><span id="22083"></span><div id="comment-22083" class="comment"><div id="post-22083-score" class="comment-score">1</div><div class="comment-text"><p>I've back-tracked through the previous versions and the last known working version is 1.8.6.</p></div><div id="comment-22083-info" class="comment-info"><span class="comment-age">(15 Jun '13, 00:51)</span> <span class="comment-user userinfo">ASGR</span></div></div><span id="23414"></span><div id="comment-23414" class="comment"><div id="post-23414-score" class="comment-score"></div><div class="comment-text"><p>Had the same problem, MacBookPro 3,1 OS X 10.5.8, current (and prior) version of Wireshark, which at the moment are Wireshark 1.10.1 Intel 32.dmg and Wireshark 1.8.9 Intel 32.dmg. Also tried the last dev. release, Wireshark 1.10.0rc2 Intel 32.dmg and the previous PPC release (since 10.5 has Rosetta, it should work, if slower) Wireshark 1.8.9 PPC 32.dmg. Crashes all around. None worked. Got 1.8.6 Intel from main repository, works!</p><p>Links: <a href="http://www.wireshark.org/download/osx/all-versions/">All OS X Versions</a></p><p><a href="http://www.wireshark.org/download/osx/all-versions/Wireshark%201.8.6%20Intel%2032.dmg">Wireshark 1.8.6 Intel 32.dmg</a></p></div><div id="comment-23414-info" class="comment-info"><span class="comment-age">(28 Jul '13, 11:35)</span> <span class="comment-user userinfo">Lubo Diakov</span></div></div><span id="23432"></span><div id="comment-23432" class="comment"><div id="post-23432-score" class="comment-score"></div><div class="comment-text"><blockquote><p>since 10.5 has Rosetta, it should work, if slower</p></blockquote><p>...but it won't support capturing packets, as Rosetta does <em>not</em> understand BPF, the underlying mechanism used by libpcap (and thus by tcpdump, Wireshark, etc.) to capture packets.</p></div><div id="comment-23432-info" class="comment-info"><span class="comment-age">(29 Jul '13, 14:27)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-22081" class="comment-tools"></div><div class="clear"></div><div id="comment-22081-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="23415"></span>

<div id="answer-container-23415" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-23415-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-23415-score" class="post-score" title="current number of votes">1</div><span id="post-23415-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The buildbot being used to build the 32-bit x86 images switched from running Leopard to running Snow Leopard. By default, building on OS X 10.x.y means that the resulting code will run (modulo bugs) on OS X 10.x.y and later, but will <em>not</em> necessarily run on earlier versions - even versions that differ in the "y" (so that something built on 10.5.2 won't necessarily run on 10.5.0 or 10.5.1).</p><p>The script used to build support libraries for Wireshark was recently changed to have a flag to build them to target a particular OS X major release, even if built on a Software Update of that release or on a later release, and the configure script for Wireshark was recently changed to have a flag that does the same thing.</p><p>(For OS X nerds:</p><p>The flag in question 1) causes the software in question to be built against the SDK for that version of the OS and 2) cause it to be built with a -mmacosx-version-min flag that specifies that version. The first makes sure the system libraries against which the software is built are the ones for that OS, so the resulting shared libraries and programs don't expect later versions than those that come with the OS, and the second makes sure various features, including linker features, not available on that version of the OS aren't required by the program; the dyld warning above is saying that a feature only available in Snow Leopard and later is required by the program.)</p><p>The buildbots have had support libraries built with the appropriate flag, but they haven't yet been reconfigured to pass the appropriate flag to the configure script. This is being tracked, for the 32-bit version, in <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8986">Wireshark bug 8986</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Jul '13, 13:54</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-23415" class="comments-container"><span id="23431"></span><div id="comment-23431" class="comment"><div id="post-23431-score" class="comment-score"></div><div class="comment-text"><p>That bug is now closed. If you download Wireshark 1.10.2pre1-51015 Intel 32.dmg or a later Wireshark 1.10.2pre1-XXX Intel 32.dmg build from <a href="http://www.wireshark.org/download/prerelease/,">http://www.wireshark.org/download/prerelease/,</a> and install it, it should work.</p><p>Note that, as per <a href="https://bugs.wireshark.org/bugzilla/show_bug.cgi?id=8993">bug 8993</a>, the icon in /Applications is invisible. You <em>might</em> have to launch it the first time by doing</p><pre><code>open /Applications/Wireshark.app</code></pre><p>from the command line; after that, although it's a bit difficult to double-click an invisible icon, it seems to work if you try hard enough. Or you might try clicking or double-clicking on the icon <em>title</em> ("Wireshark") rather than on the area where it would be if it were visible.</p></div><div id="comment-23431-info" class="comment-info"><span class="comment-age">(29 Jul '13, 14:26)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div></div><div id="comment-tools-23415" class="comment-tools"></div><div class="clear"></div><div id="comment-23415-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

