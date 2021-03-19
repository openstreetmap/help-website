+++
type = "question"
title = "Wireshark - Frame.time_epoch vs prism.did.mactime"
description = '''How to differentiate between Frame.time_epoch vs prism.did.mactime ? MACtime is in microseconds, is time_epoch also a microsecond value ?'''
date = "2014-09-16T12:37:00Z"
lastmod = "2014-09-16T17:37:00Z"
weight = 36375
keywords = [ "frame.time_epoch", "vs", "prism.did.mactime" ]
aliases = [ "/questions/36375" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Wireshark - Frame.time\_epoch vs prism.did.mactime](/questions/36375/wireshark-frametime_epoch-vs-prismdidmactime)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36375-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>How to differentiate between Frame.time_epoch vs prism.did.mactime ? MACtime is in microseconds, is time_epoch also a microsecond value ?</p></div><div id="question-tags" class="tags-container tags">frame.time_epoch vs prism.did.mactime</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>16 Sep '14, 12:37</strong></p><img src="https://secure.gravatar.com/avatar/32e1f189aa62f1787379b67ea3542959?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dheryta&#39;s gravatar image" /><p>dheryta<br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dheryta has no accepted answers">0%</span></p></div></div><div id="comments-container-36375" class="comments-container"></div><div id="comment-tools-36375" class="comment-tools"></div><div class="clear"></div><div id="comment-36375-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="36381"></span>

<div id="answer-container-36381" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-36381-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p><code>frame.time_epoch</code> is the packet time stamp from the capture mechanism; it is in units of nanoseconds since January 1, 1970, 00:00:00 UTC (except possibly for leap seconds, but you <em>really</em> don't want to hear me rant about POSIX and leap seconds). It doesn't necessarily have full nanosecond <em>precision</em>; that depends on the precision of the clock from which the time stamp came (which could be in microseconds or even larger fractions of a second).</p><p><code>prism.did.mactime</code> is the lower 32 bits of some microsecond-resolution MAC-layer timer; I <em>suspect</em> it's the timer for the Time Synchronization Function of IEEE 802.11, but I don't know for certain. Unlike <code>frame.time_epoch</code>, it does <em>not</em> represent a date and time.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>16 Sep '14, 17:37</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-36381" class="comments-container"><span id="36385"></span><div id="comment-36385" class="comment"><div id="post-36385-score" class="comment-score"></div><div class="comment-text"><p>By capture mechanism is it meant that the machine on which capture was initiated or where wireshark is capturing? Also, is mactime dependent on NIC card? Is there any official documentation which covers all possible details of these? Thanks for help.</p></div><div id="comment-36385-info" class="comment-info"><span class="comment-age">(16 Sep '14, 18:17)</span> dheryta</div></div><span id="36386"></span><div id="comment-36386" class="comment"><div id="post-36386-score" class="comment-score"></div><div class="comment-text"><p>The capture mechanism is the mechanism that the program that does the packet capture uses - for example:</p><ul><li><code>PF_PACKET</code> sockets (and the rest of the network code path) on Linux</li><li>BPF on OS X and *BSD and Solaris 11;</li><li>WinPcap on WIndows;</li></ul><p>etc.. What's the difference between "the machine on which capture was initiated" or "the machine ... where Wireshark is capturing"?</p><p>mactime is supplied by the NIC, so its meaning, in theory, depends on the NIC and the driver. The NICs and drivers <em>might</em> use the TSFT time stamp, but that timer's absolute value has no significance.</p><p>No, there is no official documentation on either of those topics.</p></div><div id="comment-36386-info" class="comment-info"><span class="comment-age">(16 Sep '14, 18:46)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-36381" class="comment-tools"></div><div class="clear"></div><div id="comment-36381-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

