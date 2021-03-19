+++
type = "question"
title = "print jobs"
description = '''Okay, here is the scenario: 100 users printing to an HP printer, (not through a server). One of the computers keeps sending a corrupt print job and locking up the HP printer. Would WireShark be able to tell us which user is sending the print job to the HP? Maybe by giving us the mac address, or IP o...'''
date = "2015-12-01T16:17:00Z"
lastmod = "2015-12-02T00:39:00Z"
weight = 48168
keywords = [ "print", "job" ]
aliases = [ "/questions/48168" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [print jobs](/questions/48168/print-jobs)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48168-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Okay, here is the scenario: 100 users printing to an HP printer, (not through a server). One of the computers keeps sending a corrupt print job and locking up the HP printer. Would WireShark be able to tell us which user is sending the print job to the HP? Maybe by giving us the mac address, or IP or user name?</p></div><div id="question-tags" class="tags-container tags">print job</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>01 Dec '15, 16:17</strong></p><img src="https://secure.gravatar.com/avatar/9e0c19138af21a3b5b05d93a04e35d3a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Robert%20Merrick&#39;s gravatar image" /><p>Robert Merrick<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Robert Merrick has no accepted answers">0%</span></p></div></div><div id="comments-container-48168" class="comments-container"></div><div id="comment-tools-48168" class="comment-tools"></div><div class="clear"></div><div id="comment-48168-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="48173"></span>

<div id="answer-container-48173" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-48173-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Sure for IP address, possibly for MAC (if the computers are on the same LAN like the printer), maybe for user name (depending on whether the protocol is encrypted). But your part will be to identify in all the streams what exactly is the corrupt job. I assume that you cannot ask all the 100 users to stop using the printer for 20 minutes, but it would be the best way, as then only the corrupt job which I assume is retried automatically, without the user knowing about it, would be sent to the printer.</p><p>As I doubt you could run Wireshark on the printer directly, you'll need to mirror the traffic at the printer port of the switch to another port of that switch and connect the computer running Wireshark to it, or run Wireshark on a computer with two network cards bridged together, inserted between the printer and the switch.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '15, 00:39</strong></p><img src="https://secure.gravatar.com/avatar/00fc6e2633725bd871ff636f0175eabc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sindy&#39;s gravatar image" /><p>sindy<br />
<span class="score" title="6049 reputation points"><span>6.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="51 badges"><span class="bronze">●</span><span class="badgecount">51</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sindy has 110 accepted answers">24%</span></p></div></div><div id="comments-container-48173" class="comments-container"></div><div id="comment-tools-48173" class="comment-tools"></div><div class="clear"></div><div id="comment-48173-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

