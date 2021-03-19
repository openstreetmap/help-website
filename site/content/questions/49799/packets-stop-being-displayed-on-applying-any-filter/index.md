+++
type = "question"
title = "Packets stop being displayed on applying ANY filter."
description = '''Hi I started using Wireshark just couple of weeks ago.  When I apply ANY filter (even as simple as ip.addr = MyIP) all packets disappear from the display. This happens with any valid filter. The status bar keeps on showing &quot;Number of packets XXX, Displayed XXX (100%). But nothing actually is seen in...'''
date = "2016-02-03T19:08:00Z"
lastmod = "2016-02-03T19:46:00Z"
weight = 49799
keywords = [ "display-filter" ]
aliases = [ "/questions/49799" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Packets stop being displayed on applying ANY filter.](/questions/49799/packets-stop-being-displayed-on-applying-any-filter)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49799-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi I started using Wireshark just couple of weeks ago. When I apply ANY filter (even as simple as ip.addr = MyIP) all packets disappear from the display. This happens with any valid filter. The status bar keeps on showing "Number of packets XXX, Displayed XXX (100%). But nothing actually is seen in the display window. I have to restart wireshark to see the packets. But as soon as I apply any filter, the packets are gone from display. Even removing the filter does not work. I am using Wireshark 2.0.1 on Windows Server 2008 R2. Strangely, it DID work on the same machine earlier. I even re-installed Wireshark, but the problem persists. Would appreciate any help on this.</p></div><div id="question-tags" class="tags-container tags">display-filter</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>03 Feb '16, 19:08</strong></p><img src="https://secure.gravatar.com/avatar/b9d9a0eb4dd0a55160e12171678a9ca6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pvm&#39;s gravatar image" /><p>pvm<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pvm has no accepted answers">0%</span></p></div></div><div id="comments-container-49799" class="comments-container"><span id="50328"></span><div id="comment-50328" class="comment"><div id="post-50328-score" class="comment-score"></div><div class="comment-text"><p>Does this also haven with saved capture files or only live captures? If it happens on a capture file, can you share the capture file publicly so we can check it?</p></div><div id="comment-50328-info" class="comment-info"><span class="comment-age">(19 Feb '16, 02:34)</span> grahamb ♦</div></div></div><div id="comment-tools-49799" class="comment-tools"></div><div class="clear"></div><div id="comment-49799-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="49800"></span>

<div id="answer-container-49800" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-49800-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Could you maybe try to restart your machine using safe mode with networking of Windows and try in safe mode? As the computer is turning on, press F8 repeatedly, and choose Safe Mode with Network. Then try your Wireshark again! We might then find it's a driver or an APP causing the problem in normal mode. Y.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>03 Feb '16, 19:46</strong></p><img src="https://secure.gravatar.com/avatar/0d34cdc32519fc3c7ebcbbfa3aa5873a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thewol&#39;s gravatar image" /><p>thewol<br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thewol has no accepted answers">0%</span></p></div></div><div id="comments-container-49800" class="comments-container"><span id="50327"></span><div id="comment-50327" class="comment"><div id="post-50327-score" class="comment-score"></div><div class="comment-text"><p>Thanks thewol, that was a good pointer. I am running it on a VM hosed on ESX server in our server room. Couldn't find time to try that due to project work. When I got hold of the login for the ESX server, I tried booting it in safe mode (with networking) but then Wireshark couldn't find the network interface. Tried few things to get around this but did not succeed. Finally I ended up switching over to another VM. But still curious to figure it out. Will do it sometime when I am free from the workload though.</p></div><div id="comment-50327-info" class="comment-info"><span class="comment-age">(19 Feb '16, 01:44)</span> pvm</div></div></div><div id="comment-tools-49800" class="comment-tools"></div><div class="clear"></div><div id="comment-49800-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

