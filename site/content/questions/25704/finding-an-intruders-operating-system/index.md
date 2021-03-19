+++
type = "question"
title = "Finding an intruder&#x27;s Operating system"
description = '''Hello all, I am very new to Wireshark, and I have been told that its possible to find an intruder&#x27;s operating system in my packet capture. I have the capture, but I&#x27;m not exactly sure what to look for, regarding the operating systems. Can anyone offer some advice? '''
date = "2013-10-07T06:36:00Z"
lastmod = "2014-05-16T17:39:00Z"
weight = 25704
keywords = [ "detection", "operating", "system" ]
aliases = [ "/questions/25704" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Finding an intruder's Operating system](/questions/25704/finding-an-intruders-operating-system)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25704-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello all, I am very new to Wireshark, and I have been told that its possible to find an intruder's operating system in my packet capture. I have the capture, but I'm not exactly sure what to look for, regarding the operating systems. Can anyone offer some advice?<br />
</p></div><div id="question-tags" class="tags-container tags">detection operating system</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Oct '13, 06:36</strong></p><img src="https://secure.gravatar.com/avatar/ff42a025a287795dd2f6ea45a43e9e5a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ruinzifra&#39;s gravatar image" /><p>Ruinzifra<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ruinzifra has no accepted answers">0%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 07 Oct '13, 06:42</p></div></div><div id="comments-container-25704" class="comments-container"></div><div id="comment-tools-25704" class="comment-tools"></div><div class="clear"></div><div id="comment-25704-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="25708"></span>

<div id="answer-container-25708" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-25708-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>There are some signs to find the OS, but none of them are 100% reliable.</p><ul><li>Look for typical values for MSS and Windows size in TCP connections</li><li>Look for typical RTT values</li></ul><blockquote><p><a href="http://www.netresec.com/?page=Blog&amp;month=2011-11&amp;post=Passive-OS-Fingerprinting">http://www.netresec.com/?page=Blog&amp;month=2011-11&amp;post=Passive-OS-Fingerprinting</a></p></blockquote><ul><li>Look for typical protocls of a certain OS (netbios, etc.)</li><li>Look for sign of certain client software (Browser: User-Agent, Banner, etc.)</li><li>Look for the TCP source ports used. There are difference of those ranges between different OSes</li><li>Look for the IP ID and how it changes. There are difference of ID between different OSes</li></ul><p>Furthermore read about: <a href="https://www.google.com/?q=passive+os+identification">passive OS detection</a></p><p>Regards<br />
Kurt</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Oct '13, 07:46</strong></p><img src="https://secure.gravatar.com/avatar/23b7bf5b13bc2c98b2e8aa9869ca5d75?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kurt%20Knochner&#39;s gravatar image" /><p>Kurt Knochner ♦<br />
<span class="score" title="24767 reputation points"><span>24.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="39 badges"><span class="silver">●</span><span class="badgecount">39</span></span><span title="237 badges"><span class="bronze">●</span><span class="badgecount">237</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kurt Knochner has 344 accepted answers">15%</span> </br></p></div><div class="post-update-info post-update-info-edited"><p>edited 08 Oct '13, 04:42</p></div></div><div id="comments-container-25708" class="comments-container"><span id="25712"></span><div id="comment-25712" class="comment"><div id="post-25712-score" class="comment-score"></div><div class="comment-text"><p>Thank you so much Kurt! That is along the lines of what I was thinking, but I needed to double check. Excellent info and answer.</p></div><div id="comment-25712-info" class="comment-info"><span class="comment-age">(07 Oct '13, 08:04)</span> Ruinzifra</div></div><span id="25715"></span><div id="comment-25715" class="comment"><div id="post-25715-score" class="comment-score"></div><div class="comment-text"><p>Hint: If a supplied answer resolves your question can you please "accept" it by clicking the checkmark icon next to it. This highlights good answers for the benefit of subsequent users with the same or similar questions. For extra points you can up vote the answer (thumb up).</p></div><div id="comment-25715-info" class="comment-info"><span class="comment-age">(07 Oct '13, 08:13)</span> Kurt Knochner ♦</div></div></div><div id="comment-tools-25708" class="comment-tools"></div><div class="clear"></div><div id="comment-25708-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="32850"></span>

<div id="answer-container-32850" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32850-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>I've been working on the <a href="http://digitalcorpora.org/corpora/scenarios/nitroba-university-harassment-scenario">Nitroba University Harassment Scenario</a>, which requires identification of individual hosts (not just operating systems) behind a NAT gateway using passive fingerprinting techniques. I found that the IPid, TTL, and TCP source port were rewritten by the gateway (as expected). The IPid was fully randomised, and the TTL was set to a fixed value (64) by the gateway. Also, HTTP user agents can be changed easily in software (I use the Firefox User Agent Switcher plugin for this).</p><p>The attributes I've settled on that should work to identify operating systems in this scenario are:</p><ul><li>TCP window size: it never seems to go above 65535 for MSIE browsers on Windows, but can be up to 524280 for Mac OS X browsers. (These numbers might have changed since 2008, when the capture was created.)</li><li>Presence/absence &amp; order of headers in HTTP requests, which cannot be changed easily in client software (although they could be spoofed with netcat or similar)</li><li>the HTTP Accept header, which can indicate the presence of certain plugins (e.g. if it includes application/x-shockwave-flash)</li></ul><p>Databases of these criteria don't seem to be publicly available, based on my searches. (Corrections gratefully accepted.)</p><p>To identify individual hosts, the following seem necessary:</p><ul><li>TCP timestamps to determine the boot time of the host and rule out certain</li><li>individual HTTP cookies</li><li>data sent in Google Analytics queries, including character set, screen resolution &amp; color depth, Flash version, and Java plugin status</li></ul></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 May '14, 17:39</strong></p><img src="https://secure.gravatar.com/avatar/04ec318f1220b29047b107472a7e5661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="paulgear&#39;s gravatar image" /><p>paulgear<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="paulgear has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 16 May '14, 17:55</p></div></div><div id="comments-container-32850" class="comments-container"></div><div id="comment-tools-32850" class="comment-tools"></div><div class="clear"></div><div id="comment-32850-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

