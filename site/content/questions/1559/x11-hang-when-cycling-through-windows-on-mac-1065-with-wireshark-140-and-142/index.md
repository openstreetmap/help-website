+++
type = "question"
title = "X11 hang when cycling through windows on Mac 10.6.5 with Wireshark 1.4.0 and 1.4.2"
description = '''I just downloaded the snow leopard 64 bit version of wireshark 1.4.2. The same problem with my 1.4.0 version. With the wireshark window open (in X11), if I hit the tilde key (~) to cycle through the windows, it cycles once but then freezes and wireshark will not do anything at all. I have to quit X1...'''
date = "2010-12-31T08:32:00Z"
lastmod = "2011-01-02T00:41:00Z"
weight = 1559
keywords = [ "leopard", "mac", "freezing", "snow", "macintosh" ]
aliases = [ "/questions/1559" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [X11 hang when cycling through windows on Mac 10.6.5 with Wireshark 1.4.0 and 1.4.2](/questions/1559/x11-hang-when-cycling-through-windows-on-mac-1065-with-wireshark-140-and-142)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1559-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>I just downloaded the snow leopard 64 bit version of wireshark 1.4.2. The same problem with my 1.4.0 version. With the wireshark window open (in X11), if I hit the tilde key (~) to cycle through the windows, it cycles once but then freezes and wireshark will not do anything at all. I have to quit X11 and start back over. I've not noticed this before. I've used wireshark for a couple of years now. It may be some recent change in my environment.</p><p>If there is some why I can help debug this, please let me know.</p><p>Thank you, pedz</p></div><div id="question-tags" class="tags-container tags">leopard mac freezing snow macintosh</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>31 Dec '10, 08:32</strong></p><img src="https://secure.gravatar.com/avatar/0ce4db5e1083663c575158643313852c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pedz&#39;s gravatar image" /><p>pedz<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pedz has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 01 Jan '11, 13:15</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></div></div><div id="comments-container-1559" class="comments-container"></div><div id="comment-tools-1559" class="comment-tools"></div><div class="clear"></div><div id="comment-1559-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="1566"></span>

<div id="answer-container-1566" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1566-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I'm not aware of any functionality to cycle through X11 windows (on OS/X) by pressing the tilde-key. If this a personal setting or shortcut, what key-sequence does it represent?</p><p>(the tilde-key is also not a Wireshark assigned key to cycle through it's open windows)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>01 Jan '11, 01:51</strong></p><img src="https://secure.gravatar.com/avatar/7901a94d8fdd1f9f47cda9a32fcfa177?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SYN-bit&#39;s gravatar image" /><p>SYN-bit ♦♦<br />
<span class="score" title="17094 reputation points"><span>17.1k</span></span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="245 badges"><span class="bronze">●</span><span class="badgecount">245</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SYN-bit has 174 accepted answers">20%</span></p></div></div><div id="comments-container-1566" class="comments-container"><span id="1567"></span><div id="comment-1567" class="comment"><div id="post-1567-score" class="comment-score"></div><div class="comment-text"><p>Oops, I should have googled first and then answered :-)</p><p>Apperently the Command+` does indeed cycle through the open X11 windows. I just tried it myself on my Mac and it does cycle through all windows, not freezing on the Wireshark ones. I'm using a development version, but also tried with version 1.4.0.</p><p>It must be something in your environment. What have you tried so far to isolate the issue?</p></div><div id="comment-1567-info" class="comment-info"><span class="comment-age">(01 Jan '11, 01:58)</span> SYN-bit ♦♦</div></div><span id="1570"></span><div id="comment-1570" class="comment"><div id="post-1570-score" class="comment-score"></div><div class="comment-text"><p>I just discovered that this is a Mac problem. I can recreate it using pure Mac xterms. It is really horrible. Once it freezes, the whole X11 system is frozen.</p><p>I found this discussion: <a href="http://lists.apple.com/archives/X11-users/2010/Apr/msg00090.html">http://lists.apple.com/archives/X11-users/2010/Apr/msg00090.html</a> (in case someone else bumps into this thread in their searches)</p><p>(I don't use the X11 stuff much and should have tested more before posting. Sorry)</p></div><div id="comment-1570-info" class="comment-info"><span class="comment-age">(01 Jan '11, 06:43)</span> pedz</div></div></div><div id="comment-tools-1566" class="comment-tools"></div><div class="clear"></div><div id="comment-1566-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="1584"></span>

<div id="answer-container-1584" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1584-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>What version of OS X do you have?<br />
</p><p>To trigger this bug, you need a non-default setting for quartz-wm, "The problem only occurs for me if the "Enable key equivalents under X11" option is disabled from the System Preferences/Input tab." : http://xquartz.macosforge.org/trac/ticket/370</p><p>So just run Software Update and you should be fine.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Jan '11, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/49ae1042b27f435f55de01b640671189?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jeremyhu&#39;s gravatar image" /><p>jeremyhu<br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jeremyhu has no accepted answers">0%</span> </br></p></div></div><div id="comments-container-1584" class="comments-container"><span id="1591"></span><div id="comment-1591" class="comment"><div id="post-1591-score" class="comment-score"></div><div class="comment-text"><p>I.e., this bug <em>should</em> be fixed in 10.6.5; were you running 10.6.5, or an earlier release? If it's an earlier release of Snow Leopard, Software Update will update you to 10.6.5.</p><p>Get the OS version from "About This Mac..." in the Apple menu. Also, get the version of X11 from "About X11..." in the X11 menu when X11 is in the foreground; on my 10.6.5 machine, the version is "XQuartz 2.3.6 (xorg-server 1.4.2-apple56)". If that's not the version you have on a 10.6.5 machine, that might be the problem.</p></div><div id="comment-1591-info" class="comment-info"><span class="comment-age">(02 Jan '11, 15:57)</span> Guy Harris ♦♦</div></div><span id="16348"></span><div id="comment-16348" class="comment"><div id="post-16348-score" class="comment-score"></div><div class="comment-text"><p>Hmmm... I'm running 10.6.8 with XQuartz 2.3.6 (xorg-server 1.4.2-apple56) and "Software Update..." says that my software is up-to-date. Still, I do now also get the same freezing behavior when cycling through X11 windows with "CMD+`".</p><p>Enabling the "Enable key equivalents under X11" option does indeed make the problem go away.</p></div><div id="comment-16348-info" class="comment-info"><span class="comment-age">(27 Nov '12, 09:16)</span> SYN-bit ♦♦</div></div></div><div id="comment-tools-1584" class="comment-tools"></div><div class="clear"></div><div id="comment-1584-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

